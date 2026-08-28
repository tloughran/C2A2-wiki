---
title: Annotated Bibliography — Plan / Design Note
updated: 2026-07-17
status: SPEC agreed 2026-07-17 (Tom). Builder NOT started. Slots into foundation §7 after reconcile (step 3), before/with build (step 4).
relates_to: "[[Referencing and linking foundation]]", "works_cited.json", "reference_master.json"
---

# Annotated Bibliography — plan

## Purpose

Every cited work in `works_cited.json` gets a **100–400 word annotation** — a compact scholarly summary of the work *and* of the role it plays in the Summa 2026 commentary. Together these annotations are the **annotated bibliography**: the reader-facing companion to the bare `Works cited.md`, and the scholarly justification for why each source belongs in a Thomistic↔contemporary commentary.

This is a **separate document** from the bibliography and the reference master. It does not replace them; it hangs off the same canonical `cite_key` spine (three-layer principle, foundation §1 — never author bibliographic fact twice).

## Scope

- **One annotation per `cite_key`** in `works_cited.json` (currently 46: 15 roster thinkers' works + Aquinas/Kuhn/Cunningham). If a work is later dropped/merged, its annotation follows.
- **Length: 100–400 words each.** Canonical works (one per thinker) sit at the longer end; secondary works and shared references at the shorter end.
- **Priority order:** the 18 `canonical:true` works first (they anchor each thinker), then the remaining works by body-citation frequency (from `reference_master.json` — Wright/Rohr/Levin/Kastrup/Friston/Stump/Aquinas are the heavily-cited spine).

## What each annotation contains

Two moves, in order:

1. **The work on its own terms** (~half): thesis, method, the specific claim/resource the commentary draws on. For a canonical work, its central argument; for a secondary work, the particular contribution that earns its place.
2. **Its role in the commentary** (~half): how the work functions in the Summa 2026 synthesis — which Aquinas questions/themes it illuminates, what cross-tradition bridge it enables, and (where relevant) its confidence register (empirical / formal / philosophical / contemplative). This is drawn from the work's `reference_master.json` occurrences (days cited, claim snippets) and the thinker's `wiki/traditions/<tag>/wiki.md` summary — NOT re-researched from scratch.

Explicitly **excluded** (foundation §5 internal-notes stripping): no PRS/CROSS/FLAG role-classification jargon, no `karpathy_wiki_sources` footer language, no internal id-strings in reader-facing prose. Annotations are publication-grade.

## Inputs (all already present)

- `works_cited.json` — the spine (cite_key, title, authors, canonical flag).
- `reference_master.json` — per-work occurrence index (days cited, claim snippets, specific-vs-generic) → supplies the "role in the commentary" half.
- `wiki/traditions/<tag>/wiki.md` — each thinker's research-program summary → supplies the "work on its own terms" half.
- The work itself / domain knowledge → thesis and method, where the wiki is thin.

## Output

- `commentary-apparatus/Annotated bibliography.md` — reader-facing, grouped by thinker (roster order, then shared references), each entry = the `Works cited.md` Chicago line + the 100–400 word annotation beneath it.
- Optionally `annotations.json` (keyed by cite_key) as the machine store, with `Annotated bibliography.md` DERIVED from it + `works_cited.json` — same generate-don't-hand-edit discipline as the rest of the apparatus. Decide when the builder starts.

## Generation approach (Rule 5 boundary)

Annotation drafting is **model judgment** (summarization from sources) — legitimately model work, unlike the deterministic harvest. Draft per `cite_key`, grounded in the three inputs above; each annotation is a candidate for Tom's review (mark a lightweight `reviewed` flag per annotation, mirroring `verified` on the bibliography). Do NOT fabricate bibliographic detail — that lives in `works_cited.json` and is already confirmed.

## Where it slots in the build order

Foundation §7 becomes: 1 seed bibliography ✓ → 2 harvest ✓ → 3 reconcile → **3b annotate (this doc)** → 4 build endnotes + Appendix 1. Annotating after reconcile means each annotation's "role in the commentary" reflects the confirmed specific-vs-generic resolutions, not the raw harvest.
