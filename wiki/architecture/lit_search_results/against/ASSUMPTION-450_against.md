SEARCH-AGAINST-ASSUMPTION-450:
  Date searched: 2026-07-13
  Original item: ASSUMPTION-450
  Original statement: "Active inference has no fatigue term and cannot obviously derive why a well-fitted model degrades once its goal is met; if that absence holds, aging is evidence about FEP rather than an application of it."

  PROVENANCE:
    Origin: 14a
    Chain: 14a -> 15b
    Original item: ASSUMPTION-450
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-12 EOD run (second consecutive weekly flag)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. [Stephan, K.E., Manjaly, Z.M., Mathys, C.D. et al. (2016). "Allostatic self-efficacy: a metacognitive theory of dyshomeostasis-induced fatigue and depression." Frontiers in Human Neuroscience 10:550. — THE SHARPEST THREAT. This IS a fatigue term inside active inference: a metacognitive layer tracks the interoceptive-allostatic circuit's success, and persistent prediction error drives a downward-updating belief in one's own regulatory capacity, yielding fatigue and then depression. Endogenous, model-internal degradation of the control model, derived from FEP machinery. The claim's first clause — "active inference has no fatigue term" — is, as stated, false.]
    2. [Cieri, F., Zhuang, X., Caldwell, J.Z.K. & Cordes, D. (2021). "Brain entropy during aging through a free energy principle approach." Frontiers in Human Neuroscience 15:647513. — An explicit FEP treatment of aging and Alzheimer's via brain entropy. Here aging is an APPLICATION of the FEP, not an anomaly for it — the exact inversion of the claim's conclusion.]
    3. [Kuchling, F., Friston, K., Georgiev, G. & Levin, M. (2020). "Morphogenesis as Bayesian inference: a variational approach to pattern formation and control in complex biological systems." Physics of Life Reviews 33:88-108. — The Friston-Levin collaboration itself. Cells are free-energy-minimising agents with generative models of target morphology; degraded or corrupted bioelectric priors are the FEP-native route to loss of pattern maintenance. Directly relevant, since this is the very bridge the claim is gating.]
    4. [Chao, Z.C. et al. (2021). "Human brain ages with hierarchy-selective attenuation of prediction errors." Cerebral Cortex 31(4):2156-2169. — Empirical precision-decay: aging selectively attenuates HIGHER-LEVEL prediction errors, i.e. Bayesian updating degrades in a structured way. Precision is an existing FEP parameter, so degradation already has a native home in the formalism.]
    5. [Greenhouse-Tucknott, A. et al. (2021/2022) and the interoceptive active-inference fatigue lineage. — Extends allostatic self-efficacy to a unified model of effort and chronic fatigue: sustained interoceptive mismatch degrades confidence in control models.]
  Strength of challenge: Strong (against the claim AS STATED); Weak-to-Moderate (against the claim's precise intended form)
  Summary: The claim's first clause is refuted by a single well-known paper: Stephan et al. (2016) is a fatigue term, constructed inside active inference, in which a model's belief about its own regulatory competence degrades endogenously. Cieri et al. (2021) go further and treat aging itself AS an FEP application, precisely inverting the claim's conclusion. Precision is a free parameter in the FEP, and its decay in aging is empirically documented (Chao et al. 2021), so degradation has a native home in the machinery. What survives is a much narrower and more interesting question, and the claim's author may have meant it: does any FEP formalism predict decay in a system with INTACT RESOURCES, NO EXOGENOUS DAMAGE, and a SATISFIED generative model? Stephan's fatigue arises from SUSTAINED FAILURE (dyshomeostasis), not from success — so it does not, strictly, answer the "well-fitted model that has met its goal" case. The claim as written is false; the claim as apparently intended is still open.
  Specific risks: This item gates the friston_levin standalone-synthesis promotion and has now been flagged two weeks running. Promoting a synthesis whose headline is "FEP has no fatigue term" would put C2A2's name behind a claim refuted by a 2016 paper in the field's own flagship venue. The reputational and epistemic cost of that is high and entirely avoidable.
  Mitigations available: Restate the assumption precisely, then re-test the narrow form. The narrow form is a genuine and possibly publishable question; the broad form is simply wrong.

  STEELMAN:
    Item: ASSUMPTION-450
    Strongest counterargument: The FEP does not merely tolerate degradation — it PARAMETERISES it. Precision is a free parameter, and a metacognitive belief about one's own allostatic competence (Stephan et al. 2016) is exactly a fatigue term that EMERGES FROM, rather than is bolted onto, the variational machinery. Aging is then falling precision plus accumulating irreducible prediction error in an unwinnable homeostatic game — an application of the FEP, not evidence against it. C2A2's assumption reads as an argument from the searcher's unfamiliarity rather than from the corpus.
    What would need to be true for C2A2 to be safe: One would have to show that these accounts are DESCRIPTIVE RE-LABELLINGS — that they take decay as an empirical input (precision declines; errors accumulate) and re-express it in FEP vocabulary, rather than deriving from free-energy minimisation alone that a well-fitted model MUST degrade. If precision decay must be stipulated exogenously (thermodynamic wear, somatic damage), then the claim's narrow form survives and aging remains evidence ABOUT the FEP.
    How to test: Read Stephan et al. (2016) in full and ask one question of it: is the downward revision of allostatic self-efficacy DERIVED from free-energy minimisation in a system with intact resources and a satisfied model, or is it triggered by exogenous persistent prediction error? If the latter, ASSUMPTION-450's narrow form stands and should be restated in those terms. This is a single-paper read and should be done before the friston_levin promotion, not after.
  Recommendation: CHALLENGED
