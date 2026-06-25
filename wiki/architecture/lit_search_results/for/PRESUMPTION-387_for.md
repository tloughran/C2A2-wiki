SEARCH-FOR-PRESUMPTION-387:
  Date searched: 2026-06-25
  Original item: PRESUMPTION-387
  Original statement: "That the adjudicator model is itself competent/unbiased at judging semantic agreement (its error rate not made a measured input)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-387
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: the adjudicator's reliability is assumed rather than measured; ties OPEN-090
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Zheng et al. 2023. 'Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.' NeurIPS. - Strong LLM judges reach ~80%+ agreement with human preference, matching human-human agreement on some tasks - i.e., adjudicators CAN be competent.
    2. LLM-as-a-judge surveys (2024-2025): on constrained tasks (e.g., entailment/agreement judgments with clear rubrics), judge-human agreement can be high.

  Strength of support: Moderate

  Summary: There is moderate support that an LLM adjudicator can be competent at agreement/entailment judgments: on well-specified tasks, strong judges match human-level agreement rates. This makes the presumption's hope (a usable adjudicator) attainable in principle. However, 'competent' is conditional on task, rubric, and calibration - and crucially the literature treats judge reliability as something to be MEASURED, which is the opposite of the presumption's implicit move (assume it). Support is for feasibility, not for leaving error unmeasured.

  Caveats: Competence is task- and rubric-dependent and coexists with documented biases (15b). The literature endorses measuring the judge against human labels - precisely making its error rate an input - rather than presuming it.

  Search scope: LLM-as-judge human-agreement rates. Adequate.

  Recommendation: PARTIALLY-SUPPORTED
