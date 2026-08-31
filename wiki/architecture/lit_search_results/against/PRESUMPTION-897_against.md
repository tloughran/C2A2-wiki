SEARCH-AGAINST-PRESUMPTION-897:
  Date searched: 2026-08-31
  Original item: PRESUMPTION-897
  Original statement: [inferred] Vault growth is benign; no threshold exists at which it would be
    throttled.
  Generalizable limb searched: Does corpus growth without integration degrade retrieval,
    navigability and usefulness — i.e. is there a growth regime that is net-negative?
  Series under test: eight weeks, 3,031 → 4,729 pages (+56%), 2,337 → 3,985 orphans (+70%),
    connected pages +69 (+~5% of the non-orphan base).

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: Weak-to-moderate. 2 queries (Priority Medium — no Pass 2, per budget). Both
    returned practitioner/trade material (SEO, personal knowledge management) rather than
    peer-reviewed work. UNDER-SEARCHED: I ran no query on the academic literatures that would bear
    most directly — information retrieval precision/recall vs. collection size, Wikipedia
    orphan-article and stub-quality studies, or hypertext navigability research. The direction of
    the finding is well-attested in practice but the evidential base I actually saw is thin.
    Snippet-level reading only.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-897
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the absence of any throttle, threshold or alarm in the growth reporting —
           growth is measured and narrated but never evaluated.
      15b: Searched for challenging literature (2026-08-31)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Multiple SEO practitioner sources, 2025-2026 (Keyword Insights, "Orphan Pages: The Hidden
       Enemy of SEO"; DefiniteSEO, "Orphan Pages in SEO: Detection, Fixes & Prevention"; OWDT,
       "What are orphan pages in SEO and why they hurt rankings"). — Converging practitioner claim
       that orphan pages are not merely inert: on large sites they dilute topical relevance, consume
       crawl budget, and make crawling inconsistent, which destabilises indexing and freshness for
       the *connected* pages too. This is the specific mechanism by which growth stops being benign
       — the cost lands on the good content, not only on the orphans. Trade sources with a
       commercial interest in finding problems; treat as hypothesis, not evidence.
    2. "Unattributed" (unattributed.cc), 2026-07-19. "Note-Taking and Personal Knowledge
       Management." — States that PKM works only when saved material comes back into use, and that
       a large archive with weak retrieval is "only a storage habit." Directly denies that
       accumulation is self-justifying. Blog source.
    3. Collector's fallacy, as summarised across the PKM sources returned (Jirak, Medium, "How to
       Build a Personal Knowledge Base That Actually Works"; Atlas Workspace, "Personal Knowledge
       Management (2026): The Practical Guide"). — Names the failure mode: collecting without
       processing, where the act of saving substitutes for the act of integrating, producing an
       archive of unconnected material. C2A2's series is a textbook instance — 84% of the corpus is
       now orphaned and the orphan share is rising.
    4. Toft, 2023. "Why I Gave Up on Personal Knowledge Management — and What I Do Instead."
       douglastoft.wordpress.com. — First-person negative case: the maintenance overhead of a
       growing unconnected system exceeded its returns. Anecdotal; included only as an existence
       proof that practitioners do hit and recognise a threshold.

  Strength of challenge: Moderate

  Summary: The presumption fails on its own numbers before the literature is consulted. Over eight
  weeks the vault added 1,698 pages, of which 1,648 (97%) were orphans; connected pages moved by 69.
  Growth is essentially pure accumulation, and the orphan share rose from 77% to 84%. The literature
  I found does not establish a specific threshold, but it does uniformly contradict the "benign"
  half of 897: unconnected material is described as imposing costs on retrieval and on the
  integrated material around it, not as neutral ballast. What I could not establish, on two queries
  of trade sources, is the magnitude of that cost for a local Obsidian-style vault, where there is
  no crawl budget and search is cheap. So the honest position is: "no threshold exists" is
  unsupported and the trend is adverse, but "growth is actively harmful at current scale" is also
  not demonstrated by anything I read.

  Specific risks: If growth is not benign, the primary casualty is the pipeline's own outputs — an
  84%-orphan corpus means graph-derived measures (hub counts, connectivity, tradition clustering)
  are computed over a shrinking fraction of the material while being reported as properties of the
  vault. The visualization has a hard node limit of 2000 (per project config) against 4,729 pages,
  so the rendered graph is already showing under half the corpus; at current growth that gap widens
  every week and the picture the graph gives becomes progressively less representative without
  anything in the reporting flagging it. Second risk: the absence of a threshold means there is no
  event that would ever trigger review — the presumption is unfalsifiable as currently held.

  Mitigations available: Report the orphan *ratio* alongside the count, so the trend is visible as a
  ratio rather than as growth. Set an explicit threshold and state it, even arbitrarily — the value
  of a threshold here is that it creates a trigger, not that it is correct. Distinguish intake from
  integration in the weekly numbers so "growth" cannot be reported without its integration deficit.
  Consider a staging area: new pages land unintegrated and are excluded from graph statistics until
  linked, which makes the deficit structural rather than a metric.

  STEELMAN:
    Strongest counterargument: A vault is an archive, not a website, and the SEO literature does not
    transfer — there is no crawl budget, no ranking, and no competition for attention between pages.
    An orphan page costs disk and nothing else; it remains fully retrievable by full-text search,
    which is how most vault lookups actually happen. "Orphan" is an artefact of measuring
    connectivity by wikilink, and a page can be well-integrated conceptually while having no inbound
    link. Premature throttling would be the more damaging error: it would suppress ingestion of
    material whose relevance only becomes apparent later, which is the whole point of keeping a
    vault rather than a reading list. The collector's-fallacy critique is aimed at humans managing
    attention, not at machine-readable corpora where recall is cheap.
    What would need to be true for C2A2 to be safe: Retrieval quality would have to be stable or
    improving as the corpus grows — i.e. the questions the vault is actually asked would have to be
    answered as well at 4,729 pages as at 3,031. Nothing in the current reporting measures this.
    How to test: Build a small fixed set of ~20 retrieval queries with known-good answers. Run them
    against the 3,031-page snapshot and the 4,729-page snapshot and compare precision and rank of
    the correct answer. If retrieval is flat or better, growth is benign at this scale and 897
    survives. If precision degrades, the threshold is already behind us. This is a cheap, decisive
    test and should displace further literature search on this item.

  Recommendation: PARTIALLY-CHALLENGED
