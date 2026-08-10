# Autonomous Magnific MCP Execution Mode

Use this mode only when the user explicitly selects Magnific MCP execution and approves a bounded
execution plan. A file upload alone does not authorize external transmission or paid generation.

After activation, complete the approved pipeline autonomously without stopping after prompt generation
or asking which approved render to create first.

## Activation gate

Before the first external upload or billable call:

1. verify Magnific authentication and discover the current MCP tool schemas;
2. identify the exact source files that will be sent to Magnific;
3. analyze source coverage and exclude outputs that require invented architecture;
4. prepare the applicable Prompt Pack from `automatic-prompt-pack.md`;
5. present one concise execution plan containing output types, maximum generation count, maximum upscale
   count, 3D attempts if supported, estimated or simulated cost when available, destination project or
   folder, and privacy disclosure;
6. obtain explicit approval for that bounded plan.

Approval applies only to the listed files, outputs, tools, and attempt limits. Expanding the plan,
changing provider, transmitting additional files, or exceeding the approved attempts requires new
approval. Never interpret “autonomous” as unlimited spending or permission to ignore privacy and
preservation policies.

## Capability mapping

Use tool names only after schema discovery. Expected Magnific capabilities may include:

- `images_generate` — supported image generation or image-conditioned variation;
- `images_upscale` — approved final-image enhancement;
- `models3d_generate` — 3D generation only when advertised and supported by sufficient source evidence;
- `creations_wait` — bounded job polling;
- `creations_show` and `creations_get` — retrieve verified job state and results.

These names are expectations, not guaranteed APIs. If the connected server exposes different names or
schemas, map by verified capability. Never invent arguments, endpoints, IDs, or successful results.

## Autonomous execution sequence

Within the approved plan:

1. inventory and analyze the uploaded references;
2. lock geometry, floor count, structure, plans, elevations, sections, camera evidence, and Design DNA;
3. generate the relevant Prompt Pack;
4. create only evidence-supported exterior, interior, image-to-image, 2D-to-3D, material, color,
   lighting, camera, and presentation outputs included in the plan;
5. submit each job with stable Prompt and Output IDs;
6. monitor jobs using verified wait or status tools with bounded polling and timeouts;
7. retrieve outputs and validate them against the Master Reference;
8. upscale only approved images that passed preservation QA;
9. save verified assets to the approved Magnific project or folder when the API supports persistence;
10. return the generated assets, corresponding prompts, source traceability, and execution summary.

Prompts are intermediate artifacts in this mode. Do not stop after prompts when approved visual jobs
remain executable. Do stop when authentication fails, a tool is unavailable, the attempt budget is
exhausted, required source evidence is missing, preservation QA fails without an approved retry, or the
provider reports an unresolved error.

## Preservation and missing information

Apply `core-policies.md` without exception. Never modify or invent geometry, floor count, structure,
elevations, sections, plans, openings, circulation, or Design DNA. A plan alone does not authorize an
invented facade, roof, height, material system, or unseen interior.

When information is missing:

- skip or block the unsupported output;
- record the missing source precisely;
- continue with independent outputs that remain supported;
- never hide an omission by generating a plausible substitute.

Reject an output that drifts from the Master Reference. Run a corrective attempt only if it remains
inside the approved attempt budget; otherwise request authorization.

## Delivery

Return:

1. generated images and 3D assets that completed successfully;
2. the prompt paired with each asset;
3. provider creation IDs and saved project or folder references when available;
4. preservation-QA results;
5. failed, blocked, omitted, or source-required outputs;
6. actual attempts used versus approved limits; and
7. a concise execution summary with next steps.

Never claim the entire pipeline completed when any required stage is blocked or failed.
