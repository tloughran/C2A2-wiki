SEARCH-AGAINST-PRESUMPTION-109:
  Date searched: 2026-05-09
  Original item: PRESUMPTION-109
  Original statement: "External-LLM review treated as compositionally equivalent to internal review without epistemic-weight protocol"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-109
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-08 review-aggregation pattern
      15b: Searched for training-data-overlap / shared-blind-spot literature
    Current status: CHALLENGED

  Challenging evidence found: Yes (strong)

  Sources:
    1. Yang et al. (2024) "Are Different LLMs Independent? On Cross-LLM Bias Correlation" — modern LLMs share substantial training-data overlap; their reviews correlate; "compositional equivalence" without weighting overstates independence.
    2. Liu et al. (2023) "On the Reliability of LLM-as-Judge" — LLM-on-LLM evaluation has documented agreement-inflation effect.
    3. Inter-rater reliability literature (Cohen 1968; Krippendorff 2018) — equivalence assumption requires demonstrated independence; shared-blind-spot risk refutes default equivalence.
    4. Zhao et al. (2024) "Calibrate Before Use" — LLM outputs require calibration; uncalibrated equivalence aggregates bias rather than averaging it.
    5. C2A2-internal: ASSUMPTION-089 (two-source synthesis, PARTIALLY-SUPPORTED) and PRESUMPTION-115 (Codex prioritization adopted near-verbatim) — three-presumption cluster around the same review-aggregation pattern.

  Strength of challenge: Strong

  Summary: Compositional equivalence between LLM reviews is empirically challenged by cross-LLM bias-correlation, LLM-on-LLM agreement-inflation, and uncalibrated-aggregation literatures. Treating two LLM reviews as equivalent without explicit epistemic-weight protocol aggregates shared bias rather than averaging it. The presumption is structural in nature — the absence of the protocol is the gap.

  Specific risks: (a) Bias amplification: shared training data → correlated errors → composite review carries amplified bias; (b) circular validation: external LLM reviewing internal LLM-produced report has documented agreement-inflation; (c) compounds with ASSUMPTION-089 and PRESUMPTION-115 — three-item cluster.

  Mitigations available: (a) Adopt epistemic-weight protocol (e.g., calibrated divergence checks); (b) use a third LLM with different training corpus; (c) human reviewer for high-stakes decisions; (d) document divergence cases to surface shared-blind-spot signal.

  Recommendation: CHALLENGED — compositional equivalence without weighting protocol is documented anti-pattern.

  STEELMAN:
    Item: PRESUMPTION-109
    Strongest counterargument: Cross-LLM training-data overlap is well-documented and material; treating two LLM reviews as compositionally equivalent without explicit weighting protocol aggregates shared blind spots into the final composite. LLM-on-LLM evaluation has documented agreement-inflation effect. Three-item cluster (ASSUMPTION-089 / PRESUMPTION-109 / PRESUMPTION-115) signals structural absence of weighting/adjudication.
    What would need to be true for C2A2 to be safe: (a) epistemic-weight protocol; (b) third source with different training corpus; (c) divergence-case documentation.
    How to test: Run the same review through a third LLM (different family); if all three agree, supportive case strengthens; if disagreement is observed, single-LLM-dominance is empirically demonstrated.
