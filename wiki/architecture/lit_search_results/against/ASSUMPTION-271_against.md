SEARCH-AGAINST-ASSUMPTION-271:
  Date searched: 2026-06-05
  Original item: ASSUMPTION-271
  Original statement: The PROCESSED_LOG canonical ingest backlog is 36 files; the divergent 152 from a naïve filename diff is a format artifact (per-file rows mixed with batch narratives), not 116 extra un-ingested files.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-271
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated claim that the 36-vs-152 divergence is a counting artifact, not lost files.
      15b: Searched data-reconciliation literature on row-count mismatch, silent data loss, and the risk of assuming the smaller count is canonical.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. dbseer, "Data Migration Validation Guide: Prove Data Accuracy, Completeness, and Parity," 2026. — Row counts must MATCH between source and target, and any discrepancy must be traced to an EXPLICIT transformation rule (dedup, filtering) rather than assumed to be benign — otherwise it is, by definition, candidate silent data loss. Directly challenges asserting 36 canonical without tracing where the other 116 went.
    2. Monte Carlo, "The Comprehensive Guide to Data Reconciliation." — Treats an unexplained count gap as a defect to be investigated/failed, not narrated away; "the larger naïve count was actually the true denominator" is a documented real-world outcome of migrations that trusted the optimistic read.
    3. Integrate.io, "Data Validation in ETL — 2026 Guide." — Recommends failing or flagging a pipeline when target count falls below source beyond a threshold; the 36-vs-152 gap (~76% shortfall) is far past any reasonable threshold and would normally HALT for investigation, not be pre-judged cosmetic.

  Strength of challenge: Moderate

  Summary: The reconciliation literature does not deny that mixed-format logs over-count under naïve diffs — but it strongly challenges the move of DECLARING 36 canonical before the reconciling fold has actually been run and the 116 explained. The discipline's core rule is the inverse of the assumption's posture: an unexplained count divergence is presumed a possible loss until each missing record is mapped to an explicit transformation rule. A ~76% gap is precisely the magnitude that mature pipelines treat as a hard stop. So the assumption is not refuted in its mechanism, but its epistemic ordering is challenged: it asserts the conclusion (artifact, 36 correct) that the literature says must be earned by the audit.

  Specific risks: If 36 is wrong and the gap conceals genuinely un-ingested files, then every downstream count, backlog-drain plan (ASSUMPTION-272), and "done" signal is built on a denominator that silently omits ~116 items — the classic silent-data-loss failure where the error only surfaces when something later tries to reference a record that was never ingested.

  Mitigations available: Run the actual reconciliation once: classify every one of the 152 naïve hits as (per-file row | batch narrative | genuine un-ingested file) and confirm the residual equals 36. This is cheap, one-time, and converts the assumption from asserted to demonstrated — exactly what 15a's event-sourcing sources also require.

  STEELMAN:
    Item: ASSUMPTION-271
    Strongest counterargument: The whole point of a system-of-record is that the canonical count is PROVEN by folding the log under its record semantics, never asserted from a convenient priors. Calling 152 a "format artifact" before doing that fold inverts the burden of proof: it assumes the benign reading of an unexplained 76% discrepancy, which is the textbook precondition for silent data loss. Until each of the 116 is individually accounted for, "36 is canonical" is a hypothesis wearing the costume of a finding.
    What would need to be true for C2A2 to be safe: The 152 must be fully partitioned with every non-36 entry mapped to a concrete, inspectable artifact-or-narrative reason (no residual "probably just formatting"), and the residual genuine-file count must land exactly at 36.
    How to test: Programmatically diff the PROCESSED_LOG: tag each entry by record type, count genuine file-ingest rows, and reconcile against the filesystem set of source files. If genuine-file rows = 36 and the remainder are provably rows/narratives, the assumption is confirmed; any residual is a real backlog item.

  Recommendation: PARTIALLY-CHALLENGED
