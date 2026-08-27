SEARCH-FOR-ASSUMPTION-1219:
  Date searched: 2026-08-26
  Original item: ASSUMPTION-1219
  Queue ref: LIT-QUEUE — 2026-08-25 (Agents 14a + 14b end-of-day intake), item 5 of 14 — Priority High
  Original statement: "Every Summa repair today lowered confidence. Four repairs, four downward.
    Combined with yesterday's two-corrected-downward result, that's six consecutive corrections that
    made the wiki claim *less*. That is either the system working exactly as designed, or a sign the
    original synthesis pass was systematically over-confident — and which of those it is bears
    directly on OPEN-165."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1219
    Item type: ASSUMPTION (stated — quoted)
    Transform at each step:
      14a: Extracted verbatim from the evening summary ("For Morning Discussion") and deliberately
        left as a two-member disjunction, passing the exhaustiveness question to 14b rather than
        resolving it here. That exhaustiveness question is filed as PRESUMPTION-880.
      15a: Searched for supporting literature
    Current status: UNTESTED (entering 15a); 15a result SUPPORTED

  Search scope: WebSearch only, 2026-08-26. WebFetch unavailable to this run; **all sources
    SNIPPET-ONLY.**
    Queries covered: (a) overconfidence and confidence calibration — the hard–easy effect, the
    general finding that confidence exceeds accuracy; (b) empirical before/after evidence on what
    peer review does to strength of claims and acknowledgment of limitations; (c) LLM self-correction
    dynamics — whether revision under critique moves systematically in one direction; (d) conservatism
    bias and insufficient belief revision; (e) LLM confidence calibration and overconfidence.
    Assessment: **good coverage of both limbs of the disjunction; the search found direct support for
    each, plus a third mechanism the disjunction omits.** Limbs NOT covered: (i) the
    peer-review/editorial-decision literature on *asymmetric error costs* (Type I vs Type II in
    gatekeeping) — I searched for it and the results did not surface it; it is the most likely home
    for a normative account of why downward correction should predominate and is a real gap;
    (ii) statistical base rates of upward vs. downward revision in post-publication correction
    notices and errata, which the queue explicitly asks for and which I did not locate; (iii) the
    forecasting/superforecasting literature on update direction. (iv) I did not test the sampling
    question at all: six is a very small n and the run-length probability under a fair coin is 1/32
    (~3%), which is suggestive but not decisive — no literature is needed to observe this and I flag
    it as an in-house calculation rather than a finding.

  Supporting evidence found: Yes — for both limbs

  Sources:
    — Limb A: "the system working exactly as designed" (review is supposed to move claims downward)
    1. "Impact of peer review on discussion of study limitations and strength of claims in randomized
       trial reports: a before and after study." *Research Integrity and Peer Review* (2019),
       DOI 10.1186/s41073-019-0078-2. [authors unverified]
       https://link.springer.com/article/10.1186/s41073-019-0078-2 ·
       https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6745784/
       — The single most on-point source for Limb A. A before/after design comparing *submitted
       manuscripts against their published versions* for all randomised trials published in 2015
       across 27 BioMed Central journals and BMJ Open, using automated detection of
       limitation-acknowledging sentences and hedging level. Its explicit premise is that "peer
       reviewers should spot and suggest changes to overstatements and claims that are too strong."
       This establishes that a review process which produces *only* downward corrections is behaving
       as the institution intends — i.e. Limb A is not merely a face-saving reading, it is the
       designed behaviour of review as such. I could not read the results section (SNIPPET-ONLY) and
       therefore **cannot report the study's effect size or even its direction of finding** — only
       its design and premise. This is a material limitation. SNIPPET-ONLY.

    — Limb B: "the original synthesis pass was systematically over-confident"
    2. "Overconfidence effect." Wikipedia (entry point to the Lichtenstein/Fischhoff/Phillips
       calibration tradition). https://en.wikipedia.org/wiki/Overconfidence_effect
       — Tertiary source, used as a pointer: confidence systematically exceeds accuracy. SNIPPET-ONLY.
    3. Baranski, J. V., & Petrusic, W. M. (1994). "The calibration and resolution of confidence in
       perceptual judgments." *Perception & Psychophysics*, DOI 10.3758/BF03205299.
       https://link.springer.com/article/10.3758/BF03205299 · https://pubmed.ncbi.nlm.nih.gov/8036121/
       [author names read from the Springer/PubMed listing; not independently confirmed]
       — Classic calibration finding: the **hard–easy effect** — underconfidence on easy judgments,
       overconfidence on hard ones. Directly relevant: cross-tradition synthesis is a hard judgment
       task, which is where overconfidence is predicted to be largest, so Limb B is the *expected*
       outcome under calibration theory rather than a surprising one. Also reports that trial-by-trial
       feedback improved resolution but **did not improve calibration** — bearing on whether repeated
       correction cycles will fix the underlying overconfidence or only its symptoms. SNIPPET-ONLY.
    4. "Overconfidence and Calibration in Medical VQA: Empirical Findings and Hallucination-Aware
       Mitigation." arXiv:2604.02543. [authors unverified] https://arxiv.org/pdf/2604.02543
       and "Confidence Calibration in Large Language Models." arXiv:2605.23909. [authors unverified]
       https://arxiv.org/pdf/2605.23909
       — Transfers the overconfidence finding to LLM-generated content, which is the relevant
       generator class here. SNIPPET-ONLY.
    5. "Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in Large Language
       Models." OpenReview. [authors unverified] https://openreview.net/forum?id=lyaHnHDdZl
       — Reports that overconfidence magnitude depends on question difficulty, format and domain, with
       hard questions showing the strongest effect — the hard–easy effect reproduced in LLMs.
       SNIPPET-ONLY.

    — A third mechanism the disjunction does not contain
    6. "Confidence v.s. Critique: A Decomposition of Self-Correction Capability for LLMs."
       arXiv:2412.19513; also ACL 2025 Long Papers. [authors unverified]
       https://arxiv.org/abs/2412.19513 · https://aclanthology.org/2025.acl-long.203.pdf
       — Decomposes self-correction into *confidence* (holding correct answers) and *critique*
       (fixing wrong ones) and finds a **trade-off**: improving one degrades the other. Identifies the
       problematic case where "the model initially generates a correct answer but lacks confidence in
       its correctness, subsequently producing a wrong answer after self-correction." SNIPPET-ONLY.
    7. "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of
       LLMs." *TACL* (2024/2025), DOI 10.1162/tacl_a_00713. [authors unverified]
       https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/ ·
       https://arxiv.org/html/2406.01297v3
       — Survey-level finding: accuracy frequently *declines* after self-correction. Identifies three
       failure mechanisms — answer wavering, prompt bias, and human-like cognitive bias — and reports
       that correct-to-wrong changes "occur systematically across models and tasks." Notes that
       prompts like "Are you sure?" significantly reduce model confidence and cause correct answers to
       be changed to incorrect ones. SNIPPET-ONLY.
    8. "A Probabilistic Inference Scaling Theory for LLM Self-Correction." arXiv:2508.16456.
       [authors unverified] https://arxiv.org/pdf/2508.16456 — theoretical treatment of the same
       dynamics. SNIPPET-ONLY.
    9. "Conservatism (belief revision)." Wikipedia; and "Conservatism in belief revision and
       participant skepticism." [authors, venue and year unverified]
       https://en.wikipedia.org/wiki/Conservatism_(belief_revision) ·
       https://www.researchgate.net/publication/284772086
       — The classical Edwards-tradition finding that people over-weight priors and under-weight new
       evidence. Included because it is the *counterweight* to Limb B: if the reviewing frame were
       conservative, corrections would be too small, not systematically directional. Tertiary/
       unverified sources; low weight. SNIPPET-ONLY.

  Strength of support: Moderate

  Summary: Both limbs of 14a's disjunction have real literature behind them, so the assumption as
    stated — that the six-correction run is explained by one or the other — is supported in the sense
    that neither limb is idle speculation. Limb A is supported institutionally: review exists in part
    to detect overstatement, and a formal before/after study of submitted-vs-published randomised
    trial reports was built on exactly that premise (source 1), which makes a uniformly downward
    correction series the *designed* signature of a working review process rather than an anomaly.
    Limb B is supported by the calibration literature, and supported with a sharpening: the hard–easy
    effect predicts that overconfidence is largest on difficult judgments (3, 5), and cross-tradition
    synthesis is a difficult judgment; overconfidence has been reproduced in LLM-generated content
    (4, 5). The search also surfaced something 14a's disjunction does not contain and which bears
    directly on OPEN-165: the LLM self-correction literature reports that revision *under critique*
    moves systematically in one direction as an artefact of the correction procedure itself — models
    change correct answers to incorrect ones when prompted to reconsider, correct-to-wrong flips occur
    systematically across models and tasks, and there is a documented confidence/critique trade-off
    (6, 7). On that account six consecutive downward corrections would be evidence about the
    *reviewer*, not about the original synthesis pass or the design of the system. That is a third
    live hypothesis, and it is the one that would most change what OPEN-165 should conclude.

  Caveats: (1) All SNIPPET-ONLY. Most consequentially, **I could not read the results of source 1** —
    only its design and stated premise — so I cannot report whether peer review was actually found to
    increase hedging, or by how much. The support for Limb A is therefore support for its
    *plausibility as the designed behaviour*, not confirmation that review empirically produces
    one-directional change. This should be treated as the weakest link in this file. (2) Several
    sources are 2026 preprints with unverified authorship; sources 2 and 9 are encyclopaedia entries.
    (3) The queue asks specifically for "base rates of upward vs. downward revision in post-hoc review
    of generated scholarly text." **I did not find these.** No located source gives a directional base
    rate for corrections. That is the item's central empirical question and it remains unanswered.
    (4) Domain transfer: the self-correction literature (6–8) concerns short-form question answering
    with verifiable ground truth. C2A2's repairs are confidence adjustments on interpretive synthesis
    claims where there is no ground truth to flip toward, so the correct-to-wrong finding does not
    transfer cleanly; what transfers is the weaker and still important point that *the act of
    reviewing has a direction of its own*. (5) n = 6. Under a null of unbiased correction the
    probability of a six-run in one direction is about 3%, which is suggestive but well short of
    decisive, and no literature is required to say so. (6) The disjunction's exhaustiveness is
    explicitly not my remit — 14a passed it to 14b as PRESUMPTION-880 — but source 6/7 material is
    directly relevant to it and I flag the overlap rather than silently duplicating the search.

  Recommendation: SUPPORTED

  PARTIAL NOVELTY-FLAG:
    Item: ASSUMPTION-1219
    Supported sub-claims: (i) that a review process producing only downward corrections may be
      functioning as designed — review is institutionally charged with detecting overstatement;
      (ii) that systematic initial overconfidence is well documented, is largest on hard judgment
      tasks, and reproduces in LLM-generated content; (iii) that a one-directional correction series
      is a recognised phenomenon with more than one available explanation.
    Third mechanism found, not in the disjunction: revision-under-critique has a documented direction
      of its own, independent of whether the original was overconfident and independent of whether the
      review process is working. This is not a novelty flag — the mechanism is published — but it is a
      **gap in the item as stated**, and it materially affects OPEN-165. Routed here for 14b's
      attention on PRESUMPTION-880 rather than resolved.
    Unaddressed: **directional base rates for post-hoc correction of generated scholarly text.** I
      found no study reporting the proportion of corrections that strengthen vs. weaken a claim in any
      corpus, machine-generated or otherwise. If C2A2 tallied direction across its own repair history
      — it already logs every repair — it would produce a number the literature does not appear to
      contain. As with ASSUMPTION-1206, this is a *measurement*, not a further literature question,
      and the independent-re-review test 14a already named as the testability condition is the right
      instrument.
