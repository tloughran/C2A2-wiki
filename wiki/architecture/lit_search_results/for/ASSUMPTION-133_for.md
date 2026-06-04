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


---

SEARCH-FOR-ASSUMPTION-133 (RE-TRIGGER cycle 1):
  Date searched: 2026-05-25
  Original item: ASSUMPTION-133
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c] (cycle 1)
    Original item: ASSUMPTION-133
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..0: prior search/disposition cycles (see blocks above)
      15d (2026-05-24): re-triggered on weekly cadence (MONITOR-148 cycle 1)
      15a (cycle 1, 2026-05-25): re-searched for supporting literature
    Current status: refresh; no new supporting literature surfaced this cycle.

  Run context: On-cadence c2a2-lit-search-pipeline processing of the 2026-05-24 15d weekly RE-TRIGGER cohort (15d fired on schedule 2026-05-24; normal hand-off into the daily pipeline, not an exceptional drain).

  New evidence weighed: No new supporting literature surfaced since the last cycle. Prior cycles' findings stand; item remains in its established disposition until new operational evidence (from C2A2's own runs) or new external literature alters the picture.
  Sources (new / refreshed): No new sources this cycle.
  Strength of support: Unchanged from prior cycle.
  Summary: Cycle-1 refresh confirms the prior cycle's finding; the supporting literature base has not materially shifted. Recommendation carries forward unchanged.
  Caveats: Automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; a human-driven scan or operational evidence from C2A2's own runs is the more sensitive signal for status change.
  Recommendation: refreshed; carry forward prior recommendation


---

SEARCH-FOR-ASSUMPTION-133 (RE-TRIGGER cycle 2):
  Date searched: 2026-06-01
  Original item: ASSUMPTION-133
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-133
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..1: prior search/disposition cycles (see blocks above)
      15d (2026-05-31): re-triggered on weekly cadence; next_check 2026-05-31 elapsed
      15a (cycle 2, 2026-06-01): re-searched for supporting literature
    Current status: refresh; no new supporting literature surfaced this cycle.

  Run context: Clean weekly drain via the c2a2-lit-search-pipeline scheduled task (15a/15b/15c), running one hour after the 14a/14b self-awareness pipeline. Cohort re-triggered by 15d on 2026-05-31 (weekly cadence fired on time; next_check 2026-05-31 elapsed). Unlike the 2026-05-17 run, there is NO overdue 15d-schedule backlog — this is a normal on-cadence refresh.
  Landscape check: Automated landscape spot-check this cycle (3 genuine web searches across distinct clusters: passwordless/one-tap-link & SMS-auth security; Levin-Hoffman-Kastrup idealist convergence; multi-agent LLM systems instantiating research traditions/consensus). All three reaffirmed prior for/against profiles; no material literature shift detected. Spot-check is a sample, not an exhaustive per-item search.

  New evidence weighed: No new supporting literature surfaced in the week since the last cycle. The prior cycles' supportive findings stand.

  Sources (new / refreshed): No new sources this cycle.

  Strength of support: Unchanged from prior cycle.

  Summary: Cycle-2 refresh confirms the prior cycle's finding. The supporting literature base has not materially shifted in the past week; no new supportive sources surfaced during this automated cycle. The recommendation carries forward unchanged.

  Caveats: An automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; a human-driven literature scan or operational evidence from the C2A2 runs themselves would be the more sensitive signal for status change.

  Recommendation: refreshed; carry forward prior recommendation (refreshed; carry forward prior recommendation)
