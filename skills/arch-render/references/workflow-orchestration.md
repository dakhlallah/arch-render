# Architectural workflow orchestration

Use this module when the user asks for a visual workflow, reverse engineering, Design DNA, a
reconstruction roadmap, a prompt pack, a project report, or an end-to-end architectural package.
Do not activate it for a simple render, prompt, review, or bare upload.

`core-policies.md` remains authoritative. A workflow may organize evidence and generate visual
representations, but it must not fabricate unseen architecture, technical drawings, measurements, or
professional sign-off.

## Detail modes

- **Quick Review** — observations, Design DNA, risks, and next action.
- **Standard** — connected workflow, component prompts, materials, lighting, and QA.
- **Expert** — dependencies, alternatives, multidisciplinary conflicts, confidence, and traceability.
- **Presentation Ready** — approved outputs arranged into a deterministic report or board.

Default to Standard. Use the smallest mode that satisfies the request.

## Interactive Project Navigation

Before starting project analysis beyond the automatic Prompt Pack, scan the supplied reference images,
drawings, and project files and build an intelligent project menu. The Prompt Pack is the initial
text-only source analysis and does not authorize workflow execution.

Present only detected or clearly relevant categories as selectable starting points, for example:

- Project overview and Design DNA
- Site and context
- Massing and proportions
- Plans, circulation, and program
- Facades, entrances, and openings
- Structure and technical coordination
- Materials and color palette
- Lighting
- Landscape
- Interiors and FF&E
- Camera, composition, and rendering
- Presentation and deliverables
- Full project analysis

Recommend one category based on the evidence, but wait for the user's selection. After selection,
analyze only that topic and build a dedicated workflow around it. Maintain the complete project evidence,
constraints, Project Identity, and prior decisions in the background.

Keep navigation available and current after every meaningful change. Allow:

- **Back** — return to the previous menu or node;
- **Switch topic** — preserve completed work and begin another category;
- **Expand** — add related categories and dependencies;
- **Full project** — merge relevant category workflows into an end-to-end plan.

When new files or instructions arrive, update the menu and dependencies without discarding approved
context. Do not repeat completed analysis unless the evidence or constraints changed.

## Workflow planning

1. Inventory every supplied source with a stable source ID.
2. Classify visible evidence as Observed, Inferred, Unknown, or Requires verification.
3. Extract the project's Design DNA:
   - architectural language and intent;
   - composition and proportion rules;
   - grids, modules, rhythms, and signature elements;
   - material, color, lighting, landscape, and camera language.
4. Identify relevant components and their dependencies.
5. Build only the nodes supported by the supplied evidence and requested deliverable.
6. Mark unsupported nodes `Source required`; never fill them with invention.
7. Present the workflow plan and paid-attempt count before generating images.

Recommended node order when supported:

`Sources -> Massing -> Grids -> Facade -> Entrances -> Openings -> Materials -> Lighting -> Landscape -> Interiors -> Camera -> Render -> QA -> Delivery`

Skip irrelevant nodes. Reorder only when dependencies require it.

## Node contract

Represent each node with:

```text
Node ID:
Purpose:
Source IDs and visible regions:
Inputs:
Observed:
Inferred with confidence:
Unknown / source required:
Locked constraints:
Output:
Dependencies:
Prompt or analysis:
QA checks:
Status: planned | awaiting approval | ready | complete | blocked
```

Every recommendation must trace back to a source ID, visible region, user instruction, or prior
approved node. Do not claim pixel-level region extraction unless the environment actually produced a
crop or annotation.

## Reverse engineering

Reverse engineering explains the visible design system; it does not recreate proprietary construction
documents or infer hidden geometry.

Analyze, when visible:

- design intent and hierarchy;
- proportions, grids, modules, and facade rhythm;
- likely construction logic, clearly labeled as inference;
- materials, junction language, and environmental response;
- spatial or circulation clues supported by plans or sections;
- inconsistencies, risks, and missing sources.

Explain what a component is, why it may be used, alternatives, advantages, disadvantages, and best
practices only when that depth helps the user.

## Multi-reference synthesis

For multiple images:

1. Assign a source ID to each image.
2. Identify agreement, disagreement, and unique evidence.
3. Never merge different projects or incompatible views silently.
4. Ask for clarification only when a conflict changes the intended output.
5. Create one Project Identity from user-approved common attributes.

## Prompt versions

Generate only the versions requested or needed:

- photorealistic rendering;
- concept visualization;
- presentation graphic;
- technical illustration based on supplied geometry;
- tool-specific image-generation prompt;
- construction-reference narrative, not fabricated construction documentation.

Version every prompt with node ID, revision, target platform, source IDs, locked constraints, and
approved changes. Maintain a concise revision log.

## Approval and revision controls

At consequential or paid milestones, offer:

- **Continue** — approve the node and proceed;
- **Modify** — revise constraints or output;
- **Skip** — omit the node and update dependencies;
- **Regenerate** — authorize another attempt under the paid-call policy.

Do not force approval after every text-only node. Gate only decisions that change scope, architecture,
cost, privacy exposure, or downstream dependencies.

## Multidisciplinary review

Load only relevant perspectives:

- architect — intent, hierarchy, space, facade, buildability;
- interior designer — ergonomics, materials, light, FF&E;
- landscape architect — ground plane, ecology, climate, maintenance;
- lighting designer — daylight, layers, glare, color temperature;
- structural coordinator — visible grid and load-path plausibility;
- visualization artist — composition, camera, realism, consistency.

Label structural and technical conclusions as coordination advice and apply the regulated-advice gate.
Summarize conflicts and opportunities rather than role-playing unnecessary specialists.

## Consistency and QA

Maintain a Project Identity containing approved geometry targets, source cameras, materials, palette,
lighting, landscape, style, and Design DNA. Compare each node against it.

Before delivery, check:

- node dependencies are satisfied;
- constraints and source traceability are intact;
- assumptions and confidence are visible;
- prompts do not contradict earlier approved nodes;
- render count matches approval;
- documents contain only real drawings and approved images;
- missing information is explicit;
- the final output matches the selected detail mode.

## Deliverables and export

Support Markdown, JSON, CSV, DOCX, PDF, presentation boards, prompt packs, revision logs, and rendering
packages only when the environment has an appropriate deterministic tool. Use `scripts/board.py` for
HTML boards. Use document, spreadsheet, PDF, or presentation tooling when available.

Never ask an image model to draw an entire document. A page may contain an approved image generated by
an image model, but titles, explanations, tables, real drawings, and layout must be produced
deterministically.

Suggested presentation sequence, including only supported pages:

1. Cover
2. Project summary and evidence inventory
3. Design DNA
4. Site analysis from supplied site data
5. Massing and composition
6. Supplied plans, sections, or elevations
7. Facade, openings, and materials
8. Lighting, landscape, and interiors
9. Approved render gallery
10. QA, uncertainties, and revision log
11. Master prompt and reconstruction roadmap

## Final workflow summary

Finish an orchestration request with:

- completed nodes;
- approved revisions;
- missing sources and blocked nodes;
- consistency or compliance risks;
- deliverables produced;
- one recommended next action.
