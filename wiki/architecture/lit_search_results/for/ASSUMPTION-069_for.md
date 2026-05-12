SEARCH-FOR-ASSUMPTION-069:
  Date searched: 2026-04-27
  Original item: ASSUMPTION-069
  Original statement: "Proposal-ID collisions are flagged-and-rolled-forward rather than blocked-on"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-069
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-04-27 — two same-day independent collision-detection-and-rename instances
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Distributed-systems literature on conflict-free replicated data types (CRDTs; Shapiro et al. 2011) — flag-and-roll-forward (or merge-with-rename) is the canonical pattern for handling identifier collisions in eventually-consistent systems.
    2. Git's branch-collision and merge-conflict handling (Chacon & Straub "Pro Git") — collision is annotated and surfaced; downstream consumers proceed with awareness rather than blocking the workflow.
    3. Database schema-change literature (Refactoring Databases by Ambler & Sadalage 2006) — additive forward migrations with later cleanup is a well-documented pattern for non-blocking evolution.
    4. Continuous-deployment literature (Humble & Farley 2010 "Continuous Delivery"): roll-forward over roll-back is the dominant modern pattern; collisions are detected, flagged, and rolled forward with corrective deploys.
    5. Operational-precedent in C2A2 itself: PREMISE-006 (flag-don't-fabricate) is conceptually parallel; both are flag-and-continue patterns rather than block-and-resolve.

  Strength of support: Strong

  Summary: Flag-and-roll-forward is a canonical pattern for ID-collision handling across CRDTs, version control, schema migrations, and continuous deployment. The literature treats it as preferable to block-and-resolve when the downstream cost of blocking is high and the cost of correction is low. C2A2's current scale (low collision rate, low correction cost) is consistent with the pattern's well-supported regime.

  Caveats: (a) The pattern degrades when collision rate scales — at high rates, accumulated debt becomes blocking anyway; (b) "low correction cost" is an unaudited claim for C2A2 specifically.

  Recommendation: SUPPORTED (the pattern is well-grounded; scaling behavior should be monitored)
