SEARCH-AGAINST-PRESUMPTION-753:
  Date searched: 2026-08-18
  Original item: PRESUMPTION-753
  Original statement: Whether retraction rate indicates convergence or instability. Risk: High.

  Reading challenged: The operative (reassuring) reading — that a rising or non-trivial retraction rate is a health signal, evidence that the system is converging because it is self-correcting. This search attacks that reading, and also attacks the weaker fallback that retraction rate is a *measurable* proxy for anything about the underlying error process.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-753
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption from operational review; queued as literature-testable.
      15b: Searched for challenging literature; found that retraction rate in science is dominated by scrutiny intensity rather than error prevalence, and is therefore a measure of the detector, not of the corpus.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Fang, F.C. & Casadevall, A. (2011). "Retracted Science and the Retraction Index." Infection and Immunity 79(10), 3855–3859. — Introduces the retraction index and shows retraction frequency correlates strongly with journal impact factor. This is the central challenge: retraction rate covaries with *attention*, not with error rate. A venue that is read harder retracts more. Applied to C2A2: a rising retraction rate can be produced entirely by increasing review intensity while the underlying defect rate is flat, and can be produced by decreasing review intensity while the defect rate rises. The metric is not identified. [VERIFIED — journal page and author-hosted PDF located; ASM journal, 2011.]
    2. Fang, F.C., Steen, R.G., & Casadevall, A. (2012). "Misconduct accounts for the majority of retracted scientific publications." PNAS 109(42), 17028–17033. — Roughly two-thirds of retractions are attributable to misconduct rather than honest error. A retraction rate is therefore a *mixture* of at least two generating processes with opposite interpretations: honest self-correction (convergence-ish) and detected bad faith (instability-ish). Reading a single scalar as evidence for one of them is unwarranted. [VERIFIED — PNAS and PubMed records located.]
    3. Brainard, J. & You, J. (2018). "What a massive database of retracted papers reveals about science publishing's 'death penalty'." Science (news feature), analysis of the Retraction Watch database. — Reports retraction at roughly 4 per 10,000 papers, and — critically — modelling suggesting the rate would be very different if all journals received uniform scrutiny. Establishes that the observed rate is a scrutiny artefact and a *lower bound* on the serious-flaw rate, not an estimate of it. [Attribution: Science news feature; author names as listed by Science. Treat as journalism reporting on the Retraction Watch dataset, not as peer-reviewed primary research.]
    4. Journal of Korean Medical Science (2025). "Fifty Years of Retracted Medical Publications From 1975 to 2024: A Comprehensive Analysis of Trends, Reasons, and Countries Using the Retraction Watch Database." — Documents a consistent multi-decade *rise* in retractions across all categories and attributes it to heightened community vigilance. The same rising curve is read by different authors as improving health and as worsening integrity; the field cannot agree on the sign of the signal. That interpretive indeterminacy is itself the challenge. [unverified — author list not confirmed in this search; journal, year and dataset confirmed.]
    5. "Self-correction in science: The effect of retraction on the frequency of citations." PLOS ONE (2022). — Retraction reduces but does not eliminate subsequent citation. A retraction event therefore does not terminate the influence of the retracted item, so counting retractions overstates how much correction has actually propagated. [unverified — author list not confirmed in this search; journal and finding located.]

  Strength of challenge: Strong

  Summary: The scientometric literature is close to unanimous that retraction rate is not a clean indicator of anything about the underlying error process. Fang and Casadevall's retraction index shows the rate tracks scrutiny intensity (proxied by impact factor); Fang, Steen and Casadevall show the retraction population is a mixture of honest error and misconduct with opposite diagnostic meanings; the Retraction Watch analyses show the observed rate is a lower bound on serious flaws and would move substantially under uniform scrutiny. Consequently the presumption's framing — convergence *or* instability — presents a false dichotomy over a quantity that measures neither. The literature's actual finding is a third option the item does not consider: retraction rate measures the intensity and coverage of the detection apparatus. For C2A2, a day on which four flags were retracted tells you the reviewers were reading hard that day; on its own it tells you nothing about whether the corpus is settling or thrashing.

  Specific risks:
    - Metric non-identification: any C2A2 dashboard, gate, or governance claim keyed to retraction rate is reading a confounded quantity. Two opposite states of the world (excellent detection over a bad corpus; poor detection over a good corpus) can produce the same number.
    - Perverse incentive: if a low retraction rate is read as health, the cheapest way to improve the metric is to reduce scrutiny. This is the exact failure mode the impact-factor correlation demonstrates in reverse.
    - Mixture confound: without classifying each retraction by cause (honest error / method drift / bad-faith or fabricated flag / policy change), the aggregate is uninterpretable.
    - Denominator instability: retraction *rate* requires a stable denominator. If C2A2's per-day claim volume varies with run configuration, the rate moves for reasons unrelated to either convergence or instability.
    - Incomplete propagation: per the PLOS ONE finding, retraction does not stop downstream use. A retraction that is counted as "corrected" may still be doing work in derived artefacts.

  Mitigations available:
    - Report retraction *count alongside review effort* (items examined, reviewer-hours, run budget). The ratio retractions/items-examined is closer to identified than retractions/items-published.
    - Stratify retractions by cause at the moment of retraction; never aggregate honest-error and bad-flag retractions into one series.
    - Use a directional test rather than a level test: oscillation (an item flagged, retracted, re-flagged) is the instability signal; monotone decay of flag rate under *constant* review intensity is the convergence signal. Neither is readable from raw retraction rate.
    - Hold review intensity fixed on a sentinel subset of the corpus so that the rate on that subset is comparable across runs — the scientometric analogue of uniform scrutiny.
    - Track downstream propagation of each retraction (which derived artefacts were regenerated), since retraction ≠ correction.

  Search scope: Web search across PNAS, ASM journals, Science, PLOS, PMC and Retraction Watch-derived analyses for: retraction rate as field-health indicator; retraction index and impact factor; causes of retraction; incidence of research fraud; effect of retraction on citation. Searched 2026-08-18. Session web-search budget was exhausted before I could cover the belief-revision/oscillation half of the brief (Bayesian belief-revision instability, opinion-dynamics oscillation, AIMD-style convergence criteria). That gap is material: the "instability" horn of the item is under-searched relative to the "convergence" horn, and 15c should note the asymmetry.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-753
    Strongest counterargument: The scientometric confound arises because science has thousands of uncoordinated venues with wildly heterogeneous scrutiny; C2A2 does not. Within a single pipeline with a logged, reconstructable review protocol, review intensity is *observable*, so the confound that defeats the retraction index in publishing is in principle controllable here. If C2A2 records reviewer-effort per run, the retraction rate can be conditioned on it and recovers interpretability. Moreover, the item may be doing useful work even as a confounded metric: a sudden spike in retractions is a legitimate trigger to go and look, regardless of what it ultimately means. Treating it as an alarm rather than a measurement is defensible.
    What would need to be true for C2A2 to be safe: (a) Review intensity per run must be logged and stable enough to serve as a denominator; (b) every retraction must be typed by cause at the moment it happens, so the mixture can be decomposed; (c) no gate, budget decision, or health claim may be keyed to the raw rate — only to the conditioned rate or to a directional oscillation statistic; (d) retraction must be defined to include propagation to derived artefacts, so the count means "corrected" and not merely "annotated".
    How to test: Instrument a controlled sentinel corpus of known composition — seed it with a known number of injected defects of known types. Run the review pipeline at two deliberately different intensities. If retraction rate moves with intensity while the seeded defect rate is held constant, the metric is confounded in C2A2 exactly as in publishing, and the presumption is refuted operationally, not just by analogy. Second test: for each retracted flag, record whether the same item is re-flagged within N runs. A high re-flag rate is oscillation (instability); a low one under constant intensity is convergence. That statistic, not the retraction rate, is the one to govern on.
