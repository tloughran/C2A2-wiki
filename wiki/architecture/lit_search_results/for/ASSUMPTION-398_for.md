SEARCH-FOR-ASSUMPTION-398:
  Date searched: 2026-07-01
  Original item: ASSUMPTION-398
  Original statement: "No-Blind-Push requires a live visual eyeball before publish even after programmatic green."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-398
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-06-30 publish-gate discussion
      15a: Searched for supporting literature (genuine web search 2026-07-01)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Testmetry / BrowserStack visual testing — visual/UI regressions are caught even when unit and e2e tests pass; a green functional build routinely masks layout/rendering defects that only a rendered view exposes.
    2. Gartner 2024 (via ShiftAsia) — defect escape rates rise ~25% when review processes are not adapted to catch what automation misses; a human gate after green measurably reduces escapes.
    3. C2A2-internal: the metabolism/heartbeat display precedent (stale-axis mislead, REVISE-158) is exactly a case where programmatic green coexisted with a visually-wrong artifact; a live eyeball would have caught it.

  Strength of support: Moderate-Strong

  Summary: Strong support that a live visual check catches a defect class automated green cannot see — visual regressions pass functional assertions but look wrong, and defect-escape rises without a review layer adapted to that gap. For a publish step producing human-facing visualizations, the eyeball gate is well grounded.

  Caveats: The support is for catching visual/rendering defects specifically. It does not establish that a MANUAL eyeball is the only or best mechanism — automated visual-regression tooling covers much of the same gap and scales better (see 15b). The premise is best read as "a visual check is required," not "a human must always be that check."

  Recommendation: SUPPORTED (Moderate-Strong — a visual gate catches what functional green misses; manual-vs-automated is a refinement)
