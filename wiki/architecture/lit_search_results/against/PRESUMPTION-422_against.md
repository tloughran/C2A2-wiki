SEARCH-AGAINST-PRESUMPTION-422:
  Date searched: 2026-06-30
  Original item: PRESUMPTION-422
  Original statement: "That a stale axis displayed beside a fresh one (no per-axis as-of marking) is acceptable — viewer presumed to attribute each axis its own freshness; the most expert viewer was in fact misled."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-422
    Item type: PRESUMPTION (unstated)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference
      15b: Searched for challenging literature (first-time, genuine web search 2026-06-30)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Elementary Data / Sifflet — embedding a visible "data last updated" label per source is explicit best practice; "simple last-updated timestamps or color-coded freshness indicators prevent users from making decisions on stale information."
    2. Skopx / dqops — freshness must be communicated at the point of use; uniform dashboard chrome without per-widget as-of marking causes exactly the cross-axis freshness conflation seen here.
    3. Operational evidence: the most expert viewer attributed today's freshness to a 6–12-day-stale axis — direct proof the no-marking design misleads.

  Strength of challenge: Strong

  Summary: Strong challenge: the prescribed control (per-widget as-of timestamps) directly targets this failure, and the failure actually occurred to the most expert user. Displaying mixed-freshness axes without per-axis marking is a known, documented mislead.

  Specific risks: Decisions (including by Tom) are made on stale axes believed current; the more authoritative the display, the more damaging the conflation.

  STEELMAN: A single as-of timestamp for the whole board is cheaper and usually 'good enough' when all feeds share a refresh — but C2A2's feeds are explicitly independent (A-390), so the single-timestamp shortcut is invalid here by the system's own model.

  Recommendation: CHALLENGED (Strong — per-axis as-of marking is the documented control; absence demonstrably misled the expert viewer)
