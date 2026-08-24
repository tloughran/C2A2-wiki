SEARCH-FOR-ASSUMPTION-1150:
  Date searched: 2026-08-19
  Original item: ASSUMPTION-1150
  Original statement: Concordance-weighted confidence was invalidated system-wide by the pipeline that
    uses it: "Kohli 2026 finds nine models from seven families supply ~2 independent votes; correlation
    *rises* with capability … This invalidates concordance-weighted confidence across the system —
    including this run's own 15a/15b concordance."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1150
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted the reflexive invalidation from two independent reporters and the mid-run change of
        disposition method that followed it.
      15a: Searched for supporting literature (2026-08-19)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Kim, E., Garg, A., Peng, K., & Garg, N. (2025). "Correlated Errors in Large Language Models."
       arXiv:2506.07962; accepted to ICML 2025. [author list and abstract verified directly from the
       arXiv abstract page, 2026-08-19] — Large-scale evaluation of 350+ LLMs on two leaderboards and a
       resume-screening task. Finds substantial correlation in model errors (models agree 60% of the time
       when both err on one leaderboard dataset). Critically for this item: "larger and more accurate
       models have highly correlated errors, even with distinct architectures and providers." Explicitly
       traces downstream effects into LLM-as-judge evaluation. This is direct support for BOTH limbs of
       the assumption — non-independence, and correlation rising with capability.
    2. Kuai, C., Jiang, J., Zhu, Z., Wang, H., Wu, K., Li, Z., Zhang, Y., Liu, C., Tu, Z., Fan, Z., &
       Zhou, Y. (2026). "How Independent are Large Language Models? A Statistical Framework for Auditing
       Behavioral Entanglement and Reweighting Verifier Ensembles." arXiv:2604.07650. [author list and
       abstract verified directly from the arXiv abstract page, 2026-08-19] — 18 LLMs, six families.
       States that multi-model systems "such as LLM-as-a-judge pipelines and ensemble verification …
       implicitly assume independent signals," and that shared pretraining, distillation and alignment
       induce latent entanglement so that "apparent agreement reflects shared error modes rather than
       independent validation." Reports Spearman 0.64 (p<0.001) and 0.71 (p<0.01) between their
       dependency metric and degradation in judge precision. Directly supports the invalidation of
       concordance as evidence.
    3. Kish, L. — design effect and effective sample size. [established-work] The formal apparatus for
       converting n correlated observations into a smaller effective n is standard survey-sampling
       theory; C2A2's "nine models supply ~2 independent votes" framing is an application of it, not a
       novel construct.

  Strength of support: Strong

  Summary: The assumption's substantive claim — that agreement among frontier LLMs is not evidence of
  independent corroboration, and that this specifically invalidates concordance-weighted confidence — is
  directly and recently supported by two peer-reviewed-or-preprint studies at scale. Kim et al. (ICML
  2025, 350+ models) establishes both non-independence and the counterintuitive direction of the
  capability relationship: more capable models are MORE correlated, even across architectures and
  providers. Kuai et al. (2026, 18 models / 6 families) names LLM-as-judge and ensemble verification as
  the specific systems whose independence assumption fails, and quantifies the link between entanglement
  and degraded judge precision. The reflexive reading in the assumption — that this applies to the
  15a/15b concordance itself — follows validly from these findings, since 15a and 15b are model-generated
  judgements over the same items. I did not locate the specific "Kohli 2026" citation named in the item;
  the claim it carries is nonetheless corroborated by the two sources above.

  Caveats: (1) I could NOT verify a source named "Kohli 2026" with the "nine models from seven families /
  ~2 independent votes" figures. The claim is supported by other literature, but the named citation
  should be treated as unverified until located — this is a live citation-integrity risk on the item as
  written. (2) Kuai et al. also show that de-entangled reweighting recovers up to 4.5% accuracy over
  majority voting, i.e. the finding is a call to *correct* concordance weighting, not necessarily to
  abandon it; "invalidates" may be stronger than the literature warrants. (3) Both studies measure
  correlation on benchmark/verification tasks, not on the long-form architectural-judgement task C2A2
  runs. (4) The reflexivity noted by 14a is real and this search does not resolve it: 15a and 15b
  agreement about ASSUMPTION-1150 is itself subject to the finding. Search scope: comprehensive on the
  core question; not extended to ensemble-diversity/decorrelation remedies beyond the reweighting result.

  Recommendation: SUPPORTED
