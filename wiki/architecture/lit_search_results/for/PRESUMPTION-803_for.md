SEARCH-FOR-PRESUMPTION-803:
  Date searched: 2026-08-15
  Original item: PRESUMPTION-803
  Original statement: [inferred] That output volume measures coverage — that eight proposals filed is a fact about how much of the tradition space was surveyed. The rollup reports the eight as the day's yield without a denominator, and the denominator is the thing that changed: two of the day's scheduled traditions produced nothing, so the eight represent four traditions out of a set the architecture treats as fifteen. The same shape appears in the corpus work: "Read-verified by hand on 11 of the 20, grep-only on the other 9", "verification at the body rather than sweeping", "107 stale transcript halves" of which four were sampled — each an honest statement of partial coverage, none aggregated anywhere into a coverage figure. The fleet counts what it produced and infers what it covered.

  POLARITY NOTE — what was searched FOR. The presumption is worded as the DEFECTIVE belief ("volume measures coverage"). The proposition searched FOR is the CORRECTIVE CONVERSE, in four clauses: (i) that PRODUCTION VOLUME AND COVERAGE ARE DISTINCT QUANTITIES with distinct denominators, and that the first is not an estimator of the second; (ii) that a count of discoveries made by an automated process bounds THE PROCESS, not the space searched — the streetlight effect, formalised; (iii) that where the SAMPLING FRAME is the set of units that happened to produce output, the resulting figure is selected on the dependent variable and describes the frame rather than the population; and (iv) that partial-coverage statements which are each locally honest do not, by aggregation or by absence of aggregation, license a coverage claim. "SUPPORTED" below means 14b's worry is well grounded, and is equivalently evidence AGAINST the presumption as worded.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-803
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by seeking the denominator behind each of the day's headline output figures
           and finding none stated.
      15a: Searched for supporting literature on the corrective proposition.
    Current status: SUPPORTED

  REGISTER CHECK (performed BEFORE writing this file):
    Grepped `validated_premises.md` for: coverage, denominator, selection bias, survivorship,
    convenience sampl, streetlight, volume, sampling frame, scope.
    Found and read in full:
      - **PREMISE-105** (2026-07-??, ACTIVE) — already holds, in terms: "AN ARTIFACT-VOLUME COUNT
        IS NOT A MEASURE OF KNOWLEDGE-GRAPH HEALTH; it is a proxy subject to Goodhart's law." Also
        carries the narrowing that connectivity as a replacement metric is subject to the identical
        argument and is directly writable by the agents being measured. This is clause (i) of the
        corrective, already minted.
      - **PREMISE-124** (2026-07-23, ACTIVE) — any self-measurement of the pipeline's own
        completeness or accuracy must cite an external baseline or a seeded/independent
        denominator, or be reported as UNCALIBRATED. Clause (a) is directly on point: "A RAW DEFECT
        CATCH COUNT IS NOT AN ESTIMATE OF DEFECTS PRESENT without capture-recapture or fault
        seeding." Names a FORBIDDEN MOVE (reading a single favourable self-observation as evidence
        a safeguard works; WYSIATI / base-rate neglect).
      - **PREMISE-150** (2026-08-10, ACTIVE, High) — "A batch of defects that a detector failed to
        catch bounds THE DETECTOR'S COVERAGE, not merely that batch... the score is computed over
        what the detector can see." Operational consequence already recorded: "adequacy claims
        require SEEDED defects, not observed pass rates." This is clause (ii) for detectors, minted
        five days ago.
      - **PREMISE-140** (2026-08-02, ACTIVE, High) — a metric derived from one observation channel
        must be NAMED BY ITS CHANNEL, not by the thing the channel proxies for; and STREAK FRAMINGS
        ARE BARRED for channel-derived metrics because a streak "converts an accumulating
        absence-of-observation into an accumulating positive claim." Cites coverage error and unit
        error as standard total-survey-error classes. Records an unusual concession: 15a found NO
        literature supporting generalisation from a single channel.
      - **PREMISE-097** (2026-07-16, ACTIVE) — a report from a bounded observational vantage must
        DISCLOSE ITS SCOPE GAP rather than imply coverage it lacks; grounded on observability-scope
        / trace-coverage literature and the survivorship-bias canon (Wald).
      - **PREMISE-109** (2026-07-20, ACTIVE) — **THE MOST CONSEQUENTIAL ENTRY FOR THIS ITEM,
        BECAUSE IT BARS THE OBVIOUS REMEDY.** "A summarizing agent is a view over its own read set,
        not a view over the system... a summary can be individually faithful to every source it
        read and collectively false about the system it describes, and THIS IS THE DEFAULT PROPERTY
        of a layered reporting stack." Its INSTRUMENTATION CONSTRAINT is explicitly load-bearing:
        "the measure is CLAIMS-WITHOUT-EVIDENCE... NEVER A READ-SET COVERAGE PERCENTAGE. Coverage
        rises when a summarizer reads more marginal artifacts without reading the decisive one, is
        unbounded over a growing vault, and would read green during exactly the failure it was
        built to catch." Any disposition of 803 that says "compute and report a coverage figure"
        collides with this and must argue past it.
      - **PREMISE-136** (2026-07-31/08-01, ACTIVE) — the achievable denominator of a settling
        quantity is fixed by its DECLARED SCOPE; every settling quantity must declare run / cohort
        / corpus scope AT THE POINT IT IS WRITTEN so the achievable denominator is visible at
        drafting time rather than discovered at evaluation time.
      - **PREMISE-101** (counts are properties of a (scope, method, time) reading, not of the
        artefact), **PREMISE-096** (denominators verified by independent corroboration; no
        self-produced artefact certifies itself), **PREMISE-141** (omission is not crash; a
        two-valued run model cannot represent a run that started and emitted nothing — directly
        relevant, since "two scheduled traditions produced nothing" is exactly that third state),
        **PREMISE-058** (agreement scales with formational independence; correlated experts give a
        reduced EFFECTIVE N).
    CONCLUSION OF THE CHECK: **VERY HEAVY OVERLAP. NO NOVELTY-FLAG. The volume-is-not-coverage
    claim is, at the level of principle, ALREADY THE REGISTER'S SETTLED POSITION** — held five
    separate ways (105 volume/Goodhart, 124 catch-count/denominator, 150 detector coverage, 140
    channel naming, 097 scope-gap disclosure). A disposition that mints a sixth would be
    duplication. What genuinely survives, and what was searched:
      (R1) THE SAMPLING-FRAME CLAIM, WHICH IS THE ITEM'S REAL CONTENT AND IS NOT HELD ANYWHERE.
           Every register entry above concerns a MONITORING metric — a health count, a detector
           score, an autonomy streak. 803's risk statement points somewhere else entirely: "the
           network figures that define this project's central claim (636 PRS triplets, 103
           cross-connections) are volume counts, and if volume has been standing in for coverage
           then the connection density is a statement about WHICH AGENTS RAN, not about the
           traditions." That is a claim about the project's substantive output, not its
           instrumentation, and it is the specific mechanism — the sampling frame is the set of
           agents that ran, and whether an agent ran is not independent of what it would have
           produced — that no premise addresses.
      (R2) THE UNAGGREGATED-HONEST-PARTIAL PATTERN. "11 of 20 read-verified, grep-only on 9";
           "107 stale halves, four sampled." Each statement is locally exemplary and satisfies
           PREMISE-097's disclosure requirement individually. The item's observation is that
           satisfying 097 item-by-item produces no system-level coverage statement and may actively
           produce a false impression of thoroughness, because a reader who sees many careful
           partial disclosures infers care rather than gaps. Nothing in the register covers the
           AGGREGATION failure, as opposed to the per-report failure.
      (R3) THE REMEDY IS CONSTRAINED AND THE CONSTRAINT IS NOT OBVIOUS. PREMISE-109 has already
           examined and REJECTED "report a coverage percentage" as an instrument. So the residual
           is not "add a denominator" — the register has already ruled that specific fix unsound
           for read-set coverage. What the residual needs is a coverage instrument that survives
           109's objection, and this file does not find one.
    DECLARED LIMITATION: string grep, measured at five-of-nine recall by the 2026-08-14 15c run
    (ASSUMPTION-1052 — ~56%). The list above is a **LOWER BOUND**, and given how many entries this
    grep DID return, the true overlap is likely larger still. That direction of error matters here:
    it argues for a NARROWER disposition, not a broader one.

  Supporting evidence found: Yes

  Sources:
    1. Klees, G., Ruef, A., Cooper, B., Wei, S. & Hicks, M. (2018), "Evaluating Fuzz Testing,"
       Proceedings of the 25th ACM Conference on Computer and Communications Security (CCS 2018);
       arXiv:1808.09700. — **The best available formal demonstration of clause (ii), from the
       field that most resembles C2A2's tradition agents: many autonomous processes searching a
       space and reporting what they found.** The paper shows that the standard output count is not
       an estimator of the underlying quantity. Against ground truth established by patch analysis,
       ALL 57,142 "unique" crashing inputs identified by AFL's coverage-profile de-duplication in
       *cxxfilt* were addressed by **only 9 distinct patches** — an overcount of roughly four
       orders of magnitude. Stack-hash de-duplication performed better and still overcounted, with
       ~500 coverage-unique crashes collapsing to ~46 stack hashes, and carried ~16% false
       negatives where hashes from one bug were shared with another. The methodological conclusion
       is exactly 14b's: the count of things produced is a property of the producing process and
       its de-duplication heuristic, and without an independently established denominator it
       supports no claim about the space searched. [SNIPPET LEVEL, but with the key numbers read
       directly from retrieved text — arXiv and UCSD-hosted PDF located this run, the ground-truth
       methodology and the 57,142/9 and 500/46/16% figures read; full paper NOT read end to end.
       Author list and venue confirmed against the arXiv record.]
    2. Geddes, B. (1990), "How the Cases You Choose Affect the Answers You Get: Selection Bias in
       Comparative Politics," *Political Analysis* 2:131-150. — **The canonical statement of clause
       (iii), and the closest formal match to the specific defect 14b names.** The argument is that
       selecting cases on the dependent variable — studying revolutions to explain revolution —
       systematically biases conclusions, and that the taboo is widely known in the abstract and
       routinely violated in practice ("all graduate students learn in statistics courses that
       selection on the dependent variable is forbidden, but few remember why, or what the
       implications of violating this taboo are for their own work"). Transfer to C2A2 is direct
       and uncomfortable: the eight proposals were produced by the four traditions that produced
       proposals. Whether an agent ran, and whether a run that ran produced output, are not
       independent of what that agent would have found — a tradition with thin literature this week
       is more likely to emit nothing, so the traditions that report are systematically the ones
       with more to report. Any density figure computed over emitters is conditioned on emission.
       [VERIFIED at bibliographic level this run — journal, volume, page range and the core argument
       confirmed across the Cambridge Core PDF listing, the eScholarship record and Semantic
       Scholar. Paper NOT read in full; the argument is summarised from the retrieved abstract and
       from established knowledge of the piece. Domain caveat in Caveat (d).]
    3. Audit-sampling standards: ISA 530 (IAASB), *Audit Sampling*, in the IAASB Handbook. —
       **Supplies the professional-practice version of clauses (iii) and (iv), and it is stricter
       than the informal intuition.** The standard requires that the sample be selected so that
       every sampling unit in the population has a chance of selection, requires that deviations be
       ANALYSED FOR CAUSE and PROJECTED to the full population, and — decisively for this item —
       holds that the auditor CANNOT PROJECT THE RESULT OF BLOCK SAMPLING to the population.
       "Everything the running agents produced today" is a block: contiguous, self-selected, not
       drawn from a frame. Under the standard's own rule such a selection supports a statement
       about the items examined and no statement whatever about the population. Note also what the
       standard requires beyond a denominator — analysis of deviations FOR CAUSE — which is the
       part that would ask why Carroll and Arkani-Hamed produced nothing, rather than recording the
       zero. [SNIPPET LEVEL — multiple authoritative hostings of ISA 530 located this run (IFAC
       handbook PDF, IAASA Ireland, MIA); the projection and block-sampling clauses read from
       retrieved summary text, the standard itself NOT read end to end. Paragraph numbers are NOT
       cited because they were not verified; do not attribute a paragraph number onward.]
    4. Total Survey Error, and specifically the distinction between COVERAGE ERROR (the frame does
       not match the target population) and NONRESPONSE / UNIT ERROR (selected units yield nothing)
       — with Sen, I. et al. (2021), "Total Error and Variability Frameworks for Digital Trace
       Data," *Public Opinion Quarterly* (the TED-On framework) as the digital-trace extension. —
       Gives the item's phenomenon its proper taxonomy, and the taxonomy does real work: "two
       scheduled traditions produced nothing" is NONRESPONSE, and "the architecture treats the set
       as fifteen but four reported" combines nonresponse with a frame question. These are
       different errors with different remedies, and the fleet currently has one word ("yield") for
       both. TED-On's specific contribution is that digital-trace data inherits total-survey-error
       structure even though nobody sampled anything, which is the situation of an agent fleet.
       [ALREADY REGISTER-CITED — this is PREMISE-140's own supporting evidence, read there this run.
       The Sen et al. citation was recorded in PREMISE-140 as "cited by 15a; NOT independently
       verified"; that verification status is UNCHANGED and was not improved this run. Cited here to
       show the taxonomy is already in-house, NOT as new support.]
    5. The code-coverage / test-effectiveness distinction in software testing practice (Qt
       Software Insights, "Code Coverage vs. Test Coverage vs. Test Effectiveness"; BrowserStack
       and Codacy guides). — Weak but on-point corroboration of clause (i) from a third domain:
       code coverage measures which code was executed and does not evaluate whether the tests are
       effective; "a line can be covered without the important logic inside it ever being tested,"
       and "an impressive percentage can still leave error paths, edge cases, or decision branches
       untouched." Included because it makes the same distinction one level further down — even a
       PROPER coverage metric is not an effectiveness metric — which is the reason PREMISE-109
       rejects coverage percentages and is directly relevant to residual (R3). [SNIPPET LEVEL —
       vendor/craft material located this run. Weak grade, cited for the DISTINCTION only.]

  Strength of support: **Strong** on clauses (i), (ii) and (iv); **Moderate-Strong** on clause (iii),
  where the formal result is canonical but its transfer to an agent fleet is argued here rather than
  found.

  Summary: The corrective proposition is strongly supported across four independent literatures and
  — importantly for disposition — is already the register's settled position at the level of
  principle. Klees et al. give the sharpest formal demonstration in the closest domain: counting
  what an automated searcher produced overestimated the underlying quantity by four orders of
  magnitude, because the count measures the searcher and its de-duplication heuristic rather than
  the space. Geddes supplies the specific defect 14b names — selection on the dependent variable —
  and its transfer is direct: the eight proposals came from the four traditions that produced
  proposals, and emission is not independent of what there was to emit, so any density computed
  over emitters is conditioned on emission. ISA 530 gives the professional-practice rule and it is
  stricter than intuition: a block selection supports a statement about the items examined and no
  projection to the population at all, and the standard additionally requires that deviations be
  analysed FOR CAUSE — the step that would ask why two scheduled traditions produced nothing rather
  than recording the zero. Total-survey-error taxonomy separates the two errors the fleet currently
  collapses into one word: coverage error (the frame is not the population) and nonresponse (the
  selected unit yielded nothing). Where this file diverges from a straightforward SUPPORTED verdict
  is on the remedy: PREMISE-109 has already examined and explicitly REJECTED read-set coverage
  percentages as an instrument, on the ground that coverage rises when a summariser reads more
  marginal artefacts without reading the decisive one and "would read green during exactly the
  failure it was built to catch." The literature located here says the current figures are
  uninterpretable; it does not supply an instrument that survives 109's objection.

  Caveats:
    (a) THE PRINCIPLE IS ALREADY HELD FIVE WAYS AND THIS SHOULD CONSTRAIN THE DISPOSITION.
        PREMISE-105 (volume/Goodhart), PREMISE-124 (catch count is not defects present),
        PREMISE-150 (missed defects bound the detector), PREMISE-140 (name the metric by its
        channel; streaks barred), PREMISE-097 (disclose the scope gap). If a disposition mints
        "volume is not coverage," it is re-minting. The disjoint content is (R1) the sampling-frame
        argument applied to the project's SUBSTANTIVE network figures rather than to its monitoring
        metrics, and (R2) the failure of aggregation across locally-honest partial disclosures.
    (b) THE REMEDY IS BARRED BY THE REGISTER AND NO REPLACEMENT WAS FOUND. This is the biggest gap
        in the file. PREMISE-109's instrumentation constraint is load-bearing and was argued
        through 15b; "add a denominator and report coverage" cannot simply be re-proposed. Note
        also PREMISE-105's warning that a replacement metric is typically subject to the identical
        Goodhart argument and is directly writable by the agents being measured — which is true of
        any coverage figure the fleet computes about itself. What survives 109 is a per-claim
        discipline (does this figure name its denominator and its frame?) rather than a
        system-level coverage number, and that is a weaker remedy than the item implies.
    (c) THE FUZZING ANALOGY HAS A LIMIT THAT CUTS AGAINST THE ITEM. Klees et al.'s overcounting
        arises from DE-DUPLICATION failure — the same bug counted many times. C2A2's proposals are
        individually authored and reviewed, so the specific mechanism does not transfer; eight
        proposals are probably eight things. What transfers is the deeper point — that a
        producer-side count has no denominator and therefore no relation to the space — not the
        overcounting factor. Do not quote 57,142/9 as if it predicts a C2A2 inflation rate.
    (d) GEDDES IS COMPARATIVE POLITICS AND THE TRANSFER IS AN ARGUMENT, NOT A FINDING. The formal
        result concerns a researcher choosing cases. Here nobody chose; agents failed to run or ran
        and emitted nothing. That is closer to NONRESPONSE than to case selection, and nonresponse
        biases estimates only if missingness is related to the outcome (Rubin's MNAR condition,
        already register-held via PREMISE-124(b)). THE CONDITION IS PLAUSIBLE HERE AND IS
        UNMEASURED: a tradition with a thin literature week is more likely to emit nothing AND
        would have contributed fewer connections, which is precisely the correlation that makes the
        missingness non-ignorable. But "plausible and unmeasured" is the honest status. The
        discriminating check is cheap and is named in the recommendation.
    (e) PER PREMISE-141, "two scheduled traditions produced nothing" is itself an under-determined
        observation. Did those agents not run, run and find nothing, or run and die silently? The
        fleet's run model is two-valued and cannot say. The coverage question cannot be answered
        before that one is, because the three cases have different implications for the frame: a
        crashed agent is missing data, an agent that ran and honestly found nothing is an observed
        zero, and only the second is a legitimate denominator entry.
    (f) THE "FIFTEEN" IS ITSELF UNAUDITED. The item's arithmetic (four of fifteen) presumes the
        architecture's tradition set is the right population. PREMISE-101 applies: fifteen is a
        property of a reading. If the target population is "traditions with active literature this
        month" the denominator is different and possibly smaller. A denominator asserted without
        its own justification reproduces the defect one level up.

  Search scope: COMPREHENSIVE on the volume-versus-coverage distinction across four domains
  (automated vulnerability discovery, comparative-politics methodology, professional audit
  sampling, survey methodology). GOOD and near-primary on the streetlight/discovery-count result
  (Klees et al., key figures read). GOOD at bibliographic level on Geddes. MODERATE on ISA 530 —
  located in authoritative hostings, read at summary level, paragraph numbers deliberately not
  cited. NOT SEARCHED, and each would materially strengthen this: (i) capture-recapture and
  fault-seeding estimators for coverage, which are PREMISE-124's own named remedy and are the only
  approach located anywhere that estimates a denominator WITHOUT the fleet asserting one — this is
  the most valuable unsearched thread and it is the plausible answer to residual (R3); (ii)
  Inozemtseva & Holmes (ICSE 2014) on coverage-versus-suite-effectiveness controlling for suite
  size, which bears directly on whether ANY coverage figure is worth computing and would sharpen
  PREMISE-109's objection; (iii) the MNAR / missing-not-at-random diagnostics literature, which
  would turn Caveat (d)'s "plausible and unmeasured" into a testable condition.

  Recommendation: **SUPPORTED (Strong)** for the corrective proposition; equivalently
  NO-SUPPORT-FOUND for the presumption as worded. But the register already holds the principle five
  ways and has already rejected the obvious remedy, so the disposition-worthy residual is narrow
  and is not "volume is not coverage":
    1. THE SUBSTANTIVE FIGURES, NOT THE MONITORING ONES (R1). Every existing premise on this
       subject governs a health metric. 803's risk statement points at 636 PRS triplets and 103
       cross-connections — the project's central claim. Whether those figures are conditioned on
       which agents ran is a question the register has never asked, and it is a different question
       from the ones it has answered.
    2. THE DISCRIMINATING TEST IS CHEAP AND IS AVAILABLE NOW. For the 636 triplets and 103
       cross-connections, record per-tradition contribution counts against per-tradition RUN
       counts. If contribution is roughly proportional to runs, the figures are a statement about
       the schedule; if not, they carry tradition-level signal. This requires no new instrument and
       no coverage percentage, so it survives PREMISE-109. It also directly tests Caveat (d)'s
       unmeasured correlation.
    3. AGGREGATION IS THE UNCOVERED FAILURE (R2). Per-report scope disclosure is already required
       by PREMISE-097 and is, by the item's own evidence, being done well. The gap is that many
       careful partial disclosures produce an impression of thoroughness and no system-level
       statement. Naming this as a distinct failure — LOCALLY HONEST, GLOBALLY SILENT — is the
       item's contribution and is the same shape as PREMISE-109's "individually faithful to every
       source it read and collectively false about the system," one layer down.
    4. CARRY CAVEAT (b) EXPLICITLY. The remedy space is constrained by an existing High-confidence
       premise and this file did not find an instrument that satisfies it. Capture-recapture and
       fault seeding (PREMISE-124's own named remedies) are the unsearched candidate and should be
       the next search, not another restatement that volume is not coverage.
