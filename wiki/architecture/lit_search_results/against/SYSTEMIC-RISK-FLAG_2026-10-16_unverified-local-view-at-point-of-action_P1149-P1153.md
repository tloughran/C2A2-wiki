SYSTEMIC-RISK-FLAG:
  Date: 2026-10-16
  Affected items: PRESUMPTION-1149, PRESUMPTION-1153
  Common vulnerability: Both treat a local, inferred view as authoritative with no check at the point of action. The lock trusts a local directory instead of a fencing token checked at write time; the attribution trusts an inferred link instead of the source text.
  Literature basis: Kleppmann 2016 (secondary only); Merton/McCain on OBI and adumbrationism (title/snippet level).
  Risk level: High
  Recommendation: Verify at the point of action: fence or deduplicate writes for twin jobs; require a source passage and an "inferred" label for back-attributions.
  15c note: the shared vulnerability is abstract (two unrelated domains). Treat as a pattern note, not a single defect. Same family as SYSTEMIC-RISK 2026-10-15 (output without lineage).
  PROVENANCE: Origin: 15b (SYSTEMIC-RISK) | Chain: [14b → 15b] | Items: PRESUMPTION-1149, PRESUMPTION-1153
