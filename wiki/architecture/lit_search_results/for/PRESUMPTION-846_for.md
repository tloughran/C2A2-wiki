SEARCH-FOR-PRESUMPTION-846:
  Date searched: 2026-08-25
  Original item: PRESUMPTION-846
  Original statement: [inferred] That a pipeline's absence is self-announcing — that monitoring
    scoped to artifact freshness can detect a job that never started.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-846
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by asking which instrument in the fleet takes a non-event as its subject.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Search scope: WebSearch, August 2026, no date restriction. Queries covered: liveness vs. safety
    properties (Alpern & Schneider); heartbeat and dead-man-switch monitoring; alerting on the
    absence of expected events; data-pipeline freshness SLA monitoring and detection of jobs that
    never started; Airflow SLA-miss mechanics and scheduler observability / expected-run
    declaration. Classification: comprehensive for the data-observability and cron-monitoring
    practitioner literature, which addresses this claim head-on; adequate for the formal
    liveness/safety anchor. Gaps: the strongest sources here are vendor documentation and
    engineering blogs rather than peer-reviewed work; I found no controlled study measuring
    freshness monitoring's actual detection rate for never-started jobs.

  Supporting evidence found: Yes

  Sources:
    1. WatchLoop, "ETL Pipeline Monitoring: Start, Success & Duration Signals."
       https://watchloop.live/blog/etl-pipeline-monitoring
       — [read as search snippet] Direct support for the operative half of the claim: "You should
       detect when scheduled jobs do not begin on time by monitoring job schedules and comparing
       the expected start times with actual start times... The monitoring system can alert on
       silence, catching the 'pipeline never started' case." Also recommends "an independent
       watchdog for the orchestrator itself." Note that the mechanism described is a *declared
       expected start time* compared against observation — an external expectation, not a
       self-announcement.
    2. Conduktor, "Data Freshness Monitoring: SLA Management."
       https://www.conduktor.io/glossary/data-freshness-monitoring-sla-management
       — [read as search snippet] Defines a data freshness SLA as "an explicit commitment about how
       current a table must be, such as no older than four hours between 07:00 and 20:00 on
       business days." Supports the claim's core mechanism: freshness monitoring converts a
       non-event into an alertable condition by pinning the artifact to a declared staleness bound.
    3. Datatrail, "Data Pipeline Monitoring — Catch Stale Data."
       https://datatrail.ai/features/freshness-monitoring ; and Dataworkers, "What Is Stale Data?
       Definition, Detection, and Prevention." https://dataworkers.io/resources/what-is-stale-data/
       — [read as search snippets] The key supporting distinction: "An orchestrator reports whether
       a task ran and exited without error, while freshness monitoring measures whether the table
       actually has current data. A job can succeed against an empty source, a DAG can be paused
       for weeks, and a table can be loaded by a process outside the orchestrator entirely — in all
       three cases the orchestrator is green and the data is stale." The "DAG paused for weeks"
       case is precisely a job that never started, and this source asserts freshness monitoring
       catches it where run-status monitoring does not. This is the single most on-point piece of
       support located.
    4. Dead-man-switch / heartbeat monitoring literature: UpDog, "What is a Dead Man's Switch?
       Heartbeat Monitoring Explained," https://updog.watch/learn/what-is-dead-mans-switch ;
       OnlineOrNot, "Cron job monitoring: How to know when your scheduled tasks fail,"
       https://onlineornot.com/cron-job-monitoring-guide ; AppStatus, "Heartbeat Monitoring,"
       https://appstatus.io/docs/heartbeats
       — [read as search snippets] Establishes alerting-on-absence as a mature, standard pattern:
       "absence is the signal"; "the alert triggers on absence of activity, not presence. If your
       job stops running for any reason — crash, server down, crontab deleted — you'll know."
       Also documents the grace-period parameterisation (hourly job: 5–10 min; daily: 30–60 min;
       weekly: hours) that makes the absence decidable. Strong support that non-events are
       routinely and reliably monitorable.
    5. Alpern, B., Schneider, F.B., 1985. "Defining Liveness." *Information Processing Letters*
       21:181–185. https://www.cs.cornell.edu/fbs/publications/DefLiveness.pdf
       — [read as search snippet + PDF landing page] The formal anchor. Liveness properties
       stipulate that "something good eventually happens"; every property is the intersection of a
       safety property and a liveness property. Supports the claim's well-posedness: "the pipeline
       ran" is a liveness property, and the classical result is that liveness is *not* refutable by
       any finite observation — which is why detection requires converting it into a bounded
       safety property by declaring a deadline. Freshness SLAs and grace periods are exactly that
       conversion. This source therefore supports the claim's mechanism while explaining why the
       declared bound is not optional.
    6. Astronomer, "Expert Tips for Monitoring the Health and SLAs of your Apache Airflow DAGs."
       https://www.astronomer.io/blog/expert-tips-for-monitoring-the-health-and-slas-of-your-apache-airflow-dags/
       and Apache Airflow Tasks documentation,
       https://airflow.apache.org/docs/apache-airflow/2.2.4/core-concepts/tasks.html
       — [read as search snippets] Supports the claim's feasibility in a concrete scheduler while
       naming the boundary conditions: "Only scheduled tasks will be checked against SLA... manually
       triggered tasks will not invoke an SLA miss," and "if your DAG does not have an interval
       between runs, meaning there is no schedule, Airflow fails to calculate the execution dates,
       leading it to miss any triggered runs." Also documents the canary-DAG practice for scheduler
       health.

  Strength of support: Moderate

  Summary: The claim's operative half — that monitoring scoped to artifact freshness can detect a
    job that never started — is directly and repeatedly supported. The data-observability
    literature makes this its central selling point, drawing an explicit contrast between
    orchestrator run-status monitoring (which reports nothing when nothing ran) and freshness
    monitoring (which fires because the artifact aged past its declared bound regardless of why).
    The paused-DAG case named in that literature is exactly the never-started case. The
    dead-man-switch pattern independently establishes alerting-on-absence as mature standard
    practice with well-understood parameterisation. Alpern & Schneider supply the formal reason
    this works: "the job ran" is a liveness property, unrefutable by finite observation, and
    freshness deadlines are the standard device for converting it into a decidable safety property.
    What the literature does *not* support is the claim's framing clause, "a pipeline's absence is
    self-announcing." In every source located, the absence becomes announceable only because
    something outside the pipeline declared, in advance, what should have been true by when.
    The announcement is manufactured by the declaration, not emitted by the absence.

  Caveats: (a) Freshness monitoring detects never-started jobs only where the artifact's expected
    cadence has been declared and the artifact is genuinely expected to change on every run; a run
    that legitimately produces no change is indistinguishable from a run that never happened.
    (b) Coverage is per-artifact: an unmonitored artifact, or a job producing no durable artifact
    at all, is outside this instrument's reach entirely — the presumption's scope claim ("monitoring
    scoped to artifact freshness") is therefore bounded by the artifact inventory. (c) The Airflow
    evidence names two silent-gap conditions: unscheduled/manually-triggered runs are not
    SLA-checked, and DAGs without an interval can miss runs without SLA evaluation. (d) The
    strongest sources are commercial data-observability vendors with an interest in this
    conclusion; I found no independent measured evaluation. (e) Alpern & Schneider is a formal
    verification paper; its application here is conceptual transfer on my part, not something the
    paper itself asserts about monitoring practice.

  Recommendation: PARTIALLY-SUPPORTED

  PARTIAL NOVELTY-FLAG:
    Item: PRESUMPTION-846
    Searched: liveness vs safety properties; heartbeat/dead-man-switch monitoring; alerting on
      absence of expected events; freshness SLA monitoring for never-started jobs; Airflow
      scheduler observability and expected-set declaration.
    Finding: The detection sub-claim is thoroughly addressed and supported. The framing sub-claim
      — that absence is *self*-announcing, i.e. that the non-event carries its own signal without
      a prior externally-held declaration of what was expected and by when — is not supported by
      anything I found, and is implicitly denied by the structure of every mechanism located
      (grace periods, freshness SLAs, expected-start-time comparison, canary DAGs all require a
      declared expectation held outside the thing being monitored). I found no source arguing that
      absence is detectable without such a declaration.
    Implication: The system's expected-set declaration — the register of what should run, how
      often, and producing which artifact — is the load-bearing component, not the freshness check
      itself. A pipeline absent from that register is absent from the monitoring, and that
      second-order absence is not covered by any instrument located in this search.
    Recommended status: PARTIAL NOVELTY — unaddressed sub-claim: that a pipeline's absence
      announces itself without a prior, externally-maintained declaration of expected runs.
