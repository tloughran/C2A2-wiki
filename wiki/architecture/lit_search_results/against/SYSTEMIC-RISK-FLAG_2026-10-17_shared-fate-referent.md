SYSTEMIC-RISK-FLAG:
  Date: 2026-10-17
  Raised by: 15b (re-trigger cycle 1 batch)
  Affected items: PRESUMPTION-1099, ASSUMPTION-514, PRESUMPTION-1102 (secondary); PRESUMPTION-1100
    (complexity facet only)
  Common vulnerability: Each remedy adds a referent that is meant to check the system, but which
    shares fate with what it checks. PRESUMPTION-1099: the shared run record is written by the same
    pipeline whose health it reports; if the writer stalls, the record reads "last healthy".
    ASSUMPTION-514: the seeded denominator is planted and recovered by agents from the same model
    family over the same corpus; seeds and finders share blind spots. PRESUMPTION-1102: a backoff
    state that fails to reset quietly degrades the poller the shared record depends on. Secondary
    (1100, 1102): each remedy adds state (fields, counters) that can go stale and mislead.
    In each case the check can fail in the same way as the thing checked, so the failure stays silent.
  Literature basis:
    - PromLabs, "Meta-Monitoring Architecture" [read in full]: self-monitoring "is brittle"; the
      watcher must be separate so it is "less likely to suffer from the same problems".
    - Ewaschuk 2016, SRE book ch. 6 [read in full]: keep monitoring simple; avoid dependency
      hierarchies; unused signals are removal candidates.
    - Knight & Ammann 1985, NTRS 19860020890 [abstract]: seeded errors not equally detectable
      within type; seeded and indigenous errors interfere.
    - Chun 2006, EJOR [snippet]: capture-recapture independence assumption; correlated model better.
    - US7631076 (IBM) background [partial]: adaptive polling lags activity.
  Related precedent: PRESUMPTION-991 cycle 3 (2026-10-12) — 09-03 metabolism-snapshot freeze went
    unnoticed; instrument liveness was an unregistered auxiliary.
  Risk level: High
  Recommendation: For every self-check C2A2 relies on, state (1) what independent path detects the
    checker's own failure (freshness/TTL, heartbeat-absence alarm, or human/other-tool seed), and
    (2) treat a stale or unverified checker as UNKNOWN/INCONCLUSIVE, never as pass. One concrete
    test covers most of the cluster: stall a checker (record writer, seeder, poller) for one cycle
    without stopping the work, and confirm something outside it raises an alarm.
