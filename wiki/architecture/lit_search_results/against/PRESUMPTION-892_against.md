SEARCH-AGAINST-PRESUMPTION-892:
  Date searched: 2026-08-28
  Original item: PRESUMPTION-892
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority Medium)
  Original statement: [inferred] That a limit continues to carry information after repeated disclosed breach;
    and, relatedly, that a repeatedly-exceeded budget is a real constraint rather than a mislabelled metric.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-892
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a 28-for-28 breach record nobody treats as evidence about the threshold; checked
        against ASSUMPTION-1221/1229 for non-duplication.
      15b: Searched for challenging literature
    Current status: CHALLENGED (against the framing, not against the observation)

  Search scope: WebSearch, 2026-08-28, one dedicated query on critiques and limits of the normalisation-of-
    deviance framework. Reached: a 2026 arXiv paper on decision-trace schemas for governance evidence
    (2604.09296) which contains the hindsight critique; Grokipedia's and Wikipedia's summaries; the Patient
    Safety Learning hub; Pinto (2014) in IJPM. NOT COVERED and material: the second limb — distinguishing a
    mislabelled metric from a real constraint — which the for direction also did not search, so **neither
    direction has searched it.** Declared, not filled. All SNIPPET-ONLY. Confidence: MODERATE on the
    critique, ZERO on limb 2.

  Challenging evidence found: Yes

  Sources:
    1. Anon. (2026), "Decision Trace Schema for Governance Evidence in Real-Time Risk Systems"
       (arXiv:2604.09296) [SNIPPET-ONLY; authors unverified] — Carries the sharpest available critique:
       "post-event analyses deem prior deviations as deviant only because outcome knowledge reframes them as
       foreseeably risky," and investigators "equipped with failure's clarity may overpathologize routine
       practices that succeeded repeatedly under uncertainty." Also notes the reflexive problem — governance
       artifacts are themselves prone to the drift they document.
    2. Grokipedia, "Normalization of deviance" [SNIPPET-ONLY] https://grokipedia.com/page/Normalization_of_deviance —
       Reports that empirical reviews highlight the framework's preliminary status and the need for primary
       data before attributing normalisation, cautioning against generalised use without context-specific
       validation. [Source-quality note: this is an AI-generated encyclopedia and is the weakest citation in
       this file; it is retained because it is the only one reached that summarises the empirical-status
       critique, and it is marked accordingly rather than dropped or dressed up.]
    3. Pinto, J. K. (2014), IJPM, S0263786313000835 [SNIPPET-ONLY] — Applies the framework outside
       safety-critical engineering, which is where the transfer question arises.

  Strength of challenge: Moderate-Strong

  Summary: The observation — 28 consecutive disclosed breaches — is not in dispute; the frame put on it is.
    Normalisation of deviance is a retrospective label with a documented hindsight problem: a practice is
    classified as deviant because we now know what it cost, and practices that succeeded repeatedly under
    uncertainty get pathologised by the same reasoning. Applying the label to a token budget in a text
    pipeline, where no adverse outcome has been demonstrated, is precisely the generalised use the empirical
    critiques caution against. There is a second and more consequential objection, which neither direction
    searched and which is stated here as an open gap rather than as a finding: a 28-for-28 breach record is
    at least as consistent with a wrongly-set limit as with an eroded norm. If the budget was never derived
    from a measurement, then it is a mislabelled metric, and the deviance frame is not merely uncertain but
    inapplicable.

  Specific risks: (a) Adopting the deviance frame licenses a disciplinary response — more disclosure, more
    flags — to what may be a calibration error, and the estate has run that experiment 28 times.
    (b) Rejecting the frame licenses the ratchet ASSUMPTION-1229 wants. Both errors are live and they point
    opposite ways, which is why the derivation question has to be settled first.

  Mitigations available: One query, and it settles the item: find the derivation of the 4,000/30,000 token
    budget. If a derivation exists, the breaches are deviations and the frame applies. If none exists, the
    number is a placeholder, the breach record is evidence about the number, and both this item and
    ASSUMPTION-1229 should be re-framed around setting a limit rather than around defending or excusing one.

  STEELMAN:
    Item: PRESUMPTION-892
    Strongest counterargument: The hindsight critique of Vaughan applies to *external* investigators
      reconstructing a failure they already know occurred. Here the observation is contemporaneous and made
      by the actor itself, before any adverse outcome, which is the one configuration the hindsight objection
      cannot touch. And the mechanism does not require an accident: Vaughan's claim is that repetition
      without catastrophe converts the deviation into the norm, so the *absence* of a bad outcome is the
      mechanism's precondition, not its refutation. Waiting for harm before accepting the frame is exactly
      the error the frame describes.
    What would need to be true for C2A2 to be safe: the limit would have to have a recorded derivation, so
      that a breach is interpretable as a breach of something.
    How to test: grep the estate for the origin of the token budget. Present → deviation. Absent →
      mislabelled metric. Either result closes the item; no further literature is needed.

  Recommendation: CHALLENGED
