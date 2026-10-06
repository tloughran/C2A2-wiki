SEARCH-FOR-PRESUMPTION-982:
  Date searched: 2026-09-14
  Original item: PRESUMPTION-982
  Original statement: [inferred] That when two runs report different numbers for the same quantity, one is
    wrong — rather than the quantity being operationally undefined. Tonight: three figures for `connected`
    in one vault on one day (65 / 75 / 82), with a mechanism found by a third run that makes **both**
    plausible (wikilink stems collide across 419 duplicated filenames); four figures for the literature
    queue (163/151/137/371); and two runs asserting contradictory tenses about whether 15d had run.

  POLARITY DECLARATION — READ BEFORE RECONCILING:
    14b's intake assigned 15a the direction "construct validity and operational definition in
    software/organisational metrics; evidence that specifying the operational definition resolves
    inter-instrument disagreement." That direction is the **negation** of the presumption as stated, not
    its confirmation. The presumption says *one run is wrong*; the assigned direction searches for *the
    quantity is under-defined*. 15b was assigned the presumption's own content ("evidence that adjudicating
    between divergent metrics is the right move; when disagreement *does* indicate simple error").
    This file therefore reports two things that must not be collapsed:
      (a) Strength of the evidence for the **assigned direction** (under-definition): **Strong**.
      (b) Strength of the evidence for the **presumption as literally stated** ("one is wrong"):
          **None found on this channel**, because this channel was not pointed at it.
    For the reconciliation table in provenance_protocol.md, treat this file as the AGAINST arm by content
    and 15b's file as the FOR arm, or the polarity will invert the verdict. Flagged rather than silently
    corrected, because the inversion is 14b's and may be deliberate.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-982
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from two cross-run collisions visible only to an end-of-day pass over the whole estate.
        Pre-check declared weak by 14b itself: grep (not read) of a 700 KB premise register on generic
        terms (`metric`, `definition`, `divergence`, `count`, `census`), no covering premise found.
      15a: Searched metrology, measurement theory, software-metrics validation, inter-rater reliability,
        and the analytic-variability/reproducibility literature for evidence that a quantity can be
        operationally under-defined such that two divergent counts are both correct, and for evidence that
        specifying the operational definition resolves inter-instrument disagreement.
    Current status: NO-SUPPORT-FOUND (for the presumption as stated) / SUPPORTED–Strong (for the assigned
      direction). See POLARITY DECLARATION.
    Independence caveat (mandatory, per PREMISE-111): 15a and 15b ran in separate contexts on this item, so
      the read channel is closed. PREMISE-111's standing discount applies: the read channel is the weakest
      of at least four correlation channels, and closing it is not independence. Both arms read the same
      item text, the same registry and the same premise statements, and MONITOR-486's three-arm dependence
      measurement remains unrun. Any later convergence between this file and 15b's must be discounted
      accordingly and must not be described as independent confirmation.

  Search scope: **Comprehensive on the core limb, preliminary on the periphery.**
    Comprehensive: formal metrology's treatment of an incompletely specified measurand (VIM/JCGM 200);
      the software size- and defect-counting definition literature (SEI CMU/SEI-92-TR-20; function-point
      inter-rater reliability); construct validity as applied to software metrics (Kaner & Bond;
      Cronbach & Meehl upstream).
    Preliminary: the many-analysts / analytic-variability reproducibility literature (two flagship studies
      retrieved at summary level only); semantic heterogeneity in data integration; bibliometric
      database-divergence; method-comparison statistics; epidemiological case-definition divergence.
    Searched and NOT retrieved: ISO/IEC/IEEE 15939:2017 and the GQM primary literature (Basili/Rombach) —
      both paywalled or not fetched this run; they are named below only as UNVERIFIED pointers and no
      content is attributed to them beyond the measurement-information-model vocabulary.
    Searched and NOT found: any study of inter-run numeric divergence among autonomous agent instruments
      over a shared document corpus. See NOVELTY-FLAG.

  Supporting evidence found: Yes — strongly, for the assigned direction (under-definition), with an
    important limit on the "specifying resolves it" clause.

  Sources:

    1. Park, R.E. et al., 1992. "Software Size Measurement: A Framework for Counting Source Statements."
       CMU/SEI-92-TR-20 / ESC-TR-92-020, Software Engineering Institute, Carnegie Mellon University.
       — **VERIFIED** (full report text retrieved this run; Chapters 1–3 and the framework steps read
       directly). The single most on-point source found. Its entire premise is that a reported software
       count is uninterpretable without an attached definition, and its worked motivating example is a
       count reported without one, which the authors say can be "misunderstood by a factor of three or
       more" (§1.2). The report's two design criteria are exactly the estate's two failure modes:
       *Communication* (will others know precisely what was included and excluded?) and *Repeatability*
       (would someone else repeat the measurement and get the same result?). The remedy is a definition
       checklist enumerating attributes and, for each, explicit inclusions and exclusions, with the
       completed definition attached to every measurement record and report (framework steps 1–10, §2).
       Directly applicable: the `connected` divergence is an inclusion/exclusion question — does a
       colliding wikilink stem across 419 duplicated filenames resolve to one node or to many — which is
       precisely an unrecorded attribute value in Park's sense. Note as coincidence only, with no
       evidential weight: Park's illustrative ambiguous figure is "163,000 source code instructions",
       and 163 is the first of the estate's four literature-queue figures.

    2. JCGM 200:2012, *International Vocabulary of Metrology (VIM3)*, entry 2.27 "definitional
       uncertainty." BIPM/JCGM.
       — **VERIFIED** (entry retrieved in full from jcgm.bipm.org this run, including all three notes).
       Formal metrology has a named concept for exactly what this presumption denies: definitional
       uncertainty is the component of measurement uncertainty resulting from the finite amount of detail
       in the definition of a measurand. NOTE 1: it is the practical minimum measurement uncertainty
       achievable in any measurement of a given measurand. NOTE 2: any change in the descriptive detail
       leads to another definitional uncertainty. NOTE 3: ISO/IEC Guide 98-3:2008 D.3.4 and IEC 60359 call
       the same concept "intrinsic uncertainty." The existence of this term in the international
       measurement vocabulary is decisive against the presumption's dichotomy: divergence between two
       faithful measurements of an under-specified measurand is a recognised, quantified, non-error
       category. NOTE 2 is also the strongest caveat on the "specifying resolves it" clause — see Caveats.

    3. Cronbach, L.J. & Meehl, P.E., 1955. "Construct Validity in Psychological Tests." *Psychological
       Bulletin* 52(4): 281–302.
       — **VERIFIED** (full text retrieved from the Classics in the History of Psychology archive this
       run; the construct-validation and nomological-network passages read directly). The foundational
       statement that construct validation is required precisely whenever a test is interpreted as a
       measure of an attribute that is not operationally defined, and that a construct's meaning is fixed
       by the nomological network of laws it enters, not by a single measurement operation. Establishes
       the general form of the estate's problem: `connected` is a construct, not a base measure, and until
       a nomological network or an explicit operationalisation fixes it, two counts of it are not rival
       estimates of one number.

    4. Kaner, C. & Bond, W.P., 2004. "Software Engineering Metrics: What Do They Measure and How Do We
       Know?" *10th International Software Metrics Symposium (METRICS 2004)*.
       — **VERIFIED at abstract and introduction level** (primary PDF retrieved from kaner.com this run;
       abstract read verbatim, body not read in full). Carries Cronbach & Meehl's construct validity into
       software measurement, and makes the argument that matters here: IEEE Standard 1061 exempts *direct*
       measures from validation, but few or no software engineering attributes are simple enough for
       measurement of them to be direct, so all metrics require validation. The paper's worked application
       is to bug counts, concluding that they capture only a small part of the meaning of the attributes
       they are used to measure. The estate's `connected` and its literature-queue count are exactly the
       kind of apparently-direct count that this paper says is not direct.

    5. Kampstra, P. & Verhoef, C., "Reliability of Function Point Counts." VU University Amsterdam,
       Department of Computer Science.
       — **VERIFIED at abstract level** (primary PDF retrieved from cs.vu.nl this run; abstract read
       verbatim, body not read). The best direct evidence found for the "specifying resolves it" clause:
       in a case study of 311 projects and 58,143 function points at one large institution, where counting
       was performed by certified professionals under a standard method, the authors found no statistical
       evidence for systematic differences between counters and concluded the counts were a reliable base.
       That is: fully specified rules plus certified instruments produced no detectable inter-rater
       divergence. The same abstract states that lines of code "seem unambiguous" but that different
       definitions can cause variations of 500%. **DO-NOT-CITE the 500% figure as a verified measurement**
       — it is the authors' summary of other work, appears in their abstract rather than in a result I
       read, and its derivation was not retrieved. Publication year not established this run; cite by
       author, title and institution only until confirmed.

    6. Herzig, K., Just, S. & Zeller, A., 2013. "It's Not a Bug, It's a Feature: How Misclassification
       Impacts Bug Prediction." *ICSE 2013*, International Conference on Software Engineering.
       — **VERIFIED** (primary PDF retrieved from st.cs.uni-saarland.de this run; the abstract and
       introduction read directly from the primary). Manual examination of more than 7,000 issue reports
       across five open-source projects found 33.8% of all bug reports misclassified — resulting in a new
       feature, a documentation update or an internal refactoring rather than a code fix — and on average
       39% of files marked as defective never had a bug. **Reported here because it cuts both ways and
       should not be suppressed**: it is simultaneously the strongest evidence that a named, standard,
       apparently-well-defined count ("bugs") is definition-relative, and evidence that some component of
       the divergence is genuine classification *error*, which is the presumption's own claim. The two
       mechanisms coexist in one dataset; neither excludes the other.

    7. Silberzahn, R., Uhlmann, E.L., Martin, D.P. et al., 2018. "Many Analysts, One Data Set: Making
       Transparent How Variations in Analytic Choices Affect Results." *Advances in Methods and Practices
       in Psychological Science* 1(3).
       — **SECONDARY** (search-layer summary and abstract only; primary not retrieved). Twenty-nine teams,
       61 analysts, one dataset, one question. Analytic approaches varied widely; 20 teams (69%) found a
       significant positive effect and 9 (31%) did not; 29 analyses used 21 unique covariate combinations.
       Crucially, neither analysts' prior beliefs nor expertise nor peer ratings of analysis quality
       explained the variation. The reported effect-size range (odds ratios 0.89–2.93, median 1.31) is
       **DO-NOT-CITE as verified**. The relevance is the negative finding: quality and competence did not
       predict which number a team produced, so "one of them is wrong" is not recoverable by ranking the
       analysts — which is what "pick the more careful run" amounts to in the estate.

    8. Botvinik-Nezer, R., Holzmeister, F., Camerer, C.F. et al., 2020. "Variability in the Analysis of a
       Single Neuroimaging Dataset by Many Teams." *Nature* 582(7810): 84–88.
       — **SECONDARY** (search-layer summary and abstract only; primary not retrieved). Seventy independent
       teams, one dataset, nine pre-specified hypotheses; no two teams chose identical workflows, and the
       flexibility produced sizeable variation in hypothesis-test outcomes even where statistical maps were
       highly correlated at intermediate pipeline stages. Two findings bear directly: (a) specifying the
       *question* in advance did not prevent divergence — only specifying the *pipeline* would have; and
       (b) a meta-analytic aggregation across teams yielded a significant consensus, i.e. the constructive
       move was combination, not adjudication.

    9. UK Health Security Agency / Office for National Statistics — the two England COVID-19 mortality
       measures (deaths within 28 days of a first positive test vs. deaths with COVID-19 mentioned on the
       death certificate); and the associated comparison paper in the *International Journal of
       Epidemiology* (2023, article dyad116).
       — **SECONDARY/UNVERIFIED** (agency explainers and article abstract at search-layer only). A
       real-world, high-stakes instance of the estate's exact situation: two fully specified counts of
       "the same quantity" published side by side, persistently divergent, with the divergence explained
       by definition and purpose (rapid public-health response vs. robust attribution) rather than by
       either being wrong. The institutional resolution was disclosure of which definition was in use, not
       convergence on a single number. Note the reverse-direction caveat: during March–April 2020 part of
       the divergence *was* an artefact (limited testing capacity), i.e. under-definition and instrument
       failure were present in the same series at different times.

   10. Halevy, A.Y. "Why Your Data Won't Mix: Semantic Heterogeneity." *ACM Queue* 3(8): 50–58.
       — **UNVERIFIED** (search-layer summary only; primary not retrieved; the search layer returned
       conflicting years, 2003 and 2005, and vol. 3 iss. 8 implies 2005 — **DO-NOT-CITE the year until
       confirmed**). Named here for the concept, not for any figure: in data integration, sources that
       use the same attribute name for differently-scoped things are the normal case rather than the
       pathological one, and the resolution is an explicit semantic mapping. The estate's colliding
       wikilink stems across 419 duplicated filenames is a textbook instance — the identity function for
       "a node" differs between instruments, so the two counts range over different entity sets.

   11. Bland, J.M. & Altman, D.G., 1986. "Statistical Methods for Assessing Agreement Between Two Methods
       of Clinical Measurement." *The Lancet*.
       — **SECONDARY** (search-layer summary only; primary not retrieved). Methodological rather than
       substantive support: the standard apparatus for two instruments measuring the same quantity assumes
       no gold standard and quantifies bias and limits of agreement, rather than designating one method
       correct. Its central polemic — that such comparisons are routinely analysed inappropriately — is
       the same error shape as the presumption.

   12. Kemerer, C.F., 1993. "Reliability of Function Points Measurement: A Field Experiment."
       *Communications of the ACM* 36(2).
       — **UNVERIFIED** (primary not retrieved; page range reported inconsistently by the search layer as
       85–87 and 85–97). The frequently repeated figures — roughly 12% difference for the same product by
       counters in the same organisation, and roughly 15% between pairs of raters using the standard
       method — are **DO-NOT-CITE as verified** and are recorded here only so that a later run does not
       rediscover them and treat them as established.

   13. ISO/IEC/IEEE 15939:2017, *Systems and Software Engineering — Measurement Process*.
       — **UNVERIFIED** (standard not obtained; vocabulary taken from search-layer summaries). Named for
       one structural point only: the standard's measurement information model distinguishes *attribute*,
       *base measure*, *derived measure* and *indicator*, and requires that a specific measurement method
       be designed to obtain a base measure for a specific attribute. On that model, `connected` in the
       estate has been reported as an indicator while never having been specified as a base measure with
       a stated measurement method — which is the structural diagnosis of the divergence.

  Strength of support: **Strong** for the assigned direction (under-definition). **None found on this
    channel** for the presumption as literally stated.

  Summary: Formal metrology already has a name and a definition for the phenomenon the presumption denies.
    VIM3 entry 2.27 defines definitional uncertainty as the uncertainty arising from the finite amount of
    detail in the definition of a measurand, and makes it the practical floor below which no measurement
    of that measurand can go — so two divergent faithful counts of an under-specified quantity are a
    recognised non-error category, not a contradiction awaiting a winner. The software-measurement
    literature says the same thing in the estate's own domain and at the estate's own object: the SEI's
    1992 counting framework exists because size counts reported without an attached inclusion/exclusion
    definition can be misunderstood by a factor of three or more, and Kaner & Bond argue that almost no
    software attribute is simple enough for its measurement to be direct, so counts that look
    self-evident — bug counts, and by extension node counts — are construct measures requiring validation.
    On the second clause, whether specifying the definition *resolves* the disagreement, the evidence is
    real but bounded. Kampstra & Verhoef's 311-project, 58,143-function-point case study found no
    statistical evidence of systematic differences between certified counters working under a standard
    method, which is the clearest demonstration available that specification plus instrument
    standardisation removes detectable divergence. But VIM3's NOTE 2 states that any change in descriptive
    detail leads to *another* definitional uncertainty, the England COVID-19 mortality series shows two
    fully specified counts diverging permanently and being resolved by disclosure rather than convergence,
    and the many-analysts studies show that specifying the question is insufficient where the pipeline
    remains free — with the Silberzahn result that analyst expertise and peer-rated quality did not
    predict which number a team produced, which removes the estate's implicit fallback of preferring the
    more careful run. The honest finding is therefore that specifying the operational definition converts
    an apparent contradiction into an interpretable, bounded spread; it does not abolish the spread.

  Caveats:
    - **The polarity inversion is the largest caveat.** This file supports the negation of the presumption
      because that is the direction 14b assigned. Read as a conventional 15a FOR file it will invert the
      verdict. See POLARITY DECLARATION.
    - **Under-definition and error are not exclusive, and the estate's own evidence contains both.** The
      item cites a third run finding a mechanism that makes 65 and 82 both plausible — that is
      definitional. It also cites two runs asserting contradictory *tenses* about whether 15d had run —
      that is a Boolean about a past event, not a quantity, and admits no definitional reconciliation. One
      of those two runs is simply wrong. The presumption should not be rejected wholesale on the strength
      of the numeric cases; Herzig et al. and the March–April 2020 COVID divergence both show the two
      mechanisms operating in one dataset.
    - **"Specifying resolves it" is supported only to a floor.** VIM3 NOTE 2 is explicit that re-specifying
      moves the definitional uncertainty rather than eliminating it. Kampstra & Verhoef's null is a
      single-institution result with certified counters and an established international counting
      standard; the estate has neither certification nor a standard, so the transfer is aspirational.
    - **Verification asymmetry.** The four sources doing the load-bearing work (Park, VIM3, Cronbach &
      Meehl, Kaner & Bond) were retrieved and read this run. The reproducibility flagships (Silberzahn,
      Botvinik-Nezer) and the method-comparison and data-integration sources were not, and their figures
      are marked DO-NOT-CITE. No numeric figure in this file should be quoted as verified except: Park's
      "factor of three or more" characterisation; VIM3's three notes; and Herzig et al.'s 33.8% and 39%.
    - **Domain transfer.** Every source concerns human analysts, certified counters, laboratory
      instruments or database indexes. None concerns LLM agent runs as measuring instruments over a
      document corpus. The measurement-theory machinery transfers by structure, not by demonstration.
    - **Publication-bias direction.** The measurement-definition literature (SEI, ISO, VIM) is normative
      standards advocacy and is not a neutral source on whether standardising definitions works. Its
      claims about the benefits of definition checklists are prescriptions, not findings.
    - **The pre-check weakness carries forward.** 14b declared its own premise-register pre-check weak
      (grep, not read, over 700 KB on generic terms). This search did not remedy that; a covering premise
      on metric definition may exist in the register and was not looked for by this agent.

  Recommendation: **NO-SUPPORT-FOUND** for the presumption as literally stated ("one is wrong"), on this
    channel, which was not pointed at it — *and* **SUPPORTED (Strong)** for the assigned direction (the
    quantity is operationally undefined and the divergence is definitional). 15c should not read the first
    clause as a disconfirmation obtained by search; it is an artefact of the polarity inversion, and the
    substantive disconfirming/confirming test of the presumption's own content lies in 15b's file.

NOVELTY-FLAG:
  Item: PRESUMPTION-982
  Searched: Formal metrology on incompletely specified measurands (VIM/JCGM 200, GUM); the software size-
    and defect-counting definition literature (SEI CMU/SEI-92-TR-20; function-point inter-rater
    reliability, Kemerer, Kampstra & Verhoef); construct validity in software metrics (Kaner & Bond;
    Cronbach & Meehl); the many-analysts / analytic-variability reproducibility literature (Silberzahn
    et al.; Botvinik-Nezer et al.); semantic heterogeneity in data integration; method-comparison
    statistics (Bland & Altman); epidemiological case-definition divergence (England COVID-19 mortality
    measures); bibliometric database citation-count divergence.
  Finding: The general principle — that a numeric disagreement between instruments can be definitional
    rather than erroneous — is thoroughly established and is NOT novel. What was searched for and not
    found is any literature in which the divergent *instruments are themselves autonomous agent runs over
    a shared document corpus*, and no study measures inter-run count divergence among such instruments,
    partitions it into definitional and erroneous components, or offers a discipline for deciding which
    partition applies to a given divergence. The estate's specific situation — three counts of `connected`
    from three runs on one vault on one day, with a mechanism located by a fourth pass that vindicates
    two of them — has no published analogue found.
  Implication: Two distinct contributions are available and they should not be conflated. The first is not
    novel and is directly actionable now: adopt Park's definition-checklist discipline for every reported
    count — enumerate the attributes (here at minimum: does a colliding wikilink stem resolve to one node
    or many; are the 419 duplicated filenames one entity or several; is an unresolved link an edge),
    record inclusions and exclusions, and attach the definition to every reported figure, per the SEI
    framework's step 10. On the ISO 15939 model, `connected` needs to be demoted from indicator to a base
    measure with a stated measurement method before any run reports it again. The second is potentially
    novel: a measured partition of inter-run numeric divergence in an agent estate into definitional and
    erroneous components would be an original measurement, and it bears directly on MONITOR-486's unrun
    three-arm dependence question — the same apparatus would serve both. Note also that the estate already
    has the right instinct on record: the third run that found the stem-collision mechanism performed
    exactly the diagnostic that this literature prescribes, and its finding was that both figures were
    admissible. The presumption is contradicted by the estate's own best run of the night.
  Recommended status: NOT NOVEL for the general principle (covered comprehensively by metrology and
    measurement theory). NOVEL for the agent-estate instrument case, and for the partition measurement.
