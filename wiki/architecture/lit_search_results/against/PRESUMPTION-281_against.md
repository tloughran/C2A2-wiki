SEARCH-AGAINST-PRESUMPTION-281:
  Date searched: 2026-05-30
  Original item: PRESUMPTION-281
  Original statement: [inferred] 'One COLORS line + regen' presumes registration stays cheap at N=33/100 -- palette distinctness, regen time, ~20MB HTML size not examined as scaling costs.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-281
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15b: Searched regen-on-add / palette-collision costs at scale and self-contained-HTML size limits.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Categorical-color perception (CleanChart; arXiv 2404.03787 'Revisiting Categorical Color Perception') — distinct categorical colors saturate near ~6-12; beyond that hues are not reliably distinguishable, a hard perceptual ceiling well below N=33/100.
    2. Tsitsulin 'Optimal qualitative colour palettes' — even optimized qualitative palettes degrade past ~12-20 categories.
    3. Chrome memory / large-DOM docs + textslashplain 'Browser Memory Limits' — a self-contained HTML already ~26MB grows with N; regen time and tab memory scale with it.

  Strength of challenge: Moderate-Strong

  Summary: Registration is cheap to *type* but not cheap to *scale*: categorical-color distinctness caps near ~10-12, so 'one COLORS line' stops yielding a distinguishable color long before N=33/100; regen output (already ~26MB) and time grow with N. The cheapness presumption ignores a hard perceptual ceiling and growing artifact size.

  Specific risks: At N>~12 new participants are visually indistinguishable; HTML size/regen latency degrade UX and the build loop.

  Mitigations available: Introduce non-color encodings (shape, label, grouping) before ~12; budget regen size/time; consider WebGL/streamed rendering at scale.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-281
    Strongest counterargument: The project's own N=33/100 targets exceed the categorical-color perceptual ceiling, so the current encoding cannot represent them distinctly no matter how cheap the edit is.
    What would need to be true for C2A2 to be safe: A distinct visual encoding exists for N up to target and regen stays within size/time budget.
    How to test: Dry-run register to N=33; measure color distinctness, regen time, HTML size.
