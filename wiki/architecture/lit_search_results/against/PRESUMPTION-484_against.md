SEARCH-AGAINST-PRESUMPTION-484:
  Date searched: 2026-07-16
  Original item: PRESUMPTION-484
  Original statement: [inferred] A flag/watch is presumed to reflect current evidence; FINDING-048 (FLAG-016) is carried forward as a live watch with no staleness marker while the deposits feeding it are un-ingested - the design presumes flags self-refresh, coupling nothing to upstream evidence freshness.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-484
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Extracted/inferred to intake queue (for_lit_search.md)
      15b: Searched for challenging literature; result CHALLENGED (strength Strong)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Stale-while-revalidate / cache-coherence literature (RFC 5861; SWR + monitoring blind-spot discussions): derived state served without a staleness marker while its source is frozen is a coherence violation; consumers cannot tell live from stale.
    2. Data-freshness SLA literature (Tacnode 2026; DQOps): live decisions require monitored freshness with an explicit max-delay threshold; a watch with no such gate silently outlives its evidence window.

  Strength of challenge: Strong

  Summary: Strongly challenged. Nothing in cache-coherence or alert-staleness practice permits a live watch to be presumed current while its upstream evidence is frozen. FINDING-048 carried with no staleness marker is indistinguishable, to a downstream reader, from a watch on fresh evidence - a coherence violation on the paradigm-shift channel, C2A2's most consequential evidence stream. Because designers were unaware of this coupling (PRESUMPTION), it warrants extra scrutiny.

  Specific risks: A stalled watch reads as live; FINDING-048 could be confirmed or killed on evidence that stopped arriving 07-10.

  Mitigations available: Attach an evidence-freshness gate to every flag/watch; block confirm/kill transitions when upstream ingestion is stale; surface a staleness marker to downstream readers.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-484
    Strongest counterargument: A flag that self-refreshes in presumption but not in fact is worse than no flag: it actively asserts a live epistemic state that no longer has evidence behind it. On the paradigm-shift channel this means C2A2 could announce or retract a paradigm-relevant finding on the strength of data that has been frozen for a week, with every downstream reader treating it as current.
    What would need to be true for C2A2 to be safe: FINDING-048's confirm/kill condition would have to be computable from already-ingested data (independent of the 07-10->07-14 deposits) for the watch to be legitimately live.
    How to test: Show whether FINDING-048's condition is evaluable given the frozen ingestion; if not, mark the watch stale.
