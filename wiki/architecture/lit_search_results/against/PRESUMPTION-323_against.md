SEARCH-AGAINST-PRESUMPTION-323:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-323
  Original statement: The eval/apply ratio is a meaningful, known-directional quality signal (surfaced and rankable without defining "good").

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-323
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference (ratio adopted from OpenStory and treated as rankable quality without directional definition)
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. Goodhart, C., 1975 / Strathern, M., 1997 ("When a measure becomes a target, it ceases to be a good measure"); software syntheses: axify.io, codepulsehq, lawsofsoftwareengineering, 2024-26. — The moment a process ratio is displayed and ranked, it shapes behavior and stops describing it; documented across LOC, PR count, story points, cycle time — all process ratios like eval/apply.
    2. Forsgren, Storey, et al., 2021. "The SPACE of Developer Productivity." ACM Queue 19(1). — Explicit finding: no single process metric is directional for quality; activity metrics must never be used alone or for ranking, because identical values arise from opposite underlying states.
    3. Javacodegeeks synthesis, 2026. "We Have Been Measuring Developer Productivity Wrong for Forty Years..." — Forty-year record of process metrics adopted with assumed directionality and later found non-monotonic or gameable; the replacement metrics (DORA-era) acquired the same pathologies once ranked.
    4. Kerr, S., 1975. "On the Folly of Rewarding A, While Hoping for B." Academy of Management Journal 18(4). — Classic statement that surfacing/rewarding an available measure substitutes it for the intended construct, regardless of disclaimers that "good" was never defined.
  Strength of challenge: Strong
  Summary: Two independent objections converge. First, directionality is genuinely unknown and plausibly non-monotonic: a high eval/apply ratio can mean careful verification (good), thrashing/failed edits (bad), or read-heavy task type (neutral) — the same value from opposite causes, which is exactly the condition under which SPACE says a metric cannot rank. The ratio is also confounded by task type: research-y agents and edit-y agents will separate on it for reasons unrelated to quality. Second, the "without defining good" hedge does not survive display: ranking literature (Kerr; Goodhart syntheses; Espeland & Sauder's reactivity work) shows that any surfaced, ordered metric is read as evaluative by its consumers, so the system acquires an implicit quality claim its authors disclaimed. An inherited third-party metric with no baseline, no validation, and no direction is being promoted to a comparator.
  Specific risks: Agents get informally judged (and possibly later tuned) on a ratio whose high end may mark dysfunction; cross-agent comparisons are confounded by task mix; once visible, the ratio becomes a target for agent-prompt tuning, corrupting it as a signal (Goodhart).
  Mitigations available: Display the ratio per agent over time (self-baseline) rather than cross-agent ranked; annotate with task-type strata; validate direction first (sample high- and low-ratio sessions, human-judge quality); present as "behavioral fingerprint," not orderable axis.
  STEELMAN:
    Strongest counterargument: Surfacing an undefined-direction signal is how baselines get discovered; you cannot learn what eval/apply means for this population without first looking at its distribution. No incentive or reward is attached, the audience is one researcher, and Goodhart effects require optimization pressure that does not yet exist. Exploratory display is epistemically prior to validation.
    What would need to be true for C2A2 to be safe: The ratio stays exploratory (no ranking UI, no thresholds); direction is validated against judged session quality before any evaluative use; agents' prompts are never tuned to the ratio.
    How to test: Stratify 20 sessions by extreme eval/apply values, blind-rate their actual quality, and check whether the ratio predicts the rating at all — and in which direction — per task type.
  Search scope: 1 search — "Goodhart's law developer productivity metrics ranking dysfunction". Plus established literature (Kerr 1975, SPACE 2021).
  Recommendation: CHALLENGED
