SEARCH-AGAINST-PRESUMPTION-083:
  Date searched: 2026-04-28
  Original item: PRESUMPTION-083
  Original statement: "Browser-authentication is user-fixable indefinitely (no escalation tier required)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-083
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Sources:
    1. Reason (1990) "Human Error" — accumulating user-fixable failures is the canonical Swiss-cheese latent-error pattern.
    2. SRE toil literature (Beyer et al. 2016 Ch. 17) — repeated user-action remediation is canonically defined as toil to be engineered away; "indefinitely" is the explicit anti-pattern.
    3. Norman (1988) — "blame the user" as systemic policy is a recognized design failure.
    4. Allspaw (2009) "Web Operations" — user-fix-floor breakdowns are documented when N>2 channels share the floor.
    5. C2A2-internal: PRESUMPTION-068 (Chrome auth) was MONITOR-flagged 2026-04-21 with same concern; PRESUMPTION-061 (mount topology) was REVISE-flagged. The OPEN-039 cluster has been growing.

  Strength of challenge: Strong

  Summary: The literature uniformly treats indefinite user-fixability as an anti-pattern; the SRE recommendation is to engineer toil away. C2A2's prior cycles already flagged the same concern. The presumption — that no escalation tier is needed — is contradicted by both literature and operational record.

  Specific risks: (a) Latent-error accumulation; (b) user-fix floor breakdown as channels accumulate; (c) the OPEN-039 cluster grows without architectural response.

  Mitigations available: (a) Add an escalation tier; (b) DECISION-NNN candidate for sandbox-infrastructure-escalation; (c) circuit-breaker that triggers escalation when user-fix occurrences exceed threshold.

  Recommendation: CHALLENGED (Strong) — PRESUMPTION + strong challenge → REVISE

  STEELMAN:
    Item: PRESUMPTION-083
    Strongest counterargument: Indefinite user-fixability is the canonical "blame the user" anti-pattern. The OPEN-039 cluster has been growing for weeks; the absence of an escalation tier is itself the documented failure mode. ASSUMPTION-078 + PRESUMPTION-083 + PRESUMPTION-061 + PRESUMPTION-068 form a coherent cluster pointing to the need for escalation.
    What would need to be true for C2A2 to be safe: Add an escalation tier with explicit triggers; track user-fix occurrence rate as a metric.
    How to test: Count user-fix occurrences for browser auth over the past 14 days; >3 falsifies the no-escalation-needed framing.
