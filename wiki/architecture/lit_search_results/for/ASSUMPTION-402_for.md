SEARCH-FOR-ASSUMPTION-402:
  Date searched: 2026-07-02
  Original item: ASSUMPTION-402
  Original statement: "A logged-out claude.ai is a hard stop for an autonomous run; entering credentials on the user's behalf is out of scope for an unattended agent."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-402
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-01 autonomous-run context (a logged-out claude.ai encountered mid-run)
      15a: Searched for supporting literature (genuine web search 2026-07-02)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Ping Identity, "Identity for AI: The Ultimate Guide to Agentic IAM" (2026) — AI agents should NEVER log in with a human user's credentials or "borrow" their access; the canonical pattern is authenticated delegation with scoped, ephemeral tokens (OAuth 2.0 / OIDC), not credential entry on the user's behalf. Directly supports the "out of scope" clause.
    2. Elementum / Galileo / TeamCopilot HITL best-practice writeups (2026) — reserve human review/approval for actions that are risky, irreversible, or sensitive (grant access, change production, authenticate). Entering credentials is exactly such an action; industry consensus keeps it human-gated.
    3. C2A2's own PREMISE-015 (validated) — "User-privacy rules prohibit password-based login by software agents on the user's behalf ... token-based delegation is the canonical alternative." ASSUMPTION-402 is the operational instance of an already-validated premise; internal consistency is strong.

  Strength of support: Strong

  Summary: The credential clause of ASSUMPTION-402 is strongly and unambiguously supported: the agentic-IAM and HITL literatures converge that unattended agents must not enter or borrow a human's credentials, and that authentication is a human-gated, delegation-only action. This also matches C2A2's already-validated PREMISE-015 and the ASSUMPTION-079 / DECISION-022 no-credential-handling boundary. Support for "not entering credentials" is therefore both external and internal.

  Caveats: The literature supports the "don't enter credentials" clause outright. It supports the "hard stop" clause only conditionally — the same sources favor a hard stop that ESCALATES/ALERTS (surfaces the blocked state to a human) over one that silently ends the run. Support is for the boundary, not for silent passivity (see 15b).

  Recommendation: SUPPORTED (Strong for the credential boundary; the "hard stop" clause is supported only when paired with escalation)
