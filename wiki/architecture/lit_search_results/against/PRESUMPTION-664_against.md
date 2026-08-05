SEARCH-AGAINST-PRESUMPTION-664:
  Date searched: 2026-08-05
  Original item: PRESUMPTION-664
  Original statement: That a scheduled run which starts is a scheduled run which reports —
    whereas four of today's scheduled sessions ended at `[Request interrupted by user]` with
    no verdict of any kind, and the watchdog built to detect that class is one of the four.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-664
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from four transcripts read directly on the 2026-08-04 run, all ending at
        `[Request interrupted by user]` with no verdict emitted, one of which was the watchdog
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Cristian, F., 1991. "Understanding Fault-Tolerant Distributed Systems."
       Communications of the ACM 34(2). — The canonical failure-semantics taxonomy separates
       crash, omission, timing and response failures. An *omission failure* is precisely a
       component that receives a request and produces no response while remaining otherwise
       intact. The presumption collapses omission into crash: it assumes that a run which does
       not report has not run. Cristian's point is that these are distinct failure classes
       requiring distinct detectors, and that a system which only detects one is not covered
       for the other.
    2. Mahmood, A. & McCluskey, E.J., 1988. "Concurrent Error Detection Using Watchdog
       Processors — A Survey." IEEE Transactions on Computers 37(2):160-174. — Foundational
       treatment of watchdogs as *separate* processors monitoring a main processor. The design
       requirement the survey establishes is independence: the checker must not share the
       failure domain of the checked. C2A2's watchdog is a scheduled session in the same fleet,
       killed by the same mechanism, on the same day — the exact configuration the watchdog
       literature exists to forbid.
    3. Oppenheimer, D., Ganapathi, A. & Patterson, D.A., 2003. "Why Do Internet Services Fail,
       and What Can Be Done About It?" USITS '03, USENIX. — Empirical failure study across
       three large Internet services. Two findings bear directly: operator/configuration error
       is the largest single failure cause, and the authors' explicit recommendation is "more
       thoroughly exposing and detecting component failures," i.e. that undetected component
       failure was a measured, material contributor. Detection was the gap, not occurrence.
    4. Cemri, M., Pan, M.Z., Yang, S., et al., 2025. "Why Do Multi-Agent LLM Systems Fail?"
       arXiv:2503.13657; NeurIPS 2025 Datasets & Benchmarks Track. — MAST, the first
       empirically grounded multi-agent-system failure taxonomy (200+ tasks, 7 frameworks, 150
       hand-annotated traces, κ=0.88). "Unaware of Termination Conditions" accounts for 12.4%
       of observed failures and one of the three top-level categories is *task verification*.
       This is the closest available base rate for C2A2's own class of system, and it says that
       runs terminating without a correct completion signal are a leading, not a marginal, mode.
    5. Huang, P., Guo, C., Zhou, L., Lorch, J.R., Dang, Y., Chintalapati, M. & Yao, R., 2017.
       "Gray Failure: The Achilles' Heel of Cloud-Scale Systems." HotOS '17. — Differential
       observability: the failure detector does not observe the failure the application
       suffers. A run killed mid-flight is observable to whoever killed it and invisible to the
       reporting channel; that gap is the definition.
    6. "When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a
       Production LLM Agent Runtime," arXiv:2606.14589 (2026). [AUTHORS UNVERIFIED — title,
       identifier and abstract content confirmed via search index; the abstract page could not
       be fetched (fetch blocked: URL not in provenance set), so authorship is not confirmed.]
       — Eight-week longitudinal study of a production agent runtime of ~40 scheduled jobs,
       reporting 22 incidents with postmortems in which the meta-pattern "a failure whose error
       signal never reaches a human in actionable form" recurred at least 28 times. Class (C) of
       its taxonomy is "error swallowing and dilution." This is the same architecture as C2A2
       (scheduled agent jobs, tool proxy, knowledge-base memory) at comparable scale, and the
       modal failure is the one this presumption assumes away.
    7. "Detecting Silent Failures in Multi-Agentic AI Trajectories," arXiv:2511.04032 (2025).
       [AUTHORS UNVERIFIED — title and identifier confirmed via search index only.] — Frames
       the problem as one requiring dedicated trajectory-level detection: unlike microservices,
       where errors are explicit and carry codes, agentic failures frequently produce no error
       signal while deviating from intended behaviour.
    8. Practitioner literature on scheduled-job monitoring (dead-man's-switch / heartbeat
       patterns; e.g. onlineornot.com cron-monitoring guide, watchflow.io "Why Cron Jobs Fail
       Silently"). [GREY LITERATURE — consistent across many independent industry sources but
       not peer-reviewed.] — The universally recommended pattern is the inverse of C2A2's:
       alarm on the *absence* of a success ping within a window, because a job that does not
       run emits nothing to log. The existence of an entire commercial product category
       (Dead Man's Snitch, Healthchecks, Cronitor) is itself evidence that "started implies
       reported" is a known and costly error.

  Strength of challenge: Strong

  Summary: The literature is uniform and the presumption is a named anti-pattern in three
    separate traditions. In classical fault tolerance it is the conflation of omission failure
    with crash failure (Cristian); in cloud systems it is differential observability (Huang et
    al.); in operations practice it is the reason dead-man's-switch monitoring exists at all.
    The multi-agent evidence is the most directly applicable: MAST finds that failure to
    recognise termination conditions is a double-digit share of observed multi-agent failures,
    and the 2026 production-runtime study finds that a failure whose signal never reaches a
    human is the single most recurrent meta-pattern in a system architecturally near-identical
    to C2A2. Separately and more seriously, the watchdog literature's one structural
    requirement — that the checker not share the failure domain of the checked — is violated
    here in the strongest possible way: the watchdog was killed by the same event it existed to
    report. Mahmood & McCluskey's framing makes this not a bad day but a design error, because
    a watchdog inside the failure domain has zero coverage for exactly the correlated failures
    that matter most. The item's own evidence is decisive without the literature: four runs
    ended at `[Request interrupted by user]` and none of them said so.

  Specific risks: Every scheduled run's outcome is currently unknown unless the run itself
    chose to say so, which means the reporting channel measures cooperation rather than
    completion. The four silent runs did work that was either not done or done and discarded,
    and nothing downstream can distinguish those cases. Because the watchdog is one of the
    four, the system's mean time to detect this class is unbounded — there is no second
    observer. This compounds with PRESUMPTION-666: a status aggregator reading the same empty
    channel will report success, so the failure is not merely undetected but actively
    contradicted by a green report. It also compounds with PRESUMPTION-661 (running ≠
    progressing) to produce a two-layer blind spot: a run can appear present, appear running,
    and have produced nothing, with all three checks passing. Finally, correlated termination
    means the failure is not independent across runs — the mechanism that killed one killed
    four — so any reliability estimate built on independent per-run failure probabilities is
    wrong by orders of magnitude.

  Mitigations available: (1) Invert the signal: require every scheduled run to emit a terminal
    verdict record (success or failure) and alarm on the *absence* of that record within a
    deadline, rather than on the presence of a failure report. This is the dead-man's-switch
    pattern and it is the only construction that detects omission failures. (2) Move the
    watchdog out of the failure domain — a different scheduler, a different process class, or
    an external service — per Mahmood & McCluskey's independence requirement. A watchdog that
    can be killed by the event it watches for is not a watchdog. (3) Add a trivially cheap
    liveness-of-the-watchdog check: the watchdog itself must emit a heartbeat that something
    else consumes, else "who watches the watchdog" is unanswered. (4) Make the terminal state
    explicit in the data model: RAN-AND-REPORTED, RAN-AND-DIED-SILENT, NEVER-STARTED. The
    current binary cannot represent what was observed. (5) Treat `[Request interrupted by
    user]` as a first-class terminal status that must be reconciled, not as an absence — it is
    a recorded fact in the transcript and could be swept for today with one grep. (6) Because
    terminations were correlated, investigate the common cause before adding detectors; four
    simultaneous interrupts is a single event, and a detector that fires four alarms for one
    cause will itself become noise (see PRESUMPTION-677).

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-664
    Strongest counterargument: `[Request interrupted by user]` is not a failure at all — it is
      the recorded signature of a human deliberately stopping a run, and a human who interrupts
      a run knows it was interrupted. On that reading there is no silent failure, only an
      undocumented manual intervention, and building an alarm for it would page someone about
      their own action. The watchdog being among the four is then unremarkable: if a person
      stopped all activity, the watchdog stopping too is correct behaviour, not a coverage gap.
      Further, the literature cited concerns systems where a missed run has external
      consequences — a backup not taken, an order not filled. A wiki-maintenance run that does
      not report costs one day of an internal process and will be picked up on the next cycle,
      so the cost of the failure may be far below the cost of the detection machinery, and
      MAST's base rates come from benchmark task suites rather than long-running maintenance
      fleets and may not transfer.
    What would need to be true for C2A2 to be safe: (a) The interruptions were genuinely
      human-initiated and the initiator knew what they were stopping — i.e. the string means
      what it says and is not a generic label for any abnormal termination. (b) No run's work
      is lost or half-applied when interrupted (which PRESUMPTION-676 already denies, on
      evidence of an orphaned external side effect). (c) The next cycle actually re-does the
      missed work rather than moving on, i.e. runs are idempotent and self-catching-up.
      (d) Someone would notice within a bounded time if a run stopped reporting permanently —
      which the sibling item PRESUMPTION-661's five-month case falsifies for this system.
    How to test: Cheap and immediate. (i) Grep the whole transcript store for
      `[Request interrupted by user]` with timestamps; if the four are within seconds of each
      other, it is one event with one cause, and the cause is findable. (ii) For each of the
      four, diff the vault state before and after: if any produced partial writes, the
      "interruption is harmless" defence fails outright. (iii) Instrument for one week: have
      every scheduled run write a start record and an end record to a single append-only file;
      count start-without-end. A single occurrence in a week where no human reports having
      interrupted anything settles the question.

  SYSTEMIC-RISK-FLAG:
    Date: 2026-08-05
    Affected items: PRESUMPTION-664, PRESUMPTION-666, PRESUMPTION-668, PRESUMPTION-669
      (continuous with PRESUMPTION-660, PRESUMPTION-661)
    Common vulnerability: All four substitute a *declaration* for a *measurement*. The system
      reads an artifact produced by, or adjacent to, the very process whose state is in
      question — an empty report channel (664), a status assertion (666), a retraction (668),
      a hold's label (669) — and treats that artifact as the state. In three of the four the
      failing component is the monitoring layer itself, which continues to emit reassurance
      while inside the failure domain it is supposed to observe.
    Literature basis: Huang et al. 2017 (differential observability); Mahmood & McCluskey 1988
      (checker independence); Cristian 1991 (omission ≠ crash); Cemri et al. 2025 (task
      verification as a top-level MAS failure category); Parasuraman & Riley 1997 and Skitka et
      al. 1999-2000 (automation complacency and omission errors in monitoring).
    Risk level: Critical
    Recommendation: Adopt a single invariant across the monitoring layer — no health claim may
      be derived from an artifact produced by the subject of the claim. Every green signal must
      trace to an independently observed, monotonically advancing quantity (a commit, a byte
      count, a file mtime, a counter). Audit all existing health instruments against this
      invariant; the ones that fail it are currently producing false assurance, not information.

  Search scope: Adequate. Concepts searched: omission vs crash failure semantics; watchdog
    processor coverage and checker independence; the "who watches the watchdog" problem; silent
    and dead-man's-switch cron/scheduled-task monitoring; silent failure taxonomies in
    production LLM agent runtimes; multi-agent failure taxonomies and termination-condition
    awareness; gray failure and differential observability; empirical Internet-service failure
    causes. Not searched: formal failure-detector completeness/accuracy results (Chandra &
    Toueg class hierarchy), which would likely strengthen the challenge further.
