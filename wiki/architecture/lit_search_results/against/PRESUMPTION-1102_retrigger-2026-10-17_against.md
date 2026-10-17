SEARCH-AGAINST-PRESUMPTION-1102 (RE-TRIGGER cycle 1):
  Date searched: 2026-10-17
  Original item: PRESUMPTION-1102
  Original statement: [inferred] Polling schedules sized for active work should back off when the
    work completes (adaptive scheduling).
  Under test this cycle (MONITOR-637, Low): costs of backoff (missed restarts, latency on
    resumption, complexity) and evidence that fixed polling is preferable at small scale. Cycle 0
    relied on a retry-after-failure blog; this cycle I looked for sources on idle/activity-driven
    polling specifically.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read lit_search_results/for/, any *_for file, or 15a
    sections of lit_search_returns.md. I read only my own cycle-0 file for this item.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 1)]
    Original item: PRESUMPTION-1102
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred across 09-30 sessions.
      15a (cycle 0): independent; not read by this agent
      15b (cycle 0, 2026-10-01): PARTIALLY-CHALLENGED (Moderate) — transfer challenge from a
        retry-backoff blog; reset-on-new-work bug risk undocumented.
      15c: disposition → MONITOR-637 (Low).
      15d: re-trigger, cycle 0 → 1.
      15b (cycle 1, 2026-10-17): 1 dedicated search (adaptive polling drawbacks); 1 fetch (Google
        Patents US7631076, background section read via targeted extraction — page too large to
        read in full); SRE ch. 6 fetch shared with PRESUMPTION-1099 (read in full).
    Current status: PARTIALLY-CHALLENGED
    Sources this cycle: Cannon & Ramke (IBM) US7631076 [partial — background section and bibliographic
      data only]; Ewaschuk 2016 SRE ch. 6 [read in full]; Adaptive-timer patent US8724612 and VWO
      polling docs [snippet].
    Date: 2026-10-17

  EVIDENCE GRADE: PRELIMINARY. Patent background is an applicant's problem statement, not an
    empirical study; SRE chapter is practitioner guidance.

  Challenging evidence found: Partial

  Sources:
    1. Cannon, D. M. & Ramke, T. F. Jr. (IBM). US Patent 7,631,076 B2, "Apparatus, system, and
       method for adaptive polling of monitored systems" (priority 2004-03-16).
       https://patents.google.com/patent/US7631076 [partial — background section] Describes the
       drawback of activity-driven adaptive polling: "the polling interval adjustment is always
       lagging server activity since the polling interval is not changed until after the activity
       level of the server has changed for a time. If the polling time is set to be a long period,
       and a server operation completes or reaches a next phase, the polling system continues to
       wait until the next scheduled poll". Bearing: this is the precise cost of "back off when
       work completes" — when work RESUMES, detection is delayed by up to the backed-off interval,
       and the schedule trails reality in both directions. Caveat: the patent's own solution is a
       different (state-aware) adaptive scheme, so it argues against naive backoff, not against
       adaptivity per se.
    2. Ewaschuk, R. (ed. Beyer, B.) (2016). SRE book ch. 6. https://sre.google/sre-book/monitoring-distributed-systems/
       [read in full] "Google has trended toward simpler and faster monitoring systems ... We avoid
       'magic' systems that try to learn thresholds"; "Observational experiments conducted over a
       very long time horizon ... with a low sampling rate (hours or days) can also often tolerate
       more fragility because occasional missed samples won't hide a long-running trend"; probing
       "more than once or twice a minute is probably unnecessarily frequent" at 99.9%. Bearing: the
       resolution should be set by the latency budget of the thing watched, not by whether work is
       active; and at C2A2's low sampling rates a single fixed cheap interval is within the regime
       SRE treats as tolerant.
    3. US8724612 (adaptive timers, mobile) and VWO "Configure Polling" docs. [snippet] Fixed short
       intervals waste requests; fixed long intervals add delay; adaptive wins when arrivals are
       bursty. Bearing: mixed — supports adaptivity when traffic is bursty and polling is costly.

  Strength of challenge: Moderate (unchanged)

  Summary: The case against is now sourced to the right scenario (activity-driven polling, not
    retry backoff). Backing off after completion introduces lag on resumption equal to the
    backed-off interval, and activity-tracking schedules always trail actual activity. SRE practice
    favours simple fixed schedules sized to the detection-latency budget and tolerates low sampling
    for slow observational series. Adaptivity pays when polling is expensive and arrivals are
    bursty; at C2A2's scale the per-poll cost is small, which weakens the presumption's motive.

  Specific risks: work restarts during a long backoff and is not observed for hours; the backoff
    state (counter/interval) fails to reset and the poller stays slow indefinitely — a silent
    degradation of exactly the monitoring PRESUMPTION-1099 depends on.

  Mitigations available: set the idle interval from an explicit detection-latency budget, not a
    multiplier; cap backoff at that budget; prefer an event trigger on resumption where available;
    log the current interval in the run record so a stuck backoff is visible.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: PRESUMPTION-1102
  Strongest counterargument: Backing off when work completes optimises the cheap thing (poll
    count) at the expense of the expensive thing (time to notice work restarting or failing). The
    engineers who patented adaptive polling describe its core flaw as always lagging activity and
    waiting out the long interval when state changes. Google SRE's guidance is to pick the
    resolution the detection budget requires and keep it simple; for a small system with cheap
    polls, a fixed interval sized to that budget gives bounded latency and no state to get stuck.
  What would need to be true for C2A2 to be safe: the maximum backed-off interval is below the
    tolerated detection latency, reset-on-activity is tested, and the current interval is
    observable.
  How to test: restart work during a backed-off period and measure time-to-detection against the
    budget; force a reset failure and confirm it surfaces.

  Search scope: preliminary — 1 dedicated search, 1 dedicated fetch (partial), 1 shared fetch.
