SEARCH-AGAINST-ASSUMPTION-1315 (RE-TRIGGER cycle 1, LIMB A only):
  Date searched: 2026-10-06
  Original item: ASSUMPTION-1315
  Original statement (limb A, per MONITOR-602): "an absence claim is invalidated by any later ingest into
    its scope" — as applied: the 22:00 ingest "re-opens 147 absence-declinations across 74 syntheses as
    unverified."

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for* file,
    `lit_search_returns.md`, or today's 15a output.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b → 15c → 15d → 15b (re-trigger cycle 1)]
    Original item: ASSUMPTION-1315
    Item type: ASSUMPTION (stated — from a sibling project, Summa)
    Transform at each step:
      14a: Extracted verbatim; cross-project (PRESUMPTION-945 scope question).
      15b (2026-09-11): Sampling limb refuted by exact bound; invalidation limb "correct in principle,
        unscoped in practice"; TMS literature named as NOT SEARCHED.
      15c: DISPOSITION-937; limb A held as MONITOR-602.
      15d (2026-09-20): Re-triggered; owed = TMS literature search.
      15b (re-trigger cycle 1): Searched TMS (Doyle; de Kleer) and local-closed-world reasoning (Etzioni et
        al.; PSIPLAN). Fetched one full paper. The formal literature supports invalidation only at
        DEPENDENCY grain and represents new entries as EXCEPTIONS, not as re-opening the claim.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes (boundary conditions; the principle itself is not contradicted)

  Sources:
    1. Babaian, T. & Schmolze, J.G. "Efficient Open World Reasoning for Planning." arXiv cs/0601032
       (Logical Methods in Computer Science, 2006). [fetched — introduction and §1.1 read; remainder not read]
       Worked case: the agent knows "no containers have fragile goods except B"; after a new container C of
       unknown contents is added, the correct updated state is "no containers with fragile goods except for B
       AND POSSIBLY C." The absence claim is not invalidated; it acquires a scoped EXCEPTION for the new
       object, and remains usable for every other object. PSIPLAN entailment and update are sound, complete
       and polynomial. The paper also states LCW reasoning is incomplete and cannot represent exceptions.
    2. Etzioni, O., Golden, K. & Weld, D. 1997. "Sound and efficient closed-world reasoning for planning."
       Artificial Intelligence 89. [search-result + described in source 1; primary NOT retrieved] LCW
       statements declare completeness over a formula ("window of expertise"), not over a whole scope.
       [background-knowledge, not verified: LCW update rules conservatively retract an LCW statement when an
       action may add unknown instances — the coarse rule, which PSIPLAN was designed to improve on.]
    3. Doyle, J. 1979. "A truth maintenance system." Artificial Intelligence 12:231–272. [background-knowledge;
       not retrieved] Non-monotonic justifications carry an OUT-list; a belief resting on "X is OUT" is
       retracted when X comes IN — invalidation is propagated along recorded justifications only.
    4. de Kleer, J. 1986. "An assumption-based TMS." Artificial Intelligence 28:127–162 (dekleer.org PDF;
       "Extending the ATMS", same year) [search-result] The basic ATMS is MONOTONIC; non-monotonic
       justifications (needed to express absence) required a separate extension.

  Strength of challenge: Moderate

  Summary: The formal home of limb A does contain "retract conclusions when their justifications change",
    but it never licenses "any ingest into the scope invalidates the absence claim." In Doyle's JTMS a
    belief is retracted only when a node on ITS OWN out-list comes in; in the open-world planning literature
    a new object turns "none" into "none except possibly the new one" — the claim survives with a precisely
    bounded exception rather than reverting to unverified. The coarse rule (retract the whole local
    closed-world statement) is documented as the incomplete fallback that later work was designed to replace.
    Applied to the run: the ingest should have converted each of the 147 declinations into "holds except
    possibly for entries E1..En in the ten registers / CROSS-132..135", re-opening only those whose scope
    formula actually matches an ingested entry. The absence-of-ATMS-non-monotonicity point is a further
    boundary: absence claims are exactly the case the base ATMS does not handle.

  Specific risks: Global re-opening converts a bounded delta into a 147-item hand-check backlog every large
    night (MONITOR-602 (ii), PREMISE-095's unstable regime); it also discards true information ("holds for
    all pre-existing entries") that the exception form keeps.

  Mitigations available: Record each absence claim as a scoped formula with a justification set (or
    timestamp-of-completeness); on ingest, attach "except possibly {new entries matching formula}" and
    re-verify only those entries — MONITOR-602 (a).

  Recommendation: PARTIALLY-CHALLENGED — principle supported in kind, rule challenged in grain. Limb A now
    has citations; primary Doyle and Etzioni texts not fetched (budget).

STEELMAN:
  Item: ASSUMPTION-1315 (limb A)
  Strongest counterargument: The literature that invented "retract when justifications change" spent the
    following decade making retraction FINER, not coarser: dependency-directed in Doyle, exception-carrying
    in open-world planning. "Any ingest into scope invalidates" is the conservative fallback those systems
    were built to avoid, because it throws away knowledge that is still true and makes the work queue scale
    with ingest size rather than with relevance. The correct state after the ingest was not "147 unverified"
    but "147 hold except possibly for the new entries" — a statement that was both sound and cheap.
  What would need to be true for C2A2 to be safe: absence claims are stored with machine-checkable scope
    formulas so the exception set can be computed; otherwise the coarse rule is the only sound option and
    its cost must be accepted.
  How to test: For the 2026-09-10 ingest, compute how many of the 147 declinations have a scope formula
    matched by any ingested entry (MONITOR-602 (a)); the ratio is the overshoot of the coarse rule.
