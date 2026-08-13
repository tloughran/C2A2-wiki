# PRESUMPTION-778 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-778

**Date searched:** 2026-08-13

**Original item:** PRESUMPTION-778

**Original statement:** That a defect-population count is a measurement of the corpus rather than a property of the instrument — four runs, one day, one class, figures of 166, 52, 45, 102.

### PROVENANCE

- **Origin:** 14b
- **Chain:** [14b → 15b]
- **Item type:** PRESUMPTION (unstated — surfaced by inference)
- **Transform at each step:**
  - 14b: Inferred, from four same-day counts of one nominal defect class differing by a factor of nearly four, that the system treats such a count as a property of the corpus when it is at least partly a property of the counting instrument; risk graded High.
  - 15b: Searched for literature challenging the inference — capture-recapture in software inspections, measurement-system analysis, and the interpretation of inter-instrument disagreement.
- **Current status:** PARTIALLY-CHALLENGED

**Polarity note (explicit inversion).** The item is a PRESUMPTION written as "That [belief the system holds]", where 14b judges the belief unsafe. The AGAINST direction is therefore not "the belief is fine" but: **14b's worry is overstated, mis-scoped, or its implied remedy is wrong.** Here the challenged step is the move from *dispersion* to *instrument-dependence*, and the implied remedy of discounting or suspending defect counts.

### Challenging evidence found: Yes

### Sources

1. **Petersson, H., Thelin, T., Runeson, P., Wohlin, C., 2004. "Capture–recapture in software inspections after 10 years research — theory, evaluation and application." *Journal of Systems and Software* 72(3).** — The entire method rests on treating disagreement between independent detectors as the *estimator input*, not as evidence that counting is invalid. Defects found by one inspector and re-found by another give the recapture rate; the dispersion 14b flags is exactly the signal capture-recapture consumes. The presumption treats as a defeater what a decade of software-inspection research treats as data.
2. **Wohlin, C., Runeson, P., 1995. "An experimental evaluation of capture-recapture in software inspections." *Software Testing, Verification and Reliability* 5(4).** — Experimental demonstration that inspector-to-inspector variation in a fixed artefact is normal and quantitatively tractable. Boundary condition on the challenge: estimates are poor when the number of detectors is small.
3. **"A Comprehensive Evaluation of Capture-Recapture Models for Estimating Software Defect Content." *IEEE Transactions on Software Engineering*, 2000. [author list not confirmed in search snippets — commonly attributed to Briand, El Emam, Freimut and Laitenberger].** — Documents that estimators are strongly affected by the number of inspectors and that with too few detectors underestimation can be substantial, and that statistical dependence between inspectors is ubiquitous. This bounds *both* sides: it limits how much the four counts can be turned into an estimate, and it means the observed dispersion is under-, not over-, dispersed relative to true variety.
4. **AIAG *Measurement Systems Analysis* / ASQ Gage R&R materials on repeatability, reproducibility and attribute agreement analysis.** — MSA partitions observed variation into equipment variation, operator variation and part variation, and requires *the same characteristic, the same operational definition, and replicate measurements of the same parts*. Four counts produced by four differently-scoped procedures on one nominal class are not four replicates; they are four different measurands. On MSA's own terms the dispersion is not attributable to instrument repeatability at all until the operational definitions are shown to be identical.
5. **ASQ / attribute-agreement guidance (limitations).** — Attribute Gage R&R "cannot identify how much of the disagreement comes from repeatability versus reproducibility." Cited against the presumption's implicit confidence that the observed spread diagnoses the instrument: with pass/fail-style detectors, spread alone is formally uninformative about which source produced it.

### Strength of challenge: Moderate

### Summary

The observation is sound and the numbers are striking, but the inference has a gap. Dispersion among independently derived counts of one population is the normal condition of defect measurement, not an anomaly, and there is an established estimation literature that treats it as the input to a population estimate rather than as grounds for distrusting counting. More damaging to the presumption's framing, measurement-system analysis — the framework whose vocabulary the item borrows — attributes variation to the instrument only when the same characteristic is measured under the same operational definition by replicate procedures. Four counts of "one class" produced by four differently scoped sweeps on the same day violate that precondition, which means the spread of 166/52/45/102 is at least as likely to be *definitional* (different inclusion criteria, different denominators, different windows) as *instrumental*. The strong reading — that a defect count is a property of the instrument — would, if generalised, make every count in the register uninterpretable, including the counts that would be needed to detect the problem. The defensible residual is narrower: the four figures were not accompanied by their operational definitions, and no estimate was formed from their overlap.

### Specific risks

If the presumption is adopted at full strength, the system acquires a general licence to discount its own quantitative findings, which is corrosive and asymmetric — it will be invoked against inconvenient counts more readily than convenient ones. If it is dismissed, the concrete hazard is a severity grade or a repair-scope decision resting on whichever of four incompatible figures happened to be in hand, with no record of which population each figure covered. The realistic failure is not a phantom defect population; it is a numerator and a denominator drawn from different sweeps.

### Mitigations available

(a) Attach an operational definition to every count — inclusion criterion, artefact set, time window — so that spread can be decomposed into definitional and instrumental components before either is asserted. (b) Where two or more sweeps genuinely share a definition, record the overlap (defects found by both) and compute a capture-recapture estimate rather than reporting the raw counts side by side; with four detectors this is at the low end of what the literature considers reliable, so report it with an interval. (c) Do not treat agreement between sweeps as corroboration without checking detector independence — the same literature reports that inspector dependence is ubiquitous. (d) Report an UNCALIBRATED marker (per the existing PREMISE-124 pattern) rather than suppressing the count.

### Recommendation: PARTIALLY-CHALLENGED

---

## STEELMAN

**Item:** PRESUMPTION-778

**Strongest counterargument:** Dispersion is what defect measurement looks like when it is working. The software-inspection literature spent a decade building estimators whose *only* input is the disagreement between independent detectors; treating that disagreement as a reason to doubt that a corpus has a defect population inverts the method. Worse, the presumption reaches for the vocabulary of measurement-system analysis without satisfying its preconditions: MSA attributes variance to an instrument only across replicate measurements of the same characteristic under one operational definition, and four same-day sweeps of "one class" with different inclusion criteria are four measurands, not four replicates. The most probable explanation of 166/52/45/102 is therefore mundane and fixable — the sweeps counted different things — and the presumption's framing directs attention away from that explanation toward an unfalsifiable one. Generalised, the claim also defeats itself: if a count is a property of the instrument, then so is the count of instrument disagreements the presumption relies on.

**What would need to be true for C2A2 to be safe:** Each count must carry its operational definition, and any comparison between counts must first establish that the definitions coincide. Where they do, the overlap must be recorded so that an estimate with an interval can replace a bare figure. Under those conditions the dispersion becomes diagnostic rather than corrosive, and the presumption reduces to a documentation requirement.

**How to test:** Take the four sweeps that produced 166, 52, 45 and 102, and for each recover the inclusion criterion and the artefact set. Then compute the pairwise overlap. Two outcomes discriminate: if the four criteria differ, the dispersion is definitional and the presumption is mis-scoped; if the criteria coincide and the overlap is low, the presumption is vindicated and a capture-recapture estimate should replace all four figures. This is a bounded, one-session exercise on data already on disk.

---

## Search scope

Moderate. Query families executed: capture-recapture in software inspections (theory, evaluation, known limitations); measurement-system analysis and attribute agreement analysis. Not searched: the inter-rater-reliability literature proper (Cohen/Fleiss kappa and its known pathologies with skewed base rates), the Orthogonal Defect Classification literature on classifier disagreement, and the ecology literature on capture-recapture assumption violations. Broader search recommended, particularly on kappa under low prevalence, which bears directly on this item.
