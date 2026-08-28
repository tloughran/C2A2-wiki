---
title: Referencing & Linking Foundation — Summa 2026 Commentary
updated: 2026-07-17
status: foundation AGREED 2026-07-17 (§8 resolved); CANONICAL home = this file (RC Karpathy Wiki Project); pointer stub left in the Summa vault refs/
governs: the apparatus-builder pass (runs here, where the wiki lives) and the Summa QC agent's citation-integrity frame
relates_to: "Summa vault Summa.md (The QC agent)", "wiki/ACPA_2026_references.md", "wiki/master/prs_pub_years.json", "[[Proposed QC citation-integrity inserts]]"
---

# Referencing & Linking Foundation

The standard the Summa 2026 corpus references against, so it can become a **citation-integral** body of work — one that exports to a standalone commentary (e.g. for ND University Press) with no orphaned, drifting, or fabricated citation, and no leakage of the project's internal sourcing guidance into print.

A *design contract*, not code and not a constitution change. The apparatus-builder implements it; the Summa QC agent verifies against it.

## 0. Cross-project topology (why this lives here)

Two projects, one apparatus:

- **RC Karpathy Wiki Project (here)** owns the **canonical bibliography** and the **builder**, because the 15 thinkers' source data lives here (`wiki/traditions/<tag>/`, `wiki/master/`) and this mount is reliable. Publication assembly (endnotes + Works Cited) also happens here, alongside `wiki/commentary-explorer`.
- **Summa 2026 vault** owns the 307 authored pairs and the **QC citation-integrity frame**, which reads the canonical `works_cited.json` from this project when the mount is present and **defers gracefully when absent** (the `ids-deferred` pattern, §6.2) — so QC never hard-depends on the flaky cross-mount.
- The **harvester** (§7 step 2) needs *both* mounts: it reads Summa `synthesis/` bodies and writes the reference-master index here.

## 1. The three-layer principle

One canonical source, two derived views. Never author a citation twice.

1. **Canonical layer — the bibliography (source of truth):** `commentary-apparatus/works_cited.json` (→ rendered `Works cited.md`). Nothing else stores bibliographic fact.
2. **Vault layer — Obsidian links:** `[[traditions/levin/prs_triplets]]` and the auto-linker footer are *navigation*; they stay wikilinks, not publication citations.
3. **Publication layer — endnotes + Works Cited (Appendix 1):** generated at export time from layer 1; not injected into synthesis bodies.

The failure this prevents: 279 Wright mentions, 266 Rohr, 210 Levin, each hand-citing slightly differently across 307 files. One canonical entry per work makes drift structurally impossible.

## 2. The canonical bibliography

**Storage** (mirrors the existing `refs/summa_index.json` + `build_index.py` precedent in the Summa vault):

- `commentary-apparatus/works_cited.json` — machine source of truth.
- `commentary-apparatus/Works cited.md` — human-readable table, *generated* from the JSON, never hand-edited.

**Per-work fields:** `cite_key`, `thinker` (roster tag), `authors`, `title`, `container`, `year`, `publisher`, `locator` (pages/DOI/URL/talk-timestamp), `work_type` (`book|article|chapter|talk|preprint`), `canonical` (bool — designated canonical work per the oracle/guardrail memories), `verified` (bool — a human has confirmed the detail against the source).

**Cite-key convention:** `surname-year-shortslug`, lowercase ASCII, hyphen-minus only. E.g. `levin-2019-computational-boundary`, `hoffman-2019-case-against-reality`, `kastrup-2019-idea-of-the-world`, `wright-2003-resurrection-son-of-god`, `rohr-2019-universal-christ`, `macintyre-1981-after-virtue`. First-author key; collisions get `-a`, `-b`.

**Seed inputs already present in this project** (absorb, don't re-author):

- `wiki/ACPA_2026_references.md` — a Chicago-style bibliography Tom already wrote (MacIntyre's three core works, Kuhn, Aquinas, et al., correctly formatted). Confirms Chicago as house style; import its entries directly.
- `wiki/master/prs_pub_years.json` — publication year/date per `<thinker>-PRS-NN`; supplies the `year` field for every PRS-linked work.
- `wiki/traditions/<tag>/wiki.md` + `prs_triplets.md` — each thinker's canonical works and PRS records (all 15 tags present, incl. `loughran`, `macintyre`).

## 3. The thinker roster (resolved — all 15)

The 11 C2A2 traditions — `levin`, `friston`, `hoffman`, `hawkins`, `mcgilchrist`, `fredrickson`, `carroll`, `arkanihamed`, `wolfram`, `kastrup`, `stump` — plus `wright`, `rohr`, **`loughran`** (author of the PRS form), **`macintyre`** (tradition-rationality bridge). All 15 have `wiki/traditions/<tag>/` folders here and get first-class bibliography entries; the harvester scans for all 15 surnames.

`loughran`'s entries are the **PRS-form scaffolding itself** (the PRS / Synergistic-Coil source): a PRS-id endnote resolves to Loughran as author of the *form*, distinct from the underlying thinker work it re-describes. `macintyre`'s entries are his own works (per `ACPA_2026_references.md`: *After Virtue* 1981, *Whose Justice? Which Rationality?* 1988, *Three Rival Versions of Moral Enquiry* 1990).

## 4. In-text conventions the builder honors

- **Specific-claim mentions** resolve to the cite-key of the grounding work → endnote at export.
- **Generic mentions** ("as Levin argues") with no specific work resolve to that thinker's `canonical` default and are **flagged for human confirmation** — never silently pinned.
- **PRS / CROSS / FLAG ids** map to the wiki node *and*, where the id encodes a published claim, to the underlying work's cite-key. The endnote cites **Loughran's PRS-form re-description + the underlying thinker work** — never the thinker as author of the PRS.
- **Verbatim quotations** (Scripture, *Catechism*, council/magisterial texts, a thinker's published line) must carry a cite-key to a canonical source.

## 5. Publication apparatus (export-time only)

- **Manuscript scope:** the standalone commentary reproduces **only the commentary half** plus **direct *Summa* citations** (Part / Question / Article). Transcripts are *not* reproduced in print; they remain the in-vault fidelity anchor.
- **Endnotes:** emitted by the build step from the reconciled harvest, **Chicago notes-bibliography** style, **day-agnostic, restarting per *Summa* Part** — Prima Pars, Prima Secundae, Secunda Secundae, Tertia Pars, Supplement — as the "chapter" unit. Not written back into vault bodies.
- **Appendix 1 — Works Cited:** auto-generated, filtered to cite-keys actually referenced, Chicago notes-bibliography.
- **Internal-notes stripping (hard requirement):** export **removes** the footer YAML sourcing notes — bracketed role-classifications like `[Wright primary on Christology]`, `[Levin/Hoffman/Kastrup lead per the guardrail]`, the `evidence_strength_summary` field, and internal `karpathy_wiki_sources` annotations. These are internal sourcing guidance and must never reach a reader. QC verifies the export is clean (§6.4).

## 6. The QC citation-integrity frame (new — verify only, never generate)

Added to the Summa QC sweep's synthesis-sense frame. It **flags/escalates**, never invents. Per reviewed pair:

1. **Surname resolution.** Every roster surname (15) in the *body* resolves to ≥1 cite-key in `works_cited.json`, else flag `no canonical work registered for <thinker>`.
2. **Id resolution.** Every `PRS-NN` / `CROSS-NN` / `FLAG-NN` / `FINDING-NNN` resolves to a real wiki node when this project is mounted; when absent, record **`ids-deferred (wiki mount absent)`** and re-queue — do not count fully clean. (Replaces today's ad-hoc "PRS-ids unverified" note.)
3. **Banned possessive form.** No `X's PRS-NN` in body or footer (`wiki's PRS-NN` allowed).
4. **No internal role-classification in the body.** "primary on", "the lead", "as counterpoint", "NOT the metaphysical lead", etc. must not appear in prose (footer exempt — internal record, stripped at export).
5. **Quote verification (character-for-character).** Every verbatim block quote carries a resolvable cite-key and matches its canonical source exactly. Scripture (cited translation), *Catechism* (paragraph), council/magisterial texts, and Aquinas (article) verified each sweep; a mismatch is fixed from source and logged in the transcript's typo-cleanup blockquote. A thinker's published line is checked when the source is retrievable, else marked `quote-unverified (source not retrievable)` — never asserted verified without the source.

Output: a per-pair `citation_integrity` sub-block, plus `last_citation_qc_at` / `last_citation_qc_outcome` (`pass|flag|deferred`) tracked independently of sense/fidelity state.

## 7. Build order (the apparatus pass — runs here, not in the QC loop)

1. **Seed `works_cited.json`:** import `wiki/ACPA_2026_references.md`; join `wiki/master/prs_pub_years.json` for years; extract canonical works from each `wiki/traditions/<tag>/wiki.md`. All 15 seedable from this project now (no external mount needed).
2. **Harvest (deterministic, code — Rule 5):** grep the 15 surnames + `PRS-\d+` / `CROSS-\d+` / `FLAG-\d+` / `FINDING-\d+` across the Summa vault's `synthesis/` bodies → `commentary-apparatus/Reference master.md`: per-thinker occurrence index of `{day, claim snippet, ids, resolved cite_key}`. **This is the "reference master page."** *Needs both mounts.*
3. **Reconcile (model judgment only where ambiguous):** pin generic mentions; human-confirm the flagged ones.
4. **Build:** emit endnotes + Appendix 1 from the reconciled data, with footer-stripping (§5).
5. **QC verifies** each Summa pair against §6 on its normal sweep.

Steps 1–4 are a one-time corpus batch + incremental top-up, deliberately *not* in the every-4-hours QC loop (token budget).

## 8. Decisions (resolved 2026-07-17 by Tom)

1. **Roster — all 15**, all first-class bibliography entries (§3).
2. **Style — Chicago notes-bibliography** (already Tom's practice in `ACPA_2026_references.md`).
3. **Endnotes — day-agnostic, restart per *Summa* Part** (the five Parts are the chapter units).
4. **Manuscript scope — commentary half + direct *Summa* citations only**; transcripts not reproduced.
5. **Quote-verification — character-for-character**, with the retrievability caveat for thinker quotes (§6.5).

## 9. Staged changes (after sign-off — signed off 2026-07-17)

- **Summa `Summa.md` "The QC agent" section:** add the §6 citation-integrity frame. Constitution edit — **Tom applies it** (the QC agent does not self-edit `Summa.md`). Insert text in `Proposed QC citation-integrity inserts.md` Part A.
- **Scheduled QC task SKILL.md:** add Step 3c mirroring §6 + the new `mark` fields. Part B; install over the scheduled task.
- **`qc_sweep.py` support:** Part C (new `--citation-*` flags + re-queue logic) before the frame can *gate* rather than report.

Rollout: the frame ships **report-only** (findings in the `mark --note`) for one sweep cycle, then flips to gating once `works_cited.json` exists and Part C lands. Applying Parts A/B now is safe — they gate nothing without `works_cited.json`.
