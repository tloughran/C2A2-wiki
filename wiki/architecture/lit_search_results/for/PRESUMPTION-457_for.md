SEARCH-FOR-PRESUMPTION-457:
  Date searched: 2026-07-09
  Original item: PRESUMPTION-457
  Original statement: "Model training priors are a valid oracle over live search results when they conflict about post-cutoff events (burden of proof on the new event)."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-457
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inference from cohort listing (2026-07-07 EOD)
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Xie et al., 2024. "Adaptive Chameleon or Stubborn Sloth: Unraveling the Behavior of Large Language Models in Knowledge Conflicts." ICLR 2024. — Empirically documents that models weigh parametric priors against external evidence and resist evidence when priors are strong; frames prior-resistance as partially rational given unreliable retrieval.
    2. Pan et al., 2023. "On the Risk of Misinformation Pollution with Large Language Models." Findings of EMNLP 2023. — Shows retrieved web evidence can be polluted with generated misinformation, materially degrading QA systems that trust retrieval; supports placing a burden of proof on retrieved claims rather than accepting them by default.
    3. 2025. "Accommodate Knowledge Conflicts in Retrieval-augmented LLMs: Towards Reliable Response Generation in the Wild." arXiv:2504.12982. — Argues retrieved context in the wild is frequently wrong (misinformation, unreliable sources, publisher bias) and that robust systems must weigh internal memory against it rather than defer to retrieval.
    4. ICR framework, 2025. "A framework for resolving knowledge conflicts in retrieval-augmented generation." Neurocomputing. — Taxonomizes conflict scenarios and treats prior-vs-evidence arbitration as a calibration problem, not a fixed retrieval-wins rule.

  Strength of support: Moderate

  Summary: The knowledge-conflict literature partially supports the presumption: retrieved live evidence is demonstrably unreliable (hallucinated results, misinformation pollution, SEO spam), so a default of skepticism toward a surprising new claim — burden of proof on the new event — is a defensible calibration stance with empirical grounding. Several works additionally find that prior-resistance correlates with prior strength in ways that are often accuracy-improving. However, no source endorses priors as an *oracle*: the same literature is explicit that for genuinely post-cutoff events the parametric prior is systematically wrong by construction, and the correct policy is confidence-weighted arbitration plus independent corroboration, not prior-wins.

  Caveats: Support collapses in exactly the post-cutoff regime the presumption targets: a true new event (e.g., a thinker's new appearance) is indistinguishable from hallucination under a prior-wins rule, guaranteeing false rejection of all genuine novelty. Literature supports burden-of-proof-with-corroboration (a second independent source discharges the burden); it does not support prior-as-final-arbiter. Interacts with ASSUMPTION-426.

  Search scope confidence: Comprehensive for the RAG knowledge-conflict literature.

  Recommendation: PARTIALLY-SUPPORTED
