SEARCH-FOR-PRESUMPTION-664:
  Date searched: 2026-08-05
  Original item: PRESUMPTION-664
  Original statement: That a scheduled run which starts is a scheduled run which
    reports; four of today's scheduled sessions ended at `[Request interrupted by
    user]` with no verdict of any kind, and the watchdog built to detect that
    class is one of the four.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-664
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from four transcripts read directly this run, in which four
        scheduled sessions terminated with no verdict and one of the four was
        the watchdog built to detect that class of failure
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Dijkstra, E.W. & Scholten, C.S., 1980. "Termination detection for
       diffusing computations." Information Processing Letters 11(1):1-4
       (EWD687a). — The foundational positive result: termination of a
       distributed computation *can* be detected reliably and message-optimally,
       via the parental-responsibility signalling tree in which each process
       reports upward and the initiator announces termination only when its
       counter returns to zero. This is the strongest available support for the
       presumption, but it is support for constructibility, not for the default:
       the guarantee is delivered by an explicit detection protocol layered over
       the computation, and does not arise from the computation merely having
       been started.
    2. Armstrong, J., 2003. "Making reliable distributed systems in the presence
       of software errors." PhD thesis, KTH (Erlang/OTP supervision trees). —
       Empirical precedent at scale that start-implies-report can be made an
       architectural property: every process is linked to a supervisor,
       abnormal termination generates an exit signal, and the supervisor
       receives it. Armstrong is explicit that "let it crash" is not "let it
       fail silently" — the crash is always observed by a supervisor. Twenty-plus
       years of telecom deployment is the empirical record behind this.
    3. Durable-execution platform documentation and design literature (Temporal
       Workflow Execution; Azure Durable Functions). — Analogous support: these
       systems obtain a run-to-completion guarantee by synchronously persisting
       an event history before each step and deterministically replaying it after
       a worker crash, so a workflow that starts does eventually report. The
       guarantee is bought with durable state and idempotent activities; it is
       explicitly not a property of ordinary schedulers. UNVERIFIED as
       peer-reviewed literature — this is vendor and practitioner documentation,
       not an academic result.
    4. "A hierarchical watchdog mechanism for systemic fault awareness on
       distributed systems," Future Generation Computer Systems, 2015
       (doi prefix S0167739X14002751). — Directly addresses the
       who-watches-the-watchdog problem the item raises: a mutual watchdog in
       which host and network interface guard each other, each node monitors its
       mesh neighbours, and duplicated supervisor nodes assemble the global
       picture, giving fault awareness with no single point of failure. Author
       list UNVERIFIED.
    5. Lease-and-heartbeat scheduler design literature (distributed job scheduler
       system design corpus, 2024-2026). — The standard mechanism: a worker takes
       a time-bounded lease, and a sweeper marks as failed any task whose
       heartbeat is older than the lease. Note the epistemic shape of this
       support: it does not observe a report, it *presumes* failure after a
       timeout. It rescues the scheduler's bookkeeping, not the presumption.
       Practitioner literature, not peer-reviewed.
    6. Dead-man's-switch / heartbeat-monitoring practice literature (2026 SRE
       and cron-monitoring guidance). — Consistent statement of the operational
       rule in the negative: cron and comparable schedulers do not report on job
       outcome at all, so external confirmation that a job ran is required, and
       the absence of a signal must itself be made the alert. This is support for
       the remedy, and simultaneously a direct statement that the presumption
       does not hold by default.

  Strength of support: Weak

  Summary: The literature supports the *achievability* of the presumption and
    not its default truth. Termination detection is a solved problem with a
    message-optimal classical algorithm, and two production lineages — Erlang/OTP
    supervision and durable-execution workflow engines — demonstrate at scale
    that "a run which starts is a run which reports" can be made an
    architectural invariant. In every case the invariant is purchased: by a
    signalling tree, by a supervisor link on every process, or by a durably
    persisted event history. No source found treats start-implies-report as a
    free property of a scheduler. The dominant scheduler idiom is the opposite —
    a lease timeout that *presumes* failure in the absence of a report, which
    concedes the point that the report cannot be relied upon. On the watchdog
    self-monitoring sub-claim, the hierarchical/mutual watchdog work is
    supportive but its whole premise is that a single watchdog is a single point
    of failure, which is the condition the item observed.

  Caveats: Sources 3, 5 and 6 are practitioner and vendor material rather than
    peer-reviewed research, and vendor documentation on execution guarantees is
    subject to obvious publication bias. Source 4's author list could not be
    verified from search results and should be checked before citation. Domain
    transfer is a live concern: Dijkstra-Scholten assumes reliable message
    delivery between cooperating processes, and Erlang supervision assumes the
    supervisor and child share a runtime with a trusted link mechanism — neither
    holds for an LLM session terminated by an external interrupt whose origin is
    itself unidentified (cf. PRESUMPTION-665). The strongest transferable finding
    is Armstrong's distinction between crashing and failing silently: the fault
    class observed here is the silent one, which the supervision literature
    treats as the case that must be engineered away rather than assumed absent.

  Recommendation: PARTIALLY-SUPPORTED

  Search scope: Adequate. Concepts searched: distributed termination detection
    and the Dijkstra-Scholten algorithm; completion detection versus failure
    detection in job schedulers; exactly-once execution and durable execution
    guarantees; silent task failure in scheduler fleets and cron; watchdog
    self-monitoring, mutual and hierarchical watchdogs; dead-man's-switch and
    absence-based alerting; Erlang/OTP supervision trees. Not searched: formal
    verification of scheduler completion properties; aviation/process-industry
    literature on mandatory positive reporting.
