SEARCH-AGAINST-ASSUMPTION-287:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-287
  Original statement: Observed telemetry should replace authored narration as the basis of the Agent Explorer.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-287
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated design assumption from 2026-06-08 OpenStory→Agent-Explorer build sessions
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. Naur, P., 1985. "Programming as Theory Building." Microprocessing and Microprogramming. — A program/system is not its artifacts: the theory (why it is the way it is, how world maps to system) is not recoverable from code or traces. Telemetry is an even lossier representation than source; replacing authored narration discards exactly the layer telemetry cannot carry.
    2. Suchman, L., 1987. "Plans and Situated Actions." Cambridge UP. — Observed action sequences underdetermine the plans/purposes behind them; behavior records are accounts, not substitutes for intent.
    3. Hollnagel, E., 2014. "Safety-I and Safety-II." Ashgate. — Work-as-done (traces) and work-as-imagined (authored descriptions) systematically diverge; safety/quality understanding requires both, not replacement of one by the other.
    4. Databahn, 2025. "Enterprise Observability vs Security Telemetry" (industry). — The "telemetry intent gap": telemetry collected for one purpose structurally fails to answer questions about purpose/intent; instrumentation only captures what supported hooks emit.
  Strength of challenge: Moderate
  Summary: A consistent literature thread says behavioral traces are necessary but not sufficient representations of what a system is for. Naur and Suchman argue intent/theory is constitutively absent from execution records; Hollnagel shows authored and observed views diverge and that the divergence itself is the signal. The challenge is to "replace" — telemetry as the *basis* with narration retained as an annotation layer is far better supported than telemetry instead of narration. Authored narration also encodes aspiration and design rationale that no amount of trace volume recovers.
  Specific risks: Agent Explorer presents activity as identity — agents become what they happened to emit, dormant purposes vanish, design rationale is lost, and the explorer silently normalizes "what fired recently" as "what this agent is."
  Mitigations available: Dual-layer model (telemetry spine + authored intent annotations); render the gap between stated purpose and observed behavior as an explicit, first-class signal rather than discarding one side.
  STEELMAN:
    Strongest counterargument: Authored narration in this vault was demonstrably stale and aspirational; telemetry is at least true. A self-representation grounded in falsifiable observation beats one grounded in unfalsifiable prose, and narration can always be re-layered on top of a truthful skeleton. For an explorer (navigation tool, not archive), recency and accuracy dominate completeness.
    What would need to be true for C2A2 to be safe: Authored narration is retained somewhere recoverable; the explorer's users understand they are viewing behavior, not purpose; intent-bearing metadata (task descriptions, prompts) rides along with telemetry.
    How to test: Pick 5 agents; have a human write what each is "for" from telemetry alone vs from narration alone; compare both to ground truth (the prompts/task definitions). Measure what each representation gets wrong.
  Search scope: 2 searches — "limitations of telemetry capturing system intent observed vs documented"; "Naur programming as theory building code does not capture theory". Plus established literature.
  Recommendation: PARTIALLY-CHALLENGED
