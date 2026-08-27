SEARCH-FOR-PRESUMPTION-880:
  Date searched: 2026-08-26
  Original item: PRESUMPTION-880
  Queue ref: LIT-QUEUE — 2026-08-25 (Agents 14a + 14b end-of-day intake)
  Original statement: "[inferred] That the two readings offered for six consecutive downward
    corrections exhaust the space — that a correction series which only ever lowers claims is either
    the system working as designed or evidence the original pass was over-confident."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-880
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by taking 14a's two-member disjunction (ASSUMPTION-1219) and asking what it omits.
        High confidence that the third member exists; no confidence about whether it obtains. Bears on
        OPEN-165.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Search scope: WebSearch, 2026-08-26, three queries. Note on direction: the item as filed is an
    *exhaustiveness* claim, while the queue's "Question for the literature" is framed around self-review
    bias — which, if present, is the third member and therefore evidence *against* exhaustiveness. I
    resolved this by searching for support of the two stated members (i.e. literature showing that a
    downward-only correction series is exactly what one should expect from an over-claiming generator
    and a correctly-designed corrector, with no reviewer-bias term needed), and by searching the
    self-review-bias limb honestly and reporting what it returned even where it cuts against the item.
    Limbs covered: (a) prevalence of over-claiming in scholarly and generated text; (b) self-review vs.
    independent-review error detection rates; (c) error-management theory / asymmetric error costs as a
    normative account of directional conservatism.
    Assessment: **thin coverage — this item is under-searched relative to its Critical priority.**
    Three queries only. Not run: the anchoring-and-adjustment literature; the peer-review
    inter-reviewer-agreement literature; any literature on directional asymmetry in *post-hoc
    correction* series specifically (as opposed to initial review). The last of these is the item's
    exact question and I did not reach it. Recorded as an explicit shortfall.

  Supporting evidence found: Partial

  Sources:
    1. "Quantifying the prevalence and impact of overreaching causal claims in social science."
       *Nature Human Behaviour* (2026), https://www.nature.com/articles/s41562-026-02553-x
       [authors unverified]
       — The strongest supportive source. An analysis of 194,631 social science articles finds causal
       overclaiming in 46% of cases, with the rate of causal language in titles/abstracts rising from
       ~20% to ~60% since 2000. If the base rate of over-claiming in the source material is near half,
       then a correction pass that only ever lowers claims is precisely what the second member of the
       disjunction predicts, and no reviewer-bias term is required to explain the direction.
       ABSTRACT-ONLY.
    2. "Hallucinations in generative AI: A threat to scholarly integrity and the urgent need for
       publisher-led academically supervised verification." *ScienceDirect*,
       https://www.sciencedirect.com/science/article/abs/pii/S221462962600191X
       [authors and year unverified]
       — Supports the same limb for generated rather than human text: the documented failure mode of
       generative systems in scholarly contexts is fabrication and overstatement, i.e. errors whose
       correction is by construction downward. ABSTRACT-ONLY.
    3. Editage Blog, "What Is Hedging Language? Meaning, Examples, and Importance."
       https://www.editage.com/blog/what-is-hedging-language-meaning-examples-and-importance/
       — Notes that language models are trained to avoid overclaiming and hedge, but that model hedging
       is generic and applied regardless of how well a specific claim is supported. Weakly supportive:
       it implies that where a generated claim *is* unhedged and specific, it is more likely than
       baseline to be unwarranted — so downward correction is the expected repair. Practitioner blog,
       not research. SNIPPET-ONLY.
    4. "The evolution of distorted beliefs vs. mistaken choices under asymmetric error costs."
       PMC10427456, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10427456/
       [authors and year unverified]
       — Error-management-theory result: where the costs of the two error types differ, systems are
       shifted toward committing the cheaper error more often in order to avoid the expensive one.
       Supports the *first* member of the disjunction as a normative reading — a corrector operating
       under asymmetric costs (an unsupported strong claim is expensive; an over-cautious weak claim is
       cheap) *should* correct downward preferentially, and doing so is the system working as designed
       rather than a bias. ABSTRACT-ONLY.
    5. "Neyman-Pearson Hypothesis Testing, Epistemic Reliability and Pragmatic Value-Laden Asymmetric
       Error Risks." arXiv:2107.01944 [authors unverified]
       — Argues that pragmatically driven asymmetry in error probabilities can be epistemically
       beneficial, and that it is legitimate to design a test so that erroneous rejection is the
       pragmatically worse error. Provides the theoretical grounding for reading systematic downward
       correction as a justified policy rather than a defect of the corrector. ABSTRACT-ONLY.
    6. "Error rates of human reviewers during abstract screening in systematic reviews." PMC6959565,
       https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6959565/ [authors and year unverified]; and
       secondary summaries of proofreading and inspection detection rates (individual inspectors
       working alone find ~40–60% of errors; group inspection 70–80%), via
       https://arxiv.org/pdf/0801.3114 ("Thinking is Bad: Implications of Human Error Research for
       Spreadsheet Research and Practice") [authors unverified]
       — Recorded for honesty: these cut *against* the exhaustiveness claim by establishing that
       single-reviewer review is substantially less complete than multi-reviewer review, which is the
       structural condition under which a third member (reviewer-specific bias) becomes live.
       SNIPPET-ONLY.
    7. "How Far Are We From True Auto-Research?" arXiv:2605.19156 [authors unverified]
       — Reports that self-refinement is effective at ideation and experiment execution but limited for
       paper writing, where revising "tends to leave scores unchanged or lower them," and that
       "single-reviewer self-evaluation drifts toward the reviewer's own bias, motivating multi-reviewer
       protocols." This is the most directly on-point source located and it supports the *third* member
       — i.e. it is evidence against the item as stated. Reported here because 15a does not cherry-pick.
       SNIPPET-ONLY.

  Strength of support: Weak-to-Moderate

  Summary: There is genuine support for both stated members of the disjunction. The second member —
    that the original pass was over-confident — is backed by a large-corpus measurement of causal
    overclaiming in 46% of 194,631 social science articles, and by the generative-AI integrity
    literature documenting fabrication and overstatement as the characteristic failure mode of
    generated scholarly text. Against a base rate that high, a correction series that only ever lowers
    claims is unremarkable and needs no further explanation. The first member — that the system is
    working as designed — is backed by error-management theory and by the philosophy-of-statistics
    treatment of asymmetric error risks: where one error type is much more costly than the other,
    directional conservatism is a justified policy, not a distortion. Both members are therefore live
    and well-grounded. What the search cannot support is the *exhaustiveness* of the pair. The one
    source located that speaks directly to single-reviewer self-correction reports that self-revision
    of written work "tends to leave scores unchanged or lower them" and that single-reviewer
    self-evaluation drifts toward the reviewer's own bias; the human-error literature independently
    reports that a lone reviewer finds only 40–60% of errors against 70–80% for a group. 14b's third
    member is thus not merely conceivable — it has direct, if thin, empirical warrant.

  Caveats: (1) This search was thin (three queries) for a Critical-priority item; the anchoring
    literature and any study of directional asymmetry in post-hoc correction series were not reached,
    and either could change the picture. (2) The over-claiming base-rate evidence is about *human*
    social-science publications and about generative fabrication; neither population is the C2A2
    corpus, and transfer is assumed rather than shown. (3) Error-management theory justifies
    directional conservatism as *adaptive*, which is not the same as justifying it as *accurate* — it
    explicitly predicts an increased rate of the cheap error, which in this setting means
    under-claiming. That is precisely the artefact 14b worries about, so source 4 arguably supports
    both the first member and the third. (4) The strongest on-point source (7) is against the item.
    (5) All sources read at abstract or snippet level; no full text retrieved; several have
    unverified authorship.

  Recommendation: PARTIALLY-SUPPORTED

  PARTIAL NOVELTY-FLAG:
    Supported sub-claims: (i) that over-claiming is prevalent enough in both human and generated
    scholarly text to explain a downward-only correction series without invoking corrector bias;
    (ii) that directional conservatism under asymmetric error costs is a normatively defensible
    design, not a defect.
    Unsupported sub-claim: that the two members *exhaust* the space. The located evidence on
    single-reviewer self-correction points the other way.
    Unaddressed sub-claim: **the base rate and direction of revision in a correction series where the
    same actor proposes, applies and scores the correction, with no adjudicator ruling on any of
    them.** I found literature on self-review *detection* rates and on single-reviewer bias drift, but
    none measuring the *directional* asymmetry of self-applied, self-scored corrections under an
    absent adjudicator. Since the item notes this bears on OPEN-165 and on whether the accelerator's
    central question is being adjudicated on a biased sample, this gap is material and is flagged as
    a candidate for in-house measurement (independent re-review of a sample of the six) rather than
    further searching.
