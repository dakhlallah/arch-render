# Arch Render MCP

The plugin includes a first-party, tool-only MCP server at `mcp-server/`. It exposes bounded
architectural intelligence without uploading files, spending credits, mutating projects, or calling
external providers.

## Tools

| Tool | Purpose |
|---|---|
| `get_capabilities` | Report supported local capabilities and explicit limitations. |
| `search` | Search the bundled Arch Render Markdown knowledge library. |
| `fetch` | Read one searched knowledge document by its safe relative identifier. |
| `build_preservation_brief` | Separate observed facts, authorized changes, locks, and unknowns before work begins. |
| `generate_prompt_pack` | Generate one to five preservation-first text prompts with confidence scores. |
| `validate_preservation` | Convert supplied QA evidence into a deterministic deliver-or-block decision. |

All tools declare `readOnlyHint: true`, `destructiveHint: false`, `openWorldHint: false`, and
`idempotentHint: true`. The server does not claim to inspect an image when it has only received text
observations. A `not-verifiable` check must remain disclosed; any recorded failure blocks delivery.

## Plugin transport

The plugin manifest starts the bundled server over stdio through `.mcp.json`. The production bundle is
`mcp-server/dist/server.mjs`, so users do not need to install Node packages after installing the plugin.

## Development and verification

From `mcp-server/`:

```bash
npm install --include=dev
npm run build
npm test
node --check dist/server.mjs
```

For local HTTP development:

```bash
npm run start:http
```

The default development endpoint is `http://127.0.0.1:8788/mcp`; `GET /` is a health check. Override
the bind address with `HOST` and `PORT`. Keep local development bound to loopback unless remote access
is intentionally configured.

## ChatGPT developer mode

ChatGPT requires a reachable HTTPS MCP endpoint. Run the HTTP transport behind a trusted HTTPS tunnel
or deploy the same bundled server on an HTTPS host, then add its `/mcp` URL in ChatGPT developer mode.
Do not expose the local endpoint directly to the public internet without transport security,
authentication where appropriate, rate limits, request limits, logging controls, and a privacy review.

## External providers

This MCP does not generate images, upload references, access Magnific, or perform paid calls. Magnific
remains a separate optional MCP integration and may be used only after its availability, authentication,
tool schemas, privacy terms, retention behavior, costs, and user authorization are verified. Never
describe an external provider as connected based only on configuration.
