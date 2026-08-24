SEARCH-FOR-ASSUMPTION-1126:
  Date searched: 2026-08-18
  Original item: ASSUMPTION-1126
  Original statement: A check was inert for nineteen consecutive runs and the cause written in the register was never the true cause — the failure was environmental (a hardcoded `/tmp/dayNNN_segments.json` path in a sandbox where `/tmp` is sticky and owned by `nobody`), not the external dependency (YouTube) that the register named.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1126
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted the root-cause statement and set it against two same-day runs still reporting the old symptom under the old explanation.
      15a: Searched for supporting literature; found convergent support from three separate bodies — software configuration-error studies (environment/path misconfiguration as a dominant and under-recognised failure cause), build-hermeticity studies (host-environment dependencies invisible to every declared specification), and diagnostic-error research (anchoring, premature closure, and propagation of a recorded diagnosis long after it is contradicted).
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Yin, Z., Ma, X., Zheng, J., Zhou, Y., Bairavasundaram, L.N., Pasupathy, S. (2011). "An Empirical Study on Configuration Errors in Commercial and Open Source Systems." SOSP '11, pp. 159–172. — Study of 546 real-world misconfigurations (309 from a commercial storage system, 237 from CentOS, MySQL, Apache, OpenLDAP). Establishes configuration errors as one of the dominant causes of system failure and documents that a large fraction produce no explicit error message, making them exceptionally prone to misdiagnosis. Directly supports the class "the failing thing was the environment, not the named dependency."

    2. Zheng, S., Adams, B., Hassan, A.E. (2025). "On Build Hermeticity in Bazel-based Build Systems." IEEE Software 42(6). (Preprint: https://mcislab.github.io/publications/2025/ieeesw-shenyu.pdf) — Traced 150 million Linux filesystem calls across 70 Bazel projects; found *none* achieved a fully hermetic build, with 2,439 non-hermetic dependency packages drawn silently from the host. The paper states explicitly that when failures arise from these unmanaged host dependencies, "diagnosing and addressing these issues can be complex, as such updates often go unnoticed due to the CI environment not being under their control." This is the mechanism ASSUMPTION-1126 describes: a host-filesystem fact (path, ownership, sticky bit) that no declared specification names, and that therefore gets attributed to whatever *is* named.

    3. Howard, J. (2019). "Premature Closure: Anchoring Bias, Occam's Error, Availability Bias, Search Satisficing, Yin-Yang Error, Diagnosis Momentum, Triage Cueing, and Unpacking Failure." In: *Cognitive Errors and Diagnostic Mistakes: A Case-Based Guide to Critical Thinking in Medicine*, Springer. — Characterises anchoring/premature closure as the tendency to hold an initial hypothesis while contradicting evidence accumulates, and identifies it as among the most frequent single causes of diagnostic error. Notes the specific variant in which "subsequent clinicians unquestioningly accept a previous working diagnosis without independently collecting and reviewing relevant data" — the direct analogue of nineteen runs re-reporting an inherited cause.

    4. Kellogg, K.M., et al. (2017). "Our current approach to root cause analysis: is it contributing to our failure to improve patient safety?" BMJ Quality & Safety 26(5): 381–387. — Empirical review of RCA outputs finding that recorded causes frequently do not withstand scrutiny and that the same events recur under the same recorded explanations, i.e. an erroneous recorded cause is not self-correcting.

    5. Peerally, M.F., Carr, S., Waring, J., Dixon-Woods, M. (2017). "The problem with root cause analysis." BMJ Quality & Safety 26(5): 417–422. — Argues RCA as practised produces causal narratives whose validity is rarely tested, and that political and procedural pressure to close an investigation entrenches the first plausible cause. Supports the specific claim that a written cause acquires standing independent of its correctness.

    6. ECRI / Partnership for Health IT Patient Safety (undated, literature review). "Copy/Paste: Prevalence, Problems, and Best Practices." — Documents that once an incorrect diagnosis is recorded, copy-forward mechanics propagate it across subsequent records, and that later readers assume prior verification. The mechanism by which a wrong cause survives nineteen re-reports without anyone re-deriving it.

    7. *Rethinking Software Misconfigurations in the Real World: An Empirical Study and Literature Analysis* (2024). arXiv:2412.11121. [unverified — author list not individually confirmed] — Reports that misconfigurations manifest as crashes, hangs, and *silent* failures, and classifies "resource unavailability" as a distinct root-cause category. Consistent with an inert-but-non-erroring check.

  Strength of support: Strong

  Summary: The literature supports both halves of the assumption independently and they compose. On the technical half, configuration and environment errors — including invalid or unvalidated path parameters and unmanaged host-filesystem dependencies — are established as a dominant, systematically under-recognised class of production failure (Yin et al. 2011; Zheng, Adams & Hassan 2025), and they are hard to diagnose precisely because they are not named in any specification the operator reads. On the diagnostic half, anchoring and premature closure are documented as the single most frequent contributor to diagnostic error, with a well-described variant in which downstream observers accept an inherited working diagnosis without re-deriving it (Howard 2019), and recorded-cause propagation through copy-forward record systems is empirically documented (ECRI). The patient-safety RCA critiques (Kellogg et al. 2017; Peerally et al. 2017) independently establish that a recorded root cause is not self-correcting: the same events recur under the same wrong explanation. Nothing in the literature contradicts the specific pattern of a check inert for nineteen runs under a stable wrong attribution; the literature makes that pattern the expected outcome, not the surprising one.

  Caveats: (a) No source quantifies the survival time of an erroneous attribution in *machine-generated* incident registers; the persistence evidence comes from human clinical and organisational records, where the propagation mechanism (a reader assuming prior verification) may not transfer cleanly to an automated pipeline that simply re-emits a template string. (b) The Yin et al. and Zheng et al. studies concern human-operated production systems and build systems respectively; neither studies agent-run sandboxes. (c) The "misattributed to an *external* dependency" specificity — YouTube rather than the sandbox — is not directly measured anywhere found; the literature supports "environment misdiagnosed," not specifically "environment misdiagnosed as third-party API." (d) Source 7 is cited with unconfirmed authorship and should be re-verified or dropped before any external use.

  Search scope: Preliminary-to-moderate. Searched via WebSearch across: software-engineering configuration-error and misconfiguration empirical studies (SOSP/OSDI/ICSE/ASE/arXiv); build hermeticity and reproducible-build literature (IEEE Software, IEEE S&P); flaky-test root-cause taxonomies (MSR/ICSE/EASE); diagnostic-error and cognitive-bias literature (BMJ Quality & Safety, AFP, Springer clinical-reasoning texts); EHR copy-paste error-propagation literature (ECRI, JAMIA-adjacent). Not searched: aviation/nuclear incident-record longevity literature, ITIL/ITSM known-error-database studies, and formal work on incident-taxonomy drift — a broader search in those areas is recommended if a quantitative "half-life of a wrong attribution" figure is needed.

  Recommendation: SUPPORTED
