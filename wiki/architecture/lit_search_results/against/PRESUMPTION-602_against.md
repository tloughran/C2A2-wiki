SEARCH-AGAINST-PRESUMPTION-602:
  Date searched: 2026-08-01
  Original item: PRESUMPTION-602
  Original statement: [as queued] The content/mechanism split presumes content and authorship provenance are separable; but tradition assignment IS the unit of analysis, so attributing Machado to Stump is an error at the operating level, not a metadata blemish, and FINDING-055 inherits it.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-602
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from the content/mechanism framing and the metadata-edit remedy
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. COPE / Elsevier / Taylor & Francis / Wolters Kluwer correction policies (2024-2025); UKRIO, "Correcting the scholarly record" FAQ (2023). — The scholarly record's own settled taxonomy places authorship error in the CORRECTION (erratum/corrigendum) tier explicitly because it does not impugn the findings; retraction is reserved for cases where the content cannot be trusted. This is a direct, standards-level contradiction of the item's claim that an attribution error is necessarily an error "at the level the system operates on."
    2. van der Vet & Nijveen, 2016, Research Integrity and Peer Review 1:3. — The same study 15a would reach for reports the finding that cuts the other way: INDIRECT citations do not contribute to propagation of the flawed result. Propagation is bounded to direct consumers. Applied here, that bounds the blast radius to artifacts that directly read the ingest — a small, enumerable set — rather than to the corpus.
    3. Provenance-in-databases literature (where-/why-/how-provenance; A Core Calculus for Provenance, arXiv 1310.6299). — This work is built on the premise that provenance is a SEPARABLE annotation layer over data; the entire field would be incoherent if source and content were inseparable in general. Separability is the default in the formalism; the item asserts the exception without establishing it.
    4. Knowledge-graph provenance work (arXiv 2606.15246; nanopublications, IJDL 2025). — Provenance is modelled as statements ABOUT statements (reification / named graphs). The architecture deliberately keeps the assertion and its attribution as distinct objects so attribution can be revised without re-asserting content. This is the opposite of the item's structural claim.

  Strength of challenge: Strong

  Summary: The item makes a general claim (content and attribution are inseparable when the schema indexes by source) and a local claim (this particular ingest is broken at the operating level). The general claim is contradicted by the two literatures most directly on point: the scholarly correction taxonomy places authorship error in the correctable tier precisely because attribution and validity are separable, and database/KG provenance formalisms are built on treating provenance as a distinct annotation layer over content. The local claim survives better, but it is an empirical claim about C2A2's schema and its truth is settled by counting downstream artifacts that read tradition membership semantically — which the item names as its own settling quantity and which was not computed. The one supporting study also supplies a bound the item does not mention: indirect citations do not propagate the error, so the affected set is direct consumers only.

  Specific risks: If the item's general form were adopted, every attribution error in the corpus would become a content-level defect requiring re-derivation of downstream claims rather than a correctable annotation — a large and possibly unbounded remediation obligation minted from a case of n=1. The inverse risk is real too: if the item is wrong in general but right locally, treating it as a metadata fix leaves FINDING-055 asserting a cross-program claim over a mislabelled endpoint.

  Mitigations available: Yes. The correction taxonomy supplies a ready-made three-tier discipline — correction (attribution wrong, content stands), expression of concern (standing uncertain pending check), retraction (claim withdrawn) — and the discriminator between tiers is exactly the count the item already names. Adopting the tiering costs nothing and defers the general claim until the count exists.

  STEELMAN:
    Item: PRESUMPTION-602
    Strongest counterargument: Scholarship has confronted this exact question for decades and answered it against the item. An authorship error is a correction, not a retraction, because the warrant for a claim rests on its evidence, not on who is recorded as having said it; a system in which changing the author line invalidates the content has confused a filing decision with an epistemic one. C2A2's own architecture reinforces this: the tradition wikis are organised as filing locations for positions, and the provenance protocol the network runs on explicitly models attribution as a separable annotation layer. The item elevates an internal schema convention — indexing by source — into a claim about the semantics of the assertion, without producing the one count that would show the convention is load-bearing. Meanwhile the only measured study of error propagation in a citation network reports that the spread is confined to direct citations, which makes the practical remedy an enumeration of direct consumers, not a re-derivation.
    What would need to be true for C2A2 to be safe: the general claim must be restricted to the local case; the direct-consumer set of the 07-31 ingest must be enumerated and each member checked; FINDING-055 must be re-examined on its own evidence rather than voided by inheritance.
    How to test: Take the existing corpus and count, over all cross-tradition artifacts, how many state a claim of the form "tradition T holds P" (semantic reading) versus how many merely retrieve P from T's folder (filing reading). Corpus-scoped, two-digit-or-larger denominator, and decisive between the item's general claim and this challenge.

  Recommendation: PARTIALLY-CHALLENGED
