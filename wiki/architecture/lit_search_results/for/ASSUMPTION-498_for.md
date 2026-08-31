SEARCH-FOR-ASSUMPTION-498:
  Date searched: 2026-08-29
  Original item: ASSUMPTION-498
  Original statement: The generate_review_page.py position-ID defect is correctness-critical, not hypothetical — decision-button IDs are offset from card IDs, so a decision registered against one card can be recorded against a different proposal.
  Generalizable limb searched: Are position/index-based bindings in generated UIs a documented source of correctness (not merely cosmetic) defects?

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
    Original item: ASSUMPTION-498
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from 2026-07-21 deferred-action monitor, exact quote
      15a: Searched for supporting literature on the generalizable limb only (2026-08-29); internal-empirical limb NOT-SEARCHED
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Wikipedia, "Off-by-one error." — standard definition: a logic error where a value differs from its intended value by one, commonly from zero-based indexing and inclusive/exclusive range confusion. Establishes the defect class as canonical rather than exotic.
    2. Medium (techsolutionsx), 2026. "Unpacking the consequences of using index as a key in React." — index keys cause the framework to reuse DOM nodes for the WRONG DATA when items are reordered, inserted, or deleted, producing stale input values. This is the exact failure shape claimed: a control bound by position acting on a different record than the one displayed.
    3. Vue.js Guide, "List Rendering." — the default in-place patch strategy makes each element reflect what should be rendered at that INDEX; a unique key is required for the framework to track item identity. Confirms that position-based binding is the default and that correctness under mutation requires opting out of it.

  Strength of support: Strong

  Summary: This is textbook. Position-based binding in generated list UIs is a documented correctness defect class, not a cosmetic one, and the specific consequence documented in the framework literature — a control acting on a different record than the one rendered beside it — is precisely the mechanism the item alleges. The literature treats index-as-key as an anti-pattern for this reason. The claim's generalizable limb is as well grounded as claims in this pipeline get.

  Caveats: Sources are documentation and practitioner writing rather than primary research; the defect class is however uncontroversial. The literature concerns framework-mediated virtual-DOM reconciliation; a hand-rolled Python HTML generator is a simpler case, which if anything strengthens the transfer. Whether THIS generator has the defect is an in-house diff, not a literature question.

  Recommendation: SUPPORTED
