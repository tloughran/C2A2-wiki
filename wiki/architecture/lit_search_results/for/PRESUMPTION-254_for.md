SEARCH-FOR-PRESUMPTION-254:
  Date searched: 2026-05-27
  Original item: PRESUMPTION-254
  Original statement: The "review-page state is authoritative over Gmail" rule (ASSUMPTION-230) presumes the review-page UI is itself reliable, but the 3-Wright follow-up showed the UI also misled within the same session; the rule handles the email-misfire case but not the UI-misfire case.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-254
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced — UI-reliability presumption embedded in ASSUMPTION-230.
      15a: Searched for supporting literature on system-of-record selection when redundant channels diverge.
    Current status: SUPPORTED (Moderate)

  Sources:
    1. Kimball & Ross (2013) — system-of-record selection IS the standard pattern; the presumption surfaces a real pattern that the source rule rests on.
    2. Fowler PEAA — Single Source of Truth requires the SoT itself be reliable; when SoT can also mislead, a 3-way reconciliation pattern is needed.
    3. Nielsen (1993) Usability Engineering — UI-state vs underlying-data divergence is a documented HCI failure mode; "what the user sees" and "what the system stores" are distinct.
    4. C2A2-internal: the 3-Wright case is internal precedent for UI-misfire.

  Strength of support: Moderate

  Summary: System-of-record selection is the right pattern (FOR-supports ASSUMPTION-230's direction); but the supportive case ALSO requires the SoR itself be reliable, which the 3-Wright case shows it is not always. The presumption is structurally correct: the rule handles the email-misfire case but presumes UI reliability that may not hold.

  Caveats: (a) The support here is for the presumption's *diagnostic claim*, not for any specific remedy; (b) the right remedy is 3-way reconciliation (email + UI + verbal intent), not UI-as-authoritative full stop.

  Recommendation: SUPPORTED (Moderate; the diagnostic claim is well-supported)
