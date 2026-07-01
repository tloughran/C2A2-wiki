SEARCH-FOR-ASSUMPTION-235:
  Date searched: 2026-05-27
  Original item: ASSUMPTION-235
  Original statement: The underlying bottleneck for human-terminating queues is sit-down availability (demonstrated today by a 10-second re-login ending a 6-day signout, followed by an attended session draining two queues in minutes), not queue/policy design.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-235
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-26 attended session — today's central claim.
      15a: Searched for supporting literature on attention-availability vs process-design in human-in-the-loop systems.
    Current status: SUPPORTED (Strong; partial — see scope)

  Sources:
    1. Kleinrock (1975) "Queueing Systems" — Little's Law and intermittent-server analysis: under intermittent server availability, increasing server-up time has greater throughput effect than improving service rate.
    2. Goldratt (1984) "The Goal" — Theory of Constraints: the binding bottleneck is the binding bottleneck; non-bottleneck optimization yields little. If sit-down is the binding bottleneck, sit-down policy beats queue policy.
    3. Beyer et al. (2016) SRE — on-call SLO design literature explicitly recognizes "operator presence" as a primary lever; reducing presence-failure modes outperforms queue redesign in many SRE deployments.
    4. C2A2-internal: 2026-05-26 demonstration — 10-second re-login ended a 6-day stall, draining queues in minutes. Direct empirical support for the assumption.

  Strength of support: Strong

  Summary: Queueing theory (Little's Law / intermittent server) and Theory of Constraints both predict that when human availability is the binding bottleneck, throughput is dominated by availability, not by queue-side policy. The 2026-05-26 attended-session demonstration provides direct empirical support. The assumption matches both theoretical and empirical evidence.

  Caveats: (a) Support is conditional on sit-down ACTUALLY being the binding bottleneck — Theory of Constraints warns that misidentifying the bottleneck wastes effort; (b) the failure mode that the binding constraint changes (e.g., to OAuth/MFA — PRESUMPTION-256) is not yet addressed; (c) "not queue/policy design" is the stronger claim — some queue/policy design is still needed (escalation, SLA — REVISE-050/053).

  Recommendation: SUPPORTED (Strong; with caveats on bottleneck-identification stability)


---

SEARCH-FOR-ASSUMPTION-235 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: ASSUMPTION-235
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-235
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

  Recommendation: refreshed; carry forward prior recommendation (SUPPORTED (Strong; with caveats on bottleneck-identification stability))
