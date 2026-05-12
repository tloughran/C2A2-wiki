SEARCH-AGAINST-ASSUMPTION-051:
  Date searched: 2026-04-20
  Original item: ASSUMPTION-051
  Original statement: "All tool definitions load upfront and never mutate mid-session (invariant condition on tool-layer for cache determinism)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-051
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Execution Protocol v1.0 invariant on tool-layer mutability
      15b: Searched for challenging literature
    Current status: NO-CHALLENGE-FOUND

  Challenging evidence found: No

  Sources:
    1. Cowork MCP architecture observations 2026: deferred-loading patterns (ToolSearch) exist and add tools mid-session — BUT this is additive, pre-first-use loading, not schema mutation of already-loaded tools. Needs verification that deferred-loading is reconcilable with the "never mutate" invariant.
    2. Dynamic tool-capability literature (some experimental agent research 2023-2024): a few research prototypes explore tool learning / tool-synthesis mid-session. These are non-production and document cache-breaking as a consequence rather than a critique of tool-stability.

  Strength of challenge: None

  Summary: No literature challenges the invariant. The only potential concern is whether deferred-loading patterns (ToolSearch-style) count as mutation — but they are pre-first-use additive loading of fully-defined schemas, not runtime schema mutation of already-invoked tools. The invariant holds cleanly. The practical risk is operational rather than conceptual: ensuring no agent framework or MCP server actually mutates schemas mid-session under the hood.

  Specific risks: (a) Operational: some MCP server could silently mutate tool schemas (e.g., retry-after-error rewriting description fields); (b) deferred-loading timing: if a new tool is fetched AFTER another tool has been invoked, the prefix layout changes between the first invocation and the second — this is a cache-invalidation event even if each tool schema individually is stable.

  Mitigations available: (a) Instrument turn-by-turn tool-manifest diffs and flag any mutation; (b) canonicalize all deferred-loads to happen before the first tool invocation; (c) for MCP servers with dynamic behavior, require a stability audit.

  Recommendation: NO-CHALLENGE-FOUND (the invariant is well-founded; operational testing is the remaining work, not conceptual revision)

  STEELMAN:
    Item: ASSUMPTION-051
    Strongest counterargument: The invariant is defensible but needs a precise operational definition. "Load upfront" in a deferred-tool-loading environment (Cowork's ToolSearch pattern) means "complete all tool-schema materialization before the first invocation" — which is stricter than simply "all tools registered at session start" and looser than "no deferred loading." Without this precise scoping, the invariant can be violated by otherwise-compliant frameworks.
    What would need to be true for C2A2 to be safe: Tool-manifest diff instrumentation at turn boundaries; explicit timing contract that deferred-loads must precede first invocation; audit of MCP servers used for any mid-session schema mutation.
    How to test: Compare tool-manifest byte-hash at turn 1 vs. turn N across a sample of 10 sessions; any diff reveals mutation.
