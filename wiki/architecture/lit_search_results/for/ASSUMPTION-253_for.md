SEARCH-FOR-ASSUMPTION-253:
  Date searched: 2026-05-30
  Original item: ASSUMPTION-253
  Original statement: The Sociogram focus-fade bug is real (foreground focus: l~s -> edges stay lit; isolate computes 185 nodes but the fade does not render), not a hidden-tab testing artifact.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-253
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15a: Searched d3 transition/rAF rendering-pitfall literature and prior bug reports.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. d3/d3 GitHub Issue #1247 "Regression issue with opacity transition?" — documents real opacity-transition regressions independent of test harness; establishes that d3 opacity transitions genuinely fail in foreground use.
    2. Bostock, M. "Working with Transitions" (bost.ocks.org) — transition.style builds a style tween by reading the DOM start value; under a running force timer this can be starved, a real foreground defect not a test artifact.
    3. d3/d3 Issue #474 "transitions fail in bar chart example" — confirmed real transition failures reproducible in foreground.
    4. C2A2-internal: the observation was made on a foreground tab with isolate computing 185 nodes, i.e. the data path executed; the symptom is render-side.

  Strength of support: Moderate

  Summary: d3's transition machinery has a documented history of genuine opacity-transition failures, and a heavy force-simulation timer can starve transition frames. A foreground observation where the isolate set computed correctly (185 nodes) but opacity did not change is consistent with a real render-path defect rather than a measurement artifact.

  Caveats: Support is for 'transition opacity can genuinely fail under force sims', not for the specific root cause; one foreground observation does not establish reproducibility across browsers/GPUs.

  Recommendation: SUPPORTED
