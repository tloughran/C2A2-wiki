SEARCH-AGAINST-PRESUMPTION-703:
  Date searched: 2026-08-07
  Original item: PRESUMPTION-703
  Original statement: That a parser bug announces itself by an implausible result; "the tell was
    the 100% miss rate; real defects are sparse" generalised in the same summary that records a
    near-miss it would not have caught (a plausible 21-pair difference).

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-703
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Read the stated heuristic against the one near-miss in the same run that it would not
        have caught — a plausible 21-pair difference against an implausible 100% miss rate.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Meta Engineering, 2021 and 2022. "Silent data corruption: Mitigating effects at scale"
       (engineering.fb.com, 2021-02-23) and "Detecting silent errors in the wild: Combining two
       novel approaches to quickly detect silent data corruptions at scale" (engineering.fb.com,
       2022-03-17). Both posts located this session with dates and titles as given; author lists
       [UNVERIFIED — the posts were not opened in full]. The defining property of a silent data
       corruption is stated as exactly the negation of this presumption: SDCs produce incorrect
       results *without* raising logs, exceptions or error reports, leave no trace in system
       logs, and therefore stay undetected within workloads and propagate across services. Meta's
       response is not a plausibility heuristic but two dedicated detection programmes —
       Fleetscanner, which tests opportunistically by piggybacking on reboots, firmware upgrades
       and reimages, and ripple, which tests in production. An organisation that could rely on
       implausible results to reveal corruption would not have built either.
    2. Google Research. "Detection and Prevention of Silent Data Corruption in an Exabyte-scale
       Database System" (research.google publications record located this session; authors,
       year and venue [UNVERIFIED]). Supporting material located alongside it (Google Cloud
       support article on silent data corruption) states the general operating position that for
       every *detected* error there are some number of *undetected* errors which in rare but not
       black-swan events corrupt data, and that the defence is software checksums — a sentinel
       mechanism carried with the data — rather than inspection of results for implausibility.
       The Google File System paper (2003) is cited there as having taken this position from the
       beginning.
    3. Barr, E.T., Harman, M., McMinn, P., Shahbaz, M. and Yoo, S. — the test-oracle literature.
       Located this session via the ACM DL record for "Oracle problem in software testing,"
       Proceedings of the 26th ACM SIGSOFT International Symposium on Software Testing and
       Analysis (ISSTA 2017), DOI 10.1145/3092703.3098235 (title, venue and DOI confirmed; the
       author list given here is the standard attribution for the underlying oracle-problem
       survey and was *not* confirmed from the record itself — treat as [UNVERIFIED]). The
       directly relevant concept is *failed error propagation*: given a faulty execution state,
       an oracle may be unable to expose the fault if it is placed at a program point with no
       access to the incorrect state, or at a point where the state is no longer corrupted. A
       plausibility check on a final result is the weakest possible oracle placement — external,
       terminal, and with access only to an aggregate. The literature's conclusion is that
       internal oracles are less subject to failed error propagation than external ones, which
       is a direct argument for instrumenting the parser rather than inspecting its output.
    4. Mutation-testing literature. "Are mutants a valid substitute for real faults in software
       testing?" Proceedings of the 22nd ACM SIGSOFT FSE, DOI 10.1145/2635868.2635929 (title,
       venue and DOI confirmed this session; authors [UNVERIFIED — commonly attributed to Just,
       Jalali, Inozemtseva, Ernst, Holmes and Fraser, 2014, but not confirmed here]). Supporting
       practitioner and academic material located this session (LittleDarwin, arXiv 1707.01123;
       PIT/Java tutorial material) states the method plainly: inject known faults and check
       whether the detector catches them; a surviving mutant is a demonstrated deficiency in the
       detector. This supplies the constructive alternative to plausibility — a *measured*
       detection rate rather than an assumed one — and it is the technique that would have
       revealed in advance that a 21-pair difference passes undetected.
    5. Sentinel/canary records in data pipelines. Practitioner literature located this session
       (Stacksync, "How to Detect Silent Failures in MuleSoft API Flows"; Inference Systems
       glossary entry on canary tests for data; several data-observability vendor posts). All
       non-peer-reviewed and cited only for the design pattern and the consensus framing: silent
       failures are workflows that *complete without errors* while failing to produce correct
       data, and the stated detection requirement is reconciliation, row-level validation and
       synthetic sentinel transactions rather than reliance on technical error logs or
       downstream implausibility. One peer-reviewed anchor was located but not opened:
       "Auto-Validate by-History: Auto-Program Data Quality Constraints to Validate Recurring
       Data Pipelines," arXiv 2306.02421 (identifier and title confirmed; authors and venue
       [UNVERIFIED]), which formalises the declarative-constraint approach.
    6. Missed-detection base rates in inspection. Located this session in the industrial
       inspection literature (Springer, "Aluminum profile surface defect detection system
       integrating deep learning and industrial internet of things," 2025; Wiley Engineering
       Reports 2026 on parts surface defect detection). Reported that skilled human visual
       inspectors detecting defects above 0.5 mm still carry a missed-detection rate of roughly
       15-20%, that small and subtle flaws are systematically the ones overlooked, and that
       prolonged inspection reduces attentiveness. [Figures taken from search summaries; papers
       not opened.] The transferable point is the shape of the curve, not the number: detection
       by inspection is strongly size-dependent, and the errors that survive are precisely the
       small, plausible ones — which is the class the 21-pair near-miss belongs to.

  Strength of challenge: Strong

  Summary: The heuristic is not merely incomplete; it is anti-correlated with the risk it is
    supposed to manage. "Real defects are sparse, so a 100% miss rate is the tell" says that
    implausibility reveals bugs — but implausibility is a function of the bug's *magnitude*,
    not its severity, so the heuristic's detection probability is highest for the errors that
    would have been caught anyway and lowest for the errors that will persist. The entire
    silent-data-corruption literature at Meta and Google exists because the failures that matter
    at scale are defined by not announcing themselves, and both organisations answered with
    sentinel mechanisms (checksums, synthetic transactions, opportunistic and in-production
    fault injection) rather than with output-plausibility inspection. The oracle-problem
    literature explains why: a plausibility check is an external, terminal oracle, the placement
    most vulnerable to failed error propagation, whereas an internal check on the parser's own
    invariants sees the corrupted state directly. The item's own record settles the matter
    empirically — the same run contains a near-miss that the heuristic does not cover, which
    means the heuristic's miss rate on this system's own defect population is already known to
    be non-zero, and was known at the moment it was generalised.

  STEELMAN:
    Item: PRESUMPTION-703
    Strongest counterargument: The heuristic is being read as a *detector* when it was offered
      as an *explanation of how this particular bug came to light*. "The tell was the 100% miss
      rate" is a true report about one diagnosis; it does not claim that every parser bug will
      produce such a tell, and 14b may be inflating a post-hoc narrative into a stated policy.
      There is also a genuine defence of outcome-based checks on their own terms: prior
      knowledge about defect sparsity is real information, and a result that violates a
      well-founded prior *is* strong evidence, in the ordinary Bayesian sense. Sparse-defect
      priors are exactly how anomaly detection works, and dismissing them because they miss
      subtle cases would be to demand that a screening test also serve as a confirmatory one. The
      cost argument is also real: sentinel records, seeded faults and internal invariants all
      require building and maintaining machinery, and this batch contains a separate finding
      (PRESUMPTION-712) that C2A2's machinery already outproduces its capacity to consume. A
      cheap heuristic that catches the gross failures, honestly labelled as catching only gross
      failures, may be the right allocation for a system of this size — the fault would then lie
      entirely in the generalisation, not in the heuristic.
    What would need to be true for C2A2 to be safe: (a) the heuristic is scoped explicitly to
      gross failures and never treated as coverage — its stated form should include the class it
      cannot see; (b) at least one detector exists whose sensitivity does not depend on the
      error's magnitude, which in practice means an invariant checked inside the parser (counts
      reconciled, every input line accounted for, a total that must balance) rather than a
      judgement about the output; (c) the detector's detection rate is measured by seeding known
      defects of *small* magnitude, not by observing that it caught a large one; (d) the
      21-pair near-miss is treated as a labelled test case and added to a regression set, so
      that the one known instance of the heuristic's blind spot is permanently covered; (e)
      results that pass the plausibility check are not thereby recorded as verified, since the
      distinguishing risk here is that a plausible wrong number enters the record with the same
      status as a right one. Condition (c) is decisive — it is the only one that converts the
      heuristic's coverage from an assumption into a number.
    How to test: Directly runnable and inexpensive. Take the parser, seed it with faults
      calibrated to produce small discrepancies — one pair, five pairs, twenty pairs, the size
      of the recorded near-miss — and run the existing checking procedure over the outputs.
      Record the smallest discrepancy the procedure reliably catches; that number is the
      heuristic's actual sensitivity floor and can be compared directly against the observed
      21-pair near-miss. Second test, retrospective: re-run the current parser over the inputs
      of past runs and diff the outputs against what was recorded at the time. Any difference is
      a defect the plausibility check did not catch, and the count gives an empirical miss rate
      rather than an asserted sparsity prior. Third, cheapest: add a reconciliation invariant
      (input items in = items accounted for out) and see whether it fires on any historical
      input; a single firing on data that previously passed plausibility refutes the presumption
      outright.

  Specific risks: If plausibility is not a reliable tell, then (i) the system's defect record is
    biased toward large errors, so its own estimate of defect sparsity — the premise of the
    heuristic — is itself an artefact of the detector, which makes the reasoning circular; (ii)
    the surviving errors are the plausible ones, which are exactly the ones most likely to be
    believed, cited and built upon, so the undetected population is more damaging per item than
    the detected one; (iii) the heuristic generates false assurance in the specific sense that a
    passing result is read as a checked result; (iv) the near-miss demonstrates the blind spot
    exists in this system's own data, so this is not a hypothetical exposure but a measured one
    with an unknown rate; (v) the summary that generalised the heuristic and the summary that
    recorded the near-miss are the same document, which means the counterevidence was available
    at the moment of generalisation and did not alter it — a failure of the evidence pathway, not
    only of the heuristic.

  Mitigations available: (1) Magnitude-independent invariants inside the parser — conservation
    and reconciliation checks that fire on a one-item discrepancy exactly as on a total one. (2)
    Seeded-fault measurement of the current detector's sensitivity floor, which is the mutation-
    testing move and converts coverage from claim to number. (3) A regression case built from the
    recorded 21-pair near-miss. (4) Sentinel/canary records with known expected outcomes carried
    through the pipeline, the pattern both Meta and the data-observability literature converge
    on. (5) Differential checking — run two independent extraction paths and compare, which
    detects small discrepancies without needing any prior about their plausibility (noting the
    independence caveat raised in PRESUMPTION-696). (6) Restate the heuristic with its scope
    attached, so that future readers of the register inherit the limitation along with the rule.

  Search scope: Comprehensive for silent data corruption at scale (Meta's two engineering posts,
    Google's exabyte-scale database work and its file-system checksum lineage) and for the
    constructive alternatives (mutation testing, sentinel/canary validation, declarative data
    quality constraints). Adequate for the oracle-problem framing, though reached via the ISSTA
    record and secondary summary rather than the full survey text, and the author list is flagged
    accordingly. Preliminary on inspection missed-detection base rates — the industrial-vision
    sources located are only loosely analogous to text parsing and are cited for the shape of the
    result rather than the magnitude. Not searched: the signal-detection-theory literature on
    ROC curves and the explicit trade of sensitivity against specificity, which would formalise
    the magnitude-dependence argument, and the near-miss reporting literature in safety science,
    which speaks directly to the question of what a system should do with a near-miss recorded
    alongside a success. Broader search recommended on near-miss reporting specifically — it is
    the literature most likely to address the failure of evidence propagation noted in risk (v).

  Recommendation: CHALLENGED

---

SYSTEMIC-RISK-FLAG:
  Date: 2026-08-07
  Affected items: PRESUMPTION-696, PRESUMPTION-703, PRESUMPTION-707, PRESUMPTION-714
  Common vulnerability: In each case a *detector or diagnostic* is credited with discriminating
    power that was never measured, and the credit is derived from the single case the detector
    happened to catch. 696 credits an internally built evaluator with independence it has not
    been tested for. 703 credits a plausibility check with coverage inferred from the one gross
    failure it caught. 707 credits a named mechanism ("the --max starvation artifact") with
    explaining an observation it does not cover. 714 credits a single-fault diagnosis derived
    from the call site where the symptom appeared. The shared structure is that the system
    reasons from a detector's *successes* to its *coverage*, and never from its misses to its
    blind spots — even where a miss is recorded in the same document as the success (703
    explicitly, 714 in its own second clause). No detector in this cluster has a measured
    sensitivity, a measured false-negative rate, or a named class of defects it structurally
    cannot see.
  Literature basis: Knight and Leveson (1986) on the untested independence assumption in
    multi-version programming; the LLM evaluation-panel work on correlated errors (arXiv
    2605.29800) showing nominal independence is ~4x its measured value; the mutation-testing
    literature (FSE 2014, DOI 10.1145/2635868.2635929) whose entire premise is that a detector's
    coverage must be established by seeded faults rather than by observed catches; Meta and
    Google on silent data corruption, whose defining property is that it does not announce
    itself; the test-oracle literature on failed error propagation (ISSTA 2017, DOI
    10.1145/3092703.3098235); and the flaky-test literature on premature root-cause attribution.
  Risk level: Critical
  Recommendation: Adopt a single cross-cutting rule: no detector, evaluator or diagnostic is
    recorded as a control until its sensitivity has been measured against seeded or historical
    faults, and no such component is recorded without an explicit statement of the defect class
    it cannot detect. Concretely — (1) run seeded-fault measurement against each of the four
    detectors above and record a number; (2) require every future diagnostic claim in the
    register to carry the observation it does *not* explain, where one is known; (3) treat a
    recorded near-miss as a mandatory regression case rather than as narrative colour. The
    cheapest immediate action is (3), because in at least two of these four items the
    counterevidence was already present in the same document as the claim and produced no
    change.
