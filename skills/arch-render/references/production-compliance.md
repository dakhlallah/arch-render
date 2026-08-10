# Production Compliance and External Integrations

Use this module for every external provider, authenticated tool, public release, or submission review.
This file is an operational gate, not a substitute for a published privacy policy or provider contract.

## Release blockers

Do not describe the public plugin or ChatGPT app as production ready until all items below are verified:

- a public HTTPS privacy policy states data categories, purposes, recipients, provider-specific retention,
  deletion controls, and privacy/support contacts;
- every external provider is authorized and its terms permit the integration;
- exact MCP tool names, descriptions, input/output schemas, and annotations are captured and tested;
- authenticated integrations have minimal scopes, revocation behavior, and reviewer test credentials;
- paid generation is idempotent or uses one POST per approved attempt with ambiguous-status recovery;
- security tests cover SSRF, redirects, private IPs, oversized responses, invalid content types, expired
  authentication, rate limits, outages, and provider schema changes;
- data retention, logging, telemetry, subprocessors, incident response, and deletion are documented;
- the public submission metadata is accurate and does not overstate capabilities or readiness.

Never invent missing provider terms, schemas, scopes, retention periods, authorization, credentials, or
review evidence. Mark them `Release blocker — provider evidence required`.

## External-provider disclosure

Before sending project data outside the current environment, disclose:

```text
Provider:
Files and fields to be sent:
Purpose:
Paid operation and maximum attempts:
Destination project or folder:
Retention and deletion: verified terms | unknown
Confidential-data warning:
```

Obtain confirmation when the initial request did not already authorize those specific files, provider,
purpose, and paid-attempt limit. Redact unnecessary title blocks, names, addresses, and identifiers when
the user approves redaction. Never request or transmit passwords, API keys, payment-card data, government
identifiers, protected health information, or authentication secrets through prompts or tool arguments.

## Paid attempt and retry policy

One user-approved generation equals one outbound generation POST. Do not automatically retry after a
connection drop, timeout, HTTP 429, or HTTP 5xx unless the provider documents that the operation was not
accepted or supports a verified idempotency key.

After an ambiguous failure, report:

> Generation status is unknown. The provider may have accepted the request. No retry was made to avoid
> a duplicate charge. Check provider history or authorize one additional attempt.

Poll an existing creation identifier instead of resubmitting whenever possible. Count every outbound
generation POST against the approved attempt budget.

## MCP tool review contract

For every external MCP tool, verify and record:

- unique verb-led name and accurate description;
- minimal task-specific input schema and minimized response schema;
- authentication and scopes;
- transmitted data and provider destination;
- user-visible side effects and paid behavior;
- retry, idempotency, cancellation, and recovery semantics;
- `readOnlyHint`, `destructiveHint`, and `openWorldHint` annotations;
- representative success, refusal, authentication, rate-limit, timeout, and provider-error responses.

Reject execution when a tool schema or consequential annotation is unavailable or has changed
incompatibly. Configuration alone does not verify a tool.

Do not return session IDs, trace IDs, request IDs, timestamps, or internal logging metadata unless they
are strictly required for the user to retrieve, resume, audit, or support the requested job.

## Authentication and permissions

Use platform-managed authentication when available. Request only scopes necessary for user-visible
features. Tokens must never appear in prompts, logs, files, output, or error messages. Disconnecting the
provider must prevent future calls and revoke access when the provider supports revocation.

For public review of an authenticated integration, provide a fully featured demo account with sample
data. Do not require the reviewer to create an account, provide payment details, or complete inaccessible
two-factor authentication.

## Job monitoring and recovery

Use provider-documented polling limits. When none are documented, poll no more frequently than every
five seconds and no more than sixty times. When the limit is reached, stop polling, report the last
verified status, and offer a later status check. Never resubmit the job automatically.

If cancellation is available, explain whether credits may still be consumed before requesting
confirmation. Never claim cancellation until the provider confirms it. On authentication expiry, pause
and request reauthentication without discarding a verified creation identifier.

## Privacy-policy publication template

Before public submission, publish a legally reviewed policy on an HTTPS URL containing at least:

```text
Data processed: architectural files, prompts, project metadata, and only task-required fields.
Purpose: the explicitly requested architectural workflow.
Recipients: each provider that may receive data, named individually.
Retention: exact provider-specific and developer-specific periods.
Controls: cancel, omit, redact, disconnect, export, and request deletion.
Restricted data: credentials, payment data, government identifiers, and PHI are not accepted.
Security, privacy contact, support contact, effective date, and change-notice process.
```

This template is not a published policy. Keep public-release status blocked until the final URL and
provider-specific facts are verified.
