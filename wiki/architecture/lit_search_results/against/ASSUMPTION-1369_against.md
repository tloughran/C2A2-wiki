SEARCH-AGAINST-ASSUMPTION-1369:
  Date searched: 2026-09-14
  Original item: ASSUMPTION-1369
  Original statement: "7 blocks drained in 14 days. Six were from the 07-05 stale-downgraded cohort, and
    **all six went to REVISE — none was confirmed.** That's an argument against the stale-downgrade rule
    as written: staleness measured cadence, not truth." Raised by 15d (2026-09-13 weekly run) as a second
    population-level STALE-MONITOR-FLAG; extracted verbatim and routed by 14a.

  READ-CHANNEL INDEPENDENCE ATTESTATION, AND ITS LIMIT: I did not read
    `architecture/lit_search_results/for/`, any 15a output, or `lit_search_returns.md` at any point in
    this run. This matters for one non-obvious reason specific to this item: the 15c *disposition
    records* (DISPOSITION-890..895) live in `lit_search_returns.md` and were therefore NOT read. The
    in-house measurement below is reconstructed entirely from `validated_premises.md`,
    `revision_flags.md` and `monitor_queue.md`, which are not 15a channels. Per PREMISE-111 (ACTIVE) the
    read-channel closure is the weakest of at least four correlation channels and is NOT independence;
    the standing discount applies and no agreement between this file and any 15a file may be cited as
    independent confirmation.
    FETCH-CHANNEL NOTE (required): nothing in this run appeared pre-served from a shared session cache —
    every retrieval below was a live fetch with a fresh body or a fresh failure. Three fetches were
    BLOCKED and are named so a later run does not assume they were skipped: (i)
    `pubmed.ncbi.nlm.nih.gov/6871349` (Begg & Greenes) returned an **empty body** — title/meta only;
    (ii) the Hanley & Lippman-Hand 1983 reprint PDF at jhanley.biostat.mcgill.ca returned
    "**PDF is empty or contains no machine-readable text**"; (iii) `academic.oup.com/ije/article/34/1/215`
    (Barnett et al.) was refused by the fetch tool's **provenance gate** ("URL not in provenance set"),
    which is a tool restriction, not a paywall. Each affected citation is downgraded accordingly below.

  PROVENANCE:
    Origin: 15d, extracted and routed by 14a
    Chain: [15d → 14a → 15b]
    Original item: ASSUMPTION-1369
    Item type: ASSUMPTION (stated — quoted from an agent run report)
    Transform at each step:
      15d: Raised as the second population-form STALE-MONITOR-FLAG of the 2026-09-13 run, on the
        2026-07-05 LOW-PRIORITY-MONITOR cohort (81 blocks still standing, 70 days since downgrade).
      14a: Extracted verbatim and routed. The gloss ("cadence, not truth") is the run's own and is
        explicitly not endorsed by the register.
      15b: Searched for literature on selection on the dependent variable, collider/endogenous selection
        bias, the missing-control-arm/denominator problem, small-n exact inference, verification bias in
        diagnostic-test evaluation, regression to the mean, and the empirical relation between artefact
        AGE and defect incidence; re-ran the register pre-check and found the intake's pre-check **NOT
        CONFIRMED**; and ran an in-house measurement which **refutes the item's central numeric claim**.
    Current status: CHALLENGED

  REGISTER PRE-CHECK — **the intake's pre-check is NOT CONFIRMED.** The intake grepped `stale`,
    `re_check`, `cadence`, `downgrade`, read PREMISE-051 once, and concluded that "no covering premise on
    the inferential question" exists. PREMISE-051 is, as the intake says, irrelevant — it is the
    graph-surface / card-directory coordinated-views premise and has nothing to do with staleness at all
    (read at source this run, line 1616). But the intake searched for the *topic* and the covering
    premises are filed under the *inference*. Re-read at source this run in
    `architecture/validated_premises.md`:
      - **PREMISE-174 (ACTIVE, 2026-08-16), clause (2), is squarely on point and is the covering
        premise the intake says does not exist.** Verbatim: "**THE REPORTABLE STATISTIC IS CORRECTION
        LATENCY, NOT A RETRACTION RATE. A retraction or refutation rate is confounded with SCRUTINY** —
        the same relationship that makes high-impact journals retract MORE — so it rises when
        14a/14b/15a/15b/15c get sharper and falls when the pipeline is idle, **measuring the auditor
        under the auditee's name.**" "Six of six went to REVISE" *is* a refutation rate. The register
        already holds that such a rate is confounded in exactly the direction the item reads it, and
        already names the substitute quantity. The item's inference was ruled out four weeks before it
        was made.
      - **PREMISE-143 (ACTIVE, 2026-08-05):** "A RETRACTION COUNT IS A MEASURE OF THE PRODUCING LAYER,
        NOT OF THE CATCHING LAYER." The six items are the oldest the pipeline ever produced; on this
        premise their REVISE count measures 14a/14b at their April-2026 vintage, not the passage of time.
      - **PREMISE-168 (ACTIVE, 2026-08-15):** "A YIELD FIGURE PUBLISHED WITHOUT ITS DENOMINATOR IS A
        STATEMENT ABOUT THE PRODUCER, NOT ABOUT THE SPACE." "Six of six" is published with a denominator
        of six drawn from a cohort of 81 and with **no comparison arm at all**.
      - **PREMISE-136 (ACTIVE, 2026-08-01), scope guard:** a single-digit denominator does not make a
        quantity undecidable, but "what it gives is a WIDE interval, and reporting a wide interval
        honestly is admissible where reporting a point estimate is not." The item reports a point
        estimate of 1.00 with no interval.
      - **PREMISE-124 (ACTIVE, 2026-07-23):** self-measurement of the pipeline's own accuracy requires an
        external baseline or a seeded/independent denominator or must be tagged UNCALIBRATED; FORBIDDEN
        MOVE named there is "reading a single favorable self-observation as evidence a safeguard works."
        This item is the mirror image — a single *unfavourable* self-observation read as evidence a rule
        fails — and the premise's rationale is symmetric.
      - **PREMISE-096 (ACTIVE, 2026-07-16):** "No self-produced artifact may certify itself... **denominators
        by independent corroboration.**" 15d's own count was the sole warrant for the claim and was not
        corroborated. It is wrong (see below).
      - **PREMISE-135 (ACTIVE, 2026-07-29):** terminality is purchased by enumerating the domain, not by
        accumulating instances; a claim over a population owes the population, a termination criterion
        and one severe out-of-sample test. Six of 81 supplies none of the three.
    **Six covering premises, all ACTIVE, all bearing directly on the inferential question, and one of
    them (174) written specifically to forbid this exact inference.** The grep the intake ran could not
    have found them because none of them contains the word "stale"; they are indexed under retraction,
    denominator and self-certification. That is a **generalisable defect in the pre-check method**, not a
    lapse on this item, and it is the substance of the SYSTEMIC-RISK-FLAG below.

  IN-HOUSE MEASUREMENT — **the item's central numeric claim is false on the register's own record.**
    Reported as internal measurement, not as literature. Method and denominators declared per
    PREMISE-168/136.

    (A) **IT WAS NOT SIX OF SIX. IT WAS FIVE OF SIX, AND THE SIXTH WAS CONFIRMED.** 15d's run report
      (`monitor_queue.md`, 2026-09-13 block, "Consumption check") enumerates the six by name:
        MONITOR-002 (ASSUMPTION-006) → REVISE-425 / DISPOSITION-890, 09-02
        MONITOR-004 (ASSUMPTION-008) → REVISE-426 / DISPOSITION-891, 09-02
        MONITOR-006 (PRESUMPTION-001) → REVISE-427 / DISPOSITION-892, 09-02
        MONITOR-009 (PRESUMPTION-004) → REVISE-428 / DISPOSITION-893, 09-04
        MONITOR-068 (PRESUMPTION-073) → "REVISE", 09-04  [= REVISE-429 / DISPOSITION-894, confirmed]
        MONITOR-070 (ASSUMPTION-071) → "REVISE", 09-04  [**FALSE**]
      Note that the first four carry a REVISE number and the last two do not. Checked at source:
      `revision_flags.md` contains **no REVISE entry whose Item is ASSUMPTION-071 or MONITOR-070** — the
      09-04 pair is REVISE-428 (PRESUMPTION-004, DISPOSITION-893) and REVISE-429 (PRESUMPTION-073,
      DISPOSITION-894). DISPOSITION-895, the next in the contiguous run, appears in
      `validated_premises.md` as the provenance of **PREMISE-198**:
        "PREMISE-198: Date validated: 2026-09-04. Source item: **ASSUMPTION-071 (MONITOR-070, monthly
        re-check cycle 5) - DISPOSITION-895**... Confidence: **High** for clauses (a) and (b)...
        Status: **ACTIVE**. PROVENANCE: Chain [14a -> 15a, 15b -> 15c -> **15d -> 15a, 15b (cycle 5)** ->
        15c]."
      That provenance chain records the cycle-5 15d re-trigger explicitly: this is a stale-downgraded
      07-05 cohort member that was re-searched *because* the stale rule flagged it, and that came back
      **INCORPORATE at High confidence**, materially strengthened by 2026 evidence unavailable in April.
      **A member of the cohort was confirmed.** The item's sentence "none was confirmed" is
      contradicted by an ACTIVE premise minted on the same day, by the same layer, from the same cohort.
    (B) **The interval is wide either way, and on the corrected count it is uninformative.** Exact
      (Clopper–Pearson) 95% intervals computed this run:
        as claimed, 6/6 = 1.000, 95% CI **[0.541, 1.000]**
        as recorded, 5/6 = 0.833, 95% CI **[0.359, 0.996]**
      The claimed figure is already consistent with a true REVISE rate of 54%. The corrected figure is
      consistent with a true rate of **36%**, i.e. with stale items being *more likely to be confirmed
      than revised*.
    (C) **THE MISSING CONTROL ARM, SUPPLIED.** The item compares six stale items against nothing. Over
      the identical 14-day window (2026-08-31 … 2026-09-13) I counted every disposition the estate
      recorded, by date field, across the three non-15a registers:
        REVISE entries in `revision_flags.md`: **44**, of which **6** belong to the 07-05 cohort
          (REVISE-424 on MONITOR-012's literature limb, plus 425–429) → **38 non-stale REVISE**
        Premises minted in `validated_premises.md` (`Date validated` in window): **11**, of which
          **1** is the stale cohort (PREMISE-198) → **10 non-stale INCORPORATE**
        MONITOR entries filed in window: **24** (MONITOR-585..606 filed 08-31…09-11, plus -607, -608)
        **Non-stale denominator: 72. Non-stale REVISE rate: 38/72 = 52.8%, 95% CI [0.407, 0.647].**
      Against that base rate:
        Fisher's exact, two-sided, **5/6 vs 38/72: p = 0.216 — not significant.**
        Fisher's exact, two-sided, 6/6 vs 38/72: p = 0.033 (i.e. the entire statistical signal in the
          item rests on the one item it miscounted).
      **The estate's REVISE rate in this window is about one in two for everything, stale or fresh.**
      Six-for-six would have been mildly surprising against it; five-for-six is ordinary variation.
      DENOMINATOR CAVEAT, stated rather than buried: this is a convenience denominator. Limb-split
      dispositions can produce a REVISE and a PREMISE from one item (PREMISE-201 and PREMISE-204 are
      both marked LIMB-SPLIT), so the 72 is approximate and the three registers are not guaranteed to
      partition the item space. The conclusion is robust to plausible jitter in the MONITOR count — the
      rate has to fall below ~25% before 5/6 becomes significant — but the figure is **UNCALIBRATED**
      in PREMISE-124's sense and should be labelled so wherever it is reused.
    (D) **THE SAMPLE WAS SELECTED ON THE ROUTE, NOT JUST ON THE AGE.** From the same run report:
      "**7 of 7 blocks drained were literature or literature-limb items; 0 of 32 standing empirical
      blocks were touched**," and ESCALATION 3: "Seven blocks burned this interval, **all seven from the
      single oldest cohort's literature tail.**" So the six were selected by two filters — oldest-first,
      and *literature-servable*. Whether a stale item is literature-servable is plausibly a function of
      what kind of claim it is, and kind-of-claim plausibly bears on whether it survives re-check. This
      is conditioning on a common effect (see Source 1). **No fresh item was re-checked in this window
      at all under the 15d route**, which is why the control arm in (C) had to be assembled from the
      14a/14b intake lane instead and is therefore not a matched comparison.
    (E) **AGE IS CONFOUNDED WITH PIPELINE VINTAGE.** ASSUMPTION-006, -008, PRESUMPTION-001, -004, -010
      are the lowest-numbered items the estate holds — the very first output of 14a/14b, before
      PREMISE-096, -111, -124, -135, -136, -143, -168 and -174 existed to discipline them. The oldest
      items were produced by the youngest pipeline. On PREMISE-143 that is precisely a measurement of
      the producing layer. **"Old items fail re-check" and "items written before the standards existed
      fail re-check" are indistinguishable in this sample**, and the second explanation requires no
      staleness mechanism whatever.
    (F) **"WENT TO REVISE" DOES NOT MEAN "WAS FOUND INVALID."** From `agents/15c_net_evaluator_agent.md`,
      read this run: REVISE = "Evidence challenges the premise strongly enough that a design revision
      **should be considered**. The item is routed back to 14a/14b with a recommendation to **flag for
      human (Tom's) review**." It is a routing verdict, not a truth verdict, and `revision_flags.md`
      records it with "What is at risk / Recommended action," not with a finding of falsity. 15d's own
      gloss in the same run — "Every one that has now been searched was **wrong, not merely
      unresolved**" — is therefore an over-reading of the disposition vocabulary. It is also
      demonstrably too strong for at least two of the five: REVISE-429's own text says the claim "as
      literally stated is false" (so, one genuine refutation), whereas REVISE-428 turns on whether **one
      threshold can serve decision types with different error-cost structures** — a scope-refinement,
      not a falsification. And 15c's own published heuristics bias the outcome independently of
      evidence: "**PRESUMPTION with strong challenge → lean REVISE with HIGH urgency**." Four of the
      seven drained (PRESUMPTION-001, -004, -010, -073) are PRESUMPTIONs and were routed down a
      REVISE-favouring path by rule.

  Challenging evidence found: **Yes — and unusually, the strongest challenge is in-house and arithmetical
    rather than literary.** The literature supplies the names and the magnitudes for a defect that the
    register itself already documents.

  Sources:
    1. **Elwert, F. & Winship, C. (2014), "Endogenous Selection Bias: The Problem of Conditioning on a
       Collider Variable," *Annual Review of Sociology* 40:31–53.** — **VERIFIED** (full author PDF
       retrieved and read this run; abstract, definitions box and the Hollywood example read verbatim).
       Abstract, verbatim: "endogenous selection bias stems from **conditioning (e.g., controlling,
       stratifying, or selecting) on a so-called collider variable**, i.e., a variable that is itself
       caused by two other variables, one that is (or is associated with) the treatment and another
       that is (or is associated with) the outcome. Endogenous selection bias can result from **direct
       conditioning on the outcome variable**, a post-outcome variable, a post-treatment variable, and
       even a pre-treatment variable." The paper's worked example maps onto the estate's draw almost
       line for line: beauty and talent are independent in the population, each is separately sufficient
       for Hollywood success, and "conditioning on the collider (success) has created a **spurious
       association** between beauty and talent among the successful." Substitute: *age* and
       *literature-servability* are each sufficient to get a block drawn; being drawn is the collider;
       and any association observed **among the drawn** between age and outcome is of exactly this kind.
       The paper's definitions box also makes clear that "conditioning" explicitly includes "**sample
       selection**," which is the only operation 15d performed. Berkson (1946) is cited here as the
       canonical antecedent — **SECONDARY** (seen as a citation inside this verified source; Berkson's
       own paper not retrieved).
    2. **Jovanovic, B.D. & Levy, P.S. (1997), "A Look at the Rule of Three," *The American Statistician*
       51(2):137–139, JSTOR 2685405.** — **VERIFIED** (full JSTOR PDF retrieved and read this run,
       including Table 1). This is the arithmetic the item omits, and it is decisive at the item's own
       n. The Rule of Three: "**3/n is an upper 95% confidence bound for binomial probability p when in
       n independent trials no events occur.**" Table 1, read directly, gives for **n = 6**: exact
       binomial upper bound **1 − α^(1/n) = .39304**; Rule of Three 3/n = **.50000**; Bayesian
       (uniform-prior) bound 3/(n+1) = **.42857**. Applied to the item as *stated*: six re-checks, zero
       confirmations, therefore the 95% upper bound on the confirmation rate of the stale cohort is
       **39%** — a rate at which roughly **one stale item in two and a half would survive re-check**,
       and at which the cohort of 81 would contain up to **32 sound items**. "None was confirmed" is
       fully consistent with a rule that is right about two-thirds of the time, and a rule that is right
       two-thirds of the time is not a rule to be suspended. Applied to the item as *recorded* (one
       confirmation in six) the zero-numerator machinery does not even apply and the interval is the
       [0.359, 0.996] computed above.
    3. **Graves, T.L., Karr, A.F., Marron, J.S. & Siy, H. (2000), "Predicting Fault Incidence Using
       Software Change History," *IEEE Transactions on Software Engineering* 26(7):653–661.** —
       **VERIFIED** (full paper retrieved and read this run). This is the best-measured empirical test
       anywhere of "does age predict defect," on 80 modules, ~1.5M lines, ~130,000 changes, >1,500 fault
       reports, and **it runs the opposite way to the item's premise.** Abstract, verbatim: "We also
       compare the fault rates of code of various ages, finding that **if a module is, on the average, a
       year older than an otherwise similar module, the older module will have roughly a third fewer
       faults.**" Results section, verbatim: "The coefficient of −0.44 for age means that if one
       module's changes occurred a year earlier than those of another module with the same number of
       deltas and in the same branch, the older module will tend to have only exp(−0.44) = **0.64** as
       many faults. **This finding is consistent with our expectation that code which survives a long
       time is likely to be well-written.**" And on the mechanism, verbatim: "**Old changes either will
       have been fixed or will have been demonstrated to be fault-free.**" Their best model damps old
       changes' fault potential by "about **50 percent a year**." **The variable that predicts defects is
       CHANGE, not AGE**: "the number of times code has been changed is a better indication of how many
       faults it will contain than is its length," and lines-of-code adds nothing once deltas are in the
       model. Transfer caveat, stated: a wiki premise is not a code module, and an unchanged *premise*
       can be falsified by a changing world in a way an unchanged *module* cannot. But the item's
       implicit model — that sitting still makes an item more likely to be wrong — is the model this
       literature tested at scale and found inverted. The estate's own PREMISE-198 is a small instance
       of the opposite mechanism working as Graves describes: the item sat, the world moved, and the
       re-check **strengthened** it.
    4. **Rutjes, A.W.S., Reitsma, J.B., Di Nisio, M., Smidt, N., van Rijn, J.C. & Bossuyt, P.M.M. (2006),
       "Evidence of bias and variation in diagnostic accuracy studies," *CMAJ* 174(4):469–476.** —
       **VERIFIED** (full text retrieved and abstract/Interpretation read verbatim this run). 31
       meta-analyses, 487 primary studies; "**Only 1 study had no design deficiencies.**" The figure
       that bears: "We found significantly higher estimates of diagnostic accuracy in studies with
       **nonconsecutive inclusion of patients (relative diagnostic odds ratio [RDOR] 1.5, 95% CI
       1.0–2.1)**" and "The estimates were highest in studies that had **severe cases and healthy
       controls (RDOR 4.9, 95% CI 0.6–37.3)**." The estate's draw was nonconsecutive by construction
       (oldest-first, literature-tail-only), which is the design feature this meta-epidemiologic study
       associates with **inflated apparent test performance**. **HONESTY NOTE, recorded because it cuts
       against my own direction:** this paper explicitly failed to find the effect I would most have
       liked — "**we were unable to demonstrate a consistent effect of partial verification**... If a
       proportion of negative test results is not verified, this tends to increase sensitivity and lower
       specificity, which may leave the odds ratio unchanged." So the verification-bias limb of my brief
       is **not** supported by the best available quantification, and I am not claiming it is. What
       survives is the *structural* point (Source 5), not a magnitude.
    5. **Begg, C.B. & Greenes, R.A. (1983), "Assessment of diagnostic tests when disease verification is
       subject to selection bias," *Biometrics* 39(1):207–215, DOI 10.2307/2530820, PMID 6871349.** —
       **SECONDARY** (bibliographic record and abstract summary confirmed across three independent
       search-layer sources; **the PubMed record itself returned an empty body on fetch** and the primary
       was not read). Reported content, used only structurally and with no figure quoted: when a
       diagnostic test's properties are estimated only from cases that received definitive verification,
       "omission of nonverified cases can seriously bias the estimates." The structural point transfers
       exactly and is the sharpest single statement of what is wrong with the item: **the stale-downgrade
       rule's precision cannot be measured by re-checking only the items the rule flagged.** Sensitivity
       and specificity are properties of a 2×2 table, and the estate has populated one cell. It has
       never re-checked a *non*-stale item under the same instrument in the same window, so the rule's
       false-positive rate is not merely unknown, it is **unestimable from the data the item cites**.
    6. **Barnett, A.G., van der Pols, J.C. & Dobson, A.J. (2005), "Regression to the mean: what it is and
       how to deal with it," *International Journal of Epidemiology* 34(1):215–220, DOI
       10.1093/ije/dyh299, PMID 15333621.** — **SECONDARY** (abstract obtained at the search layer;
       **the publisher page was refused by the fetch tool's provenance gate**, so the primary was not
       read and no figure from it is used). Reported abstract, one clause of which is directly on point:
       "The effect of RTM in a sample becomes more noticeable with increasing measurement error and
       **when follow-up measurements are only examined on a sub-sample selected using a baseline
       value.**" That is a literal description of the estate's design — a sub-sample selected on a
       baseline value (no-evidence-movement across four cycles), then re-measured. Used for direction
       only; no magnitude claimed.
    7. **Geddes, B. (1990), "How the cases you choose affect the answers you get: selection bias in
       comparative politics," *Political Analysis* 2(1):131–150.** — **SECONDARY** (bibliographic record
       and topical summary confirmed at the search layer across three sources; primary not retrieved
       this run). Already **register-held**: PREMISE-168 cites Geddes for the proposition that block
       samples are not projectable. Reported content: selecting cases on the basis of their outcome on
       the dependent variable biases the conclusions drawn from them. Named here because it is the
       canonical short form of the objection and because the register already accepts it, so the item is
       in tension with a premise the estate has already validated on this author.
    8. **DO-NOT-CITE — figures encountered and deliberately excluded.** (i) Any *rate* from the
       verification-bias literature: the canonical primary (Begg & Greenes) could not be read, and the
       best quantification I did read (Source 4) reports **no consistent effect**, so no
       partial-verification magnitude may enter the record from this run. (ii) The Hanley &
       Lippman-Hand (1983) JAMA original, 249(13):1743–1745 — **the reprint PDF returned no
       machine-readable text**; the rule-of-three numbers above are taken from Jovanovic & Levy's Table 1,
       which was read, and Hanley is cited only as the attributed origin of the rule *within* that
       verified source. (iii) The "~50% per year" fault-decay constant from Source 3 is quoted as the
       authors state it, but their own bootstrap gives a 95% interval for θ of [0.375, 1.5] and a second
       overlapping window produced θ = 12, which they call "**disconcerting**" — so the decay *direction*
       is usable and the decay *constant* is not. **No unverified number carries any part of the rating
       below.**

  Strength of challenge: **Strong.**

    Limb split:
      - "**All six went to REVISE — none was confirmed**": **Refuted**, in-house, at source. One of the
        six (ASSUMPTION-071 / MONITOR-070, cycle 5, DISPOSITION-895) was **INCORPORATED** as PREMISE-198
        on 2026-09-04, at High confidence, ACTIVE, with the 15d cycle-5 re-trigger written into its
        provenance chain. The correct figure is 5 of 6. This is not a quibble: the item's entire
        rhetorical and statistical force is the perfect record, and the perfect record is not there.
      - "**Six were from the 07-05 stale-downgraded cohort**": **internally inconsistent in the source
        run.** The same report's ESCALATION 3 says "Seven blocks burned this interval, **all seven** from
        the single oldest cohort's literature tail," while the consumption check says six plus a partial.
        The two are reconcilable (MONITOR-012 is a half-exit) but the run does not reconcile them, and a
        claim whose denominator moves between two paragraphs of one document is not a measurement.
      - "**That's an argument against the stale-downgrade rule as written**": **Strong** challenge. On
        the corrected count, Fisher's exact against the estate's own 14-day non-stale disposition mix
        gives **p = 0.216**. There is no signal. On the *claimed* count the exact 95% interval is
        [0.541, 1.000] and the rule-of-three upper bound on the confirmation rate is 39% — i.e. even
        the claimed result is compatible with a third of the 81-block cohort being sound.
      - "**Staleness measured cadence, not truth**": **Strong** challenge, and on two independent
        grounds. (a) The rule *never claimed* to measure truth. Read at source in `monitor_queue.md`,
        the 15d rule fires at "**4+ cycles with no change in evidence**" and its action is
        "DOWNGRADE → LOW-PRIORITY-MONITOR (monthly cadence) AND ESCALATE," with the stated rationale
        that "the blocker is an un-run empirical/paired test, NOT an unsettled literature — so
        additional 15a/15b literature cycles are predicted **low-yield**." That is a *throughput*
        instrument with a *throughput* justification. Discovering that it does not track truth is
        discovering that a thermometer is not a clock. (b) The one external literature that has
        actually measured age-versus-defect at scale (Source 3) finds the relation running the *other*
        way — older, unchanged artefacts carry roughly a third fewer faults — which means the item's
        implicit alternative hypothesis ("old ⇒ probably wrong") is not the null the data should be
        tested against.
      - What the item gets right, and it should not be lost: **six or seven items out of an 81-block
        cohort sat unsearched for 59–70 days**, and that is a real and serious finding about starvation
        and queue policy. The item's *operational* recommendation — "do not downgrade more items under
        this rule until reviewed" — may well be correct **for throughput reasons**. It simply is not
        supported by the evidential argument the item gives for it, and the two should not be allowed to
        travel together.

  Summary: The item's decisive fact does not survive contact with the register. Of the six 2026-07-05
    cohort members re-checked in the 14-day window, **five went to REVISE and the sixth
    (ASSUMPTION-071 / MONITOR-070) was INCORPORATED as PREMISE-198 on 2026-09-04 at High confidence**,
    with the cycle-5 stale re-trigger written into its own provenance chain — so "none was confirmed"
    is contradicted by an ACTIVE premise minted the same day by the same layer from the same cohort.
    With the count corrected, the result is statistically indistinguishable from the estate's own
    behaviour: over the identical window the non-stale REVISE rate was **38 of 72 (52.8%)**, and
    Fisher's exact for 5/6 against it returns **p = 0.216**. Even on the item's claimed 6/6, exact
    small-sample inference puts the 95% interval at **[0.541, 1.000]** and the rule-of-three upper bound
    on the cohort's confirmation rate at **39%** (Jovanovic & Levy 1997, Table 1, verified) — up to 32
    sound items in the 81. The design is compromised three ways beyond the arithmetic: the six were
    selected on age *and* on literature-servability, which is conditioning on a common effect and
    generates spurious association by construction (Elwert & Winship 2014, verified); the rule's
    precision cannot be estimated at all without re-checking items the rule did *not* flag, and no fresh
    item was re-checked under the 15d route in this window (Begg & Greenes 1983, structural point only);
    and age is perfectly confounded with pipeline vintage, since ASSUMPTION-006/008 and
    PRESUMPTION-001/004/010 are the earliest items 14a/14b ever produced, before the standards that now
    govern them existed. Finally "went to REVISE" is a routing verdict meaning "a design revision should
    be considered / flag for Tom," not a finding of invalidity, and 15c's own published heuristic routes
    PRESUMPTIONs toward REVISE by rule — four of the seven drained were PRESUMPTIONs. Against all of
    this, the one large-scale empirical study of whether age predicts defect in an ageing artefact corpus
    found the opposite: a module a year older than an otherwise similar one carries "roughly a third
    fewer faults," because "old changes either will have been fixed or will have been demonstrated to
    be fault-free."

  Specific risks:
    - **A rule is about to be suspended on a number that is wrong.** The item's recommendation is
      "ESCALATE to Tom / 15c — review the stale-downgrade rule, **do not downgrade more items under it
      until reviewed**." The stale-downgrade rule is the estate's only mechanism for keeping a
      190-item weekly carry-over lane from consuming every cycle. Suspending it on the strength of
      5-mislabelled-as-6 would move ~150 items back onto weekly re-trigger into a lane that, by the same
      run's own measurement, **drains 7 blocks per fortnight and would take ~80 weeks to clear**. The
      predictable outcome is that the backlog grows faster and the *genuine* starvation finding gets
      harder to act on, not easier.
    - **The error is of a class the register has already paid for, twice.** PREMISE-096 requires
      denominators to be independently corroborated; PREMISE-124 requires an external baseline or an
      UNCALIBRATED tag; PREMISE-168 bars a bare numerator; PREMISE-174 forbids reading a refutation rate
      as a property of the auditee. **All four are ACTIVE, all four were breached by one sentence, and
      the sentence was then routed for external literature search** — i.e. the pipeline was about to
      spend two subagents' budget adjudicating a claim that one grep of its own premise register would
      have stopped.
    - **If 15c dispositions this without the recount, PREMISE-198 and ASSUMPTION-1369 enter the register
      in direct contradiction.** One says a cycle-5 stale item was confirmed at High confidence; the
      other says none was. 15c's own spec requires flagging both for human review when a new INCORPORATE
      contradicts an existing PREMISE. That check will only fire if someone notices, and the
      contradiction is currently invisible because it spans two files.
    - **Reflexive risk, and it is the sharpest one.** The estate's *only* evidence for the state of its
      own machinery is measurements like this one, produced by the machinery, read by the machinery, and
      routed by the machinery. This item is a clean instance of that loop returning a false value and
      being believed all the way to a literature-search budget. The item's own moral — that a
      convenient-looking number should not be trusted because it was easy to compute — applies to the
      item with full force.
    - **Over-correction risk in the other direction.** Nothing here shows the stale rule is *good*. It
      shows the evidence offered against it is not evidence. The rule remains untested in the only sense
      that would matter, and treating this file as a vindication would reproduce the original error with
      the sign flipped.

  Mitigations available:
    - **Recount before dispositioning. One command, and it is owed before anything else.** Re-derive the
      six dispositions from `revision_flags.md` and `validated_premises.md` by DISPOSITION id
      (890–895) rather than from the 15d run's prose, and correct the item in place to 5 of 6 with
      PREMISE-198 named. Per PREMISE-174 clause (3) the correction is recorded by **supersession**, not
      by mutating the 09-13 entry.
    - **Build the control arm before the next claim, not after.** The rule's precision needs a 2×2
      table. The cheap version needs no new instrument: on the next 15d draw, take **k stale and k
      non-stale items matched on route (literature-servable) and on intake vintage**, search both arms
      blind to cohort, and compare. Matching on vintage is the load-bearing part — without it, (E)
      above guarantees the result is uninterpretable whichever way it comes out.
    - **Make the draw order explicit and record it.** Oldest-first is currently a de facto pattern, not
      policy (the same run recommends making it policy, for the 16th time). Until the selection rule is
      written down, **every** outcome statistic computed over drawn items is conditioned on an
      unrecorded selection mechanism and is uninterpretable under Source 1. Writing the draw rule down
      costs one line and converts the whole lane into an analysable design.
    - **Publish correction latency, not refutation rate.** PREMISE-174 already specifies the substitute
      statistic and the reason. For this cohort the honest quantity is: assertion date → withdrawal
      date, per item, which is computable today and is not confounded with how hard anyone looked.
    - **Separate the throughput finding from the evidential one and keep the throughput finding.** "81
      blocks, 70 days, 7 drained per fortnight, ~80 weeks to clear, zero of 32 empirical blocks ever
      touched" is a strong, well-evidenced, independently reported operational finding and it does not
      need the 6/6 claim at all. File it on its own so that recounting the six does not discredit it.
    - **Add the missing index terms to the pre-check.** The intake's grep could not have found any of the
      six covering premises because none contains "stale." A standing pre-check term list for
      *inferential* questions — `denominator`, `base rate`, `retraction`, `selection`, `self-certif`,
      `UNCALIBRATED`, `scrutiny` — would have returned PREMISE-174 on the first hit.

  STEELMAN:
    Item: ASSUMPTION-1369
    Strongest counterargument: The recount is real and the statistics are correct, and neither touches
      the argument the item is actually making. Strip the number away entirely and what remains is
      this: **six items that the stale rule certified as quiet enough to check only monthly turned out,
      on first contact, to contain at least five live defects, one of which
      (PRESUMPTION-073 — "adding two traditions does not affect N-dependent properties") is false on
      four independent grounds and had been sitting under a downgraded cadence for 59 days while the
      register held the very premise that refutes it.** That is not a rate estimate and it does not
      need a control arm to be alarming. The stale rule's *stated* logic is that four cycles without
      evidence movement means further literature cycles are low-yield — and the moment literature
      cycles were finally run on these items, they yielded, five or six times out of six. Whatever the
      base rate is, the rule's own predictive claim about *these* items was falsified by the only test
      ever applied to it. Demanding a matched control arm before acting sets an evidentiary bar the
      estate has never met for any operational decision and cannot meet at a drain rate of seven blocks
      a fortnight: by the time k matched pairs exist, another 150 items will have been downgraded under
      the rule. And the asymmetry of costs is not symmetric with the asymmetry of evidence — pausing
      further downgrades is cheap and reversible; continuing to downgrade items that are wrong is
      neither. The correct reading of the recount is therefore not "the item is refuted" but "the item
      overstated by one, and five is still five."
    What would need to be true for C2A2 to be safe: (a) the five REVISEs would have to be genuine
      invalidity findings rather than routing verdicts — **partly true and partly not**: REVISE-429
      states its claim "as literally stated is false," which is a real refutation, while REVISE-428
      turns on threshold uniformity across decision types, which is a scope refinement of a claim that
      remains usable; the steelman is entitled to about two or three of its five, not five;
      (b) the vintage confound would have to be immaterial — **it is not**, and this is where the
      steelman is weakest, because "the first items 14a/14b ever wrote were rough" fully explains the
      observation and predicts, unlike the staleness story, that **fresh items downgraded next year will
      be fine**, which is a different and much cheaper remedy (re-audit the April cohort once, rather
      than suspend the rule forever); (c) pausing downgrades would have to be cheap — **it is not, at
      this drain rate**, and the same run that raised the flag is the run that measured the lane at ~80
      weeks to clear, so the item's own file contains the cost of its own recommendation;
      (d) the steelman would have to survive its best case, and it partly does: PRESUMPTION-073 sitting
      refuted-in-the-register for 59 days is a genuine and uncomfortable instance, and it is the reason
      this file's recommendation is CHALLENGED rather than REFUTED. The steelman's real contribution is
      to relocate the finding: the defect it identifies is **the estate holding a premise that refutes
      one of its own downgraded items and never connecting the two** — which is a
      retrieval/propagation failure (PREMISE-123's territory), not a staleness failure, and would not
      be fixed by changing the downgrade rule at all.
    How to test: **Three tests, in cost order, all in-house.**
      (1) **The recount (minutes).** Re-derive DISPOSITION-890..895 from the disposition-bearing
      registers and publish the corrected 5/6 with PREMISE-198 named. This is not optional; it is a
      factual correction to a claim already in the record.
      (2) **The vintage discriminator (one afternoon, and it decides between the two live
      explanations).** Take all items ever downgraded under the stale rule that have since been
      re-searched, of any cohort, and cross-tabulate disposition against **intake date**, not against
      time-since-downgrade. If the REVISE rate tracks *intake vintage* — high for the April cohort,
      falling for later cohorts — the finding is "the early pipeline was rough" and the remedy is a
      one-time audit of the earliest items. If it tracks *time-since-downgrade* at constant vintage,
      the item is right and the rule is wrong. These make opposite predictions and the data already
      exist.
      (3) **The matched arm (one 15d cycle).** k stale and k non-stale items, matched on route and
      vintage, searched blind to cohort, dispositioned by 15c blind to cohort. This is the only design
      that estimates the rule's precision rather than its yield, and blinding the dispositioner is the
      part that matters, because of (F) above.

  SYSTEMIC-RISK-FLAG:
    Date: 2026-09-14
    Affected items: ASSUMPTION-1369 (this item) — and, as reported to me by my dispatching context and
      **not independently verified by me**, four sibling 15b runs this cycle that also found the
      intake's register pre-check NOT CONFIRMED. I verify one instance; I record the pattern as
      reported, at the strength of a report.
    Common vulnerability: **The 14a/14b intake pre-check searches the register by TOPIC KEYWORD and the
      register indexes its epistemic premises by INFERENCE TYPE, so covering premises are systematically
      invisible to it.** On this item the intake grepped `stale`, `re_check`, `cadence`, `downgrade` and
      read one premise, and concluded no covering premise existed. Six ACTIVE covering premises exist
      (096, 124, 135, 136, 143, 168, 174) and **not one of them contains the word "stale"** — they are
      filed under retraction rate, denominator, self-certification and terminality. The pre-check cannot
      fail loudly, because a keyword search that returns nothing looks identical to a genuine gap. The
      downstream cost is concrete and measured: a claim already forbidden by PREMISE-174 was minted as
      an ASSUMPTION, routed to two literature-search subagents, and — per the 09-13 snapshot — the
      pipeline spends **~355k tokens** per cycle on those subagents.
    Literature basis: none required; this is an internal enforcement finding against ACTIVE premises.
      The external framing, if one is wanted, is Source 1's point that a selection mechanism you have
      not written down cannot be corrected for.
    Risk level: **High** (not Critical — no terminator is missing, the premises all exist and are
      ACTIVE; this is an enforcement and indexing gap, which PREMISE-172's family already classifies as
      the more common defect).
    Recommendation: **Do not mint a new premise.** PREMISE-096 and PREMISE-174 are the terminators and
      adding a seventh would be exactly the register inflation PREMISE-105 warns about. Instead: (i)
      give the intake a **standing inference-type term list** to grep alongside the topic terms
      (`denominator`, `base rate`, `retraction`, `refutation rate`, `selection`, `self-certif`,
      `scrutiny`, `UNCALIBRATED`, `severe test`); (ii) require the pre-check to **name the terms it
      grepped** in the intake block, as this one did — that disclosure is what made the failure
      diagnosable, and it should be kept; (iii) require any intake block carrying a **numeric claim
      quoted from an agent run report** to state whether the number was re-derived from a
      disposition-bearing register or taken on the report's word. On this item the answer would have
      been "taken on the report's word," and the number was wrong.

  Search scope: **Comprehensive on the inferential question; preliminary on one limb, named.** Six angles
    searched: endogenous selection / collider bias, selection on the dependent variable, exact
    small-sample binomial inference and zero-numerator interpretation, verification and
    design-feature bias in diagnostic-accuracy evaluation, regression to the mean under
    baseline-selected sub-samples, and the empirical age-versus-defect relation in ageing artefact
    corpora. **Four external primaries were retrieved and read in full this run** — Elwert & Winship
    2014, Jovanovic & Levy 1997 (including Table 1), Graves et al. 2000, and Rutjes et al. 2006 — and
    they carry the rating alone. Three fetches were blocked and are named in the attestation above;
    the affected citations (Begg & Greenes, Barnett et al., Hanley & Lippman-Hand) are marked SECONDARY
    and no figure is taken from any of them. **The under-searched limb is the one the estate would most
    want and I did not find:** a study measuring whether *time-since-last-review* predicts the
    invalidity of a curated claim in a knowledge register, as distinct from a code module. Source 3 is
    the nearest analogue and it is an analogue, not the thing. Reported as insufficient search, not as
    absence of evidence — and noted that 15a's brief is pointed at exactly that literature, so the pair
    may cover it. **The in-house measurement, not the literature, is what carries this file**, and it is
    labelled as in-house throughout, with its denominator declared and its convenience-denominator
    caveat stated rather than buried.

  Recommendation: **CHALLENGED**
