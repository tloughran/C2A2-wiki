# Chat Summary — 2026-10-05
*Scraped 2026-10-05 from Chat "Morning greeting" (last activity ~15 h before scrape, i.e. evening of 2026-10-04). No walk conversation dated today existed yet.*

> **Run notes (fail-loud):**
> - This file replaces an earlier 2026-10-05 stub that recorded a failed run (Chrome extension unreachable). That earlier firing suggests this task is also registered twice — same pattern as the duplicate-schedule issue below.
> - Only the tail of the conversation was captured; "Load earlier messages" did not expand the text. The morning portion was presumably covered by `2026-10-04_chat_summary.md`.

## Key Discussion Points
- **Six universal layers** for C2A2 Explorers, all sitting on a shared **manifest**: search, subscriptions, explainer videos, explanatory documents (split out from videos), data export, and the voice guide. The arXiv paper is separate, not a layer. Tom confirmed this enumeration.
- **Where the manifest work belongs:** Chat advised Code or Cowork (repo access), with findings filed to **memory**, the only cross-surface channel Chat could verify. Chat could *not* confirm that Cowork/Code sessions show up in its conversation search.
- **Evening Cowork→Chat sync (10-04) was then discussed in the same thread**; Chat's reply changes the plan (see below).

## Planning Notes & Priorities
- Plan has changed: **the manifest already exists** (`voice_guide/manifests.json`, 9 of 24 surfaces). The job is now to *extend* it (identity layer first) rather than reverse-engineer a new schema.
- Surface count is **24**, about double the morning assumption.
- Chat's suggested sequence for today:
  1. Decide which duplicate sewing-agent registration to kill.
  2. Check the Cowork desktop app for a **local** lit-pipeline schedule (likely source of the second instance).
  3. Give Cowork the go-ahead on **Step 1** (unify key namespace; generate the six page tables from the manifest), schema revisions **R1–R8**, and the **three live defects**.

## Open Questions
- **Sewing agent double-fire:** "c2a2 wiki bootstrap audit" (Sun 4:00) vs "sewing agent weekly" (Sun 4:30). Distinct modes or straight duplicate? Chat couldn't see prompts.
- **Lit pipeline duplicate:** only one cloud registration (0:30 daily); the second is probably local to Cowork desktop.
- **Other possible overlaps:** "System health check" (noon UTC, May) vs "Morning system health" (6:00, Sept); "Morning brief" (weekdays noon UTC) vs "Morning project status" (8:00 daily). "Live dashboard refresh" last ran as *abandoned* on 10-02.
- **McGilchrist Think Spiral vs MacIntyre's critique of liberalism** for the ISME paper: left as a content call for Tom.

## C2A2-Specific Items
- **Re-sequencing:** Chat agrees: identity for all 24 surfaces first, with capability filled in per surface as each layer is wired. The 23% unknown leaf values (337/1,494) are a coverage fact, not a blocker, *provided the gate distinguishes "unknown" from "absent."*
- **Intent placement:** keep intent in the manifest under its own key; the coverage gate counts **observed** capability only. The FIND_TABS slip is the argument for keeping declared / observed / intent separate.
- **Live defects to fix:** KNOWLEDGE basename collision; `destinations.json` stale since 07-23 and missing `rc_sandbox`; a blind `derive_tab_help` gate.
- **Levin cards:** hold at Speculative (built without primary text). Chat agreed.
- **Rohr/Wright** empire/violence vs divine-reign convergence is in `wright_rohr_bridge.md`.
- Artefacts from 10-04 (not yet live): `voice_guide/manifests.v2.json`, `scripts/generate_page_tables.py`.

## Action Items Mentioned
- [ ] Tom: choose which sewing-agent registration to delete (Chat offered to delete it on his say-so).
- [ ] Tom/Cowork: find and remove the local duplicate lit-pipeline schedule.
- [ ] Cowork: Step 1 (unify key namespace, generate the six tables from the manifest), pending Tom's go-ahead.
- [ ] Cowork: apply schema revisions R1–R8.
- [ ] Cowork: fix the three live defects.
- [ ] Cowork: process the 6 still-orphaned sewing cards.
- [ ] File manifest findings into **memory** so Chat can see them.

## Context for Cowork
- Chat updated memory under "C2A2 Explorer Directions" with the six-layer/manifest framing.
- Treat memory as the reliable Chat↔Cowork channel. Chat's ability to search Cowork transcripts is unverified.
- Step 1 and the other build items are proposed, **not approved**. Wait for Tom's explicit go-ahead before changing live files.
- No new DECISION IDs were logged (last is DECISION-083; last OPEN is OPEN-263).
