SEARCH-FOR-ASSUMPTION-133:
  Date searched: 2026-05-15
  Original item: ASSUMPTION-133
  Original statement: "File-based handoff (signed JSON over HTTPS) is the primary wire format for inter-instance federation per PRESUMPTION-145; OAuth-token APIs demoted"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-133
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Pathway 19 federation wire-format commitment
      15a: Searched for federation wire-format design tradeoffs (ActivityPub, scientific data exchange, signed-JSON precedents)
    Current status: PARTIALLY-SUPPORTED (Moderate)

  Sources:
    1. ActivityPub (W3C 2018) and Mastodon implementation — federated social network using signed JSON over HTTPS; canonical precedent for file-based handoff federation at scale.
    2. JSON-LD signatures + Linked Data Proofs (W3C Verifiable Credentials 2.0, 2025) — signed-JSON-over-HTTPS is the canonical W3C federation pattern.
    3. SOLID protocol (Berners-Lee et al.) — file-based federation with signed data; aligns with C2A2 commitment.
    4. Scientific data exchange standards: NetCDF, HDF5, JSON-API — file-based handoffs dominate cross-organization scientific data flow; OAuth-token APIs are common for compute access but not for data archival.
    5. ATProto (Bluesky 2024+) — signed-record-based federation; demonstrates file-based handoff at scale.
    6. RFC 7515 / 8725 — JWS (JSON Web Signature) is the canonical signed-JSON spec.

  Strength of support: Moderate-to-Strong (Moderate overall due to security caveats from 15b)

  Summary: Signed JSON over HTTPS is a well-established federation wire format with multiple canonical implementations (ActivityPub, ATProto, SOLID, Verifiable Credentials). The "OAuth-token APIs demoted" framing is also defensible for archival/data-exchange flows: OAuth is canonical for delegated authorization to live services, but is not the natural choice for inter-organizational archival data exchange. The "primary" framing aligns with ActivityPub-class federation patterns. Moderate-to-Strong support, though security caveats (key management, replay) are real (15b paired).

  Caveats: (a) Signed JSON requires key management — non-trivial in multi-organization deployments; (b) Replay attacks must be prevented (timestamps, nonces); (c) Staleness — file-based handoff trades real-time for archival; (d) "Primary" doesn't preclude OAuth-token APIs for live-query flows; (e) PRESUMPTION-170 paired — transfer from intra-user origin context to inter-org federation is not audited.

  Recommendation: PARTIALLY-SUPPORTED (Moderate) — canonical pattern; security implementation is the load-bearing concern
