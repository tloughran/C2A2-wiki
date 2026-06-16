SEARCH-AGAINST-ASSUMPTION-314:
  Date searched: 2026-06-12
  Original item: ASSUMPTION-314
  Original statement: "Falsifier (b) as positive prediction and master-plan §6 interaction yield are the same measurement (agreed rungs = first countable PRS-milestone yield)."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-314
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated assumption from 2026-06-11 EOD session
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Kelley, K. and Maxwell, S. E., 2003. "Sample Size for Multiple Regression: Obtaining Regression Coefficients that Are Accurate, Not Simply Significant." Psychological Methods 8(3): 305–321. — Establishes foundational concerns about construct identity: two measures can be highly correlated without measuring the same construct, and treating correlated proxies as identical in a measurement model inflates apparent precision. The assumption that "agreed rungs" operationalises both falsifier (b) and PRS-milestone yield simultaneously requires demonstrating construct identity, not merely correlation.

    2. Thorndike, E. L., 1904. "An Introduction to the Theory of Mental and Social Measurements." (Classic source on the jingle-jangle fallacies, formalised by Block 1995.) The jingle fallacy: two constructs with different theoretical roles are mistakenly treated as one because they share an observable. Here, "falsifier-positive-prediction" and "PRS-milestone yield" have different theoretical roles — one is a disconfirmation criterion, the other a progress metric — and using the same observable to serve both creates circularity: the system cannot be falsified by low rung counts if the same counts constitute the progress claim.

    3. Bollen, K. A., 1989. Structural Equations with Latent Variables. Wiley. — Discusses the problem of instrument reuse: when a single observable is used as an indicator for two latent constructs in the same model, parameter estimates become unidentified or biased. The C2A2 system, applied to itself, faces exactly this problem if agreed-rung counts are both the outcome variable (PRS yield) and the falsifier criterion.

    4. Cronbach, L. J. and Meehl, P. E., 1955. "Construct Validity in Psychological Tests." Psychological Bulletin 52(4): 281–302. — The foundational paper on construct validity: a construct must be embedded in a nomological network distinguishing it from co-measured constructs. Using the same observable for two distinct theoretical functions (falsification criterion vs. progress count) collapses the nomological network and makes it impossible to distinguish construct failure from measurement failure.

    5. Lakatos, I., 1978. The Methodology of Scientific Research Programmes. Cambridge University Press. — In the context of research programme evaluation, Lakatos warns that a programme that designates its own main result as the success criterion is degenerative. Assigning "agreed rungs" as both the falsifier and the yield metric has this structure: the system cannot fail on its own terms if the very quantity that defines failure is the same quantity being optimised.

  Strength of challenge: Strong

  Summary: The assumption that the falsifier criterion and the PRS-milestone yield are "the same measurement" conflates two theoretically distinct functions into one observable. The jingle fallacy literature warns precisely against this: treating a single indicator as simultaneously encoding a predictive/falsification criterion and a progress metric creates a non-falsifiable inner loop. The Lakatos critique adds that making the main performance indicator also the falsification criterion is a mark of a degenerating research programme. This is a structural measurement problem, not merely a risk of miscounting: the C2A2 self-assessment architecture may be constitutively unable to detect certain forms of failure. The strength of the challenge is strong because the problem is internal to the measurement architecture and cannot be resolved by collecting more data.

  Specific risks: If agreed-rung count serves as both the progress metric and the falsification criterion, the system is protected from falsification in the very domain where it claims to be most testable. This is a form of immunisation that could allow C2A2 to pass M7–M8 milestones while the underlying research program has in fact stagnated or degenerated.

  Mitigations available: Decompose the single observable into two distinct operationalisations: (a) for falsifier (b), define a threshold rung-count level that, if not achieved, would count as refutation — fixed in advance and held stable; (b) for PRS-milestone yield, use a richer composite measure (e.g., rung count × rung depth × time-to-agreement × percentage of contested rungs resolved substantively rather than via weaker reading). The two operationalisations can correlate with the same underlying phenomenon while being formally distinct and not circularly interdefined.

  STEELMAN:
    Strongest counterargument: If the claim is that agreed rungs operationalise both in the same direction (more rungs = more progress = prediction confirmed), then the conceptual risk of circularity may be lower than it appears — a genuine null result (zero agreed rungs) would still constitute falsification, and a strong positive result would still constitute confirmation, with the metrics running in parallel without contradiction. The concern arises mainly at the margin: what counts as "enough" rungs for milestone certification.
    What would need to be true for C2A2 to be safe: The threshold for falsification (b) must be specified independently of whatever rung count the system actually achieves, and the PRS-milestone yield must include components beyond mere rung count that can diverge from it (so the two measures can in principle disagree, enabling the measurement model to be identified).
    How to test: Pre-register the falsification threshold for M3–M4 rung counts before the measurement period begins, and define the PRS composite in advance with at least one component that does not reduce to rung count. Then check at milestone review whether the two operationalisations give the same verdict. If they always agree by construction, the decomposition has failed.

  Search scope: Searched for jingle-jangle fallacies in psychometrics, double-counting in construct validity, Bollen on measurement model identification, Cronbach-Meehl construct validity, and Lakatos on research programme degeneration. Comprehensive; the specific literature on self-referential measurement in AI system evaluation was not separately searched.

  Recommendation: CHALLENGED
