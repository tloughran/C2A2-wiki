SEARCH-AGAINST-PRESUMPTION-975:
  Date searched: 2026-09-13
  Original item: PRESUMPTION-975
  Original statement: "[inferred] That independence is a property an agent can attest to rather than a
    property of how the searches were run. 15a and 15b ran sequentially for a second consecutive cycle,
    declared it, and filed independence attestations in all eight result files; the cycle's strongest
    evidence is that both directions 'independently found' the same covering premises."

  **CAVEATS — THE MECHANISM ACTUALLY USED THIS CYCLE, STATED BEFORE ANYTHING ELSE AND NOT
  SELF-CERTIFIED.** The intake instructs that this item be searched by the two agents whose
  independence it questions, in the execution order it questions, and notes the reflexive hazard. The
  following is a description of the arrangement, not an attestation to its adequacy. **I am not
  competent to certify my own independence and I am not doing so.**
    (1) 15a and 15b ran as **separate isolated agent contexts with no shared state**. There was no
        message passing between them, no shared scratch space, and no common working memory.
    (2) **My prompt was authored from the intake register alone** and its author states it contains
        nothing from 15a's findings. I have no way to verify that from inside; I am relaying the
        claim and labelling it as a claim.
    (3) The read channel was closed: I did not read `lit_search_results/for/`, any 15a output, or
        `lit_search_returns.md` at any point.
    (4) **The two were launched SEQUENTIALLY in wall-clock time, not simultaneously.** This is the
        third consecutive cycle with that deviation. It is stated plainly here rather than in a
        closing caveat, because PRESUMPTION-979 (searched the same run) establishes that a closing
        caveat would not be read.
    (5) **The dominant correlation channel is untouched by all of the above.** 15a and 15b are
        instances of the same model, from the same provider, on the same base architecture. Sources 2
        and 3 below measure that this is the maximum-correlation configuration. Nothing in (1)–(4)
        addresses it, and PREMISE-111 already says so.
    (6) Self-demonstrating instance, recorded because it is evidence: PREMISE-111's own entry notes
        "15a and 15b independently retrieved the same two key sources for this item." **I independently
        retrieved one of those same two sources again this run (arXiv:2605.29800), without having seen
        PREMISE-111 first — I found the premise afterwards, while running the pre-check.** That is a
        third convergence on the same source by the same model family, and it is an instance of the
        phenomenon rather than a confirmation of it. Per the intake's own instruction, **15c should
        treat convergence on this item as uninformative.** So should any reader of this file.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-975
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from the co-occurrence of a declared sequencing deviation and an undiminished
        independence claim, twice. **Note the reflexive hazard and route anyway:** this item will be
        searched by the two agents whose independence it questions, in the execution order it
        questions. 15c should treat convergence on this item as uninformative.
      15b: Searched for order and anchoring effects in sequential retrieval and for direct measurement
        of independence loss among LLM panels; retrieved two primaries; re-ran the register pre-check
        and found that **an ACTIVE premise already answers this item in general form, carrying a
        standing discount, and the intake's pre-check reported it absent**; recorded the actual
        execution mechanism above without certifying it.
    Current status: CHALLENGED

  REGISTER PRE-CHECK — **the intake's pre-check is WRONG, and the premise it missed is the one that
    governs this exact pair of agents.** The intake states: "grepped for `independen`, `concurrent`,
    `anchoring` — **the provenance spec requires the attestation and defines no condition on execution
    order.** No covering premise. Confirmed by reading `provenance_protocol.md` v1.0, not by grep
    alone." The provenance-spec half of that is correct and useful. The "no covering premise" half is
    false.
    - **PREMISE-111 (ACTIVE, Confidence Moderate, validated 2026-07-21, re-check due 2026-08-21 — 23
      days overdue)** — decisive, and it contains a clause marked load-bearing that disposes of the
      item. Read verbatim: "The read channel was **not** the dominant correlation source between 15a
      and 15b, and removing it removed the weakest of at least four. **Frontier LLMs sharing no
      procedural channel collapse to roughly two effective votes out of nine**, so the dominant channels
      — shared pre-training corpora, shared alignment procedures, distillation — are **upstream of any
      coupling C2A2 can remove**... **STANDING DISCOUNT (load-bearing): the correct inference from this
      premise is that the record is MORE compromised than the fix addressed, not less. No downstream
      argument may cite 15a/15b agreement as independent confirmation**; agreement between the two
      directions carries a residual correlation of roughly the magnitude the panel literature measures
      (8–22pp accuracy shortfall against the independence benchmark) and must be discounted
      accordingly." Its `Applicable to` line names "Agents 15a, 15b, 15c; **every disposition citing
      cross-agent convergence**."
      Three consequences. First, the item's premise — that independence is treated as attestable — is
      **already refuted in the register**, which says in terms that it is a property of shared upstream
      channels C2A2 cannot remove. Second, the item's stated evidence, that "the cycle's strongest
      evidence is that both directions 'independently found' the same covering premises," is **a direct
      violation of an ACTIVE load-bearing clause**: no downstream argument may cite 15a/15b agreement
      as independent confirmation. Third, the grep term the intake used — `independen` — appears in
      PREMISE-111 at least three times ("independent confirmation," "independence benchmark,"
      "independently retrieved"). The grep could not have missed it; the return was not read. This is
      the ASSUMPTION-1343 failure occurring inside a pre-check that claims to have gone beyond grep.
    - **PREMISE-120 (ACTIVE)** bears and supplies binding vocabulary: "Reproducing a result does not
      confirm it... **the phrase 'independently confirmed' is forbidden unless the second check obtained
      its own data**." Filing an independence attestation and then citing agreement is the forbidden
      construction.
    - **PREMISE-110** (per 141's consistency note) holds that a monitor sharing a failure domain with
      its subject is "a single channel wearing two labels." Two instances of one model are that.
    Routed to the SYSTEMIC-RISK-FLAG.

  Challenging evidence found: **Yes — directly measured, twice, on this exact system class.**

  Sources:
    1. **PREMISE-111 (ACTIVE), read in full this run.** — **VERIFIED, in-house.** The single decisive
       source, quoted above. The item asks whether independence is attestable; the register already
       answered no, already installed a standing discount, and the discount is being violated by the
       evidence the item cites.
    2. **"Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels,"
       arXiv:2605.29800v1.** — **VERIFIED** (abstract and Table 2 retrieved and read directly from the
       arXiv HTML this run; this is an independent retrieval by me, not a transcription from
       PREMISE-111, which I found afterwards). Abstract, read verbatim: "Testing a panel of **9 frontier
       LLMs from 7 model families** on three natural language inference datasets (each with 100 human
       annotations per item), we find that the 9 judges effectively provide only about **2 independent
       votes' worth of information. Roughly three-quarters of the panel's nominal independence is lost
       because the models make the same mistakes on the same items.**" Table 2, read verbatim: "n_eff
       (Kish) | **2.18 [2.07, 2.31]**", with the caption "The 9-judge panel provides only 2.18 effective
       independent voters... The panel's 0.2pp lift is within noise and tie-breaking margin (11 ties,
       1.1%)." **The load-bearing detail for this item is the 7 model families.** Three-quarters of
       independence is lost even across *different* architectures from *different* providers. 15a and
       15b are not seven families; they are one model. Whatever n_eff is for a two-agent panel drawn
       from a single model, it is bounded above by what this paper measures for a maximally diverse
       nine-agent panel, and there is no argument available by which it could approach 2.
    3. **Kim, E., Garg, A., Peng, K. & Garg, N. (2025), "Correlated Errors in Large Language Models,"
       ICML 2025 (PMLR 267), arXiv:2506.07962.** — **VERIFIED** (abstract and Introduction §1 retrieved
       and read directly this run). Abstract, read verbatim: "We conduct a large-scale empirical
       evaluation on **over 350 LLMs**... We find substantial correlation in model errors—on one
       leaderboard dataset, **models agree 60% of the time when both models err**. We identify factors
       driving model correlation, **including shared architectures and providers. Crucially, however,
       larger and more accurate models have highly correlated errors, even with distinct architectures
       and providers.**" Introduction, read verbatim: "on Helm, pairs of models agree on average about
       60% of the time when both models are incorrect (**choosing between incorrect answers uniformly at
       random would lead to an agreement rate of 1/3**)"; and "models with the **same provider
       (company), with the same base architecture**, or with similar sizes have **more correlated
       errors**... even after conditioning on these factors, pairs of models that are *more accurate
       individually* also have more correlated errors." **This is the specification of the
       maximum-correlation configuration, and 15a/15b satisfy every term of it**: same provider, same
       base architecture, same size, individually accurate. The 60%-versus-33% comparison is the
       cleanest statement of what "agreement" is worth here: most of it is structural.
    4. Order and position effects in LLMs: "Fragile preferences: A deep dive into order effects in
       large language models," *PNAS Nexus* (2026), and the position-bias literature. — **UNVERIFIED**
       (search-layer summaries only; neither primary retrieved). Reported: strong and consistent order
       effects with a quality-dependent shift; serial-position (primacy/recency) effects analogous to
       human ones; accumulated-context effects in which prior conversation polarity biases subsequent
       judgements. **Excluded from the rating, and the reason is a domain-transfer objection I am
       raising against my own best evidence**: these measure ordering *within a single prompt or
       context*, whereas the item concerns two *separate contexts* launched in sequence. With no shared
       context there is no within-prompt order for these effects to operate on. Citing them here would
       be the unwarranted transfer this agent exists to catch. They are recorded so a later run does not
       mistake their absence for an oversight.
    5. Linear Sequential Unmasking (LSU / LSU-E): Dror, I.E. et al. (2015), "Context Management
       Toolbox," *J. Forensic Sciences*; Dror & Kukucka (2021), "Linear Sequential Unmasking–Expanded
       (LSU-E)," *Forensic Science International: Synergy* 3:100161. — **UNVERIFIED** (search-layer
       summaries only; PMC was behind a CAPTCHA and ScienceDirect was not fetched). Reported: a
       research-based **procedural** framework requiring examiners to analyse trace evidence in
       isolation before exposure to reference material, on the finding that the order in which
       information is presented significantly influences interpretation. **No figure is used.** What it
       contributes is the disciplinary precedent for the item's core claim: the field that has thought
       hardest about contextual bias concluded that independence must be **engineered into the
       information flow**, and does not accept an examiner's assurance of impartiality as a substitute.
       That is the item's proposition, arrived at independently in a human domain, and it is why the
       challenge here is to the *attestation format*, not only to the sequencing.
    6. **EXCLUDED and named.** PREMISE-111 cites two further sources — van Rooyen et al. (1998), JAMA
       280(3):234–237 on blinding in peer review, and arXiv:2604.07650, "How Independent are Large
       Language Models?" **I did not retrieve either this run.** They are second-hand to me via the
       register and no figure from them is used.

  Strength of challenge: **Strong**, and the item is additionally **substantially pre-answered
    in-house**.

    Limb split:
      - "Independence is treated as a property an agent can attest to": **Strong** challenge, and it is
        conceded by the register. PREMISE-111 states that the dominant correlation channels are
        "upstream of any coupling C2A2 can remove." An attestation cannot reach an upstream channel, so
        the attestation format is, on the estate's own ACTIVE premise, addressing the weakest of at
        least four channels while creating the impression of having addressed the property. The
        attestations filed in eight result files are true statements about the read channel and
        misleading as independence claims.
      - "Sequential execution is the thing that matters": **Partially challenged — and here the item
        overstates.** On sources 2 and 3, execution order is a *second-order* concern: independence
        loss is measured at three-quarters even across seven model families with no procedural channel
        at all. Fixing the wall-clock sequencing would change little. The item is right that
        attestation is not independence, and wrong to locate the defect primarily in ordering.
        **Simultaneity would not have fixed this cycle.**
      - "The cycle's strongest evidence is that both directions independently found the same covering
        premises": **Strong** challenge, and it is a **procedural breach** rather than an inaccuracy.
        PREMISE-111's standing discount is load-bearing and reads "No downstream argument may cite
        15a/15b agreement as independent confirmation." PREMISE-120 forbids the phrase "independently
        confirmed" unless the second check obtained its own data. Convergence on a *register lookup* —
        both directions grepping the same file — is the least independent possible form of agreement,
        since the data source is literally identical.
      - "There is no condition on execution order in the provenance spec": the intake verified this by
        reading `provenance_protocol.md` v1.0 and I have no reason to doubt it. **That is a real gap
        and the item's most useful contribution**: the spec mandates an attestation whose content it
        does not constrain, which is how a true statement about the read channel came to stand in for
        an independence claim.

  Summary: The item is right that independence is not attestable, and the register already says so.
    PREMISE-111 is ACTIVE, applies by name to agents 15a and 15b, and holds that the read channel was
    the weakest of at least four correlation channels, the dominant ones — shared pre-training corpora,
    shared alignment, distillation — being upstream of anything C2A2 can remove; it installs a standing
    load-bearing discount forbidding any downstream argument from citing 15a/15b agreement as
    independent confirmation. The cycle's stated strongest evidence does exactly that. Two primaries
    retrieved this run measure the magnitude: a nine-judge panel drawn from seven different model
    families retains only 2.18 effective independent votes, losing roughly three-quarters of nominal
    independence to shared errors on shared items; and across 350+ models, pairs agree on the same
    wrong answer 60% of the time against a 33% chance baseline, with correlation rising for models
    sharing a provider, a base architecture, a size, and individual accuracy. 15a and 15b share all
    four. Where the item overstates is in locating the defect in sequencing: on this evidence
    simultaneous execution would have bought very little, because the binding channel is the weights,
    not the clock. The genuinely actionable finding is the one the intake verified by reading the spec
    — the provenance protocol mandates an independence attestation without constraining what it may
    claim, which is how a true statement about one closed channel came to be filed as an independence
    claim eight times.

  Specific risks:
    - **Every disposition in the record that cites cross-direction convergence is discounted by an
      unknown amount, and the discount has never been applied.** PREMISE-111 names the magnitude as
      roughly the panel literature's 8–22pp shortfall and makes the discount mandatory. If it has not
      been arithmetically applied anywhere, the estate's confidence figures are systematically inflated
      and the inflation is invisible because the attestations read as controls.
    - **The attestation format actively conceals the exposure.** A reader encountering "READ-CHANNEL
      INDEPENDENCE ATTESTATION" in eight files reasonably infers the independence question is handled.
      On PREMISE-111 it is handled for the weakest channel only. This is a warning that makes the
      system less safe than no warning would — and under the corrective-action hierarchy read for
      PRESUMPTION-974 this same run, "Warnings" is classified among the **Weaker Actions**.
    - **The error is in the direction that produces false confidence, never false alarm.** Correlated
      agreement inflates apparent confirmation; it never manufactures spurious disagreement. So the
      bias accumulates monotonically toward SUPPORTED and away from CONTESTED across the whole
      register, and the reconciliation rule in the 15b role definition ("Both support → SUPPORTED, high
      confidence") converts it directly into status.
    - **PREMISE-111 is 23 days past re-check and reads ACTIVE.** So does the standing discount nobody
      has applied.
    - **This item cannot be settled by the pipeline that filed it.** The intake said so and it is
      correct. A CHALLENGED verdict reached by 15b about 15b's own independence is worth exactly as
      much as an attestation, which is the item's point. **The verdict below should be read as "the
      external literature and the estate's own ACTIVE premise both say the attestation does not do what
      it appears to do," not as "15b has established its own non-independence."**

  Mitigations available:
    - **Stop filing independence attestations in their current form.** Replace with a one-line
      **correlation disclosure** that states what it actually is: same model, same provider, read
      channel closed, dominant channels open, PREMISE-111 discount applies. This removes a misleading
      control and costs nothing. It is the single highest-value action here.
    - **Amend `provenance_protocol.md` to constrain the attestation's content**, since the intake
      verified that v1.0 mandates the attestation without bounding its claim. A schema constraint is a
      structural forcing function, which the action hierarchy classes as **Stronger**; a guideline
      would be weak.
    - **Apply PREMISE-111's standing discount arithmetically, or record that it is not being applied.**
      At present it is an ACTIVE load-bearing clause with no implementation. Either a numeric
      confidence haircut on convergence-based dispositions, or an explicit entry saying the discount is
      unimplemented. The current state — mandated and silently unapplied — is the worst of the three.
    - **Bar convergence-on-a-register-lookup from counting as evidence at all.** When both directions
      "independently find" the same premise by grepping the same file, the data source is identical and
      PREMISE-120's rule applies on its face. This is a one-line rule with no cost.
    - **Buy real independence where it is affordable, and only there.** The only channel C2A2 can
      actually vary is the model: running one direction on a different provider's model would move the
      configuration off the maximum-correlation point sources 2 and 3 identify. Whether that is
      affordable is not my call; what is my call is that **re-ordering the launches is not a substitute
      for it** and should not be recorded as one.
    - **Retrieve arXiv:2604.07650 and van Rooyen et al. 1998** as primaries. Both are load-bearing for
      PREMISE-111 and both are currently second-hand in the register.

  STEELMAN:
    Item: PRESUMPTION-975
    Strongest counterargument: The item, and this file, prove too much. If shared weights are the
      dominant and irremovable correlation channel, then **no** procedural discipline C2A2 adopts can
      produce independence, from which it follows that the 15a/15b architecture was never an
      independence mechanism and should never have been read as one — but that is an argument for
      relabelling it, not for treating the current cycle as defective. The attestation, read charitably,
      never claimed weight-level independence; it claimed the read channel was closed, which is true,
      verifiable, and the only thing an agent is actually in a position to assert about itself. Holding
      it to a standard it does not claim is uncharitable, and demanding simultaneity is worse than
      uncharitable — it is a control that this file's own evidence shows would purchase almost nothing,
      so insisting on it would be the estate spending scarce engineering effort on the visible channel
      precisely because it is visible. The deeper point is that the two directions are not an ensemble
      and the panel literature does not straightforwardly apply: sources 2 and 3 measure *agreement*
      among judges answering the *same* question, whereas 15a and 15b are assigned **opposite**
      questions, so their outputs are not votes to be aggregated but two adversarial briefs to be read
      by a third party. Correlated errors matter for a jury; they matter much less for a prosecution
      and a defence, whose value comes from the assignment of direction, not from the independence of
      the advocates. On that reading the architecture is sound, the attestation is honest, the
      sequencing is irrelevant, and the only genuine defect is the sloppy sentence in which convergence
      was cited as confirmation — a reporting error in one cycle, not a structural failure.
    What would need to be true for C2A2 to be safe: (a) the adversarial-briefs reading must be the one
      the estate actually operates, and it is **not**: the 15b role definition's own reconciliation
      table maps "Both support → SUPPORTED (high confidence)," which is vote aggregation, and
      PREMISE-111 was written precisely because agreement *was* being treated as confirmation; (b) the
      relabelling must actually happen — the steelman's best move is "it was never an independence
      mechanism," and that is only a defence if the record stops calling it one, which requires the
      protocol amendment above; (c) the directional assignment must be doing the work the steelman
      credits it with, which is **testable and untested** — if two same-model agents assigned opposite
      directions nonetheless converge on the same sources and the same framing, the assignment is a
      thinner control than claimed, and note that this file and PREMISE-111 converged on
      arXiv:2605.29800 across directions and cycles; (d) the one-cycle-reporting-error framing must
      survive the count, and it does not: the intake records the deviation-plus-undiminished-claim
      pattern **twice** before this cycle and this is the third. (a) and (d) are the binding ones. The
      steelman's strongest surviving contribution is (b): relabelling is cheap, correct, and should
      happen whether or not anything else does.
    How to test: **A source-overlap and framing-overlap measurement, retrospective and in-house.** For
      every item searched by both directions in the last N cycles, compute (i) the Jaccard overlap of
      the cited source sets and (ii) the overlap of the covering premises each direction identified,
      with denominators per PREMISE-168. Under the steelman's adversarial-briefs reading, directional
      assignment should drive the two briefs to substantially *different* sources; under the
      correlated-errors reading they will converge. This distinguishes the two positions without
      requiring any new capability and uses data the estate already has on disk. A second, sharper test
      if it is ever affordable: run one direction on a **different provider's model** for a single
      cycle and measure whether the overlap drops. That is the only experiment that isolates the weight
      channel from the direction channel, and until it is run, **no one — including me — is entitled to
      a quantitative claim about how independent 15a and 15b are.**

  Search scope: **Adequate on the measurement limb; deliberately narrowed on one limb and the
    narrowing is declared.** Searched: LLM ensemble/judge-panel correlation and effective sample size,
    correlated errors across model providers and architectures, order/anchoring and position effects in
    LLMs, forensic contextual-bias procedure (LSU/LSU-E), and the register itself. **Two external
    primaries were retrieved and read this run** (arXiv:2605.29800 abstract and Table 2;
    arXiv:2506.07962 abstract and Introduction §1) and they carry the rating alongside PREMISE-111 read
    in full. **The LLM order-effects literature was located and deliberately EXCLUDED** on a
    domain-transfer objection I raised against my own strongest-looking evidence — it measures ordering
    within a context, and this item concerns separate contexts — and that exclusion is the single most
    consequential judgement in this file. LSU/LSU-E is UNVERIFIED and contributes precedent, not
    evidence. Two sources cited by PREMISE-111 were not retrieved and are named as second-hand.
    **Structural limit, load-bearing: this search was performed by one of the two agents whose
    independence is at issue, using the same model as the other, in the execution order under
    question. That limit is not remediable from inside this file and the verdict should be read
    subject to it.**

  Recommendation: **CHALLENGED**
