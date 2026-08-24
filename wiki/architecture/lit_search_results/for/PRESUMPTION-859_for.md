SEARCH-FOR-PRESUMPTION-859:
  Date searched: 2026-08-24
  Original item: PRESUMPTION-859
  Original statement: That agreement between two runs inside one estate constitutes independent
    corroboration and therefore licenses an increase in confidence. Three same-day instances. The channel
    of correlation here is a shared corpus and a shared parser rather than a shared model — the two runs
    are downstream of the same input pipeline.

  Reading used for this search: the FOR direction is read as support for 14b's diagnosis — that
  agreement between two measurements confers a confirmatory boost only under a conditional-independence
  premise, that the premise fails silently when the measurements share an upstream channel, and that this
  failure has been named, quantified and made into mandatory design practice in more than one discipline.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-859
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by observing that a confidence increase was recorded on the strength of two runs
        agreeing, with no clause asking what the two runs shared upstream of the point at which they
        agreed.
      15a: Searched for supporting literature (2026-08-24)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Hurlbert, S. H. (1984). "Pseudoreplication and the Design of Ecological Field Experiments."
       *Ecological Monographs* 54(2), 187–211. — The canonical statement of the error in its
       experimental-design form: statistical inference applied where "treatments were not replicated or
       the replicates were not independent." Hurlbert's survey of 176 ecological studies found 27%
       pseudoreplicated overall and 48% among those using inferential statistics — i.e. the error is not
       exotic, it is the modal error among competent practitioners. Directly supports 14b's structural
       point: two observations drawn through one shared upstream channel are one replicate presented as
       two.
    2. Knight, J. C. & Leveson, N. G. (1986). "An Experimental Evaluation of the Assumption of
       Independence in Multiversion Programming." *IEEE Transactions on Software Engineering* SE-12(1),
       96–109. — The strongest single source, and the closest structural analogue. Twenty-seven versions
       of a program were written independently from *the same specification* at two universities and
       subjected to a million tests. The versions were individually very reliable, but the number of
       tests in which more than one failed was substantially greater than independence predicts. The
       shared artefact was the specification — the exact position occupied in 14b's item by the shared
       corpus and parser. Knight and Leveson's finding is that independence of *process* does not deliver
       independence of *error* when the input is common.
    3. Eckhardt, D. E. & Lee, L. D. (1985). "A Theoretical Basis for the Analysis of Multiversion
       Software Subject to Coincident Errors." *IEEE TSE* SE-11(12). [established-work, cited as the
       theoretical companion to Knight & Leveson within the multiversion-failure literature retrieved] —
       Supplies the model: coincident failure is expected whenever difficulty varies across the input
       space, because all versions face the same hard inputs.
    4. Common-cause failure (CCF) modelling in probabilistic risk assessment: U.S. NRC, "Common-Cause
       Failure Analysis in Event Assessment" (NUREG/ML081720219); the beta-factor, alpha-factor and MGL
       parametric models. — The engineering discipline that exists because redundancy without
       independence is not redundancy. The literature retrieved reports that CCF events may contribute
       between 20% and 80% of the unavailability of nuclear safety systems — that is, in the paradigm
       case of designed-in redundancy, the correlated-failure term dominates the independent-failure
       term. Regulators require CCF to be modelled explicitly with a fitted coupling parameter; they do
       not permit an independence default.
    5. Podsakoff, P. M., MacKenzie, S. B., Lee, J.-Y. & Podsakoff, N. P. (2003). "Common Method Biases in
       Behavioral Research: A Critical Review of the Literature and Recommended Remedies." *Journal of
       Applied Psychology* 88(5), 879–903. — The measurement-science form of the same point, and the one
       nearest to a shared *parser*. Method effects — shared instrument, shared rater, shared source —
       inflate observed correlations, and the multitrait-multimethod syntheses summarised put method
       variance at roughly 20–30% of variance in behavioural outcomes. The recommended remedies are all
       structural: separate the sources, do not de-bias afterwards.
    6. Bovens, L. & Hartmann, S. (2003). *Bayesian Epistemology*. Oxford University Press. — Supplies the
       formal condition under which agreement licenses a confidence increase at all: witness reports must
       be probabilistically independent *conditional on the truth of what they report*. Bovens and
       Hartmann's framework makes explicit that coherence among reports is "maximally effective if the
       witnesses are independent," and that the confirmatory work is done by the independence premise,
       not by the agreement. Where the premise fails, agreement is evidence about the shared channel and
       not about the hypothesis.
    7. Bovens, L. & Hartmann, S. (2017/2019 discussion). "The Variety-of-Evidence Thesis: A Bayesian
       Exploration of Its Surprising Failures." *Synthese*. (Claveau & Grenier; see philsci-archive
       14086.) — Strengthens the condition considerably: the thesis that varied evidence confirms more
       strongly than narrow evidence "fails to be generally true," fails in more circumstances than
       previously expected, and can fail whatever the chance that the sources are unreliable. Supports
       14b's implicit warning that "two agreeing runs" is not merely a weaker case of corroboration but
       can, under specifiable conditions, be no case at all.

  Strength of support: Strong

  Summary: Four disciplines have independently named this error and made avoiding it a design
  requirement, which is about as strong a form of support as a search of this kind can return.
  Epistemology supplies the licensing condition: on the Bovens–Hartmann treatment, agreement between two
  reports raises confidence only under conditional independence given the truth of the reported
  proposition, and the variety-of-evidence results show the boost can vanish or reverse when that premise
  is disturbed. Experimental design supplies the diagnosis of the specific defect — Hurlbert's
  pseudoreplication, where non-independent replicates are counted as replicates, present in nearly half
  of the inferential studies he surveyed. Software fault tolerance supplies the closest structural
  analogue: Knight and Leveson's twenty-seven independently written versions failed together far more
  often than independence predicts, and the thing they shared was the specification — occupying exactly
  the position that the shared corpus and parser occupy in C2A2's two runs. Reliability engineering
  supplies the quantitative scale, with common-cause failure contributing a reported 20–80% of safety
  system unavailability, and the regulatory response of requiring an explicit coupling parameter rather
  than an independence default. Measurement science supplies the closest match to a shared *parser*:
  common-method variance from a shared instrument inflates correlations by an estimated 20–30% of
  variance, and the remedies are structural separation of sources, not post-hoc adjustment. The
  convergence of these five on one rule — that agreement is informative only to the extent that the
  channel is not shared, and that the burden is on the claimant to show the channel is not shared — is
  what makes this Strong rather than Moderate.

  Caveats: Every source establishes that shared-channel agreement *can* be uninformative; none
  establishes that the particular C2A2 instances were uninformative, and none gives a way to size the
  effect without a model of the coupling. Domain-transfer is uneven. Knight–Leveson is the best analogue
  but concerns deterministic programs with a defined oracle; two agent runs over a corpus have no oracle,
  so the "coincident failure" notion has to be reconstructed rather than imported. The CCF numbers are
  from nuclear I&C and should not be read as a prior for a text pipeline. Podsakoff et al. concerns human
  raters and self-report instruments; the parser analogy is apt in structure but the 20–30% figure does
  not transfer. Bovens and Hartmann is a formal framework, not an empirical finding, and the
  variety-of-evidence result (source 7) is a negative existence proof about the general thesis rather
  than a claim about typical cases. One asymmetry worth recording for reconciliation: this item is
  *distinct* from PRESUMPTION-717 in that the correlation runs through corpus and parser rather than
  through a shared model; the multiversion and common-method literatures speak to the shared-input
  channel well, but I found nothing that separately quantifies input-channel coupling against
  model-family coupling, which is where the two items would be told apart. Sources 3 and 4 are cited from
  the retrieved secondary literature; no page-level claims asserted. Search scope: good — covered
  experimental design, multiversion software, PRA common-cause modelling, psychometric method bias, and
  Bayesian confirmation. Did NOT cover meta-analytic dependence (multiple effect sizes from one sample)
  or the ensemble-diversity literature in machine learning, both of which would be additive.

  Recommendation: SUPPORTED
