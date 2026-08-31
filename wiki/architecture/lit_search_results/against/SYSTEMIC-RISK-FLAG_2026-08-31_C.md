SYSTEMIC-RISK-FLAG_2026-08-31_C

  Date: 2026-08-31
  Filed by: Agent 15b (Literature Search AGAINST), 7-item assignment
  Cohort: 2026-08-30 intake by Agents 14a/14b
  Affected items: ASSUMPTION-1233, ASSUMPTION-1234, PRESUMPTION-893
  Scope note: This flag covers only the seven items in this 15b assignment. A separate 15b context
    filed SYSTEMIC-RISK-FLAG_2026-08-31_A this cycle over a different item set; this assignment also
    filed flag B covering 894/895/896/903. All are valid and none supersedes the others.

  COMMON VULNERABILITY:
    Remedy declared complete at design time, never exercised. All three items concern the same
    incident response — protecting against a destructive write — and all three assert sufficiency on
    the strength of the remedy's *design* rather than any demonstration that it works. The three
    unverified claims compose into a single unverified recovery path:

      1233 — the snapshot exists, therefore rollback is available.   (reachability, unverified)
      1234 — the rename idiom is atomic, therefore both failure halves are closed.  (completeness,
             overstated)
      893  — one snapshot per run, therefore the loss window is acceptable.  (recency, undeclared)

    Reachability, completeness, and recency are the three properties a recovery control needs. C2A2
    currently has an assertion for each and a measurement for none.

  WHY THIS IS SYSTEMIC RATHER THAN THREE SEPARATE FINDINGS:
    1. They are the same control, not three controls. A rollback capability is only as good as its
       weakest property. A snapshot that is recent (893) and taken via an atomic write (1234) is
       still worthless if the restore path has never been exercised (1233); a restorable, recent
       snapshot is still insufficient if the write that produced it degraded to non-atomic copy
       across a filesystem boundary (1234). Assessing these separately makes the control look
       three-times-defended when it is in fact one path with three untested links in series.
    2. Shared failure trigger and shared discovery moment. All three failure modes are latent under
       normal operation and surface only at the moment of an actual restore — which is the one
       moment at which the original state is already gone. There is no operating condition short of
       a real incident that would reveal any of them. This is the same structural property flagged
       in B (silence is indistinguishable from health), reached by a different route.
    3. Each unverified claim licenses the next. Because 1233 asserts rollback is available, the
       coarseness of 893's interval feels tolerable; because 1234 asserts the write is atomic, the
       integrity of the snapshot in 1233 feels assured. The three assertions mutually reduce the
       felt need to test any of them. This is a confidence structure, not an evidence structure.
    4. The gap is measurable and cheap to close, which raises rather than lowers the significance
       of leaving it open. Unlike the epistemic problems in flag B, every claim here is settleable
       by a short deterministic test (see recommendations). The persistence of an untested recovery
       control that could be tested in minutes is itself a finding about the pipeline's disposition
       toward verification.

  LITERATURE BASIS:
    - Pillai, Chidambaram, Alagappan, Al-Kiswany, Arpaci-Dusseau & Arpaci-Dusseau, 2014. "All File
      Systems Are Not Created Equal: On the Complexity of Crafting Crash-Consistent Applications."
      OSDI '14, USENIX. — 60 crash vulnerabilities across eleven mature systems; 27 from out-of-order
      persistence; the data-before-rename heuristic fixes only 3 of them. Directly limits 1234's
      completeness claim.
    - Mohan, Martinez, Ponnapalli, Raju & Chidambaram, 2018. "Finding Crash-Consistency Bugs with
      Bounded Black-Box Crash Testing." arXiv:1810.02904 / OSDI '18. — Broken rename atomicity found
      in shipped btrfs, including files appearing in both source and destination. Rename atomicity
      is an implementation property, not a guarantee (1234).
    - Enterprise Storage Forum, "Silent Data Corruption, the Backup Killer," citing a NetApp study
      of ~1.5M production disks finding >400,000 silent corruptions (~13% of data studied). —
      Corruption propagates into backups and surfaces only at restore. Limits 1233.
    - Computer Weekly, "Storage 101: Crash-consistent vs application-consistent snapshots." —
      Crash-consistent snapshots shift recovery risk from backup time to restore time rather than
      eliminating it; rebuild "not always" possible. Limits 1233.
    - Veeam, 2026, "Data Trust and Resilience Report" (press coverage). — 90% of security leaders
      believe they can recover quickly; 28% fully restore after an attack. Vendor source,
      directional only, but the confidence-versus-proof gap is the exact shape of this cluster.
    - Commvault, US Patent 10,754,729 and family, background section. — Ad hoc operator-chosen
      backup schedules "in many cases fail to meet the RPO, resulting in unacceptable amounts of
      lost data"; introduces Actual Recovery Point as the measured counterpart to the declared RPO.
      With no declared RPO, drift is unmeasurable (893).
    - Druva, "Recovery Point Objective (RPO)" explainer. — Backup frequency must be derived from the
      RPO, not the reverse. Inverts the reasoning structure of 893.

    Evidence grade caveat: all sources seen at snippet level; no full texts read. The 893 prevalence
    limb is under-searched — I could not find a survey quantifying how many organisations operate
    without a documented RPO, so I make no claim about whether C2A2 is typical.

  RISK LEVEL: High
    Rationale: Lower than flag B because the underlying remedies are the *right* remedies —
    snapshotting and atomic rename are correct choices, and the challenges are about overstated
    sufficiency rather than misdirected design. Also lower because the failure requires an actual
    destructive incident to bite, whereas B's failures accumulate continuously. High rather than
    Medium because the control is the last line of defence for register data, because all three
    links fail in the same direction (silently, at restore time), and because the interaction with
    flag B is severe: if damage is not detected (895) then the snapshot is not taken as a response,
    and by the time it is wanted the retention window may have passed.

  RECOMMENDATION:
    1. Run one restore drill. Snapshot, deliberately corrupt the live artefact, restore, verify
       byte-equality, record elapsed time. This single exercise converts 1233 from assertion to
       demonstration and simultaneously yields the RTO figure that 893 lacks. It is the highest
       value-per-minute action in this cluster.
    2. Check st_dev at runtime. Compare the device of the temp path against the device of the target
       path and log any mismatch. If they differ, rename() is cross-filesystem and 1234's atomicity
       claim is already void in production, independent of any crash-model argument. This is a
       few lines of code and settles the most likely real-world residue.
    3. Constrain the temp file to the target's own directory, and add fsync on the temp file before
       rename plus fsync on the containing directory after. This closes the durability residue
       Pillai et al. document and makes recommendation 2 moot by construction.
    4. Declare an RPO, however crude. The value matters less than its existence — without a
       reference value, no run can ever be identified as having exceeded tolerance, and drift is not
       merely unmeasured but unmeasurable. Then record the Actual Recovery Point per run and compare.
    5. Consider moving the snapshot trigger from the run boundary to the destructive write itself.
       For this workload the marginal cost is near zero and it removes 893's variable-interval
       problem entirely — the exposure stops being a function of how long a run happened to be.
    6. Restate the two assumption texts to match the evidence: 1233 as "creates a rollback
       candidate, pending restore verification"; 1234 as "closes the torn-write half outright, and
       the durability half conditional on fsync ordering and same-filesystem rename."

  NOTE FOR 15c:
    The steelmen here are genuinely strong and should not be discounted. For 1234, if the failure
    class in the originating incident was process-level interruption rather than machine crash, then
    rename is completely atomic against it and the OSDI literature is a category error — the
    completeness claim may be correct for the actual threat model. For 1233 and 893, the register
    may be re-derivable from retained inputs, in which case a coarse recovery point costs bounded
    rework rather than permanent loss. Both steelmen turn on facts about C2A2 that I could not
    establish from literature and that the pipeline can establish directly: what failure model the
    original incident belonged to, and whether run output is reproducible. I recommend 15c resolve
    those two questions before weighting this flag, and note that recommendations 1 and 2 are worth
    doing regardless of how they resolve, since both are cheap and both produce measurements the
    system currently lacks entirely.
