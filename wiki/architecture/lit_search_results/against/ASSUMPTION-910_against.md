# ASSUMPTION-910 CHALLENGE REPORT

## SEARCH-AGAINST-ASSUMPTION-910

**Date searched:** 2026-08-10

**Original item:** ASSUMPTION-910

**Original statement:** "MC0001 is a competitor, not a corroboration. The wiki holds none of the three MC0001 talks." Discriminator: obtain and ingest the three talks; re-evaluate.

### PROVENANCE

- **Origin:** 14a
- **Chain:** [14a → 15b]
- **Original item:** ASSUMPTION-910
- **Item type:** ASSUMPTION (stated)
- **Transform at each step:**
  - 14a: Quoted verbatim; cross-referenced against yesterday's opposite reading of the same venue. [stated]
  - 15b: Searched for challenging literature on the same angle as PRESUMPTION-747 — corroboration vs. common-source bias, and the risk of characterizing an unread source sight-unseen.
- **Current status:** PARTIALLY-CHALLENGED

### Challenging evidence found: Partial

### Sources

1. **Common source bias (Wikipedia summary of the methodological concept, used across intelligence analysis and journalism).** — When two accounts trace back to a shared origin rather than independent observation, treating them as independent corroboration (or independent competition) is an error; the correct test is whether the sources are causally independent, not merely whether their surface content agrees or disagrees. This directly bears on labeling MC0001 "competitor, not corroboration" *before* the underlying talks are read: the current judgment is being made on a proxy (topic/venue framing) rather than on the actual argumentative content, which is exactly the failure mode common-source-bias analysis warns against.
2. **[unverified — from search snippet] Office of Research Integrity (ORI), "Citing Sources that Were Not Read or Thoroughly Understood."** — Characterizing a source's stance (here, "competitor") without having read it is a documented and cautioned-against research practice; secondary characterization is reported to be common (only ~20% of citing authors are estimated in some studies to have read the original in full) but is explicitly flagged as a source of downstream error propagation.
3. **Confirmation-bias-in-cascade literature (general summaries on information cascades and bias-snowball effects).** — If the "competitor, not corroboration" framing is itself propagated onward (e.g., into related PRESUMPTION-747's cross-connection register) before verification, the system risks a bias cascade where a provisional, unread-source judgment hardens into an accepted classification through repeated downstream citation, independent of whether it was ever correct.

### Strength of challenge: Moderate

### Summary

The assumption is explicitly self-flagged as untested and already carries its own discriminator (obtain and ingest the talks), which is good practice. The literature's challenge is not that the "competitor" reading is wrong, but that classifying a source's relationship to the wiki's position as competing vs. corroborating *before reading the primary material* is a known-risky move: common-source-bias analysis shows surface-level agreement/disagreement labels are unreliable proxies for genuine independence or genuine conflict, and citation-integrity literature documents that characterizing unread sources is a frequent, cautioned-against practice that can propagate errors downstream once the label is picked up by related items (here, explicitly linked to PRESUMPTION-747's cross-connection question).

### Specific risks for C2A2

If "competitor, not corroboration" is treated as settled before the three MC0001 talks are ingested, and this classification feeds into the cross-connection count (PRESUMPTION-747's headline metric), the system risks recording a confident classification on an unverified basis — and if downstream agents cite this assumption rather than re-deriving it from the primary talks, the error (if any) becomes harder to catch (bias cascade).

### Mitigations available

The assumption already names its own fix (obtain and ingest the three talks; re-evaluate) — this is the correct mitigation per the citation-integrity literature. Additionally, the classification should be explicitly marked "provisional, based on venue framing not primary content" in any downstream register entry until the talks are ingested, to prevent the common-source-bias/cascade risk from hardening prematurely.

### Recommendation: PARTIALLY-CHALLENGED

---

## STEELMAN

**Item:** ASSUMPTION-910

**Strongest counterargument:** The strongest objection is that "competitor, not corroboration" is a conclusion about the *relationship between two arguments*, which cannot be reliably assessed without reading both arguments — and the assumption itself concedes the wiki holds none of the three source talks. Common-source-bias methodology holds that surface framing (same venue, same speaker code MC0001) is a weak proxy for whether the underlying claims genuinely conflict; two talks could easily share a venue and topic while making compatible arguments, or could superficially agree while resting on incompatible premises. Until the primary talks are ingested, "competitor" is a hypothesis derived from context, not a finding derived from content, and treating it as a POSITIVE finding (as the surrounding register apparently does) risks anchoring later agents to an unverified label.

**What would need to be true for C2A2 to be safe:** The "competitor" label would need to be explicitly tagged as provisional/context-derived (not content-derived) everywhere it propagates, and any downstream metric or register entry (e.g., PRESUMPTION-747's cross-connection count) that depends on it would need to be flagged as resting on an unverified classification until the talks are read.

**How to test:** Obtain and ingest the three MC0001 talks (the assumption's own stated discriminator), independently re-derive the competitor-vs-corroboration judgment from their actual argumentative content, and check whether it matches the pre-ingestion label — this is directly testable and requires no external literature, only the primary sources.
