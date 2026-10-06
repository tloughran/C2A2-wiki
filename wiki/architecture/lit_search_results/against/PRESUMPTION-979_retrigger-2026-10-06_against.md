SEARCH-AGAINST-PRESUMPTION-979 (RE-TRIGGER cycle 1, COMPARATIVE limb only):
  Date searched: 2026-10-06
  Original item: PRESUMPTION-979
  Original statement: "[inferred] That a report's prose caveats are read at the same rate as its status
    fields." Held at MONITOR-608 as the comparative limb: relative uptake of a prose qualification vs. a
    structured status field in the same document — a declared literature gap.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for* file,
    `lit_search_returns.md`, or today's 15a output. Note: a direct fetch of the Thieme abstract page for
    Brown et al. 2014 was refused by the session tool as "already fetched in this session" by another
    caller; I did not see that content. I retrieved the same abstract independently through the Europe PMC
    REST API.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b → 15c → 15d → 15b (re-trigger cycle 1)]
    Original item: PRESUMPTION-979
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from four same-day reports and one counter-example (red freshness gate unread six days).
      15b (2026-09-13): Searched caveat neglect / warning compliance; CHALLENGED.
      15c: DISPOSITION-956; operative limb → REVISE-466; comparative limb held as MONITOR-608.
      15d (2026-09-20): Re-triggered as a literature gap.
      15b (re-trigger cycle 1): Narrow search for within-document attention to narrative vs. structured
        sections. Found one direct eye-tracking study; its direction runs AGAINST the "move it into a status
        row" reading.
    Current status: CHALLENGED (equal-rate presumption) — with direction reversed relative to the intuitive remedy

  Challenging evidence found: Yes (narrow)

  Sources:
    1. Brown, P.J., Marquard, J.L., Amster, B., Romoser, M., Friderici, J., Goff, S. & Fisher, D. 2014.
       "What do physicians read (and ignore) in electronic progress notes?" Applied Clinical Informatics
       5(2):430–444. PMC4081746. [fetched — abstract via Europe PMC API; PMC full text blocked by reCAPTCHA,
       not bypassed] Eye-tracking, 10 hospitalists, 3 notes: most time and slowest reading in the narrative
       "Impression and Plan"; structured/imported sections (medication profile, vital signs, labs) "read very
       quickly even if they contained more content"; only 9% of verbal-handoff content came from outside the
       Impression and Plan; imported data "appears to largely be ignored."
    2. Structured codes vs. free-text notes in a Dutch GP database of 2.9M records (repub.eur.nl/pub/73187;
       summarised by trade pages tandemhealth.ai, johnsnowlabs.com) [search-result, trade summary — not
       verified; figures NOT carried forward] Structured and narrative channels are complementary rather than
       redundant: much of what is recorded in one is absent from the other.

  Strength of challenge: Moderate (direct within-document measurement exists, but small-n, clinical, and
    "imported structured data" is not identical to a one-token status field)

  Summary: The comparison MONITOR-608 calls unaddressed has at least one direct measurement in an adjacent
    domain: within a single document, readers spent their attention on the interpretive prose and skimmed
    the structured fields. That refutes the equal-rate presumption, but in the direction opposite to the
    intuitive remedy — prose was read MORE, structured data LESS. This converges with the estate's own
    counter-case (the unread red status field) and with MONITOR-608 constraint (1). The boundary: Brown's
    prose section was the author's synthesis (impression/plan), whereas the estate's at-risk prose is the
    qualification BENEATH a headline; the study does not separate synthesis prose from caveat prose. So the
    literature says "channel matters, and structure is not automatically more salient", not "caveats are
    read".

  Specific risks: A remedy that relocates qualifications into status rows may move them into the
    least-read region of the document. Treating channel as the variable when the operative variable is
    function (synthesis vs. imported/boilerplate) mis-specifies the experiment.

  Mitigations available: Put the load-bearing qualification inside the synthesis sentence the reader acts
    on (the scheduler-check pattern), and measure per audience (MONITOR-608 constraint 2).

  Recommendation: CHALLENGED (equal-rate presumption); the "literature gap" label should be narrowed —
    a within-document attention measurement exists; a caveat-specific one was not found. Preliminary search.

STEELMAN:
  Item: PRESUMPTION-979 (comparative limb)
  Strongest counterargument: Readers allocate attention by function, not by format: they read the part of
    a document that tells them what to do and skim everything that looks machine-generated. Status fields
    look machine-generated. The one direct eye-tracking measurement found shows structured sections read
    fastest and contributing under a tenth of what readers carried forward, so a status field is not a safe
    harbour for a qualification — and the estate's six-day-unread red gate is the same phenomenon.
  What would need to be true for C2A2 to be safe: the human reader of daily reports treats status rows as
    action-bearing (unlike the clinicians), or agents doing targeted retrieval are the only consumers.
  How to test: MONITOR-608 (b), split by audience; additionally classify each prose qualification as
    synthesis-embedded vs. trailing-caveat and compare act-on rates.
