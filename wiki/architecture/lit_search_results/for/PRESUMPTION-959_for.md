SEARCH-FOR-PRESUMPTION-959:
  Date searched: 2026-09-12
  Original item: PRESUMPTION-959
  Original statement: "[inferred] That replication of a measurement raises its epistemic standing even
    when the same instrument produced every replicate."

  READ-CHANNEL INDEPENDENCE ATTESTATION (PREMISE-111 / PREMISE-197):
    I did not read `architecture/lit_search_results/against/` at any point in this run, and did not read
    any 15b output for this item or any other. This attestation matters more for this item than for the
    others in the cohort: the item is a question about the register's own instrumentation, 14a and 14b
    are named parts of that instrument, and so am I. Agreement between this file and 15b's would be a
    same-instrument replicate — which is precisely the thing the item asks about, and precisely the
    thing PREMISE-111 forbids counting as confirmation.

  DIRECTION NOTE: the item is an unstated presumption the register is acting under. "FOR" therefore
    means literature supporting the proposition that same-instrument replication raises epistemic
    standing. That proposition is TRUE under one reading and FALSE under another, and the two readings
    are separated by a distinction the measurement literature has maintained since 1959. The FOR search
    finds real support, for the narrow reading only.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-959
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the register's treatment of repeated measurements of its own pre-answering
        behaviour. Routed deliberately against the night's pattern because it is a question about the
        register's own instrumentation.
      15a: Register pre-check performed; found a near-verbatim ACTIVE pre-answer. Searched anyway, on a
        limb split, because the pre-answering premise states the rule in the reproducibility vocabulary
        and the item is posed in the replication vocabulary — worth confirming the two vocabularies
        converge, which they do.
    Current status: PARTIALLY-SUPPORTED

  Register pre-check:
    - **PREMISE-120 (ACTIVE, High — SUPPORTED + NO-CHALLENGE-FOUND). PRE-ANSWERS THIS ITEM, close to
      verbatim.** "Reproducing a result does not confirm it. Reproducibility — obtaining consistent
      results using the same input data, computational steps, methods and code — is a property of the
      pipeline, expected as a baseline; replicability requires independently obtained data. Replication
      and reproducibility do not imply correctness, and **a systematic defect reproduces exactly as
      reliably as a correct measurement**: a deterministic analyser with a >95% false-alarm rate
      reproduces every false alarm perfectly." Its BINDING VOCABULARY clause forbids the phrase
      "independently confirmed" unless the second check obtained its own data by a different path, and
      obliges every claimed second check to record what it shares: code path, corpus, model, execution
      context. Scope guard (ii) is also directly on point: "a second implementation written from the
      same specification SHARES the specification, and structural variation does not buy failure
      independence."
    - **PREMISE-111 (ACTIVE, Moderate)** — the read-channel fix removed the weakest of at least four
      correlation channels between 15a and 15b; the dominant channels (shared pre-training corpora,
      shared alignment, distillation) are upstream of anything C2A2 can remove. STANDING DISCOUNT: no
      downstream argument may cite 15a/15b agreement as independent confirmation.
    - **PREMISE-197 (ACTIVE, Moderate-High)** — agreement among independently-run generators is
      corroboration by default and redundancy only under stated conditions. Bears on the two-mention
      promotion threshold, which is the concrete register mechanism this presumption is embedded in.
    - PREMISE-124 (ACTIVE, High) — self-measurement of the pipeline's own accuracy must cite an external
      baseline or be tagged UNCALIBRATED. Bears: the replicates in question are the instrument
      measuring itself.
    - PREMISE-143 (ACTIVE, Moderate) — a retraction count measures the producing layer. Adjacent, not
      covering.
    Recording the hits per OPEN-192. **This is the most directly pre-answered item in the cohort.**
    PREMISE-120 states the rule; I searched only to test whether the measurement literature reaches the
    same place by a different route and to locate the boundary at which the presumption is actually
    correct. It does, and there is one.

  LIMB SPLIT:
    Limb A (PRECISION): repeating a measurement with the same instrument improves the PRECISION of the
      estimate — it reduces the contribution of random error. **The presumption is TRUE on this limb.**
    Limb B (VALIDITY / EPISTEMIC STANDING): repeating a measurement with the same instrument raises
      confidence that the measurement is CORRECT. **The presumption is FALSE on this limb**, and this is
      the limb the register is relying on when it treats repeated same-instrument observations of its
      own behaviour as accumulating evidence.

  Supporting evidence found: Partial (Limb A only)

  Sources:
    1. Standard measurement-error theory (random vs systematic error; precision vs accuracy). Sources
       located: University of Maryland PHYS276 error-analysis notes; University of Oxford Physical
       Chemistry teaching notes on accuracy and precision; Scribbr methodology reference.
       — **UNVERIFIED at source level** — these are teaching materials located by search; I read the
       search-returned summaries, not the pages. **The content, however, is canonical and not in
       dispute:** random errors in repeated measurements average toward zero, the standard error of the
       mean is s/√n, and precision is limited by random error. The figure s/√n is textbook and I am
       comfortable stating it; I am NOT attributing it to any one of these pages as a primary source.
       This is the whole of Limb A's support, and it is real: if the quantity being measured is stable
       and the instrument's error is random, more replicates is a better estimate.
    2. The same corpus, on the boundary: **"systematic errors cannot be detected or reduced by
       increasing the number of observations."** Systematic error is removed by calibration against an
       external referent, never by repetition. — **UNVERIFIED at source level**, same caveat, same
       canonical status. This sentence is Limb A's terminus and Limb B's refutation in one line, and it
       is the metrological form of PREMISE-120's "a systematic defect reproduces exactly as reliably as
       a correct measurement."
    3. Campbell, D.T. & Fiske, D.W. (1959). "Convergent and discriminant validation by the
       multitrait-multimethod matrix." *Psychological Bulletin* 56(2):81-105.
       — **UNVERIFIED** — located via search; I did not retrieve the paper or a full-text mirror. The
       MTMM design requires that the multiple methods be **maximally different**, and the entire
       apparatus exists because a correlation between two same-method measures is confounded with
       method variance. Convergent validity is defined as agreement ACROSS methods; same-method
       agreement is definitionally excluded from counting toward it. **This is the canonical statement
       that Limb B is false, and it is 67 years old.**
    4. Common-method variance / mono-method bias literature (Podsakoff-lineage; located via
       Journal of International Business Studies editorial and a 2024 *Management Communication
       Quarterly* reassessment).
       — **UNVERIFIED** — snippet level only; I retrieved none of these. Reported content: mono-method
       bias is "consistently described as a threat to construct validity," it "biases estimates of the
       true relationships among constructs," it inflates or deflates observed relationships and produces
       both Type I and Type II errors, and the first-best remedy is prevention at design stage by
       collecting data from **multiple sources**. **I flag this explicitly: I am not treating any of
       these characterisations as a verified quotation from a primary source.** They are consistent
       with source 3 and with PREMISE-120, which is why I report them; consistency with two things I
       trust is not the same as verification.
    5. Replication-typology literature: Derksen & Morawski (2022), "Kinds of Replication," *Perspectives
       on Psychological Science*; Crandall & Sherman (2016), "On the scientific superiority of
       conceptual replications"; the *Experimentology* open textbook, ch. 3.
       — **UNVERIFIED** — snippet level. One reported case is worth recording because it is the
       strongest available illustration and because it is an EMPIRICAL instance rather than a
       definitional claim: a cognitive-dissonance finding (Brehm) was **directly replicated many times,
       across different labs, different decades and different subject populations**, and was
       nevertheless misleading, because a flaw in the experimental design **recurred in every direct
       replication**. Repetition propagated the flaw with perfect fidelity. I could not retrieve the
       source making this claim and therefore cannot name the original study or the flaw; **it is
       reported here as an unverified illustration and must not be cited as a documented case without
       retrieval.** If it holds up it is the single best external analogue for C2A2's situation.

  Strength of support: **Weak.** Limb A is supported and is a real property, but it is the limb that
    does not bear any weight in the register's reasoning. Limb B — the only limb that matters for what
    the register does with repeated observations of itself — has no support, and is contradicted by the
    defining apparatus of measurement validity.

  Summary: The FOR direction has exactly one thing to offer and it is narrow. If C2A2's instrument has
    random error and the thing being measured is stable, then more replicates give a tighter estimate,
    with standard error falling as s/√n — that is genuine and it is the honest case for the presumption.
    It stops precisely where systematic error begins: a bias in the instrument is not reduced by
    repetition at all, and Campbell and Fiske built the whole multitrait-multimethod apparatus in 1959
    around the fact that same-method agreement is confounded with method variance and cannot count
    toward convergent validity. PREMISE-120 already says this in the reproducibility vocabulary — "a
    systematic defect reproduces exactly as reliably as a correct measurement" — so the register holds
    the answer and the measurement literature reaches the same place by an independent route, which is
    the one useful thing this search adds. The sharpest point for C2A2 is the direction of the error:
    the register's repeated observations of its own pre-answering behaviour are produced by the same
    pipeline, the same model family, the same prompt lineage and the same corpus, which is the maximum
    possible common-method loading, so the replicates carry close to zero independent information about
    whether the observation is correct. What they do carry information about is the instrument's
    stability — which is worth knowing, and is not what it is being used for.

  Caveats:
    (i) **Five of five sources are UNVERIFIED at source level.** I retrieved no primary text for this
      item. The claims I report are canonical and mutually consistent, and two of them (s/√n; systematic
      error is unaffected by repetition) are textbook facts I would assert on my own authority. The
      Campbell & Fiske characterisation I would also assert. The Brehm/dissonance illustration I would
      NOT — it is the one disposition-relevant specific here that rests on a snippet, and it is labelled
      as such above and should not be carried forward without retrieval.
    (ii) **This item is self-referential and I am inside it.** 15a and 15b share pre-training, alignment
      and prompt lineage. My finding that same-instrument replication is weak evidence is itself
      produced by the instrument. That does not make it wrong — PREMISE-120 and Campbell & Fiske are
      external referents and that is the point of citing them — but it does mean this file cannot be
      cited as an independent check on the register's instrumentation. It is the instrument reading a
      ruler it fetched from outside.
    (iii) **Limb A is not nothing, and the reconciling agent should not flatten it.** If the register
      wants to claim its pre-answering observation is STABLE, repeated same-instrument measurement is
      the right instrument and supports that claim. The error is only in reading stability as
      correctness. Those are separable claims and the register is entitled to the first one.
    (iv) **The remedy this implies is expensive and should be priced before it is proposed
      (PREMISE-173).** What Limb B's failure calls for is a differently-constructed measurement — a
      different model family, a hand-audited sample, or a seeded denominator — not more runs of the
      same. A "we ran it twice" field would be the acknowledgement-receipt defect of PREMISE-108 in
      measurement clothing.

  Search scope: comprehensive for the concepts named, shallow on retrieval. Searched: common-method
    variance and mono-method bias; the multitrait-multimethod matrix and convergent validity; direct
    vs conceptual replication and their epistemic functions; random vs systematic error and the
    precision/accuracy distinction in metrology. **Did NOT search: measurement invariance** (named in my
    intake; it is the psychometric machinery for testing whether an instrument measures the same
    construct across groups or occasions, and it is the right next body if the estate wants to test
    whether its own instrument has drifted between the replicates rather than whether it is biased).
    Also did not search test-retest reliability coefficients or generalizability theory, either of which
    would formalise the Limb A / Limb B split more precisely than the informal precision/accuracy
    framing used here.

  NO NOVELTY FLAG. The distinction is one of the oldest in measurement theory and the register already
    holds it as PREMISE-120.

  Recommendation: **PARTIALLY-SUPPORTED (Weak).** Support exists and is confined to precision against
    random error. The presumption as stated — that replication raises EPISTEMIC STANDING — is not
    supported for the use the register is making of it, and PREMISE-120 already forbids that use in
    terms. The load-bearing finding for the reconciling agent is that this item is an enforcement gap
    against an ACTIVE High-confidence premise, not a knowledge gap, and per the 2026-08-13 precedent
    (PRESUMPTION-781/783) that disposition is REVISE, not a mint.
