SEARCH-FOR-ASSUMPTION-071:
  Date searched: 2026-04-28
  Original item: ASSUMPTION-071
  Original statement: "Browser-authentication on the user's behalf is an agent-prohibited / explicit-permission action"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-071
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-04-27 daily run — Cowork↔Chat sync attempt blocked by browser auth-gap
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Anthropic MCP design notes and "tool-use safety" guidance (Anthropic 2024–2025) — user-mediated credential entry is the canonical pattern; tools that exercise the user's identity must require explicit authorization.
    2. OAuth 2.0 / OpenID Connect specifications (RFC 6749, RFC 6750) — delegated authorization is mediated through the resource owner; agent acting "on behalf of" the user is conditioned on the user-granted scope, not on the agent acquiring credentials directly.
    3. NIST SP 800-63 (Digital Identity Guidelines) — credential entry is treated as a user-only action; surrogates require separately-issued tokens.
    4. Agent-safety literature (Shavit et al. 2023 "Practices for Governing Agentic AI Systems"; Anthropic Responsible Scaling Policy v2 discussion of agentic tool authorization) — autonomous agents acquiring user credentials is a recognized failure mode and is uniformly recommended against in early AI-agent governance work.
    5. C2A2-internal precedent: DECISION-024 (turn-cap), PREMISE-009 (orchestrator least-privilege) — both align with the same principle that user-bound capabilities require user mediation.

  Strength of support: Strong

  Summary: The literature on delegated authorization, identity standards, and agent safety converges on the same principle: an autonomous agent acting on the user's behalf does so via tokens issued in a user-mediated flow, not by acquiring credentials and signing in directly. Treating browser sign-in as an agent-prohibited / explicit-permission action is the canonical stance and is reinforced by Anthropic's own MCP design guidance. C2A2's framing is well-supported as a default posture.

  Caveats: (a) The "prohibited" framing is strong; the literature actually says "user-mediated and explicit", not "prohibited under all conditions"; pre-issued long-lived tokens, when stored properly, are a literature-endorsed substitute that ASSUMPTION-071's framing might over-restrict. (b) Support is strongest for credential entry; weaker for already-authenticated browser profiles where the user has pre-consented at the OS level.

  Recommendation: SUPPORTED (the policy aligns with delegated-authorization standards and agent-safety guidance; "prohibited" framing slightly overshoots the literature's "user-mediated/explicit-consent" formulation)
