SEARCH-AGAINST-PRESUMPTION-645:
  Date searched: 2026-08-03
  Original item: PRESUMPTION-645
  Original statement: That an audit trail can be trusted to be complete in the successful
    direction — that a completed step implies a logged step.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-645
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a disclosed seven-week log gap, generalised to the registers that
           depend on log completeness (origin ASSUMPTION-670)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. OWASP Top 10:2025 A09, Security Logging and Alerting Failures — auditable events
       are "not logged or logged inconsistently"; asymmetric logging (one side of a
       control recorded, the other silently dropped) is the named canonical instance.
       Being in the OWASP Top 10 is itself a statement about base rate.
    2. "Application Logs Are Not Audit Logs" (dev.to) — for audit purposes a single
       dropped event is a completeness failure, and forwarding to central stores drops
       silently under load with no error surfaced at the writer.
    3. Time, Causality, and Observability Failures in Distributed AI Inference Systems,
       2026. arXiv:2604.21361 — silent failure produces no signal detectable by automated
       monitoring; components keep returning plausible output while the record diverges.
    4. Agent Delivery Engineering Predictive Reliability Framework, 2026.
       arXiv:2607.07689 — silent failures in agent systems surface only through outcome-
       based evaluation, not through error-and-latency monitoring.

  Strength of challenge: Strong

  Summary: The literature treats log completeness as a property requiring independent
  verification and routinely violated, with silent drops the expected mode. Under
  fail-fast shell semantics an append-last write is precisely the operation most likely to
  be skipped when an earlier step exits non-zero, and the skip produces no artifact — the
  absence of a line is indistinguishable from the absence of an event. The asymmetry 14b
  identifies is documented rather than novel: success-path gaps are systematically harder
  to detect than failure-path gaps, because a missing failure record leaves a broken thing
  behind while a missing success record leaves nothing behind at all. C2A2 has already
  realised this failure once (the seven-week gap) and has no mitigation.

  Specific risks: Every autonomy count, streak figure and "Nth consecutive day" claim in
  the registers rests on log completeness in the successful direction, and all of them are
  therefore under-counts of unknown size. The same day produced the exact inverse case —
  a task that ran and wrote where no check looked (ASSUMPTION-667). Both were found by
  accident, which means the discovery process for this class of error is itself luck.
  Compounding: the streak figures feed the maturity narrative and the daily summary, so a
  logging gap propagates into the human-facing artifact that PRESUMPTION-639 shows is
  already unverified.

  Mitigations available: Yes. (i) Write the log line first, or write it in a trap/finally
  handler so it survives non-zero exits — removes the fail-fast skip path entirely.
  (ii) Reconcile logs against filesystem evidence: artifacts have mtimes, and a run that
  wrote a file but no log line is detectable by a join. (iii) Assert on expected cadence —
  a scheduled daily task that produces no log line on a weekday should raise, since
  "nothing happened" and "nothing was recorded" are then distinguishable. (iv) Stop
  reporting streaks derived from logs alone until (ii) exists, or report them with an
  explicit completeness caveat.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-645
    Strongest counterargument: The presumption is an inference from absence, and absence
    is exactly what a logging system fails to produce reliably. Worse, the inference runs
    in the direction the system most wants: a complete log makes the streak real, so the
    presumption is load-bearing for a figure the system reports about itself with pride.
    The structural problem is that no self-check can detect this class of error, because
    the self-check reads the same log. Verification requires an out-of-band witness —
    filesystem mtimes, scheduler records, artifact contents — and none is currently
    consulted. The seven-week gap is not an anomaly to be patched; it is the first
    observed instance of a failure mode the architecture cannot see, and it was found by
    accident, which tells you nothing about how many others there are.
    What would need to be true for C2A2 to be safe: that log writes are unconditional
    with respect to the success or failure of preceding steps, and that some independent
    record exists against which the log can be reconciled.
    How to test: for the last 60 days, join scheduled-task log lines against the mtimes of
    the artifacts those tasks write. Every date with an artifact but no log line is a
    silent success-path drop. This is an in-house query and settles the magnitude.
