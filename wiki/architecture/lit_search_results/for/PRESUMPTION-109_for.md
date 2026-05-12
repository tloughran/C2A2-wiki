SEARCH-FOR-PRESUMPTION-109:
  Date searched: 2026-05-09
  Original item: PRESUMPTION-109
  Original statement: "External-LLM review treated as compositionally equivalent to internal review without epistemic-weight protocol"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-109
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-08 review-aggregation pattern: external-LLM (Codex) review weighted equally with internal C2A2 report
      15a: Searched for supporting literature on multi-LLM review-aggregation and cross-model bias-correlation
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Yes (weak — supportive only on equivalence-as-default; literature requires weighting protocol)

  Sources:
    1. Wang et al. (2023) "Self-Consistency"; Du et al. (2024) "Improving Factuality and Reasoning via Multi-Agent Debate" — multi-LLM aggregation works when models have non-correlated errors; equivalence is the default starting point before weight calibration.
    2. Inter-rater reliability literature (Cohen 1968; Krippendorff 2018) — equivalence-as-default is canonical for unweighted aggregation; weighting requires explicit protocol.
    3. ML-ensemble literature (Dietterich 2000 "Ensemble Methods in Machine Learning") — equal-weight ensembles are baseline; weighted ensembles dominate baseline only when calibration data exists.
    4. C2A2-internal: ASSUMPTION-089 (two-source composite synthesis, PARTIALLY-SUPPORTED) and PRESUMPTION-014 / PRESUMPTION-020 cross-tradition signal validity cluster — equivalence-as-default is consistent with prior framings, but weighting protocol is the standard guard.

  Strength of support: Weak

  Summary: "Compositional equivalence" between external-LLM and internal review has weak default support: equal-weight aggregation is the literature baseline, and the absence of calibration data justifies the default. However, this is supportive only as a baseline — the literature uniformly requires an epistemic-weight protocol to convert baseline into operational discipline. Without that protocol, the presumption is operationally fragile under the same shared-blind-spot conditions that cross-LLM literature flags.

  Caveats: (a) Equivalence-as-default applies before evidence of differential reliability; the literature treats the default as a starting point, not as endpoint; (b) shared-blind-spot risk (Codex 5.5 trained on overlapping data with the LLM that produced the internal report) is documented and not addressed by the presumption (this is PRESUMPTION-115 territory); (c) the explicit absence of an epistemic-weight protocol is the structural gap — the presumption is not "wrong" in the small but is unsafe to operate at scale.

  Recommendation: PARTIALLY-SUPPORTED (equivalence-as-default has baseline literature support; epistemic-weight protocol is the canonical guard, currently absent)
