SEARCH-FOR-PRESUMPTION-690:
  Date searched: 2026-08-06
  Original item: PRESUMPTION-690
  Original statement: That a scheduled task's environment is capable of the
    task; metabolism regen is established as structurally impossible where it
    is scheduled and remains scheduled there, with no channel by which the
    schedule could learn otherwise. Risk: High.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-690
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a task arguing for its own relocation on structural
        grounds, second day.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Real-time schedulability and admission-control literature: Wellings, A.
       et al. / Springer, "Scalable Online Feasibility Tests for Admission
       Control in a Java Real-Time System," Real-Time Systems (DOI
       10.1007/s11241-005-4679-0) [author list not verified]; Abdelzaher, T. &
       Shin, K. [attribution uncertain], "Utilization-Based Admission Control
       for Scalable Real-Time Communication," Real-Time Systems (DOI
       10.1023/A:1021778402786); and the schedulability-test comparison
       literature for rate-monotonic scheduling (ScienceDirect
       S1665642313715517). — The strongest support, and it is real. In this
       class of scheduler the presumption is not an assumption at all: it is an
       enforced invariant. Fast online feasibility tests are run *before* a
       thread is allowed to enter the system; a task is admitted only while it
       remains feasible under worst-case execution-time estimates; under
       overload the controller degrades or rejects. Where such a gate exists,
       "the environment is capable of the task" is true by construction,
       because incapability is the rejection condition.
    2. Cron and cron-class scheduler behaviour (practitioner literature,
       consistent across many independent sources this session; no
       peer-reviewed source located). — Cuts the other way and identifies which
       class C2A2's scheduler is in. The recurring formulation is that cron was
       designed to be minimal, acts as a scheduler and not a monitoring system,
       and has no concept of success — only of execution. By default a failed
       or missed run produces no alert. Environment drift — changed variables,
       secrets, permissions — is listed as a leading cause of failure. This is
       exactly the item's "no channel by which the schedule could learn
       otherwise," and it is a documented and widely acknowledged property of
       the design, not an accident of this system.
    3. Configuration-drift literature (Spacelift, Harness, Octopus Deploy, Wiz
       — practitioner sources; no peer-reviewed source located this session).
       — Explains why even a correct admission decision decays. Configuration
       drift is defined as the gradual divergence of a running environment from
       its intended baseline through untracked change. The recommended controls
       are continuous detection, scheduled comparison of runtime state against
       a declared desired state, and policy-as-code guardrails — that is, a
       standing *re-verification* channel rather than a one-time check. The
       existence of this whole control category concedes the presumption is
       unsafe over time.
    4. Cron-job heartbeat and dead-man's-switch monitoring (Sentry Crons
       documentation and the broader cron-monitoring practitioner literature).
       — Directly addresses the item's "did it produce" versus "could it have"
       distinction, and shows the industry has only solved the first. Heartbeat
       monitoring detects that a job did not report completion. It does not
       distinguish a transient failure from structural impossibility, and it
       cannot detect a job that completes vacuously. No located source
       describes a scheduler that re-evaluates whether an already-admitted
       recurring job's environment still satisfies the job's preconditions.
    5. Kubernetes scheduler node-feasibility filtering. [UNVERIFIED — cited
       from established knowledge, not confirmed this session] — Noted as the
       widely deployed middle case: the scheduler filters to feasible nodes
       before binding a pod, so placement is feasibility-checked, but a
       CronJob's *task-level* preconditions are not. Included for completeness;
       not relied on for the recommendation.

  Strength of support: Moderate — but only inside the boundary condition

  Summary: This is the one item in this batch where supporting literature
    genuinely exists, and it exists because a whole class of schedulers makes
    the presumption true by refusing to schedule anything for which it is
    false. Real-time and cluster admission control run a feasibility test
    before a task enters the system and reject or degrade under overload, so
    "the environment is capable of the task" is an enforced invariant rather
    than a hope. The support does not transfer to the case in this item. Cron
    and cron-class schedulers, which is the design C2A2's recurring tasks
    match, are documented as having no concept of success, no feasibility gate,
    and no default failure signal — environment drift is a named leading cause
    of their failures. Configuration-drift practice concedes the deeper point:
    even a correct one-time feasibility decision decays, which is why the
    recommended control is continuous re-comparison against a declared desired
    state rather than a check at admission. On the item's "did it produce"
    versus "could it have" distinction, the industry's answer — heartbeat and
    dead-man's-switch monitoring — solves only the first, and no located source
    describes a scheduler that re-verifies feasibility for an already-admitted
    recurring job.

  Caveats: The support is conditional and does not apply here unless C2A2's
    scheduler has an admission gate, which the item implies it does not. The
    real-time schedulability literature concerns resource feasibility —
    processor demand, utilisation, worst-case execution time — and does not
    cover semantic or structural impossibility of the kind described ("regen is
    impossible in this location"), which is not expressible as a utilisation
    bound. That is a real limit on the transfer. Several of the strongest
    sources on the against side are practitioner rather than peer-reviewed,
    which weakens their standing though their agreement is unusually uniform.
    Author attributions on sources 1 are uncertain and should be confirmed
    before onward citation. Source 5 is unverified.

  NOVELTY-FLAG: Partial, and worth recording. The literature covers feasibility
    verification *at admission* (real-time scheduling) and drift detection *of
    configuration* (infrastructure-as-code), but no source was located
    addressing the specific case this item names: periodic re-verification that
    a recurring task's environment still satisfies the task's structural
    preconditions, with a feedback channel from the executing task back to the
    schedule. The nearest constructs — heartbeats, liveness probes, drift
    detection — each solve an adjacent problem. A scheduler design in which a
    task can report "I am not runnable here" and have the schedule act on it
    appears to be a genuine gap rather than a gap in this search.

  Recommendation: PARTIALLY-SUPPORTED

  Search scope: Adequate. Concepts searched: real-time schedulability tests and
    online admission control; utilisation-based feasibility analysis; cron
    silent failure, environment drift and heartbeat monitoring; configuration
    drift and continuous verification against declared desired state;
    "did it produce" versus "could it have" as a monitoring distinction.
    Not searched in depth: HPC batch schedulers (Slurm, PBS) which reject jobs
    requesting unsatisfiable resources and are a closer institutional analogue;
    and the workflow-orchestration literature (Airflow sensors, task
    preconditions), both recommended as follow-up seams.
