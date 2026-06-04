SEARCH-AGAINST-ASSUMPTION-258:
  Date searched: 2026-05-30
  Original item: ASSUMPTION-258
  Original statement: Increment 1.5's deterministic friendly-label typeahead (no LLM) is the correct Pathway-27 substrate and replaces the earlier library-science requirement.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-258
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15b: Searched where deterministic label-match underperforms semantic retrieval.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Redis, 'Semantic vs keyword search' — keyword search 'struggles with synonyms and context' (e.g. 'car repairs' misses 'automotive maintenance'); cross-tradition naming is exactly this synonymy problem.
    2. Top-k String Auto-Completion with Synonyms (arXiv 1611.03751) — plain prefix completion misses synonym-linked completions; synonym-aware indexes are needed, evidence that deterministic-only underperforms.
    3. AmazonQAC (arXiv 2411.04129) — even strong autocomplete reaches only ~half of theoretical recall; deterministic matching alone leaves recall on the table.

  Strength of challenge: Moderate-Strong

  Summary: Deterministic prefix typeahead systematically misses synonymy and cross-tradition naming variants, which is central to a cross-tradition system. The literature shows keyword/prefix matching trades recall for determinism; declaring it the 'correct' substrate that 'replaces' the library-science requirement understates the recall gap.

  Specific risks: Users searching a concept under a different tradition's vocabulary get no hit; perceived as missing data; cross-tradition discovery (a core C2A2 goal) degraded.

  Mitigations available: Add a synonym/alias table (cheap, Top-k-with-synonyms approach) or a fallback semantic layer for misses.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-258
    Strongest counterargument: In a cross-tradition system, vocabulary mismatch is the *normal* case, so a substrate that only matches exact/prefix labels structurally cannot serve cross-tradition discovery, the very thing Pathway 27 is for.
    What would need to be true for C2A2 to be safe: A synonym/alias layer covers the cross-tradition naming variants, or misses are rare in practice.
    How to test: Sample real cross-tradition queries; measure deterministic typeahead recall vs an alias-augmented version.
