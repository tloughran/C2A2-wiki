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

--- CYCLE RE-SEARCH: 2026-08-25 (15a) ---
  Date searched: 2026-08-25
  Trigger: 15d re-trigger (MONITOR-502, cycle 1). Disposition-changer sought: is periodic
    re-verification that a RECURRING task's environment still satisfies its STRUCTURAL
    preconditions — plus a feedback channel by which the task reports "I am not runnable here"
    and the schedule acts on it — a genuine gap in the literature, or a gap in one search?

  Search scope: Searched scheduling/cron reliability, runtime environment drift, self-adaptive
    systems (MAPE-K), runtime requirements monitoring, and precondition monitoring. Two seams the
    2026-08-06 pass explicitly listed as NOT SEARCHED were opened this cycle and both produced
    direct hits. ACCESSED IN FULL: the kubernetes-sigs/descheduler official repository
    documentation (fetched, ~103k characters, read at the relevant plugin sections); the SEAMS 2011
    AwReqs paper PDF (author-hosted at nemo.inf.ufes.br, downloaded and text-extracted, 54kB).
    NOT ACCESSED: ACM Digital Library full text for the SEAMS paper (author copy used instead);
    Slurm/PBS and Airflow-sensor literature still not searched in depth.
    TOOL LIMIT DECLARED: the session's WebSearch budget (200 calls) was exhausted partway through
    this cycle's work; the remaining retrieval was done by direct fetch and by Crossref/arXiv
    bibliographic APIs. This limited breadth but not the two findings below, which were already in
    hand.

  Supporting evidence found: Yes

  New sources this cycle:
    1. kubernetes-sigs/descheduler, official project documentation (README, "Policy and Strategies"
       section), github.com/kubernetes-sigs/descheduler — FULL-TEXT (fetched and read this cycle).
       **THE FINDING THAT CLOSES THE NOVELTY-FLAG.** The descheduler runs periodically over an
       ALREADY-SCHEDULED workload and evicts it when the environment has drifted out of the
       workload's declared structural preconditions. Two plugins are exactly on point. Verbatim from
       the documentation for `RemovePodsViolatingNodeAffinity`: node affinity of the
       `requiredDuringSchedulingIgnoredDuringExecution` type "tells the scheduler to respect node
       affinity when scheduling the pod but kubelet to ignore in case node changes over time and no
       longer respects the affinity. When enabled, the strategy serves as a temporary implementation
       of `requiredDuringSchedulingRequiredDuringExecution` and evicts pod for kubelet that no
       longer respects node affinity." And for `RemovePodsViolatingNodeTaints`: "If the node's taint
       is subsequently updated/removed, taint is no longer satisfied by its pods' tolerations and
       will be evicted." The decisive detail is the NAME: the platform has a first-class vocabulary
       term — `requiredDuringSchedulingRequiredDuringExecution` — for precisely the construct the
       2026-08-06 pass reported as unlocated. The construct is not missing from the literature; it
       is named, specified, and implemented, and the implementation is a separately-running periodic
       control loop rather than something the scheduler does inline.
    2. Souza, V.E.S., Lapouchnian, A., Robinson, W.N. & Mylopoulos, J. (2011). "Awareness
       Requirements for Adaptive Systems." Proceedings of the 6th International Symposium on
       Software Engineering for Adaptive and Self-Managing Systems (SEAMS 2011), pp. 60-69. DOI
       10.1145/1988008.1988018 — FULL-TEXT (author-hosted PDF retrieved and read this cycle).
       **THE FEEDBACK-CHANNEL HALF.** AwReqs are defined as "requirements that refer to other
       requirements or domain assumptions and their success or failure at runtime," are "represented
       in a formal language" and "can be directly monitored by a requirements monitoring framework"
       (EEAT/ReqMon), and the paper gives "a process for designing full MAPE loops from a set of
       AwReqs." The paper's own worked types include the simplest AwReq form — "the requirement to
       which it refers should never fail" — and aggregate AwReqs specifying a success RATE over
       attempts. This is a formalised, monitorable channel in which "the precondition I depend on is
       not holding here" is a first-class, machine-readable statement that drives adaptation, which
       is the second limb of the item's flagged gap.
    3. Peer-reviewed self-adaptive-systems context located but NOT read in full this cycle (listed
       for the follow-up seam, not relied on): "Runtime Verification of Self-Adaptive Systems with
       Changing Requirements" (arXiv:2303.16530) and "A MAPE-K-Based Method for Architectural
       Conformance Checking in Self-Adaptive Systems" (arXiv:2401.16382). SNIPPET-ONLY. Both are
       preprints; neither is load-bearing here.

  Strength of support: Strong — and stronger than the prior cycle, because the support now transfers
    to the item's own case rather than stopping at the admission-control boundary condition.

  Summary: The PARTIAL NOVELTY-FLAG raised on 2026-08-06 does not survive this cycle and should be
    withdrawn. Both limbs of the construct the flag described as unlocated turn out to exist, to be
    named, and to be in production. The Kubernetes descheduler is a periodic control loop whose
    entire purpose is re-verifying that an already-admitted workload's environment still satisfies
    the workload's declared structural preconditions, and evicting it when it does not — and the
    platform's own vocabulary carries a term for the exact semantic
    (`requiredDuringSchedulingRequiredDuringExecution`), which is the strongest possible evidence
    that this is a recognised design point rather than an unexplored one. On the feedback-channel
    limb, Souza et al.'s Awareness Requirements supply the peer-reviewed construct: requirements
    that predicate over the success or failure of OTHER requirements and domain assumptions at
    runtime, formalised, monitored, and wired into a MAPE loop. Between them these cover "the
    schedule re-checks feasibility" and "the task can say it is not runnable and be heard." The
    2026-08-06 file's own stated follow-up seams were where the answer was, which is the honest
    reading: this was a gap in one search, not a gap in the literature. What survives from the prior
    cycle unchanged is the substantive finding that cron-class schedulers have none of this by
    default, and that C2A2's scheduler is in the cron class.

  Caveats: (a) The descheduler is vendor/project documentation, not peer-reviewed research; its
    standing is as DOCUMENTED PRACTICE and an existence proof, not as measured effect. No source
    located reports how well this actually works. (b) The transfer is not perfect and the limit
    should be stated: Kubernetes preconditions are labels, taints and topology — declarative,
    machine-checkable properties of a node. C2A2's case is a SEMANTIC/structural impossibility
    ("regen is impossible in this location"), which is only re-checkable if it is first made
    declarative. That is a real gap, but it is an ENCODING gap in C2A2, not a gap in the literature,
    and it is the same conclusion the prior cycle reached about utilisation bounds. (c) AwReqs
    presuppose a requirements model to predicate over; C2A2 has prose contracts, so adopting the
    construct requires writing the preconditions down first. (d) The SEAMS paper was read from an
    author-hosted PDF, not the ACM DL copy; page range 60-69 is from the search index and the DOI is
    confirmed, but I did not verify pagination against the ACM record. (e) WebSearch budget
    exhaustion (declared above) means the Slurm/PBS and Airflow-sensor seams remain unopened; given
    two independent direct hits, opening them would likely add confirmation rather than change the
    reading.

  Disposition-changer met: **YES — and it resolves AGAINST the novelty flag.** The construct is
    prior art. The citation that meets it is the kubernetes-sigs/descheduler documentation naming
    `requiredDuringSchedulingRequiredDuringExecution` and implementing it as
    `RemovePodsViolatingNodeAffinity` / `RemovePodsViolatingNodeTaints`, together with Souza et al.
    (2011) SEAMS pp. 60-69 for the runtime "this requirement is failing" channel. **The PARTIAL
    NOVELTY-FLAG of 2026-08-06 should be RETRACTED.**

  Recommendation: SUPPORTED — with the correction that what is supported is the EXISTENCE of the
    construct in the literature and in practice, which withdraws the novelty claim while leaving the
    prior cycle's substantive conclusion (cron-class schedulers do not have it; C2A2's does not have
    it) intact and now better grounded. The remedy shape is named by the sources and is cheap: make
    the precondition declarative, then re-check it on a period.

  PROVENANCE: Origin: 14b · Chain: [14b → 15a, 15b → 15c → 15d → 15a] · Item type: PRESUMPTION
    (unstated — surfaced by inference) · Transform: 15a re-searched on 15d re-trigger, opening the
    two seams the prior pass listed as unsearched · Current status: SUPPORTED (Strong);
    NOVELTY-FLAG RETRACTED
