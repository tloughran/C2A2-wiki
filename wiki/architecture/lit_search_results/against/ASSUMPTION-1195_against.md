SEARCH-AGAINST-ASSUMPTION-1195:
  Date searched: 2026-08-25
  Original item: ASSUMPTION-1195
  Queue ref: LIT-QUEUE-2026-08-24-001
  Original statement: "A partial check reported as a full one" is the dominant failure mode of automated verification.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1195
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim from the scheduler task file's rationale and queued for search
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Search scope: Preliminary-to-moderate. Queries covered silent test failure, false-pass vs false-fail
    in automated verification, flaky-test empirics, and failure-mode taxonomies for automated
    issue-solving/repair pipelines. Venues reached: FSE 2014, ESEC/FSE 2021, arXiv software-engineering
    preprints 2024–2026, Google SRE book (2016). Date range 2014–2026.
    GAPS: web-search budget was exhausted after six queries; later retrieval was limited to URLs already
    in the provenance set, and dl.acm.org returned an empty body, so the Ericsson paper is cited from
    search-result metadata only (authors unverified). No source was found that measures the *relative
    frequency* of "check silently narrowed and reported as complete" against other verification failure
    modes in a shared denominator — which is precisely the quantity the word "dominant" asserts. This is
    the central gap and it cuts both ways: I found no evidence for dominance and no clean refutation of it,
    only adjacent distributions that make it improbable.

  Challenging evidence found: Partial

  Sources:
    1. [Authors not captured in retrieved HTML — names unverified]. 2025. "An Empirical Study on Failures in
       Automated Issue Solving." arXiv:2509.13941v1. — The most direct challenge to the *dominance* claim.
       Manual analysis of 150 failing issues from SWE-Bench-Verified yielded 342 failure instances organised
       into 9 primary categories and 25 subcategories across three phases (Location, Repair, Iteration &
       Validation). The reported distribution puts the mass elsewhere than verification misreporting:
       "Pipeline-based tools mainly fail in localization stage, whereas agentic tools become more prone to
       iteration anomalies failures as tasks grow harder. Yet across all settings, fix implementation
       remains the dominant bottleneck." Verification-related problems sit inside "environmental friction
       (approx. 10%) ... which is the cause of verification issues or tool usage errors." If ~10% is the
       ceiling for the whole environmental/verification band, a single failure mode within it cannot be
       dominant over the taxonomy. FULL-TEXT (HTML, read in relevant part).
    2. "Quantifying no-fault-found test failures to prioritize inspection of flaky tests at Ericsson."
       Proceedings of ESEC/FSE 2021. DOI 10.1145/3468264.3473930. [author list unverified — dl.acm.org
       returned an empty body]. — At industrial scale the failure population that consumes engineering
       attention is *false failures* ("no-fault-found"), i.e. checks that report a problem where none
       exists: the inverse of the claimed dominant mode. The existence of a paper devoted to prioritising
       inspection of this class at one large vendor indicates the observed frequency ordering runs against
       the assumption. SNIPPET-ONLY.
    3. Luo, Q., Hariri, F., Eloussi, L., Marinov, D. 2014. "An empirical analysis of flaky tests."
       Proceedings of the 22nd ACM SIGSOFT International Symposium on the Foundations of Software
       Engineering (FSE 2014), pp. 643–653. DOI 10.1145/2635868.2635920. — The foundational empirical study
       of non-deterministic test outcomes. Flakiness is a *non-determinism* failure, orthogonal to
       scope-misreporting, and it is the class the field has found most prevalent enough to spawn a decade
       of follow-on work. Its prominence is evidence that the verification failure landscape is dominated by
       determinism and environment problems rather than by silent scope narrowing. SNIPPET-ONLY (citation
       and pagination verified via two independent search results; body not read).
    4. Ewaschuk, R. "Monitoring Distributed Systems," Ch. 6 in Beyer et al. (eds.), Site Reliability
       Engineering, O'Reilly/Google, 2016. https://sre.google/sre-book/monitoring-distributed-systems/
       — BOUNDARY CONDITION rather than contradiction. The chapter names the phenomenon precisely (errors
       occur "implicitly (for example, an HTTP 200 success response, but coupled with the wrong content)")
       and states that "only end-to-end system tests can detect that you're serving the wrong content."
       This confirms the mode is real and hard to detect — but it is listed as one of several error classes
       alongside explicit failures and policy failures, not as the dominant one. FULL-TEXT.

  Strength of challenge: Moderate

  Summary: The literature strongly confirms that a partial check reported as a full one is a real,
    consequential, and structurally hard-to-detect failure mode; it does not support the claim that it is
    the *dominant* one. Every distributional study retrieved places the mass elsewhere — reasoning and
    fix-implementation failures in agentic pipelines (~10% ceiling for the entire environmental/verification
    band), non-determinism in test suites, and no-fault-found false *failures* at industrial scale. The
    assumption therefore survives as a hazard statement and fails as a frequency statement. The distinction
    matters operationally, because a frequency claim justifies allocating the majority of verification-design
    budget to scope-completeness auditing, whereas the retrieved evidence would direct that budget toward
    localisation quality, determinism, and false-failure triage. It is also worth noting that the assumption
    is unfalsifiable as currently written: "dominant" has no stated denominator, population, or measurement
    window, so no dataset could confirm or refute it as-is.

  Specific risks: If ASSUMPTION-1195 is false as a frequency claim, C2A2 over-invests verification effort
    against one hazard and under-invests against the classes the literature actually finds larger. Two
    concrete consequences: (a) resources spent proving that checks are complete are not spent on
    determinism/environment control, so the pipeline accumulates flaky results that get re-run until green —
    which manufactures exactly the false-pass condition 1195 was meant to prevent, by a different route;
    (b) false *failures* go untriaged, and under the alarm-fatigue mechanism documented in the
    PRESUMPTION-866 file they train the system's responders to discount failure reports generally. There is
    a second-order risk specific to the wording: an unfalsifiable premise held as settled tends not to get
    re-examined, so an incorrect resource allocation can persist indefinitely without generating evidence
    against itself.

  Mitigations available:
    - Restate the claim with a denominator ("of verification failures observed in C2A2 runs over window W,
      X% were scope-narrowing misreports") so it becomes testable against the run log.
    - Adopt the end-to-end/black-box discipline for the cases that matter (Ewaschuk, SRE book Ch. 6:
      black-box monitoring "forc[es] discipline to only nag a human when a problem is both already ongoing
      and contributing to real symptoms"); this is the known control for the 200-with-wrong-content class.
    - Make the check's own scope a first-class reported field — record what was checked, not only the
      verdict — which converts a silent partial into an inspectable one without requiring the dominance
      claim to be true.
    - Maintain a taxonomy-based failure log of C2A2's own verification failures modelled on the 9-category /
      25-subcategory scheme in arXiv:2509.13941, so the frequency question is answered locally rather than
      assumed.

  STEELMAN:
    Item: ASSUMPTION-1195
    Strongest counterargument: The distributional studies cited above measure failures that were *observed*,
      and a partial check reported as a full one is by construction the failure mode least likely to appear
      in any observed-failure dataset — it does not produce a failing run to be sampled. Every taxonomy
      built from failing traces has a survivorship hole exactly the shape of this mode. So the finding that
      it accounts for a small share of catalogued failures is weak evidence about its true share, and could
      even be read as consistent with dominance among *undetected* failures. If C2A2 means "dominant among
      failures that escape the pipeline" rather than "dominant among failures the pipeline reports," the
      claim is both plausible and largely untestable by the methods used in the retrieved literature — and
      the practical prescription (audit scope, not just verdicts) is prudent either way.
    What would need to be true for C2A2 to be safe: The prescription this assumption motivates must be
      cheap enough that being wrong about dominance costs little, and it must not crowd out determinism
      control and false-failure triage. If verification-scope auditing is additive rather than substitutive,
      the frequency claim's truth value stops being load-bearing.
    How to test: Run a mutation-style audit against C2A2's own verification stages — deliberately narrow a
      check's scope (skip a subset it claims to cover) and see whether any stage reports the narrowing.
      The escape rate over a sample of injected narrowings gives a local, measurable estimate of the mode's
      real prevalence in this pipeline, and can be compared directly against the injected-fault escape rate
      for non-determinism and for environment failures to settle the ordering empirically.

  Recommendation: PARTIALLY-CHALLENGED
