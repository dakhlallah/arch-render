# Skill Self-Review and Optimization

Use this module before finalizing a substantial skill or plugin release, or when the user requests an
audit, cleanup, optimization, consolidation, conflict check, or production-readiness review.

The review is read-only by default. Never modify prompts, workflows, menus, references, scripts,
manifests, marketplace files, or installed copies as a result of the review without explicit user
approval for the proposed changes.

## Contents

1. Review scope
2. Review checks
3. Severity and confidence
4. Readiness scoring
5. Structured report
6. Optimization rules
7. Audit and optimization cycle
8. Completion gate
9. Approval gate
10. User-approved prompt

## Review scope

Inventory and inspect:

- skill metadata and trigger description;
- the main `SKILL.md` router and workflow precedence;
- core and specialist policies;
- menus, modes, approval gates, status terms, and output contracts;
- reference routing and cross-file links;
- scripts, schemas, limits, errors, and provider assumptions;
- plugin manifest, assets, marketplace entry, and optional integrations;
- evaluations, fixtures, test coverage, and validation commands;
- standalone, plugin, installed, and GPT-facing variants when they exist.

Record the reviewed version, paths, file count, and date. Distinguish verified findings from suspected
issues that require forward testing.

## Review checks

### Duplicates and overlaps

Identify:

- repeated rules expressed in multiple files;
- workflows or menus that serve the same intent;
- duplicated examples, templates, checklists, or output formats;
- modules whose responsibilities overlap without a clear precedence rule;
- standalone and packaged copies that have drifted.

Do not treat deliberate reinforcement of a safety-critical rule as a defect automatically. Recommend one
authoritative location plus concise references when that preserves compliance.

### Conflicts and ambiguity

Check for:

- contradictory routing or precedence;
- execute-now rules conflicting with approval, privacy, or capability gates;
- preservation rules conflicting with redesign or proposal modes;
- automatic retries conflicting with paid-attempt authorization;
- environment or agent claims exceeding detected capabilities;
- document generation conflicting with the prohibition on fabricated drawings;
- different names or definitions for the same state, mode, role, or deliverable;
- requirements that cannot all fit within a target platform's limits.

Quote or cite both conflicting locations precisely.

### Missing steps and capabilities

Check whether each workflow includes, when applicable:

1. trigger and scope;
2. evidence and source inventory;
3. capability and environment discovery;
4. privacy, authorization, and cost gates;
5. inputs, constraints, dependencies, and acceptance criteria;
6. execution or handoff;
7. validation and failure handling;
8. provenance and traceability;
9. delivery, status, and session summary;
10. tests and maintenance ownership.

Identify missing functionality separately from missing documentation or missing automated tests.

### Terminology consistency

Create a glossary of normative terms and flag variants, including:

- Master Reference;
- Project Context;
- Project Identity;
- Design DNA;
- Preserve, Proposal, and Redesign modes;
- source ID, node ID, revision, deliverable, environment, capability, approval, status, and QA.

Recommend one spelling, capitalization, and definition for each term.

### Performance and maintainability

Assess:

- main prompt length and context cost;
- progressive disclosure and reference size;
- deeply nested or brittle cross-references;
- provider-specific assumptions in general workflows;
- repeated capability discovery or unnecessary menus;
- unbounded input, output, iteration, or retry behavior;
- manual-only tests and duplicated release steps;
- versioning, cache invalidation, installation, and synchronization risk.

### Safety and reliability

Assess:

- prompt injection and untrusted project content;
- privacy and external data transmission;
- credentials and secrets;
- paid-call authorization;
- regulated professional advice;
- destructive actions and overwrites;
- fabricated evidence, citations, drawings, measurements, or completion claims;
- cross-agent, cross-tool, and cross-environment context drift.

## Severity and confidence

Assign each finding:

- **Severity:** Critical | High | Medium | Low
- **Confidence:** Confirmed | Likely | Needs testing
- **Type:** Duplicate | Conflict | Missing | Terminology | Performance | Reliability | Safety |
  Maintainability | UX

Prioritize by user harm, incorrect output risk, financial/privacy exposure, frequency, and maintenance
cost.

## Readiness scoring

Calculate an evidence-based score from 0 to 100. Do not choose a score impressionistically. Score each
category and cite the strongest evidence for deductions:

```text
Instruction hierarchy and conflict control: 15
Architectural accuracy, preservation, and evidence: 15
Safety, privacy, professional boundaries, and paid-call control: 15
Workflow completeness and failure recovery: 10
Tool, MCP, provider, and integration reliability: 10
UX, accessibility, and deliverable quality: 10
Performance and context efficiency: 10
Maintainability, modularity, and scalability: 10
Tests, validation, release, and observability: 5
Total: 100
```

Apply these caps:

- any unresolved Critical issue: maximum 59 and `Not production ready`;
- any unresolved High safety, privacy, paid-call, professional-boundary, data-loss, or fabricated-evidence
  issue: maximum 69;
- any other unresolved High issue: maximum 84;
- missing validation of packaged, standalone, installed, or GPT-facing variants when applicable:
  maximum 89;
- 95–100 requires no unresolved Critical or High findings, passing required validations, synchronized
  release copies, and evidence that core workflows and failure paths were tested.

Report both `Overall quality score` and `Production-readiness score`. Explain the difference when design
quality is strong but operational evidence, testing, deployment, or external integration remains weak.
Never inflate a score because the skill is large, polished, or feature-rich.

## Structured report

Use this format:

```text
SKILL SELF-REVIEW
Version and scope:
Files reviewed:
Validation status:

Executive summary:
Overall quality score (0–100):
Production-readiness score:
Readiness verdict: Not ready | Major remediation | Release candidate | Production ready

Strengths:
Weaknesses:
Remaining gaps:

Findings:
ID | Severity | Confidence | Type | Locations | Problem | Impact | Recommendation

Duplicate and overlap map:
Conflicting instructions:
Missing capabilities or steps:
Terminology inconsistencies:
Performance and maintainability opportunities:
Safety and reliability concerns:

Recommended simplifications and merges:
1. Proposal
   Exact locations
   Functionality preserved
   Risk and migration notes

Prioritized action plan:
High:
Medium:
Low:

Approval-required change set:
Files to change:
Exact intended edits:
Validation and rollback plan:

Post-optimization re-audit:
Previous score:
New score:
Resolved findings:
Remaining findings:
Completion gate status:
```

## Optimization rules

Recommend simplification only when it preserves full functionality, project integrity, safety, source
fidelity, and user-visible behavior. Prefer:

- one authoritative policy with short references elsewhere;
- one router with explicit precedence;
- conditional modules loaded only when needed;
- stable semantic identifiers instead of fragile section numbers;
- deterministic scripts for repeatable operations;
- executable tests for routing, safety, cost, and failure handling;
- one canonical source synchronized to packaged and installed variants.

Do not remove a feature merely to reduce prompt size. Explain how its behavior will remain available.

Strengthen unclear prompts by replacing vague absolutes with testable behavior, explicit prerequisites,
bounded outputs, truthful capability checks, failure handling, and acceptance criteria. Preserve the
user-approved verbatim prompt in one canonical location when exact reuse is required, while keeping the
operational policy accurate and non-conflicting.

## Audit and optimization cycle

Use this sequence for a final release audit:

1. **Inventory** — enumerate every in-scope module, prompt, router entry, script, tool, integration,
   asset, manifest, release copy, test, and validation command.
2. **Baseline audit** — inspect completeness, accuracy, consistency, hierarchy, logical flow, best
   practices, safety, reliability, UX, performance, scalability, and maintainability. Do not rely only on
   filenames or prior claims.
3. **Report and score** — produce the structured report, strengths, weaknesses, remaining gaps, exact
   change proposals, readiness scores, and caps.
4. **Approval** — obtain explicit approval for the proposed optimization change set. A direct request to
   apply named fixes or resolve the reported critical issues authorizes only those changes.
5. **Optimize** — merge overlapping sections, remove true duplication, strengthen ambiguous prompts,
   repair routing and terminology, improve progressive disclosure, and add missing tests or failure paths
   within the approved scope. Preserve safety-critical reinforcement and backward-compatible behavior.
6. **Validate** — run deterministic skill, plugin, schema, script, link, synchronization, installation,
   and representative workflow checks as applicable. Record failures; do not treat a successful syntax
   check as behavioral proof.
7. **Re-audit** — audit the modified artifacts independently against the same rubric, compare scores,
   confirm resolved findings, and list regressions or remaining gaps.
8. **Release decision** — mark production ready only if the completion gate passes.

Do not perform open-ended self-modification, silently broaden scope, remove user-visible capabilities,
weaken preservation or safety rules, change provider/privacy/cost behavior, edit external systems, or
install a release without the authorization required for those actions.

## Completion gate

Do not mark the skill, plugin, or release complete while any of these remain:

- an unresolved Critical issue;
- a broken or ambiguous instruction hierarchy that can bypass safety, privacy, preservation,
  professional-boundary, or paid-call rules;
- fabricated capability, evidence, completion, geometry, regulation, product, cost, or tool claims;
- failing required validation, broken cross-reference, missing manifest requirement, or unsynchronized
  canonical, packaged, standalone, installed, or GPT-facing copy;
- a destructive, credential, data-transmission, retry, or external-action path without an adequate gate;
- a critical workflow with no responsible failure or recovery behavior.

When a critical issue cannot be resolved within the authorized scope, set the status to `Not production
ready — blocked`, explain the exact blocker and required authority or evidence, and do not claim success.

## Approval gate

After presenting the report:

1. stop before editing;
2. ask the user which proposed change set to approve;
3. apply only approved changes;
4. preserve an unchanged source or reversible diff;
5. validate the skill, plugin, scripts, and installation;
6. report exactly what changed and what remains unresolved.

Silence, general praise, or a request for review does not authorize implementation. A direct request to
apply named recommendations does.

## User-approved prompt

Use this wording verbatim when the user requests the compact final-audit prompt:

```text
Final Skill Audit & Self-Optimization. Instruct the skill to audit every module and instruction for completeness, accuracy, consistency, logical flow, and best practices. Identify gaps, conflicts, weak spots, and redundancies. Merge overlapping sections, remove duplication, strengthen unclear prompts, and optimize structure for long-term maintainability and scalability. Provide a readiness score from zero to one hundred, summarize strengths, weaknesses, and remaining gaps, and propose final improvements. Do not mark the skill as complete until critical issues are resolved. The goal is a production-ready architectural co-pilot that operates like a world-class multidisciplinary practice.
```
