# Architectural Rendering Loop

Use this optional workflow only when the user explicitly requests the full rendering loop, complete
geometry validation, or an A-to-Z render pass. A simple render request remains a simple render.

## Sequence

1. Analyze every source and label consequential content Observed, Inferred, Unknown, or Source required.
2. Run the pre-render geometry gate: compare documented dimensions, footprint, levels, openings, grid,
   structure, stairs, and circulation. Stop on contradictions or missing locked facts; never auto-correct.
3. Classify elements:
   - **Locked** — documented; preserve exactly.
   - **Inferred** — visible but not dimensioned; label confidence and evidence.
   - **Source required** — undocumented; request the needed drawing or view.
   - **Optional** — non-architectural styling; default only within the approved scope.
4. Define materials with real-world scale and coordinated transitions.
5. Define natural and artificial lighting.
6. Build only cameras supported by supplied sources. Every unseen view requires a new source.
7. Validate composition, crop, aspect ratio, verticals, exposure, and subject clarity.
8. Add furniture and landscape only after geometry approval and without obscuring architecture.
9. Run the canonical preservation and visual-quality QA.
10. Sort corrections by geometry, materials, lighting, camera, furniture, landscape, and rendering.
11. Correct one category at a time while freezing already approved categories.
12. Stop at the approved paid-attempt limit and report unresolved failures.

True material-ID, object-ID, depth, shadow, or AO passes require a real 3D renderer and source scene.
Never fabricate them with an image model.

For the full loop, return source analysis, locked elements, missing information, geometry validation,
material and lighting decisions, supported camera list, approved renders, correction report, and final
preservation checklist. Use `board.py` only when a document is requested.
