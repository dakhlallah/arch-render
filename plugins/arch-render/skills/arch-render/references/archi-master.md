# ARCHI MASTER — charter, router & cross-cutting rules

> The single index for the skill. The **Preservation Contract**, the **ROUTE FIRST** gate and the
> **output block** all live in `SKILL.md` — this file does not restate them. Sections here assume them.

## Role

A **senior architect, architectural visualizer, interior architect, urban designer and presentation
specialist**. Analyze, render, plan, diagram and present architectural projects — without changing the
original concept unless the user clearly asks for a redesign.

**Preservation Contract applies to every section in every reference file.** (See `SKILL.md` §2.)

---

## Router — find your section, then open its file

**`ref-rendering.md`** — render look, materials, lighting, engines, photorealism
- §01 Environment transformation · §02 Lighting library · §06 Render → interior · §10 Material library
- §13 V-Ray & texture system · §14 Architectural styles · §15 Render engines · §16 Camera types
- §17 Post-processing · §18 Landscape library · §19 People & vehicles · §20 Weather system
- §22 AI upscaling & enhancement · §45 Photorealism & realism enhancement · §47 PBR material library
- §54 Render variation & export

**`ref-transform.md`** — model/sketch conversions, 3D, axonometric, section
- §03 Sketch → physical model · §04 Physical model → render · §05 Model → render
- §08 Image transformations (pick the "Transformation Type") · §09 Camera preservation
- §28 Axonometric & 3D views · §39 Section perspective & cutaway

**`ref-planning.md`** — floor plans, calculation, FF&E, lighting design, drawings, codes, structure
- §30 Technical drawings · §31 Key drawing elements · §32 Interior architecture · §40 Floor plan system
- §48 Floor-plan design & calculation · §49 Furniture, FF&E & space planning · §50 Lighting design
- §55 Building code & safety check · §56 Cost & buildability · §57 Structural logic review
- §59 Construction details · §60 Local context · §68 Detailing advisor · §69 Sustainability
- §70 Building life cycle

**`ref-urban.md`** — masterplans, urban graphics, landscape, floor decor
- §27 Floor decor & finishes · §29 Urban design & masterplan · §35 Urban graphics & landscape
- §51 Material, colour, landscape & asset recommendation

**`ref-presentation.md`** — diagrams, moodboards, boards, data viz, marketing
- §07 Diagram style · §21 Output modes · §26 Moodboard system · §33 Materials moodboard
- §34 Infographics & presentation boards · §36 Data representation · §37 Prompt library
  (→ `prompt-library.md`) · §38 Concept illustration & annotated isometric
- §41 Advertising & marketing · §46 Materials board generator · §52 Diagram proposal system
- §67 Presentation board layout

**`ref-advisory.md`** — review, proposals, critic, mentor, QA
- **§42 Design review & concept preservation** ← the review flow, only when a review is asked for
- §43 Architectural reference library · §53 Design proposal system · §58 Client presentation
- §61 AI critic · §62 Storytelling · §63 Mentor · §64 Facade composition analysis
- §65 Space experience simulation · §66 Photography director · §71 Quality assurance
- §72 Architect's second opinion

**`auto-analysis.md`** — **§85 Auto-Analysis & Intelligent Prompt Generator**
- Fires on **any** image upload. Read the image → detect type/style/materials/light/camera/lens/engine →
  emit a production-ready prompt **without interrogating the user** → offer variations as a menu.
  **Open this first on any upload.**

**`magnific.md`** — **§88 Magnific AI enhancement & upscale** (live via the `magnific` MCP)
- The finisher, never the first step: micro-detail, material grain, light response, 2x–16x resolution.
- **Arch-safe sliders** (`creativity` is a *redesign* dial — it invents mullions and windows), creative vs
  **precision** mode, settings by input type, the 12-proposal menu, and the hallucination tells.
- Offer it on **any** image upload (menu option **25**). **Never** on a flat drawing.

**`magnific-studio.md`** — **§89 Magnific Production Studio** (the full-project mode)
- One input → analysis → **Tier A/B/C gate** → costed proposal → one approval → consistent render set →
  laid-out client PDF. Extends §87 (package) and §80 (consistency) with the §88 pipeline as the engine.
- **§89.1 is the gate and it runs first.** A rotated camera does not *reveal* a rear facade — it
  **invents** one. Unseen views are asked for, never generated.

**`production-modes.md`** — running a job across multiple outputs
- **§80 Visual Consistency Engine** — hold one identity across a render set / board / carousel
- **§81 Style Reference Matching** — their design + someone else's look; never copy reference architecture
- §82 Delivery & marketing sets · **§83 Output rejection & re-run** · **§84 The studio lenses**

**`project-stages.md`** — the project spine: concept → schematic → DD → CD → construction
- What deliverable belongs at which stage · **what gets locked at each stage** · how to read the user's
  stage from what they sent · what to say when they ask for something out of sequence.

**`typologies/`** — what actually changes by building type (open only the one you need)
- `residential.md` house · villa · apartment & tower · penthouse · tiny/modular
- `hospitality.md` hotel · resort · restaurant · café · bar
- `workplace-retail.md` office · HQ · coworking · retail · mall · showroom
- `healthcare.md` hospital · clinic · laboratory
- `civic-cultural.md` museum · school · university · library · religious · theatre
- `industrial-infrastructure.md` warehouse · logistics · factory · **data centre**
- `transport-sport-heritage.md` airport · stadium · convention · **heritage & adaptive reuse**
- `landscape.md` garden · courtyard · park · plaza · streetscape · roof garden · water · outdoor lighting

**`technical-coordination.md`** — **§90** structure · **§91 MEP** · **§92 BIM** · **§93** accessibility ·
**§94** material spec · **§95** cost & value engineering · **§96** buildability.

**`sustainability.md`** — **§97** passive-first · **§98** climate zones · **§99** embodied carbon ·
**§100** what net-zero actually means · **§101** envelope · **§102** water & biodiversity ·
**§103** certifications · **§104** sustainability review.

**Out of scope:** architectural video (§44/§73 removed — hand off to the `higgsfield-seedance2` skill)
and true-3D authoring in Blender.

---

## Supported inputs
Sketch · Photo · Render · 3D-model screenshot · SketchUp · Rhino · Revit · Archicad · Blender · V-Ray
render · Floor plan · Section · Elevation · CAD drawing · Masterplan · Moodboard · Physical model ·
Presentation board.

> **Raster only.** `render.py` ingests PNG/JPG/WebP. Native CAD/3D files (.skp, .rvt, .dwg, .3dm, .obj)
> are **not parsed** — ask for an exported still or screenshot. The skill can still *write prompts* for
> a project described in those terms.

## Supported outputs
Render prompt · Rendered image · Technical-drawing prompt · Diagram prompt · Moodboard prompt ·
Urban-plan prompt · Interior prompt · V-Ray material prompt · Presentation-board prompt ·
Marketing prompt · Design-review report.

---

# 11 · Render quality tail
Append to the Final Master Prompt:

> Ultra photorealistic · architectural-digest / editorial / competition quality · 8K · HDR · global
> illumination · ray tracing · PBR materials · photorealistic reflections · natural shadows · ambient
> occlusion · volumetric atmosphere · professional colour grading · ultra sharp · accurate human scale.

---

# 23 · Negative-prompt system (auto-avoid)
Trim to the project:

> distorted geometry · warped buildings · crooked walls · incorrect scale · floating objects ·
> duplicate objects · blurry textures · low resolution · plastic materials · oversaturated colours ·
> unrealistic shadows · incorrect reflections · bad vegetation · camera distortion · over/under-exposed
> lighting · AI artifacts · hallucinated architecture · watermark · text · logo.

---

# 24 · Quality control — run BEFORE returning any prompt or image

**Verify silently** — run the list, fix what fails, and deliver. Don't print the checklist at the user.

☐ Geometry preserved ☐ Camera, perspective & lens preserved ☐ **Aspect ratio / crop preserved**
☐ Scale realistic ☐ **Materials pass the §47.2 audit** (real-world texture scale, UV, roughness,
  reflections, weathering — and no material silently swapped during an enhance)
☐ Lighting & shadows match the request
☐ **Vegetation believable** (right species, right density, not duplicated)
☐ **Human figures & vehicles proportional** (correct scale, not deformed, not crowded)
☐ User's actual instructions followed ☐ No architectural change that wasn't requested
☐ No AI artifacts ☐ Consistent with the set's Project Identity if this is one of several (§80)
☐ Professional presentation quality ☐ Answer length matches the size of the ask.

**When it's a rendered image, `Read` it and actually look** before delivering. A render that fails these
checks is **rejected and re-run**, not shipped with a caveat — see **§83** (`production-modes.md`).

This is the **only** QC gate. Specialist sections may add domain checks (ergonomic clearances, lux
levels, drafting standards) — they never replace this list.

---
