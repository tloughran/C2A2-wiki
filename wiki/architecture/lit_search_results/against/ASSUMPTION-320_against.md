SEARCH-AGAINST-ASSUMPTION-320:
  Date searched: 2026-06-16
  Original item: ASSUMPTION-320
  Original statement: "Gap-honest visualization (showing absence explicitly) is preferable to interpolation/silent zero."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-320
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-06-15 session (missing-data display choice)
      15b: Searched for challenging literature
    Current status: NO-CHALLENGE-FOUND (weak boundary conditions only)

  Challenging evidence found: Partial (boundary conditions, not contradiction)

  Sources:
    1. Time-series missing-data visualization review (arXiv:2507.14920). — Notes that showing gaps can "bring more noise than signal" in dense or highly-fragmented series, where many small gaps fragment the display and impair pattern reading. A boundary condition, not a refutation: honesty can cost legibility when missingness is dense.
    2. Imputation-display practice (imputeTS gallery; "Handling Gaps in Time Series," TDS). — For some analytic tasks (forecasting input, trend estimation) a model-based imputation with explicit uncertainty bands is more useful than a raw gap, provided the imputation is marked as inferred. Challenges the absolute "interpolation is worse" framing: marked interpolation-with-uncertainty can be preferable to a bare gap for certain purposes.
    3. (No source contradicts the core integrity principle.) — Searched directly for arguments that silent zero-fill or unmarked interpolation is preferable; found none. The graphical-integrity consensus is one-directional against silent imputation.

  Strength of challenge: Weak

  Summary: No literature contradicts the assumption; the integrity principle (don't silently impute or zero-fill) is essentially uncontested. The only challenges are boundary conditions: (a) in dense/fragmented series, raw gaps can add visual noise and hurt legibility, and (b) for some downstream tasks, an EXPLICITLY-MARKED imputation with uncertainty can be more useful than a bare gap. Neither defeats the assumption — both refine HOW to be gap-honest, not WHETHER. The "silent zero" alternative the assumption rejects has no defenders.

  Specific risks: Minimal. The only risk from over-applying the assumption is legibility: if gap-honesty is implemented as raw blanks in a dense series, the chart becomes hard to read; and treating "show the gap" as sufficient can leave viewers without the interpretation they need (this is the real issue — see PRESUMPTION-351, visibility ≠ comprehension).

  Mitigations available: Use a legible, deliberate gap encoding (marked break/annotation) rather than raw blanks; where imputation aids a task, show it as a clearly-labeled inferred band with uncertainty, never silently; pair the gap with a one-line explanation of why data is absent (capture artifact vs real inactivity — couples PRESUMPTION-352).

  STEELMAN:
    Strongest counterargument: The strongest case against is purely pragmatic: for an at-a-glance personal dashboard, a sea of honest gaps may communicate LESS than a smoothed line that conveys the overall trajectory, so "honesty" could trade truth for usability. But this is an argument for legible gap-encoding, not for silent imputation — even the steelman concedes any imputation must be marked.
    What would need to be true for C2A2 to be safe: The gap encoding must be legible and explained, and any imputation must be visibly marked as inferred. Under those conditions the assumption is not just safe but best-practice.
    How to test: Show users both versions (gap-honest vs silently-imputed) and ask them to report periods of no activity; silent imputation will produce more false "active" reports, confirming the integrity advantage.

  Search scope: Graphical integrity, missing-data visualization reviews, imputation-display practice, gap-vs-interpolation tradeoffs. Comprehensive; no genuine contradiction found.

  Recommendation: NO-CHALLENGE-FOUND
