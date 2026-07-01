SEARCH-AGAINST-ASSUMPTION-387:
  Date searched: 2026-06-29
  Original item: ASSUMPTION-387
  Original statement: "Deterministic path/size heuristics (no model - Rule 5) correctly classify 2,984 orphan+sparse pages into A-E by directory and file size."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-387
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: path + size deterministic rules used to bucket pages
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Metadata-only classification accuracy limits. - Production guidance treats metadata classification as a high-throughput APPROXIMATION that must fall back to content analysis below a confidence threshold; metadata alone is explicitly not treated as correct.
    2. Folder-taxonomy decay. - Folder structures "rarely work for long in a growing environment"; misfiled and mis-sized content accumulate, so directory location is an unreliable ground truth in an evolving vault.
    3. Mislabeling risk at scale. - Metadata-driven classification "risks mislabeling when metadata is incomplete or incorrect," and file size is a particularly weak proxy for content type/value (a short stub and a short index page differ in kind, not size).

  Strength of challenge: Moderate-Strong

  Summary: "Correctly classify" overstates what deterministic path/size rules can deliver. The literature consistently positions metadata-only classification as an approximate first pass that needs a content-based backstop, and warns that folder taxonomies decay and produce misfiled content in growing repositories. File size is an especially weak signal for content type or synthesis value. Without a content check or a sampled accuracy audit, the per-page correctness claim is unsupported and likely has a non-trivial error rate.

  Specific risks: Misclassified pages routed to the wrong A-E bucket drive wrong downstream actions (e.g., a high-value sparse page bucketed as disposable); errors compound across 2,984 pages.

  Mitigations available: Sample-audit classifications against content (e.g., 50-100 pages) to estimate error rate; add a content-based confidence fallback for ambiguous cases; treat the A-E labels as provisional.

  STEELMAN:
    Item: ASSUMPTION-387
    Strongest counterargument: Metadata classification is universally documented as an approximation requiring a content fallback, and file size barely encodes content type - so "deterministic path/size rules CORRECTLY classify ~3,000 pages" claims an accuracy that the technique is not known to deliver, with errors silently driving downstream triage actions.
    What would need to be true for C2A2 to be safe: A sampled audit shows the path/size error rate is low enough for the downstream use, OR ambiguous pages get a content check.
    How to test: Draw a random sample of the 2,984 pages, hand-classify by content, and compare against the heuristic labels to estimate accuracy.

  Search scope: Metadata vs content classification accuracy; taxonomy decay; misfiling. Adequate.

  Recommendation: CHALLENGED
