SEARCH-AGAINST-PRESUMPTION-648:
  Date searched: 2026-08-04
  Original item: PRESUMPTION-648
  Original statement: That instrumenting the specific path that failed protects the
    sibling paths that have not yet failed — the blind validator having been bypassed
    with `|| true` rather than repaired.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-648
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-08-03 remediation that added instrumentation to the
        failed path while suppressing the blind validator with `|| true`
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. (2024). "Learning From Lessons Learned: Preliminary Findings From a Study of
       Learning From Failure." arXiv:2402.09538. — Distinguishes explicitly between
       post-incident actions that address the specific defect and those that address
       the class of similar potential defects, and finds that action items
       overwhelmingly target the former; the generalising action is the exception,
       not the default.
    2. Cook, R.I., Allspaw, J. et al., 2017. "STELLA: Report from the SNAFUcatchers
       Workshop on Coping with Complexity." — Dark debt arises from interactions and
       is therefore not addressable by inspecting or instrumenting the component that
       happened to surface it; fixing the surfacing component leaves the generating
       condition intact.
    3. ShellCheck rule SC2312 and associated Bash error-handling guidance (shellcheck
       wiki; `set -euo pipefail` practice). — Codifies `cmd || true` as an exit-code
       masking construct: the command's failure becomes structurally unobservable to
       the caller and to CI, which then reports success. The suppression does not
       merely leave the defect unfixed; it removes the signal that would reveal it.
    4. Cloud incident-recurrence analyses, e.g. (2024) "Automated Root Causing of
       Cloud Incidents using In-Context Learning with GPT-4," arXiv:2401.13810, and
       (2023) "Automatic Root Cause Analysis via Large Language Models for Cloud
       Incidents," arXiv:2305.15778. — Report that incidents cluster strongly into
       recurring classes, with a large fraction of recurrences reappearing within
       weeks of the original resolution — i.e. the defect class survives the
       point fix.
    5. Huang, P. et al., 2017. "Gray Failure: The Achilles' Heel of Cloud-Scale
       Systems." HotOS '17. — Differential observability: the failure detector's view
       and the application's view diverge. A validator forced to return success is
       the extreme case — the detector is now guaranteed to disagree with reality on
       every future instance.

  Strength of challenge: Strong

  Summary: The literature challenges the presumption on two separate grounds. First,
    the empirical one: post-incident actions are documented to be predominantly
    specific rather than class-level, and incident recurrence rates show that the
    class outlives the point fix — so "we instrumented the path that failed" is
    precisely the pattern that correlates with recurrence, not the one that prevents
    it. Second, and more seriously, `|| true` is not a neutral deferral. It is a
    documented anti-pattern whose effect is to convert a failing check into a passing
    one, which means the sibling paths are not merely uninstrumented but are now
    covered by a validator that reports success unconditionally. That is worse than
    having no validator, because a validator that exists and returns PASS suppresses
    the suspicion that would otherwise prompt manual inspection. The gray-failure
    framing names the resulting state: the detector and the world have been formally
    decoupled.

  Specific risks: Any defect in a sibling path that the validator was designed to
    catch will now pass silently and will carry a PASS artifact attesting that it was
    checked. Because the suppression is a one-line construct with no expiry, it will
    persist indefinitely and will not be visible in any dashboard — the pipeline
    stays green. Downstream, C2A2 accumulates artifacts marked verified whose
    verification was structurally incapable of failing; there is no field recording
    that the check was suppressed, so the affected set is not enumerable after the
    fact (this compounds directly with PRESUMPTION-655). The recurrence data suggests
    the window before the next instance of this class is weeks, not years.

  Mitigations available: (1) Grep the whole repository for `|| true`, `|| exit 0`,
    `continue-on-error`, `set +e`, and equivalent suppressions; enumerate them and
    attach an owner and an expiry date to each. This is a one-command audit. (2) Make
    suppression loud rather than silent: replace `cmd || true` with a wrapper that
    still returns 0 but emits a distinct SUPPRESSED marker into the run log and into
    any artifact the run produces, so PASS and PASS-WITH-SUPPRESSED-CHECK are never
    the same string. (3) Fix the blind validator rather than the path — the validator's
    blindness is the class-level defect; the failed path was only its first symptom.
    (4) After any point fix, require an explicit written answer to "what other paths
    share this mechanism?" and treat the absence of that answer as an incomplete
    remediation. (5) Add a canary: deliberately inject the known defect into a sibling
    path in a test context and confirm the validator catches it. If it does not, the
    coverage claim is falsified cheaply.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-648
    Strongest counterargument: Instrumenting the failed path is the highest-value
      single action available under time pressure, and `|| true` is a legitimate,
      explicitly-disclosed temporary unblock — the alternative was a validator that
      blocked all progress while providing no true signal. Partial coverage that
      catches one real class of defect is strictly better than a blocked pipeline
      or an abandoned validator, and demanding class-level generalisation before
      shipping any fix is a counsel of perfection that in practice yields no fix at
      all. The recurrence literature describes organisations with many concurrent
      incident streams; a single-operator system can reasonably fix incidents one at
      a time, in order of observation.
    What would need to be true for C2A2 to be safe: (a) The `|| true` is genuinely
      temporary and has a recorded expiry that something enforces. (b) No artifact
      produced while the suppression is active carries an unqualified PASS. (c) The
      sibling paths either do not share the failure mechanism, or are covered by an
      independent check that was not suppressed. (d) Someone can currently name,
      without searching, every suppression active in the system — if not, the
      "temporary" framing is not operative.
    How to test: Two cheap queries. First, repository-wide grep for suppression
      constructs and count them; a count above a handful, or any instance older than
      the incident that motivated it, falsifies the temporary framing. Second, take
      the specific defect that was observed on the failed path, construct the
      analogous input for one sibling path, and run the validator. If it returns
      PASS, the coverage presumption is directly disproven.

  Search scope: Adequate. Concepts searched: defect-class coverage; generalisation of
    post-incident corrective actions; incident recurrence rates; `|| true` and exit-code
    suppression as CI anti-pattern; dark debt; differential observability.
