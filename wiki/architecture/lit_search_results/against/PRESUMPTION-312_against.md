SEARCH-AGAINST-PRESUMPTION-312:
  Date searched: 2026-06-07
  Original item: PRESUMPTION-312
  Original statement: [inferred] Assigning shared CC-xxx ids presumes that sharing an id key constitutes genuine entity identity rather than asserting a link by fiat; the merge may have manufactured the identity that 2026-06-05 found missing (disjoint id spaces) rather than discovering it.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-312
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated presumption that minting a shared key establishes entity identity.
      15b: Searched for evidence that key-assignment cannot constitute identity and that declaring identity is a known error.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Entity-resolution theory (Fellegi-Sunter probabilistic model; Christen 2012). — Identity is an INFERENCE from evidence (matching attributes), not a stipulation; declaring co-reference where measured overlap is ~0 (0 id / 3 name / 5 host) is precisely a false-match, the error ER is built to avoid. Direct challenge.
    2. Identity-vs-association distinction (Chen ER model; relational theory). — A shared key encodes identity; using it for entities that are merely associated (or unrelated) is a category error that propagates through every foreign-key consumer. Challenges "shared key = identity."
    3. MDM golden-record over-merge failures. — Industry practice documents that merging non-co-referent records into one id produces persistent false golden records that are expensive to split; the 2026-06-05 disjoint-id finding is the warning sign MDM says to heed. Challenges the merge.

  Strength of challenge: Strong

  Summary: The presumption is strongly challenged: across ER, relational modeling, and MDM, identity is something you ESTABLISH from evidence and then EXPRESS with a key — never something a key CREATES. The 2026-06-05 measurement (0 id / 3 name / 5 host overlap) is exactly the near-zero-evidence regime where assigning a shared id manufactures co-reference rather than discovering it. The merge answers "are these the same entity?" with "they are now," which is the canonical false-match / over-merge error. This is the realized escalation of the prior unvalidated-P3-join cluster (REVISE-089, MONITOR-307): the doubted join is no longer merely unbuilt — it has been asserted by fiat.

  Specific risks: Every downstream consumer (cross-navigation, "one dataset" reasoning, P3 promotion, health metrics over the merged set) inherits a manufactured identity; if a later linkage measurement contradicts it, splitting a committed id space is costly and may already have corrupted derived artifacts.

  Mitigations available: Treat CC-xxx assignment as PROVISIONAL pending the REVISE-089 linkage measurement; model curated↔directory as association (link table) until identity is positively established; if a shared id is needed operationally, tag it explicitly as an ASSERTED (not evidenced) link so consumers can discount it; make the identity-vs-association decision explicit for Tom.

  STEELMAN:
    Item: PRESUMPTION-312
    Strongest counterargument: The disjoint-id finding of 2026-06-05 posed a question — are these two record sets the same entities? — and the merge answered it not by measuring but by minting ids, which makes the answer "yes" true by construction. That is the textbook false-match: identity asserted, not inferred, in exactly the near-zero-overlap regime where ER theory says false matches are most likely and most damaging. Because a committed id space is load-bearing and hard to reverse, the fiat may have locked in an identity the data actively contradict.
    What would need to be true for C2A2 to be safe: A real co-reference between each curated community and its directory record, established by a linkage measurement, not by the act of assigning the id.
    How to test: Run the REVISE-089 record-linkage experiment on attributes other than the freshly-minted id; if overlap stays near the signal floor, the identity was manufactured and should be downgraded to an asserted association.

  Recommendation: CHALLENGED
