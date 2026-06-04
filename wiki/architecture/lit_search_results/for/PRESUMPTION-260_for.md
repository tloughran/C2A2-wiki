SEARCH-FOR-PRESUMPTION-260:
  Date searched: 2026-05-28
  Original item: PRESUMPTION-260
  Original statement: [inferred] The web_enrich design presumes Tavily top-5 snippets are sufficient for cross-tradition / paradigm-bridge queries; no calibration check on whether top-5 + WEB_CONTEXT-injection is adequate for C2A2's tradition-aware query shape.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-260
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced via inference from broker-v4 design discussion lacking calibration step.
      15a: Searched for supporting literature on RAG adequacy benchmarks and Tavily-top-K practice.
    Current status: PARTIALLY-SUPPORTED (Weak)

  Supporting evidence found: Yes (weak)

  Sources:
    1. Karpukhin et al. (2020) "Dense Passage Retrieval for Open-Domain QA" — top-K with K=5 is a documented baseline in open-domain QA; many production systems use K=3-10 successfully.
    2. Perplexity, You.com, Phind product disclosures (2024-2025) — top 3-8 snippet RAG is the documented production norm for general-purpose research tools.
    3. Tavily case studies — Tavily-marketed customer deployments cite top-5 as the default with documented success across general research queries.
    4. Lewis et al. (2020) "RAG" — original RAG paper used top-5 / top-10 routinely; the K=5 default has empirical backing for general retrieval tasks.

  Strength of support: Weak

  Summary: Top-5 is a defensible baseline in general-purpose RAG and has production track record. However, the presumption is specifically about cross-tradition / paradigm-bridge queries — a more specialized retrieval shape that the cited literature does not directly address. The available support is for general-purpose research-tool retrieval, not for the specific C2A2 query shape.

  Caveats: (a) General-purpose RAG benchmarks do NOT validate paradigm-bridge / cross-tradition retrieval; (b) Tavily is optimized for general web queries, not scholarly cross-domain retrieval (BeIR or domain-specific benchmarks would be more relevant); (c) "no calibration check" is itself the inference — the presumption is about ABSENCE of validation, not refutation; (d) top-5 may be adequate but only luck of the draw without an empirical check.

  Recommendation: PARTIALLY-SUPPORTED (Weak) — top-5 is defensible as a starting point but does not validate the specific cross-tradition use case.
