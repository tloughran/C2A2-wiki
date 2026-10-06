SEARCH-AGAINST-ASSUMPTION-1305 (RE-TRIGGER cycle 1, LIMB C only):
  Date searched: 2026-10-06
  Original item: ASSUMPTION-1305
  Original statement (limb C, per MONITOR-600): "therefore the correct act on the morning `pending/` hit
    zero was to skip the hunt phase." Watched as: withholding intake supply when the intake queue empties
    raises throughput of adequately-reviewed items, rather than starving stage 1 while stage 3 stays congested.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for* file,
    `lit_search_returns.md`, or today's 15a output. I read my own prior file (ASSUMPTION-1305_against.md,
    first 30 lines only), the queue block and MONITOR-600. Channel note: the session fetch tool reported
    three unrelated URLs in today's cohort as "already fetched in this session" by another caller; their
    content was never shown to me and is not used anywhere in this cohort.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b → 15c → 15d → 15b (re-trigger cycle 1)]
    Original item: ASSUMPTION-1305
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim from the run report. First day `pending/` reached zero and supply was withheld.
      15b (2026-09-11): Searched for challenging literature; argued DBR forbids starving the constraint buffer.
      15c: DISPOSITION-928, limb-split; limb C held as MONITOR-600.
      15d (2026-09-20 / 2026-10-04): Re-triggered; owed = Goldratt / DBR primary-source retrieval.
      15b (re-trigger cycle 1, 2026-10-06): Narrow search for primary DBR / CONWIP release logic on
        skip-the-hunt at pending = 0. **Goldratt's primary texts were again NOT retrieved (books; no open
        full text found).** Found that the primary release logic weakens 15b's own prior counter and
        relocates the challenge to the release SIGNAL and to perishability.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Goldratt, E.M. & Cox, J. 1984. *The Goal.* North River Press. [search-result, secondary summaries
       only — primary NOT retrieved] Aphorisms "an hour lost at a bottleneck is an hour lost for the entire
       system; an hour saved at a non-bottleneck is a mirage." **Cuts BOTH ways and mostly FOR limb C:** if the
       hunt phase is a non-constraint, idling it costs nothing.
    2. Drum-buffer-rope descriptions (6sigma.us; fortelabs.com "Theory of Constraints 105") [search-result,
       practitioner] The buffer is held in front of the CONSTRAINT; the rope releases new work "only when the
       constraint consumes one, offset by the buffer time." Release is keyed to constraint consumption, not to
       the state of the intake queue.
    3. Spearman, M.L., Woodruff, D.L. & Hopp, W.J. 1990. "CONWIP: a pull alternative to kanban." Int. J.
       Production Research 28:879–894. [fetched — abstract and reference list only via the PPI reprint page;
       body not available] Release rule (CONWIP: a new job enters only when a card frees at system exit)
       [search-result, Wikipedia/allaboutlean summary]. Release is keyed to TOTAL system WIP against a cap.
    4. Schragenheim — Simplified DBR, buffer-penetration zones (TOCICO course page; 6sigma.us) [search-result]
       Release and expediting are driven by buffer penetration (green/yellow/red), i.e. a BAND, not emptiness.

  Strength of challenge: Weak-to-Moderate

  Summary: The primary-source logic does NOT straightforwardly support 15b's prior counter. In DBR and CONWIP
    the protected buffer is the one in front of the CONSTRAINT; on 15c's own reading the constraint is review
    (stage 3), and 85 triplets were sitting in front of it — the constraint buffer was full, and both the
    rope and a CONWIP cap would have WITHHELD release that morning. The prior "starving the constraint"
    objection holds only if `pending/` is itself the constraint buffer, which MONITOR-600 does not establish.
    What survives is narrower and still real: (i) both doctrines key release to the constraint's buffer
    state or total WIP, never to upstream-queue EMPTINESS — so `pending/ = 0` was the wrong trigger even if
    the act was right; and (ii) DBR/CONWIP assume raw material can be released later at will. A hunt over
    perishable sources (dated windows, paywalled recordings) violates that assumption; the doctrine has no
    rule for it, which is a failed-transfer boundary, not a contradiction.

  Specific risks: A skip rule keyed to emptiness will fire both when review is congested (harmless) and when
    review is idle (starves the constraint) — it cannot tell them apart. Perishable sources lost on skipped
    days are an unpriced, irreversible cost DBR does not model.

  Mitigations available: Key the hunt to a review-buffer band (MONITOR-600's TARGET BUFFER BAND), not to
    `pending/`; standing on-sight capture exemption for perishable sources.

  Recommendation: PARTIALLY-CHALLENGED (challenge relocated from "act" to "trigger" and "perishability");
    preliminary search — Goldratt primary (The Goal; The Haystack Syndrome 1990) still unretrieved.

STEELMAN:
  Item: ASSUMPTION-1305 (limb C)
  Strongest counterargument: Every pull doctrine that limb C borrows authority from — DBR's rope, CONWIP's
    card, kanban — makes release a function of the constraint's state, never of the feeder queue's. Limb C
    reasoned from the feeder ("pending/ is empty, so don't refill it"), which means the decision was right
    only by coincidence of review being congested that day; the same rule on a light-review day starves the
    bottleneck, which is the one loss TOC says is unrecoverable. And unlike factory raw stock, the hunt's
    inputs decay: a source not captured today may not exist tomorrow, so "release later" is not available.
  What would need to be true for C2A2 to be safe: review is the constraint AND its buffer was above a set
    floor on every skip day; and the skipped hunt's sources were non-perishable (MONITOR-600 (b)).
  How to test: log review-buffer depth/age on skip days; any skip with the review buffer below floor is a
    DBR violation. Re-attempt retrieval of the 2026-09-10 sample (MONITOR-600 (b)).
