SEARCH-FOR-PRESUMPTION-751:
  Date searched: 2026-08-18
  Original item: PRESUMPTION-751
  Original statement: Whether agreement between two same-model readers is evidence about the world or about the model. Risk: Critical.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-751
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption from operational review; queued as literature-testable.
      15a: Searched for supporting literature; found direct, quantitative, recent evidence that agreement among LLM readers is largely a property of the shared model rather than of the item being judged.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Kohli, Guneet, 2026. "Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels." arXiv:2605.29800 [cs.CL], submitted 28 May 2026. — A panel of 9 frontier LLMs drawn from 7 *different* model families supplies only about 2 independent votes' worth of information; roughly three-quarters of nominal independence is lost because the models err on the same items. Panel accuracy falls 8–22 percentage points short of the independent-voting ideal, and the best single judge matches or beats the full panel. Quantified with Kish effective sample size (n_eff) against a Condorcet null; robust across prompt variants, temperature, chain-of-thought, and a pairwise-preference task.
    2. Kim, Elliot; Garg, Avi; Peng, Kenny; Garg, Nikhil, 2025. "Correlated Errors in Large Language Models." ICML 2025; arXiv:2506.07962. — Measures error correlation across many LLMs and finds it is substantially *higher* for models sharing a provider, sharing a base architecture, or of similar size; correlation also rises with individual model accuracy. Establishes the shared-lineage gradient that makes the same-model case the worst case.

  Strength of support: Strong

  Summary: The presumption is directly and quantitatively supported. Kohli (2026) shows that even a maximally diverse panel — nine frontier models from seven distinct families — retains only ~25% of the independence that a naive reading of "they agreed" would imply, and that neither more judges nor better aggregation recovers the deficit, because the bottleneck is correlated judges rather than the aggregation rule. Kim et al. (2025) supplies the gradient: correlation increases with shared provider and shared base architecture. Two readers instantiated from the *same* model sit at the extreme of that gradient, so their agreement carries strictly less information about the world than the cross-family case that already loses three-quarters of its nominal independence. The concurring finding that the best single judge matches the full panel is the sharpest operational form of the concern: a second same-model reader may be adding cost without adding evidence. Kohli's most damaging result for the pipeline is that ensembles suppress disagreement precisely on the items where the shared model is collectively wrong — the failure is silent and correlated with difficulty.

  Caveats: Kohli (2026) is a single-author preprint (14 pp) with no confirmed peer review as of this search; its findings are strong but should be treated as not-yet-refereed. Both sources measure *cross-model* correlation and extrapolate to the same-model case a fortiori — I found no study that isolates agreement between two independently-sampled readers of an identical model at identical settings, which is the pipeline's actual configuration. The n_eff framework assumes an exchangeable-judge model; systems that deliberately vary prompt or role between readers may recover some independence, and neither paper quantifies how much.

  Search scope: LLM ensemble error correlation; LLM-as-judge panel independence; correlated estimator agreement and information content; effective sample size for correlated voters; Condorcet jury theorem with dependent voters; adversarial collaboration (searched as a term — no verified hit retained; the psychology literature on adversarial collaboration did not surface a source I could attribute with confidence, so none is cited). Comprehensive for the LLM-ensemble arm; preliminary for the classical-statistics arm (correlated estimators / effective sample size in survey and meta-analytic settings) — a broader search there would likely add older, well-established formal results.

  Recommendation: SUPPORTED

  FLAG-FOR-15c: This item bears on the warrant of the pipeline that searched it. The literature located here implies that any C2A2 finding resting on agreement between two same-model readers has an inflated apparent confidence, and that the inflation is largest exactly where the shared model is systematically wrong. This search itself was conducted by a single model, so the flag is self-referential and cannot be discharged from within the pipeline. Recommend 15c treat the effective-sample-size correction as applying to the review layer, not only to the reviewed corpus.
