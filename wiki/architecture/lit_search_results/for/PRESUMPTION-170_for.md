SEARCH-FOR-PRESUMPTION-170:
  Date searched: 2026-05-15
  Original item: PRESUMPTION-170
  Original statement: "File-based handoff transferred from intra-user (PRESUMPTION-145 origin context) to inter-organizational federation (ASSUMPTION-133) without explicit transfer-validity audit; joins PRESUMPTION-002 CRITICAL cluster"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-170
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as transfer-validity inference (intra-user → inter-org federation)
      15a: Searched for federation wire-format security and update-cadence patterns across single-user vs multi-organization contexts
    Current status: SUPPORTED (Strong)

  Sources:
    1. Cartwright (1999) "The Dappled World" / (2007) "Hunting Causes and Using Them" — domain-transfer validity audit is canonical: principles validated in one domain don't automatically transfer to adjacent domains; explicit audit is required.
    2. Anderson (2008) "Security Engineering" — security properties of intra-user systems vs. multi-org federation systems differ at every layer: threat model, key management, replay, revocation, attribution.
    3. NIST SP 800-57 — key lifecycle management at federation scale requires HSM, rotation; intra-user single-machine systems usually skip this.
    4. ActivityPub deployment lessons — intra-instance behaviors do not transfer cleanly to cross-instance behaviors; defederation, abuse, attribution all emerge at federation scale.
    5. PRESUMPTION-002 carry-forward — Thousand Brains architecture transfers conceptually intact (CRITICAL priority MONITOR); the same transfer-validity pattern applies.
    6. PRESUMPTION-145 origin context — file-based handoff was designed for intra-user (Cowork-to-Cowork, single-user) flows; transfer to inter-org federation expands the threat model substantially.

  Strength of support: Strong

  Summary: The transfer-validity audit gap is well-supported across multiple converging literatures. Cartwright on domain-transfer validity, Anderson on security-property differences at federation scale, ActivityPub deployment lessons, and the C2A2-internal PRESUMPTION-002 cluster all converge on the same conclusion: principles validated in one context (here, intra-user file handoff) do not automatically transfer to another (inter-organizational federation). The presumption identifies a CRITICAL transfer-validity cluster member. Strong support: the inference is well-grounded; cluster membership is appropriate.

  Caveats: (a) "Transfer-validity audit" must be specified — what does the audit consist of? — without specification, the audit can stay open forever; (b) PRESUMPTION-002 CRITICAL cluster has been open since 2026-04-13; pattern of clusters staying open longer than they should; (c) HIGH priority for this item is appropriate (federation security surface).

  Recommendation: SUPPORTED (Strong) — transfer-validity audit gap is well-established; CRITICAL cluster membership confirmed; HIGH priority appropriate
