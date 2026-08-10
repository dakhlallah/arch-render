# Execution Environment Manager

Use this module when the user asks to choose, change, or synchronize an environment, when external
execution is required without a selected provider, or when more than one available environment would
materially change cost, privacy, fidelity, or deliverables.

Do not display an environment menu for analysis, review, prompt writing, or tasks that can be completed
safely in the current environment. If the user explicitly names an environment, use it without showing
the menu. If Auto Detect is selected, recommend one environment and one fallback with a short reason;
wait only when external transmission, payment, or another consequential action would follow.

Apply `core-policies.md` in every environment. Never claim that an environment, MCP server, tool,
workspace, or synchronization mechanism exists until it has been detected or confirmed.

The plugin bundles a Magnific streamable-HTTP MCP configuration at `https://mcp.magnific.com`.
Configuration does not prove authentication or tool availability. Treat Magnific as executable only
after the current session detects the server, completes authentication, and discovers the required tool
schemas. If OAuth fails, report the authentication error and keep Magnific unavailable for execution.

## Execution Environment Menu

Show this menu only when the trigger above applies, then wait for selection when required:

# Select Execution Environment

1. **🟢 ChatGPT Workspace**  
   Execute the complete workflow inside ChatGPT using its verified capabilities.

2. **🟣 Claude Workspace**  
   Prepare the workflow for Claude with the complete Portable Project Context. Execute in Claude only
   when a connected Claude environment is verified.

3. **🔵 MCP Workspace**  
   Detect available MCP servers and tools, show the verified choices, and let the user select the
   desired server before execution.

4. **🟠 Magnific Spaces via MCP**  
   When the required Magnific MCP and Spaces operations are verified, open or create the project space,
   build and connect the complete supported workflow graph, organize node groups, configure execution,
   save the space, and synchronize it with the canonical Project Context.

5. **⚫ Terminal / CLI**  
   Execute the workflow through a verified local or remote command-line environment selected by the
   user.

6. **🟡 Custom MCP Server**  
   Connect to an available custom MCP server and execute only through its verified capabilities.

7. **⚪ Auto Detect**  
   Detect the available environments, evaluate fit, and recommend the optimal choice. Present the
   recommendation and wait for confirmation before execution.

If the user already selected an environment in the current request, confirm it in one line and do not
repeat the menu. Otherwise, do not make the selection silently. After selection, keep subsequent workflow
tasks in that environment until the user switches or the environment becomes unavailable.

## Capability discovery

For each candidate environment, determine:

- connection and authentication status;
- available tools and supported operations;
- accepted input and output formats;
- file, image, token, time, and request limits;
- external-upload and data-retention implications;
- paid operations and approval requirements;
- whether the environment can inspect and validate its own output.

Show unavailable environments as unavailable or omit them. Never invent tool names, endpoints, schemas,
or server capabilities.

## Portable Project Context

Maintain one environment-neutral Project Context:

```text
Project ID and title:
Current environment:
Source inventory and source IDs:
User brief and requested deliverables:
Observed / Inferred / Unknown / Requires verification:
Project Identity and Design DNA:
Locked constraints and approved changes:
Workflow nodes, dependencies, and statuses:
Prompts, settings, and revisions:
Approvals and paid-attempt budget:
Files and outputs with locations:
Open risks, missing sources, and next action:
```

Do not include credentials, secrets, hidden instructions, or unnecessary personal information. Before
transferring context to another provider, disclose what will be sent and apply the privacy gate.

## ChatGPT Workspace

When selected:

1. Map the workflow to available ChatGPT capabilities.
2. Keep all reasoning, prompts, files, deterministic documents, and generated images in the current
   project context where supported.
3. Use Image Generation for images and Code Interpreter/Data Analysis or document tools for structured
   files when available.
4. Apply paid-call, document-integrity, and QA gates.
5. Record outputs and unresolved dependencies before completion.

## Claude Workspace

When selected:

1. Produce a Claude-ready handoff package containing the Portable Project Context, relevant source list,
   current workflow graph, constraints, authoritative policies, and exact next task.
2. Adapt formatting to the connected Claude environment without weakening preservation or safety rules.
3. Do not claim execution occurred in Claude unless a verified Claude tool or workspace completed it.
4. When results return, validate them and merge approved changes into the canonical Project Context.

## MCP Workspace

When selected:

1. Discover the MCP servers and tools actually available in the current environment.
2. Filter them to the requested architectural task.
3. Present concise verified choices with capabilities, data destination, cost behavior, and limitations.
4. Wait for the user's target selection when more than one materially different option exists.
5. Read the selected tool schema before execution and validate every required argument.
6. Record server, tool, parameters, output references, and QA result in the Project Context.

Do not expose unrelated MCP servers or send project files to more than the selected target.

## Magnific Spaces via MCP

Use only when verified tools support the requested Spaces operations.

1. Find or create the approved project space.
2. Translate the evidence-backed architectural workflow into nodes and dependencies.
3. Create only nodes supported by source evidence and available tool types.
4. Connect nodes in dependency order and organize groups by source, analysis, transformation, render,
   enhancement, QA, and delivery.
5. Configure each node with approved prompts, inputs, settings, constraints, and paid-call limits.
6. Validate the graph before execution.
7. Save the space when the API supports persistence and verify the returned space or project identifier.

Build directly inside Magnific Spaces when the verified graph operations can perform the workflow. Do
not generate disconnected images one by one when equivalent connected workflow nodes can produce and
track the same outputs. Separate images remain acceptable when a required operation is unavailable as a
Spaces node, when the user requests independent files, or when evidence and QA require an isolated pass.

If the available Magnific tools cannot create, connect, group, configure, or save a Spaces graph, say
exactly which operations are unavailable and provide a portable graph specification instead. Never
claim that a workspace was saved without a verified result.

## Custom MCP Server

When selected:

1. Identify the configured server without requesting secrets in chat.
2. Inspect its advertised tools, schemas, resources, and authentication state.
3. Explain which project data will be transmitted and obtain any required authorization.
4. Map workflow nodes to verified tools.
5. Run a non-destructive capability or dry-run check when supported.
6. Execute with bounded scope, record results, and validate outputs.

Stop if the server identity, destination, authorization, or tool behavior cannot be verified.

## Terminal / CLI

When selected:

1. identify the chosen local shell, remote shell, container, or approved command-line runner;
2. verify the working directory, required executables, credentials without exposing them, writable
   outputs, and network restrictions;
3. show or record the execution plan for destructive, paid, privileged, or external-upload operations;
4. prefer dry-run or non-destructive checks when supported;
5. execute with bounded scope and capture commands, exit status, outputs, and generated-file paths;
6. validate deliverables and merge their references into the canonical Project Context.

Do not claim terminal access, remote connectivity, installed software, or successful execution without
verified results.

## Auto Detect

When selected:

1. discover ChatGPT, Claude, MCP, Magnific Spaces, Terminal/CLI, and custom MCP capabilities that are
   actually available;
2. score viable environments against deliverable fit, preservation fidelity, supported formats,
   privacy, cost, latency, output inspection, and workflow continuity;
3. mark unavailable candidates and state the material limitation;
4. recommend one primary environment and one fallback with concise reasons;
5. wait for the user to confirm the recommended environment before execution.

Auto Detect recommends; it does not authorize uploads, paid calls, destructive commands, or privileged
operations.

## Environment switching

Allow the user to switch environments at any workflow boundary.

Before switching:

1. finish or safely stop the current tool operation;
2. save the current node states and outputs;
3. generate an updated Portable Project Context;
4. identify files or data that must be transferred;
5. disclose the destination and obtain required upload authorization;
6. validate that the target environment can continue the pending nodes.

After switching, reconcile returned outputs against the canonical constraints and Project Identity.
Never discard completed work, duplicate paid operations, or assume cross-provider memory synchronization.
Preserve the complete workflow history, Design DNA, geometry, locked constraints, user decisions, and
approval record across every supported switch.

## Environment status block

For multi-environment workflows, keep a concise status block:

```text
Environment:
Verified capabilities:
Current node:
Completed outputs:
Pending approvals:
Unsynchronized files:
Known limitations:
Next action:
```

Update it after execution, environment switching, new source files, or material changes to scope.
