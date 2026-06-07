SEARCH-AGAINST-PRESUMPTION-311:
  Date searched: 2026-06-06
  Original item: PRESUMPTION-311
  Original statement: [inferred] Deferring the join to the P3 promotion pipeline presumes curated communities and directory records are the same kind of object that should eventually share an id space; the alternative — categorically distinct, should never join — was never raised.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-311
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the presumption that two record types are one object that should share an id space.
      15b: Searched for when to keep schemas distinct and the error of conflating association with identity.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Data-modeling fundamentals (entity vs relationship; Chen ER model). — Identity (same entity) and association (related entities) are distinct relations; modeling two associated-but-distinct entity types as one identity is a recognized modeling error. Challenges the "same object, shared id space" presumption.
    2. Ontology / classification literature (Bowker & Star, "Sorting Things Out"). — Forcing categorically distinct kinds into one category to enable a join encodes a substantive ontological commitment that should be argued, not assumed; the un-raised alternative (distinct kinds) is exactly the omission flagged.
    3. Master-data-management caution against over-merging. — MDM practice warns that merging records that are NOT the same entity creates false golden records; unification is appropriate only when identity is established, not presumed. Reinforces that shared id space must be earned.

  Strength of challenge: Moderate-Strong

  Summary: The presumption pre-commits to an ontology — that a curated community and a directory seed are the same object at different maturities — without raising the live alternative that they are categorically distinct (e.g., a measured tradition vs a pointer-to-a-community) that should associate but never merge. Data-modeling and ontology literature treat identity and association as different relations and warn that over-merging distinct kinds produces conceptual errors and false golden records. This couples tightly to PRESUMPTION-306: 306 says the join may be infeasible (empirical), 311 says it may be inappropriate (conceptual) even if feasible. Deferring the join to P3 hides this unexamined ontological choice inside a pipeline step.

  Specific risks: A shared id space welds together two kinds that should stay distinct, propagating category errors through every downstream consumer; if 306 forces a low-overlap fuzzy join, 311 means even the recovered links may be conceptually wrong, not just statistically noisy.

  Mitigations available: Raise the suppressed alternative explicitly — decide whether curated communities and directory records are one object (shared id space) or two (association via a link table, never merged); make this an explicit modeling decision for Tom before P3; prefer association-by-link until identity is positively established (consistent with MDM caution).

  STEELMAN:
    Item: PRESUMPTION-311
    Strongest counterargument: Whether two record sets should share an id space is an ontological question, not a pipeline detail — and answering it by deferral silently answers "yes, same object." But a curated, self-articulated community and a directory seed pointer may simply be different kinds of thing: one is a measured tradition, the other a lead. Lifecycle/MDM models only license shared identity when it is the SAME entity across stages; presuming that here, with the alternative never even raised, conflates association with identity — a known modeling error that, once baked into an id space, is expensive to undo.
    What would need to be true for C2A2 to be safe: The curated community and the directory record genuinely denote the same real-world entity at different maturities (not merely related entities), established positively rather than presumed.
    How to test: Articulate the entity definitions for CC-* and C0001-* and check whether a single real-world referent underlies both; if they can co-exist as distinct referents, model them as associated, not identical.

  Recommendation: CHALLENGED
