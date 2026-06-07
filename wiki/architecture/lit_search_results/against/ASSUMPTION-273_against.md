SEARCH-AGAINST-ASSUMPTION-273:
  Date searched: 2026-06-06
  Original item: ASSUMPTION-273
  Original statement: Sociogram LOCKED search semantics (highlight lens, never filter; checkboxes filter, search highlights, never sync — 2026-05-29) transfer correctly and should be inherited exactly by the 156-node Community Explorer graph.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-273
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as a stated commitment to inherit the sociogram search lock exactly.
      15b: Searched for cases where filtering beats highlighting and where graph size should change interaction semantics.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Munzner, 2014. "Visualization Analysis and Design" (filter vs highlight idioms). — For targeted retrieval ("find item X"), removing non-matches (filter) reduces visual search cost more than highlighting-in-place, because highlight leaves all distractor marks on screen. Challenges "highlight, never filter" for the lookup task CE states.
    2. Cockburn, Karlson & Bederson, 2008. — Documents that the value of context-preservation depends on the task and on the cost of losing context; at small N the cost of filtering out context is low, undercutting the main reason highlight was chosen at 1647 nodes.
    3. Shneiderman, "Dynamic Queries / filtering" line of HCI work. — Strong empirical tradition that filtering (tight-coupling controls that remove non-matches) is highly effective for finding specific records — the exact "156 unlabeled dots need name lookup" use-case.

  Strength of challenge: Moderate

  Summary: The challenge is not to the highlight idiom in general but to inheriting it "exactly" for CE's stated task. CE's dominant task is targeted name lookup, and the retrieval/dynamic-query literature favors filtering (remove non-matches) for finding specific records, because highlighting leaves all distractors on screen and raises visual-search cost. The sociogram chose highlight-over-filter to preserve global structure under clutter at 1647 nodes; at 156 nodes the context-loss cost of filtering is small, so the original justification largely evaporates. "Inherit exactly" therefore risks importing a constraint tuned for a different scale and task.

  Specific risks: CE users hunting for a named community see the match highlighted but still scan ~155 distractor dots, making lookup slower than a filter that isolates the match; the team locks in a sociogram-scale rationale that does not fit CE, then treats the mismatch as fixed.

  Mitigations available: Treat the lock as a default, not a law: A/B the 156-node lookup task highlight-vs-filter; allow search to optionally filter (or a "isolate match" toggle) at small N while preserving the highlight grammar for structure-reading; decide by measured lookup time, not by inheritance.

  STEELMAN:
    Item: ASSUMPTION-273
    Strongest counterargument: The sociogram's highlight-never-filter lock is a solution to a problem CE does not have. At 1647 nodes, filtering destroys the structure that is the whole point, so highlight is correct there. CE's own stated need is "156 unlabeled dots need name lookup" — a retrieval task for which the HCI record favors filtering. Inheriting the lock "exactly" is cargo-culting a scale-bound constraint: it optimizes context-preservation that 156 nodes barely need while under-serving the lookup task that motivated CE in the first place.
    What would need to be true for C2A2 to be safe: CE's real dominant task is structure-reading (not lookup), OR measured lookup time at 156 nodes is no worse with highlight than with filter.
    How to test: Time a name-lookup task on the 156-node graph under highlight vs filter with representative users; if filter wins materially, relax the lock for CE.

  Recommendation: PARTIALLY-CHALLENGED
