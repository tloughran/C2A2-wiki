SEARCH-FOR-PRESUMPTION-418:
  Date searched: 2026-06-29
  Original item: PRESUMPTION-418
  Original statement: "[inferred] That orphan-detection should have a single canonical owner - bootstrap-beside-weekly framed as wasteful 'double-counting' rather than useful redundant cross-check (against the project's own monitor-of-monitor principle)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-418
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: redundant orphan-detection treated as wasteful rather than as defense-in-depth
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Vulnerability/finding deduplication practice (security ops). - Single-ownership and deduplication of findings genuinely speed real-progress tracking, reduce handoffs, and avoid closing multiple tickets for one fix, supporting an efficiency case for one canonical owner.
    2. Backlog/ownership management. - Assigning a single responsible owner reduces confusion and coordination cost, partially supporting the "avoid double-counting" framing.

  Strength of support: Moderate

  Summary: There is a real efficiency case for single-ownership and deduplication: it streamlines tracking and prevents duplicated remediation effort. To that extent the presumption is grounded. However, this support is about TRACKING efficiency, not detection RELIABILITY - and it stands in direct tension with the defense-in-depth / monitor-of-monitor principle the project itself endorses elsewhere (see 15b, which challenges this strongly). Support is partial and narrow.

  Caveats: The efficiency argument does not transfer to detection coverage; deduplicating the DETECTORS (not just the findings) removes an independent cross-check. This contradicts the project's own redundancy/dead-man's-switch family (PREMISE-086).

  Search scope: Deduplication/single-ownership; backlog ownership. Adequate.

  Recommendation: PARTIALLY-SUPPORTED
