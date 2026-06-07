SEARCH-AGAINST-ASSUMPTION-278:
  Date searched: 2026-06-07
  Original item: ASSUMPTION-278
  Original statement: Merging the 156 curated communities into the Cards directory under their own CC-xxx ids (graph becomes a literal id-subset of the cards) is the correct way to make the directory⊇graph relationship true and to unblock the deferred cross-navigation hand-off on the shared key.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-278
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the stated decision that minting shared ids makes directory⊇graph true.
      15b: Searched for evidence that key-assignment cannot MAKE a subset relation true and that this is a known modeling error.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Record-linkage / entity-resolution theory (Fellegi-Sunter; Christen, "Data Matching," 2012). — A join key is supposed to ENCODE an established co-reference, not create it; minting a key where measured overlap is near zero (0 id / 3 name / 5 host) manufactures matches the data do not support. Challenges "makes the relationship true."
    2. Identity-vs-association modeling (Chen ER model). — Making one set a subset of another by assigning ids asserts an IS-A/identity relation; if the true relation is association between distinct kinds, this is a category error baked into the schema. Challenges "correct way."
    3. MDM over-merge caution (golden-record practice). — Assigning a shared id to records that are not the same entity creates false golden records that propagate downstream; unification must be earned, not declared. Direct challenge.

  Strength of challenge: Moderate-Strong

  Summary: The assumption confuses making a relationship ADDRESSABLE with making it TRUE. Assigning CC-xxx ids does unblock the hand-off mechanically, but it does so by DECLARING the directory⊇graph relation rather than establishing it — and the only measurement to date (2026-06-05: 0 id / 3 name / 5 host overlap across 156×855) says the relation is empirically near-absent. Record-linkage, ER, and MDM literature all treat a key as the expression of an established identity, not its creator; minting it here risks manufacturing the very identity that was found missing. This is the realized, enacted form of the prior unvalidated-P3-join systemic risk (REVISE-089 / MONITOR-307).

  Specific risks: A false directory⊇graph relation becomes load-bearing: cross-navigation, any "one dataset / two projections" reasoning, and downstream P3 promotion all inherit an identity that was asserted by fiat; unwinding a committed id space later is expensive (the MDM false-golden-record failure mode).

  Mitigations available: Run the record-linkage experiment FIRST (the REVISE-089 measurement) before committing the id space; if overlap stays near zero, model curated↔directory as ASSOCIATION via a link table (never merge); treat the CC-xxx assignment as PROVISIONAL until identity is positively established; make the identity-vs-association decision explicit (couples PRESUMPTION-312, MONITOR-307).

  STEELMAN:
    Item: ASSUMPTION-278
    Strongest counterargument: "The correct way to make directory⊇graph true" begs the question: a subset relation is true only if the members are the same entities, and that is exactly what is unmeasured here. Surrogate keys and MDM ids are legitimate only as the OUTPUT of an identity decision; used as a SUBSTITUTE for one, they manufacture the relation and hide an empirical gap (0/3/5) behind a schema fact. Once the id space is committed and consumers depend on it, the unexamined identity assertion is costly to reverse — so the "correct way" may have foreclosed the very question it needed to answer.
    What would need to be true for C2A2 to be safe: The curated communities and their directory records genuinely co-refer (same entities), established by a linkage measurement BEFORE the id space is committed — not assumed by the act of assigning ids.
    How to test: Run the REVISE-089 record-linkage experiment; if overlap remains near the signal floor, the merge asserted rather than discovered identity, and association-by-link is the correct model.

  Recommendation: CHALLENGED
