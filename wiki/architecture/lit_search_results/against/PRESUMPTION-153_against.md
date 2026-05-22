SEARCH-AGAINST-PRESUMPTION-153:
  Date searched: 2026-05-14
  Original item: PRESUMPTION-153
  Original statement: "Signed-link integrity presumed sufficient against adversarial replay / signing-key compromise / SMS interception; no threat model articulated"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-153
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced via inference from ASSUMPTION-121 mechanism choice without threat model
      15b: Searched for counter-evidence on UX-optimized-without-threat-model designs
    Current status: NO-CHALLENGE-FOUND

  Sources:
    1. Shostack (2014) "Threat Modeling" — threat-model articulation is canonical prerequisite.
    2. For low-stakes flows, lighter threat model is acceptable — only mild counter.
    3. Twilio Verify default-implementation does some mitigations implicitly (TTL, single-use) — partial counter.

  Strength of challenge: Weak

  Summary: The presumption is well-founded. The only counter is that low-stakes flows tolerate lighter threat models and that Twilio's default-implementation handles some risks implicitly. Neither defense suffices because the stakes assignment itself requires a threat model. Weak counter.

  Specific risks: None substantial.

  Mitigations available: Threat model articulation, stakes classification.

  Recommendation: NO-CHALLENGE-FOUND — presumption inference is sound

  STEELMAN:
    Item: PRESUMPTION-153
    Strongest counterargument: Twilio default-implementation handles some risks (TTL, single-use) implicitly, so the threat model is partially encoded in the platform choice.
    What would need to be true for C2A2 to be safe: Threat model documented; stakes classified; platform-defaults audited against threats.
    How to test: Articulate threat model; map each threat to implementation or platform mitigation.
