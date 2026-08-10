# Portfolio Content Generator

Use this module when the user requests an architectural portfolio, competition booklet, publication,
project monograph, editorial case study, or a complete set of portfolio pages. Apply
`core-policies.md`, `output-deliverables-standards.md`, `project-continuity-storytelling.md`,
`project-stages.md`, and the matching typology file.

## Operating contract

Automatically curate a complete, professional portfolio from the available project evidence. Create
only sections that support the portfolio's purpose, audience, project type, stage, and source coverage.
Never insert a section merely to make the document longer.

Do not invent drawings, dimensions, analysis results, project facts, client requirements, credits,
awards, performance data, construction details, specifications, quantities, or unseen architecture.
When a valuable section lacks evidence, mark it `Source required`, identify the exact missing asset,
and omit it from the issued document until supplied. A placeholder may appear only in a clearly labeled
working draft.

If the user supplied enough information, begin without asking which pages to create. Ask one concise,
grouped question only when the audience, output format, confidentiality, portfolio ownership, or a
missing authoritative source materially blocks responsible production.

## 1. Establish the publication brief

Record:

```text
Portfolio ID and revision:
Project title, type, location, stage, and status:
Purpose: client | competition | publication | academic | recruitment | presentation
Audience and decision:
Author, collaborators, client, and approved credits:
Format: screen | print | both
Page size, orientation, binding, and target page count:
Brand system and supplied fonts/logos:
Authoritative source set and revision:
Confidentiality and permitted publication scope:
Deadline and delivery formats:
```

Do not assume permission to publish confidential project material. Do not fabricate missing credits or
copyright permissions.

## 2. Build the source and section register

Inventory every supplied drawing, model view, diagram, photograph, render, schedule, specification,
text source, and approved project decision. Assign stable asset IDs and record filename, revision,
source, rights/status, resolution, orientation, and usable page scale.

Evaluate every candidate section as:

- `Include` — relevant and supported by authoritative sources;
- `Include as proposal` — requested editorial or design content, clearly separate from approved facts;
- `Source required` — valuable but blocked by a named missing asset or decision;
- `Not applicable` — unrelated to this project, typology, stage, or audience;
- `Excluded` — intentionally omitted for confidentiality, repetition, weak evidence, or page-budget fit.

The issued table of contents must contain only `Include` and explicitly approved `Include as proposal`
sections. Never print a long menu of unavailable sections as though they were deliverables.

## 3. Candidate section library

Select from the following library; combine closely related items when that improves editorial flow.

### Front matter and narrative

Cover; Table of Contents; Project Overview; Executive Summary; Project Brief; Client Brief; Design
Vision; Design Concept; Design Philosophy; Final Presentation; Conclusion.

### Site, environment, and access

Site Analysis; Site Context; Site Constraints; Climate Analysis; Sun Path; Wind Analysis;
Accessibility; Master Plan; Site Plan; Water Management; Landscape Strategy; Landscape Planting.

### Program, organization, and circulation

Space Allocation; Space Program; Bubble Diagram; Adjacency Diagram; Functional Zoning; Circulation
Diagram; Ground Floor Plan; Basement Plan; Typical Floor Plan; Roof Plan; Isometric Plan; Room
Isometric.

### Form, concept, and development

Massing Development; Design Evolution; Volume Diagram; Concept Development; Design Process; Process
Sketches; Design Iterations; Axonometric View; Exploded Isometric; 3D Exploded View; Virtual Model.

### Technical design and documentation

Grid System; Structural Grid; Structural Strategy; Sections; Elevations; Section and Elevation
Composition; Facade Design; Facade Detailing; Wall Sections; Construction Details; Canopy Design;
Construction Sequence; Technical Specifications; BOQ Summary.

### Courtyard study

Courtyard Design; Courtyard Plan; Courtyard Section; Courtyard Detail; Courtyard Process; Courtyard
Sketch; Courtyard Model; Courtyard Interior Perspective; Courtyard Exterior Perspective.

Include a courtyard chapter only when a courtyard is an evidenced or explicitly authorized project
feature. Treat it as one coherent chapter rather than nine automatic pages.

### Interiors, materials, FF&E, and lighting

Interior Perspectives; Material Palette; Material Specifications; Furniture Board; FF&E Schedule;
Lighting Concept; Lighting Layout; Ceiling Plan; Floor Finish Plan; Joinery Details; Door Schedule;
Window Schedule.

### Experience, visualization, and closure

Exterior Perspectives; Render Gallery; Hero Render; Detail Render; Human Experience; Sustainability
Strategy.

## 4. Specialized chapter routing

Load a specialized chapter only when it is identified by the user or supported by project sources:

- Slope House;
- Courtyard House;
- Fold House;
- Study Utopia;
- Pavilion;
- Villa;
- Residential;
- Commercial;
- Hospitality;
- Mixed Use;
- Office;
- Educational;
- Healthcare;
- Competition Project.

Treat named concepts such as `Fold House` or `Study Utopia` as project-specific labels, not generic
facts. Preserve the user's approved spelling and meaning. For recognized typologies, load only the
matching file under `typologies/` and keep professional-boundary requirements visible.

## 5. Generate a section card

For every included section, generate:

```text
Section ID and status:
Professional title:
Editorial role and short description:
Source assets and revisions:
Recommended drawings:
Recommended diagrams:
Recommended renders or photographs:
Recommended annotations and legends:
Recommended graphic devices:
Page count and sequence position:
Recommended page layout and grid span:
Suggested image dimensions and minimum effective resolution:
Caption text with source/status:
Design notes and narrative link:
Missing inputs or verification:
```

Recommendations are production instructions, not claims that assets already exist. If an item is not
supported, omit it or label it `Source required`.

## 6. Editorial system

Define one portfolio-wide system before laying out pages:

- page size, orientation, bleed, safe area, margins, columns, gutters, and baseline grid;
- primary and secondary typefaces, type scale, line length, hierarchy, and caption style;
- restrained palette, background, rules, legends, numbering, and annotation conventions;
- spacing tokens, alignment logic, image-crop policy, folios, section openers, and running headers;
- drawing line-weight hierarchy, scale-bar and north-arrow rules, diagram key, and status labeling;
- image treatment, color-management target, print profile when known, and accessibility contrast;
- cover, contents, opener, narrative spread, technical spread, gallery, schedule, and closing templates.

Maintain consistent typography, spacing, margins, grids, captions, and visual hierarchy across the
whole document. Allow intentional variation only to support narrative emphasis, not decorative noise.
Do not imitate or falsely attribute a living firm's proprietary identity. Aim for premium international
editorial quality using original composition.

Calculate image requirements from physical placement and output use. For print, state target effective
PPI and required pixel dimensions; for screen, state displayed pixel dimensions and export scale. Never
label an image 4K, print-ready, or high resolution without checking its actual pixels and intended size.

## 7. Narrative and page architecture

Organize the selected content into a clear sequence:

1. identity and project promise;
2. brief, context, and constraints;
3. concept, program, and form development;
4. spatial organization and architectural resolution;
5. technical, environmental, material, and experiential evidence;
6. final visual synthesis, outcomes, and conclusion.

Remove duplicate drawings, near-identical renders, repeated captions, and diagrams with no new decision
value. Use hero imagery sparingly. Balance plans, sections, diagrams, text, detail, and human experience
according to the audience and project stage.

## 8. Production workflow

1. Create the publication brief, source register, and section decision matrix.
2. Produce the curated table of contents and page budget.
3. Generate section cards and a spread-by-spread storyboard.
4. Draft evidence-supported titles, summaries, captions, labels, and design notes.
5. Place real supplied or approved assets with deterministic document or presentation tools. Use
   `scripts/board.py` for compatible HTML boards; use an available document, slide, or PDF workflow for
   longer portfolios.
6. Generate new diagrams or renders only when explicitly authorized, evidence-supported, and within the
   approved external-call and attempt budget.
7. Export the requested formats and visually inspect every page or spread.
8. Deliver the portfolio with an asset manifest, missing-source register, and QA summary.

If native layout production is unavailable, deliver the complete editorial specification, copy deck,
section cards, storyboard, asset register, and handoff package. Never claim that a PDF, InDesign file,
slide deck, or board was created unless the file exists and has been inspected.

## 9. Portfolio QA

Before delivery verify:

- every page is relevant to the purpose, audience, project type, and stage;
- all facts, drawings, diagrams, renders, photographs, captions, and credits are traceable;
- no missing or invented architectural content is presented as complete;
- approved geometry, Design DNA, revisions, and proposal status remain intact;
- contents, folios, section numbering, drawing titles, scales, units, legends, and cross-references agree;
- typography, margins, grids, spacing, image treatment, and caption styles are consistent;
- raster assets meet the stated effective resolution and crops preserve essential content;
- technical and regulated material carries the correct verification boundary;
- confidential or unapproved material is excluded;
- the final file opens, pages render correctly, links work when applicable, and exports match the
  requested dimensions and color intent.

Conclude with `Delivered`, `Validation`, `Omitted or source-required sections`, and `Next production
steps`. A premium portfolio is a curated, evidence-based publication—not an automatically expanded list
of every possible architectural page.

## User-approved prompt

Use the user's supplied wording as the feature brief, but apply the evidence, relevance, privacy,
professional-boundary, and file-verification rules above. Preserve all listed section options as the
candidate library; do not treat them as mandatory output.
