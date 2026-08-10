# AI Image Generation and High-Resolution Quality Engine

Use this module when the user requests generated or edited architectural images, one or two strongest
visual options, ChatGPT Image Generation, Nano Banana, native 4K, high-resolution output, portfolio
imagery, presentation imagery, or print delivery. Apply `core-policies.md`, `architectural-camera-director.md`,
and the relevant source, prompt, rendering, and continuity modules first.

## Contents

1. Provider routing
2. Goal and bounded generation
3. Preservation and camera control
4. High-resolution production standard
5. Image QA and selection
6. User-approved prompt

## Provider routing

Treat **ChatGPT Image Generation** and **Nano Banana** as separate engines:

- ChatGPT Image Generation means the verified built-in OpenAI image-generation capability.
- Nano Banana means the verified Gemini or Imagen image capability and its required authentication,
  model, API, limits, and output workflow.

Do not combine the names into a nonexistent model or tool. Honor an explicit provider choice. When the
user has not selected one, prefer the verified available engine that best supports the source inputs,
preservation requirements, target aspect ratio, resolution, privacy needs, cost, and output format.
Prefer built-in ChatGPT Image Generation in a ChatGPT or Codex workflow when it is available and fit for
the task; treat Nano Banana as the preferred alternate when its capability and authentication are
verified. Never claim either engine is available, authenticated, free, image-conditioned, seedable, or
4K-capable without checking the current tool and model.

Changing provider may change data destination, cost, fidelity, reproducibility, and output limits.
Disclose those changes and obtain the approvals required by `core-policies.md`. If no suitable engine is
available, return the final production prompt and exact execution specification instead of pretending an
image was generated.

## Goal and bounded generation

Before generation determine the image's decision or communication goal, intended audience and use,
source and revision, edit target versus style reference, locked architecture, allowed changes, approved
Project Context, camera, lighting, aspect ratio, target output, and acceptance criteria. Ask only when a
missing answer materially affects the output; otherwise proceed using disclosed safe defaults.

Generate one strong image when one satisfies the request. Generate a maximum of two images or attempts
per user request unless the user explicitly asks for more. Do not create filler variations, duplicate
prompts, arbitrary cameras, or unrequested scenes. More than two images still requires provider,
privacy, cost, and attempt-count approval when applicable.

If producing two options, vary only one approved axis such as lighting, material proposal, atmosphere,
or documented viewpoint. Keep architecture, revision, Design DNA, continuity, and all other locked
variables constant. Record the provider, tool or model when known, prompt, source IDs, output path,
dimensions, and approved variation axis for each image.

## Preservation and camera control

Use the approved architecture as the Master Reference. Preserve documented footprint, massing, floor
count, walls, openings, structure, room positions, dimensions, proportions, facade organization,
circulation, and Design DNA. Preserve the approved camera exactly; when no camera is locked, select one
through `architectural-camera-director.md` before generation and keep it consistent across options.

Generative imagery cannot prove dimensional or pixel-level identity. Do not claim an exact or 100%
architectural match solely because the prompt requested it. Validate visually against the reference and,
when identical framing permits, use alignment, overlay, edge, silhouette, opening-count, and key-anchor
comparisons. Reject material drift such as moved openings, altered volumes, added floors, changed room
geometry, or camera drift. A rejected result is not permission for another paid attempt unless that
attempt was already authorized.

For geometry-critical deliverables, state that the authoritative CAD/BIM or measured drawing remains the
source of truth and recommend a deterministic 3D/CAD render workflow when generative fidelity is
insufficient.

## High-resolution production standard

Request native 4K only when the selected tool and model support the required pixel dimensions and aspect
ratio. Otherwise generate at the highest verified native quality that preserves the intended crop, then
use a verified upscale workflow when available and authorized. Never describe an upscaled image as
native 4K, and never equate a prompt phrase such as “4K” with actual pixel dimensions.

For every final image report:

```text
Pixel dimensions and aspect ratio:
Native generation or upscale:
Provider and model/tool when verified:
Upscale factor and method when used:
File format, color profile when known, and file size:
Intended presentation or print size and effective PPI when requested:
Source revision and preservation status:
QA status and unresolved limitations:
```

Use a lossless or high-quality delivery format appropriate to the workflow. Preserve an archival master
before compressed derivatives. Do not promise large-format print suitability from pixel count alone;
consider physical size, viewing distance, effective PPI, compression, color profile, sharpening, and the
printer or publication specification. Do not invent CMYK conversion, bleed, proofing, or printer
requirements.

## Image QA and selection

Inspect each image at full available resolution. Check:

- architectural preservation, camera, verticals, horizon, crop, scale, and perspective;
- material scale, texture continuity, junctions, edges, reflections, transparency, shadows, and lighting;
- sharp focal detail without halos, oversharpening, noise, smearing, repeated textures, fake HDR, or
  low-detail patches;
- entourage anatomy, contact, scale, duplication, and occlusion;
- consistency with approved materials, palette, lighting, furniture, landscape, atmosphere, and grade;
- actual dimensions, format integrity, successful upscale, and visible artifacts at 100% view;
- watermarks, unintended text, logos, or provider artifacts.

Reject images that fail critical preservation or quality criteria. Do not call a result publication-ready
until the available checks pass, and disclose any item that cannot be verified.

After delivery, briefly explain the specific strength and limitation of each accepted image. Recommend
one based on the stated goal, not personal preference. If only one image passes, identify it as the sole
accepted option. If none passes, report the failure and next corrective action instead of recommending a
failed result.

## User-approved prompt

Use this wording verbatim when the user requests the compact image-generation and quality prompt:

```text
AI Image Generation Engine. Use ChatGPT Image Generation Nano Banana as the default when images are needed. Generate a maximum of two images per request unless explicitly asked for more. Never generate unnecessary variations. First, understand the goal of the image, then produce only the two strongest options. Each image must preserve the approved architecture exactly, follow the selected camera composition, and remain consistent with all project decisions. After generating, briefly explain why each image works and recommend one.  High Resolution Image Quality Standards. Generate all final images in ultra-high resolution suitable for professional presentations, portfolios, and large-format printing. Target native4K when supported. Otherwise, use the highest native quality available, optimized for clean upscaling. Require sharp details, realistic materials, accurate lighting, clean edges, high dynamic range, and no blurry or low-detail outputs. Prioritize quality over speed. Every image must be publication-ready.
```
