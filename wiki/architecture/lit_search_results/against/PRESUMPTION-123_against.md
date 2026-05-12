SEARCH-AGAINST-PRESUMPTION-123:
  Date searched: 2026-05-10
  Original item: PRESUMPTION-123
  Original statement: "'100% drained in one cycle' celebrates throughput while INCORPORATE rate stays at 0 and REVISE backlog grows — throughput presumed right success metric"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-123
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-09 EOD throughput-celebration analysis
      15b: Searched for counter-evidence on throughput-only metric drift in long-running review pipelines
    Current status: CHALLENGED

  Sources:
    1. Goodhart's Law (Goodhart 1975; Strathern 1997) — single-metric optimization is canonical anti-pattern; throughput-as-target is paradigm Goodhart instance.
    2. Kaplan & Norton (1996) "The Balanced Scorecard" — multi-metric design is required for review pipelines; throughput-only is documented failure mode.
    3. DORA / Accelerate literature (Forsgren 2018) — throughput must be paired with quality and stability metrics; throughput-only celebrations predict downstream-quality regression.
    4. Drucker (1954) "The Practice of Management" — measuring what's measurable rather than what matters is canonical management failure mode.
    5. C2A2-internal: 2026-05-09 cycle: 0 INCORPORATE, 11 MONITOR, 9 REVISE; throughput celebrated while INCORPORATE rate 0% and REVISE backlog growing — exactly the predicted failure mode.

  Strength of challenge: Strong

  Summary: The presumption is strongly challenged across Goodhart's Law, balanced-scorecard, DORA, and management-theory literatures. The challenge is uniform: throughput-only is canonical failure mode for review pipelines. The empirical pattern (0% INCORPORATE, growing REVISE backlog) is the predicted Goodhart failure mode.

  Specific risks: (a) Throughput optimization at expense of INCORPORATE quality; (b) REVISE backlog growth treated as noise rather than signal; (c) success-metric drift over time as throughput-as-target reinforces.

  Mitigations available: (a) Multi-metric design (throughput + INCORPORATE-rate + REVISE-backlog + quality-drift); (b) explicit success-metric definition with multi-axis weighting; (c) tracking REVISE-backlog growth as first-class metric.

  Recommendation: CHALLENGED (literature consensus strong; empirical pattern matches predicted Goodhart failure mode)

  STEELMAN:
    Item: PRESUMPTION-123
    Strongest counterargument: This is the canonical Goodhart instance. Throughput became the celebrated metric; INCORPORATE rate is 0%; REVISE backlog grew. The empirical pattern matches the literature prediction exactly. Multi-metric design is canonical for review pipelines (Kaplan & Norton 1996); single-metric optimization is documented failure mode. The "100% drained" framing is itself the Goodhart signal — when the metric becomes a target, it ceases to be informative.
    What would need to be true for C2A2 to be safe: (a) Multi-metric design with INCORPORATE-rate / REVISE-backlog / quality-drift as first-class; (b) explicit success-metric definition; (c) REVISE-backlog growth tracked as first-class signal.
    How to test: Track INCORPORATE rate over the next 4 cycles; track REVISE-backlog growth; if INCORPORATE stays at 0% and REVISE-backlog grows, the throughput-as-success framing is empirically refuted.
