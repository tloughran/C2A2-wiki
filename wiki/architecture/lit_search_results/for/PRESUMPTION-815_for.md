SEARCH-FOR-PRESUMPTION-815:
  Date searched: 2026-08-16
  Original item: PRESUMPTION-815
  Original statement: [inferred] That two counts of one population disagreeing is a defect requiring
    arbitration, rather than two undefined measurands both correct.
  Risk if wrong: Medium
  NOTE CARRIED FROM 14b — PARTIALLY RESOLVED SAME DAY: the queue-counter instance was settled hours
    earlier ("both count LINES, and they count DIFFERENT lines"). This item is queued for the
    GENERALISATION only: the premise-register, review-queue and census-versus-sample disputes, all
    still pursued as arbitration.
  Search question (as queued): Measurand definition and construct validity; VIM/GUM metrology on the
    measurand; operational definitions and counting rules in official statistics.

  POLARITY NOTE — WHAT WAS ACTUALLY SEARCHED FOR. The item is worded as the DEFECTIVE belief. The
  proposition searched FOR is the CORRECTIVE CONVERSE, in four clauses:
    (C1) A MEASUREMENT RESULT IS UNINTERPRETABLE UNTIL ITS MEASURAND IS SPECIFIED, and the standards
         make the specification a formal requirement with named contents, not a nicety.
    (C2) DISAGREEMENT BETWEEN TWO RESULTS IS, IN THE STANDARD ITSELF, THE TEST FOR WHETHER THEY REFER TO
         THE SAME MEASURAND — so "they disagree" is not the start of an arbitration, it is the trigger
         for asking what each one measures.
    (C3) THERE IS A FLOOR BELOW WHICH NO AMOUNT OF CARE HELPS: definitional uncertainty is a component
         of measurement uncertainty, set by the finite detail in the definition, and it bounds every
         reading. An undefined measurand therefore has UNBOUNDED definitional uncertainty and its
         readings are not merely imprecise but formally incomparable.
    (C4) OFFICIAL-STATISTICS PRACTICE OPERATES THIS WAY BY CONSTRUCTION: two counting rules over one
         nominal population produce two series that are each internally valid and mutually
         non-comparable, and the discipline's response is to publish the definition and the
         comparability boundary — never to adjudicate a winner.
  "SUPPORTED" below means 14b's diagnosis is well grounded, and is equivalently evidence AGAINST the
  presumption as worded.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-815
    Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: the arbitration framing was
      never stated as a choice and so was never examined)
    Transform at each step:
      14b: Examined what the two diverging series actually count and found neither defined.
      15a: Searched for supporting literature on the corrective proposition; register check first.
    Current status: SUPPORTED — BUT SEE THE DUPLICATION WARNING

  **DUPLICATION WARNING — READ BEFORE DISPOSITION.** The register check found that PRESUMPTION-815's
  core claim and its remedy are held THREE TIMES OVER, once at High confidence:
    - **PREMISE-101** (2026-07-19, High): "Counts over shared artifacts are properties of a reading — a
      (scope, method, time) tuple — not properties of the artifact; absent a designated counting
      authority and a recorded method, **independent agents will produce divergent counts of the same
      object WITHOUT EITHER BEING WRONG.**" That final clause is PRESUMPTION-815, verbatim in substance,
      twenty-eight days earlier.
    - **PREMISE-114** (2026-07-21, Moderate) supplies the remedy the item implies, as its load-bearing
      "THE EXIT": "**write the counting definition first (including every exclusion rule), designate it
      the reference, and re-derive all readings against it; convergence is the expected outcome and
      arbitration is not needed.**"
    - **PREMISE-161** (2026-08-14, Moderate — TWO DAYS BEFORE THIS FILE) minted the recording obligation
      for unarbitrated disagreement, and its own 15b line records that JCGM VIM3/GUM measurand semantics
      and definitional uncertainty were **verified in that run**, with `df`/`du` and AWS SQS
      `Approximate*` metrics offered as direct counterexamples of instruments that "measure DIFFERENT
      THINGS by construction."
  A disposition that mints a new premise here would be minting PREMISE-101 a fourth time, which
  PREMISE-138(1) and PREMISE-135 bar. This file proceeds because the queue asked for the search and
  because there is one narrow, genuine and load-bearing residual, identified as (R1) below.

  REGISTER CHECK (performed BEFORE writing this file):
    Grepped `validated_premises.md` for: measurand, operational definition, operationalis/z, construct
    validity, counting rule, what is counted, two counts, disagree, reconcil, arbitrat, census,
    definitional, VIM, GUM, metrolog, denominator, sample.
    Found and read in full:
      - **PREMISE-101** (2026-07-19, ACTIVE, High) — see DUPLICATION WARNING. Applicable-to already
        names "every agent report that states a quantity over a shared artifact."
      - **PREMISE-114** (2026-07-21, ACTIVE, Moderate) — incommensurability absent external calibration;
        Bland-Altman limits of agreement rather than a winner; latent-class methods need conditional
        independence that same-codebase counters lack; and THE EXIT quoted above. **SCOPE LIMIT (b) is
        the hinge for this item and is quoted in full under (R1).**
      - **PREMISE-161** (2026-08-14, ACTIVE, Moderate) — the RECORDING obligation for an unarbitrated
        disagreement, plus ISO 14253-1 guard-band rule. Its own scope limit states it "carves out only
        the two things 114 does not hold."
      - **PREMISE-105** (2026-07-20, ACTIVE) — a change in the definition of what is counted makes
        adjacent periods NON-COMPARABLE (a break in the series), and a delta spanning the change is
        uninterpretable. The temporal form of the same result; also carries the Eurostat backcasting
        preference for correction over marking.
      - **PREMISE-117** (2026-07-21, ACTIVE, Moderate-High) — publish-then-revise under an unresolved
        definitional dispute is codified practice; **the defect is silence, not continuation**; quarantine
        excluded. This is the discipline's answer to what to do WHILE the measurand is being written.
      - **PREMISE-168** (2026-08-15, ACTIVE, Moderate) — a yield figure without its denominator is a
        statement about the producer; the DENOMINATOR IS ITSELF A CHOSEN FRAME whose provenance must be
        stated. Directly bears on the census-versus-sample dispute named in 14b's note.
      - **PREMISE-136** (ACTIVE) — the achievable denominator of a settling quantity is fixed by its
        DECLARED SCOPE; every settling quantity must declare its scope (run / cohort / corpus) at the
        point it is written.
      - **PREMISE-113** (ACTIVE) — a detector's findings are evidence about the detector until its
        precision is measured; the instrument-versus-object distinction in the detector setting.
      - **PREMISE-120** (ACTIVE) — reproducing is not confirming; a second implementation written from
        the same specification SHARES the specification. Relevant because two counters written from one
        vague spec are not two measurements.
    CONCLUSION OF THE CHECK: **NEAR-TOTAL OVERLAP; THE CLAIM IS HELD AT HIGH CONFIDENCE AND ITS REMEDY
    IS HELD SEPARATELY. NO NOVELTY-FLAG.** Nine ACTIVE premises bear on this. The genuine residual is
    one thing, and it is the reason this file was worth writing:
      (R1) **PREMISE-114'S EXIT DOES NOT COVER THE THREE DISPUTES 14b QUEUED, BY ITS OWN SCOPE LIMIT.**
           114's binding scope limit (b) reads: "**114's definitional exit is conditioned on a quantity
           DETERMINISTIC OVER A FROZEN SNAPSHOT; a live growing database is not, so four differing DB
           sizings may ALL be correct and forcing them to one definition would destroy information.**"
           The queue-counter instance that was settled hours earlier WAS deterministic over a snapshot,
           which is why it settled. The three still-open disputes are not: the premise-register is
           appended to continuously, the review queue drains and fills, and census-versus-sample is a
           difference of SAMPLING FRAME rather than of counting rule — a case 114 does not address at
           all. **So the register holds the diagnosis and holds a remedy that does not reach the cases
           14b actually queued.** That gap is real, it is narrow, and it is the only thing here that is
           not a restatement.
    DECLARED LIMITATION: string grep, measured at ~56% recall (ASSUMPTION-1052). The list above is a
    **LOWER BOUND**; with nine hits the true overlap is likely larger, which argues for the narrowest
    possible disposition.

  Supporting evidence found: Yes

  Sources:
    1. JCGM 200:2012, *International Vocabulary of Metrology* (VIM3), entry **2.47 metrological
       compatibility of measurement results**. — **The direct support for clause (C2), and the single
       most useful sentence located this run.** NOTE 1 reads: "Metrological compatibility of measurement
       results replaces the traditional concept of 'staying within the error', as it **represents the
       criterion for deciding whether two measurement results refer to the same measurand or not**." The
       definition itself is scoped "for a *specified* measurand" — compatibility is not even defined
       until the measurand is written. This is exactly the inversion 815 asks for: disagreement is not
       the beginning of an adjudication, it is the diagnostic that answers "are these the same
       quantity?"
       **HONESTY CORRECTION, MATERIAL, AND IT NARROWS THE SUPPORT.** A secondary summary retrieved
       earlier in this search paraphrased NOTE 1 as offering "two possibilities — one being that they
       are actually measuring different measurands." **THE VERIFIED PRIMARY TEXT DOES NOT SAY THAT.**
       The alternatives NOTE 1 enumerates are only: "either the measurement was not correct (e.g. its
       measurement uncertainty was assessed as being too small) **or the measured quantity changed
       between measurements**." The "different measurands" conclusion is licensed by the CRITERION
       clause and by entry 2.3, not stated as an option in NOTE 1. The paraphrase overstated the
       standard and is not used. NOTE 2 adds a caution that bears on C2A2 directly: **correlation
       between the measurements influences compatibility**, so two counters sharing a codebase are not
       two independent readings for this purpose either.
       [VERIFIED this run — https://jcgm.bipm.org/vim/en/2.47.html fetched and read in full, including
       both notes and the informative annotation. Every quotation above is read directly.]
    2. JCGM 200:2012 (VIM3), entry **2.3 measurand** — "quantity intended to be measured." — **The
       direct support for clause (C1).** NOTE 1 makes specification a formal requirement with named
       contents: "**The specification of a measurand requires knowledge of the kind of quantity,
       description of the state of the phenomenon, body, or substance carrying the quantity, including
       any relevant component**." NOTE 3 and the steel-rod example add the point 815 needs most: the
       measuring act and its conditions may make **"the quantity being measured differ from the measurand
       as defined,"** and the remedy is a stated correction, not a preference between readings. The
       informative annotation states it flatly: "**The quantity that is being measured may not actually
       be the quantity that is intended to be measured.**" Applied to 815, "the number of items in the
       review queue" names no kind of quantity, no state, and no inclusion rule — it is not a measurand
       specification at all, so nothing in the standard's apparatus even applies yet.
       [VERIFIED this run — https://jcgm.bipm.org/vim/en/2.3.html fetched and read in full.]
    3. JCGM 200:2012 (VIM3), entries **2.26 measurement uncertainty** and **2.27 definitional
       uncertainty**. — **The support for clause (C3), and the reason this is a floor rather than a
       nicety.** 2.26 NOTE 1 states that measurement uncertainty "includes components arising from
       systematic effects ... **as well as the definitional uncertainty**" — so the vagueness of the
       definition is not outside the error budget, it is inside it. 2.27's own content, as reported in
       retrieved summaries, is that definitional uncertainty is "the practical minimum measurement
       uncertainty achievable in any measurement of a given measurand," that it "sets a minimum limit to
       any measurement uncertainty," that "even the most refined measurement cannot reduce the interval
       to a single value because of the finite amount of detail in the definition of a measurand," and
       that "any change in the descriptive detail leads to another definitional uncertainty." The
       corollary for 815 is sharp: **improving the counters cannot close a gap that is definitional**,
       so effort spent arbitrating is spent below the floor.
       [MIXED. Entry **2.26 is VERIFIED this run** — fetched and read in full, and NOTE 1's inclusion of
       definitional uncertainty is quoted directly from it. Entry **2.27 is SNIPPET LEVEL** — its
       wording is reported from retrieved search summaries; the page itself was NOT read in this file's
       session (a fetch attempt returned a session-level deduplication notice rather than content, so
       the text was not obtained). Do not quote 2.27 verbatim onward without opening it. NOTE ALSO:
       PREMISE-161's 15b line records VIM3/GUM measurand semantics and definitional uncertainty as
       "verified this run" on 2026-08-14, so a verified reading exists in the vault two days old — but
       it is in the AGAINST directory, which this agent is barred from reading, and is named here only
       from PREMISE-161's own summary line in `validated_premises.md`.]
    4. Deming, W.E. — operational definitions; the position that there is no true value of a quantity
       defined by a procedure, and that a definition without an operational statement of how to observe
       it communicates nothing. — **The philosophical form of clauses (C1) and (C4), and the frame that
       makes "two undefined measurands both correct" intelligible rather than paradoxical.** On this
       view a count is not a fact about a population but the output of a stated procedure applied to a
       stated frame, so two procedures give two facts, and asking which is right is a category error
       until a third thing — the definition — is written.
       [CANONICAL — cited from established knowledge, NOT re-verified this run. **Already
       register-cited** in PREMISE-161's supporting-evidence line ("Deming (no true value of a quantity
       defined by a procedure)"), so this adds no independent weight and must not be counted as a second
       source.]
    5. ILO / ICLS labour-statistics practice on unemployment, and the associated national-versus-
       international comparability literature (ILOSTAT topic pages; ILO measurement guidance; ONS
       "Unemployment and the Claimant Count"; BLS, "International unemployment rates: how comparable are
       they?"). — **The support for clause (C4), and the best available demonstration that "two counts,
       both correct, not comparable" is a routine operating condition of a mature discipline rather than
       a pathology.** The ILO's operational definition rests on three explicit criteria (not employed;
       active search; current availability) with the search and availability windows fixed by regulation
       to specific week-counts — i.e. the definition is written down to the level of exclusion rules,
       which is precisely what 14b found absent. The comparability consequence is stated plainly in the
       practice: work statistics for countries not using the same standards **are not comparable**, and
       ILOSTAT keeps series separated by standard (13th vs 19th ICLS) so that each "contains only data
       comparable within and across countries." The worked contrast is the one 815 needs: a national
       claimant count includes only persons registered at a government labour office, while the ILO
       definition includes persons seeking work by other means — **two counts of "the unemployed,"
       neither wrong, differing by inclusion rule, and the discipline's response is to publish both with
       their definitions and never to arbitrate.** The ONS maintains exactly this pair as a standing,
       documented, permanent discrepancy.
       [SNIPPET LEVEL — the ILOSTAT topic page, ILO measurement-guidance PDFs, the ONS claimant-count
       methodology PDF and the BLS Monthly Labor Review article were LOCATED this run and read at
       retrieved-summary level; **none was opened and read in full.** The three ILO criteria, the
       EU Regulation 1897/2000 window, the ICLS-series separation and the claimant-count contrast are
       reported as retrieved. Titles, issuing bodies and identifiers are confirmed; do not quote a page.]
    6. Construct validity, and the operationalisation gap between a construct and its indicator
       (Cronbach & Meehl 1955; the standard psychometric treatment). — Named because the queued search
       question asked for it. It supplies the discipline in which "the two counts measure different
       things" is the DEFAULT hypothesis rather than the exotic one.
       [CANONICAL — cited from established knowledge, NOT re-verified this run. **No construct-validity
       source was retrieved in this search**; this is a pointer, not a finding, and is graded
       accordingly.]

  Strength of support: **Strong** on (C1), (C2) and (C4); **Moderate-to-Strong** on (C3).
    (C1) and (C2) rest on a verified reading of the primary international standard, where the relevant
    text is definitional rather than empirical and therefore not subject to replication doubt. (C4) is
    demonstrated by a large, mature, instrumented practice that maintains permanent definitional
    discrepancies as a matter of policy. (C3) is downgraded one grade only because entry 2.27's exact
    wording is second-hand in this file, though 2.26's inclusion of definitional uncertainty in the
    uncertainty budget is verified.

  Summary: The corrective proposition is strongly supported, and the metrological standard states it
  more sharply than the item does. Under VIM3, a measurement result is not interpretable until its
  measurand is specified, and specification is a formal requirement with named contents: the kind of
  quantity, the state of the thing carrying it, and every relevant component. "The number of items in
  the review queue" satisfies none of these, so it is not a measurand specification and the machinery
  of comparison does not yet apply to it. More decisively, the standard makes disagreement itself the
  DIAGNOSTIC: metrological compatibility "represents the criterion for deciding whether two measurement
  results refer to the same measurand or not." That is the inversion 815 identifies — two divergent
  counts are the evidence that answers "same quantity?", not a defect awaiting a judge. Definitional
  uncertainty is a component of the uncertainty budget and sets a floor below which no refinement of
  the instruments can go, so effort spent arbitrating between two undefined counters is spent beneath
  the floor and cannot succeed. Official statistics operates on exactly this basis: the ILO writes its
  unemployment definition down to the number of weeks in the search window, keeps series separated by
  which standard produced them, and maintains the claimant-count-versus-ILO discrepancy as a permanent
  documented pair — two counts of one nominal population, neither wrong, never arbitrated. Where this
  file must stop short of the item is that the register already holds the diagnosis at High confidence
  as PREMISE-101, whose text ends "without either being wrong," and holds a definitional remedy as
  PREMISE-114. What it does not hold — and this is the residual worth carrying — is a remedy that
  reaches the three disputes 14b actually queued, because PREMISE-114's exit is expressly conditioned on
  a quantity deterministic over a frozen snapshot and none of the three is.

  Caveats:
    (a) THIS IS SUBSTANTIALLY PREMISE-101 AGAIN AND THAT SHOULD DRIVE THE DISPOSITION. See the
        DUPLICATION WARNING. Per PREMISE-151, a second (here fourth) recording of an unremediated
        condition is evidence of incubation, not confirmation.
    (b) THE ITEM'S FRAMING CAN BE OVER-READ INTO A LICENCE FOR PERMANENT NON-DECISION, AND PREMISE-117
        FORBIDS THAT. "Both correct" does not mean "no figure may be used." The official-statistics
        answer is publish-then-revise with a break flag and a documented account of the change; **the
        defect is silence, not continuation**. Any disposition that converts 815 into a reason to
        suspend dependent work reproduces the quarantine failure mode PREMISE-117 explicitly excludes,
        in a channel already known to have near-zero decision throughput.
    (c) NOT EVERY DISAGREEMENT IS DEFINITIONAL, AND ASSUMING SO IS THE SYMMETRIC ERROR. VIM3 NOTE 1's
        enumerated alternatives are that the measurement was incorrect, or that the quantity CHANGED
        BETWEEN MEASUREMENTS. The second is live here: PREMISE-161 already carries a cross-item lead
        asking whether the disputed readings were taken at different times of day, in which case the
        disagreement is TEMPORAL and the remedy is PREMISE-165's as-of stamp, not a definition. **A rule
        that reads every divergence as definitional would mask real drift, and 815's generalisation is
        exactly the move most likely to produce that error.**
    (d) THE CENSUS-VERSUS-SAMPLE DISPUTE IS A DIFFERENT ANIMAL AND THIS FILE'S SOURCES ONLY PARTLY REACH
        IT. A census and a sample of one frame differ in SAMPLING DESIGN, not in counting rule; the
        sample carries sampling error that the census does not, and the correct apparatus is a
        confidence interval and a frame definition (PREMISE-136, PREMISE-168), not a measurand
        rewrite. Folding it into "two measurands" would lose the estimator's uncertainty. It is the
        weakest of the three queued disputes for this item's frame.
    (e) DOMAIN TRANSFER FROM PHYSICAL METROLOGY IS IMPERFECT IN A SPECIFIC WAY. VIM's apparatus assumes
        a quantity with a unit and a traceability chain to an external reference. Counts of vault
        artefacts have neither; there is no SI base unit for "premise" and no external standard to
        which a counting method could be traced. What transfers robustly is the CONCEPTUAL requirement —
        specify the measurand, and read disagreement as a compatibility test — which is
        distribution-free and reference-free. What does not transfer is any uncertainty arithmetic:
        do not compute a coverage interval on a premise count using GUM machinery.
    (f) SOURCE INDEPENDENCE IS LOWER THAN THE SOURCE COUNT SUGGESTS. Sources 1-3 are three entries of
        ONE document. Source 4 is already cited by PREMISE-161. Source 6 was not retrieved. The
        genuinely independent external evidence in this file is the standard plus the ILO practice —
        two lines, not six. Per PREMISE-120's vocabulary this must be recorded rather than glossed.

  Search scope: COMPREHENSIVE and VERIFIED on the metrological core (VIM3 entries 2.3, 2.26 and 2.47
    fetched and read in full). GOOD at snippet level on definitional uncertainty (2.27) and on official-
    statistics counting practice (ILO/ICLS, ONS claimant count, BLS comparability). NOT SEARCHED, and
    each would materially change this file: (i) **GUM (JCGM 100:2008) clause 3.1.3 and Annex D on the
    definition of the measurand and on "the result of a measurement after correction"**, which is the
    companion document and was identified but NOT retrieved — it is where the formal treatment of
    incomplete measurand definition lives; (ii) **CONSTRUCT VALIDITY proper**, which the queue asked for
    and which this search did not reach at all — a clearly-labelled negative result, and the gap most
    relevant to the premise-register dispute, since "what counts as a premise" is a construct question
    before it is a counting question; (iii) **survey-methodology treatment of frame versus population**
    (Groves et al., total survey error), which is the right apparatus for the census-versus-sample
    dispute in caveat (d) and was not searched.

  Recommendation: **SUPPORTED (Strong)** for the corrective proposition; equivalently NO-SUPPORT-FOUND
  for the presumption as worded. **But the disposition should be a SCOPE-EXTENSION OF PREMISE-114
  rather than a new premise.** Four carries:
    1. NO NEW PREMISE. PREMISE-101 holds the claim at High confidence with the words "without either
       being wrong." Minting again is barred by PREMISE-138(1) and PREMISE-135.
    2. THE RESIDUAL IS (R1) AND IT IS A REAL HOLE. PREMISE-114's exit is conditioned on a quantity
       deterministic over a frozen snapshot; the premise-register, the review queue and the
       census-versus-sample pair are none of them that. The register therefore holds a diagnosis with a
       remedy that does not reach the three cases 14b queued. Extending 114 to non-deterministic
       quantities — where the correct move is to write the measurand AND an as-of stamp, per
       PREMISE-165 — is the smallest change that closes it.
    3. THE ONE-LINE OPERATIONAL RULE IS AVAILABLE AND CHEAP. Before any two figures are compared,
       each must carry its inclusion rule and its as-of time. This is PREMISE-136's declared-scope
       requirement plus PREMISE-165's stamp, applied at the point of writing rather than at the point of
       dispute, and it dissolves the arbitration framing without needing anyone to adjudicate anything.
    4. THE STANDARD'S OWN CAUTION SHOULD TRAVEL WITH ANY ADOPTION (caveat c). Not every divergence is
       definitional. VIM3 NOTE 1 names "the quantity changed between measurements" as an alternative,
       and PREMISE-161 already carries an open lead that this may be the actual explanation in at least
       one disputed pair. A generalisation that assumed otherwise would install a rule that hides drift.
