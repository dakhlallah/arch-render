# 89 · Magnific Production Studio — input → coordinated client package

> The **full-project mode**: one architectural input becomes an analyzed, costed, approved, consistently
> rendered, board-laid-out, client-ready proposal. Extends **§87** (client presentation package) and
> **§80** (visual consistency) with the Magnific pipeline (**§88**) as the production engine.
> **Preservation Contract applies** (`SKILL.md` §2) — and §89.1 is the reason this section exists.

---

## 89.1 · THE GATE — what the input can and cannot tell you

**This is the first thing you do, before any proposal, and it is not optional.**

A single image contains **one view of one building**. It does not contain the other three sides, the
roof, the interior, the plan, or the site. Any tool that appears to produce those is **generating them
from nothing**.

**The three tools that will fool you:**

| Tool | What it looks like | What it actually does |
|---|---|---|
| `images_change_camera` (`rotate` 0–360°, `vertical` −30…90°) | "rear facade view", "aerial view" | **Invents** every surface the camera didn't see. Rotate 180° on a front shot and the model *makes up* a back elevation — your stair core, service door and window rhythm are fiction. |
| `images_variations` (`variationMode: "angles"`) | "9 coordinated views" | Nine **invented** angles. A 3×3 grid of buildings that aren't the user's. |
| `images_generate` + `references[]` | "same building, new view" | Style/subject-conditioned, **not geometry-locked**. It reinterprets. |

**Therefore: NEVER use these to produce a view the input doesn't contain.** Not for a client. Not "just
to show the idea". A plausible fake rear facade is worse than no rear facade, because the client believes
it.

**Sort every proposed deliverable into one of three tiers, and show the user the tiers.**

| Tier | Meaning | Examples | Rule |
|---|---|---|---|
| **A · DERIVABLE** | Fully contained in the input. Architecture provably preserved. | Enhance / upscale the given view · relight it (day → golden → blue → night) · weather & season · material & colour palettes on the visible surfaces · detail crops of what's visible · moodboards · material boards · captions & text | **Produce freely** (after the cost gate). |
| **B · NEEDS SOURCE** | Real architecture that exists — in the user's model, drawings or camera — but **not in this image**. | Rear / side facades · aerial · other elevations · sections · floor plans · site plan · interiors & room views · massing & zoning diagrams · entrance view (if not in frame) | **Ask for the source.** One screenshot per view from their SketchUp/Revit/Rhino model, or their PDF/DWG drawings. **Each becomes its own source of truth**, then Tier A applies to it. |
| **C · INVENTION** | Nothing in reality corresponds to it. | Any Tier-B item produced **without** the source · "what the interior might look like" from an exterior photo · a generated floor plan | **Default: refuse.** Only on the user's explicit, informed request — and then it is **labelled "concept illustration — not the built design"** on the board and in the caption, and it never enters a drawing page. |

**Say the gate out loud, in one short paragraph, in the proposal.** For example:

> *From this one street-level photo I can give you the hero, all five lighting states, three material
> palettes and the detail crops — the geometry is provably yours in every one. I **cannot** see the rear
> facade, the roof, or any interior; if I generate those, I'm inventing your building. Send me a
> screenshot per view from your model (or the drawings) and each becomes a real render.*

This single paragraph is what makes the package honest — and it's usually a 30-second ask for the user,
because they already have the model open.

---

## 89.2 · Step 1 — Automatic project analysis (silent)

Run the **§85** structured read (`auto-analysis.md`), extended for a full project:

Project type & building use · interior / exterior / landscape / urban · style & design concept (the parti,
one line) · geometry & spatial organization · visible materials & finishes · lighting & time of day ·
camera, perspective, lens, crop, aspect ratio · image quality & what limits it · **and the asset gap** —
which of the pages a real client deck needs are **not** in what they sent.

**The asset gap is the point.** It's what produces the Tier-B list in §89.1, and it's the difference
between "here's a render" and "here's what your proposal is missing".

Read the confidence honestly: material at **read / estimate / unknown** (§47). Never promote an estimate
into a spec.

---

## 89.3 · Step 2 — The proposal (ONE approval, not twenty)

**Free. No API calls. Produce it before touching a paid tool.** The user approves the whole thing with
one answer — never make them request each image.

```
PROJECT          <name>  ·  <type>  ·  <style>  ·  source: <what they sent>

TIER A — from your image (architecture provably preserved)
  A1  Hero render (enhanced + upscaled 4x)          1 image
  A2  Lighting set: day · golden · blue · night     4 images
  A3  Material palettes: warm · neutral · minimal   3 images
  A4  Detail crops: entrance · facade junction      2 images
                                                    ─────────
                                                    10 images

TIER B — needs one screenshot each from your model
  B1  Rear facade · B2  Corner perspective · B3  Aerial
  B4  Interior: living · B5  Interior: kitchen
  (send the views → each becomes a real render; without them I'd be inventing them)

DELIVERABLES     10 renders (4x, print-ready) · material board · moodboard ·
                 14-page client PDF (structure below) · captions & page text ·
                 Magnific settings sheet · named project folder

COST             ~<N> credits  (priced with simulate_cost, per stage)
TIME             <n> stages

Approve, or trim it — one answer is enough.
```

**Rules for the proposal:**
- **Never propose a Tier-C image.** It doesn't go on the menu; it goes in the paragraph explaining why.
- **Scale the page count to the project.** 10 pages for a villa, 40 for a mixed-use scheme. Never pad.
- **Price it before you propose it** — `simulate_cost` on the biggest stage, extrapolate, quote a range.
- **Cost gate (`SKILL.md` §2):** this is many paid calls. The approval *is* the gate. No approval, no run.

---

## 89.4 · Step 3 — Lock the Project Identity (before the first render)

**§80** applies with full force. Write it down once, reuse it verbatim in **every** prompt:

```
PROJECT IDENTITY  <name>
  Architecture     locked from <source image> — never restated as a request
  Materials        <exact palette: board-formed concrete · oxidised bronze · low-iron glass · travertine>
  Landscape        <species + language: olive, rosemary, gravel — Mediterranean, drought-tolerant>
  Furniture        <one collection, named>
  People/vehicles  <styling + density: sparse, muted, one dark estate car>
  Sun              <azimuth + elevation — PHYSICALLY CONSISTENT across every view>
  Grade            <colour grade: warm neutral, low contrast, film-like>
  Realism          <one level, all views>
```

**Sun direction is the tell.** If the hero has the sun from the west and the corner view has it from the
east, the set falls apart and a client will feel it without knowing why. Fix the azimuth in the identity
and honour it in every prompt and every relight.

---

## 89.5 · Step 4 — Prompts: one per view, never one for all

**Write a separate prompt for every image.** A generic prompt reused across ten views produces ten
buildings. Each prompt carries the **shared identity block** (§89.4, verbatim) plus **what is specific to
that view**:

```
Subject:        <exact architectural subject of THIS view>
Locked:         geometry · openings · massing · camera · perspective · crop · design intent
Allowed:        <only what this image changes>
Materials:      <from the identity — same words every time>
Lighting:       <this view's light — consistent with the identity's sun>
Environment:    <context, ground plane, sky>
Landscaping:    <from the identity>
Furniture:      <from the identity>
Camera & lens:  <this view's camera — matched to the source>
Mood:           <this view's mood>
Avoid:          <§23, trimmed>
```

**For Magnific `images_upscale`, collapse this to one short factual line** — the upscaler's `prompt` is a
nudge, not a brief (§88.2). The full block above governs the `render.py` stage; the Magnific stage gets
the one-liner naming real materials and real light.

---

## 89.6 · Step 5 — Material & colour proposals

Coordinated alternatives, **applied to the visible surfaces only**, geometry untouched:

Original enhanced · warm natural · neutral contemporary · luxury · minimal · **sustainable** (low-carbon:
timber, lime render, reclaimed brick — and say *why* it's lower carbon, per §99) · light and dark variants.

**Change only the selected surfaces.** If they pick "warm natural" for the facade, the frames, glass,
roof and ground plane stay exactly as they were unless the palette explicitly names them. Silently
re-skinning an unmentioned surface is a Preservation Contract breach — it's the §24 "no material silently
swapped" check.

Each palette is a `render.py` pass (it changes materials) → then a Magnific finish (§88). Not the reverse.

---

## 89.7 · Step 6 — The production pipeline, per image

**Order matters. Magnific is the finisher, never the first step (§88.1).**

1. **Compose / transform** — `render.py` (GPT Image, image-conditioned: holds geometry, camera and crop).
   This is where materials, lighting, time of day, weather and context change.
2. **Check fidelity** — `Read` the output. Count window bays. Compare to the source. Fail → **re-run**
   (§83), don't patch.
3. **Relight, if the ask is a light *direction* move** — `images_relight` (1–4 lights, azimuth/elevation/
   intensity, gel colour). **Not** for day→night; that's step 1.
4. **Finish & upscale** — `images_upscale` (§88.3 table). Arch-safe: `creativity ≤ +2`, `resemblance ≥ +4`,
   or **precision mode**. `scale` from the delivery: screen 2x · A3 4x · large-format 8x+.
5. **Final consistency check** — against the Project Identity **and the other images in the set**, not
   just against the source.
6. **Name and file it** (§89.8).

**Low creativity, high resemblance whenever an existing design is being preserved — which is almost
always.** Raise `creativity` **only** when the user has explicitly asked for a new concept or a redesign,
and say that you're doing it.

---

## 89.8 · Naming & project organization

Create a real project on Magnific: `folders_create({name: "<PROJECT>"})`, then pass its
`folderReference` on **every** generation call so the whole package lands in one place.

**File naming — one system, used everywhere** (renders, board images, captions, the settings sheet):

```
<PROJECT>_<VIEW>_<VARIANT>_<STAGE>_v<N>.png

VILLA-KANGA_hero_neutral_final-4x_v2.png
VILLA-KANGA_facade-front_warm_render_v1.png
VILLA-KANGA_interior-living_neutral_final-4x_v1.png
```

`STAGE` ∈ `render` · `relight` · `final-2x/4x/8x`. The user must be able to hand the folder to a printer
without renaming a thing.

---

## 89.9 · Step 7 — The client presentation

**The board is LAID OUT, never generated** (`SKILL.md` §2 and §4b). `scripts/board.py` places real images
with a real layout engine → self-contained HTML → **browser Print → Save as PDF** (margins None,
background graphics ON). **Magnific has no PDF export — this is the path.**

**Page count follows the project: 10 · 20 · 30 · 40+.** Only pages you can actually fill.

| Page group | Source | If the source is missing |
|---|---|---|
| Cover · title · summary · brief · vision · concept | **You write it** (professional text, §89.10) | — |
| Site context · site analysis · location map | User's site plan / a real map | **Omit the page.** Never generate a fake map or site plan. |
| Massing · zoning · circulation diagrams | User's model / drawings | Omit, or offer to draw them **from their plan** if they send it |
| **Floor plans · elevations · sections** | **The user's real drawings — full stop** | **Omit the page and say so.** An image model producing a "floor plan" is the single worst thing this skill can do (`SKILL.md` §2). |
| Material palette · colour palette · moodboard | Tier A — produce | — |
| Landscape concept · lighting concept | Tier A (text + renders) | — |
| Exterior hero · additional exteriors | Tier A / Tier B | Tier B without source → **omit**, don't invent |
| Interiors · room-by-room | Tier B | Omit until they send interior views |
| Day/night comparison · material alternatives | Tier A — produce | — |
| Details · selected proposal · summary · closing | Produce / write | — |

**A missing drawing means a missing page, and you say which page is missing and why.** That sentence is
what a real architect says to a client. A fabricated plan is what loses the commission.

---

## 89.10 · Presentation text

**Write real text. Never filler.** Every page gets prose a principal would actually read aloud: what this
page shows, why the design does it, what the client gets from it. Ground every claim in what's visible in
the image or stated by the user. No "Lorem ipsum", no "This stunning architectural masterpiece
seamlessly blends form and function."

Captions: one line, factual — *"West facade, 17:40 — board-formed concrete with oxidised bronze reveals;
the deep reveal shades the glazing through the afternoon."* Not *"A breathtaking vision of modern
living."*

If you don't know the client's brief, **ask for it once** in the proposal, or write the summary from what
the drawing tells you and mark the assumptions.

---

## 89.11 · Final deliverables checklist

☐ High-res renders, named (§89.8), in one Magnific project folder
☐ The prompt used for each image · the Magnific settings used for each image (the settings sheet)
☐ Material board · colour board · moodboard
☐ Diagrams **only where a real source existed**
☐ Board HTML → **PDF via browser print** · every page's text and captions written
☐ **The Tier-B gap list** — what's missing, what to send, what it would unlock

---

## 89.12 · Quality control — before delivery

Run **§24** on every image, then this set on the **package**:

☐ No geometry changed unintentionally — **count the window bays against the source**
☐ Doors, windows, openings correctly positioned
☐ Floor levels and roof form consistent **across every view**
☐ Materials identical across views (same words → same surfaces)
☐ **Sun direction physically consistent across the whole set** (§89.4)
☐ People, furniture, vegetation, vehicles correctly scaled and from one styling
☐ Texture scale and alignment real (§47.2)
☐ No duplicated or malformed objects
☐ **Every image is unmistakably the same building**
☐ Every page has a purpose — no page exists to pad the count
☐ **Nothing in the package is Tier-C without being labelled as such**
☐ The package could be put in front of a real client tomorrow

**The last check is the one that matters.** The objective is not an image. It's a coordinated,
honest, client-ready proposal — where every architectural claim in it is one the user's own design
actually makes.
