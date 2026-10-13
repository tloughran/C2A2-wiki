SEARCH-AGAINST-PRESUMPTION-1115:
  Date searched: 2026-10-10
  Original item: PRESUMPTION-1115
  Original statement: [inferred] Instruments with partial coverage report silence as a negative
    finding. Question: do non-detections by partial-coverage instruments warrant "absent"
    conclusions, and what minimal coverage statement makes them interpretable?
  Under test: the implied correction that partial-coverage silence must NOT be read as absence
    without a detection/coverage model (the occupancy-modelling analogy). I searched for evidence that
    absence-of-evidence inference is often reasonable, and that formal detection corrections can fail
    or fail to transfer.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for file,
    `lit_search_returns.md`, or any 15a output from today.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1115
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b (2026-10-09): Inferred from instrument outputs that silence from partial-coverage
        instruments is being read as a negative finding; queued with question on minimal coverage
        statement.
      15b (2026-10-10): Searched for challenging literature. 4 search calls (1 cut off before
        results, retried): occupancy imperfect-detection critique; Bayesian absence-of-evidence;
        Welsh-Lindenmayer-Donnelly (2 calls). 2 fetch attempts: Hsu et al. 2017 (abstract, OK);
        Welsh et al. reply PMC4411262 (FAILED, reCAPTCHA wall).
    Current status: PARTIALLY-CHALLENGED

  EVIDENCE GRADE: PRELIMINARY. One fetched abstract; one fetch failure; rest search-result.

  Search scope: preliminary (3 effective searches + 1 cut-off retry; 2 fetch attempts, 1 failed).

  Challenging evidence found: Partial
  Strength of challenge: Weak-Moderate

  Sources:
    1. Hsu AS, Horng A, Griffiths TL, Chater N. 2017. "When Absence of Evidence Is Evidence of
       Absence: Rational Inferences From Absent Data." Cognitive Science 41:1155-1167.
       doi:10.1111/cogs.12356. [fetched, abstract] A rational Bayesian analysis predicts that
       inferences from absences should depend on how expected the absence is. People make such
       inferences in line with a simple Bayesian model. Bearing: absence of evidence IS evidence of
       absence, graded by search sensitivity. A blanket refusal to read silence as negative is also
       irrational. The question is calibration, not prohibition.
    2. Stephens C. 2011. Informal Logic (absence-of-evidence analysis in a Bayesian framework);
       Downey A., "Absence of evidence" (blog). [search-result] Under plausible assumptions absence
       of evidence is evidence of absence, and it is strong when P(detect | present) is high.
       Bearing: for an instrument that reliably covers a component, silence about that component is
       legitimately a strong negative.
    3. Welsh AH, Lindenmayer DB, Donnelly CF. 2013. "Fitting and Interpreting Occupancy Models."
       PLoS ONE 8(1):e52015. [search-result] Occupancy models that correct for imperfect detection
       are often hard to fit: multiple solutions, boundary estimates, instability with sparse data.
       Adjusting for non-detection "can be as misleading as ignoring non-detection", and ignoring
       it can be better. Bearing: a FAILED-TRANSFER warning. Importing a formal detection-correction
       model into a sparse, low-replicate setting (a few runs of a software instrument) may produce
       unstable, falsely precise "occupancy" estimates.
    4. Guillera-Arroita G, Lahoz-Monfort JJ, MacKenzie DI, Wintle BA, McCarthy MA. 2014. "Ignoring
       Imperfect Detection in Biological Surveys Is Dangerous: A Response to 'Fitting and
       Interpreting Occupancy Models'." PLoS ONE (PMC4116132). [search-result] Rebuts source 3:
       WLD's result holds only under extreme heterogeneity. Ignoring detection makes the bias
       unknowable. Recorded honestly: this rebuttal weakens source 3 and SUPPORTS the item's premise.
    5. MacKenzie DI & Royle JA. 2006 (survey design for occupancy). [search-result] When detection
       probability is high, effort is better spent on more units than on repeat surveys. Bearing:
       for high-sensitivity instruments the detection correction matters less.

  Summary: The challenge is a qualified one. The literature does not support "silence from a
    partial instrument means absent". It also does not support the opposite reflex of treating all
    silence as uninformative. Bayesian work says absence is evidence, graded by the probability that
    the instrument would have detected the thing if present. So within the inspected scope, silence
    from a sensitive instrument is a legitimate negative. The main challenge is to the remedy, not the
    diagnosis. Formal occupancy-style detection modelling is contested even in ecology (WLD 2013 vs
    Guillera-Arroita 2014). It needs replicate surveys and degrades with sparse data, conditions that
    may not hold for one-shot software checks. A deterministic software instrument has a coverage
    question (did it look?) more than a detection-probability question (would it have seen?). That
    makes the ecological analogy an imperfect transfer.

  Specific risks: (a) Over-correction: if every non-detection is downgraded to "unknown", C2A2 loses
    legitimate negatives within an instrument's scope and generates noise (see PRESUMPTION-1118 on
    UNKNOWN fatigue). (b) A heavyweight detection model applied to sparse runs gives unstable, falsely
    precise estimates.

  Mitigations available: The minimal coverage statement may be just a scope list ("inspected: X, Y;
    not inspected: Z"). That separates "looked and found nothing" (a strong negative for
    deterministic checks) from "did not look" (no evidence), without probabilistic detection
    modelling.

  STEELMAN:
    Item: PRESUMPTION-1115
    Strongest counterargument: Absence of evidence is evidence of absence whenever the search would
      probably have found the thing, and many software instruments are deterministic within their
      scope (a grep either matches or it does not). For those, a scoped non-detection is close to
      conclusive, and demanding a detection-probability model adds machinery that the ecology
      literature itself finds unstable with sparse data. The real defect is undeclared SCOPE, not
      the inference from silence. Fixing it with occupancy-style hedging would turn many valid
      negatives into "unknown" and erode the signal.
    What would need to be true for C2A2 to be safe: Each instrument declares what it inspected, and
      within that scope its detection is near-deterministic. Absence claims are limited to the
      inspected scope.
    How to test: Seed known defects inside and outside each instrument's declared scope. Measure
      detection inside scope (should be about 1) and confirm silence outside scope is not reported
      as absence.

  Boundary conditions identified:
    - Silence is strong evidence only where P(detect | present) is high. That holds for
      deterministic in-scope checks, not for sampling or heuristic instruments (LLM-judgement scans).
    - Occupancy-style correction requires replicate surveys. It fails or is unstable with sparse data
      (contested: WLD 2013 vs Guillera-Arroita 2014).
    - The transfer from ecology to software is weak. Software gaps are mostly coverage gaps (the
      instrument did not look), not detection-probability gaps.

  Recommendation: PARTIALLY-CHALLENGED (challenge is to the remedy's form, not to the diagnosis)

  SYSTEMIC-RISK-FLAG: shared with ASSUMPTION-1757, PRESUMPTION-1117, PRESUMPTION-1118,
    PRESUMPTION-1119. Common vulnerability: binary corrections (here: silence → absent vs unknown)
    plus added meta-process, where the literature favours graded, sensitivity-weighted, documented
    handling. Risk level: High. Full flag text in PRESUMPTION-1117_against.md.
