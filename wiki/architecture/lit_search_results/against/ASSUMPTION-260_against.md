SEARCH-AGAINST-ASSUMPTION-260:
  Date searched: 2026-05-30
  Original item: ASSUMPTION-260
  Original statement: Adding a participant is a single-source operation: one COLORS line + vault files + regen.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-260
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15b: Searched regen-on-add scaling cost and fail-loud gaps in registration.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Categorical-color perception literature (CleanChart/arXiv 2404.03787) — distinct categorical colors saturate around ~10-12, so 'one COLORS line' stops yielding a distinguishable color at scale (couples PRESUMPTION-281).
    2. Chrome memory / large-DOM docs — regen produces an ever-larger self-contained HTML (already ~26MB); regen-on-add cost grows with N.
    3. Fail-loud literature — the get_group -> 'root' silent fallback means a mis-registered participant is absorbed silently rather than erroring (couples ASSUMPTION-259).

  Strength of challenge: Moderate

  Summary: The single-source claim is cheap only at small N: the categorical-color budget caps distinct hues near ~10-12, regen output (already ~26MB) and time grow with N, and a silent grouping fallback can swallow a mis-add. 'One line + regen' understates these scaling and fail-loud costs.

  Specific risks: At N>~12 new participants get indistinguishable colors; regen latency/size degrade; silent mis-grouping.

  Mitigations available: Plan non-color encodings beyond ~12; budget regen cost; make grouping fail loud.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-260
    Strongest counterargument: 'Cheap' is scale-relative; the color budget and the silent fallback make 'one line + regen' break before the project's own N=33/100 targets.
    What would need to be true for C2A2 to be safe: Distinct encoding exists for N up to target, regen stays within size/time budget, and mis-adds fail loudly.
    How to test: Add the 13th..33rd participant in a dry run; measure color distinctness, regen time, HTML size, and mis-add behavior.
