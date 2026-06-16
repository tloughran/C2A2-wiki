SEARCH-AGAINST-PRESUMPTION-326:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-326
  Original statement: Recent/available activity is representative; bounded-window + sparse-old-data ingest under-renders low-frequency agents.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-326
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference (windowed ingest treated as the population; low-frequency agents under-rendered)
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. Yaghmaei et al., 2021. "Log2NS: Enhancing Deep Learning Based Analysis of Logs with Formal [Methods] to Prevent Survivorship Bias." arXiv:2105.14149. — Direct treatment of survivorship bias in log analytics: observational logs over-represent frequent/successful paths; conclusions drawn from what was logged in-window systematically miss rare-event entities.
    2. Wald, A., 1943 (the survivorship-bias archetype; see Wikipedia "Survivorship bias" synthesis). — The structural lesson: entities absent from the sample channel are not absent from the population; designing from the visible subset hardens the bias into the artifact.
    3. CFA Institute methodology literature ("time-period bias"; AnalystPrep/AnalystNotes syntheses). — A formally named bias for exactly this design: results from a bounded time window generalize only to that window; seasonal/episodic entities (quarterly agents, ad-hoc agents) are mis-estimated by construction.
    4. Vitter, J., 1985. "Random Sampling with a Reservoir." ACM TOMS (and the stream-sampling literature descending from it). — The standard remedy exists: frequency-independent sampling/ingest designs were developed precisely because window-plus-volume-driven capture mis-weights low-frequency items.
  Strength of challenge: Strong
  Summary: Note the polarity: this presumption was surfaced by 14b *with its own refutation attached* (the bounded window demonstrably under-renders low-frequency agents), and the literature confirms rather than rescues it. Time-period bias and survivorship bias are formally named, well-characterized failure modes of windowed observational data, and the agent-explorer case has both at once: the window excludes old activity, and the sparse-old-data ingest means even in-window low-frequency agents appear at reduced fidelity. The consequence compounds with PRESUMPTION-325 (those agents drop toward the unmapped residue) and ASSUMPTION-292 (the "representative enough" DB inherits the same window). A monthly or quarterly agent is not a smaller version of a daily agent in this design — it is rendered as a different, lesser kind of thing.
  Specific risks: Low-frequency but high-importance agents (e.g., monthly consolidation or audit agents) appear marginal or absent; the explorer's visual size/density encodings translate sampling artifact into apparent insignificance; lifecycle decisions (prune, deprecate) get made against under-rendered agents.
  Mitigations available: Per-agent normalization by expected firing cadence (render activity relative to schedule, not absolute volume); explicit "window coverage" indicator per agent (what fraction of its lifetime the window sees); full-history backfill for the roster dimension even if event detail stays windowed; flag agents whose expected fires exceed observed fires.
  STEELMAN:
    Strongest counterargument: For an operational explorer, recent activity is the decision-relevant population — what matters is what the swarm is doing now, and stale history can actively mislead. The under-rendering is acknowledged, bounded, and fixable at reseed; shipping a recency-weighted view first is a sequencing choice, not an epistemic error.
    What would need to be true for C2A2 to be safe: The view is labeled as windowed; cadence metadata exists so under-rendering is computable rather than invisible; reseed/backfill actually happens before population-level conclusions are drawn.
    How to test: For each rostered agent, compute expected-fires-in-window from its cron schedule vs observed sessions; the size and skew of the shortfall directly quantifies the under-rendering the presumption denies.
  Search scope: 1 search — "survivorship bias recency bias log analysis time window sampling low-frequency events underrepresented". Plus established sampling literature.
  Recommendation: CHALLENGED
