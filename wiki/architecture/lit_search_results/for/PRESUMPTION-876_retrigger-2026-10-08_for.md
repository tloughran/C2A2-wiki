SEARCH-FOR-PRESUMPTION-876 (OWED LIMBS ONLY: SRE alarm lifecycle; bitemporal arbitration):
  Date searched: 2026-10-08
  Original item: PRESUMPTION-876
  Original statement: "A dated health verdict in an append-only register can be read as current state
    without a staleness or retraction mechanism."
  Limbs searched: (i) operations/SRE alarm lifecycle: auto-clear, re-arm, flapping, heartbeat/liveness
    timeout; (ii) bitemporal/temporal-database literature, read to ARBITRATE the unarbitrated cycle-0
    disagreement (15a read it as supportive; 15b predicted it decisive against). "Support" = evidence
    that a dated assertion is safely read as current with neither staleness nor retraction machinery.
  Cycle: 1 (RE-TRIGGER by 15d 2026-09-13, MONITOR-553; processed 2026-10-08)

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c → 15d → 15a (re-trigger cycle 1)]
    Original item: PRESUMPTION-876
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced during 14a's resolution of a three-way contradiction that dissolved once observation
        times were applied
      15a (cycle 0, 2026-08-25): SUPPORTED, Moderate (self-declared preliminary). Event-calculus inertia,
        XTDB/JUXT bitemporal docs and ISA-18.2/OPC UA, all snippet-only; three self-named disqualifiers
      15b (cycle 0): CHALLENGED, Moderate, no targeted query; one "stale-generation" formalisation
      15c: DISPOSITION-813 → MONITOR-553 (HIGH); flagged the bitemporal disagreement for arbitration per
        PREMISE-161
      15d: re-triggered cycle 1 2026-09-13; 15d did not evaluate evidence
      15a (cycle 1, 2026-10-08): 3 searches, 2 fetches; bitemporal source read in full; see below
    Current status: PARTIALLY-SUPPORTED (retraction limb only); NO-SUPPORT-FOUND (staleness limb).
      Cycle-0 SUPPORTED is downgraded.

  Search scope: 3 web searches (Fowler bitemporal history; Snodgrass "now"/"until changed" valid-time
    semantics; Prometheus Alertmanager resolve_timeout + dead-man's-switch/heartbeat + flapping
    hysteresis). Fetches: martinfowler.com/articles/bitemporal-history.html (FULL TEXT) and
    prometheus.io/docs/alerting/0.29/alerts_api/ (FULL TEXT). Snodgrass primary texts NOT read.
    The "Now in Temporal Databases" encyclopedia entry (Dyreson, Jensen & Snodgrass) was located but its
    body was not retrieved. Comprehensive enough to arbitrate; preliminary on the Snodgrass primary sources.

  Supporting evidence found: Partial

  Sources:
    1. Fowler, M., 2021. "Bitemporal History." martinfowler.com, 7 Apr 2021. [fetched, full text]
       Terminology explicitly mapped to Snodgrass's valid/transaction time and SQL:2011. What it actually says:
       (a) "In a simple world a history is append-only. If communication is perfect and instantaneous ...
       we can then just treat history as something we add to." (b) "Bitemporal history is a way of coming
       to terms that communication is neither perfect nor instantaneous." Actual history "is no longer
       append-only". Only the RECORD history is append-only, and corrections are appended ("We don't change
       what we thought we knew ... We just append the later knowledge"). (c) Every assertion carries an
       ACTUAL-time RANGE as well as a record time. Current state is read by defaulting record time to
       today against those ranges. (d) "If we are merely recording a history ... we essentially ignore
       record history", and bitemporality is to be avoided when possible because it "complicate[s] a
       system quite significantly".
    2. Prometheus Alertmanager, Alerts API (v0.29 docs). [fetched, full text] "If omitted, Alertmanager sets
       `endsAt` to the current time + `resolve_timeout`." "Clients are expected to re-send firing alerts ...
       at regular intervals until the alert is resolved." "Firing alerts are resolved once their `endsAt`
       timestamp has elapsed." The SRE default is the inverse of inertia: an un-reasserted firing verdict
       EXPIRES. Currency is a lease that must be renewed, not a default that persists.
    3. Dead-man's-switch / heartbeat practice (dev.to, OneUptime, Crontap write-ups). [search-result]
       Silence is treated as a failure signal. An always-firing watchdog whose ABSENCE raises an alarm
       exists because a monitor "can't reliably report its own failure". This is a liveness-timeout
       mechanism, i.e. explicit staleness detection.
    4. Flapping/hysteresis (Nagios forum; Zabbix "recovery expression" best-practice docs; industrial
       alarm guide). [search-result] Raise and clear use separate thresholds and on/off delays. Clear
       semantics are actively specified, not left to persistence.
    5. GitHub checks API (Enterprise Server docs). [search-result] A check run left incomplete for more
       than 14 days has its conclusion set to `stale` by the platform: an automatic staleness verdict.
    6. Dyreson, C., Jensen, C. S. & Snodgrass, R. T. "Now in Temporal Databases." Encyclopedia of Database
       Systems. [search-result; keywords only] Indexed keywords include "until changed" and "current
       time", which indicates that open-ended validity ("until changed") is a modelled, explicit value
       in the temporal-database literature. Body not read.

  ARBITRATION (cycle-0 15a vs 15b on the bitemporal literature), per PREMISE-161:
    Both cycle-0 readings were partly right, about different halves of the presumption, and the split is
    clean. The bitemporal literature SUPPORTS "no RETRACTION mechanism": corrections are appended, nothing
    is deleted, and the append-only record history is the audit trail (Fowler 1b). It does NOT support "no
    STALENESS mechanism". It decides against that half in two ways. First, the model exists precisely
    because the "perfect and instantaneous communication" condition fails (Fowler 1a–b), and that
    condition is exactly what reading an old verdict as current presupposes. Second, the current-state
    read works only because each assertion carries an explicit actual-time validity range or an explicit
    "until changed" end (Fowler 1c; source 6). That interval is itself the staleness mechanism. A register
    whose entries carry a single date and no validity scope has none, and cycle-0's own caveat (2)
    ("no located source addresses the single-timestamp case") is now answered: the literature treats
    single-axis history as acceptable only for "merely recording a history" (1d), not for current-state
    reads under late information. Cycle-0 15a's supportive reading came from XTDB/JUXT snippets that
    describe as-of queries without the precondition. Read in full, the source supports 15b's prediction on
    the staleness half and 15a's on the retraction half.

  Strength of support: Moderate for "no retraction operation is needed in an append-only register"
    (Fowler). None for "no staleness mechanism is needed". On that half the SRE sources (2–5) are uniformly
    the other way.

  Summary: The owed SRE limb returns no support. Mainstream alerting (Prometheus) makes a firing verdict
    expire unless re-asserted. Heartbeat/dead-man's-switch practice treats absence of fresh signal as a
    fault. Hysteresis practice specifies clearing explicitly. GitHub marks long-incomplete runs `stale`
    automatically. Cycle-0's ISA-18.2/OPC UA "auto-clear by default" reading holds only because a monitor
    continuously re-evaluates the condition, as cycle-0's own caveat (4) noted. Prometheus states that
    dependency outright: currency is a lease. The bitemporal literature, read in full, divides the
    presumption. Retraction-free correction is supported. Staleness-free currency is not, because currency
    depends on an explicit validity interval that a single-dated verdict lacks.

  Caveats: (i) Snodgrass primary texts (1986 IEEE Computer; TSQL2; *Developing Time-Oriented Database
    Applications in SQL*) were not read, so the arbitration rests on Fowler, who cites Snodgrass and maps
    the terms explicitly. (ii) Sources 3–5 are practitioner/vendor material at search-result level.
    (iii) Event-calculus inertia (cycle 0) was not re-searched. It remains the strongest formal warrant
    for persistence, but it presupposes that terminating events are recorded, which an un-rechecked
    register does not guarantee. (iv) Still no source on agent-authored JUDGEMENTS as against sensor
    measurements.

  Recommendation: PARTIALLY-SUPPORTED on the retraction limb; NO-SUPPORT-FOUND on the staleness limb.
    Arbitration result for the record: the bitemporal literature is supportive of append-only correction
    and decisive AGAINST staleness-free current-state reads of single-dated entries. 15b's prediction holds
    for the operative half.

  NOVELTY-FLAG: No.

  Independence attestation: Read: 15a definition; provenance_protocol.md; for/PRESUMPTION-897_retrigger-
    2026-10-07_for.md; for/PRESUMPTION-876_for.md; for_lit_search.md owed-limb note; MONITOR-553 (which
    paraphrases 15b's cycle-0 prediction). NOT read: any against/ file dated 2026-10-08, nor 15b's cycle-0
    PRESUMPTION-876 file.
