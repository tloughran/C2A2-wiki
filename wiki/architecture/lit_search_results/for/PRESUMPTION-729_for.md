SEARCH-FOR-PRESUMPTION-729:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-729
  Original statement: That "invisible to every detector currently in use" is a fact about one batch rather than a bound on the whole series; the batch carrying four undetectable defects also produced the highest fidelity scores ever recorded in the log.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-729
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: 14b connected two statements the run made in one summary without connecting them
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Trail of Bits Blog, 2025. "Use mutation testing to find the bugs your tests don't catch." — Directly supports the mechanism: coverage/adequacy metrics ("100% line coverage," analogous to "highest fidelity scores") can coexist with critical undetected faults, because coverage measures execution not verification quality. Mutation testing exists specifically because high scores on the metrics in use do not bound the defects that exist.
    2. Survey, arXiv:2212.06118, "A Brief Survey on Oracle-based Test Adequacy Metrics." — Establishes the formal distinction between what a test-adequacy metric measures and the true (unmeasured) defect population — i.e., the "unmeasured denominator" the presumption names.
    3. [unverified — from search snippet] Rees, M. / Sagan, C. attribution discussed in "Absence of evidence is not evidence of absence" (PMC10065758, NIH). — Classical epistemic principle directly on point: a clean/high score from the detectors "currently in use" bounds only what those detectors can see, not the true defect rate; failure to detect is not evidence defects are absent, especially when detection power is unassessed.
    4. thecoder.cafe / practitioner literature, "Streetlight Effect Explained: A Common Observational Bias" — Describes how teams infer system health from what existing dashboards/detectors show ("if metrics are green, assume fine"), even though the detectors may not cover the relevant defect class — this is the general form of treating a single batch's clean detector readout as evidence about the whole series rather than a bound on detector coverage.

  Strength of support: Strong

  Summary: The mutation-testing and test-adequacy literature is a close structural match for this presumption: it is well established that a test/detector suite can report its best-ever scores on exactly the inputs where it is blind to real defects, because adequacy metrics measure what was exercised or matched, not what exists. This is precisely why mutation testing was invented — to expose the "coverage illusion." Combined with the general epistemic point that absence of detection is not detection of absence, there is strong convergent support that a batch's undetectability should be read as revealing a bound on detector coverage (a property of the whole series/toolset), not a fact isolated to that batch.

  Caveats: Sources are drawn from software test-adequacy and general epistemology, not from whatever specific "fidelity score" domain PRESUMPTION-729 refers to (unclear if code, text, or other artifact fidelity) — the mapping is conceptual/analogous. No source directly addresses the specific correlation described (highest scores co-occurring with worst blind spots) as an empirical finding, only as a structurally predicted possibility.

  Recommendation: SUPPORTED
