SEARCH-FOR-PRESUMPTION-236:
  Date searched: 2026-05-23
  Original item: PRESUMPTION-236
  Original statement: "Inline-embedding faculty summaries (index.html 1.3 -> 1.9 MB) presumes self-containment outweighs page-weight/scaling cost as the corpus grows."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-236
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the choice to inline 307 faculty summaries into a single file.
      15a: Searched for supporting literature (training-corpus grounding per ASSUMPTION-199 convention; FLAG E noted)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Single-file / self-contained web-app practice (e.g., single-file HTML deliverables). — Self-containment buys portability, offline robustness, no broken external references, and trivial deploy/versioning.
    2. HTTP Archive page-weight data: a ~2 MB document is within current median page weight; at present scale 1.9 MB is not anomalous.
    3. Critical-path simplicity: inlining removes extra round-trips, which can improve load on high-latency links (relevant to the project's off-grid/low-bandwidth contexts).

  Strength of support: Moderate (at current scale)

  Summary: At the current size the inline choice is well-justified: self-containment gives real portability and robustness benefits that matter for this project's distribution contexts, and 1.9 MB is within normal page-weight tolerances. The trade is defensible NOW. Support is partial/conditional because the justification is scale-bound — the same reasoning weakens as the corpus grows (the 15b scaling case), so this is a "true now" support, not an unconditional one.

  Caveats: Support is current-scale only; it does not extend to arbitrary corpus growth (joins PRESUMPTION-229 scaling family).

  Recommendation: PARTIALLY-SUPPORTED
