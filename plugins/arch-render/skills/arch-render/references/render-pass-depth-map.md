# Render Pass and Depth Map Generation

Use this module when the user requests depth maps, Z-depth, ambient occlusion, material or object IDs,
shadow passes, masks, compositing passes, or a post-production package aligned with a beauty render.
Apply `core-policies.md`, `image-generation-quality-engine.md`, and the selected renderer's verified
capabilities.

## Native versus derived passes

Prefer native passes exported from the same 3D scene, render frame, and camera as the beauty image. Only
native renderer data can reliably provide true geometric depth, object/material IDs, normals, lighting
components, and exact registration.

If only a flattened beauty image exists, label any monocular depth, segmentation, AO, shadow, normal, or
mask result `AI-derived approximation`. Do not call it a true render pass or claim exact geometry,
occlusion, physical lighting separation, reversible compositing, or pixel-perfect alignment. An inferred
Material ID cannot recover hidden material assignments; an inferred Shadow Pass cannot separate all
direct, indirect, contact, and baked shadows.

If the requested accuracy requires native passes but the scene or renderer is unavailable, provide the
exact pass-export specification and identify the required source files instead of fabricating passes.

## Select useful passes

Generate passes only when requested or when they have a clear post-production use. Recommend the smallest
useful package:

- **Depth or Z-depth** — atmospheric depth, depth-aware grading, fog, or controlled depth of field;
- **Ambient Occlusion** — subtle contact definition; never multiply so strongly that corners look dirty;
- **Material ID or Cryptomatte** — material-specific selection and grading;
- **Object ID or Cryptomatte** — object, entourage, glazing, vegetation, or fixture isolation;
- **Shadow** — controlled shadow density or color when the renderer supports a separable shadow result;
- **Diffuse, direct, indirect, reflection/specular, refraction/transmission, emission, normal, alpha, or
  position** — include only when the renderer and compositing plan require them.

Do not generate a large default pass stack for a simple presentation render. Record the purpose of every
included pass and omit redundant or unsupported channels.

## Alignment and export specification

Lock the scene revision, frame, camera transform, projection, lens, sensor fit, shift, clipping, render
resolution, pixel aspect, crop, render border, overscan, and distortion workflow across the beauty and
all passes. Disable any pass-specific crop or resize. Apply identical denoising and edge treatment only
where technically appropriate, and document exceptions.

Use professional formats appropriate to the data:

- Beauty and preview: high-quality PNG, TIFF, or EXR as required;
- depth and high-dynamic-range data: 16-bit or 32-bit float EXR when supported;
- IDs and masks: Cryptomatte in EXR when supported, otherwise lossless PNG/TIFF with stable IDs;
- preserve linear data for compositing passes and state the working color space, transfer function,
  premultiplication, alpha behavior, and channel mapping when known.

For depth, record camera near/far interpretation, units, whether values are linear or normalized, and
which tone-mapped grayscale preview accompanies the raw data. A visible grayscale preview is not a
replacement for a float depth channel. Use smooth gradients without banding, clipping, halos, stair-step
edges, holes, or invented geometry.

Name files consistently:

```text
<project>_<view>_<revision>_beauty.<ext>
<project>_<view>_<revision>_depth.<ext>
<project>_<view>_<revision>_ao.<ext>
<project>_<view>_<revision>_material-id.<ext>
<project>_<view>_<revision>_object-id.<ext>
<project>_<view>_<revision>_shadow.<ext>
```

## Registration and QA

Before delivery verify:

- identical width, height, aspect ratio, crop, orientation, and pixel origin;
- matching silhouette, opening, edge, and camera anchors at full resolution;
- no spatial drift, warping, resampling offset, fringe, halo, compression damage, or missing pixels;
- smooth, monotonic depth transitions with correct foreground/background direction;
- unique, stable, documented IDs and clean selections at anti-aliased edges;
- correct alpha, premultiplication, data range, bit depth, channels, and color-management metadata;
- the beauty render is unchanged and every pass matches the same approved revision.

Where possible, verify registration with a difference, edge-overlay, or compositing test. Deliver a pass
manifest listing filename, type, native or derived status, purpose, format, dimensions, bit depth, color
space or data encoding, source revision, alignment result, and limitations.

## User-approved prompt

Use this wording verbatim when the user requests the compact render-pass prompt:

```text
Render Pass and Depth Map generation. Generate clean grayscale depth maps and professional render passes aligned perfectly with each final render. Include Depth Map, Ambient Occlusion, Material ID, Shadow Pass, and other useful passes when appropriate. Ensure smooth gradients, artifact-free edges, and exact alignment with the beauty render. Provide passes only when useful for post-production or upon request.
```
