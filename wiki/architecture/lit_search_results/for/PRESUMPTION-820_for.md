SEARCH-FOR-PRESUMPTION-820:
  Date searched: 2026-08-17
  Original item: PRESUMPTION-820
  Original statement: [inferred] That a review verdict is durable — that a pass mark is a fact about the
    day rather than a record of which questions one reviewer asked. Extends PRESUMPTION-810 (08-15) with
    today's mechanism, which changes the remedy from "record scope" to "record method."
  Risk if wrong: **High**. Priority: High.
  Search question (as queued): test coverage as a property of the suite not the code; audit sampling and
    re-performance; absence of evidence versus evidence of absence in inspection regimes.

  POLARITY NOTE — WHAT WAS ACTUALLY SEARCHED FOR. The item is worded as the DEFECTIVE belief. The
  proposition searched FOR is the CORRECTIVE CONVERSE, in four clauses:
    (C1) A COVERAGE FIGURE IS A PROPERTY OF THE PROCEDURE, NOT OF THE OBJECT. What a suite exercises is
         a fact about the suite; it is not a fact about the code.
    (C2) **AND THE PROCEDURE'S SCOPE IS THE WEAKER HALF OF THE PREDICTION — WHAT WAS DONE INSIDE THE
         SCOPE PREDICTS BETTER THAN HOW MUCH SCOPE WAS COVERED.** This is 820's specific advance over
         PRESUMPTION-810 (scope -> method) and it is the clause on which this file turns.
    (C3) AUDIT PRACTICE RELATIVISES THE CONCLUSION TO THE PROCEDURE EXPLICITLY, AND MAKES
         RE-PERFORMANCE A DISTINCT EVIDENCE TYPE because inspecting the record of a control is not the
         same act as executing it.
    (C4) A CLEAN INSPECTION LICENSES "NO DEFECT FOUND BY THIS METHOD," NEVER "NO DEFECT."
  "SUPPORTED" below means 14b's diagnosis is well grounded, and is equivalently evidence AGAINST the
  presumption as worded.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-820
    Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: pass marks were consumed
      downstream as facts about days, by readers who had not asked the reviewer's question)
    Transform at each step:
      14b: Extended PRESUMPTION-810 with a new same-day mechanism; identified that the mechanism
        relocates the remedy from recording SCOPE to recording METHOD.
      15a: Searched for supporting literature on the corrective proposition; register check first.
    Current status: SUPPORTED (Strong on the core, Moderate on the advance) — BUT SEE THE DUPLICATION
      WARNING, WHICH IS NEAR-TOTAL

  **DUPLICATION WARNING — READ BEFORE DISPOSITION. THIS WAS MINTED YESTERDAY.**
    - **PREMISE-172** (validated **2026-08-16**, ACTIVE, Moderate, source item **PRESUMPTION-810** —
      the item 820 explicitly extends): "**A PASS MARK IS A VERDICT ABOUT A (READER, FRAME, SCOPE)
      READING — NOT A PROPERTY OF THE FILE. Review is not idempotent across reviewers or across frames,
      so a mark carries no information about what was NOT examined and is therefore not transferable to
      a later reader with a different question.**" That is PRESUMPTION-820's first sentence, twenty-four
      hours old. PREMISE-172 further records that three professions independently made scope a MANDATORY
      FIELD OF THE VERDICT (ISA 705 modified opinions; systematic-review search reporting; code-review
      coverage/participation research), and it already cites **McIntosh, Kamei, Adams & Hassan (2014)**
      for the finding that coverage and participation are SEPARATELY associated with post-release
      defects, with **participation the larger effect (~5 extra defects vs ~2)** — i.e. the register
      already holds a measured statement that the scope axis is the smaller half.
    - PREMISE-172 also already carries: an EXPLICITLY-NOT-INCORPORATED clause refusing the self-reported
      coverage field (a self-produced artefact certifying a self-produced artefact, PREMISE-096); a
      pointer to PREMISE-162 (capture-recapture needs TWO INDEPENDENT READERS by construction); and a
      **CHEAP PRIOR TEST owed before any remedy is built** — classify the defective pass-marked days as
      FRAME-MISMATCH versus WITHIN-FRAME MISS, "because the two classes have disjoint fixes."
    - Adjacent and binding: **PREMISE-150** (a batch of defects a detector failed to catch bounds THE
      DETECTOR'S COVERAGE, not the population); **PREMISE-162** (a run auditing its own instrument
      produces a catch count with no denominator); **PREMISE-109** (bars the coverage percentage);
      **PREMISE-168** (bars the bare numerator); **PREMISE-132** (citing is not verifying — the direct
      ancestor of "checking that identifiers exist is not checking what they say"); **PREMISE-096**
      (self-produced artefact certifying a self-produced artefact); **PREMISE-121** (the review queue
      degrades specifically on LOW-INFORMATION items).
  Grep terms used against `validated_premises.md`: pass mark, verdict, review, coverage, re-perform,
  sampling, scope, frame, idempot, inspection, absence of evidence, method. DECLARED LIMITATION: string
  grep at ~56% recall (ASSUMPTION-1052) — LOWER BOUND. **NO NOVELTY-FLAG.**
  **THE RESIDUAL:** PREMISE-172 obliges STATING THE FRAME. 820 asserts something one step stronger —
  that **two reviewers sharing a frame and a scope can still return different verdicts, because the
  frame does not determine the questions asked inside it.** The literature below supports that stronger
  claim and, in one case, MEASURES the size of the gap between the scope axis and the method axis. That
  measurement is the whole of 820's advance over 810.

  Supporting evidence found: Yes

  Sources:
    1. Inozemtseva, L. & Holmes, R. (2014), "Coverage Is Not Strongly Correlated with Test Suite
       Effectiveness," *Proceedings of ICSE 2014*, pp.435-445 (ACM Distinguished Paper). — **The direct
       support for clauses (C1) and (C2), and the best source located this run because it separates the
       two axes and measures them.** The study took five large open-source Java projects (~100 KLOC
       each, each with 1000+ test methods), generated mutants, and asked whether coverage predicts a
       suite's ability to detect them. Two findings, both load-bearing for 820. First, **once the NUMBER
       OF TEST CASES is controlled for, the correlation between coverage and effectiveness is only LOW
       TO MODERATE** — the raw association is substantially an artefact of suite size. Second,
       **stronger forms of coverage (decision, modified-condition) "do not provide greater insight into
       the effectiveness of the suite"** — i.e. refining the SCOPE METRIC does not recover the missing
       predictive power, because the missing power is not in that axis at all. Transferred to 820: a
       recorded scope field is the coverage metric, and this is the measured demonstration that the
       scope metric is the weak half. It also supplies the reason WHY a pass mark is not durable — the
       same nominal coverage is compatible with widely different detection ability, so two reviewers
       reporting the same scope are not reporting the same verdict.
       [SNIPPET LEVEL — the ACM DL record, the Semantic Scholar entry, a PDF mirror, Adrian Colyer's
       "the morning paper" write-up and the "It Will Never Work in Theory" summary were all LOCATED this
       run and read at retrieved-summary level. **The paper itself was NOT fetched and read in full.**
       Authors, venue, page range, award status and the two headline findings are confirmed across
       multiple independent summaries; the effect sizes are not quoted here because they were not read
       from the paper.]
    2. IAASB, *International Standard on Auditing 530: Audit Sampling*. — **The support for clause (C3),
       and it is stronger than it first appears because of one word in the definition.** ISA 530 defines
       SAMPLING RISK as "the risk that the auditor's conclusion based on a sample may be different from
       the conclusion **if the entire population were subjected to the SAME AUDIT PROCEDURE**." The
       conclusion is therefore DOUBLY relativised — to the sample AND to the procedure — and the
       standard's own counterfactual holds the procedure fixed, which concedes that a different
       procedure would give a different answer and treats that as a separate risk entirely (NON-sampling
       risk). The standard then requires the auditor to **evaluate whether the sampling has provided a
       reasonable basis for conclusions about the population**, and where it has not, to extend the
       sample or perform ALTERNATIVE PROCEDURES — the remedy for a method shortfall is a different
       method, not more of the same. The companion point, from ISA 500's evidence hierarchy, is that
       **RE-PERFORMANCE is a distinct procedure from INSPECTION**: the auditor executes the control
       independently rather than examining the record that it was executed. ASSUMPTION-1108's four
       pass-marked days — reviewed by checking that identifiers EXIST rather than what they SAY — is
       exactly inspection standing in for re-performance.
       [SNIPPET LEVEL — four independent hostings of the ISA 530 text (IBR-IRE, ICJCE, MIA Malaysia, and
       an O'Reilly chapter) were LOCATED this run and read at retrieved-summary level. **No ISA text was
       opened and read in full.** The sampling-risk definition is reported as retrieved and is
       consistent across the summaries; the re-performance/inspection distinction is cited from
       established knowledge of ISA 500 and was NOT retrieved this run. NOTE: PREMISE-172 already flags
       its ISA 705 citation as "SNIPPET LEVEL — primary text not reached, and this is the entry's
       weakest citation." **This file reproduces that weakness for a second auditing standard**, which
       should be recorded rather than glossed.]
    3. Altman, D.G. & Bland, J.M. (1995), "Absence of evidence is not evidence of absence," *BMJ*
       311:485. — **The support for clause (C4), and the canonical short statement of it.** The argument
       is about statistical power but transfers exactly: a non-significant result from an underpowered
       study is routinely misread as demonstrating no effect, when it establishes only that this study
       did not detect one. A clean pass mark from a review of unknown power says only that THIS reading
       found nothing; the strength of that negative is a function of the method's sensitivity, which is
       precisely the quantity a scope field does not carry.
       [CANONICAL — cited from established knowledge, NOT re-verified this run; no search was executed
       against it. The citation is standard and stable, but this file did not confirm it, and per
       PREMISE-132 that should be visible.]
    4. McIntosh, S., Kamei, Y., Adams, B. & Hassan, A.E. (2014), "The Impact of Code Review Coverage and
       Code Review Participation on Software Quality," *MSR '14*, pp.192-201. — Named because it is the
       measured bridge between clauses (C1) and (C2) and because it is the one source that speaks to
       820's scope-to-method shift in the review domain directly: coverage and participation are
       separate variables, each independently associated with post-release defects, and **participation
       — a property of HOW the review was conducted — outranks coverage, a property of HOW MUCH was
       looked at.**
       [REGISTER-HELD. Recorded in PREMISE-172 as "[VERIFIED at abstract/record level]" on 2026-08-16.
       NOT re-verified this run. Counted as reinforcing, not as independent evidence — per PREMISE-120,
       a second citation of the same source by a second agent is not a second measurement.]
    5. Petersson, Thelin et al. on capture-recapture and defect-content estimation, via PREMISE-162. —
       Named for the constructive alternative, and because it settles what the recorded field CANNOT do:
       estimating what a review MISSED requires **two independent readers by construction**. A method
       field creates no second stream, so it can improve the interpretability of a verdict but cannot
       estimate its miss rate.
       [REGISTER-HELD via PREMISE-162/172. NOT retrieved this run.]

  Strength of support: **Strong** on (C1) and (C4); **Moderate-to-Strong** on (C2) — the advance —
    and **Moderate** on (C3).
    (C1) has a direct empirical study behind it in the nearest technical domain and is already
    register-held from two further professions. (C4) is canonical and definitional. (C2) is graded
    Moderate-to-Strong rather than Strong for a specific reason worth stating: Inozemtseva & Holmes
    establishes that the scope axis is a WEAK PREDICTOR, and McIntosh et al. establishes that a
    process axis PREDICTS BETTER — but **neither is a study of METHOD RECORDING, and no located source
    tests whether recording the method improves anything.** The support is for the diagnosis, not for
    the remedy. (C3) is Moderate because both auditing standards in play remain unread at primary level
    across two consecutive 15a runs.

  Summary: The corrective proposition is well supported and its core is already a validated premise of
  this register, minted yesterday from the item 820 extends. What this search adds is evidence bearing
  specifically on 820's advance — the shift from recording SCOPE to recording METHOD. Inozemtseva and
  Holmes provide the measured form: once suite size is controlled for, coverage correlates only weakly
  with a suite's actual detection ability, and refining the coverage criterion does not recover the
  gap, because the predictive content is not in that axis. A scope field is a coverage metric, so this
  is a direct measurement that the field 810's remedy proposed is the smaller half. McIntosh et al.,
  already register-held, points the same way from the review side: participation outranks coverage.
  Auditing practice relativises its conclusions to the procedure by definition — ISA 530's sampling risk
  is defined against "the same audit procedure," which concedes the procedure-dependence rather than
  denying it — and treats re-performance as a distinct evidence type precisely because examining a
  record of a control is a different act from executing it, which is the exact defect ASSUMPTION-1108
  reports. Altman and Bland supply the general licence condition: a clean result establishes only that
  this method did not detect, and the strength of that negative depends on a sensitivity the mark does
  not carry. The limit of the support is sharp and should be stated plainly: **the literature supports
  the diagnosis, and no located source tests the proposed remedy.**

  Caveats:
    (a) THIS IS PREMISE-172 AT ONE DAY OLD. PREMISE-151 applies — a second recording of an unremediated
        condition is evidence of incubation, not confirmation. Minting again is barred by
        PREMISE-138(1) and PREMISE-135.
    (b) **THE PROPOSED REMEDY INHERITS THE OBJECTION PREMISE-172 ALREADY SUSTAINED AGAINST THE PREVIOUS
        ONE, AND THIS IS THE MOST IMPORTANT LINE IN THIS FILE.** PREMISE-172 refused the self-reported
        coverage field because it is "a self-produced artefact certifying a self-produced artefact"
        (PREMISE-096). **A recorded METHOD field is exactly as self-certified as a recorded SCOPE
        field.** "I resolved each URL" is a claim about method, and PREMISE-132 (citing is not verifying)
        is the register's own finding that such claims are unreliable in generated text. Moving the
        field from scope to method changes WHAT is asserted, not WHO asserts it, and the objection was
        never about the content. Any disposition that treats 820 as licensing a method field without
        addressing this has not read 172.
    (c) PREMISE-172's CHEAP PRIOR TEST IS STILL OWED AND SHOULD BLOCK THIS ITEM. 172 requires the
        defective pass-marked days be classified as FRAME-MISMATCH (a different question would have
        caught it — metadata helps) versus WITHIN-FRAME MISS (the same question missed it — metadata is
        irrelevant), "because the two classes have disjoint fixes." **820's four days from
        ASSUMPTION-1108 look like WITHIN-FRAME MISSES on their face** — the reviewer asked whether
        identifiers exist and they did; nothing about recording that method would have changed the
        verdict. If that reading holds, 820's remedy is aimed at the wrong class and the correct
        response is re-performance, not documentation. The test is cheap, it is owed from yesterday, and
        it determines this item's disposition.
    (d) DOMAIN TRANSFER FROM MUTATION TESTING IS ANALOGICAL, NOT DIRECT. Inozemtseva & Holmes measure
        automated suites against synthetic mutants in Java. Human and agent review of prose documents
        has no mutation operator, no ground-truth defect population, and no way to control for "number
        of test cases." What transfers is the STRUCTURE of the result — a scope metric that survives
        controlling for effort is a weak predictor — not any coefficient.
    (e) INSPECTION YIELD IS BOUNDED WELL BELOW 100% EVEN INSIDE A PERFECTLY DECLARED METHOD, so no
        recording scheme makes a pass mark durable in the sense the presumption assumes. PREMISE-172
        already states this. The achievable goal is an INTERPRETABLE mark, not a transferable one, and
        conflating the two would set an unreachable target.
    (f) COST, AND IT LANDS ON A KNOWN-FRAGILE CHANNEL. PREMISE-121 holds that the review queue degrades
        specifically on LOW-INFORMATION items; PREMISE-102 holds that the review channel has
        demonstrated zero throughput. A per-verdict method field adds friction to a queue already
        failing, and 15b's cost objection to 172 (metadata on every approval is rarely done and reduces
        throughput) applies here with more force, since a method statement is longer than a scope tag.
    (g) SOURCE INDEPENDENCE. Sources 4 and 5 are register-held from yesterday's run, not independent
        findings. Source 3 was not searched. **Only sources 1 and 2 are new to this file, and neither was
        read at primary level.**

  Search scope: MODERATE, and narrower than the item deserves. Searched: Inozemtseva & Holmes and the
    coverage-versus-effectiveness literature; ISA 530 audit sampling and sampling risk. NOT SEARCHED,
    and each would materially change this file: (i) **INTER-RATER RELIABILITY IN REVIEW** — the queue's
    own angle for ASSUMPTION-1108, and the most direct possible evidence for 820's core claim (two
    reviewers, same artefact, different verdicts, measured kappa); not touched at all, and this is the
    largest gap; (ii) **ISA 500 on re-performance versus inspection at primary level**, cited here from
    established knowledge only; (iii) **REFERENCE-ACCURACY STUDIES IN BIBLIOMETRICS** (citation-
    verification error rates), which would supply a base rate for exactly the identifier-exists-versus-
    identifier-says failure and was named in the queue for the sibling item; (iv) **MUTATION-SCORE-BASED
    review-quality work post-2014**, which may have superseded Inozemtseva & Holmes; (v) **Altman &
    Bland's primary text**, not retrieved.

  Recommendation: **SUPPORTED (Strong on the diagnosis; Moderate on the advance)** for the corrective
  proposition; equivalently NO-SUPPORT-FOUND for the presumption as worded. **Disposition should be
  DEFERRED PENDING PREMISE-172's OWN PRIOR TEST, then a SCOPE-EXTENSION OF PREMISE-172 — not a new
  premise.** Four carries:
    1. NO NEW MINT. PREMISE-172 was validated 2026-08-16 from PRESUMPTION-810 and holds 820's first
       sentence verbatim in substance.
    2. **BLOCK ON THE FRAME-MISMATCH / WITHIN-FRAME TEST (caveat c).** It is owed from yesterday, it is
       cheap, and 820's own instances appear to fall in the class its remedy cannot help. Running it
       is worth more than any further literature search on this item.
    3. IF THE TEST FAVOURS METHOD-RECORDING, THE EXTENSION IS NARROW AND HAS A CONDITION. PREMISE-172
       obliges STATING THE FRAME; the extension is that the statement must name **the ACT PERFORMED
       against the artefact** (what was executed, not what range was looked at), because
       Inozemtseva & Holmes and McIntosh et al. both locate the predictive content on that axis. The
       CONDITION, from caveat (b), is that a method field is a self-report and must be graded as one —
       it improves interpretability and provides NO assurance, and per PREMISE-096 it may not be counted
       as verification.
    4. THE ASSURANCE PROBLEM IS SEPARATE AND HAS A KNOWN ANSWER THAT IS NOT A FIELD. Estimating what a
       review missed requires two independent readers (PREMISE-162). If the goal is assurance rather
       than interpretability, the correct instrument is re-performance on a sample — which is also ISA
       530's remedy when sampling has not provided a reasonable basis — and it should not be confused
       with, or displaced by, a metadata change.
