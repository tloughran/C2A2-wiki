SEARCH-AGAINST-PRESUMPTION-278:
  Date searched: 2026-05-30
  Original item: PRESUMPTION-278
  Original statement: [inferred] The hidden-tab rAF confound is presumed isolated to that one diagnosis; remote-Chrome probes are still trusted for other visual-rendering diagnoses without re-examination.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-278
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15b: Searched rAF throttling as a general background-tab artifact class and tool-trust after a known failure.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Chrome 'Background tabs in chrome 57' / 'Timer throttling in Chrome 88' — rAF/timer throttling is a *general* background-tab artifact class, not a one-off; any background visual probe is exposed.
    2. MDN Page Visibility API — hidden documents stop rAF callbacks generally, so every background visual-rendering probe shares the confound.
    3. Reliability engineering (tool-trust after known failure) — continuing to trust an instrument for a class of measurements after a confirmed failure mode, without re-examination, is a documented methodological error.

  Strength of challenge: Moderate-Strong

  Summary: rAF/timer throttling is a general property of background tabs, so the confound that broke one diagnosis applies to the whole class of remote-Chrome visual-rendering probes. Presuming it isolated and continuing to trust those probes without re-examination is a systemic tool-trust error.

  Specific risks: Other past/future visual diagnoses via remote Chrome may be silently corrupted by the same throttling; a class of conclusions is suspect.

  Mitigations available: Audit remote-Chrome visual diagnoses; force foreground/visibility or set throttling-disable flag; re-validate prior visual findings.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-278
    Strongest counterargument: If the confound is a general background-tab behavior, then 'isolated to one diagnosis' is false by construction; every background visual probe inherits it.
    What would need to be true for C2A2 to be safe: All remote-Chrome visual probes run with visibility forced/throttling disabled, and prior visual findings are re-validated.
    How to test: Re-run a sample of prior remote-Chrome visual diagnoses with throttling disabled and compare.

  SYSTEMIC-RISK-FLAG:
    Date: 2026-05-30
    Affected items: PRESUMPTION-278 (and coupled items noted in disposition)
    Common vulnerability: see Summary.
    Risk level: High
    Recommendation: address at the class/pattern level, not per-instance.
