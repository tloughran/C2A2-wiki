SEARCH-AGAINST-ASSUMPTION-071:
  Date searched: 2026-04-28
  Original item: ASSUMPTION-071
  Original statement: "Browser-authentication on the user's behalf is an agent-prohibited / explicit-permission action"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-071
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-04-27
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. RFC 8628 (OAuth 2.0 Device Authorization Grant) — establishes patterns for delegated agent authorization that can be initiated and exercised by an agent within user-pre-issued grants. The "blanket no-sign-in" framing can be too restrictive; pre-issued long-lived tokens or device-flow tokens are literature-endorsed substitutes.
    2. Service-account / robot-account literature (Google IAM service accounts; AWS IAM roles for service accounts) — endorses pre-authenticated identities for autonomous agents in well-scoped enterprise contexts; the "user-mediated only" framing does not capture this.
    3. Browser-extension / Chrome MCP design notes — already-authenticated browser profiles are a working substitute for credential entry; the literature on browser-automation supports agents acting through pre-authenticated sessions.
    4. Anthropic's own "Claude in Chrome" extension — operationally, the user pre-authenticates via the OS, and the agent acts within that pre-authentication. This contradicts a literal reading of "agent-prohibited."
    5. Practical-agent-systems literature (Park et al. 2023 "Generative Agents"): when narrowly scoped, agents do exercise the user's session via pre-authenticated channels; "prohibited" is too strong.

  Strength of challenge: Weak-to-Moderate

  Summary: The literal "agent-prohibited" framing of ASSUMPTION-071 is challenged by pre-issued-token, service-account, and pre-authenticated-browser patterns — all of which are literature-endorsed agent capabilities. The defensible version is "user-credential-entry is agent-prohibited"; the broader version is too restrictive and contradicts working systems including Anthropic's own Chrome MCP.

  Specific risks: (a) Overly strict policy may block legitimate sync workflows for Cowork ↔ Chat that could be enabled by pre-issued tokens; (b) the framing conflates "credential entry" with "any auth-bearing action"; (c) the policy may force user-fix into a bottleneck where a token-based workaround was available.

  Mitigations available: (a) Reframe as "user-credential-entry is agent-prohibited; pre-issued tokens / pre-authenticated profiles are explicitly permitted under defined scope"; (b) document the substitution patterns in the architecture record.

  Recommendation: PARTIALLY-CHALLENGED (the credential-entry version is well-supported; the broader "any auth action" version is challenged by pre-issued-token patterns)

  STEELMAN:
    Item: ASSUMPTION-071
    Strongest counterargument: A literal "agent-prohibited" stance on browser-authentication is wider than the agent-safety literature actually warrants. The literature is consistent against agents *entering credentials*; it is permissive about agents *exercising pre-issued tokens or pre-authenticated sessions*. ASSUMPTION-071's framing collapses these two cases and forecloses the workaround that would resolve the daily Cowork↔Chat sync gap.
    What would need to be true for C2A2 to be safe: The policy is articulated as "user-credential-entry is prohibited; pre-issued tokens / pre-authenticated profiles are permitted under defined scope and audit," with the substitution pattern documented in the architecture record.
    How to test: Implement a token-based sync path in a sandboxed test; verify it satisfies agent-safety guidelines (audit log, scope-restriction, revocability) without triggering the credential-entry concern.
