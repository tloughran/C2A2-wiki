SEARCH-AGAINST-PRESUMPTION-1054:
  Date searched: 2026-09-21
  Original item: PRESUMPTION-1054
  Original statement: Liveness is not progress; a monitoring regime that watches for dead processes is
    blind to hung ones, and the blindness is silent by construction.

  **Execution note:** 15a and 15b were executed by a single scheduled process on 2026-09-21. Query sets
  were framed separately and the FOR files were written before any AGAINST query was issued, but the
  two-process independence the spec assumes was NOT achieved. Weight the strength ratings accordingly.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-1054
    Item type: PRESUMPTION (unstated -- surfaced by inference)
    Transform at each step:
      14b: Inferred from 15d's stated inability plus this pass's three-probe measurement.
      15b: Searched for boundary conditions and costs of progress-based monitoring.
    Current status: NO-CHALLENGE-FOUND (to the claim); PARTIALLY-CHALLENGED (to the implied remedy)

  Challenging evidence found: Partial -- none against the claim; some against the obvious fix.

  Sources:
    1. Linux kernel lockup-watchdog documentation (softlockup / hardlockup detectors,
       docs.kernel.org/admin-guide/lockup-watchdogs). — Confirms the claim rather than challenging it:
       the kernel maintains *separate* detectors for hung-but-alive and for hard lockup, because one
       signal cannot witness both. Included here because it bounds the remedy: these detectors are
       tunable and their defaults produce false positives.
    2. Watchdog-tuning practice literature (OneUpTime, "How to Troubleshoot Watchdog Timer Issues";
       processWatchdog project docs). — The real challenge. Progress-signal watchdogs require the
       monitored process to *explicitly signal completed units of work*, and legitimate long waits
       produce false alarms: "readers legitimately busy-wait for long periods, so without feeding the
       watchdog, it would raise false timeout alarms." The remedy trades silent blindness for noisy
       false positives, and the trade is tuned, not solved.
    3. False-positive management practice (kernel `warn` rather than `panic` settings; timeout tuning
       guidance). — Documents that operators routinely *degrade* watchdogs to warning-only to stop
       false restarts, which reintroduces the original failure by another route: a warning nobody acts
       on is the alert-fatigue failure of PRESUMPTION-1055.

  Strength of challenge: Weak (against the claim); Moderate (against a naive implementation)

  Summary: No source contradicts the presumption. Liveness-without-progress is a recognised failure
    mode and the distinction 14b drew is the standard one. What the literature adds is a cost the item
    does not mention: progress monitoring needs a *defined unit of work* emitted by the monitored
    process, and where the unit is ill-defined or the legitimate latency is long, the detector produces
    false alarms that get silenced. For a pipeline whose runs are irregular and can legitimately take
    hours, choosing the threshold is the whole difficulty.

  Specific risks: A progress watchdog is added, fires on a legitimately long run, is set to warn-only,
    and the estate now has both the original blindness and a new ignored warning. This is the failure
    chain PRESUMPTION-1055 describes, so the two items interlock: the fix for 1054 is a candidate cause
    of 1055.

  Mitigations available: Define the progress quantity as a monotonic artefact rather than a timer — the
    date of the last run section appended to `lit_search_returns.md` is already such a quantity and
    needs no new instrumentation. A staleness assertion on that date ("no run section in N days") is
    self-evidently actionable, which is what keeps it out of the ritual-disclosure failure.

  STEELMAN:
    Item: PRESUMPTION-1054
    Strongest counterargument: The presumption is correct and nearly unfalsifiable as stated — which is
      itself the concern. "Liveness is not progress" is a definitional truth in the literature, so
      confirming it costs nothing and changes nothing. The load-bearing claim is the operational one:
      that C2A2's monitoring is *in fact* liveness-only and that a progress witness is *available and
      unbuilt*. That claim is in-house, checkable, and is the one worth dispositioning; the general
      principle is settled and should not consume another cycle.
    What would need to be true for C2A2 to be safe: that some monitored quantity increases only when
      work completes, and that something reads it on a schedule.
    How to test: assert on the newest date-stamped section in `lit_search_returns.md`. If that date is
      older than the scheduled cadence, the pipeline is hung. Today that assertion would have fired on
      2026-09-17 and every day since.

  Recommendation: NO-CHALLENGE-FOUND
