SEARCH-AGAINST-ASSUMPTION-1231:
  Date searched: 2026-08-28
  Original item: ASSUMPTION-1231
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority Medium)
  Original statement: A queue cleared by hand will refill, because arrival rate is unchanged and the server
    is an intermittently available human. Pinned to pending=0 at 2026-08-27, scoreable 2026-09-10.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1231
    Item type: ASSUMPTION (stated prediction)
    Transform at each step:
      14a: Extracted verbatim and pinned to a measured baseline with a scoring date.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Search scope: WebSearch, 2026-08-28, two dedicated queries — criticism of Little's law under
    non-stationarity, and evidence that backlog clearance or surge capacity durably improves throughput.
    Reached: Polaris Flow Dispatch, "Little's Law in a Complex Adaptive System"; Project Production
    Institute's practical treatment and its WIP tutorial; Nave and Capgemini on Little's law and Kanban;
    InfoQ, "The Mathematics of Backlogs: Capacity Planning for Queue Recovery"; oxmaint on maintenance
    backlog reduction; arXiv 2605.19139 (hybrid ABS/DES hospital queue study). NOT COVERED: the
    queueing-with-vacations literature, again — it is the exact model and neither direction has now reached
    it across two runs. All SNIPPET-ONLY. Confidence: MODERATE.

  Challenging evidence found: Yes — against the prediction's determinacy, not its direction

  Sources:
    1. Polaris Flow Dispatch, "Little's Law in a Complex Adaptive System" [SNIPPET-ONLY]
       https://www.polaris-flow-dispatch.com/p/littles-law-in-a-complex-adaptive —
       "Once humans enter the loop, assumptions collapse very quickly," and most knowledge-work processes are
       inherently non-stationary; pull policies and WIP limits are deployed to *approximate* stationarity,
       and under Little's strict framing even those approximations would not suffice. A gate whose server is
       intermittently absent is the paradigm case of the regime where the law gives no dated prediction.
    2. Project Production Institute, "Little's Law – A Practical Approach…" and "Optimal Level of WIP in a
       Production System" [SNIPPET-ONLY] https://projectproduction.org/journal/ —
       Warns against treating the relation as if fixing two variables sets the third: real systems have
       further physical constraints bounding throughput and cycle time.
    3. InfoQ, "The Mathematics of Backlogs: Capacity Planning for Queue Recovery" [SNIPPET-ONLY]
       https://www.infoq.com/articles/capacity-planning-queue-recovery/ ; oxmaint maintenance-backlog
       guidance [SNIPPET-ONLY] — Report that clearance combined with criticality-based prioritisation and
       temporary surge recovers durable capacity (a cited 15–25% labour-capacity recovery in facilities),
       i.e. a manual clearance is not always a pure reset when it is accompanied by a triage change.

  Strength of challenge: Moderate

  Summary: The challenge is to the prediction's precision rather than its sign. Little's law is an identity
    over long-run averages in a stable system; this queue has an arrival process driven by an autonomous
    pipeline and a server who has been absent for extended stretches, which is neither stable nor
    long-run-averaged over a two-week window. The law therefore supports "it will refill if nothing else
    changes" and says nothing about whether that is visible by 2026-09-10 — the scoring date the item pins
    itself to. Separately, the backlog-recovery literature supplies a real defeater: a clearance accompanied
    by a prioritisation change is not the same intervention as a bare clearance, and if the manual drain was
    accompanied by any change in what gets admitted, the prediction is testing the wrong thing.

  Specific risks: Scoring this on 2026-09-10 and finding pending > 0 will be read as confirmation when it is
    also consistent with ordinary arrival; scoring it and finding pending = 0 will be read as refutation when
    it may only mean fourteen days was too short. Either way the estate would record a settled result from an
    underpowered test.

  Mitigations available: State the falsifier numerically before the date — e.g. "pending ≥ 14 by 09-10,
    given an arrival rate of ~1/day" — so the test can fail. Record whether anything about admission changed
    at the time of the clearance; if it did, the prediction is confounded and should be re-pinned.

  STEELMAN:
    Item: ASSUMPTION-1231
    Strongest counterargument: The non-stationarity objection cuts the wrong way. If the server's
      availability is not merely variable but has been *zero* for extended periods, then the queue is not in
      a regime where refill is uncertain; it is in one where refill is the only possible outcome, and
      Little's law is being invoked as an illustration rather than as a load-bearing derivation. The
      prediction is nearly trivial and its value is that it is dated and falsifiable — which is more than
      most claims in this estate carry.
    What would need to be true for C2A2 to be safe: the arrival rate would have to have changed at the same
      time as the clearance. If it did not, the prediction stands on arithmetic, not on queueing theory.
    How to test: count arrivals to the gate between 08-27 and 09-10 and compare to the fourteen days before
      08-27. The prediction's whole content is in that comparison.

  Recommendation: PARTIALLY-CHALLENGED
