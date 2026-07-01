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


---

SEARCH-FOR-PRESUMPTION-299 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: PRESUMPTION-299
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14b
    Chain: [14b->15a,15b->15c->15d->15a,15b->15c]
    Original item: PRESUMPTION-299
    Item type: PRESUMPTION
    Transform at each step:
      cycle 0..2: prior search/disposition cycles (see blocks above)
      15d (2026-06-28): re-triggered on weekly cadence (catchup run; next_check elapsed)
      15a (cycle 3, 2026-06-30): re-searched for supporting literature
    Current status: refresh; no new supporting literature surfaced this cycle.

  Run context: Clean weekly drain via the c2a2-lit-search-pipeline scheduled task (15a/15b/15c), running one hour after the 14a/14b self-awareness pipeline. Cohort re-triggered by 15d on 2026-06-28 (weekly catchup — first 15d fire since 2026-06-07; the 06-14 and 06-21 weekly runs did not fire, so the 06-28 run drained the accumulated due cohort). This 15a/15b/15c run processes that 147-item re-trigger cohort (124 carry-over weekly items at cycle 3 + 23 newer weekly items at cycle 1).
  Landscape check: Automated landscape spot-check this cycle (6 genuine web searches across distinct clusters: Goodhart's-law / surrogate-metric validity (count-rate as a productivity proxy); git pull --rebase --autostash safety on dirty / untracked working trees; dashboard data-freshness / staleness observability and per-widget as-of timestamps; human-in-the-loop quality-gate routing vs blanket deferral; SMS-OTP / passwordless authentication security momentum (NIST SP 800-63-4; UAE/India/Philippines 2026 deprecation deadlines); multi-agent LLM consensus / idealist-convergence). Security cluster reaffirmed STABLE-but-STRONG (anti-SMS-OTP regulatory momentum continues; NIST SP 800-63-4 excludes SMS OTP from AAL2). All other clusters reaffirmed prior for/against profiles; no disposition-flipping literature shift detected. Spot-check is a sample, not an exhaustive per-item search.

  New evidence weighed: No new supporting literature surfaced in the week(s) since the last cycle. The prior cycles' supportive findings stand.

  Sources (new / refreshed): No new sources this cycle.

  Strength of support: Unchanged from prior cycle.

  Summary: Cycle-3 refresh confirms the prior cycle's finding. The supporting literature base has not materially shifted; no new supportive sources surfaced during this automated cycle. The recommendation carries forward unchanged.

  Caveats: An automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; operational evidence from the C2A2 runs themselves remains the more sensitive signal for status change.

  Recommendation: refreshed; carry forward prior recommendation (SUPPORTED)
