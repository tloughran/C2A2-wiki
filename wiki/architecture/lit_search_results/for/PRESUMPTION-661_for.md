SEARCH-FOR-PRESUMPTION-661:
  Date searched: 2026-08-04
  Original item: PRESUMPTION-661
  Original statement: That a session reported as "running" is thereby
    progressing — four scheduled sessions unchanged in turn count across three
    polls, one silent for five months.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-661
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-08-03 observation of four scheduled sessions
        reported as running while unchanged in turn count across three polls,
        one silent for five months
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. Huang, P. et al., 2017. "Gray Failure: The Achilles' Heel of Cloud-Scale
       Systems." HotOS. — Defines gray failure as partial failure with
       differential observability: some observers see the system as healthy
       while others see it as failed. The paper's motivating case is exactly
       the pattern reported — heartbeats continued to arrive via a host agent
       while the monitored VMs were severely degraded, so no recovery was
       triggered until a user complained.
    2. Dong, R. et al., 2025. "Understanding and Detecting Fail-Slow Hardware
       Failures." USENIX ATC '25; and Lu, R. et al., 2025. "Understanding and
       Enhancing Slow-Fault Tolerance in Modern Distributed Systems." NSDI '25.
       — Systematic evidence that components which have not crashed but have
       stopped making progress evade status-based detection, including cases
       where an internal checker is itself blocked by the slow fault.
    3. Liveness-probe practice literature (2026 SRE guidance on detecting
       deadlocks in application logic). — States the operational rule directly:
       to detect logic-level freezes a liveness check must verify that critical
       threads are making progress, not merely that the process is alive.
    4. Fischer, M., Lynch, N. & Paterson, M., 1985. "Impossibility of
       Distributed Consensus with One Faulty Process"; Chandra, T.D. & Toueg,
       S., 1996. "Unreliable failure detectors for reliable distributed
       systems." JACM. — The theoretical boundary, and the only route to
       support: a perfect failure detector is implementable in a fully
       synchronous system where maximum processing and communication delays are
       known and only crash failures occur. In an asynchronous system a crashed
       process is formally indistinguishable from a slow one.

  Strength of support: None

  Summary: No support was found for reading a "running" status as evidence of
    progress. The one theoretically supportive result — that perfect failure
    detection is achievable under full synchrony with known delay bounds and a
    crash-stop fault model — requires assumptions that an LLM session scheduler
    plainly does not satisfy, since turn latency is unbounded and the relevant
    fault is not a crash. Under the applicable model, absence of a failure
    signal carries no information about progress, and the gray-failure and
    fail-slow literatures document at length how status-based monitors miss
    exactly this condition. The specific evidence pattern reported — turn count
    unchanged across successive polls — is what the liveness-probe literature
    identifies as the correct signal and status as the incorrect one. Five
    months of silence under a "running" status is, on this literature, the
    predicted outcome of monitoring liveness where progress was the question,
    not an unusual failure.

  Caveats: The distributed-systems evidence concerns machine-to-machine failure
    detection, where progress is cheap to define; defining progress for an agent
    session is less obvious, and turn count may itself be an imperfect progress
    proxy (a session could legitimately be mid-turn for a long period). The
    theoretical support would become real if the scheduler could guarantee a
    bounded maximum turn duration and treat exceedance as failure — that
    conversion of an asynchronous problem into a synchronous one is well
    precedented and is the standard remedy the literature points to.

  Recommendation: NO-SUPPORT-FOUND

  Search scope: Adequate. Concepts searched: liveness vs progress detection;
    hung-process and stall detection; gray failure and differential
    observability; fail-slow and limplock; heartbeat sufficiency; liveness
    probes and deadlock detection; failure detectors, FLP impossibility and
    perfect detection under synchrony.
