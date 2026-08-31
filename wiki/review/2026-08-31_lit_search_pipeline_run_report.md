# C2A2 literature-search pipeline — run report, 2026-08-31

Scheduled task `c2a2-lit-search-pipeline`. Agents 15a, 15b, 15c over the 2026-08-30 intake cohort.

## Outcome

The cohort is fully drained. 27 items: 19 searched by both directions, 8 tagged `[NOT-SEARCHED-15a/15b]`
with a stated reason rather than left implicitly open.

| Disposition | Count | Ids |
|---|---|---|
| INCORPORATE | 4 | PREMISE-194..197 |
| MONITOR | 6 | MONITOR-585..590 |
| REVISE | 11 | REVISE-413..423 (421 and 423 are roll-ups) |

Full records: DISPOSITION-870..888 in `architecture/lit_search_returns.md`. Nothing is left
searched-but-undispositioned. All 38 result files carry complete provenance chains.

## Two things went right

**15a and 15b were genuinely independent for the first time.** Every disposition since 2026-08-29 has
carried an independence discount because both directions ran in one process. This run used six separate
agent contexts — three FOR, three AGAINST, partitioned by cluster — neither able to read the other's
files. Five items turned on the two directions independently converging on the *same correction*
(ASSUMPTION-1234, 1235, 1236/1237, 1242/900); under the old coupling those convergences would have been
discounted to nothing.

PREMISE-197, minted this run, immediately qualifies that: separate contexts sharing a base model and
prompt scaffold are not independent generators. Context separation removed a contamination channel; it
did not create statistical independence. The premise was applied against its own run.

**The 2026-08-25 budget recommendation worked.** Every agent ran a mandatory 2 queries per item across
its whole list before deepening anything, then 1 more on High-priority items. ~104 queries, no
truncation, and the four under-searched item-sides are under-searched *by design* and are all MONITOR,
never INCORPORATE. The confound that spoiled the 08-25 run did not recur. Worth making standing.

## One thing went wrong, and it measured something

**The run caused two destructive writes and detected one.** Three concurrent 15b agents each picked a
`SYSTEMIC-RISK-FLAG` filename by globbing for a free letter — a check-then-act race. It fired twice
within a minute; two flag files were overwritten and lost unread. One overwrite was voluntarily
self-reported by its perpetrator. The other was invisible to every agent involved and surfaced only
because 15c reconciled the agents' return summaries against the directory listing.

That is a **detection rate of 1 in 2** for the voluntary self-report channel. Accidental, n=2, and it is
the only measurement this estate has ever had of that channel — pointing the same way as the ~1-in-20 in
the healthcare literature 15b found. It is cited as internal evidence in PREMISE-195 and REVISE-417.

Both flags were reconstructed from the authoring agents' own end-of-run summaries and are labelled
**lossy and derivative** — which is precisely the substitution PRESUMPTION-894 names and both directions
challenged in this same run. I did it anyway, because a labelled lossy reconstruction beats an unlabelled
hole, and recorded the act as a known violation of PREMISE-194 rather than as a recovery.

Fourth consecutive last-writer-wins incident in this estate; first caused *by* the pipeline *while
searching literature about* that failure class.

## What to read first

**REVISE-417** (PRESUMPTION-895) — voluntary self-report is not a detection control. Both directions
Strong. Remedy is cheap and off the shelf: a per-run manifest of (path, size, sha256, line count) per
register, written at run end and diffed at the next run's start. It would have caught both of today's
overwrites.

**REVISE-422** (PRESUMPTION-901) — the clearest result in the intake, and the one with the most bite for
you specifically. A project whose methodology descends from MacIntyre — whose criterion for rational
tradition-progress is that a tradition must be able to say what it has *lost* as well as what it has
absorbed — was presuming that no failure mode exists for absorbing every challenge. Popper's immunizing
stratagem and Lakatos's degenerating problemshift both name it, and both name the same discriminating
property: content reduction. The pipeline cannot detect it because it does not retain what it amended
away. Remedy is one retained line per amendment. Note the reflexive bite: three amendments in *this* run
are themselves ungraded.

**REVISE-413** (ASSUMPTION-1233) — no restore has ever been performed. A snapshot regime that has never
been restored from is a plan, not a control. Thirty minutes converts it.

## Novelty ledger — 3 of 4 nominations withdrawn

ASSUMPTION-1241, PRESUMPTION-901 and PRESUMPTION-900 are all heavily named in existing literature
(Popper/Lakatos; Bommasani et al. on algorithmic monoculture; Bovens & Hartmann). The survivor is
**ASSUMPTION-1244, on one limb only**: neither direction found *any* literature on whether
contemplative-tradition stage frameworks encode normative ascent the way psychometric ones do. Two
opposite-direction contexts both returning empty is a strong null, and it is the cohort's real novelty.
Suggested routing: Agent 19, against Rohr's own sources (John of the Cross, Teresa's mansions, the Cloud
author) — a tradition-wiki question as much as a 15a/15b one.

A 3-of-4 miss rate, all three in philosophy of science, in a project with a resident expert on that
shelf, is worth naming. Possibly connected to REVISE-418: this cohort was extracted from a daily digest
rather than a transcript, and a digest surfaces what was already salient.

## Decisions waiting on you (REVISE-423)

None of these can progress without a ruling. Weeks deferred in brackets.

- **[3]** 26 one-line alias files — do non-destructive new files fall under the no-blind-push rule? One
  authorisation covers ASSUMPTION-1238 and PRESUMPTION-898. Baseline pinned: 281 broken links → predicted
  116. ~20 links accrue per week.
- **[9 days]** Gmail draft authorisation (ASSUMPTION-1245). One line, testable immediately.
- **ASSUMPTION-1247** — a flag asserts "nothing depends on PREMISE-122's result" while itself listing
  three items that rest on it. Someone must read the two and rule.
- **PRESUMPTION-899** — name the daily summary's readers. Eight days undelivered. If none, stop producing it.

Separately, the **26-item 2026-07-21 cohort is now 41 days old and untagged**. This is the eighth
consecutive run to report it. Per PREMISE-183 this run does not re-file the same request — the binary
decision put to you on 2026-08-25 (search them with reserved budget, or close them WONTSEARCH) stands
unanswered and is restated once in `revision_flags.md`.

## Write discipline

The queue file was snapshotted before modification and rewritten via temp-file-in-the-same-directory →
fsync → rename → fsync(parent), i.e. REVISE-413 and REVISE-414 were applied to the run that filed them.
All four register appends were byte-verified against expected length. Had this discipline been in the 15b
agents' file-writing path, the incident above would not have happened.

**Verification pass:** all 27 cohort ids tagged exactly once; 38 result files present, non-empty, with
complete PROVENANCE blocks; no searched-but-undispositioned items; no id collisions in any range minted
this run. The apparent duplicate ids elsewhere in the registers were checked and are benign —
cross-references and one amendment block, plus a regex artifact from `DISPOSITION-15c:`.

**Evidence grade for the whole cohort:** snippet-level web search, zero full-text reads. Several cited
2026 arXiv preprints were seen as title-plus-URL only and are flagged unverified in their own files.
Nothing load-bearing rests on a single unverified preprint; where one was the strongest source, the
disposition is MONITOR.
