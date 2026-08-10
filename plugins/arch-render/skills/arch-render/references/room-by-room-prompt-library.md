# Room-by-Room Floor-Plan Prompt Library

Use this workflow automatically when a bare uploaded architectural source is confidently classified as
a 2D floor plan. Also use it when the user requests separate prompts for each room or space. Generate
text prompts only; do not make paid image calls without separate authorization.

## Source coverage and preservation

Read `2d-to-3d-reconstruction.md` and `core-policies.md`. Treat the plan as the Master Reference and lock
all documented dimensions, room boundaries, wall locations and thicknesses, columns, doors, windows,
openings, stairs, level relationships, balconies, fixed fixtures, and circulation.

Do not infer a room function from furniture alone when the label is absent or ambiguous. Use
`Unlabeled space <ID> — function requires verification`. Do not invent ceiling height, window height,
door height, facade appearance, structure, services, materials, furniture, or decor. Treat missing
vertical or aesthetic information as `Source required` or as an explicitly labeled reversible proposal.

AI imagery cannot guarantee exact dimensional fidelity. The prompt must demand preservation, but the
delivery must not claim that a generated image is measured proof or a substitute for CAD/BIM and a
deterministic renderer.

## Automatic workflow

1. Confirm the source is a floor plan and record filename, sheet/view, revision, scale, units, level,
   orientation, and legibility when available.
2. Detect every distinct evidence-supported space, including living areas, kitchens, bedrooms,
   bathrooms, toilets, corridors, halls, stairs, balconies, terraces, storage, utility rooms, closets,
   lobbies, and other labeled or enclosed spaces.
3. Assign stable IDs such as `L01-R01`, `L01-R02`, and `L01-C01`. Do not merge spaces with different
   boundaries or duplicate the same space because it has multiple labels.
4. Build a space inventory before writing prompts:

```text
Space ID | source label | normalized name | boundary confidence | documented dimensions |
doors/openings | windows | fixed elements | adjacent spaces | unknowns | source location
```

5. Flag ambiguous boundaries, illegible labels, conflicting dimensions, open-plan zones, double-height
   relationships, stairs, shafts, and exterior spaces. Continue with unaffected spaces; request
   clarification only for facts that block a responsible prompt.
6. Lock one whole-project Interior Identity before the first room prompt. Reuse it across every space:

```text
Architectural language:
Material family:
Color palette:
Lighting language:
Furniture language:
Detailing language:
Camera language:
Photorealism and color grade:
Variables marked as reversible proposals:
```

7. Generate exactly one separate, copy-ready prompt per detected space. If the library is long, deliver
   numbered parts while preserving the complete index and stable IDs.
8. Apply `furniture-styling-object-curation.md` to create the matching room-level FF&E packages. Keep
   proposed objects subordinate to geometry, circulation, openings, and required clearances.
9. Finish with a Prompt Index, unresolved source requirements, and a preservation checklist.

## Room prompt contents

Every prompt must appear in its own Markdown code block and include:

- space ID, source label, plan source, and adjacency context;
- explicit geometry, dimensions, walls, openings, fixed elements, and circulation locks supported by
  the plan;
- a camera position and direction located inside the documented room footprint, with a realistic
  full-frame-equivalent lens chosen through `architectural-camera-director.md`;
- camera height, level horizon, straight verticals, composition, and focal point;
- intentional lighting supported by documented openings, with missing vertical information disclosed;
- materials, palette, furniture, and decor as reversible visualization proposals when unspecified;
- clearance and circulation protection so furniture never changes or obstructs architecture;
- the shared Interior Identity verbatim;
- a negative prompt prohibiting changed geometry, moved or missing walls, altered openings, invented
  doors/windows, wrong room proportions, changed circulation, fisheye distortion, warped structure,
  impossible furniture, artifacts, pseudo-text, dimensions, logos, and watermarks;
- a confidence score and concise list of Unknown or Source required items.

Do not create a camera that sees through walls or reveals undocumented adjacent rooms, facades, ceiling
conditions, or exterior context. A plan-supported camera is a proposed visualization viewpoint, not an
existing approved camera. When a room is too small for an honest interior camera, produce a restrained
wide or doorway-supported prompt, or mark the view Source required rather than using a fisheye lens.

## Output order

```text
FLOOR-PLAN SOURCE AND LIMITATIONS
SPACE INVENTORY
WHOLE-PROJECT INTERIOR IDENTITY
ROOM PROMPTS — one code block per Space ID
PROMPT INDEX
UNRESOLVED SOURCE REQUIREMENTS
PRESERVATION CHECKLIST
```

## User-approved prompt

Use this wording verbatim when the user requests the compact room-library prompt:

```text
When a 2D architectural floor plan is uploaded, automatically detect every individual space. Then, generate a separate professional AI prompt for each space, living room, kitchen, each bedroom, each bathroom, corridor, staircase, balcony, and so on, without changing any dimensions or wall locations. For each room prompt, include camera angle, lens, lighting style, materials, color palette, furniture suggestions, decor style, negative prompts, while strictly preserving the exact room geometry from the plan. Generate the full set automatically, so the user receives a complete prompt library room by room without asking. Maintain a coherent architectural style across all spaces.
```
