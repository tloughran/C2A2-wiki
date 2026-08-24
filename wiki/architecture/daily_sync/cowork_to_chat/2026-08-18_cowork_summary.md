# Cowork Progress Summary — 2026-08-18
*Generated at 18:38 EDT for daily walk Chat context*

> **Note on the Chat→Cowork side:** this morning's inbound scrape **FAILED** — the Chrome
> profile is signed out of claude.ai and the Claude-in-Chrome extension reported not
> connected. So today's Cowork work ran with **no** Chat context from the morning walk.
> Delivery status of *this* file to Chat is recorded at the bottom.

## What Was Accomplished Today

The day was dominated by a single large pipeline run: **Agents 15a/15b/15c completed a
23-item literature-search batch (DISPOSITION-739..761)** across four cohorts (G1–G4), and
15b raised **four SYSTEMIC RISK FLAGS** — the first time a single run has produced systemic
flags on every cohort.

The 23 items split **5 INCORPORATE / 7 MONITOR / 11 REVISE**. Notably, 15c deliberately
cited *sources* rather than inter-agent agreement for every disposition, because one of the
findings in the batch invalidates agreement-as-evidence inside this system (see
PRESUMPTION-751 below). That is a methodological change the run made to itself, mid-run.

Also today: the daily review HTML regenerated (`2026-08-18_review.html`, 677 KB); one new
proposal filed (PROP-2026-08-18-001, Hawkins / Thousand Brains plain-language explainer —
self-flagged in its own body as a likely deny, since it explains a paper the vault already
ingested twice); and watch_list WATCH-002 and WATCH-003 were both checked on cadence
(count 5), **both conditions NOT met**.

## Key Decisions Made

No new DECISION-NNN entries were written to `decisions.md` today. The consequential
determinations were recorded as dispositions and revision flags instead:

- **DISPOSITION-739..761** — 23 items dispositioned (5 INCORPORATE, 7 MONITOR, 11 REVISE).
- **Methodological ruling at DISPOSITION-749 / REVISE-350** — 15a and 15b are the same
  model, so their concordance is not independent corroboration; every disposition in the
  batch must cite sources, not agreement. Applied immediately and retroactively flagged
  against prior counts.
- **PREMISE-176 (from ASSUMPTION-1129)** — *for an irreversible operation, review is not a
  control; reversibility is.* Any pass that can delete, retire or overwrite must be
  structurally reversible (quarantine / tombstone / recovery window) before it is permitted
  to run. Founded on two regex instruments that were wrong **by construction** — both bound
  only the head id after a tradition name, so every trailing id in an enumerated citation
  read as absent, and a false absence is exactly what a retirement pass acts on.
- Total validated premises now **178 unique**.

## New Open Questions

No new OPEN-NNN entries in `open_questions.md`. The equivalent output today was
**12 revision flags (REVISE-347..358)** and **7 monitor items (MONITOR-535..541)**.

The four systemic flags each name a question the system cannot currently answer about itself:

- **G1 — monocausal inference from single-day, uncontrolled observation, and the correction
  inheriting the standing of the thing it corrected.** Six items (ASSUMPTION-1126, -1129,
  -1132; PRESUMPTION-829, -830, -834). The pipeline that detects wrong causes is
  structurally identical to the one that produced them. Secondary limb: in each case the
  *proposed remedy* is subject to the failure mode it is meant to catch.
- **G2 — identifier-level verification used as a proxy for content-level, polarity-aware
  verification.** Six items. Checking that a citation exists, matches its label, has the
  right author list, hasn't been withdrawn — and then concluding something about whether the
  source *supports* the sentence it anchors. The proposed fixes (add a polarity field,
  escalate to read-the-body) are further identifier-layer moves against a relation-layer
  problem. Quotation-accuracy literature puts the gap at ~17–25% error among references that
  exist and are correctly identified.
- **G3 — "declared but unenforced": constraints that exist as text and not as force.**
  PRESUMPTION-758, -762, -764, -833. A recall window with an unbounded exception clause; a
  hold queue with no expiry or default disposition; **a token budget that every run declares
  and every run breaches, with disclosure as the only sanction**; a status lifecycle with no
  terminal state for a withdrawn flag. All four failures are *invisible in the artefact* —
  a nullified window looks identical to one in force. Diagnosis: normalization of deviance.
- **G4 — HIGH RISK — shared vocabulary converted into asserted structural identity, then
  closed on a single unreviewed reading.** ASSUMPTION-933, -937, -939 (primary), -934
  (secondary). Bears on **90+ CROSS entries** — the wiki's headline output metric, which
  feeds the master index, pattern detector, synthesis files and the narration graph's
  shared-reference edges. Rated HIGH because the artefact rate is *unmeasured*, not because
  it has been shown to be large.

## Files Created or Modified

- `architecture/lit_search_returns.md` — 15a/15b returns + 15c dispositions appended (now 32,677 lines)
- `architecture/revision_flags.md` — REVISE-347..358 appended (now 10,547 lines)
- `architecture/monitor_queue.md` — MONITOR-535..541 appended (now 20,522 lines)
- `architecture/validated_premises.md` — PREMISE-176 et al. + register-reinforcement notice
- `architecture/lit_search_results/for/` and `/against/` — 22 item files each direction
- `architecture/lit_search_results/against/SYSTEMIC-RISK-FLAG_2026-08-18_G1..G4.md` — 4 new
- `architecture/for_lit_search.md`, `monitor_queue.md`, `revision_flags.md` — status updated
- `inbox/proposals/pending/2026-08-18_hawkins_tbs-plain-language-explainer.md` — new proposal
- `deferred/watch_list.md` — WATCH-002 / WATCH-003 checks recorded
- `master/C2A2_master_wiki.md` — regenerated
- `review/2026-08-18_review.html` — daily review interface

## Pipeline Status

- Assumptions extracted (14a): **870**
- Presumptions surfaced (14b): **823**
- Lit search queue: **1,693 total — 1,454 dispositioned, ~220 still QUEUED** (23 dispositioned today)
- Deferred items watching: **2** (WATCH-002, WATCH-003 — both checked today, count 5, neither condition met)
- Validated premises: **178 unique**
- Revision flags awaiting Tom: **12 new today** (1 CRITICAL, 5 High, 2 Medium-High, rest Medium)
- Systemic risk flags open: **4 new today** (G4 rated HIGH)
- Proposals pending review: **54** — review-pass gap now **10 days** (last decisions file 2026-08-08)

## What's Next

1. **The proposal review backlog is the binding constraint.** 54 pending, no decisions file
   since 08-08. WATCH-003 literally cannot resolve until Tom does a review pass.
2. **G4 recommendation 1 — the blind re-detection audit on the CROSS corpus** is the
   highest-value, cheapest, most informative next action the system has. Sample 20–30 CROSS
   entries stratified by age and tradition pair, strip all C2A2-minted vocabulary from the
   source excerpts, give a fresh detector only the excerpts, ask what the two share. The
   proportion whose convergence survives *is* the artefact rate. Publish it beside the CROSS
   count.
3. **G4 recommendation 2 — own-voice provenance sweep across all 90+ CROSS entries.** Pure
   text matching, runnable immediately, no judgement calls: does the convergent term appear
   in a verbatim source quotation on *both* sides, or only in C2A2 paraphrase?
4. **Fix the Chat→Cowork scrape.** Sign in to claude.ai in Chrome and let the session
   persist; reconnect the Claude-in-Chrome extension side panel. Today was a gap in the
   record and tomorrow will be too if this isn't done.
5. **Retrofit PREMISE-176** — audit existing passes that can delete/retire/overwrite for
   structural reversibility. The two broken regex instruments should be re-run after fixing.

## For Morning Discussion

**1. PRESUMPTION-751 is the most consequential result of the run, and it is reflexive.**
Rated CRITICAL. Kohli (2026), arXiv:2605.29800: nine frontier models from *seven different
families* supply approximately **two independent votes** by Kish effective sample size;
panel accuracy falls 8–22 points short of the independent-voting ideal; the best single
judge matches or beats the panel; no aggregation method recovers more than 11% of the gap.
Kim/Garg/Peng/Garg (ICML 2025): 60% same-wrong-answer coincidence, **rising** with model
capability.

What this means inside C2A2, stated plainly: *"N independent reports agree" is not worth N
votes anywhere it currently appears.* That includes ASSUMPTION-1132's five residue reports
and ASSUMPTION-943's three reviewers. It includes 15a/15b concordance itself. And the
pipeline cannot discharge this finding from inside itself — **your adjudication is the only
decorrelated stream this system has.** Worth thinking about on the walk: is there any way to
get a second genuinely-independent stream that isn't you?

**2. G4's HIGH rating touches the headline number.** 90+ CROSS entries. The honest framing
from the flag itself, recorded for balance: *"the network demonstrably produces
disconfirmations against its own constructs, including three in this very cohort. A system
in the grip of pure confirmation would not do that."* The risk is HIGH because the rate is
unmeasured. Do you want the blind re-detection audit run this week? It's cheap and it would
either substantially clear or substantially indict the CROSS corpus.

**3. G3 names the token budget as a fiction.** "A budget that every run declares and every
run breaches, with disclosure as the only sanction." That's your Rule 6 sitting in a
systemic risk flag as a worked example of normalization of deviance. The literature's
standing remedy is mandatory expiry + non-automatic renewal + escalating approver seniority.
Do you want an actual enforcement mechanism, or do you want to formally downgrade the budget
to a target and stop calling it a budget?

**4. The review backlog needs a decision, not a nudge.** 54 pending / 10 days. Either block
a session for it, or change the intake rate. PROP-2026-08-18-001 is a good test case — it
argues *against itself* in its own body ("a reviewer who wants nothing but new sources should
deny this in five seconds"), which suggests the proposal agents could pre-filter more
aggressively.

**5. Small one:** ASSUMPTION-1129's regex bug (bound only the head id after a tradition name,
so every trailing id in an enumerated citation read as absent) means some prior "absent
citation" findings were false. Worth knowing how far back that instrument ran.

---

### Delivery status — **FAILED. Read this file directly.**

Browser delivery to the daily-walk Chat conversation did **not** happen. Sequence:

1. `claude-in-chrome` extension MCP — **not connected**, two consecutive attempts.
2. Fell back to the `Control_Chrome` connector. It accepted an `open_url` for
   `https://claude.ai/recents`, but the follow-up page read returned
   **"Google Chrome is not running."** Chrome is closed on the machine right now.
3. Even with Chrome running, this morning's inbound scrape established that the Chrome
   profile is **signed out of claude.ai** (`/recents` → `/login?from=logout`), and signing
   in is out of scope for an automated run. The fallback connector also lacks the
   text-input tools needed to compose a Chat message.

**Both directions of the Chat↔Cowork sync are now down.** This is the second consecutive
failure today (morning inbound also failed). To restore before tomorrow's runs:

- Leave Chrome running.
- Sign in to claude.ai in that Chrome profile and let the session persist.
- Reconnect the Claude in Chrome extension (side panel → sign in, same account as the
  desktop app). Both sync skills are written against that connector, not the fallback.
