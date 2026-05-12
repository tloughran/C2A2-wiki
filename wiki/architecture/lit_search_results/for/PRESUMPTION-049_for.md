SEARCH-FOR-PRESUMPTION-049:
  Date searched: 2026-04-20
  Original item: PRESUMPTION-049
  Original statement: "Wiki daily run and Levin+Friston specialist run are scope-partitioned without coordination contract"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-049
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from observed parallel-pipeline state without cross-task coordination contract
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Unix / sharding literature (Raymond 2003; Kleppmann 2017): scope-partition-by-convention is a valid coordination primitive when the partition is *disjoint* and *stable*. No explicit contract is needed when the partition guarantees non-overlap.
    2. Idempotency-based coordination (Helland 2012 "Idempotence is not a medical condition"): parallel tasks that produce idempotent outputs on disjoint scopes do not need a central coordinator — convergence is a natural consequence of the partition.
    3. Eventual-consistency literature (Vogels 2009 ACM Queue "Eventually Consistent"): overlap-tolerant parallel pipelines converge without contract if output writes are idempotent and conflict-free.
    4. CRON / scheduled-task practice (Anglin 2020 sysadmin literature): simple scope-partition by schedule+tag is a common and defensible pattern for independent scheduled tasks.

  Strength of support: Weak-Moderate

  Summary: Scope-partition without explicit coordination contract is a valid pattern *only when* the partition is disjoint, stable, and the writes are idempotent. The literature supports the *pattern* but not *unchecked use of the pattern* — it requires verification that the partition actually holds. In the specific case flagged, the partition is implicit (by thinker-slot schedule) rather than explicit, so the partition's disjointness is not verified and could drift.

  Caveats: (a) The partition is conventional (by schedule), not enforced (no write-exclusion at the filesystem layer); (b) the presence of a duplicate-Levin-production signal in the review queue is direct empirical evidence that the partition has already drifted — so the "scope-partitioned" claim is empirically falsified on that thinker; (c) the literature's support is conditional on the partition actually holding, which is the specific thing that fails here.

  Recommendation: PARTIALLY-SUPPORTED (pattern is valid; specific instance shows observed partition drift — weak empirical evidence against the "without coordination contract" clause)
