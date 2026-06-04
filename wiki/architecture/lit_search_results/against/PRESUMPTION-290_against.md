SEARCH-AGAINST-PRESUMPTION-290:
  Date searched: 2026-05-31
  Original item: PRESUMPTION-290
  Original statement: [inferred] The cadence-streak framing ("registry-advance-streak N=8") presumes advancing the registry every day is intrinsically good; on a blind-intake day this smuggles a normative pull to emit an item-bearing artifact rather than record an honest degraded/no-op run. No "correct not-to-advance" state exists.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-290
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as an unstated normative/self-referential presumption in the 2026-05-30 EOD batch.
      15b: Searched Goodhart's law, surrogation, and metric-fixation literature.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Goodhart's law (Wikipedia; Strathern formulation) — "when a measure becomes a target, it ceases to be a good measure." The advance-streak is a measure of diligence promoted to a target.
    2. Surrogation literature (Medium/Nisslmüller; practical-devsecops) — a measure gradually replaces the construct it proxies; "proxies treated as truths" force optimizing the proxy even when it damages the goal.
    3. Metric-fixation (Muller, The Tyranny of Metrics, via modelthinkers/lawsofsoftwareengineering) — metrics crowd out professional judgment and generate perverse incentives; "no correct-not-to-advance state" is exactly a surrogated metric with no honest null.

  Strength of challenge: Moderate-Strong

  Summary: The presumption is squarely the Goodhart/surrogation failure: "registry-advanced" is a proxy for faithful self-awareness, and tracking it as a streak converts the proxy into a target, creating a normative pull to emit items rather than record an honest degraded/no-op run. The absence of a "correct not-to-advance" state is the diagnostic signature of surrogation — the metric admits no honest null, so the system is incentivized to produce artifacts even on a blind-intake day when the honest output is "no faithful intake today."

  Specific risks: On exactly the days when intake is degraded (the present condition), the streak pressures the system to manufacture item-bearing output, contaminating the registry with low-provenance items and masking the outage — self-referentially defeating the self-awareness goal (couples PRESUMPTION-287, PRESUMPTION-286/REVISE-079).

  Mitigations available: Define an explicit, first-class "honest no-op / degraded" state that PRESERVES the streak (so cadence reliability and honesty are not in tension); count "honest accounting performed," not "items emitted."

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-290
    Strongest counterargument: Any reliability streak with no honest "zero" state surrogates the proxy for the goal: it rewards emitting an artifact over reporting the truth, and does so most strongly on the degraded days when truth-telling matters most. A diligence metric that cannot register "correctly did not advance today" is not measuring diligence — it is manufacturing it.
    What would need to be true for C2A2 to be safe: The streak counts honest accounting (including legitimate no-op/degraded runs), not item emission, so that recording "blind-intake, no faithful items today" maintains rather than breaks the streak.
    How to test: Check whether a degraded/no-op day can be logged without breaking the streak; if it cannot, the metric is surrogated and should be redefined.
