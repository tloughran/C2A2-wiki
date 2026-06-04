SEARCH-FOR-PRESUMPTION-299:
  Date searched: 2026-06-03
  Original item: PRESUMPTION-299
  Original statement: [inferred] The 10x cap raise (2000->20000) presumes graceful performance across the whole new range; it was validated only against the present 2529-node case, with no characterization between ~2.5k and 20k nodes.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-299
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as scale-blindness — a 10x ceiling validated only at current load.
      15a: Searched performance cliffs in force-directed layout and validating limits across the permitted range.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Force-directed render limits (Weber/Medium "Best Libraries for Large Force-Directed Graphs"; GraphAware PIXI.js scale-up). — D3+SVG hits a performance cliff around ~1000+ nodes because the full DOM tree is retained; performance degrades non-linearly well below 20000, so a 20000 SVG cap can permit unrenderable graphs.
    2. Graph-viz efficiency benchmarks (PMC12061801 web-library comparison; GraphWaGu PDF). — Empirically, popular web libraries slow sharply with node/edge count; the safe node count is rendering-method-dependent and must be measured, not assumed.
    3. Capacity-must-be-tested principle (octocore Capacity vs Load; SRE headroom guides). — A configured ceiling is not a tested safe limit; true capacity is found experimentally, so a cap set 10x above the only tested point is uncharacterized across most of its range.

  Strength of support: Strong

  Summary: Strongly supported. Browser force-directed rendering has well-documented non-linear performance cliffs (notably ~1000+ nodes for D3/SVG), so "20000 renders gracefully" cannot be inferred from a single 2529-node success. The capacity-planning literature is explicit that a configured limit is not a tested limit. The ~2.5k–20k range is uncharacterized, meaning the raised cap could re-admit the very render failure the cap exists to prevent (couples ASSUMPTION-267). The scale-blindness the presumption names is a real, literature-recognized gap.

  Caveats: For a dataset growing slowly (222 triplets → 2529 nodes over the project's life), the untested upper range may never be reached, making exhaustive perf characterization arguably YAGNI in the near term (see 15b). Support is for the gap's existence, not its imminent realization.

  Recommendation: SUPPORTED
