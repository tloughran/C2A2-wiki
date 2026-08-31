SEARCH-FOR-ASSUMPTION-500:
  Date searched: 2026-08-29
  Original item: ASSUMPTION-500
  Original statement: PREMISE-001..043 are missing from validated_premises.md while 40 of those IDs remain actively referenced; the consistency check ran against only 78 of 118 premises (REVISE-242).
  Generalizable limb searched: Is a register with live references to absent records a recognised integrity fault with established detection methods?

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
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-500
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from 2026-07-21 evening sync reporting 15c's verification addendum
      15a: Searched for supporting literature on the generalizable limb only (2026-08-29); internal-empirical limb NOT-SEARCHED
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Webocreation, "Referential Integrity." — a dangling tuple is a record whose corresponding related record does not exist; referential integrity requires that a parent exist before its child and that a parent not be deleted while children remain. The register violates the second condition by construction.
    2. USPTO 10,289,706 / 10,885,000. "Repairing corrupted references." — detection programs collect the reference location, the object IDs involved, and the mapping information; where a dangling reference cannot be repaired on detection it is RECORDED TO A FILE for later repair. Establishes both that automated detection is standard and that unrepairable danglers are expected to be logged rather than tolerated silently.
    3. Evolveum, "Relaxed Referential Integrity." — documents the deliberate-tolerance variant, in which dangling references are permitted but must be explicitly accounted for. Relevant as the only legitimate form of the current state, and it requires a declared policy the register does not have.

  Strength of support: Strong

  Summary: Forty live references to forty-three absent records is a dangling-reference condition in the textbook sense, and the literature is unambiguous that this is a fault requiring either repair or an explicit relaxed-integrity policy. Automated detection of exactly this condition is old and well-specified. The one genuinely informative addition from the literature is the middle option: relaxed referential integrity is a legitimate design choice, but only when declared — silent tolerance is not one of the two acceptable states.

  Caveats: Two sources are patents (methods, not results). The finding is generic to registers; it carries no information about how the C2A2 records were lost or whether they are recoverable — that is PRESUMPTION-519's question and is answered differently there.

  Recommendation: SUPPORTED
