SEARCH-AGAINST-PRESUMPTION-492:
  Date searched: 2026-07-18
  Original item: PRESUMPTION-492
  Original statement: [inferred] The lit pipeline presumes 15d RE-TRIGGER generation stays within daily drain capacity; a 129-item undrained backlog (07-05, 07-12) with no fan-out cap or STALE-aging shows re-triggers can outpace draining unboundedly.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-492
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from the observed 129-item undrained RE-TRIGGER backlog
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. AWS Builder Library, "Avoiding insurmountable queue backlogs." — Distinguishes a transient backlog (drains once a burst passes) from a persistent one; a snapshot count cannot tell them apart. 129 items across two discrete dates (07-05, 07-12) is consistent with two bounded bursts, not necessarily λ>μ.
    2. Causely, "Queue Growth ... Why Asynchronous Failures Are Easy to Misread." — Warns that during a transient period a queue "appears as if it were stable" and instability is hard to infer from a single observation; backlog snapshots are routinely misread.

  Strength of challenge: Moderate

  Summary: The challenge targets the word "unboundedly." The observed backlog is real, but the evidence (a static count on two dated cohorts) does not establish a SUSTAINED arrival-rate > service-rate condition — the only thing that yields true unbounded growth. It is equally consistent with 15d emitting bounded weekly cohorts (e.g., MONITOR-345..399) that the daily run simply never scheduled — a coverage/omission bug (the pipeline drains only fresh 14a/14b items) rather than a rate-instability. The distinction matters: an omission is fixed by scheduling the cohort once; genuine λ>μ requires a cap + load-shedding.

  Specific risks: Diagnosing "unbounded" when the truth is "never scheduled" could add unnecessary fan-out caps/TTLs while leaving the actual bug (RE-TRIGGER items excluded from the daily drain loop) unfixed — the backlog would persist.

  Mitigations available: First MEASURE: log 15d enqueue count/day vs 15abc drain count/day for a week. If enqueue ≤ drain but backlog persists, it's an omission (schedule the cohorts). If enqueue > drain sustained, add a fan-out cap + STALE-aging.

  STEELMAN:
    Strongest counterargument: The backlog is more likely a COVERAGE bug (the daily loop structurally skips RE-TRIGGER cohorts) than a rate instability; both produce a growing snapshot, but only one is cured by caps/TTL. Calling it "outpaces draining unboundedly" prejudges the mechanism before measuring rates.
    What would need to be true for "unbounded" to hold: Sustained λ (re-trigger emission) > μ (drain capacity) across multiple periods, not a one-time cohort that was simply never picked up.
    How to test: Instrument enqueue vs drain per day for 1-2 weeks; compare. (Note: the daily run's own logs already show it drains only the fresh batch — evidence FOR the omission hypothesis.)

  Recommendation: PARTIALLY-CHALLENGED
