# Dispatch — Cross-Tradition Signal Backlog Clear (Level-2 dataset)

**Goal:** turn the Level-2 signal-stream prototype from a frozen-April snapshot into a live dataset by processing the approved-card backlog that the daily orchestrator has been deferring. Run on the Mac, metered, before ISME (July 8–10).

## Decisions locked (2026-06-26)
- **Scope:** 158 **approved** cards only (review gate intact). The 18 `pending` + 1 `needs_review` stay gated — the processor must never touch them.
- **Agent shape:** backlog batch (one metered clear) + daily standing pass (extend `c282-wiki-agent-daily-run`, which already defers this backlog). Not an always-on daemon.
- **QC:** machine-readable extension of `PROCESSED_LOG.md` (= `qc_trace.csv`). **Strict on coverage** (158/158 accounted, fail loud — Rule 12). **Loose on judgment** (PoC; extraction may be creative; experts rule on usefulness later).
- **Timeline meaning:** **dual encoding** — primary series = processing date (formation activity, i.e. when the agent registers the signal); overlay = source-date distribution (when the material appeared). Backlog clear yields a truthful late-June surge; May stays flat (queue latency, explained), and the overlay shows the latent source spread.

## Already built (in `prototypes/backlog/`)
- `build_manifest.py` → `backlog_manifest.json` (158 cards, ordered by source_date; card, tradition, source_date, title, file) and `qc_trace.csv` (empty rows, status=PENDING).
- Backlog by tradition: levin 21, wolfram 20, carroll 18, kastrup 14, mcgilchrist 14, wright 12, stump 11, fredrickson 11, friston 10, rohr 10, hoffman 8, arkanihamed 7, hawkins 2.
- Upstream extractor + viz: `prototypes/extract_signals.py`, `prototypes/build_prototype.py`, `prototypes/level2_signal_stream.html`.

## To build

### 1. Extraction prompt (model judgment — Rule 5)
Per card, give the model: the card's Summary + Why-This-Matters + PRS-CANDIDATE blocks, and the 14-tradition roster with one-line descriptions. Ask it to emit 0–N cross-tradition signals, each:
```
{ "from": <this card's tradition>, "to": <other tradition in roster>,
  "strength": High|Strong|Moderate|Speculative,
  "nature": convergence|tension|structural analogy|explanatory bridge|paradigm-shift candidate,
  "text": <=300 chars why, "card": <proposal_id> }
```
Rules in the prompt: `to` MUST be one of the 14 roster keys (never invent); omit a tradition rather than force a weak link; Speculative is allowed and encouraged over silence; no self-pairs.

### 2. Processor harness (deterministic — code)
Loop `backlog_manifest.json`. For each card: read file → call model with prompt → parse JSON → validate (every `to` in roster; no self-pair; strength/nature in enum; card id matches) → append valid signals to the dataset → write the `qc_trace.csv` row (processed_by, date_processed=today, signals_emitted=N, dup_check, status=pass/flag, notes). Dedupe against existing signals by (card, from, to). Meter token spend; print running total (Rule 6). **Idempotent:** re-running skips cards already marked processed.

### 3. Coverage gate (fail loud — Rule 12)
After a run: assert `rows with status!=PENDING == 158` (or the run's batch size). Any card that errored stays PENDING and is reported, not silently dropped. Emit a one-line coverage summary: `processed X/158, flagged Y, spend $Z`.

### 4. Dual-encoding timeline (viz)
In `build_prototype.py`: keep the cumulative line on **processing date**; add a faint **source-date** histogram/area behind it (monthly bins). Legend distinguishes "formation (when engaged)" vs "source material (when published)". Regenerate `level2_signal_stream.html` from the grown dataset.

### 5. Standing pass
Add a phase to `c282-wiki-agent-daily-run`: after the daily approve→inbox step, run the harness over any approved card not in `qc_trace.csv`, append signals + trace row, regenerate the viz dataset. Keeps the dataset live so the plateau never recurs.

## Run plan (within the week)
- Day 1 (Mac): build prompt + harness + coverage gate. Validate on a 5-card sample; eyeball the signals + trace rows.
- Day 2: metered full run over 158 (chunked if needed). Verify 158/158, review flagged rows.
- Day 3: dual-encoding viz regen; local HTTP review per constitutional rule; eyeball; then decide on wiring into `community_interactions.html` Level-2 panel.
- Standing pass added once the batch is trusted.

## Notes
- Runs on the Mac: vault writes + the agent rail. The Cowork sandbox can't push and the mount blocks some ops.
- This is distinct from the narrative-connectome cross-edges (computed PRS-similarity, static). The signals are the dated event stream of formation.
- Open question parked: reword the scaffold's Level-2 label ("Small-Group Tradition / within a research collective") to the "builders/searchers becoming mutually informed" sense.
