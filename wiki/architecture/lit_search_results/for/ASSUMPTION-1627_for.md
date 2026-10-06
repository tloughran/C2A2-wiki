SEARCH-FOR-ASSUMPTION-1627:
  Date searched: 2026-09-23
  Original item: ASSUMPTION-1627
  Original statement: Search results that echo a query's idiosyncratic phrasing are disproportionately
    synthetic, adversarial or self-citing.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-1627
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted the candidate the pipeline addressed to 14a/14b.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Golebiewski, M. & boyd, d., 2018/2019. "Data Voids: Where Missing Data Can Easily Be Exploited."
       Data & Society / Microsoft Research. — Strongest analogous support: obscure or unusual query
       terms return few legitimate results, and manipulators deliberately produce content matching
       those exact terms, so results for idiosyncratic phrasings are disproportionately low-quality or
       manipulative.
    2. Zou, W. et al., 2025. "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented
       Generation of Large Language Models." USENIX Security 2025 (arXiv 2402.07867). — Adversarial
       passages are engineered to contain words strongly related to the target query so they rank
       highly in retrieval; five injected texts per question achieved ~90% attack success in a
       multi-million-document corpus. Mechanistic support: query-echo is the property attackers
       optimize for.
    3. Greshake, K. et al., 2023. "Not What You've Signed Up For: Compromising Real-World
       LLM-Integrated Applications with Indirect Prompt Injection." AISec '23 / arXiv 2302.12173. —
       Adversaries place instructions in data likely to be retrieved; supports the "adversarial" branch
       for agentic search pipelines.
    4. Nature news feature, 2026. "Hallucinated citations are polluting the scientific literature. What
       can be done?" (d41586-026-00969-z); and arXiv 2602.05930, "Compound Deception in Elite Peer
       Review: A Failure Mode Taxonomy of 100 Fabricated Citations at NeurIPS 2025." — Fabricated
       citations mimic plausible titles and venues; supports the "synthetic" branch generally, though
       not the phrasing-echo mechanism specifically.

  Strength of support: Moderate

  Summary: Two literatures independently predict the claim. Data-void research shows that
    low-competition, unusual query terms are where manipulated content concentrates, and RAG-poisoning
    research shows that adversarial documents are built precisely to echo target queries lexically and
    semantically. Indirect prompt-injection work establishes that retrieval pipelines are an active
    attack surface. Together these make it theoretically well grounded that query-echoing results carry
    elevated risk. What is missing is a base-rate study measuring the proportion of synthetic or
    adversarial content among echo-matching vs. non-echo-matching web results.

  Caveats: "Disproportionately" is a base-rate claim; no source measured it directly. Echo can also
    arise innocently (a real paper coining the phrase; the query borrowing a real paper's wording), so
    the heuristic will have false positives. "Self-citing" (results reflecting the pipeline's own
    outputs back) was not directly addressed by any source found. PoisonedRAG concerns a
    controlled knowledge base, not open-web search.

  Search scope: Preliminary — three searches (indirect prompt injection; data voids; hallucinated
    citation contamination) plus one on RAG poisoning.

  Excluded results: greshake/llm-security GitHub README (repo mirror; primary paper used). Vendor blogs
    (Enago, Sourcely, INRA.AI, Fluid Attacks) not used — unverifiable statistics, no venue.

  Recommendation: PARTIALLY-SUPPORTED
