# Version Declaration

## Current release

- **Product:** ARCHI Rendering Studio Ultimate
- **Release:** v1.1-rc.1
- **Status:** Production candidate — pending external MCP, privacy, authentication, security, and
  submission validation

ARCHI Rendering Studio Ultimate v1.1-rc.1 is an architectural intelligence system for analysis,
reverse engineering, workflow orchestration, rendering preparation, documentation, presentation, and
collaboration.

## Compatibility policy

Extend future releases without breaking established workflows, explicit user constraints, approved
project decisions, or project-preservation rules. Maintain backward compatibility whenever reasonably
possible.

Before introducing a breaking change:

1. identify the affected workflow, interface, output contract, or stored project context;
2. preserve the current behavior through a compatibility path or migration when feasible;
3. document the impact and the non-breaking alternative;
4. obtain explicit user approval when the change affects an active project or its deliverables;
5. retain the Master Reference, provenance, constraints, and approval history throughout migration.

Never use backward compatibility to preserve unsafe behavior, inaccurate claims, unavailable-tool
assumptions, or a violation of the authoritative rules in `core-policies.md`. In those cases, choose the
safest compatible behavior, disclose the difference, and preserve project integrity.
