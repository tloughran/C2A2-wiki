SEARCH-AGAINST-ASSUMPTION-1203:
  Date searched: 2026-08-25
  Original item: ASSUMPTION-1203
  Queue ref: LIT-QUEUE-2026-08-24-003
  Original statement: A human review gate is the sole bottleneck when all automated stages report completion.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1203
    Item type: ASSUMPTION (stated, already marked CHALLENGED on internal evidence)
    Transform at each step:
      14a: Extracted, checked against the same run's phase table, marked CHALLENGED without literature;
           queued for external test
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: Moderate. Queries covered process-vs-outcome metrics, the "green dashboard" /
    watermelon-SLA problem, and measurement bias in system-health indicators; supplemented by
    provenance-set retrieval of the Google SRE monitoring chapter, the SRE cascading-failures chapter,
    Leveson's accident-model preprint, and an empirical failure-taxonomy study of automated issue solving.
    Venues: Google/O'Reilly SRE book (2016), MIT preprint, arXiv software-engineering preprint (2025),
    plus ITSM practitioner literature on the watermelon effect. Date range 2004–2026.
    GAPS: web-search budget was exhausted after six queries. The watermelon-effect material retrieved is
    practitioner/vendor writing (Compucom, HappySignals, Alloy, ALVAO, Rezolve, Workativ), not peer-reviewed,
    and is cited only as evidence that the pattern is named and widely recognised in industry, not as
    empirical support. A peer-reviewed source specifically on measurement-induced fault localisation bias
    was not retrieved; Inozemtseva & Holmes (2014, "Coverage is not strongly correlated with test suite
    effectiveness," ICSE) is the obvious next target and the query for it was refused for budget reasons.

  Challenging evidence found: Yes

  Sources:
    1. Ewaschuk, R. "Monitoring Distributed Systems," Ch. 6 in Beyer, B., Jones, C., Petoff, J., Murphy, N. R.
       (eds.), Site Reliability Engineering. O'Reilly/Google, 2016.
       https://sre.google/sre-book/monitoring-distributed-systems/ — The decisive source. It defines errors
       as including those that occur "implicitly (for example, an HTTP 200 success response, but coupled
       with the wrong content)" and states flatly that "only end-to-end system tests can detect that you're
       serving the wrong content." A stage reporting completion is an HTTP-200-class signal: it reports that
       the stage terminated, not that it produced the right result. The chapter's symptoms-versus-causes
       framing makes the general point: "'What' versus 'why' is one of the most important distinctions in
       writing good monitoring," and white-box internal signals (which is what stage-completion reports are)
       "sometimes symptom-oriented, and sometimes cause-oriented, depending on just how informative your
       white-box is." Completion reports are the least informative white-box signal available. FULL-TEXT.
    2. Ewaschuk, ibid., on black-box monitoring. — "For paging, black-box monitoring has the key benefit of
       forcing discipline to only nag a human when a problem is both already ongoing and contributing to
       real symptoms." The corollary that challenges 1203: a pipeline whose only outcome-measured stage is
       the human gate has black-box visibility at exactly one point, and therefore can only ever localise
       problems at that point. The inference "the gate is the sole bottleneck" is entailed by the
       instrumentation, not by the system. FULL-TEXT.
    3. Leveson, N. "A New Accident Model for Engineering Safer Systems." MIT preprint,
       http://sunnyday.mit.edu/accidents/safetyscience-single.pdf [published venue — details unverified].
       — Gives the general form of the objection: analysis models "impose patterns on the accidents and
       influence both the data collected and the factors identified as causative... they may either act as a
       filter and bias toward considering only certain events and conditions or they may expand activities
       by forcing consideration of factors that are often omitted." A termination-based health scheme is
       such a filter: it can only nominate as causative those stages it measures by outcome. FULL-TEXT
       (PDF, read in relevant part).
    4. [Authors not captured in retrieved HTML — names unverified]. 2025. "An Empirical Study on Failures in
       Automated Issue Solving." arXiv:2509.13941v1. — Empirical counterexample to the substantive claim.
       Across 150 failing issues and 342 catalogued failure instances, "across all settings, fix
       implementation remains the dominant bottleneck," with pipeline tools failing mainly at localisation
       and agentic tools at iteration. These are automated stages that run to completion and report
       completion while producing wrong or inadequate output. The real bottleneck in this dataset is never
       the review gate. FULL-TEXT (HTML, read in relevant part).
    5. Practitioner literature on the "watermelon effect" — e.g. "The Watermelon Effect in IT,"
       HappySignals, https://www.happysignals.com/the-watermelon-effect-in-it ; "What the 'Watermelon Effect'
       Tells Us About Experience Management," Compucom,
       https://www.compucom.com/the-watermelon-effect-in-it-service-management/ ; "Beneath the Rind: Peeling
       Away the Watermelon Effect," Alloy Software, https://www.alloysoftware.com/blog/watermelon-effect/.
       — Non-peer-reviewed, but consistent across independent vendors: SLA dashboards are "green on the
       outside, red on the inside" when the tracked metrics measure volume and process rather than outcome,
       and the effect is attributed to "tracking irrelevant metrics... focusing on volume rather than
       outcome." Cited only as evidence that the phenomenon named in the search direction is a recognised
       industry failure pattern. SNIPPET-ONLY.
    6. "Addressing Cascading Failures," Ch. 22 in Beyer et al. (eds.), SRE, O'Reilly/Google, 2016.
       https://sre.google/sre-book/addressing-cascading-failures/ — Supplies a concrete mechanism by which
       a stage can report health while being the actual fault: "Thread starvation — When a thread can't make
       progress because it's waiting for a lock, health checks may fail if the health check endpoint can't
       be served" — and, inversely, health endpoints served by a separate thread continue to report healthy
       while the work threads are wedged. Self-reported stage health and stage function are separable.
       FULL-TEXT (read in relevant part via targeted extraction).

  Strength of challenge: Strong

  Summary: The external literature confirms 14a's internal CHALLENGED marking and supplies the mechanism.
    A stage that reports completion has reported termination, not correctness; the SRE monitoring literature
    treats this as a first-class error class ("an HTTP 200 success response, but coupled with the wrong
    content") that is undetectable except by end-to-end testing. When every automated stage is measured by
    termination and only the human gate is measured by outcome, the instrumentation guarantees that faults
    localise at the gate regardless of where they actually live — this is the general filtering bias Leveson
    describes, applied to health indicators rather than accident models. The empirical taxonomy of automated
    issue-solving failures independently shows the substantive claim is false in the closest available
    analogue: fix implementation, not review, is the dominant bottleneck, and it fails inside stages that
    terminate normally. The assumption should be treated as an artefact of the measurement scheme, and the
    fact that it can be derived from the phase table without any external evidence (as 14a did) is itself
    diagnostic — a claim that follows from how you measured is not a finding about the system.

  Specific risks: If ASSUMPTION-1203 is false, C2A2 has a systematic mislocalisation: every investigation
    it launches will terminate at the human gate, and no amount of investigation will find upstream faults,
    because upstream stages are incapable of reporting anything but completion. Three consequences.
    (a) Remediation effort is directed at the review stage — recruiting reviewers, throttling intake (see
    ASSUMPTION-1190) — while the actual defect sits in a stage that reported green. (b) The bottleneck
    diagnosis is self-confirming: fixing the gate will reveal a new "sole bottleneck" only if the next
    outcome-measured stage happens to be instrumented, and it is not, so the gate will remain the answer
    indefinitely. (c) Combined with the 49-day unattended condition, the system now has a stated reason to
    believe that nothing is wrong except an absent human — the most comfortable possible conclusion, and
    the one its instrumentation was always going to produce.

  Mitigations available:
    - Add end-to-end / black-box checks at the pipeline's output boundary, which SRE Ch. 6 identifies as the
      only class of check that detects correct-termination-with-wrong-content.
    - Instrument at least one automated stage by outcome rather than by termination, so the gate is no
      longer the unique outcome-measured point and the localisation is no longer forced.
    - Require stages to report *what they did*, not only *that they finished* — the scope-reporting change
      recommended in the ASSUMPTION-1195 file addresses the same underlying defect and the two mitigations
      share an implementation.
    - Apply the symptoms-versus-causes discipline explicitly (Ewaschuk, SRE Ch. 6): treat stage-completion
      reports as cause-oriented debugging aids and never as evidence of system health.
    - Before accepting any "sole bottleneck" conclusion, ask what the measurement scheme could have
      concluded instead. If the answer is "nothing else," the conclusion carries no information.

  STEELMAN:
    Item: ASSUMPTION-1203
    Strongest counterargument: In a pipeline where every automated stage is deterministic, idempotent, and
      covered by its own assertions, "reported completion" is in fact strong evidence of correct completion,
      and the human gate is genuinely the only stage with unbounded and unmodelled latency. Machine stages
      have known service-time distributions; a human reviewer does not. So even granting that stage-level
      completion reports are weak evidence of correctness, the *bottleneck* claim is about latency, not
      correctness — and on latency the human gate really is categorically different, because it is the only
      stage that can stall for 49 days. On this reading the challenge attacks a correctness claim the
      assumption never made: one can concede that upstream stages may be silently wrong and still hold that
      they are not the throughput constraint.
    What would need to be true for C2A2 to be safe: (1) The assumption must be understood and used strictly
      as a latency claim, never as a health claim, and nothing downstream may read "all automated stages
      reported completion" as "the automated pipeline is correct." (2) Automated stages must actually carry
      assertions strong enough that termination implies correctness — verified, not assumed (this is the
      test in the ASSUMPTION-1195 file). (3) At least one outcome-measured signal must exist outside the
      human gate, or the latency claim itself is untestable. (4) The bottleneck conclusion must be
      re-derived after the gate is unblocked; if the pipeline still underperforms with a fully attended
      gate, the assumption is refuted directly.
    How to test: Two clean experiments against C2A2's own history. (a) Retrospective: take completed runs
      where the gate was attended promptly, and check whether output defects were later found in stages
      that had reported completion. Any such defect refutes the "sole" quantifier. (b) Prospective:
      inject a known semantic fault into one automated stage that does not cause it to abort, and see
      whether any indicator other than the human reviewer notices. If nothing does, the localisation bias
      is confirmed and the assumption is an artefact.

  Recommendation: CHALLENGED
