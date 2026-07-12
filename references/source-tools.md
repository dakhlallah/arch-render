# Source Tools — feeding D5 Render, Cinema 4D & others into arch-render

The skill accepts ANY image as input. But **where the image comes from changes the job**:

- **Flat input** (hand sketch, CAD line drawing, SketchUp/Revit screenshot, floor plan)
  → the AI must *invent* materials, depth and lighting. Use the full preserve clause.
- **Already-rendered 3D input** (D5 Render, Cinema 4D, Lumion, Enscape, Twinmotion, Blender)
  → the AI's job is to **enhance / polish**, not redesign. The geometry, perspective and basic
  materials are already correct — we only push realism, lighting, materials and surroundings.
  Use the **Enhance clause** (see `prompt-recipe.md`) so it stays faithful to your render.

---

## D5 Render

D5 is a real-time arch-viz renderer. Two good ways to get an input image:

1. **Final/draft render export** — render a still in D5 (any quality, even draft/low-sample) and
   export the PNG/JPG. Feed that file to the skill to clean noise, upgrade materials and add a
   believable sky/environment.
2. **Viewport / screenshot** — a quick screen grab of the D5 viewport also works as input.

Tips for best results:
- Export at the **largest resolution** you can; the skill keeps aspect ratio.
- A neutral/grey "clay" D5 render is fine — the skill adds the real materials.
- If you already set materials in D5, mention them in the request ("keep the stone facade and
  wood balconies") so the skill preserves them instead of guessing.
- Use the **Enhance clause** so D5's camera angle and proportions are respected exactly.

## Cinema 4D (C4D)

Maxon Cinema 4D — 3D modeling/animation, often rendered with Redshift, Octane, or the standard/
physical renderer. To use a C4D model in this skill:

1. **Rendered still** — render a frame (Redshift/Octane/Standard) and save the image, then feed it
   in for a photoreal polish. Best path.
2. **Viewport capture** — a screenshot of the C4D viewport (even untextured/clay shading) works;
   the skill adds materials and lighting.
3. **Turntable frames** — if you have several angles, render a few stills and run the skill on each
   to get a consistent set of photoreal views.

Tips:
- Clay/grey C4D viewport grabs → use the **full preserve clause** (treat like a model screenshot).
- Textured Redshift/Octane stills → use the **Enhance clause** (treat like a draft render to polish).
- For interiors, mention the room type and key furniture so scale stays believable.

---

## Software I/O table — what to export, and what we can give back

**This skill consumes raster images.** It cannot open, parse or drive a native CAD/BIM/3D file. What it
*can* do is take your export, and hand back either a **prompt**, a **scene-setup checklist**, or a
**coordination/authoring note** — depending on what the tool actually is.

| Tool | Best export to feed in | Clause | What we hand back |
|---|---|---|---|
| **AutoCAD / Vectorworks** | PDF→PNG or DWG plotted to image | Preserve | Render prompt · drawing-standards review (§30/§31) |
| **Revit / ArchiCAD (BIM)** | 3D view screenshot, or a plotted sheet | Preserve | Render prompt · **BIM coordination advice (§92)** · drawing-set review. We do **not** edit the model. |
| **Rhino** | viewport capture or a Rhino render | clay→Preserve · rendered→Enhance | Render prompt |
| **Grasshopper / Dynamo** | a captured result geometry image | Preserve | Prompt on the *output*. ⚠️ **We cannot author or drive the parametric definition** — say so plainly. |
| **SketchUp** | viewport screenshot | Preserve | Render prompt · scene-setup checklist |
| **Blender / 3ds Max / Maya / C4D / Houdini** | viewport grab (clay) **or** a rendered still | clay→Preserve · rendered→Enhance | Render prompt · **scene-setup checklist** (HDRI, sun, PBR, camera, samples). We do **not** drive the app. |
| **V-Ray / Corona / Octane / Redshift / Arnold / FStorm** | rendered still (any quality, even draft) | **Enhance** | Polish prompt · **§13 V-Ray tail** · material/setup checklist |
| **Lumion / Enscape / Twinmotion / D5** | rendered still or viewport | rendered→Enhance · clay→Preserve | Polish prompt · scene-setup checklist |
| **Unreal Engine** | high-res screenshot / movie-render still | Enhance | Polish prompt · lighting/post checklist |
| **Substance 3D** | material preview / render | — | PBR material direction (§47, `material-catalog.md`). We don't author `.sbsar`. |
| **Photoshop / Lightroom** | any image | — | Post-processing direction (§17) · Firefly/Generative-Fill prompts for **surgical local edits** |
| **Illustrator / InDesign** | board or sheet export | — | Board layout & graphic critique (§34/§67) |
| **Figma** | frame export | — | Board/presentation layout critique. For actual Figma authoring, that's the `figma` skills, not this one. |

**Be honest about the boundary.** If a user asks this skill to *model*, *edit the BIM*, *drive
Grasshopper* or *render in Blender*, say clearly that it can't — and offer what it can: the prompt, the
checklist, or the coordination review. Never imply the model was touched.

## Quick decision

| Input you have | Clause to use | What the skill does |
|---|---|---|
| Hand sketch / CAD line / floor plan / elevation | Preserve (full) | Build a realistic building from scratch, faithful to shape |
| SketchUp / C4D / D5 **clay** screenshot | Preserve (full) | Add all materials + lighting + context |
| D5 / Redshift / Octane / Lumion **render** | **Enhance** | Polish realism, fix materials, add sky & surroundings |
| **Photo of an existing built building** | **Preserve (materials-locked)** | Relight / restyle the environment only — see below |

### Photo of an existing building (relight / re-season / re-context)

A photo is not a sketch: nothing needs inventing, and the real materials are already correct. Use the
preserve clause but **also lock the materials** — the job is lighting, sky, weather, season or context.

> "This is a real photograph of an existing building. Keep the EXACT geometry, proportions, floor count,
> and the placement of every window, door and balcony. Keep the same camera, perspective, framing and
> crop. **Preserve the existing facade materials, colours and textures exactly as photographed** — do
> not restyle or replace them. Change ONLY [the lighting / time of day / weather / season / surroundings]:
> [golden-hour sun, long warm shadows, warm interior glow in the windows…]. Photorealistic, ultra-detailed."

If the user *does* want a new facade skin on a real building, that's a **facade redesign** (render type 7)
— materials move to the modifiable list, geometry and openings stay locked.
