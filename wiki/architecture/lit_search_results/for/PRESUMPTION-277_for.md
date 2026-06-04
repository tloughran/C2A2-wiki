SEARCH-FOR-PRESUMPTION-277:
  Date searched: 2026-05-30
  Original item: PRESUMPTION-277
  Original statement: [inferred] The fade bug 'real' verdict generalizes from one foreground query/user/browser to the whole fade mechanism; symptom presumed code-path-bound, not render-context-bound.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-277
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15a: Searched reproducibility of render faults across contexts.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. d3/d3 Issues #1247/#474 — some opacity-transition faults are reproducible across contexts, lending partial support that a code-path-bound fault can generalize.
    2. Bostock 'Working with Transitions' — transition starvation under a force timer is a code-path mechanism that would recur across contexts.
    3. Software-defect generalization literature — defects in deterministic code paths often do reproduce broadly.

  Strength of support: Weak

  Summary: There is partial support that a transition/timer code-path fault is reproducible across contexts, so generalizing from one observation is not baseless. But the support is weak because reproducibility-across-contexts is precisely what was not yet tested.

  Caveats: Partial support is for 'code-path faults can generalize', not that this one does.

  Recommendation: PARTIALLY-SUPPORTED
