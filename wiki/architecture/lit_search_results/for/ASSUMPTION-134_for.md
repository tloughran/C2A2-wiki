SEARCH-FOR-ASSUMPTION-134:
  Date searched: 2026-05-15
  Original item: ASSUMPTION-134
  Original statement: "Federation defaults to OFF; 'optionality is structural, not aspirational'; selective sharing per-topic per-peer; attribution mandatory"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-134
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Pathway 19/20 federation default-off commitment
      15a: Searched for default-off federation precedents in academic networks and fediverse design
    Current status: SUPPORTED (Strong)

  Sources:
    1. Thaler & Sunstein (2008) "Nudge" — default selection has outsized effect on adoption; opt-in defaults preserve agency.
    2. ActivityPub / Mastodon instance design — most fediverse instances default to "manually approve federation" or "instance allowlist"; defederation is a first-class operation.
    3. Academic data-sharing networks (DataONE, ICPSR, Re3data) — default-off with explicit opt-in per-dataset is the canonical academic federation pattern.
    4. Verifiable Credentials (W3C 2.0) — selective disclosure with attribution is canonical.
    5. GDPR Article 5 / data-minimization principle — opt-in attribution is the canonical privacy-preserving default.
    6. CITI Program / FAIR data principles — attribution is mandatory for academic data exchange; aligns with C2A2 commitment.
    7. Norman (2013) "Design of Everyday Things" — "structural not aspirational" framing matches affordance design literature: defaults must be implemented as the easy path, not declared as policy.

  Strength of support: Strong

  Summary: Default-off federation with mandatory attribution is well-supported across multiple traditions: behavioral economics (Nudge), W3C federation standards (ActivityPub, Verifiable Credentials), academic data-sharing (FAIR, DataONE), and privacy regulation (GDPR). The "structural not aspirational" framing matches affordance-design literature — defaults must be enforced by the implementation, not stated as policy. Selective per-topic per-peer sharing aligns with capability-based security and verifiable-credential selective-disclosure patterns. Strong support across multiple converging literatures.

  Caveats: (a) "Mandatory attribution" enforceability at federation scale is the implementation challenge — see 15b paired; (b) Default-off can produce under-federation (no one ever opts in); requires complementary opt-in affordances; (c) Per-topic per-peer granularity has UI complexity cost.

  Recommendation: SUPPORTED (Strong) — default-off + attribution is canonical pattern; enforcement remains the load-bearing implementation concern
