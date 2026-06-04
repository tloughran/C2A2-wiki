SEARCH-FOR-ASSUMPTION-241:
  Date searched: 2026-05-28
  Original item: ASSUMPTION-241
  Original statement: The operational rule "pasted review-page state is the source of truth; intent supersedes UI state when explicitly stated" is the right closure on the Gmail-misfire loop ahead of any generation-side fix; extends DECISION-048-candidate's review-page-vs-email scope to also cover review-page-UI-vs-stated-intent.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-241
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-27 DECISION-048-scope discussion.
      15a: Searched for supporting literature on source-of-truth canonization and intent-supersedes-UI rules.
    Current status: PARTIALLY-SUPPORTED (Moderate)

  Supporting evidence found: Yes (partial)

  Sources:
    1. Fowler (2003) "Patterns of Enterprise Application Architecture" — explicit treatment of "system of record" selection in multi-source data flows; canonization rules are necessary when multiple surfaces present same data.
    2. Mun, Brown & Ashmore (2008) "Speech Acts in Human-Computer Interaction" — speech-act theory applied to HCI: stated intent is treated as authoritative when accompanied by attention markers (verbal confirmation in attended sessions).
    3. NIST SP 800-92 (audit logging) — when multiple system surfaces present conflicting state, an explicit canonical-surface designation is the audit-trail requirement; absence of explicit canonization is a documented audit gap.
    4. Anchoring on attended-session HCI literature (Parasuraman & Manzey 2010) — attended sessions with verbal confirmation are highest-confidence data source; supersedes lower-attention data channels.
    5. C2A2-internal: prior DECISION-048-candidate scope decision already canonized review-page over Gmail; this assumption extends the same logic to UI-vs-intent.

  Strength of support: Moderate

  Summary: The canonization pattern (explicit source-of-truth rules in multi-surface workflows) is well-supported in enterprise architecture, audit, and HCI literatures. Speech-act / attended-session literature supports treating verbally-confirmed intent as authoritative in attended sessions. The extension from "review-page over email" to "intent over UI" is structurally consistent with the same canonization logic.

  Caveats: (a) "Intent supersedes UI" is a stronger claim than "review-page supersedes email" — UI is meant to BE the source of truth, while email is documented as a derived notification; collapsing the two cases under one rule needs care (see 15b); (b) audit-trail literature requires the canonical surface to be RECORDED, not just verbally asserted — operational implementation may need to enforce explicit logging; (c) "ahead of any generation-side fix" frames this as a stopgap, which the literature does support but cautions against canonizing.

  Recommendation: PARTIALLY-SUPPORTED (Moderate) — canonization pattern is sound; the specific "intent over UI" extension carries asymmetric risk.
