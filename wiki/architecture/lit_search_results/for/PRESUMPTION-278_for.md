SEARCH-FOR-PRESUMPTION-278:
  Date searched: 2026-05-30
  Original item: PRESUMPTION-278
  Original statement: [inferred] The hidden-tab rAF confound is presumed isolated to that one diagnosis; remote-Chrome probes are still trusted for other visual-rendering diagnoses without re-examination.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-278
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15a: Searched headless/background-tab testing reliability boundaries.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Chrome '--disable-background-timer-throttling' flag docs — the throttling confound is controllable, so trusting probes *with* the flag set can be legitimate.
    2. Headless-testing literature — background/headless testing is reliable within documented boundaries when visibility state is managed.
    3. C2A2-internal: the rAF confound was identified and (presumably) handled in the one diagnosis.

  Strength of support: Weak

  Summary: Background-tab confounds are controllable (e.g., throttling-disable flags, visibility management), so remote-Chrome probes can be trusted when those controls are applied. Support is weak because nothing confirms the controls are applied to the *other* visual diagnoses.

  Caveats: Conditional on the confound being controlled in every visual probe, which is exactly what is unexamined.

  Recommendation: PARTIALLY-SUPPORTED
