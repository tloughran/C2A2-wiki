SEARCH-FOR-ASSUMPTION-1692:
  Date searched: 2026-09-29
  Original item: ASSUMPTION-1692
  Original statement: For/against search agents that share a core source on half of items still add retrieval diversity worth their cost.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1692
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from lit pipeline 253a8f8e.
      15a: Searched for supporting literature (scheduled run 2026-09-29; depth: web search + selective fetch; sources marked 'search-result level' were not read in full)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Strength: Moderate

  Sources:
    1. Ross et al., 2026. 'How retriever redundancy and diversity impact RAG effectiveness.' arXiv:2608.13956 (fetched summary 2026-09-29) — diverse documents raised answer correctness 17%–47% across 1B–12B generators; the gain came from diversity of genre, not from repeated support. Supports that a non-overlapping half of retrieval is worth having.
    2. Denisov-Blanch et al. 2026 arXiv:2603.06612 and Begin et al. arXiv:2606.26583 (verified in the 09-28 run, not re-fetched) — cross-model decorrelation exceeds same-model, supporting the value of the non-shared portion.

  Notes: Transfer caveat: RAG-generator setting, not adversarial for/against search agents.
