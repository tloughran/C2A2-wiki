SEARCH-FOR-ASSUMPTION-1195:
  Date searched: 2026-08-25
  Original item: ASSUMPTION-1195
  Queue ref: LIT-QUEUE-2026-08-24-001
  Original statement: "A partial check reported as a full one" is the dominant failure mode of automated verification.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1195
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: 14a extracted verbatim from the scheduler task file's rationale and queued for search
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Search scope: Web searches run 2026-08-25 across four literatures, plus one full-text retrieval.
    Queries: silent CI failure / "tests not run" reported as passing / false green build; monitoring
    blind spots, alarm coverage, "unknown unknowns", silent-failure detection; vacuity detection in
    temporal model checking / "vacuous pass"; automation bias, omission errors, complacency
    (Mosier/Skitka/Parasuraman); assertion-free tests, test smells, mutation testing; static-analysis
    and container-scanner false negatives with exit code 0; IEC 61508 diagnostic coverage, "dangerous
    undetected" failures, proof-test coverage; the test oracle problem (Barr et al.).
    Venues reached: Formal Methods in System Design, STTT, IEEE TSE, Human Factors, HFES Proceedings,
    Annals of Nuclear Energy, arXiv cs.SE, plus vendor/practitioner grey literature (GitLab issue
    tracker, exida, DEV Community).
    Date range: 1996–2026.
    Assessment: COMPREHENSIVE for the existence and naming of the phenomenon; PRELIMINARY for the
    quantifier "dominant" — broader search recommended. Gaps: no bibliographic-database (Scopus/
    ACM DL) frequency-ranked taxonomy of automated-verification failure modes was located; several
    sources reached at abstract or snippet level only.

  Supporting evidence found: Partial

  Sources:
    1. Beer, I., Ben-David, S., Eisner, C., Rodeh, Y. 2001. "Efficient Detection of Vacuity in
       Temporal Model Checking." Formal Methods in System Design 18(2):141–163.
       DOI 10.1023/A:1008779610539. — The canonical statement of the claim's mechanism in formal
       verification: a property can "pass" while the check performed was strictly narrower than the
       one intended (antecedent failure), and the pass is reported indistinguishably from a real one.
       Reports that roughly 20% of specifications passed vacuously in first formal-verification runs
       of new hardware designs at IBM Haifa, and that vacuous passes always indicated a real problem
       in design, specification or environment. ABSTRACT-ONLY (plus verified bibliographic record).
    2. Kupferman, O., Vardi, M. 2003. "Vacuity detection in temporal model checking." International
       Journal on Software Tools for Technology Transfer (STTT) 4(2):224–233.
       DOI 10.1007/s100090100062. — Formalises why "true" is an insufficient model-checker answer:
       users need to know whether parts of the formula were exercised at all. Establishes vacuity
       checking as a standard component of commercial model checkers, i.e. the industry treats
       "partial check reported as full" as a first-order risk rather than an edge case.
       ABSTRACT-ONLY.
    3. Bilal, M., Mughal, A.H. 2026. "All Green, Still Broken: Real-Flow Verification Lessons from an
       LLM-Integrated, Multi-Market Web Application." arXiv:2606.22475 (preprint, submitted to IEEE
       Software). — Production rental-search assistant with 1,553 automated test cases that "passed
       continuously, yet user-facing defects continued to reach production." Classification of all
       252 bug-fix commits by escape seam found ~44% fell in four seams component-level unit tests
       cannot observe (live browser runtime, non-default market, end-to-end flow, whole-system).
       Directly instantiates the claim: a scope-limited check reported as a clean verification.
       ABSTRACT-ONLY (PDF text layer did not extract; abstract verified from arXiv listing).
    4. Parasuraman, R., Manzey, D.H. 2010. "Complacency and Bias in Human Use of Automation: An
       Attentional Integration." Human Factors. DOI 10.1177/0018720810376055.
       [volume/issue/pages unverified] — Establishes that automation complacency causes operators to
       fail to detect automation failures in due time, is present in both naive and expert
       participants, and cannot be overcome by simple practice. Supplies the human-side reason the
       failure mode persists once a check reports success. ABSTRACT-ONLY.
    5. Mosier, K.L., Skitka, L.J., Burdick, M.D., Heers, S.T. 1996. "Automation Bias,
       Accountability, and Verification Behaviors." Proceedings of the Human Factors and Ergonomics
       Society Annual Meeting 40(4). DOI 10.1177/154193129604000413. — Origin of the
       omission/commission distinction. Omission errors are precisely the case where the operator is
       not informed of a problem by the automated aid; subsequent work reports that training reduced
       commission but *not* omission errors, i.e. the unreported-gap failure is the more resistant
       of the two. ABSTRACT-ONLY.
    6. Barr, E.T., Harman, M., McMinn, P., Shahbaz, M., Yoo, S. 2015. "The Oracle Problem in Software
       Testing: A Survey." IEEE Transactions on Software Engineering 41(5):507–525. — Frames the
       structural reason a check is routinely narrower than its reported scope: automated tests
       cannot in general decide correctness, so what is actually verified is whatever the (partial,
       often implicit) oracle covers, while the reported result is binary pass/fail.
       ABSTRACT-ONLY.
    7. "Impact of proof test interval and coverage on probability of failure of safety instrumented
       function." ScienceDirect, PII S0306454915004806. [journal/volume/pages unverified] —
       Functional-safety literature (IEC 61508/61511) treats *diagnostic coverage* and *proof-test
       coverage* as first-class design parameters precisely because the residual "dangerous
       undetected" (DU) failure class dominates PFDavg. The standard's own assumption that 100%
       proof-test coverage is not reasonable is a formal admission that every automated check is
       partial. ABSTRACT-ONLY / SNIPPET-ONLY.
    8. GitLab issue #324634, "DESIGN: Make Secure analyzers exit with non-zero code when
       vulnerabilities are found," and issue #358600, "Vulnerability Report fails to update if
       scanner exit code is not 0." gitlab.com/gitlab-org/gitlab. — Grey literature documenting the
       mechanism concretely: a scanner returning exit code 0 produces "a misleading green checkmark
       in the UI (end users interpret this as meaning no vulnerabilities were found)" whether or not
       the scan actually completed or found anything. SNIPPET-ONLY.
    9. "The CI/CD Pipeline That Looked Fine But Was Silently Failing." DEV Community,
       dev.to/sumit_gautam_379d5. — Practitioner account of the canonical instance: Jest, pytest and
       JUnit all exit 0 by default when they collect zero tests, so a pipeline can report success
       for weeks having run nothing. Non-peer-reviewed; corroborative only. SNIPPET-ONLY.

  Strength of support: Moderate

  Summary: The phenomenon named in the claim is real, well-documented, and independently named in at
  least four mature literatures: vacuity in formal verification (a specification "passes" without
  ever being exercised), silent/zero-collected test runs and exit-code-0 scanner results in CI,
  dangerous-undetected failures and diagnostic/proof-test coverage in IEC 61508 functional safety,
  and automation omission errors in human-factors research. Each of these treats the case where a
  check's actual scope is narrower than its reported scope as a first-order engineering hazard rather
  than a corner case, and two supply quantitative anchors — roughly 20% of specifications passing
  vacuously in first model-checking runs (Beer et al. 2001), and ~44% of production bug fixes
  escaping through seams a continuously-green 1,553-case suite could not observe (Bilal & Mughal
  2026). The human-factors strand adds that the failure mode is self-reinforcing: omission errors
  resist the training that reduces commission errors, so a false all-clear is unlikely to be caught
  downstream. What the literature does not supply is the claim's quantifier. No source located ranks
  failure modes of automated verification by frequency and places "partial check reported as full"
  first; the strongest datum found (44%) is a plurality within one project, not a demonstrated
  dominance.

  Caveats: (a) The claim's strong form ("the dominant failure mode") is not established by anything
  found — the supporting sources establish prevalence and severity, not rank. (b) Support is
  assembled by domain transfer: the formal-verification, CI, functional-safety and human-factors
  literatures each describe a structurally similar failure but none was written about "automated
  verification" as a single category, so the synthesis is mine, not any author's. (c) The strongest
  quantitative anchors are narrow — Beer et al.'s 20% is hardware model checking at one lab circa
  2001; Bilal & Mughal's 44% is a single six-week LLM-integrated web project (n=252 commits,
  preprint, not yet peer-reviewed). (d) Several citations are abstract- or snippet-level; the
  Parasuraman & Manzey and Annals-of-Nuclear-Energy bibliographic details are partly unverified and
  are marked as such. (e) Support weakens where the verification stage has an independent liveness
  or coverage signal (vacuity checkers, minimum-test-count assertions, heartbeat/proof-test
  regimes), since these literatures exist precisely because the mitigation is known.

  Recommendation: PARTIALLY-SUPPORTED

PARTIAL NOVELTY-FLAG:
  Item: ASSUMPTION-1195
  Searched: Frequency-ranked taxonomies of automated-verification failure modes; comparative studies
    placing "check performed but scoped narrower than reported" against competing failure modes
    (false positives, flaky/nondeterministic results, correct-but-ignored findings, oracle error).
  Finding: The *existence, mechanism and prevalence* of the failure mode is richly documented and
    separately named in four literatures. The *relative dominance* sub-claim is unaddressed: no
    located study ranks automated-verification failure modes by frequency or cost, and the two
    quantitative anchors found (20%, 44%) do not establish a majority or a rank.
  Implication: The claim is safe to hold in its existence form ("a partial check reported as a full
    one is a well-attested and under-detected failure mode of automated verification") and is
    currently unsupported in its comparative form ("the dominant" one).
  Unaddressed sub-claim: that this failure mode is *dominant* relative to other failure modes of
    automated verification.
  Recommended status: NOVEL (comparative/dominance sub-claim only)
