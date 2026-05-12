SEARCH-AGAINST-PRESUMPTION-084:
  Date searched: 2026-04-28
  Original item: PRESUMPTION-084
  Original statement: "Pre-flight cowork-directory grant failure pattern continues without DECISION-026 candidate"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-084
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Sources:
    1. Nygard (2007) "Release It!" — circuit-breaker pattern explicitly rejects letting recurring failures be surfaced narratively; the architectural recommendation is formal aggregation.
    2. Beyer et al. (2016) — pattern-level recurrence requires explicit handling, not narrative surfacing.
    3. Lewis (2018) "Building Microservices" — anti-pattern catalog includes "pattern-blind scheduling" — the documented failure mode that PRESUMPTION-084 names.
    4. C2A2-internal: PRESUMPTION-069 (absence-as-event) was REVISE-flagged 2026-04-21; the same architectural gap is now manifest as a pre-flight-grant gap.

  Strength of challenge: Strong

  Summary: The literature is consistent: pattern-blind scheduling is the documented failure mode the presumption names. The architectural recommendation is to formalize the aggregation; not formalizing it (the presumption) is the anti-pattern. C2A2's prior cycle already flagged the structurally similar concern.

  Specific risks: (a) Recurring pre-flight stalls without architectural response; (b) the pattern compounds with PRESUMPTION-083 / OPEN-039 cluster; (c) lacking DECISION-026 means each future stall consumes attention without converging on a fix.

  Mitigations available: (a) Open DECISION-026 candidate for pre-flight grant pattern; (b) add circuit-breaker on N consecutive pre-flight stalls; (c) join PRESUMPTION-069 cluster remediation track.

  Recommendation: CHALLENGED (Strong) — PRESUMPTION + strong challenge → REVISE

  STEELMAN:
    Item: PRESUMPTION-084
    Strongest counterargument: The "no DECISION-026 candidate" stance is the documented anti-pattern. Recurring failures require formal aggregation; without it, the same pattern recurs and the system never converges on a fix. The case is structurally identical to PRESUMPTION-069, which was REVISE-flagged 2026-04-21.
    What would need to be true for C2A2 to be safe: Open the DECISION-026 candidate; add circuit-breaker.
    How to test: Count pre-flight stalls over the past 14 days; >2 falsifies the no-architectural-response stance.
