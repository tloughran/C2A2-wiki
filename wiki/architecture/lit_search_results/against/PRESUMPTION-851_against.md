SEARCH-AGAINST-PRESUMPTION-851:
  Date searched: 2026-08-25
  Original item: PRESUMPTION-851
  Original statement: "[inferred] That corroboration is external if its content is external —
    independence of evidence conferred by externality of authorship, when selection was internal."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-851
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by tracing the selection path of a source credited as external validation.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: Queries run 2026-08-25: citation distortion and selective citation networks;
    congeniality bias and selective exposure to information; self-preference bias in LLM judges and
    evaluators; pre-registration of search strategy as a control on selection. Venues reached: BMJ,
    Psychological Bulletin, NeurIPS 2024 proceedings, arXiv cs.CL/cs.AI (2024–2026), James Lind
    Library, Systematic Reviews methods guidance. Date range: 2009–2026. Depth: MODERATE-to-
    COMPREHENSIVE on the selection-bias and self-preference legs. Gaps: web-search budget was
    exhausted before I could search the formal epistemology of evidential independence (conditional
    independence / common-cause structures in testimony), which is the cleanest theoretical
    statement of the objection and would strengthen this file; several 2026 arXiv items are index
    entries whose authorship I could not verify.

  Challenging evidence found: Yes

  Sources:
    1. Greenberg, S. A., 2009. "How citation distortions create unfounded authority: analysis of a
       citation network." BMJ 339:b2680. PMID 19622839.
       — The most direct challenge available. A complete citation network of 242 papers and 675
       citations, containing 220,553 citation paths supporting a single belief, in which unfounded
       authority arose through citation bias against refuting papers, amplification by papers
       presenting no data, and invention (hypothesis converted to accepted fact). Every one of those
       papers was externally authored. Externality of authorship provided no protection whatever;
       the distortion lived entirely in the selection. ABSTRACT plus James Lind Library summary.
    2. Hart, W., Albarracín, D., Eagly, A. H., Brechan, I., Lindberg, M. J., & Merrill, L., 2009.
       "Feeling validated versus being correct: a meta-analysis of selective exposure to
       information." Psychological Bulletin, 135(4). PMID 19586162.
       — Meta-analytic estimate of the congeniality bias: a moderate preference for congenial over
       uncongenial information, d = 0.36, strengthened where the belief is value-relevant or held
       with conviction. Quantifies the size of the selection distortion a motivated selector
       introduces even when drawing from a fully external corpus. ABSTRACT-ONLY.
    3. Panickssery, A., Bowman, S. R., & Feng, S., 2024. "LLM Evaluators Recognize and Favor Their
       Own Generations." Advances in Neural Information Processing Systems 37 (NeurIPS 2024).
       https://proceedings.neurips.cc/paper_files/paper/2024/hash/7f1f0218e45f5414c79c0679633e47bc-Abstract-Conference.html
       — Directly on the reflexive case (REVISE-350). LLM evaluators score their own outputs higher
       than human annotators do, and the strength of self-preference correlates with the model's
       ability to recognise its own output. Where selector and assessor share a generator, the
       assessment is not independent of the selection. FULL-TEXT (proceedings PDF).
    4. "Quantifying and Mitigating Self-Preference Bias of LLM Judges." arXiv:2604.22891.
       https://arxiv.org/pdf/2604.22891
       — Reports that judges favour themselves even when their own output is objectively worse, and
       that judges can favour outputs of models trained on their own synthetic data — i.e. the
       contamination survives one degree of separation. Authorship unverified. SNIPPET-ONLY.
    5. "Self-Preference Bias in Rubric-Based Evaluation of Large Language Models."
       arXiv:2604.06996. — Extends the finding to rubric-scored evaluation, which is the format
       C2A2's registers use. Authorship unverified. SNIPPET-ONLY.
    6. "Self- and Other-Labels Induce Bidirectional Bias in LLM Judges." arXiv:2608.18091.
       — Shows the bias is inducible by provenance labelling alone, independent of content, which
       is precisely the confound at issue when a source is labelled "external." Authorship
       unverified. SNIPPET-ONLY.
    7. Wataoka, K. et al., 2024. [self-preference bias in pairwise comparisons; attributed in the
       secondary literature reached, primary record not verified — details unverified]
       — Attributes self-preference to a familiarity effect, judges favouring lower-perplexity
       outputs. Relevant because it means the bias does not require self-recognition and so is not
       removable by anonymising provenance.
    8. PROSPERO / PRISMA-S search-reporting conventions (systematic-review methods guidance,
       consulted 2026-08-25 via KCL, UCL, Monash library guides).
       — The field's institutional answer to exactly this problem: the search strategy is registered
       before the search is run, and screening is done independently in duplicate, so selection
       cannot be adjusted to the result. Establishes that independence is treated as a property of
       the *procedure*, not of the corpus. FULL-TEXT (guidance pages).

  Strength of challenge: Strong

  Summary: The presumption confuses two different senses of independence, and the literature is
    unusually clear that it is the wrong one. Greenberg 2009 is the canonical demonstration: an
    entire belief system was built out of externally authored, peer-reviewed papers and acquired
    unfounded authority anyway, because the selection among them was biased against refutation and
    amplified by papers containing no data. Externality of authorship was never the load-bearing
    property; independence of selection was, and it was absent. Hart et al. 2009 gives the magnitude
    of the selector-side effect in humans (d = 0.36, larger where conviction is high), and the
    2024–2026 LLM-judge literature gives the machine analogue: evaluators favour their own
    generations, favour them even when they are worse, favour outputs of models trained on their own
    output, and can be swayed by provenance labels alone. That last finding is the sharpest for the
    reflexive case flagged in REVISE-350, because it means a source labelled "external" is treated
    differently for reasons having nothing to do with whether it is. Evidence synthesis has already
    codified the remedy — pre-registered search strategy and independent duplicate screening — which
    is itself evidence that the field regards corpus-externality as insufficient.

  Specific risks: If this presumption is false, then every C2A2 item currently carried as
    "externally corroborated" is mislabelled, and the mislabelling is systematically in one
    direction: toward confirmation. The mechanism is Greenberg's — supportive sources are retrieved,
    cited and amplified while sources that would weaken the claim are never surfaced, so the
    register accumulates apparent corroboration without any actual test having occurred. Two
    specific compounding hazards. First, ASSUMPTION-1164 is explicitly flagged in its own brief as
    "here read as externally corroborated," with its selection critique routed to this very item;
    if 851 is false, 1164's corroboration status is void and the two failures are not independent.
    Second, the pipeline's own architecture instantiates the self-preference case: where the agent
    that selected a source and the agent that assesses it share a generator, the NeurIPS 2024 result
    predicts inflated assessment, and the arXiv 2604.22891 result predicts that inserting an
    intermediate agent does not clear it. The register would then be measuring its own familiarity
    with a text rather than the text's evidential force.

  Mitigations available:
    - Pre-register the search strategy before running it, and record it in the register alongside
      the result, so that post hoc narrowing is visible (PROSPERO / PRISMA-S conventions).
    - Separate the "for" and "against" searches by construction and forbid cross-reading — which is
      what the 15a/15b split already does; this is the single strongest existing control and should
      be documented as the mitigation it is.
    - Require the against-agent to report NO-CHALLENGE-FOUND explicitly, so absence of challenge is
      a recorded outcome rather than a silence (mirrors PRISMA's treatment of unretrieved records).
    - Do not use the same generator for selection and assessment where avoidable; where unavoidable,
      apply a documented discount (Panickssery et al., NeurIPS 2024).
    - Strip provenance labels before assessment where the assessment is of content quality, given
      that labels alone induce bias (arXiv:2608.18091, unverified).
    - Retire the term "external corroboration" for sources whose selection path was internal;
      replace with "externally authored, internally selected," which is accurate and non-flattering.

  STEELMAN:
    Item: PRESUMPTION-851
    Strongest counterargument: Independence of evidence is a property of the selection procedure,
      not of the authorship of what got selected. Greenberg's citation network is the proof by
      construction: hundreds of independent authors, one belief, and unfounded authority produced
      purely by which of them were cited and how. Nothing about a paper's having been written
      elsewhere prevents an internal selector from retrieving only the papers that agree, and the
      measured congeniality effect says a motivated selector will do exactly that at
      d ≈ 0.36 — larger when the belief matters to them. For an automated pipeline the problem is
      worse rather than better, because the LLM-judge literature shows evaluators favour their own
      generations, favour them even when objectively worse, and can be moved by a provenance label
      alone; so where the selector and assessor share a generator, "external corroboration" is
      measuring familiarity, not agreement. The field that has thought hardest about this responded
      by pre-registering search strategies, which concedes the point directly.
    What would need to be true for C2A2 to be safe: (1) The search that produced the corroborating
      source must have been specified before its result was known, or run by an agent with no access
      to the claim's desired direction. (2) A disconfirmatory search of comparable effort must have
      been run over the same scope, with its null result recorded as an outcome. (3) The selector
      and the assessor must not share a generator, or a documented discount must be applied. The
      15a/15b split satisfies (2) and partially (1) by construction. Where all three hold, the
      corroboration is genuinely independent and this challenge does not apply; where the source was
      retrieved by the same process that formulated the claim, it does.
    How to test: Yes. Run a blind-selection replication: give the search brief to an agent that has
      not seen the claim's provenance or its desired direction, with a pre-specified query set, and
      compare the returned source set against the original. Measure overlap and, more importantly,
      directional composition — the fraction of supportive versus challenging sources in each set.
      If the blind set is substantially less supportive than the original, the selection was not
      independent and the "externally corroborated" label is falsified for that item. Applying this
      to ASSUMPTION-1164 specifically would resolve both items at once.

  Recommendation: CHALLENGED
