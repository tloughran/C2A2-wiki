SEARCH-FOR-ASSUMPTION-278:
  Date searched: 2026-06-07
  Original item: ASSUMPTION-278
  Original statement: Merging the 156 curated communities into the Cards directory under their own CC-xxx ids (graph becomes a literal id-subset of the cards) is the correct way to make the directory⊇graph relationship true and to unblock the deferred cross-navigation hand-off on the shared key.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-278
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the stated decision that assigning shared CC-xxx ids makes directory⊇graph true and unblocks the hand-off.
      15a: Searched for support for shared-key / surrogate-key subset modeling and key-based data integration.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Record linkage / data integration (Christen, "Data Matching," 2012; Wikipedia "Record linkage"). — Assigning a shared key so one record set becomes addressable as a subset of a superset directory is a standard integration mechanism; once a reliable key exists, the directory⊇subset hand-off is trivial. Supports the mechanics.
    2. Surrogate-key / dimensional modeling practice (Kimball). — Systems routinely mint surrogate keys to make cross-table joins deterministic where no natural key exists; assigning CC-xxx ids is the recognized way to create a stable join column. Supports "shared key unblocks cross-navigation."
    3. Master Data Management golden-record practice. — MDM creates a unified id space across sources precisely to make superset/subset membership and cross-references computable; the move is well-precedented.

  Strength of support: Moderate

  Summary: As a piece of data-engineering mechanics, assigning shared CC-xxx ids to the curated set is a recognized and effective way to create a deterministic join column and make the directory a literal superset of the graph — surrogate keys, record-linkage keys, and MDM golden ids all do exactly this. The technique reliably unblocks the deferred cross-navigation hand-off. The support is for the MECHANISM, conditional on the records genuinely denoting the same entities.

  Caveats: All three precedents assign a shared id only AFTER (or in order to express) an established same-entity relation; they support "if the records are the same entities, assigning a shared key is the correct way to make the subset relation addressable." They do NOT establish that minting a key MAKES the directory⊇graph relation true where the underlying identity is unestablished — that is the identity question contested by PRESUMPTION-312 and unresolved since the 2026-06-05 disjoint-id finding (0 id / 3 name / 5 host).

  Recommendation: PARTIALLY-SUPPORTED
