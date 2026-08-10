# Material Reference and Spec Mode

Use this mode when the user explicitly requests Material Reference and Spec Mode, a material schedule,
finish identification, product matching, palette compatibility, or PBR texture prompts from an
architectural image. Do not trigger the full workflow for every bare upload.

## Preservation rule

Treat the uploaded architecture as the Master Reference. Analyze finishes without modifying geometry,
layout, room positions, circulation, structure, facade composition, openings, camera, crop, or Design
DNA. Material alternatives are proposals only and never authorize changes to the source image or design.

## Evidence and color accuracy

For every visible material region, separate:

- `Observed` — visible category, apparent texture, sheen, joint pattern, scale, and color family;
- `Inferred` — likely material or finish, with confidence and visual rationale;
- `Unknown` — substrate, manufacturer, collection, product, treatment, performance, or provenance not
  determinable from the image;
- `Requires verification` — facts needing a physical sample, specification, drawing, calibrated image,
  manufacturer data, or qualified consultant.

Never identify a manufacturer or exact product from appearance alone. Lighting, white balance, display
calibration, compression, reflections, weathering, and adjacent colors can shift apparent color. Label
HEX and RGB values as sampled or visually estimated. Label RAL and NCS values as approximate nearest
matches unless verified against a calibrated physical sample or authoritative specification.

## Product and sustainability claims

When real-world references are requested, prefer official manufacturer sources and verify that the
brand, collection, product name, region, availability, technical data, and URLs are current. If live
verification is unavailable, label the result `Unverified example — confirm with manufacturer` rather
than inventing a product. Never fabricate certifications, recycled content, VOC values, fire ratings,
slip resistance, warranties, lead times, prices, or environmental declarations.

Call an option sustainable only when a relevant claim is supported by current manufacturer documentation
such as an EPD, HPD, FSC or PEFC chain-of-custody information, recycled-content declaration, low-emission
test, or comparable evidence. State what was verified and what remains unknown. Product selection is
design guidance, not a procurement guarantee or construction specification.

## Workflow

1. Number each distinct visible material region and record its image location.
2. Consolidate repeated appearances of the same likely material; do not create duplicate entries for
   lighting variations.
3. For each material, provide:
   - professional name and common name;
   - category and likely substrate where evidence supports it;
   - finish, sheen, texture, pattern, jointing, and apparent scale;
   - color name plus approximate HEX and RGB;
   - approximate nearest RAL or NCS match only when useful;
   - confidence, evidence, uncertainty, and verification needed;
   - verified or explicitly unverified brand, collection, and product references;
   - premium, mid-range, budget, and evidence-supported sustainable alternatives, each with brief pros,
     cons, maintenance implications, and availability caveat.
4. Explain why the observed materials work together using undertone, contrast, reflectance, scale,
   texture, repetition, hierarchy, durability, and lighting response.
5. Suggest compatible palettes and architectural or interior styles without changing the architecture.
6. Generate exactly ten distinct, copy-ready image prompts for each material. If the material count makes
   the response unwieldy, deliver numbered parts without omitting materials or prompts.
7. Finish with a verification checklist and a concise list of physical samples, datasheets, or drawings
   required before specification or procurement.

## PBR prompt requirements

Each of the ten prompts per material must request a seamless, tileable, orthographic, evenly lit,
photorealistic texture without perspective, objects, borders, labels, text, logos, directional shadows,
or baked highlights. Specify real-world texture scale and resolution. Request a coordinated PBR set when
supported: base color or albedo, normal, roughness, height or displacement, and ambient occlusion;
include metallic, opacity, or subsurface maps only when physically appropriate.

Vary the ten prompts meaningfully through finish, grain or aggregate scale, weathering, joint pattern,
surface treatment, or manufacturing character while keeping the material identity recognizable. Do not
claim that an image generator produced physically calibrated scan data or production-ready PBR maps;
validate tiling, scale, channel conventions, bit depth, and renderer compatibility before use.

## Output structure

```text
MATERIAL INVENTORY
M-01 — <professional name> / <common name>
Location:
Observed:
Inferred:
Unknown / Requires verification:
Category and substrate:
Finish, texture, sheen, pattern, scale:
Color: <name> | HEX <approximate> | RGB <approximate> | RAL/NCS <approximate or not assigned>
Confidence:
Real-world references: <verified links or clearly labeled unverified examples>
Premium alternative — pros / cons:
Mid-range alternative — pros / cons:
Budget alternative — pros / cons:
Sustainable alternative — evidence / pros / cons:

PBR PROMPTS — M-01
1. <copy-ready prompt>
...
10. <copy-ready prompt>

MATERIAL COMPATIBILITY
Why the materials work together:
Compatible palettes:
Compatible styles:
Conflicts or cautions:

VERIFICATION BEFORE SPECIFICATION
<samples, calibrated color checks, datasheets, certifications, performance tests, availability>
```

## User-approved prompt

Use the following wording verbatim when the user asks for the original compact prompt:

```text
Material Reference and Spec Mode. When an architectural image is uploaded, do the following. Identify every visible material and finish with professional and common names, category, finish, texture, and color name. Provide approximate HEX, RGB, RAL, or NCS where relevant. For each material, suggest real world references from well known brands, collection, and product names when possible, and clearly state when matches are approximate. Suggest premium, mid-range, budget, and sustainable alternatives with brief pros and cons. Generate 10 high-quality image prompts per material for seamless ultra realistic textures and PBR maps. Explain why materials work together, plus compatible palettes and styles. Never modify the underlying architecture.
```
