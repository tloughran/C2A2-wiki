SEARCH-FOR-ASSUMPTION-1682 (RE-TRIGGER — 15d 2026-10-11, MONITOR-617, cycle 1; Medium):
  Date searched: 2026-10-12
  Original item: ASSUMPTION-1682
  Original statement: A finding counts as a proper null hypothesis when the same instrument could observe
    either outcome. (FINDING-091 rationale: "The same instrument could observe either outcome, so it works as
    a proper null hypothesis.")
  Owed (per 15d block): "Supported as a necessary condition; challenged as a sufficient one. Wording should
    carry a power/sensitivity clause. Would tip to INCORPORATE if restated as necessary-not-sufficient with a
    sensitivity requirement." This cycle therefore looks for an authoritative source for that restated form.
  Cycle: 1 (RE-TRIGGER by 15d 2026-10-11; processed 2026-10-12)

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c -> 15d -> 15a (re-trigger cycle 1)]
    Original item: ASSUMPTION-1682
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from daily run bc6bea9e (2026-09-24); PRS count verified; rationale unverified.
      15a (cycle 0, 2026-09-29): SUPPORTED (Moderate). Sources: Mayo 2018 (background), Lakens et al. 2018
        (abstract), Popper 1959.
      15b (cycle 0): independent; not read by this agent.
      15c: DISPOSITION-1001 -> MONITOR-617
      15d: re-triggered 2026-10-11 without evaluating evidence
      15a (cycle 1, 2026-10-12): 2 web searches; 2 fetches.
        - ICH E10 PDF via hhs.gov: fetched in full; relevant sections read (intro and §1.5).
        - PMC fetch FAILED at a captcha.
    Current status: SUPPORTED (Strong) for the restated form

  Search scope: regulatory and methodological sources that require test sensitivity, over and above "the
    instrument could register either outcome", before a null or no-difference result is interpreted:
    (a) ICH E10 assay sensitivity; (b) Dienes 2014 on data insensitivity.
    Targeted search for the restated wording. Not a broad review.

  Supporting evidence found: Yes, for the necessary-not-sufficient form with a sensitivity clause.

  Sources:
    1. ICH E10 / FDA Guidance for Industry, 2001. "E10 Choice of Control Group and Related Issues in Clinical
       Trials." (hhs.gov PDF) [read: fetched in full; Introduction and Section 1.5 "Assay Sensitivity" read
       directly; remainder not read]
       - "Assay sensitivity is a property of a clinical trial defined as the ability to distinguish an
         effective treatment from a less effective or ineffective treatment."
       - "a successful non-inferiority trial ... or an unsuccessful superiority trial, generally does not
         contain such direct evidence of assay sensitivity".
       - A trial lacking it "may find an ineffective treatment to be non-inferior".
       - On no-difference results: "the question of whether the trial could have shown such a difference if
         there had been one is critical".
       Relevance: a regulatory-grade statement of exactly the restated form. An instrument that can in
       principle register both outcomes (any two-arm trial can) is NOT enough. A null or no-difference
       finding is interpretable only if the instrument has demonstrated sensitivity to the effect in
       question.
    2. Dienes, Z., 2014. "Using Bayes to get the most out of non-significant results." Frontiers in
       Psychology 5:781. doi:10.3389/fpsyg.2014.00781. [abstract-level via search; PMC fetch FAILED at a
       captcha] A non-significant result must be distinguished as evidence for H0 versus "data
       insensitivity". Power, intervals or Bayes factors are required to tell them apart, and Bayes factors
       use the data themselves to determine their sensitivity.
       Relevance: methodological support for adding the sensitivity clause, and a choice of how to
       operationalise it.
    3. (On record from cycle 0, not repeated) Lakens, Scheel & Isager 2018 (equivalence bounds); Mayo 2018
       (severity).

  Strength of support: Strong for the restated form ("same instrument can observe either outcome" is
    NECESSARY; a demonstrated sensitivity/power to the effect size of interest is ALSO required). Source 1 is
    an international regulatory guideline read directly. Source 2 and the cycle-0 sources converge on it.
    Note that this support is FOR the restatement, and in effect AGAINST the original sufficiency reading.

  Summary: The owed restatement has authoritative backing. ICH E10 draws the distinction precisely. A trial
    that can in principle show a difference but has not shown it can detect one ("assay sensitivity")
    cannot support a no-difference conclusion. In superiority designs, a positive result is itself proof of
    sensitivity, but a null is not. Dienes 2014 makes the same point for null results generally ("data
    insensitivity"). FINDING-091's rationale therefore states a necessary condition. A version that adds
    "...and the instrument is shown to be sensitive enough to detect the effect of interest (e.g. a positive
    control, a power estimate, or pre-set equivalence bounds)" is directly supported.

  Owed condition: MET at the literature level. Primary/regulatory support for the necessary-not-sufficient
    form with a sensitivity requirement was found and read. Whether FINDING-091 is reworded is for 15c and
    the registers, not 15a.

  Caveats:
    - ICH E10 is clinical-trial guidance, and the transfer to wiki "findings" is by principle, not by
      domain.
    - Only the relevant sections of E10 were read.
    - Dienes was read at abstract level.

  Recommendation: SUPPORTED (Strong), for the restated, necessary-not-sufficient form with a
    sensitivity/power clause.
