SEARCH-AGAINST-PRESUMPTION-307:
  Date searched: 2026-06-06
  Original item: PRESUMPTION-307
  Original statement: [inferred] Inheriting the 1647-node sociogram's search LOCK "exactly" into a 156-node graph presumes the lock's rationale survives a ~10x scale drop, though CE's stated need ("156 unlabeled dots need name lookup") differs from the sociogram's.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-307
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the presumption that a scale-motivated lock survives a 10x reduction.
      15b: Searched for scale-dependent UX and small-N graph labeling/lookup needs favoring filter over highlight.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Cockburn, Karlson & Bederson, 2008. — The justification for context-preserving idioms (highlight/focus+context) scales with the cost of losing context, which is high at large N and low at small N; the lock's rationale is therefore scale-bound, directly contradicting "survives the 10x drop unchanged."
    2. Shneiderman dynamic-queries / filtering tradition. — At small, browsable N the effective pattern for "find a named item" is filtering/isolation, not highlight-in-context; the CE stated need favors the idiom the lock forbids.
    3. Munzner, filter vs highlight idioms. — Idiom choice is task- and scale-dependent, not a transferable constant; challenges inheriting any interaction lock "exactly" across a large scale change.

  Strength of challenge: Moderate-Strong

  Summary: The presumption's load-bearing claim — that a scale-motivated rationale survives a 10x scale drop — is contradicted by the very literature that justifies the original lock. Highlight-over-filter earns its keep when losing context is expensive (large, cluttered graphs); at 156 nodes that cost is small, so the rationale does not transfer intact. Worse, CE's stated dominant task (name lookup) is precisely the retrieval case where filtering tends to win. So inheriting "exactly" is transferring a constraint whose justification has lapsed, while possibly under-serving CE's actual task. This is the same underlying issue as ASSUMPTION-273, viewed as the unexamined scale-transfer presumption.

  Specific risks: A reasoned-at-1647 constraint is imported to 156 as if axiomatic; the team optimizes context-preservation CE barely needs and under-serves lookup; the mismatch is invisible because it was inherited, not chosen.

  Mitigations available: Re-derive the idiom from CE's task and scale rather than inheriting it; keep the interaction GRAMMAR consistent (for learnability) while allowing the idiom (highlight vs filter/isolate) to be chosen by task at small N; validate with a lookup-time test.

  STEELMAN:
    Item: PRESUMPTION-307
    Strongest counterargument: "Inherit exactly" treats a context-dependent design decision as a context-free rule. The sociogram lock was the right answer to a specific question (how to search a 1647-node clutter without losing structure). CE asks a different question at a different scale. Reusing the answer without re-asking the question is how scale-bound rationales silently become cargo cult. The fact that one rationale (clutter at 1647) does not even apply at 156 is dispositive: the lock cannot be justified for CE by the reasons it was justified for the sociogram.
    What would need to be true for C2A2 to be safe: CE's dominant task is structure-reading rather than lookup, OR highlight measurably serves the 156-node lookup task as well as filter.
    How to test: Same lookup-time A/B as ASSUMPTION-273; additionally, articulate CE's task profile and check it matches the sociogram's before inheriting.

  Recommendation: CHALLENGED
