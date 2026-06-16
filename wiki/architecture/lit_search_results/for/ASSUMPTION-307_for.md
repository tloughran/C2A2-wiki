SEARCH-FOR-ASSUMPTION-307:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-307
  Original statement: Git-history-derived yield is a valid productivity axis for the agent-metabolism instrument (tokens as cost, commits as yield), pending PRS-completion integration.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-307
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted stated assumption from architecture work log (cycle 0, 2026-06-10)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Sources:
    1. Forsgren, N., Storey, M.-A., et al., 2021. "The SPACE of Developer Productivity." ACM Queue. — Activity (commit counts etc.) is a legitimate dimension of productivity measurement, but explicitly only as one of five dimensions, never standalone — matching the item's own "pending integration" framing.
    2. Forsgren, N., Humble, J., Kim, G., 2018. "Accelerate." (DORA research program). — Throughput-style delivery metrics (e.g., deployment frequency) are empirically validated predictors of organizational performance at team level, giving precedent for output-event counts as a meaningful axis.
    3. Graphite engineering guide, "How to measure developer productivity beyond commit counts" (2025/2026). — Practitioner consensus: commit counts are gameable and reward fragmentation, but are acceptable as a visible activity signal when explicitly paired with outcome measures.
  Strength of support: Moderate
  Summary: The literature supports commit-derived measures as one valid axis of a multi-dimensional productivity instrument: SPACE legitimizes activity metrics as a dimension, and DORA shows event-count throughput metrics can be validated against outcomes. Crucially, the assumption as stated already contains the literature's own safeguard — it labels the axis interim, "pending PRS-completion integration," which is precisely the multi-dimensional completion SPACE demands. The cost/yield (tokens/commits) framing is analogous to efficiency ratios in the SPACE Efficiency dimension. What is not supported is treating commit count as a proxy for value or research progress: the same literature documents that commit counts reward splitting work and ignore quality, and DORA's validation is team-level delivery, not knowledge-work yield.
  Caveats: Valid only as interim and only if never used alone or as a target (Goodhart exposure is severe for commit counts); agent-generated commits inflate the AI-attribution problem the SPACE literature flags for 2026. Commit size/quality heterogeneity means tokens-per-commit is noisy without normalization.
  Search scope: 1 WebSearch ("commit count lines of code developer productivity proxy validity SPACE framework critique DORA metrics misuse").
  Recommendation: PARTIALLY-SUPPORTED
