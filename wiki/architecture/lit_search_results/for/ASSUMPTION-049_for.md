SEARCH-FOR-ASSUMPTION-049:
  Date searched: 2026-04-20
  Original item: ASSUMPTION-049
  Original statement: "Session lifetime = one full tradition agent run (all pending proposals for that tradition); NOT one session per proposal"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-049
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from C2a2 caching architecture monday session; explicit architectural commitment in Execution Protocol v1.0
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Anthropic prompt-caching documentation (2024-2025 — "Prompt caching"): cache scope is session/request-scoped; reusing the same cached prefix across multiple proposals within one session is the canonical pattern for amortizing prefix token cost. A session boundary defines the cache lifetime.
    2. Chawla, Avi (2024). "Prompt Caching" (cited in the task brief). Frames per-session caching economics: cost amortization grows with the number of operations performed against a single cached prefix. Per-agent-run session (with N proposals) is the natural unit for amortization if N > 1.
    3. OpenAI prompt-caching / Assistants API threading (2024-2026 docs): threads and cached-context runs assume multiple turn-completions against a stable prefix; single-invocation (one-shot) requests forfeit the caching benefit. Evidence that multi-proposal-per-session matches the platform's caching model.
    4. Agent-framework practice (LangChain / LangGraph / OpenAI Assistants API 2024-2026): session = logical unit of related work against shared context; per-query sessions are acknowledged as anti-pattern for any workflow with shared state or shared preamble.
    5. C2A2 internal scaffolding: DECISION-005 (tradition agents as coherent reasoners over a shared reference frame) and ASSUMPTION-053 (appended-turn pipeline) both presuppose a coherent session boundary. The per-agent-run scope aligns with the existing architecture.

  Strength of support: Strong

  Summary: Per-agent-run session scope is the canonical prompt-caching pattern across Anthropic, OpenAI, and all major agent frameworks. Amortization economics require N>1 operations against a stable prefix per session; per-proposal sessions forfeit almost all caching value for any agent whose pending queue has more than one item. The commitment aligns with C2A2's existing decision architecture (DECISION-005) and the pipeline-as-appended-turns reorganization (ASSUMPTION-053).

  Caveats: (a) Breaks down if an agent typically has exactly one pending proposal — single-proposal case collapses to one-session-per-proposal economically; (b) very long sessions may hit context-window limits or degrade output quality; (c) cross-proposal pollution (one proposal's reasoning bleeding into the next) is a known risk at long-session scales.

  Recommendation: SUPPORTED (strong literature convergence + aligns with platform caching model + consistent with C2A2 internal scaffolding)
