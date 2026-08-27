SEARCH-FOR-ASSUMPTION-1160:
  Date searched: 2026-08-25
  Original item: ASSUMPTION-1160
  Original statement: That a fleet of unattended scheduled jobs can be made observable by
    per-job self-reporting, when the observed failure mode is jobs that die before
    they can report — including the job whose purpose is detecting that.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1160
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from four null runs including the health check, with its own
        anti-silence clause quoted against its own silence.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Search scope: WebSearch, August 2026, no date restriction. Queries covered: fail-stop vs
    fail-silent failure taxonomies; dead-man-switch / heartbeat / cron-job monitoring;
    "who watches the watchmen" meta-monitoring and watchdog architecture; gray failure and
    differential observability; Google SRE white-box vs black-box monitoring; Airflow
    scheduler observability and canary DAGs. Sources surfaced span peer-reviewed systems
    literature (HotOS, JACM, IPL), the Google SRE book, vendor/practitioner monitoring
    documentation, and engineering blogs. Classification: comprehensive for the practitioner
    and classical-systems literature; preliminary for any formal treatment of *self*-monitoring
    coverage bounds — I found no formal proof-style work quantifying what fraction of failure
    modes in-process reporting can cover. Gap: no ACM/IEEE full-text database access; all
    peer-reviewed items were reached via search snippets and landing pages, not full text.

  Supporting evidence found: Partial

  Sources:
    1. Beyer, B., Jones, C., Petoff, J., Murphy, N.R. (eds.), 2016. "Monitoring Distributed
       Systems," Chapter 6 of *Site Reliability Engineering*. O'Reilly / Google.
       https://sre.google/sre-book/monitoring-distributed-systems/
       — [read as search snippet + landing page] States that Google SREs "combine heavy use of
       white-box monitoring with modest but critical uses of black-box monitoring." This is the
       strongest available support for the *first* half of the claim: in-process self-reporting
       (white-box) is the primary, recommended observability substrate for production fleets,
       not a deficient one. Note the qualifier "critical" attached to the external component.
    2. Dead-man-switch / heartbeat monitoring practitioner literature, e.g. UpDog, "What is a
       Dead Man's Switch? Heartbeat Monitoring Explained," https://updog.watch/learn/what-is-dead-mans-switch ;
       Crontap, "Dead man's switch, explained for developers,"
       https://crontap.com/blog/dead-man-switch-explained-for-developers ; AppStatus,
       "Heartbeat Monitoring — Cron Job & Scheduled Task Checks," https://appstatus.io/docs/heartbeats
       — [read as search snippets] These describe a working pattern in which the unit of
       instrumentation *is* per-job self-reporting: the job itself emits the ping
       (`backup.sh && curl -fsS https://.../abc123`). This supports the claim that per-job
       self-reporting is the correct instrumentation primitive for a scheduled-job fleet.
       Crucially, however, every source frames the alerting decision as external: "absence is
       the signal," evaluated by a service the job does not control, against a declared
       grace period. Self-reporting supplies the positive evidence; an external timer supplies
       the negative inference.
    3. Astronomer, "Expert Tips for Monitoring the Health and SLAs of your Apache Airflow DAGs,"
       https://www.astronomer.io/blog/expert-tips-for-monitoring-the-health-and-slas-of-your-apache-airflow-dags/
       — [read as search snippet] Documents that "many deployments include a canary DAG to their
       deployment that has a single task, acting to suppress an external alert from going off to
       monitor scheduler health." This is direct evidence that a fleet's meta-observer can itself
       be implemented as a job within the fleet — partial support for the claim's final clause.
       The same snippet immediately qualifies it: "the returned signal does not always indicate
       that the scheduler is working properly, as its state is simply indicative that the service
       is up and running," and separately notes cases "where the scheduler would send a heartbeat,
       but not schedule any tasks or DAGs."
    4. Mercari Engineering, 2022. "Who Watches the Watchmen? Keeping an Eye on Our Monitoring
       Systems." https://engineering.mercari.com/en/blog/entry/20220805-who-watches-the-watchmen-keeping-an-eye-on-our-monitoring-systems/
       — [read as search snippet] A production account of meta-monitoring. Supports the claim only
       in the weak sense that the problem is treated as tractable in practice. The resolution
       described is *external*: GCP services (with Terraform) watch the monitoring systems — i.e.
       the watcher is watched from outside its own failure domain, not by itself.
    5. PagerDuty, "Who watches the watchmen?" https://pagerduty.com/blog/watches-watchmen
       — [read as search snippet] Same shape: PagerDuty consolidates alerts from all monitoring
       systems, i.e. the meta-observation is delegated to a distinct system. Supports tractability,
       not self-sufficiency.
    6. Huang, P., Guo, C., Zhou, L., Lorch, J.R., Dang, Y., Chintalapati, M., Yao, R., 2017.
       "Gray Failure: The Achilles' Heel of Cloud-Scale Systems." *Proceedings of the 16th Workshop
       on Hot Topics in Operating Systems (HotOS '17)*, pp. 150–155. DOI 10.1145/3102980.3103005.
       https://www.microsoft.com/en-us/research/wp-content/uploads/2017/06/paper-1.pdf
       — [read as search snippet + abstract] Introduces "differential observability": a system's
       failure detectors may not notice problems even when applications are afflicted by them.
       Included here because it is the closest peer-reviewed anchor for the claim's *problem
       statement*; it does not support the claim's proposed solution.
    7. Wikipedia, "Fail-silent system," https://en.wikipedia.org/wiki/Fail-silent_system ; and
       standard failure taxonomy (crash / omission / timing / arbitrary) as summarised in
       University of Rochester CSC258 lecture notes, "Fault Tolerance and Recovery in Distributed
       Systems," https://www.cs.rochester.edu/u/sandhya/csc258/lectures/fault_tolerance_recovery.pdf
       — [read as search snippets] Establishes the vocabulary. A fail-silent component "stops
       producing outputs altogether"; the taxonomy distinguishes crash (fail-stop) from omission
       (fail-silent). Provides the terminological support for naming the fleet's observed mode,
       which is a prerequisite for the claim being well-posed.

  Strength of support: Weak

  Summary: The literature strongly supports the *component* practice the claim rests on —
    per-job self-reporting (white-box instrumentation, heartbeat pings emitted by the job
    itself) is the standard and recommended instrumentation primitive for unattended
    scheduled-job fleets, and there is documented production practice of implementing a
    fleet's health monitor as a job inside that fleet (the Airflow canary DAG). But every
    source that endorses self-reporting pairs it with an externally-held expectation: the
    dead-man-switch pattern derives its detection power not from the job's report but from a
    third party's declared grace window elapsing without one. No source I found argues that
    self-reporting alone achieves observability of deaths that precede the report, and none
    argues that a self-monitoring detector can observe its own silence. The Airflow canary
    literature explicitly documents the failure mode where the canary reports healthy while
    the scheduler schedules nothing. Huang et al.'s "differential observability" names the
    general condition under which the claim fails.

  Caveats: (a) The support I found is for a strictly weaker claim — that per-job self-reporting
    is a *necessary and sufficient positive channel*, covering the failure classes in which the
    process survives long enough to report. The claim as stated is scoped precisely to the
    complement of that set. (b) Domain transfer: most heartbeat/cron-monitoring sources are
    vendor marketing for external monitoring services and have an obvious commercial interest
    in the external-observer framing; I weighted them for the mechanics they describe, not their
    conclusions. (c) The Airflow canary evidence cuts both ways and I have reported it as such
    rather than extracting only the supportive half. (d) The classical failure-model literature
    (fail-silent, unreliable failure detectors) is about message-passing consensus systems, not
    scheduled batch fleets; the concepts transfer, the quantitative results do not. (e) I did not
    reach full text for any of the peer-reviewed items.

  Recommendation: PARTIALLY-SUPPORTED

  PARTIAL NOVELTY-FLAG:
    Item: ASSUMPTION-1160
    Searched: fail-silent/fail-stop taxonomies; dead-man-switch and watchdog design;
      meta-monitoring and "who watches the watchmen" patterns; gray failure and differential
      observability; SRE white-box/black-box monitoring; Airflow scheduler observability.
    Finding: The general problem is thoroughly addressed — there is a large, mature literature
      on alerting from absence and on monitoring the monitor, and it uniformly resolves the
      problem by moving the detection decision outside the failing component's failure domain.
      What I could not find addressed is the specific reflexive sub-claim: that a health-check
      job whose own purpose is detecting fleet silence can detect its own silence, i.e. that
      self-reporting closes over the detector. Every treatment located breaks the recursion by
      appeal to an external party (a hosted ping service, a separate cloud project, a distinct
      alerting vendor) and none argues the recursion can be closed internally. The literature
      does not so much refute this sub-claim as decline to entertain it.
    Implication: The reflexive sub-claim ("including the job whose purpose is detecting that")
      is unaddressed by the located literature and should be treated as an untested premise of
      this system rather than as inherited practice. The non-reflexive part of the claim is
      well-covered and weakly supported only under the added condition of an external
      expectation window.
    Recommended status: PARTIAL NOVELTY — unaddressed sub-claim: that a detector implemented
      as a member of the fleet it monitors can observe its own failure to run.
