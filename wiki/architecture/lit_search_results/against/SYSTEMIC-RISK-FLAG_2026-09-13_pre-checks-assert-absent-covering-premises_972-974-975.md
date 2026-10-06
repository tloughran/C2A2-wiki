SYSTEMIC-RISK-FLAG:
  Date: 2026-09-13
  Raised by: Agent 15b (Literature Search AGAINST), during the five-item cycle of 2026-09-13.
  Affected items: PRESUMPTION-972, PRESUMPTION-974, PRESUMPTION-975.
    (ASSUMPTION-1336 and PRESUMPTION-979 are NOT affected — their pre-checks were re-run and held.)

  Common vulnerability: **THE INTAKE PRE-CHECK ASSERTS THE ABSENCE OF A COVERING PREMISE WITHOUT
    ESTABLISHING IT, AND DID SO ON THREE OF FIVE ITEMS IN A SINGLE CYCLE.** In each case an ACTIVE
    premise covers the item in general form, and in each case the grep terms the pre-check reports
    having used would have returned it. The failure is not in the search; it is in reading the return.

  The three instances, with the premise text that was missed:
    1. **PRESUMPTION-972.** Pre-check: "grepped for `recency`, `window`, `dormant`, `cadence` —
       PREMISE-154 bears adjacently... but does not cover the active/dormant distinction."
       **PREMISE-141 (ACTIVE, High, re-check due 2026-09-05 — 8 days overdue)** covers it in general
       form: "ABSENCE OF A REPORT IS A THIRD TERMINAL STATE, NOT A VALUE OF THE OTHER TWO... a
       two-valued model... CANNOT REPRESENT [it]... each reader supplies the missing value from their
       own prior." **PREMISE-089 (ACTIVE, re-check due 2026-09-06 — 7 days overdue)** covers the second
       limb: "Freshness/liveness is a per-source property; the liveness of any one feed must never be
       taken as evidence for the liveness of another," with cross-source liveness inference named a
       known anti-pattern.
    2. **PRESUMPTION-974** (intake-flagged CRITICAL). Pre-check: "grepped for `in-house`, `unowned`,
       `discharge`, `owner` — REVISE-459 and DISPOSITION-948 name the condition; **no premise
       generalises it.**"
       **PREMISE-026 (ACTIVE, Confidence HIGH, re-check due 2026-08-18 — 26 days overdue)** generalises
       it explicitly: "Long-unowned RE-TRIGGER cohorts in C2A2 should be classified as
       ownership-boundary problems (unassigned accountability), not item-ageing problems... remediation
       requires owner assignment," applicable to "any long-running unowned queue across C2A2
       pipelines." **PREMISE-108 (ACTIVE)** answers it: "Transmission is not delivery... until then the
       finding is held by nobody while the record shows it discharged. That state is worse than not
       flagging." The grep terms `owner` and `unowned` appear verbatim in PREMISE-026.
       **Aggravating fact: PREMISE-108 is itself one of the four items in the 178 days of unexecuted
       owed tests that PRESUMPTION-974 counts.** The register is failing the premise that describes the
       failure, and its pre-check then reported that no such premise exists.
    3. **PRESUMPTION-975.** Pre-check: "grepped for `independen`, `concurrent`, `anchoring` — the
       provenance spec requires the attestation and defines no condition on execution order. **No
       covering premise.** Confirmed by reading `provenance_protocol.md` v1.0, not by grep alone."
       **PREMISE-111 (ACTIVE, re-check due 2026-08-21 — 23 days overdue)** is the governing premise for
       this exact pair of agents and contains a clause marked load-bearing: "**STANDING DISCOUNT
       (load-bearing)... No downstream argument may cite 15a/15b agreement as independent
       confirmation.**" The string `independen` occurs in it at least three times. The item's own
       stated evidence — that both directions "independently found" the same covering premises — is a
       direct violation of that clause. **PREMISE-120 (ACTIVE)** additionally forbids the phrase
       "independently confirmed" unless the second check obtained its own data.

  Literature basis:
    - **In-house and decisive: PREMISE-136 clause (2) (ACTIVE)**, read verbatim: "a claim that no route
      to a larger denominator exists **is false of this register and must be checked against it before
      being asserted**." Its `Applicable to` line names "**14a and 14b item drafting**." The structure
      of the breach is identical here — a negative existential asserted about the register without
      checking the register — and PREMISE-136 already makes that class of assertion a procedural
      breach rather than a mere inaccuracy. **This is the second consecutive cycle in which a
      PREMISE-136-shaped breach has been found**: the 2026-09-12 finding on PRESUMPTION-968 was the
      first, and that item's own stated evidence position was likewise false against the register.
    - **ASSUMPTION-1343**, which the 979 pre-check cites as demanding that premise texts be "read, not
      matched on keyword." That correction was applied to PRESUMPTION-979 (whose pre-check held) and
      **not** to the other three.
    - External: none required, and none is offered. This flag rests entirely on in-house documents read
      in full this run.

  Risk level: **CRITICAL.**

  Why critical rather than high: the pre-check is the **gate that decides whether an item is an
    external question at all**. Its output determines (i) whether 15a and 15b spend a search cycle on a
    question the register has already answered, (ii) whether a new premise is minted that duplicates an
    ACTIVE one — which PREMISE-135 bars and PREMISE-138 clause (1) calls an in-channel repetition with
    no effector — and (iii) whether an existing premise's **enforcement gap** is correctly identified
    as such. On all three items tonight the correct finding was an enforcement gap, not a knowledge
    gap, and the pre-check's error converts an enforcement failure into an apparent research question.
    That is the most expensive possible misclassification: it consumes the scarce search budget while
    leaving the unenforced premise unenforced, and it produces a *new* register entry whose existence
    then argues that the matter is being attended to.

  Compounding factor, recorded separately because it is independently actionable: **all four premises
    missed are past their re-check date** — PREMISE-026 by 26 days, PREMISE-111 by 23, PREMISE-141 by
    8, PREMISE-089 by 7 — and all four still read `Status: ACTIVE`. A premise that is overdue,
    unenforced, and invisible to the pre-check that should surface it is, operationally, not a premise.

  Second flag, lower severity, recorded here to avoid a separate file:
    **WEAKEST-CONTROL-CLASS DEPENDENCE (Risk level: High). Affected items: PRESUMPTION-974,
    PRESUMPTION-979.** The IHI/VA National Center for Patient Safety Action Hierarchy (2019, retrieved
    and read in full this run) places three categories in its **Weaker Actions** tier — "New
    procedure/memorandum/policy," "**Warnings**," and "Training" — on the stated ground that "these
    tasks require more reliance on humans to remember to perform the task correctly," and notes that
    when used alone they "are unlikely to be sufficient for sustained improvement." The guidance
    requires "at least one strong or intermediate action for each identified cause."
    **C2A2's two principal control mechanisms are both in that bottom tier.** PRESUMPTION-974's
    finding is that the register's remedial output is named-but-unowned tests (procedure/memorandum);
    PRESUMPTION-979's finding is that its epistemic discipline is prose qualifications (warnings). Of
    tonight's five filed remedial actions, per the intake, all five are greps — zero strong, zero
    intermediate, against a standard requiring at least one per cause. Kwok et al. 2020 (verified, 760
    recommendations across 43 hospitals) measures 82% weak as the *norm* in a mandatory safety system,
    so weak actions are not anomalous — **a rate of zero in the top two tiers is.** Recommendation: the
    estate should either adopt the "at least one strong or intermediate action per cause" rule, or
    record explicitly that it is declining to, and stop treating the weak tier as coverage.

  Recommendation (primary flag):
    1. **Re-run the pre-checks for PRESUMPTION-972, 974 and 975 against the four named premises before
       any disposition is taken on them.** All three items are, on this run's reading, enforcement gaps
       in ACTIVE premises rather than new questions, and should be dispositioned that way.
    2. **Do not mint new premises for these three items.** PREMISE-135 and PREMISE-138(1) both bar it,
       and minting would make the enforcement gap harder to see, not easier.
    3. **Change what the pre-check is required to produce.** At present it reports a conclusion ("no
       covering premise"). It should be required to report the **grep terms used and the premise IDs
       returned**, so that a negative finding is auditable and a missed return is visible at the point
       of drafting rather than one hop downstream. This is a schema constraint — a forcing function,
       which the action hierarchy classes as **Stronger** — and not a guideline, which it classes as
       weak. Filing this recommendation as an unowned in-house test would be PRESUMPTION-974
       reproducing inside the flag that names it, and it is written to be assignable for that reason.
    4. **Re-check the four overdue premises** (026, 089, 111, 141) and, for each, record whether it is
       enforced and where it is not.
    5. **Apply PREMISE-111's standing discount, or record that it is unapplied.** It has been ACTIVE
       and load-bearing since 2026-07-21 and this run found no evidence of it having been applied
       anywhere. An unapplied load-bearing clause is the PRESUMPTION-979 finding in its most
       consequential instance.

  Caveat on this flag's own status, stated up front rather than buried: **three of the five items in
    this cycle were searched by an agent whose independence from its sibling is itself one of the five
    items.** Per the intake's instruction and PREMISE-111, convergence between 15a and 15b on any of
    tonight's findings — including this flag — is uninformative and must be discounted. This flag rests
    on in-house documents read in full and quoted verbatim, which is the form of evidence least
    sensitive to that limitation, but the limitation is not thereby removed.
