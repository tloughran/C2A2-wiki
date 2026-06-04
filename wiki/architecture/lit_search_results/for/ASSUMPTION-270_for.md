SEARCH-FOR-ASSUMPTION-270:
  Date searched: 2026-06-04
  Original item: ASSUMPTION-270
  Original statement: An autonomous browser/sync agent must not authenticate as Tom; a lapsed claude.ai session is therefore a hard external blocker the pipeline cannot self-clear (re-auth is attended-only).

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-270
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the safety/autonomy boundary that an autonomous agent must not assume Tom's credentials.
      15a: Searched least-privilege for AI agents, excessive-agency mitigation, and human-in-the-loop authority limits.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. OWASP Agentic AI Top 10 / OWASP AI Agent Security Cheat Sheet; Auth0 "Mitigate Excessive Agency in AI Agents with Zero Trust." — "Excessive agency" is a named top-tier agentic-AI risk; the recommended control is that the agent remain a scoped assistant, not an unchecked actor holding broad user authority. Directly supports "must not authenticate as Tom."
    2. Microsoft/Curity least-privilege AI-agent template; just-in-time / ephemeral credential issuance. — Best practice is workload identity + intent-based authorization + JIT credentials that expire after the task, NOT a standing user login. An agent operating under its own least-privilege identity (not the user's) is the canonical pattern.
    3. Human-in-the-loop authority boundary (Auth0 / Microsoft step-up approval). — For high-risk or authority-bearing actions the agent pauses for a human; obtaining/refreshing a session that carries the user's full authority is exactly such an action. Supports treating re-auth as a human-gated step.

  Strength of support: Strong

  Summary: The core boundary — an autonomous agent must not authenticate as Tom — is strongly supported by current agent-security guidance: excessive agency is a recognized failure mode, least privilege dictates the agent run under its own scoped identity rather than the user's, and high-authority actions warrant a human gate. The principle that the agent should not silently assume Tom's credentials is well-grounded.

  Caveats: The literature supports "agent must not hold the USER's identity"; it does NOT establish that re-auth must be FULLY attended-only. The same least-privilege sources describe scoped, delegated, revocable machine credentials that let unattended automation refresh access without ever being the user (see 15b). So the FIRST clause is strongly supported; the SECOND clause ("hard blocker the pipeline cannot self-clear") over-reaches the literature.

  Recommendation: SUPPORTED (core boundary); note scope limit on the attended-only sub-claim
