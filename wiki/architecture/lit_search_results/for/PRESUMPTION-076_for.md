SEARCH-FOR-PRESUMPTION-076:
  Date searched: 2026-04-27
  Original item: PRESUMPTION-076
  Original statement: "Canonical-works fallback is methodologically equivalent to native wiki tradition entries"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-076
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated structural premise of ASSUMPTION-064
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Retrieval-Augmented Generation (RAG) literature (Lewis et al. 2020; Gao et al. 2023): well-curated raw-text corpora can substitute for structured knowledge bases for many downstream tasks, especially when the texts are canonical and well-known.
    2. LLM-on-canonical-works literature: GPT-class models have substantial training on canonical authors (e.g., Wright, Rohr have major works in training data); fallback to canonical works can leverage embedded knowledge.
    3. Information-extraction literature (Mitchell et al. on Never-Ending Language Learner): canonical-text extraction can approximate curated entries for structured queries.
    4. Pragmatic equivalence in operational settings: many production systems use raw-corpus fallback as a near-equivalent of curated entries when curation cost is high.

  Strength of support: Weak-Moderate

  Summary: For some downstream tasks (especially LLM-driven synthesis on canonical texts), canonical-works fallback approximates native curation moderately well. The literature supports "approximately equivalent" rather than "fully equivalent." For C2A2's specific use case (PRS-triplet decomposition + cross-program signal recognition), the equivalence is weaker because the curation step in native entries does pre-processing that the fallback path does not.

  Caveats: (a) "Methodologically equivalent" is strong; "operationally similar with caveats" is weaker; (b) curation introduces structure (PRS triplets, cross-program seeds) that fallback does not produce; (c) the equivalence depends on the canonical works being well-represented in training data.

  Recommendation: PARTIALLY-SUPPORTED (operational similarity is supported; methodological equivalence is too strong)
