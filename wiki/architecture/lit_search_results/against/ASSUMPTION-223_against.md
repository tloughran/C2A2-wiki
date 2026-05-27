SEARCH-AGAINST-ASSUMPTION-223:

  Date searched: 2026-05-25
  Original item: ASSUMPTION-223
  Original statement: "When a MONITOR item reaches cycle 4 with stable evidence and the blocker is an un-run empirical/paired test (not unsettled literature), further weekly literature cycles are low-yield; STALE-flag, downgrade Weekly->Monthly, and escalate to a human for the empirical test."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-223
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: original extraction of stated assumption
      15b: Searched for challenging literature (cycle 0)
    Current status: SEARCHED

  Challenging evidence found: Partial

  Sources:
    1. OnPage (2024), "The Silent Failure: When Monitoring Doesn't Wake the Right People"; incident.io (2025), alert-fatigue guidance. — Escalation only resolves a stall if the next tier is actually available; escalating into an absent endpoint relabels the bottleneck without clearing it (the substance of PRESUMPTION-245).
    2. Parasuraman, R. & Manzey, D. (2010). "Complacency and bias in human use of automation." Human Factors 52(3), 381-410. — Already in the C2A2 corpus; cautions that automated "stop and hand to human" steps degrade when the human leg is unexercised.
    3. Research-synthesis literature on premature stopping. — Declaring a literature "saturated" after a handful of automated cycles risks a false-negative; genuine but slow-moving evidence can be missed.

  Strength of challenge: Moderate

  Summary: The challenge is not that the rule is wrong in principle but that two of its preconditions are fragile in C2A2's actual context: (a) "escalate to a human for the empirical test" presumes a reachable human, which the current review-gate outage contradicts; and (b) "further literature cycles are low-yield" presumes the saturation judgment is reliable after few, automated cycles. Both are conditional failures rather than refutations.

  Specific risks: The rule can convert a tractable literature-stall into an intractable human-stall (PRESUMPTION-245), and can prematurely retire items that would have yielded to a more sensitive human scan.

  Mitigations available: Pair the STALE-flag with an out-of-band escalation path and an SLA/timeout (the REVISE-050 mechanism), and retain a low-frequency (monthly) literature touch rather than full retirement, so a slow literature can still re-open the item.

  STEELMAN:
    Item: ASSUMPTION-223
    Strongest counterargument: A stop-and-escalate rule whose escalation target is structurally unavailable is not a resolution policy but a queue-relabeling policy; it makes the stall *look* actioned ("escalated to Tom") while changing nothing, which is worse than honestly leaving the item OPEN because it hides the failure.
    What would need to be true for C2A2 to be safe: A guaranteed, exercised human endpoint with an SLA, plus a saturation criterion validated against at least one human scan.
    How to test: Track time-to-human-action on STALE escalations; if it diverges (items sit unactioned), the escalation leg is non-operative and the rule needs the REVISE-050 SLA bolt-on.

  Recommendation: PARTIALLY-CHALLENGED
