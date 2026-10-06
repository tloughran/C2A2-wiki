SEARCH-FOR-ASSUMPTION-1670:
  Date searched: 2026-09-24
  Original item: ASSUMPTION-1670
  Original statement: A per-session token cap applied by the worker, with no priority rule, cuts the
    lowest-cost work rather than the lowest-value work.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-1670
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted the stated assumption about unprioritized budget caps in the worker.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Wang, X., Liu, Z., Feng, S. et al., 2026. "On Time, Within Budget: Constraint-Driven Online
       Resource Allocation for Agentic Workflows." arXiv 2605.06110 (fetched). — Frames completion
       under an explicit budget as an online allocation problem requiring per-subtask estimates of
       value (success probability) and cost; a closed-loop planner is needed because budget
       consumption does not by itself track value. Theoretical support that value-aligned cutting
       requires an explicit allocation rule.
    2. "BAGEN: Are LLM Agents Budget-Aware?" arXiv 2606.00198 (seen in search; fetch returned
       deduplicated/unavailable content, authors unconfirmed). — Reports that budget awareness in
       frontier agents decouples from task performance and fails with optimistic bias and late
       failure recognition. Consistent with a cap binding on whatever work happens to come last rather
       than on the least valuable work.
    3. Payne, J.W., Bettman, J.R. & Johnson, E.J., 1993. The Adaptive Decision Maker. Cambridge UP;
       Simon, H.A., 1955 (bounded rationality/satisficing). — Under resource constraints decision
       makers trade accuracy for effort and fall back on cheap heuristics; cutting follows effort
       rather than value unless value is made explicit. Theoretical grounding by analogy.
    4. BAMAS: "Structuring Budget-Aware Multi-Agent Systems," arXiv 2511.21572 (seen in search,
       authors unconfirmed). — Casts LLM allocation under budget as ILP maximizing performance;
       again shows value-aligned allocation is an explicit optimization, not a default behavior.

  Strength of support: Weak

  Summary: The budget-aware agent literature consistently treats value-aligned allocation under a
    cap as something that must be explicitly designed (ILP, portfolio planning, value-guided search);
    agents left to themselves show poor budget awareness and late recognition of exhaustion.
    Behavioral decision research supplies the mechanism: under constraint, effort (cost) rather than
    value drives what is dropped. No study directly measures which work an unprioritized hard cap
    removes, so the specific claim is inferred, not observed.

  Caveats: The wording "lowest-cost" is ambiguous (cheapest-to-cut vs. cheapest-to-do); the
    literature supports "not value-aligned" more clearly than any specific alternative ordering. With
    FIFO execution, a cap truncates the tail of the queue, which may correlate with neither cost nor
    value. Sources are recent preprints.

  Search scope: Preliminary — three searches (budget-aware LLM agents; value-aware scheduling under
    caps; bounded rationality/effort-accuracy). No direct empirical test found.

  Excluded results: pith.science citation page (aggregator); arXiv 2605.09104 and 2605.17410
    ("Token Economics") surveyed but not used — survey framing only.

  Recommendation: PARTIALLY-SUPPORTED
