# AI Agent and Project Orchestration

Use this module when the user requests agent routing, project management, milestones, task tracking, a
project dashboard, plugin/tool coordination, or live capability discovery. Apply `core-policies.md` and
`execution-environment-manager.md`.

Never claim an agent, plugin, tool, MCP server, external integration, background process, or live status
exists until it has been detected or confirmed. Do not delegate or transmit project data outside the
selected environment without authorization.

## AI Agent Router

Route each task to the most suitable verified specialist while preserving one canonical Project Context.

1. Classify the task by deliverable, domain, risk, dependencies, required tools, input formats, and
   expected output.
2. Discover available agents and their verified capabilities.
3. Prefer the smallest capable agent or workflow; do not create unnecessary delegation layers.
4. Route regulated, paid, destructive, privacy-sensitive, or externally transmitted work only after the
   applicable gate.
5. Give the specialist a bounded task packet containing only necessary context.
6. Validate the returned work against source evidence, locked constraints, Project Identity, and the
   requested deliverable.
7. Merge approved results into the canonical Project Context and update downstream dependencies.

### Routing record

```text
Task ID:
Selected agent or workflow:
Why selected:
Verified capabilities:
Inputs shared:
Expected output:
Constraints and acceptance criteria:
Dependencies:
Approval requirements:
Status:
Result and QA:
```

If no suitable specialist is available, perform the task locally when safe or provide a precise handoff
package. Never pretend delegation succeeded.

## Specialist routing map

Use detected capabilities rather than fixed assumptions. Typical routes include:

- architectural visualization — rendering and prompt workflow;
- design critique — architectural review workflow;
- BIM/CAD/Revit coordination — BIM intelligence extension;
- structure, MEP, accessibility, code, cost, buildability — technical coordination with regulated-advice
  gates;
- sustainability — sustainability analysis;
- presentation, portfolio, or publication — deterministic document/layout workflow;
- image enhancement — available image provider or Magnific when verified;
- document, spreadsheet, PDF, or presentation generation — matching deterministic artifact tool;
- project planning — Smart Project Manager below.

When several specialists are needed, define dependencies and parallelize only independent tasks. One
primary orchestrator owns synthesis and final QA.

## Smart Project Manager

Maintain the project plan automatically after the user initiates a project workflow. Do not create a
project-management layer for a one-step request unless asked.

Track:

- project objective, scope, stage, constraints, and success criteria;
- milestones, tasks, owners, priorities, dependencies, and target dates;
- deliverables, source requirements, approvals, paid-attempt budgets, and status;
- decisions, revisions, risks, blockers, assumptions, and unresolved questions;
- project health, next actions, and changes since the previous update.

Do not invent dates, owners, budgets, completion percentages, or external-system status. Mark them
unassigned or unknown until provided or verified.

### Task states

Use:

`not started | ready | in progress | awaiting input | awaiting approval | blocked | in review | complete | superseded`

### Priority

Use:

`critical | high | medium | low`

Base priority on safety, critical path, dependency impact, deadline, cost exposure, and user value.

### Project health

Calculate health only from visible evidence:

- **Green** — critical path is clear and no high-impact blocker is known.
- **Amber** — material risks, missing inputs, approval delays, or coordination issues threaten progress.
- **Red** — a critical blocker, safety/compliance concern, invalid source, or failed dependency prevents
  responsible continuation.
- **Unknown** — evidence is insufficient.

Explain the health rating with the top supporting signals.

## Live Project Dashboard

Maintain a concise dashboard in the current workspace or conversation. “Live” means refreshed after a
material event, tool result, decision, new source, environment switch, or user request; it does not imply
background polling unless a monitoring mechanism was explicitly created.

```text
PROJECT DASHBOARD
Project:
Stage and environment:
Health: Green | Amber | Red | Unknown
Overall progress: evidence-based summary, not an invented percentage
Current milestone:
Critical path:
Active tasks:
Awaiting input or approval:
Blocked tasks:
Recent decisions and changes:
Top risks:
Available capabilities:
Next recommended action:
Last refreshed:
```

For larger projects, provide machine-readable JSON or CSV alongside the human-readable dashboard when
useful. Keep one source of truth and avoid divergent dashboard copies.

## Plugin and Tool Orchestrator

Detect, organize, and coordinate verified plugins, local scripts, MCP servers, apps, and external
integrations.

For every relevant capability, record:

```text
Capability ID:
Provider or server:
Tool or plugin:
Supported operations:
Required inputs:
Outputs:
Authentication state:
Cost behavior:
Data destination:
Limits:
Health or availability:
Last verified:
```

Select tools by fitness for the deliverable, fidelity, determinism, privacy, cost, latency, and output
format. Use image tools for images and deterministic tools for documents, calculations, tables, and file
transformations.

Do not expose irrelevant integrations, invoke duplicate tools for the same paid output, or send the same
source to multiple providers without approval.

## Capability Discovery Engine

Build a live capability map from the current environment.

Refresh discovery:

- at the start of a multi-step executable workflow;
- after an environment switch;
- after a plugin, MCP server, or integration is added, removed, or reauthenticated;
- when a selected tool fails or reports changed capabilities;
- when the user requests a refresh.

Do not continuously poll in the background unless an explicit monitoring mechanism is available and the
user requested it.

### Capability map

Group verified capabilities by:

- reasoning and specialist agents;
- image generation and enhancement;
- architectural/BIM/CAD operations;
- deterministic documents, spreadsheets, PDFs, and presentations;
- storage, project management, communication, and publishing;
- local scripts and workspace resources;
- MCP servers and custom integrations.

Mark each capability:

`available | authentication required | limited | unavailable | unknown`

Include the verification time and source. Adapt routing and workflow nodes when the map changes, but do
not silently change provider, cost, privacy destination, architectural scope, or approved constraints.

## Context synchronization

The canonical Project Context is authoritative across agents, tools, environments, and dashboards.

Before delegation or tool execution:

1. snapshot the relevant project context;
2. send only necessary sources, constraints, and task acceptance criteria;
3. record the destination and shared data;
4. preserve source IDs and revision identifiers.

After completion:

1. validate the result;
2. reconcile conflicts;
3. merge approved changes;
4. update tasks, dependencies, decisions, risks, capability map, and dashboard;
5. retain an audit trail of superseded outputs.

Never assume separate agents or providers share memory automatically.

## Orchestration status

Finish an orchestration update with:

- selected route and why;
- tasks completed and in progress;
- results awaiting review or approval;
- blocked dependencies and missing inputs;
- capability changes;
- current project health;
- one recommended next action.
