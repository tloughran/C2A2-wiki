---
title: The Review→Decision→Merge Gate — how to (reusable pattern)
updated: 2026-07-17
status: pattern doc; the concrete instance is the step-3 reconcile gate
relates_to: "reconcile_decisions.json", "merge_decisions.py", "Reconcile review.md", "reconciliation.json"
---

# The review gate, in general

Any time a deterministic pass produces a large overlay plus a queue of judgment calls
(reconcile here; could be a QC sweep, an import audit, a dedup pass), run it through a
**three-surface gate**. The point is that you make a handful of real decisions, code applies
them, and nothing half-decided can ever read as "done."

## The three surfaces (never collapse them)

1. **Reading surface — `Reconcile review.md`.** DERIVED, regenerated from the JSONs. You read
   it; you never write decisions into it (they'd be overwritten on the next render).
2. **Decision surface — `reconcile_decisions.json`.** The *only* hand-edited file. Batch
   policies (one toggle per cluster) + staged-work decisions + an `overrides` map for
   exceptions. Pre-filled with the recommended default for every group, so you skim and flip
   only what you disagree with.
3. **Merge step — `merge_decisions.py`.** Code applies your decisions. NON-DESTRUCTIVE: never
   touches `works_cited.json`, `reference_master.json`, or `build_works_cited.py`.

## Where the input goes

On disk in `commentary-apparatus/`, in `reconcile_decisions.json`. Durable across sessions,
machine-readable, git-gated. (Or just tell me your calls in chat and I'll write them in.)

## How to run it (≈6 decisions, not 82)

```
python3 merge_decisions.py --init      # (already done) writes the pre-filled decisions file
# ... edit reconcile_decisions.json ...
python3 merge_decisions.py             # apply -> resolved outputs; exits nonzero if anything is HELD
```

Pass order for speed:

1. **The 6 staged works** — the only high-value calls. Per work set `decision`:
   `approve` (optionally correct fields via `fields`), `amend` (same, with edits),
   `decline` (+ `redirect: "<cite_key>"` = where that PRS should point instead), or leave
   `hold`. Two are pre-set to **hold** because they're genuine judgment calls: the Ferriss
   #849 podcast (admissible as a source at all?) and Mindscape #349 (guest Harlow's content —
   don't credit Carroll). The gate will not close while anything is `hold`.
2. **The 6 batch policies** — accept the default or change one word:
   `rc_tome_prs_to_canonical`, `existing_seeded_prs`, `generics_canonical_default`,
   `friston_active_inference` (`keep_generic` | `promote_all` | `per_day`),
   `unscoped_prs_scope` (`master_framework` | `per_day`), `cross_flag_internal`.
3. **Exceptions only** — add to `overrides` (e.g. `"levin-PRS-01": {"underlying_work": "levin-2018-bioelectric-code"}`). Skip the 33 CROSS/2 FLAG bridges — spot-check, no decision.

## What merge emits

- **`reconciliation.resolved.json`** — the overlay with `needs_human_confirm` cleared where you
  decided; an `unresolved` list of everything still open (holds, `per_day` choices, the
  FLAG-003/005 location check). This is what step 3b (annotate) and step 4 (build) consume.
- **`approved_works.json`** — approved staged works, `verified:true`, ready to fold into
  `build_works_cited.py`'s `WORKS` dict; then re-run that generator to refresh
  `works_cited.json` + `Works cited.md`. (Kept separate so the confirmed-46 file is only ever
  updated through its own generator — the existing discipline.)

## Fail-loud contract

If any staged work or policy is left `hold`, merge prints the holds and **exits 2**. A gate that
isn't fully decided can't be mistaken for a finished one. `unresolved` always tells you exactly
what remains, so you can close it incrementally across sessions.

## Reusing this for the next review

`merge_decisions.py --init` regenerates a pre-filled decision file from whatever
`reconciliation.json` + `works_cited_staged.json` are present. Point `$APPARATUS_DIR` at another
review's folder and the same three-surface gate applies unchanged.
