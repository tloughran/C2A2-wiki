SEARCH-FOR-PRESUMPTION-897:
  Date searched: 2026-08-31
  Original item: PRESUMPTION-897
  Original statement: [inferred] Vault growth is benign; no threshold exists at which it would be
    throttled.
  Generalizable limb searched: Is unbounded growth of a document corpus benign for retrieval and
    navigability, in particular where most added material is unintegrated (orphaned)?
  Series for context: eight weeks, 3,031 -> 4,729 pages, 2,337 -> 3,985 orphans, 69 connected.

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: UNDER-SEARCHED. Snippet-level results only; 2 queries run (Priority Medium, so no
    Pass 2 query); no full-text reads. Both queries were framed to find support and both returned
    material that qualifies rather than confirms the presumption.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-897
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference from the absence of any stated growth threshold, throttle, or
           integration gate anywhere in the pipeline's design
      15a: Searched for supporting literature (2026-08-31)
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. Shao and colleagues, 2024. "Scaling Retrieval-Based Language Models with a Trillion-Token
       Datastore." arXiv:2407.12854. — The best available support for the *benign growth* half, and
       it is partial. Snippet: datastore scaling brings major improvements on knowledge-intensive QA,
       performance increases monotonically with datastore scale, and the scaling dimension "remains
       unsaturated." Supports "more corpus is good" for retrieval-augmented generation over a
       *curated, deduplicated* web-scale datastore.
    2. "Less LLM, More Documents: Searching for Improved RAG," 2025. arXiv:2510.02657. — Corpus
       scaling consistently strengthens RAG and can match the gains of a larger model tier, "though
       with diminishing returns at larger scales." Support with an explicit qualifier.
    3. Same source / adjacent snippet on retrieval accuracy. — Directly counter to the presumption:
       as corpus size increases, retrieval approaches "exhibit a gradual decrease in retrieval
       accuracy," described as a common phenomenon in information retrieval as the number of
       potential matches for a query grows. Recorded here because a FOR search that surfaces the
       counter-finding must report it.
    4. Zettelkasten Forum and Christian Tietze, "Zettelkasten Orphanage" (forum.christiantietze.de).
       Practitioner sources, not research. — Offer the only found argument for orphan tolerance:
       an "orphanage" can be a holding area from which implicit themes are later extracted into
       explicit structure notes, and a note taken years ago "may find a new home in a department
       that didn't exist when it was created." Full-text search helps surface relevant but unlinked
       notes. This is a real argument that orphans are not immediately wasted.
    5. Same practitioner sources, counter-direction. — Also state that unlinked and isolated notes
       "tend to lose much of their power," that an unlinked note "risks getting lost in the pile,"
       and that orphans proliferate specifically when notes are created rapidly without time to
       integrate them. The recommended practice is a bounded inbox, i.e. a throttle.

  Strength of support: Weak

  Summary: Searching in the supportive direction did not produce support for the presumption as
    stated. The RAG scaling literature supports a weaker and differently-scoped claim — that a larger
    retrieval datastore improves downstream QA — and even there the sources found attach diminishing
    returns and an explicit finding that raw retrieval accuracy degrades as corpus size grows. That
    literature also concerns machine retrieval over curated corpora, not human navigability of a
    personal wiki, and it presumes deduplication and quality filtering that the vault's growth
    pattern does not evidence. The personal-knowledge-management sources, which are the closer
    domain match, run the other way: they treat orphan proliferation as a known failure mode of rapid
    unintegrated capture and prescribe a bounded holding area precisely as a throttle. The strong
    limb of the presumption — that *no* threshold exists at which growth would be throttled — found
    no support at all; every source that engages with growth engages with it as something to be
    managed. The series is the aggravating detail: 1,698 pages added and 1,648 of them orphaned, so
    97% of eight weeks of growth arrived unintegrated and the connected fraction fell from roughly
    23% to 16%.

  Caveats: (a) Under-searched — 2 queries, Medium priority. A third query aimed at index bloat or
    navigability-at-scale in wikis specifically might yet find support and was not run. (b) The
    Zettelkasten material is forum and blog practice, not research, and reflects a manual-curation
    tradition whose assumptions may not hold for a machine-generated corpus where marginal
    authoring cost is near zero. (c) The RAG results are genuinely positive evidence for one reading
    of the presumption: if the vault's purpose is to be retrieved from by machine rather than
    navigated by a person, corpus growth may indeed be close to benign, and this search should not
    be read as settling that. The presumption's weakness is chiefly in its absolute form. (d) No
    source found identifies a specific numeric threshold for any corpus, so "no threshold exists"
    was not directly refuted either — it simply found no backing.

  Recommendation: NO-SUPPORT-FOUND
