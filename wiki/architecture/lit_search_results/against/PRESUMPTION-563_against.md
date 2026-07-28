SEARCH-AGAINST-PRESUMPTION-563:
  Date searched: 2026-07-28
  Original item: PRESUMPTION-563
  Original statement: [inferred] Floating "learnable novelty" as "the quantitative handle on progress the program has been missing" presumes progress is a well-defined construct awaiting a measure; if it is underdetermined, adopting the metric would define progress rather than measure it, importing the definition from a paper about exploration in learning systems.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-563
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: surfaced from a metric proposed as the answer to an unspecified construct
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Chang, H. 2004. Inventing Temperature: Measurement and Scientific Progress. Oxford Studies in Philosophy of Science, OUP. — The decisive counterexample. Chang shows the concept of temperature was not fixed by antecedent theory but emerged THROUGH iterative cross-calibration of imperfect instruments; his notion of "epistemic iteration" is a process in which successive stages of knowledge each build on the preceding one, reaching a standard step-by-step without possessing a correct answer in advance. This directly refutes the presumption's implicit rule that a construct must be specified before it can be operationalised - the paradigm case of a successful quantitative construct did the opposite.
    2. Cronbach, L. J. & Meehl, P. E. 1955. "Construct Validity in Psychological Tests." Psychological Bulletin 52(4): 281-302. — The founding text of construct validity, invoked by the presumption, in fact describes construct development as iterative: "when a construct is fairly new, there may be few specifiable associations by which to pin down the concept. As research proceeds, the construct sends out roots in many directions, which attach it to more and more facts or other constructs." Construct validation is the co-development of measure and construct via a nomological network, not the validation of a measure against a pre-existing definition. The presumption's standard is stricter than its own authority.
    3. Bartha / SEP and Holyoak & Thagard on the discovery use of formal borrowings; plus the LLM-benchmark methodology literature (e.g. "Establishing Construct Validity in LLM Capability Benchmarks Requires Nomological Networks," arXiv:2603.15121). — The recommended remedy in current practice is not "define the construct first" but "build the nomological network around the candidate measure," i.e. adopt provisionally and test the measure's relations to other observables. That is an adoption-with-conditions route, which the presumption's framing forecloses.
    4. Boundary condition (partially conceding the presumption): the surrogation and Goodhart literature is real and is not challenged here - once a proxy is institutionalised it does tend to displace the construct. The located challenge is not that this risk is absent, but that the correct response is a validation programme around a provisional measure, not abstention from measurement.

  Strength of challenge: Strong

  Summary: The presumption's methodological premise - that a construct must be well-defined before a measure can legitimately be adopted - is contradicted by both the history and the theory of measurement. Chang's study of thermometry shows the concept of temperature was invented in the process of measuring it, via epistemic iteration, with no correct answer available in advance; this is the standard example of a construct that was underdetermined and became determinate through measurement. Cronbach & Meehl, the source the presumption's vocabulary comes from, explicitly describe new constructs as thinly specified and progressively pinned down through the nomological network as research proceeds. So the fact that C2A2 lacks an independent written specification of "progress" is not a bar to adopting a candidate metric; it is the normal starting condition. The presumption's real and surviving contribution is the second clause: adopting the metric WOULD partly define progress, and doing so silently, with the definition imported unexamined from a paper about exploration in learning systems, is the failure mode - not measurement itself.

  Specific risks: If C2A2 adopts the presumption as a bar to adoption, it forgoes any quantitative handle indefinitely, since no independent specification of progress exists or is likely to appear from introspection alone - and the corpus continues to grow with progress assessed narratively. If C2A2 ignores the presumption, "learnable novelty" becomes the operative definition of progress by default, complete with the scope conditions of its source domain (exploration in learning systems, where novelty is instrumentally valuable and cheaply generated), and Goodhart pressure then rewards novelty production over whatever the programme actually cares about.

  Mitigations available: Adopt provisionally and declare it. Per Cronbach & Meehl, register the metric with a nomological network: name at least three independent observables that should co-vary with genuine progress (e.g. bridge survival across review, external-referent verification rate, reduction in open questions) and check whether learnable novelty tracks them. Per Chang, treat the definition as revisable across iterations and record each revision. Write down the source paper's scope conditions explicitly and mark which ones C2A2 violates. And guard against surrogation by never using the metric as a target while it is under validation.

  STEELMAN:
    Item: PRESUMPTION-563
    Strongest counterargument (against the presumption): The requirement that a construct be specified before it is operationalised is not how quantitative constructs are actually established. Chang's history of thermometry shows temperature was devised in the very process of being measured, through epistemic iteration - reaching a standard stepwise without a correct answer to check against - and Cronbach & Meehl, the source of the construct-validity vocabulary, say plainly that a new construct starts with few specifiable associations and is pinned down as research proceeds. On that account C2A2's lack of a prior written specification of progress is the ordinary starting condition for a measurement programme, not a disqualification, and refusing to operationalise until the construct is defined is a demand that no successful construct has met. The metric partly defining progress is not a defect either - it is what measurement does; the defect would be doing it silently and without a validation network.
    What would need to be true for C2A2 to be safe: the metric is adopted as provisional and revisable, its source-domain scope conditions are written down, it is embedded in a nomological network of at least a few independent observables, and it is never used as an optimisation target during validation.
    How to test: implement the metric alongside two or three independent progress indicators over several cycles and check whether they co-vary. Divergence falsifies the metric's construct validity cheaply and empirically - which is a stronger test than any prior specification exercise could have provided.

  Recommendation: CHALLENGED
