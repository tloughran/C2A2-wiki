SEARCH-FOR-PRESUMPTION-350:
  Date searched: 2026-06-16
  Original item: PRESUMPTION-350
  Original statement: "[inferred] Git commit timestamps are faithful clocks for knowledge-production events."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-350
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated timing premise beneath ASSUMPTION-319
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Claes et al., 2018, "Do Programmers Work at Night or During the Weekend?" (arXiv:1802.05084). — Commit timestamps reliably reconstruct working-hour rhythms (lunch-hour dips, weekday/weekend patterns), evidence that for AGGREGATE, DAILY-RESOLUTION purposes timestamps track real work timing well.
    2. MSR validity literature (Palomba & Verdecchia 2025; "Does the Tool Matter?" arXiv:2501.15114). — Treats commit timestamps as usable temporal data for event series, with the documented finding that invalid/outlier timestamps are rare (<1/1000), so the clock is faithful for the large majority of commits.

  Strength of support: Moderate

  Summary: For aggregate, daily-resolution timelines, commit timestamps are a reasonably faithful clock — work-rhythm studies recover real temporal structure from them and invalid timestamps are rare. The support is for the WEAK reading: timestamps are good enough to date knowledge-production events at day granularity in aggregate. It does not extend to the strong reading that the commit instant equals the production instant for any individual artifact.

  Caveats: The same literature is explicit that committer-date vs author-date differ, that history can be rewritten, and that batch/backfill commits decouple commit time from work time. "Faithful clock" holds in aggregate at coarse resolution; it fails for backfilled or batched commits and for committer-vs-author divergence. The supportive reading must be scoped to daily aggregates and paired with a backfill check.

  Search scope: Commit-timestamp reliability studies, MSR temporal-validity threats, committer-vs-author date semantics. Comprehensive.

  Recommendation: PARTIALLY-SUPPORTED
