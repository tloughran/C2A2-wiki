SEARCH-AGAINST-PRESUMPTION-442:
  Date searched: 2026-07-03
  Original item: PRESUMPTION-442
  Original statement: "[inferred] That co-authorship where the same model family generates the dialogue data AND analyzes/writes it up does not compromise evidential independence."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-442
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred unstated evidential-independence premise
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Panickssery, Bowman & Feng, 2024, "LLM Evaluators Recognize and Favor Their Own Generations," NeurIPS. — Models self-recognize and self-prefer their own outputs; when generator and evaluator are the same family, scoring is biased toward the generated text.
    2. "Self-Preference Bias in LLM-as-a-Judge" (arXiv 2410.21819); "Quantifying and Mitigating Self-Preference Bias" (arXiv 2604.22891). — Self-preference persists across architectures and is linked to self-recognition; mitigation requires *not* using the same model to generate and judge.
    3. "Measuring Self-Rating Bias in LLM-Generated Survey Data" (arXiv 2602.13862). — Same-model generation-and-scoring conflates two operations psychometric theory requires to be independent; the evaluation can reflect internal consistency rather than the text's true content.
    4. Shared-method / common-method-bias literature (Podsakoff et al., 2003). — When the same instrument/source produces predictor and outcome, spurious shared-method variance inflates apparent relationships; the classic non-independence failure.

  Strength of challenge: Strong

  Summary: The presumption of preserved independence is strongly challenged. Both the LLM-as-judge literature and classical common-method-bias theory hold that when one source generates the data and also analyzes/evaluates it, the two operations are not independent: self-recognition and self-preference bias the evaluation toward the generated material, and shared-method variance inflates apparent structure. Same-model-family generation-and-analysis is precisely the configuration these literatures warn against.

  Specific risks: The study's measured effects (understanding deltas, the C0 gate verdicts, the write-up's interpretive claims) may partly reflect the model family's internal consistency and self-preference rather than the phenomenon; this compounds P-436 (agent fidelity) and P-440 (allegiance) into a stacked non-independence.

  Mitigations available: Use a *different* model family (or human raters) for scoring/analysis than for generation; blind the evaluator to which agent produced which text; report inter-model agreement as an independence check; treat same-model results as a lower bound pending cross-model replication.

  Recommendation: CHALLENGED

  STEELMAN:
    Strongest counterargument: Not every same-model pipeline is fatally circular: if the analysis is a deterministic, pre-specified computation (counts, clustered CIs) rather than a model-graded judgment, self-preference has limited purchase, and the C0 gate's *verdict* limb (0.93 vs 0.00 strawman) may be robust even if the lexical limb is not. The presumption is dangerous chiefly where model *judgment* enters scoring or interpretation.
    What would need to be true for C2A2 to be safe: Model-graded steps are cross-validated by a different family or humans; deterministic steps are separated from model-judgment steps in reporting; self-preference is measured, not assumed absent.
    How to test: Re-score a sample with an independent model family and with blind human raters; compare to same-family scores. A systematic same-family advantage quantifies the compromised independence.
