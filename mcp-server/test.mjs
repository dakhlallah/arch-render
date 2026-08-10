import assert from "node:assert/strict";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { InMemoryTransport } from "@modelcontextprotocol/sdk/inMemory.js";
import { createArchRenderServer } from "./server.mjs";

const server = createArchRenderServer();
const client = new Client({ name: "arch-render-test", version: "0.1.0" });
const [clientTransport, serverTransport] = InMemoryTransport.createLinkedPair();
await Promise.all([server.connect(serverTransport), client.connect(clientTransport)]);

const listed = await client.listTools();
const names = listed.tools.map((tool) => tool.name).sort();
assert.deepEqual(names, ["build_preservation_brief", "fetch", "generate_prompt_pack", "get_capabilities", "search", "validate_preservation"]);
for (const tool of listed.tools) {
  assert.equal(tool.annotations?.readOnlyHint, true);
  assert.equal(tool.annotations?.destructiveHint, false);
  assert.equal(tool.annotations?.openWorldHint, false);
}

const capabilities = await client.callTool({ name: "get_capabilities", arguments: {} });
assert.equal(capabilities.structuredContent.serverVersion, "0.1.0");

const search = await client.callTool({ name: "search", arguments: { query: "floor plan preservation" } });
assert.ok(search.structuredContent.results.length > 0);
const documentId = search.structuredContent.results[0].id;
const fetched = await client.callTool({ name: "fetch", arguments: { id: documentId } });
assert.equal(fetched.structuredContent.id, documentId);

const brief = await client.callTool({ name: "build_preservation_brief", arguments: {
  projectTitle: "Test project", sourceType: "plan", intent: "Prepare an exact 3D reconstruction",
  observedFacts: ["Two bedrooms", "North arrow visible"], unknowns: ["Ceiling height"], authorizedChanges: [],
} });
assert.equal(brief.structuredContent.mode, "Strict Preservation");

const pack = await client.callTool({ name: "generate_prompt_pack", arguments: {
  projectSummary: "Two-bedroom apartment plan", sourceFacts: ["Two bedrooms"], task: "2d-to-3d", platform: "universal", count: 2,
} });
assert.equal(pack.structuredContent.prompts.length, 2);
assert.equal(pack.structuredContent.paidAttempts, 0);

const validation = await client.callTool({ name: "validate_preservation", arguments: { checks: [
  { category: "floor-count", status: "pass", evidence: "Matches source sheet A-101" },
  { category: "openings", status: "fail", evidence: "One window was added" },
] } });
assert.equal(validation.structuredContent.decision, "block");

await client.close();
await server.close();
console.log("arch-render MCP contract tests passed");
