SEARCH-FOR-ASSUMPTION-283:
  Date searched: 2026-06-08
  Original item: ASSUMPTION-283
  Original statement: Automating regeneration on a schedule is the right fix for "PRS triplets accumulate but the published connectome never changes."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-283
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-06-07 PRS-connectome session as the stated fix for a stale published derived artifact.
      15a: Searched for support that scheduled regeneration is the correct pattern for keeping a published derived view in sync with an append-only source.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. The Twelve-Factor App, Factor XII "Admin processes" / Factor X "Dev-prod parity" (12factor.net). — Recurring one-off/maintenance processes (e.g., regenerating a derived artifact) are first-class and should run on the same codebase/config as the app; scheduling such regeneration is endorsed practice.
    2. Materialized-view maintenance literature (Postgres REFRESH MATERIALIZED VIEW on pg_cron / scheduled cadence; Databricks materialized-view recompute). — A derived view that "does not reflect the current state of its source" until rebuilt is the canonical staleness problem; the standard remedy is exactly a scheduled (or incremental) refresh on a cadence.
    3. Sculley et al. 2015, "Hidden Technical Debt in Machine Learning Systems" (NeurIPS). — Derived/downstream data products drift from their sources unless their regeneration is made an explicit, owned, repeatable pipeline step; ad-hoc manual regeneration is itself a debt the scheduled pipeline pays down.

  Strength of support: Strong (for the general pattern)

  Summary: The diagnosis (a published derived artifact silently lagging an append-only source) is a textbook staleness problem, and scheduled regeneration of derived/materialized state is the standard, well-validated remedy across web-app methodology, database materialized-view practice, and data-engineering. Making regeneration a scheduled, owned pipeline step (rather than a remembered manual chore) is precisely what the literature recommends.

  Caveats: The support is for scheduling as the RIGHT PATTERN, conditional on two things the literature also stresses: (a) the scheduled execution context must actually be CAPABLE of running and publishing the regeneration (dev/prod parity — see PRESUMPTION-317), and (b) the scheduled job must be monitored for FAILURE, because a silently-failing cron job reproduces the very staleness it was meant to cure. Within those conditions, scheduling is necessary; it is not by itself sufficient.

  Recommendation: SUPPORTED
