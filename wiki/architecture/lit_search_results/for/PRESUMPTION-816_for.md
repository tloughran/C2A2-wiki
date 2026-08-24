SEARCH-FOR-PRESUMPTION-816:
  Date searched: 2026-08-16
  Original item: PRESUMPTION-816
  Original statement: [inferred] That the reviewer's unit of work is the pair, so corpus-level findings
    have no slot, no budget and no count.
  Risk if wrong: Medium
  Search question (as queued): Sampling versus census in quality audit; unit-of-analysis effects on
    inspection yield; Goodhart effects from throughput metrics in review work.

  POLARITY NOTE — WHAT WAS ACTUALLY SEARCHED FOR. The item is worded as the DEFECTIVE arrangement. The
  proposition searched FOR is the CORRECTIVE CONVERSE, in four clauses:
    (C1) THE UNIT OF INSPECTION DETERMINES THE FAULT CLASS THAT CAN BE DETECTED. An inspection regime
         whose only unit is the individual item is structurally capable of finding item-level defects
         and structurally incapable of finding population-level ones — not because it is done badly but
         because the population-level property does not exist at the item level.
    (C2) THE DOMINANT FAULT CLASS IS THE ONE SUCH A REGIME CANNOT SEE. The quality tradition's central
         empirical claim is that the great majority of variation belongs to the system rather than to
         the individual item or worker, and that system-level causes are visible only in the aggregate.
    (C3) MATURE AUDIT PRACTICE IS BUILT AROUND A POPULATION-LEVEL CONCLUSION BY DESIGN — it samples
         deliberately rather than examining everything, and it requires the auditor to state how
         findings extrapolate to the population — so "the corpus-level finding" is not an unbudgeted
         extra in that discipline, it is the deliverable.
    (C4) A THROUGHPUT COUNT OVER ITEMS IS A GOODHART-EXPOSED METRIC in exactly this setting: once the
         reviewed-items-per-period figure is what is scheduled, budgeted and counted, corpus-level work
         competes against a measured quantity while being itself unmeasured, and loses by construction.
  "SUPPORTED" below means 14b's diagnosis is well grounded, and is equivalently evidence AGAINST the
  arrangement as described.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-816
    Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: the unit of work was never
      chosen, it was inherited from the review tool's page layout)
    Transform at each step:
      14b: Separated the day's outputs into pair-level and corpus-level and found only one kind is
        scheduled, budgeted or counted.
      15a: Searched for supporting literature on the corrective proposition; register check first.
    Current status: SUPPORTED

  REGISTER CHECK (performed BEFORE writing this file):
    Grepped `validated_premises.md` for: unit of analysis, unit of work, per-pair, pair-level,
    corpus-level, sampling, sample, audit, Goodhart, throughput, inspection, coverage, denominator,
    census, defect class.
    Found and read in full:
      - **PREMISE-130** (ACTIVE) — **the closest neighbour and the register's existing statement of the
        unit-of-analysis principle.** "RECURRENCE RECLASSIFIES. When the same component fails a third
        time in a third distinct signature, **the correct unit of analysis is a DEFECT CLASS in that
        component, not three independent bugs**; the empirical basis is that prior fault count is the
        dominant predictor of future faults and that faults cluster densely in a small minority of
        modules." That is 816's clause (C1) in the incident setting. Its SCOPE GUARD is load-bearing and
        transfers: 130 licenses the RECLASSIFICATION only, not the implied remedy.
      - **PREMISE-150** (2026-08-10, ACTIVE) — "A batch of defects that a detector failed to catch
        **bounds THE DETECTOR'S COVERAGE, not merely that batch.** A high adequacy score and a confirmed
        missed-defect class co-occur mechanistically and are not in tension; the score is computed over
        what the detector can see." This is a corpus-level finding-type already validated, and it is
        precisely the kind of finding 816 says has no slot.
      - **PREMISE-168** (2026-08-15, ACTIVE, Moderate) — a yield figure without its denominator is a
        statement about the PRODUCER, not about the space; the denominator is a chosen frame whose
        provenance must be stated; **the percentage is barred and the bare numerator is barred**, and
        its own DECLARED CONSTRAINT records that "no instrument was found that satisfies both — the
        surviving practice is the stratified statement, which is not a metric and cannot be trended."
        That constraint bears directly on 816's "no count": the register has already established that
        the obvious corpus-level count is not available.
      - **PREMISE-136** (ACTIVE) — the achievable denominator of a settling quantity is fixed by its
        DECLARED SCOPE, and **every settling quantity must declare its scope — run / cohort / corpus —
        at the point it is written**. Clause (2) records that rescoping to cohort or corpus is a
        legitimate and usually the cheapest route to a usable denominator. This is the register's
        nearest thing to a corpus-level SLOT, and it is a declaration rule rather than a schedule.
      - **PREMISE-109** (ACTIVE) — a summarizing agent is a view over its own READ SET, not over the
        system; a summary can be individually faithful to every source it read and collectively false
        about the system. Its INSTRUMENTATION CONSTRAINT explicitly rejects a read-set coverage
        percentage, on the ground that coverage "rises when a summarizer reads more marginal artifacts
        without reading the decisive one."
      - **PREMISE-095** (ACTIVE) — usefulness must not be equated with productivity (Goodhart/Campbell);
        the test must be ASYMMETRIC.
      - **PREMISE-113 / PREMISE-158 / PREMISE-162** — the detector family: a detector's findings are
        evidence about the detector until precision is measured; error profiles are two-sided; a catch
        count produced by a run auditing its own instrument has no denominator.
      - **PREMISE-001/002** (ACTIVE) — human review capacity is the binding constraint on throughput,
        which is why the budgeting question in 816 is consequential rather than cosmetic.
    CONCLUSION OF THE CHECK: **SUBSTANTIAL OVERLAP ON THE PRINCIPLE; A GENUINE AND NARROW GAP ON THE
    ITEM'S ACTUAL CLAIM. NO NOVELTY-FLAG on the principle.** Nine ACTIVE premises bear on this. The
    register already holds (a) that the unit of analysis determines the finding class (PREMISE-130), (b)
    two worked corpus-level finding types (PREMISE-150, PREMISE-109), and (c) a declaration rule that
    requires scope to be stated (PREMISE-136). What NO premise addresses, and what 816 is actually
    about, is the three-part institutional claim:
      (R1) **NO SLOT** — nothing in the register or the review tooling creates a place where a
           corpus-level finding is filed as a first-class object rather than as a note attached to some
           pair.
      (R2) **NO BUDGET** — no premise allocates reviewer time to corpus-level work; PREMISE-001 says
           review capacity is the binding constraint but says nothing about how it is divided.
      (R3) **NO COUNT** — and PREMISE-168 has just established that the natural count is barred, so the
           absence is not an oversight that a metric would fix. This is the sharpest part of the item
           and the part the register makes HARDER rather than easier to remedy.
    DECLARED LIMITATION: string grep, measured at ~56% recall (ASSUMPTION-1052). The list above is a
    **LOWER BOUND** and the true overlap is likely larger, which argues for a narrow disposition.

  Supporting evidence found: Yes

  Sources:
    1. Deming, W.E. — Point 3 of the Fourteen Points, *Out of the Crisis* (MIT CAES, 1986): "**Cease
       dependence on inspection to achieve quality. Eliminate the need for inspection on a mass basis by
       building quality into the product in the first place.**" — **The direct support for clause (C1),
       and the sharpest available statement of why an item-level unit is the wrong instrument.** The
       accompanying argument, as it circulates in the Deming Institute's own materials, is "**inspection
       is too late: the quality, good or bad, is already in the product**." The item-by-item regime is
       described as sifting output to remove defectives, which by construction produces a verdict per
       item and no information about the process that produced them. The clarification that matters and
       that must travel with the citation: **the key word is "dependence," not "inspection"** — Deming
       did not call for eliminating inspection, and explicitly retains "necessary sample inspection" to
       monitor product and process. That is exactly 816's claim: the defect is that the pair is the ONLY
       unit, not that the pair is a unit.
       [SNIPPET LEVEL — the Deming Institute's Fourteen Points page and quotation page, and several
       independent expositions (Baudin; Curious Cat/Hunter; Quality Assurance Solutions), were located
       and read at summary level this run. **"Out of the Crisis" was NOT opened**; the Point 3 wording is
       standard and is reproduced identically across the located sources, but no page citation should be
       given. Partly CANONICAL as well as retrieved.]
    2. Deming / Shewhart — the common-cause versus special-cause distinction, and the "94% belongs to
       the system" estimate. — **The direct support for clause (C2), and the reason (C1) matters rather
       than being a technicality.** Special-cause variation is attributable to a specific assignable
       event and is in principle findable at the item; common-cause variation is the natural behaviour
       of the system, is predictable only within limits, and **is not visible in any single item at
       all** — it is a property of the distribution and is detectable only by looking at the population
       over time. Deming's estimate, given in *Out of the Crisis* and revised upward later, is that
       **roughly 94% of causes are common-cause and are management's — i.e. the system's —
       responsibility**, with ~6% special. Transposed to 816: if the split is anywhere near that in a
       review corpus, a regime whose only unit is the pair is aimed at the small share and is blind to
       the large one. **This is the strongest single argument available for the item and it is an
       argument about detectability, not about diligence.**
       [SNIPPET LEVEL, with a stated reliability caution. The 94/6 figure was located this run in the
       Deming Institute's "Knowledge of Variation" material and in several independent secondary
       expositions, all attributing it to *Out of the Crisis*; **the primary was not opened.** The figure
       is widely repeated and widely criticised as an estimate rather than a measurement — Deming
       himself is reported to have changed it — so it should be used as an order-of-magnitude claim
       about which class dominates, NEVER as a parameter. The QUALITATIVE claim (common causes are
       invisible at the item level) is robust and does not depend on the number.]
    3. ISO 19011:2018, *Guidelines for auditing management systems*, especially the audit-evidence and
       findings clauses (6.4.8 on findings; the sampling guidance). — **The support for clause (C3), and
       the demonstration that a discipline built for this problem organises itself the opposite way from
       C2A2's review.** Two features are decisive. First, **audit evidence is to be based on APPROPRIATE
       SAMPLING rather than 100% examination**, with sampling either judgement-based or statistical.
       Second — and this is the clause 816 needs — **the auditor must document the sampling methodology,
       justify the sample size, and explain HOW FINDINGS EXTRAPOLATE TO THE LARGER POPULATION.** In
       other words the standard treats the population-level statement as the OUTPUT of the audit and the
       item examinations as the means; the corpus-level finding is not an unbudgeted extra, it is the
       deliverable, and the item-level verdicts exist to support it. The standard also makes audit scope
       and depth RISK-BASED, focused on "areas where previous nonconformities were identified, any new
       products or processes, and anything that changed significantly" — a targeting rule that is
       itself a corpus-level judgement made before any item is opened.
       [SNIPPET LEVEL — the standard itself is paywalled and was NOT obtained. Its content is reported
       here from multiple independent secondary expositions located this run (SimplerQMS; GoAudits;
       Certainty Software; Supervizor; Medical Device Academy; Process Street). The clause number 6.4.8
       and the sampling/extrapolation requirements are consistently reported across them. **Do not quote
       ISO 19011 verbatim onward without the standard in hand.** STANDARDS DOCUMENT, cited as documented
       professional practice.]
    4. Goodhart's law as applied to review throughput; Campbell (1979); Strathern (1997) — **the support
       for clause (C4)**, held in the register already as PREMISE-095. The specific mechanism 816
       exhibits is not the classic one (a metric being gamed) but its quieter form: **an unmeasured
       activity competing for a fixed budget against a measured one.** Corpus-level work has no count, so
       a day spent on it registers as a day of low output; pair-level work has a count, so it registers.
       No one need intend anything for the allocation to drift. The corroborating empirical shape comes
       from the code-review literature, where queue pressure is reported to produce approval without
       review ("LGTM"), and where reviewer effectiveness is reported to fall sharply with batch size —
       both being cases of a throughput measure displacing the activity it was meant to proxy.
       [MIXED. Goodhart/Campbell/Strathern: **CANONICAL — cited from established knowledge, NOT
       re-verified this run, and already register-cited via PREMISE-095, so not independent.** The
       code-review figures (effectiveness ~80-90% under 200 lines, below 50% over 1,000 lines; the
       ~400-line degradation threshold; a reported 65% rubber-stamp rate): **SNIPPET LEVEL AND WEAK
       PROVENANCE** — these circulate through practitioner blogs citing a SmartBear white paper and a
       Cisco case study at second or third hand; **the primary was NOT retrieved and the numbers must
       not be quoted onward as measurements.**]
    5. Inozemtseva, L. & Holmes, R. (2014), "Coverage Is Not Strongly Correlated with Test Suite
       Effectiveness," ICSE 2014. — Carried from the register (PREMISE-168's challenge line, where 15b
       records the primary PDF as verified) as the standing warning against the obvious fix. If 816's
       remedy is read as "add a corpus-level coverage percentage," this is the source that says the
       percentage would be a weak proxy that degrades further once it becomes a target.
       [CANONICAL / register-carried — NOT re-verified this run; the verification marker in
       `validated_premises.md` belongs to a prior 15b run, not to this one.]

  Strength of support: **Moderate-to-Strong.**
    (C1) and (C2) rest on a foundational and near-universally taught body of quality practice, though
    reported here from secondary sources and with the 94% figure explicitly downgraded to an
    order-of-magnitude claim. (C3) is a standards document read at second hand but consistently reported
    across six independent expositions, and the extrapolation requirement is the specific thing 816
    needs. (C4) is the weakest: the principle is canonical and register-held, but the empirical
    magnitudes located are practitioner-grade. Not graded Strong overall because **no source located this
    run addresses 816's actual claim** — that corpus-level findings lack a slot, a budget and a count —
    which is an institutional-design claim rather than a methodological one, and for which the search
    returned nothing on point.

  Summary: The corrective proposition is well supported in its methodological half and unaddressed in
  its institutional half. The quality tradition's foundational position is that the inspection unit
  determines what can be found and that item-by-item inspection is aimed at the wrong target: "inspection
  is too late — the quality, good or bad, is already in the product," and the instruction is to cease
  DEPENDENCE on it while retaining sample inspection to monitor the process. The reason this matters is
  the common-cause/special-cause split: special causes are assignable to particular items and are
  findable there; common causes are properties of the system, are invisible in any single item by
  construction, and on Deming's much-repeated estimate account for the great majority of variation. A
  review regime whose only unit is the pair is therefore not merely under-resourced for corpus-level
  work — it is structurally incapable of it, and would remain so with unlimited reviewer time. Mature
  audit practice is organised the other way round: ISO 19011 has the auditor sample rather than examine
  everything and requires an explicit statement of how the findings extrapolate to the population, so
  the population-level conclusion is the deliverable and the item examinations are the means. Against
  that, the Goodhart mechanism explains the persistence without anyone intending it — pair-level work
  has a count and corpus-level work does not, so the unmeasured activity loses a competition for a fixed
  budget that no one ever staged. The register already holds the underlying principle in two places
  (PREMISE-130's defect-class reclassification, PREMISE-150's coverage bound) and holds two worked
  corpus-level findings, but holds nothing about slot, budget or count — and PREMISE-168 has just
  established that the natural count is barred in both its forms, which makes 816's third clause harder
  to remedy rather than easier.

  Caveats:
    (a) THE OBVIOUS REMEDY IS ALREADY BARRED BY THE REGISTER AND MUST NOT BE PROPOSED. "Give
        corpus-level findings a count" runs directly into PREMISE-168's declared constraint —
        PREMISE-109 bars the coverage percentage and PREMISE-168 bars the bare numerator, and 168
        records that no instrument satisfying both was found. **A disposition that answers 816 by
        creating a corpus-findings-per-week metric would violate two ACTIVE premises.** The surviving
        practice named in 168 is the stratified statement, which "is not a metric and cannot be
        trended." So the honest form of the remedy for (R3) is a SLOT AND A BUDGET WITHOUT A COUNT, and
        that is an uncomfortable but defensible position that should be stated as such.
    (b) DEMING'S 94% IS AN ESTIMATE, NOT A MEASUREMENT, AND IS FROM A DIFFERENT DOMAIN. It concerns
        manufacturing and service variation in human organisations. There is no evidence located here
        that the common-cause share in an LLM-generated review corpus is anywhere near 94%, and it is
        entirely possible that agent output has an unusually high share of assignable, item-local
        defects. **The qualitative claim survives the transfer; the number does not, and quoting it as
        though it applied to C2A2 would be the error PREMISE-124 forbids.**
    (c) THE AUDIT ANALOGY HAS A LIMIT THAT CUTS AGAINST THE ITEM. ISO 19011 audits a MANAGEMENT SYSTEM
        against stated criteria — there is a specification to audit against, which is what makes
        extrapolation meaningful. C2A2's review has no comparable written criterion for the corpus as a
        whole, so importing the extrapolation requirement without first writing down what the corpus is
        supposed to satisfy would produce population-level statements with no referent. **The
        prerequisite for a corpus-level finding slot is a corpus-level criterion, and 816 does not say
        one exists.**
    (d) SAMPLING VERSUS CENSUS WAS THE QUEUED QUESTION AND IS ONLY HALF-ANSWERED HERE. ISO 19011 gives
        the audit-side answer (sample deliberately, justify the size, state the extrapolation). What was
        NOT located is anything on the specific trade in 816's setting: whether reviewing every pair is
        actually superior to reviewing a stratified sample and spending the released time on
        corpus-level work. That is the decision the item implies and no source located here supports or
        refutes it. Note also that ISO 2859-3 skip-lot practice is already register-adjacent via
        ASSUMPTION-1077 (2026-08-15), where the finding was that **the acceptance rule is set by the
        party bearing the risk** — which means this trade is Tom's to make, not the pipeline's.
    (e) SOURCE QUALITY IS UNEVEN AND NO PRIMARY WAS OBTAINED FOR ANY OF SOURCES 1-4. Deming's book,
        ISO 19011, and the SmartBear/Cisco study were all identified and none was opened. The
        methodological claims are robust because they are foundational and consistently reported; the
        numbers are not.
    (f) 14b'S SEPARATION OF THE DAY'S OUTPUTS WAS NOT INDEPENDENTLY REPRODUCED. This file did not
        enumerate the day's findings or classify them. Per PREMISE-124 nothing here is a calibrated
        measurement of the pair/corpus ratio.

  Search scope: GOOD at snippet level on the quality-tradition core (Deming Point 3; common/special
    cause) and on audit sampling practice (ISO 19011, via six independent secondary expositions).
    CANONICAL and register-held on Goodhart. WEAK on the code-review magnitudes, flagged in place. NOT
    SEARCHED, and each would materially change this file: (i) **UNIT-OF-ANALYSIS EFFECTS ON INSPECTION
    YIELD as an empirical literature** — the queue asked for it and this search located nothing that
    measures how detection rate varies with the inspection unit; that is a clearly-labelled negative
    result and the single most valuable missing piece; (ii) **software-inspection research on
    perspective-based reading and on defect-class versus defect-instance reporting** (Basili et al.;
    Porter & Votta), which is the closest thing to a controlled comparison of review units and was
    identified but NOT reached; (iii) **any literature on BUDGETING an unmeasured review activity**,
    which is 816's clause (R2) and for which nothing was found — the institutional half of the item
    remains unsupported by anything external.

  Recommendation: **PARTIALLY-SUPPORTED (Moderate-to-Strong)** for the corrective proposition;
  equivalently a partial NO-SUPPORT-FOUND for the arrangement as described. The split is clean and
  should be preserved in any disposition. Four carries:
    1. THE METHODOLOGICAL HALF IS SUPPORTED AND IS LARGELY ALREADY HELD. That the unit of inspection
       determines the detectable fault class is Deming's Point 3 and is PREMISE-130 in the register. A
       new premise on that alone would duplicate 130 and is barred by PREMISE-138(1).
    2. THE INSTITUTIONAL HALF — NO SLOT, NO BUDGET, NO COUNT — IS THE ITEM'S REAL CONTENT, IS NOT IN THE
       REGISTER, AND IS **NOT SUPPORTED BY ANYTHING LOCATED THIS RUN EITHER.** It is not novel enough
       for a NOVELTY-FLAG (the audit disciplines plainly do budget population-level work), but the
       specific claim that an unmeasured review activity loses budget to a measured one has no located
       empirical source. If a disposition wants to act on 816, this is the clause that needs its own
       search and does not have one.
    3. THE ADOPTABLE STEP IS A SLOT, NOT A METRIC (caveat a). PREMISE-136 already requires every
       settling quantity to declare its scope as run / cohort / corpus. Extending that from quantities
       to FINDINGS — every review finding declares whether it is pair-level or corpus-level at the point
       it is written — creates the slot at zero cost, satisfies (R1), and does so without creating the
       count that PREMISE-109 and PREMISE-168 jointly forbid.
    4. THE BUDGET QUESTION IS TOM'S, NOT THE PIPELINE'S. Per the 2026-08-15 finding on ASSUMPTION-1077,
       an acceptance rule is set by the party bearing the risk. How reviewer time divides between pair
       and corpus is a risk-allocation decision, and the pipeline may surface it but may not settle it.
