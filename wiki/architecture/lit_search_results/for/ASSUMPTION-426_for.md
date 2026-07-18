SEARCH-FOR-ASSUMPTION-426:
  Date searched: 2026-07-09
  Original item: ASSUMPTION-426
  Original statement: "A tradition agent can reliably reject hallucinated web-search results by cross-checking against its own knowledge of a thinker's appearance catalog."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-426
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extraction from cohort listing (2026-07-07 EOD)
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Manakul, Liusie & Gales, 2023. "SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models." EMNLP 2023. — Establishes that consistency-checking generated claims against a model's own knowledge (sampled self-knowledge) is an effective hallucination-detection signal, the core mechanism the assumption relies on.
    2. Huo, Arabzadeh & Clarke, 2023. "Retrieving Supporting Evidence for LLMs Generated Answers." arXiv:2306.13781. — Shows LLMs can compare an answer against retrieved evidence to self-detect hallucination; supports the triangulation direction (knowledge vs. retrieved claim) used here.
    3. 2025. "A Comprehensive Survey of Hallucination in Large Language Models: Causes, Detection, and Mitigation." arXiv:2510.06265. — Surveys retrieval-augmented verification, self-consistency, and LLM-as-judge detection pipelines; cross-checking against a trusted knowledge prior is a recognized, empirically studied detection family.
    4. 2025. "HalluDetect: Detecting, Mitigating, and Benchmarking Hallucinations in Conversational Systems." arXiv:2509.11619. — Multi-stage pipelines that check claims against both retrieved documents and prior knowledge achieve substantial but imperfect detection rates.

  Strength of support: Moderate

  Summary: Cross-checking incoming claims against an internal knowledge prior (here, the agent's appearance catalog) is a well-established hallucination-detection technique with real empirical grounding: self-consistency checking, retrieval-augmented verification, and knowledge-grounded adjudication all measurably reduce accepted hallucinations. However, the literature consistently reports nonzero miss and false-rejection rates, and detection quality depends on the completeness and correctness of the prior itself. The mechanism is supported; the word "reliably" is stronger than the literature warrants.

  Caveats: Support weakens when (a) the catalog prior is itself incomplete or stale — a genuine new appearance looks exactly like a hallucination (interacts with PRESUMPTION-457); (b) the hallucinated result is plausible and consistent with the catalog's style; (c) no independent second source is consulted. Reported detection F1/precision in the surveyed pipelines is well below 1.0.

  Search scope confidence: Preliminary-to-comprehensive for the detection-methods literature; no source found that measures catalog-prior filtering error rates in curation pipelines specifically.

  Recommendation: PARTIALLY-SUPPORTED
