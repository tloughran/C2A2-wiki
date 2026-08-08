SEARCH-AGAINST-PRESUMPTION-714:
  Date searched: 2026-08-07
  Original item: PRESUMPTION-714
  Original statement: That a hang with a migrating blocker is one fault; "the same hang" on two
    different tool call sites two days apart presumes a single underlying fault, against the
    rival reading that there is no fault at any call site, only a general absence of timeouts.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-714
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Took the run's own second clause seriously as a rival hypothesis to its first — the
        run recorded both "the same hang" and the absence of timeouts, and 14b asked which is the
        fault.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Timeout design in distributed and microservice architectures. Located this session:
       GeeksforGeeks system-design article on timeout strategies in microservices (practitioner,
       non-peer-reviewed); US Patent 10798146, "System and method for universal timeout in a
       distributed computing environment" (patent number and title confirmed this session;
       assignee and date [UNVERIFIED]). The patent's own background statement is the directly
       useful part: in order to prevent indefinitely hanging requests a timeout is used, but
       conventional per-hop timeout implementations perform poorly because a request may cross
       the network an unknown number of times and the calling code may not know how many
       traversals it will incur — so a timeout passed down each path multiplies rather than
       bounds. The framing establishes that the *absence of a bounding timeout at the
       supervisory level* is itself a recognised, named design defect, independent of anything
       wrong at any particular call site. That is 14b's rival hypothesis stated in the design
       literature's own terms.
    2. Watchdog timers, heartbeats and liveness detection. Located this session: US Patent
       8453013, "System-hang recovery mechanisms for distributed systems"; US Patent 11579957,
       "Distributed watchdog timer and active token exchange"; a hierarchical watchdog paper
       (ResearchGate record, "A hierarchical watchdog mechanism for systemic fault awareness on
       distributed systems"; authors, year and venue [UNVERIFIED]); NXP community material on
       watchdog timers in an RTOS; singhajit.com on heartbeats in distributed systems
       (practitioner). Two findings bear directly. First, the standard architecture places the
       watchdog *above* the work — a supervisory timer that the worker must reset — rather than
       at each individual call, which is exactly the design that makes the identity of the
       blocking call irrelevant to detection and recovery. Second, the patents state the
       propagation property: an application that hangs and fails to respond can cause other
       components to wait indefinitely, so a hang in one place triggers a chain reaction. This
       matters because it means the call site where the stall is *observed* need not be the site
       where anything is wrong.
    3. Flaky-test and root-cause-attribution literature (shared with PRESUMPTION-707). Located
       this session: Datadog knowledge-center article on flaky tests; Wikipedia "Flaky test";
       "Test Flakiness' Causes, Detection, Impact and Responses: A Multivocal Review"
       (ResearchGate record; authors, year and venue [UNVERIFIED]); US Patent 9311220, "System to
       uncover root cause of non-deterministic (flaky) tests." The transferable findings: an
       intermittent failure can fail for different reasons across executions, making it difficult
       to identify which failures relate to a fault in the system under test; it is typically not
       clear to decision makers whether the cause lies in the system under test, in the test
       itself, or in the environment; and — the sharpest point — practitioners frequently assign
       a cause without investigation, and the inability to identify a clear reason for
       intermittent behaviour does not imply that there is not one. "The same hang" on two
       different call sites is precisely the situation in which the three-way ambiguity applies,
       and the phrase resolves it by assertion.
    4. Fault-localisation framing, taken from the same body of work: hidden non-determinism
       leaves root causes unaddressed and persisting across pipelines, and misattribution causes
       real defects elsewhere in the system to be overlooked. Applied here: if the true defect is
       the absence of a bound at the loop level, then every call-site-specific fix will appear to
       work — the hang will not recur at that site — while the fault remains, and will surface at
       the next site. The observation that the blocker *migrated* across two days is the
       predicted signature of this pattern, not of a single site-local fault.

  Strength of challenge: Moderate

  Summary: The presumption asserts a single fault from a repeated symptom, and both the
    hang-detection literature and the fault-attribution literature caution against exactly that
    inference. A stall is observed at the outstanding call, but the outstanding call is the site
    where the symptom surfaces, not necessarily the site of the defect — the patent literature
    on system-hang recovery is explicit that a hang propagates and that waiting components are
    victims rather than causes. Meanwhile the rival hypothesis 14b extracted from the run's own
    second clause is not exotic: the absence of a bounding timeout at the supervisory level is a
    named, recognised design defect in its own right, and the standard remedy — a watchdog above
    the work rather than a timeout at each call — is specifically the architecture that makes the
    identity of the blocking call irrelevant. The migration of the blocker across two call sites
    two days apart is more consistent with a missing global invariant than with a site-local
    fault, because a site-local fault does not move. The flaky-test literature supplies the
    procedural warning: "the same X again" is the characteristic form of a cause assigned without
    investigation, and its cost is that the real defect persists while appearing to have been
    addressed. Strength is recorded as Moderate rather than Strong because the sources that speak
    most directly are patents and practitioner guides rather than empirical studies; the
    underlying engineering position (unbounded waits are a defect regardless of what is being
    waited on) is close to universally held but was not evidenced here from a primary empirical
    source.

  STEELMAN:
    Item: PRESUMPTION-714
    Strongest counterargument: The two hypotheses are not rivals but layers, and treating them as
      rivals is the actual error. A missing timeout is a *latent* defect: it converts a transient
      stall into an unbounded one, but something still has to cause the stall. On that reading
      the run's two clauses are consistent and complementary — there is a fault (whatever is
      stalling) and there is an aggravating condition (nothing bounds the wait) — and "the same
      hang" may be a perfectly accurate report that the same underlying stall condition
      manifested at whichever call happened to be outstanding. Indeed, a fault that migrates
      across call sites is *evidence for* a single shared underlying cause rather than against
      one: two unrelated site-local faults would not present identically. There is also a
      practical argument for prioritising the fault over the bound. Adding a timeout converts a
      hang into a failure, which is an improvement in observability but not in outcome; if the
      underlying stall is frequent, a timeout produces a system that fails fast and often rather
      than one that works. And timeouts have their own well-known failure mode — the patent
      literature cited above exists because naive timeout placement produces either false
      positives that kill healthy work or multiplied bounds that fail to bound. "Just add
      timeouts" is not free, and a system that adds them without understanding the stall may
      simply move the symptom again.
    What would need to be true for C2A2 to be safe: (a) the two hypotheses are held
      simultaneously rather than resolved by assertion — the record should say "stall of unknown
      cause, unbounded because no timeout exists," which is what is actually known; (b) a
      supervisory bound exists regardless of the fault's identity, because an unbounded wait is a
      defect on its own terms and its remedy does not depend on diagnosing the stall; (c) the
      bound is placed at the loop or supervisory level, not per call site, since per-site
      placement reproduces the migration problem — a new call site is a new unbounded wait; (d)
      the timeout value is chosen with the false-positive cost in view, and its firing is logged
      with the identity of the outstanding call, which is how the stall's cause becomes
      diagnosable at all; (e) the claim "the same hang" is either supported by a comparison of
      the two incidents' signatures or withdrawn. Condition (b) is decisive and is available
      independently of any diagnosis: it is the one action that is correct under both hypotheses.
    How to test: Partly runnable, partly a matter of instrumentation. First, compare the two
      recorded incidents directly — same outstanding call? same duration profile? same preceding
      operations? same recovery? "The same hang" is a testable claim about signature identity and
      has not been tested. Second, decide the rival hypotheses empirically by adding a
      supervisory bound and observing what happens: if hangs cease entirely, the absence of a
      bound was sufficient to explain the observable and no site-local fault needs positing; if
      the bound now fires regularly at varying call sites, there is a real underlying stall and
      the bound has converted it into a diagnosable signal — which is a win either way, and is
      why (b) above is unconditionally correct. Third, count: how many distinct call sites have
      exhibited this? Two is 14b's figure; if a third appears at a third site, the site-local
      reading is effectively refuted. Fourth: grep the tool-call layer for whether *any* call has
      a bound. If none does, the "general absence of timeouts" clause is established as fact
      rather than hypothesis, and the burden shifts entirely to whoever claims a site-local
      fault.

  Specific risks: If the hang is not one fault, then (i) each site-local fix will appear
    successful and the fault will resurface at a new site, producing an unbounded sequence of
    apparent fixes — the pattern already visible in two incidents two days apart; (ii) effort is
    spent on diagnosis when the unconditionally correct action (bound the wait) is cheap and
    available now, so the cost is not just misdirection but delay of a known-good remedy; (iii)
    an unbounded wait is not merely slow — it consumes a run indefinitely, which in a system with
    a single human consumer and a saturated register (PRESUMPTION-710, -712) means a hung run is
    a lost run and the loss compounds with the backlog; (iv) the diagnosis "the same hang" is
    load-bearing for whatever remediation follows, and if it is wrong the remediation is aimed at
    a fault that does not exist, while the real one is documented in the same sentence and not
    acted on; (v) the absence of any bound means the system currently has no upper limit on the
    cost of a single stall, which is a tail-risk exposure of unknown magnitude rather than a
    known nuisance.

  Mitigations available: (1) Add a supervisory timeout or watchdog above the tool-call loop —
    the action that is correct under both hypotheses and does not require resolving them. (2)
    Place it at the loop level, not per call site, so that new call sites inherit the bound
    automatically and the migration problem cannot recur. (3) Log the outstanding call's identity
    when the bound fires, converting every future stall from an unobservable hang into a labelled
    data point, which is the only route to a real diagnosis. (4) Compare the two existing
    incidents' signatures before retaining the claim that they are the same hang. (5) Record both
    hypotheses in the register rather than one, since the run itself stated both and the
    single-fault reading was a compression, not a finding. (6) Choose the bound with the
    false-positive cost explicit, and treat a firing bound as a signal to investigate rather than
    as a resolution — the patent literature's warning that naive timeout placement kills healthy
    work is worth heeding.

  Search scope: Adequate but not comprehensive, and the source quality is the main limitation.
    The timeout-design, watchdog-placement and hang-propagation material located this session
    consists largely of patents and practitioner guides rather than empirical studies, and while
    the engineering positions they state are close to universally held, none constitutes a
    measured finding. The fault-attribution material from the flaky-test literature is stronger
    on the procedural point (causes assigned without investigation; three-way ambiguity between
    system, test and environment) but is only analogous to the tool-call case rather than
    directly about it. Not searched, and directly relevant: the empirical fault-localisation
    literature on the relationship between failure site and fault site (which would put a number
    on how often the observable location is the defect location), the LLM-agent literature on
    tool-call loop reliability and stall handling specifically, and the SRE literature on
    deadline propagation, which is the modern and better-developed form of the timeout-placement
    argument. Broader search recommended on deadline propagation in particular — it would likely
    convert this challenge from Moderate to Strong.

  Recommendation: CHALLENGED
