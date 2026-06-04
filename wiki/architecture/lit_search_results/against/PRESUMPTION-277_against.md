SEARCH-AGAINST-PRESUMPTION-277:
  Date searched: 2026-05-30
  Original item: PRESUMPTION-277
  Original statement: [inferred] The fade bug 'real' verdict generalizes from one foreground query/user/browser to the whole fade mechanism; symptom presumed code-path-bound, not render-context-bound.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-277
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15b: Searched single-observation generalization error and render-context variance.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Chrome/MDN visibility & throttling docs — rendering behavior varies by tab visibility and compositor state; a single context cannot establish a render fault generalizes.
    2. Mozilla Bugzilla #731974 — rAF frame timing varies by context, producing context-bound render artifacts.
    3. Reproducibility methodology (single-observation generalization error) — inferring a whole-mechanism verdict from N=1 (one query/user/browser) is a textbook over-generalization.

  Strength of challenge: Moderate-Strong

  Summary: Generalizing from one foreground query/user/browser to 'the whole fade mechanism is broken' is a single-observation over-generalization, and render behavior is known to be context-dependent. The presumption (symptom is code-path-bound) is unverified and the literature gives strong reason to suspect render-context dependence.

  Specific risks: The .attr() fix (ASSUMPTION-254) and the v1.6 hold (255) are predicated on a verdict drawn from N=1; if context-bound, both are misdirected.

  Mitigations available: Reproduce across >=2 browsers/machines and tab-visibility states before treating the fade verdict as general.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-277
    Strongest counterargument: N=1 across one query/user/browser cannot distinguish a code-path bug from a compositor/visibility artifact; the generalization is unsupported until reproduced.
    What would need to be true for C2A2 to be safe: Multi-context reproduction with identical symptom.
    How to test: Matrix: {Chrome,Firefox} x {2 machines} x {foreground} run of the same isolate query.
