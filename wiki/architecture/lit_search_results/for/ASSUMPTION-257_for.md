SEARCH-FOR-ASSUMPTION-257:
  Date searched: 2026-05-30
  Original item: ASSUMPTION-257
  Original statement: The recent Sociogram crash was pure memory pressure, not the edge cap; MAX_EDGES=30000 stays.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-257
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15a: Searched browser memory-pressure crash signatures in large SVG graphs.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Chrome DevTools 'Fix memory problems' — a tab exceeding ~1GB (desktop) is terminated by the browser; large graphs are a known OOM trigger, consistent with a memory-pressure crash.
    2. Nightingale, 'How to Visualize a Graph with a Million Nodes' — SVG fails past a few thousand animated objects; memory/DOM pressure (not an explicit edge cap) is the dominant crash mode.
    3. textslashplain, 'Browser Memory Limits' — per-tab/process memory ceilings cause tab termination independent of any application-level cap.

  Strength of support: Moderate

  Summary: Browser per-tab memory ceilings and SVG's poor scaling past a few thousand objects make a memory-pressure crash a credible diagnosis; large graphs are a documented OOM trigger. Keeping MAX_EDGES as a guardrail is consistent with this.

  Caveats: Supports 'memory pressure is a real crash mode'; does not establish that the edge cap is *unrelated* to memory pressure.

  Recommendation: SUPPORTED
