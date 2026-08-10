# Automatic Reference Engine

Use this engine for every architectural, interior-design, FF&E, visualization, and presentation task.
Its priority is high within the creative workflow, but it never precedes or overrides `core-policies.md`,
source intake, privacy, provider-capability, professional-boundary, or paid-attempt gates.

## Configuration

```json
{
  "reference_engine": {
    "enabled": true,
    "priority": "high",
    "trigger": "automatic",
    "execution_order": "before_analysis",
    "description": "Automatically generate a complete architectural and interior design reference package before starting analysis, rendering, or documentation.",
    "generate": {
      "architectural_references": true,
      "interior_references": true,
      "furniture_references": true,
      "material_references": true,
      "lighting_references": true,
      "landscape_references": true,
      "facade_references": true,
      "bathroom_references": true,
      "kitchen_references": true,
      "bedroom_references": true,
      "living_room_references": true,
      "dining_room_references": true,
      "ceiling_references": true,
      "flooring_references": true,
      "wall_finish_references": true,
      "color_palette_references": true,
      "mood_board": true,
      "style_board": true
    },
    "reference_data": {
      "style": true,
      "design_language": true,
      "materials": true,
      "textures": true,
      "colors": true,
      "lighting": true,
      "furniture": true,
      "decor": true,
      "plants": true,
      "artwork": true,
      "fixtures": true,
      "hardware": true,
      "joinery": true,
      "brand_inspiration": true,
      "luxury_alternatives": true,
      "mid_range_alternatives": true,
      "budget_alternatives": true
    },
    "rules": [
      "Generate references before any rendering begins.",
      "Maintain one consistent architectural language.",
      "Match all references to the approved project style.",
      "Do not recommend conflicting styles.",
      "Explain why each reference was selected.",
      "Generate references for every room automatically.",
      "Reuse approved references consistently throughout the project."
    ]
  }
}
```

## Execution order

Interpret `before_analysis` as before creative design analysis, rendering, or documentation—not before
mandatory policy and source analysis. Execute in this order:

1. Read `core-policies.md`; identify the Master Reference, authoritative sources, privacy destination,
   provider availability, paid-attempt budget, and regulated-advice boundaries.
2. Inventory only evidence-supported project spaces, elements, typology, stage, and known design
   decisions. Mark missing or ambiguous project data `Unknown` or `Source required`.
3. Create one reference package covering only categories relevant to the detected project. A `true`
   category enables automatic consideration; it does not require filler, duplicate references, invented
   rooms, external searches, image generation, or paid calls.
4. Present the reference package as reversible proposals. Obtain approval before adding any proposal to
   the canonical Project Context or using it as a cross-project lock.
5. Reuse only approved references in subsequent prompts, renders, schedules, boards, and documents.

## Reference package schema

Use stable IDs and keep each retained reference decision-useful:

```text
Reference Package ID and revision:
Master Reference and authoritative sources:
Project style status: supplied | inferred | proposed | approved
Applicable rooms, zones, facades, or landscape areas:
Shared design language and continuity locks:
Reference ID and category:
Reference type: supplied asset | verified external source | precedent principle | generated proposal
Selected attributes: form, palette, material response, texture, lighting, furniture, detailing, or mood
Selection rationale and project relevance:
Allowed influence:
Prohibited influence and locked architecture:
Luxury, mid-range, and budget alternatives when relevant:
Source, link, date checked, region, and verification status:
Approval status: proposed | approved | rejected | superseded | requires verification
```

## Reference rules

- Preserve architecture first. A reference may influence only approved aesthetic and furnishing
  variables; it never authorizes changes to geometry, structure, dimensions, openings, circulation,
  ceiling heights, camera locks, or source-document content.
- Maintain one shared architectural and interior language. Resolve conflicts before downstream work;
  do not average incompatible styles.
- Explain why every retained reference was selected and which decision it supports. Remove semantic
  duplicates and categories irrelevant to the project.
- Generate a room-specific reference subset for every evidence-supported room or space while reusing
  the same approved project-level palette, material family, lighting language, furniture language, and
  detailing language.
- Treat furniture, materials, finishes, lighting, landscape, facade treatments, ceilings, joinery,
  decor, art, and brand inspiration as proposals unless the user or authoritative project source has
  approved them.
- Do not infer room functions, facade design, ceiling geometry, elevations, services, landscape, or
  unseen conditions from a plan alone. Produce a partial reference package and identify the missing
  source instead.
- Do not make external searches, uploads, image-generation calls, purchases, or paid calls merely
  because a category is enabled. Follow the normal authorization, privacy, provider, citation, and
  attempt-budget rules.
- Verify current product names, dimensions, finishes, availability, prices, certifications, and links
  with authoritative manufacturer or dealer sources. Otherwise label brand examples and alternatives
  `Unverified inspiration — confirm with manufacturer or dealer`.
- Mood boards and style boards must use real supplied, licensed, verified, or explicitly generated
  assets. Never fabricate product images, project photography, citations, or provenance.
- Record approved reference IDs in the canonical Project Context and continuity decision register.

## Minimum output

Before downstream creative work, provide or internally establish:

1. a project-level reference concept and selection rationale;
2. the applicable reference categories and omissions;
3. a deduplicated room/zone reference matrix;
4. material, color, lighting, furniture, decor, landscape, facade, ceiling, and finish references only
   where relevant and source-supported;
5. tiered alternatives where they add a real procurement or design decision;
6. mood-board and style-board specifications or artifacts when supported;
7. approval status, source traceability, conflicts, unknowns, and verification requirements.

