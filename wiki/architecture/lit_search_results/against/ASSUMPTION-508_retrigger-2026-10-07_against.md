SEARCH-AGAINST-ASSUMPTION-508 (RE-TRIGGER cycle 1 — DEDICATED 15b search, explicitly owed):
  Date searched: 2026-10-07
  Original item: ASSUMPTION-508
  Original statement: "McGilchrist-002 entered at Speculative because only title/venue were available;
    flagged transcript-verify-before-ingest — fail loud, not fabricate."
  Why owed: MONITOR-575 records the cycle-0 15b file as NOT independently searched ("the null reflects
    search scope, not a searched-and-empty challenge direction"). This file is the first real AGAINST pass.
  Challenge lanes searched: (a) costs of over-conservative exclusion of thin sources; (b) evidential
    signal in title/venue/abstract-only metadata; (c) whether quarantine labels lead to verification
    backlogs (items never verified).

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for* file,
    `lit_search_returns.md`, or today's 15a output. (MONITOR-575's one-line record of the 15a verdict was
    visible in monitor_queue.md, which I was directed to read; I did not read 15a's sources.)

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 1, dedicated)]
    Original item: ASSUMPTION-508
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-22 McGilchrist specialist run (PROP-2026-07-22-002).
      15b (2026-08-30): NO-CHALLENGE-FOUND (None) — no dedicated challenge query run.
      15c: DISPOSITION-857 → MONITOR-575 (HIGH, procedural).
      15d (2026-09-13): Re-triggered; dedicated 15b search owed.
      15b (re-trigger cycle 1, 2026-10-07): 3 searches, 1 fetch (Redi et al., abstract + intro read,
        lines 1–80 of ~1,150), plus an in-house state check of the item's own trail (inbox/PROCESSED_LOG.md).
    Current status: PARTIALLY-CHALLENGED

  EVIDENCE GRADE: one fetched paper (partial read); remainder search-result. In-house check is
    observational, flagged as such, and is NOT literature.

  Challenging evidence found: Partial — the core "fail loud, not fabricate" rule is NOT challenged;
    its downstream (does the Speculative label ever get discharged?) is.

  Sources:
    1. Hopewell, S., McDonald, S., Clarke, M. & Egger, M. 2007. "Grey literature in meta-analyses of
       randomized trials of health care interventions." Cochrane Database of Systematic Reviews MR000010.
       [search-result] Published trials showed larger effects than grey-literature trials in all five
       included studies; failing to capture conference-proceedings material can bias a review. Cochrane
       and the US National Academies recommend searching for and including conference abstracts.
       Bearing (lane a): EXCLUDING thin sources is a documented source of bias. BOUNDARY: 508 does not
       exclude — it admits at Speculative. This challenges only an exclusion reading of 508, not 508.
    2. Abstract-vs-full-report concordance literature (e.g. Trials 2016, doi 10.1186/s13063-016-1343-z;
       Cochrane Colloquium abstracts 1998, 2015). [search-result] ~Half of conference abstracts reach
       full publication; 31%–60% of abstract/full-paper pairs show discordant results; 79% when the
       abstract reported interim data. Bearing (lane b): CUTS FOR 508 — thin metadata is unreliable
       about content, so withholding content claims until a transcript exists is well-founded.
       Reported honestly as non-challenging.
    3. Redi, M., Fetahu, B., Morgan, J. & Taraborelli, D. 2019. "Citation Needed: A Taxonomy and
       Algorithmic Assessment of Wikipedia's Verifiability." WWW '19, arXiv:1902.11116. [fetched —
       abstract and introduction only] Wikipedia's policy is that unsourced material is "removed or
       challenged with a {citation needed} flag"; as of Feb 2019 "more than 350,000 articles with one or
       more {citation needed} flag, we might be missing many more"; manual verification "at scale" does
       not keep up. [search-result, not in the portion read: tags "stay in place for months or years,
       forming an ever-growing backlog"; 380,000+ articles by Feb 2020.] Bearing (lane c): the closest
       large-scale analogue of a "verify-before-use" label shows the label is cheap to apply and
       expensive to discharge, producing a growing standing backlog.

  IN-HOUSE OBSERVATION (not literature; checked because lane (c) is directly testable on this item):
    inbox/PROCESSED_LOG.md shows PROP-2026-07-22-002 HELD at the verification gate on 2026-08-11 (no
    transcript/recording found); PROP-2026-08-15-002 records the RE-OPEN CONDITION MET (recording live,
    00:08:58) but "+0 ... The content gate still stands." A grep of the wiki (excluding for/) found no
    later record of the address being listened to or transcribed. The item has been Speculative for
    77 days, 53 of them after its stated discharge condition was met. ALSO NOTED, NOT ADJUDICATED:
    PROCESSED_LOG line ~695 records "PROP-2026-06-24-002 mcgilchrist_ralston-commencement-2026 ->
    mcgilchrist PRS-47 (+1)" — the same commencement may already have been ingested a month BEFORE the
    07-22 Speculative entry. If so, the fail-loud gate quarantined a duplicate of an admitted item. Routed
    to 14a/15c as an empirical question; I did not verify.

  Strength of challenge: Weak-to-Moderate (literature: Weak on the rule itself, Moderate on the backlog
    lane; in-house observation strengthens lane (c) but is not literature)

  Summary: The rule "fail loud, not fabricate" survives a dedicated adversarial search: the evidence on
    abstract/full-report discordance positively supports refusing to infer content from title/venue,
    and the grey-literature bias finding attacks exclusion, which 508 did not do. What the search does
    challenge is the implicit second half of the rule — that a Speculative/verify-before-ingest flag is
    a temporary state. The Wikipedia verifiability literature shows such flags accumulate into a large,
    persistent backlog, and the item's own trail fits that pattern: the discharge condition was met in
    mid-August and the flag still stands. A fail-loud gate without a discharge path converts "not
    fabricated" into "not known" indefinitely.

  Specific risks: Speculative items accumulate unverified; the label is applied consistently but never
    discharged (the documentation-as-compliance pattern named at cycle 0, now with a datum); possible
    duplicate-quarantine of already-ingested content.

  Mitigations available: Attach a discharge owner and a due date to every Speculative flag; auto-schedule
    the verification task when the re-open condition fires (it fired 2026-08-15 and nothing scheduled);
    report count and median age of open Speculative flags.

  Recommendation: PARTIALLY-CHALLENGED — rule supported in kind; its discharge path is challenged.
    The pairing is now complete; 15c may disposition.

STEELMAN:
  Item: ASSUMPTION-508
  Strongest counterargument: "Fail loud" is only half a protocol. Every large verification system that
    marks content "needs source" instead of deleting or verifying it accumulates hundreds of thousands
    of such marks that persist for months or years, because applying the mark is one step and
    discharging it is a separate unowned task. A Speculative tag that is never discharged is not
    caution; it is a permanent gap that reads as caution, and it can even quarantine material the
    system already holds. The test of the rule is not whether it refused to fabricate on 07-22 — it did
    — but whether the item became known once it could be; on 2026-10-07 it had not.
  What would need to be true for C2A2 to be safe: Speculative flags have owners, triggers and a measured
    median time-to-discharge.
  How to test: list all open Speculative/verify-before-ingest flags with age and whether their re-open
    condition has fired; the share with condition-met-but-undischarged is the backlog measure.
