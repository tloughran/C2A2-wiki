SEARCH-FOR-PRESUMPTION-291:
  Date searched: 2026-06-02
  Original item: PRESUMPTION-291
  Original statement: [inferred] Under blind intake, the EOD summary presumes latest-on-disk == produced-today; today's cowork summary narrated 2026-05-30's self-awareness AND lit-search batches as "today's," a cross-day attribution echo.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-291
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as an unstated epistemic/self-referential presumption from the degraded-session behavior (cross-day attribution echo in the EOD summary).
      15a: Searched data-freshness / staleness detection, event-time vs processing-time correctness, and idempotent dated-delta reporting.
    Current status: SUPPORTED (the concern is well-grounded)

  Supporting evidence found: Yes

  Sources:
    1. Event-time vs processing-time distinction (Kleppmann, Designing Data-Intensive Applications, 2017; Kleppmann/Beresford/Svingen, "Online Event Processing," CACM 2019). — The foundational stream-processing correctness principle: the time an event occurred (event-time) must not be conflated with the time it was processed/read (processing-time); conflating them produces exactly the "latest-on-disk == today's" error.
    2. Data-freshness / staleness requirement (stream-processing patterns; "freshness = maximum acceptable age of data"). — Establishes that age-of-data must be tracked and bounded; an artifact read today but produced on a prior day is stale and must be labelled as such, not narrated as current.
    3. Idempotent dated-delta processing (Kleppmann patterns; idempotency-in-stream-processing literature). — Reporting should be a dated delta keyed to event-time so that re-reads of the same on-disk state do not re-emit it as new — directly the remedy for the attribution echo.

  Strength of support: Moderate

  Summary: The presumption identifies a textbook event-time/processing-time confusion: narrating the latest on-disk batch as "today's" conflates when an artifact was produced (event-time) with when it was read (processing-time). Stream-processing correctness practice treats this as a defect to design out via explicit freshness/age tracking and idempotent dated-delta reporting. The concern is not hypothetical — the echo was empirically realized (2026-05-30 batches narrated as 2026-05-31's).

  Caveats: The strength of the principle is established for correctness-sensitive pipelines; whether a low-stakes personal daily digest needs full event-time discipline is the cost-benefit question 15b examines.

  Recommendation: SUPPORTED
