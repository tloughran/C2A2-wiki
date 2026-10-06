SEARCH-AGAINST-ASSUMPTION-1261:
  Date searched: 2026-09-05
  Original item: ASSUMPTION-1261
  Original statement: "Restart the self-awareness pipeline — five days dark means five days of assumptions,
    presumptions and open questions unsurfaced."  (Frame under challenge: the gap is DEFERRED work;
    what went unsurfaced remains recoverable after the fact. PRESUMPTION-903 filed the opposite frame.)

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1261
    Item type: ASSUMPTION (stated — quoted from a derived digest)
    Transform at each step:
      14a: Extracted verbatim; flagged rationale drift vs PRESUMPTION-903 (destroyed vs deferred).
      15b: Searched for challenging literature (2026-09-05). NOTE ON AUTHORSHIP: run by the 15c
        orchestrating context after the delegated 15b subagent was interrupted. This context HAD
        ALREADY WRITTEN ASSUMPTION-1261_for.md ~1 hour earlier. This is the one item this run where the
        same context produced both directions; independence for this item is NOT claimed. Declared for
        15c to discount.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Naur 1985, "Programming as Theory Building" [established work; multiple secondary readings
       VERIFIED] — The theory built during the work "cannot be expressed in the developed program" and
       can only be enunciated by those who built it; reconstruction from artifacts yields something
       "incomplete and different." Challenge: the assumptions operative during 08-31…09-03 were held in
       the sessions, not in the files; the files are a lossy projection and 14a/14b extract from
       transcripts precisely because the files are insufficient. No interactive transcript was
       reachable for that window (PRESUMPTION-911).
    2. Roese & Vohs 2012, "Hindsight Bias," Perspectives on Psychological Science 7(5), doi
       10.1177/1745691612454303 [VERIFIED: title/journal/DOI/authors] and Hawkins & Hasher-lineage
       "Hindsight bias: An interaction of automatic and motivational factors?" Memory & Cognition,
       doi 10.3758/BF03197054 [VERIFIED: DOI; authors NOT verified] — Retrospective reconstruction of a
       prior judgement anchors on the known outcome and adjusts insufficiently; the bias is reduced when
       reasons were recorded at the time. Challenge: a later run "surfacing" the assumptions of a past
       window reconstructs them through outcomes already known by 09-04 (the outline held / did not; the
       re-pass count), which is not the same evidence a contemporaneous extraction would have produced.
    3. Recall bias, Catalogue of Bias (catalogofbias.org) and "Recall Bias can be a Threat to
       Retrospective and Prospective Research Designs" (ResearchGate 269933925) [VERIFIED: pages located;
       authors of the second NOT verified] — Accuracy and volume of recalled events degrade with
       interval and are shaped by subsequent events. Same direction, for the human half of the record.
    4. Informative missingness / MNAR: "Informative missingness: What can we learn from patterns in
       missing laboratory data in the electronic health record?" JBI 2023, S1532046423000278 [VERIFIED:
       title/journal/ID; authors NOT verified] — Absence of a record is itself informative about the
       conditions that produced it and cannot be treated as absence of events; imputation under MNAR is
       invalid without a model of the missingness. Challenge: "five days unsurfaced" treats the gap as
       MCAR (the events happened, just not logged); PRESUMPTION-903's frame is that the gap is MNAR (what
       went dark is correlated with what was happening). PREMISE-124(b) already holds this for the
       pipeline's own self-audits.
    5. Alkadhi et al. 2018, "How Do Developers Discuss Rationale?" [VERIFIED: title; TUM PDF located] —
       Cited AGAINST the frame for its denominator: only ~25% of persisted developer messages carry
       rationale, and that is in a medium written to be read. The rationale that lives in unpersisted
       session reasoning has a recovery rate of zero by construction.

  Strength of challenge: Moderate-to-Strong

  Summary: The frame "unsurfaced, therefore recoverable later" is challenged on three grounds. Naur and
  the rationale-capture literature hold that what is recoverable from artifacts is a different and
  smaller object than what was operative; the hindsight and recall literatures hold that whatever is
  reconstructed later is systematically distorted by outcomes known in the interim; and the
  missing-data literature holds that a gap whose cause is correlated with the content of the gap cannot
  be imputed from its edges. The 09-04 run's own conduct is the strongest evidence: it did not attempt
  to reconstruct 08-31…09-03, and 14a recorded that no transcript was reachable. What the assumption
  calls deferred is, for the transcript-borne portion, gone.

  Specific risks:
    - The register will contain a five-day hole that later reads as "quiet" rather than "dark"
      (PREMISE-124(b) names this failure).
    - Any assumption that was operative during the sandbox re-pass on 09-01..03 and abandoned by 09-04
      is unrecoverable and unrecorded — the class most worth having.
    - Rationale drift between PRESUMPTION-903 and this digest is itself an instance: the "destroyed"
      frame was surfaced, then lost, in five days.

  Mitigations available:
    - Tag the window explicitly as DARK / not reconstructed in the registers (cheap; matches PREMISE-124).
    - Where transcripts exist but were unreachable, retrieve and run 14a/14b on them with the run dated
      as retrospective, so the hindsight discount is visible.
    - Persist session reasoning contemporaneously (the daily_sync digest is the existing channel).

  Search scope: Preliminary — 3 queries (Naur/theory-building; hindsight and recall bias; informative
  missingness). Not covered: the design-rationale-capture literature proper (Burge & Brown, Dutoit et
  al.), which would quantify capture-vs-recovery rates.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-1261
    Strongest counterargument: "Unsurfaced" is the wrong verb because it presupposes the thing is still
      down there. The assumptions operative in a working session live in the session; the artifacts it
      leaves are a lossy projection, which is the entire reason 14a/14b read transcripts rather than
      files. For 08-31…09-03 there is no reachable transcript, so the recoverable set is whatever the
      files happen to encode — at a rate the rationale literature measures at a quarter, in media built
      for reading. Whatever IS reconstructed later will be reconstructed by a reader who already knows
      how the sandbox re-pass came out, and hindsight research says that reader cannot un-know it. And
      the gap is not random: the pipeline went dark because attention was on the sandbox, which is
      exactly the work whose assumptions matter most. The digest's frame turns a hole into a backlog;
      PRESUMPTION-903 had it right five days earlier, and the reversion is itself the phenomenon.
    What would need to be true for C2A2 to be safe: reachable transcripts for the window; a retrospective
      run explicitly dated as such; and a check that the retrospective extraction does not simply
      re-derive the 09-04 outcome.
    How to test: If transcripts become reachable (PRESUMPTION-911's condition), run 14a/14b on them and
      compare against what the 09-04 gap-filling run produced from files alone. The difference is the
      destroyed set. If no transcript is ever reachable, the test cannot be run and that fact is the
      answer.
