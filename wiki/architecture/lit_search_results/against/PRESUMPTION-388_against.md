SEARCH-AGAINST-PRESUMPTION-388:
  Date searched: 2026-06-25
  Original item: PRESUMPTION-388
  Original statement: "That preserved dissensus = genuine under-determination, not instrument failure (bad axes / erratic adjudicator)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-388
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: dissensus read as signal without ruling out instrument noise; gated by OPEN-089/090
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. VARIERR NLI (Weber-Genzel et al. 2024). - Demonstrates that a large share of disagreement is annotation ERROR; equating disagreement with genuine variation overcounts signal.
    2. Test-retest reliability theory. - Without demonstrated stability, disagreement cannot be attributed to the items rather than to an unreliable instrument.
    3. LLM-judge instability (position/sampling variance). - An erratic adjudicator or temperature variance produces non-reproducible 'dissensus' that is pure instrument noise.

  Strength of challenge: Strong

  Summary: Strongly challenged: the equation 'preserved dissensus = genuine under-determination' ignores the dominant alternative explanation - instrument failure. The same human-label-variation literature that legitimizes disagreement insists on separating genuine variation from error, and shows error is a large fraction. For C2A2, bad analytic axes, an unreliable adjudicator, or sampling variance would generate dissensus that is reproducible-looking noise, not contestability. Without test-retest and an error/variation split, the equation is unsupported.

  Specific risks: The detector could report 'genuine contestability' that is actually adjudicator/axis noise, fabricating a constitutional finding out of instrument failure.

  Mitigations available: Establish test-retest stability of dissensus; run an error-vs-variation audit (VARIERR-style); set a measured noise floor below which dissensus is not reported.

  STEELMAN:
    Item: PRESUMPTION-388
    Strongest counterargument: Disagreement has (at least) two sources - genuine under-determination and instrument failure - and the literature shows the second is large; absent reliability evidence, preserved dissensus is an uncalibrated mixture, so equating it with under-determination is unwarranted.
    What would need to be true for C2A2 to be safe: The dissensus measure is test-retest stable and its error fraction is quantified and small.
    How to test: Re-run identical inputs across sessions/seeds; measure dissensus reproducibility; hand-audit a sample for genuine-vs-spurious disagreement.

  Search scope: Error-vs-variation separation; reliability; judge instability. Comprehensive.

  Recommendation: CHALLENGED
