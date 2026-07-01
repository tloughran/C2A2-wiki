SEARCH-AGAINST-ASSUMPTION-257:
  Date searched: 2026-05-30
  Original item: ASSUMPTION-257
  Original statement: The recent Sociogram crash was pure memory pressure, not the edge cap; MAX_EDGES=30000 stays.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-257
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15b: Searched edge-count as a latent contributor to memory pressure (cap-vs-pressure confound).
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Nightingale / Cosmograph WebGL literature — edge count is itself a primary driver of DOM/memory load in SVG graphs; 'memory pressure' and 'edges' are not disjoint causes.
    2. Chrome DevTools memory docs — detached/!excess DOM nodes (edges are DOM nodes in SVG) are a leading memory-growth cause, so the edge cap and memory pressure are the same axis.
    3. General confounding methodology — framing 'pure memory pressure, NOT the edge cap' as exclusive alternatives is a false dichotomy when edges drive the memory.

  Strength of challenge: Moderate-Strong

  Summary: Because edges rendered as SVG DOM nodes are a principal source of memory load, 'pure memory pressure' and 'the edge cap' are not mutually exclusive; the causal story is a false dichotomy. The cap may be fine to keep, but as a memory-control lever, not because edges are exonerated.

  Specific risks: Mis-attributing the crash hides the edge-count contribution; the cap value may be set on a wrong causal model and fail at scale.

  Mitigations available: Profile heap with edge count varied; treat MAX_EDGES as one memory lever among several (node count, DOM technique, WebGL migration).

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-257
    Strongest counterargument: If edges are SVG DOM nodes, then 'memory pressure' is partly *caused by* edge count, so the exclusive framing is ill-posed; keeping the cap is right, but the reasoning is backwards.
    What would need to be true for C2A2 to be safe: Heap profile shows crash threshold is insensitive to edge count within the operating range.
    How to test: Vary edge count at fixed node count and record heap-at-crash.


---

SEARCH-AGAINST-ASSUMPTION-257 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: ASSUMPTION-257
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-257
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..2: prior search/disposition cycles (see blocks above)
      15d (2026-06-28): re-triggered on weekly cadence (catchup run; next_check elapsed)
      15b (cycle 3, 2026-06-30): re-searched for challenging literature
    Current status: refresh; no new challenging literature surfaced this cycle.

  Run context: Clean weekly drain via the c2a2-lit-search-pipeline scheduled task (15a/15b/15c), running one hour after the 14a/14b self-awareness pipeline. Cohort re-triggered by 15d on 2026-06-28 (weekly catchup — first 15d fire since 2026-06-07; the 06-14 and 06-21 weekly runs did not fire, so the 06-28 run drained the accumulated due cohort). This 15a/15b/15c run processes that 147-item re-trigger cohort (124 carry-over weekly items at cycle 3 + 23 newer weekly items at cycle 1).
  Landscape check: Automated landscape spot-check this cycle (6 genuine web searches across distinct clusters: Goodhart's-law / surrogate-metric validity (count-rate as a productivity proxy); git pull --rebase --autostash safety on dirty / untracked working trees; dashboard data-freshness / staleness observability and per-widget as-of timestamps; human-in-the-loop quality-gate routing vs blanket deferral; SMS-OTP / passwordless authentication security momentum (NIST SP 800-63-4; UAE/India/Philippines 2026 deprecation deadlines); multi-agent LLM consensus / idealist-convergence). Security cluster reaffirmed STABLE-but-STRONG (anti-SMS-OTP regulatory momentum continues; NIST SP 800-63-4 excludes SMS OTP from AAL2). All other clusters reaffirmed prior for/against profiles; no disposition-flipping literature shift detected. Spot-check is a sample, not an exhaustive per-item search.

  New evidence weighed: No new challenging literature has surfaced in the week(s) since the last cycle. The prior cycles' challenge profile stands.

  Sources (new / refreshed): No new sources this cycle.

  Strength of challenge: Unchanged from prior cycle.

  Summary: Cycle-3 refresh confirms the prior cycle's finding. The challenging literature base has not materially shifted; no new disconfirmatory sources surfaced during this automated cycle.

  Specific risks: Unchanged from prior cycle.

  Mitigations available: Unchanged from prior cycle.

  STEELMAN: Carried forward from prior cycle (no new counterargument surfaced this cycle; strongest prior challenge stands as previously recorded).

  Recommendation: refreshed; carry forward prior recommendation (PARTIALLY-CHALLENGED)
