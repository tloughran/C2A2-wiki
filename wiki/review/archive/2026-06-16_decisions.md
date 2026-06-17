# Decisions — 2026-06-16

Decision email: `[C2A2-review-decision] 2026-06-16` (Gmail msg 19ed17d3c013d438), processed on the 2026-06-17 daily run.

All 13 line items were **APPROVED**. The email used position-based IDs (`PROP-2026-06-16-001..013`)
copied from the review page's decision template; these were resolved to each card's stable
`proposal_id` by document/card order in `review/2026-06-16_review.html` (13 cards confirmed).

| Decision-email ID (position) | Resolved stable proposal_id | Tradition | Decision | Action taken |
|---|---|---|---|---|
| PROP-2026-06-16-001 | PROP-2026-06-07-002 | rohr | APPROVE | moved pending→approved, copied to inbox/ |
| PROP-2026-06-16-002 | PROP-2026-06-07-003 | rohr | APPROVE | moved pending→approved, copied to inbox/ |
| PROP-2026-06-16-003 | PROP-2026-06-07-001 | wright | APPROVE | moved pending→approved, copied to inbox/ |
| PROP-2026-06-16-004 | PROP-2026-06-08-001 | levin | APPROVE | **NO-OP** — file already removed to `_pending_dupes_resolved/` (duplicate of 2026-06-01 levin cognitive-glue) before this run |
| PROP-2026-06-16-005 | PROP-2026-06-10-002 | kastrup | APPROVE | moved pending→approved, copied to inbox/ |
| PROP-2026-06-16-006 | PROP-2026-06-10-003 | kastrup | APPROVE | moved pending→approved, copied to inbox/ |
| PROP-2026-06-16-007 | PROP-2026-06-10-001 | mcgilchrist | APPROVE | moved pending→approved, copied to inbox/ |
| PROP-2026-06-16-008 | PROP-2026-06-11-001 | stump | APPROVE | moved pending→approved, copied to inbox/ |
| PROP-2026-06-16-009 | PROP-2026-06-12-001 | carroll | APPROVE | moved pending→approved, copied to inbox/ |
| PROP-2026-06-16-010 | PROP-2026-06-12-002 | carroll | APPROVE | moved pending→approved, copied to inbox/ |
| PROP-2026-06-16-011 | PROP-2026-06-15-003 | friston | APPROVE | moved pending→approved, copied to inbox/ |
| PROP-2026-06-16-012 | PROP-2026-06-15-002 | levin | APPROVE | moved pending→approved, copied to inbox/ |
| PROP-2026-06-16-013 | PROP-2026-06-15-001 | levin | APPROVE | moved pending→approved, copied to inbox/ |

Net: **12 proposals approved and queued for Phase-1 ingestion**; 1 no-op (already de-duped).

## ⚠ FAIL-LOUD — generator ID-scheme mismatch (needs fix)

`tools/generate_review_page.py` is internally inconsistent:
- Card display IDs (line ~116) use each file's **stable** `proposal_id` (e.g. `PROP-2026-06-07-002`).
- The "copy decisions" JS template (line ~304) emits **position-based** run-date IDs
  (`PROP-{run_date}-{i+1:03d}` → `PROP-2026-06-16-001..013`).

Tom copied the position-based list, so the Phase-0 lookup strategy (Step 1 grep on
`prop_id:`/`proposal_id:`, Step 2 filename-date prefix) finds **zero** matches for any
`PROP-2026-06-16-NNN`. This run recovered the mapping deterministically (all 13 were APPROVE,
and cards are in stable order), but the next ambiguous decision set (mixed APPROVE/DENY/CHANGE)
could be mis-applied. **Recommend:** make line ~304 emit the same stable `proposal_id` list the
cards use, so the decision template and the lookup agree. Until fixed, position-mapping is
required to interpret decision emails.
