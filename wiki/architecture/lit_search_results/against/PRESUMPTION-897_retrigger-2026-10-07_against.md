SEARCH-AGAINST-PRESUMPTION-897 (RE-TRIGGER cycle 1):
  Date searched: 2026-10-07
  Original item: PRESUMPTION-897
  Original statement (per MONITOR-586): [inferred] "Vault growth is benign; no threshold exists at which
    it would be throttled."
  Owed this cycle: peer-reviewed sources (cycle 0 found only trade material) on (a) retrieval quality as
    a function of corpus size / index bloat; (b) wiki navigability and orphan articles at scale.
  Series carried (MONITOR-586): 3,031 → 4,729 pages over 8 weeks; orphans 2,337 → 3,985 (97% of growth);
    orphan share 77% → 84%; connected fraction ~23% → ~16% (intake rule: raise to HIGH below 15%).

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for* file,
    `lit_search_returns.md`, or today's 15a output.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 1)]
    Original item: PRESUMPTION-897
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the absence of any throttle, threshold or alarm in growth reporting.
      15b (2026-08-31): PARTIALLY-CHALLENGED (Moderate); 2 queries; SEO/PKM trade material only.
      15c: DISPOSITION-881 → MONITOR-586.
      15d (2026-09-20): Re-triggered; owed = peer-reviewed IR / wiki-navigability pass.
      15b (re-trigger cycle 1, 2026-10-07): 3 searches, 2 fetches (abstracts). Located three peer-reviewed
        sources, two directly on point. Cycle-0's "no peer-reviewed source" gap is closed.
    Current status: PARTIALLY-CHALLENGED

  EVIDENCE GRADE: two abstract-level fetches; one search-result. Preliminary scope.

  Challenging evidence found: Yes (on the "no threshold" limb); Partial (on magnitude for this vault)

  Sources:
    1. Reimers, N. & Gurevych, I. 2021. "The Curse of Dense Low-Dimensional Information Retrieval for
       Large Index Sizes." ACL-IJCNLP 2021 (short), arXiv:2012.14210. [fetched — abstract] "Performance
       for dense representations decreases quicker than sparse representations for increasing index
       sizes ... this can even lead to a tipping point where at a certain index size sparse
       representations outperform dense representations"; mechanism: lower dimension → higher chance
       of false positives (returning irrelevant documents). Bearing: direct, peer-reviewed, theoretical
       AND empirical evidence that retrieval quality is a decreasing function of index size, with a
       tipping point. This contradicts "no threshold exists" for any embedding-based retrieval over the
       vault. It does not by itself say where the tipping point is for 4,729 pages (the paper's
       regime is far larger).
    2. Arora, A., West, R. & Gerlach, M. 2024. "Orphan Articles: The Dark Matter of Wikipedia." ICWSM
       18(1):100–112, arXiv:2306.03940. [fetched — abstract] ~15% of Wikipedia articles (8.8M) are
       orphans, "de facto invisible to readers navigating Wikipedia"; quasi-experimental CAUSAL evidence
       that adding in-links raises pageviews; frames orphans as a "challenge of maintenance associated
       with content creation at scale." Bearing: peer-reviewed confirmation that orphan status causally
       reduces use. Note the base rate: Wikipedia, which the authors treat as having a serious orphan
       problem, is at ~15%; the vault is at 84% and rising.
    3. Cuconasu, F. et al. 2024. "The Power of Noise: Redefining Retrieval for RAG Systems." SIGIR 2024,
       arXiv:2401.14887. [search-result] Highly-scored but NON-relevant retrieved passages degrade LLM
       answer accuracy. HONEST CAVEAT: the same paper reports that adding RANDOM documents can IMPROVE
       accuracy (up to 35%). Bearing: growth harms RAG specifically through near-miss distractors (the
       kind a topically dense, weakly-integrated vault generates), not through sheer volume. This is a
       boundary condition, not a blanket "more is worse."

  Strength of challenge: Moderate (upgraded in evidential grade from trade to peer-reviewed; not
    upgraded to Strong because no source measures a vault of this size or this retrieval setup)

  Summary: The cycle-0 gap is closed: there is peer-reviewed literature, and it runs against the
    "no threshold" limb. Dense retrieval degrades with index size and can cross a tipping point
    (Reimers & Gurevych); orphan articles are causally under-used, and the field treats a 15% orphan
    rate as a maintenance crisis (Arora, West & Gerlach); and RAG accuracy is damaged specifically by
    plausible-but-irrelevant retrievals (Cuconasu et al.). None of the three establishes harm at 4,729
    pages, and the Power of Noise result shows volume per se is not the damaging variable — near-miss
    density is. The defensible statement is: thresholds exist in kind; their location for this vault
    is unmeasured; the vault's orphan rate is ~5.6× the level the Wikipedia literature already treats
    as a problem.

  Specific risks: (i) any embedding-based retrieval over the vault (narration tracks, agent lookups)
    silently loses precision as pages accumulate; (ii) 84% orphans are invisible to graph navigation —
    and the visualization's 2000-node cap means the rendered graph shows <45% of the corpus;
    (iii) near-duplicate inbox/proposal cards are exactly the "high-scoring non-relevant" distractor class.

  Mitigations available: A fixed probe-question set run at each growth milestone (MONITOR-586's own
    "retrieval-quality measurement"); hybrid sparse+dense retrieval (Reimers & Gurevych's tipping point
    favours sparse at scale); de-orphanization as a tracked rate; a stated throttle trigger (e.g. the
    15% connected-fraction rule already on the books).

  Recommendation: PARTIALLY-CHALLENGED — "no threshold exists" contradicted in kind by peer-reviewed IR
    work; "benign at current size" neither shown nor refuted.

STEELMAN:
  Item: PRESUMPTION-897
  Strongest counterargument: The IR literature does not say "bigger corpora are fine up to a point";
    it says retrieval precision falls monotonically with index size and that dense methods can fall off
    a cliff. The Wikipedia literature says that orphaned content is causally invisible and that 15%
    orphaned is a serious maintenance failure. A vault adding pages at 97% orphan rate is therefore not
    in a benign regime that has yet to meet its threshold; it is accumulating, every week, the two
    quantities the literature identifies as the drivers of degradation — index size and unlinked mass —
    with no instrument that would detect the crossing. "No threshold" is unfalsifiable as held.
  What would need to be true for C2A2 to be safe: retrieval over the vault is sparse/lexical or
    structure-guided rather than dense; questions actually asked of the vault are answered equally well
    at 4,729 as at 3,031 pages (measured, not assumed).
  How to test: fix 30 representative questions; score answer quality against a frozen 3,031-page snapshot
    vs the current vault; repeat at each +1,000 pages.
