SEARCH-AGAINST-PRESUMPTION-387:
  Date searched: 2026-06-25
  Original item: PRESUMPTION-387
  Original statement: "That the adjudicator model is itself competent/unbiased at judging semantic agreement (its error rate not made a measured input)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-387
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: adjudicator reliability is assumed rather than measured; ties OPEN-090
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Zheng et al. 2023 (LLM-as-judge, bias side). - Documents position bias, verbosity bias, and self-enhancement bias in LLM judges.
    2. 'Self-Preference Bias in LLM-as-a-Judge' (arXiv 2410.21819). - LLM judges systematically favor their own/own-family generations; self-recognition correlates with self-preference (10-25% inflation).
    3. Position-bias studies (CalibraEval, arXiv 2410.15393). - Up to ~75% preference for first-positioned response; selection bias must be calibrated out.
    4. Scoring-bias evaluations (arXiv 2506.22316). - LLM judges show systematic scoring biases vs human labels.

  Strength of challenge: Strong

  Summary: The presumption - that the adjudicator is competent/unbiased and its error need not be measured - is strongly challenged by the LLM-as-judge literature. Judges exhibit position bias, verbosity bias, and self-preference bias, and their agreement with humans varies by task; treating the adjudicator as a trusted oracle whose error is not an input ignores documented, sometimes large, systematic biases. If the adjudicator decides what counts as 'agreement', its biases propagate into BOTH the consensus and dissensus outputs - the adjudicator is the whole contract.

  Specific risks: Adjudicator bias silently determines the detector's headline outputs; e.g., position/verbosity bias could systematically mislabel agreement, and an unmeasured error rate makes consensus and dissensus uninterpretable.

  Mitigations available: Calibrate the adjudicator against human labels; swap-and-average to cancel position bias; use a different model family than the columns to limit self-preference; make adjudicator error a reported input.

  STEELMAN:
    Item: PRESUMPTION-387
    Strongest counterargument: An adjudicator with unmeasured, documented biases (position, verbosity, self-preference) is not a neutral instrument; since it defines 'agreement', its error rate is not optional metadata but a primary determinant of every downstream number.
    What would need to be true for C2A2 to be safe: The adjudicator's agreement with human labels is measured, acceptable, and de-biased (position-swapped, cross-family).
    How to test: Benchmark the adjudicator against a human-labeled agreement set; measure position/verbosity/self-preference effects; report its error rate.

  Search scope: LLM-as-judge bias and calibration. Comprehensive.

  Recommendation: CHALLENGED
