SEARCH-AGAINST-PRESUMPTION-256:
  Date searched: 2026-05-27
  Original item: PRESUMPTION-256
  Original statement: The 1-week-cadence sit-down target and the sit-down-availability bottleneck diagnosis presume future signout/attention-outage events share the 10-second-resolvable failure mode of the 2026-05-22 to 2026-05-26 outage; alternate failure modes may not be 10-second-resolvable.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-256
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced.
      15b: Searched for challenging literature on failure-mode heterogeneity.
    Current status: CHALLENGED (Moderate-Strong — sustains the presumption)

  Sources:
    1. Kahneman & Tversky (1974) availability heuristic — recent events get over-weighted; single-event-attribution is a documented cognitive bias.
    2. SRE post-incident analysis literature — failure modes in human-tooling are typically heterogeneous; one resolution mode rarely generalizes.
    3. OAuth/MFA failure-mode taxonomy — credential failures span minutes to hours to days depending on root cause; 10-sec resolution is the easy-case minority.
    4. Mood / executive-function literature — non-tooling attention dips have their own failure-mode profile, not 10-sec resolvable.
    5. Reason (1990) — generalizing from one incident is the canonical error-analysis anti-pattern.

  Strength of challenge: Moderate-Strong (sustains the presumption)

  Summary: The failure-mode-heterogeneity literature directly supports the presumption. Single-event-attribution from one 10-sec resolution generalizes poorly. The presumption is well-supported as a challenge to ASSUMPTION-235/236's single-failure-mode framing.

  Specific risks: (a) Design optimized for 10-sec resolution may fail on other modes; (b) the next outage may not be 10-sec resolvable, defeating the diagnosis; (c) failure-mode tracking has not been instrumented.

  Mitigations available: (a) Track failure modes; (b) design escalation/SLA/safe-defaults that work across modes; (c) treat 10-sec resolution as one mode among several.

  Recommendation: CHALLENGED (Moderate-Strong; presumption sustained)

  STEELMAN:
    Item: PRESUMPTION-256
    Strongest counterargument (to the presumption): The 10-sec resolution is one data point but it WAS the resolution. Use what worked.
    What would need to be true for C2A2 to be safe (if relying on single-mode): Failure-mode distribution must be stationary AND dominantly 10-sec-resolvable. Neither is established.
    How to test: Instrument failure-mode tracking; revisit after 5 outage events.
