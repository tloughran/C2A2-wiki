# DISPATCH — Track A PRS-triplet backlog clear (attended, on the Mac)

Companion to `DISPATCH_backlog_signal_clear.md` (Track B / cross-signals). This is
**Track A**: ingest the un-ingested inbox cards into per-tradition PRS triplets.

Scope locked 2026-06-30: run Track A first, then downstream steps 1-2-4 (PRS yield
-> connectome -> metabolism). Track B (signals reconcile + viz) is a separate pass.

## Ground truth — CORRECTED 2026-06-30 PM (gate bug fixed)
The earlier "70 units / 127 triplets" came from a BUGGY un-ingested gate in
`build_prs_manifest.py` (it tested inbox FILENAMES against a log keyed on
proposal-id/slug). That erred BOTH ways: it re-staged ~15 already-ingested cards
AND hid genuinely-pending cards whose basename was merely mentioned in the log
(deposit/deferral notes). Fixed: the gate now excludes a card iff its proposal_id
is cited as a `Source:` in any live `traditions/*/prs_triplets.md` OR appears in a
PROCESSED_LOG `→ <trad> PRS-` ingestion line (authoritative).

Corrected, validated set (0 already-ingested leakage, spot-checked):
- **72 un-ingested staging files -> 70 unique units** (2 same-source re-stagings:
  PROP-2026-05-09-002, PROP-2026-05-23-001).
- **152** pre-drafted `PRS-CANDIDATE` triplets across the 70 units.
- By tradition (units): wright 9, wolfram 8, rohr 8, carroll 8, fredrickson 6,
  levin 6, stump 5, friston 4, hoffman 4, mcgilchrist 4, arkanihamed 3, kastrup 3,
  hawkins 2. (wright/rohr jumped because the old gate had hidden their May cards.)
- **124 cards correctly SKIPPED** as already ingested (was the silent corruption risk).
- Regenerate to `/tmp/prsC` with the paste-ready block below; gates PASS.
- One unit has 0 candidates (rohr PROP-2026-06-21-001) — stages nothing, log as empty.

## Build-order parts 1-2 — SHIPPED to working copy (sandbox, deterministic)
- `prototypes/backlog/build_prs_manifest.py` — emits `prs_manifest.json` (70 units,
  each with `proposal_ids[]`, `files[]`, `tradition`, `source_date`, `title`,
  `n_candidates`) + `prs_qc_trace.csv`. Coverage gate: 73 files = 70 units + 3
  restagings, else exit 2.
- `prototypes/backlog/stage_prs.py` — parses each card's `PRS-CANDIDATE` blocks,
  computes the next live `PRS-NN` per tradition (reads `traditions/<key>/prs_triplets.md`,
  numbers forward across all units in a tradition), renders ready-to-paste append
  blocks into `<OUT>/prs_staging/<trad>__<unit_id>.txt`. Writes ONLY to the scratch
  OUT dir + qc_trace — never to live `traditions/`, `master/`, or `PROCESSED_LOG.md`.
  Verified: manifest count == staged count for all 70 units (no silent drops).

### Regenerate the manifest + staging (paste-ready, run from repo root)
```
cd "/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project"
rm -rf /tmp/prsC
python3 prototypes/backlog/build_prs_manifest.py wiki /tmp/prsC
python3 prototypes/backlog/stage_prs.py wiki /tmp/prsC/prs_manifest.json /tmp/prsC
ls /tmp/prsC/prs_staging | wc -l
```
Expect: builder prints `skipped (already ingested) : 124`,
`UNIQUE extraction units : 70`, `candidate triplets total : 152`,
`coverage gate : PASS`; stager prints `coverage gate : PASS`; the `ls` prints `70`.

### Commit tool — apply_prs.py (deterministic, idempotent, dry-run by default)
Part 1-2 (manifest + staging) plus the new `apply_prs.py` make the mechanical
half code-driven; only vet/dedup/drop is model judgment. apply_prs.py strips the
staging header, inserts kept blocks BEFORE the `*Total PRS triplets:` footer (one
`---` per block, footer count bumped, parenthetical suffix preserved), appends one
PROCESSED_LOG line per unit under a dated Track-A header, and marks the unit DONE
in qc_trace. Skips units already DONE or whose first PRS-N is already present.
Verified on hawkins: SUPP-001 +6 (PRS-19..24), footer 18->24, clean separators.
```
python3 prototypes/backlog/apply_prs.py wiki /tmp/prsC/prs_manifest.json \
    /tmp/prsC/prs_staging /tmp/prsC/prs_qc_trace.csv --tradition <T> \
    --drop UNIT:PRS-NN,UNIT2:PRS-MM            # omit --apply = DRY-RUN
```
Add `--apply` once the dry-run diff looks right. Cross-tradition routing into
`master/cross_program_index.md` is NOT done by the script (attended, flagged in
qc_trace notes) — author CROSS-/FINDING- entries by hand after the triplets land.

## Part 3 — ATTENDED extraction loop (the metered, model-judgment step)
The staged blocks are pre-drafted from each card's own candidates. Per unit, the
judgment is **vet / dedup / route**, not authoring. For each
`/tmp/prsA/prs_staging/<trad>__<unit_id>.txt`:

1. **Vet** each staged `PRS-N` against the source card
   (`prs_manifest.json` -> the unit's `primary_file`). Accept, trim, or drop.
2. **Dedup** against existing triplets in `wiki/traditions/<trad>/prs_triplets.md`
   — if a candidate restates a triplet already there, drop it and note the PRS-N it
   duplicates in qc_trace `notes`.
3. **Append** the accepted blocks to `wiki/traditions/<trad>/prs_triplets.md`,
   and bump its `*Total PRS triplets: N*` footer line.
4. **Route cross-tradition signals** (the card's `## Cross-Tradition Signals` and any
   `[-> X agent]` agentic calls): add CROSS-/FINDING- entries to
   `wiki/master/cross_program_index.md`; reflect material new bridges in
   `wiki/master/C2A2_master_wiki.md`.
5. **Log** the file(s) in `wiki/inbox/PROCESSED_LOG.md` (both proposal_ids for a
   re-staged unit; mark the duplicate so it is never re-queued).
6. **qc_trace**: set `processed_by`, `date_processed`, `triplets_emitted` (after
   vetting), `cross_refs`, `first_prs_n`, `status=DONE`.

Guardrails (non-negotiable):
- Confidence labels are **High / Medium / Speculative** only — never Easy/Low/Hard.
- Count triplets from `PRS-CANDIDATE-` lines in source, not rendered chips.
- The PRS/coil **method is Loughran's** — never attribute it (or thinkers cited
  inside a triplet) to Stump; provenance is the card's own `tradition_key`.
- Idempotent: a unit already `DONE` in qc_trace is skipped on re-run.
- DROP no-net-new units: a card that only upgrades a citation or restates an
  existing triplet emits 0 (e.g. hawkins PROP-2026-06-23-002 "PRS-25" says verbatim
  "no new triplet content is added"); pass all its PRS-N to `--drop`, log as
  no-net-new (+0). Do the citation upgrade itself as a separate edit if worthwhile.

Coverage gate for part 3: when the loop finishes, every one of the 70 units is
`DONE` or explicitly `SKIPPED` (with a reason) in qc_trace, and every of the 73
files is in PROCESSED_LOG. Fail loud otherwise.

## Downstream regens — COMMIT FIRST (order matters; corrected 2026-06-30)
**`prs_yield.py` reconstructs the yield series from GIT HISTORY**, so it FAILS
loud (Rule 12) on triplets that are on disk but not yet committed ("present on disk
but absent from git history"). Therefore the triplet commit must PRECEDE the metrics
regen — the reverse of the original runbook order. Step 0 = review + commit the
triplets, THEN regen. Paste-ready, ASCII, paste-safe:
```
cd "/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project"
git checkout main
git add wiki/traditions wiki/inbox/PROCESSED_LOG.md
git commit -m "Track A PRS backlog clear: ingest 144 vetted triplets across 12 traditions"
python3 wiki/architecture/metrics/prs_yield.py
bash scripts/regen_prs_connectome.sh
```
Then the metabolism view (picks up the new PRS-yield CSV + the cross-signal yield
axis shipped 2026-06-29):
```
cd "/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project/wiki/metabolism/scripts"
python3 build_metabolism_view.py --outdir ..
```
(Steps 3/5/6 — signal viz, sociogram, review log — belong to the Track-B pass unless
extraction surfaced new `cross_program_index` entries worth carrying into the
sociogram early; if so, run `bash wiki/c2a2-wiki-narration/regen_sociogram.sh` — the
wrapper, never the bare generator.)

## Verify, then push (constitutional No-Blind-Push)
```
cd "/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project/wiki"
python3 -m http.server 8080
```
Open http://localhost:8080/explorer.html and confirm: Metabolism PRS bars now
extend past mid-June; a spot-checked tradition (e.g. carroll) shows the new triplets
in its node panel; prs_3d.html still loads. Ctrl-C when satisfied.

Publish after sign-off (triplets already committed above; this commits the regen
outputs; clears the known stale lock; rebases for heartbeat cron):
```
cd "/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project"
rm -f .git/index.lock .git/refs/heads/main.lock
git add wiki/architecture/metrics/prs_yield_detail.csv wiki/prs_3d.html wiki/metabolism
git commit -m "Regen yield/connectome/metabolism after Track A PRS backlog clear"
git pull --rebase --autostash origin main
git push origin main
```
NOTE: this session applied the 144 triplets to the working tree only (uncommitted).
Cross-tradition routing into `master/cross_program_index.md` was DEFERRED (a
separate attended step; apply_prs.py does not touch master/), so `wiki/master` is
intentionally omitted from the commit until routing is done. qc_trace audit had a
metadata glitch on the 3 cross-tradition-shared proposal-ids (PROP-2026-05-18-001/
002/003, levin/wright/friston) — vault content is git-verified correct (144 blocks
in the right files); re-derive the audit from PROCESSED_LOG if needed. Harden
apply_prs.py's qc write (now guarded to fail loud) before the standing-pass reuse.

## Standing-pass follow-on (so the plateau never recurs)
Once trusted, extend `c282-wiki-agent-daily-run` to run `build_prs_manifest.py` +
the extraction over any approved card not yet `DONE` in `prs_qc_trace.csv`, append +
regen daily. Keep the attended-QC gate for anything the loop flags.
