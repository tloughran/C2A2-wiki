SEARCH-FOR-PRESUMPTION-1076:
  Date searched: 2026-09-23
  Original item: PRESUMPTION-1076
  Original statement: A single positive control cannot discriminate between failure causes that share a
    symptom; differential diagnosis needs a control per candidate cause.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-1076
    Item type: PRESUMPTION (unstated)
    Transform at each step:
      14b: Inferred from two diagnoses resting on one control that does not separate them.
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Fault detection and isolation (FDI) literature on structured residuals and fault signature
       matrices — e.g. Varga, A., "Fault Detection and Isolation Tools (FDITOOLS) User's Guide," arXiv
       1703.08480; "Fault detection and diagnosis: computational issues and tools," arXiv 1902.11186;
       "Fault isolability with different forms of the faults–symptoms relation" (ResearchGate record).
       — Formal result: faults with identical signatures across the available residuals are
       non-distinguishable; isolation requires a set of residuals giving each fault a unique
       signature. A single test that responds identically to two faults cannot isolate them. This is
       direct theoretical support.
    2. "Fault Detection and Isolation Based on Structural Analysis: Application to a Multi-Engine
       Propulsion Cluster," Sensors (MDPI), 2025, 25(4):1054. — Applied precedent: residual subsets are
       chosen specifically so every candidate fault has a distinct signature.
    3. Platt, J. R., 1964. "Strong Inference." Science 146:347–353 (cited via Wikipedia and "Fifty years
       of J. R. Platt's strong inference," Journal of Experimental Biology 217(8):1202, 2014). — Method
       requires devising crucial experiments whose outcomes each exclude one or more alternative
       hypotheses; a test whose outcome is predicted equally by all hypotheses is non-discriminating.
    4. [unverified — from background knowledge, not confirmed by this search] Clinical
       differential-diagnosis reasoning: tests are chosen for their likelihood ratio between competing
       diagnoses; a finding common to all candidates has a likelihood ratio near 1 and does not shift
       the differential.

  Strength of support: Strong (for the first clause); Moderate (for "a control per candidate cause")

  Summary: Control-theory FDI formalizes the presumption exactly: two faults are isolable only if some
    residual responds differently to them, so a single check that both faults trip cannot tell them
    apart. Platt's strong inference gives the same result in experimental-design terms: discriminating
    tests must have outcomes that differ across hypotheses. Both frameworks confirm the first clause
    unambiguously.

  Caveats: The second clause ("a control per candidate cause") is sufficient but stronger than
    necessary: FDI theory shows that k binary tests can in principle separate up to 2^k causes if their
    signatures are designed well, so one control per cause is a safe heuristic rather than a strict
    requirement. Also, a positive control that fails (rather than passes) can sometimes exclude causes
    downstream of it; the presumption holds for the shared-symptom case specified.

  Search scope: Preliminary — two searches (strong inference/differential diagnosis; fault isolability
    and structured residuals).

  Excluded results: USPTO patent PDF on Kalman-filter residual FDI (patent, not literature); none
    suspicious.

  Recommendation: SUPPORTED
