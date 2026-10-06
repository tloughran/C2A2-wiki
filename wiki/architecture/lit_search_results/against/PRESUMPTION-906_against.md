SEARCH-AGAINST-PRESUMPTION-906:
  Date searched: 2026-09-05
  Original item: PRESUMPTION-906
  Original statement: [inferred] Worker-reported confidence (high 1,255 / med 1,077 / low 70) is calibrated —
    a `high` from batch 3 means the same as a `high` from batch 7, and the distribution is usable as a
    quality signal. (The 92% Loughran prior handed to workers came back at 92.4%.)

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-906
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the absence of any accuracy measurement in the pipeline record and the
        prior/outcome match on `voice`.
      15b: Searched for challenging literature (2026-09-05). NOTE ON AUTHORSHIP: run by the 15c
        orchestrating context after the delegated 15b subagent was interrupted before writing. The same
        context had ALREADY written the 15a files for ASSUMPTION-1256/1261 and PRESUMPTION-910 (different
        items) and had NOT read PRESUMPTION-906_for.md. Search independence for this item holds by
        item; execution independence does not hold by context. Declared.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. "Large Language Models Are Overconfident in Their Own Responses," arXiv:2606.03437 [VERIFIED:
       title/ID; authors NOT verified] — Reports pervasive overconfidence when LLMs verbalise confidence,
       concentrated in the 80–100% band, across models, domains and elicitation strategies. Challenge:
       a `high` label is the modal output regardless of correctness, so 1,255 `high` is what the mechanism
       produces, not evidence of 1,255 correct labels.
    2. "Wired for Overconfidence," arXiv:2604.01457 [VERIFIED: title/ID; authors NOT verified] — Locates
       verbalised overconfidence in a stable model-internal mechanism rather than a task-specific
       artefact. Challenge: cross-batch comparability is not the problem; all eight batches share the
       same bias, so `high` is consistently inflated everywhere, which is worse for the presumption than
       inconsistency would be — the signal is uniformly uninformative rather than noisily informative.
    3. "Assessing and Mitigating Miscalibration in LLM-Based Social Science Measurement," arXiv:2605.11954
       [VERIFIED: title/ID; authors NOT verified] — Post-training and RLHF exacerbate miscalibration;
       instruction-tuned models are worse calibrated than base models; verbalised approaches are
       "systematically biased and poorly correlated with correctness." Directly on the use case
       (classification for measurement).
    4. "Before You Interpret the Profile: Validity Scaling for LLM Metacognitive Self-Report,"
       arXiv:2604.17707 [VERIFIED: title/ID; authors NOT verified] — Argues LLM self-report needs validity
       scales before interpretation, by analogy with psychometrics. Challenge: the pipeline interprets
       the profile (70 `low` = the review set) with no validity scale.
    5. "Anchoring Bias in LLM-as-a-Judge Systems: Prior Scores Compromise Evaluation Independence,"
       arXiv:2608.25869 [VERIFIED: title/ID/abstract figures; authors NOT verified] — 7 of 8 models show
       significant anchoring across 192,000 evaluations; on categorical data with human ground truth,
       anchored metadata blocks 48% of error corrections and flips 10.18% of correct judgments toward
       the supplied label; neither chain-of-thought nor a "disregard the metadata" warning removes the
       effect. Challenge to the 92%→92.4% reading: this is the signature of anchoring, and the
       literature says the coincidence cannot be disambiguated from calibration by inspection.
    6. "Human bias in AI models? Anchoring effects and mitigation strategies in large language models,"
       Journal of Behavioral and Experimental Finance 2024, S2214635024000868 [VERIFIED: title/journal/ID;
       authors NOT verified] — Prior prompting with a lower anchor lowers estimates in most or all
       variables for all four models tested. Same direction.

  Strength of challenge: Strong

  Summary: The 2024–2026 calibration literature is close to unanimous that verbalised LLM confidence is
  systematically overconfident, that the overconfidence is a model-internal mechanism aggravated by RLHF,
  and that it correlates poorly with correctness in classification-for-measurement settings. That
  undercuts the presumption on both limbs. Cross-batch comparability is not rescued by the batches
  sharing a model: they share the bias, so `high` is uniformly inflated and the 70-cell `low` tail is a
  floor on the error set, not an estimate of it. Separately, the anchoring literature makes the 92%→92.4%
  match evidence of anchoring at least as readily as evidence of calibration, and reports that warnings
  and chain-of-thought do not remove the anchor. No source found supports interpreting a verbalised
  confidence distribution as a quality signal without a gold-sample check.

  Specific risks:
    - The review set (70 `low`) is chosen by the least reliable field in the output; errors among the
      1,255 `high` are invisible by construction.
    - Per-node counts in toc_sandbox.csv inherit an unknown error rate that the confidence column cannot
      bound.
    - The 92.4% `voice` result is being read as validation of the pipeline when it may be the prior
      echoed back.
    - The eight-batch design multiplies the same bias eight times rather than averaging it out.

  Mitigations available:
    - A 50-cell blind gold sample (already named by 14b) stratified across `high`/`med`/`low` and across
      batches; report accuracy per stratum. This is the only measurement that settles the question.
    - Re-run a sample without the 92% prior in the prompt and compare `voice` distributions.
    - Replace or supplement verbalised confidence with agreement between two decorrelated workers
      (PREMISE-197 territory) as the quality signal.

  Search scope: Preliminary — 3 queries (verbalised-confidence calibration; anchoring by supplied priors;
  one shared with PRESUMPTION-908). Not covered: the "Just Ask for Calibration" line that reports
  verbalised confidence beating token probabilities (this is 15a's territory; it does not rescue
  cross-batch comparability); the applied social-science annotation literature on confidence-weighted
  inference.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-906
    Strongest counterargument: The confidence column is not a measurement; it is a generation. The model
      that wrote the label also wrote the confidence, from the same forward pass, with a documented
      internal bias toward the 80–100% band that RLHF strengthens. Eight independent batches do not
      average that bias out — they replicate it, so a `high` from batch 3 and a `high` from batch 7 mean
      the same thing only in the sense that both mean little. The one number offered as external
      corroboration, 92.4% against a supplied prior of 92%, is exactly what the anchoring literature
      predicts a prompted model will return, and that literature reports the effect survives explicit
      instructions to ignore the prior. The pipeline has therefore selected its 70-cell review set using
      its least trustworthy output and called the remaining 2,332 cells validated.
    What would need to be true for C2A2 to be safe: A gold sample would have to show accuracy that
      rises monotonically with the confidence label AND is comparable across batches; and the `voice`
      distribution would have to hold when the 92% prior is removed from the prompt.
    How to test: 50-cell blind re-label stratified by confidence and batch (accuracy per stratum);
      50-cell re-run without the prior (compare `voice` rate). Two afternoons of work; both were named
      by 14b already.
