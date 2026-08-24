SEARCH-FOR-PRESUMPTION-818:
  Date searched: 2026-08-17
  Original item: PRESUMPTION-818
  Original statement: [inferred] That a warning is a weaker failure — that the pass/warn/fail schema
    can express the difference between a small defect found, an instrument that did not execute, and a
    disagreement about the definition. Today's three instances show it cannot.
  Risk if wrong: **Critical**. Priority: Critical.
  Search question (as queued): as ASSUMPTION-1106 (severity taxonomies in static analysis;
    indeterminate/uninterpretable results in diagnostic and screening tests; the "not applicable" state
    in test harnesses; negative-control design), plus alarm/severity schema design and the treatment of
    indeterminate results in metrology (VIM/GUM).

  POLARITY NOTE — WHAT WAS ACTUALLY SEARCHED FOR. The item is worded as the DEFECTIVE belief. The
  proposition searched FOR is the CORRECTIVE CONVERSE, in five clauses:
    (C1) SEVERITY AND KIND ARE ORTHOGONAL AXES, and a schema with only an ordinal severity axis cannot
         express kind. Standards bodies that started with one axis have been forced to add a second.
    (C2) "DID NOT EXECUTE" / "COULD NOT BE EVALUATED" IS A DISTINCT OUTCOME CLASS, NOT A WEAKER PASS,
         and folding it into either pole produces a MEASURABLY BIASED accuracy figure.
    (C3) "TOO CLOSE TO CALL" / "THE DEFINITION IS DISPUTED" IS ITS OWN ZONE in which NO CONFORMITY
         STATEMENT IS MADE, and the metrological standards name this explicitly.
    (C4) THE DATA-MODEL FORM: absence must be representable distinctly from a value, and there are at
         least TWO kinds of absence (missing-and-applicable vs missing-and-inapplicable).
    (C5) TEST-HARNESS PRACTICE ALREADY IMPLEMENTS THIS — pass / fail / error / skip / xfail are
         separate result classes, not points on one severity scale.
  "SUPPORTED" below means 14b's diagnosis is well grounded, and is equivalently evidence AGAINST the
  presumption as worded.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-818
    Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: the three-valued schema was
      never chosen as a schema, it was inherited, so its expressive limit was never examined)
    Transform at each step:
      14b: Inferred from three same-day instances in which "warn" was used to carry three different
        conditions; observed that the schema flattens them.
      15a: Searched for supporting literature on the corrective proposition; register check first.
    Current status: SUPPORTED (Strong) — BUT SEE THE DUPLICATION WARNING

  **DUPLICATION WARNING — READ BEFORE DISPOSITION.** The register already holds the PRINCIPLE and the
  INSTANCE, in two separate places, one at High confidence:
    - **PREMISE-103** (2026-07-19, ACTIVE, Moderate) holds the principle in a different domain, in
      almost the exact words 818 needs: "**Absence of primary text is a KIND-DIFFERENCE in evidence, not
      a DEGREE-DIFFERENCE: no confidence label over metadata-only material is well-founded, and
      DOWNGRADING CONFIDENCE IS NOT A VALID SUBSTITUTE for an explicit 'unfounded pending retrieval'
      state.**" Substitute "warning" for "downgraded confidence" and "check did not execute" for
      "metadata-only" and PRESUMPTION-818 is PREMISE-103 with the nouns changed.
    - **PREMISE-100** (2026-07-19, ACTIVE, **High**) holds the instance: "a health check that cannot
      execute in its runtime context **reports as passing rather than as absent**; monitoring that
      conflates the two produces false-green at a rate proportional to the number of inoperable
      checks." The anti-fabrication guard inert on 66 of 307 transcripts is a textbook instance of
      PREMISE-100, twenty-nine days old.
    - **PREMISE-131** (2026-07-28, High) already establishes that a warning is the weakest admissible
      tier and that an undelivered warning has ZERO effect, not reduced effect — the same
      degree-versus-kind move on the mitigation side rather than the reporting side.
    - **PREMISE-158** (2026-08-13) holds that an instrument's error profile is two-sided and is a
      **designed and declarable property** — which is the schema-design obligation 818 implies.
    - **PREMISE-171** (2026-08-16) holds that a declaration register is not a failure detector and its
      completeness is zero — the adjacent "the record says nothing about the world" result.
  Grep terms used against `validated_premises.md`: warning, severity, indeterminate, inconclusive,
  no-op, cannot execute, did not execute, inoperable, false-green, absence, kind-difference, taxonomy,
  pass/fail, warn. DECLARED LIMITATION: string grep, ~56% recall (ASSUMPTION-1052); the list is a LOWER
  BOUND. **NO NOVELTY-FLAG** — the literature on this is large and old.
  **THE RESIDUAL, and the only thing here that is not a restatement:** PREMISE-100 and PREMISE-103
  establish that the conflation happens and that it is a kind-error. **Neither creates a SCHEMA
  OBLIGATION.** Neither says what the outcome vocabulary must contain. That is what the literature below
  supplies and what the register does not hold: the requirement for a SECOND, CATEGORICAL, ORTHOGONAL
  AXIS alongside severity, with named members.

  Supporting evidence found: Yes

  Sources:
    1. OASIS, *Static Analysis Results Interchange Format (SARIF) Version 2.1.0* (OASIS Standard, with
       Errata 01), `result.kind` and `result.level`. — **The single most exact hit located this run, and
       it is a normative standard in precisely 818's domain.** SARIF carries TWO properties on every
       result. `level` is the ordinal severity axis: `none`, `note`, `warning`, `error`. `kind` is a
       CATEGORICAL evaluation-state axis whose members are `pass`, `fail`, `open`, `review`,
       `informational` and — decisively for 818 — **`notApplicable`**. The specification records that
       the two were SPLIT because the original single `level` property mixed severity values (warning,
       error) with status values (open); and it states that **"the concept of 'severity' does not apply
       to a result when `kind` has a value other than `fail`."** That is 818's claim as a normative
       clause: a warning is only a weaker failure WHEN THERE IS A FAILURE; an instrument that did not
       execute is `kind: notApplicable`, on which severity is undefined, and a disagreement about the
       definition is `kind: review` or `kind: open`, likewise. The `open` member exists specifically for
       "the tool could not decide."
       [SNIPPET LEVEL — the OASIS specification URLs (docs.oasis-open.org/sarif/sarif/v2.1.0/ and the
       v2.0 predecessor) and the sarif-spec issue tracker thread on separating status from kind
       (oasis-tcs/sarif-spec issue #371) were LOCATED this run and read at retrieved-summary level;
       **the specification itself was NOT fetched and read in full.** The enumerated members and the
       severity-does-not-apply clause are reported as retrieved, not quoted from the primary. Verify
       before quoting normatively.]
    2. ILAC-G8:2019, *Guidelines on Decision Rules and Statements of Conformity*, together with ISO/IEC
       17025:2017 clause 7.1.3. — **The support for clause (C3), and the metrology answer the queue
       asked for.** ILAC-G8 frames decision rules as a spectrum: binary simple acceptance (guard band
       zero); binary guarded acceptance/rejection; **non-binary rules, which "add an explicit CONDITIONAL
       or INDETERMINATE ZONE where NO CONFORMITY STATEMENT IS MADE"**; and shared-risk rules. Guard
       banding creates three zones — acceptance, a guard band "where the result is too close to the
       limit to claim conformity with confidence," and rejection. Clause 7.1.3 makes the rule itself a
       mandatory recorded artefact: it must be agreed and documented BEFORE conformity is stated. Two
       transfers to 818. First, the discipline that has thought hardest about pass/fail under
       uncertainty does not have a "weak pass"; it has a THIRD LABEL that withholds the statement.
       Second, the label is not the deliverable — **the decision rule is**, and a schema that emits
       pass/warn/fail without recording which rule produced them is not defensible on this standard's
       own terms.
       [MIXED. The ILAC-G8 content above is taken from a SECONDARY SOURCE **fetched and read in full**
       this run: CalibrationOS, "Guard Banding & Decision Rules: ILAC G8 Conformity Decisions Explained"
       (calibrationos.com/learn/guard-banding-decision-rules-ilac-g8, CC BY-SA 4.0). **This is a
       calibration-software vendor's explainer, not the standard.** The primary ILAC-G8:2019 text was NOT
       retrieved. A Eurachem workshop presentation (PL3-03, da Silva) and the ILAC/Eurachem announcement
       page were located and not opened. Treat the quoted phrases as the vendor's paraphrase.]
    3. Schuetz, G.M., Schlattmann, P. & Dewey, M. (2012), "Use of 3x2 tables with an intention to
       diagnose approach to assess clinical performance of diagnostic tests," *BMJ* (PMID 23097549);
       and Bossuyt, P.M. et al. (2015), *STARD 2015 Explanation and Elaboration*. — **The support for
       clause (C2), and the only source family located that MEASURES the cost of the conflation.** STARD
       requires indeterminate, uninterpretable and missing results to be reported as such, and records
       that **only ~35% of diagnostic-accuracy studies explicitly report them**. The methodological
       finding is the one 818 needs: indeterminates may be ignored, reported-but-not-accounted-for, or
       handled as a SEPARATE RESULT CATEGORY; and **"ignoring indeterminate test results can produce
       BIASED estimates of accuracy IF THESE RESULTS DO NOT OCCUR AT RANDOM."** They do not occur at
       random in C2A2's instance either — the guard is inert specifically on unpunctuated ASR, a
       systematically different subpopulation. Schuetz et al. supply the constructive remedy, a **3x2
       table under an "intention to diagnose" approach** keeping the non-evaluable column visible
       instead of allocating it, and report non-evaluable results in 109 of 120 CCTA studies.
       [SNIPPET LEVEL. The BMJ article, the PMC review of methods for handling inconclusive results, the
       Stahlmann/Reitsma/Zapf 2023 scoping review, and the STARD 2015 E&E PDF were LOCATED this run and
       read at retrieved-summary level. **A direct fetch of the STARD/Schuetz PDF at rama.mahidol.ac.th
       RETURNED AN EMPTY BODY and the paper was not read.** Titles, venues, authors and PMID confirmed;
       the 35% figure and the bias clause are reported as retrieved.]
    4. Codd, E.F. — Rule 3 of the twelve rules ("systematic treatment of null values"), and the RM/V2
       two-mark extension. — **The support for clause (C4), and the oldest form of the argument.** Rule
       3 requires nulls "**distinct from the empty character string or a string of blank characters and
       distinct from zero or any other number**," supported "for representing MISSING INFORMATION AND
       INAPPLICABLE INFORMATION in a systematic way, independent of data type." Codd's second model
       splits the mark in two: an **A-mark** for missing-but-APPLICABLE, an **I-mark** for missing
       because INAPPLICABLE. That is 818's three-way distinction one level down — a defect found (a
       value), an instrument that did not run (A-mark), a definitional dispute (I-mark: the question does
       not apply as posed) — and three-valued logic makes the consequence formal: any comparison against
       the mark yields UNKNOWN, not FALSE, so a schema without the mark converts "not known" into "not
       so."
       [CANONICAL + SNIPPET. Codd's rules cited from established knowledge; the A-mark/I-mark wording and
       Rule 3 phrasing confirmed against retrieved summaries this run (SIGMOD Record 1991 "A More General
       Model For Handling Missing Information"; Wikibooks 3VL; modern-sql.com). **No Codd primary text
       was opened.**]
    5. xUnit / pytest / GoogleTest result classes. — **The support for clause (C5).** Harnesses converged
       independently on a categorical outcome set — PASSED, FAILED, SKIPPED, plus pytest's XFAIL/XPASS —
       and GoogleTest issue #160 is an explicit request to add SKIPPED "in addition to PASS & FAIL,"
       i.e. the two-state schema was found insufficient in practice and extended. The corroborating
       detail for 818 is the recurring DEFECT around these states: tracker items record whole suites of
       skipped tests rendering GREEN, which is PREMISE-100's false-green in the harness domain and shows
       that having the third state is necessary but not sufficient — the aggregation rule must also be
       defined.
       [SNIPPET LEVEL — pytest documentation and xunit/googletest issue threads located and read at
       retrieved-summary level; none opened. Weakest-graded family here; used for existence-of-practice
       only.]
    6. ANSI/ISA-18.2-2016 and IEC 62682:2023 (aligned with EEMUA 191 Ed.4, Nov 2024). — Named because
       the queued angle asked for alarm/severity schema design. The relevant fact is that these
       standards treat **alarm CLASS** (a categorical grouping carrying its own management requirements,
       e.g. "safety alarms," "highly managed alarms") as a **separate attribute from alarm PRIORITY**
       (the ordinal urgency axis), and require rationalisation to assign both — the same two-axis result
       as SARIF, reached independently in process control.
       [SNIPPET LEVEL and WEAK — the ISA-18.2 PDF, EEMUA 191 contents listing and vendor explainers were
       located; **no standard text was read.** Do not rely on this without opening the standard.]

  Strength of support: **Strong** on (C1), (C2) and (C4); **Moderate-to-Strong** on (C3);
    **Moderate** on (C5).
    (C1) and (C4) rest on normative artefacts (a standards-body schema; the relational model's third
    rule) where the content is definitional rather than empirical. (C2) is the only clause with a
    measured cost attached and it is measured in a mature reporting discipline. (C3) is downgraded one
    grade because the primary standard was not reached and the reading is a vendor's. (C5) is existence-
    of-practice evidence only.

  Summary: The corrective proposition is strongly supported and, in one case, is already a normative
  requirement in 818's own domain. SARIF carries severity and evaluation-state as two orthogonal
  properties precisely because an earlier single-axis design mixed them, and states that severity does
  not apply when kind is anything other than `fail`. Metrology reaches the same place from the
  uncertainty side: ILAC-G8's non-binary rules carve out a zone in which NO conformity statement is
  made, and ISO/IEC 17025 makes the decision rule itself the documented artefact rather than the label.
  Diagnostic-test reporting supplies the measured cost — ignoring indeterminates BIASES the accuracy
  estimate whenever they are non-random, and only ~35% of studies report them, a base rate of exactly
  the failure 14b observed. Codd's third rule and the A-mark/I-mark split make the distinction in the
  data model, with three-valued logic showing the consequence: without the mark, "not known" silently
  becomes "not so." Where this file stops short of the item is that the register already holds the
  principle (PREMISE-103) and the instance (PREMISE-100, at High confidence). What it does not hold is
  a schema obligation naming the second axis, and that is the whole residual.

  Caveats:
    (a) THIS IS SUBSTANTIALLY PREMISE-103 AND PREMISE-100 AGAIN. Per PREMISE-151, a second recording of
        an unremediated condition is evidence of incubation, not confirmation. The disposition should be
        a SCOPE-EXTENSION, not a mint (PREMISE-138(1), PREMISE-135 bar the re-mint).
    (b) A THIRD LABEL RELOCATES THE JUDGEMENT; IT DOES NOT DISCHARGE IT. The diagnostic literature is
        explicit that once indeterminates are visible someone must still handle them, and the honest
        treatments are BOUNDING (best-case/worst-case reclassification) or a 3x2 intention-to-diagnose
        presentation — both of which are COMPUTATIONS, not labels. Adding "not-executed" to the
        vocabulary without deciding how it aggregates into `last_qc_outcome` reproduces the false-green
        in a new spelling; the harness sources show this happening in practice.
    (c) MORE STATES COST LEGIBILITY, AND THE ALARM LITERATURE IS THE ONE THAT WARNS ABOUT IT. The
        register already carries the alarm-fatigue/over-saturation concern (PRESUMPTION-163,
        MONITOR-140, and PREMISE-154's rubber-stamp finding). A five-member `kind` enum on every check
        in a fleet report is a real legibility cost against a benefit that has not been measured here.
        SARIF's cost is borne by machines; C2A2's would be borne by a human reader.
    (d) DOMAIN TRANSFER IS CLEAN FOR TWO OF THE THREE INSTANCES AND STRAINED FOR THE THIRD. "Small
        defect found" maps to `fail`+`level: warning`; "instrument did not execute" maps to
        `notApplicable`. **"Disagreement about the definition" has no clean SARIF member** — `review` and
        `open` mean "the tool could not decide," not "two parties define the measurand differently."
        That third case is closer to PREMISE-101/161 territory (an undefined measurand) than to a
        results-schema problem, and the literature located here does not reach it. This is the
        weakest-supported third of the item.
    (e) SOURCE INDEPENDENCE IS LOWER THAN SIX SUGGESTS, AND VERIFICATION DEPTH IS SHALLOW. Sources 1,
        2, 5 and 6 are all "a standards body or tool ecosystem added a second axis" — one argument in
        four costumes. **Not one primary standard was fetched and read in full this run**; the single
        full-text read is a vendor explainer. Per PREMISE-132 (citing is not verifying), this file's
        citation count materially overstates its evidential depth, and the SARIF clause — the load-
        bearing one — should be confirmed against the OASIS text before it is quoted in a premise.

  Search scope: GOOD but SHALLOW. Searched: SARIF result kind/level; ILAC-G8 and ISO/IEC 17025 decision
    rules and guard banding; STARD 2015 and the inconclusive-results methods literature; Codd nulls and
    three-valued logic; xUnit/pytest/GoogleTest outcome classes; EEMUA 191 / ISA-18.2 alarm
    classification. NOT SEARCHED, and each would materially change this file: (i) **CVSS / CWE severity
    taxonomies and the static-analysis "unable to analyse" state** in specific tools (the queue asked
    for severity taxonomies in static analysis and this run reached the interchange FORMAT, not the
    taxonomies); (ii) **GUM (JCGM 100:2008) and VIM3 on indeterminate results proper** — the queue named
    VIM/GUM and this run reached ILAC-G8 instead, which is the conformity-decision layer above them;
    (iii) **negative-control design**, named in ASSUMPTION-1106's angle and not touched at all, which is
    the right apparatus for "prove the instrument would have fired"; (iv) **HL7/LOINC and laboratory
    result-status vocabularies**, which have a mature "cancelled / not performed / specimen unsuitable"
    enumeration that is probably the closest existing analogue to C2A2's need.

  Recommendation: **SUPPORTED (Strong)** for the corrective proposition; equivalently NO-SUPPORT-FOUND
  for the presumption as worded. **Disposition should be a SCOPE-EXTENSION OF PREMISE-103 into the
  results-schema domain, not a new premise.** Four carries:
    1. NO NEW MINT. PREMISE-103 holds "kind-difference, not degree-difference" and PREMISE-100 holds the
       false-green instance at High confidence. The extension is narrow: PREMISE-103 currently binds
       CONFIDENCE LABELS over evidence; extend it to OUTCOME LABELS over checks.
    2. THE SUBSTANTIVE ADDITION IS THE SECOND AXIS, WITH NAMED MEMBERS. Every check result should carry
       a categorical `kind` (executed-and-clean / executed-and-found-defect / did-not-execute /
       not-applicable / definition-disputed) SEPARATE from any severity, and severity should be
       undefined where kind is not "found-defect" — SARIF's own rule.
    3. THE AGGREGATION RULE IS THE REAL DELIVERABLE AND MUST BE DECIDED WITH THE SCHEMA (caveat b).
       Specify now what `last_qc_outcome` becomes when kind is `did-not-execute`. The defensible answer
       from both the ILAC and STARD sources is that it is NOT `pass`: either the day carries no outcome,
       or it carries a bounded pair. Naming the state without fixing the roll-up leaves the 66-of-307
       days green.
    4. THE THIRD INSTANCE SHOULD BE SPLIT OFF (caveat d). "Disagreement about the definition" is not a
       results-schema problem and this search found no schema that handles it. Route it to the
       measurand family (PREMISE-101/114/161) rather than folding it into the enum, where it will be
       mislabelled as "could not decide."
