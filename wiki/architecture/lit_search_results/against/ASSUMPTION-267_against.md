SEARCH-AGAINST-ASSUMPTION-267:
  Date searched: 2026-06-03
  Original item: ASSUMPTION-267
  Original statement: Raising the Sociogram MAX_NODES cap from 2000 to 20000 is correct crash-proofing — the old 2000 cap would truncate the 2529-node graph, and 20000 is a safe ceiling current/near-term data will not reach while keeping the render stable.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-267
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2000→20000 cap change.
      15b: Searched setting limits by current-load-only and untested ceilings that re-admit the failure they guard against.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Force-directed performance cliff (~1000+ nodes for D3/SVG) (Weber/Medium large-graph survey; GraphAware PIXI.js). — A 20000 ceiling is far above where SVG-based force layouts degrade; the cap no longer reflects the render's real safe capacity, so it can ADMIT graphs that hang or crash the browser — re-introducing the failure the cap exists to prevent.
    2. "Capacity must be determined experimentally; a configured limit is not a tested limit" (octocore Capacity vs Load; SRE headroom guides). — Setting the ceiling to a round 10x of nothing-in-particular, validated only at 2529, is current-load-plus-guesswork, not a measured safe limit.
    3. Untested-limit anti-pattern (this register's verify-the-effect / scale-blindness lineage; PRESUMPTION-299). — The cap's whole job is to stop a crash; an unverified cap silently relocates the crash threshold into untested territory, which is worse than a known-conservative cap because failure now appears only on large real data, in front of users.

  Strength of challenge: Moderate-Strong

  Summary: The "fix the truncation" half is sound, but the assumption over-reaches by asserting 20000 is a SAFE ceiling. Browser force-directed rendering degrades non-linearly well below 20000 (D3/SVG cliffs near ~1000+ nodes), so the new cap likely sits above the real safe capacity and can re-admit the crash it guards against. The safe limit was never measured — it was set to a round 10x and validated only at the current 2529-node point. The defensible change is "raise above 2529 with margin"; "20000 is safe" is an untested claim. Tightly couples PRESUMPTION-299.

  Specific risks: If/when the graph grows past the (unknown, likely <20000) render cliff, the browser hangs or crashes with no guard tripping — a silent regression of the crash-proofing, surfacing only on large real data.

  Mitigations available: Measure the actual render cliff for this build (sweep node counts, watch frame time / memory) and set the cap to a tested fraction below it; OR switch the renderer to canvas/WebGL so the safe ceiling is genuinely high; until measured, set a conservative cap that fits current data plus modest headroom, not a round 10x.

  STEELMAN:
    Item: ASSUMPTION-267
    Strongest counterargument: Raising the cap to clear the immediate truncation is right, but pinning it at 20000 and calling that "safe" substitutes a round number for a measurement. Browser force layouts have performance cliffs far below 20000, so the cap may no longer bound the render to a safe region — it can let a future graph crash exactly as the original cap was meant to prevent, only now the failure is hidden until the data grows.
    What would need to be true for C2A2 to be safe: Either the render is measured to stay stable up to ~20000 on target hardware, OR the cap is set to a tested value below the measured cliff, OR the renderer is canvas/WebGL with a genuinely high safe ceiling.
    How to test: Generate synthetic graphs at 3k/5k/8k/12k/16k/20k nodes, measure frame time, interaction latency, and memory until degradation; set the cap below the first cliff.

  Recommendation: CHALLENGED
