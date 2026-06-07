SEARCH-FOR-PRESUMPTION-307:
  Date searched: 2026-06-06
  Original item: PRESUMPTION-307
  Original statement: [inferred] Inheriting the 1647-node sociogram's search LOCK "exactly" into a 156-node graph presumes the lock's rationale survives a ~10x scale drop, though CE's stated need ("156 unlabeled dots need name lookup") differs from the sociogram's.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-307
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated presumption that a scale-motivated interaction lock survives a 10x reduction in node count.
      15a: Searched for interaction patterns that hold across graph scale and for consistency-of-grammar benefits.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Nielsen, usability heuristic "Consistency and standards." — Interaction grammar that is consistent across a product family reduces learning cost and error; supports inheriting the same search semantics so a user moving between sociogram and CE does not re-learn the controls.
    2. Cockburn, Karlson & Bederson, 2008 (ACM Computing Surveys). — The highlight/focus+context idioms are described as general interaction techniques, not size-specific ones; gives some grounding that the technique is not inherently invalid at smaller N.
    3. Heer & Shneiderman, 2012. — Treats highlight as a general cue-based primitive applicable across view sizes; supports that the primitive itself transfers.

  Strength of support: Weak-Moderate

  Summary: There is a legitimate consistency argument FOR inheriting the lock: a shared interaction grammar across the sociogram and CE lowers learning cost, and the highlight idiom is a general technique not intrinsically tied to large N. This supports inheriting the MECHANISM. It does not support inheriting it "exactly" as the optimal choice, because the sociogram's specific rationale for highlight-over-filter was clutter-preservation at 1647 nodes — a motivation that weakens at 156. The FOR case is thus "consistency is a real benefit," which is genuine but lighter than the presumption's "rationale survives unchanged."

  Caveats: Consistency is a benefit only if the inherited choice is at least adequate for the new task. Where CE's dominant task is targeted name lookup (retrieval), the consistency benefit can be outweighed by a task-fit cost (filter may serve lookup better at small N) — see 15b. Support is for keeping the grammar familiar, not for the claim that the original scale-bound rationale still holds.

  Recommendation: PARTIALLY-SUPPORTED
