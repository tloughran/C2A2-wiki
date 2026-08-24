SEARCH-FOR-ASSUMPTION-1153:
  Date searched: 2026-08-19
  Original item: ASSUMPTION-1153
  Original statement: Four instruments retracted their own confident, specific findings within a single
    day, and one retraction prevented the reversal of correct repairs: "Had that reading been carried
    forward, it would have licensed reversing the correct Day 268/269 repairs … One grep prevented it."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1153
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Collected four same-day self-retractions and one near-miss, and paired them against the prior
        night's opposite failure mode (instruments whose failure was a pass mark).
      15a: Searched for supporting literature (2026-08-19)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. "Deploying Static Analysis" (arXiv:2202.11861) and "Static Analysis Deployment Pitfalls"
       (arXiv:2202.13026). (author lists not verified) — Practitioner-facing accounts of static analysis
       deployment. Report that no significant static analysis tool is immune to false positives and that
       the rate is "very roughly, 20%"; that excessive false positives cause developers to distrust and
       abandon the tools. Direct support for the premise that verification instruments produce confident,
       specific findings that do not survive checking.
    2. "Reducing False Positives in Static Bug Detection with LLMs: An Empirical Study in Industry."
       arXiv:2601.18844. (author list not verified) — States that static analysis tools "often suffer from
       high false positive rates when applied to large-scale software systems in practice." Supports the
       claim in the current (LLM-assisted) tooling generation, not just the classical one.
    3. "Analyzing False Positive Source Code Vulnerabilities Using Static Analysis Tools." IEEE
       (ieeexplore document 8622456). (author list not verified) — Reports that a large number of false
       positives lowers trust and leads developers to ignore results.
    4. "Certainty robustness: Evaluating LLM stability under self-challenging prompts."
       arXiv:2603.03330. (author list not verified) — Finds that positive confidence calibration does not
       prevent unjustified answer changes under conversational pressure. Directly relevant to the
       "retracted its own confident, specific finding" shape: confidence at time of assertion does not
       predict stability of the assertion.
    5. CRITIC (arXiv:2305.11738) and related self-correction work (e.g. "Boosting LLM Reasoning via
       Spontaneous Self-Correction," arXiv:2506.06923). (author lists not verified) — Establish that
       intrinsic self-correction without external feedback often fails or degrades performance, whereas
       *tool-interactive* checking against external evidence improves it. This supports the item's causal
       claim that the retraction was produced by an external check ("one grep"), not by introspection.

  Strength of support: Moderate-to-Strong

  Summary: Two distinct literatures support this item. The static-analysis literature establishes that
  verification instruments routinely emit confident, specific findings that are wrong, at rates around
  20% in general practice, and that this is the dominant reason such instruments lose credibility. The LLM
  literature establishes that a model's confidence does not predict the stability of its assertion under
  challenge, and — most directly relevant to the item's near-miss — that self-correction succeeds when
  grounded in an external check and fails when purely introspective. The item's specific structure (an
  instrument's confident finding, retracted by a cheap external verification, where carrying the finding
  forward would have reversed correct work) is exactly the CRITIC-style pattern. The framing that
  verification instruments themselves require validation is well supported; nothing found contradicts it.

  Caveats: The 20% false-positive figure is a rough practitioner estimate, not a measured constant, and
  varies enormously by tool and codebase (some vendor tools claim ~5%). No source establishes a base rate
  for same-day self-retraction by agentic verification pipelines — that number is specific to this vault
  and untestable against literature. The Type I / Type II cost-asymmetry limb of the search angle was
  addressed only obliquely: the sources establish that false positives are costly to trust, not that they
  are more or less costly than false negatives, and this vault's own prior-night finding (instruments
  whose failure signature was a pass) is the counterweight. Search scope: moderate — covered static
  analysis false positives and LLM self-correction/confidence stability; did NOT cover the medical
  diagnostic-testing literature on predictive values, which would formalise the asymmetry argument.

  Recommendation: SUPPORTED
