SEARCH-FOR-ASSUMPTION-401:
  Date searched: 2026-07-01
  Original item: ASSUMPTION-401
  Original statement: "Cross-tradition routing into master/cross_program_index.md can be deferred out of the first commit without harming ingestion."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-401
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-06-30 staged-commit plan
      15a: Searched for supporting literature (genuine web search 2026-07-01)
    Current status: PARTIALLY-SUPPORTED

  Sources:
    1. Staged-rollout / incremental-commit practice (trunk-based development) — deferring a downstream, non-blocking artifact out of an initial commit is standard when the deferred item is not an ingestion dependency; ingestion reading vault+git (not the index) makes the index genuinely downstream.
    2. C2A2-internal: A-399 (git-confirmed) establishes PRS/yield/connectome read vault+git, not the cross_program_index — so ingestion correctness does not depend on the index being present in the first commit.

  Strength of support: Moderate

  Summary: Deferring a purely-downstream index out of the first commit is defensible: if ingestion does not read the index, its absence cannot harm ingestion, and staged commits are normal practice. Support is moderate and conditional on the dependency claim (A-399) holding.

  Caveats: Support holds only while the deferral is tracked and backfilled. The literature on staged rollouts also flags a temporary consistency window (the index lags its sources) and the risk that a deferred step is forgotten — that downside is the 15b concern, not covered here.

  Recommendation: PARTIALLY-SUPPORTED (Moderate — safe if the deferral is tracked and the index is genuinely non-blocking)
