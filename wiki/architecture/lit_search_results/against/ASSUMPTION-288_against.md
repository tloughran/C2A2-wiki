SEARCH-AGAINST-ASSUMPTION-288:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-288
  Original statement: Routing extraction through OpenStory's DB (vs direct transcripts) is worth the heavier dependency because eval/apply + turns are valuable signal.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-288
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated design assumption from 2026-06-08 OpenStory→Agent-Explorer build sessions
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. Cox, R., 2019. "Surviving Software Dependencies." Communications of the ACM 62(9). — Dependency cost = sum over bad outcomes of cost x probability; a dependency taken for a small convenience (left-pad: 11 lines) can transmit ecosystem-scale failure. The derived-metric convenience must be priced against the full failure surface of the dependency.
    2. Helland, P., 2005. "Data on the Outside versus Data on the Inside." CIDR. — Another application's internal database is not a contract; integrating against it couples you to private representations that change without notice (the classic "shared database integration" antipathy, also Fowler/Sadalage).
    3. Winters, Manshreck, Wright, 2020. "Software Engineering at Google." O'Reilly (Hyrum's Law). — With enough use, all observable behaviors of a system get depended on; depending on OpenStory's schema means inheriting its unstated invariants and every upstream migration.
    4. InfoQ, 2022. "Pitfalls and Patterns in Microservice Dependency Management." — Transitive/derived-data dependencies are systematically underpriced at adoption time; failures show up as availability and evolution constraints later.
  Strength of challenge: Moderate
  Summary: The literature does not dispute that eval/apply and turn counts may be useful; it disputes the pricing. Dependency-cost analyses (Cox) and shared-database integration critiques (Helland) say the relevant comparison is not "richer signal vs poorer signal" but "richer signal vs poorer signal plus a permanent coupling to a third party's private schema." OpenStory's DB is an internal representation, not a published API: every upstream schema migration, semantic change to eval/apply counting, or capture bug becomes a silent corruption of C2A2's agent metrics. Direct transcripts are the system of record; the DB is a derived view of unknown stability.
  Specific risks: Upstream schema change silently breaks or skews extraction; eval/apply semantics drift between OpenStory versions, making longitudinal agent comparisons invalid; pipeline availability becomes bounded by OpenStory's capture coverage (already known to have a gap).
  Mitigations available: Treat the DB as a cache, transcripts as ground truth; pin OpenStory version and add a schema-fingerprint check that fails loudly; periodically reconcile DB-derived counts against direct-transcript counts (as was done once for ASSUMPTION-289).
  STEELMAN:
    Strongest counterargument: The join key was already verified exactly against independent SQL (ASSUMPTION-289, 572 sessions reconciled), so this is not blind coupling — it is audited reuse. Rebuilding eval/apply extraction from raw transcripts is real engineering cost for a one-person project, and OpenStory is locally controlled (not a remote SaaS), so "upstream changes" arrive only when deliberately pulled.
    What would need to be true for C2A2 to be safe: OpenStory upgrades are infrequent and accompanied by re-running the reconciliation check; transcripts remain retained independently so the DB path is reversible.
    How to test: Run the existing eval/apply reconciliation script after the next OpenStory upstream pull; if it still matches exactly, the coupling is being actively managed rather than assumed.
  Search scope: 1 search — "cost of software dependencies coupling risk left-pad lessons". Plus established literature (Cox 2019, Helland 2005, Hyrum's Law).
  Recommendation: PARTIALLY-CHALLENGED
