SEARCH-AGAINST-ASSUMPTION-402:
  Date searched: 2026-07-02
  Original item: ASSUMPTION-402
  Original statement: "A logged-out claude.ai is a hard stop for an autonomous run; entering credentials on the user's behalf is out of scope for an unattended agent."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-402
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-01 autonomous-run context
      15b: Searched for challenging literature (genuine web search 2026-07-02)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. incident.io / OneUptime / AlertOps heartbeat + dead-man's-switch guides (2026) — the dangerous failure is the SILENT one; a run that hits a blocker and simply ends without emitting an alert lets hours pass before anyone notices. Challenges the "hard stop" (as a terminal, quiet end) rather than the credential clause.
    2. DigitalApplied, "Human-in-the-Loop Escalation Design for AI Agents" (2026) — blockers that require human action should trigger an escalation/handoff carrying context, not just a stop; ~70% of users expect the escalated party to receive prior context, yet most handoffs drop it. A bare hard-stop drops context.
    3. HITL literature (Elementum/Galileo) — agrees the agent must not authenticate; it does NOT endorse silent termination as the response. The endorsed response is "pause AND notify a human for the gated action."

  Strength of challenge: Moderate (aimed only at the "hard stop" framing, not the credential boundary)

  Summary: The credential clause is not challenged — the literature affirms it. What is challenged is the "hard stop" framing: treating a logged-out state as a terminal, self-contained stop (with no alert/escalation) is itself the silent-failure anti-pattern. The correct posture is stop-the-gated-action AND escalate with context, so the human can restore the session promptly.

  Specific risks: If a hard stop is silent, the run's failure is invisible until the next manual check; the human-context loop degrades unnoticed (compounds PRESUMPTION-434). "Out of scope" can be misread as "nothing further is owed," dropping the escalation obligation.

  Mitigations available: Pair the hard stop with an escalation/alert (surface the logged-out blocker to Tom immediately, per the dead-man's-switch/escalation pattern); keep the credential boundary intact.

  STEELMAN:
    Item: ASSUMPTION-402
    Strongest counterargument: The credential boundary is correct and non-negotiable, but "hard stop" wrongly locates the safe behavior in STOPPING rather than in NOT-AUTHENTICATING. The genuinely safe unattended behavior is to refuse the credentialed action AND raise a context-bearing escalation, so a human closes the loop fast. A silent hard stop satisfies the safety constraint while failing the liveness/observability constraint the rest of C2A2 already honors (PREMISE-086/006).
    What would need to be true for C2A2 to be safe: The hard stop must be accompanied by an escalation/alert to Tom; then the assumption is fully safe.
    How to test: Verify the autonomous run emits a visible, actionable notification whenever it terminates on a logged-out/credential blocker (not merely a log line no one reads).

  Recommendation: PARTIALLY-CHALLENGED (Moderate — credential boundary uncontested; "hard stop" should be "stop + escalate")
