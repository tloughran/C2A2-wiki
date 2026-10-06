SEARCH-FOR-ASSUMPTION-1277:
  Date searched: 2026-09-08
  Original item: ASSUMPTION-1277
  Original statement: A guard rule is not adopted until it passes a fixture AND a control in which the
    rule is neutralised fails — the paired falsifier is the adoption gate.
  Routed question: Does paired fixture-plus-neutralised-control test design measurably reduce defect
    escape in configuration guards and filter rules, relative to a positive fixture alone?

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1277
    Item type: ASSUMPTION (stated — quoted from a commit message written with the designer present)
    Transform at each step:
      14a: Extracted verbatim from the `commit_daily_run.sh` fix message in
        `inbox/rc_sandbox/COMMIT_ME_2026-09-07.sh`; routed as a general methodological claim, not as a
        judgement on the specific guard.
      15a: Searched for supporting literature (2026-09-08), FOR direction only.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Petrović, G., Ivanković, M., Fraser, G., Just, R., 2021. "Does mutation testing improve testing
       practices?" Proceedings of ICSE'21. arXiv:2103.07189.
       [VERIFIED: full abstract retrieved from arxiv.org/abs/2103.07189 this run; full text NOT read —
       ABSTRACT-ONLY] — The single most directly on-point source. Verbatim from the abstract: "Our
       analyses suggest that developers using mutation testing write more tests, and actively improve
       their test suites with high quality tests such that fewer mutants remain," and, from a dataset of
       past fixes of real high-priority faults, "had mutation testing been used for the changes
       introducing the faults, it would have reported a live mutant that could have prevented the bug."
       Scale: ~15 million mutants. CLAIM RESTING ON THIS SOURCE (abstract-only): that the neutralised-
       control step, applied at the point of change, is coupled to real defects that would otherwise
       have escaped. The counterfactual ("could have prevented") is the authors' inference from
       coupling, not a measured escape-rate reduction from a controlled trial — see Caveats.
    2. Just, R., Jalali, D., Inozemtseva, L., Ernst, M.D., Holmes, R., Fraser, G., 2014. "Are mutants a
       valid substitute for real faults in software testing?" Proceedings of FSE'14, ACM.
       DOI 10.1145/2635868.2635929.
       [VERIFIED: authors, title, venue via ACM DL listing; the numeric results below read verbatim from
       the authors' own FSE'14 presentation deck retrieved this run at
       pdfs.semanticscholar.org/8cd7/9062e6aecee8e1c99471114607c63e54ca4b.pdf, dated 20 Nov 2014.
       Journal-paper full text NOT read] — 357 reproducible, isolated real faults across 5 Java projects
       (321 KLOC), 230,000 mutants, 35,141 generated test suites. Verified findings: when a developer
       strengthened a suite to catch a real fault, the mutant detection rate rose for 73% of faults,
       versus 50% for branch coverage and 40% for statement coverage; mutant detection correlated with
       real-fault detection more strongly than statement coverage did. Direct empirical support for the
       *comparative* limb of ASSUMPTION-1277: a neutralised-artefact control is a strictly more
       sensitive adequacy signal than "the positive fixture passed and the line was exercised."
    3. Petrović, G., Ivanković, M., Fraser, G., Just, R., 2021. "Practical Mutation Testing at Scale: A
       view from Google." IEEE Transactions on Software Engineering. DOI 10.1109/TSE.2021.3107634;
       preprint arXiv:2102.11378.
       [VERIFIED: abstract and §1 read verbatim from arxiv.org/pdf/2102.11378 this run; remainder of the
       paper grepped, not read in full] — §1 states the exact failure mode ASSUMPTION-1277 guards
       against, in a worked example: a fully covered function whose returned buffer is never asserted
       upon. Verbatim: "The tests only exercise the function, but do not assert upon its effects on the
       returned buffer... even though the line that appends some content to buf is covered, a developer
       is not informed about the fact that no test checks for its effects. The statement-deletion
       mutation, on the other hand, explicitly points out this testing weakness." Deployment evidence:
       >24,000 developers, >1,000 projects; the productive-mutant ratio was raised from 15% to 89% by
       filtering. Establishes that the paired-control method is not merely sound but operable at
       industrial scale — relevant to 14a's "whether it generalises" framing.
    4. Lipsitch, M., Tchetgen Tchetgen, E., Cohen, T., 2010. "Negative controls: a tool for detecting
       confounding and bias in observational studies." Epidemiology 21(3), 383-388. PMID 20335814.
       [VERIFIED: title, authors, journal, year, volume/issue/pages via PubMed 20335814 and the Google
       Scholar citation record surfaced this run; the PubMed abstract page itself returned a reCAPTCHA
       interstitial and was NOT retrieved — treat as CITATION-VERIFIED, CONTENT-NOT-READ] — Cross-
       disciplinary theoretical grounding: the canonical statement that a negative control (an exposure
       or outcome known *not* to be connected to the effect under test) is the standard instrument for
       detecting that an apparently positive result is an artefact of the measurement apparatus rather
       than of the thing measured. The C2A2 "neutralised control that must fail" is a negative control
       in exactly this sense.
    5. Laboratory practice on paired positive/negative controls (assay validity).
       [VERIFIED at tertiary-source level only: multiple methodological guides retrieved this run
       (Rockland Immunochemicals "Positive and Negative Controls"; Boster Bio control-design guide;
       Labster theory notes). NO primary or peer-reviewed source retrieved — treat as WEAK] — The
       standard formulation is that a positive control validates negative results and a negative control
       validates positive results, and that both are required for an assay to be interpretable: a
       positive signal in the negative control indicates a procedural flaw (contamination, non-specific
       reaction) rather than presence of the analyte. This is the same two-sided logic as
       ASSUMPTION-1277, and it is normative laboratory practice, but I did not find a peer-reviewed
       primary source for it in this run.
    6. Martin, E. and Xie, T., 2007. "A fault model and mutation testing of access control policies."
       Proceedings of WWW'07, pp. 667-676.
       [VERIFIED: authors, title, venue and page range via multiple secondary citations retrieved this
       run (Springer chapter "Validation of Access Control Systems"; ACM DL listings for follow-on work
       including "Automated Strong Mutation Testing of XACML Policies," SACMAT 2020). PRIMARY TEXT NOT
       RETRIEVED — the page range is taken from the citing works, not from the paper itself] — The
       nearest the literature comes to C2A2's actual artefact class: mutation operators defined for
       declarative access-control *policies* (XACML), i.e. for rule sets rather than program code, with
       a continuing line of follow-on work through 2020. Establishes that the neutralised-control method
       has been carried into the configuration/filter-rule domain and is treated there as the adequacy
       criterion. Weight: precedent for the transfer, not measurement of it.

  Strength of support: Strong (for the general software-testing case); Weak-to-Moderate (for the
    specific domain named in the routed question — configuration guards and filter rules)

  Summary: The literature supports the *mechanism* ASSUMPTION-1277 asserts, and supports it well. Just
  et al. (2014) show empirically, on 357 real faults, that a suite's ability to kill a neutralised
  variant tracks its ability to catch real faults substantially better than the "it passed and the line
  was covered" signal (73% vs 40-50%). Petrović et al. (2021, ICSE) go one step further and report, over
  ~15M mutants, both that the practice changes developer behaviour (more tests written, fewer surviving
  mutants) and that real high-priority faults were coupled to mutants that the method would have
  surfaced before release. Petrović et al. (2021, TSE) give the failure mode in its purest form — a line
  fully covered by a passing fixture with no assertion on its effect, which the neutralised control
  catches and the positive fixture cannot — and show the method runs at Google scale. Outside software,
  the negative-control principle (Lipsitch et al. 2010; standard assay design) is the mature, cross-
  disciplinary version of the same argument: a positive result is uninterpretable until you have
  demonstrated that the apparatus can produce a negative. The adoption-gate framing — the control must
  actually fail before the rule is trusted — is therefore not a C2A2 invention; it is the orthodox
  position in two independent literatures.

  Caveats:
  (a) SCOPE MISMATCH ON THE ROUTED QUESTION. The question asks about "defect escape in configuration
      guards and filter rules." Sources 1-3 measure *program code* in large Java/C++ codebases. Source
      6 is in the right artefact class (declarative policies) but I verified it only through citing
      works and it reports method design, not escape-rate reduction. I found no study measuring defect
      escape in shell-script guards, regex filters or CI configuration rules under paired-control versus
      positive-fixture-only designs. Searched for and not found: mutation testing of firewall rule sets
      with an escape-rate outcome (the query returned trade/practitioner material only).
  (b) NO RANDOMISED COMPARISON EXISTS in any source found. Petrović et al. (ICSE'21) is observational at
      Google, with self-selection into mutation-testing use; the "could have prevented the bug" claim is
      a retrospective counterfactual computed from coupling, not a measured reduction in escapes. The
      strongest honest reading is "consistently associated with," not "measurably reduces."
  (c) COST AND NOISE ARE REAL AND DOCUMENTED IN THE SUPPORTIVE SOURCES THEMSELVES. Petrović et al.
      (TSE'21) report that Google developers initially judged ~85% of surfaced mutants unproductive; the
      15% → 89% improvement required substantial engineering (context-based filtering, suppression
      rules, one mutant per covered line). A naive paired-control regime is cheap at n=1 (C2A2's case)
      and expensive at scale. The assumption's own priority note ("the method is cheap and already in
      use once") is consistent with this: the support is strongest exactly where C2A2 currently sits.
  (d) KNOWN CEILING. Just et al. verified that 17% of the real faults studied could not be represented
      by any mutant at all — a neutralised control cannot exist for that class of fault, so passing the
      paired gate is not evidence of adequacy against it. The gate is a floor, not a ceiling.
  (e) PUBLICATION BIAS. Three of the six sources share an author (René Just) and two share the full
      author team; the mutation-testing effectiveness literature is small and comparatively closed.
      15b should be expected to find the Facebook counterpoint ("What It Would Take to Use Mutation
      Testing in Industry," arXiv:2010.13464), which appeared in my searches and which I did not read,
      being out of my direction.
  (f) SEARCH SCOPE. Preliminary — broader search recommended. Eight queries run, five sources retrieved
      at full or partial text, one (Lipsitch) verified as a citation only. Not covered: assertion-
      adequacy / checked-coverage literature (Schuler & Zeller), TDD "see it fail first" experimental
      literature, negative-control design in ML evaluation (Adebayo et al. 2018 model-parameter
      randomisation was located but not read), and the specific regex/filter-rule defect studies named
      in 14a's Search hint, which I did not find.

  Recommendation: SUPPORTED
