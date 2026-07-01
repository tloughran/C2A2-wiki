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


---

SEARCH-FOR-ASSUMPTION-257 (RE-TRIGGER cycle 3):
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
