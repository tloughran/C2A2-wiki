SEARCH-AGAINST-PRESUMPTION-1113:
  Date searched: 2026-10-04
  Original item: PRESUMPTION-1113
  Original statement (presumption under test): One PASS/FAIL field can carry both whether a run succeeded and whether its data are fresh.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1113
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference (lane: observability — job health vs data freshness/SLOs; data-pipeline freshness monitoring).
      15b: Searched for challenging literature; found SRE and data-observability practice that treats run success and freshness as separate signals; strength: Strong
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. "Your pipeline is running, your data is wrong, and you have no idea" (Data Engineer Things blog); Kestra "Data Pipeline Monitoring"; Airbyte "Data Pipeline Observability"; CubeAPM "Observability for data pipelines" [search-result, practitioner] — Agree that "pipeline success and data freshness measure different things, and teams routinely treat the first as a proxy for the second". A job "could run successfully but produce no new data". Freshness must be measured separately, from the timestamp of the newest record against an expected interval.
    2. dbt Labs, `dbt source freshness` (via Paradime "Snapshot Source Data Freshness" template and "dbt Source Freshness Best Practices"; Astronomer "checking-freshness" skill) [search-result] — Mainstream tooling puts freshness in a *separate command* with its own three-state result (pass / warn / error), apart from model run success. The Paradime template has distinct alert channels for freshness failure and for the freshness *job's own* SLA breach. The field's tools keep the two dimensions apart.
    3. Beyer, B., Murphy, N.R., Rensin, D., Kawahara, K. & Thorne, S. (eds.), 2018. The Site Reliability Workbook, ch. 2 "Implementing SLOs" (data-processing pipelines: freshness, correctness, coverage as distinct SLIs); and Site Reliability Engineering (2016) ch. 6 [background-knowledge] — For pipelines, SRE practice defines freshness as its own SLI next to correctness and coverage, rather than inferring it from job exit status.
    4. Data-quality dimension frameworks (e.g. Wang, R.Y. & Strong, D.M., 1996, "Beyond Accuracy: What Data Quality Means to Data Consumers," J. Management Information Systems 12(4); timeliness as a distinct dimension) [background-knowledge] — Timeliness/currency is a separate quality dimension. Collapsing it into a process-success flag loses information that consumers need.

  Strength of challenge: Strong

  Summary: Observability and data-engineering practice consistently treat "the job ran successfully" and "the data are fresh" as independent signals that can disagree in both directions. Success with stale data (no new upstream records, wrong window, cached input) is the classic silent failure. A failed run over still-fresh data (a non-critical step erroring) is the reverse. One PASS/FAIL field can represent only one combination rule. If PASS means "ran OK", staleness is hidden. If PASS means "ran OK AND fresh", a FAIL does not say which dimension failed, and consumers cannot tell "retry the job" from "upstream is dry". Either way, a later reader of the log cannot recover the missing dimension.

  STEELMAN:
    Item: PRESUMPTION-1113
    Strongest counterargument: Folding two independent failure modes into one bit gives two bad options. If the bit tracks execution, stale-but-successful runs, the most common silent failure in data pipelines, show as PASS indefinitely, and downstream tasks that trust the PASS reuse stale data. If the bit tracks the conjunction, a FAIL is ambiguous, and readers, being human or agent, will tend to read it as an execution failure and re-run a job that cannot fix an upstream freshness problem. Mainstream tools (dbt, SRE SLIs) separate these signals because collapsing them has failed in practice.
    What would need to be true for C2A2 to be safe: PASS is explicitly defined as "succeeded AND data newer than threshold T", with the freshness timestamp checked against the data rather than the run time; FAIL carries a reason code that separates the two; and no consumer reads PASS as only one of the two meanings.
    How to test: For each task emitting PASS/FAIL, write down what PASS asserts. Inject a stale-input case (upstream unchanged) and confirm the field turns FAIL or a separate freshness field flags it. Audit historical PASS rows for runs whose output timestamp did not advance.

  Specific risks: Stale data reported as PASS and carried forward (compounding with inherited-PASS patterns); ambiguous FAILs drive wrong remediation; dashboards and run logs overstate pipeline health.

  Mitigations available: Separate fields (run_status, data_as_of / freshness_status); a reason code on FAIL; freshness measured from data timestamps (newest record/file mtime) with warn/error thresholds; SLO-style freshness targets per artefact.

  Caveats: A single composite go/no-go bit is reasonable for a *gate* where the consumer only needs "safe to use?", provided it is defined as the conjunction and the diagnostic detail is logged elsewhere. The challenge is to the field carrying *both* meanings for readers who need to tell them apart, or carrying them implicitly.

  Search scope: preliminary search (2 searches, 0 fetches), plus established SRE/data-quality background; independent of 15a.

  Recommendation: CHALLENGED
