SEARCH-FOR-PRESUMPTION-714:
  Date searched: 2026-08-07
  Original item: PRESUMPTION-714
  Original statement: That a hang with a migrating blocker is one fault; "the
    same hang" on two different tool call sites two days apart presumes a single
    underlying fault, against the rival reading that there is no fault at any
    call site, only a general absence of timeouts. Risk: High.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-714
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Took the run's own second clause seriously as a rival hypothesis to
        its first.
      15a: Searched for supporting literature
    Current status: SUPPORTED (in a form that dissolves the disjunction)

  Supporting evidence found: Yes

  Sources:
    1. Dai, T. et al., 2018. "Understanding Real-World Timeout Problems in Cloud
       Server Systems." IEEE International Conference on Cloud Engineering
       (IC2E) 2018. [PDF located at dance.csc.ncsu.edu/papers/IC2E18.pdf this
       session; not opened. First author and venue from the located filename and
       result title; full author list NOT verified.] — The most on-point source
       and it supports the presumption in a specific and slightly surprising
       way. The paper's taxonomy, as reported in the located summary, divides
       missing-timeout bugs into two groups — missing timeout checking for
       network communications and missing timeout checking for intra-node
       synchronisations — and states that missing timeout checking can cause
       system hang or crash. The important structural point is that this
       literature treats a *missing timeout* as a bug, catalogued and
       attributable, rather than as a mere absence of a feature. That means the
       item's rival hypothesis ("no fault at any call site, only a general
       absence of timeouts") is not actually a rival to "there is one fault";
       in the field's own vocabulary, a general absence of timeouts *is* a
       fault, and one of a named class.
    2. Shared-client configuration as a single defect with many manifestation
       sites — practitioner incident write-ups located this session (several
       independent Medium post-mortems on HttpClient timeout defaults causing
       cascade failures; oneuptime.com, "How to Fix 'Timeout' Errors in
       Service-to-Service Calls," January 2026; an AWS SDK JS v3 GitHub issue,
       #7076). [All practitioner; none opened beyond returned summaries. The
       .NET HttpClient default of 100,000 ms mentioned in one summary is
       consistent with established knowledge but was not verified.] — Direct
       support for the presumption's "one fault, migrating blocker" reading. The
       recurring structure in these accounts is a single configuration
       parameter, set once in a shared client, that governs the fate of every
       request in the application; the symptom then appears at whichever call
       site happens to be slow that day, and moves as load moves. One defect,
       many observation points, a blocker that migrates. This is exactly the
       pattern the run described and it is a well-attested one.
    3. The same material, on symptom versus cause. — The consistent framing is
       that the visible symptoms — thread pool starvation, socket exhaustion,
       memory growth from in-flight requests, cascading collapse — are
       downstream of the configuration, and that fixing the site where the
       symptom appeared does not fix the system. One located summary notes that
       without an upstream timeout, a component receiving 100 calls/second could
       accumulate roughly 1 GB of in-flight request memory in a minute when the
       upstream crashes. [Figure from an unopened source; illustrative only, not
       verified.] This supports treating recurrence at a second call site as
       evidence of a shared cause rather than as a second, unrelated bug.
    4. Timeout and watchdog fundamentals — Contentful engineering blog, "The two
       friends of a distributed systems engineer: timeouts and retries";
       Grokipedia entry "Timeout (computing)"; Cisco, "Troubleshooting Watchdog
       Timeouts." [Located this session; not opened.] — Theoretical grounding
       for the remedy and for where it belongs. The stated principle is that a
       timeout interrupts an ongoing process when an expected event fails to
       occur within a predefined interval, thereby preventing indefinite
       resource consumption or hangs, and that one should never wait
       indefinitely on a remote service. The watchdog framing is the relevant one
       for placement: a watchdog sits above the individual call site and fires on
       liveness failure regardless of which call is outstanding, which is the
       structural answer to a blocker that migrates.
    5. Runtime liveness checking — "Assurance of Distributed Algorithms and
       Systems: Runtime Checking of Safety and Liveness" (arXiv 2008.09735);
       "TFix+: Self-configuring Hybrid Timeout Bug Fixing for Cloud Systems"
       (arXiv 2110.04101). [Titles and IDs only; neither opened; no claims taken
       beyond the existence of the work.] — Corroborates that automated
       detection and repair of timeout bugs is a recognised research problem
       with dedicated tooling, which is further evidence that "absence of
       timeouts" is treated as a defect class rather than as a non-issue.

  Strength of support: Moderate

  Summary: The literature supports the run's reading, and it does so by
    collapsing the disjunction 14b constructed rather than by choosing a side.
    The rival hypothesis — that there is no fault at any call site, only a
    general absence of timeouts — is not, in the terms this field uses, a rival
    at all: Dai et al.'s taxonomy of real-world cloud timeout problems treats
    missing timeout checking as a named bug class that causes hangs, so a
    general absence of timeouts *is* the single underlying fault. The
    practitioner incident literature then supplies the mechanism by which one
    such fault produces the migrating-blocker signature the run observed: a
    single shared client configuration governs every outbound call, so the
    symptom surfaces at whichever call site is slow on a given day and moves as
    load moves, while the defect stays put. Both of the run's clauses are
    therefore correct and they are the same claim stated at two levels of
    description. Where the search offers a corrective, it is on remedy rather
    than on diagnosis: the watchdog literature places liveness detection above
    the individual call site precisely because a per-site fix chases a symptom
    that has already moved, which is a consequence of the run's own reasoning
    that the run's framing ("the same hang" at a second site) does not quite
    draw out. This is the rare item where the FOR direction is genuinely
    supportive.

  Caveats: Source 1's author list is unverified and I have cited it as "Dai, T.
    et al." on the strength of a filename and a result title; this should be
    corrected before reuse. Sources 2 and 3 are practitioner incident write-ups
    on unopened pages, and both numeric figures appearing in this file (the
    100,000 ms default and the ~1 GB/minute accumulation) are illustrative and
    unverified — neither should be quoted downstream. The whole located
    literature concerns distributed service architectures with HTTP or RPC
    clients; C2A2's hang is at agent tool call sites, which may or may not share
    a configurable client layer, and if the two tool call sites do not share any
    common timeout configuration then source 2's mechanism does not transfer and
    the "one fault" reading loses its best support. That is the single largest
    open question and it is a local one. There is also a form of the rival
    hypothesis the search does not dispose of: if the two call sites hang for
    genuinely different upstream reasons and merely present alike, then there
    are two faults plus one missing control, and the run's "same hang" framing
    would be conflating three things. Nothing located rules this out, and the
    two-days-apart, different-site pattern is consistent with it. The support
    recorded here is for the *plausibility and precedent* of the one-fault
    reading, not for its confirmation in this instance.

  NOVELTY-FLAG: Not raised. Missing-timeout bugs, watchdog placement and
    shared-configuration defects are all well-covered ground.

  Recommendation: SUPPORTED

  Search scope: Adequate. Concepts searched: attributing stalls to the
    outstanding call; missing timeout checking as a documented bug class in
    cloud systems; timeout design in service and tool call loops; watchdog
    placement and liveness detection; single configuration defects manifesting
    at multiple call sites. Not searched, and recommended: the fault-localisation
    literature on distinguishing one root cause from several correlated ones,
    which would speak to the residual version of the rival hypothesis; and
    agent-framework tool-loop design specifically, since all located material is
    from service architecture rather than from agent harnesses.
