---
title: Optional Interoperability
pathway_id: optional_interoperability
status: drafted
created: 2026-05-14
depends_on: [portability_toolkit, broker, outreach_automation]
enables: [institutional_scale]
isme_critical: no
---

# Pathway 19: Optional Interoperability

## Purpose

Independent instances can plug into a shared layer when they choose if it serves their purposes, enabling federation without forcing data-sharing or loss of autonomy.

Once Pathway 18 enables portability — multiple communities running their own instances of the framework — Pathway 19 addresses what happens when those communities want to connect. The key design principle is optionality: federation is never required, never forced, and never assumed. Communities that have built their own instances can choose to plug into a shared layer when doing so serves their specific purposes, and disconnect just as cleanly when it does not.

This is distinct from a centralized architecture. There is no master vault, no required alignment, no canonical authority. Instead, there is a shared layer — call it the inter-instance bus — that communities can access for specific purposes: comparing how different traditions address the same problem, exploring cross-tradition PRS connections, finding partners for joint inquiry, or invoking a peer instance's perspective lattice on a question their own does not yet cover. PRESUMPTION-145 (file-based handoff as simpler primary path) directly informs the wire-format choice here; the architecture should follow that lead rather than default to OAuth-token-mediated APIs.

## Function set

*(Cowork-drafted 2026-05-14; not yet validated in walk dialogue.)*

Four pieces:

1. **Federation registry.** A lightweight, optional public list of instances that have opted in to be discoverable. Each entry: instance name, public URL, contact, list of topics the instance claims competence in, public-portion-of-vault root. No private data lives in the registry; it is a phone book of consenting parties.

2. **Inter-instance query protocol.** A request format an instance can issue to a peer: "Here is a question (or a PRS fragment, or a perspective-lattice gap). Do you have substantive material on this? If so, return a pointer to your public attestations." Responses include the same honesty-layer markings as internal claims. Following PRESUMPTION-145, the default wire format is file-based exchange (signed JSON drops over HTTPS) rather than persistent API connections.

3. **Selective sharing controls.** Per-instance configuration over what is queryable, by whom, and on what topics. Default: nothing is queryable. Communities opt in to surface specific perspectives, specific PRS entries, or specific decisions to specific federation peers. Granularity matters: a community might federate with a partner instance on shared problems but not on internal governance debates.

4. **Cross-instance attribution and provenance.** When material from a peer instance shows up in a local query result, it carries the peer's instance ID, the peer's honesty-layer markings, and a link back to the peer's source. Attribution is mandatory; silent absorption of peer material is a federation failure mode.

## Architecture sketch

*(Cowork-drafted 2026-05-14.)*

```
   instance-A (Carpathi)                instance-B (peer)
        │                                     │
        │ (1) consults federation registry    │
        │     ──────────────────────────────→ │
        │                                     │
        │ (2) issues inter-instance query     │
        │     (signed JSON, file-based)       │
        │     ──────────────────────────────→ │
        │                                     │
        │                                     │ (3) consults selective
        │                                     │     sharing config:
        │                                     │     is topic shareable
        │                                     │     to instance-A?
        │                                     │
        │ (4) returns public attestations     │
        │     with honesty-layer markings     │
        │     ←────────────────────────────── │
        │     (or polite decline)             │
        │                                     │
        │ (5) local broker renders peer       │
        │     material with attribution       │
        │     and provenance link             │
        │                                     │
   user-facing answer in A,
   peer material clearly marked
   as instance-B / public-vault-root/path
```

## Decisions taken

*(Cowork-derived from walk description; subject to Tom's amendment.)*

- **Optionality is structural, not aspirational.** Federation defaults to off. An instance that simply runs and never federates is a fully legitimate use of the framework. Federation is an affordance, not an expectation.

- **File-based handoff is the primary wire format (per PRESUMPTION-145).** Signed JSON drops over HTTPS are simpler, more inspectable, and less brittle than persistent OAuth-token-mediated APIs. The architectural commitment from Pathway 00 (broker as scope enforcer) extends to inter-instance queries: each request is a discrete, signed, scope-checked event.

- **Selective sharing is per-topic, per-peer.** Not a binary public/private flag. Communities should be able to say "share our Aquinas material with the Notre Dame physics instance but not with anyone else, and never share our internal governance debates."

- **Attribution is mandatory.** Peer material in local results always carries the peer's identity, honesty-layer markings, and source link. Federation that obscures provenance defeats the purpose.

- **No canonical instance.** Carpathi is not a master vault even after federation. Peer instances have equal standing. The framework is designed for a federated ecosystem of peers, not a hub-and-spoke architecture.

## Open questions

- What is the minimal shared layer that enables meaningful federation without requiring standardization of content?
- How do communities signal willingness to interoperate without exposing private intellectual work? (Registry entry granularity, claim-of-competence vocabularies.)
- What does "opt-in at specific points" look like technically — selective sharing vs. full access, per-topic vs. per-peer, per-request vs. standing permissions?
- How does PRESUMPTION-145 (file-based handoff as simpler primary path) inform the wire format in practice? (Open: is file-based sufficient for all federation, or does some use case require persistent connections?)
- What happens when a federated peer's instance goes dark? (Stale registry entries, broken provenance links, attribution drift over time.)
- Governance of the federation registry itself: who runs it, who can list, who can delist? (See Pathway 24, Meta-Crafts and Governance.)

## Edges

- **portability_toolkit (18):** portability is the prerequisite; federation only makes sense for instances that exist as autonomous entities first.
- **broker (00):** the broker is the natural enforcement point for federation policy — signed-request verification, selective-sharing config, attribution preservation all happen broker-side.
- **outreach_automation (12):** the broker must refuse outreach that violates federation autonomy (e.g., contacting a peer's faculty without their instance's consent).
- **institutional_scale (20):** institutional deployment will be one of the first federation test cases (SGA communities connecting across departments).
- **meta_crafts_governance (24):** the governance of inter-instance relationships is itself a meta-craft; federation needs a community of practice around how peers should behave.
- **agent_developed_participant (17):** the agent's character must remain consistent locally even when invoking peer material; cross-instance peer responses do not overwrite the local agent's voice or commitments.

## Provenance / source dialogue

- Session: 2026-05-14 morning walk, Tom on phone in Chat mode, conversation `https://claude.ai/chat/ed8b7056-407d-4a71-8fae-62b08e9613e0`. Source dialogue captured in `morning_walk_2026-05-14.md` and `2026-05-14_pathways_18-25_review.md`.
- Originating framing from the walk: "Independent instances can plug into a shared layer when they choose if it serves their purposes, enabling federation without forcing data-sharing or loss of autonomy."
- The file-based-handoff commitment derives from PRESUMPTION-145, REVISE'd 2026-05-13: the file-based-handoff alternative to OAuth/token delegation may be the simpler primary path rather than the parenthetical alternative it was originally presented as.

## Status

*(Implementation outline drafted by Cowork 2026-05-14; sequencing subject to Tom's amendment.)*

Drafted in prose. Implementation order: (a) ratify PRESUMPTION-145 as decision, fixing file-based handoff as the federation wire format; (b) specify the inter-instance query schema (request and response JSON shapes); (c) build the broker-side selective-sharing config and enforcement; (d) build the federation registry as a small static-site-friendly artifact (probably a YAML file in a public repo); (e) implement attribution rendering in the local agent and visualization layer; (f) test by spinning up a second internal instance and federating Carpathi with it before any external peer is invited. Not ISME-critical; demonstration of federation likely waits until after the July prototype lands.
