SEARCH-FOR-PRESUMPTION-123:
  Date searched: 2026-05-10
  Original item: PRESUMPTION-123
  Original statement: "'100% drained in one cycle' celebrates throughput while INCORPORATE rate stays at 0 and REVISE backlog grows — throughput presumed right success metric"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-123
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-09 EOD throughput-celebration analysis
      15a: Searched for review-pipeline metric-design literature on balanced-scorecard / throughput-vs-quality patterns
    Current status: NO-SUPPORT-FOUND

  Sources:
    1. Kaplan & Norton (1996) "The Balanced Scorecard" — single-metric optimization (throughput-only) is documented as a canonical anti-pattern; balanced-scorecard requires multi-metric design.
    2. DORA / DevOps performance literature (Forsgren et al. 2018 "Accelerate") — throughput must be paired with quality and stability metrics; throughput-only celebrations are documented as predictors of downstream-quality regression.
    3. Goodhart's Law (Goodhart 1975; Strathern 1997) — when a metric becomes a target it ceases to be a good metric; throughput-as-target is the canonical Goodhart instance.
    4. (No literature supports throughput-as-sole-success-metric for review pipelines.)
    5. C2A2-internal: 2026-05-09 cycle: 0 INCORPORATE, 11 MONITOR, 9 REVISE — REVISE backlog grew while INCORPORATE rate stayed at 0%; the metric being celebrated is the metric most decoupled from architectural progress.

  Strength of support: None

  Summary: No literature supports throughput-as-sole-success-metric. The balanced-scorecard, DORA, and Goodhart's Law literatures uniformly require multi-metric design for review pipelines. The presumption operates against literature consensus, and the empirical pattern (0% INCORPORATE, growing REVISE backlog) is the predicted failure mode.

  Caveats: This is a NO-SUPPORT-FOUND for the FOR direction.

  Recommendation: NO-SUPPORT-FOUND
