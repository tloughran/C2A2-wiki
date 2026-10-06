SEARCH-AGAINST-PRESUMPTION-988:
  Date searched: 2026-09-14
  Original item: PRESUMPTION-988
  Original statement: "[inferred] that citation-integrity checking is a check on the claim. Two defects
    today passed every gate with every citation correct: a limb attached to an article that does not
    contain the claim (I-II Q.53), and a file whose own correctly-graded High anchors defeat its
    reading — concealed by a **charitable gradient paraphrase** standing where a categorical claim
    belonged, which left the supersession criterion nothing to supersede."

  POLARITY NOTE, STATED FIRST BECAUSE THIS FILE INVERTS THE USUAL 15b SIGN. The intake assigns 15a the
    disconfirming direction (rates of attribution error that survive citation checking) and 15b the
    confirming one (**evidence that structural citation gates DO catch claim error — that this is an
    outlier rather than a base rate**). So in this file "challenge" means *challenge to 14b's
    inference that the two defects generalise*, not challenge to the presumption. A reconciler reading
    only the Strength line must read this paragraph with it: **Weak** below means the case for "these
    are outliers" is weak, i.e. 14b's inference survives.

  READ-CHANNEL INDEPENDENCE ATTESTATION, AND ITS LIMIT: I did not read
    `architecture/lit_search_results/for/`, any 15a output, or `lit_search_returns.md` at any point in
    this run. `PRESUMPTION-988_for.md` appeared in a directory listing produced by a filename-only
    grep; it was not opened. Per PREMISE-111 (ACTIVE) that closes the weakest of at least four
    correlation channels and is not independence, and the STANDING DISCOUNT applies: nothing in this
    file may be cited as independent confirmation of anything 15a returns.
  **A FIFTH CHANNEL, NEWLY OBSERVED THIS RUN AND NOT NAMED IN PREMISE-111.** A `web_fetch` of
    `https://www.nature.com/articles/s41467-025-58551-6` (the SourceCheckup paper) returned
    **"Already fetched ... 2806s ago in this session"** and refused to serve content. I had not
    fetched it. **The retrieval cache is session-scoped and shared with concurrently-running siblings.**
    Three consequences, all recorded rather than worked around: (i) I could not read that page and
    obtained the source from arXiv instead, marked accordingly below; (ii) the cache silently tells one
    direction which sources the other has already pulled, which is a correlation channel of exactly the
    kind PREMISE-111 enumerates and is **not** closed by the 2026-07-19 read-channel fix; (iii) it is
    also a *suppression* channel — a source one direction has consumed can be made unavailable to the
    other, which is worse than correlation. **This should be raised as a register item in its own
    right.** I read no sibling output as a result of it.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-988
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from two cross-project defects with a common structure, then transferred to C2A2's
        own gates — a transfer neither originating run made, since neither was working in this wiki.
      15b: Searched the reference-checking-intervention literature, the editorial-verification
        literature, the scientific-claim-verification literature (SciFact / MULTIVERS / SourceCheckup),
        and the scite-classifier accuracy exchange, for evidence that a structural citation gate catches
        claim error; re-ran the register pre-check by hand and **refuted it**; and addressed the
        base-rate question directly, including the in-house denominator.
    Current status: NO-CHALLENGE-FOUND (one narrow PARTIAL, stated below)

  REGISTER PRE-CHECK — **NOT CONFIRMED. The intake's pre-check is wrong, and it is wrong three times
    over.** The intake reports "grepped for `citation`, `attribution`, `paraphrase`, `anchor`, `gate` —
    **no covering premise found** (grep)." I ran the same terms on the same file and got **39 hits for
    `citation`, 96 for `cite`, 22 for `attribution`, 20 for `anchor`, 114 for `gate`, 7 for
    `quotation`**. Reading them rather than counting them produces three ACTIVE covering premises, all
    read at source this run:

      **PREMISE-178 (2026-08-18, source ASSUMPTION-1131, Confidence: HIGH, ACTIVE) is the item, almost
      word for word.** Verbatim: "**AN EXISTENCE CHECK AND A LABEL CHECK DO NOT ESTABLISH THAT A CITED
      SOURCE SUPPORTS THE SENTENCE IT ANCHORS.** Verification at the identifier layer certifies that the
      referent exists and is named correctly; it is silent on the relation between the source's content
      and the anchoring claim. Reading the body is therefore not an optional strengthening of the check,
      it is the only step that tests the property at issue — and automated polarity classification is
      NOT an available substitute at present accuracy. **Founding instance: four ids cited for claims
      their own bodies argue against, every one of which passed both checks.**" Its "Applicable to" line
      names "**the review page's anchor checks**" explicitly. **This is PRESUMPTION-988's first limb,
      settled at High confidence twenty-seven days ago, with a founding instance of four.**

      **PREMISE-132 (2026-07-28, Moderate, ACTIVE).** Verbatim: "**CITING IS NOT VERIFYING.** The
      presence of a citation is not evidence that the citing claim was checked against the cited
      source... a register in which 'all items do cite external referents' is a statement about FORM,
      not about verification."

      **PREMISE-148 (2026-08-06, Moderate, ACTIVE), clause (1)**, carries the measured rates for exactly
      this failure mode: "Quotation error — **whether the cited source actually supports the citing
      author's statement** — pools at 25.4%... recalculated more strictly to 14.5%... who also finds that
      64.8% of content errors are MAJOR — **the referenced source fails to substantiate, is unrelated
      to, or CONTRADICTS the assertion**."

    Adjacent and also on point: **PREMISE-172** ("A PASS MARK IS A VERDICT ABOUT A (READER, FRAME,
    SCOPE) READING — NOT A PROPERTY OF THE FILE... a mark carries no information about what was NOT
    examined"), which is the "passed every gate" limb; and **PREMISE-103** (absence of primary text is a
    kind-difference in evidence).

    **AND THE ITEM HAS BEEN RAISED BEFORE, TWICE.** `revision_flags.md` **REVISE-397 (2026-08-26)**
    carries PRESUMPTION-877, stated as: "**[inferred] That id-resolution *is* citation health — that a
    reference which points at an existing record is thereby a good reference.**" That is PRESUMPTION-988
    with the nouns changed. Its pair **REVISE-393** (ASSUMPTION-1206) records the register's own verdict
    at the time: "**this is settled ground in the register already... the finding is an ENFORCEMENT
    failure against premises the register validated three weeks ago.**" And `validated_premises.md`
    PREMISE-186's batch note records both as GROUP 1 — ALREADY HELD, with the line "**The register knew
    this before the search ran.**"

    **Verdict: NOT CONFIRMED.** This is the **third** arrival of the same claim (2026-08-18 →
    2026-08-26 → 2026-09-14), the second time the intake's pre-check has missed PREMISE-178, and the
    grep terms the intake used would have found it — `citation` and `anchor` both hit its Statement
    line. What PRESUMPTION-988 genuinely ADDS is (a) two new first-party instances, (b) a second failure
    mode (the paraphrase limb) that **PREMISE-178 does not cover**, and (c) the C2A2 cross-connection
    exposure the intake states explicitly. Per PREMISE-138 the remedy for a claim that already has an
    entry is not a second entry beside it.

  Challenging evidence found: **Partial, and much weaker than the direction asked for.** A claim-fit
    check that works is well documented — but every documented instance **reads the body**, which is
    precisely the step the C2A2 gate omitted. **I found nothing whatever showing that an
    existence-and-label citation gate catches claim error**, and the one literature that measures
    whether editorial reference-checking has reduced the error rate reports that it has not.

  Sources:

    1. **Wadden, D., Lo, K., Wang, L.L., Cohan, A., Beltagy, I. & Hajishirzi, H. (2022), "MULTIVERS:
       Improving scientific claim verification with weak supervision and full-document context,"
       *Findings of the Association for Computational Linguistics: NAACL 2022*, pp. 61–76.** —
       **VERIFIED** (full PDF retrieved from ACL Anthology and read this run; Tables 2 and 5 read
       directly). **This is the best source in my assigned direction and its best number is about
       humans, not machines.** Table 5, the "abstract-provided" setting on SCIFACT — i.e. the setting
       where the candidate source is already identified and the only question left is *does this source
       support this claim*, which is exactly the C2A2 gate's missing step — reads: **Human P 94.8, R
       84.1, F1 89.1** at abstract level. The authors' method, verbatim: "we assign 151 claim-evidence
       pairs from SCIFACT for independent annotation by two different annotators. We estimate
       human-level performance by treating the first annotator's results as 'gold,' and the second
       annotator's results as predictions." Their reading, verbatim: "**experts tend to agree on the
       overall relationship between claim and abstract**, but may disagree about exactly which sentences
       contain the best evidence," and the task "may be nearly" solved at that level. **So: two
       independent readers, given the source and the claim, agree on claim-fit at 89.1 F1 with 94.8
       precision. The check is real, it is cheap, and it works.** Machine numbers from the same tables,
       also verified: MULTIVERS abstract-level F1 **72.5** on SCIFACT fully supervised (**77.6**
       HealthVer, **77.3** COVIDFact), and **80.9** in the abstract-provided setting — below the human
       89.1. **The figure that governs transfer to C2A2 is the zero-shot row and it is poor: abstract-
       level F1 30.7 (HealthVer), 47.2 (COVIDFact), 46.7 (SCIFACT).** C2A2's corpus is scholastic
       philosophy and contemplative theology with no in-domain training data; the zero-shot row is the
       applicable one, not 72.5.

    2. **Wu, K., Wu, E., Wei, K., Zhang, A., Casasola, A., Nguyen, T., Riantawan, S., Shi, P.S., Ho, D.
       & Zou, J. (2024/2025), "How well do LLMs cite relevant medical references? An evaluation
       framework and analyses," arXiv:2402.02008; published as "An automated framework for assessing how
       well LLMs cite relevant medical references," *Nature Communications*, April 2025,
       doi:10.1038/s41467-025-58551-6.** — **VERIFIED as to the abstract** (arXiv abstract page fetched
       and read verbatim this run). **The published Nature Communications page could NOT be read — the
       session-shared fetch cache refused it; see the attestation above. The author list is taken from
       the search layer and is UNVERIFIED; the arXiv identifier and the abstract text are not.** The
       load-bearing sentence, verbatim from arXiv: "**we demonstrate that GPT-4 is highly accurate in
       validating source relevance, agreeing 88% of the time with a panel of medical doctors.**" The
       secondary reporting adds that the source-verification model's agreement with the doctor consensus
       **exceeded the average agreement between the doctors themselves** — I mark that claim
       **SECONDARY** (search-layer summary of the published version, not read in the primary) and no
       argument here rests on it. **The 88% figure is the strongest thing my direction has: an automated
       claim-to-source check is buildable today at roughly expert-panel agreement.** Against it, from
       the same abstract, verbatim: "**between ~50% to 90% of LLM responses are not fully supported by
       the sources they provide**," and with RAG, "**around 30% of individual statements are
       unsupported, while nearly half of its responses are not fully supported.**" Those latter figures
       are about the generator, not the checker, and they describe the population C2A2's own synthesis
       machinery belongs to.

    3. **Wager, E. & Middleton, P., "Technical editing of research reports in biomedical journals,"
       *Cochrane Database of Systematic Reviews*, Art. No. MR000002, DOI 10.1002/14651858.MR000002.pub3
       (published version dated 1 November 2021; searches to July 2006/June 2007).** — **VERIFIED**
       (full structured abstract read directly from cochrane.org this run). **This is the
       intervention-effectiveness literature the direction asked for, and it is the source that defeats
       the direction.** What it gives me, verbatim: "**More intensive editorial processes were
       associated with fewer errors in abstracts and references. Providing instructions to authors was
       associated with improved reporting of ethics requirements in one study and fewer errors in
       references in two studies.**" What it takes away, in the same paragraph and the same breath:
       "We located 32 studies addressing technical editing and 66 surveys of reference accuracy. **Only
       three of the studies were randomised controlled trials**"; "**no difference was seen in the
       quality of abstracts in one randomised controlled trial**"; "**The reference accuracy studies
       showed a median citation error rate of 38% and a median quotation error rate of 20%.**"
       Conclusion, verbatim: "**Surprisingly few studies have evaluated the effects of technical editing
       rigorously.**" **Three things follow and they are all against me.** (i) The positive finding is
       *associational*, from two studies, in a review whose own authors call the evidence base
       inadequate. (ii) The 20% median quotation-error rate is **the rate that survives** — these are
       published articles in journals that run technical editing and check cited references as a matter
       of course. A gate that leaves one quotation in five wrong is not a gate that catches claim error.
       (iii) The review separates **citation error** (38%) from **quotation error** (20%) as distinct
       defect classes. **That separation is the whole item.** C2A2's gate measures the first and reports
       on the second.

    4. **Jergas, H. ... Baethge, C. (2025), "Systematic review and meta-analysis of quotation inaccuracy
       in medicine," *Research Integrity and Peer Review* 10(1):13, doi:10.1186/s41073-025-00173-z
       (online 23 July 2025).** — **VERIFIED** (open-access full text retrieved from BioMed Central and
       read this run: Methods, Results and the relevant Discussion paragraph read verbatim; first author
       and corresponding address read from the article metadata — **the full intermediate author list
       is UNVERIFIED and is elided above rather than guessed**). **This is the decisive source against
       my direction and it is a direct test of "the gate is working, these are outliers."** Results,
       verbatim: "**16.9% (95% CI: 14.1%–20.0%) of quotations were incorrect, with approximately half
       classified as major errors (8.0% [95% CI: 6.4%–10.0%])**... **Meta-regression showed no
       significant improvement in quotation accuracy over recent years (slope: −0.002 [95% CI: −0.03 to
       0.02], p = 0.85).**" Method, verbatim: "46 studies analyzing 32,000 quotations/references...
       Literature search, data extraction, and risk of bias assessments were performed independently by
       two raters... protocol pre-registered on OSF." Conclusion, verbatim: "**Quotation errors remain a
       problem in the medical literature, with no improvement over time.**" And the sentence that ends
       the argument, from the Discussion, verbatim: "**Several remedies (Table 2) have been repeatedly
       recommended but the situation has not improved.**" **The design is the point.** The observation
       window spans the decades in which reference managers, DOIs, CrossRef and automated
       reference-integrity checking drove *pointer* error toward zero. If structural citation gates
       caught claim error, quotation accuracy should have risen over that period. **The slope is −0.002
       and the p-value is 0.85.** Two further verified findings sharpen it: risk-of-bias score was not
       associated with error rate (slope −0.11 [−0.27–0.04], p = 0.14), and journal impact factor was
       associated but trivially — the authors write, verbatim, "**only a weak negative correlation with
       journal impact factors explaining merely 7.5% of the variance**," i.e. the most heavily edited
       journals in the world are barely better.

    5. **Bakker, C., Theis-Mahon, N. & Brown, S.J. (2023), "Evaluating the Accuracy of scite, a Smart
       Citation Index," *Hypothesis: Research Journal for Health Information Professionals* 35(2).** —
       **VERIFIED** (full PDF retrieved and read this run, including Table 1 and the sample flow).
       Already held in the register as PREMISE-178's incorporated challenge; re-retrieved because the
       direction specifically asked for scite's precision. **Table 1, verbatim: Supporting — Precision
       1.0, Recall 0.05, F 0.096. Contrasting — Precision 0.0, Recall 0.0, F 0.0. Mentioning —
       Precision 0.41, Recall 1.0, F 0.58.** **The precision of 1.0 is the only "high precision" figure
       my direction has, and it must not be used, because its numerator is two.** From the Results,
       verbatim: "Of the 98 citations that were classified, scite found that **2 (2%) were supporting**,
       96 (98%) were mentioning, and **0 (0%) were contrasting**... We agreed with two citations scite
       had indicated were supporting." **Precision 1.0 on 2 of 2 is the same inferential move the intake
       warns against in the other direction**, and I flag it here so it is not imported later as
       evidence that automated classifiers are precise. The coverage finding is separately fatal for any
       C2A2 application: "**In 97 cases (31%) the referenced article was in scite, but the systematic
       review's citation to it was not.** As scite did not have access to the full text, **118 (37.7%)
       of the references were unclassified.**" Roughly one citation in three was classifiable at all.
       The authors' own limitation, recorded in fairness: "Retraction is a relatively rare and extreme
       publication state... this does limit the generalizability of our findings."

    6. **Rife, S.C., Nicholson, J.M., Uppala, A. & Rosati, D. (2025), "Reply to Bakker et al.,"
       *Hypothesis*, doi:10.18060/28018.** — **SECONDARY** (abstract and an editorial restatement read
       from a third-party aggregator, `lacuna.tiptreesystems.com`; **the publisher PDF at
       journals.indianapolis.iu.edu was refused by the fetch provenance rule and was NOT retrieved**.
       The body prose on the aggregator page is an LLM-generated restatement, not the authors' text, and
       nothing from it is quoted here as the authors' words except the abstract). Included because it is
       the strongest available rehabilitation of source 5 and it is a real methodological point.
       Abstract, verbatim: "**we argue that Bakker et al.'s assessment is incorrect, and that their
       conclusions are due to their definition of what constitutes supporting or contrasting citations.
       Additionally, Bakker, et al. restricted their analyses to citations of retracted works in
       systematic literature reviews, which artificially limits the types of statements that could be
       considered supporting or contrasting a specific claim.**" The substance is a label-mismatch
       objection: Bakker et al. coded "supporting" as *cited without noting the retraction* and
       "contrasting" as *noted the retraction*, whereas scite's model is trained to detect **new
       evidence** that agrees or disagrees. That is a fair criticism of the construct. **Two things stop
       it from helping me.** (i) Nicholson is scite's co-founder and Rife, Uppala and Rosati are
       scite-affiliated; this is the vendor replying to its own evaluation, which is disclosed here
       rather than discounted silently. (ii) **The reply supplies no alternative accuracy figure at
       all.** It argues the measurement was wrong; it does not produce a right one. For C2A2 the net
       effect is to move the automated-polarity question from "measured poor" to **"unmeasured"** — and
       PREMISE-178's clause forbidding an automated substitute survives either way, because an
       unmeasured classifier is not an available substitute for the same reason a poor one is not.

    7. **DO-NOT-CITE — figures encountered and deliberately excluded.** (a) "**Error rates of 25%–54%**"
       for reference accuracy across disciplines, and per-specialty figures ("major citation errors 10.3%,
       minor 17.2%, qualitative quotational errors 35.2%, quantitative 47%" in emergency medicine;
       "21.2% overall"; "22.9% in critical care nursing") — all **search-layer summaries of primaries I
       did not retrieve**. (b) The claim that the SourceCheckup verifier **exceeded** inter-doctor
       agreement — SECONDARY, see source 2; the 88% figure is verified, the "exceeded" claim is not.
       (c) Any historical claim that requiring authors to submit **photocopies of cited first pages**
       reduced error — I searched for this specifically at the direction's request and **found the
       practice described but no study measuring its effect**; the search layer said so explicitly. (d)
       Mogull 2017 and Jergas & Baethge 2015 figures are already in PREMISE-148/178 and I did **not**
       re-retrieve the primaries this run; where I refer to them I am citing **the register**, not the
       papers. **The rating below depends on none of these.**

  Strength of challenge: **Weak.** (Reading per the polarity note: the case that the two defects are
    outliers rather than instances of a base rate is weak. 14b's inference stands.)

    Limb split:
      - **"Structural citation gates catch claim error": NO evidence found, and one measurement
        against.** This is the direction as literally assigned and it returns empty. Source 3 separates
        citation error from quotation error as distinct classes and measures the latter at a 20% median
        *inside* the edited literature; source 4 shows that thirty years of improvement in the
        structural layer produced a quotation-accuracy slope of −0.002 (p = 0.85). **The one literature
        that could have shown gates catching claim error is the one that shows they have not.**
      - **"A claim-fit check works": STRONG evidence found — and it is not a citation gate.** Source 1's
        human figure (89.1 F1, 94.8 precision, two independent readers, source and claim in hand) and
        source 2's 88% automated agreement both establish that the check C2A2 omitted is tractable,
        cheap and near-expert. **This is the genuine partial and it is worth more than the rest of the
        file: it converts "we cannot verify claim-fit" into "we did not."** But it supports *build the
        missing check*, not *the defects are rare*.
      - **"Weak local gate rather than a general limit": SUPPORTED, and the register already said so
        louder than the literature does.** REVISE-393's own words, read at source this run: "**the
        finding is an ENFORCEMENT failure against premises the register validated three weeks ago.**"
        PREMISE-178 already requires reading the body. **The gate as specified in the register DOES
        include claim-fit; the gate as run does not.** That is the strongest true thing in my
        direction — and it makes the situation worse, not better, because it means the defect is not a
        design gap that argues for caution but an unenforced rule that argues for a forcing function.
      - **The second defect is not covered by any of this.** The paraphrase limb — a file whose own
        correctly-graded High anchors defeat its reading, concealed by a charitable gradient paraphrase
        standing where a categorical claim belonged — is **not a citation-to-source problem at all**. No
        system in sources 1, 2 or 5 takes as input "this document's own graded internal anchors versus
        this document's stated reading." SciFact-family systems verify a claim against an *external*
        abstract. **I searched for work on internal-consistency checking against a local evidence
        grading and found none.** Reported as **insufficient search, not as absence of evidence** — but
        note that even a perfect claim-fit gate would have passed this defect, because every citation
        pointed where it said and the paraphrase was charitable rather than false. **The item's two
        defects are not one phenomenon, and a remedy scoped to the first leaves the second untouched.**

  THE BASE-RATE QUESTION, TAKEN HEAD ON AS INSTRUCTED. **Is 2 defects evidence of a base rate? No — and
    the item does not need it to be, which is why the objection fails.** Four steps.

    (1) **The formal objection is correct and irrelevant.** Two defects with no stated denominator
      estimate nothing. PREMISE-168 is explicit: "A YIELD FIGURE PUBLISHED WITHOUT ITS DENOMINATOR IS A
      STATEMENT ABOUT THE PRODUCER, NOT ABOUT THE SPACE," and PREMISE-101 holds that counts are
      properties of a (scope, method, time) reading. Neither the item nor this file may convert 2 into a
      rate. The standard small-n apparatus does not help either: the rule of three bounds a rate from
      *zero* observed events (0 to 3/n at 95%); with two events and no n it yields nothing.
    (2) **But the rate is already measured externally, and the item inherits it rather than inferring
      it.** Source 4: **16.9% of quotations incorrect, 8.0% major**, over ~32,000 quotations in 46
      studies, two independent raters, pre-registered. Source 3: **20% median quotation error** over 66
      surveys. The register's PREMISE-148 carries 25.4% (Jergas & Baethge 2015) and 14.5% with 64.8% of
      content errors major (Mogull 2017). **Under any of these, two defects is not an outlier — it is
      an order of magnitude below what the external rate predicts for a corpus of this size.** The
      inference that survives is therefore the opposite of the one my direction wanted: **the pipeline
      is under-detecting.**
    (3) **And the in-house count is not two.** Read at source this run: PREMISE-178's founding instance
      is "**four ids cited for claims their own bodies argue against, every one of which passed both
      checks**" (2026-08-18). REVISE-393 records that "**two hand-reading frames found five citation
      defects across five days of material and every one of the five resolves**" (2026-08-26). Today
      adds two. **That is at least eleven first-party instances across three separate discovery events
      nineteen and twenty-seven days apart — every one found by a human or an agent reading the body,
      and not one found by a gate.** Three independent discoveries at three separate times, by
      different frames, is precisely the pattern that rules out "outlier." A single cluster could be
      chance; a recurrence every eight days is a rate.
    (4) **The test that would settle it was specified nineteen days ago and has not been run.**
      REVISE-393 item (3), verbatim: "**Draw the sample.** 40 random attributable PRS references; open
      each cited record; score the claim made from it as substantiated / partial / not substantiated,
      using the major/minor split from the medical literature so the number is comparable; report with
      a binomial interval. **Cost is hours.**" It is still an open REVISE. **Until it is run, "these are
      outliers" is not a hypothesis the estate is entitled to — it is the absence of a measurement that
      was costed at hours and named by the register itself.** REVISE-393 also states the estate's own
      projection: "if general rates transfer even loosely, 979 references carry on the order of 10²
      quotation-level defects, of which roughly two thirds would be major; **the five found by hand are
      a DENSITY ESTIMATE, not an incident count.**"

  Summary: The direction asked for evidence that structural citation gates catch claim error, and the
    literature that would contain it instead contains its refutation. Wager & Middleton's Cochrane
    methodology review separates citation error (38% median) from quotation error (20% median) as
    distinct defect classes and measures the second *inside* journals that already run reference
    checking; its positive findings on editorial intervention are associational, drawn from two studies
    in an evidence base the authors themselves call inadequate, and the one relevant randomised trial
    was null. Jergas and Baethge's 2025 meta-analysis of ~32,000 quotations then closes the question
    directly: quotation error sits at 16.9% (8.0% major) and the meta-regression across the decades in
    which DOIs, reference managers and automated citation checking eliminated pointer error shows a
    slope of −0.002 (p = 0.85), with the authors writing that remedies "have been repeatedly recommended
    but the situation has not improved." What my direction did find is real and valuable but does not
    say what was wanted: the claim-fit check itself works — two independent human readers agree at 89.1
    F1 and 94.8 precision on SciFact when handed the source and the claim, and GPT-4 agrees with a panel
    of medical doctors 88% of the time on source relevance — so the omitted step is tractable, cheap and
    near-expert, and C2A2's failure is a weak *local* gate against a rule the register already validated
    at High confidence in PREMISE-178. On the base rate: two defects with no denominator prove nothing,
    but the item never needed them to, because the external rate is measured and large and the in-house
    count is at least eleven across three discovery events in twenty-seven days, every one found by
    hand-reading and none by a gate.

  Specific risks: (stated for the case that my direction is wrong, which on this evidence it is)
    - **The estate is on its third arrival at a premise it validated at High confidence on 2026-08-18,
      and each arrival has consumed a full 15a/15b search cycle.** PREMISE-178, PREMISE-132, PREMISE-148
      and PREMISE-172 between them settle the first limb completely. The grep-only intake pre-check has
      now missed PREMISE-178 twice with search terms that hit its Statement line. **The cost is not
      embarrassment; it is that the search budget spent re-deriving settled ground is the budget not
      spent on the 40-reference sample, which is the only thing that would move the question forward.**
    - **"Outlier" is the most dangerous available reading and this file cannot supply it.** If the
      estate concludes from a Weak challenge that the two defects are rare, it will decline the sample,
      and REVISE-393 names the consequence precisely: a zero on an insensitive instrument "TERMINATES
      INQUIRY — the headline discourages the hand-reading that is currently the only thing finding
      defects."
    - **The automated remedy will under-deliver at exactly the point C2A2 needs it.** Source 1's
      zero-shot abstract-level F1 is 30.7–47.2. C2A2's corpus is scholastic Latin philosophy,
      contemplative theology and consciousness science with no in-domain training data, and the Aquinas
      instance (I-II Q.53, whether habits diminish) is a discrimination between *adjacent articles of
      the same question* — the hardest case in the class. **A system benchmarked at 72.5 on biomedical
      abstracts should not be assumed to reach half that here.** Source 5's coverage finding compounds
      it: roughly two-thirds of citations were unclassifiable for want of full text.
    - **The cross-connection machinery is the live exposure and the item names it correctly.** The
      intake's own sentence — the machinery "paraphrases a tradition's claim into a shared column before
      looking for tension, which is the exact step that failed" — describes a step for which **no
      verification literature exists at all**. The paraphrase limb has no covering premise, no external
      source, and no benchmark. It is the genuinely new half of PRESUMPTION-988 and it is the half
      nobody has searched.
    - **A "read the body" rule filed as a rule will fail the way PREMISE-178's own challenge predicted.**
      That challenge, read at source this run, warns that "a read-the-body RULE is itself an
      identifier-layer move if compliance is recorded rather than measured" (carried to REVISE-349 and
      the G2 flag). **The rule already exists and was not enforced.** Filing it again is the
      PREMISE-138 pathology — repetition inside a channel with no effector.

  Mitigations available:
    - **Do not mint a premise. Attach to PREMISE-178 and reopen REVISE-393/397.** This is PREMISE-138's
      prescribed handling and PREMISE-186 set the precedent for exactly this claim four weeks ago.
      What attaches is new: two instances, the paraphrase failure mode, and the C2A2 cross-connection
      exposure.
    - **Run the 40-reference sample.** It is specified, costed at hours, nineteen days old, and it is
      the only action here that produces a number rather than a position. Report it with a binomial
      interval against the 16.9% / 8.0% benchmark from source 4 so it is comparable to the external
      literature by construction.
    - **Adopt the two-independent-reader design, because that is where the 89.1 comes from.** Source 1's
      human figure is an *inter-annotator* figure — two readers, independently, source and claim in
      hand. It is not a figure about one careful reader. Source 4's own methodological recommendation
      says the same thing, verbatim: "**two raters should independently look into quotations.**" This
      also matches PREMISE-148 clause (2) (structural duplication is the control shown to work) and
      PREMISE-162's capture-recapture requirement. **A single-reader "read the body" rule is not the
      intervention these numbers measure.**
    - **Name the class.** REVISE-393 item (2) and REVISE-397 item (1) both call for it and it has not
      been done: the field's term is **quotation error**, or "resolvable but unsubstantiated." A class
      with no name cannot be counted, trended or assigned, and "dead citation" currently monopolises the
      vocabulary.
    - **If an automated claim-fit check is built, benchmark it in-domain before trusting it, and treat
      it as a triage filter with a recall target, not a gate.** Source 5's scite numbers show what a
      production classifier does when the domain shifts: recall 0.05 on supporting, 0.0 on contrasting.
      Source 2's 88% is the target; source 1's zero-shot 30.7–47.2 is the realistic starting point.
    - **Search the paraphrase limb separately and do not let it ride on this file.** It is a distinct
      failure mode with no covering premise and no located literature. The nearest tractable framing is
      *charitable paraphrase as a construct-validity failure in a normalisation step* — and
      SYSTEMIC-RISK-2026-08-26-A (construct validity in automated proxies) is the existing flag it
      belongs under.
    - **Raise the shared-fetch-cache channel as a register item** (see attestation). It is a fifth
      correlation channel and also a suppression channel, and PREMISE-111 does not name it.

  STEELMAN:
    Item: PRESUMPTION-988
    Strongest counterargument (i.e. the strongest case for my assigned direction, that the gate does
      catch claim error and these two are outliers): **The item commits a category error about what the
      gate was ever for, and then reads a design boundary as a failure.** A citation-integrity check is
      a *referential* check: it certifies that the pointer resolves, the identifier is correct, and the
      label matches the referent. It has never, in any field, claimed to certify semantic entailment —
      that is why the literature has a *separate name* for the other thing, and Wager & Middleton's
      review reports the two as separate line items with separate rates. **A tool performing to
      specification is not a tool that failed.** And the remainder of the item's force comes from a
      denominator it does not have. Two defects, hand-found, in an unstated population, on a day when
      two frames were specifically hunting for defects — that is a *search-effort* artefact, and its
      expected yield rises with the looking, not with the underlying rate. The external medical figures
      do not rescue it either: 16.9% is measured on numeric and inferential claims in biomedical
      research articles, where "the source supports the assertion" has a sharp truth condition, whereas
      C2A2's material is philosophical and theological exposition where a citation to a *question* of the
      Summa rather than the precise *article* is a granularity slip of a kind the medical instrument
      would not even code. **PREMISE-148 concedes this explicitly and it is load-bearing**: "Direction
      and MECHANISM transfer cleanly; **RATE does not**." So the honest position is: the gate did its job,
      a second and different check is needed, that check is demonstrably buildable at 88–89% agreement
      (sources 1 and 2), and until the 40-reference sample is drawn nobody — including 14b — knows
      whether the in-corpus rate is 1% or 20%. **Treating two hand-found instances as a base rate is the
      same inferential error as reading scite's precision of 1.0 off a numerator of two**, and this file
      flags that error in one direction while the item commits it in the other.
    What would need to be true for C2A2 to be safe: **(a)** the two defects would have to be drawn from a
      population whose rate is genuinely low — **untested, and the test is nineteen days overdue**;
      **(b)** the referential/semantic split would have to be a *stated* boundary of the C2A2 gate rather
      than an unnoticed one — and it is not, which is the whole finding: REVISE-393 shows the gate's
      output was published as "**zero dead citations**" and read as citation *health*, so the boundary
      was not merely unstated, it was actively overstated; **(c)** the rate-transfer objection would have
      to be the only thing at issue, and it is not — PREMISE-178 is about **polarity and support, not
      rate**, and it holds at High confidence "whatever the lexical instrument's error profile turns out
      to be"; **(d)** the search-effort objection would have to explain three discovery events, and it
      does not — the four ids of 2026-08-18, the five of 2026-08-26 and the two of today were found by
      different frames on different days looking for different things, which is the signature of a
      population, not of one hard look. **The steelman's real contribution is (b) restated as a
      remedy**: the correct action is not to distrust the gate but to *restate its scope truthfully and
      build the second check beside it* — which is REVISE-393 item (1) verbatim and is still open.
    How to test: **Two tests, both in-house, both cheap, and the first is already written.**
      **Test 1 — the sample (settles the base rate).** REVISE-393 item (3) as specified: 40 random
      attributable references, open each cited record, score substantiated / partial / not substantiated
      with the major/minor split, binomial interval, compared against 16.9% total and 8.0% major from
      source 4. Materially below → the steelman is supported and the transfer objection is vindicated;
      at or above → the two defects are a density estimate and the corpus carries on the order of 10²
      defects. **Do this with two independent readers on the same 40**, per source 4's own
      recommendation and PREMISE-148 clause (2) — the second reader also yields a capture-recapture
      estimate of what a single reader misses, which is the quantity PREMISE-162 requires and which no
      single-reader design can produce.
      **Test 2 — the granularity discriminator (settles the steelman's best objection).** The steelman's
      sharpest point is that the Aquinas defect is a *granularity slip* (question vs. article) that the
      medical instrument would not code as a quotation error. Test it: of the eleven known in-house
      instances, classify each as (i) pointer correct, claim absent from the cited unit but present
      elsewhere in the cited work — a granularity slip; (ii) pointer correct, claim absent from the
      cited work entirely; (iii) pointer correct, cited work **contradicts** the claim. Source 4 and
      PREMISE-148 both report roughly half of errors are major, i.e. classes (ii)/(iii). **If C2A2's
      instances are overwhelmingly class (i), the steelman is right that the external rate does not
      transfer and the remedy is a citation-granularity rule, which is far cheaper than a claim-fit
      gate. If class (ii) or (iii) appears, the steelman is refuted on its own chosen ground.** The
      intake's own description of the Aquinas instance — "an article that **does not contain** the
      claim" — points at (ii), but eleven instances is enough to classify and nobody has.
      **Neither test needs external data, authorisation, or a new search.**

  SYSTEMIC-RISK-FLAG:
    Date: 2026-09-14
    Affected items: PRESUMPTION-988 (this item); PRESUMPTION-877 / REVISE-397 (2026-08-26);
      ASSUMPTION-1206 / REVISE-393 (2026-08-26); ASSUMPTION-1131 / PREMISE-178 (2026-08-18).
      Adjacent: PRESUMPTION-559 / PREMISE-132; PRESUMPTION-695 / PREMISE-148.
    Common vulnerability: **The intake's grep-only register pre-check does not find covering premises,
      and the pipeline is consequently re-deriving High-confidence ACTIVE ground on an eight-to-
      nineteen-day cycle.** PREMISE-178's Statement contains the words `citation` and `anchor`; the
      intake grepped both and reported "no covering premise found." This is the **second** miss of the
      same premise by the same method. The failure is not laziness — it is that a 700 KB register
      answers a `grep -c` with 39 hits for `citation` and 114 for `gate`, so a term-presence check
      returns a number rather than an answer and the reader treats a high count as noise. **The
      second-order cost is the one that matters: three full search cycles have been spent on a settled
      claim while the one cheap measurement the register itself specified (REVISE-393 item (3), costed
      at hours) has gone unrun for nineteen days.** The pipeline is substituting search for
      measurement — which is the same shape as the defect under examination, at the level of the
      pipeline rather than the citation: **a procedure that certifies form is being read as a check on
      substance.**
    Literature basis: Wager & Middleton, Cochrane MR000002.pub3 (a process audit is not a product
      audit; "surprisingly few studies have evaluated the effects of technical editing rigorously");
      Jergas & Baethge 2025, *Res Integr Peer Rev* 10(1):13 ("several remedies have been repeatedly
      recommended but the situation has not improved" — recommendation without enforcement produced a
      slope of −0.002 over three decades). In-house: PREMISE-138 (repetition inside a channel with no
      effector is not a remedy), PREMISE-148 clause (3) (process conformance does not license an
      inference to product quality), PREMISE-172 (a pass mark carries no information about what was not
      examined).
    Risk level: **High.**
    Recommendation: **(1)** Replace the intake pre-check's term-presence grep with a **statement-line
      read**: `grep -n "^  Statement:" -A3` over `validated_premises.md` returns 169 statements and is
      readable in one pass; term counts are not. **(2)** Before any item is queued, require the intake
      to name the **three nearest ACTIVE premises and say why each does not cover it** — an explicit
      non-coverage argument, not a null result. **(3)** Treat a third arrival of the same claim as a
      **hard stop on further searching** and a mandatory routing to the open REVISE. **(4)** Run
      REVISE-393 item (3).

  Search scope: **Comprehensive for the citation limb; preliminary-to-absent for the paraphrase limb,
    and that is stated as insufficient search rather than as absence of evidence.** Six angles were
    searched: (i) editorial reference-verification policies and their measured effect; (ii) the
    reference-checking intervention literature, including the historical photocopy-of-first-page
    requirement, for which **the practice was located but no effectiveness study was**; (iii) scientific
    claim verification (SciFact / MULTIVERS / SourceCheckup / CiteAudit); (iv) the scite classifier and
    the 2023–2025 accuracy exchange in both directions; (v) time-trend evidence on whether structural
    citation improvements moved quotation accuracy; (vi) the small-numerator statistics of the
    base-rate question. **Five primaries were retrieved and read this run** — the MULTIVERS PDF in full
    (Tables 2 and 5), the Bakker et al. PDF in full (Table 1 and sample flow), the Jergas & Baethge 2025
    open-access full text (Methods, Results, Discussion), the Cochrane MR000002.pub3 structured abstract
    in full, and the SourceCheckup arXiv abstract verbatim — and the rating rests on those alone. **Two
    retrieval failures are named rather than worked around:** the *Nature Communications* SourceCheckup
    page was refused by the session-shared fetch cache (see attestation), and the publisher PDF of the
    Rife et al. reply was refused by the fetch provenance rule, so that source is SECONDARY. PMC was
    reCAPTCHA-blocked throughout, as in prior runs. **No unverified number appears in the rating, and
    the excluded figures are named in source 7 so a later run does not re-import them believing them
    checked.** The genuinely under-searched question is the second defect: *charitable paraphrase
    defeating a document's own graded internal anchors*. I found no literature on it and I am not
    supplying a proxy. It should be queued as its own item.

  Recommendation: **NO-CHALLENGE-FOUND** — with one narrow PARTIAL recorded so it is not lost: **the
    claim-fit check is demonstrably tractable (89.1 F1 human, 88% automated agreement with an expert
    panel), which locates C2A2's failure in an unenforced local gate rather than in a general limit.**
    That finding argues for building and enforcing the missing check; it does **not** support the
    proposition my direction was assigned, that the two defects are outliers. On the base-rate question
    asked head-on: two defects prove no rate, but the item does not rest on them — the external rate is
    measured at 16.9% total / 8.0% major over ~32,000 quotations with no improvement across three
    decades of structural-citation progress, and the in-house count is at least eleven across three
    discovery events in twenty-seven days, every one found by reading and none by a gate.
