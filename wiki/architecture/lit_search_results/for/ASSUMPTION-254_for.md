SEARCH-FOR-ASSUMPTION-254:
  Date searched: 2026-05-30
  Original item: ASSUMPTION-254
  Original statement: The prime suspect for the fade bug is the d3 .transition() opacity calls; likely fix is plain .attr('opacity').

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-254
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15a: Searched d3 .transition() vs .attr() behavior under heavy force sims.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Bostock, 'Working with Transitions' — confirms .transition() schedules interpolated frames via the timer/rAF loop, whereas .attr/.style apply immediately; replacing a transition with a direct attribute write removes the rAF dependency.
    2. d3/d3 Issue #1247 — community workarounds for failing opacity transitions repeatedly resolve by setting the attribute/style directly rather than transitioning.
    3. dev.to 'requestAnimationFrame Explained' — heavy rAF-driven loops (force sim) contend for the same frame budget as transitions, so a non-transitioned write is the standard mitigation.

  Strength of support: Moderate

  Summary: Mechanistically, d3 transitions depend on the timer/rAF loop that a running force simulation also drives; a direct .attr('opacity') write bypasses that contention. Both the official transition docs and community bug threads support direct attribute writes as the standard fix for stuck opacity transitions.

  Caveats: Supports plausibility of the fix, not certainty of the root cause; 'prime suspect' is a single-hypothesis framing.

  Recommendation: SUPPORTED
