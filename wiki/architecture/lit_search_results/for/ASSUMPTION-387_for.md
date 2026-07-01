SEARCH-FOR-ASSUMPTION-387:
  Date searched: 2026-06-29
  Original item: ASSUMPTION-387
  Original statement: "Deterministic path/size heuristics (no model - Rule 5) correctly classify 2,984 orphan+sparse pages into A-E by directory and file size."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-387
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: path + file-size deterministic rules used to bucket pages, no model invoked
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Metadata-based file classification (supervised + rule-based). - Classifying from file metadata (path, size, type) is an established, fast first-pass technique; it is the canonical low-cost layer in production classification systems.
    2. Hybrid classification architectures (metadata-first with confidence threshold, content fallback). - Documented best practice assigns by metadata when confidence is high and falls back to content analysis when it is low, supporting metadata as a legitimate primary signal.

  Strength of support: Weak-Moderate

  Summary: Using path and size as deterministic classification features is a recognized and cheap first-pass approach, consistent with applying it where a model is unnecessary (Rule 5). The literature supports metadata as a usable signal for coarse bucketing (A-E). However, the same sources treat metadata-only classification as a high-throughput approximation that is typically backstopped by a content check, so "correctly classify" is supported only in the coarse/first-pass sense, not as a guarantee of per-page correctness.

  Caveats: Support is for "reasonable coarse triage," not for "correct." Accuracy is precisely the contested point (see 15b and PRESUMPTION-415); misfiled or mis-sized pages will be misclassified by construction.

  Search scope: Metadata vs content classification; hybrid confidence-threshold pipelines. Adequate.

  Recommendation: PARTIALLY-SUPPORTED
