import { createServer as createHttpServer } from "node:http";
import { readFile, readdir } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import path from "node:path";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { z } from "zod";

const SERVER_VERSION = "0.1.0";
const here = path.dirname(fileURLToPath(import.meta.url));
const referenceRoot = path.resolve(here, "../skills/arch-render/references");
const MAX_QUERY = 200;
const MAX_TEXT = 12_000;
const MAX_RESULTS = 10;

const safeAnnotations = Object.freeze({
  readOnlyHint: true,
  destructiveHint: false,
  openWorldHint: false,
  idempotentHint: true,
});

function result(structuredContent, message) {
  return {
    structuredContent,
    content: [{ type: "text", text: message ?? JSON.stringify(structuredContent) }],
  };
}

function normalizeId(value) {
  const clean = String(value ?? "").replaceAll("\\", "/").replace(/^\/+/, "");
  if (!clean || clean.includes("..") || !/^[a-zA-Z0-9/_-]+\.md$/.test(clean)) {
    throw new Error("Invalid knowledge document id");
  }
  return clean;
}

async function listMarkdownFiles(dir = referenceRoot, prefix = "") {
  const entries = await readdir(dir, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    if (entry.name.startsWith(".")) continue;
    const relative = prefix ? `${prefix}/${entry.name}` : entry.name;
    const absolute = path.join(dir, entry.name);
    if (entry.isDirectory()) files.push(...await listMarkdownFiles(absolute, relative));
    else if (entry.isFile() && entry.name.endsWith(".md")) files.push(relative);
  }
  return files.sort();
}

async function readKnowledge(id) {
  const normalized = normalizeId(id);
  const absolute = path.resolve(referenceRoot, normalized);
  if (!absolute.startsWith(referenceRoot + path.sep)) throw new Error("Document outside knowledge root");
  const text = await readFile(absolute, "utf8");
  return { id: normalized, title: normalized.replace(/\.md$/, "").replaceAll("/", " / "), text };
}

function createPrompt({ projectSummary, sourceFacts, task, platform, count }) {
  const facts = sourceFacts.map((item) => `- ${item}`).join("\n");
  const platformClause = platform === "universal" ? "Use platform-neutral natural language." : `Optimize syntax for ${platform}.`;
  const base = [
    "Treat the supplied project sources as the Master Reference.",
    `Project summary: ${projectSummary}`,
    "Observed source facts:",
    facts || "- No source facts supplied; mark all project-specific details Source required.",
    `Requested task: ${task}.`,
    platformClause,
    "Preserve documented geometry, floor count, room placement, walls, structure, openings, circulation, camera, crop, proportions, dimensions, and Design DNA.",
    "Do not invent missing architecture. Mark unreadable, missing, or conflicting information as Source required and stop any affected reconstruction.",
    "Return only evidence-supported work and include a preservation validation summary.",
  ].join("\n");
  return Array.from({ length: count }, (_, index) => ({
    id: `prompt-${index + 1}`,
    title: count === 1 ? `${task} prompt` : `${task} prompt — option ${index + 1}`,
    prompt: index === 0 ? base : `${base}\nVariation ${index + 1}: vary only reversible lighting, finish, atmosphere, or presentation treatment; keep all architectural locks unchanged.`,
    confidence: sourceFacts.length ? 85 : 40,
  }));
}

export function createArchRenderServer() {
  const server = new McpServer({ name: "arch-render", version: SERVER_VERSION });

  server.registerTool("get_capabilities", {
    title: "Get Arch Render capabilities",
    description: "Use this when you need to understand the preservation-first architectural workflows this MCP can perform before selecting a tool. It does not call external providers or modify data.",
    inputSchema: {},
    outputSchema: {
      serverVersion: z.string(),
      capabilities: z.array(z.string()),
      limitations: z.array(z.string()),
    },
    annotations: safeAnnotations,
  }, async () => result({
    serverVersion: SERVER_VERSION,
    capabilities: [
      "search bundled architectural knowledge",
      "fetch one bundled knowledge document",
      "build a preservation brief",
      "generate a bounded evidence-first prompt pack",
      "validate a preservation checklist",
    ],
    limitations: [
      "no certified architecture, engineering, code, cost, or legal sign-off",
      "no direct CAD or BIM authoring",
      "no external upload, image generation, paid call, or project mutation",
      "AI imagery cannot guarantee dimensional fidelity",
    ],
  }, "Arch Render MCP capabilities returned."));

  server.registerTool("search", {
    title: "Search Arch Render knowledge",
    description: "Use this when you need to find relevant preservation, rendering, BIM, presentation, typology, or coordination guidance in the bundled Arch Render knowledge library.",
    inputSchema: { query: z.string().trim().min(2).max(MAX_QUERY) },
    outputSchema: { results: z.array(z.object({ id: z.string(), title: z.string(), url: z.string() })) },
    annotations: safeAnnotations,
  }, async ({ query }) => {
    const tokens = query.toLowerCase().split(/\s+/).filter(Boolean);
    const files = await listMarkdownFiles();
    const scored = [];
    for (const id of files) {
      const doc = await readKnowledge(id);
      const haystack = `${doc.id}\n${doc.text}`.toLowerCase();
      const score = tokens.reduce((total, token) => total + (haystack.includes(token) ? 1 : 0), 0);
      if (score) scored.push({ score, id: doc.id, title: doc.title, url: "" });
    }
    scored.sort((a, b) => b.score - a.score || a.id.localeCompare(b.id));
    const structuredContent = { results: scored.slice(0, MAX_RESULTS).map(({ id, title, url }) => ({ id, title, url })) };
    return result(structuredContent);
  });

  server.registerTool("fetch", {
    title: "Fetch Arch Render knowledge document",
    description: "Use this when a prior Arch Render knowledge search returned a document id and you need that document's complete guidance. It reads one bundled Markdown file only.",
    inputSchema: { id: z.string().min(3).max(200) },
    outputSchema: {
      id: z.string(), title: z.string(), text: z.string(), url: z.string(),
      metadata: z.record(z.string(), z.string()),
    },
    annotations: safeAnnotations,
  }, async ({ id }) => {
    const doc = await readKnowledge(id);
    return result({ ...doc, url: "", metadata: { source: "arch-render bundled knowledge" } });
  });

  server.registerTool("build_preservation_brief", {
    title: "Build architectural preservation brief",
    description: "Use this when the user supplied architectural source facts and needs a structured brief that separates locked facts, authorized changes, and unknown information before rendering or review.",
    inputSchema: {
      projectTitle: z.string().trim().min(1).max(200),
      sourceType: z.enum(["plan", "elevation", "section", "render", "photo", "sketch", "bim-sheet", "mixed"]),
      intent: z.string().trim().min(1).max(1000),
      observedFacts: z.array(z.string().trim().min(1).max(500)).max(100),
      unknowns: z.array(z.string().trim().min(1).max(500)).max(100).default([]),
      authorizedChanges: z.array(z.string().trim().min(1).max(500)).max(50).default([]),
    },
    outputSchema: {
      projectTitle: z.string(), mode: z.string(), sourceType: z.string(), intent: z.string(),
      locked: z.array(z.string()), allowedChanges: z.array(z.string()), unknowns: z.array(z.string()),
      executionGate: z.string(),
    },
    annotations: safeAnnotations,
  }, async (input) => result({
    projectTitle: input.projectTitle,
    mode: input.authorizedChanges.length ? "Preserve First, Propose Second" : "Strict Preservation",
    sourceType: input.sourceType,
    intent: input.intent,
    locked: input.observedFacts,
    allowedChanges: input.authorizedChanges,
    unknowns: input.unknowns,
    executionGate: input.unknowns.length
      ? "Resolve any unknown that blocks the requested view or measurement before execution."
      : "Proceed only with evidence-supported output and run preservation QA before delivery.",
  }, "Preservation brief prepared without external calls or project changes."));

  server.registerTool("generate_prompt_pack", {
    title: "Generate architectural prompt pack",
    description: "Use this when the user explicitly requests a bounded architectural Prompt Pack or supplies an architectural source without a stated intent. It creates one to five text prompts and never generates images or calls paid providers.",
    inputSchema: {
      projectSummary: z.string().trim().min(1).max(4000),
      sourceFacts: z.array(z.string().trim().min(1).max(500)).max(100).default([]),
      task: z.enum(["preservation", "2d-to-3d", "exterior", "interior", "materials", "lighting", "presentation", "documentation"]),
      platform: z.enum(["universal", "gpt-image", "midjourney", "flux", "stable-diffusion", "magnific"]).default("universal"),
      count: z.number().int().min(1).max(5).default(1),
    },
    outputSchema: {
      prompts: z.array(z.object({ id: z.string(), title: z.string(), prompt: z.string(), confidence: z.number() })),
      externalCalls: z.number(), paidAttempts: z.number(),
    },
    annotations: safeAnnotations,
  }, async (input) => result({
    prompts: createPrompt(input), externalCalls: 0, paidAttempts: 0,
  }, "Prompt Pack generated locally. No files were uploaded and no paid calls were made."));

  server.registerTool("validate_preservation", {
    title: "Validate architectural preservation checklist",
    description: "Use this when you have evidence-backed preservation check results and need a deterministic delivery decision. It does not inspect images itself and never converts unverified claims into passes.",
    inputSchema: {
      checks: z.array(z.object({
        category: z.enum(["floor-count", "massing", "rooms-walls", "openings", "structure", "circulation", "roof", "dimensions", "camera", "crop-aspect", "materials", "source-coverage"]),
        status: z.enum(["pass", "fail", "not-verifiable"]),
        evidence: z.string().trim().min(1).max(1000),
      })).min(1).max(50),
    },
    outputSchema: {
      decision: z.enum(["deliver", "block"]),
      failures: z.array(z.string()), notVerifiable: z.array(z.string()), summary: z.string(),
    },
    annotations: safeAnnotations,
  }, async ({ checks }) => {
    const failures = checks.filter((check) => check.status === "fail").map((check) => check.category);
    const notVerifiable = checks.filter((check) => check.status === "not-verifiable").map((check) => check.category);
    const decision = failures.length ? "block" : "deliver";
    return result({
      decision, failures, notVerifiable,
      summary: failures.length
        ? `Delivery blocked by ${failures.length} preservation failure(s).`
        : `No recorded failures. Disclose ${notVerifiable.length} not-verifiable item(s) with the output.`,
    });
  });

  return server;
}

export async function startStdio() {
  const server = createArchRenderServer();
  await server.connect(new StdioServerTransport());
}

export async function startHttp() {
  const port = Number(process.env.PORT ?? 8788);
  const host = process.env.HOST ?? "127.0.0.1";
  const httpServer = createHttpServer(async (req, res) => {
    const url = new URL(req.url ?? "/", `http://${req.headers.host ?? "localhost"}`);
    if (req.method === "GET" && url.pathname === "/") {
      res.writeHead(200, { "content-type": "application/json; charset=utf-8" });
      res.end(JSON.stringify({ name: "arch-render-mcp", version: SERVER_VERSION, mcp: "/mcp" }));
      return;
    }
    if (req.method === "OPTIONS" && url.pathname === "/mcp") {
      res.writeHead(204, {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, GET, DELETE, OPTIONS",
        "Access-Control-Allow-Headers": "content-type, mcp-session-id",
        "Access-Control-Expose-Headers": "Mcp-Session-Id",
      });
      res.end();
      return;
    }
    if (url.pathname !== "/mcp" || !["POST", "GET", "DELETE"].includes(req.method ?? "")) {
      res.writeHead(404).end("Not Found");
      return;
    }
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.setHeader("Access-Control-Expose-Headers", "Mcp-Session-Id");
    const server = createArchRenderServer();
    const transport = new StreamableHTTPServerTransport({ sessionIdGenerator: undefined, enableJsonResponse: true });
    res.on("close", () => { transport.close(); server.close(); });
    try {
      await server.connect(transport);
      await transport.handleRequest(req, res);
    } catch (error) {
      console.error("MCP request failed", error instanceof Error ? error.message : "unknown error");
      if (!res.headersSent) res.writeHead(500).end("Internal server error");
    }
  });
  httpServer.listen(port, host, () => console.log(`Arch Render MCP listening on http://${host}:${port}/mcp`));
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  if (process.argv.includes("--http")) await startHttp();
  else await startStdio();
}
