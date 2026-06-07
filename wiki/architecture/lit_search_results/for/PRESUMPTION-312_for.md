SEARCH-FOR-PRESUMPTION-312:
  Date searched: 2026-06-07
  Original item: PRESUMPTION-312
  Original statement: [inferred] Assigning shared CC-xxx ids presumes that sharing an id key constitutes genuine entity identity rather than asserting a link by fiat; the merge may have manufactured the identity that 2026-06-05 found missing (disjoint id spaces) rather than discovering it.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-312
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated presumption that minting a shared key establishes (not merely asserts) entity identity.
      15a: Searched for support for key-assignment as a legitimate way to establish entity identity / referential linkage.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Surrogate-key practice (Kimball dimensional modeling). — Systems legitimately assign surrogate keys to stand in for entity identity where no natural key exists; in a single authoritative system the assigned id IS the operative identity. Weak support that an assigned key can constitute working identity.
    2. Deterministic record linkage (Christen 2012). — When a curator has external knowledge that records co-refer, asserting the link deterministically (rather than probabilistically) is a recognized and valid method. Supports key-by-assertion WHEN identity is independently known.
    3. MDM golden-record id minting. — A unified id is routinely minted to represent a resolved entity across sources; the id expresses an identity decision. Supports that id-assignment is the normal vehicle for an established identity.

  Strength of support: Weak-Moderate

  Summary: There is real but conditional support: assigning an id is the standard vehicle for entity identity, and deterministic (assertion-based) linkage is legitimate WHEN the curator independently knows the records co-refer. In a single authoritative directory, an assigned id can function as the operative identity. The support is entirely conditional on identity being established before (or independently of) the id assignment.

  Caveats: Every precedent treats id-assignment as the EXPRESSION of an identity decision, not its EVIDENCE. None licenses minting a shared id as a way to CREATE identity that was empirically absent — and the 2026-06-05 finding (0 id / 3 name / 5 host overlap) is exactly the absent-evidence case. So the FOR case supports "assign an id once identity is established," leaving unsupported the specific move the presumption flags: treating the assignment itself as having discovered the identity.

  Recommendation: PARTIALLY-SUPPORTED
