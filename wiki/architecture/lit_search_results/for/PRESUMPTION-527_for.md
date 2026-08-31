SEARCH-FOR-PRESUMPTION-527:
  Date searched: 2026-08-29
  Original item: PRESUMPTION-527
  Original statement: [inferred] Leaving Phase-6 artifacts on disk 'for the Mac to pick up' presumes an attended Mac session that has not occurred in 17 days and whose login is currently broken.
  Generalizable limb searched: Is uncommitted work held pending a deferred integration event a documented accumulation risk?

  SCOPE NOTE (load-bearing, applies to every item in this run):
    This item was triaged on 2026-07-25 as INTERNAL-EMPIRICAL and declared out of 15a/15b scope.
    That triage is here treated as HALF RIGHT. Each item has TWO limbs: (1) an internal-empirical
    claim about this repository's own file state, which literature cannot adjudicate and which is
    NOT-SEARCHED here; and (2) a generalizable question, named by the item's own "Search targets"
    line, which is squarely searchable. Only limb (2) was searched. The item is NOT retagged
    [MISROUTED-INTERNAL-EMPIRICAL]; REVISE-408's authorisation request to Tom stands untouched.
    Searching limb (2) does not pre-empt it.

  INDEPENDENCE CAVEAT (per PREMISE-096 and the standing 15a/15b correlation discount):
    15a and 15b were executed by the same process in this run, a stronger coupling than the
    read-channel coupling the standing discount was written for. Agreement between the two
    directions in this run therefore carries LESS evidential weight than usual, not more, and
    is discounted accordingly in every 15c disposition below.
  EVIDENCE GRADE: snippet-level search results only. Zero full-text reads, zero abstract-level reads.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-527
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: surfaced from the 'Mac will pick it up' deferral against the 17-day gap
      15a: Searched for supporting literature on the generalizable limb only (2026-08-29); internal-empirical limb NOT-SEARCHED
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. USPTO 7,480,896. "Lightweight methods for storing work in progress in a source code control system." — motivates the invention on the ground that developers want the VCS to back up work in progress precisely because system failure can lose changes held in a private workspace. Holding work outside the committed store is treated as a loss exposure by construction.
    2. Tutorialspoint / DBMS recovery literature, "NO-UNDO REDO Recovery Based on Deferred Update." — under deferred update, changes live only in the log and cache until the transaction REACHES ITS COMMIT POINT. The whole guarantee is conditional on the commit point arriving; a deferral whose commit event never fires is outside the model's assumptions.
    3. SAFe Principle #6, "Visualize and limit WIP, reduce batch sizes, and manage queue lengths." — small batches move through the system faster and with less variability; large accumulated batches raise per-transaction risk and slow defect detection.

  Strength of support: Moderate

  Summary: The risk the presumption glosses over is real and standard. Every framework found treats uncommitted work as exposed until an integration event occurs, and treats the arrival of that event as an assumption rather than a certainty. The 17-day gap with a broken login is the case where the assumption plainly fails. Support is for the risk's existence and for batch-size discipline as the remedy, both of which C2A2 has already validated in a neighbouring premise on draining ingest backlogs in small scoped batches.

  Caveats: One patent, one textbook DBMS analogy, one methodology framework — none is primary research on this exact situation, and the DBMS transfer is loose (a transaction's commit point is machine-scheduled; an attended session is not). Support does not extend to the item's implicit further claim that the attended session is the BINDING constraint; see 15b.

  Recommendation: SUPPORTED
