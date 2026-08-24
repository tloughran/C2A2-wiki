SEARCH-FOR-ASSUMPTION-1094:
  Date searched: 2026-08-16
  Original item: ASSUMPTION-1094
  Original statement: **THE DAY'S BEST WORK WAS SIX INDEPENDENT REFUSALS TO PROPAGATE A RECORDED FIX.**
  Across eleven Summa runs, six separate ids that "look wrong from the standing record" were verified
  correct at the body and deliberately left alone. "The band table is a list of observed wrong-uses, not
  a rename table" — the recorded `Levin PRS-30 → 17` repair "would have corrupted Day 158"; "CROSS-013 is
  *correct* on 222 and 223 … a sweep would have broken both"; "Stump PRS-05 on Day 053 and Friston PRS-16
  on Day 054 both look wrong from the standing record and are correct at the body"; "The Hoffman PRS-01,
  PRS-02 bundle on Days 046 and 050 is exact, and I deliberately left it alone"; "Rohr PRS-06 and PRS-07
  return empty under a padded lookup and are both exact … Two false escalations avoided in this run
  alone." **The record's storage form (id → correction) asserts a scope the evidence does not have.**

  POLARITY NOTE — what was searched FOR. The item is worded as a finding rather than as a defective
  belief, but the belief it corrects is real and unstated: that a recorded repair is a RULE. The
  proposition searched FOR has four clauses: (i) A DEFECT RECORD CAPTURES INSTANCE-LEVEL EVIDENCE, and
  storing it keyed by an identifier alone silently promotes an existentially-quantified observation
  ("this id was used wrongly HERE") into a universally-quantified rule ("this id is wrong"), which is a
  representation error and not a discipline failure; (ii) APPLYING A RECORDED CORRECTION TO NEW INSTANCES
  HAS A MEASURED AND SUBSTANTIAL ERROR RATE, so refusing to propagate is a defensible default rather than
  timidity; (iii) MATURE QUALITY SYSTEMS ALREADY SEPARATE the correction of the found instance from the
  question of whether the condition exists elsewhere, and require the latter to be EVALUATED, never
  assumed in either direction; (iv) THE FORMAL FIX IS TO STORE THE CORRECTION WITH ITS CONDITION — the
  scope on which it holds — rather than with its key, and the database literature has a named
  construct for exactly this. "SUPPORTED" means these four clauses are supported.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1094
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Collected the six refusals verbatim across five transcripts and identified the shared claim
           none of them states. [stated]
      15a: Searched for supporting literature on the representation clause and on the propagation error
           rate; performed the arithmetic the item's evidence permits, and disclosed why it is not a
           precision estimate.
    Current status: SUPPORTED (Strong on clauses ii-iv; Moderate-Strong on clause i)

  REGISTER CHECK (performed BEFORE writing this file):
    Grepped `validated_premises.md` for: sweep, propagat, precedent, generalis/generaliz, scope, batch,
    refactor, exception, detection.
    Found and read in full:
      - **PREMISE-135** (2026-07-29, ACTIVE, Moderate) — **THE NEAREST ANTECEDENT AND IT IS CLOSE.**
        "TERMINALITY IS PURCHASED BY ENUMERATING THE DOMAIN, NOT BY ACCUMULATING INSTANCES… There is no
        schema-level warrant for 'generalise from the instances seen'; an inductive step is licensed by a
        stated material fact about the domain." It owes three things: (a) THE POPULATION, (b) THE
        TERMINATION CRITERION, (c) ONE SEVERE TEST out of sample. **ASSUMPTION-1094 is PREMISE-135's
        requirement (a) being enforced in practice by six runs that had never read it** — the band table
        claims generality over a population ("every occurrence of this id") that was never enumerated,
        and the runs went and looked instead. The register therefore already holds the epistemics. What
        135 does NOT contain is the STORAGE clause: it governs the warrant of a generalisation, not the
        data structure that manufactures one silently.
      - **PREMISE-143 clause (2)** (2026-08-05, ACTIVE, High) — "THE CORRECTION IS NOT SAFE: 14.8-24.4% of
        sampled post-release fixes in four operating systems were themselves incorrect and reached users
        (Yin et al. 2011). A correction issued and unreviewed carries a one-in-five-to-one-in-seven prior
        of being wrong, so 'corrected' is not a terminal state even for the single instance." This is
        clause (ii) ALREADY HELD, for the single-instance case. 1094 extends it to the propagated case,
        which is strictly worse, and supplies the extension's evidence below.
      - **PREMISE-113** (2026-07-21, ACTIVE, Moderate) — a rule-based detector's findings are evidence
        about the DETECTOR until its precision is measured; false-positive rates of 76-90%+ are inside
        the normal operating band; and the load-bearing clause, that a labelled corpus with known-genuine
        AND known-clean cases is required before any reading is evidence about the corpus. **The band
        table read as a rename rule IS a rule-based detector**, and 113 governs it directly. This is the
        premise that forbids the arithmetic below from being reported as a precision figure.
      - **PREMISE-160** (2026-08-14, ACTIVE, High) — a named defect explanation is discharged by ONE
        DISCONFIRMING CASE; asymmetric case selection is the failure. The six refusals ARE six
        disconfirming cases for "the band table is a rename table," which by 160's own standard
        discharges that reading six times over.
      - **PREMISE-107** (ACTIVE, High) — the diagnose-before-repair scope guard, with its cost term:
        diagnosis is 60-70% of mean time to repair, and the rule binds for remedies that are expensive
        or IRREVERSIBLE. A corpus sweep over 307 files is irreversible in the sense that matters (it
        silently changes correct data), so 107 binds in its strict form here, and the verify-at-the-body
        cost that ASSUMPTION-1098 complains about is 107's predicted cost, not an overrun.
      - **PREMISE-128** (ACTIVE) — a defect producing no error and plausible-looking output cannot be
        certified benign; its blast radius is unknown at the point of failure; the response is
        reconciliation against an uncorrupted source. A propagated wrong rename is exactly this class:
        the corrupted day still parses, still renders, and emits nothing.
      - **PREMISE-101** (ACTIVE, High) and **PREMISE-136** (ACTIVE) — quantities are properties of a
        declared (scope, method, time) reading, and the achievable denominator is fixed by declared
        scope. Both bind the "third id this week" count.
    CONCLUSION OF THE CHECK: **HEAVY OVERLAP ON THE EPISTEMICS AND ON THE ERROR-RATE CLAUSE; NO
    NOVELTY-FLAG.** Seven ACTIVE premises bear on this. The residual is two things:
      (R1) **THE STORAGE FORM IS THE MECHANISM, AND NO PREMISE ADDRESSES A DATA STRUCTURE.** PREMISE-135
           says a generalisation needs a stated population. 1094's contribution is that the RECORD'S KEY
           SUPPLIES ONE BY DEFAULT — writing `id → correction` makes the id the population without anyone
           deciding that it should be, so the over-generalisation is committed by the schema at write
           time and merely executed by the reader. That is a different and cheaper intervention point
           than "reason better," and it is the clause the located literature supports most sharply.
      (R2) **THE PROPAGATED-CORRECTION ERROR RATE IS UNQUANTIFIED IN THE REGISTER.** PREMISE-143 holds
           14.8-24.4% for a fix applied to the instance it was written for. Nothing holds a figure for a
           fix applied to a DIFFERENT instance, which is the operation 1094 concerns and which is
           strictly more error-prone. A figure is located below.
    DECLARED LIMITATION: this was a string grep, measured at ~56% recall by the 2026-08-14 15c run
    (ASSUMPTION-1052). The list above is a **LOWER BOUND** and the true overlap is likely larger.

  Supporting evidence found: Yes

  Sources:
    1. Bohannon, P., Fan, W., Geerts, F., Jia, X. & Kementsietsidis, A. (2007), "Conditional Functional
       Dependencies for Data Cleaning," ICDE 2007; extended as Fan, W., Geerts, F., Jia, X. &
       Kementsietsidis, A. (2008), "Conditional functional dependencies for capturing data
       inconsistencies," *ACM Transactions on Database Systems* 33(2). — **The formal statement of
       clauses (i) and (iv), and the source of the vocabulary this item most needs.** The construct was
       invented for precisely the defect 1094 names. Ordinary functional dependencies "were developed
       mainly for SCHEMA DESIGN" and hold over the WHOLE relation; CFDs "aim at capturing the consistency
       of data by ENFORCING BINDINGS OF SEMANTICALLY RELATED VALUES," and a CFD holds only on the SUBSET
       of tuples selected by an attached PATTERN TABLEAU. Translated to the band table: the recorded
       repair `Levin PRS-30 → 17` is being stored as if it expressed the FD `id → correct_id`, a
       relation-wide constraint; the evidence actually supports the CFD `(id, day) → correct_id` with a
       tableau naming the days on which the wrong-use was observed. The two have identical surface syntax
       and completely different scope, which is exactly why "the band table is a list of observed
       wrong-uses, not a rename table" was a discovery rather than a reading. **The existence of a
       fifteen-year data-cleaning literature built on this distinction is the finding: an over-general
       repair rule is a catalogued defect class with a named remedy, not a local lapse.**
       [SNIPPET LEVEL — the ICDE 2007 and TODS 2008 records were located this run at the Edinburgh
       Research Explorer, dblp, Google Research and the Antwerp mirror of the TODS paper; the FD/CFD
       contrast and the value-binding motivation were read from retrieved abstract text. NEITHER PAPER
       WAS READ IN FULL, and the search explicitly returned no confirmation of the pattern-tableau
       detail from a primary source this run. The pattern-tableau mechanism as described above is
       CANONICAL knowledge of CFDs, not verified text. Do not quote a definition or a theorem onward.]
    2. Bader, J., Scott, A., Pradel, M. & Chandra, S. (2019), "Getafix: Learning to Fix Bugs
       Automatically," *Proceedings of the ACM on Programming Languages* 3 (OOPSLA), article 159;
       arXiv:1902.06111; deployed at Facebook. — **The quantified answer to clause (ii), from the single
       closest analogue to the operation 1094 refused.** Getafix does exactly what a sweep from the band
       table would do: it learns fix patterns FROM PAST HUMAN-WRITTEN FIXES and applies them to new
       instances of the same reported defect, with a hierarchical clustering step that generalises
       patterns from specific to general and a ranking step that uses the CONTEXT OF THE CHANGE to pick
       among them. On 1,268 bug fixes across six static-analyser-reported categories in Java, it
       "predicts exactly the human-written fix as the top-most suggestion **between 12% and 91% of the
       time, depending on the bug category**," and the top-5 suggestions contain the fix for **526 of the
       1,268** bugs (41.5%). **Read as a bound on propagation: an industrially-deployed system built for
       this task, with a learned context model that a hand-maintained id→correction table does not have,
       is wrong at its first suggestion for as much as 88% of instances in its worst category and for
       roughly three-fifths of all instances even given five guesses.** The six C2A2 runs were performing
       Getafix's context-ranking step by hand, at the body, and reaching "none of the above" six times.
       [SNIPPET LEVEL — the OOPSLA 2019 session record, the ACM DL entry, the arXiv listing and the Meta
       engineering post were located this run and the 12-91% / 526-of-1268 figures were read from
       retrieved summaries. THE PAPER WAS NOT READ. NOTE the direction of the caveat: 12-91% is an
       ACCURACY figure for a top-1 suggestion, not a defect-introduction rate — a wrong suggestion in
       Getafix's setting is reviewed by a human before landing, whereas a sweep in C2A2's setting lands
       silently. The transfer is a fortiori but it is a transfer, not a measurement of C2A2.]
    3. Qi, Z., Long, F., Achour, S. & Rinard, M. (2015), "An Analysis of Patch Plausibility and
       Correctness for Generate-and-Validate Patch Generation Systems," *ISSTA 2015*. — **The
       plausible/correct distinction, which is the exact shape of "looks wrong from the standing record
       and is correct at the body," inverted.** The paper introduced the discrimination between a
       PLAUSIBLE patch (one that satisfies the acceptance oracle) and a CORRECT one, by manually
       inspecting the patches earlier heuristic repair systems had reported as successes, and the
       finding that made it influential is that the two sets diverge badly. The mechanism named is the
       one that operates here: **the acceptance oracle is INCOMPLETE**, so the search optimises against a
       proxy and returns changes that satisfy the proxy while being wrong about the artefact. In C2A2 the
       incomplete oracle is the standing band table consulted without the body; a padded-lookup miss or a
       recorded wrong-use is a plausibility signal, and the six runs are the manual-inspection step this
       literature says must exist. Subsequent work (Long & Rinard 2016; Le, Thung, Lo & Le Goues, EMSE
       2018, "Overfitting in semantics-based automated program repair") established that repair systems
       "tend to produce more OVERFITTING patches than correct patches" — an overfitting patch being one
       fitted to the observed instances that does not generalise, which is PREMISE-135's failure arriving
       from the software-repair side.
       [SNIPPET LEVEL — the ISSTA 2015 paper's existence, title, authors and venue confirmed via multiple
       secondary citations located this run; the plausible/correct distinction and the incomplete-oracle
       explanation read from retrieved summaries and from the EMSE overfitting paper's framing. NEITHER
       PRIMARY PAPER READ. The "more overfitting than correct" attribution to Long & Rinard 2016 comes
       from a secondary source and should be checked before it is quoted with a proportion attached.]
    4. US NRC, 10 CFR Part 50 Appendix B, Criterion XVI ("Corrective Action"); NRC Regulatory Issue
       Summary 2015-08 Rev. 1; NEI 08-02 Rev. 3, *Corrective Action Processes for New Nuclear Power
       Plants*. — **Clause (iii): the mature-practice separation of "fix this one" from "does this exist
       elsewhere," as a MANDATORY EVALUATION rather than an assumption in either direction.** Criterion
       XVI requires that conditions adverse to quality — "failures, malfunctions, deficiencies,
       deviations, defective material and equipment, and nonconformances" — "be promptly identified and
       corrected," and that for SIGNIFICANT conditions the cause be determined and action taken "to
       preclude repetition." The doctrine built on it names the second question separately as **EXTENT OF
       CONDITION**: "when conditions are identified, the extent to which OTHER ITEMS AND ACTIVITIES may
       be affected should be considered so that appropriate action is taken," and the disposition of a
       corrective action report records the cause, THE EXTENT OF CONDITION, the actions addressing
       causes, and an implementation plan as separate fields. **The structural lesson for C2A2 is the
       field list, not the regulation: a discipline that has spent forty years on this stores the
       instance correction and the scope determination as DISTINCT, SEPARATELY DISPOSITIONED OBJECTS,
       because collapsing them is how a single finding becomes either an unbounded sweep or an
       unexamined one-off.** The band table collapses them into a key.
       [SNIPPET LEVEL — the Criterion XVI text, the RIS 2015-08 Rev. 1 extent-of-condition language and
       the NEI 08-02 Rev. 3 disposition-field list were located this run at NRC-hosted PDFs and read from
       retrieved passages; NO document was fetched and read in full. REGULATORY / INDUSTRY-GUIDANCE
       GRADE, labelled as such — this is practice doctrine, not an empirical result, and it carries no
       measurement of how often extent-of-condition reviews are right.]
    5. Yin, Z., Yuan, D., Zhou, Y., Pasupathy, S. & Bairavasundaram, L. (2011), "How do fixes become
       bugs?", ESEC/FSE 2011 — 14.8-24.4% of sampled post-release fixes in four operating systems were
       themselves incorrect. — Supplies the single-instance baseline against which the propagated case
       must be worse. [CANONICAL — ALREADY HELD IN THE REGISTER at PREMISE-143 clause (2), where it is
       marked as cited by both directions and NOT independently verified. NOT re-verified this run.]
    6. Codd's relational normalisation and the update-anomaly result (2NF/3NF/BCNF): a relation storing a
       fact at a key on which it is not fully functionally dependent suffers insertion, update and
       deletion anomalies, and the remedy is to decompose so that every fact is stored at the key it
       actually depends on. — The textbook form of clause (i): `id → correction` is a partial dependency
       on a composite key `(id, day)`, and the observed failure (a correct update to Day 158 requires
       knowing which days the rule covers) is a textbook update anomaly.
       [CANONICAL — cited from established knowledge; the framing was checked against retrieved teaching
       material this run but NO primary source (Codd 1970/1971, or a database text) was read. This is a
       useful ANALOGY for stating the defect precisely; it is not evidence, and it should not be
       presented as though a database theorist had written about band tables.]

  THE ARITHMETIC, and why it is NOT a precision estimate:
    WHAT THE DAY SHOWS. Six ids across five transcripts, each flagged by the standing record and each
    verified correct at the body: `Levin PRS-30` (Day 158), `CROSS-013` (Days 222, 223), `Stump PRS-05`
    (Day 053), `Friston PRS-16` (Day 054), the `Hoffman PRS-01/PRS-02` bundle (Days 046, 050), and
    `Rohr PRS-06/PRS-07`. One run reports "the third id this week."
    THE TEMPTING FIGURE AND WHY IT IS BARRED. Six of six flagged ids were false alarms, which invites
    "the band table's precision as a rename rule is 0%." **PREMISE-113 forbids this and PREMISE-124(a)
    forbids it a second time.** The six were not a random draw from the flagged population; they are the
    cases six runs chose to open the body on, and a reviewer opens the body precisely when something
    looks off. This is selection on the very variable being estimated. The denominator is also undeclared
    (PREMISE-136): six of how many flags, across what scope, over what window? Nobody has written it.
    **The only defensible statement is a LOWER BOUND ON HARM AVERTED, not a rate: at least six corruption
    events did not occur, on days that were clean.**
    WHAT WOULD MAKE IT A RATE, and it is cheap. Per PREMISE-113's labelled-corpus clause: take the next
    N flags in file order — not the suspicious ones — open the body on all N, and record both cells. That
    yields a precision figure for the band-table-as-rename-rule and, run against a set of known-genuine
    wrong-uses, a recall figure too. Without both, "the record over-claims" is supported qualitatively
    (six disconfirming cases, and per PREMISE-160 one would do) but has no magnitude.
    THE ASYMMETRY THAT MAKES THE REFUSAL CORRECT EVEN AT UNKNOWN PRECISION. A false escalation costs a
    reviewer's minutes and is visible. A false propagation writes a wrong id into a clean day, emits no
    error, renders normally, and enters the standing record as precedent for the NEXT sweep — PREMISE-128's
    silent-corruption class, with a feedback path. The loss function is lopsided by orders of magnitude,
    which is why the correct default does not wait on the precision measurement.

  Strength of support: **Strong** on clause (ii) — Getafix is a directly analogous, industrially deployed,
  quantified system and its numbers bound the operation from above; and on clause (iii) — a mature
  regulated discipline stores instance-correction and extent-of-condition as separate dispositioned
  objects. **Moderate-Strong** on clauses (i) and (iv): the CFD construct is exactly on point and its
  existence as a research programme is itself the argument, but it was reached at snippet level only.
  **The support is for the item's stated general claim, not for its six particular verdicts** — no source
  here says anything about whether `CROSS-013` is right on Day 222, and the runs' body-level readings are
  the only evidence for that.

  Summary: The item's unstated claim — that the record's storage form asserts a scope its evidence does
  not have — is supported, and the sharpest support is that the database community built a whole
  constraint class to fix this exact representation error. Functional dependencies were designed for
  schema design and hold over an entire relation; conditional functional dependencies were introduced
  because real data-cleaning rules hold only on a subset, and must therefore carry the subset with them.
  A band table keyed `id → correction` is an FD asserted where the evidence supports a CFD, and the
  promotion happens silently at write time, which is why six independent runs had to discover it
  separately at read time. On the cost of getting this wrong, Getafix supplies the closest available
  figure: a deployed system that learns fix patterns from past human fixes and ranks them by change
  context predicts the human-written fix at top-1 between 12% and 91% of the time, and needs five guesses
  to reach 41.5% of 1,268 bugs — so even a well-engineered propagation of a recorded repair to new
  instances is wrong most of the time in its harder categories. Automated program repair supplies the
  mechanism: an incomplete acceptance oracle produces PLAUSIBLE-but-incorrect changes, and repair systems
  overfit to the instances they were built from. The register already holds the neighbouring results —
  PREMISE-135 that generality is purchased by enumerating the domain rather than accumulating instances,
  PREMISE-143(2) that even a single-instance correction carries a 15-24% prior of being wrong, PREMISE-113
  that a rule-based detector's output is evidence about the detector — so 1094's genuine increment is
  narrow but real: the DATA STRUCTURE is where the over-generalisation is committed, and nuclear
  corrective-action practice shows what the fix looks like, which is to store the instance correction and
  the extent-of-condition determination as two objects with independent lifecycles rather than as one key.

  Caveats:
    (a) THE SIX VERDICTS ARE UNAUDITED AND WERE PRODUCED BY THE RUNS THAT REPORT THEM. Per PREMISE-124,
        a favourable number produced inside the instrument being evaluated licenses no completeness or
        quality claim; the runs that declare "correct at the body" are the same runs that would have had
        to do the sweep. Nothing external confirms that the six ids are in fact correct. Six independent
        agreements are also weak evidence per PREMISE-152 (homogeneous, unguided) and per PREMISE-120
        (checks sharing corpus, model and execution context are re-runs, not independent confirmations)
        — and the item's own "six INDEPENDENT refusals" framing is exactly the word 120 governs. **The
        cheap external check is one human spot-check of one of the six.**
    (b) THE OPPOSITE ERROR IS REAL AND NOTHING HERE BOUNDS IT. Extent-of-condition doctrine exists
        because under-propagating is also a failure mode: a genuine defect present in twenty files and
        fixed in one is a regulated finding in every discipline that has a corrective-action programme.
        This file locates no measurement of how often a refusal-to-propagate leaves real defects
        standing, and six refusals in one day is equally consistent with a table that is 0% precise and
        with reviewers who have become reluctant. **The literature supports "evaluate the extent," NOT
        "do not sweep."** A blanket no-propagation rule would be this item over-read.
    (c) THE COST IS REAL AND IS ALREADY BITING. ASSUMPTION-1098 records a run naming this discipline as
        the cause of its token overrun: "the verify-at-the-body discipline is what costs it." PREMISE-107
        predicts this — diagnosis is 60-70% of mean time to repair — and endorses paying it for
        irreversible remedies, which a silent corpus write is. But the endorsement is conditional and the
        cost is measurable, so the honest framing is a trade priced at roughly the observed overrun, not
        a free win. The CFD framing is what makes the cost fall: **a repair stored with its scope needs
        verifying once, not once per reader.**
    (d) THE GETAFIX TRANSFER IS A FORTIORI BUT IT IS A TRANSFER. Getafix operates on Java ASTs with a
        static analyser as oracle and a human reviewer before landing. C2A2 operates on markdown ids with
        a hand-maintained table and no reviewer. The direction of the difference favours the item — less
        context, weaker oracle, no gate — but the 12-91% band is a measurement of Getafix, not of a band
        table, and must never be quoted as C2A2's rate.
    (e) THE CFD SOURCE IS SNIPPET-LEVEL AND IS THE FILE'S LOAD-BEARING FORMAL CLAIM. If a disposition
        wants to write "store the repair as a conditional dependency with its scope," the TODS 2008
        paper should be read first. The pattern-tableau mechanism as stated above is canonical knowledge,
        not verified text from this run, and that is the weakest link in the file.
    (f) PUBLICATION BIAS RUNS TOWARD THE ITEM HERE, NOT AWAY. Automated-repair papers report the
        plausible/correct gap because reporting it is the contribution; systems whose propagated fixes
        were fine do not generate papers. The 12-91% figure is from a paper reporting its own system's
        success, which cuts the other way and is the more reliable of the two.

  Search scope: GOOD and BROAD on automated repair and learned-fix propagation (Getafix, Qi et al.,
  the overfitting literature) — all at snippet level, none read in full. GOOD on the conditional-dependency
  formalism at snippet level. GOOD on corrective-action / extent-of-condition doctrine at
  regulatory-guidance grade. NOT SEARCHED, and each would materially change this file: (i) **CODEMOD /
  LARGE-SCALE-CHANGE FALSE-POSITIVE RATES AT INDUSTRIAL SCALE** — Google's ClangMR and Rosie
  large-scale-change practice, and the rename-refactoring literature (a type-aware rename is safe; a
  textual one is not), which is the closest thing to a base rate for "applying a recorded correction
  mechanically across a corpus" and was identified but not reached; (ii) the ARCHIVAL / SCHOLARLY-EDITING
  literature on emendation policy and the treatment of a witness reading, which is the correct home
  discipline for "the body is the authority and the standing record is a note about it" and was not
  searched at all; (iii) any measurement of the UNDER-propagation error rate, which Caveat (b) says is
  the missing half; (iv) CFD DISCOVERY algorithms, which would tell C2A2 whether the band table's true
  scope can be inferred from the corpus rather than verified file by file — the direct route to
  Caveat (c)'s cost problem.

  Recommendation: **SUPPORTED (Strong on the propagation-cost and mature-practice clauses;
  Moderate-Strong on the representation clause).** Four carries:
    1. **THE DISPOSITION SHOULD BE A SCHEMA CHANGE, NOT A DISCIPLINE.** Six runs reached the right
       behaviour with no contract clause requiring it, which is impressive and unreliable — per
       PREMISE-116 a finding does not change conduct, and per Norman et al. (carried as a binding
       prohibition in PREMISE-160) asking runs to "be more careful" is contraindicated by the strongest
       available synthesis. **Add a scope field to the band table.** Every row records the days on which
       the wrong-use was OBSERVED, and a reader may act without opening the body only within that set.
       That is the CFD's pattern tableau, it is one column, and it moves the fix from the reader to the
       writer.
    2. **RENAME THE ARTEFACT.** One run already did the work: "the band table is a LIST OF OBSERVED
       WRONG-USES, not a rename table." Per PREMISE-140, a record must be named by what it observed, not
       by what a reader might do with it. `observed_wrong_uses.md` cannot be swept from; `band_table.md`
       invites it. This is a filename and a header line.
    3. **SPLIT THE OBJECT, PER THE CORRECTIVE-ACTION FIELD LIST.** An instance correction and an
       extent-of-condition determination are two records with independent lifecycles. This is the same
       move PREMISE-167 clause (3) already requires for measurements and escalations, and PREMISE-143(3)
       already requires for retractions — **three separate premises now converge on "split the object,"
       which is itself worth noting to 15c.**
    4. **DO NOT REPORT SIX-OF-SIX AS A PRECISION FIGURE, AND RUN THE CHEAP MEASUREMENT INSTEAD.** Per
       PREMISE-113 and PREMISE-124(a) the six are a selected sample and yield no rate. Opening the body
       on the next N flags in FILE ORDER rather than in suspicion order costs one run and converts the
       day's best qualitative finding into a number that can be acted on — including, if precision turns
       out to be high, the finding that the six were unlucky and the table is mostly a rename table
       after all.
