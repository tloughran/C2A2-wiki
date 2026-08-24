SEARCH-FOR-ASSUMPTION-943:
  Date searched: 2026-08-18
  Original item: ASSUMPTION-943
  Original statement: Whether partial correction of a systematic corpus defect is worse than none. Stated independently by three reviewers as an operating principle; never tested.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-943
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted a stated operating principle articulated independently by three reviewers in one day.
      15a: Searched for supporting literature; found a published demonstration that an attempted bias correction both failed to remove the target bias and introduced a new one in the opposite direction, plus a data-management framework that scores cleaning on the distortion it introduces rather than on defects removed.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Hanley, James A., 2017. "Correction of Selection Bias in Survey Data: Is the Statistical Cure Worse Than the Bias?" American Journal of Public Health 107(4): 503–505. (also PubMed 28272961) — Commissioned jointly by the editors of AJPH and the American Journal of Epidemiology to assess a published correction method. Hanley shows the approach used not only failed to correct the simulated selection bias but *introduced a new bias in the opposite direction of the true association*. This is a direct, published instance of the item's claim: a partial correction left the corpus further from the truth than no correction would have.
    2. Dasu, Tamraparni; Loh, Ji Meng, 2012. "Statistical Distortion: Consequences of Data Cleaning." Proceedings of the VLDB Endowment 5(11): 1674–1683 (arXiv:1208.1932). — Introduces statistical distortion as a necessary metric for evaluating cleaning strategies, and proposes evaluating any strategy along three dimensions — glitch improvement, statistical distortion, and cost. The framework's premise is that removing defects and improving the data are different quantities that can move in opposite directions, which is the general form of the item's principle.
    3. Editorial: "Note About Inaccurate Results Published in the American Journal of Epidemiology and the American Journal of Public Health," 2017 (PMC5343702). [Editorial note, authorship not individually attributed in this search pass.] — The joint-editorial context for source 1; corroborates that the failed correction was serious enough for two journals to act jointly, i.e. that the partial-correction harm was judged consequential rather than academic.

  Strength of support: Moderate

  Summary: The operating principle stated by the three reviewers is supported, though the support is narrower than the principle as worded. Hanley (2017) is a strong, directly on-point case: a method intended to correct selection bias in survey data was shown, against simulated ground truth, to leave a bias in the opposite direction — so the corrected corpus was not merely incompletely fixed but wrong in a new way, and wrong while carrying the credibility of having been corrected. That last property is the mechanism that makes partial correction potentially worse than none: an uncorrected systematic defect at least remains visible and uniformly present, whereas a partially corrected one is heterogeneous, no longer detectable by the original diagnostic, and now warranted as clean. Dasu and Loh (2012) generalise this into a measurement discipline, insisting that any cleaning strategy be scored on the distortion it introduces alongside the glitches it removes — an implicit concession that the two routinely diverge. The practical recommendation these sources jointly support is not "do not correct" but "do not correct without measuring distortion against the uncorrected baseline, and record which records were touched."

  Caveats: The claim as the reviewers stated it is universal ("partial correction is worse than none") and the located evidence is existential (partial correction *can* be worse than none, and was in at least one documented case). No source I found establishes the general claim, and Dasu and Loh's framework presupposes the opposite — that cleaning is usually net-beneficial and the task is to measure when it is not. Hanley's case is a single methodological dispute in epidemiology with simulated ground truth available, which is precisely the condition C2A2 does not have when repairing a wiki corpus; without ground truth, neither the original defect nor the distortion introduced can be measured, so the sources' own remedy is unavailable. The survivorship-artefact arm of the item — that selectively repaired records create a false impression about the unrepaired remainder — was searched but returned no source specific enough to cite; that specific mechanism should be treated as unsupported pending a broader search.

  Search scope: partial remediation and selective correction bias; statistical distortion from data cleaning; selection-bias correction failure; survivorship artefacts in corpus repair; selective row removal and exclusion bias; imputation-induced bias; systematic versus random corruption in training corpora. Preliminary — broader search recommended, specifically on survivorship artefacts from partial repair and on record-level provenance of corrections, neither of which this pass resolved.

  Recommendation: SUPPORTED

  NOVELTY-FLAG:
    Item: ASSUMPTION-943
    Searched: Data-cleaning distortion metrics; selection-bias correction failures; selective/partial remediation; survivorship bias in repaired corpora.
    Finding: The existential claim is well-evidenced. The *universal* operating principle as stated by the three reviewers — that partial correction of a systematic defect is categorically worse than none — has no located support, and the main data-management source assumes the contrary default. The specific survivorship mechanism (that repairing a subset misleads about the unrepaired remainder) returned nothing citable.
    Implication: Three reviewers independently converged on a principle stronger than the literature supports, which given PRESUMPTION-751's finding on correlated same-model agreement is itself worth noting — independent statement by same-model reviewers is weak evidence of independent derivation. Recommend the principle be reformulated existentially before it is relied on, and that the convergence be re-examined by 15c.
    Recommended status: NOVEL (as a universal principle; the existential form is supported)
