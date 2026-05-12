SEARCH-AGAINST-ASSUMPTION-078:
  Date searched: 2026-04-28
  Original item: ASSUMPTION-078
  Original statement: "Two parallel sandbox-infrastructure failure modes (auth gap, mount topology) are treated as user-fixable"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-078
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-04-27
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Sources:
    1. Reason (1990) "Human Error" — accumulated user-fixable failures generate latent error conditions ("Swiss-cheese model"); the system becomes more fragile, not less, with each user-fix.
    2. Beyer et al. (2016) "Site Reliability Engineering", Ch. 17 (toil) — repeated user-action remediation is canonically defined as "toil"; the SRE recommendation is to engineer toil away, not normalize it.
    3. Norman (1988) "The Design of Everyday Things" — systemic failures classified as user-fixable is the canonical "blame the user" anti-pattern.
    4. Allspaw (2009) "Web Operations" — when N>2 channels share user-fix-floor, the cumulative attention cost grows superlinearly; the user becomes the bottleneck.
    5. C2A2-internal: PRESUMPTION-061 (mount topology) was REVISE-flagged 2026-04-21; PRESUMPTION-068 (Chrome auth) was MONITOR-flagged 2026-04-21. Both have prior escalation flags; ASSUMPTION-078's framing contradicts these.

  Strength of challenge: Strong

  Summary: The literature is consistent: parallel infrastructure failures classified as user-fixable is a documented anti-pattern. The SRE recommendation is to engineer the user-action remediation away; the human-factors literature warns of latent-error accumulation. C2A2's own prior cycles already flagged both failure modes as warranting escalation — ASSUMPTION-078's user-fixable framing contradicts the system's own prior dispositions.

  Specific risks: (a) Latent-error accumulation: each user-fix preserves the underlying fragility; (b) user becomes the bottleneck for both Cowork↔Chat sync and sandbox-mount stability; (c) cumulative attention cost grows superlinearly; (d) inconsistency with prior REVISE/MONITOR flags creates architectural-record incoherence.

  Mitigations available: (a) Reclassify both failure modes as escalation-required; (b) add a circuit-breaker or pre-flight check; (c) audit user-fix occurrences as a metric and trigger escalation when a threshold is crossed.

  Recommendation: CHALLENGED (Strong — both literature and C2A2's own prior dispositions contradict the user-fixable framing for these specific failure modes)

  STEELMAN:
    Item: ASSUMPTION-078
    Strongest counterargument: Two simultaneous sandbox-infrastructure failures classified as user-fixable converts the user into the system's load-bearing maintenance layer. The literature treats this as the canonical "blame the user" anti-pattern; the SRE literature treats it as toil to be engineered away. C2A2's own prior REVISE flag (PRESUMPTION-061) and MONITOR flag (PRESUMPTION-068) already disagree with the user-fixable framing — ASSUMPTION-078 contradicts the system's own record.
    What would need to be true for C2A2 to be safe: Both failure modes are reclassified as escalation-required; pre-flight checks or circuit-breakers are added; user-fix occurrence rate is tracked as a metric.
    How to test: Sum the user-fix interventions for both failure modes in the past 14 days. >3 across both channels would falsify the "user-fixable, no escalation needed" stance.
