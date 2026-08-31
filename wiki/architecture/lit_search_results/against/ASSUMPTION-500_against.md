SEARCH-AGAINST-ASSUMPTION-500:
  Date searched: 2026-08-29
  Original item: ASSUMPTION-500
  Original statement: PREMISE-001..043 are missing while 40 of those IDs remain actively referenced; the consistency check ran against only 78 of 118 premises.

  SCOPE NOTE (load-bearing, applies to every item in this run):
    Two limbs. (1) The internal-empirical claim about this repository's file state: NOT-SEARCHED,
    literature cannot adjudicate it. (2) The generalizable question named by the item's own
    "Search targets" line: searched here. The item is NOT retagged [MISROUTED-INTERNAL-EMPIRICAL];
    REVISE-408's authorisation request to Tom stands untouched.

  INDEPENDENCE CAVEAT: 15a and 15b ran in the same process this run — a stronger coupling than the
    read-channel coupling the standing 15a/15b correlation discount was written for. Where this
    search agrees with 15a, that agreement is worth LESS than usual and 15c discounts it.
  EVIDENCE GRADE: snippet-level search results only. Zero full-text reads, zero abstract-level reads.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-500
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: original extraction/inference (2026-07-21 cohort)
      15b: Searched for challenging literature on the generalizable limb only (2026-08-29); internal-empirical limb NOT-SEARCHED
    Current status: NO-CHALLENGE-FOUND

  Challenging evidence found: No

  Sources:
    1. No source was found arguing that live references to absent register records are acceptable, nor that partial-register consistency checking is sound. Searches covered referential integrity, dangling-reference tolerance, and ledger-integrity practice.
    2. Evolveum, "Relaxed Referential Integrity" is the nearest thing to a challenge and is not one: it permits dangling references only under an EXPLICIT declared policy, which is the opposite of silent tolerance and would itself require a decision C2A2 has not made.
    3. USPTO 10,289,706 records that unrepairable dangling references are to be LOGGED for later repair rather than left implicit — again a requirement, not a permission.

  Strength of challenge: None

  Summary: No challenging evidence found. This is one of the rare items where the disconfirmatory direction returns empty because the claim is a definitional consequence rather than a hypothesis: a register missing records that other records cite is in a dangling state by definition, and a consistency check over 78 of 118 entries has not checked 40 of them. The only near-challenge, relaxed referential integrity, converts into an additional requirement. Note for 15c: an empty result here is NOT evidence of strength in the usual sense — there is nothing to disagree with.

  Specific risks: Every downstream consistency check, including 15c's own pre-INCORPORATE check on this run, silently runs against a partial register. New premises can therefore be minted that contradict a missing one. This run is itself an instance: the consistency check performed below could not see PREMISE-001..043.

  Mitigations available: Declare relaxed integrity explicitly (with the dangling set enumerated), or reconstruct. Until either, every consistency check should carry a stated denominator — an inexpensive change that makes the defect visible in the output of every run that depends on it.

STEELMAN:
  Item: ASSUMPTION-500
  Strongest counterargument: No steelman is available; the disconfirmatory direction found nothing. The strongest thing 15b can say is procedural: this is REVISE-242, filed 2026-07-21 and open for 39 days, and re-searching it produces no new information. The finding worth recording is the duration, not the literature.
  What would need to be true for C2A2 to be safe: n/a — no challenge found.
  How to test: Recount validated_premises.md by ID; check dated backups for PREMISE-001..043 (this is PRESUMPTION-519's test and should be run once, for both).

  Recommendation: NO-CHALLENGE-FOUND
