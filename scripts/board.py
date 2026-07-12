#!/usr/bin/env python3
"""
arch-render — presentation board / deck builder.

Turns a JSON spec + the user's own images (plans, elevations, sections, renders) into a
SELF-CONTAINED HTML document with a real layout engine. Open it in a browser and print to PDF.

This exists because an image model CANNOT make a presentation board: it hallucinates the plans
and produces illegible pseudo-text. Here, the user's real drawings are PLACED by CSS. Nothing is
invented.

Usage:
  python3 board.py --spec board.json [--out ~/Downloads/arch-renders/<project>/board.html]
  python3 board.py --example            # print a spec template and exit

Then: open the HTML → Cmd/Ctrl-P → "Save as PDF" → set margins to None, backgrounds ON.

Page types:
  cover        title · subtitle · meta · full-bleed image
  text         title · body (paragraphs, or "- " bullets)
  image-full   one image, full page, optional caption
  image-grid   2-6 images in a grid, each with a caption
  drawings     the user's plans/elevations/sections, placed on a light sheet with captions
  materials    material swatches: image + name + finish + application
  summary      title · body · optional "next steps" list
"""

import argparse
import base64
import json
import mimetypes
import os
import sys
from html import escape

PAGE_SIZES = {  # width x height in mm (landscape)
    "A2": (594, 420),
    "A3": (420, 297),
    "A4": (297, 210),
    "16:9": (338, 190),   # ≈ a 16:9 slide, print-friendly
}

EXAMPLE = {
    "project": "Villa Marais",
    "client": "Private client",
    "location": "Kinshasa, RDC",
    "date": "July 2026",
    "format": "A3",
    "accent": "#8a6a4a",
    "pages": [
        {"type": "cover", "title": "Villa Marais",
         "subtitle": "A two-storey residence", "image": "01-hero-exterior-golden.png"},
        {"type": "text", "title": "Design Concept",
         "body": "The house is organised around a shaded courtyard.\n\n- Deep overhangs for tropical rain\n- Cross-ventilation through the plan\n- A single material palette, inside and out"},
        {"type": "drawings", "title": "Floor Plans",
         "images": [{"src": "plan-ground.png", "caption": "Ground floor"},
                    {"src": "plan-first.png", "caption": "First floor"}]},
        {"type": "image-full", "title": "Exterior — Golden Hour",
         "image": "01-hero-exterior-golden.png", "caption": "Approach from the south-west"},
        {"type": "image-grid", "title": "Day / Night",
         "images": [{"src": "01-hero-exterior-golden.png", "caption": "Golden hour"},
                    {"src": "04-hero-exterior-night.png", "caption": "Blue hour"}]},
        {"type": "materials", "title": "Material Palette",
         "items": [{"src": "mat-stucco.jpg", "name": "Lime stucco", "finish": "Matte, hand-applied",
                    "application": "Facade"},
                   {"src": "mat-timber.jpg", "name": "Iroko slats", "finish": "Oiled",
                    "application": "Screens, soffits"}]},
        {"type": "summary", "title": "Summary",
         "body": "The scheme delivers 320 m² across two floors.",
         "next": ["Confirm the material palette", "Approve the plan layout", "Proceed to design development"]},
    ],
}

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
@page{size:%(w)smm %(h)smm;margin:0}
html,body{background:#ststst}
body{font-family:"Helvetica Neue",Inter,Arial,sans-serif;color:#1a1a1a;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:%(w)smm;height:%(h)smm;position:relative;overflow:hidden;background:#fff;
  page-break-after:always;break-after:page;display:flex;flex-direction:column;
  padding:%(pad)smm;margin:0 auto 8mm;box-shadow:0 2px 18px rgba(0,0,0,.13)}
.page:last-child{page-break-after:auto;break-after:auto}
@media print{body{background:#fff}.page{margin:0;box-shadow:none}}

h1{font-size:%(h1)spt;font-weight:600;letter-spacing:-.02em;line-height:1.05}
h2{font-size:%(h2)spt;font-weight:600;letter-spacing:-.01em;margin-bottom:%(gap)smm;
   padding-bottom:2mm;border-bottom:1.5px solid #1a1a1a}
p{font-size:%(body)spt;line-height:1.55;max-width:62ch;margin-bottom:3mm}
li{font-size:%(body)spt;line-height:1.55;margin:0 0 1.5mm 5mm}
.cap{font-size:%(cap)spt;color:#666;margin-top:1.5mm;letter-spacing:.01em}
.meta{font-size:%(cap)spt;color:#666;letter-spacing:.08em;text-transform:uppercase}

/* cover */
.cover{padding:0;justify-content:flex-end}
.cover img{position:absolute;inset:0;width:100%%;height:100%%;object-fit:cover}
.cover .veil{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.05) 40%%,rgba(0,0,0,.72))}
.cover .txt{position:relative;color:#fff;padding:%(pad)smm}
.cover h1{font-size:%(cover)spt;margin-bottom:2mm}
.cover .sub{font-size:%(h2)spt;opacity:.92;margin-bottom:%(gap)smm;font-weight:300}
.cover .meta{color:rgba(255,255,255,.82)}
.rule{width:18mm;height:2.5px;background:%(accent)s;margin-bottom:%(gap)smm}

/* content */
.body{flex:1;min-height:0;display:flex;flex-direction:column}
.full{flex:1;min-height:0;display:flex;flex-direction:column}
.full img{flex:1;min-height:0;width:100%%;object-fit:cover}
.grid{flex:1;min-height:0;display:grid;gap:%(gap)smm}
.grid.n2{grid-template-columns:1fr 1fr}
.grid.n3{grid-template-columns:repeat(3,1fr)}
.grid.n4{grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr}
.grid.n6{grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr}
.cell{display:flex;flex-direction:column;min-height:0}
.cell img{flex:1;min-height:0;width:100%%;object-fit:cover}
/* drawings: contain, never crop a plan */
.dwg .cell img{object-fit:contain;background:#f7f7f5;padding:3mm}
/* materials */
.mats{flex:1;display:grid;grid-template-columns:repeat(auto-fit,minmax(46mm,1fr));gap:%(gap)smm;align-content:start}
.mat img{width:100%%;height:38mm;object-fit:cover;margin-bottom:2mm}
.mat .nm{font-size:%(body)spt;font-weight:600}
.mat .fn{font-size:%(cap)spt;color:#666}
.mat .ap{font-size:%(cap)spt;color:%(accent)s;letter-spacing:.06em;text-transform:uppercase;margin-top:1mm}
.miss{display:flex;align-items:center;justify-content:center;background:#f2f2f0;border:1px dashed #bbb;
  color:#999;font-size:%(cap)spt;flex:1;min-height:24mm;text-align:center;padding:4mm}

.foot{display:flex;justify-content:space-between;align-items:baseline;margin-top:%(gap)smm;
  padding-top:2mm;border-top:1px solid #ddd}
.foot .p{font-size:%(cap)spt;color:#999}
"""


def embed(path, base):
    """Return a data: URI for an image, or None if it's missing."""
    if not path:
        return None
    p = path if os.path.isabs(path) else os.path.join(base, path)
    p = os.path.expanduser(p)
    if not os.path.isfile(p):
        return None
    mime, _ = mimetypes.guess_type(p)
    if not mime or not mime.startswith("image/"):
        mime = "image/png"
    with open(p, "rb") as f:
        return f"data:{mime};base64,{base64.b64encode(f.read()).decode('ascii')}"


def img_tag(src, base, missing_label, cls=""):
    uri = embed(src, base)
    if not uri:
        return f'<div class="miss">missing image:<br>{escape(str(src or missing_label))}</div>'
    return f'<img class="{cls}" src="{uri}" alt="">'


def render_body(text):
    """Paragraphs; lines starting with '- ' become a list."""
    out, bullets = [], []
    for block in (text or "").split("\n"):
        s = block.strip()
        if s.startswith("- "):
            bullets.append(f"<li>{escape(s[2:])}</li>")
            continue
        if bullets:
            out.append("<ul>" + "".join(bullets) + "</ul>")
            bullets = []
        if s:
            out.append(f"<p>{escape(s)}</p>")
    if bullets:
        out.append("<ul>" + "".join(bullets) + "</ul>")
    return "".join(out)


def page_html(pg, spec, base, n, total):
    t = pg.get("type", "text")
    title = escape(pg.get("title", ""))
    foot = (f'<div class="foot"><span class="p">{escape(spec.get("project",""))}</span>'
            f'<span class="p">{n} / {total}</span></div>')

    if t == "cover":
        meta = " · ".join(escape(str(spec.get(k))) for k in ("client", "location", "date") if spec.get(k))
        return (f'<section class="page cover">{img_tag(pg.get("image"), base, "cover")}'
                f'<div class="veil"></div><div class="txt"><div class="rule"></div>'
                f'<h1>{title}</h1><div class="sub">{escape(pg.get("subtitle",""))}</div>'
                f'<div class="meta">{meta}</div></div></section>')

    if t == "image-full":
        cap = f'<div class="cap">{escape(pg["caption"])}</div>' if pg.get("caption") else ""
        return (f'<section class="page"><h2>{title}</h2><div class="full">'
                f'{img_tag(pg.get("image"), base, "image")}{cap}</div>{foot}</section>')

    if t in ("image-grid", "drawings"):
        imgs = pg.get("images", [])[:6]
        n_cls = {1: "n2", 2: "n2", 3: "n3", 4: "n4", 5: "n6", 6: "n6"}.get(len(imgs), "n2")
        dwg = " dwg" if t == "drawings" else ""
        cells = "".join(
            f'<div class="cell">{img_tag(i.get("src"), base, "image")}'
            f'<div class="cap">{escape(i.get("caption",""))}</div></div>' for i in imgs)
        return (f'<section class="page{dwg}"><h2>{title}</h2>'
                f'<div class="grid {n_cls}">{cells}</div>{foot}</section>')

    if t == "materials":
        cells = "".join(
            f'<div class="mat">{img_tag(i.get("src"), base, "swatch")}'
            f'<div class="nm">{escape(i.get("name",""))}</div>'
            f'<div class="fn">{escape(i.get("finish",""))}</div>'
            f'<div class="ap">{escape(i.get("application",""))}</div></div>'
            for i in pg.get("items", []))
        return (f'<section class="page"><h2>{title}</h2><div class="mats">{cells}</div>{foot}</section>')

    if t == "summary":
        nxt = pg.get("next") or []
        nxt_html = ("<h2 style='margin-top:8mm'>Next steps</h2><ul>" +
                    "".join(f"<li>{escape(s)}</li>" for s in nxt) + "</ul>") if nxt else ""
        return (f'<section class="page"><h2>{title}</h2><div class="body">'
                f'{render_body(pg.get("body",""))}{nxt_html}</div>{foot}</section>')

    # default: text
    return (f'<section class="page"><h2>{title}</h2><div class="body">'
            f'{render_body(pg.get("body",""))}</div>{foot}</section>')


def build(spec, base):
    fmt = spec.get("format", "A3")
    if fmt not in PAGE_SIZES:
        sys.exit(f"ERROR: format must be one of {sorted(PAGE_SIZES)}")
    w, h = PAGE_SIZES[fmt]
    scale = w / 420.0  # type scales off A3
    css = CSS % {
        "w": w, "h": h,
        "pad": round(14 * scale, 1), "gap": round(6 * scale, 1),
        "cover": round(44 * scale), "h1": round(30 * scale), "h2": round(15 * scale),
        "body": round(9.5 * scale, 1), "cap": round(7.5 * scale, 1),
        "accent": spec.get("accent", "#8a6a4a"),
    }
    css = css.replace("#ststst", "#e9e9e7")
    pages = spec.get("pages", [])
    if not pages:
        sys.exit("ERROR: spec has no pages")
    body = "\n".join(page_html(p, spec, base, i + 1, len(pages)) for i, p in enumerate(pages))
    title = escape(spec.get("project", "Presentation"))
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>'
            f'<style>{css}</style></head><body>{body}</body></html>')


def main():
    ap = argparse.ArgumentParser(description="Build a presentation board / deck as self-contained HTML")
    ap.add_argument("--spec", help="JSON spec file")
    ap.add_argument("--out", default="", help="Output .html (default: alongside the spec)")
    ap.add_argument("--example", action="store_true", help="Print an example spec and exit")
    args = ap.parse_args()

    if args.example:
        print(json.dumps(EXAMPLE, indent=2))
        return
    if not args.spec:
        sys.exit("ERROR: --spec is required (or use --example)")

    spec_path = os.path.expanduser(args.spec)
    if not os.path.isfile(spec_path):
        sys.exit(f"ERROR: spec not found: {spec_path}")
    with open(spec_path) as f:
        try:
            spec = json.load(f)
        except json.JSONDecodeError as e:
            sys.exit(f"ERROR: spec is not valid JSON — {e}")

    base = os.path.dirname(os.path.abspath(spec_path))  # image paths resolve relative to the spec
    html = build(spec, base)

    out = os.path.expanduser(args.out) if args.out else os.path.join(base, "board.html")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w") as f:
        f.write(html)

    missing = html.count('class="miss"')
    print(out)
    if missing:
        print(f"WARNING: {missing} image(s) missing — placeholders shown. Fix the paths and re-run.",
              file=sys.stderr)
    print(f"{len(spec.get('pages', []))} page(s), {spec.get('format', 'A3')}. "
          f"Open in a browser → Print → Save as PDF (margins: None, background graphics: ON).",
          file=sys.stderr)


if __name__ == "__main__":
    main()
