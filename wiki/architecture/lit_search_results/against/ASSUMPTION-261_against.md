SEARCH-AGAINST-ASSUMPTION-261:
  Date searched: 2026-05-30
  Original item: ASSUMPTION-261
  Original statement: The session-handoff rail (gitignored handoff doc + CLAUDE.md 'read handoff first on resume' rule) fixes next-session resume because CLAUDE.md auto-loads and steers the resume.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-261
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15b: Searched stale-doc mis-steer and unreliable instruction-following.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. mem0.ai (2026) — 'if an agent violates a constraint it followed 10 turns ago, the attention weight has dropped below the enforcement threshold'; auto-loaded rules are not reliably honored.
    2. Long-context degradation studies — 11 of 13 LLMs drop below 50% of baseline at 32K tokens even when the needed content is present; a loaded handoff can be present yet ignored.
    3. XTrace handoff article — stale or partial handoff docs actively mis-steer; 'rule will be followed' is unverified without a check.

  Strength of challenge: Moderate-Strong

  Summary: Auto-loading a rule does not guarantee adherence: instruction-following degrades with context length and a stale handoff doc can mis-steer. The word 'fixes' overstates a mechanism that is probabilistic and has no defined failure mode or verification (couples PRESUMPTION-282).

  Specific risks: Resume silently proceeds on a stale/ignored handoff; no detection that the rule was skipped.

  Mitigations available: Add a verification step (handoff freshness check; explicit acknowledgement) and a fail-loud if the rail is skipped.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-261
    Strongest counterargument: 'CLAUDE.md auto-loads' guarantees presence, not adherence; the literature shows presence != following, so 'fixes' is unwarranted without a check.
    What would need to be true for C2A2 to be safe: A freshness check + explicit resume-acknowledgement make rule-skip detectable.
    How to test: Run resumes with a deliberately stale handoff; measure how often the rule is followed and whether staleness is detected.
