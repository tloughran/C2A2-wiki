# Voice-guide FAQ: finishing the key migration

**Status 2026-08-28:** blocked on 12 unwritten knowledge files. 27 pairs authored and
validated; publication correctly refused. Nothing shipped.

## What is wrong right now

`wiki/voice_guide_faq.json` was generated **2026-07-18** and is fetched live by
`explorer.html` (`loadFaq()`, line ~1970) as the guide's first-pass source. On
**2026-07-22** `bd33ef7` re-keyed features from per-tab filenames to per-affordance
`state_key`s and made `wiki/voice_guide/knowledge/` the canonical source. The FAQ was
never regenerated. It has been five weeks.

`voice_faq.py scan` reads: **7 new, 14 removed, 0 unchanged.** Nothing in the published
file corresponds to anything in the inventory.

### The guide is serving claims its own architecture forbids

`00_project.md` and `sociogram.graph.default.md` both say: never state a node or edge
count as current fact, and name the legacy "1,600+" string specifically. The shipped FAQ
answers **"Over sixteen hundred, one for each wiki article"** to *How many nodes are in
the Sociogram?*, and repeats it inside *What is the Sociogram?*. `what_is_c2a2.default.md`
forbids quoting a total for the framings; four Start Here answers assert "the fifteen
angles". **Six of the sixteen movable pairs assert something the knowledge files were
written to stop.** They are live today.

## What was done 2026-08-28

`wiki/voice_guide/qa_migration_2026-08-28.json` -- 27 pairs across all 7 canonical keys:

| state_key | pairs | provenance |
|---|---|---|
| `start_here.default` | 4 | 1 verbatim from `start_here.html`, 3 rewritten to drop the total |
| `sociogram.graph.default` | 8 | 6 verbatim from `wiki_narration.html`, 2 rewritten to drop the count |
| `sociogram.graph.node_selected` | 3 | 1 re-keyed from `wiki_narration.html`, 2 authored from the knowledge file |
| `what_is_c2a2.default` | 3 | 1 rewritten from `start_here.html`, 2 authored |
| `00_project` | 3 | authored from the knowledge file |
| `sociogram.graph.edge_selected` | 3 | authored from the knowledge file |
| `what_is_saying.default` | 3 | authored from the knowledge file |

Every authored pair comes from its knowledge file's own **Answerable questions** section
and respects its **Must not claim** list, including the locked vocabulary
(trans-agentic, AI contributors, constitutional arrangements; card 3 says *flourish*).
No total is quoted anywhere.

`merge --dry-run` passes validation and then correctly **REFUSES** to publish.

## The blocker

`merge` rebuilds the published file by iterating the inventory, so any key not in
`knowledge/` is dropped. The guard from `b38c469` refuses that. Of the 14 legacy keys,
**2 are now re-homed** (16 pairs) and **12 have no knowledge file**, holding 86 pairs:

| legacy key | pairs | knowledge file needed |
|---|---|---|
| `community_explorer.html` | 8 | `community_explorer.default.md` |
| `physics_explorer.html` | 8 | `physics_explorer.default.md` |
| `community_interactions.html` | 7 | `community_interactions.default.md` |
| `prs_3d.html` | 7 | `prs_3d.default.md` (+ selected states?) |
| `agents_tab.html` | 7 | `agents_tab.default.md` |
| `metabolism/metabolism_view.html` | 7 | `metabolism.default.md` |
| `summa_explorer.html` | 7 | `summa_explorer.default.md` |
| `interT_study.html` | 7 | `inter_tradition_study.default.md` |
| `rc_document_explorer.html` | 7 | `rc_document_explorer.default.md` |
| `commentary-explorer/commentary_explorer.html` | 7 | `trv_commentary.default.md` |
| `heartbeat/index.html` | 7 | `heartbeat.default.md` |
| `community/index.html` | 7 | `community_cards.default.md` |

Two legacy pairs have no home even in principle and are not carried forward: *What are
the review cards?* (`review_log.html`) and *Is Start Here different from the Community
Explorer?* -- both need their target page to gain a knowledge file first.

## Acceptance test

`python3 scripts/voice_faq.py merge <qa.json>` completes **without `--allow-drop`**.
That is the whole test. Passing `--allow-drop` today would ship 27 good pairs and delete
86, stripping the guide of every answer it has for twelve tabs -- a coverage regression
far larger than the six bad claims it would fix.

Do not hand-edit `wiki/voice_guide_faq.json`. It is generated.
