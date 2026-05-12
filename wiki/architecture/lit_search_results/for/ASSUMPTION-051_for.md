SEARCH-FOR-ASSUMPTION-051:
  Date searched: 2026-04-20
  Original item: ASSUMPTION-051
  Original statement: "All tool definitions load upfront and never mutate mid-session (invariant condition on tool-layer for cache determinism)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-051
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Execution Protocol v1.0 invariant on tool-layer mutability
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Anthropic prompt-caching documentation (2024-2025): the tool-definitions block is part of the cached prefix. Any mutation to tool schemas, ordering, or descriptions invalidates the cache for the remainder of the session. Explicit platform guidance that tools must be stable for caching to hit.
    2. OpenAI Assistants API / function-calling documentation (2024-2026): tool schemas registered at thread/run start; documented that changing tool definitions requires a new run. Implicit commitment to tool-immutability as a condition for stable caching.
    3. Agent-framework best practice (LangChain, LangGraph, OpenAI Assistants 2024-2026): tools are registered once at agent construction; tools-as-state-mutations are an acknowledged anti-pattern because they break several invariants (serialization, caching, reproducibility).
    4. ToolSearch / deferred-loading patterns (Cowork MCP architecture 2026): deferred loading is permitted only in ONE DIRECTION — additive fetches of fully-defined schemas at runtime before first call. Mutation AFTER a tool has been invoked in a session is not supported. This aligns with ASSUMPTION-051's "load upfront and never mutate" framing (the deferred-loading exception is not a mutation).
    5. Cache-integrity theory (Fowler 2018; cache-coherence literature generally): any state variable in the cache key must be immutable for the cache lifetime; tool manifests are state variables.

  Strength of support: Strong

  Summary: Tool-layer immutability as a precondition for cache determinism is a universal invariant across major LLM agent platforms and aligns with general cache-coherence theory. Anthropic and OpenAI platform documentation explicitly include tool definitions in the cacheable prefix region, making mutation-during-session an explicit cache-invalidator. No credible counter-literature was found.

  Caveats: (a) "Load upfront" is subtly different from "never deferred" — Cowork's ToolSearch deferred-loading pattern is a staged-load-before-first-use, which is compatible if all schemas are loaded before any tool is invoked; (b) testing needs to verify no agent framework currently in use does runtime tool-schema rewriting.

  Recommendation: SUPPORTED (strong; platform-documented invariant; universal across major frameworks)
