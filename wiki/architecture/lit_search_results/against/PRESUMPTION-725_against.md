SEARCH-AGAINST-PRESUMPTION-725:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-725
  Original statement: That retracting an escalation retracts only that escalation; the Day-106 test was declared invalid as a test, and no operation exists for withdrawing a criterion — the same shape as 08-06's 88 phantom drift items, never retracted from wherever they landed.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-725
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inferred from the scope of the retraction's wording against the scope of its application
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. "Continued use of retracted papers: Temporal trends in citations and (lack of) awareness of retractions shown in citation contexts in biomedicine" (MIT Press, Quantitative Science Studies) — of 13,252 postretraction citation contexts, only 5.4% acknowledged the retraction; databases do not consistently link retracted articles to their retraction notices.
    2. "Propagation of errors in citation networks..." (Research Integrity and Peer Review, Springer, 2016) — traces the full citation network of one retracted Nature paper and shows the erroneous result propagates through direct citations regardless of the retraction's formal scope.
    3. "Why do some retracted articles continue to get cited?" (Scientometrics, 2024) — confirms retracted results keep circulating years after retraction, largely because retraction is a metadata event at the source, not a propagated operation across everything derived from it.

  Strength of challenge: Strong

  Summary: This is a well-established, decades-deep body of scientometric research: retracting a source item does not retract the downstream artefacts (citations, derived claims, restated results) that depended on it, because retraction is scoped to the item itself and there is no standard mechanism to propagate the withdrawal outward. The literature shows this is not an edge case but the norm — most consumers of a retracted result never learn of the retraction, and the erroneous content persists indefinitely in the ecosystem. This maps closely onto the item's core claim: a narrow, scoped retraction (of a test, an escalation) leaves everything derived from it (phantom drift items, downstream flags) untouched and untraceable.

  Specific risks: If C2A2 declares a test or escalation invalid without an operation to retract everything derived from the criterion it embodied, invalid conclusions (like the 88 phantom drift items) persist indefinitely in whatever stores or summaries consumed them, silently degrading trust in downstream aggregates — precisely mirroring the retracted-citation propagation pattern, which research shows self-corrects only rarely and slowly (over years, if at all).

  Mitigations available: Maintain backward links from every derived artefact to the criterion/test that produced it (so retraction can be structurally propagated, akin to retraction-linking efforts like OpenCitations); require retraction operations to declare their blast radius (which downstream items are affected) rather than only the item itself; periodic sweep audits explicitly for orphaned artefacts tied to retracted criteria.

  STEELMAN:
    Item: PRESUMPTION-725
    Strongest counterargument: Retraction-citation research shows this failure mode is structural, not accidental — it persists across an entire scientific ecosystem with dedicated infrastructure (CrossRef retraction watch, journal policies) and still only reaches ~5% awareness in citation contexts. A system with far less infrastructure for tracking "what depended on this criterion" should expect the propagation gap to be at least as bad, if not worse, since there is no equivalent of a retraction-watch database for C2A2's internal artefacts. The fact that 08-06's 88 phantom drift items were never retracted despite the shape being previously identified is itself evidence that the gap is not self-healing.
    What would need to be true for C2A2 to be safe: Every derived artefact would need an explicit, queryable dependency edge back to the criterion that produced it, and retraction would need to be defined as a graph operation (cascade or flag-for-review) rather than a single-node edit.
    How to test: Pick a retracted criterion and attempt to enumerate everything derived from it using current tooling; if this cannot be done reliably, the presumption is confirmed live.
