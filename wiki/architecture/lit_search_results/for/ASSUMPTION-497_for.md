SEARCH-FOR-ASSUMPTION-497:
  Date searched: 2026-08-29
  Original item: ASSUMPTION-497
  Original statement: Two 07-19 proposals vanished with no recorded disposition and no surviving file; likeliest reading is deliberate withholding, but incidental loss in the bulk pending->approved move cannot be excluded from the artifacts alone.
  Generalizable limb searched: Can an artifact set that lacks omission detection distinguish a deliberately withheld record from an incidentally lost one?

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
    Original item: ASSUMPTION-497
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from 2026-07-21 deferred-action monitor, exact quotes
      15a: Searched for supporting literature on the generalizable limb only (2026-08-29); internal-empirical limb NOT-SEARCHED
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Aura Docs, 2026. "The Immutable Audit Trail." — defines omission as the case where an entry is prevented from being recorded at all, and states that detection requires an INDEPENDENT tip: a peer whose log is shorter than its peers' detects the gap on sync. Where one party controls both the log and the committer, a single entry can be silenced undetectably.
    2. USPTO 7,908,160. "System and method for producing audit trails." — the method generates an ANOMALY audit event when expected events associated with declared state transitions are not retrieved. The existence of the patent establishes that detecting missing-by-omission requires a pre-declared expected-event set; without one, absence is simply absent.
    3. Datamondial, 2026. "Audit Trail Loss During Software Migration." — extraction from legacy systems without explicit metadata focus yields immediately corrupt or incomplete logs. Establishes bulk state transitions as a recognised high-risk moment for audit-trail loss, i.e. the item's alternative hypothesis is a documented mechanism, not a courtesy hedge.

  Strength of support: Moderate-Strong

  Summary: The literature converges on the item's own epistemic hedge. Distinguishing omission from loss is not a matter of looking harder at the surviving artifacts; it requires an independently maintained expectation about what should be there — a peer log, a declared state-transition set, a pre-move manifest. Where the same actor produces both the records and the move, the two hypotheses are formally indistinguishable from the artifacts. Bulk migrations are independently documented as a high-loss operation, so the 'incidental loss' limb is not the weaker hypothesis on priors.

  Caveats: Two of three sources are practitioner or patent literature. The patent describes a method, not a validated result. The finding is about what the artifact set can and cannot settle; it says nothing about which hypothesis is true here.

  Recommendation: SUPPORTED
