SEARCH-AGAINST-PRESUMPTION-1076:
  Date searched: 2026-09-23
  Original item: PRESUMPTION-1076
  Original statement: A single positive control cannot discriminate between failure causes
    that share a symptom; differential diagnosis needs a control per candidate cause.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-1076
    Item type: PRESUMPTION (unstated)
    Transform at each step:
      14b: Inferred from two diagnoses resting on one control that does not separate them.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED (first clause corroborated when the control's outcome
      is the same under every candidate cause; second clause, "a control per candidate cause,"
      challenged by the fault-isolation and group-testing literature)

  Challenging evidence found: Partial

  Sources:
    1. de Kleer, J. & Williams, B.C. (1987). "Diagnosing Multiple Faults." Artificial
       Intelligence 32(1): 97–130 (General Diagnostic Engine). Measurements are chosen by
       minimum expected entropy over the candidate set. A single well-chosen probe can split
       many candidates at once, and the number of measurements needed scales with the
       information required (about log of the number of candidates), not with the number of
       candidates. Direct challenge to "a control per candidate cause."
    2. Group-testing literature: Dorfman (1943), as discussed in "Group Testing: An
       Information Theory Perspective" (arXiv:1902.06002) and "Optimal adaptive group testing"
       (arXiv:1911.06647). Pooled or adaptive tests identify s defective items among n using
       about s·log(n) tests, far fewer than n. Each test is shared across many candidates.
       Discrimination comes from the pattern of results across tests, not from a dedicated
       control per cause.
    3. Platt, J.R. (1964). "Strong Inference." Science 146 (republished 1965), with the
       retrospective "Fifty years of J. R. Platt's strong inference," Journal of Experimental
       Biology 217(8). The central step is designing a crucial experiment that excludes one or
       more hypotheses. A single experiment can discriminate among several alternatives if it
       is designed so that they predict different outcomes. This CORROBORATES the first clause:
       a control that all candidates predict the same outcome for (such as a generic positive
       control) is uninformative. It CHALLENGES the second: what is needed is discriminating
       experiments, not one control per cause.

  Strength of challenge: Moderate (against the second clause); None (against the first clause)

  Summary: The first half of the presumption is well supported. If every candidate cause
  predicts the same result for a positive control, that control has zero discriminating power
  between them. This is the core of Platt's argument and of entropy-based measurement
  selection. The second half ("needs a control per candidate cause") is too strong. Model-based
  diagnosis (de Kleer & Williams) and group testing both show that discrimination needs tests
  whose outcomes differ across candidates. Such tests can be shared: one probe can separate
  several causes, and k causes can be separated in about log₂k well-designed tests. Per-cause
  controls are sufficient but not necessary. For two candidate causes the distinction is
  small, since one discriminating test suffices and that equals one test per cause minus one.
  At larger candidate sets it matters a great deal.

  Specific risks: If C2A2 adopts "one control per candidate cause" as policy, diagnostic cost
  grows linearly with the number of hypotheses when logarithmic designs exist. It may also
  build many per-cause controls that each fail to discriminate, when what matters is
  discrimination and not the count of controls.

  Mitigations available: For each diagnostic control, write down the result each candidate
  cause predicts. Keep only controls whose predicted outcomes differ. Choose the next test to
  maximize the expected reduction in uncertainty (the GDE approach). Use splitting or pooled
  tests when candidates are numerous.

  Search scope: Preliminary — 3 searches (de Kleer & Williams GDE; group testing; Platt strong
  inference). Did not search the clinical differential-diagnosis literature on test
  sequencing, which may give further examples of multi-hypothesis single tests.

  Excluded results: Scribd copy of Platt (1964) (unauthorized mirror; the primary citation is
  used instead); academia.edu mirror of the JEB retrospective.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: PRESUMPTION-1076
  Strongest counterargument: Discrimination is a property of a test's predicted-outcome
    profile across hypotheses, not of how many controls there are. One test whose result
    differs under cause A and cause B separates them completely. Five per-cause controls that
    each give the same result under every cause separate nothing. Classic model-based
    diagnosis and group testing formalize this: the number of tests needed grows with the
    logarithm of the candidate count, and tests are shared across candidates. "A control per
    candidate cause" confuses a sufficient heuristic with a necessary condition, and it would
    lead to over-building controls when the real gap is a missing discriminating test.
  What would need to be true for the presumption to hold as stated: The candidate causes are
    so different in mechanism that no shared probe can produce different outcomes for them, so
    each cause can only be tested by its own specific control. This does happen in practice
    (for example, when causes live in unrelated subsystems), but it is not the general case.
  How to test: For the two diagnoses 14b flagged, list what each cause predicts for every
  available probe. If some existing or cheap probe gives different predicted outcomes, one
  test settles it and the "per cause" requirement is unnecessary. If none does, per-cause
  controls are needed in this instance.
