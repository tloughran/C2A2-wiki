SEARCH-AGAINST-PRESUMPTION-541:
  Date searched: 2026-07-25
  Original item: PRESUMPTION-541
  Original statement: [inferred] A second connected Chrome extension is presumed neutral-or-helpful (redundancy = resilience), but it broke unattended delivery by adding a selection ambiguity — a redundant path reduced availability.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: surfaced from a redundant client that degraded delivery
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Standard reliability engineering (parallel redundancy, k-of-n). — Correctly arbitrated redundancy is one of the best-established availability improvements known; the overwhelming default is that a redundant path RAISES availability. The observed degradation therefore indicts the MISSING ARBITRATION RULE, not redundancy as such.
    2. Failover/leader-election literature (e.g., quorum, Raft). — The known remedy for "two candidates, which acts?" is a deterministic selection/priority rule. This is a solved problem; the failure is a design omission, not an intrinsic property of a second client.
    3. Human-in-the-loop automation design. — "Requires a human prompt to disambiguate" is an interaction-design defect (no default target), routinely fixed by pre-selecting a primary. The redundancy did not have to reduce availability.

  Strength of challenge: Moderate

  Summary: The challenge is that the presumption generalizes a specific misconfiguration into a property of redundancy. Redundancy reduced availability HERE only because there was no arbitration/priority rule for which extension acts; with a deterministic primary the second client is neutral-to-helpful, as the default reliability result predicts. The lesson is "arbitrate redundant clients," not "redundancy is a hazard."

  Specific risks: Over-reading the presumption could push the system to remove redundancy entirely, losing genuine failover benefit and reintroducing a single point of failure.

  Mitigations available: Designate one extension as primary (deterministic selection); keep the second as a priority-ordered standby. Preserves failover while removing the selection ambiguity.

  STEELMAN:
    Item: PRESUMPTION-541
    Strongest counterargument: The correct engineering framing is that UNARBITRATED redundancy reduced availability; arbitrated redundancy would not. The presumption's headline ("a redundant path reduced availability") is true only under the omitted-arbitration condition, and prescribes the wrong fix if read as "reduce to one path" rather than "add a selection rule."
    What would need to be true for C2A2 to be safe: a deterministic primary-selection rule exists for the two clients.
    How to test: add a primary-selection rule (or pre-select) and confirm unattended delivery resumes with BOTH extensions connected — isolating arbitration from redundancy.

  Recommendation: PARTIALLY-CHALLENGED
