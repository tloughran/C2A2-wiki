SEARCH-FOR-PRESUMPTION-465:
  Date searched: 2026-07-10
  Original item: PRESUMPTION-465
  Original statement: "Appending a FAIL line to a file constitutes surfacing — fail-loud presumes a reliable listener, never verified."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-465
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inference from 2026-07-09 EOD cohort
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. DataSunrise, 2024–2025. "Data Audit Trails: Best Practices for Security & Compliance." — Establishes the genuine value of append-only records: a chronological, tamper-evident record of failures has forensic, compliance, and downstream-review worth independent of whether anyone reads it in real time. Supports FAIL-line appending as a legitimate first layer of error surfacing.
    2. Ping Identity, 2024–2025. "Understanding Audit Trails — Uses and Best Practices." pingidentity.com. — Audit entries capturing action, timestamp, and outcome (success/failure/error code) "preserve the details needed for downstream review"; supports the position that a written failure record is a real artifact of accountability, not a null act.
    3. Last9, 2025. "Logging vs Monitoring: Key Differences Explained." last9.io. — Confirms logging's standing as one of the two pillars: logs record discrete failure events for later analysis. In architectures where a scheduled reviewer *does* read the log (the C2A2 pattern of agents reading state files each run), the written line genuinely is the surfacing mechanism.
    4. OneUptime, 2026. "How to Implement Log Alerting." oneuptime.com. — Log-alerting practice is built on the premise that log lines are the raw substrate from which problems are surfaced ("log alerting bridges the gap by surfacing the specific problems that need attention") — i.e., writing the FAIL line is the necessary first half of a surfacing pipeline, and suffices when a reliable consumer exists.

  Strength of support: Weak-to-Moderate

  Summary: The literature supports a qualified version of the presumption. Append-only failure records have well-established value: audit-trail practice treats written outcome records (including failures) as the evidentiary backbone for downstream review, and the entire log-alerting discipline presumes log lines are the substrate from which problems get surfaced. Crucially, the adequacy of write-only surfacing is architecture-relative: in systems with a scheduled, contractual reader — as in C2A2, where successor agents are obligated to read state files at each run — appending a FAIL line genuinely constitutes surfacing to the listener that exists, and the pattern is analogous to accepted file-based signaling (exit-status files, sentinel files, dead-letter records) in batch systems. No source, however, endorses write-only logging as adequate *without* a verified consumer; the literature that comes closest (audit trails) values the record for retrospective forensics, not timely surfacing.

  Caveats: Support collapses if the "reliable listener" clause fails — logging/monitoring literature is emphatic that logs nobody reads bury the important stuff, and OWASP classes insufficient monitoring of logged events as a top-10 failure. The presumption's own rider ("never verified") is the pressure point: the literature supports FAIL-line appending as surfacing only conditional on a consumer whose reliability is established, which is exactly what has not been verified here.

  Search scope confidence: comprehensive for logging/audit-trail practice; no literature found squarely endorsing unverified write-only error surfacing

  Recommendation: PARTIALLY-SUPPORTED
