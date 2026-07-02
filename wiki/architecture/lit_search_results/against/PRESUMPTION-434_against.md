SEARCH-AGAINST-PRESUMPTION-434:
  Date searched: 2026-07-02
  Original item: PRESUMPTION-434
  Original statement: "[inferred] That a 2nd-day logged-out claude.ai is transient/self-healing, not a single point of failure in the human-context loop with no fallback or escalation."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-434
    Item type: PRESUMPTION (unstated)
    Transform at each step:
      14b: Surfaced as unstated presumption from a 2nd consecutive logged-out day
      15b: Searched for challenging literature (genuine web search 2026-07-02)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. TechTarget / Wikipedia, "Single point of failure" — a SPOF is a component whose failure stops the whole system with no redundant/backup path. A logged-in claude.ai session with no fallback and no escalation is definitionally a SPOF for the human-context loop.
    2. incident.io / OneUptime / AlertOps heartbeat + dead-man's-switch (2026) — silent degradations must be surfaced by watching for the ABSENCE of expected signal; recurrence across days is the signature of a structural fault, not a self-healing blip.
    3. DigitalApplied HITL escalation design (2026) — dependencies on human action require an escalation path; without one, "self-healing" is wishful and the loop simply stays broken until someone happens to look.

  Strength of challenge: Strong

  Summary: A recurring (2nd-day) logged-out state with no fallback or escalation is a textbook single point of failure, not a transient self-healing condition. The reliability and observability literatures both read recurrence-without-redundancy as structural, and prescribe escalation/heartbeat rather than passive waiting. The "transient/self-healing" reading is strongly challenged.

  Specific risks: The human-context loop silently stays degraded across multiple runs; autonomous work proceeds on stale context or stalls, and no one is alerted. The single dependency (one session) can take down the whole context loop.

  Mitigations available: Add escalation/alerting when the session is logged out (surface to Tom, per ASSUMPTION-402 steelman); provide a fallback/degraded-mode path; track recurrence as a reliability metric rather than dismissing it.

  STEELMAN:
    Item: PRESUMPTION-434
    Strongest counterargument: Session expiry is genuinely outside C2A2's control (it cannot log itself in — correctly, per ASSUMPTION-402), so in one sense it IS transient from the system's side: a human re-login fixes it. But "a human can fix it" is not "it self-heals"; with no escalation the human is never prompted, so the fix does not occur on its own. The transient framing is only true if paired with an escalation that actually summons the human.
    What would need to be true for C2A2 to be safe: An escalation fires on logout AND a fallback/degraded mode exists so a single expired session does not halt the whole loop.
    How to test: Force a logout and confirm an alert reaches Tom and that non-claude.ai-dependent work continues.

  Recommendation: CHALLENGED (Strong — recurrence + no fallback/escalation = single point of failure, not self-healing)
