SEARCH-FOR-ASSUMPTION-105:
  Date searched: 2026-05-11
  Original item: ASSUMPTION-105
  Original statement: "User-privacy rules prohibit password-based login on Tom's behalf — binding operating constraint surfacing as 5th-consecutive evening sync delivery failure cause"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-105
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-10 EOD 5th-consecutive evening-sync failure attribution
      15a: Searched for agent-autonomy boundaries, credential-handling rules, and user-privacy as binding operational constraint
    Current status: SUPPORTED

  Sources:
    1. NIST SP 800-63B (2017, rev. 2020) "Digital Identity Guidelines" — authentication-secret entry by an agent on the user's behalf is explicitly out-of-pattern for "something you know" credentials; delegation requires distinct credential type (e.g., OAuth-issued token).
    2. OWASP ASVS v4.0.3 §2.1 — passwords must not be exposed to or handled by intermediary services; brokered credential flows must use token-based delegation.
    3. Anthropic Acceptable Use Policy and Claude Usage Policies (as in effect 2026) — Claude must not collect, store, or use end-user authentication credentials such as passwords.
    4. Bonneau, Herley, van Oorschot, Stajano (2012) "The Quest to Replace Passwords" IEEE S&P — password-replay by proxy violates the canonical password security model.
    5. C2A2-internal: ASSUMPTION-079 (delegation-via-token only) and DECISION-022 (no-credential-handling boundary) are upstream architectural commitments that this assumption operationalizes.

  Strength of support: Strong

  Summary: Password-based login on a user's behalf by a software agent is explicitly out-of-pattern across the canonical authentication literature (NIST, OWASP, Bonneau et al.) and is prohibited by the operating Anthropic policies that govern Claude. Token-based delegation (OAuth 2.0, SAML, OIDC) is the canonical alternative. Treating user-privacy rules as a binding operating constraint — and surfacing the constraint as the cause of repeated delivery failure — is the literature-endorsed posture. The 5th-consecutive recurrence is a strong diagnostic signal that the constraint is in fact binding, not contingent.

  Caveats: (a) The binding-constraint framing should not preclude evaluating token-based delegation (Anthropic Connectors / OAuth) as the alternative — the constraint binds password-based delegation specifically; (b) Repeated-failure surfacing means the binding constraint is interacting with a workflow that does not accommodate it — the workflow is the variable, not the constraint; (c) Privacy-as-policy and privacy-as-architecture should be distinguished — policy can be relaxed only by Tom and only via deliberate explicit consent, never by inference.

  Recommendation: SUPPORTED (strong) — the binding-constraint framing is canonical; the operational implication is that the failing workflow must be redesigned around token-based delegation, not that the constraint should be relaxed
