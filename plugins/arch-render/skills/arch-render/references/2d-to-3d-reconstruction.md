# 2D-to-3D Architectural Reconstruction

Use this workflow for a 2D floor plan, architectural drawing, blueprint, CAD export, PDF drawing, or
BIM-derived sheet when the user requests a 3D architectural visualization.

## Objective

Analyze the supplied source and prepare or generate evidence-based photorealistic 3D architectural
renderings, such as:

- exterior views;
- interior views;
- bird's-eye views;
- isometric plans; and
- sectional perspectives.

Focus on rendering quality only. Do not treat visualization as permission to redesign.

## Preservation contract

Treat the uploaded plan as the Master Reference for every fact it visibly documents. Preserve its
geometry, scale, proportions, dimensions, floor count, room positions, walls, doors, windows, openings,
circulation, structural elements, annotations, spatial relationships, and design intent. Do not scale or
rotate the layout, stretch walls, shrink rooms, alter proportions, redesign, reinterpret, optimize,
complete, or invent architectural elements.

Apply `core-policies.md` as the authority. Distinguish:

- **Documented** — directly supported by the source;
- **Derivable** — can be constructed without adding architectural information;
- **Unknown** — absent or illegible; and
- **Source required** — necessary for the requested view but not supplied.

A 2D plan does not normally prove facade design, vertical dimensions, roof geometry, materials,
ceiling design, structural depth, or the appearance of unseen rooms. Never silently infer these as
facts.

## Reconstruction preflight

Before generating a view:

1. identify the source type, drawing scale, orientation, levels, dimensions, grids, room labels,
   openings, stairs, section markers, elevation markers, and referenced sheets;
2. verify that the requested camera can be supported by the available sources;
3. create a Source Coverage Matrix listing each required element as Documented, Derivable, Unknown,
   or Source required;
4. verify every documented wall, room location, opening, dimension, circulation path, structural
   alignment, and floor relationship against the Master Reference;
5. list the minimum missing sources needed for an accurate reconstruction;
6. stop before generation when information is missing, illegible, internally inconsistent, or would
   require invented architecture; identify the issue and request clarification instead of correcting it;
7. complete the privacy, provider-capability, and paid-attempt gates before external generation.

## Execution rule

When the user explicitly requests a 2D-to-3D render, begin the reconstruction analysis automatically.
Generate only views fully supported by the supplied evidence and the approved attempt count. If the
upload has no stated deliverable, use the interactive project menu and do not spend credits.

If a requested view is only partly supported, do one of the following:

1. request the missing elevation, section, dimension, material schedule, or reference image;
2. offer a clearly labeled schematic visualization that uses no invented architectural elements; or
3. provide a production-ready reconstruction brief instead of generating an inaccurate image.

Never describe an AI-generated reconstruction as dimensionally exact, BIM-authoritative, measured
documentation, or a substitute for the source model.

For a geometry-locked photorealistic interior or dollhouse request, use the full Floor plan to 3D
template in `templates.md` after completing the Source Coverage Matrix. Do not weaken its locks, and do
not fill its missing-information fields with unsupported assumptions.

## Output

Return:

1. **Source Read** — source IDs and drawing type;
2. **Locked Geometry** — elements that must remain unchanged;
3. **Source Coverage Matrix** — Documented, Derivable, Unknown, and Source required;
4. **Approved Views** — only evidence-supported views;
5. **Missing Information** — concise and specific;
6. **Rendering Brief or Generated Output** — focused on photorealism, materials only when documented
   or explicitly approved, lighting, camera, and visual quality; and
7. **Preservation Validation** — visible comparison against the supplied drawings.

Reject and do not deliver an output that changes documented geometry, scale, orientation, proportions,
dimensions, room positions, walls, openings, circulation, structural layout, floor count, annotations,
or design intent. Rendering may improve materials, lighting, furniture, vegetation, and image quality
only when those changes remain non-destructive and do not obscure or imply architectural changes.
