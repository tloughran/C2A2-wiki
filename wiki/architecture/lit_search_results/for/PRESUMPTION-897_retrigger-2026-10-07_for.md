SEARCH-FOR-PRESUMPTION-897 (OWED LIMBS ONLY: navigability at scale; orphan pages; index bloat; retrieval vs corpus size):
  Date searched: 2026-10-07
  Original item: PRESUMPTION-897
  Original statement: [inferred] Vault growth is benign; no threshold exists at which it would be throttled.
  Limbs searched: peer-reviewed literature on (a) wiki navigability and orphan pages as a corpus grows;
    (b) retrieval quality as a function of corpus/index size. "Support" = evidence that growth is benign,
    i.e. that more material does not degrade (or improves) findability/retrieval.
  Cycle: 1 (RE-TRIGGER by 15d 2026-09-20; processed 2026-10-07)

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c → 15d → 15a (re-trigger cycle 1)]
    Original item: PRESUMPTION-897
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption: vault grows 3,031 → 4,729 pages in eight weeks with no throttle
      15a (cycle 0, 2026-08-31): NO-SUPPORT-FOUND (Weak). Two queries; Shao et al. 2024 at snippet level;
        Zettelkasten practitioner material
      15c: DISPOSITION-881 → MONITOR-586
      15d: re-triggered cycle 1 2026-09-20; owed = peer-reviewed sources on navigability/index bloat/
        retrieval-vs-size
      15a (cycle 1, 2026-10-07): 3 searches, 2 fetches; see below
    Current status: PARTIALLY-SUPPORTED (on the retrieval limb only; NOT on the navigability limb)

  Search scope: 3 web searches (MassiveDS datastore scaling; Wikipedia orphan articles/navigability;
    dense-retrieval index-size degradation). 2 fetches (NeurIPS 2024 abstract page; ICWSM 2024 abstract
    page). Peer-reviewed sources were obtained this pass, which answers 15d's specific request.
    Preliminary scope.

  Supporting evidence found: Partial (conditional, and only for the retrieval limb)

  Sources:
    1. Shao, R., He, J., Asai, A., Shi, W., Dettmers, T., Min, S., Zettlemoyer, L. & Koh, P. W., 2024.
       "Scaling Retrieval-Based Language Models with a Trillion-Token Datastore." NeurIPS 37.
       doi:10.52202/079017-2896. [fetched, abstract] "Increasing the size of the datastore used by a
       retrieval-based LM monotonically improves language modeling and several downstream tasks without
       obvious saturation." This is the strongest peer-reviewed support for "more corpus is benign or
       better". The abstract also says the authors analysed "datastore quality filtering" and retriever
       improvements as moderators, so the benign result is conditioned on retrieval design.
    2. Reimers, N. & Gurevych, I., 2021. "The Curse of Dense Low-Dimensional Information Retrieval for Large
       Index Sizes." ACL-IJCNLP 2021 (short). [search-result] Recorded for completeness and the boundary it
       sets. Dense-retrieval precision falls faster than sparse (BM25) as the index grows, because false
       positives rise with size. Read supportively: growth is benign for SPARSE/lexical retrieval relative
       to dense, so whether growth is benign depends on the retriever. NOT support for the unconditioned
       statement.
    3. Arora, A., West, R. & Gerlach, M., 2024. "Orphan Articles: The Dark Matter of Wikipedia." ICWSM 18,
       100–112. doi:10.1609/icwsm.v18i1.31300. [fetched, abstract] Peer-reviewed study across 319 language
       editions: ~15% (8.8M) of articles are orphans and "de facto invisible to readers navigating
       Wikipedia". A quasi-experiment shows that de-orphanising causes a significant rise in pageviews. The
       authors frame this as a "challenge of maintenance associated with content creation at scale". NO
       support for benign growth on the navigability limb. Listed because it is the peer-reviewed source
       15d asked for, and on this limb the honest supportive result is null.

  Strength of support: Weak overall. Moderate for "a larger corpus can improve retrieval" under a
    well-designed retriever (Shao et al.). None for navigability.

  Summary: The peer-reviewed literature splits by access mode. For retrieval-mediated access there is
    strong evidence (NeurIPS 2024) that a larger datastore improves downstream performance without
    saturation, though dense low-dimensional retrievers lose precision as indices grow (ACL 2021). For
    link-mediated navigation, the one systematic peer-reviewed study found (ICWSM 2024) treats orphaned
    content as invisible and causally shows that linking restores visibility. That is the opposite of
    benign. By comparison, Wikipedia's orphan rate is ~15%, and the vault's last recorded series (from the
    cycle-0 file, ~84% orphaned) is far past it. Growth is benign only if the vault is read through a
    retriever that scales, and not through its link graph.

  Caveats: (i) Shao et al. concerns LM perplexity/QA over web-scale text, not a human-curated wiki.
    (ii) Reimers & Gurevych read at search-result level only. (iii) The vault orphan figure is carried from
    the cycle-0 file and is not re-measured here. (iv) No peer-reviewed source was found on a specific
    THRESHOLD for throttling; the "no threshold exists" clause is unaddressed in either direction.

  Recommendation: PARTIALLY-SUPPORTED on the retrieval limb (conditional on retriever type);
    NO-SUPPORT-FOUND on the navigability limb. The item's adverse reading now has a peer-reviewed anchor
    (Arora et al. 2024) where cycle 0 had only trade material.

  NOVELTY-FLAG: No.
