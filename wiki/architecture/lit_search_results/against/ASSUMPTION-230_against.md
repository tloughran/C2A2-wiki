SEARCH-AGAINST-ASSUMPTION-230:
  Date searched: 2026-05-27
  Original item: ASSUMPTION-230
  Original statement: When Gmail decision-email body and review-page state disagree, review-page state is authoritative; the email body is non-authoritative until the decision-email generator is fixed.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-230
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted.
      15b: Searched for challenging literature on UI-vs-email-mismatch handling.
    Current status: PARTIALLY-CHALLENGED (Weak-Moderate)

  Sources:
    1. Nielsen (1993) — UI-state-as-authoritative has documented failure modes (rendering bugs, state-display lag); UI-misfire is at least as common as email-misfire.
    2. Distributed-systems literature (Nygard 2007) — when multiple views diverge, neither may be the system-of-record; the SoR is the underlying store, not any view.
    3. C2A2-internal: PRESUMPTION-254 surfaces this directly — the 3-Wright case shows UI also misled.
    4. Audit literature — best practice is 3-way reconciliation (intent + UI + email + log) for any approval workflow, not 2-way priority.

  Strength of challenge: Weak-Moderate

  Summary: The challenge is bounded but real: UI-authoritative is a defensible 2-way rule but a 3-way reconciliation pattern (intent + UI + email + log) is closer to industrial best practice. The assumption is too narrow.

  Specific risks: (a) UI-misfire (PRESUMPTION-254) defeats the rule; (b) ossifying UI-as-authoritative may delay fixing the deeper generator-divergence issue.

  Mitigations available: (a) 3-way reconciliation rule; (b) fix the underlying generator-divergence; (c) explicit intent log per session.

  Recommendation: PARTIALLY-CHALLENGED (Weak-Moderate)

  STEELMAN:
    Item: ASSUMPTION-230
    Strongest counterargument: UI is no more reliable than email; the 3-Wright case proves UI can mislead too. The right pattern is 3-way reconciliation, not 2-way priority.
    What would need to be true for C2A2 to be safe: Documented intent log; 3-way reconciliation rule when channels diverge; underlying generator fixed.
    How to test: Sample divergence events; check whether UI was always correct. Likely not.
