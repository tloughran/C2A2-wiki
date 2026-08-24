SEARCH-FOR-ASSUMPTION-1176:
  Date searched: 2026-08-24
  Original item: ASSUMPTION-1176
  Original statement: "N>=3 licenses only R>=0.464 at 90% confidence; R>=0.80 needs n=11." Bears on every
    C2A2 gate of the form "released at N corroborating sources."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1176
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as a stated quantitative claim about what a corroboration count licenses, together with
        its stated scope (every gate expressed as a raw source count).
      15a: Searched for supporting literature, and verified the arithmetic independently (2026-08-24)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Clopper, C. J. & Pearson, E. S. 1934. "The Use of Confidence or Fiducial Limits Illustrated in the Case
       of the Binomial." *Biometrika* 26(4): 404–413. — The exact interval that generates the stated numbers.
       For x successes in n independent Bernoulli trials, the one-sided lower 100(1−α)% confidence limit when
       x = n is the value p_L satisfying p_L^n = α. This searcher computed the values directly rather than
       relying on a recalled table:
         n=3,  α=0.10 → p_L = 0.10^(1/3)  = 0.4642
         n=10, α=0.10 → p_L = 0.10^(1/10) = 0.7943   (below 0.80)
         n=11, α=0.10 → p_L = 0.10^(1/11) = 0.8111   (first n at or above 0.80)
       And ln(0.10)/ln(0.80) = 10.32, so n=11 is the smallest integer satisfying the second clause. Both stated
       figures reproduce exactly. The item is not an estimate or a rule of thumb; it is an identity.
    2. Louis, T. A. 1981. "Confidence Intervals for a Binomial Parameter After Observing No Successes."
       *The American Statistician* 35(3): 154. — The complementary case (x = 0), which is the same identity
       reflected. Establishes that the all-agree / none-agree situation is a recognised and separately treated
       problem in the binomial-interval literature precisely because the point estimate (1 or 0) is maximally
       misleading about what the data license.
    3. Hanley, J. A. & Lippman-Hand, A. 1983. "If Nothing Goes Wrong, Is Everything All Right? Interpreting
       Zero Numerators." *JAMA* 249(13): 1743–1745. — The canonical clinical statement of the same logic and
       the origin of the "rule of three" (with zero events in n subjects, 0 to 3/n is an approximate 95%
       interval). Hanley and Lippman-Hand's emphasis is the one this item makes: *observing zero events does
       not justify concluding the underlying risk is zero*, and by symmetry observing n-for-n agreement does
       not justify concluding the underlying agreement rate is high. Their paper exists because practitioners
       systematically read small unanimous samples as strong evidence. See also Jovanovic, B. D. & Levy, P. S.
       1997, "A Look at the Rule of Three," *The American Statistician* 51(2): 137–139, for the derivation and
       its accuracy limits.
    4. Hedges, L. V. & Olkin, I. 1980. "Vote-Counting Methods in Research Synthesis." *Psychological Bulletin*
       88(2): 359–369. — Support for the item's second, more consequential limb: evidence thresholds expressed
       as raw counts of corroborating sources are not merely imprecise, they can be actively perverse. Hedges
       and Olkin proved that the power of a vote-counting rule can be *lower* than the power of the individual
       studies it aggregates, and that when the component power is below roughly one third, the probability of
       detecting a true effect *decreases* toward zero as the number of studies increases. Adding sources can
       make a count-based gate worse. See also "Why 'Vote-Counting' Is Never Acceptable in Evidence Synthesis"
       (2022; author list not verified) for the current methodological consensus, and Hedges & Olkin 1985,
       *Statistical Methods for Meta-Analysis*, Academic Press, for the standard treatment.
    5. Beach, M. et al. 2015. "If a Little Bit Is Wrong, How Much Is Alright? Interpreting the Significance of
       Small Numerators in Clinical Trials." *Anaesthesia* 70(11) (author list not fully verified); and
       Uzoigwe, C. E. 2015, "A Rule of Thumb for Estimating the Lower Confidence Interval in Trials with Small
       Event Rates," *Anaesthesia* 70(12). — Contemporary applied extensions confirming that the small-n
       interval problem remains a live source of misreading in practice, not a settled historical curiosity.

  Strength of support: Strong

  Summary: The numerical claim is exactly correct and is a standard result, not a novel one. Both figures are
  the Clopper–Pearson exact one-sided lower confidence limit for a binomial proportion under n-for-n
  agreement at α = 0.10, and both were reproduced independently here to four decimal places: 0.4642 at n = 3,
  and n = 11 as the least n whose bound reaches 0.80. The surrounding literature — Louis on zero numerators,
  Hanley and Lippman-Hand's rule of three, and the applied follow-ups — exists specifically because unanimous
  small samples are systematically over-read, which is the behaviour the item is warning against. The item's
  scope claim is separately and more strongly supported: Hedges and Olkin established forty-five years ago
  that vote-counting is not a conservative approximation to evidence synthesis but a rule whose power can fall
  below that of its inputs and can *decline* as inputs accumulate. A gate of the form "released at N
  corroborating sources" is a vote-counting rule with the significance test removed, and inherits that defect
  while discarding the only quantity (precision) that would let it be repaired.

  Caveats: One point of interpretation matters more than any of the sources. The arithmetic identifies R as a
  *binomial proportion* — an underlying agreement or corroboration rate — not as a Pearson correlation or a
  reliability coefficient. If "R" is intended in either of the latter senses the stated numbers do not follow:
  the small-n confidence bounds for a correlation coefficient are governed by the Fisher z transform and give
  materially different values (for n = 3, a one-sided 90% lower bound on ρ from an observed r is far weaker
  than 0.464 for almost any r). The claim should be read, and if necessary restated, as a claim about
  agreement rates. Second, the identity assumes the n sources are *independent* Bernoulli trials. Where
  corroborating sources share a corpus, a parser, a model family, or an author community, the effective n is
  smaller than the nominal n and 0.464 is an overestimate of what n = 3 licenses — so the item errs on the
  generous side, which is the safe direction for its argument but means the true bound is worse than stated.
  Third, α = 0.10 one-sided is a weak confidence level by most conventions; at 95% the n = 3 bound falls to
  0.368 and reaching 0.80 requires n = 14. Search scope: good and, unusually for this queue, closed — the
  claim is a mathematical identity that was verified rather than merely corroborated; the literature search
  served to place it and to test the second limb. Did NOT cover Bayesian alternatives (Jeffreys or
  beta-binomial credible intervals), which would give slightly different and generally less conservative
  numbers and would be the natural objection to raise.

  Recommendation: SUPPORTED
