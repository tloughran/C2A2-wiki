SEARCH-FOR-PRESUMPTION-153:
  Date searched: 2026-05-14
  Original item: PRESUMPTION-153
  Original statement: "Signed-link integrity presumed sufficient against adversarial replay / signing-key compromise / SMS interception; no threat model articulated; UX optimization without security-depth tradeoff"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-153
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced via inference from ASSUMPTION-121 signed-link mechanism choice without threat model
      15a: Searched for threat-modeling-before-implementation in passwordless-auth security literature
    Current status: SUPPORTED

  Sources:
    1. Shostack (2014) "Threat Modeling: Designing for Security" — explicit threat models are a recognized prerequisite for security-relevant design decisions.
    2. OWASP Threat Modeling and STRIDE / PASTA methodologies — the gap (no threat model articulated) is the canonical concern.
    3. NIST SP 800-30 Risk Assessment — threat-model documentation is endorsed practice for authentication / authorization gates.
    4. SIM-swap, replay, and signing-key compromise are all canonical SMS-class threats with published mitigations (Twilio Verify documentation 2024; NIST SP 800-63B SP-3 SMS-as-restricted authenticator class).

  Strength of support: Strong

  Summary: The inference that signed-link mechanism design without an articulated threat model is a security-process gap is well-supported. SIM-swap, replay, and signing-key compromise are canonical SMS-class threats with established mitigation patterns. The presumption is correctly identifying that UX optimization without explicit security-depth tradeoff documentation is a recognized gap. Strong support for the inference.

  Caveats: (a) The threat-model gap is documentation, not necessarily implementation — the implementation may already implicitly mitigate; (b) For low-stakes external-escalation (e.g., "approve sending a tweet"), a lighter threat model may be acceptable; (c) Documentation-cost vs. analytic-clarity tradeoff exists.

  Recommendation: SUPPORTED — threat-model articulation is a recognized prerequisite; the gap is real
