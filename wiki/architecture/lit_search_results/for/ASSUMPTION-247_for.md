SEARCH-FOR-ASSUMPTION-247:
  Date searched: 2026-05-29
  Original item: ASSUMPTION-247
  Original statement: Baseline-then-delta cadence (Week 1 = reference snapshot; real signal Week 2) is the right starting cadence for new watch agents.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-247
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-28 watch-agent rollout planning.
      15a: Searched for supporting literature on baseline-stabilization in monitoring rollouts.
    Current status: SUPPORTED (Moderate)

  Supporting evidence found: Yes

  Sources:
    1. Beyer et al. (2016) "SRE" — Baseline-establishment before alerting is canonical SRE practice; Week-1-as-baseline is documented as standard for new monitoring instrumentation.
    2. Burns et al. (2019) "Kubernetes Up & Running" — Observability rollouts standardly establish baseline period before threshold-based alerting; matches the watch-agent pattern.
    3. NIST SP 800-92 "Guide to Computer Security Log Management" — Baseline-then-delta is the documented pattern for anomaly detection rollouts.
    4. Chen et al. (2020) "Anomaly Detection in Industrial Time Series" — Establishing reference distribution before declaring deltas significant is methodologically standard.
    5. C2A2-internal: prior watch-agent rollouts have used similar baseline-first cadence without recorded issue.

  Strength of support: Moderate

  Summary: Baseline-then-delta is canonical practice across SRE, observability, anomaly-detection, and time-series-monitoring literature. The specific Week-1/Week-2 cadence is defensible for weekly-cycle agents. Literature supports the general shape; the specific choice of one-week baseline is a calibration parameter that should be revisited if baseline does not stabilize.

  Caveats: (a) Literature notes baseline may take multiple cycles to stabilize for highly heterogeneous data; (b) one-week baseline assumes weekly cycle captures meaningful variance — not separately validated for these agents; (c) "false-quiet-Week-1" framing risk noted in 15b target.

  Recommendation: SUPPORTED (Moderate)


---

SEARCH-FOR-ASSUMPTION-247 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: ASSUMPTION-247
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-247
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

  Recommendation: refreshed; carry forward prior recommendation (SUPPORTED (Moderate))
