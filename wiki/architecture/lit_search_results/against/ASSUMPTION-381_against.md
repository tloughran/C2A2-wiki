SEARCH-AGAINST-ASSUMPTION-381:
  Date searched: 2026-06-27
  Original item: ASSUMPTION-381
  Original statement: "Dating signals by proposal date (formation) while carrying source_date (vintage overlay) is the honest dual encoding"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-381
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: formation-date + source/vintage-date dual encoding claimed as honest
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Bitemporal-modeling literature (which event is valid-time begin?). - Two timestamps are honest only if their semantics are precisely defined; calling proposal date "formation" embeds a contestable choice of the valid-time start event (cf. PRESUMPTION-410).
    2. Bitemporal completeness arguments. - Strict bitemporal honesty often needs MORE than two points (e.g., engagement, approval, supersession); a two-field scheme can still collapse distinct lifecycle events and thus be only partially honest.
    3. Semantic-ambiguity / metadata-provenance critiques. - A label like "formation" can be read inconsistently by downstream consumers if the chosen event is not documented, reintroducing the very conflation the dual encoding aims to avoid.

  Strength of challenge: Weak-Moderate

  Summary: The dual-encoding structure is sound; the challenge targets the SEMANTICS, not the form. Honesty depends on rigorously defining what "formation" denotes - proposal authoring is one defensible choice among several (engagement, approval), and picking it silently is a modeling commitment, not a neutral fact. A strictly honest temporal model may also require more than two timestamps to avoid collapsing distinct lifecycle events.

  Specific risks: "Formation" interpreted inconsistently downstream; distinct lifecycle moments collapsed into one date; apparent honesty masking an unexamined choice (routed to 410).

  Mitigations available: Document precisely which event "formation" denotes; consider carrying engagement/approval timestamps when they differ materially; treat the choice as explicit, reviewable metadata.

  STEELMAN:
    Item: ASSUMPTION-381
    Strongest counterargument: Two timestamps are only "honest" if their referents are pinned down; naming the proposal date "formation" quietly decides a contested semantic question, so the scheme can look rigorous while encoding an unexamined choice about when a connection is born.
    What would need to be true for C2A2 to be safe: "Formation" is explicitly defined and documented, and the two-axis scheme does not collapse materially distinct lifecycle events.
    How to test: Check cases where authoring, engagement, and approval dates diverge and see whether a single "formation" date misrepresents the connection's history.

  Search scope: Bitemporal semantics; valid-time event choice; lifecycle modeling. Adequate.

  Recommendation: PARTIALLY-CHALLENGED
