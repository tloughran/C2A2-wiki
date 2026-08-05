SEARCH-AGAINST-PRESUMPTION-655:
  Date searched: 2026-08-04
  Original item: PRESUMPTION-655
  Original statement: That a verification mark is independent of the tool that produced
    it — a retrieval method having been caught producing false affirmatives, with no
    field recording which method was used and no enumerable set of affected marks.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-655
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-08-03 discovery that a retrieval method produced false
        affirmatives, with no provenance field and no enumerable affected set
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Hsiao, T.-K. & Schneider, J., 2021. "Continued use of retracted papers: Temporal
       trends in citations and (lack of) awareness of retractions shown in citation
       contexts in biomedicine." Quantitative Science Studies, 2(4), 1144. — Of 13,252
       post-retraction citation contexts, only 722 (5.4%) acknowledged the retraction;
       retraction did not change how the retracted papers were cited. Withdrawal of
       support does not propagate to marks already issued.
    2. (2024). "Why do some retracted articles continue to get cited?" Scientometrics,
       doi:10.1007/s11192-024-05147-4. — Finds ~90% of retracted articles continue to
       receive citations post-retraction, and that continuing citers are
       disproportionately those least positioned to know the status.
    3. Teixeira da Silva, J.A., 2025. "The Citation of Retracted Papers and Impact on the
       Integrity of the Scientific Biomedical Literature." Learned Publishing. —
       Argues the integrity harm is a function of the un-annotated surviving marks, not
       of the original error.
    4. Dixit, H.D. et al., 2021. "Silent Data Corruptions at Scale." arXiv:2102.11245
       (Meta). — Directly on point for the enumerability problem: silent data corruptions
       are not captured by error-reporting mechanisms and are therefore not traceable at
       the hardware level; consequences propagate across the stack and take months to
       attribute. Where the producing mechanism records nothing, the affected set cannot
       be reconstructed after the fact.
    5. Huang, P. et al., 2017. "Gray Failure: The Achilles' Heel of Cloud-Scale Systems."
       HotOS '17. — Differential observability: a component reporting healthy while
       producing wrong output is the canonical case, and it is undetectable from the
       component's own affirmations.
    6. Cook, R.I., Allspaw, J. et al., 2017. "STELLA Report." SNAFUcatchers. — A mark
       whose generating conditions are not recorded is precisely the interaction-level
       debt the report describes: it cannot be assessed by examining the mark.

  Strength of challenge: Strong

  Summary: The retraction literature is an unusually clean natural experiment for this
    presumption, and it goes hard against it. Science operates the most developed
    withdrawal-propagation machinery in existence — indexed retraction notices, publisher
    alerts, dedicated databases — and still under six percent of downstream uses
    acknowledge the withdrawal, with roughly ninety percent of retracted work continuing
    to accrue citations. A verification mark in a wiki has none of that machinery. The
    silent-data-corruption work supplies the second half: when the producing mechanism
    records nothing about itself, the affected set is not merely unknown but
    unreconstructable, and attribution takes months even with substantial engineering
    effort. Together these say that the mark and the method are not independent, that
    discovering the method was faulty does not retroactively neutralise the marks it
    produced, and that without a provenance field there is no path from "the method was
    wrong" to "these specific claims are now unsupported."

  Specific risks: Every verification mark issued by the faulty retrieval method is now a
    false affirmative that reads identically to a true one, and no query can separate them.
    Downstream agents will treat those marks as settled and will not re-check. Because
    C2A2's verification marks are consumed by other agents rather than by humans reading
    citation contexts, propagation is likely faster and acknowledgement lower than the
    5.4% baseline. The absence of an enumerable affected set means the only sound
    responses are (a) invalidate all marks of that type, which is expensive and destroys
    good work, or (b) leave them standing, which is what will actually happen by default.
    The system will therefore carry an unbounded number of unsound "verified" claims
    indefinitely, and this compounds with PRESUMPTION-660 (fallback substitutions that did
    not reach the artifact carrying the PASS) and PRESUMPTION-648 (a suppressed validator
    still emitting PASS).

  Mitigations available: (1) Add a provenance field now — method, version, timestamp,
    and any degradations in effect — to every verification mark going forward. This is
    the single change that makes future recalls possible and costs almost nothing.
    (2) Date-bound the recall: even without a method field, marks issued between the
    faulty method's introduction and its discovery form a conservative superset; flag that
    interval's marks as UNCONFIRMED rather than leaving them as VERIFIED. Dates are
    almost certainly recoverable from file history even though methods are not.
    (3) Annotate in place rather than correcting at source — write the withdrawal onto
    each affected mark, since the retraction literature shows source-side notices do not
    reach consumers. (4) Introduce a distinct third value: VERIFIED / UNVERIFIED /
    VERIFICATION-WITHDRAWN, so that withdrawal is representable at all. (5) Sample-audit:
    re-verify a random sample of the suspect cohort by an independent method and use the
    observed false-affirmative rate to decide whether wholesale invalidation is warranted.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-655
    Strongest counterargument: A verification mark asserts a fact about the world, and
      facts do not become false because the route to them was unreliable — a faulty
      retrieval method that produces false affirmatives at some rate still produces true
      affirmatives at the complementary rate, and most marks are probably fine. Wholesale
      invalidation on the basis of a known-faulty tool discards a large body of correct
      work to remove a small body of incorrect work, which is a poor trade when the
      marks are cheap to spot-check on demand at the point of use. The retraction analogy
      overstates the harm: retracted papers are cited by strangers across a global
      literature, whereas C2A2's marks are consumed inside one system by agents that can
      be instructed to re-check.
    What would need to be true for C2A2 to be safe: (a) The false-affirmative rate of the
      faulty method is low and measurable. (b) Consumers of a mark can and do re-check
      cheaply at point of use rather than treating the mark as terminal. (c) The window in
      which the faulty method was active is recoverable, even if the method field is not.
      (d) No high-consequence downstream decision depends on a single unaudited mark.
    How to test: Draw a random sample of 20 existing verification marks and independently
      re-verify each by a different method. The observed disagreement rate is the
      false-affirmative rate and settles the question empirically for a few minutes of
      work. Separately, check whether mark timestamps exist in file history — if they do,
      the "no enumerable set" claim is weaker than stated and a date-bounded recall is
      immediately available.

  Search scope: Adequate. Concepts searched: provenance metadata for verification claims;
    retraction propagation and post-retraction citation; annotation-in-place practice;
    silent data corruption and non-enumerable affected sets; differential observability.
