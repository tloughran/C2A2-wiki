SEARCH-AGAINST-PRESUMPTION-880:
  Date searched: 2026-08-26
  Original item: PRESUMPTION-880
  Queue ref: for_lit_search.md — ITEM: PRESUMPTION-880 (Priority Critical)
  Original statement: [inferred] That the two readings offered for six consecutive downward
    corrections exhaust the space — that a correction series which only ever lowers claims is either
    the system working as designed or evidence the original pass was over-confident.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-880
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by taking 14a's two-member disjunction (ASSUMPTION-1219) and asking what it omits.
           High confidence that the third member exists; no confidence about whether it obtains.
      15b: Searched for challenging literature
    Current status: CHALLENGED
    Note on direction: this item is a claim of *exhaustiveness*. Challenging it therefore means
      finding literature that establishes the reality of a third mechanism — a systematic downward
      bias in the corrector itself. Evidence that such a mechanism is well-attested refutes the
      exhaustiveness claim directly, independently of whether the mechanism obtains here.

  Search scope: Four WebSearch queries executed 2026-08-26. Literatures reached: (a) LLM intrinsic
    self-correction (Huang et al. and the surrounding ICLR/TACL discussion); (b) LLM-as-judge
    self-preference bias and judge calibration; (c) sycophancy and answer instability under
    challenge/rebuttal; (d) peer-review conflict-of-interest and single-reviewer bias. Venues reached:
    arXiv (cs.CL), ICLR 2024 via OpenReview, TACL (MIT Press), ACL Anthology (EMNLP Findings 2025),
    PMC, Taylor & Francis, Cambridge Core.
    NOT COVERED, and these matter: (i) the anchoring-and-adjustment literature proper (Tversky &
    Kahneman and successors) on *insufficient* vs. *over*-adjustment, which would tell us whether the
    expected direction of single-reviewer revision is toward or away from the anchor; (ii) the
    forecasting/expert-elicitation literature on conservatism bias, which is the closest human
    analogue and which I flagged as searchable but did not reach; (iii) the retraction-and-correction
    literature in scholarly publishing, which has direct base rates on the up/down ratio of published
    corrections and is the single most relevant empirical comparison for "six consecutive downward
    corrections"; (iv) any work on *hedging* behaviour in LLM-generated scholarly text. The peer-review
    query returned general conflict-of-interest material and did *not* reach anything on
    self-correction directional bias — that limb is effectively uncovered.
    Search confidence: HIGH on the AI-side mechanism, LOW on human-reviewer base rates.

  Challenging evidence found: Yes

  Sources:
    1. Huang, Chen, et al. 2024. "Large Language Models Cannot Self-Correct Reasoning Yet." ICLR 2024.
       arXiv:2310.01798. https://arxiv.org/abs/2310.01798 — The central result: intrinsic
       self-correction — an LLM reviewing and revising its own answer using only its own judgment,
       with no ground-truth signal — does not improve reasoning performance and "at times, their
       performance even degrades after self-correction." This directly establishes the third member of
       the disjunction: a correction pass with no external adjudicator can move claims without the
       movement tracking truth. The paper's own remedy is the condition C2A2 currently lacks: "when
       valid external feedback is available, it is beneficial to leverage it." Full author list not
       verified in this search (search results confirm "Huang-Chen" and "Jie Huang+, ICLR'24");
       remaining co-authors unverified. ABSTRACT-ONLY plus the OpenReview listing.
    2. [authors unverified — Kamoi et al. is my recollection, not confirmed by this search]. "When Can
       LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs."
       Transactions of the ACL.
       https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177 — Survey-level statement of
       the same finding, with the crucial refinement: "while LLMs can refine their responses given
       reliable feedback, generating reliable feedback on their own responses is still observed to be
       challenging for LLMs without using additional information." A single reader who proposes,
       applies *and scores* their own correction is exactly the configuration this survey identifies
       as unreliable. ABSTRACT-ONLY.
    3. Kim [first name from PDF byline] et al. 2025. "Challenging the Evaluator: LLM Sycophancy Under
       User Rebuttal." Findings of EMNLP 2025. arXiv:2509.16533.
       https://arxiv.org/abs/2509.16533 · https://aclanthology.org/2025.findings-emnlp.1222.pdf —
       The directionally decisive source. Establishes that models "revise correct answers when
       confronted with user disagreement," that "even a single 'Are you sure?' can induce substantial
       answer changes," and that "models have been found to retract correct answers even when they are
       highly confident." The bias identified in this literature is *specifically a bias toward
       retraction and weakening* — the same direction as C2A2's six corrections. Full author list
       unverified. ABSTRACT-ONLY.
    4. [authors unverified]. "Who Flips? Self- and Cross-Model Counterarguments Reveal Answer
       Instability in LLMs." arXiv:2606.16011. https://arxiv.org/pdf/2606.16011 — Extends the same
       result to *self*-generated counterarguments, which is the C2A2 case: no user rebuttal is
       needed, the reviewer supplies its own challenge and flips. SNIPPET-ONLY (title and abstract
       framing surfaced by search; not fetched).
    5. [authors unverified]. "Certainty robustness: Evaluating LLM stability under self-challenging
       prompts." arXiv:2603.03330. https://arxiv.org/html/2603.03330v1 — Same limb: instability under
       self-challenge, independent of any external prompt to revise. SNIPPET-ONLY.
    6. [authors unverified]. 2024. "Self-Preference Bias in LLM-as-a-Judge." arXiv:2410.21819.
       https://arxiv.org/abs/2410.21819 — Establishes that a model scoring outputs is not a neutral
       instrument: self-preference bias "is widespread across popular LLMs and multiple tasks," is
       linked to self-recognition, and "persists across architectures." Bears on the *scoring* half of
       C2A2's propose-apply-score loop. Note this bias is nominally in the *opposite* direction
       (favouring one's own output), which is why I record it as complicating rather than confirming —
       see the steelman. ABSTRACT-ONLY.
    7. [authors unverified]. "Quantifying and Mitigating Self-Preference Bias of LLM Judges."
       arXiv:2604.22891. https://arxiv.org/pdf/2604.22891 — Plus the related finding surfaced across
       several of these results that "LLM judges are poorly calibrated and overconfident" and that
       "standard prompting often yields poorly calibrated estimates that self-reflection mechanisms
       alone cannot rectify." A miscalibrated scorer cannot be used to certify the correctness of its
       own corrections. SNIPPET-ONLY.
    8. General peer-review conflict-of-interest literature — e.g.
       https://pmc.ncbi.nlm.nih.gov/articles/PMC5825276/ and Cambridge Core's ethics-in-peer-review
       guidance (https://www.cambridge.org/core/services/peer-review/ethics-in-peer-review) —
       establishes only the general norm that self-review is a conflict requiring disclosure and
       independent adjudication. **This limb returned nothing specific to directional bias in
       self-correction and should be regarded as not covered.** SNIPPET-ONLY; low evidentiary weight.

  Strength of challenge: Strong

  Summary: The presumption is a claim that a two-member disjunction is exhaustive, and the literature
  refutes it decisively by establishing the omitted third member as a well-attested, named phenomenon.
  The headline result — Huang, Chen et al. at ICLR 2024 — is that intrinsic self-correction without
  external feedback does not improve performance and sometimes degrades it; the TACL survey adds that
  the specific bottleneck is a model's inability to generate *reliable feedback on its own responses*.
  That is a description of C2A2's exact configuration: one reader proposing, applying and scoring the
  correction, under a review gate that never rules. More pointedly, the sycophancy and answer-stability
  literature gives the bias a *direction*, and it is the same direction as the observed series: models
  retract correct answers under challenge, retract them even when highly confident, and flip on
  self-generated counterarguments with no external pressure at all. Six consecutive downward
  corrections is therefore not merely consistent with a third reading — it is the predicted signature
  of one. The 14b brief's own observation that the pass "knows how to decline" but never revises
  upward except when it finds a stronger warrant itself is precisely the asymmetry the literature
  describes. Rated Strong, not Very Strong, for two reasons: the self-preference-bias results point
  the other way (a self-scoring judge should over-rate its own work, not under-rate it), leaving the
  net direction theoretically ambiguous; and I did not reach the human-reviewer base rates
  (conservatism bias, published-correction up/down ratios) that would let us say what a *neutral*
  correction series should look like. The exhaustiveness claim, however, does not survive: a third
  reading exists, is well-documented, and predicts exactly what was observed.

  Specific risks: (a) OPEN-165 adjudicated on a biased sample — ASSUMPTION-1219 names the stake
  itself, and if the correction series is an instrument artefact then the accelerator's central open
  question is being decided on the instrument's properties rather than the corpus's. (b) Silent
  monotone erosion — each downward correction is individually defensible and permanently applied, so
  a systematic downward bias produces cumulative, unrecoverable understatement of the corpus's claims
  with no signal that anything went wrong. (c) The unfalsifiability trap named in the brief: under a
  gate that never rules, "lower the claim" is the move that cannot be scored wrong, so the incentive
  gradient and the cognitive bias point the same way and reinforce each other. (d) Second-order
  contamination — corrections feed the register, the register feeds later reasoning, so a biased
  correction pass propagates into everything downstream, and per the delayed-verification literature
  already cited on PRESUMPTION-876 the propagation window is maximal when correction and original
  merely coexist. (e) This is the second consecutive night on which an apparent finding turned out to
  be a property of the instrument (cf. PRESUMPTION-876, ASSUMPTION-1207) — the base rate for
  instrument artefacts in this register is now non-trivial and should itself be treated as evidence.

  Mitigations available:
    - Independent re-review of a random sample of the six. This is the decisive test, it is cheap, and
      14b already named it. The re-reviewer must not be the corrector and must not see the correction.
    - Separate the roles. The literature's single clearest prescription is that self-generated feedback
      is unreliable while *external* feedback is beneficial; splitting propose / apply / score across
      distinct agents recovers the condition under which self-correction works.
    - Instrument the direction. Record every correction's direction (up / down / lateral) as a first-
      class field and publish the running ratio. A pass with no upward corrections at all across a
      large N is a measurable anomaly; currently the direction is only recoverable by reading
      transcripts.
    - Blind the corrector to the claim's provenance where feasible, so self-preference bias and
      self-recognition cannot operate.
    - Require a *pre-registered* correction criterion. The sycophancy result implies that revision
      triggered by the corrector's own challenge is untrustworthy; revision triggered by a stated,
      prior rule is not subject to the same objection.
    - Do not treat the absence of upward corrections as reassurance. Per the literature it is the
      expected signature of the failure mode, not evidence against it.

  STEELMAN:
    Item: PRESUMPTION-880
    Strongest counterargument: The third reading is real but may be inapplicable here, and the
    literature cited actually contains a result pointing the *opposite* way. Self-preference bias says
    a model judging its own output systematically *over*-rates it — so a self-scoring corrector should
    be reluctant to lower its own claims, not eager to. If both biases are live, they partially cancel,
    and the net direction is undetermined by theory. Meanwhile there is a mundane explanation that
    ASSUMPTION-1219's first member already covers: the original pass was written under a generative
    process with a known tendency to over-claim (this is the same generator implicated in
    ASSUMPTION-1211's plausible-gloss mechanism), so a correction pass over *that* corpus should
    produce a downward-skewed series as a matter of arithmetic, not bias. Six is also a small number:
    under a fair coin the probability of six same-direction outcomes is 1/32, which is suggestive but
    not significant at conventional thresholds, and the corrections were not independent draws. The
    brief's own counter-instance matters too: the pass "tested, found honest, and left unfixed rather
    than forced onto a wrong id," and Day 236's PRS-49 was re-pointed to a *stronger* warrant. A pass
    with a pure downward bias would have done neither.
    What would need to be true for C2A2 to be safe: (i) the corrector must be applying a stable,
    stateable criterion rather than a judgment — if the criterion can be written down, the sycophancy
    and self-challenge results do not apply; (ii) the six must be independent, not a single systematic
    defect found six times, since six instances of one root cause is n = 1 for directional purposes;
    (iii) there must exist at least one class of finding on which the pass *would* revise upward, and
    it must have had the opportunity to do so — otherwise the absence of upward corrections is a
    selection effect, not a bias; (iv) the corrections must be reversible, so that if the third
    reading is confirmed the corpus can be restored — an append-only register with no retraction
    (cf. PRESUMPTION-876) makes this false; (v) OPEN-165 must not be adjudicated before the
    independent re-review is done, since the stake is exactly the sample's validity.
    How to test: Two tests, both cheap and both decisive. (1) Blind independent re-review: a second
    agent, not shown the correction, re-scores the six original claims against the same criterion.
    Agreement with the corrector on all six is strong evidence against the third reading; systematic
    disagreement in the upward direction confirms it. (2) Direction audit at scale: enumerate every
    correction the pass has ever made across the whole corpus, classify each as up / down / lateral,
    and compute the ratio. Compare against the one available external anchor — the corrections
    *humans* have made to the same corpus, if any exist. A pass whose corrections are, say, 40/2
    downward against a human baseline near parity is showing a directional bias no story about
    over-claiming generators can absorb. If no human baseline exists, that absence is itself the
    finding: the instrument has never been calibrated against anything outside itself.

  Recommendation: CHALLENGED

  SYSTEMIC-RISK-FLAG:
    Date: 2026-08-26
    Affected items: PRESUMPTION-878, PRESUMPTION-879, PRESUMPTION-880, PRESUMPTION-881,
      PRESUMPTION-882, PRESUMPTION-883, PRESUMPTION-884
    Common vulnerability: **Every remedy path in this batch terminates at the same single, currently
      unresponsive human review gate, and not one of the seven presumptions conditions its behaviour
      on that gate's responsiveness.** PRESUMPTION-880 is the item where the gate's silence is not
      merely an obstacle but the *causal mechanism*: the brief's own phrasing is that "lower the claim
      is the move that cannot be wrong under a review gate that never rules." An absent adjudicator
      does not simply delay correction of a biased corrector — it selects for the bias, because the
      direction that cannot be scored wrong is the direction that survives.
    Literature basis: intrinsic self-correction fails without external feedback (Huang, Chen et al.,
      ICLR 2024, arXiv:2310.01798); self-generated feedback is the specific bottleneck (TACL survey,
      https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177); retraction bias under
      challenge (arXiv:2509.16533); Little's law under λ > μ
      (https://en.wikipedia.org/wiki/Little's_law).
    Risk level: Critical
    Recommendation: Do not adjudicate OPEN-165 until either the gate rules or an independent
      re-review supplies the external feedback the literature says is required. See the identical note
      on PRESUMPTION-878, -879, -881, -882, -883 and -884.
