SEARCH-FOR-PRESUMPTION-459:
  Date searched: 2026-07-09
  Original item: PRESUMPTION-459
  Original statement: "Priority labels assigned at queue time remain valid at burn time — triage may select on stored tags without re-scoring."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-459
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inference from cohort listing (2026-07-08 EOD)
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Liu & Layland, 1973. "Scheduling Algorithms for Multiprogramming in a Hard-Real-Time Environment." JACM. — The foundational fixed-priority scheduling result: static priorities assigned once (rate-monotonic) are provably valid at execution time *when task characteristics are stationary*. Strongest analogous support: static tags suffice if nothing about the items or context changes.
    2. US Patent 10,609,045, "Autonomic incident triage prioritization by performance modifier and temporal decay parameters." — Industry artifact showing priority validity is treated as time-decaying: systems are built to re-score with temporal decay, implying stored tags are trusted only under short queue-residence times.
    3. Maintenance backlog triage practice (Oxmaint, "Maintenance Backlog Triage Checklist"). — Codifies periodic re-scoring: stale work orders are re-reviewed at age thresholds (8–30d, 31–90d, >90d), and weekly triage meetings "re-score stale items" — i.e., stored priorities are honored between reviews, which is a bounded version of the presumption.

  Strength of support: Weak

  Summary: There is genuine but narrow support: fixed-priority scheduling is a rigorously validated discipline (Liu & Layland) under the stationarity condition — if item urgency is intrinsic and the environment doesn't shift between queue time and burn time, selecting on stored tags is exactly what proven schedulers do. Practice literature partially supports the pattern in bounded form: stored priorities are routinely trusted for short residence times, with re-scoring only at staleness thresholds. However, the same practice literature builds in temporal decay and periodic re-triage precisely because priority validity erodes with queue age, and this queue's items age across days-to-weeks in a fast-changing pipeline context — the regime where the stationarity condition is least plausible. Support therefore holds for freshly queued items and weakens with residence time.

  Caveats: Support weakens as (a) queue residence time grows past the environment's change timescale (here: daily fires, config changes — likely days); (b) priorities encode context-relative judgments (relative severity vs. other then-present items) rather than intrinsic properties; (c) overload (ASSUMPTION-429) lengthens residence, compounding staleness. A cheap hybrid the literature suggests: trust tags under N days old, re-score older ones at burn time.

  Search scope confidence: Preliminary-to-comprehensive; no direct empirical study of rank churn on re-scoring was found.

  Recommendation: PARTIALLY-SUPPORTED
