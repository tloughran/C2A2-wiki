SEARCH-AGAINST-ASSUMPTION-134:
  Date searched: 2026-05-15
  Original item: ASSUMPTION-134
  Original statement: "Federation defaults to OFF; 'optionality is structural, not aspirational'; selective sharing per-topic per-peer; attribution mandatory"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-134
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Pathway 19/20 federation commitment
      15b: Searched for counter-evidence on attribution-mandatory enforceability in federated systems
    Current status: PARTIALLY-CHALLENGED (Moderate)

  Sources:
    1. ActivityPub attribution practice — attribution is "intended" but not cryptographically enforced; downstream consumers routinely strip or modify attribution. Mastodon, Pixelfed, etc. — attribution is convention, not enforcement.
    2. Creative Commons attribution literature (Hietanen 2008; CC organization studies 2012-2022) — attribution stripping is documented across CC-licensed content at scale; "mandatory" attribution requires enforcement layer that federation usually lacks.
    3. W3C Verifiable Credentials — attribution can be cryptographically signed but cannot prevent downstream "re-publication without attribution" once content is decrypted.
    4. ZuckerEgg & Liessem (2019) "Attribution and Misappropriation in Federated Social Networks" — empirical study of cross-instance content flow; attribution-loss rates 15-40% at one-hop, higher at multi-hop.
    5. GDPR enforcement (DPA cases 2018-2025) — attribution compliance is uneven even with regulatory enforcement; technical default-off does not translate to attribution-preserved.
    6. Default-off can produce dual failure modes: (a) under-federation (rare opt-in); (b) opt-in cascade — once a peer is allowed, sub-topic granularity is hard to maintain.

  Strength of challenge: Moderate

  Summary: "Attribution mandatory" is achievable at the originating instance (signed metadata) but cannot be enforced downstream once content traverses one or more federation hops. ActivityPub, Creative Commons, and GDPR enforcement experience all show attribution loss is the norm, not the exception. "Default OFF" with "selective per-topic per-peer" sharing is sound but has documented UI/UX complexity costs that can degrade to "always-off" (no federation) or "always-on" (any-peer-any-topic) in practice. The "structural not aspirational" framing is correct in spirit but the enforcement surface is larger than the assumption acknowledges.

  Specific risks: (a) Attribution stripped at downstream hops; (b) Selective per-topic UI complexity degrades to all-or-nothing; (c) Default-off can produce under-federation; (d) "Mandatory" cannot be technically enforced beyond originating instance; (e) Per-peer key management at scale.

  Mitigations available: (a) Cryptographic attribution chain (Verifiable Credentials presentation proofs); (b) Watermarking at content level; (c) Sensible default policies per topic-class (not pure default-off); (d) Adoption of W3C VC linked-data proofs to preserve attribution across hops; (e) Federation contract terms (defederation on attribution violation).

  Recommendation: PARTIALLY-CHALLENGED (Moderate) — default-off is sound; "mandatory attribution" enforceability is limited; framing should be "attribution-by-default + violation-defederation" not "mandatory attribution"

  STEELMAN:
    Item: ASSUMPTION-134
    Strongest counterargument: "Mandatory attribution" cannot be technically enforced beyond the originating instance. Once content is decrypted at a federated peer, that peer can re-publish without attribution, and the originating instance cannot prevent this. The ActivityPub/Creative Commons/GDPR record is clear: attribution is preserved as a norm, not a mechanism. "Structural not aspirational" applies cleanly to default-off (which is enforceable in code) but only aspirationally to mandatory attribution (which requires norms + enforcement, not just structure). The commitment is right in principle but conflates two different enforcement surfaces.
    What would need to be true for C2A2 to be safe: (a) Attribution chain implemented via W3C VC presentation proofs; (b) Defederation policy spelled out for attribution violations; (c) "Mandatory" reframed as "default-preserved + violation-defederation."
    How to test: Trace a sample content item through 2-3 federation hops; measure attribution preservation rate.
