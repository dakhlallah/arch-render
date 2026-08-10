# Automatic Prompt Pack Generator

Use this module only when the user explicitly requests a Prompt Pack, uploads architectural material
without stating an intent, or requests a multi-deliverable production workflow. When the user states a
specific intent, perform that task directly and generate only the prompt required for it.

Prompt generation is text-only and does not authorize image generation, external uploads, paid calls,
or architectural changes. Default to a compact pack of three to five high-confidence prompts. Expand
beyond five only when the user requests a comprehensive pack or approves a multi-deliverable plan. Do
not ask which prompt to create after the pack trigger is established.

## Applicability

Evaluate these prompt types and include every type supported by the uploaded evidence and likely project
workflow:

1. Master Architectural Prompt
2. Reverse Engineering Prompt
3. Image-to-Image Prompt
4. 2D Floor Plan to 3D Rendering Prompt
5. Exterior Rendering Prompt
6. Interior Rendering Prompt
7. Facade Enhancement Prompt
8. Material Proposal Prompt
9. Color Palette Proposal Prompt
10. Lighting Design Prompt
11. Camera Composition Prompt
12. Landscape Prompt
13. AI Upscaling Prompt
14. Magnific Prompt
15. Magnific Spaces Workflow Prompt
16. Reconstruction Blueprint Prompt
17. Rendering Optimization Prompt
18. Presentation Board Prompt
19. Documentation Prompt
20. Design Preservation Prompt

Generate only applicable prompts. Omit a prompt when the source does not support its task, the required
environment is unavailable, or producing it would require invented architecture. Record the omission in
the Prompt Index only when the missing prompt is reasonably expected from the source, using `Omitted —
<reason>`.

Magnific and Magnific Spaces prompts are applicable only when the user targets those platforms or their
capabilities are verified. A paste-ready Magnific prompt may still be supplied when the user explicitly
requests text for manual use, but never claim that the integration can execute.

## Preservation rules

Apply `core-policies.md` and the relevant source workflow. Preserve the original architecture exactly.
Never modify or invent geometry, floor count, plans, elevations, sections, structure, openings,
circulation, dimensions, camera evidence, or Design DNA.

If a prompt requires information that is absent, either:

1. omit the prompt and explain the missing source in the Prompt Index; or
2. include explicit placeholders such as `[SOURCE REQUIRED: north elevation]` when the prompt remains
   useful without guessing.

Proposal prompts for materials, colors, lighting, or landscape must use Preserve First, Propose Second.
Label them as separate non-destructive proposals and never represent them as the original design.

## Confidence scoring

Give every generated prompt an evidence-confidence score from 0 to 100:

- **90–100** — directly documented and complete;
- **70–89** — mostly documented with minor non-architectural unknowns;
- **40–69** — partially supported; the prompt contains explicit Source Required placeholders;
- **0–39** — do not generate the prompt; list it as omitted.

Confidence measures source support, not predicted image quality. State one short confidence reason.

## Output format

For each generated prompt, return exactly:

### `<number>. <Prompt title>`

**Confidence:** `<score>/100 — <short evidence reason>`

```text
<one complete, immediately reusable, paste-ready prompt>
```

Place every prompt in its own Markdown code block. Never merge multiple prompts into one block. Do not
put analysis, confidence, warnings, or source notes inside the prompt unless they are necessary execution
constraints.

Keep prompts internally consistent by reusing the same Project Identity, source IDs, locked geometry,
approved proposal set, and preservation clause. Adapt platform-specific prompts only to verified or
user-named platforms.

## Prompt Index

Finish with:

## Prompt Index

| # | Prompt | Purpose | Confidence | Status |
|---|---|---|---:|---|
| 1 | Master Architectural Prompt | ... | 94/100 | Generated |
| 5 | Exterior Rendering Prompt | ... | — | Omitted — exterior evidence missing |

List every generated prompt. Also list materially relevant omissions with the precise missing source or
capability. Do not pad the pack with irrelevant prompts merely to reach twenty items.

After the Prompt Index, the interactive project menu may be offered for further analysis or execution.
Do not require the user to choose a prompt before delivering the pack.
