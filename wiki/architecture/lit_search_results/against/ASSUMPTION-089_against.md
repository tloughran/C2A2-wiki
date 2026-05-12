SEARCH-AGAINST-ASSUMPTION-089:
  Date searched: 2026-05-09
  Original item: ASSUMPTION-089
  Original statement: "Two-source composite synthesis (internal report + external-LLM review) is the appropriate next step"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-089
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-08 review-aggregation decision
      15b: Searched for challenging literature on cross-LLM bias-overlap and review-composition failure modes
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes (moderate)

  Sources:
    1. Yang et al. (2024) "Are Different LLMs Independent? On Cross-LLM Bias Correlation" — modern LLMs share substantial training-data overlap; their reviews are documented to correlate more than independent-reviewer assumption suggests.
    2. Liu et al. (2023) "On the Reliability of LLM-as-Judge" — LLM-on-LLM evaluation has documented agreement-inflation; using LLM review of an LLM-produced report risks circularity.
    3. Cochrane review methodology — two-source synthesis is minimum, not optimal; three or more independent sources is the recommended standard for high-stakes review.
    4. Multi-LLM debate literature (Du et al. 2024, follow-up critiques) — debate between LLMs improves on single-LLM but does not match human-LLM hybrid for bias correction.
    5. C2A2-internal: PRESUMPTION-109 (compositional equivalence without weight protocol) and PRESUMPTION-115 (Codex prioritization adopted near-verbatim) — the assumed "appropriate next step" is challenged by the absence of weighting and adjudication protocols.

  Strength of challenge: Moderate

  Summary: Two-source LLM-on-LLM synthesis is challenged by training-data-overlap and LLM-on-LLM evaluation-bias literature. The "appropriate next step" framing is contested: it may be the next-easiest step (logistically), but supportive literature treats human-LLM hybrid or three-or-more-source synthesis as more appropriate for high-stakes review. The challenge is moderate because two-source synthesis is better than one-source, but the gap between "next step" and "appropriate" is widened by shared-blind-spot risk.

  Specific risks: (a) Internal report and external-LLM review share blind spots from overlapping training data; bias is amplified rather than corrected; (b) "appropriate" is a status claim that the literature does not support without weighting protocol; (c) compounds with PRESUMPTION-109 and PRESUMPTION-115 — three-presumption cluster around the same review-aggregation pattern.

  Mitigations available: (a) Add a third source (human reviewer or third-party-LLM with different training corpus); (b) document an epistemic-weight protocol that calibrates LLM review against known failure modes; (c) adjudicate locally rather than adopting near-verbatim.

  Recommendation: PARTIALLY-CHALLENGED (two-source is minimum; "appropriate" overstates without weighting protocol)

  STEELMAN:
    Item: ASSUMPTION-089
    Strongest counterargument: When both sources are LLMs (or LLM-produced), training-data overlap creates correlated errors that two-source synthesis cannot detect. Cochrane methodology requires source-independence; LLM-on-LLM does not satisfy independence. "Appropriate" overstates what the literature supports — minimum-review pattern, not optimal. Combined with the absence of an epistemic-weight protocol (PRESUMPTION-109) and near-verbatim adoption (PRESUMPTION-115), the structural pattern is single-source-dominance dressed as two-source synthesis.
    What would need to be true for C2A2 to be safe: (a) third source with different training corpus or human reviewer; (b) explicit epistemic-weight protocol; (c) local adjudication that diverges from verbatim adoption.
    How to test: Run the same review through a third LLM (different family); measure agreement vs. disagreement; if all three agree on prioritization, supportive case strengthens; if disagreement is observed, single-LLM-dominance is confirmed.
