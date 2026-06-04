SEARCH-AGAINST-ASSUMPTION-253:
  Date searched: 2026-05-30
  Original item: ASSUMPTION-253
  Original statement: The Sociogram focus-fade bug is real (foreground focus: l~s -> edges stay lit; isolate computes 185 nodes but the fade does not render), not a hidden-tab testing artifact.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-253
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15b: Searched single-observation generalization and render-context-variance literature.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Chrome for Developers, 'Background tabs in chrome 57' / 'Timer throttling in Chrome 88' — rAF and chained timers are throttled/suspended in background tabs; a fade that 'does not render' can be a visibility-state artifact rather than a code defect.
    2. MDN, Page Visibility API — documents that hidden documents stop receiving rAF callbacks, the exact mechanism by which a transition-driven fade would silently not run.
    3. Mozilla Bugzilla #731974 — rAF generates anomalously short/long frames especially at animation start, a context-dependent render variance that can masquerade as a logic bug.
    4. General reproducibility methodology: a single foreground observation on one machine/browser is insufficient to exclude a GPU/compositor-specific render fault (couples PRESUMPTION-277).

  Strength of challenge: Moderate

  Summary: The literature on background-tab throttling and rAF frame variance shows that 'the fade does not render' is exactly the signature a visibility/compositor artifact would produce, so a single foreground observation does not by itself exclude a context-bound cause. The claim that it is 'real, not a testing artifact' is plausible but under-determined by one observation.

  Specific risks: If the fade is actually render-context-bound, the planned .attr() fix (ASSUMPTION-254) may not generalize, and the v1.6 hold (ASSUMPTION-255) gates on a misdiagnosis.

  Mitigations available: Reproduce on >=2 browsers/machines in foreground; capture a frame-by-frame trace; confirm opacity attribute value vs rendered pixels.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-253
    Strongest counterargument: The symptom (data path runs, pixels unchanged) is the canonical signature of a compositor/visibility render artifact; absent multi-context reproduction, calling it a 'real code bug' overcommits.
    What would need to be true for C2A2 to be safe: Reproduced in >=2 independent foreground contexts with identical opacity-attr-vs-render divergence.
    How to test: Run the same isolate query in foreground on Chrome+Firefox on two machines; compare computed opacity attr to rendered alpha.
