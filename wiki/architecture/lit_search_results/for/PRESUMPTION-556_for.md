SEARCH-FOR-PRESUMPTION-556:
  Date searched: 2026-07-27
  Original item: PRESUMPTION-556
  Original statement: [inferred] "2 INCORPORATE -> PREMISE-127/128" is read as validation, but 14b (surfacing), 15a/15b (searching) and 15c (dispositioning) are the same model on different prompts over one corpus, so an INCORPORATE may record the pipeline agreeing with itself, not external grounding; the concrete per-batch instance of OPEN-139 / PRESUMPTION-536.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-556
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: surfaced from an INCORPORATE disposition read as validation when surfacing, search, and disposition share one model and corpus
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Panickssery, A. et al. (2024), "LLM Evaluators Recognize and Favor Their Own Generations," NeurIPS 2024, arXiv:2404.13076; Wataoka & Takahashi (2024), "Self-Preference Bias in LLM-as-a-Judge," arXiv:2410.21819. — Direct empirical evidence that a model evaluating outputs from the same/related model systematically favors them; the disposition step (15c) judging content surfaced/searched by the same model is the paradigm case. An INCORPORATE can partly record self-preference.
    2. "Correlated Errors in Large Language Models," arXiv:2506.07962 (OpenReview kzYq2hfyHB). — Same/similar models make correlated errors; a judge inflates accuracy when it shares the generator's mistake (agreement on a wrong answer counts as correct). Under a shared failure model, the evaluator's agreement adds little information about correctness beyond the generator's own claim — the pipeline can agree with itself on an error.
    3. Krogh & Vedelsby (1995), "Neural Network Ensembles, Cross Validation, and Active Learning"; Dietterich (2000), "Ensemble Methods in Machine Learning." — Ensemble error decreases only to the extent members are DECORRELATED; identical members give no error reduction ("ensemble monoculture"). Same-model-different-prompt roles are a low-diversity ensemble, so agreement across 14b/15a/15b/15c is weak independent corroboration.

  Strength of support: Strong

  Summary: Strongly supported. The self-preference literature shows a model judging same-model content favors it; the correlated-errors literature shows agreement between same/similar models is low-information about correctness because errors are shared; and ensemble theory shows corroboration is only as strong as member decorrelation. Since 14b/15a/15b/15c are one model under different prompts over one corpus, an INCORPORATE records, at least in part, the pipeline agreeing with itself rather than external grounding. This is the per-batch instance of OPEN-139 / PRESUMPTION-536 and reinforces REVISE-246 (a validation standard must name a referent external to the pipeline). Note: dispositions that DO cite external literature or in-house empirical tests (e.g., PREMISE-129 below rests on proof theory + external LLM-limitation papers) partially escape this critique; dispositions resting only on intra-pipeline agreement do not.

  Caveats: Not every same-model multi-role step is worthless — decomposition into surfacing/for/against/disposition can surface considerations a single pass misses (see 15b), and WebSearch/in-house tests inject genuine external referents. The supported claim is that INCORPORATE is not self-certifying evidence of external validity absent a named external referent.

  Recommendation: SUPPORTED
