SEARCH-FOR-PRESUMPTION-310:
  Date searched: 2026-06-06
  Original item: PRESUMPTION-310
  Original statement: [inferred] Accepting "zero Civic<->Scientific cross-links" as honest signal presumes TF-IDF lexical similarity is a valid proxy for genuine inter-community relatedness; the verification confirmed the count, not the construct validity of TF-IDF edges.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-310
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated presumption that TF-IDF lexical similarity validly measures inter-community relatedness.
      15a: Searched for support that TF-IDF/cosine is a valid edge-construction method for document/community relatedness.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Salton & Buckley, "Term-weighting approaches in automatic text retrieval" (TF-IDF foundational); standard IR. — TF-IDF/cosine is the canonical, decades-validated baseline for document relatedness and is the default similarity-network edge construction in countless deployed systems.
    2. "Document Similarity Using TF-IDF and Cosine Similarity" (ResearchGate, 2024); osher.com.au applied write-up. — Documents that TF-IDF + cosine reliably recovers topical relatedness, especially within a shared vocabulary domain; supports using it as the relatedness proxy for community text.
    3. PyImageSearch, "TF-IDF vs Embeddings" (2026). — Concedes TF-IDF "ranks documents by keyword overlap"; within a domain where related items share vocabulary, keyword overlap IS a defensible relatedness signal, supporting TF-IDF edges as a reasonable first construct.

  Strength of support: Moderate

  Summary: TF-IDF/cosine is a well-established, defensible proxy for document relatedness and a standard edge-construction method for similarity networks, so using it to build community-relatedness edges is methodologically respectable rather than ad hoc. Within a shared vocabulary domain, keyword overlap tracks topical relatedness well, which supports trusting intra-domain edges. The support is qualified, however, precisely on the cross-domain case at issue: the same literature notes TF-IDF measures lexical, not semantic, overlap — so its validity as a relatedness proxy is strongest within a domain and weakest across domains (Civic vs Scientific), which is exactly where the "zero cross-links" claim is being read as signal.

  Caveats: The FOR case validates TF-IDF as a general relatedness baseline, not as a construct that can distinguish "genuinely unrelated" from "related but lexically divergent." The verification confirmed the edge COUNT, not that the edges measure relatedness in the cross-domain regime — a construct-validity gap the 15b search develops.

  Recommendation: SUPPORTED
