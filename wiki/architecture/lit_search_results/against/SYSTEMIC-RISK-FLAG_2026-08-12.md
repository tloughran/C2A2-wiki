SYSTEMIC-RISK-FLAG:
  Date: 2026-08-12
  Affected items: PRESUMPTION-766, PRESUMPTION-768, PRESUMPTION-770,
    PRESUMPTION-771, PRESUMPTION-773, PRESUMPTION-775
    (secondary: PRESUMPTION-765, PRESUMPTION-769)

  Common vulnerability: The register records failure modes without recording the cost
    and failure modes of the remedy each finding implies, and the literature challenges
    the implied remedy in six of the fourteen items searched today. This is a defect in
    the remediation layer, not in the detection layer, and it has a consistent shape.
    In each case 14b correctly observed a real hazard, and then the natural reading of
    the finding points at the one intervention the relevant literature has already tried
    and warned against.

    Item by item. PRESUMPTION-768 points at architecture-wide negative controls; the
    negative-control methodology literature says a passing control produces false
    confidence when its structural assumptions are unmet, so the remedy reproduces the
    finding one level up. PRESUMPTION-770 points at attestation binding a mark to run
    completion; the distributed-transactions literature since Helland treats that
    direction as an availability anti-pattern and prescribes re-derivability instead —
    and a commit barrier composes badly with the ephemeral-storage exposure in
    PRESUMPTION-776. PRESUMPTION-771 points at coordination stronger than convention;
    optimistic concurrency control is the recommended design at the contention level
    observed, and locks compose into deadlock with the dying writers of
    PRESUMPTION-770. PRESUMPTION-766 points at logging every enacted decision; ADR
    practice is documented as widely adopted and consistently abandoned.
    PRESUMPTION-773 points at global consistency checking; requirements engineering
    settled on tolerate-and-surface-at-use two decades ago, and semantic contradiction
    detection over a thousand natural-language items would fall far outside the ~10%
    false-positive budget below which developers keep trusting a checker.
    PRESUMPTION-775 points at making later readers act; alert-fatigue research says
    raising volume lowers the action rate on the findings that matter.

    The compounding mechanism is the important part. Each implied remedy adds an
    instrument. Every added instrument is, on the day it ships, a check that has never
    failed — which is PRESUMPTION-768 restated. So the remediation programme this batch
    implies is self-amplifying: it generates precisely the class of artefact whose
    unfalsifiability the batch's most severe item identifies as Critical. Six findings
    resolved this way would leave the architecture with six more unfalsified
    instruments and a smaller remediation budget, and the register has no field in which
    that cost is recorded, so nothing in the current process would notice.

    A second and independent vulnerability spans the two 14a items, ASSUMPTION-966 and
    ASSUMPTION-968: both import a quantitative claim across a construct boundary without
    checking that the construct transfers. ASSUMPTION-966's arithmetic holds only under
    an unstated per-item serial review model that no assurance discipline uses.
    ASSUMPTION-968 quotes -70% as a coefficient when the source reports a 39-70% band
    attached to sequential *planning* on one benchmark, classifies a staged pipeline of
    heterogeneous roles as sequential when the source's sequential arm concerns
    splitting one dependent reasoning chain, and omits the same source's finding that
    centralised coordination cuts error amplification from 17.2x to 4.4x — a result that
    supports C2A2's current topology. It also carries an unstable citation: 180
    configurations per the Google Research blog, 260 across six benchmarks per paper
    summaries. Both items would pass any check that verifies a citation exists and fail
    any check that verifies the cited construct matches the local one, and C2A2 has the
    former and not the latter.

  Literature basis:
    - "Negative controls: concepts and caveats." Statistical Methods in Medical
      Research, 2023 (doi:10.1177/09622802231181230). — Negative controls detect bias
      sometimes, never rule it out, and mislead when their structural assumptions fail.
      [authors unverified]
    - "Pitfalls of Using Negative Control Outcomes in Environmental Epidemiology."
      Current Environmental Health Reports, 2025 (doi:10.1007/s40572-025-00513-7). — A
      null control "may give researchers false confidence."
    - Helland, P., 2007. "Life Beyond Distributed Transactions: An Apostate's Opinion."
      CIDR 2007 / CACM (doi:10.1145/3009826). — Distributed atomicity degrades
      availability; idempotence, not attestation, is the discipline.
    - Kung, H.T. & Robinson, J.T., 1981. "On Optimistic Methods for Concurrency
      Control." ACM TODS (doi:10.1145/319566.319567). — Optimistic control is superior
      where conflicts are rare; validation, not prevention, is the requirement.
    - Nuseibeh, B. et al., 2001. "Making inconsistency respectable in software
      development." Journal of Systems and Software. — The problem is undetected
      inconsistency, not inconsistency; tolerance is rational and normal.
    - Sadowski, C. et al., 2015. "Tricorder: Building a Program Analysis Ecosystem."
      ICSE 2015. — Analysers above ~10% false-positive rate are dismissed or disabled;
      placement at the point of change, not urgency, determines action.
    - "Mitigating False Positive Static Analysis Warnings: Progress, Challenges, and
      Opportunities." IEEE TSE, 2023 (doi:10.1109/TSE.2023.3329667). — Alert fatigue as
      the mechanism by which volume suppresses action.
    - "Architecture Decision Records in Practice: An Action Research Study." ECSA 2024.
      — Prioritisation of what to document is the practitioners' real problem.
      [authors unverified]
    - Guo, P.J. et al., 2010. "Characterizing and Predicting Which Bugs Get Fixed."
      ICSE 2010. — Fix probability tracks process factors, not defect validity.
    - "Towards a Science of Scaling Agent Systems." arXiv:2512.08296 (MIT Media Lab /
      Google). — Source of the +80.8/-70.0 figures; also the 17.2x-to-4.4x error
      amplification result favouring centralised coordination.
    - ISA 500, Audit Evidence, IAASB. — Evidence is graded by reliability and
      corroborated, not admitted or excluded; assurance over large populations is
      delivered by sampling with a stated confidence level.

  Risk level: High

  Recommendation: Treat this as two process defects rather than as commentary on eight
    findings, and fix both at the register level.

    First, add a remedy-cost field to every item. Any finding whose implied remedy is a
    new instrument must record (a) what the instrument's own failure mode is, (b) how it
    would be shown capable of failing, and (c) what it costs to maintain. An item that
    cannot populate (b) should not be graded above Moderate, because it is proposing an
    unfalsifiable check. This single field converts the six affected items from
    remediation liabilities into decisions, and it is the cheapest available intervention
    against the self-amplification described above.

    Second, add a construct-transfer check for imported quantitative claims. Any figure
    imported from external literature must record the population it was measured on, the
    range it came from if it came from a range, and one sentence stating why the source
    construct matches the local one. ASSUMPTION-968 fails all three and would have been
    caught by any of them; ASSUMPTION-966 fails the third. Note that this check is
    itself an instrument and must therefore satisfy the first recommendation — the
    negative control for it is a deliberately mis-scoped figure planted in the intake
    queue, which is cheap to arrange.

    Third, and specific to this batch: before any of the six affected items is
    remediated, run the cheap discriminating experiments already written into their
    STEELMAN sections. Four of them are decisive and cost under an hour each — kill a
    run mid-write and observe whether stale marks are trusted (770); reconstruct how the
    two collisions were discovered (771); re-run the four dark cycles' original queries
    verbatim (772); resolve the 191 paths to their filesystem device (776). Three of the
    four also happen to be positive controls in the sense PRESUMPTION-768 says the
    architecture has none of, which is the one place in this batch where a remedy pays
    for itself twice.

    Finally, note the reflexive exposure. PRESUMPTION-777 observes that transcripts
    return no tool outputs, so the counts in these items — four fail-open instruments,
    twelve pass-marks, 191 paths, thirteen dark days, two collisions, three false
    provenance claims, seven recurrences — are unmarked self-reports. Every severity
    grade in this batch rests on one of them, and every one is a count over a store that
    still exists on disk and could be re-derived today. Re-derive the gating figures
    before grading; it is the shortest path from this batch's findings to defensible
    ones.
