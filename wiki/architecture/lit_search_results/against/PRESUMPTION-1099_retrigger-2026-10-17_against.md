SEARCH-AGAINST-PRESUMPTION-1099 (RE-TRIGGER cycle 1):
  Date searched: 2026-10-17
  Original item: PRESUMPTION-1099
  Original statement: [inferred] Monitoring a system split across execution environments needs a
    shared run record; per-environment health checks give false negatives.
  Under test this cycle (MONITOR-634, Medium): the disposition tips to REVISE on evidence that the
    shared record itself becomes the blind spot (single point of failure, stale/synced state,
    monitoring-the-monitor). I searched meta-monitoring practice and the Google SRE monitoring
    chapter for that failure mode and for arguments favouring decoupled per-component checks.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read lit_search_results/for/, any *_for file, or 15a
    sections of lit_search_returns.md. I read only my own cycle-0 file for this item.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 1)]
    Original item: PRESUMPTION-1099
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred across 09-30 sessions.
      15a (cycle 0): independent; not read by this agent
      15b (cycle 0, 2026-10-01): PARTIALLY-CHALLENGED (Weak) — shared record is a failure point;
        dead-man's-switch literature mostly corroborates shared record + external staleness check.
      15c: disposition → MONITOR-634 (Medium); REVISE trigger = shared record as blind spot.
      15d: re-trigger, cycle 0 → 1.
      15b (cycle 1, 2026-10-17): 2 searches (meta-monitoring / "who monitors the monitor"; SRE
        monitoring chapter); 2 fetches (PromLabs meta-monitoring page; SRE book ch. 6), both read
        in full. Shared with the systemic search on shared-fate referents (see SYSTEMIC-RISK flag).
    Current status: PARTIALLY-CHALLENGED
    Sources this cycle: PromLabs training [read in full]; Beyer et al./Ewaschuk 2016 SRE ch. 6
      [read in full]; Grafana Labs 2021 blog [snippet]; prommsd / alertdog READMEs [snippet].
    Date: 2026-10-17

  EVIDENCE GRADE: PRELIMINARY-PLUS. Two practitioner primary sources read in full; no academic study.

  Challenging evidence found: Partial — the REVISE trigger condition is documented as a general
    failure mode, but the same sources prescribe a remedy that keeps the shared record.

  Sources:
    1. PromLabs (n.d.). "Meta-Monitoring Architecture." Monitoring and Debugging Prometheus training.
       https://training.promlabs.com/training/monitoring-and-debugging-prometheus/metrics-based-meta-monitoring/meta-monitoring-architecture/
       [read in full] "You could configure a Prometheus server to scrape and monitor its own
       metrics, but that is brittle: as soon as that Prometheus server is experiencing issues that
       would prevent it from correctly collecting data ... your meta-monitoring will break as
       well." Recommends a dedicated, separate pair "whose only job" is watching the main monitor,
       so "it is less likely to suffer from the same problems". Bearing: a shared run record that
       is also where liveness of the recorder is read is self-monitoring in exactly this sense —
       the record's own failure is invisible from inside it. This is the blind-spot condition
       MONITOR-634 names.
    2. Ewaschuk, R. (ed. Beyer, B.) (2016). "Monitoring Distributed Systems." Ch. 6 in Site
       Reliability Engineering (O'Reilly/Google). https://sre.google/sre-book/monitoring-distributed-systems/
       [read in full] Three bearings: (a) "Google SRE has experienced only limited success with
       complex dependency hierarchies" — cross-environment correlation logic is the kind of rule
       they avoid; (b) "maintaining distinct systems with clear, simple, loosely coupled points of
       integration is a better strategy" than blending; (c) black-box, symptom-oriented checks are
       preferred for paging. Bearing: the SRE position favours symptom checks at the user-visible
       edge over a central correlating record — a partial counter to "needs a shared record". It
       does NOT say per-component checks suffice; it says page on end-to-end symptoms.
    3. Grafana Labs (2021). "How we use metamonitoring Prometheus servers to monitor all other
       Prometheus servers at Grafana Labs." [snippet] Cross-cluster meta-monitors watch each other,
       plus a dead-man's-switch heartbeat to an external service. Bearing: at scale the answer to
       a central blind spot is redundancy + external heartbeat, not abandoning the centre.
    4. G-Research prommsd; errm/alertdog (Go packages). [snippet] Inverted alerting: alarm when the
       expected heartbeat STOPS. Bearing: corroborates that absence-of-writes is the dangerous
       failure of a central record.

  Strength of challenge: Moderate (up from Weak) — against the presumption AS STATED (shared record
    as sufficient remedy); None against the false-negative half (per-environment checks miss
    cross-environment failures — no source disputes this).

  Summary: The literature now directly documents the REVISE trigger as a known failure class: a
    monitor that reports on itself goes silent with the thing it monitors. A shared run record is a
    single shared-fate component; if its writer or sync path fails, every environment can look
    "last healthy" at once. But the same sources do not recommend reverting to per-environment
    checks; they add an independent watcher and an external heartbeat that alarms on absence.
    SRE ch. 6 adds a separate push: page on end-to-end symptoms and keep cross-component logic
    simple, rather than build correlation hierarchies.

  Specific risks: C2A2 treats the shared run record as the source of truth; its own staleness (sync
    lag, writer crash, frozen file) reads as "nothing new happened". This is the same shape as the
    09-03 metabolism-snapshot freeze noted in PRESUMPTION-991 work.

  Mitigations available: (1) record carries a written-at timestamp and a TTL; reader treats
    expired as UNKNOWN, not healthy; (2) an always-fires heartbeat entry whose ABSENCE is checked
    from outside the record's write path; (3) one end-to-end symptom check (did the expected output
    appear?) independent of the record.

  Recommendation: PARTIALLY-CHALLENGED — evidence meets the MONITOR-634 REVISE trigger in kind
    (shared record as blind spot is documented), but supports amending the presumption to "shared
    run record PLUS an independent liveness check on that record", not dropping it.

STEELMAN:
  Item: PRESUMPTION-1099
  Strongest counterargument: Centralising status into one record moves the false-negative problem
    rather than solving it. Per-environment checks can miss cross-environment failures; a shared
    record misses its own failure, and that failure silences every environment at once — a
    correlated false negative, which is worse than several uncorrelated ones. Practitioners who run
    monitoring at scale say plainly that self-monitoring is brittle and that the watcher must not
    share fate with what it watches. Google SRE adds that correlation logic across components is
    where monitoring gets fragile, and that the robust page is an end-to-end symptom.
  What would need to be true for C2A2 to be safe: the shared record is never read as healthy
    without a freshness check, and at least one check (heartbeat absence or end-to-end output) runs
    outside the record's write path.
  How to test: stop the record's writer for one cycle without stopping the work. If any reader
    still reports "healthy", the record is a blind spot.

  Search scope: preliminary — 2 searches, 2 fetches. Practitioner sources only; no agent-system study.
