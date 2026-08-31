SEARCH-AGAINST-PRESUMPTION-527:
  Date searched: 2026-08-29
  Original item: PRESUMPTION-527
  Original statement: [inferred] Leaving artifacts on disk for an attended Mac session presumes a session that has not occurred in 17 days.

  SCOPE NOTE (load-bearing, applies to every item in this run):
    Two limbs. (1) The internal-empirical claim about this repository's file state: NOT-SEARCHED,
    literature cannot adjudicate it. (2) The generalizable question named by the item's own
    "Search targets" line: searched here. The item is NOT retagged [MISROUTED-INTERNAL-EMPIRICAL];
    REVISE-408's authorisation request to Tom stands untouched.

  INDEPENDENCE CAVEAT: 15a and 15b ran in the same process this run — a stronger coupling than the
    read-channel coupling the standing 15a/15b correlation discount was written for. Where this
    search agrees with 15a, that agreement is worth LESS than usual and 15c discounts it.
  EVIDENCE GRADE: snippet-level search results only. Zero full-text reads, zero abstract-level reads.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-527
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: original extraction/inference (2026-07-21 cohort)
      15b: Searched for challenging literature on the generalizable limb only (2026-08-29); internal-empirical limb NOT-SEARCHED
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. LeSS, "Flow & Queueing Theory" and Kanban Tool, "Queuing Theory & Kanban." — holding items in a queue before a process 'does not reduce overall demand but shifts the queue's location'. Deferral relocates the problem; it does not create it.
    2. SAFe Principle #6 and the WIP-limit literature: where arrival rate exceeds service rate a queue forms without bound, and the corrective variable is the ARRIVAL side as much as the service side.
    3. C2A2's own validated premise on the lit-search queue (unstable regime; arrival exceeds service; 'arrival and service are BOTH decision variables ... admission control is available alongside throughput increase') — the same result, already established in-house for a different queue.

  Strength of challenge: Moderate

  Summary: The accumulation risk is not in dispute; the presumption's implicit diagnosis is. Queueing results say the binding constraint is the relation between arrival and service rates, not the absence of any particular service event, and that a broken Mac login is one realisation of a service rate that was already too low. Framing the problem as 'the attended session has not happened' points the remedy at restoring the session, when the same literature — and C2A2's own prior premise on exactly this pattern — says bounding the arrival side is an equally available and often cheaper fix. This is the same family as ASSUMPTION-492 above: an availability problem read as a coverage problem.

  Specific risks: Restoring the attended session clears the backlog once and leaves the generation rate untouched, so the backlog re-forms and the next broken login produces an identical incident. The recurring incident is then read as an infrastructure problem rather than a rate problem.

  Mitigations available: Cap what may be left pending an attended event (admission control), and make the pending-artifact count a monitored quantity rather than one discovered when the session finally happens.

STEELMAN:
  Item: PRESUMPTION-527
  Strongest counterargument: Strongest counterargument: C2A2 has already validated, for its own lit-search queue, that arrival exceeds service and that no scheduling discipline recovers it — and that an existing backlog drains at the SURPLUS rate, not the service rate. That premise transfers to this queue without modification, and it implies restoring the Mac session will not clear the Phase-6 backlog either. Filing this as a session-availability item rather than as another instance of the known rate problem means the pipeline has now met the same queueing result twice and named it twice.
  What would need to be true for C2A2 to be safe: Safe if the pending-artifact backlog is bounded by admission control and monitored continuously, not only at attended-session time.
  How to test: Measure uncommitted-artifact count against the attended-commit interval over 30 days. If the count grows monotonically between sessions, the constraint is the rate, not the session.

  Recommendation: PARTIALLY-CHALLENGED
