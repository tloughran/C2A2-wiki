SEARCH-AGAINST-ASSUMPTION-254:
  Date searched: 2026-05-30
  Original item: ASSUMPTION-254
  Original statement: The prime suspect for the fade bug is the d3 .transition() opacity calls; likely fix is plain .attr('opacity').

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-254
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15b: Searched single-suspect debugging risk and cases where .attr swaps mask a deeper cause.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Zeller, 'Why Programs Fail' (systematic debugging) — single-suspect, fix-first debugging frequently treats a symptom while the true defect (e.g., a stale selection, join error, or visibility state) persists.
    2. MDN Page Visibility API / Chrome timer-throttling docs — if the real cause is visibility/compositor state, switching .transition() to .attr() will not fix a background-throttled render and may give false confidence.
    3. d3 join/selection literature — opacity that 'stays lit' can stem from selecting the wrong nodes (enter/update/exit mismatch), which an opacity-write change would mask, not resolve.

  Strength of challenge: Moderate

  Summary: Naming a single 'prime suspect' before reproduction risks fixing a symptom. The same observable could arise from a selection/join error or a visibility-state artifact, in which case the .attr() swap masks rather than resolves the defect. Established debugging methodology cautions against fix-first on one hypothesis.

  Specific risks: A masked root cause re-surfaces later (e.g., at scale or on another browser) and the test suite still shows green (couples ASSUMPTION-262/PRESUMPTION-285).

  Mitigations available: Bisect: confirm opacity attribute value in DOM vs rendered pixels before changing code; verify the selection set; only then swap to .attr().

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-254
    Strongest counterargument: If the divergence is between the opacity *attribute* (correct) and rendered pixels, the bug is downstream of any .transition()/.attr() choice, so the proposed fix targets the wrong layer.
    What would need to be true for C2A2 to be safe: DOM opacity attribute confirmed to disagree with the transition target before the fix, and to agree after.
    How to test: Log .style('opacity') / .attr('opacity') of the affected selection pre- and post-fix and compare to rendered alpha.
