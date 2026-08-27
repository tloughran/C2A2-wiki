SEARCH-AGAINST-PRESUMPTION-878:
  Date searched: 2026-08-26
  Original item: PRESUMPTION-878
  Queue ref: for_lit_search.md — ITEM: PRESUMPTION-878 (Priority High)
  Original statement: [inferred] That the right response to a defect class found by hand is to build a
    downstream check — rather than to repair the process that generates the defect, or to accept that
    hand-reading is the instrument.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-878
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from absent alternatives — a one-member remedy space held across five runs,
           sharpened by a generator-level hypothesis (ASSUMPTION-1211) that no run picked up.
           Medium-high confidence; the absence is clear, the alternatives are 14b's construction.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: Four WebSearch queries executed 2026-08-26, plus one cross-cutting query on defect
    removal efficiency. Literatures reached: (a) quality management / cost-of-quality (Deming, Dodge,
    prevention-vs-appraisal economics); (b) software engineering empirical work on defect prevention
    vs. defect detection; (c) static analysis deployment studies — false positives, suppression
    practice, alert fatigue; (d) LLM guardrail / post-hoc-correction literature. Venues reached:
    arXiv (cs.SE), IEEE TSE, FSE 2025, ResearchGate abstracts, industry practitioner sources.
    NOT COVERED, and these matter: (i) the Toyota/lean *jidoka* and poka-yoke literature on
    error-proofing at source, which is the strongest form of the prevention argument and would likely
    move this from Strong to Very Strong; (ii) the Orthogonal Defect Classification (ODC) literature,
    which is the standard method for deciding *whether* a defect class is generator-fixable — this is
    the single most decision-relevant body of work for C2A2 and I did not reach it; (iii) any
    empirical work specifically on hallucination-mitigation-by-retrieval vs. hallucination-detection
    in citation generation, which is the closest analogue to ASSUMPTION-1211's "plausible gloss from
    two real neighbouring fields." Search confidence: MODERATE-HIGH on the general claim, LOW on the
    C2A2-specific transfer.

  Challenging evidence found: Yes

  Sources:
    1. Harold F. Dodge (attributed) / W. Edwards Deming. "You cannot inspect quality into a product."
       Deming's Point 3 of the Fourteen Points: "Cease dependence on mass inspection ... Require
       statistical evidence that quality is built in, to eliminate need for inspection on a mass
       basis." https://en.wikiquote.org/wiki/W._Edwards_Deming — This is the canonical statement of
       the challenge: the quality is there or it is not by the time it is inspected, so the inspection
       is at best a measurement and never a repair. Note this is a quotation-collection source;
       primary text is *Out of the Crisis* (1986), which I did not reach. SNIPPET-ONLY (tertiary
       source; attribution of the Dodge formulation is itself contested in the literature).
    2. [authors unverified]. "A literature survey of the quality economics of defect-detection
       techniques." arXiv:1612.04590. https://arxiv.org/pdf/1612.04590 — A survey of accumulated
       empirical knowledge on the *efficiency* of defect-detection techniques; establishes that
       detection efficiency is an empirical quantity with wide variance rather than a property one
       can assume by building a check. Directly relevant because C2A2 has assumed the efficiency of
       four unbuilt checks without estimating any of them. SNIPPET-ONLY.
    3. [authors unverified]. "Defects Prediction and Prevention Approaches for Quality Software
       Development." International Journal of Advanced Computer Science and Applications, Vol 9 No 8.
       https://thesai.org/Downloads/Volume9No8/Paper_57-Defects_Prediction_and_Prevention_Approaches.pdf
       — Reports the standard cost-of-quality finding: "a small increase in the prevention measure
       will normally create a major decrease in total quality cost," and that the longer a defect
       stays in process the more expensive it becomes to fix. SNIPPET-ONLY.
    4. [authors unverified]. 2025. "An Empirical Study of Suppressed Static Analysis Warnings."
       FSE 2025. https://software-lab.org/publications/fse2025_suppressions.pdf — The sharpest hit
       against the presumption's *delivery* assumption. Finds false positives are the most common
       reason for suppressing warnings (34.4% of all suppression cases), and that suppression is a
       routine practice rather than an exception. A built check whose output is suppressed has the
       same net effect as an unbuilt check, minus the build cost. SNIPPET-ONLY.
    5. Chou [first name unverified] et al. 2005. "False Positives Over Time: A Problem in Deploying
       Static Analysis Tools." Workshop on the Evaluation of Software Defect Detection Tools.
       https://www.cs.umd.edu/~pugh/BugWorkshop05/papers/34-chou.pdf — Documents a ratchet:
       "false positives accumulate over time because developers fix real defects but tend to leave
       false positives in the source code." Applied to C2A2, a check's flag population monotonically
       enriches for non-actionable items, so the check's apparent value decays even if its true
       detection rate is constant. SNIPPET-ONLY.
    6. [authors unverified]. 2023. "Mitigating False Positive Static Analysis Warnings: Progress,
       Challenges, and Opportunities." IEEE Transactions on Software Engineering.
       https://dl.acm.org/doi/10.1109/TSE.2023.3329667 — "Reports generated by static analysis tools
       often contain a large number of non-actionable findings, which can overwhelm developers to the
       point of ignoring them altogether — a phenomenon known as alert fatigue." This is a direct
       prediction about what happens when four new checks discharge into a review gate that is already
       seventeen days silent. ABSTRACT-ONLY (paywalled; read via search snippet and the ResearchGate
       abstract).
    7. [authors unverified]. 2025. "Bridging the Safety Gap: A Guardrail Pipeline for Trustworthy LLM
       Inferences." arXiv:2502.08142. https://arxiv.org/html/2502.08142 — States the transfer of the
       Deming argument into the generative-AI setting explicitly: "post-hoc correction methods rewrite
       problematic content in LLM outputs but fail to address their root causes, such as
       hallucinations, that often stem from insufficient, inaccurate, or outdated source
       information." This is precisely ASSUMPTION-1211's mechanism — a gloss assembled from real
       neighbouring fields is a source-grounding failure, not an output-formatting failure.
       SNIPPET-ONLY.
    8. [authors unverified]. 2025. "No Free Lunch with Guardrails." arXiv:2504.00441.
       https://arxiv.org/pdf/2504.00441 — Frames guardrailing as a constrained trade rather than a
       free addition; supports the claim that each new downstream check imposes a cost that must be
       priced against the prevention alternative. SNIPPET-ONLY (title and framing only).
    9. Capers Jones. "Software Defect Removal Efficiency."
       https://www.ppi-int.com/wp-content/uploads/2021/01/Software-Defect-Removal-Efficiency.pdf —
       Included as *counter-evidence to my own challenge*, in the interest of honesty. Jones's
       benchmarks give inspections a DRE of up to ~85% and hold that "this level of DRE cannot be
       achieved using testing alone" — i.e. detection layers do work, and the industry average of 85%
       DRE is achieved primarily by stacking them. The presumption is therefore not absurd; the
       challenge is about the *ordering and completeness* of the remedy space, not about whether
       checks ever help. SNIPPET-ONLY.

  Strength of challenge: Strong

  Summary: The presumption's remedy — build a downstream check — is the one that seventy years of
  quality management specifically warns against making the *first* move. Deming's third point is that
  dependence on mass inspection must cease and evidence be required that quality is built in;
  cost-of-quality economics consistently find that marginal prevention spending dominates marginal
  appraisal spending in total-cost terms. The generative-AI literature restates the same finding for
  C2A2's actual failure mode: post-hoc correction "fails to address root causes such as
  hallucinations, that often stem from insufficient, inaccurate, or outdated source information,"
  which is a near-verbatim description of ASSUMPTION-1211's plausible-gloss mechanism. Independently
  of the prevention argument, the deployment literature challenges the detection remedy on its own
  terms: static-analysis checks produce non-actionable findings at rates high enough to induce alert
  fatigue and outright ignoring; false positives are the most common reason for suppression (34.4%);
  and false positives accumulate over time because real defects get fixed and false ones do not. Two
  facts already in C2A2's own record are what make this Strong rather than Moderate. First, four
  checks named across five runs and none built — the detection remedy has a demonstrated delivery
  failure rate of 100% in this system, which no literature is needed to establish. Second, the
  destination for the checks' output is a gate that has not moved in seventeen days, which is the
  precondition the alert-fatigue literature identifies for a check to become net-negative. The honest
  qualifier is Jones's DRE benchmarks: inspection layers genuinely do remove defects, and nothing
  found here says a check would fail to detect. The challenge is that detection was treated as the
  whole remedy space, and the literature says it is the least cost-effective member of it and the one
  most sensitive to a condition C2A2 currently violates.

  Specific risks: (a) Five runs of engineering attention spent naming the wrong object — if the
  generator is fixable, every check built is permanent recurring cost incurred to observe a defect
  that need not have been produced. (b) Alert-fatigue conversion: four new flag populations
  discharging into a seventeen-day-silent gate is the textbook setup for the checks to be ignored
  wholesale, at which point they cost more than they return (cf. PRESUMPTION-884, which is already an
  instance — a 307-entry flag population dismissed by a single blanket attribution). (c) Ratchet
  effect: per Chou et al., the flag population enriches for false positives over time as true ones are
  fixed, so a check's signal-to-noise ratio degrades monotonically unless actively retuned, and
  nothing in C2A2 currently retunes checks. (d) Suppression as the observed endpoint: FSE 2025 finds
  suppression is routine and driven by false positives; a suppressed check is indistinguishable from
  an unbuilt one except in maintenance cost. (e) The third, entirely unexamined member of the remedy
  space — "accept that hand-reading is the instrument" — carries its own risk if wrong (it does not
  scale past the reader's throughput), and no run has priced it either.

  Mitigations available:
    - Before building check number five, run Orthogonal Defect Classification (or any structured
      defect-cause taxonomy) over the existing hand-found defect population to determine what
      fraction is generator-attributable. This is the standard method for exactly this decision and
      I did not reach the literature; flagged as a known gap, not an absence.
    - Estimate each proposed check's expected false-positive rate *before* building it, and refuse to
      build any check whose flag population would exceed the gate's demonstrated disposition rate
      (currently zero for seventeen days). This makes PRESUMPTION-883 a hard precondition on
      PRESUMPTION-878.
    - Treat ASSUMPTION-1211 as a live prevention lead: if the writer assembles a gloss from two real
      neighbouring fields, the prevention fix is to make the writer emit field provenance rather than
      to build a reader that detects spliced glosses.
    - Adopt an explicit three-member remedy space in the run template (detect / prevent / accept),
      requiring each run that proposes a check to state why the other two were rejected. The cost is
      one sentence per run.
    - Retain the detection remedy where prevention is unavailable — Jones's DRE data says stacked
      detection layers are how 95%+ removal is actually achieved. The challenge is to ordering, not
      to existence.

  STEELMAN:
    Item: PRESUMPTION-878
    Strongest counterargument: Deming's argument is about *mass inspection of manufactured units* in a
    process with statistical control, where the generator's variance can be measured and reduced. A
    language-model writer is not that object: its error process is not stationary, cannot be brought
    into statistical control by any presently known method, and "editing the writer" means editing a
    prompt whose effect on any specific defect class is unmeasurable without — precisely — a
    downstream check to measure it against. On this reading the presumption is not a blind spot but
    the correct engineering order: you cannot know whether a prevention edit worked without a
    detector, so the detector is prior to the fix, not an alternative to it. Capers Jones's benchmarks
    support this operationally — 85%+ defect removal efficiency is achieved by stacking detection
    layers, not by process purification. And the alert-fatigue objection is an argument about a
    *badly-tuned* check discharging into an *unresponsive* gate, both of which are contingent
    conditions C2A2 could fix without abandoning the detection strategy.
    What would need to be true for C2A2 to be safe: (i) the checks must actually get built — four
    named and zero built across five runs is the fact that most undermines the counterargument, since
    a detector that is prior to the fix but never exists leaves the fix unreachable too; (ii) each
    check's flag population must be disposable at a rate at least equal to its production rate,
    which requires PRESUMPTION-883 to be resolved first; (iii) the checks must be *deterministic*
    (the queue calls them "deterministic check candidates"), because a probabilistic check
    inherits the generator's error process and the alert-fatigue result then applies with full force;
    (iv) the flag populations must be periodically re-audited for false-positive enrichment per Chou
    et al., or their value silently decays; (v) at least one run must actually attempt the prevention
    experiment, so the claim "prevention is unmeasurable" is tested rather than assumed.
    How to test: Directly testable and cheap. Take the existing hand-found defect corpus and classify
    each instance by whether ASSUMPTION-1211's mechanism (gloss spliced from two real neighbouring
    fields) explains it. If a majority is generator-attributable, run one prevention experiment —
    change the writer's field-emission behaviour on a held-out slice — and hand-read the slice. Two
    numbers settle it: the defect rate in the prevention slice vs. the control, and the build-cost of
    the check that would have detected the same defects. Separately and independently, measure the
    detection remedy's *delivery* rate directly: four checks named, zero built, across five runs.
    That is an observed 0/4 on a base of five opportunities, and it is a property of this system, not
    of the literature.

  Recommendation: CHALLENGED

  SYSTEMIC-RISK-FLAG:
    Date: 2026-08-26
    Affected items: PRESUMPTION-878, PRESUMPTION-879, PRESUMPTION-880, PRESUMPTION-881,
      PRESUMPTION-882, PRESUMPTION-883, PRESUMPTION-884
    Common vulnerability: **Every remedy path in this batch terminates at the same single,
      currently unresponsive human review gate, and not one of the seven presumptions conditions its
      behaviour on that gate's responsiveness.** 878 sends new flag populations to it; 879 hands
      declined fixes to it; 880's downward corrections are unadjudicated because it never rules; 881's
      fifteen consecutive breach disclosures are addressed to it; 882's "findings" would enter it;
      883 is about it directly; 884's blanket suppression rule was never ruled on by it. The gate has
      not moved in seventeen days and stands at 74 pending. This is a single point of failure that
      every item in the batch treats as an available, responsive counterparty.
    Literature basis: Little's law under λ > μ — the queue grows without bound and "the law still
      holds, but it tells you the system is broken" (https://en.wikipedia.org/wiki/Little's_law;
      Little & Graves, Ch. 5, https://web.eng.ucsd.edu/~massimo/ECE158A/Handouts_files/Little.pdf);
      backpressure literature on unbounded queues as "the mechanism of collapse"
      (https://designgurus.substack.com/p/system-design-deep-dive-backpressure); Vaughan's
      normalisation of deviance (https://en.wikipedia.org/wiki/Normalization_of_deviance); alert
      fatigue with acceptance dropping ~30% per repeated reminder (Ancker et al. [attribution
      recalled, not confirmed], BMC MIDM 2017,
      https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-017-0430-8); HITL
      governance guidance that escalation gates must "deny by default on timeout"
      (https://www.arthur.ai/column/human-in-the-loop-governance-for-ai-agents).
    Risk level: Critical
    Recommendation: No further remedy in this batch should be designed on the assumption that the gate
      will rule. Either (i) give the gate a timeout semantics — an unruled item auto-dispositions to a
      named default state after N days, which converts silence from an unbounded liability into a
      decision; or (ii) couple intake to disposition (PRESUMPTION-883) so the gate cannot be
      over-filled; or (iii) formally re-designate the gate as unavailable and re-plan every item in
      this batch against a remedy path that does not require it. Doing none of these means five to
      seven independent presumptions all fail together on one condition.
