SEARCH-FOR-ASSUMPTION-057:
  Date searched: 2026-04-21
  Original item: ASSUMPTION-057
  Original statement: "17→11 findings filter uses the rule 'Active or Highest Priority, excluding subsumed/downgraded.'"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a — also converts PRESUMPTION-053]
    Original item: ASSUMPTION-057
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Morning walk handoff 2026-04-21 — filter criterion now stated rather than unstated
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Rule-based filtering literature (Hayes-Roth 1985 "Rule-Based Systems"; classic expert-system design): rule-based filters with explicitly documented criteria are well-understood and auditable. Stating the rule is a necessary first step to auditing it. The transition from PRESUMPTION-053 (unstated rule) to ASSUMPTION-057 (stated rule) is literature-endorsed.
    2. Transparency-over-opacity literature (PRISMA 2020; Cochrane reporting standards): filter criteria should be explicitly stated to allow replication and audit. The stated-rule move is consistent with systematic-review reporting standards.
    3. Prioritized-subset literature (Glance, Duda: "active vs. archived" classification; operational research on ticket triage): filtering to "active + highest priority" is a standard pattern for reducing consumer cognitive load. The rule as stated has precedent in bug-tracker, incident-management, and literature-review systems.
    4. C2A2-internal precedent (PREMISE-006 = ASSUMPTION-047, INCORPORATED 2026-04-20): the briefing-layer-epistemic-commitment to transparent flagging endorses stating rules over leaving them implicit. ASSUMPTION-057 is consistent with PREMISE-006.

  Strength of support: Moderate

  Summary: The stated rule — "Active or Highest Priority, excluding subsumed/downgraded" — is a standard filter pattern with precedent in expert systems, literature-review reporting, and ticket triage. Stating the rule is itself an improvement over the prior unstated form (PRESUMPTION-053), consistent with the BRIEFING-LAYER-EPISTEMIC-COMMITMENTS cluster direction and with PREMISE-006 transparent-flagging. However, support is for the rule as a legitimate filter pattern; support is NOT for the rule being correctly applied to the specific case (which requires audit against the 6 excluded findings).

  Caveats: (a) Support is conditional on the rule being audited against its excluded set (FINDING-001, 002, 003, 004, 006, 007, 008, 010); the rule may be stated correctly but applied incorrectly; (b) the stated rule does not specify who adjudicates "subsumed" and "downgraded" — the classification criterion is nested one level deeper and may itself be unaudited; (c) moving from PRESUMPTION to ASSUMPTION is a visibility improvement but not an audit — it means the rule can now be audited, not that it has been.

  Recommendation: PARTIALLY-SUPPORTED (rule pattern has strong precedent; specific application still requires audit against the 6 excluded findings; stating the rule is necessary but not sufficient)
