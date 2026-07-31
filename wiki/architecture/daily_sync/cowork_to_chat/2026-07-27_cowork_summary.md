# Cowork Progress Summary — 2026-07-27
*Generated at 18:40 EDT for daily walk Chat context*

> **⚠️ READ ITEM 1 FIRST. The `generate_review_page.py` bug fired again today, and this time it is not benign.** Today's `review/2026-07-27_review.html` will write **12 phantom dispositions and lose all 12 real ones** if submitted. Details below.

> **DELIVERY FAILED — read this file directly.** At 18:40 EDT **both** connected Chrome browsers were signed out of claude.ai. Browser 1 (`97286349…`) and Browser 2 (`42c9fd50…`) each redirected `/recents` → `/logout`. This is the **fifth consecutive failed sync** (07-25 evening, 07-26 morning, 07-26 evening, 07-27 morning, 07-27 evening), same root cause every time. An autonomous agent may not sign in, so this summary was **not** delivered to the daily-walk Chat. Fix in item 5.

## What Was Accomplished Today
Monday — again **entirely automated-pipeline work**. No interactive Cowork session logged a changelog or decisions entry (decisions.md still ends at DECISION-078 / 2026-07-05; open_questions.md still ends at OPEN-139 / 2026-07-23). Today's 07-27 changelog + metrics snapshot write at the ~23:40 EOD run.

- **Lit-search pipeline (15a/15b/15c):** dispositioned **PRESUMPTION-551, 553, 554, 555, 556** — FOR and AGAINST files written for each. Batch mix: **1 INCORPORATE → PREMISE-129**, 4 MONITOR (MONITOR-483…486), 0 REVISE. Running totals: **PREMISE → 129 · MONITOR → 486 · REVISE → 246 (unchanged) · DISPOSITION → 539.**
  - **PREMISE-129:** a formal-identity claim is settled by proof/derivation, not by an agent's stated verdict — attach a checker. Notably, it was INCORPORATED *because* it names an external referent (proof theory + the empirical LLM-limitation literature).
  - **The batch turned the pipeline's reflexivity screw hard.** MONITOR-486 (from PRESUMPTION-556) states that 14b/15a/15b/15c are the same model on different prompts over one corpus, so an INCORPORATE can record *the pipeline agreeing with itself*. 15c held it at MONITOR rather than INCORPORATE on the grounds that incorporating-from-inside a premise about the pipeline's own untrustworthiness would enact the circularity it warns of. It then **applied its own discipline within the same batch**: PREMISE-129 cleared INCORPORATE because it cites an external referent; sibling PRESUMPTION-554 was held at MONITOR-485 partly for lacking one. Audit result recorded: PREMISE-127 (Gentner et al.), -128 (Meta/Synopsys), -129 (proof theory) all do cite external referents.
  - **MONITOR-484 formalizes the backlog flag** with queueing theory: arrivals > 0 with service rate 0 is an unbounded, unstable queue (Little's Law). Observed 110 → 147 → ~174 unconsumed, consumption 0 since 2026-07-08. Reinforces REVISE-245.
  - **MONITOR-483** extends PREMISE-127 to generation scale: a bridge file certifies authorship, not that the homology holds. Auto-bridges enter `synthesis/` with no validation-status field.

- **Four new proposals surfaced — a strong Levin/Friston day, and two of them are directly load-bearing on the project's own framing:**
  - `PROP-2026-07-27-001` **Levin, "Alignment Is to a Virtual Governor"** (Lyons, Pio-Lopez & Levin, preprint 2026-07-03) — alignment in decentralized systems is always alignment *to a virtual governor*: an abstract governing entity, not a physical object, embodied in the coordinating relationships among agents and causally instructive. Spans development, markets, and AI.
  - `PROP-2026-07-27-002` **Levin, "Intelligence from Learnable Novelty"** (Zhang & Levin, arXiv 2607.18433) — diagnoses novelty search ("transfixed by a noisy television") and the FEP ("most content in a dark room") as **the same root error**, both conflating convertible surprise with unconvertible surprise. Proposes *learnable novelty* as the single underlying quantity.
  - `PROP-2026-07-27-003` **Levin, "From Development to Cognitive Glue"** (*Bioelectricity* 8:2) — Levin's own canonical programmatic self-summary; a landmark anchor node the wiki has only held via secondary sources.
  - `PROP-2026-07-27-004` **Friston, "Self-orthogonalizing attractor neural networks emerging from the FEP"** (Spisak & Friston, arXiv 2505.22749; *Neurocomputing* 2026) — Hopfield/Boltzmann dynamics *derived from* the FEP rather than posited; orthogonal-basis formation, sequence learning, resistance to catastrophic forgetting.

- **Agent 16 (deferred/watch monitor):** steady-state, ran 1 day early of the due date. 2 items WATCHING (WATCH-002 Wright, WATCH-003 Rohr), **both fall due tomorrow, 2026-07-28** — their first re-check since intake. All three intake channels clean.

- **Telemetry refresh:** `agents/openstory/` PASS at 10:28Z — 33 agents, 27 nodes, DB age 0h. `metabolism/` view + data regenerated.

- **Morning Chat→Cowork sync: FAILED** — claude.ai signed out in the reachable Chrome; no fresh Chat context captured for 07-27.

## Key Decisions Made
None. No new DECISION-NNN entries.

## New Open Questions
None formally logged. Two candidates from today's batch worth adopting:
1. Does the C2A2 pipeline need a **standing policy that every INCORPORATE must name an external referent**? MONITOR-486 says a decorrelated spot-check (Tom, a human, or a different model) is exactly what would let it close and fold into PREMISE-124 enforcement. This is a policy Tom could adopt in one sentence.
2. Is **learnable novelty** (Levin, PROP-...-002) the quantitative handle on "progress" the program has been missing — neither pure exploration nor pure surprise-minimization? It is a substrate-independent metric aimed squarely at the thing PRS triplets try to track.

## Files Created or Modified
- `inbox/proposals/pending/2026-07-27_{levin_alignment-virtual-governor, levin_intelligence-from-learnable-novelty, levin_cognitive-glue-journey, friston_self-orthogonalizing-attractor-networks}.md` (4 new)
- `architecture/lit_search_results/{for,against}/PRESUMPTION-{551,553,554,555,556}_*.md` (10 new files)
- `architecture/validated_premises.md` (PREMISE-129), `lit_search_returns.md` (DISPOSITION-535…539), `for_lit_search.md`, `monitor_queue.md` (MONITOR-483…486)
- `review/2026-07-27_review.html` (**defective — see item 1**), `review_log.html`
- `deferred/watch_list.md` (Agent 16 run log), `master/C2A2_master_wiki.md`, `agents_tab.html`
- `metabolism/metabolism_{view.html,data.json}`, `agents/openstory/{agent_telemetry.json, agent_node_edges.json, REFRESH_STATUS.md}`
- `architecture/daily_sync/chat_to_cowork/2026-07-27_chat_summary.md` (records the morning sync failure)

## Pipeline Status
- Assumptions extracted: ~1,450 (unchanged; no new extraction run)
- Presumptions surfaced: **556** (max ID in queue)
- Lit search queue: dispositioned through **PRESUMPTION-556**; DISPOSITION count → **539**
- Validated premises: **129 cumulative INCORPORATE** (PREMISE-129 added today)
- Monitor queue: **486** items; ~174+ unconsumed (backlog flag standing, zero consumption since 2026-07-08)
- Deferred items watching: **2** (WATCH-002, WATCH-003 — **both due tomorrow, 2026-07-28**)
- Proposals pending Tom's review: **16** (2× 07-21, 5× 07-22, 1× 07-24, 1× 07-25, 3× 07-26, 4× 07-27)
- Connectivity (2026-07-26 row, latest): 3,667 total / 2,943 orphan / 57 connected — curated figure excluding machine dumps: ~1,602 / ~878

## What's Next
- **Fix `generate_review_page.py` before touching the review page.** 16 items are queued behind it and today's page is actively dangerous (item 1).
- **Tomorrow (07-28): both watch items fall due** — WATCH-002 (Wright episode content availability), WATCH-003 (Rohr disposition recorded). First re-check since intake.
- EOD run (~23:40) writes the 07-27 changelog + metrics snapshot.

## For Morning Discussion

**1. The review-tool bug fired a third time, and today's manifestation is the bad one. This is the single most important item.**
Today's `review/2026-07-27_review.html` renders **16 correct cards** — DOM ids run `PROP-2026-07-21-001` through `PROP-2026-07-27-002`, matching the 16 real pending proposals. But `submitDecisions()` at line 1055 carries a hardcoded array:

```
const pids = ['PROP-2026-07-27-001', ... , 'PROP-2026-07-27-016'];
```

Sixteen *sequential* IDs, all datestamped today. Only **four** of those exist. So if you work that page and submit:
- **12 phantom dispositions** get written against `PROP-2026-07-27-005` … `-016`, which do not exist;
- **all 12 real older proposals** (07-21 through 07-26 — including the two Hoffman Trace papers, the Carroll AMA, and both Scripture proposals) get **no recorded disposition at all**;
- and the tool **reports success**. No error, plausible-looking output.

This is precisely the class PREMISE-128 named yesterday, and it is now *demonstrated with mismatched IDs*, not merely padded ones. The 07-23 manifestation (7 phantom NO-OP APPROVEs against 2 real cards) was benign because the phantoms were no-ops and the reals were correct. **Today's is not benign: the mapping itself is wrong.** It is also the exact mechanism that plausibly dropped PROP-2026-07-19-001 and -003 on 07-20 (→ WATCH-002/003), which strengthens that read considerably.

*Recommended:* do not open that page. Fix the generator to emit pids from the actual card set, add a reconciliation assertion that recomputes decision records against the real proposal list and **can fail**, regenerate, then do the review pass. This also finally lets the 07-20 in-house reconciliation run against a trustworthy tool.

**2. Adopt the external-referent rule — it's a one-line policy that closes a HIGH-priority monitor.**
MONITOR-486 says explicitly what would resolve it: either you spot-check INCORPORATED premises against external referents, or a policy is adopted requiring every INCORPORATE to name one. The pipeline already behaved as if the rule existed today (PREMISE-129 in, PRESUMPTION-554 held at MONITOR for lacking a referent). Making it explicit costs a sentence and retires a standing self-exemption worry (REVISE-246 / OPEN-139).

**3. Levin's "learnable novelty" lands directly on the FEP — and on your own bridge work.**
PROP-...-002 argues novelty search and the FEP make *the same* mistake in opposite directions. That is a live, on-the-record Levin↔Friston contact point, arriving the same day as a Friston paper deriving Hopfield/Boltzmann dynamics from the FEP. Combined with the carried `friston_hoffman` question (is a trace kernel Q_A *identical* to a blanket-marginalized generative model?), you now have **two decidable formal questions pointed at the Friston tradition from two directions**. PREMISE-129 tells you how to settle both: proof or derivation with a checker attached, not an agent's verdict.

**4. "Alignment is to a virtual governor" may be the most C2A2-shaped paper of the week.**
Levin's virtual governor — abstract, non-physical, embodied in the coordinating relationships among agents, causally instructive — is close to a formal description of what a *tradition* is in your accelerator/detector architecture. Worth asking whether it belongs as a CROSS entry, and whether the PRS lattice is itself a virtual governor in Levin's sense.

**5. Carried and still unresolved (all need you, none new):**
- The two undisposed 2026-07-19 proposals (INTEGRITY FLAG) — restore or retroactively disposition. Recoverable from `review/2026-07-20_review.html` + live URLs. Now looking much more like tool-caused loss than coincidence, given item 1.
- **The browser sync is still broken, and now it's both browsers.** Previously only Browser 2 was signed out; tonight Browser 1 is too. Sign at least one Chrome into claude.ai and leave it running with the extension connected at scheduled times. Five syncs now lost — meaning Chat has had no Cowork context since 07-24.
- The ~174-item monitor backlog — now formally an unstable queue (MONITOR-484). Point the pipeline at the oldest cohort, bound the queue, or re-scope 15d cadence.
- Metric inflation (6th flag) — exclude `lit_search_results/` + `daily_sync/` from the connectivity metric, or split the CSV.
- Housekeeping: roll `watch_list.md` run log into dated archives (~254 KB, active <2%); delete the `2026-04-21_carroll_singer-mindscape-351.md` tombstone.

---
*Autonomous scheduled run (evening Cowork→Chat sync). The .md file is the primary deliverable; browser delivery status recorded in the header.*
