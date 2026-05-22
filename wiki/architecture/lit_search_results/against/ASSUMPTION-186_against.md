SEARCH-AGAINST-ASSUMPTION-186:
  Date searched: 2026-05-20
  Original item: ASSUMPTION-186
  Original statement: "The 51-pending alarm is a measurement artifact — 36 stale duplicates; genuine unreviewed = 15."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-186
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session: pending-queue alarm investigated; 51 nominal decomposed to 36 stale duplicates + 15 genuine.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; see PRESUMPTION-215/REVISE-040)
    Current status: NO-CHALLENGE-FOUND

  Challenging evidence found: Weak

  Sources:
    1. Hand, D. (2018). "Statistical challenges of administrative and transaction data." — Raw operational counts are sometimes used directly, but only with explicit acknowledgement of known error sources; not a defense of skipping dedup.

  Strength of challenge: Weak

  Summary: No credible body of literature defends acting on a raw count known to contain duplicate records. The only weak counter is pragmatic: dedup has cost, and if the alarm threshold has wide margin the artifact may not change the decision. Here it did change the decision (drove a conservation-gate throttle), so the weak counter does not apply.

  Specific risks: If the 36/15 split is itself wrong, the throttle was mis-calibrated in the opposite direction.

  Mitigations available: Re-count after dedup fix; assert genuine-count invariant in the alarm path.

  Recommendation: NO-CHALLENGE-FOUND

  STEELMAN:
    Item: ASSUMPTION-186
    Strongest counterargument: The strongest case for using the raw 51 is that conservatism is cheap: throttling on an over-count errs safe. But that argument collapses because the over-count masks the real generation-rate signal and trains the operator to distrust the alarm.
    What would need to be true for C2A2 to be safe: Safe if the genuine count is recomputed from deduplicated state before any throttle decision.
    How to test: Re-run the count on deduplicated pending/ and confirm genuine==15 across two cycles.
