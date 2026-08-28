SEARCH-AGAINST-ASSUMPTION-1228:
  Date searched: 2026-08-28
  Original item: ASSUMPTION-1228
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority Medium)
  Original statement: An index at 82% of a hard read limit requires a compaction strategy, and compaction
    carries a real cost — the loss of an accumulated known-traps record.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1228
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim; the underlying measurement was attempted and found out of mount, declared.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Search scope: WebSearch, 2026-08-28, one dedicated query on whether retrieval-augmented memory resolves
    long-context degradation. Reached: Liu et al., "Lost in the Middle: How Language Models Use Long
    Contexts," TACL (MIT Press, doi:10.1162/tacl_a_00638); Databricks' long-context RAG benchmark post;
    arXiv 2511.05850 (retrieval quality at context limit), 2505.00675 (memory in LLM agents survey),
    2606.14047, 2607.16848. NOT COVERED: the cache-replacement literature, which would supply the mature
    counter-argument that lossy eviction with a good policy is routine and safe. All SNIPPET-ONLY.
    Confidence: MODERATE.

  Challenging evidence found: Partial

  Sources:
    1. Liu, N. F. et al., "Lost in the Middle: How Language Models Use Long Contexts," TACL
       [SNIPPET-ONLY] https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00638/119630/ —
       Information in the middle of a long context is systematically under-attended regardless of relevance.
       The challenge this poses to ASSUMPTION-1228 is oblique but real: *not* compacting does not preserve
       the known-traps record in any operational sense, because an index carried at 82% of the limit is
       largely in the under-attended region.
    2. Anon., "Retrieval Quality at Context Limit" (arXiv:2511.05850); Anon., "Rethinking Memory in LLM
       based Agents" (arXiv:2505.00675) [SNIPPET-ONLY; authors unverified] —
       Memory-augmented retrieval returns passages that mention the same terms rather than passages
       describing related states of the same entity; interference grows with context length, and "a
       million-token window may be a poor substitute for curated memory." The remedy space the assumption
       assumes it is choosing within is itself compromised.
    3. Databricks, "Long Context RAG Performance of LLMs" [SNIPPET-ONLY]
       https://www.databricks.com/blog/long-context-rag-performance-llms — Longer retrieved context does not
       monotonically improve task performance.

  Strength of challenge: Moderate

  Summary: The challenge does not deny that compaction loses information — the against corpus concedes that
    as readily as the for corpus asserts it. It denies the framing that the estate faces a choice between a
    preserved record and a compacted one. At 82% of a hard limit the record is already in the regime where
    position determines attention and retrieval degrades, so "do not compact" preserves bytes rather than
    usable memory. There is a second and simpler challenge: the 82% figure is unmeasured. The queue entry
    records that the measurement was attempted and the path was out of mount, so the premise's trigger
    condition is an estimate, and a compaction decision taken on it is taken blind.

  Specific risks: (a) Deferring compaction on the strength of the preservation argument leaves the estate
    with a record that is nominally intact and operationally unread — the worst of both, since it also
    carries the cost. (b) Compacting on an unverified 82% could discard a known-traps record that was never
    near the limit.

  Mitigations available: Measure the index size first — one command, and the blocking issue is a mount path,
    not a research question. Then prefer structured eviction with an explicit retention rule for the
    known-traps entries over summarisation, which is what the structured-eviction line of work exists to
    provide.

  STEELMAN:
    Item: ASSUMPTION-1228
    Strongest counterargument: The known-traps record is not ordinary context; it is the estate's only
      accumulated defence against repeating diagnosed failures, and its loss is not recoverable by
      re-derivation because the traps were found by accident over months. Even a degraded, under-attended
      copy retains the possibility of being read; a summarised copy does not contain the entries at all.
      Asymmetric loss justifies asymmetric caution.
    What would need to be true for C2A2 to be safe: the known-traps entries would need to be extracted into
      a separate, small, always-loaded artifact — at which point the index's total size stops being the
      binding question.
    How to test: extract the known-traps entries, measure their size, and check whether the remaining index
      is anywhere near a limit. If the traps fit in a few kilobytes, this whole item dissolves.

  Recommendation: PARTIALLY-CHALLENGED
