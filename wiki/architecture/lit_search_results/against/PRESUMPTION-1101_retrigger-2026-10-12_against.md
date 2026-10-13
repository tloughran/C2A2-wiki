SEARCH-AGAINST-PRESUMPTION-1101 (RE-TRIGGER cycle 1):
  Date searched: 2026-10-12
  Original item: PRESUMPTION-1101
  Original statement: [inferred] Normative: deferring to the designer is the safe default even when the
    designer is absent. (Every run met judgment calls with "the hold is yours"; open items grew; no
    human input 7+ days. Risk if wrong: High — escalations stop being decisions and become a backlog.)
  Under test this cycle (MONITOR-636, High): the refined form — escalation-to-human designs need a
    policy for reviewer absence; otherwise the queue grows without bound. Owed: "peer-reviewed or
    measured evidence on HITL queue behaviour under reviewer absence; or in-house backlog data".
    I searched for challenges: does an unattended queue actually grow without bound; is "reviewer
    present" itself a safe baseline; is an absence policy the right control variable.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read lit_search_results/for/ or 15a sections of
    lit_search_returns.md. I read my own cycle-0 file to avoid repeating its blog sources. No fetch was
    refused as "already fetched".

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 1)]
    Original item: PRESUMPTION-1101
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b (2026-09-30): Inferred across sessions (c2274f26, e5156b86, 496689c2, 9e53c0d9; OPEN-259).
      15a (cycle 0): [not read — independence]
      15b (cycle 0, 2026-10-01): PARTIALLY-CHALLENGED (Moderate) — blog sources only; default-on-
        timeout flagged as harmful.
      15c: DISPOSITION-1019 → MONITOR-636 (High).
      15d (2026-10-11): re-triggered, cycle 0 → 1.
      15b (cycle 1, 2026-10-12): 4 searches (HITL backlog/absence; queueing with reneging; learning-
        to-defer under capacity; automation complacency); 2 fetches (arXiv 2402.12237 HTML — abstract
        read; arXiv abs page blocked as not-in-provenance).
    Current status: PARTIALLY-CHALLENGED
    Sources this cycle: Lykouris & Weng [abstract read from fetched HTML]; reneging-queue
      paper arXiv 1903.06870 [search-result only]; Parasuraman & Manzey 2010 [search-result only];
      Skitka, Mosier & Burdick 1999 [search-result, figures quoted second-hand].
    Date: 2026-10-12

  EVIDENCE GRADE: PRELIMINARY. First cycle with peer-reviewed/academic sources for this item, but only
    one abstract read; no study measures a review queue under reviewer ABSENCE. The owed evidence was
    NOT found — the search explicitly returned "nothing measured deferral or backlog behavior when
    reviewers are absent."

  Challenging evidence found: Partial

  Sources:
    1. Lykouris, T. & Weng, W. (MIT). "Learning to Defer in Congested Systems: The AI-Human Interplay"
       (earlier title "Learning to Defer in Content Moderation"). arXiv:2402.12237 (v4). [fetched HTML;
       abstract read, body NOT read] Models human review as a congested queue; the ADMISSION decision
       (whether to send an item to a human at all) is a control variable, and review delay is
       "endogenous to both the admission and the scheduling decisions"; fixed thresholds that ignore
       "the time-varying element of human review capacity" are inefficient. Bearing: the right
       response to reviewer absence is to change what gets escalated (raise the autonomy threshold when
       capacity is low), not to add an expiry/default/batching rule at the queue's exit. The refined
       presumption puts the control at the wrong end of the queue.
    2. Single-server queue with reneging (M/M/1+M), arXiv:1903.06870 "Large Deviations for the Single
       Server Queue and the Reneging Paradox" (authors not verified). [search-result only] In overload
       with abandonment, the long-run reneging count does not depend on the per-item reneging rate.
       Bearing (my inference, flagged as such): queues with abandonment are self-limiting — the
       backlog does NOT grow without bound; the cost reappears as silent loss. In C2A2 terms, escalated
       items go stale and are effectively abandoned (Day 076 re-flagged every 4 h is a renege-and-
       re-arrive pattern). "Grows without bound" is the wrong failure description; "silently loses
       decisions" is the right one, and it calls for a different metric (abandonment count, not depth).
    3. Parasuraman, R. & Manzey, D. H. (2010). "Complacency and Bias in Human Use of Automation: An
       Attentional Integration." Human Factors 52(3):381–410. doi:10.1177/0018720810376055.
       [search-result/abstract summaries only] Automation bias produces omission and commission errors,
       "cannot be prevented by training or instructions", affects experts and teams. Skitka, Mosier &
       Burdick (1999), IJHCS, as cited second-hand: 41% vs 3% missed critical events with vs without an
       automated aid [figures NOT verified against the paper]. Bearing: the presumption's comparison
       class ("reviewer present = safe") is itself not safe; a returning designer facing a 25-item
       backlog is the high-load condition under which complacency is strongest. An absence policy that
       ends in "batch for the human" may deliver rubber-stamping, not review.

  Strength of challenge: Moderate (unchanged level; now academically sourced, still indirect)

  Summary: The literature does not contradict the item's core worry — unattended escalation is costly.
    It challenges two parts of the refined form. First, unbounded growth is not the expected dynamic:
    with abandonment, queues self-limit and the damage is silent loss of decisions. Second, the lever
    is upstream admission (escalate less when capacity is low), not a downstream expiry/default/batch
    rule. And a backlog cleared in one sitting by a returning reviewer is the condition the automation-
    bias literature associates with rubber-stamping.

  Specific risks: (i) measuring queue depth will under-read the harm if items are effectively
    abandoned; (ii) a batching policy produces a burst review that is complacent by construction;
    (iii) an expiry policy converts silence into decisions without anyone deciding.

  Mitigations available: track abandonment (items escalated, never decided, no longer re-flagged) as
    well as depth; make escalation admission capacity-aware (when no human input for N days, the
    autonomy threshold rises and only items above a stated stakes level are escalated); cap batch size
    on reviewer return and require a stated reason per approval.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: PRESUMPTION-1101 / MONITOR-636 refined form
  Strongest counterargument: A queue with impatient customers does not explode; it bleeds. C2A2's
    escalations do not pile up forever — they go stale, get re-flagged, and quietly stop mattering,
    so depth is a misleading alarm. The congestion literature says the controllable quantity is
    what you admit to the human, not what you do with items already waiting; and the automation-
    bias literature says the human you are waiting for will rubber-stamp a big batch anyway. An
    "absence policy" at the exit of the queue therefore treats the symptom at the wrong end.
  What would need to be true for C2A2 to be safe: escalation admission falls when the reviewer is
    silent; abandoned/stale escalations are counted; reviewer-return batches are size-capped.
  How to test: in-house — for 2026-09-23..10-11, count escalations raised, decided, and abandoned
    (no decision, no longer re-flagged). If abandoned ≫ queue depth, the "unbounded growth" framing is
    wrong and the metric should change.

  Search scope: preliminary — 4 searches, 1 partial read. The owed item (measured HITL behaviour under
    reviewer absence) remains unfound; broader search (ACM DL, clinical decision-support "deferred
    decisions") recommended.
