# ARCHI MASTER — Rendering — look, materials, lighting, engines, photorealism

> **Preservation Contract applies** (see `SKILL.md` §2). Jump to a section by its `# NN · Title`.
> Sections: §01 §02 §06 §10 §14 §15 §16 §17 §18 §19 §20 §21 §22 (pick-lists) · §13 V-Ray ·
> §45 Photorealism · §47 PBR materials · §54 Render variations.

---

# Pick-lists (§01 §02 §06 §10 §14 §15 §16 §17 §18 §19 §20 §21 §22)

Menus to compose a prompt fast. Pick, don't dump — name only what the project needs.

- **§01 Environment** — urban downtown · luxury district · European city · Japanese street · forest ·
  mountain · desert · beachfront · waterfront · park · campus · industrial · business district ·
  historical city · tropical · winter. *Transform only the surroundings; the building stays exact.*
- **§02 Lighting** — morning · golden hour · blue hour · sunrise · sunset · midday · overcast · soft
  diffused · studio · night · moonlight · warm/cold interior · volumetric · HDRI · editorial · competition.
- **§06 Interior languages** — minimal · Japanese · Scandinavian · Japandi · contemporary · luxury ·
  industrial · Mediterranean · Arabic · brutalist · tropical · neo-classical.
- **§10 Materials** — concrete · fair-face concrete · stone · marble · travertine · granite · wood ·
  oak · walnut · steel · brass · copper · glass · curtain wall · aluminium · brick · terracotta ·
  corten. *Full catalogue with paste-ready prompt fragments: `material-catalog.md`.*
- **§14 Styles** — minimalist · contemporary · modern · Bauhaus · brutalism · Scandinavian · Japanese ·
  wabi-sabi · Mediterranean · Arabic · Islamic · tropical · industrial · classical · art deco ·
  parametric · organic · high-tech · vernacular · sustainable.
- **§15 Engines** — V-Ray · Corona · Lumion · Twinmotion · Enscape · D5 · Unreal · Blender Cycles ·
  Octane · Redshift · Arnold · KeyShot.
- **§16 Cameras** — eye level · bird's eye · worm's eye · isometric · axonometric · drone · street view ·
  interior wide-angle · tilt-shift · 24 / 35 / 50 / 85mm · orthographic · section perspective.
- **§17 Post** — colour grading · exposure · white balance · contrast · bloom · ambient fog · film grain ·
  sharpening · depth of field · atmospheric perspective.
- **§18 Landscape** — trees · palms · pines · shrubs · grass · rocks · water · pools · paving · sidewalks ·
  street furniture · benches · bollards · lighting poles · pergolas · outdoor furniture.
- **§19 People & vehicles** — walking · sitting · families · cyclists · office workers · wheelchair users;
  cars · SUVs · buses · bicycles · EVs. *Scale cues only — never overcrowd.*
- **§20 Weather** — sunny · cloudy · rain · snow · storm · fog · mist · wet pavement · seasonal.
- **§21 Output modes** — competition board · presentation board · client presentation · portfolio ·
  marketing render · social · print A0–A4 · PDF-ready.
- **§22 Upscaling** — 2K / 4K / 8K · super-resolution · noise removal · detail enhancement.
  → To actually **run** one, use **§88 Magnific** (`magnific.md`) — it's wired to the `magnific` MCP and
  carries the arch-safe slider ranges. Mind the trap: `creativity` hallucinates windows and mullions.
  In this skill: raise `--max-edge` (up to 3840) and `--quality high`. For a dedicated upscaler, hand the
  file to the user's tool of choice (Magnific, Topaz) — this skill does not call them.

---

# 13 · V-Ray & texture system

When the user works in V-Ray (or asks for V-Ray quality), write the prompt/setup in V-Ray terms.

**Supports:** V-Ray for SketchUp · Rhino · Revit · 3ds Max · Cinema 4D · Blender. Features: V-Ray Sun ·
Sky · Dome Light · HDRI · Physical Camera · Environment Fog · Light Mix · VFB · Denoiser · Chaos Cosmos.

**PBR maps:** Diffuse/Albedo · Roughness · Normal · Bump · Displacement · Reflection · Glossiness ·
Metallic · AO · Opacity. With: real-world scale · seamless textures · correct UV / triplanar mapping.

**Material rules:** realistic V-Ray materials · accurate texture scale · texture direction matched to the
architecture · never stretch textures · no fake plastic · correct roughness & reflection · subtle
imperfections · real construction materials.

**Final V-Ray prompt tail** — always append for V-Ray tasks:
> "camera locked, design preserved, original geometry unchanged, realistic PBR V-Ray materials,
> accurate UV scale, natural lighting, global illumination, high-quality texture mapping, clean
> shadows, professional architectural visualization."

**Prompt Box — V-Ray render (paste-ready):**
> Photorealistic V-Ray render of the attached [building/interior], camera locked, design preserved,
> original geometry unchanged. Realistic PBR V-Ray materials: [fair-face concrete, brushed brass,
> low-iron glass] with accurate UV scale and roughness. Lighting: V-Ray Sun + Sky [time of day],
> [HDRI dome], Physical Camera, global illumination (Brute Force + Light Cache), ray-traced
> reflections, clean denoising. Natural shadows, professional colour correction, arch-viz quality.

For Lumion/Enscape-style real-3D tools the output is a **setup checklist** instead (sun/HDRI, GI, material
maps to assign, Physical Camera, denoiser, LightMix, VFB grade).

---

# 45 · Photorealism & realism enhancement

Target: output that reads as **professional architectural photography**, not an AI image.

**Standards:** true-to-life materials · physically accurate lighting · real-world scale · correct
construction details · natural imperfections · realistic reflections · accurate shadows · PBR ·
cinematic colour science.

**Realism cues to add:** surface micro-texture · concrete pores · wood-grain variation · stone veining ·
glass reflections (interior + exterior) · metal roughness & micro-scratches · weathering · edge wear ·
contact shadows · natural vegetation · interior light spill · exterior bounce light.

**Photography simulation:** bodies — Hasselblad X2D · Phase One XF · Sony A1 · Canon R5 · Fujifilm
GFX100 II. Lenses — 24mm TS · 35mm · 50mm · 90mm TS. Settings — real focal length · natural depth of
field · HDR exposure · correct white balance · perspective correction · soft optical falloff.

**Material realism:** *Concrete* — fine aggregate, pores, form-tie marks, natural discolouration.
*Wood* — real grain direction, variation, small imperfections. *Glass* — true transparency, correct
refraction, layered reflections. *Metal* — brushed finish, fingerprints, oxidation. *Stone* — natural
veining, correct edge profiles.

**Auto-eliminate:** plastic materials · over-smooth surfaces · fake reflections · melted geometry ·
warped lines · floating objects · duplicate/repeating vegetation & textures · oversaturation ·
hallucinated windows · distorted furniture · unrealistic people & cars.

**Post:** filmic grade · natural contrast · soft highlight roll-off · balanced shadow detail · accurate
exposure · professional sharpening · noise control · subtle bloom only.

**Aim** for an image a professional would accept as a photograph of the built project. Don't claim in
your reply that it *is* indistinguishable from one — show it and let the user judge.

---

# 47 · Intelligent material & texture system

Fires on **every** image upload and every render. **→ The catalogue, with a paste-ready prompt fragment
per material, is `material-catalog.md`.** Open it rather than improvising material descriptions.

## 47.1 · Identify — every major element, with a confidence level

For each visible element (facade · roof · frames · base · ground plane · floor · walls · ceiling ·
joinery · furniture · water · planting), name the most likely material from the catalogue:

> concrete · exposed/fair-face concrete · brick · stone · marble · granite · travertine · limestone ·
> wood · engineered wood · bamboo · steel · stainless · aluminium · corten · copper · brass · glass ·
> frosted/fluted glass · ceramic · porcelain · terrazzo · microcement · stucco · plaster · composite
> panel · fabric · leather · asphalt · gravel · grass (natural/artificial) · water · green wall

**Mark confidence, and never fabricate.** Three states, and say which:
- **Read** — clearly visible in the image. State it.
- **Estimate** — plausible but not certain ("reads as honed travertine, but could be limestone —
  **estimate**"). Say the word *estimate*.
- **Unknown** — a clay/white model or line drawing carries **no** material information. Don't pretend it
  does. **Choose a defensible default for the building type and say in one line that you chose it**
  (`SKILL.md` §2 — material is an *aesthetic* default, not an architectural fact).

## 47.2 · Audit — the material QC pass

When a render (yours or theirs) is on the table, check each material against these, and **name what
fails** rather than silently re-rendering:

| Dimension | The failure it catches |
|---|---|
| **Real-world scale** | Bricks the size of shoeboxes; floor planks 3 m wide. **The #1 tell of a fake render.** |
| **UV alignment & direction** | Stretched textures; wood grain running the wrong way; tile grid off-axis to the wall |
| **Tiling / repetition** | The same knot, brick or leaf visibly repeating |
| **Texture resolution** | Mush up close; detail that dissolves at the foreground |
| **Roughness / gloss** | Polished when it should be honed; the plastic look |
| **Metallic response** | Metal that reads as grey plastic; anisotropy missing on brushed finishes |
| **Reflection quality** | Reflections that don't match the scene; missing interior reflection in glass |
| **Refraction** | Glass with no thickness, no distortion, no green edge |
| **Normal / bump depth** | Flat concrete with no pores; brick with painted-on mortar |
| **Ambient occlusion** | No darkening in corners, reveals, or under sills |
| **Shadow interaction** | Contact shadows missing — objects float |
| **Weathering & imperfection** | Showroom-perfect surfaces. Real buildings have dirt runs, edge wear, water staining, patina. |

## 47.3 · Material lock during enhancement (the big one)

When **polishing an existing render** (Enhance clause), the job is to make the *chosen* material more
real — **never to swap it for a "better" one.** AI enhancers habitually "upgrade" concrete into marble
and timber into oak-veneer perfection. That is a **defect**, not an improvement.

> **Increase realism. Preserve the material palette.** Same material, same colour, same finish —
> more truth: pores, grain, roughness variation, weathering, correct reflection.

State it in the prompt: *"Keep every material exactly as chosen — do not replace or upgrade any
material. Improve only realism: texture detail, roughness, reflections, imperfections."*

## 47.4 · Replacement — only what was asked

If the user requests a material change, change **only the named surface**. The other materials, and all
geometry, dimensions, proportions and design intent, are untouched (Preservation Contract, `SKILL.md` §2).
"Change the facade to corten" is not permission to restyle the interior, the paving or the frames.

## 47.5 · Consistency across a project

Materials go in the **Project Identity block (§80)** and are reused **verbatim** across every image in a
set. If image 3's stone is warmer than image 1's for no requested reason, that's a defect — re-run it.

## 47.6 · Output — PBR descriptions

Write materials as physically-based descriptions fit for arch-viz: base colour · roughness · normal/bump ·
displacement where relevant · metalness · AO · real-world scale · seamless · correct UV direction. Use the
catalogue's prompt fragments (`material-catalog.md`) and swap the bracketed variant + finish.

A full materials board with manufacturer alternatives — **only if the user asks** (§46). Reference
professional scanned-PBR libraries for *quality standard* only; never copy proprietary assets.

---

# 54 · Render variation & export

When the user wants the same project in a different look — **architecture preserved, only the render
style changes.**

**Auto-detect from the input:** camera angle · focal length · geometry · materials · lighting · scale ·
building type · style · landscape · existing render quality.

**Variation axes:**
- **Day** — morning · midday · afternoon · golden hour · soft overcast
- **Night** — warm residential · luxury hotel · commercial · blue hour · city lights · rainy · foggy
- **Season** — summer · spring · autumn · winter · rain · snow · fog
- **Material** — concrete · stone · wood · glass · steel · brick · travertine · microcement · terracotta
- **Landscape** — minimal · luxury · Mediterranean · Japanese · tropical · urban · forest · waterfront
- **Engine look** — V-Ray · Corona · D5 · Lumion · Twinmotion · Enscape · Unreal · Octane
- **Export style** — photorealistic · clay · white model · diagram · technical illustration ·
  presentation board · marketing image · competition board

**Offer, don't auto-generate.** After delivering what was asked, offer a variation set in **one line** —
e.g. *"Want the golden-hour / night / editorial set (3 more renders)?"* — and say how many API calls it
costs. Generate only on a yes. A common set: 01 daytime editorial · 02 golden hour · 03 luxury night ·
04 landscape enhancement · 05 competition render.

**Prompt Box — Render variation (paste-ready):**
> Using the attached architectural [model / render / screenshot], generate a professional [GOLDEN HOUR /
> NIGHT / SEASONAL / MATERIAL] render variation. Preserve the EXACT geometry, camera angle, focal length,
> proportions, composition and structure — change ONLY the [lighting / materials / environment / season].
> Materials: [list]. Lighting: [time of day + temperature]. Environment: [landscape + context].
> Photorealistic, accurate material scale, realistic reflections and shadows, no AI artifacts,
> publication quality.

---
