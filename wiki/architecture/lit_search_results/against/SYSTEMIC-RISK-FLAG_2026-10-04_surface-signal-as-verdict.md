SYSTEMIC-RISK-FLAG:
  Date: 2026-10-04
  Raised by: 15b (Literature Search AGAINST)
  Affected items: PRESUMPTION-1110, PRESUMPTION-1111, PRESUMPTION-1112, PRESUMPTION-1113

  Common vulnerability: A cheap surface signal is used as the final verdict on a content question, with no check against the underlying artefact. When the signal is wrong, the error is silent because the decision removes or skips the very thing that would show it.
    - PRESUMPTION-1110: "same-day output exists" is taken as the verdict "an earlier run completed this slot". Schedulers are at-least-once, and the output may be partial or come from another process.
    - PRESUMPTION-1111: "chat title" is taken as the verdict "contains / lacks designer input". Titles are auto-generated from the first exchange, and excluded chats are never inspected.
    - PRESUMPTION-1112: "LLM recalls a prior publication" is taken as the verdict "candidate is a reissue". Recall confabulates bibliographic detail, worst for less-cited authors, and rejected items are never compared.
    - PRESUMPTION-1113: "PASS" is taken as the verdict on both execution and freshness. One bit cannot carry two independent states, and stale-but-successful runs read green.
    All four are exclusion/skip decisions with asymmetric visibility. False negatives (work skipped, chats excluded, items rejected, staleness hidden) leave no trace for downstream review.

  Literature basis:
    - Google Cloud Scheduler overview (at-least-once delivery; idempotent targets); Red Hat Bug 138001 (cron DST double runs); Kleppmann 2016/2017 (fencing tokens) [background]
    - Galke et al. 2017, arXiv:1705.05311 (titles vs full text; titles strong but lossy); chat auto-titling vendor docs; Heckman 1979 (selection bias) [background]
    - Agrawal et al. 2024, Findings of EACL, arXiv:2305.18248 [fetched]; Walters & Wilder 2023, Sci. Rep.; PMC11530843 (worse for low-citation authors); Topaz et al. 2026, Lancet
    - dbt source freshness; SRE Workbook 2018 ch. 2 (freshness as a distinct pipeline SLI) [background]; practitioner data-observability sources

  Relation to prior flags:
    - SYSTEMIC-RISK-FLAG_2026-10-03_action-as-outcome-proxy: same family. 10-03 covered a task's own *action* standing in for the outcome. This flag covers *metadata/recall/existence* standing in for *content*. PRESUMPTION-1113 extends 10-03 directly (a PASS standing in for freshness).
    - SYSTEMIC-RISK-FLAG_2026-09-29_inherited-pass-status: PRESUMPTION-1110 (existing output read as a prior run's completed work) and 1113 (PASS carried forward) are new instances of inheriting status without re-verification.
    - SYSTEMIC-RISK-FLAG_2026-10-01_silence-read-as-health / 2026-09-09_absence-read-as-all-clear: the exclusion side (1111, 1112) produces silence that would later be read as "nothing relevant".
    The recurrence across 09-09, 09-29, 10-01, 10-03 and 10-04 suggests a design habit, not isolated slips.

  Risk level: Moderate, trending High. Each item's harm is recoverable (re-run, re-ingest, re-check). The pattern is now recurring across consecutive runs and touches ingestion (1111, 1112), scheduling (1110) and status reporting (1113) at once. Failures would be correlated and invisible to the system's own logs. The agent spec's High|Critical scale would put this at High if the 10-03 family is counted together.

  Recommendation (what the system should consider, not a design directive): For every skip/exclude/reject/PASS decision, record which signal it rests on and whether that signal was checked against the artefact itself. Prefer asymmetric policies, where a cheap signal may *include or flag* but only a verified check may *exclude or skip*. Schedule recall sampling of excluded/rejected/skipped sets (e.g., 20-50 items per month) so that false-negative rates become measurable.
