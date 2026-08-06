SEARCH-AGAINST-PRESUMPTION-690:
  Date searched: 2026-08-06
  Original item: PRESUMPTION-690
  Original statement: That a scheduled task's environment is capable of the task; metabolism
    regen is established as structurally impossible where it is scheduled and remains
    scheduled there, with no channel by which the schedule could learn otherwise.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-690
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: 14b inferred from a task arguing for its own relocation on structural grounds,
        second day.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Cron/scheduled-job monitoring practice — the silent-failure literature (confirmed this
       session across OnlineOrNot, "Cron job monitoring: How to know when your scheduled tasks
       fail"; Cronping, "Why Nobody Knows When Your Cron Job Stops Running"; SimpleObservability,
       "Cron Monitoring: How to Stop Silent Failures"; QuietPulse, "Cron Job Monitoring Best
       Practices"). These are practitioner sources rather than peer-reviewed work, but they are
       unanimous and they state C2A2's exact failure. "Cron has no concept of success, only
       execution." "A job starting does not mean it succeeded." And decisively: "Cron job
       failures are passive. They're the absence of something happening. Your APM won't alert
       you that a script didn't run." The standard remedy inverts the logic — heartbeat/ping
       monitoring, where the job reports success to an external service and the *external*
       service alerts on silence. The field's settled position is that a scheduler which
       assumes environmental capability and receives no contradicting signal will never learn
       otherwise; the learning channel must be built deliberately and must live outside the
       scheduler.
    2. Open-loop versus closed-loop control (confirmed this session via control-engineering
       sources including ADVANCED Motion Controls, "What is Closed-Loop Control," and
       open-loop testing guidance). The formal statement of the presumption's defect: an
       open-loop system "follows a command schedule whether or not the output matches the
       target," and without a feedback signal "the system cannot automatically correct for
       disturbances or internal deviations" and "may drift from its setpoint." A schedule that
       fires metabolism regen into an environment that cannot perform it is an open-loop
       controller with an unobserved plant. The control literature's position is not that this
       is risky but that it is *definitionally incapable* of correction — there is no amount of
       care in specifying the schedule that substitutes for the missing measurement.
    3. Real-time admission control and schedulability analysis (Springer, Real-Time Systems,
       "Utilization-Based Admission Control for Scalable Real-Time Communication," title and
       journal confirmed this session; QPA schedulability analysis, York, confirmed this
       session). The constructive alternative: in domains where infeasibility matters,
       feasibility is tested before dispatch, and the standard architecture is a cheap
       sufficient test that rejects obviously infeasible requests quickly, refined by an exact
       test. The design principle transfers directly — the scheduler's contract should be
       "admit only if the target environment can execute," not "dispatch and observe
       completion." Note this is precisely the "could it have" side of the suggested search
       framing, and the field long ago concluded that "did it produce" is the wrong question.
    4. Dev/prod parity — factor X of the Twelve-Factor App methodology (12factor.net/dev-prod-
       parity; confirmed this session, along with secondary expositions on DEV Community and
       KodeKloud). The methodology's core claim is that environments diverge silently over time
       and that the divergence surfaces as work that "passes testing and fails production."
       The prescribed control is to keep the gap between environments small and to use the same
       tooling everywhere, precisely because a specification written against one environment
       carries an implicit and unverified capability assumption about the other. The
       configuration-drift literature (Flexagon on Oracle configuration drift; "V2: Fast
       Detection of Configuration Drift in Python," arXiv:1909.06251 — both confirmed as
       existing this session) makes the same point empirically: drift is progressive, and its
       symptom is exactly automation "producing inconsistent results" requiring manual
       investigation.
    5. "Skill Drift Is Contract Violation: Proactive Maintenance for LLM Agent Skill Libraries,"
       arXiv:2605.10990 — [UNVERIFIED — title and URL appeared in search results this session;
       the paper was not retrieved and its content is not confirmed. Attempted fetch was
       blocked: the URL was outside the fetch provenance set.] Flagged here only because the
       title suggests direct relevance to agent-capability drift; it should not be relied on
       until read.

  Strength of challenge: Strong

  Summary: The presumption is challenged by every literature that has confronted it, and the
    challenge is unusually clean because the failure mode is structural rather than
    probabilistic. Control theory says an open-loop scheduler cannot correct what it cannot
    measure; scheduled-job operations practice says the specific failure — a task that cannot
    succeed where it is scheduled — is passive, generates no signal, and is invisible to
    ordinary monitoring; real-time systems practice says feasibility should be tested at
    admission, not inferred from completion; and the dev/prod-parity and configuration-drift
    literature says environment capability silently diverges from specification as a matter of
    course. 14b's observation that there is "no channel by which the schedule could learn
    otherwise" is not an incidental gap; it is the necessary and sufficient condition for the
    fault to persist indefinitely. The task arguing for its own relocation is the only signal
    the system is currently generating, and it is generated by the wrong component — the task,
    not the scheduler.

  STEELMAN:
    Strongest counterargument: Feasibility checking is not free and is often not decidable. The
      real-time literature is explicit that exact schedulability tests "have high time
      complexities and may not be adequate for online admission control," and that cheap
      sufficient tests reject many task sets that would in fact have succeeded. For an agent
      environment, "can this environment perform metabolism regen" may not be answerable
      without attempting it, in which case scheduling-and-observing is not a defect but the
      only available oracle. Furthermore, the environment is not static: a capability absent
      today may be present next week, and a scheduler that refuses admission on a
      previously-failed feasibility check would then be *stuck* — permanently excluding a task
      that has become possible. Keeping the task scheduled where it currently cannot run may be
      a deliberate cheap bet that the environment will acquire the capability, with the
      recurring failure serving as a low-cost probe. On that reading the missing piece is not a
      feasibility gate but simply a report.
    What would need to be true for C2A2 to be safe: (a) the recurring failure actually produces
      an observable, i.e. someone or something reads the outcome — the steelman collapses
      entirely if the probe's result is never consumed; (b) the cost of repeated failed
      execution is genuinely low and bounded, with no side effects on state; (c) the capability
      is plausibly acquirable, so the bet has positive expected value, rather than being
      "structurally impossible" as 14b reports — this is the condition the item's own wording
      says is violated; (d) the task's own argument for relocation reaches a component with
      authority to relocate it, on a bounded timeline. The fact that the task made the argument
      twice (second day) and remains scheduled is direct evidence that (d) fails.
    How to test: Two checks, both runnable against this vault. First, capability audit: for
      every scheduled task, record the environment it is scheduled in and whether that
      environment possesses the capability the task requires; report the count of
      capability-mismatched schedules. Metabolism regen is one known instance — the question
      the presumption raises is how many others there are, and only an enumeration answers it.
      Second, learning-channel audit: for each scheduled task, trace whether any artefact
      records its outcome, and whether any artefact records a *change* to the schedule
      following a failure. If outcomes are recorded but no schedule has ever changed in
      response, the loop is open at the actuator; if outcomes are not recorded at all, it is
      open at the sensor. A third, cheap probe: count consecutive failures of metabolism regen
      and check whether the count is anywhere represented — if nothing counts them, the
      "cheap probe" steelman is unavailable, since a probe nobody reads is not a probe.

  Specific risks: If a scheduled task's environment is not guaranteed capable, C2A2 accrues a
    silent class of scheduled work that consumes slots, produces nothing, and reports nothing.
    The specific harms: (i) invisible non-execution — downstream consumers assume the task ran
    because it is scheduled, so absent output is misread as "nothing to report" rather than
    "could not run"; (ii) unbounded persistence — with no feedback channel, the fault has no
    natural expiry and could survive arbitrarily long, exactly the 118-day-class latency seen
    elsewhere in this register; (iii) misattribution of downstream deficits — whatever
    metabolism regen was supposed to maintain is now degrading for reasons that will be
    attributed to some other component; (iv) enumeration failure — because there is no channel,
    the system cannot even report how many other tasks are in this state, so the blast radius is
    unknown. Risk (iv) is the one that should drive remediation priority: the presumption's
    falsity is currently unmeasurable, which is worse than measurably bad.

  Mitigations available: (1) Heartbeat inversion: have the scheduler alert on the *absence* of a
    success signal rather than on the presence of an error, the settled cron-monitoring remedy;
    this is the smallest change that closes the loop. (2) Admission-time capability check: a
    cheap sufficient test of "does this environment expose what this task needs" before
    dispatch, with exact checking reserved for expensive tasks. (3) Output verification rather
    than execution verification — check that the artefact the task should have produced exists
    and is non-trivial, the "backup file exists and is larger than zero bytes" pattern. (4)
    Environment parity: make the environment a scheduled task runs in explicit and comparable
    to the environment it was authored against, so drift is detectable. (5) A relocation
    channel: a task's structural argument for its own relocation should be a first-class,
    routed object with an owner and an SLA, not prose in a daily output — the task has already
    diagnosed itself twice and the diagnosis has nowhere to go. (6) Consecutive-failure counter
    with escalation, so that indefinite persistence becomes impossible by construction.

  Search scope: Comprehensive for the operations and control framings — scheduled-job silent
    failure, open-loop versus closed-loop control, pre-execution feasibility and admission
    control, dev/prod parity and configuration drift. Preliminary on the agent-specific
    framing: capability-aware task allocation in multi-agent systems, and LLM-agent skill/tool
    drift, where one directly-titled paper was found but could not be retrieved (see source 5).
    Broader search recommended there — the general lesson transfers cleanly, but a
    C2A2-specific mechanism for capability advertisement between agents and schedulers was not
    located this session.

  Recommendation: CHALLENGED
