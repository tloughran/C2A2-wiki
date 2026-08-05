SEARCH-AGAINST-PRESUMPTION-654:
  Date searched: 2026-08-04
  Original item: PRESUMPTION-654
  Original statement: That a trap's catches occur upstream of consequence — whereas the
    seventh instance was caught only after the false conclusion had already entered a
    persistent memory and a pending batch.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-654
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-08-03 seventh trap instance, detected after the false
        conclusion had already reached persistent memory and a pending batch
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Dillon, R.L. & Tinsley, C.H., 2008. "How Near-Misses Influence Decision Making
       Under Risk: A Missed Opportunity for Learning." Management Science, 54(8). —
       Central finding: organisations and individuals code near-misses as successes,
       which lowers perceived risk and increases subsequent risk-taking. A trap that
       "caught it again" is therefore systematically read as reassurance, which is
       exactly the reading PRESUMPTION-654 encodes.
    2. Institute of Medicine, 2004. "Patient Safety: Achieving a New Standard for Care,"
       Chapter 7: Near-Miss Analysis. National Academies Press. — Establishes that the
       difference between a near miss and an adverse event is frequently the presence or
       absence of a latent condition rather than the effectiveness of the barrier; the
       same error yields either outcome depending on conditions the barrier does not
       control.
    3. "Near-Miss Analysis," NCBI Bookshelf NBK216107. — Sets out the recovery taxonomy
       as detection, diagnosis, correction, each with distinct enablers, and treats
       failed-recovery cases as a separate class requiring separate analysis. This is the
       formal basis for distinguishing pre-consequence detection from post-consumption
       recovery — a distinction the presumption collapses.
    4. Huang, P. et al., 2017. "Gray Failure: The Achilles' Heel of Cloud-Scale Systems."
       HotOS '17. — Differential observability: detection lags the application's exposure
       to the fault, so the interval between fault and detection is where propagation
       occurs. Detection is not simultaneous with containment.
    5. Hsiao, T.-K. & Schneider, J., 2021. "Continued use of retracted papers: Temporal
       trends in citations and (lack of) awareness of retractions shown in citation
       contexts in biomedicine." Quantitative Science Studies, 2(4), 1144. — Empirical
       measure of how poorly post-consumption withdrawal propagates: only 5.4% of
       post-retraction citation contexts acknowledged the retraction. Once a conclusion
       has been consumed, correcting the source does not correct the consumers.

  Strength of challenge: Strong

  Summary: The safety literature draws precisely the distinction the presumption erases.
    A near miss is not evidence that a barrier works; it is evidence that an error
    reached the barrier, and whether it produced harm often turned on latent conditions
    rather than on the barrier. Dillon and Tinsley then show the psychological hazard:
    repeated catches lower perceived risk and increase subsequent risk-taking, so seven
    catches produce more confidence than one, in the wrong direction. The recovery
    taxonomy makes the operational point — detection, diagnosis and correction are
    separate phases with separate failure modes, and a catch that occurs after the
    conclusion has entered persistent memory and a pending batch has already failed the
    detection phase's timing requirement. The retraction literature quantifies the cost
    of that timing failure: post-consumption withdrawal propagates to under six percent
    of consumers. On this evidence the seventh instance should be classified not as a
    successful catch but as a recovery event with incomplete propagation.

  Specific risks: If catches routinely occur downstream of consumption, then the trap's
    firing count is not a measure of harm prevented. Every instance leaves residue: an
    entry in persistent memory that other agents will read as fact, and a batch item that
    may already have been acted upon. Correcting the origin does not correct the copies,
    and C2A2 has no mechanism (see PRESUMPTION-655) for enumerating where a withdrawn
    conclusion propagated. Worse, the accumulating catch count actively reduces urgency:
    each catch reads as the trap working, so the underlying generator of the false
    conclusion is never eliminated, and the seven instances become a stable operating
    condition rather than an escalating alarm. The failure mode is a slow accumulation of
    retracted-but-still-cited claims inside the wiki's own memory.

  Mitigations available: (1) Record, for every trap firing, the detection point relative
    to consumption — pre-write, post-write-pre-read, post-read. Firing count without this
    field is uninterpretable. Any instance in the third category should escalate, not
    reassure. (2) On a catch, run propagation search: grep persistent memory and pending
    batches for the false conclusion and its paraphrases, and annotate every occurrence in
    place rather than only correcting the source. (3) Move the trap upstream — place it at
    the write boundary into persistent memory, so that detection and containment coincide
    by construction. (4) Treat repeat count as a severity multiplier rather than a comfort
    signal; wire an explicit rule that the Nth instance of the same trap escalates its
    priority rather than confirming the trap's adequacy. (5) Give false conclusions a
    tombstone: a persistent record that this claim was withdrawn, so a later reader
    encountering a surviving copy has a way to discover it.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-654
    Strongest counterargument: A catch after entry into persistent memory but before any
      irreversible external action is still a catch — persistent memory is internal, the
      pending batch was pending rather than executed, and the trap therefore did prevent
      the consequence in the sense that matters. The near-miss literature is written about
      domains where consequence is physical and irreversible; in a text-based wiki the
      consequences are editable, so the recoverability assumption the presumption relies on
      is actually well founded. Seven catches with zero realised harms is genuine evidence
      of an effective barrier, and reclassifying successes as failures on theoretical
      grounds would degrade the system's ability to distinguish real incidents from
      controlled ones.
    What would need to be true for C2A2 to be safe: (a) Every consumer of the persistent
      memory and pending batch between write and catch is identifiable and reachable.
      (b) Correction genuinely propagates — i.e. the annotation practice exists and is
      verified, not assumed. (c) No irreversible act (an external send, a published
      artifact, a downstream memory in another agent) occurred in the window. (d) The trap's
      detection latency is bounded and measured, not incidental.
    How to test: For the seventh instance specifically, search persistent memory and the
      pending batch for surviving traces of the withdrawn conclusion today. Any surviving
      uncorrected copy is a direct falsification. More generally, add a detection-latency
      field to the trap and review after the next three firings; if latency is nonzero and
      unbounded, the presumption is empirically false in this system, independent of the
      literature.

  Search scope: Adequate. Concepts searched: near-miss taxonomies and recovery phases;
    near-miss bias and outcome-based learning failure; latent conditions determining
    outcome; error propagation and detection latency; retraction propagation as a proxy
    for post-consumption correction.
