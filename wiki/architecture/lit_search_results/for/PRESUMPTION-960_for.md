SEARCH-FOR-PRESUMPTION-960:
  Date searched: 2026-09-12
  Original item: PRESUMPTION-960
  Original statement: "[inferred] That 20-of-20 pre-answering is a routing fault to be fixed rather than
    an observation whose interpretation (saturation vs unfalsifiability) is undetermined."

  READ-CHANNEL INDEPENDENCE ATTESTATION (PREMISE-111 / PREMISE-197):
    I did not read `architecture/lit_search_results/against/` at any point in this run, and did not read
    any 15b output for this item or any other. Agreement between this file and 15b's is not independent
    confirmation and carries PREMISE-111's standing discount.

  DIRECTION NOTE: "FOR" here means literature supporting the presumption as stated — i.e. supporting the
    treatment of a high pre-answer rate as a **process/routing fault with a process fix**, rather than as
    an epistemic observation whose meaning is open. That literature exists and is substantial. It is
    also not the whole story, and the caveats below carry more weight than usual for a FOR file.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-960
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the register's handling of the 20-of-20 pre-answering observation — the
        observation was routed straight to remedy without its interpretation being settled.
      15a: Register pre-check performed. Confirmed 14b's own note that PREMISE-174 pre-answers the
        MECHANISM limb and not the INTERPRETATION limb; searched the interpretation limb only.
    Current status: PARTIALLY-SUPPORTED

  Register pre-check:
    - **PREMISE-174 (ACTIVE, Moderate-High)** — "A register with expansion and no contraction cannot
      revise — it can only accumulate, and its growth curve is therefore not a health signal."
      **PRE-ANSWERS THE MECHANISM LIMB, AS THE INTAKE STATES, AND NOTHING MORE.** 174 explains why an
      accumulating register produces an answer for everything: it has no contraction operator, so the
      answer set only ever grows, and a growth curve is not a health signal. That is the mechanism. It
      says nothing at all about whether a saturated answer set is COMPLETE or VACUOUS — those are the
      two readings 14b names, and 174 does not discriminate between them. **Conflating these is the
      specific error my intake warns against and I am recording that I did not commit it.** 174 clause
      (2) does bear on one sub-question: it holds that the reportable statistic is CORRECTION LATENCY,
      not a rate, because a rate is confounded with scrutiny. The same confound applies to a
      pre-answering rate, which rises as 14a/14b get sharper.
    - PREMISE-124 (ACTIVE, High) — 20/20 is a self-measurement from inside the instrument; it requires
      an external baseline or a seeded denominator or an UNCALIBRATED tag. Bears directly, and source 2
      below is the nearest thing to an external baseline that exists.
    - PREMISE-143 (ACTIVE, Moderate) — a count of this kind measures the producing layer, not the
      catching layer. Bears on which layer 20/20 is a statement about.
    - PREMISE-123, PREMISE-116 (ACTIVE, High) — propagation must be engineered. These bear on the
      ROUTING reading; they do not settle the interpretation either.
    Recording the hits per OPEN-192. **Pre-answer status: PARTIAL. The load-bearing limb is open and was
    searched.**

  LIMB SPLIT:
    Limb A (MECHANISM — why does an accumulating register pre-answer everything?): **PRE-ANSWERED by
      PREMISE-174. NOT SEARCHED.**
    Limb B (INTERPRETATION — is 20/20 a routing fault, or is it saturation, or is it unfalsifiability by
      accretion?): **OPEN. SEARCHED.** This is the item.
    Limb C (IS THERE A DISCRIMINATOR?): open, and the most useful thing a literature search can supply
      here, since it converts an undecidable-looking question into a testable one.

  Supporting evidence found: Partial

  Sources — FOR the routing-fault reading:
    1. Chalmers, I. & Glasziou, P. (2009). "Avoidable waste in the production and reporting of research
       evidence." *The Lancet* 374:86-89. And: Robinson, K.A. & Goodman, S.N. (2011), "A systematic
       examination of the citation of prior research in reports of randomized, controlled trials,"
       *Annals of Internal Medicine* 154(1):50-55.
       — **UNVERIFIED** — both located via search at citation level only; I retrieved neither. The
       Lancet abstract page and several secondary discussions were returned but not read. The reported
       framing, which is what matters for this item: where new work reproduces an answer the prior
       literature already settled, the discipline classifies this as **avoidable research waste**, and
       the prescribed remedy is a **process control** — a mandatory systematic review of prior evidence
       before new work is commissioned. **This is the strongest available support for the presumption:**
       an entire mature discipline treats "the answer already existed and nobody checked" as a
       correctable process defect, not as an epistemic signal about the field's maturity.
       **The "85% of research is wasted" figure returned alongside these is NOT quoted here.** It is a
       heavily-contested aggregate, it was snippet-level, and PREMISE-124's prohibition on quoting
       favourable self-referential aggregates applies by analogy.
    2. Duplicate bug report literature (Bettenburg et al., "Duplicate bug reports considered harmful…";
       Runeson et al., "Detection of duplicate defect reports using natural language processing"; and
       later survey work).
       — **UNVERIFIED** — snippet level across several secondary sources; I retrieved none. Reported
       rates were inconsistent across the corpus: **"42% of all reports" in Bugzilla-like systems**,
       **"approximately 20-30%"**, and **"about 40%"** appear in different sources. **I am recording the
       inconsistency rather than picking a number, and no single figure here should be carried forward
       as a base rate.** What IS consistent across all of them, and is the point for this item: a
       substantial standing duplicate rate is treated in software engineering as **triage overhead to be
       reduced by automated detection** — a routing problem with a routing fix — and not as evidence
       that the defect space has been exhaustively characterised. This supports the presumption's
       framing directly.
       **It also cuts the other way and I am obliged to say so:** every rate in that literature sits in
       a 20-42% band. C2A2's observation is 20 of 20. A value that far outside the band in the mature
       analogue is weak evidence that C2A2 is NOT experiencing the ordinary duplicate-report phenomenon,
       which is the very thing this source is being used to support.

  Sources — establishing that the interpretation is genuinely UNDETERMINED (against the presumption,
  reported per the no-cherry-picking rule):
    3. Braun, V. & Clarke, V. (2021). "To saturate or not to saturate? Questioning data saturation as a
       useful concept for thematic analysis and sample-size rationales." *Qualitative Research in Sport,
       Exercise and Health* 13(2):201-216.
       — **UNVERIFIED** — snippet level; I did not retrieve it. Reported content: saturation is
       "deeply problematic" in the thematic-analysis context, is **often poorly defined and lacking
       clear criteria**, and is "frequently used as a **rhetorical device to justify sample sizes**
       rather than a deliberate methodological choice"; they prefer Malterud's "information power."
       This is the direct authority for 14b's position: a no-new-findings observation does NOT
       self-interpret, and treating it as self-evidently meaningful is the named failure mode.
    4. The **no-new-codes vs no-new-information** distinction in the saturation literature (Saunders et
       al.; Low; the 2024 *Methods in Psychology* evolutionary concept analysis).
       — **UNVERIFIED** — snippet level. **This is the discriminator my intake asked for and it is real:**
       "no new CODES" means the coding frame has stopped growing, which is a property of the INSTRUMENT
       and is exactly what you would observe if the instrument had stopped being able to generate new
       categories. "No new INFORMATION" means the phenomenon has stopped yielding novelty, which is a
       property of the WORLD. The two are routinely conflated and the literature's critique is precisely
       that conflating them lets an instrument's exhaustion masquerade as a field's completeness.
       Applied here: 20/20 pre-answering is a no-new-codes observation. It has not been shown to be a
       no-new-information observation, and the register has no test that would distinguish them.
    5. Lakatos, I., on progressive vs degenerating research programmes (hard core, protective belt,
       ad hoc auxiliary hypotheses; problemshifts).
       — **UNVERIFIED** — located via the Stanford Encyclopedia entry and secondary essays, none
       retrieved. Reported content: a programme is **progressive** if theoretically progressive (core
       plus auxiliaries predict **novel** facts) AND experimentally progressive (some of those novel
       facts are corroborated); **degenerating** programmes lack both, "devolve into repeated
       corroboration of very similar ideas," and are sustained by ad hoc auxiliaries invoked to absorb
       anomalies without generating new predictions.
       **This supplies a second, independent discriminator and it is directly operational for C2A2:**
       the question is not whether the register answers everything — a complete theory would — but
       whether the register has recently made a NOVEL prediction that was then CORROBORATED. "Repeated
       corroboration of very similar ideas" is Lakatos's own description of the degenerate case, and it
       is a fair description of 20-of-20 pre-answering absent such a prediction.

  Strength of support: **Moderate** for the routing-fault reading, on two mature analogues (research
    waste; duplicate defect reports) that both treat pre-answered work as a correctable process defect.
    **But the presumption's load-bearing content is not that routing is A fault — it is that the
    interpretation is SETTLED.** On that, the support is Weak-to-None: sources 3-5 establish that the
    saturation/vacuity question is live, named, and has been contested for decades in two separate
    disciplines.

  Summary: There is a real case for the presumption, and it comes from two disciplines that have faced
    the same observation and both decided it was a process problem. Clinical research treats work that
    reproduces a settled answer as avoidable waste and fixes it with a mandatory prior-evidence check;
    software engineering treats a standing duplicate-report rate as triage overhead and fixes it with
    automated detection. Neither reads a high duplication rate as a signal that the underlying domain
    has been exhaustively mapped. That is genuine support for routing the observation to remedy. The
    case weakens sharply on two points. First, the duplicate-report rates in the mature analogue cluster
    at 20-42%; 20 of 20 is nowhere near that band, which is itself evidence that whatever C2A2 is
    observing is not the ordinary phenomenon these sources describe. Second, and decisively, the
    interpretation is not settled by anyone: Braun and Clarke's critique of saturation is that a
    no-new-findings observation is routinely used as a rhetorical device rather than a finding, and the
    no-new-codes / no-new-information distinction names exactly the ambiguity 14b flagged — the first is
    a fact about the instrument, the second is a fact about the world, and C2A2 has measured the first
    while reasoning as though it had measured the second. Lakatos supplies a second discriminator that is
    directly actionable: a saturated-and-complete register would still generate novel predictions that
    are subsequently corroborated, whereas a degenerating one produces "repeated corroboration of very
    similar ideas." Both tests are runnable in-house and neither has been run.

  Caveats:
    (i) **Every source in this file is UNVERIFIED at source level.** I retrieved no primary text for this
      item — not Chalmers & Glasziou, not Robinson & Goodman, not Braun & Clarke, not the duplicate-bug
      corpus, not Lakatos. This is the weakest-retrieved of my four files and it should be read with
      that discount. The Lakatos content is canonical enough that I would assert it independently; the
      others I would not.
    (ii) **No figure in this file should be quoted as a base rate.** The duplicate-report numbers
      conflict across sources (20-30% / ~40% / 42%) and I did not resolve them. The "85% of research is
      wasted" figure is deliberately excluded.
    (iii) **The transfer is by analogy and the analogy is imperfect in a specific way.** Duplicate bug
      reports and redundant trials are duplicates of PRIOR WORK OF THE SAME KIND. C2A2's 20/20 is
      different in kind: items generated by one layer being pre-answered by a DIFFERENT layer's standing
      register. That is closer to a legal system in which every new case is disposed of by existing
      precedent — a situation whose interpretation is, in exactly the way 14b says, undetermined between
      "the law is settled" and "the precedent set is unfalsifiable."
    (iv) **Both of the alternative readings imply expensive remedies, and PREMISE-173 binds.** A
      Lakatosian test requires the register to make a dated, novel, falsifiable prediction and then be
      checked against it. A no-new-information test requires generating items by a method the register
      did not produce — a different model family, or a human-authored set. Neither is a counter, a field,
      or a flag; both have final elements. That is in their favour, and it is also their cost.
    (v) **PREMISE-174 clause (2)'s confound applies to the pre-answer rate itself.** The rate rises when
      14a/14b get sharper at surfacing items the register happens to cover and falls when the pipeline is
      idle. Like a retraction rate, it measures the auditor under the auditee's name. Any longitudinal
      reading of this number inherits that confound.

  Search scope: comprehensive on the interpretation limb. Searched: theoretical/data saturation and its
    critics in qualitative method, including the no-new-codes vs no-new-information distinction and the
    information-power alternative; Lakatos on progressive vs degenerating research programmes and ad hoc
    auxiliaries; avoidable research waste and prior-evidence citation in clinical trials; duplicate
    defect-report rates and triage. **Did NOT search: belief-revision theory on when a closed answer-set
    is complete versus vacuous** — named in my intake, and the omission is deliberate rather than
    accidental. AGM and the truth-maintenance literature are already the grounding of PREMISE-174, so
    searching them would have returned to the pre-answered mechanism limb; the formal question of
    completeness-vs-vacuity for a closed theory is a logic question (categoricity, ω-completeness) that I
    judged too far from an operational discriminator to be worth the round trip against two discriminators
    already in hand. If the reconciling agent disagrees, that is the untouched body.

  NOVELTY-FLAG:
    Item: PRESUMPTION-960
    Searched: qualitative-method saturation and its critics; Lakatosian appraisal of research
      programmes; research-waste and duplicate-report literatures.
    Finding: The two candidate interpretations are each well developed in isolation, and each supplies a
      usable discriminator. **No literature I located applies either discriminator to a
      machine-maintained normative register that answers items generated by its own upstream layer.**
      The saturation literature assumes a human analyst sampling an external world; the Lakatosian
      apparatus assumes a scientific community making predictions about nature. A register whose items
      are produced by the same system that holds the answers is a configuration neither framework
      addresses, and the self-referential loop — the instrument generates the questions AND grades them
      as already-answered — is the specific feature that makes the saturation/vacuity question hard
      here and is absent from both bodies.
    Implication: A genuine contribution is available, and it is small and concrete rather than grand:
      stating the completeness-vs-vacuity discriminator for a self-generating normative register, and
      running it. The Lakatosian form is the cheaper of the two — file a dated novel prediction, check
      it later — and it would be the first thing in the estate that could fail.
    Recommended status: **NOVEL on the configuration, NOT on the concepts.** The concepts are old; their
      application to this object is not. This should NOT be read as licence to mint a premise: the
      novelty is that the question is unanswered, which is an argument for running the test, not for
      recording a finding about it (PREMISE-173).

  Recommendation: **PARTIALLY-SUPPORTED (Moderate).** The routing-fault reading has real analogical
    support from two disciplines that made the same call. The presumption's actual content — that the
    interpretation is settled and needs no adjudication — is not supported, and sources 3-5 establish
    that the question is live and, more usefully, that it is decidable by two independent tests the
    estate can run. The recommendation to the reconciling agent is that this item's value is the test,
    not the disposition.
