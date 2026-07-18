SEARCH-FOR-PRESUMPTION-486:
  Date searched: 2026-07-17
  Original item: PRESUMPTION-486
  Original statement: [inferred] Re-syncing the narrative status line is presumed to discharge staleness, but narrative-freshness and evidence-freshness are decoupled; the pointer reads current while FINDING-048's feeding deposits stay un-ingested — the fix touched the indicator, not the referent.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-486
    Item type: PRESUMPTION (unstated -- surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption (indicator update presumed to discharge referent staleness)
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Sifflet, 2025. "What Is Data Freshness in Data Observability?" — Distinguishes process-success from outcome-freshness; updating the orchestration signal does not make the data current.
    2. Goodhart / Campbell's Law (secondary summaries, 2025-2026). — When an indicator is optimized/refreshed as a substitute for the referent, the two diverge; "green dashboard over stale data" is the canonical anti-pattern.
    3. IBM, 2025. "What Is Stale Data?" — Refreshed surface signals mask cumulative, silent staleness beneath.

  Strength of support: Strong

  Summary: The presumption names a recognized anti-pattern: refreshing an indicator (narrative status line) is not equivalent to refreshing the referent (ingested evidence), and treating the former as discharging the latter is exactly the substitution Goodhart/Campbell warn against. The observability literature independently confirms indicator/referent decoupling as a real, common, and dangerous condition.

  Caveats: Literature also offers the fix (couple the indicator to a computed freshness gate / last-deposit mtime), so the presumption identifies a fixable design gap rather than an inevitability.

  Recommendation: SUPPORTED
