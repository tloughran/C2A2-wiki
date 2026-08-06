SEARCH-FOR-PRESUMPTION-685:
  Date searched: 2026-08-06
  Original item: PRESUMPTION-685
  Original statement: That deferring to a prior published figure is the
    conservative move; a run withheld its own 57 in favour of the prior day's
    24 on the ground that its parser had carried a bug, a rule that makes a
    figure durable in proportion to how long it has gone unchallenged. Risk:
    High.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-685
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Read a stated deference rule against the same run's opposite use of
        the same register.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Henrion, M. & Fischhoff, B., 1986. "Assessing uncertainty in physical
       constants." American Journal of Physics 54(9): 791-798. — The central
       finding, and it runs hard against the presumption. Examining historical
       measurement series and recommended values for the fundamental constants,
       the authors find reported uncertainties consistently biased toward
       underestimating actual error, comparable to persistent overconfidence in
       the subjective-probability literature. They document a bandwagon effect:
       speed-of-light measurements from 1876 to 1902 overestimated by roughly
       70 km/s, then from 1905 to 1950 underestimated by roughly 15 km/s. The
       mechanism is exactly the rule this item names — successive
       experimentalists treating the standing figure as the conservative
       reference — and the result is that the error survives longer, not that
       the record is safer.
    2. Jeng, M., 2007. "Bandwagon effects and error bars in particle physics."
       Nuclear Instruments and Methods in Physics Research A 571: 704-708. And:
       Jeng, M., 2006. "A selected history of expectation bias in physics."
       American Journal of Physics 74(7): 578. — Quantifies the same effect on
       a much larger corpus. A significant number of particle properties show
       reported values trending and clustering as a function of publication
       year rather than scattering randomly about the mean. The related
       observation on the Particle Data Group series is the sharpest form of
       the item's worry: measurements are distributed around *previous
       averages* with chi-squared about half that associated with distribution
       around the currently accepted value, and values shift over time but
       rarely by more than one standard deviation per step. Deference produces
       a slow, monotone, self-concealing drift — the opposite of conservatism.
    3. JCGM 100:2008, Evaluation of measurement data — Guide to the expression
       of uncertainty in measurement (GUM), BIPM. — The route to genuine
       partial support, and it is narrow. The GUM treats blunders in recording
       or analysing data as a distinct category from random variation, states
       that large blunders can usually be identified by proper review of the
       data while small ones may be masked by or appear as random variation,
       and insists that uncertainty evaluation is neither routine nor purely
       mathematical but depends on detailed knowledge of the measurand and the
       measurement. On this reading, a run that has *established* a defect in
       its own parser has an independent, documented cause for setting its
       output aside, and that is the recognised warrant. The support attaches
       to the documented-cause condition, not to the prior figure's seniority.
    4. Chang, G. et al., 2006 — five retractions (three in Science, two
       elsewhere) traced to an error in a homemade data-analysis program;
       reported in Miller, G., 2006. "A Scientist's Nightmare: Software Problem
       Leads to Five Retractions." Science 314. [Retraction count and the
       Science news framing confirmed this session via secondary sources; the
       original retraction notices were not fetched.] And: Soergel, D.A.W.,
       2015. "Rampant software errors undermine scientific results."
       F1000Research [author attribution uncertain — confirm before reuse]. —
       Supports the withdrawal half of the item's decision. When an analysis
       program is shown to be defective, the discipline's norm is to withdraw
       the affected results rather than publish them alongside a caveat. The
       most dangerous class is characterised as semantic bugs producing
       plausible but wrong results, which is precisely the situation of a
       parser that returns a number rather than an error.
    5. Blind analysis literature: "Blind analysis in Physics experiments: Is
       this trip necessary?" arXiv:2311.13542; and Klein, J.R. & Roodman, A.,
       2005. "Blind Analysis in Nuclear and Particle Physics." Annual Review of
       Nuclear and Particle Science 55. [Klein & Roodman UNVERIFIED — cited
       from established knowledge, not confirmed this session] — The
       discipline's engineered answer, and it inverts the item's rule. Blinding
       exists specifically to prevent the analyst from comparing a provisional
       result against the standing published value before deciding whether to
       keep it. Any procedure in which a new figure is checked against the
       prior figure and discarded on disagreement is the practice blinding was
       built to block.

  Strength of support: Weak

  Summary: The presumption as stated — that deference to a prior published
    figure is the conservative move — is not supported, and the measurement
    literature was written largely to refute it. Henrion and Fischhoff and Jeng
    document that deference to standing values produces systematic multi-decade
    bias with understated uncertainty, and the Particle Data Group series shows
    new measurements clustering around previous averages more tightly than
    around the truth. Blind analysis exists precisely to prevent the comparison
    the item's rule requires. There is a real and important zone of partial
    support: where a defect in the producing instrument has been independently
    established and documented, the GUM's treatment of blunders and the
    retraction record for analysis-code bugs both warrant setting the affected
    output aside. But that warrant is conditioned on documented cause, and it
    is symmetric — it says nothing about which figure should stand in the
    interim. The item's diagnosis holds: converting "my instrument is suspect"
    into "therefore the older figure stands" imports an asymmetry the
    literature does not license, and makes durability a function of elapsed
    unchallenged time.

  Caveats: The support turns entirely on one question the literature can
    answer only in principle: whether the prior day's 24 was produced by a code
    path that shares the defect. If it was, the parser bug invalidates both
    figures and neither should stand; the deference is then not conservative
    but arbitrary. If it demonstrably was not, the deference is defensible
    under the documented-cause condition and this item's criticism weakens
    substantially. Nothing in the located literature adjudicates that
    factual question, and this file cannot. Scope limits: the physical-constant
    and particle-physics evidence concerns figures with a true value and
    repeated independent measurement, whereas a parser count over a changing
    corpus may have no stable target, which weakens the bandwagon analogy —
    though it also removes the main justification for treating an older figure
    as better established. Source 4's second attribution is uncertain. The
    Klein & Roodman citation is unverified.

  NOVELTY-FLAG: Not raised. Both directions of this question are well covered.

  Recommendation: PARTIALLY-SUPPORTED

  Search scope: Comprehensive on the metrology and measurement-bias side;
    adequate elsewhere. Concepts searched: anchoring and first-value
    persistence; Henrion & Fischhoff and the bandwagon effect in physical
    constants; Particle Data Group historical series and expectation bias;
    blind analysis; GUM treatment of blunders and outlier rejection with
    documented cause; retraction norms following analysis-software defects.
    Not searched: official-statistics revision policy (e.g. GDP and CPI
    revision practice), which is the closest institutional analogue to a
    long-running record with a standing published figure, and is recommended as
    a follow-up seam.
