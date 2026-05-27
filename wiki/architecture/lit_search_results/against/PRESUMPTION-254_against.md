SEARCH-AGAINST-PRESUMPTION-254:
  Date searched: 2026-05-27
  Original item: PRESUMPTION-254
  Original statement: The "review-page state is authoritative over Gmail" rule presumes the review-page UI is itself reliable, but the 3-Wright follow-up showed the UI also misled within the same session.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-254
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced.
      15b: Searched for challenging literature on UI-state failure modes.
    Current status: CHALLENGED (Moderate — challenge supports the presumption)

  Sources:
    1. Nielsen (1993) "Usability Engineering" — UI-state vs underlying-data divergence is canonical HCI failure mode.
    2. Distributed-systems literature (Nygard 2007) — when multiple views diverge, the SoR is the underlying store, not the view.
    3. Audit literature — 3-way reconciliation (intent + UI + email + log) is industrial best practice for approval workflows.
    4. C2A2-internal: the 3-Wright follow-up case is direct empirical evidence.

  Strength of challenge: Moderate (sustains the presumption)

  Summary: The challenge to the presumption is essentially "UI is usually right" — Weak. The presumption's claim (UI can also fail) is empirically demonstrated by the 3-Wright case AND supported by HCI literature.

  Specific risks: (a) Treating UI as reliable in the assumption may delay fixing the deeper generator-divergence; (b) the 2-way rule fails on UI-misfire days.

  Mitigations available: (a) 3-way reconciliation; (b) underlying-store as SoR.

  Recommendation: CHALLENGED (Moderate; presumption sustained)

  STEELMAN:
    Item: PRESUMPTION-254
    Strongest counterargument (to the presumption): UI is right most of the time; treating it as authoritative is a practical heuristic.
    What would need to be true for C2A2 to be safe (if relying on UI-authoritative): UI bug rate must be near zero; the 3-Wright case suggests it is not.
    How to test: Audit UI-vs-store discrepancies over time. >0 means the UI-authoritative rule is unsafe.
