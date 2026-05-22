# Repair Manifest — 2026-05-12

**Purpose:** Documents the manual repair of 34 orphaned proposal approvals from Tom's May 12 decision email (`[C2A2-review-decision] 2026-05-11`).

**Root cause:** `generate_review_page.py` assigns PROP IDs using the review-page generation date (e.g. `PROP-2026-05-11-NNN`), but proposal files are named with their specialist-agent creation date (e.g. `2026-05-04_thinker_slug.md`). The Phase 0 decision processor matched files by looking for the PROP ID date prefix (`2026-05-11`) in the filename — so only the 4 proposals actually created on 2026-05-11 (PROP-035 through PROP-038) were processed. The remaining 34 (PROP-001 through PROP-034) had no matching files and were silently skipped.

**Corrected decisions file note:** The `2026-05-11_decisions.md` archive incorrectly recorded that PROP-001–004 mapped to the `2026-05-11_*` files. The true mapping (per the HTML review page) is:
- PROP-001–034 → files dated 2026-05-04 through 2026-05-10 (repaired here)
- PROP-035–038 → files dated 2026-05-11 (already correctly in `approved/`)

**Repair action (2026-05-13):**
- All 34 files copied from `pending/` to `approved/`
- YAML front matter patched in both copies: `status: approved`, `prop_id: PROP-2026-05-11-NNN`, `decision: APPROVE`, `decided_at: 2026-05-12`
- Pending copies updated in-place (same content as approved copies, with `status: approved` to prevent re-pickup)

**Note for next wiki agent run:** Process all 34 files below in order. Each has `prop_id`, `decision: APPROVE`, and `decided_at: 2026-05-12` in its YAML front matter.

---

## Files Moved (34 total)

| PROP ID | Original Filename |
|---|---|
| PROP-2026-05-11-001 | 2026-05-04_carroll_mindscape-347-ferguson-data-surveillance.md |
| PROP-2026-05-11-002 | 2026-05-04_friston_phenotyping-agency-ai.md |
| PROP-2026-05-11-003 | 2026-05-04_wolfram_future-science-tech-qa-april24.md |
| PROP-2026-05-11-004 | 2026-05-04_wolfram_south-park-commons-fireside.md |
| PROP-2026-05-11-005 | 2026-05-05_arkanihamed_fermion-mass-hierarchy-tev.md |
| PROP-2026-05-11-006 | 2026-05-05_carroll_ama-may-2026.md |
| PROP-2026-05-11-007 | 2026-05-05_carroll_mindscape-352-brunton-connectome.md |
| PROP-2026-05-11-008 | 2026-05-05_fredrickson_does-positivity-resonance-signify-love.md |
| PROP-2026-05-11-009 | 2026-05-05_fredrickson_interparental-positivity-spillover-theory.md |
| PROP-2026-05-11-010 | 2026-05-05_friston_online-generalised-predictive-coding.md |
| PROP-2026-05-11-011 | 2026-05-05_hoffman_spacetime-bounds-v2.md |
| PROP-2026-05-11-012 | 2026-05-05_hoffman_trace-institute-launch.md |
| PROP-2026-05-11-013 | 2026-05-05_kastrup_more-than-allegory-myth-archetype.md |
| PROP-2026-05-11-014 | 2026-05-05_kastrup_rovelli-rqm-physical-non-realism.md |
| PROP-2026-05-11-015 | 2026-05-05_levin_bootstrapping-life-inspired-machine-intelligence.md |
| PROP-2026-05-11-016 | 2026-05-05_levin_cancer-to-ai-alignment-homeostasis.md |
| PROP-2026-05-11-017 | 2026-05-05_mcgilchrist_closer-to-truth-life-after-death.md |
| PROP-2026-05-11-018 | 2026-05-05_stump_good-of-thomas-aquinas-agatheos.md |
| PROP-2026-05-11-019 | 2026-05-05_stump_infused-virtues-indwelling-holy-spirit.md |
| PROP-2026-05-11-020 | 2026-05-05_wolfram_madrid-geometric-ideas-computational-frontiers.md |
| PROP-2026-05-11-021 | 2026-05-05_wolfram_rulial-ensemble-biology-bulk-orchestration.md |
| PROP-2026-05-11-022 | 2026-05-08_arkanihamed_single-minus-gluon-graviton-gpt52.md |
| PROP-2026-05-11-023 | 2026-05-08_carroll_mindscape-351-singer-utilitarianism.md |
| PROP-2026-05-11-024 | 2026-05-08_fredrickson_positive-emotions-cornerstones-oxford-2025.md |
| PROP-2026-05-11-025 | 2026-05-08_fredrickson_positively-in-sync-convergent-validity.md |
| PROP-2026-05-11-026 | 2026-05-08_stump_meaning-of-suffering-human-flourishing-pine-dialogue.md |
| PROP-2026-05-11-027 | 2026-05-09_mcgilchrist_unsiloed-648-attention-modes.md |
| PROP-2026-05-11-028 | 2026-05-09_wolfram_business-april29-paradigm-shifting-ideas.md |
| PROP-2026-05-11-029 | 2026-05-09_wolfram_kids-167-brains-evolution-life.md |
| PROP-2026-05-11-030 | 2026-05-10_rohr_2026-meditations-good-news-fractured-world.md |
| PROP-2026-05-11-031 | 2026-05-10_rohr_america-magazine-universal-christ-interview.md |
| PROP-2026-05-11-032 | 2026-05-10_wright_collins-oxford-god-and-science.md |
| PROP-2026-05-11-033 | 2026-05-10_wright_gods-homecoming-biblical-story-essay.md |
| PROP-2026-05-11-034 | 2026-05-10_wright_gods-homecoming-book.md |

## Already correct (not touched)

PROP-2026-05-11-035 through PROP-2026-05-11-038 — the four `2026-05-11_*` files — were correctly moved to `approved/` by the original decision processor and need no further action.
