SEARCH-AGAINST-PRESUMPTION-1053:
  Date searched: 2026-09-21
  Original item: PRESUMPTION-1053
  Original statement: Measurement instruments that are also members of the measured population
    systematically distort their own series, and the estate has not enumerated which of its registers
    are both.

  **Execution note:** 15a and 15b were executed by a single scheduled process on 2026-09-21. Query sets
  were framed separately and the FOR files were written before any AGAINST query was issued, but the
  two-process independence the spec assumes was NOT achieved. Weight the strength ratings accordingly.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-1053
    Item type: PRESUMPTION (unstated -- surfaced by inference)
    Transform at each step:
      14b: Generalised three same-day, independently-reached instrument-contamination findings.
      15b: Searched for cases where self-inclusion is negligible or self-correcting.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. "The Strong, Weak and Benign Goodhart's Law: an independence-free and paradigm-agnostic
       formalisation." arXiv:2505.23445. — The direct challenge to the word "systematically." This work
       formalises Goodhart's law into variants and identifies a *benign* regime in which optimising the
       proxy does not degrade the target. Distortion is therefore conditional, and the conditions are
       specifiable. A blanket claim that self-including instruments *systematically* distort is stronger
       than the current state of the formalism supports.
    2. Bibliometrics critique literature ("Excessive use, ill use and misuse of Bibliometrics,"
       arXiv:2606.03117). — Locates the damage in *evaluative use under incentive*, not in
       self-reference as such. Self-referential measures (citations of citations) are used
       descriptively for decades without the collapse Goodhart describes; the collapse arrives with the
       target, not with the reflexivity.
    3. Goodhart's own framing, as transmitted in the reception literature. — The regularity collapses
       "once pressure is placed upon it for control purposes." Pressure is the operative term. Where no
       agent benefits from moving the number, the mechanism the law describes has no motor.

  Strength of challenge: Moderate

  Summary: The general phenomenon is real; the quantifier is not established. The literature's
    well-documented cases all involve an agent with an incentive to move a metric under evaluative
    pressure. C2A2's registers have no such agent: contamination there would be *mechanical*
    self-inclusion (a run-note entering a corpus its own run counts), which biases a level, is usually
    small, is constant-ish, and is removable by a filter. Calling that the same failure as
    incentive-driven Goodhart collapse overstates it, and overstating it invites an expensive redesign
    where a WHERE clause would do.

  Specific risks: (1) Over-correction: registers rebuilt to exclude self-reference at a cost far above
    the bias removed. (2) Under-correction of the real risk, which this framing obscures — the danger is
    not distortion of a *level* but distortion of a *trend*, if the instrument's own activity rate
    changes over time. A stalled pipeline that stops emitting run-notes would change the self-inclusion
    rate mid-series; that is the version worth measuring, and "systematically distort" does not name it.

  Mitigations available: Enumerate first, quantify second: for each register, compute the share of rows
    originating from the estate's own agents, and plot that share over time. If the share is small and
    flat, the bias is a level effect and a filter fixes it. That enumeration is the second half of
    14b's own claim and is cheap.

  STEELMAN:
    Item: PRESUMPTION-1053
    Strongest counterargument: The presumption is true in the weak form and unestablished in the strong
      form it is stated in. "Systematically distort" imports a mechanism (incentive under evaluative
      pressure) that C2A2's registers do not have, and a recently formalised account of the law
      explicitly carves out a benign regime. Generalising from three same-day findings to all
      self-including registers is the same inferential move the estate is criticising elsewhere in the
      same intake (see ASSUMPTION-1571): small n, no base rate, strong quantifier.
    What would need to be true for C2A2 to be safe: that self-inclusion shares are small and stable over
      time, and that no register is used as a target for any agent's behaviour.
    How to test: the per-register self-inclusion share, plotted over 90 days. Same instrument settles
      both the strong and weak readings.

  Recommendation: PARTIALLY-CHALLENGED
