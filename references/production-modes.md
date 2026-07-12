# Production Modes — consistency, style references, delivery

> **Preservation Contract applies** (see `SKILL.md` §2). These modes govern *how a job is run across
> multiple outputs* — they never loosen the geometry/camera lock.

---

# 80 · Visual Consistency Engine (multi-render sets)

The moment a project produces **more than one image** — a variation set, a day/night pair, a board, a
carousel, an interior + exterior pair, a before/after — every image must read as **the same building,
shot by the same photographer, on the same project**.

**Lock a Project Identity before the first render**, then reuse it verbatim in every subsequent prompt
of that project. Write it down in the reply once, and don't re-derive it per image (re-deriving is how
sets drift):

```
PROJECT IDENTITY (reuse verbatim across every render in this set)
Materials & finishes:
Colour palette:
Lighting mood:
Architectural language:
Landscape style:
Furniture style:
Camera language:      (lens, height, framing habits)
Atmosphere:
Colour grade:
Render quality tail:
```

**Only the axis the user asked to vary may change** between images in a set (time of day, season,
material, angle). Everything else in the Identity block stays byte-for-byte identical. If a variation
axis *forces* a change (a night render obviously changes the lighting mood), change **only** that field
and keep the rest.

**Drift check before delivering a set** — the same building? the same palette? the same landscape
species and density? the same grade? If image 3 has different trees or a warmer grade than image 1
for no requested reason, **it's a defect** — re-run it, don't ship it.

**Across sessions:** if the user returns later with "add a night one to the set I made yesterday",
ask for (or read) the earlier render and rebuild the Identity block from it before generating.

---

# 81 · Style Reference Matching (their design, someone else's look)

When the user supplies reference images **for visual inspiration only** — an ArchDaily shot, a
competitor's render, a photographer's work, a moodboard — alongside their own design.

**This is two different roles for two different images. Never confuse them:**

| Image | Role | What you take from it |
|---|---|---|
| The user's design (sketch/model/render/plan) | **The architecture** | Geometry, massing, openings, camera, composition — **locked** |
| The reference image(s) | **The look only** | Lighting · material *language* · composition habits · camera behaviour · colour grade · mood · atmosphere · render quality · vegetation style · interior styling |

**Never copy the architecture from a reference.** Not its massing, not its facade, not its windows, not
its plan, not its building. Take the *artistic language*, apply it to the user's own design. Copying a
reference building is plagiarism and it destroys the user's project.

**Workflow:**
1. **Name what you're extracting**, out loud, before rendering — so the user can correct you:
   > *"From your reference I'm taking: blue-hour grade, warm interior spill, wet-paving reflections,
   > low 35mm street-level camera, sparse birch planting. I'm taking **nothing** from its architecture."*
2. Build the prompt: **user's geometry** (preserve/enhance clause) **+ extracted look** (as style language).
3. Pass both images to the renderer — the design first, references after:
   ```bash
   python3 scripts/render.py --image design.png ref1.jpg ref2.jpg --prompt "<...>" --aspect auto
   ```
   Say explicitly in the prompt which is which:
   > "The FIRST image is the building to render — keep its exact geometry, openings and camera.
   > The FOLLOWING images are STYLE REFERENCES ONLY — copy their lighting, mood, colour grade and
   > landscaping language. **Do not copy any architecture, massing or facade from them.**"
4. `--aspect auto` still applies — the **user's** design sets the framing, never the reference.

**If the reference and the design fight** (a brutalist reference over a Mediterranean villa), say so in
one line and ask which wins, rather than producing a confused hybrid.

---

# 82 · Delivery & marketing sets

Marketing/presentation outputs are **§41** (`ref-presentation.md`) — hero images, brochure visuals,
competition and presentation boards, website heroes, social/Instagram carousels, LinkedIn visuals,
teasers, billboards. Nothing new is needed here; two rules govern the *set*:

- **§80 Visual Consistency applies to every asset in a campaign** — a carousel whose slides don't match
  is worse than one good image.
- **Cost gate:** state the number of render calls and wait for a yes before generating a multi-asset set
  (`SKILL.md` §4).

---

# 83 · Output rejection & re-run

**Look at what came back before you hand it over.** `Read` the output PNG and check it against §24.

**Reject and re-run** (do not deliver, do not apologise-and-ship) if the render shows:
- warped, melted or bent geometry · a changed floor/window count · a moved or rotated camera
- a changed crop or aspect ratio · duplicated or floating objects
- plastic/fake materials · obvious AI artifacts · deformed people or vehicles
- landscaping or a grade that breaks the set's Project Identity (§80)

**Re-run protocol:** simplify the prompt (over-long prompts are the usual cause), re-state the lock
clause harder, re-run **once**. If the second attempt also fails, **stop, show the user what went wrong,
and say so plainly** — don't burn API calls in a loop, and don't ship a broken render with a caveat.

Never claim an output is publication-ready if you can see that it isn't.

---

# 87 · Client Presentation Package (plan → approve → produce)

**The goal is a client-ready package, not a single render.** Fires when the user wants a presentation,
proposal, pitch, board set, marketing set, "the full thing" — or picks **24** from the §86 menu.

> ⚠️ **Never fire this unasked.** "Render it at night" gets a night render, not a 15-image pitch deck.
> Presentation intent, or the menu. Otherwise §85 / §86 own the upload.

## What this mode can and cannot produce — read before proposing anything

The skill has **two output primitives: a rendered image, and text.** The document is a **layout**
(`scripts/board.py`, `SKILL.md` §4b) — it *places* content, it does not invent it.

| Deliverable | Can it actually be made? |
|---|---|
| Rendered images (hero, night, detail, variants) | **Yes** — `render.py`, one paid call each |
| Narrative, project info, concept, summary text | **Yes** — it's text |
| Cover, text, render, material and summary **pages** | **Yes** — `board.py` lays them out |
| Plan / elevation / section **pages** | **Yes — but only from the user's own drawings.** `board.py` places their file. |
| Plans/elevations/sections the user **hasn't sent** | **NO. Not ever.** No page, no substitute, no render of one. |
| A board or deck "rendered" by the image model | **NO.** Pseudo-text and a hallucinated plan. **Banned** (`SKILL.md` §2). |

**The failure this prevents:** a page headed *Floor Plans* containing a plausible, invented, wrong plan,
shown to a paying client. That is the worst thing this skill could do. If the drawings aren't there, the
page isn't there — **say so and offer what you can fill.**

## Step 1 · Propose the plan. Render NOTHING yet.

Read the project (§85), then put a **concise, editable plan** on the table. This is the whole point of
the mode — the user approves, trims or adds **before** a single paid call.

```
PRODUCTION PLAN — <Project name>
Read:        <type · style · storeys · context · source (D5 / plan / photo)>
Identity:    <materials · palette · lighting mood · camera language>   ← §80, locked across all outputs

RENDERS                                        view              lighting        calls
  01  Hero exterior                            3/4 eye-level     golden hour       1
  02  Street-level approach                    35mm pedestrian   day               1
  03  Aerial / context                         drone 3/4         day               1
  04  Hero exterior — night                    same as 01        blue hour         1
  05  Interior — main living space             24mm eye height   natural day       1
  06  Detail — facade / material close-up      85mm              raking light      1
OPTIONS
  07  Material variant B (<stone> → <timber>)  same as 01        golden hour       1
  08  Landscape variant (lush / minimal)       same as 02        day               1
GRAPHICS (no render calls)
  09  Moodboard                    §26
  10  Material board               §33 / §46
  11  FF&E board                   §49
  12  Presentation boards (A2 ×2)  §34 / §67
  13  Design narrative + client slides  §62 / §58

ESTIMATED RENDER CALLS: 8      (graphics are free — text/layout only)
```

## Step 1b · Propose the DOCUMENT — a paginated presentation

The plan above lists *assets*. The client sees a *document*. Propose its **page structure** too, with a
**page count that flexes with the project's scope** — a villa is not a masterplan:

| Scope | Typical | |
|---|---|---|
| Small (villa, apartment, interior, café) | **8–12 pages** | |
| Medium (tower, hotel, school, mixed-use block) | **14–20 pages** | |
| Large (masterplan, campus, competition) | **24–40 pages** | boards may replace slides |

**The page menu — pick what the project actually needs, in this order:**

```
PRESENTATION — <Project>            <N> pages          paid renders: <n>
  01  Cover                          hero image + project name + client + date        [render 01]
  02  Project information            client · location · site area · GFA · programme · status
  03  Design concept                 the parti in one diagram + a short narrative      §62
  04  Site analysis                  context · access · orientation · sun · views      §07 / §52
  05  Masterplan / site plan         (if relevant)
  06  Floor plans                    YOUR drawing file, placed by board.py             — free ‡
  07  Elevations                     YOUR drawing file, placed by board.py             — free ‡
  08  Sections                       YOUR drawing file, placed by board.py             — free ‡
  09  Material options               palette A / B, with samples                       §33 / §46
  10  Moodboard                      atmosphere and design language                    §26
  11  Exterior render — day          hero                                              [render]
  12  Exterior render — night        same camera, blue hour                            [render]
  13  Interior render                main space                                        [render]
  14  Summary                        what's proposed · next steps · what you need back
```

**Rules that keep it honest:**
- **Most pages are free.** Plans, elevations, sections, info, concept and summary are *the user's own
  drawings and text laid onto pages* — zero API calls. **Only render pages are paid.** Show that split
  in the header (`14 pages · 4 paid renders`) so the cost is legible at a glance.
- **Only include a page the project can actually fill.** If they've sent one clay model and no drawings,
  you have no plans, elevations or sections — **say so and offer the pages you can fill**, rather than
  proposing a 14-page deck that's 60% placeholders. Never fabricate a drawing they didn't give you.

- **⚠️ A new camera angle is new architecture you haven't seen.** This is the package mode's sharpest
  hallucination trap. From a single front three-quarter view you **cannot** honestly produce a rear
  elevation, an aerial, or an interior — those require inventing facades, roofs and rooms that aren't in
  the input. The plan's standard rows (street-level, aerial, interior) are only valid when the user has
  **given you an input that shows them**.

  | You have | You can honestly render |
  |---|---|
  | One exterior view | That view — relit, re-materialed, re-seasoned. **Variations of the same camera.** |
  | Several model views / an orbit | Each of those cameras |
  | A floor plan | Plan-derived: dollhouse, layout analysis — **and interiors, only as far as the plan defines them** |
  | Nothing of the interior | **No interior render.** Say so. |

  **List what you can't do, and why, in the plan** — then offer the fix: *"export 2–3 more SketchUp views
  (rear, aerial, an interior) and each becomes an honest input; I'll add the matching pages."* A user
  who exports two more screenshots gets a real package. A user who gets invented rooms gets a lie.
- **Order tells the story:** why (concept, site) → what (drawings) → how it feels (materials, renders) →
  what happens next (summary). Don't lead with a render and back-fill the reasoning.
- **One visual identity across every page** — §80 governs the renders; the same palette, type and grid
  govern the pages (§34 / §67).
- Ask for the format if it isn't obvious: **16:9 deck slides** vs **A3/A2 boards** vs **A4 PDF**.

Then one line: *"Approve, or tell me what to cut, add or change."* **Wait.**

- **Scale the plan to the project.** A villa is not a masterplan. 6–10 renders is a normal package; 20 is
  a lot of money. If the user hasn't said, propose the smaller set and offer to extend.
- **Say what each image is FOR.** A hero sells; a street view contextualises; a detail proves quality.
  A deliverable with no purpose is padding — cut it before the user has to.
- **Graphics are free, renders are not.** Keep the two columns separate so the cost is legible.

## Step 2 · Produce, under one Identity

On approval:
- Lock the **Project Identity block (§80)** first. Reuse it **verbatim** in every render. Only the axis
  each image is *meant* to vary (time of day, angle, material option) may change.
- Preservation Contract applies to every image. `--aspect auto` throughout unless a deliverable
  genuinely needs a different format (a 9:16 social crop, a 4:3 board plate) — and when it does,
  **say so**, because it's a deliberate exception to the crop lock.
- Run **§83** on every output: `Read` it, check it, reject and re-run anything that drifts from the
  Identity or shows artifacts. **A set is only as good as its worst image.**

## Step 3 · Organize the package

Renders go into a **project folder with ordered, self-describing names** — not a flat timestamp dump:

```bash
python3 scripts/render.py --image design.png --prompt "<...>" --aspect auto \
  --out "~/Downloads/arch-renders/<project-slug>/01-hero-exterior-golden.png"
```

Convention: `NN-<deliverable>-<variant>.png` → `01-hero-exterior-golden.png` ·
`04-hero-exterior-night.png` · `07-material-variant-timber.png`. The number is the plan's row, so the
folder reads back as the plan.

Close by listing what was produced, where it is, and what's still open (e.g. *"boards are drafted as
layouts — say the word and I'll render the plates"*).

---

# 84 · The studio lenses (multidisciplinary review)

The skill thinks like a **studio**, not a soloist. A persona list changes nothing — *lenses* change the
output. When reviewing, critiquing or quality-checking a project, pass it through the lenses that are
actually relevant, and **name which lens raised each point** so the user knows who's talking.

| Lens | The question it asks | Where it lives |
|---|---|---|
| **Architect** | Is the concept clear, and does the building deliver it? | §42, §61 |
| **Interior designer** | Does the inside honour the outside? Ergonomics, materials, light. | §32, §49 |
| **Landscape architect** | Is the ground plane designed, or just decorated? Will it be alive in 20 years? | `typologies/landscape.md`, §35 |
| **Urban designer** | What does this do to the street, the block, the public realm? | §29, §35 |
| **Lighting designer** | Does light reveal the architecture, or fight it? Layers, glare, temperature. | §50 |
| **FF&E specialist** | Is every piece functional, correctly scaled, ergonomically clear? | §49 |
| **Structural coordinator** | Does the structure make sense? Grid, load path, vertical continuity. | §57, **§90** |
| **MEP coordinator** | Where do the services go? Is the floor-to-floor honest? | **§91** |
| **BIM manager** | Is it coordinated, clash-free, issuable? | **§92** |
| **Accessibility specialist** | Can everyone approach, enter, circulate, use, and *escape*? | **§93** |
| **Sustainability consultant** | Passive first — or is it a glass box with PV on top? | **§97–104** |
| **Cost / buildability** | Can this be built, in this market, for this money? | §56, **§95**, **§96** |
| **Visualization artist** | Does it read? Composition, light, scale, believability. | §45, §66 |
| **Critic** | Would this survive a jury? | §61 |

**Rules of use:**
- **Pick the lenses that matter.** A kitchen render does not need a BIM manager. Running all fourteen on
  every job is noise, and noise is what this skill was rebuilt to stop.
- **Every lens is advisory.** Lenses *observe and propose* — none of them may redesign the project. The
  **Preservation Contract** outranks all of them.
- **Cite the discipline boundary.** The structural, MEP, fire and accessibility lenses are
  *architect-level coordination*, not engineering — say so (see `technical-coordination.md`).
- **Disagreement is signal.** If the sustainability lens and the visualization lens want opposite things
  (shading vs. the money shot), say so out loud and let the user decide. Don't quietly average them.

---
