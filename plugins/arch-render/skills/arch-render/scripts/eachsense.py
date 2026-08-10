#!/usr/bin/env python3
"""Run a bounded each::sense architectural image job through EachLabs.

Use only after explicit authorization for the named paid attempt. Public HTTPS inputs only; for local
design references and crop fidelity, prefer render.py. No credentials are bundled.
"""

import argparse
import base64
import binascii
import ipaddress
import json
import os
import re
import socket
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid

ENDPOINT = "https://eachsense-agent.core.eachlabs.run/v1/chat/completions"
MODEL = "eachsense/beta"
IMAGE_URL = re.compile(r'https?://[^\s"\'<>]+\.(?:png|jpe?g|webp)(?:\?[^\s"\'<>]*)?', re.I)
DATA_URI = re.compile(r'data:image/[a-zA-Z.+-]+;base64,[A-Za-z0-9+/=]+')
MAX_OUTPUT_BYTES = 25 * 1024 * 1024
ALLOWED_OUTPUT_TYPES = {"image/png", "image/jpeg", "image/webp"}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def allowed_result_hosts():
    return {host.strip().lower() for host in os.environ.get(
        "EACHSENSE_RESULT_HOSTS", ""
    ).split(",") if host.strip()}


def validate_result_url(value):
    parsed = urllib.parse.urlsplit(value)
    host = (parsed.hostname or "").lower()
    if parsed.scheme != "https" or not host:
        sys.exit("ERROR: result URL must use HTTPS and include a hostname")
    allowlist = allowed_result_hosts()
    if not allowlist or host not in allowlist:
        sys.exit(
            "ERROR: provider returned an unapproved asset host. Set EACHSENSE_RESULT_HOSTS "
            "to the provider-documented comma-separated host allowlist before downloading."
        )
    try:
        addresses = {item[4][0] for item in socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM)}
    except socket.gaierror as error:
        sys.exit(f"ERROR: cannot resolve approved asset host: {error}")
    for address in addresses:
        ip = ipaddress.ip_address(address)
        if not ip.is_global:
            sys.exit("ERROR: result URL resolved to a non-public address; download refused")
    return value


def download_result(value, target):
    request = urllib.request.Request(validate_result_url(value), headers={"Accept": "image/*"})
    opener = urllib.request.build_opener(NoRedirect)
    try:
        with opener.open(request, timeout=120) as response, open(target, "wb") as handle:
            content_type = response.headers.get_content_type().lower()
            if content_type not in ALLOWED_OUTPUT_TYPES:
                sys.exit(f"ERROR: unsupported result Content-Type: {content_type}")
            declared = response.headers.get("Content-Length")
            if declared and int(declared) > MAX_OUTPUT_BYTES:
                sys.exit("ERROR: result exceeds the 25 MB output limit")
            total = 0
            while True:
                chunk = response.read(64 * 1024)
                if not chunk:
                    break
                total += len(chunk)
                if total > MAX_OUTPUT_BYTES:
                    sys.exit("ERROR: result exceeded the 25 MB output limit")
                handle.write(chunk)
    except urllib.error.HTTPError as error:
        if 300 <= error.code < 400:
            sys.exit("ERROR: result URL redirected; redirects are refused unless revalidated")
        raise


def key():
    value = os.environ.get("EACHLABS_API_KEY", "").strip()
    if not value:
        sys.exit("ERROR: EACHLABS_API_KEY is not set; no key is bundled with this skill")
    return value


def output_path(value, extension="png"):
    target = os.path.expanduser(value or "~/Downloads/arch-renders")
    if os.path.splitext(target)[1]:
        os.makedirs(os.path.dirname(target) or ".", exist_ok=True)
        if os.path.exists(target):
            sys.exit("ERROR: output exists; choose another path")
        return target
    os.makedirs(target, exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    return os.path.join(target, f"eachsense-{stamp}-{uuid.uuid4().hex[:6]}.{extension}")


def scan(value, urls, data_uris):
    if isinstance(value, str):
        urls.extend(IMAGE_URL.findall(value))
        data_uris.extend(DATA_URI.findall(value))
    elif isinstance(value, list):
        for item in value:
            scan(item, urls, data_uris)
    elif isinstance(value, dict):
        for name, item in value.items():
            if name == "b64_json" and isinstance(item, str):
                data_uris.append("data:image/png;base64," + item)
            else:
                scan(item, urls, data_uris)


def execute(body, api_key, timeout):
    request = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(body).encode(),
        method="POST",
        headers={"Content-Type": "application/json", "Accept": "text/event-stream",
                 "X-API-Key": api_key},
    )
    try:
        text, urls, data_uris = [], [], []
        with urllib.request.urlopen(request, timeout=timeout) as response:
            for raw in response:
                line = raw.decode("utf-8", "ignore").strip()
                if not line.startswith("data:"):
                    continue
                payload = line[5:].strip()
                if not payload or payload == "[DONE]":
                    continue
                try:
                    event = json.loads(payload)
                except ValueError:
                    scan(payload, urls, data_uris)
                    continue
                scan(event, urls, data_uris)
                try:
                    delta = event["choices"][0].get("delta", {}).get("content")
                    if isinstance(delta, str):
                        text.append(delta)
                except (KeyError, IndexError, TypeError, AttributeError):
                    pass
        return "".join(text), urls, data_uris
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", "ignore")[:800]
        suffix = ""
        if error.code == 429 or error.code >= 500:
            suffix = ("\nNo automatic retry was made. Check provider history before authorizing "
                      "another paid attempt.")
        sys.exit(f"ERROR: each::sense HTTP {error.code}\n{detail}{suffix}")
    except urllib.error.URLError as error:
        sys.exit(
            "ERROR: each::sense generation status is unknown; no automatic retry was made to "
            f"avoid a duplicate charge. Network detail: {error.reason}"
        )


def main():
    parser = argparse.ArgumentParser(description="Architectural render via each::sense")
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--image-url", action="append", default=[])
    parser.add_argument("--mode", choices=("eco", "max"), default="max")
    parser.add_argument("--session", default="")
    parser.add_argument("--model", default=MODEL)
    parser.add_argument("--out", default="")
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--dry-run", action="store_true",
                        help="Validate and print the request without spending credits")
    args = parser.parse_args()

    for url in args.image_url:
        if not url.startswith("https://"):
            sys.exit("ERROR: --image-url must be public HTTPS; use render.py for local files")

    body = {"messages": [{"role": "user", "content": args.prompt}], "model": args.model,
            "stream": True, "mode": args.mode}
    if args.session:
        body["session_id"] = args.session
    if args.image_url:
        body["image_urls"] = args.image_url

    if args.dry_run:
        print(json.dumps({"provider": "eachlabs", "endpoint": ENDPOINT, "mode": args.mode,
                          "model": args.model, "input_count": len(args.image_url),
                          "paid_attempts": 0}, indent=2))
        return

    text, urls, data_uris = execute(body, key(), args.timeout)
    if data_uris:
        match = re.match(r"data:image/([a-zA-Z.+-]+);base64,(.*)", data_uris[0], re.S)
        extension = match.group(1).split("+")[0].replace("jpeg", "jpg")
        target = output_path(args.out, extension)
        try:
            decoded = base64.b64decode(match.group(2), validate=True)
        except (ValueError, binascii.Error) as error:
            sys.exit(f"ERROR: invalid base64 image payload: {error}")
        if len(decoded) > MAX_OUTPUT_BYTES:
            sys.exit("ERROR: returned image exceeds the 25 MB output limit")
        with open(target, "wb") as handle:
            handle.write(decoded)
    elif urls:
        extension = os.path.splitext(urls[0].split("?")[0])[1].lstrip(".") or "png"
        target = output_path(args.out, extension)
        download_result(urls[0], target)
    else:
        sys.exit("ERROR: no image returned\n" + (text.strip()[:1000] or "(empty response)"))
    print(target)
    print(f"mode={args.mode} · {args.model}", file=sys.stderr)


if __name__ == "__main__":
    main()
