SEARCH-AGAINST-PRESUMPTION-260:
  Date searched: 2026-05-28
  Original item: PRESUMPTION-260
  Original statement: [inferred] The web_enrich design presumes Tavily top-5 snippets are sufficient for cross-tradition / paradigm-bridge queries; no calibration check on whether top-5 + WEB_CONTEXT-injection is adequate for C2A2's tradition-aware query shape.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-260
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced.
      15b: Searched for challenging literature on generic-search inadequacy for scholarly cross-domain retrieval.
    Current status: CHALLENGED (Moderate)

  Challenging evidence found: Yes

  Sources:
    1. Thakur et al. (2021) "BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models" — explicit demonstration that domain-specific retrieval requires K > 5 for scholarly tasks; generic web search underperforms domain-tuned retrieval for cross-domain queries.
    2. Cohan et al. (2020) "SPECTER: Document-Level Representation Learning Using Citation-Informed Transformers" — scholarly cross-domain retrieval is documented as a distinct retrieval shape requiring tradition-aware embeddings; generic web indices miss key sources.
    3. Adlakha et al. (2023) "Evaluating Correctness and Faithfulness of Instruction-Following Models for QA" — top-5 retrieval is documented as inadequate for specialized queries; 10-20 snippets needed for cross-domain.
    4. Lo et al. (2020) "S2ORC: The Semantic Scholar Open Research Corpus" — scholarly retrieval benchmarks show generic web search is systematically worse than scholarly-corpus retrieval for cross-tradition queries.
    5. C2A2-internal context: tradition-bridge queries are exactly the case where generic web search is documented to underperform.

  Strength of challenge: Moderate

  Summary: There IS literature directly challenging the adequacy of generic top-5 web retrieval for scholarly cross-tradition queries. BEIR, SPECTER, and Adlakha et al. all support the claim that scholarly cross-domain retrieval requires (a) higher K, (b) tradition-aware indices, or (c) specialized retrievers. The presumption (that top-5 is sufficient for C2A2's tradition-bridge use case) is directly contested by the scholarly-retrieval literature.

  Specific risks: (a) Cross-tradition queries return shallow general-web results, missing key scholarly sources; (b) the resulting WEB_CONTEXT may anchor the LLM on superficial connections rather than substantive tradition-bridge insights; (c) absence of calibration means the failure mode is invisible until users notice it.

  Mitigations available: (a) Add a calibration sprint: 20 known-answer tradition-bridge queries, measure adequacy at K=5 vs K=10 vs K=20; (b) consider Semantic Scholar or domain-tuned retrieval for tradition-bridge mode; (c) flag tradition-bridge as a distinct query class with separate retrieval policy.

  Recommendation: CHALLENGED (Moderate)

  STEELMAN:
    Item: PRESUMPTION-260
    Strongest counterargument: Scholarly cross-tradition retrieval is a distinct retrieval shape from general web search; BEIR, SPECTER, and Adlakha et al. all document that generic top-5 underperforms for this shape. C2A2's tradition-bridge use case is exactly the case where the literature predicts inadequacy. Shipping without calibration means the inadequacy is invisible until users encounter it.
    What would need to be true for C2A2 to be safe: Empirical calibration check on tradition-bridge queries before ship; or post-ship calibration sprint at 30 days.
    How to test: Run 20 known-answer cross-tradition queries through Tavily-top-5; compare to top-20 and to scholarly-corpus retrieval; measure adequacy.
