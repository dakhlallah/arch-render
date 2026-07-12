#!/usr/bin/env python3
"""
arch-render — turn a sketch / model screenshot into a photorealistic architectural render.

Calls OpenAI GPT Image (gpt-image-2) over the REST API (no SDK).
  - With --image  → /v1/images/edits      (preserves the uploaded design)
  - Without       → /v1/images/generations (text-only, from scratch)

Usage:
  python3 render.py --image sketch.png --prompt "..." [--aspect auto] [--out DIR_OR_FILE]
  python3 render.py --image a.png b.png --prompt "..."      # design first, style refs after
  python3 render.py --prompt "..."                          # text-only, no reference

Aspect:
  --aspect auto (DEFAULT) derives the output size FROM THE INPUT IMAGE, so the original framing
  and crop survive. This is load-bearing: the skill's Preservation Contract forbids re-framing an
  input. Only pass an explicit ratio when the user asks to reframe.

Streaming is ON by default (--no-stream to disable). A quality=high render can take longer than
60s to return, and any network path with a ~60s idle timeout will drop a silent connection before
the first byte arrives. Streaming partial images keeps bytes flowing so the connection stays alive.

API facts (probed 2026-07-11, gpt-image-2):
  - width and height must each be divisible by 16
  - longest edge <= 3840
  - quality: low | medium | high | auto
  - stream + partial_images work on both /generations and /edits (probed 2026-07-12)

Key: $OPENAI_API_KEY. No key is bundled with this skill.
"""

import argparse
import base64
import http.client
import io
import json
import mimetypes
import os
import sys
import time
import urllib.error
import urllib.request
import uuid

EDITS = "https://api.openai.com/v1/images/edits"
GENERATIONS = "https://api.openai.com/v1/images/generations"
DEFAULT_MODEL = "gpt-image-2"
QUALITIES = {"low", "medium", "high", "auto"}
MAX_EDGE_HARD = 3840          # API limit
DEFAULT_MAX_EDGE = 1536       # cost/quality default; raise with --max-edge
RETRY_STATUS = {429, 500, 502, 503, 504}
MAX_ATTEMPTS = 3

RATIOS = {  # explicit reframes only
    "1:1": (1, 1), "16:9": (16, 9), "9:16": (9, 16),
    "4:3": (4, 3), "3:4": (3, 4), "3:2": (3, 2), "2:3": (2, 3),
}


def get_key():
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        sys.exit(
            "ERROR: OPENAI_API_KEY is not set.\n"
            "  export OPENAI_API_KEY=sk-...\n"
            "Get one at https://platform.openai.com/api-keys — no key is bundled with this skill."
        )
    return key


def snap16(n):
    """Round to the nearest multiple of 16, minimum 16."""
    return max(16, int(round(n / 16.0)) * 16)


def input_size(path):
    """(w, h) of an image — Pillow if present, else a minimal PNG/JPEG header parse."""
    try:
        from PIL import Image
        with Image.open(path) as im:
            return im.size
    except ImportError:
        pass
    with open(path, "rb") as f:
        head = f.read(32)
        if head[:8] == b"\x89PNG\r\n\x1a\n":
            import struct
            w, h = struct.unpack(">II", head[16:24])
            return w, h
        f.seek(0)
        data = f.read()
    if data[:2] == b"\xff\xd8":  # JPEG: walk the SOF marker
        i = 2
        while i < len(data) - 9:
            if data[i] != 0xFF:
                i += 1
                continue
            m = data[i + 1]
            if m in (0xC0, 0xC1, 0xC2, 0xC3):
                h = (data[i + 5] << 8) | data[i + 6]
                w = (data[i + 7] << 8) | data[i + 8]
                return w, h
            i += 2 + ((data[i + 2] << 8) | data[i + 3])
    return None


def resolve_size(aspect, image_paths, max_edge):
    """The whole point: 'auto' means KEEP THE INPUT'S FRAMING."""
    if aspect == "auto":
        if not image_paths:
            return f"{snap16(max_edge)}x{snap16(max_edge)}"  # text-only: square default
        size = input_size(image_paths[0])
        if not size:
            print("WARNING: could not read input dimensions — falling back to 1:1. "
                  "Install Pillow (pip3 install Pillow) for reliable aspect preservation.",
                  file=sys.stderr)
            return f"{snap16(max_edge)}x{snap16(max_edge)}"
        w, h = size
    else:
        if aspect not in RATIOS:
            sys.exit(f"ERROR: --aspect must be 'auto' or one of {sorted(RATIOS)}")
        w, h = RATIOS[aspect]

    scale = max_edge / float(max(w, h))
    return f"{snap16(w * scale)}x{snap16(h * scale)}"


def resolve_outfile(out):
    default_dir = os.path.expanduser("~/Downloads/arch-renders")
    out = os.path.expanduser(out) if out else default_dir
    is_dir = out.endswith(os.sep) or os.path.isdir(out) or not os.path.splitext(out)[1]
    if is_dir:
        os.makedirs(out, exist_ok=True)
        return os.path.join(out, f"render-{time.strftime('%Y%m%d-%H%M%S')}.png")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    return out


def multipart(fields, files):
    """Build a multipart/form-data body (no external deps)."""
    boundary = uuid.uuid4().hex
    buf = io.BytesIO()
    for k, v in fields.items():
        buf.write(f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n".encode())
    for k, path in files:
        mime = mimetypes.guess_type(path)[0] or "image/png"
        name = os.path.basename(path)
        buf.write(f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"; "
                  f"filename=\"{name}\"\r\nContent-Type: {mime}\r\n\r\n".encode())
        with open(path, "rb") as f:
            buf.write(f.read())
        buf.write(b"\r\n")
    buf.write(f"--{boundary}--\r\n".encode())
    return buf.getvalue(), f"multipart/form-data; boundary={boundary}"


def read_stream(resp):
    """Consume the SSE stream and return the final image event.

    Streaming is not a nicety: a `quality=high` render can take well over 60s to produce
    a response, and any network path with a ~60s idle timeout (router, ISP, corporate
    proxy) will drop a silent connection before the first byte lands. Partial-image
    events keep bytes flowing, so the connection never goes idle.
    """
    final = None
    for raw in resp:
        line = raw.decode("utf-8", "ignore").strip()
        if not line.startswith("data:"):
            continue
        payload = line[5:].strip()
        if not payload or payload == "[DONE]":
            continue
        try:
            event = json.loads(payload)
        except ValueError:
            continue
        # /generations emits image_generation.*, /edits emits image_edit.* — match on the suffix.
        etype = event.get("type", "")
        if etype.endswith(".partial_image"):
            print(f"  … partial {event.get('partial_image_index', 0) + 1}", file=sys.stderr)
        elif etype.endswith(".completed"):
            final = event
        elif etype == "error":
            msg = (event.get("error") or {}).get("message") or json.dumps(event)[:400]
            sys.exit(f"ERROR: OpenAI streamed an error\n{msg}")
    if not final:
        sys.exit("ERROR: stream ended without a completed image.")
    return {"data": [final]}


def call(url, body, content_type, key, stream=False):
    for attempt in range(1, MAX_ATTEMPTS + 1):
        req = urllib.request.Request(
            url, data=body, method="POST",
            headers={"Authorization": f"Bearer {key}", "Content-Type": content_type},
        )
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                if stream:
                    return read_stream(resp)
                return json.loads(resp.read().decode())
        except (http.client.RemoteDisconnected, ConnectionError) as e:
            # A dropped connection is transient — retry it like any 5xx.
            if attempt < MAX_ATTEMPTS:
                wait = 2 ** attempt
                print(f"connection dropped — retrying in {wait}s ({attempt}/{MAX_ATTEMPTS})",
                      file=sys.stderr)
                time.sleep(wait)
                continue
            sys.exit(
                "ERROR: the network closed the connection before OpenAI responded "
                f"({type(e).__name__}).\n"
                "This usually means the render outran an idle timeout on your network path.\n"
                "HINT: streaming is on by default and avoids this. If you passed --no-stream, "
                "drop it, or retry with --quality medium."
            )
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "ignore")
            if e.code in RETRY_STATUS and attempt < MAX_ATTEMPTS:
                wait = 2 ** attempt
                print(f"HTTP {e.code} — retrying in {wait}s ({attempt}/{MAX_ATTEMPTS})", file=sys.stderr)
                time.sleep(wait)
                continue
            try:
                msg = json.loads(detail)["error"]["message"]
            except Exception:
                msg = detail[:600]
            hint = ""
            if e.code == 429:
                hint = "\nHINT: rate limit or insufficient quota — check billing at platform.openai.com."
            elif e.code == 400 and "safety" in msg.lower():
                hint = "\nHINT: prompt was refused. Simplify it and re-run."
            sys.exit(f"ERROR: OpenAI API HTTP {e.code}\n{msg}{hint}")
        except urllib.error.URLError as e:
            if attempt < MAX_ATTEMPTS:
                time.sleep(2 ** attempt)
                continue
            sys.exit(f"ERROR: network problem calling OpenAI: {e.reason}")


def main():
    ap = argparse.ArgumentParser(description="Architectural render via OpenAI GPT Image")
    ap.add_argument("--image", nargs="*", default=[],
                    help="Input image(s). The DESIGN first; style references after. Omit for text-only.")
    ap.add_argument("--prompt", required=True, help="The architectural render prompt")
    ap.add_argument("--aspect", default="auto",
                    help="'auto' (default) keeps the input's framing. Override ONLY to reframe.")
    ap.add_argument("--quality", default="high", choices=sorted(QUALITIES))
    ap.add_argument("--max-edge", type=int, default=DEFAULT_MAX_EDGE,
                    help=f"Longest edge in px (default {DEFAULT_MAX_EDGE}, max {MAX_EDGE_HARD})")
    ap.add_argument("--out", default="", help="Output dir or file (default ~/Downloads/arch-renders/)")
    ap.add_argument("--model", default=DEFAULT_MODEL, help=f"Model id (default {DEFAULT_MODEL})")
    ap.add_argument("--no-stream", action="store_true",
                    help="Wait for one whole response instead of streaming. A high-quality render "
                         "can then exceed a 60s network idle timeout and be dropped.")
    ap.add_argument("--partial-images", type=int, default=2, choices=[1, 2, 3],
                    help="Partial images to stream (default 2). These keep the connection alive.")
    args = ap.parse_args()

    if not 16 <= args.max_edge <= MAX_EDGE_HARD:
        sys.exit(f"ERROR: --max-edge must be 16..{MAX_EDGE_HARD}")
    for p in args.image:
        if not os.path.isfile(p):
            sys.exit(f"ERROR: input image not found: {p}")

    key = get_key()
    size = resolve_size(args.aspect, args.image, args.max_edge)

    stream = not args.no_stream
    fields = {"model": args.model, "prompt": args.prompt, "size": size, "quality": args.quality}
    if args.image:
        if stream:  # multipart values must be strings
            fields.update(stream="true", partial_images=str(args.partial_images))
        body, ctype = multipart(fields, [("image[]", p) for p in args.image])
        resp = call(EDITS, body, ctype, key, stream=stream)
    else:
        if stream:
            fields.update(stream=True, partial_images=args.partial_images)
        resp = call(GENERATIONS, json.dumps(fields).encode(), "application/json", key, stream=stream)

    data = (resp.get("data") or [{}])[0]
    b64 = data.get("b64_json")
    if not b64:
        sys.exit(f"ERROR: no image returned.\n{json.dumps(resp)[:600]}")

    outfile = resolve_outfile(args.out)
    with open(outfile, "wb") as f:
        f.write(base64.b64decode(b64))
    print(outfile)
    print(f"{size} · quality={args.quality} · {args.model}"
          + (" · aspect preserved from input" if args.aspect == "auto" and args.image else ""),
          file=sys.stderr)


if __name__ == "__main__":
    main()
