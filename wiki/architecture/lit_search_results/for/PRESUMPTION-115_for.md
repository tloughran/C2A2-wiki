SEARCH-FOR-PRESUMPTION-115:
  Date searched: 2026-05-09
  Original item: PRESUMPTION-115
  Original statement: "Codex 5.5 prioritization adopted near-verbatim without project-context adjudication"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-115
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-08 review-aggregation: external-LLM prioritization adopted near-verbatim
      15a: Searched for supporting literature on review-aggregation frameworks weighting reviewers by domain familiarity
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No (extension of PRESUMPTION-074 SYSTEMIC-RISK at external-tool-review layer)

  Sources:
    1. Inter-rater reliability literature (Cohen 1968; Krippendorff 2018) — adoption of one rater's judgment as authoritative requires demonstrated reliability advantage; near-verbatim adoption without weighting is documented anti-pattern.
    2. Multi-LLM review-aggregation (Wang et al. 2023; Du et al. 2024) — ensemble methods endorse weighted aggregation calibrated by reviewer-domain familiarity; near-verbatim adoption from single external review is documented as reviewer-dominance.
    3. Software-architecture review literature (Bass et al. 2012) — external review is endorsed as input to local adjudication; adoption-without-adjudication is documented anti-pattern.
    4. Domain-familiarity literature (Dreyfus & Dreyfus 1980; Klein 2008) — reviewers without project context cannot be authoritative on prioritization; adjudication step is canonical.
    5. C2A2-internal: PRESUMPTION-074 (specialist-self-attribution as primary signal, REVISE; SYSTEMIC-RISK 2026-04-27) — recurrence at external-tool-review layer; same structural failure mode (one source treated as primary signal).

  Strength of support: None — adoption-without-adjudication is documented anti-pattern.

  Summary: Supportive literature for "near-verbatim adoption of external-LLM prioritization without project-context adjudication" does not exist. Inter-rater, multi-LLM, software-architecture, and domain-familiarity literatures all require local adjudication when external reviewers lack project context; adoption-without-adjudication is documented reviewer-dominance. The presumption is the recurrence of PRESUMPTION-074 at a new operational layer (external-tool-review) and confirms the SYSTEMIC-RISK pattern flagged 2026-04-27.

  Caveats: (a) Operationally, near-verbatim adoption sometimes works when external reviewer is highly aligned with project context — but Codex 5.5 has no specific project-context channel; alignment is presumed rather than demonstrated; (b) the presumption pairs with ASSUMPTION-089 (two-source synthesis, PARTIALLY-SUPPORTED) and PRESUMPTION-109 (compositional equivalence) — all three together compound the structural gap; (c) NO-SUPPORT here is uniformly active recommendation against the pattern.

  Recommendation: NO-SUPPORT-FOUND — local-adjudication is canonical; recurrence of PRESUMPTION-074 SYSTEMIC-RISK at external-tool-review layer
