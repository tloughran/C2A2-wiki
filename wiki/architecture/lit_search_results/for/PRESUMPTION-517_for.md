SEARCH-FOR-PRESUMPTION-517:
  Date searched: 2026-08-29
  Original item: PRESUMPTION-517
  Original statement: [inferred] The integrity flag presumes the 07-20 review page + live URLs are a sufficient recovery source for the two lost proposals — but the same run escalates the position-ID bug that makes that page's card/button wiring unreliable. Recovery source and corrupted instrument are the same artifact.
  Generalizable limb searched: Does forensic/recovery practice permit an artifact whose integrity is in question to serve as its own recovery reference?

  SCOPE NOTE (load-bearing, applies to every item in this run):
    This item was triaged on 2026-07-25 as INTERNAL-EMPIRICAL and declared out of 15a/15b scope.
    That triage is here treated as HALF RIGHT. Each item has TWO limbs: (1) an internal-empirical
    claim about this repository's own file state, which literature cannot adjudicate and which is
    NOT-SEARCHED here; and (2) a generalizable question, named by the item's own "Search targets"
    line, which is squarely searchable. Only limb (2) was searched. The item is NOT retagged
    [MISROUTED-INTERNAL-EMPIRICAL]; REVISE-408's authorisation request to Tom stands untouched.
    Searching limb (2) does not pre-empt it.

  INDEPENDENCE CAVEAT (per PREMISE-096 and the standing 15a/15b correlation discount):
    15a and 15b were executed by the same process in this run, a stronger coupling than the
    read-channel coupling the standing discount was written for. Agreement between the two
    directions in this run therefore carries LESS evidential weight than usual, not more, and
    is discounted accordingly in every 15c disposition below.
  EVIDENCE GRADE: snippet-level search results only. Zero full-text reads, zero abstract-level reads.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-517
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: surfaced by reading the monitor's recovery claim against its own position-ID escalation
      15a: Searched for supporting literature on the generalizable limb only (2026-08-29); internal-empirical limb NOT-SEARCHED
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Hive Security, 2026. "DFIR 2026: Memory Forensics, Windows Artifacts, and Incident Response." — recovery requires validating system integrity against KNOWN-GOOD BASELINES or reinstalling from scratch, rather than restoring and moving forward. The compromised artifact is explicitly disqualified as its own reference.
    2. Kusari, "Integrity Verification." — no single verification mechanism provides complete protection; controls must be layered so a failure in one does not compromise the whole, and multiple INDEPENDENT verification layers are what localise where a compromise occurred.
    3. Cloudsmith, "OWASP CI/CD Part 9: Improper Artifact Integrity Validation." — treats validating an artifact against metadata carried by that same artifact as the named anti-pattern.

  Strength of support: Strong

  Summary: The presumption the item surfaces is one the forensic and supply-chain literature rejects explicitly. Recovery references must be independent of the artifact under suspicion; the standard remedy is a known-good baseline or a disjoint evidence source. This is also NOT a novel finding for C2A2 — it restates ACTIVE PREMISE-096 ('No self-produced artifact may certify itself... require that the corroborating layer draw on a genuinely disjoint evidence source, or independent is nominal only'). The literature adds the forensic framing but not a new premise.

  Caveats: Practitioner sources. Note explicitly: this item's generalizable limb is already covered by PREMISE-096, so 15a's finding here is a CONFIRMING INSTANCE, not new ground. See 15c's disposition — no new premise should be minted.

  Recommendation: SUPPORTED
