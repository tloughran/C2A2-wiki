SEARCH-AGAINST-PRESUMPTION-668:
  Date searched: 2026-08-05
  Original item: PRESUMPTION-668
  Original statement: That catching an error discharges it — whereas three self-retractions
    occurred today across three independent runs, in each of which the erroneous output was
    corrected and the producing instrument was not, including one method whose false-positive
    sweep has now been observed twice (2026-07-31 and 2026-08-04).

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-668
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from three same-day retractions read together, one of which is the second
        observed occurrence of the same false-positive sweep
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Tucker, A.L. & Edmondson, A.C., 2003. "Why Hospitals Don't Learn from Failures:
       Organizational and Psychological Dynamics That Inhibit System Change." California
       Management Review 45(2). — The central and directly applicable result. Qualitative field
       study of nurses across nine hospitals distinguishing *first-order problem solving*
       (patching the immediate symptom so work can continue) from *second-order problem
       solving* (changing the process that produced it). First-order solving dominates, and the
       paper's dynamic model shows an "illusory equilibrium" in which small failures are
       reliably caught and repaired while organisational effectiveness *erodes*, because each
       successful catch removes the pressure that would have driven the systemic fix. This is
       the exact configuration described in the item: the erroneous output was corrected, the
       producing instrument was not.
    2. Dillon, R.L. & Tinsley, C.H., 2008. "How Near-Misses Influence Decision Making Under
       Risk: A Missed Opportunity for Learning." Management Science 54(8):1425-1440. — Events in
       which failure was averted are evaluated as *successes*, and decision-makers who observe
       them subsequently choose riskier options because *perceived* risk falls while the
       statistical probability of failure is unchanged. This is precisely what a self-retraction
       does: it converts an error into a success story about error-catching, without altering
       the error rate.
    3. Tinsley, C.H., Dillon, R.L. & Cronin, M.A., 2012. "How Near-Miss Events Amplify or
       Attenuate Risky Decision Making." Management Science 58(9). — Extends the 2008 result:
       whether a near-miss teaches or emboldens depends on whether the observer's attention is
       drawn to the *chance* element in the recovery. Absent that framing, repeated catches
       systematically attenuate perceived risk. A run that reports "I caught my own error"
       supplies the emboldening frame, not the cautionary one.
    4. Yin, Z., Yuan, D., Zhou, Y., Pasupathy, S. & Bairavasundaram, L., 2011. "How Do Fixes
       Become Bugs? A Comprehensive Characteristic Study on Incorrect Fixes in Commercial and
       Open Source Operating Systems." ESEC/FSE '11. — Empirically, 14.8%-24.4% of sampled
       fixes for post-release bugs in Linux, OpenSolaris, FreeBSD and a mature commercial OS
       were themselves incorrect and reached end users. The act of correcting is not
       risk-neutral: roughly one fix in five to one in seven introduces a new defect. A
       correction therefore cannot be treated as terminating the error's lifecycle even for the
       specific instance, let alone for the mechanism.
    5. Vaughan, D., 1996. The Challenger Launch Decision: Risky Technology, Culture, and
       Deviance at NASA. University of Chicago Press. — Normalization of deviance: the gradual
       process by which an anomaly that recurs without catastrophic consequence becomes an
       accepted feature of normal operation. [PRIMARY TEXT NOT DIRECTLY RETRIEVED THIS SESSION;
       definition and mechanism confirmed via multiple secondary safety-science sources.] A
       false-positive sweep observed twice and retracted twice is on exactly this trajectory:
       the second occurrence is already less surprising than the first.
    6. Dekker, S., 2011. Drift into Failure: From Hunting Broken Components to Understanding
       Complex Systems. Ashgate. — Complements Vaughan: erosion of margin proceeds by small
       locally-rational steps, each of which is defensible, and the system's own success at
       absorbing them is what conceals the drift. Retraction-and-continue is a locally rational
       step.
    7. Lunney, J. et al., 2017. "Postmortem Action Items." ;login: 42(1), USENIX. [SUBTITLE AND
       CO-AUTHORSHIP UNVERIFIED — article and venue confirmed via USENIX-hosted PDF.] — The
       operational-practice statement of the same problem: what distinguishes teams whose
       reliability improves from teams stuck firefighting is what happens to the action items
       *after* the incident is closed. Grey-literature surveys report postmortem action-item
       completion rates in the 30-40% range [FIGURES UNVERIFIED — sourced from practitioner
       blog summaries, no primary study retrieved], but the qualitative claim is uncontested
       across the SRE literature.
    8. Cemri, M., Pan, M.Z., Yang, S., et al., 2025. "Why Do Multi-Agent LLM Systems Fail?"
       arXiv:2503.13657; NeurIPS 2025 D&B Track. — MAST records "Step Repetition" at 15.7% of
       observed failures, the single largest system-design failure mode. Repetition of an
       already-encountered failure is empirically the *most common* thing multi-agent systems
       do, which is the base-rate argument that a caught-and-uncorrected mechanism will recur.

  Strength of challenge: Strong

  Summary: This presumption is challenged by an unusually well-aligned body of work, because
    Tucker & Edmondson's first-order/second-order distinction is not an analogy to the item —
    it is a description of it. Their finding is stronger than "catching is insufficient": the
    reliable catching of small failures actively *suppresses* systemic learning, because each
    catch removes the signal that would have justified changing the process, producing an
    equilibrium that looks healthy and degrades. Dillon & Tinsley supply the mechanism at the
    level of the individual decision-maker: a recovered error is encoded as a success, and
    perceived risk falls while actual risk does not, so the willingness to run the unrepaired
    instrument increases after each retraction. Yin et al. add that the correction itself is a
    substantial new source of defects, so "corrected" is not even a terminal state for the
    single instance. The item's own evidence already contains the predicted outcome: the same
    false-positive sweep has been observed twice, four days apart, and the interval between
    occurrences is the only quantity that matters — it establishes the recurrence rate
    empirically rather than by inference. Three retractions in one day from three independent
    runs is not a good day for error-catching; on this literature it is the signature of an
    error-*generating* layer operating at a rate the catching layer happens to be keeping up
    with, which is a condition with no margin.

  Specific risks: The recurrence rate of each uncorrected mechanism is unbounded and the
    catching layer's capacity is finite, so the system is one missed catch away from an
    uncorrected error propagating into the vault as fact. Because retractions are logged as
    successes, the retraction count is currently being read as evidence of rigour when it is
    evidence of defect production — the metric points the wrong way, which is the worst
    property a metric can have. Per Dillon & Tinsley, each retraction lowers the perceived
    urgency of fixing the instrument, so the probability of the fix ever being made *decreases*
    with each occurrence, which is a self-sealing failure. The false-positive sweep is the
    acute case: a method that produces false positives twice-observed has an unknown true false
    positive rate and every prior use of it is retrospectively suspect, including uses whose
    outputs were accepted and are now load-bearing elsewhere in the wiki. Per Yin et al., the
    three corrections issued today each carry a 15-25% prior of being wrong themselves, and
    nothing checked them. Finally this interlocks with PRESUMPTION-662 (disclosure discharges a
    defect) and PRESUMPTION-669 (a hold's terms are re-read): the system has three separate
    mechanisms for converting an open problem into a closed record without changing anything.

  Mitigations available: (1) Split the record: every retraction must produce two items, a
    corrected-output record and an instrument-defect record, with independent lifecycles. The
    second must not be closable by the run that filed it. This is the direct operationalisation
    of second-order problem solving. (2) Measure recurrence, not catches. Track per-mechanism
    occurrence dates; the 07-31/08-04 pair is a two-point series that already yields an
    interval. A mechanism with two occurrences and no instrument change should be treated as
    having a forecast third. (3) Invert the reporting frame per Tinsley et al. 2012: retraction
    reports should foreground what would have happened had the error not been caught, and by
    what margin it was caught, rather than the catch itself. Framing the chance element is the
    manipulation shown to prevent risk attenuation. (4) Quarantine the twice-failing method:
    a false-positive sweep observed twice should be suspended from producing accepted output
    until its false positive rate is measured on a known set. (5) Audit backwards: enumerate
    prior outputs of the twice-failing method and check which were accepted; the retraction only
    covered today's. (6) Per Yin et al., subject corrections to the same review as originals —
    an unreviewed fix is not obviously better than the defect it replaces. (7) Cap the ratio:
    if retractions per week exceed a threshold, treat it as a capacity signal about the
    producing layer rather than a quality signal about the catching layer.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-668
    Strongest counterargument: A system that catches and publicly retracts three of its own
      errors in a single day is exhibiting the behaviour every safety literature says it should
      — self-reporting without external prompting, at high frequency, with the erroneous output
      withdrawn rather than defended. Tucker & Edmondson's hospitals failed because nurses
      patched silently and told no one; C2A2's runs patched and announced. That is second-order
      *reporting* even where the second-order *repair* has not yet happened, and it creates
      exactly the record from which the repair can later be made — as evidenced by the fact
      that 14b was able to notice the 07-31/08-04 pair at all. The near-miss literature's
      finding is about perceived risk in human decision-makers deciding whether to take a
      subsequent gamble; an agent pipeline has no such gamble to take, and stateless runs do
      not accumulate the complacency the mechanism requires. And repairing the instrument may
      be strictly worse than repairing the output where the instrument is an LLM-based method
      whose failure mode is stochastic: there may be no "fix" to apply, only a detection layer,
      which is what the retraction is.
    What would need to be true for C2A2 to be safe: (a) The retraction records are durable,
      indexed and actually consulted before the same method is used again — otherwise the
      "record from which repair can be made" is theoretical. (b) Someone or something has
      authority and a schedule to convert instrument-defect records into changes; the sibling
      item PRESUMPTION-673 reports two agents naming durable fixes that neither was authorised
      to make, which is evidence against this condition holding. (c) The recurrence interval is
      long relative to the repair interval — two occurrences four days apart against a repair
      backlog measured in weeks fails this. (d) The catching layer's coverage is high enough
      that an uncaught error is rare; this is unmeasured, and by construction the system cannot
      observe its own misses.
    How to test: Cheap and decisive. Take every self-retraction in the vault's history, extract
      the named producing instrument, and count distinct instruments against repeat
      occurrences. If the distribution has a heavy tail — a few instruments producing most
      retractions — the first-order/second-order diagnosis is confirmed and the fix list is the
      head of that distribution. Then, for each retraction, check whether any commit touched the
      producing instrument within N days; the fraction where none did is the discharge rate,
      and Tucker & Edmondson predicts it is near zero. Both are single passes over data already
      held.

  SYSTEMIC-RISK-FLAG:
    Date: 2026-08-05
    Affected items: PRESUMPTION-664, PRESUMPTION-666, PRESUMPTION-668, PRESUMPTION-669
      (continuous with PRESUMPTION-660, PRESUMPTION-661)
    Common vulnerability: All four substitute a *declaration* for a *measurement*. The system
      reads an artifact produced by, or adjacent to, the very process whose state is in
      question — an empty report channel (664), a status assertion (666), a retraction (668),
      a hold's label (669) — and treats that artifact as the state. In 668 specifically, the
      declaration is a record of *having caught* something, which the literature shows is
      encoded as a success and therefore actively reduces the pressure to measure.
    Literature basis: Tucker & Edmondson 2003 (first-order solving suppresses system change);
      Dillon & Tinsley 2008 and Tinsley et al. 2012 (recovered failures encoded as successes,
      perceived risk falls while actual risk does not); Vaughan 1996 / Dekker 2011
      (normalization of deviance, drift); Huang et al. 2017 (differential observability);
      Cemri et al. 2025 (step repetition as the largest MAS design failure mode).
    Risk level: Critical
    Recommendation: Adopt a single invariant across the monitoring layer — no health claim may
      be derived from an artifact produced by the subject of the claim, and no defect may be
      closed by the instrument that produced it. Every green signal must trace to an
      independently observed quantity; every catch must open an instrument record that outlives
      the run that filed it.

  Search scope: Adequate. Concepts searched: self-reported error correction and recurrence;
    first-order vs second-order problem solving; near-miss learning, risk attenuation and the
    Dillon/Tinsley programme; incorrect bug fixes and fix-induced defects; normalization of
    deviance and drift into failure; postmortem action-item follow-through; step repetition in
    multi-agent systems. Not searched: CAPA (corrective and preventive action) effectiveness
    literature from regulated manufacturing and pharma, which likely contains quantitative
    recurrence-after-correction rates and would sharpen the estimate.
