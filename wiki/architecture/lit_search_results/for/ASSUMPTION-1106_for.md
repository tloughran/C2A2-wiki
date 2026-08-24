SEARCH-FOR-ASSUMPTION-1106:
  Date searched: 2026-08-17
  Original item: ASSUMPTION-1106
  Original statement: A check that cannot execute reports a warning, and warnings do not fail.
    Measured instance: the anti-fabrication guard is inert on 66 of 307 transcripts (21.5%) because
    the sentence splitter returns zero sentences on unpunctuated ASR; those days carry
    `last_qc_outcome: pass`.
  Risk if wrong: **Critical** (the day's lead finding; stated to generalise).
  Search question (as queued): severity taxonomies in static analysis; indeterminate and
    uninformative results in diagnostic and screening tests; the "not applicable" state in test
    harnesses; negative-control design.

  POLARITY NOTE — WHAT WAS ACTUALLY SEARCHED FOR. The item is worded as the DEFECTIVE BEHAVIOUR of
  the instrument. The proposition searched FOR is the CORRECTIVE CONVERSE, in four clauses:
    (C1) A SCHEMA THAT CANNOT DISTINGUISH "RAN AND FOUND NOTHING" FROM "COULD NOT RUN" IS DEFECTIVE
         BY DESIGN; mature schemas carry a *first-class* non-applicable value, not a shade of pass.
    (C2) WHERE A CHECK'S ENABLING PRECONDITION FAILED, THE DISCIPLINES THAT HAVE STUDIED THIS VOID
         THE RESULT RATHER THAN RETURN THE NEGATIVE, and attach a re-test action to the void state.
    (C3) VACUOUS PASSES OCCUR AT DOUBLE-DIGIT RATES IN MATURE INSTRUMENTED PRACTICE, so 21.5% is a
         normal magnitude for this fault class — which is what licenses the generalisation claim.
    (C4) THE REMEDY IS A CO-RUNNING CONTROL THAT ASSERTS EXECUTABILITY, NOT A LOUDER WARNING.
  "SUPPORTED" below means 14a's diagnosis is well grounded.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-1106
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from a stated measurement — 66/307 transcripts inert, `last_qc_outcome: pass`.
      15a: Register pre-check, then searched for supporting literature on the corrective proposition.
    Current status: SUPPORTED (Strong)

  REGISTER CHECK (before writing; grep for: warning, severity, inert, no-op, vacuous, "not
  applicable", skip, indeterminate, negative control, fail-open, stuck-at-nominal, proof-test):
    - **PREMISE-110** (2026-07-20, ACTIVE) — the nearest neighbour. "Detectors do not reliably
      degrade gracefully; they invert ... stuck-at-nominal, one of five standard non-fail-stop sensor
      faults." Prescribes a **live proof-test**. **1106 is a measured instance of this fault class**,
      at the check level rather than the monitor level.
    - **PREMISE-131** (ACTIVE) — "A WARNING IS NOT A CONTROL"; warnings occupy the two least-effective
      tiers of the NIOSH hierarchy. The register's existing answer to "warnings do not fail."
    - **PREMISE-154** (2026-08-13) — a clock-driven re-audit "**manufactures a false record of having
      looked**."
    - **PREMISE-148** (2026-08-06) — indeterminate items "must be flagged as unreverifiable and
      excluded from load-bearing conclusions."
    CONCLUSION: **SUBSTANTIAL BUT NOT TOTAL OVERLAP; NO NOVELTY-FLAG.** No ACTIVE premise states the
    composition rule this item exposes: **a QC schema whose only non-fail value is "warning" cannot
    represent non-execution, so an inert check is arithmetically indistinguishable from a clean one
    at the aggregate.** DECLARED LIMITATION: string grep, ~56% recall (ASSUMPTION-1052); lower bound.

  Supporting evidence found: Yes

  Sources:
    1. **OASIS, *SARIF Version 2.1.0 Plus Errata 01*, `result.kind` / `result.level`
       (docs.oasis-open.org/sarif/sarif/v2.1.0/).** — **Direct support for (C1); the most useful
       artefact located.** `kind` enumerates **`pass`, `fail`, `open`, `review`, `notApplicable`,
       `informational`** — the interchange standard treats "the rule was not applicable" as a
       *sibling* of pass. The spec imposes an invariant: if `level` is `error`/`warning`/`note` then
       `kind` MUST be `fail`; if `kind` is anything but `fail`, `level` MUST be `none`. **Severity and
       outcome are orthogonal axes**, which is exactly the separation C2A2's schema collapses. A QC
       record emitting `warning` for a check that did not run is not expressible in SARIF at all.
       [SNIPPET LEVEL — spec URL located; the enumeration and invariant are reported from retrieved
       summaries and independent implementation docs (projectdiscovery/sarif; microsoft/sarif-sdk;
       GitHub discussion #65477). **The OASIS document was NOT opened.** Do not quote a clause number.]
    2. **Beer, I., Ben-David, S., Eisner, C. & Rodeh, Y. (1997/2001), "Efficient Detection of Vacuity
       in Temporal Model Checking," CAV '97 / *Formal Methods in System Design*; Kupferman, O. &
       Vardi, M.Y. (2003), "Vacuity detection in temporal model checking," *STTT* 4(2).** — **Support
       for (C3); the closest formal analogue.** "Every request is eventually followed by a grant" is
       satisfied **vacuously** where no request is ever issued: the antecedent never fires, the check
       passes unexercised. **~20% of specifications passed vacuously in initial verification runs at
       IBM Haifa** — against C2A2's 21.5%. The field's response was not to reword the report but to
       build a **separate detector** and require a *witness* trace.
       [SNIPPET LEVEL — records and a hosted PDF (cs.toronto.edu/~chechik/courses05/csc2108/beer01.pdf)
       located; **none opened.** The 20% figure and the request/grant example are from retrieved
       summaries. Authors, venue, year confirmed; do not quote verbatim.]
    3. **The Bethesda System for Reporting Cervical Cytology — "Unsatisfactory for Evaluation" versus
       "Negative for Intraepithelial Lesion or Malignancy" (2001 revision; CAP *Gynecologic Cytology*;
       IARC atlas).** — **Support for (C2).** An inadequate slide is **Unsatisfactory** — a category
       structurally distinct from Negative — and is recollected. The 2001 revision deliberately
       **abolished the intermediate hedge** ("satisfactory but limited by") because clinicians could
       derive no action from it, leaving an explicit adequacy gate that must be passed before any
       interpretive result issues. The pass/warn/fail collapse in reverse: the middle tier was found
       unactionable and removed.
       [SNIPPET LEVEL — IARC, CAP and AAFP pages read at retrieved-summary level; **none opened.**]
    4. **QuantiFERON-TB Gold Plus interpretation criteria (QIAGEN); CDC / NYC DOHMH LTBI guidance.** —
       **Support for (C4).** Every IGRA run carries a **mitogen positive control**; below the
       threshold the run is **INDETERMINATE**, with the explicit rubric that "a positive or negative
       result cannot be determined," and the action is repeat testing. Causes are both subject-side
       (immunosuppression) and process-side (draw volume, transport delay, incubation). **The control
       is what makes an uninformative run visible as uninformative**, and it is a separate measured
       channel, not a severity label on the main one.
       [SNIPPET LEVEL — QIAGEN interpretation page, *J. Clin. Microbiol.* 2021 on raised indeterminate
       rates in COVID-19 inpatients, and NYC DOHMH TB manual ch.2 located; **none opened.** The
       0.5 IU/mL threshold is reported as retrieved — re-check against the package insert.]
    5. **Test-harness outcome taxonomies: pytest `skip`/`xfail`/`xpass` (docs.pytest.org); JUnit XML
       `<skipped>`; TAP `# SKIP` / `# TODO`.** — **Support for (C1) from ordinary practice, with a
       warning attached.** pytest counts skipped and xfailed **separately** from passed, and defines
       `skip` as the non-execution case. The warning: **the distinction is routinely lost in
       serialisation** — pytest issues #2190, #5891 and #7009 all document xfail/xpass rendered as
       `<skipped>` or as conflicting results in JUnit XML, because the target vocabulary is narrower.
       **The information is destroyed at the schema boundary, not at the check** — which is where
       C2A2 lost it, in `last_qc_outcome`.
       [SNIPPET LEVEL — pytest docs and the three issue threads read at summary level; none opened.]
    6. **Static-analysis severity practice (Parasoft; `dart analyze`; "Quieting the Static: A Study of
       Static Analysis Alert Suppressions," arXiv 2311.07482).** — Cited for honesty: it confirms the
       *descriptive* half of the item — warning tiers conventionally do not fail a build absent
       `-Werror` — and that suppressing inapplicable findings is legitimate. **It supplies no warrant
       for encoding non-execution in the warning tier**; suppression records a human judgement, not a
       silence.
       [SNIPPET LEVEL — vendor and arXiv pages read at summary level only.]

  Strength of support: **Strong** on (C1), (C2), (C4); **Moderate-to-Strong** on (C3).
    (C1) is carried by an OASIS interchange standard that makes the distinction normative, and
    independently by every mainstream test runner's vocabulary. (C2) is carried by two regulated
    diagnostic disciplines with mandatory void-the-result rules and attached actions. (C4) converges
    with PREMISE-110's live-proof-test prescription from an unrelated direction. (C3) is downgraded
    because the 20% figure rests on one industrial report at one laboratory, read at snippet level,
    and because the base rate of vacuous passes is a property of specification style, not a constant.

  Summary: The corrective proposition is strongly supported and, in the disciplines that have met
  this fault, settled. Formal verification named it "vacuity," measured it at roughly one
  specification in five, and answered with a separate detector plus a required witness trace — not
  with better wording on the pass. Static-analysis interchange made the distinction structural:
  SARIF carries `notApplicable` as a peer of `pass`, and forbids a severity level from co-existing
  with a non-failing kind, so severity and outcome cannot be conflated in a conformant record.
  Clinical laboratory practice supplies the strongest reporting rule: an inadequate cervical specimen
  is Unsatisfactory and not Negative; an IGRA whose mitogen control fails is Indeterminate with an
  explicit statement that no result can be determined. Both attach an action a warning does not
  carry. The cautionary finding is that the distinction is most often lost at the *schema boundary* —
  the pytest issue history shows skip and xfail collapsing into `<skipped>` under a narrower
  vocabulary, which is the shape of `last_qc_outcome: pass`. The register already holds the fault
  class (PREMISE-110) and the warning-tier verdict (PREMISE-131); the increment is the composition
  rule that a three-valued schema with no non-applicable state cannot represent non-execution.

  Caveats:
    (a) THE SOURCES SUPPORT A DISTINCT STATE, NOT NECESSARILY A FAILING ONE. SARIF's `notApplicable`
        does not fail; Bethesda's Unsatisfactory does not diagnose. What each requires is that the
        state be **separately representable, separately counted, and action-bearing**. Reading 1106
        as "inert checks should return `fail`" over-claims and would fire on legitimately
        inapplicable inputs. The supported remedy is a fourth value plus an aggregate exclusion rule.
    (b) DOMAIN TRANSFER FROM DIAGNOSTICS IS FLATTERING IN ONE RESPECT. Both clinical sources assume a
        recollection pathway. A transcript that cannot be re-recorded has none, so the C2A2 analogue
        of "repeat the test" may not exist; there the honest disposition is PREMISE-148's — flag
        unreverifiable and exclude from load-bearing conclusions.
    (c) THE 21.5% ≈ 20% CORRESPONDENCE IS A COINCIDENCE UNTIL SHOWN OTHERWISE. Different denominators
        (specifications vs transcripts), different generating mechanisms. Do not report as convergent
        measurement.
    (d) PUBLICATION BIAS RUNS SUPPORTIVE. Vacuity detection is a research programme presupposing the
        problem is real; the clinical categories are consensus documents. **Nothing located this run
        *measured* the benefit of adding a non-applicable state against not adding one.**
    (e) SEVERITY-TIER PRACTICE CUTS BOTH WAYS (source 6). Real toolchains do treat warnings as
        non-failing by default, which is why the defect survived — an argument for an engineering
        control (PREMISE-131) rather than for more careful schema use.

  Search scope: GOOD breadth; **NOT VERIFIED AT PRIMARY LEVEL ANYWHERE — no source in this file was
    opened and read in full.** All six are at retrieved-summary level with identifiers confirmed.
    NOT SEARCHED, each of which would strengthen the file: (i) **the SARIF 2.1.0 spec text itself**,
    §3.27.9/§3.27.10 — the highest-value outstanding fetch; (ii) **CLSI / ISO 15189 language on
    invalid versus indeterminate results and QC acceptance criteria**, the formal metrology of (C2);
    (iii) **negative-control design proper** — the queue asked for it and this search did not reach
    it at all, a clearly-labelled negative result (the IGRA mitogen control is the mirror-image
    instrument); (iv) **mutation testing and assertion-free-test detection**, the software measurement
    of "the test ran but could not have failed," arguably the closest analogue of all.

  Recommendation: **SUPPORTED (Strong)** for the corrective proposition; the behaviour described in
  ASSUMPTION-1106 is a recognised, named and instrumented defect in four independent disciplines.
    1. THE MINIMAL CHANGE IS A FOURTH OUTCOME VALUE, NOT A SEVERITY PROMOTION. Add `not_applicable`,
       emit it when the precondition fails, and **exclude those runs from every pass-rate
       denominator**. This is SARIF's model exactly.
    2. THE VALUE MUST CARRY A REASON CODE OR IT WILL BE UNACTIONABLE — Bethesda deleted its middle
       category for precisely that defect. "Zero sentences returned by splitter" is the reason code
       the measured instance needs.
    3. PAIR IT WITH PREMISE-110'S LIVE PROOF-TEST, the only located instrument that would have caught
       this. Feed the guard a transcript containing a known fabrication and confirm it fires.
    4. AUDIT THE SCHEMA BOUNDARY, NOT ONLY THE CHECK. Wherever `last_qc_outcome` is aggregated or
       re-emitted, verify the new value survives rather than degrading to `pass`.
