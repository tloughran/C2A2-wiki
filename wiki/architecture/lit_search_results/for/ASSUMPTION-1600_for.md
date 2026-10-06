SEARCH-FOR-ASSUMPTION-1600:
  Date searched: 2026-09-22
  Original item: ASSUMPTION-1600
  Original statement: "Those controls can't detect blindness to a form they don't use" — a probe
    validated against a control set that shares its blind spot is not validated.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-1600
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted a hypothesis that invalidates a control-validated instrument.
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Findings on LLM-as-judge / evaluator blind-spot propagation (see "Finding Blind Spots in
       Evaluator LLMs with Interpretable Checklists," arXiv:2406.13439; and related 2026 discussion of
       LLM-judge reasoning blind spots, e.g. coverage of the "dice problem" finding that "a benchmark
       scored by a language model and a reward model trained on that model's preferences can agree
       completely and both be wrong in the same direction"). — Near-direct match: an evaluator built
       from, or correlated with, the same mechanism as the system it checks inherits that system's
       blind spot, so agreement between the two is not evidence of correctness.
    2. Psychometric validation-methodology literature on "modality bias," summarized in search results
       tied to work on validating LLM/behavioral instruments: "validation instruments might share
       similar biases with the instruments being validated, and such validation pipelines can appear
       well-validated against text-based criteria while failing to track other intended outcomes...
       shared across judges." — Directly supports the claim's structure: a control/validation set that
       shares the target's blind spot yields false confidence rather than genuine validation.
    3. General epidemiological/psychometric methodology principle (case-control study design guidance,
       e.g. discussion in "Assessing Bias in Case-Control Studies" and standard measurement-validity
       texts): "when no gold standard method is available, it is desirable that the comparison method
       relies on a different type of measurement... to avoid introducing correlated errors." — Classic,
       well-established methodological grounding: validating an instrument against a comparison that
       shares its measurement mechanism risks correlated error, undermining the validation.

  Strength of support: Strong

  Summary: This is the best-supported item in the cohort. The claim's core logic — that a control or
    validation set sharing the same structural blind spot as the instrument under test cannot certify
    that instrument against that blind spot — has a close, current analog in the LLM-evaluator
    literature (evaluators inheriting the reasoning failures of the models they grade) and a classical
    grounding in measurement methodology (the correlated-error principle in case-control and
    psychometric validation design, which explicitly recommends comparison methods that do NOT share
    the same measurement mechanism). Both limbs of the claim (the negative claim "can't detect X" and
    the conclusion "therefore not validated") are addressed by the same sources.

  Caveats: The LLM-judge sources are software/ML-specific and recent (2026), so the analogy to whatever
    domain the original C2A2 probe/control-set concerns (which is not specified in the brief) is not
    confirmed to be exact — it is a structural analogy, not a citation about the same system. The
    case-control methodology principle is well-established but general; it was not independently
    verified against a single canonical textbook citation this session.

  Search scope: Preliminary but targeted — three searches converging on the same structural finding
    from two different domains (ML evaluation, epidemiological methodology), which increases confidence
    despite each individual search being narrow.

  Recommendation: SUPPORTED
