// ============================================================================
// cc-broker — Pathway-00 Edge Function
//
// Project: C2A2-wiki (akhcocmgfwybdovqeovd)
// Spec:    PATHWAY00_BROKER_SPEC.md §3 (request flow)
//          PATHWAY00_BROKER_SPEC_v2_web_enrich.md (web_enrich action)
// Schema:  supabase/migrations/20260526200000_broker_schema.sql
//          supabase/migrations/20260528120000_web_enrich.sql
//
// One endpoint, four actions:
//   action=enrich          → LLM call against client-provided context
//                            (free pool → BYO → 402)
//   action=web_enrich      → Tavily web search + LLM call grounded on snippets
//                            (separate cap; 502 on Tavily down; 402 on cap-hit)
//   action=register_byo    → store an OpenRouter key for this device
//   action=realtime_session → mint an OpenAI Realtime ephemeral token for the
//                            public voice guide (needs OPENAI_API_KEY)
//
// Secrets read from env (set in Supabase dashboard, never logged):
//   OPENROUTER_FREE_KEY        — Tom's pool, used when free tier under cap
//   OPENAI_API_KEY             — OpenAI standing key, ONLY for Realtime minting
//   TAVILY_API_KEY             — web search provider, free tier 1000/mo
//   SUPABASE_URL               — auto-provided by runtime
//   SUPABASE_SERVICE_ROLE_KEY  — auto-provided by runtime
//
// PROVENANCE (2026-07-20): this file drifted from the deployment. The deployed
// v9 gained action=realtime_session while this copy sat at 2026-05-28, and the
// deploy pipeline strips inline comments — so neither copy was a superset. The
// realtime_session block below was recovered from the deployment via
// `supabase functions download cc-broker` and merged back in here, keeping this
// file's rationale comments. Verified: every other line is functionally
// identical; all rate/cap constants match exactly.
// ============================================================================

import { createClient } from "https://esm.sh/@supabase/supabase-js@2.45.0";

// ----------------------------------------------------------------------------
// Tunables. All cheap to change; bump these as usage data justifies.
// ----------------------------------------------------------------------------
const DEFAULT_MODEL          = "openai/gpt-4o-mini";  // cheap, fast, capable enough for ranking
const DEVICE_DAILY_LIMIT     = 50;                    // free-pool asks per device per day — research-tier (was 10; raised 2026-05-27 to support real work, not just PoC demos)
const GLOBAL_DAILY_CENTS_CAP = 500;                   // circuit-breaker: $5/day → ~$150/mo ceiling — research-tier (was 40)
const IP_DAILY_CAP           = 500;                   // backstop against device-UUID cycling — scaled with DEVICE_DAILY_LIMIT (was 100)
const MAX_BODY_BYTES         = 32 * 1024;             // 32 KB — ranking payloads (60 candidates × ~410B) routinely hit ~25 KB; cost is bounded by GLOBAL_DAILY_CENTS_CAP, not payload size

// web_enrich tunables — separate budget so web search caps don't starve dataset enrichment
const WEB_DEVICE_DAILY_LIMIT     = 20;    // web_enrich asks per device per day
const WEB_GLOBAL_DAILY_CENTS_CAP = 300;   // $3/day ceiling for web_enrich (separate from $5 dataset)
const WEB_SEARCH_CENTS_PER_CALL  = 1;     // flat per-search cost estimate (Tavily free tier; bump when paid)
const TAVILY_API_URL             = "https://api.tavily.com/search";
const TAVILY_MAX_RESULTS         = 5;
const TAVILY_QUERY_MAX_CHARS     = 500;   // longest query string we'll send to Tavily

const ALLOWED_ORIGINS = new Set([
  "https://tloughran.github.io",   // public deployed wiki
  "http://localhost:8080",         // local HTTP server per CLAUDE.md
  "http://127.0.0.1:8080",
]);

// Penny-rounded cost estimate per ask. OpenRouter returns exact token counts
// in the response; we bump cents based on that, with a 1-cent floor so the
// global meter never undercounts even on tiny calls.
function estimateCostCents(usage: { prompt_tokens?: number; completion_tokens?: number } | null | undefined): number {
  if (!usage) return 1;
  // gpt-4o-mini: $0.15/M input, $0.60/M output. Convert to cents.
  const inCents  = ((usage.prompt_tokens     ?? 0) / 1_000_000) * 15;
  const outCents = ((usage.completion_tokens ?? 0) / 1_000_000) * 60;
  return Math.max(1, Math.ceil(inCents + outCents));
}

// ----------------------------------------------------------------------------
// Helpers
// ----------------------------------------------------------------------------
const corsHeaders = (origin: string | null) => {
  const allowed = origin && ALLOWED_ORIGINS.has(origin) ? origin : "";
  return {
    "Access-Control-Allow-Origin": allowed,
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "content-type, x-cc-device",
    "Access-Control-Max-Age": "86400",
    "Vary": "Origin",
  };
};

const json = (status: number, body: unknown, origin: string | null) =>
  new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/json", ...corsHeaders(origin) },
  });

const isUuid = (s: unknown): s is string =>
  typeof s === "string" && /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i.test(s);

async function sha256Hex(input: string): Promise<string> {
  const bytes = new TextEncoder().encode(input);
  const buf   = await crypto.subtle.digest("SHA-256", bytes);
  return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, "0")).join("");
}

// Extract the originating client IP. Supabase Edge Functions sit behind a
// proxy, so x-forwarded-for is the canonical source.
function clientIp(req: Request): string {
  const xff = req.headers.get("x-forwarded-for");
  if (xff) return xff.split(",")[0].trim();
  return req.headers.get("cf-connecting-ip") ?? "0.0.0.0";
}

// ----------------------------------------------------------------------------
// OpenRouter call. Returns text + usage + which model actually served.
// Throws on transport failure; returns {error} on provider error so the
// caller can decide whether to surface it.
// ----------------------------------------------------------------------------
async function callOpenRouter(opts: {
  apiKey: string;
  system: string;
  user: string;
  model?: string;
}): Promise<{ text: string; model: string; usage: { prompt_tokens?: number; completion_tokens?: number } | null; error?: string }> {
  const model = opts.model ?? DEFAULT_MODEL;
  const resp = await fetch("https://openrouter.ai/api/v1/chat/completions", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${opts.apiKey}`,
      "Content-Type": "application/json",
      // OpenRouter attribution headers — show up in their dashboard
      "HTTP-Referer": "https://tloughran.github.io/C2A2-wiki/",
      "X-Title": "C2A2 Community Explorer",
    },
    body: JSON.stringify({
      model,
      messages: [
        { role: "system", content: opts.system },
        { role: "user",   content: opts.user },
      ],
    }),
  });

  if (!resp.ok) {
    const errText = await resp.text();
    // Don't leak the full provider response — could contain key fragments in unusual error paths
    return { text: "", model, usage: null, error: `provider_error_${resp.status}` };
  }

  const data = await resp.json();
  const text  = data?.choices?.[0]?.message?.content ?? "";
  const usage = data?.usage ?? null;
  return { text, model, usage };
}

// ----------------------------------------------------------------------------
// Tavily web search. Returns at most TAVILY_MAX_RESULTS clean snippets.
// On any failure (transport, non-2xx, malformed payload) returns {error}.
// ----------------------------------------------------------------------------
type TavilyResult = { url: string; title: string; snippet: string };
async function callTavily(opts: {
  apiKey: string;
  query: string;
}): Promise<{ results: TavilyResult[]; error?: string }> {
  let resp: Response;
  try {
    resp = await fetch(TAVILY_API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        api_key: opts.apiKey,
        query: opts.query,
        max_results: TAVILY_MAX_RESULTS,
        search_depth: "basic",
      }),
    });
  } catch (_e) {
    return { results: [], error: "tavily_unreachable" };
  }

  if (!resp.ok) {
    return { results: [], error: `tavily_error_${resp.status}` };
  }

  let data: { results?: Array<{ url?: string; title?: string; content?: string }> };
  try {
    data = await resp.json();
  } catch {
    return { results: [], error: "tavily_bad_json" };
  }

  const raw = Array.isArray(data?.results) ? data.results : [];
  const results: TavilyResult[] = raw.slice(0, TAVILY_MAX_RESULTS).map(r => ({
    url:     typeof r.url     === "string" ? r.url     : "",
    title:   typeof r.title   === "string" ? r.title   : "",
    // Tavily calls it `content`; we surface it as `snippet` to clients for clarity.
    snippet: typeof r.content === "string" ? r.content : "",
  })).filter(r => r.url && r.snippet);

  return { results };
}

// Extract a clean query string from the client's `user` field. Heuristic per
// spec §3.4: take the substring after "Query: " if present, else use the whole
// user field trimmed to TAVILY_QUERY_MAX_CHARS. Newlines collapsed.
function extractTavilyQuery(userField: string): string {
  const marker = "Query: ";
  const idx = userField.indexOf(marker);
  let q: string;
  if (idx >= 0) {
    // Take everything after "Query: " up to the next newline (or end of string)
    const after = userField.slice(idx + marker.length);
    const nl = after.indexOf("\n");
    q = nl >= 0 ? after.slice(0, nl) : after;
  } else {
    q = userField;
  }
  return q.replace(/\s+/g, " ").trim().slice(0, TAVILY_QUERY_MAX_CHARS);
}

// Build the WEB_CONTEXT block appended to the system prompt. Spec §3.5.
function buildWebContext(results: TavilyResult[]): string {
  const lines = results.map((r, i) => `[${i + 1}] ${r.title} — ${r.snippet} (${r.url})`);
  return [
    "",
    "--- WEB_CONTEXT ---",
    "You also have these web search results. When you draw on any of them in your answer,",
    "cite the source by its numeric index in square brackets, e.g. [1] or [2].",
    "These are snippets only, not full documents — verify before quoting.",
    "Do not invent sources beyond this list. If none apply, do not cite any.",
    "",
    ...lines,
  ].join("\n");
}

// ----------------------------------------------------------------------------
// Main handler
// ----------------------------------------------------------------------------
Deno.serve(async (req) => {
  const origin = req.headers.get("origin");

  // CORS preflight
  if (req.method === "OPTIONS") {
    return new Response(null, { status: 204, headers: corsHeaders(origin) });
  }

  if (req.method !== "POST") {
    return json(405, { error: "method_not_allowed" }, origin);
  }

  if (!origin || !ALLOWED_ORIGINS.has(origin)) {
    return json(403, { error: "origin_not_allowed" }, origin);
  }

  // Body size guard before parsing
  const contentLength = parseInt(req.headers.get("content-length") ?? "0", 10);
  if (contentLength > MAX_BODY_BYTES) {
    return json(413, { error: "payload_too_large" }, origin);
  }

  // Device id from header
  const deviceId = req.headers.get("x-cc-device");
  if (!isUuid(deviceId)) {
    return json(400, { error: "bad_device_id" }, origin);
  }

  // Parse body
  let body: { action?: string; system?: string; user?: string; api_key?: string; model?: string; tab?: string };
  try {
    body = await req.json();
  } catch {
    return json(400, { error: "bad_json" }, origin);
  }

  // ---- Supabase service-role client (bypasses RLS) ----
  const sb = createClient(
    Deno.env.get("SUPABASE_URL")!,
    Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!,
    { auth: { persistSession: false } },
  );

  // ---- IP backstop (runs for every action) ----
  const ip       = clientIp(req);
  const ipSalt   = new Date().toISOString().slice(0, 10);   // rotates daily
  const ipHash   = await sha256Hex(`${ip}|${ipSalt}`);
  const { data: ipHits, error: ipErr } = await sb.rpc("ip_hit", { p_ip_hash: ipHash });
  if (ipErr) return json(500, { error: "db_error", where: "ip_hit" }, origin);
  if ((ipHits ?? 0) > IP_DAILY_CAP) {
    return json(429, { error: "ip_rate_limited" }, origin);
  }

  // ----------------------------------------------------------------------
  // Action: register_byo — store this device's OpenRouter key (encrypted)
  // ----------------------------------------------------------------------
  if (body.action === "register_byo") {
    if (typeof body.api_key !== "string" || body.api_key.length < 10 || body.api_key.length > 256) {
      return json(400, { error: "bad_api_key" }, origin);
    }
    const { error } = await sb.rpc("store_byo_key", { p_device_id: deviceId, p_api_key: body.api_key });
    if (error) return json(500, { error: "db_error", where: "store_byo_key" }, origin);
    return json(200, { ok: true }, origin);
  }

  // ----------------------------------------------------------------------
  // Action: enrich — the main LLM call
  // ----------------------------------------------------------------------
  if (body.action === "enrich" || body.action === undefined) {
    if (typeof body.system !== "string" || typeof body.user !== "string") {
      return json(400, { error: "bad_prompt" }, origin);
    }
    if (body.system.length + body.user.length > MAX_BODY_BYTES) {
      return json(413, { error: "prompt_too_large" }, origin);
    }

    // Read today's usage
    const { data: usage, error: useErr } = await sb.rpc("get_usage", { p_device_id: deviceId });
    if (useErr) return json(500, { error: "db_error", where: "get_usage" }, origin);
    const u = Array.isArray(usage) ? usage[0] : usage;
    const deviceAsks      = u?.device_asks       ?? 0;
    const globalCostCents = u?.global_cost_cents ?? 0;

    // Decide: free pool vs BYO vs deny
    const underFreeTier = deviceAsks < DEVICE_DAILY_LIMIT && globalCostCents < GLOBAL_DAILY_CENTS_CAP;

    let source: "free" | "byo";
    let apiKey: string;
    if (underFreeTier) {
      apiKey = Deno.env.get("OPENROUTER_FREE_KEY") ?? "";
      if (!apiKey) return json(500, { error: "broker_misconfigured" }, origin);
      source = "free";
    } else {
      const { data: byoKey, error: byoErr } = await sb.rpc("get_byo_key", { p_device_id: deviceId });
      if (byoErr) return json(500, { error: "db_error", where: "get_byo_key" }, origin);
      if (!byoKey) {
        return json(402, {
          error: "free_limit_reached",
          deviceAsks,
          deviceLimit: DEVICE_DAILY_LIMIT,
          globalCostCents,
          globalCap: GLOBAL_DAILY_CENTS_CAP,
          hint: "POST again with action=register_byo and a personal OpenRouter key to continue.",
        }, origin);
      }
      apiKey = byoKey;
      source = "byo";
    }

    // Call OpenRouter
    let result;
    try {
      result = await callOpenRouter({ apiKey, system: body.system, user: body.user, model: body.model });
    } catch (e) {
      return json(502, { error: "upstream_unreachable" }, origin);
    }
    if (result.error) {
      return json(502, { error: result.error }, origin);
    }

    // Only meter free-pool calls; BYO spends on the user's own key
    let freeRemaining = DEVICE_DAILY_LIMIT - deviceAsks;
    if (source === "free") {
      const costCents = estimateCostCents(result.usage);
      const { data: post, error: incErr } = await sb.rpc("increment_usage", {
        p_device_id: deviceId,
        p_cost_cents: costCents,
      });
      if (incErr) {
        // We made the call but failed to meter it. Log loudly, still return the
        // result — losing a count is preferable to losing the user's response.
        console.error("increment_usage_failed", incErr);
      } else {
        const p = Array.isArray(post) ? post[0] : post;
        freeRemaining = Math.max(0, DEVICE_DAILY_LIMIT - (p?.device_asks ?? deviceAsks + 1));
      }
    } else {
      freeRemaining = 0;
    }

    return json(200, {
      text: result.text,
      source,
      model: result.model,
      freeRemaining,
    }, origin);
  }

  // ----------------------------------------------------------------------
  // Action: web_enrich — Tavily search + LLM answer with citations
  // Spec: PATHWAY00_BROKER_SPEC_v2_web_enrich.md §3
  // ----------------------------------------------------------------------
  if (body.action === "web_enrich") {
    if (typeof body.system !== "string" || typeof body.user !== "string") {
      return json(400, { error: "bad_prompt" }, origin);
    }
    if (body.system.length + body.user.length > MAX_BODY_BYTES) {
      return json(413, { error: "prompt_too_large" }, origin);
    }

    // Read today's web usage
    const { data: webUsage, error: webUseErr } = await sb.rpc("get_web_usage", { p_device_id: deviceId });
    if (webUseErr) return json(500, { error: "db_error", where: "get_web_usage" }, origin);
    const w = Array.isArray(webUsage) ? webUsage[0] : webUsage;
    const deviceWebAsks      = w?.device_web_asks       ?? 0;
    const globalWebCostCents = w?.global_web_cost_cents ?? 0;

    // Decide: free pool vs BYO vs deny — independent budget from `enrich`
    const underWebFreeTier =
      deviceWebAsks < WEB_DEVICE_DAILY_LIMIT && globalWebCostCents < WEB_GLOBAL_DAILY_CENTS_CAP;

    let source: "free" | "byo";
    let apiKey: string;
    if (underWebFreeTier) {
      apiKey = Deno.env.get("OPENROUTER_FREE_KEY") ?? "";
      if (!apiKey) return json(500, { error: "broker_misconfigured" }, origin);
      source = "free";
    } else {
      const { data: byoKey, error: byoErr } = await sb.rpc("get_byo_key", { p_device_id: deviceId });
      if (byoErr) return json(500, { error: "db_error", where: "get_byo_key" }, origin);
      if (!byoKey) {
        return json(402, {
          error: "web_free_limit_reached",
          webAsks: deviceWebAsks,
          webLimit: WEB_DEVICE_DAILY_LIMIT,
          webCostCents: globalWebCostCents,
          webCap: WEB_GLOBAL_DAILY_CENTS_CAP,
          hint: "POST again with action=register_byo and a personal OpenRouter key to continue.",
        }, origin);
      }
      apiKey = byoKey;
      source = "byo";
    }

    // Tavily search
    const tavilyKey = Deno.env.get("TAVILY_API_KEY") ?? "";
    if (!tavilyKey) return json(500, { error: "broker_misconfigured", where: "TAVILY_API_KEY" }, origin);

    const query = extractTavilyQuery(body.user);
    if (!query) {
      // Defensive: client sent an empty user field through the length check
      return json(400, { error: "bad_prompt", where: "empty_query" }, origin);
    }

    const tavily = await callTavily({ apiKey: tavilyKey, query });
    if (tavily.error) {
      // Per spec §1: clear error, no silent degrade.
      return json(502, { error: "search_provider_down" }, origin);
    }
    if (tavily.results.length === 0) {
      // No results at all — surface explicitly so client can show clear message.
      return json(502, { error: "search_provider_down", reason: "no_results" }, origin);
    }

    // Inject WEB_CONTEXT block into the system prompt
    const augmentedSystem = body.system + buildWebContext(tavily.results);

    // OpenRouter call (re-checks combined size including WEB_CONTEXT)
    if (augmentedSystem.length + body.user.length > MAX_BODY_BYTES * 2) {
      // After context injection we allow up to 2× the raw cap, since WEB_CONTEXT
      // is broker-controlled, not client-controlled. Still bounded.
      return json(413, { error: "prompt_too_large", where: "after_web_context" }, origin);
    }

    let result;
    try {
      result = await callOpenRouter({ apiKey, system: augmentedSystem, user: body.user, model: body.model });
    } catch (_e) {
      return json(502, { error: "upstream_unreachable" }, origin);
    }
    if (result.error) {
      return json(502, { error: result.error }, origin);
    }

    // Meter on free-pool calls only. Total cost = flat Tavily fee + LLM tokens.
    let webRemaining = WEB_DEVICE_DAILY_LIMIT - deviceWebAsks;
    if (source === "free") {
      const llmCents   = estimateCostCents(result.usage);
      const totalCents = WEB_SEARCH_CENTS_PER_CALL + llmCents;
      const { data: post, error: incErr } = await sb.rpc("increment_web_usage", {
        p_device_id: deviceId,
        p_cost_cents: totalCents,
      });
      if (incErr) {
        console.error("increment_web_usage_failed", incErr);
      } else {
        const p = Array.isArray(post) ? post[0] : post;
        webRemaining = Math.max(0, WEB_DEVICE_DAILY_LIMIT - (p?.device_web_asks ?? deviceWebAsks + 1));
      }
    } else {
      webRemaining = 0;
    }

    // Read freeRemaining for the response (dataset-enrich budget, unchanged field)
    let freeRemaining = DEVICE_DAILY_LIMIT;
    const { data: dsUsage } = await sb.rpc("get_usage", { p_device_id: deviceId });
    const d = Array.isArray(dsUsage) ? dsUsage[0] : dsUsage;
    if (d) freeRemaining = Math.max(0, DEVICE_DAILY_LIMIT - (d.device_asks ?? 0));

    return json(200, {
      text: result.text,
      source,
      model: result.model,
      freeRemaining,
      webRemaining,
      sources: tavily.results,
    }, origin);
  }

  if (body.action === "realtime_session") {
    const openaiKey = Deno.env.get("OPENAI_API_KEY") ?? "";
    if (!openaiKey) return json(500, { error: "broker_misconfigured", where: "OPENAI_API_KEY" }, origin);

    const REALTIME_SESSION_CENTS = 25;
    const { data: usage, error: useErr } = await sb.rpc("get_usage", { p_device_id: deviceId });
    if (useErr) return json(500, { error: "db_error", where: "get_usage" }, origin);
    const u = Array.isArray(usage) ? usage[0] : usage;
    const deviceAsks      = u?.device_asks       ?? 0;
    const globalCostCents = u?.global_cost_cents ?? 0;
    if (deviceAsks >= DEVICE_DAILY_LIMIT || globalCostCents >= GLOBAL_DAILY_CENTS_CAP) {
      return json(402, {
        error: "free_limit_reached",
        deviceAsks, deviceLimit: DEVICE_DAILY_LIMIT,
        globalCostCents, globalCap: GLOBAL_DAILY_CENTS_CAP,
        hint: "Daily free voice limit reached. Try again tomorrow, or use your own OpenAI key.",
      }, origin);
    }

    const model = "gpt-realtime";
    const voice = "cedar";
    const scope =
      "You are the spoken guide to C2A2, the Community Dialogue Accelerator/Detector System, " +
      "and its wiki explorer. Stay on C2A2 topics: the project, its 14 thinker traditions, and " +
      "the explorer's tabs. If asked something clearly outside that, answer briefly and steer back. " +
      "Keep spoken answers short and warm.";

    let mint: Response;
    try {
      mint = await fetch("https://api.openai.com/v1/realtime/client_secrets", {
        method: "POST",
        headers: { "Authorization": `Bearer ${openaiKey}`, "Content-Type": "application/json" },
        body: JSON.stringify({ session: { type: "realtime", model, audio: { output: { voice } }, instructions: scope } }),
      });
    } catch (_e) {
      return json(502, { error: "upstream_unreachable", where: "openai_mint" }, origin);
    }
    if (!mint.ok) {
      const t = await mint.text();
      return json(502, { error: "openai_mint_failed", status: mint.status, detail: t.slice(0, 200) }, origin);
    }
    const md = await mint.json();
    const ephemeral = md?.value ?? md?.client_secret?.value;
    if (!ephemeral) return json(502, { error: "no_ephemeral" }, origin);

    const { error: incErr } = await sb.rpc("increment_usage", {
      p_device_id: deviceId,
      p_cost_cents: REALTIME_SESSION_CENTS,
    });
    if (incErr) console.error("increment_usage_failed(realtime)", incErr);

    return json(200, { value: ephemeral, expires_at: md?.expires_at ?? null, model }, origin);
  }

  return json(400, { error: "unknown_action" }, origin);
});
