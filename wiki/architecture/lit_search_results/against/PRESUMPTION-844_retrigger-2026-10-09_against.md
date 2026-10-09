SEARCH-AGAINST-PRESUMPTION-844 (RE-TRIGGER cycle 1):
  Date searched: 2026-10-09
  Original item: PRESUMPTION-844
  Original statement: [inferred] That the review artifact is the right instrument, and only its depth
    is the problem (a 677 KB, 54-card single-page review treated as a neutral container).
  Under test this cycle (MONITOR-543): the monitored counter-claim — the review ARTIFACT is itself a
    variable in review throughput — and its NOVELTY flag, against the code-review change-set-size /
    review-effectiveness literature (unsearched at intake). Direction of challenge: I searched for
    evidence that (a) the novelty claim fails and (b) the container/granularity mechanism the
    proposed split-test assumes does not operate.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for file,
    `lit_search_returns.md`, or any 15a output from today.
  INDEPENDENCE INCIDENT: my fetch of peerj.com/articles/cs-193 (di Biase et al. 2019) was refused as
    "Already fetched … 27s ago in this session." I did not fetch it earlier; another agent sharing the
    fetch layer did, seconds before. No content returned to me. See today's SYSTEMIC-RISK flag.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 1)]
    Original item: PRESUMPTION-844
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b (2026-08-18): Inferred from four escalations framing the review bottleneck as depth only.
      15a (cycle 0): supportive on volume and quality limbs; NOVELTY-flagged (no container literature);
        cautioned that change-set-size literature was unsearched.
      15b (cycle 0, 2026-08-19): challenged the presumption (Moderate) — artifact is a variable;
        400-LOC figure secondary only; recommended split-test over citation-hunting.
      15c: → MONITOR-543 (High, NOVELTY-flagged).
      15d (2026-08-30): Re-triggered, cycle 1; owed = change-set-size literature + split-test.
      15b (re-trigger cycle 1, 2026-10-09): 3 searches (review rate/size; change decomposition;
        pagination vs scrolling); 2 fetch attempts — di Biase (FAILED, dedup), Sharma & Murano
        (fetched, abstract).
    Current status: PARTIALLY-CHALLENGED

  EVIDENCE GRADE: PRELIMINARY. One abstract fetched; decomposition experiment at search-result level;
    review-rate figures still secondary.

  Challenging evidence found: Yes (against NOVELTY); Partial (against the container mechanism)

  Sources:
    1. di Biase, M., Bruntink, M., van Deursen, A. & Bacchelli, A. 2019. "The effects of change
       decomposition on code review — a controlled experiment." PeerJ Computer Science 5:e193
       (arXiv:1805.10978; PMC7924728). [search-result; fetch failed — dedup] 28 developers;
       decomposing a change "led to fewer wrongly reported issues" and made reviewers seek more
       context, but did NOT change defects found or understanding of the change's rationale.
       Bearing: (a) a controlled experiment on splitting the review artifact exists — the NOVELTY
       flag does not survive in its "nothing on artifact granularity" form; (b) its result is that
       splitting changes reviewer noise, not detection. If transferred, paginating the 54-card page
       would at best reduce erroneous dispositions, not raise throughput.
    2. Sharma, S. & Murano, P. 2020. "A usability evaluation of Web user interface scrolling types."
       First Monday 25(3). doi:10.5210/fm.v25i3.10309. [fetched, abstract] Normal scrolling with
       pagination, infinite scroll, load-more and infinite-with-pagination compared on serendipitous
       and goal-oriented tasks: "no single scrolling method stood out as being the most usable."
       Bearing: the container contrast the split-test would manipulate (paginated vs single page) has
       a null-ish prior in the HCI literature.
    3. usability.gov Research-Based Web Design & Usability Guidelines (2004, archived, ch. 8).
       [search-result] "no reliable difference between scrolling and paging when people are reading
       for comprehension" when pages load fast. Bearing: as source 2. Caveat: 677 KB may not load
       fast, which is the one place the container could matter.
    4. Kemerer, C. F. & Paulk, M. C. 2009. "The Impact of Design and Code Reviews on Software Quality:
       An Empirical Study Based on PSP Data." IEEE TSE. (via Wikipedia "Code review") [search-result;
       primary NOT read; title from background knowledge, unverified] Review effectiveness tracks
       review RATE (200–400 LOC/hour recommended). SmartBear/Cisco figures (defect density falls above
       ~200 LOC; none found after 90 minutes) remain secondary-only (agileconnection.com summary).
       Bearing: the variable the review literature actually measures is attention per unit time and
       session length — amount per sitting — not presentation container. This SUPPORTS the monitored
       claim's volume limb and CHALLENGES its container framing.
    5. Rigby et al. (six OSS projects): "small change size is essential to the fine-grained style of
       peer review." [search-result, as reported inside the di Biase result] Bearing: size, again, not
       container.

  Strength of challenge: Moderate (against NOVELTY); Weak-to-Moderate (against container mechanism)

  Summary: The change-decomposition and review-rate literatures exist and bear directly on the item,
    so the NOVELTY flag as worded should not survive. But they cut in a specific direction: what
    predicts review outcome is how much is reviewed per sitting and how fast, not how it is paged.
    The one controlled experiment on splitting a review artifact found fewer erroneous reports but no
    gain in detection, and HCI comparisons of paginated vs scrolling layouts are mixed-to-null. The
    original presumption ("only depth matters") stays challenged — size per sitting matters — but a
    paginated-vs-single-page split-test that leaves 54 cards per sitting is likely to return a null
    and be misread as clearing the artifact.

  Specific risks: (i) running the endorsed split-test on the wrong variable (container) and
    concluding the artifact is innocent; (ii) keeping the NOVELTY priority bump on a flag the
    literature removes; (iii) load time of a 677 KB page is the only container-level mechanism with
    support, and it is untested.

  Mitigations available: redesign the split-test to vary cards-per-session (e.g. 10 vs 54) rather
    than pagination; measure disposition error/reversal rate as well as throughput (di Biase's
    sensitive outcome); retrieve Kemerer & Paulk 2009 primary before quoting any LOC figure.

  Recommendation: PARTIALLY-CHALLENGED — NOVELTY flag challenged; "artifact is a variable" survives
    only as "amount per sitting is a variable"; container granularity per se weakly challenged.

STEELMAN:
  Item: PRESUMPTION-844 (monitored counter-claim and NOVELTY flag)
  Strongest counterargument: Software engineering has studied exactly this — splitting large review
    artifacts into smaller ones — in a controlled experiment, and found that reviewers made fewer
    spurious complaints but caught no more defects. Usability research finds no consistent winner
    between paged and scrolled layouts. The robust finding is the old one: reviewers degrade with
    volume and time on task. So the 54-card page is a problem because it asks for 54 judgements in
    one sitting, and paginating it would change nothing a human experiences; the item's genuine
    insight is volume-per-session, which is not novel.
  What would need to be true for C2A2 to be safe: the remedy chosen changes judgements per sitting
    (smaller batches, more frequent), not merely the page structure.
  How to test: a split-test on batch size per session (10 vs 54 cards) with outcome = cards
    dispositioned within 72 h and later-reversed dispositions; a pagination-only arm as a control
    expected to show no difference.
