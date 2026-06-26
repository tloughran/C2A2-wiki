SEARCH-AGAINST-PRESUMPTION-400:
  Date searched: 2026-06-26
  Original item: PRESUMPTION-400
  Original statement: "That 'looking alive' (visible feedback every click, pulsing button) is a worthwhile goal - presumes perceived liveness ~= actual freshness"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-400
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: perceived liveness presumed a worthwhile proxy for actual freshness
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Dark-patterns / deceptive-design literature (Gray et al. 2018; UXP2 dark-patterns taxonomy). - Feedback engineered to make users FEEL progress/freshness that is not real is a recognized deceptive pattern; "looking alive" without being fresh manipulates perception.
    2. Placebo / fake-progress-bar research (perceived-performance studies). - Motion cues can make users believe more has happened than has; designers are warned the indicator must reflect TRUE progress.
    3. C2A2 honesty-layer commitments (and ASSUMPTION-367's honesty refinement). - A pulsing "alive" cue decoupled from real refresh contradicts the project's own honesty stance.

  Strength of challenge: Moderate

  Summary: The presumption's danger is the equation perceived-liveness ~= actual-freshness. Responsiveness feedback (input was received) is fine (15a), but a cue that makes the tool "look alive" while the underlying data is stale is exactly the placebo/dark-pattern the deceptive-design literature warns against - and it directly contradicts C2A2's honesty layer. "Looking alive" is worthwhile ONLY if the liveness cue is tied to real state; decoupled, it manufactures false confidence in freshness.

  Specific risks: Users (and demo audiences) trust stale data because the UI looks active; honesty-layer violation; erosion of trust when the gap is discovered.

  Mitigations available: Bind any liveness cue to real refresh state (last-updated timestamp; cue only on actual fetch/change); reserve motion for input-acknowledgement, not freshness implication; show explicit staleness.

  STEELMAN:
    Item: PRESUMPTION-400
    Strongest counterargument: A pulsing button that fires regardless of whether data refreshed is a freshness placebo - it optimizes perception over truth, which is precisely the dark pattern the field condemns and the honesty layer forbids.
    What would need to be true for C2A2 to be safe: Liveness cues are functions of actual fetch/refresh events and true data age, not decorative motion.
    How to test: Withhold real updates while triggering clicks; if the UI still signals "alive/fresh," the cue is decoupled from truth - presumption falsified.

  Search scope: Deceptive design; perceived performance; honesty. Comprehensive.

  Recommendation: CHALLENGED
