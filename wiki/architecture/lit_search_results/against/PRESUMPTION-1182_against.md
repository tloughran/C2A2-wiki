# PRESUMPTION-1182 — Literature Search AGAINST (15b)

Search scope: PRELIMINARY SEARCH. A broader search is recommended. For this item I ran 3 web searches (standard mode) and 1 page fetch, which succeeded: Google SRE Book ch. 6, "Monitoring Distributed Systems", read in full. I read no local files for this item, including routine_health.md and the run_stall source. I did not open lit_search_results/for/ or lit_search_returns.md.

Reading of "challenge" used: I counted evidence as a challenge if it showed that the presumption, or the literature claim tied to it, is (a) mis-specified, meaning established monitoring practice does not handle staleness by stamping each verdict with the age of its inputs; (b) overstated, meaning the cited authority (Beyer et al. 2016, ch. 6) does not require freshness stamps, or argues for simplicity that cuts against adding them; or (c) bounded, meaning staleness protection is normally provided by a different mechanism (input expiry, absence alerts, dead-man's-switch meta-monitoring), so the stated remedy is one option among several. I did not dispute the facts in the item: an 18-day-old routine_health.md read as OK, and OK rows not being written.

```
SEARCH-AGAINST-PRESUMPTION-1182:
  Date searched: 2026-10-25
  Original item: PRESUMPTION-1182
  Original statement: "[inferred] A verdict computed from a stale source is presumed current.
    run_stall reports OK for the daily run from an 18-day-old routine_health.md; the morning
    check reports live-DB checks as fine because OK rows are not written. Extends
    PRESUMPTION-1177 (absence read as absence) to staleness read as health: the output carries
    no freshness stamp on its inputs."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-1182
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred at the 2026-10-24 intake from monitor behaviour (run_stall reading an
           18-day-old routine_health.md as OK; morning check treating unwritten OK rows as
           fine). Framed as an extension of PRESUMPTION-1177.
      15b: Searched for challenging literature (preliminary; 3 searches, 1 fetch)
    Current status: SEARCHED-15b — PARTIALLY-CHALLENGED

  Challenging evidence found: Partial (challenges the remedy and the reading of the cited
    authority, not the diagnosis)

  Sources:
    1. Ewaschuk, R. (ed. Beyer, B.), 2016/2017. "Monitoring Distributed Systems." Ch. 6 in Beyer,
       Jones, Petoff & Murphy (eds.), Site Reliability Engineering. O'Reilly / sre.google.
       [fetched; read in full]
       — Overstatement challenge to the literature claim. Ch. 6 contains no requirement that
       each verdict carry the age of its input. Staleness, freshness, heartbeats and
       dead-man's switches are not discussed in the chapter. Its governing principle runs the
       other way: "As Simple as Possible, No Simpler". It says rules "should be as simple,
       predictable, and reliable as possible", it warns that monitoring "can become so complex
       that it's fragile", and it says signals "not exposed in any prebaked dashboard nor used
       by any alert, are candidates for removal". A freshness stamp on every verdict is the
       kind of per-output metadata the chapter would ask to justify. The chapter does give
       indirect support to the diagnosis. It prefers black-box, symptom-oriented checks of
       whether the system is working "right now", and it notes that only end-to-end checks
       catch an "HTTP 200 success response, but coupled with the wrong content". A stale OK is
       that kind of failure. Ch. 6 is therefore not a source for the freshness-stamp remedy,
       even though it is consistent with the worry.
    2. Prometheus staleness semantics: default 5-minute lookback delta; staleness markers;
       last_over_time / absent_over_time. Sources: OneUptime blog posts (2026-07-31,
       2026-09-29) and a discuss.prometheus.io thread. [snippet only; secondary; the official
       Prometheus docs were not read]
       — Mis-specification challenge to the remedy. In the most widely used open-source
       monitoring stack, staleness is handled by expiring inputs, not by stamping outputs. A
       sample older than the lookback window, or one followed by a staleness marker, is simply
       not returned to an instant query. The rule then evaluates over nothing, and absence is
       caught by absent()/absent_over_time() alerts. On this design a stale input cannot
       produce an OK verdict, because it never reaches the verdict. That is a different and
       arguably simpler guarantee than "each verdict carries the age of its input". Boundary
       condition that cuts back: the same sources stress that "the lookback ... should not be
       interpreted as a missing-data grace period", and that expiry turns staleness into
       absence. That routes the problem straight into PRESUMPTION-1177 (absence read as
       absence). Input expiry fixes 1182 only if 1177 is also fixed.
    3. Dead-man's-switch / Watchdog pattern: always-firing Watchdog alert (vector(1)) routed to
       an external heartbeat receiver; G-Research prommsd; OneUptime (2026-02-06, 2026-07-31);
       dev.to "A dead man's switch for your monitoring stack"; Torproject TPA issue 41641.
       [snippet only]
       — Bounding challenge. The standard answer to "the monitor may itself be stale or dead" is
       a separate, independent meta-monitor that alerts when expected signals stop arriving. It
       is not freshness metadata on each verdict. The snippets stress independence ("the
       up{job="prometheus"} alert stored on that same server will never fire after the process
       dies") and note that, by default, "the absence of data does not trigger any alert".
       Practice therefore puts the guarantee in a heartbeat channel, not in the verdict.
       This is a challenge to the remedy, and it supports the diagnosis.

  Strength of challenge: Moderate against the literature claim as worded ("monitoring practices
    require each verdict to carry the age of its input") and against freshness stamps as the
    remedy. None against the diagnosis that a stale input was read as health.

  Summary: The AGAINST search found nothing showing that it is acceptable to compute OK from an
    18-day-old input. Every source treats unnoticed staleness as a failure. The challenge is to
    the claim's framing and remedy. The cited authority (SRE Book ch. 6) does not mention
    freshness stamps and argues hard for minimal, simple monitoring. Mainstream practice
    (Prometheus) blocks stale-input verdicts by expiring inputs at query time (lookback
    window, staleness markers), and guards the monitor itself with an independent
    dead-man's-switch heartbeat. Neither attaches an input age to each output. Staleness is
    handled upstream, by expiry, and alongside, by heartbeat, not inside the verdict. The
    literature also shows that expiry converts staleness into absence, so 1182's fix depends
    on 1177's fix.

  Specific risks: If C2A2 accepts the presumption with its stated remedy, it may (a) add
    freshness stamps that humans or downstream agents still ignore, so a verdict reads "OK
    (input age 18d)" and is still treated as OK, which is the alert-fatigue and skimming
    failure ch. 6 describes; (b) multiply per-verdict metadata across monitors, against ch. 6's
    simplicity guidance; (c) fix staleness by expiry but leave absence silent (1177 unfixed),
    so a stale input becomes a missing input and the monitor still reports nothing wrong.

  Mitigations available: (i) Input expiry with a hard rule: any input older than its expected
    cadence times k yields STALE/UNKNOWN, never OK (Prometheus lookback-style), so stale input
    cannot produce an OK verdict. (ii) Pair it with an absent-signal rule so expiry produces an
    alert rather than silence (absent_over_time pattern; closes the 1177 coupling). (iii)
    Write OK rows (positive heartbeats) for live-DB checks, so "no row" can mean "check did not
    run" rather than "fine" (dead-man's-switch pattern). (iv) If freshness stamps are added,
    make them gating (they change the verdict), not decorative.

  Recommendation: PARTIALLY-CHALLENGED
```

```
STEELMAN:
  Item: PRESUMPTION-1182
  Strongest counterargument: The problem is real, but "each verdict should carry the age of
    its input" is not what monitoring practice requires, and it is not what the cited source
    says. Google SRE ch. 6 never mentions freshness stamps and spends a full section arguing
    that monitoring should be "as simple as possible". Adding provenance metadata to every
    output is the kind of complexity it warns makes monitoring fragile and its outputs
    skimmed. Prometheus solves the same failure without stamps: a sample past its lookback
    window or staleness marker is simply not used, so no rule can compute OK from it. A
    separate dead-man's switch catches the case where the monitor itself has stopped. The
    right lesson from the literature is "stale inputs must be impossible to evaluate as
    healthy", enforced by expiry and heartbeat. "Every verdict must disclose its input age"
    is a weaker guarantee, because a disclosed age can still be ignored.
  What would need to be true for C2A2 to be safe: (1) every monitor input has a declared
    expected cadence; (2) inputs past cadence are excluded or force a non-OK state; (3) the
    resulting absence raises an alert rather than passing silently (1177 resolved); (4) at
    least one heartbeat runs outside the monitors themselves, so a dead monitor is detected.
  How to test: (a) Back-date a copy of routine_health.md by 18 days in a sandbox and run
    run_stall. Any OK output confirms the failure. Then add a cadence-based expiry and confirm
    the output becomes STALE/UNKNOWN. (b) Stop writing live-DB check rows for one cycle and
    confirm the morning check raises an alert rather than reporting fine. (c) Ask a reader,
    blind, to act on a stamped verdict ("OK, input 18d old") and on an expired verdict
    ("UNKNOWN, input stale"), and compare how often each is treated as healthy.
```

```
SYSTEMIC-RISK-FLAG (CANDIDATE — preliminary, for 14b reconciliation):
  Date: 2026-10-25
  Affected items: PRESUMPTION-1179, PRESUMPTION-1182 (and, by 1182's own statement,
    PRESUMPTION-1177)
  Common vulnerability: Both items rely on monitors that infer health from the absence of a
    negative signal, not from the presence of a positive, path-tagged, time-bounded one. In
    1179 the cloud path cannot be confirmed because nothing positive is observed from it. In
    1182 OK is inferred from an old file and from rows that were never written. In both, the
    missing piece is a positive heartbeat, not a richer verdict. AGAINST-side caveat: in both
    items the literature challenges the stated remedy (an independent observer in 1179,
    freshness stamps in 1182) more than the diagnosis, and the same shared fix (effect-based,
    expiring heartbeats) addresses both.
  Literature basis: Beyer et al. 2016, SRE Book ch. 6 (black-box monitoring of externally
    visible behaviour; read in full). Dead-man's-switch / Watchdog pattern (prommsd, OneUptime;
    snippet only). Prometheus staleness and absent_over_time semantics (secondary; snippet only).
  Risk level: High (structural)
  Recommendation: 14b to consider a single cross-cutting rule: every scheduled routine emits a
    positive, source-tagged, timestamped heartbeat artefact, and every monitor treats a missing
    or expired heartbeat as non-OK. That would bear on 1177, 1179 and 1182 together.
```

Source-reading status: Source 1 [fetched; read in full]. Sources 2 and 3 [snippet only, via search-result summaries; secondary blog and vendor sources]. I did not read the official Prometheus querying or staleness documentation, the SRE Workbook chapters on monitoring or alerting on SLOs, or any data-observability literature on freshness SLOs. Statements about them are framing only and UNVERIFIED. A search for primary literature that explicitly requires per-verdict input-age metadata was not run, because the budget did not allow it, so whether such a norm exists elsewhere (e.g., data-pipeline freshness SLOs) remains untested.
