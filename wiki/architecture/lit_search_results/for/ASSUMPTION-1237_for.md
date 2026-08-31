SEARCH-FOR-ASSUMPTION-1237:
  Date searched: 2026-08-31
  Original item: ASSUMPTION-1237
  Original statement: Reproducing five top-hub counts licenses treating week-over-week deltas as
    real.
  Generalizable limb searched: Does agreement between a method and known values on a small stable
    control subset license inference about a changed or novel part of the population?

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: snippet-level search results only; 3 queries run; no full-text reads. Sources are
    a mix of laboratory-methods guidance and general statistics/reproducibility material; none
    addresses the graph-metrics case directly.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-1237
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced from the run's justification for treating week-over-week deltas as signal
      15a: Searched for supporting literature (2026-08-31)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Microbiologics, n.d. "Importance of Testing a Positive Control When Performing a Diagnostic
       Assay." Industry technical blog. — States the licensing logic the assumption relies on: a
       positive control confirms the test as performed can detect the analyte, and if control
       readings are incorrect "all of the sample readings taken for that test type are called into
       question." This is the standard-practice basis for the assumption's structure.
    2. Rockland Immunochemicals, n.d. "Positive and Negative Controls." Technical resource. —
       A positive control is a sample treated in a way known to produce a positive result,
       confirming the experiment is capable of producing results under the experimental conditions.
       Supports the design pattern generically.
    3. "Practical computational reproducibility in the life sciences," bioRxiv 10.1101/200683. —
       Directly relevant caution, and the most important source here: successful reproduction
       confirms a workflow is reproducible, but "controlling the environment and archiving data and
       processing operations ensures that results are reproducible, but not that they are correct.
       A computational pipeline can be considered as correct only if it performs the operations
       that it claims it should." This licenses less than the assumption asks for.
    4. Neuroimaging reproducibility review, 2018. "Computational and informatics advances for
       reproducible data analysis in neuroimaging." arXiv:1809.10024. — Snippet: statistical
       assumptions of data-processing pipelines must be checked empirically and validated "in
       multiple ways on multiple datasets." Five stable hubs is one way on one subset.
    5. Statistical Thinking (Peck, ed.), bookdown, UM STAT 216. "Generalization and external
       validity." — Standard treatment: generalisation from a sample to a population is warranted
       only where the sample is representative and free of systematic sampling bias.
    6. "Assessing the representativeness of large medical data using population stability index."
       PMC11844046. — Representativeness of a subset relative to a population is an assessable,
       quantifiable property, not something to be assumed. Suggests a concrete strengthening move.

  Strength of support: Moderate

  Summary: The *form* of the argument is standard and defensible. Positive-control design is
    established practice across laboratory and computational work, and the underlying logic — if the
    instrument reproduces known values it is probably operating correctly, and if it fails on them
    every reading is suspect — is exactly what the assumption invokes. To that extent the assumption
    sits on solid ground and the run was right to run the check. But the searches also turned up the
    limit of what such a control licenses, and it is narrower than the assumption claims. The
    reproducibility literature is explicit that reproduction demonstrates the pipeline is
    *reproducible*, not that it is *correct*, and the generalisability literature makes warrant for
    extending a subset result to a population contingent on the subset being representative of it.
    The specific configuration here is unfavourable on that second point: the controls are the five
    largest and most stable hubs while all of the growth is in new machine-generated trees, so the
    control set is drawn from the part of the population that is by construction least like the part
    the inference is about. Sensitivity is the concern — a pipeline can reproduce counts on large
    stable hubs while mishandling a structurally different new subpopulation, and this control cannot
    detect that.

  Caveats: (a) The controls are maximally unrepresentative of the changed population along the exact
    dimension (size, stability, provenance) that matters. Standard positive-control practice assumes
    the control is processed identically to and is comparable with the unknowns; that condition is
    not met here. (b) n=5 supports a determinacy check but not a quantitative claim about error
    rates. (c) A positive control bounds *systematic pipeline failure*, not measurement noise, so it
    says nothing about whether an observed delta exceeds week-to-week variation — a separate
    question the assumption appears to fold in. (d) None of the sources found addresses graph or
    corpus metrics; transfer from assay validation is by analogy. (e) Constructive strengthening
    implied by the sources, in rough order of cost: add controls sampled from the new
    machine-generated trees rather than only from stable hubs; validate on more than one subset
    (per arXiv:1809.10024); and quantify subset-to-population representativeness rather than
    assuming it (per PMC11844046). (f) Note the relationship to ASSUMPTION-1236: 1237 depends on
    exact reproduction being evidentially valuable, which 1236 calls clutter. Both survive only if
    the *fact* of reproduction is separated from the *retained artifact* of reproduction — see the
    1236 file. This search supports that separation rather than either item outright.

  Recommendation: PARTIALLY-SUPPORTED
