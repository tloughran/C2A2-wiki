SEARCH-FOR-PRESUMPTION-844 (OWED LIMB ONLY: code-review change-set-size / review-effectiveness literature — NOVELTY flag test):
  Date searched: 2026-10-09
  Original item: PRESUMPTION-844
  Original statement: [inferred] That the review artifact is the right instrument and only its depth is the
    problem. The 677 KB, 54-card single-page review is treated as a neutral container rather than a design variable.
  Limbs searched: the code-review change-set-size / decomposition / review-effectiveness literature, explicitly
    unsearched at intake. Purpose: to test whether 15a's provisional NOVELTY flag ("nothing on artifact size or
    container as a throughput variable") survives. The paired SPLIT-TEST limb is an in-house test and was not searched.
  Cycle: 1 (RE-TRIGGER by 15d 2026-08-30, MONITOR-543; processed 2026-10-09)

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c → 15d → 15a (re-trigger cycle 1)]
    Original item: PRESUMPTION-844
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from four escalations that framed the review queue only by depth and never questioned the
        single-page artifact
      15a (cycle 0): partial support (volume limb; alert-quality limb); provisional NOVELTY-FLAG on interface
        granularity; code-review size literature declared unsearched
      15b (cycle 0): challenged the supporting apparatus (decision fatigue contested; 400-LOC figure traced to a
        blog); recommended a split-test
      15c: → MONITOR-543 (High, NOVELTY-flagged); split-test endorsed
      15d: re-triggered cycle 1 2026-08-30; did not evaluate evidence
      15a (cycle 1, 2026-10-09): 3 searches, 2 fetch attempts (1 full text, 1 FAILED); see below
    Current status: PARTIALLY-SUPPORTED (Moderate). The size-of-review-unit literature exists and supports "the
      unit presented to the reviewer is a variable". NOVELTY is reduced to the container/batch dimension.

  Search scope: 3 web searches: (a) patch size vs review effectiveness (Rigby & Bird; Cisco/SmartBear 200–400
    LOC); (b) Bacchelli & Bird 2013 on understanding; (c) change decomposition / untangling / stacked PRs and review
    outcomes. Fetches: arxiv.org/abs/1805.10978 FAILED (URL refused by fetch tool, not in provenance set; not
    retried); peerj.com/articles/cs-193 (di Biase et al. 2019) FULL TEXT. Baum/Schneider/Bacchelli 2019, Rigby
    et al. 2014, Ram et al. 2018 and Sadowski et al. 2018 are cited WITHIN the fetched paper and not read directly.

  Supporting evidence found: Partial (Yes for unit size as a variable; No for the page-container)

  Sources:
    1. di Biase, M., Bruntink, M., van Deursen, A. & Bacchelli, A., 2019. "The effects of change decomposition on
       code review — a controlled experiment." PeerJ Computer Science 5:e193. [fetched, full text] n=28; one
       tangled PR vs two decomposed PRs (~100 LOC, 7 files). Decomposition gave fewer false positives (6 vs 1;
       p=0.03; Cliff's δ=0.36, medium) and more suggested improvements (7 vs 19, n.s.). There was NO significant
       difference in defects found, review time or rationale understanding. The authors explain the time result by
       the context-switch overhead of reviewing two PRs instead of one. They state that negative effects of tangled
       review "could be visible when a reviewer has to assess a large number of changes every day". That is the
       C2A2 situation, and the paper did not test it.
    2. Baum, T., Schneider, K. & Bacchelli, A., 2019 (as cited in source 1). [cited within fetched text; not read]
       "performance in code review is significantly higher when code changes are small, whereas complex and longer
       changes lead to lower review effectiveness." Rigby et al. 2014 (as cited): small change size is "essential
       to the more fine-grained style of peer review" across six OSS projects. Ram et al. 2018 (as cited):
       reviewability is empirically defined partly by change size.
    3. Cisco/SmartBear study (Cohen et al., "largest case study of code reviews ever", via AgileConnection /
       StickyMinds / SmartBear). [search-result] Defect density found falls sharply above ~200 LOC; 400 LOC
       "absolute maximum"; ≤400–500 LOC/hour. These are industry data from one team, with methodology not reported.
       This is the primary trail for the "400-LOC blog" figure 15b flagged. It is now traced to an industry source,
       not to peer review.
    4. Bacchelli, A. & Bird, C., 2013. "Expectations, Outcomes, and Challenges of Modern Code Review." ICSE 2013.
       [search-result, abstract] Understanding the change is "the key aspect of code reviewing". Current tools do not
       meet reviewers' understanding needs. This supports treating the review TOOL/ARTIFACT as a variable.
    5. arXiv 2311.02489 ("Does Code Review Speed Matter for Practitioners?"). [search-result] Summarises prior work
       finding that patch size negatively affects every review-effectiveness outcome considered. A 2018 JSERD
       patch-rejection study [search-result] counters that size is a minor factor.

  Strength of support: Moderate for "the size/composition of what is put before a reviewer affects review outcomes"
    (one controlled experiment read in full plus a convergent cited body). None for single-page versus paginated
    presentation of MANY INDEPENDENT decisions.

  Summary: The code-review literature exists, as cycle 0 predicted, and it weakens the NOVELTY flag. Change size
    and tangling are established review-outcome variables (Baum et al.; Rigby et al.; Cisco data). A controlled
    experiment (di Biase et al.) shows that splitting a review unit improves precision without costing time, even
    after context-switch overhead. That supports the presumption's core move: the unit put in front of the reviewer
    is a design choice, not terrain. But every study varies the size of ONE change; none varies the container in
    which a reviewer meets a QUEUE of independent decisions (54 cards on one page). The di Biase time null is also a
    caution: decomposition does not automatically speed review, so pagination alone may not drain the queue.

  Caveats: (i) Code review is a judgement on one artefact; C2A2's gate is 54 independent accept/reject decisions,
    which is closer to batch triage. (ii) Small n (28) and one ~100-LOC change in source 1. (iii) Cisco figures are
    industry, one team, methodology not given. (iv) Sources 2 and 5 were not read directly.

  Recommendation: PARTIALLY-SUPPORTED (Moderate). The NOVELTY-FLAG should be NARROWED, not kept as stated. The
    within-system split-test MONITOR-543 endorsed remains the right instrument for the narrowed residue.

  NOVELTY-FLAG: Partial (narrowed). Item PRESUMPTION-844. Searched: change size, tangled/decomposed changes,
    MCR understanding. Finding: unit-size effects on review are established. No source addresses presentation
    granularity of a multi-decision review queue (single page vs paginated vs per-item). Implication: the residual
    novelty is the CONTAINER for a queue of decisions, not "artifact size as a variable".

  Independence attestation: Read: 15a definition; batch_context.md (queue block, MONITOR-543); for/PRESUMPTION-888_
    retrigger-2026-10-08_for.md (format); presumptions.md statement via grep. NOT read: any against/ file; any 15b
    output dated 2026-10-09.
