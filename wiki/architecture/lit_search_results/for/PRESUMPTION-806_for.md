SEARCH-FOR-PRESUMPTION-806:
  Date searched: 2026-08-15
  Original item: PRESUMPTION-806
  Original statement: [inferred] That the fleet's failures are independent events. Today's nine deliverable-less runs are treated, wherever they are treated at all, as nine separate incidents; but at least four share one signature — a stall at a permission-gated or environment-gated tool call, with no timeout and no artefact. The 08:00 slot is triple-booked (`c282-wiki-agent-daily-run`, `morning-project-status`, `morning-system-health`) and all three of the runs in and after that window failed. The health contract itself records the base rate — "over 110 runs, 39 never finished" — as a property of runs rather than of a shared gate. If the failures are correlated, then the fleet's redundancy is nominal: adding another monitor adds no independent evidence, which is exactly what PRESUMPTION-799 predicts from the other direction.

  POLARITY NOTE — what was searched FOR. The presumption is worded as the DEFECTIVE belief ("failures are independent events"). The proposition searched FOR is the CORRECTIVE CONVERSE, in four clauses: (i) that CORRELATED FAILURE IS THE NORM RATHER THAN THE EXCEPTION in redundant and co-scheduled systems, and that the independence assumption has been directly tested and directly falsified where anyone bothered to test it; (ii) that correlation is analysed by separating a ROOT CAUSE from a COUPLING FACTOR, and that shared time window, shared environment and shared interface are canonical coupling factors; (iii) that the correlation is QUANTIFIABLE — the beta-factor apparatus gives both a parameter and a ceiling on how much any amount of redundancy can buy; and (iv) that a fleet reliability figure computed as a product of per-run probabilities is therefore not conservative-but-approximate, it is wrong in the unsafe direction, often by orders of magnitude. "SUPPORTED" below means 14b's worry is well grounded, and is equivalently evidence AGAINST the presumption as worded.

  **DUPLICATION WARNING — READ BEFORE DISPOSITION.** The register check below found that
  PRESUMPTION-806's core claim was minted as **PREMISE-141 clause (2) on 2026-08-05 at High
  confidence**, from PRESUMPTION-664, on the evidence of the 2026-08-04 four-silent-run event —
  the same phenomenon, ten days earlier, in the same fleet. PREMISE-141 clause (2) reads: "the
  four silent runs were ONE event with one cause, not four independent failures. Any fleet
  reliability figure computed as a product of per-run failure probabilities is therefore wrong by
  orders of magnitude, and any redundancy argument that counts two instruments as two chances is
  counting one." That is PRESUMPTION-806, verbatim in substance. This file proceeds because the
  queue asked for the search and because there is a genuine residual, but a disposition that mints
  a new premise here would be minting PREMISE-141 a second time, which PREMISE-138 clause (1) and
  PREMISE-135 both bar.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-806
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by grouping the day's failures by signature and time slot rather than by task,
           which no run does.
      15a: Searched for supporting literature on the corrective proposition, and performed the
           correlation arithmetic the item's evidence permits.
    Current status: SUPPORTED (but see DUPLICATION WARNING)

  REGISTER CHECK (performed BEFORE writing this file):
    Grepped `validated_premises.md` for: common-cause, common-mode, correlated, independen,
    redundan, contention, single point, beta-factor.
    Found and read in full:
      - **PREMISE-141** (2026-08-05, ACTIVE, High) — see DUPLICATION WARNING. Clause (2),
        "CORRELATED TERMINATION VOIDS PER-RUN INDEPENDENCE," is stated by its own text to have "no
        antecedent in this register" and is explicitly the ARITHMETIC complement to PREMISE-110.
        Its Applicable-to already names "any reliability, streak or coverage figure computed over
        runs" and "the redundancy argument in PREMISE-142." Its LOAD-BEARING SCOPE LIMIT transfers
        directly and must travel with 806: "THE CAUSE OF `[Request interrupted by user]` IS
        UNDETERMINED... This premise licenses no claim that the interruptions were faults rather
        than deliberate human stops." 806 cites the same signature and inherits the same limit.
      - **PREMISE-110** (ACTIVE) — a monitor sharing a failure domain with its subject is a single
        channel wearing two labels. The monitoring-layer form of the same result; PRESUMPTION-799's
        direction.
      - **PREMISE-089** (2026-07-??, ACTIVE) — freshness/liveness is a PER-SOURCE property; and the
        recorded refinement is exactly this item: "freshness-independence does NOT imply
        failure-independence — FEEDS SHARING AN UPSTREAM SCHEDULER CAN FREEZE TOGETHER, so
        per-source freshness tracking must coexist with shared-failure awareness." 15b's noted
        challenge on that premise was, in the register's own words, that "shared upstream
        schedulers create common-mode failure (captured in the Statement)."
      - **PREMISE-045** (2026-06-02, ACTIVE) — the sufficiency gap: "a same-regime re-check can
        share the fault (Knight & Leveson; common-mode failure), so re-verification is NECESSARY
        but not automatically SUFFICIENT."
      - **PREMISE-004** (ACTIVE, with standing independence caveat) — triangulation is legitimate
        but depends on GENUINE independence; sharpened 2026-07-06 (DISPOSITION-409) so that
        "correlated LLM errors (Kim et al. ICML 2025) mean SAME-MODEL-FAMILY CONVERGENCE IS NOT
        INDEPENDENT EVIDENCE; count same-mechanism/same-family lines as one."
      - **PREMISE-058** (correlated experts give a reduced EFFECTIVE N, not near-chance noise;
        Clemen & Winkler 1985), **PREMISE-080** (a convergence battery is robust only CONDITIONAL
        on demonstrated independence; shared method variance yields pseudo-convergence and
        independence must be MEASURED, not assumed), **PREMISE-096** (a corroborating layer must
        draw on a genuinely disjoint evidence source "or 'independent' is nominal only"; explicit
        Knight & Leveson common-mode caveat), **PREMISE-085** (a single supervised node remains a
        single point of failure), **PREMISE-082** (redundant fallback paths count only if actually
        exercised).
    CONCLUSION OF THE CHECK: **NEAR-TOTAL OVERLAP ON THE PRINCIPLE, AND ONE ENTRY IS A SUBSTANTIVE
    DUPLICATE. NO NOVELTY-FLAG.** Nine ACTIVE premises bear on this, one of them minted ten days
    ago from the same phenomenon. The residual is genuinely narrow and consists of three things
    that PREMISE-141 does not contain:
      (R1) THE COUPLING FACTOR IS NAMED AND IS SPECIFIC. PREMISE-141 says the four runs were "one
           event with one cause" and leaves the cause undetermined. 806 supplies a candidate that
           141 does not: the 08:00 slot is TRIPLE-BOOKED, and three runs in and after that window
           failed. Schedule co-location as a coupling factor is a testable hypothesis with a
           trivial intervention (stagger the slot), and it is the extension of PRESUMPTION-797's
           schedule-as-design finding that the queue explicitly asked for.
      (R2) THE QUANTIFICATION IS ABSENT FROM THE REGISTER. PREMISE-141 says independence-assuming
           calculations are "wrong by orders of magnitude." It supplies no parameter, no estimator,
           and — most usefully — no CEILING. The beta-factor apparatus supplies all three, and the
           ceiling result is the sharp form of 806's "the fleet's redundancy is nominal."
      (R3) THE SCALING QUESTION IS NEW AND IS THE ITEM'S TYPE. 806 is typed `scaling`, and its risk
           statement asks "whether that fraction is stable or GROWS WITH THE SCHEDULE'S DENSITY."
           No premise addresses the density relationship. This is the one clause of 806 that is not
           a restatement of anything, and it is also the one clause for which the literature located
           here provides the least direct support (see Caveat d).
    DECLARED LIMITATION: string grep, measured at five-of-nine recall by the 2026-08-14 15c run
    (ASSUMPTION-1052 — ~56%). The list above is a **LOWER BOUND**, and given that it returned nine
    entries the true overlap is likely larger. That argues for a narrower disposition, not a wider.

  THE ARITHMETIC, so far as the item's own evidence permits it:
    BASE RATE. 39 of 110 runs never finished = 35.5%. Today: 9 of ~25 deliverable-less = 36%.
    The two agree closely, which is itself worth noting — today is not an outlier day, it is the
    base rate happening again, and treating it as an incident rather than as the process is part
    of what 806 identifies.
    THE 08:00 TRIPLE. Three runs booked in one slot; all three failed. Under an independence
    assumption at p = 0.355, P(a specified triple all fail) = 0.355^3 = 0.045, i.e. ~4.5%.
    **THIS IS NOT A VALID TEST AND MUST NOT BE REPORTED AS ONE.** The triple was selected BECAUSE
    it co-failed; computing a tail probability on a post-hoc-selected group is the error
    PREMISE-124 names (reading a single favourable self-observation as evidence) and PREMISE-136
    warns about (the achievable denominator is fixed by scope). The honest statement is: 4.5% is
    what the co-failure would have cost in surprise had the triple been nominated IN ADVANCE, and
    nominating it in advance — which the schedule file permits, since the triple-booking is a
    static fact — is the whole content of the recommendation below.
    IMPLIED BETA, AND WHY IT IS THE STRIKING NUMBER. Treat the 08:00 slot as a common-cause
    component group. All three members failed together, so the observed common-cause fraction for
    that group approaches 1.0. Set against the empirical ranges the reliability literature reports
    — nuclear component data giving beta from 0.03 to 0.22 with an average of ~0.10, and the IEC
    61508 checklist yielding 0.5-5% for logic solvers and 1-10% for sensors and final elements — an
    implied beta near unity is ONE TO TWO ORDERS OF MAGNITUDE ABOVE anything the field treats as a
    designed system. In reliability-engineering terms that is not a system with common-cause
    contamination; it is a system whose "redundant" elements are one element. n = 1 slot, so this
    is an illustration of the apparatus rather than an estimate (Caveat c).
    THE REDUNDANCY CEILING — the derivation 806 asserts and does not perform. In the beta-factor
    model a 1oo2 group has PFDavg ~= [(1-beta)*lambda*tau]^2 / 3 + beta*lambda*tau / 2, and the
    second term IS INDEPENDENT OF THE VOTING ARRANGEMENT (Rausand & Lundteigen show it is identical
    for 1oo2 and 2oo3). Independent failures fall quadratically with redundancy; the common-cause
    term does not fall at all. Therefore the total improvement available from ANY amount of
    redundancy is bounded by approximately 1/beta. At beta = 0.10 the ceiling is ~10x. At a beta
    approaching 1 — which is what the 08:00 observation implies for co-scheduled runs — THE CEILING
    IS 1x, AND ADDING A MONITOR BUYS NOTHING. That is 806's "the fleet's redundancy is nominal,"
    derived from a standard model rather than asserted, and it is the single most useful thing in
    this file.

  Supporting evidence found: Yes

  Sources:
    1. Rausand, M. & Lundteigen, M.A., "Common Cause Failures (CCFs)," Chapter 10 of the SIS
       textbook, RAMS Group, NTNU. — **The systematic treatment of clauses (i)-(iii), and the
       source of the vocabulary this item most needs.** States the core proposition flatly: "Common
       cause failures represent events where multiple failures occur due to a shared cause. They
       are important to consider because THEY CAN VIOLATE THE EFFECTS OF REDUNDANCY," and notes
       that "today, 'all' standards on functional safety require that CCFs are taken into account —
       regardless of industry domain." Supplies the ROOT CAUSE / COUPLING FACTOR decomposition,
       which is the analytical move 806 needs and no C2A2 artefact makes: a root cause is the basic
       cause which if corrected would prevent this and similar faults; a COUPLING FACTOR is "a
       property (commonality) that makes multiple items susceptible to failure from a shared
       cause." The chapter's enumerated coupling factors read as a checklist for the 08:00 slot:
       same design principles, same hardware, same function, same software, same procedures, SAME
       SYSTEM/ITEM INTERFACE, same environment, SAME PHYSICAL LOCATION. C2A2's runs share all of
       these. Also supplies the beta-factor model (Fleming 1975), its two interpretations (the
       fraction of channel failures that are CCFs; equivalently Pr(CCF | failure of a channel)),
       the 1oo2 and 2oo3 PFD formulas from which the redundancy ceiling above is derived, and the
       defence-strategy taxonomy — reduce root-cause occurrence versus REDUCE COUPLING FACTORS by
       separation and segregation, diversity, and simplifying architecture to avoid undiscovered
       couplings. [VERIFIED this run — the 73-slide chapter PDF was fetched and read in full. Every
       quoted definition, the coupling-factor list, the beta-factor interpretations and the PFD
       formulas are read directly. Version 0.1 lecture material, so treat slide-level phrasing as
       teaching text rather than as a citable standard; the underlying content is standard IEC
       61508 / NUREG practice.]
    2. NUREG/CR-5485 (INEL/EXT-97-01327), *Guidelines on Modeling Common-Cause Failures in
       Probabilistic Risk Assessment*, US NRC; with the ICDE (International Common-cause Failure
       Data Exchange) project, running since 1994. — **The quantitative anchor for clause (iii),
       and the demonstration that this is an instrumented discipline rather than a caution.** The
       guidance provides the beta-factor and Multiple Greek Letter treatments and is the standard
       reference for applying them to instrumentation and control systems. The reported empirical
       ranges are the numbers used in the arithmetic above: a survey of electrical equipment gives
       best-case beta 0.01 and worst-case 0.30; nuclear plant data across thirteen component types
       gives beta from 0.03 to 0.22 with an average of 0.10. The existence of a thirty-year
       international data-exchange programme for exactly this parameter is itself the finding: the
       field concluded decades ago that correlation cannot be assumed away and must be measured per
       system. [SNIPPET LEVEL on quantities — the NUREG/CR-5485 PDF was located at the NRC/INL
       public document host and the beta ranges were read from retrieved secondary summaries and
       from source 1's cross-reference; the NUREG itself was NOT read. Do not quote a page or table
       number onward. The document's existence, title and identifier are confirmed.]
    3. Knight, J.C. & Leveson, N.G. (1986), "An Experimental Evaluation of the Assumption of
       Independence in Multiversion Programming," *IEEE Transactions on Software Engineering*
       SE-12(1):96-109. — **The direct experimental falsification of clause (i), and the closest
       structural analogue to a fleet of same-family LLM agents.** Twenty-seven programmers at two
       universities independently implemented the Launch Interceptor Program from one specification
       with no mutual communication — a design intended to maximise independence — and the versions
       were run against a reference on one million random test cases. Of the 24 versions with
       nonzero failure rates, coincident failures occurred **far more often than independence
       predicts, at z ~= 100, p < 1e-9**. The explanation is the one that transfers: because all
       versions derive from the same finite and partly ambiguous specification, there exist inputs
       on which a common misinterpretation is likely, and "programmers who share a training
       background, a programming language, or exposure to the same reference materials will tend to
       make the same misinterpretation, creating SYSTEMATIC COINCIDENT FAILURE MODES." Substitute
       "agents instantiated from one model family against one contract file" and the sentence
       describes C2A2 exactly — which is PREMISE-004's sharpened independence proviso and
       PREMISE-058's reduced-effective-N result arriving from the software-reliability side.
       [SNIPPET LEVEL with strong corroboration — the paper PDF was located at two independent
       hosts (KTH course pages; sunnyday.mit.edu, Leveson's own site, which also hosts the authors'
       "A Reply to the Criticisms of the Knight & Leveson Experiment"). The experimental design and
       the z ~= 100 / p < 1e-9 figure were read from retrieved text; the paper was NOT read in
       full. NOTE, and it matters: this experiment was contested for decades and the authors
       published a formal reply to criticisms; the finding stands in the field but is not
       uncontroversial, and anyone relying on it should read the reply. ALREADY REGISTER-CITED via
       PREMISE-045 and PREMISE-096.]
    4. Ford, D., Labelle, F., Popovici, F., Stokely, M., Truong, V.-A., Barroso, L., Grimes, C. &
       Quinlan, S. (2010), "Availability in Globally Distributed Storage Systems," Proceedings of
       the 9th USENIX Symposium on Operating Systems Design and Implementation (OSDI '10). — **The
       operational-scale confirmation of clause (iv), from a year-long study of a real fleet.** The
       paper applies a clustering heuristic to group failures occurring almost simultaneously and
       finds that a large fraction of failures happen in BURSTS, with most large bursts associated
       with rack- or multirack-level events — that is, with a shared physical or infrastructural
       coupling factor rather than with per-node causes. The methodological consequence is the one
       806 needs: reliability calculations for replicated and erasure-coded systems "depend
       critically on the assumption of independence," and where failures are correlated, those
       calculations are INFLATED — the error runs in the unsafe direction. Its clustering heuristic
       is also the concrete method 806's evidence calls for and no C2A2 artefact performs: group
       failures by time proximity FIRST, then look for the shared cause, rather than filing each by
       task. [SNIPPET LEVEL — the OSDI '10 proceedings record, the USENIX video listing and the
       ResearchGate/Semantic Scholar entries were located this run; the burst-clustering finding
       and the rack-level attribution were read from retrieved summaries. Full author list and
       venue confirmed. Paper NOT read.]
    5. Google SRE, "Data Processing Pipelines" (*Site Reliability Engineering*, O'Reilly 2016,
       ch. 25) — the catalogue of failure modes arising from PERIODICITY rather than from logic:
       uneven work distribution, THUNDERING HERD, moiré load patterns, and jobs whose runtime
       silently exceeds their period. — Supplies the mechanism most likely to be operating in the
       triple-booked slot: co-scheduled work contending for a shared resource is a named,
       catalogued pattern with named remedies (jitter, staggering, rate limiting). [CANONICAL,
       cited from established knowledge; carried forward from PRESUMPTION-797's file where it was
       likewise NOT re-verified. Do not cite the chapter's specific taxonomy onward without
       checking.]

  Strength of support: **Strong.** Clause (i) is experimentally falsified in the direction the item
  claims (Knight & Leveson, p < 1e-9) and confirmed at fleet scale (Ford et al.). Clauses (ii) and
  (iii) rest on a mature, standardised, internationally instrumented discipline with a verified
  primary reading. Clause (iv) follows from (iii) arithmetically. The only weak clause is the one
  the register does not already hold — the scaling question (R3) — which no located source
  addresses directly.

  Summary: The corrective proposition is strongly supported, and the striking feature of the
  literature is that it treats the independence assumption not as an approximation but as a known
  error with a name, a parameter, an international data-collection programme and a place in every
  functional-safety standard. Knight and Leveson tested it directly under conditions designed to
  maximise independence and found coincident failures at z ~= 100 — with an explanation (shared
  specification, shared training, shared reference materials) that transfers to a fleet of
  same-family agents reading one contract file more cleanly than it transfers to most of the
  systems it is usually applied to. Ford et al. confirm at fleet scale that failures arrive in
  bursts attributable to shared infrastructure, and that independence-assuming availability
  calculations are inflated. Rausand and Lundteigen supply the analytical vocabulary the item most
  needs and C2A2 entirely lacks: the separation of ROOT CAUSE from COUPLING FACTOR, and a
  coupling-factor checklist — same environment, same interface, same physical location, same
  procedures — every entry of which C2A2's runs satisfy. And the beta-factor model turns 806's
  qualitative worry into a bound: because the common-cause term of a redundant group's failure
  probability is independent of the voting arrangement, independent failures fall quadratically
  with redundancy while common-cause failures do not fall at all, so the total benefit available
  from ANY redundancy is capped at roughly 1/beta. Against published beta values of 0.03-0.22, the
  cap would be a factor of five to thirty; against what three-of-three co-failure in one slot
  implies, the cap is one. That is the item's claim that "adding another monitor adds no
  independent evidence," derived rather than asserted. Where this file must stop short of the item
  is on its own strongest move: the register already holds this, at High confidence, as PREMISE-141
  clause (2), minted ten days ago from the same signature.

  Caveats:
    (a) THIS IS SUBSTANTIALLY PREMISE-141 AGAIN AND THAT SHOULD DRIVE THE DISPOSITION. See the
        DUPLICATION WARNING. The correct reading of 806 is not "a new finding" but "the second
        instance of a finding validated ten days ago, on which nothing has changed." PREMISE-141's
        own SYSTEMIC-RISK note anticipated exactly this: it declined to mint a duplicate invariant
        and recorded instead that "the flag therefore records an ENFORCEMENT gap, not a knowledge
        gap." 806 is the enforcement gap producing its predicted output. Under PREMISE-135
        (terminality is not purchased by accumulating instances) and PREMISE-151 (repeated
        disclosure of an unremediated condition normalises rather than resolves it, and the
        disclosure record is evidence of INCUBATION), a second recording is itself the thing to
        worry about.
    (b) PREMISE-141'S SCOPE LIMIT TRANSFERS AND IS LOAD-BEARING. "THE CAUSE OF `[Request
        interrupted by user]` IS UNDETERMINED... this premise licenses no claim that the
        interruptions were faults rather than deliberate human stops." 806 cites the same signature
        and inherits the same limit exactly. If those stops were human-initiated, the correlation
        is real but its cause is a person's attention, not a resource gate — which changes the
        remedy completely and makes staggering the schedule useless. 806's own confidence line is
        honest about this ("Moderate confidence — the transcripts show the signature but not the
        gate") and the honesty must survive into any disposition.
    (c) THE BETA ARITHMETIC IS AN ILLUSTRATION, NOT AN ESTIMATE. One slot, three runs, one day.
        Beta is estimated in the reliability literature from populations over years, through the
        ICDE data exchange or through structured checklists (Humphreys; IEC 61508 Annex D's 37
        questions), and even then the checklists are criticised in source 1 for ambiguous questions
        and unexplained scores. An implied beta from n=1 event is a number to think with, not a
        number to report. The 4.5% figure is worse — it is computed on a post-hoc-selected group
        and is not a test at all, which is stated in the arithmetic block rather than buried here.
    (d) THE SCALING CLAIM (R3) IS THE ITEM'S ONLY NOVEL CLAUSE AND IT IS THE LEAST SUPPORTED.
        "Whether that fraction is stable or grows with the schedule's density" is a question about
        how beta behaves as co-scheduling increases, and nothing located this run addresses it. The
        SRE contention literature makes it plausible (more co-scheduled work, more contention, more
        shared-resource coupling) but plausible is not supported. If a disposition wants a
        forward-looking claim, this is the clause that needs its own search and does not yet have
        one.
    (e) THE DOMAIN TRANSFER FROM NUCLEAR PRA IS IMPERFECT IN A SPECIFIC WAY. The beta-factor model
        assumes a defined common-cause component group of nominally identical channels with
        estimable rates, proof-test intervals, and a demand model. C2A2 has heterogeneous agents on
        a scheduler with no proof tests and no rate estimates. What transfers robustly is the
        CONCEPTUAL apparatus — root cause versus coupling factor, the coupling-factor checklist,
        defence by separation and diversity — and the QUALITATIVE ceiling result, which is
        distribution-free (a term that does not fall with redundancy caps the benefit of
        redundancy). What does not transfer is any numeric PFD.
    (f) DIVERSITY AS A DEFENCE HAS A DOCUMENTED COST AND SOURCE 1 SAYS SO. Its critique of IEC
        61508's checklist notes that "diversity is given high credit, but in some sectors it is not
        a desired strategy due to e.g. complexity and possibility of human errors during
        maintenance." For C2A2 the obvious diversity move — a monitor on a different model family
        or outside the sandbox — is exactly what PREMISE-096 and PREMISE-110 already require and
        what PREMISE-141 filed for Tom as a code change. Adding a same-family monitor is not
        diversity and, per PREMISE-004's sharpened proviso, counts as one channel.

  Search scope: COMPREHENSIVE and VERIFIED on common-cause failure theory, the root-cause/coupling-
  factor decomposition, the beta-factor model and its defence strategies (source 1 read in full).
  GOOD on the quantitative beta ranges, at secondary level with the primary located. GOOD on the
  experimental falsification of independence (Knight & Leveson, with the existence of a sustained
  critical literature disclosed). GOOD on fleet-scale correlated failure (Ford et al., at summary
  level). NOT SEARCHED, and each would materially change this: (i) THE SCALING RELATIONSHIP —
  how correlated-failure fraction behaves as co-scheduling density rises — which is residual (R3),
  is the item's declared type, and is the only clause here that the register does not already hold;
  (ii) the multi-agent-LLM failure taxonomy (Cemri et al. 2025, MAST, arXiv:2503.13657), already
  cited in PREMISE-141 and the closest available base rate for C2A2's own system class, which was
  deliberately not re-searched to avoid re-minting but WOULD be the right source for a beta estimate
  in this domain; (iii) statistical tests for failure clustering (the burst-detection and
  clustering-heuristic methodology behind Ford et al.), which is the rigorous version of what 806
  did by eye and would replace the invalid 4.5% with something defensible.

  Recommendation: **SUPPORTED (Strong)** for the corrective proposition; equivalently
  NO-SUPPORT-FOUND for the presumption as worded. **But the disposition should almost certainly be
  a RE-CONFIRMATION of PREMISE-141 rather than a new premise.** Four carries:
    1. NO NEW PREMISE. PREMISE-141 clause (2) already holds this at High confidence and is due for
       re-check on 2026-09-05. This file is that re-check's evidence, arriving three weeks early
       with a second instance. Minting again is barred by PREMISE-138(1) and PREMISE-135, and per
       PREMISE-151 the second recording is better read as incubation than as confirmation.
    2. THE COUPLING FACTOR IS THE NEW CONTENT AND IT IS CHEAP TO TEST (R1). The 08:00 triple-booking
       is a static fact readable from the schedule file, and staggering the slot is a one-line
       change with an immediately observable result. Per PREMISE-107's scope guard, this is exactly
       the case where applying the remedy IS the discriminating test and is faster than designing
       one: the remedy is cheap, reversible and immediately observable. If failures decorrelate
       after staggering, the coupling factor was contention; if they do not, it was not, and
       Caveat (b)'s human-stop hypothesis rises.
    3. THE REDUNDANCY CEILING IS THE QUOTABLE RESULT (R2). Because the common-cause term does not
       fall with voting, the benefit of any redundancy is capped at ~1/beta. This turns "the fleet's
       redundancy is nominal" from a rhetorical claim into a bound, and it gives PRESUMPTION-799 —
       the watchdog-regress item it couples to — its arithmetic: a second monitor in the same
       failure domain does not add a second chance, and no number of them will.
    4. THE ANALYTICAL MOVE THE FLEET DOES NOT MAKE IS ONE LINE OF DISCIPLINE. Ford et al.'s method
       and Rausand's decomposition agree: GROUP FAILURES BY TIME AND SIGNATURE FIRST, THEN LOOK FOR
       THE SHARED CAUSE — rather than filing each by task, which is what 806 observes "no run does."
       That is a change to how the daily health report is written, not a new instrument, and it is
       the step that would have surfaced this on 2026-08-04 instead of 2026-08-14.
