SEARCH-FOR-PRESUMPTION-1099 (RE-TRIGGER — 15d, MONITOR-634, cycle 1; Medium):
  Date searched: 2026-10-17
  Original item: PRESUMPTION-1099
  Original statement: [inferred] Monitoring a system split across execution environments needs a shared run
    record; per-environment health checks give false negatives.
  Owed (per 15d block): a source showing that a shared run record with staleness detection catches failures
    that per-environment checks miss (e.g., dead-man's-switch / heartbeat monitoring, distributed tracing,
    SRE monitoring literature).
  Cycle: 1 (RE-TRIGGER by 15d; processed 2026-10-17)

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a, 15b -> 15c -> 15d -> 15a (re-trigger cycle 1)]
    Original item: PRESUMPTION-1099
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred across 2026-09-30 sessions.
      15a (cycle 0, 2026-10-01): PARTIALLY-SUPPORTED (Moderate). SRE book ch. 6 [fetched]; Chandra & Toueg
        1996 [bibliographic]; Prometheus/GitLab dead-man's-snitch [snippet]. No source directly prescribed a
        shared run record.
      15b (cycle 0): independent; not read by this agent.
      15c: -> MONITOR-634 (Medium)
      15d: re-triggered without evaluating evidence; owed = staleness-detecting shared record beats
        per-environment checks.
      15a (cycle 1, 2026-10-17): 2 web searches; 1 fetch (Colyer summary of Huang et al. 2017, read in full).
    Current status: PARTIALLY-SUPPORTED (Moderate)

  Search scope: (a) gray-failure / differential-observability literature (Microsoft Azure); (b) dead-man's-
    switch / heartbeat (absence-of-signal) monitoring for scheduled jobs. Distributed-tracing literature was
    searched but returned nothing specific.

  Supporting evidence found: Partial — strong on the false-negative limb; practitioner-only on the
    shared-record-with-staleness limb.

  Sources:
    1. Huang, P., Guo, C., Zhou, L., Lorch, J.R., Dang, Y., Chintalapati, M. & Yao, R., 2017. "Gray Failure:
       The Achilles' Heel of Cloud-Scale Systems." HotOS '17. (Primary PDF: cs.jhu.edu/~huang/paper/
       grayfailure-hotos17.pdf — NOT fetched.) [read in full — via A. Colyer, "the morning paper", 2017-06-15,
       which quotes the paper extensively; author list from background knowledge — UNVERIFIED]
       Findings quoted:
       - Gray failure is defined as "differential observability": an app observes the system as unhealthy
         while the observer (failure detector) observes it as healthy — i.e., a monitoring false negative.
       - "Gray failure is behind most cloud incidents" (Azure first-hand experience).
       - Case: VMs with severe internal network failure kept passing heartbeats via a host agent over local
         RPC; the problem was not spotted until a user reported it.
       - Case ("finger-pointing"): failures spanning compute and storage clusters were misattributed because
         each subsystem's detector had only a partial view.
       - Prescription: "many gray failure cases we investigated are only detectable in a distributed fashion
         because each individual component has only a partial view"; advocates combining observations from
         many vantage points and "an independent plane that is outside the boundaries of the core system".
       Relevance: peer-reviewed (workshop) industrial evidence that per-component/per-environment health
       checks systematically produce false negatives, and that cross-component aggregation outside any one
       component is the remedy. This is the closest published analogue of the presumption.
    2. Huang et al., 2024. SREcon24 Americas talk (Microsoft Azure / U. Michigan), "Gray Failure: The
       Achilles' Heel of Cloud-Scale Systems" (revisited). [snippet] "nines and heartbeats alone are not
       enough"; multi-dimensional signals needed to close the observation gap.
    3. Panorama (Huang et al., OSDI 2018, "Capturing and enhancing in situ system observability for failure
       detection"). [title only / snippet] Turns components into in-situ observers to catch gray failures.
    4. Dead-man's-switch / heartbeat monitoring for cron and scheduled jobs: crontap.com, enterno.io,
       oneuptime.com, cronjob-guardian docs, Healthchecks.io. [snippet — vendor/practitioner]
       - Inverts monitoring: alert on ABSENCE of an expected ping within a window (= staleness detection).
       - Rationale stated: scheduled jobs have no port to probe; if the scheduler never fires, "there's no
         error email either, and silence looks exactly like normal" — a per-host check sees nothing wrong.
       - The monitor should run outside the host it watches, because the alerting path can die with the host.
       - Limit stated: a heartbeat proves the ping arrived, not that the job did correct work.
       Relevance: direct practitioner support for the staleness-detection mechanism of a shared run record.

  Strength of support: Moderate.
    - False-negative limb: Moderate-Strong (workshop paper with industrial incident evidence, Azure scale).
    - Shared-record-with-staleness limb: Weak-Moderate (practitioner/vendor consensus; no controlled study).

  Summary: The gray-failure literature directly names the failure mode the presumption describes:
    differential observability, where a component's own detector reports healthy while users see failure.
    Its authors report this is behind most Azure incidents and that many such failures are detectable only by
    combining views from multiple components in a plane outside any single one. Dead-man's-switch practice
    supplies the staleness mechanism: alert when an expected run record does not appear, which catches the
    "scheduler never fired" case that no per-host check can see. Together these support the presumption by
    close analogy.

  Owed condition: PARTIALLY met. A source showing that per-component checks give false negatives and that
    cross-component aggregation catches them: FOUND (Huang 2017). A source measuring that a shared run record
    with staleness detection specifically outperforms per-environment checks: NOT found; practitioner only.

  Caveats:
    - Huang et al. concern cloud infrastructure components, not scheduled LLM-agent tasks split across
      cloud and local schedulers. Domain transfer is by analogy.
    - Primary HotOS PDF not fetched; the secondary summary quotes it directly but is still secondary.
    - Huang et al. also note that fully eliminating differential observability is infeasible; a shared
      record narrows, not closes, the gap.
    - Heartbeats prove liveness, not correctness (see PRESUMPTION-1100).

  Recommendation: PARTIALLY-SUPPORTED (Moderate). Upgrade from cycle 0 on the false-negative limb.
