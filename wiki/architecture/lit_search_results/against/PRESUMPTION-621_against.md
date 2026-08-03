SEARCH-AGAINST-PRESUMPTION-621:
  Date searched: 2026-08-02
  Original item: PRESUMPTION-621
  Original statement: Copy-forward error — that assertions recorded in logs reflect measurements actually taken rather than propagating by template from prior entries; and that structured templates raise the fidelity of recorded checks.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-621
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced an unstated assumption that a recorded check in a log is evidence that the check occurred, rather than evidence that a prior record existed to copy.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. ECRI / Partnership for Health IT Patient Safety, "Copy/Paste: Prevalence, Problems, and Best Practices" (htais_copy_paste_report). — Reports a 2022 analysis of over 100 million EHR notes finding that 50.1% of all text in notes was duplicated from prior documentation on the same patient. Roughly half of a mature structured record propagates by copy rather than by observation. This is the single strongest quantification of the claimed mechanism.
    2. Tsou, A.Y. et al., 2017. "Safe Practices for Copy and Paste in the EHR: Systematic Review, Recommendations, and Novel Model for Health IT Collaboration." Applied Clinical Informatics 8(1). — Systematic review: as many as 90% of clinicians report using copy-and-paste when documenting, and 81% admit to frequently copying other authors' notes. The behaviour is near-universal among trained professionals under formal documentation obligations.
    3. AHRQ PSNet, "Copy paste and cloned notes in electronic health records: prevalence, benefits, risks and best practices." — Synthesises the safety case: unverified copy-forward propagates documentation errors that contribute to real downstream errors; carried-forward assertions persist long after the underlying state has changed.
    4. Rosenbloom, S.T. et al. NOTE trial — "Effect of Outpatient Note Templates on Note Quality: NOTE (Notation Optimization through Template Engineering) Randomized Clinical Trial." Journal of General Internal Medicine. — Randomised evidence that a redesigned template produced notes judged by experienced reviewers as *less accurate and less useful* than prior-state notes, despite better organisation and despite authors perceiving the templated notes as improved. Directly contradicts the presumption that templating raises fidelity, and identifies the dangerous part: the producer's confidence rises while accuracy falls.
    5. "Restricted use of copy and paste in electronic health records potentially improves healthcare quality," 2022 (PMC8797538). — Restricting the copy mechanism, rather than instructing against its misuse, is what shifts quality. Consistent with the forcing-function finding in PRESUMPTION-623.
    6. ECRI report (as above), citing a VA study of 2,645 notes containing duplicated text: 338 notes (1.2%) were judged high risk on expert review — misleading information with major potential for patient harm — and one study attributed 2.6% of diagnostic errors requiring additional care to copy-paste issues. Gives the harm-conversion rate: ~50% duplication yields ~1-3% actively dangerous records.

  Strength of challenge: Strong

  Summary: The clinical documentation literature supplies both the mechanism and a rate. In a large, audited, professionally staffed record system, about half of all text propagates from prior entries rather than from fresh observation, and roughly 90% of authors use the copy mechanism. Between 1.2% and 2.6% of the resulting records are judged actively misleading or implicated in downstream error. Critically, the one randomised trial located on structured templates found templated notes to be *less* accurate than free-form notes while authors rated them as improved — so templating can raise the confidence attached to a record faster than it raises the record's fidelity. The presumption that a recorded check evidences a performed check is not supported; the base rate for template propagation in comparable systems is roughly 50%.

  Specific risks: The audit trail becomes self-referential — each entry's warrant is the previous entry, and the chain has no measurement at its root. Because the copied assertion is well-formed and passes any structural validation, the failure is invisible to every check the system runs on itself, including checks that count how many checks were recorded. Downstream, any metric computed over the log (verification coverage, check frequency, recurrence counts) inherits the duplication and overstates activity by up to the duplication rate. Worst case: a check that has never once been executed is recorded as executed on every run.

  Mitigations available: (a) Require each recorded check to carry a machine-generated artifact of the measurement (timestamp from the measuring process, output hash, tool exit code) rather than a prose assertion; (b) run duplicate-text detection over the log and report the duplication rate as a first-class health metric — the EHR literature's 50.1% figure gives a comparison baseline; (c) restrict rather than discourage the copy path, per PMC8797538; (d) treat any assertion that is byte-identical across N consecutive entries as unverified until re-measured; (e) do not assume templating improves fidelity — the NOTE trial shows it can invert.

  Search scope: Comprehensive for clinical copy-forward/copy-paste prevalence and harm. Moderate for structured-template fidelity — the evidence is genuinely mixed (recent emergency-medicine and low-resource-hospital studies report template-associated improvements in documentation completeness scores), and only one randomised trial was found on the negative side. Preliminary for audit-trail integrity outside healthcare; a search of the software audit-logging and financial-controls literature is recommended.

  STEELMAN:
    Strongest counterargument: Copy-forward is not the same as fabrication. Much duplicated text is duplicated because the underlying state genuinely has not changed, and re-deriving an unchanged fact from scratch on every entry is waste, not rigour. The 50.1% duplication figure is a measure of redundancy, not of error; the measured error conversion is 1.2-2.6%, two orders of magnitude smaller. Templates, meanwhile, have positive recent evidence in several studies — the negative NOTE finding is one trial, and the mechanism it identified (organisation improving faster than content) is addressable by template design rather than by abandoning templates. A system that forbids carrying forward unchanged state will spend most of its effort re-establishing things it already knows.
    What would need to be true for the system to be safe: (i) carried-forward assertions are marked as carried-forward and distinguishable from freshly measured ones; (ii) the assertions that matter — the ones a decision rests on — are always re-measured, whatever the rest of the log does; (iii) an independent artifact ties each load-bearing assertion to an execution.
    How to test: Diff consecutive log entries and compute the byte-level duplication rate over the last N entries. Then take a stratified sample of duplicated assertions and independently re-measure the underlying state; the fraction where the carried-forward assertion is now false is the copy-forward error rate for this system. Compare against the EHR baseline of ~1-3% high-risk.

  Recommendation: CHALLENGED
