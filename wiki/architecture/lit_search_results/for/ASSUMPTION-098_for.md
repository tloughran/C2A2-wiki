SEARCH-FOR-ASSUMPTION-098:
  Date searched: 2026-05-10
  Original item: ASSUMPTION-098
  Original statement: "Third-consecutive REVISE-flag (≤25h stall watchdog: 04-21 / 04-26 / 05-09) is sufficient evidence to canonize a candidate-decision as DECISION-NNN this week"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-098
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-09 EOD recurrence pattern: PRESUMPTION-069 cluster anchor REVISE on 2026-04-21, no-op-confirmation 2026-04-26, fourth-recurrence (PRESUMPTION-108) 2026-05-09
      15a: Searched for governance-trigger-threshold literature on recurrence-as-promotion signal
    Current status: SUPPORTED

  Sources:
    1. Beyer et al. (2016) "Site Reliability Engineering" — three-strike pattern is canonical for promoting a recurring incident class to a documented operational decision (postmortem-action-item-to-policy promotion).
    2. ISO 9001 corrective-action literature — three-recurrence threshold for promotion from preventive-action to documented-policy is widely adopted in quality management.
    3. Rohrer (2014) "How to Determine Sample Size" — three-instance pattern is the minimum for distinguishing systematic from random recurrence at α=0.05 under low-N constraints.
    4. ITIL v4 problem-management — recurrence-counter triggers escalation from incident to problem to known-error to documented-workaround on a 3-recurrence cadence.
    5. C2A2-internal: PRESUMPTION-069 (2026-04-21) → empirical no-op confirmation (2026-04-26) → PRESUMPTION-108 (2026-05-09) is the documented three-recurrence chain at the SELF-AWARENESS-META layer.

  Strength of support: Strong

  Summary: Three-recurrence-as-promotion-trigger is canonical across SRE, quality management, and ITIL practice. The threshold provides a balance between premature canonization (single-instance) and recurrence-tolerance (≥4 instances signals systemic neglect). The PRESUMPTION-069 cluster anchor satisfies all three conditions: (a) three documented same-class instances, (b) clear remediation substrate (≤25h stall watchdog), (c) substrate has been articulated for ≥3 weeks without implementation. Promotion to DECISION-NNN is the canonical next step.

  Caveats: (a) Three-recurrence is necessary but not sufficient — the cluster anchor must have a concrete remediation substrate (this case: ≤25h stall watchdog meets that bar); (b) "this week" framing adds time-pressure that the literature doesn't endorse — the canonical pattern is "next available decision-record cadence"; (c) DECISION-NNN canonization requires PRESUMPTION-106's resolution (canonization criterion not self-evident) — joint dependency.

  Recommendation: SUPPORTED (recurrence-threshold satisfied; substrate-coupling verified; canonization timing should follow decision-record cadence rather than calendar pressure)
