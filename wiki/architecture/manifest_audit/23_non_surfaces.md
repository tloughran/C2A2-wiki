# Build inputs, orphans, stale and dead

Eleven tracked HTML files that are not live user surfaces, plus two untracked
candidates that confuse the roster. Recorded so that the manifest's `status`
field has something true to say on day one, and so the published tree can be
trimmed.

"How reached" was determined by grepping each filename across `wiki/**/*.html`
and `scripts/`.

## Build inputs — live, but never served

| path | size | role |
|---|---|---|
| `wiki/study_shell.html` | 13.6 KB | The template `scripts/build_study.py` substitutes `__TAB_BUTTONS__` and `__DOC_BLOCKS__` into (`:29, 64-65`) to produce `interT_study.html`. **Edit this, not the output**: a hand-edit of the output is overwritten and fails `--check`. Opened directly it shows placeholder text and no documents. Its `#help` modal prose is the best narration seed for the Inter-Tradition Study. |
| `wiki/c2a2-prs-3d/template_prs_3d.html` | 216 KB | The template input to `c2a2-prs-3d/scripts/generate_prs_3d.py:14`, used by `scripts/regen_prs_connectome.sh:25`, `publish_prs_connectome.sh:42` and `check_scheduler_health.py:174`. **The generator is not idempotent** and must never be run against the built page (`assumptions.md:3409`, `SPEC_prs_time_axis_2026-08-27.md:104`). |

Both are published (tracked) and shouldn't be. `status: build_input` in the
manifest, and ideally a `.nojekyll`-adjacent exclusion.

## Live but reachable only by typed URL or a new window

| path | size | how reached |
|---|---|---|
| `wiki/architecture/lowlevel_architecture.html` | 40 KB | `what_is_c2a2.html:665`, `target="_blank"`. Described in `site_guide.html:261`, which is itself orphaned. **Because it is `_blank`, the voice guide structurally cannot follow it** — the manifest's `controls_excluded` records exactly this. |
| `wiki/architecture/ecosystem_diagram.html` | 20 KB | **Orphaned in practice.** The only mention is plain text inside `lowlevel_architecture.html:255` ("ecosystem_diagram ←new"). Its commit message says it was meant to be linked from the what_is_c2a2 Tech appendix; `what_is_c2a2.html:665` links only its sibling. Real content, committed 2026-06-26, reachable only by URL. **Cheapest fix in the audit: add the missing link.** |

## Stale

| path | size | why |
|---|---|---|
| `wiki/master/C2A2_master_wiki.html` | 34 KB | Orphaned — no reference to the `.html` anywhere in `wiki/` or `scripts/`; only the `.md` twin is referenced (`reference_master.json:8788`, `agents/openstory/agent_node_edges.json:7951`). Last commit 2026-04-08, light theme, never regenerated. `STATE_OF_PROJECT_2026-05-08.md:61,77` already flags the dual `.md`/`.html` format and asks to pick one. |
| `wiki/architecture/metrics/prs_created_vs_delivered.html` | 4.8 KB | A generated June 2026 snapshot; the only writer is the default `--out` of `wiki/architecture/metrics/prs_yield_histogram.py:42`, and no scheduled caller was found in `scripts/*.sh` or `scripts/*.py`. |
| `wiki/inbox/Resurrecting Civility — Document Explorer.html` | 1.88 MB | The initial-commit (2026-04-07) original of the live RC Document Explorer, untouched since. **Not diffed** against `rc_document_explorer.html` (1.76 MB), so "original" is inferred from names, dates and sizes. |
| `wiki/inbox/rc_sandbox/quodlibet_notebook.html` | 1.67 MB | Last commit 2026-09-05; `rc_sandbox_notebook.html` (1.78 MB, 2026-09-22) is newer and is what the shell loads. The changelog for 2026-09-04 records this file as the first browsable version. **Not diffed.** `explorer.html:1937` keeps "quodlibet notebook" as a spoken alias for the live page, so the name is still in use for something else — a live confusion a manifest `aka` field would resolve. |

Together the two inbox duplicates are **3.55 MB of published dead weight** whose
only function is to be mistaken for the live page.

## Dead

| path | size | why |
|---|---|---|
| `wiki/site_guide.html` | 26.7 KB | Orphaned — nothing in `wiki/*.html` or `scripts/` links it. `explorer.html:561` comment: "No Site-Guide chapter tab exists (site_guide.html documents a phantom one"; the `chap-guide` lookup is null-safe and resolves to null. `fact_inventory.md:109,113`: "largely counterfactual". A 27 KB published document describing a chapter tab that does not exist, with `<details>` sections labelled written / planned / drafting. **If it were opened in the frame, `activeManifest()` would return null and the shell would fall back to generic caps.** |
| `wiki/prs_3d_debug.html` | 194 KB | Orphaned; title is the old "3D PRS Landscape", superseded by `prs_3d.html` ("Narrative (PRS) Connectome"). Last commit 2026-05-11. `SESSION_SUMMARY_2026-08-27.md:124` already says "untrack wiki/prs_3d_debug.html". |
| `wiki/test_load.html` | 6.8 KB | A node-array loading fixture — `<script>var N = [{"id":"…","group":"test"}…`. Zero inbound references. Last commit 2026-05-11 (a bulk sync). `status: test_fixture`. |

## Untracked, but roster-confusing

- `physics_explorer_candidate_2026-04-02.html` (185,548 B, "75 concepts / 6
  physicists / PRS") and `physics_explorer_candidate_2026-05-01.html`
  (254,632 B, "48 concepts") at repo root. Superseded, unreferenced, not
  published. Their existence is the evidence that Physics Explorer changes by
  whole-corpus expansion (see `09_physics_explorer.md`).
- `C2A2_Heartbeat_Explorer_Update_20260617_bundle/` and the matching `.zip`
  (41,560 B) at repo root — a superseded install bundle whose own
  `INTEGRATION.md:3` says "Do NOT apply" explorer.html.
- ~100 untracked review pages under `wiki/review/` in `_superseded/`, `_trash/`,
  `_deleted_quarantine/`, `.stale_review_pages/`, plus `2026-10-01..04_review.html`.
  Correctly unpublished; only the assembled `review_log.html` is tracked.
- `wiki/architecture/` also holds 9 `.fuse_hidden*` files (~6 MB total) and
  several hundred `assumptions.md.bak.*` files. Not HTML, but they are why
  enumerating that directory takes 746 entries to find 3 pages.

## Summary of the trim

Cutting the three dead files, the two inbox duplicates and the stale master wiki
removes **~4.1 MB** from the published tree and six names from the roster, none of
which any live page references. Moving the two build inputs out of the published
path removes two more. None of this is architecture — but it is what makes
`status` a field with content rather than a field everyone leaves blank.
