SEARCH-FOR-PRESUMPTION-557:
  Date searched: 2026-07-28
  Original item: PRESUMPTION-557
  Original statement: [inferred] The review-page defect is treated as local (wrong pid array) when the same generator has failed in three different signatures on three dates; a submission mapping constructed independently of the render pass is a structural defect class, not a bug.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-557
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: surfaced from a three-incident defect history treated as three bugs rather than one class
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Ostrand, T.J., Weyuker, E.J., & Bell, R.M. (2005). "Predicting the Location and Number of Faults in Large Software Systems." IEEE Transactions on Software Engineering 31(4). — Across 17 quarterly releases of one industrial system and 9 releases of another, the 20% of files with the highest predicted fault counts contained 71-92% of actually detected faults (mean 83%), with prior fault and modification history as the dominant predictors. Empirically: a component that has already produced faults is the most likely site of the next fault, which is direct support for reading a three-incident history in one generator as a property of that component rather than three independent events.
    2. Chillarege, R., Bhandari, I.S., Chaar, J.K., Halliday, M.J., Moebus, D.S., Ray, B.K., & Wong, M.-Y. (1992). "Orthogonal Defect Classification - A Concept for In-Process Measurements." IEEE Transactions on Software Engineering 18(11):943-956. — ODC's whole premise is that the defect stream carries semantic information (defect type + trigger) that measures the *process*, not just the artifact; recurring defect types at a stage are read as a signal about that stage's adequacy. This is the established methodology for converting "three bugs" into "one defect class," and it treats such classification as the normal analytic move, not an overreach.
    3. Leveson, N.G. (2004). "A New Accident Model for Engineering Safer Systems." Safety Science 42(4):237-270. — Argues that in systems whose components are individually working-as-written, losses arise from inadequate enforcement of constraints in the control structure rather than from component failure, and that repeated events with differing surface signatures are the diagnostic signature of a control-structure inadequacy. Supports the specific inference that three different visible failures of one generator point above the individual code sites.
    4. Hunt, A. & Thomas, D. (1999). The Pragmatic Programmer, Addison-Wesley (DRY principle); and the "single source of truth" design principle in information-systems practice. — DRY states that every piece of knowledge must have a single, unambiguous, authoritative representation within a system, and identifies duplicated representations of the same knowledge as the standing cause of divergence defects. A submission-time pid mapping constructed independently of the render pass is exactly a second authoritative representation of "which cards exist," so the DRY/SSoT literature both names this as a defect class and prescribes derivation-from-one-source as the remedy.

  Strength of support: Strong

  Summary: Supported, and the support is EXTERNALLY ANCHORED (named referents outside the pipeline: Ostrand/Weyuker/Bell 2005 in IEEE TSE, Chillarege et al. 1992 in IEEE TSE, Leveson 2004 in Safety Science, and the DRY/single-source-of-truth principle). Three independent literatures converge: fault-history research shows prior faults in a component are the strongest available predictor of the next fault there, so a three-incident record is evidence about the component rather than a coincidence; defect-classification methodology (ODC) treats recurring defect types as measurements of the producing process; and systems-safety theory holds that repeated losses with differing surface signatures indicate an inadequate control structure rather than three component failures. On the specific mechanism, the DRY/SSoT principle names duplicated authoritative representations of the same state as a recognised defect class and prescribes deriving the second representation from the first — precisely the "pid list derived from the rendered card set" remedy the in-house adjunct proposes to test.

  Caveats: (a) The fault-prediction literature is statistical over large file populations; it licenses "this component is high-risk" but not "these three specific incidents share one cause" — that requires the in-house code inspection, and the literature only makes the structural reading the *better-supported prior*, not a finding. (b) ODC classification is conventionally performed on a defect population large enough to see distributions; n=3 is thin. (c) DRY/SSoT is engineering doctrine with strong practitioner consensus but limited controlled empirical validation; it is normative rather than experimental support. (d) None of the sources rules out that the three failures genuinely had unrelated causes in one frequently-edited file; a file under heavy churn produces multiple unrelated faults, and churn is itself a known fault predictor. Preliminary-to-moderate search scope: three targeted searches plus two verification searches; the software-engineering defect-classification literature is large and a fuller sweep could sharpen (b).

  Recommendation: SUPPORTED
