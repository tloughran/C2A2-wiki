# OpenStory → C2A2 — Session 6 handoff (2026-06-29)

Build-sequence step 1 (the `extract_turn_structure.py` bridge) was **not built**.
Pre-flight inspection of the live DB found the bridge's named sources are dead, so per
the agreed fork we **investigated the freeze first** instead of coding a tombstone.

## TL;DR

The `turns` / `turn.sentence` / `agent.delegation` data the bridge was meant to mine
**froze on 2026-04-07/08**. Root cause: OpenStory's Claude Code translator derives a
turn boundary from exactly one raw signal — a transcript line with
`subtype == "turn_duration"` → `system.turn.complete` (`rs/core/src/translate.rs:301-305`).
That `system.turn.complete` is the *sole* trigger for `eval_apply::step` to return
`TurnComplete`, which crystallizes a `StructuralTurn` (→ `turns`), fires the
`SentenceDetector` (→ `turn.sentence`), and emits `eval_apply.turn_end`. The
`turn_duration` signal stopped arriving ~Apr 7–8, so the whole turn-boundary family
went silent while per-message patterns kept flowing.

## Evidence (live DB, read-only snapshot probes)

- **Zero** `system.turn.complete` events in the store (290,942 events, none of that
  subtype). Other synthetic `system.*` events DO persist live (`system.compact` through
  Jun 24), so persistence is not the filter — the translator simply isn't producing
  turn.complete because no `turn_duration` line reaches it.
- A whole family froze together on Apr 7–8 (max `start_time`):
  `eval_apply.turn_end` 115, `turn.sentence` 115, `turn.phase` 517, `scope_open` 7499,
  `scope_close` 1086, `error.recovery` 155, `agent.delegation` 28 (Apr 6).
- Still flowing (max `start_time` = today): `eval_apply.eval` 103,690,
  `eval_apply.apply` 83,967, `eval_apply.compact` 391 — exactly the patterns emitted
  per `message.assistant.*` / `system.compact` event on the fold's *Continue* branch,
  independent of turn boundaries.
- `turns` table: 115 rows, 115 distinct sessions (1 turn each, 7% of 1552 sessions),
  all timestamped 2026-03-30 → 2026-04-07. Sampled turns are thin (29/115 have any
  `applies`; `is_agent` spawn signal effectively empty).
- Live wiring is intact and would persist turns if it got them:
  `PatternsConsumer.process_batch → PatternPipeline.feed_event → eval_apply::step`;
  `rs/src/server/mod.rs:266` calls `insert_turn` per completed turn;
  `should_skip_pattern_detection` does NOT skip turn.complete. The gap is upstream of
  the fold — no boundary event is produced.

## CONFIRMED upstream (Mac grep, 2026-06-29)

`grep -rl turn_duration ~/.claude/projects` returned **nothing** — no current Claude
Code transcript anywhere under the watch root contains a `turn_duration` line (the
Mar–Apr transcripts that did have since rotated away). So the translator's sole
turn-boundary signal is genuinely absent from the live input. **Root cause = upstream
Claude Code transcript format drift** (the `turn_duration` system line was dropped ~Apr
2026). The internal-refactor hypothesis is ruled out: there is no `turn_duration` in the
input for any pipeline to drop, and `system.compact` still persists fine.

Caveat worth a follow-up grep on the Mac: Claude Code may have *renamed* the duration
signal rather than removed it (e.g. a different `type`/`subtype` key or a `durationMs`
on another line). The proposed fix does NOT depend on finding it (it keys off
`stop_reason`), but knowing the new key would let us also restore exact `duration_ms`.

## Fix IMPLEMENTED (code written; NOT yet compiled/deployed)

Edited **`rs/core/src/translate.rs`** only. `translate_line` now appends a synthetic
`system.turn.complete` event after an assistant message whose `stop_reason` is terminal
(`end_turn` or `stop`) — exactly one boundary per turn (a `tool_use` message is mid-turn
and gets none). Mirrors the existing `translate_pi.rs` (`stopReason=="stop"`) and
`translate_codex.rs` (`task_complete`) synthesis. The boundary event gets a deterministic
id `"{uuid}:turn_complete"` so re-ingest is idempotent (INSERT OR REPLACE, no dup).
`duration_ms` is left None (the removed `turn_duration` was its only source); the
eval-apply fold derives `is_terminal` from accumulator phase, so turns still crystallize.

Added an inline `#[cfg(test)] mod synth_turn_complete_tests` (3 tests): `end_turn` →
trailing `system.turn.complete` (subtype + deterministic id + agent asserted); `stop` →
same; `tool_use` → single event, NO boundary (guards against splitting one turn into
many). Tests encode WHY, not just count.

**Could NOT compile/run in the Cowork sandbox** — no Rust toolchain there and the shell
slices can't build the axum/tokio workspace. Static move/borrow/type review done by hand
(clean). **Must be compiled + tested on the Mac before trusting.**

### Deploy on the Mac

```sh
cd "$HOME/Documents/Non-Claude Projects/OpenStory/rs"
cargo test -p open-story-core synth_turn_complete   # the 3 new tests
cargo test -p open-story-core                        # full core suite (no regressions)
# then rebuild + restart the backend so the live watcher uses the new translator:
launchctl bootout  "gui/$(id -u)/com.tomloughran.openstory.backend" 2>/dev/null
launchctl bootstrap "gui/$(id -u)" ~/Library/LaunchAgents/com.tomloughran.openstory.backend.plist
# verify boundaries start flowing (was 0 before):
sqlite3 "$HOME/Documents/Non-Claude Projects/OpenStory/data/open-story.db" \
  "SELECT COUNT(*) FROM events WHERE subtype='system.turn.complete';"
```

After restart, NEW turns crystallize live; the `turns`/`turn.sentence` tables grow again,
and **step 1 (`extract_turn_structure.py`) can then read a live source** as intended.

### Historical backfill (separate job — NOT in this fix)

There is no `rebuild`/`replay` CLI subcommand (only Serve/Watch/Synopsis/Pulse/Context/
Reconcile/…). Re-crystallizing the ~1552 historical sessions is a follow-up with a real
fork to decide:
- **(a) re-read retained transcripts** through the watcher — limited by Claude Code
  transcript rotation (old files may be gone; the watcher backfill window is 72h).
- **(b) one-time migration over the `events` table** — synthesize `system.turn.complete`
  rows from existing `message.assistant.*` events carrying terminal `stop_reason` (all
  290k events are already stored), then re-run pattern/turn crystallization. Doesn't
  depend on transcripts; cleaner for full history. Needs a small dedicated script.
Going-forward live capture does NOT need this; decide backfill scope separately.

## SECOND break found post-deploy (crystallization gap) — OPEN

After deploy, the translator fix works: `system.turn.complete` events went 0 → 587 (live,
newest = now), confirming boundaries are synthesized and persisted. BUT the crystallized
layer is still frozen: `turns` = 115 and `turn.sentence` = 115, both max 2026-04-07.
`eval_apply.turn_end` also still 115. So a **second, distinct bug**: the boundaries reach
the persist path but are NOT delivered to the eval-apply crystallization fold.

Proof it's delivery, not lag: the fold's frontier (`eval_apply.eval` max) caught up to
22:52, and all 587 boundaries have timestamps ≤ that frontier (`tc_before_frontier=587,
after=0`) — the fold ran past every boundary's timestamp and emitted no `turn_end`.
`EvalApplyDetector::feed_cloud_event` has no subtype filter and `should_skip_pattern_detection`
doesn't skip turn.complete, so the gap is UPSTREAM of the fold: the batches the
PatternsConsumer folds don't contain the synthetic boundaries. Prime suspect: the boot
backfill burst that produced the 587 boundaries was missed by the PatternsConsumer
subscription (both nominally share `events.>`, but PersistConsumer is the durable writer),
i.e. a bus/backfill-ordering or batch-assembly issue — NOT the translator.

### Test result (RESOLVED): crystallization works; it's a backfill-delivery gap
`turns`, `turn.sentence`, and `eval_apply.turn_end` all moved 115 → 117 **in lockstep,
same fresh timestamp**. `turn_end` is emitted only in the boundary branch (not by
session-flush), so those turns were crystallized by real `turn.complete` events flowing
through the fold — the full pipeline works end-to-end when a boundary reaches it.

So NOT systematic non-delivery. It's specifically the **boot-backfill burst** (~585 of
587 boundaries) reaching the durable `PersistConsumer` but never being republished onto
`events.>` for the `PatternsConsumer` fold — exactly the shape of
`rs/server/src/catch_up.rs` ("…no JetStream source backfills them … `bus.publish(events.{sid}, batch)`").
Going-forward LIVE turns crystallize on their own.

### Remaining follow-up (contained) — replay historical boundaries
Re-publish the persisted boundary (and surrounding) events onto `events.{sid}` so the
patterns consumer folds them — via the existing `catch_up` path, or a small one-time
replay over the `events` table grouped by session. Targets: the ~585 backfilled
boundaries + the 1552 pre-existing sessions. After that, `turns` fills out and step 1
(`extract_turn_structure.py`) has full-history depth. Not a redesign; scope next session.

Past a sensible session budget — good place to checkpoint.

## What was touched

- **`rs/core/src/translate.rs`** — synthesis block in `translate_line` + inline test
  module. One file. No other crates, extractors, DB, scheduled task, or feed JSON
  changed. Not compiled, not deployed, not pushed.

---

# Session 7 addendum (2026-06-29) — the replay fix is WRITTEN, DEPLOYED, and VERIFIED

**STATUS 2026-06-29 (deployed):** Built + bootstrapped on physmini02 with
`OPEN_STORY_RECRYSTALLIZE_ONCE=1` in the backend launchd plist
(`com.tomloughran.openstory.backend`, StandardErrorPath
`~/Library/Logs/openstory-backend-error.log`). `turns` went **117 → 4,892** (and
climbing during the sweep) — confirming the historical boundaries now fold. Gate
removed after the sweep and the backend re-bootstrapped clean. The three-month freeze
(2026-04-07) is closed end-to-end: translator fix restored live boundaries (S6),
this replay backfills history (S7). Next: the original step 1 `extract_turn_structure.py`
now has a full-depth source.

---


The "remaining follow-up" above is now implemented as a one-time, operator-gated
**local replay onto the bus** — the same mechanism `catch_up_once` uses
(`bus.publish("events.{sid}", batch)`), but sourced from the LOCAL `EventStore`
instead of a remote peer. Confirmed by reading the live path that this is the only
missing route: `reconcile_local`, `reproject_all`, and `replay_boot_sessions` all
rebuild the store/projections but **never republish onto `events.>`**, so none of
them feed the eval-apply fold. Idempotency verified at the store layer before
writing: events PK-dedup; `insert_turn` is `INSERT OR REPLACE` on `turn:{sid}:{n}`;
`insert_pattern` is `INSERT OR IGNORE` on `{type}:{started_at}:{sid}`. Re-running is
safe.

### Files touched (3) — all in the OpenStory repo, NOT the wiki
- **NEW `rs/server/src/recrystallize.rs`** — `replay_local_to_bus(event_store, bus)`
  iterates `list_sessions` → `session_events` (already ordered by timestamp ASC) →
  deserializes to `CloudEvent` → chunks at 200 events/batch (NATS ~1 MB payload cap)
  → `bus.publish("events.{sid}", batch)` sequentially (preserves per-session fold
  order) → returns `ReplayReport{sessions,events,batches,skipped_events}`. Pure
  helpers `parse_session_events` + `build_session_batches` are unit-tested (3 tests,
  intent-encoding: malformed counted-not-swallowed, order preserved, chunk boundary
  loses nothing).
- **`rs/server/src/lib.rs`** — `pub mod recrystallize;`.
- **`rs/src/server/mod.rs`** — in `run_server`, inside `if is_consumer`, between
  Actor 2 (patterns) and Actor 3 (projections): a spawn gated on
  `OPEN_STORY_RECRYSTALLIZE_ONCE` that, after a 3 s settle, runs the sweep and logs
  a `recrystallize` report.

**Could NOT compile in the Cowork sandbox (no Rust toolchain).** Types hand-checked
against `catch_up.rs` (same crate, same imports) and the consumer test helper. Must
`cargo test` + build on the Mac before trusting.

### Deploy + run-once + verify on the Mac
```sh
cd "$HOME/Documents/Non-Claude Projects/OpenStory/rs"
cargo test -p open-story-server recrystallize
cargo test -p open-story-server
cargo build --release
```
Then set the gate in the backend launchd job, restart, watch turns fill, then remove
the gate (label assumed `com.tomloughran.openstory.backend` — confirm). The sweep
runs once per boot only while the env var is present; replays ~290k events, so turns
climb from 117 toward ~1552+ over a minute or two. The broadcast consumer will also
re-emit these to any open UI — a harmless one-time burst.

### Resume cue
"resume the turn-structure replay" / "resume the OpenStory recrystallize". Originating
sessions: `local_bb3d4ba0-...` (Extract turn structure bridge, S6 deploy+diagnosis),
this session (S7, replay fix written). Next increment after verify: unblock step 1
`extract_turn_structure.py` (the original bridge) now that `turns` has full-history
depth.

---

# Session 7 close (2026-06-29 night) — DEPLOYED, VERIFIED, LEGIBILITY DONE; design ladder set

**Deploy verified live:** `turns` 117 → **4,910** (full history Mar→Jun: 117/895/993/2905).
Gate removed, backend clean. Fix is done end-to-end.

**Pivoted from "build the bridge" to "legibility first" (Tom's call): see what the
substrate actually is before designing on it.** Took a static snapshot
(`~/Documents/Non-Claude Projects/OpenStory/data/open-story-snapshot.db`, 2.2 GB, via
`sqlite3 .backup` — safe, online-backup API) and probed it read-only. Deliverables in
repo at **`openstory-legibility/`**: `probe_substrate.py` (idempotent, re-runnable
against any snapshot) + `legibility_report.md` (generated). Both also pushed to Drive
(report = Google Doc id `1_R9OI1mI19mwsejO1I0yxmc5LKnzZXXT03aQPkcGEpw`; .py = reference
pointer only, full source in repo).

**Key legibility findings (the design inputs):**
- The `turns` table carries **content, not just counts** — `human` (prompt), `thinking`,
  `eval` (response) in the same row as `applies`/`stop_reason`/`scope_depth`. ~75-80% of
  4,910 turns carry the dialogue. So it's a content-bearing dialogue record; relational
  folds build directly on `turns.data`, no new OpenStory instrumentation needed.
- **AI-to-AI is already in the data:** 191 `agent-*` sessions where the `human` field is
  the *orchestrating agent's* instruction → 191 AI↔AI dialogues in the same schema.
  (Per-turn `is_agent` flag is dead 0/4910; lineage via `origin_agent` on all 1564.)
- **Two honest gaps:** (a) four detectors (`scope_*`, `turn.phase`, `error.recovery`,
  `agent.delegation`) went dark at the same Apr-7/8 drift and the replay did NOT revive
  them — separate signal gap, candidate question for OpenStory; (b) 807 prompt-bearing
  sessions crystallize no turns (only 223/1564 have turns) — fold-coverage gap to close
  before measuring on top.
- **Scope caveat:** single human / single host — human↔AI history is rich, but the
  multi-human *community* dimension isn't in this corpus yet.

**Design ladder proposed (each rung = an idempotent fold keyed by turn id):**
1. **Uptake** (deterministic, no model): consecutive-turn semantic similarity + explicit
   reference → per-session "uptake curve." The cheapest test of whether "listening" is
   even legible. **This is the smallest real next step** — build ONLY this on the 223
   turn-bearing sessions first.
2. **Relational moves** (cheap model = judgment only): classify each `eval` vs prior
   `human` — acknowledge / build-on / steelman / concede / repair-after-error / deflect /
   override. The MacIntyrean deep-listening instrument; the paper's spine.
3. **History → futures:** does uptake/repair/steelman rise as a session (or a human-AI
   pair) accumulates history. Falsifiable.

**Status:** design is articulated, NOT built. Tom low on cycles, parking after this.
Resume cue still "resume the turn-structure replay" or "resume the OpenStory legibility".
Pick up at Rung 1 (uptake prototype) when cycles return.

---

# Session 8 close (2026-06-30) — RUNG 1 BUILT, RUN, VERIFIED. Verdict: GREEN for Rung 2.

**Built and ran Rung 1 (uptake) directly in Cowork** — the snapshot is reachable from the
sandbox at `Documents/Non-Claude Projects/OpenStory/data/open-story-snapshot.db`, so this
was NOT dispatch-mode; real numbers, not just a script to carry to the Mac.

**Deliverables in repo at `openstory-legibility/`:**
- `rung1_uptake.py` — read-only, idempotent, **zero-dependency** (pure stdlib; TF-IDF in
  plain math, NO model, no numpy/sklearn/torch/network). Deterministic (seed 1729, 200
  shuffles). Same default DB path as `probe_substrate.py`, so it runs unchanged on the Mac.
- `rung1_report.md` — the verdict (generated).
- `rung1_uptake.json` — per-session uptake curves + role-tagged adjacency, for later plotting/Rung 3.

**Metric (grounded in the real schema, not the original sketch):** a `turn` is one message
beat — human & eval live in SEPARATE alternating turns (or combined). So the script first
reconstructs each session's dialogue STREAM (flatten human-then-eval per turn, turn_number
order, drop empties → ordered [(H|A, text)]). Uptake = adjacent-utterance TF-IDF cosine.
**Control is ROLE-MATCHED** (the key correctness fix): adjacent pairs are always cross-role
(short human ↔ long AI, few shared words), so an all-pairs floor is confounded by same-role
pairs and gives a bogus NEGATIVE lift (caught and discarded mid-build). Correct null = same
later-utterance paired with a RANDOM opposite-role utterance from the same session;
`lift = mean(real adjacent) − mean(role-matched null)`; permutation p over 200 reassignments.

**VERDICT (the population correction matters):** of 223 turn-bearing sessions, only **15 are
genuine extended two-sided dialogues** (each role ≥3 utts, ≥10 total, non-degenerate null).
The rest are single-prompt runs or repetitive scheduled-task sessions where `real==null`
exactly (near-identical utterances → lift 0 by construction); they wash the all-105 median to
~0 and must NOT be averaged in (Rule 7). On the 15 genuine dialogues:
- median lift **+0.031**; **positive in 14/15**; permutation-significant (p<0.05) in **13/15**.
- direction: **H→A** (AI takes up human) +0.050, positive 14/15 — the easy, expected floor;
  **A→H** (the *listening* signal, next human takes up AI) +0.025, positive 11/15 — present
  but noisier, exactly where short human backchannels make a lexical lens go blind.
- the 2 non-significant are the 42-utt Summa-status chat (short turns) and a 17-utt session.

**So: listening IS legible even through a pure-lexical lens, in real conversations → Rung 2
(model-as-judgment) is justified.** Two scoping consequences for Rung 2:
1. Target the **~15 genuine dialogues**, NOT all 223 turn-bearing sessions. "223" is the wrong
   denominator — most are automated/single-shot. This echoes the legibility map's
   one-human/heavily-skewed caveat.
2. Point Rung 2's classifier at the **A→H direction** specifically — that's where lexical is
   blind and where the MacIntyrean acknowledge/build-on/steelman/concede/repair vocabulary
   lives. Concrete proof: session `ea7b2dcd` (the turn-pipeline-fix chat) has human turns
   "Implement now.", "all OK; passed" — high-quality listening, lexically ~invisible.
3. **AI↔AI is still not measurable**: only 1 of 191 `agent-*` sessions has ≥2 turns (a dup).
   Agent sessions are single-shot in this corpus; the AI↔AI bonus needs multi-turn agent
   dialogues that don't yet exist here.

**Rung 3 hook:** `rung1_uptake.json` already stores the per-session curve + per-pair role tags,
so "does uptake rise as a session matures" (Rung 3) can be read off the existing JSON without
recompute.

**No push:** all artifacts are local analysis under `openstory-legibility/` (not the published
wiki); the no-blind-push rule doesn't engage. Nothing committed.

**Regen anytime (idempotent):** `python3 openstory-legibility/rung1_uptake.py [snapshot.db] [out_dir]`
(make a fresh snapshot first via the `sqlite3 .backup` line in `probe_substrate.py`'s header).

**Resume cue:** "resume the OpenStory legibility" / "resume Rung 1" / "build Rung 2 uptake".
Next increment when cycles return: Rung 2 relational-move classifier on the 15 dialogues,
A→H direction, cheap batched model. Originating session: this one (Cowork, 2026-06-30).

---

# Session 9 close (2026-06-30) — RUNG 2 PILOTED + DATA BUG FOUND (replay dup). Both rungs now clean.

**Found and fixed a real data bug mid-Rung-2 (fail-loud).** The `turns` table is
**replay-duplicated 2-9x**: the S7 recrystallize replay (deployed last session) re-folds the
same events each pass and `insert_turn` keys on `turn:{sid}:{n}`, so a fresh turn_number per
pass ACCUMULATES duplicate rows instead of replacing. Proof: in `9d0fb79a` one event
(`event_id 17d46ee0`) crystallized into 6 turn rows at turn_number 1,6,11,16,21,26 — 35 rows,
only **5 distinct beats**. Universal across all 15 "substantive" sessions (84f7ebea 258 rows→29
distinct; the 4,910 headline is really ~700-1000 distinct turns). **Likely also inflates the
metabolism/agent-telemetry turn counts — flag for a separate check.** Upstream fix for OpenStory:
make `insert_turn`'s key event-derived/stable, not per-pass turn_number.

**Both rungs now dedup at the source.** `rung1_uptake.build_stream` collapses turn rows whose
`event_ids` tuple was already seen (principled: same source events = same turn), keeping first
in turn order; `rung2_moves.py` imports it, so it inherits the dedup. Dedup did not weaken
Rung 1 — it STRENGTHENED it (duplicate partners had inflated the null): **median lift +0.031 →
+0.053, positive 14/14, sig 13/14, A→H +0.034 (11/14+), H→A +0.063 (13/14+)**. "Measured"
dropped 105→16 because most of the 105 were duplication-inflated single beats — the true corpus
is ~14 genuine dialogues. Re-run `rung1_uptake.py` to regenerate the clean `rung1_report.md`.

**Rung 2 piloted (deliverables in `openstory-legibility/`):**
- `rung2_moves.py` — read-only, idempotent, imports the deduped stream; classifies the HUMAN's
  A→H move toward the prior AI turn. Backends: `manual` (default, reads `rung2_labels.json`, no
  spend) and `anthropic`/`openai` (cheap model, temp 0, MERGES new labels — needs an API key,
  absent in sandbox → run on the Mac). After dedup the WHOLE instrument is **107 A→H pairs**
  across the 12 genuine dialogues (the 4,812 outlier excluded), so the full run is trivially cheap.
- `rung2_labels.json` — pilot labels (model-as-judgment, Opus) for 3 dialogues Tom ran himself
  (4f18c86c, ea7b2dcd, 84f7ebea) = **44/107 pairs**, + the taxonomy definitions.
- `rung2_report.md` — distribution + per-dialogue relational signature (generated).

**Rung 2 verdict — the instrument works, but the move ALPHABET is genre-dependent.** Human moves
classify cleanly and per-dialogue signatures discriminate (debug session `ea7b2dcd` = 12/17
`report`; scoping session `84f7ebea` = `override`/`build_on`/`direct` mix). BUT the dominant moves
are **report 52%** (paste execution results back) and **direct 20%** (approve+command) — NEITHER
in the original 7-move set — while **steelman/concede are ~absent**. This corpus is collaborative
execution, not rival-traditions debate. So the MacIntyrean deep-listening vocabulary
(steelman/concede/build-on across incommensurable frames) needs DEBATE-GENRE dialogue to exercise
it, which this single-human operational corpus does not contain. That's the real Rung-2 result and
it sharpens the paper: deep listening looks different in collaboration vs. inquiry, and we have only
the former. To study the MacIntyrean case we need rival-traditions transcripts (the 15-tradition
CRM-team dialogues), not more coding sessions.

**Rung 3 readiness:** `rung1_uptake.json` carries per-session curves + role tags; once Rung 2
labels span all 107 pairs (Mac run), "do uptake / repair / override shift as a session matures"
is computable without recompute.

**No push:** all local under `openstory-legibility/`. Nothing committed.
**Resume cue:** "resume the OpenStory legibility" / "finish Rung 2 full run" / "Rung 3 maturation".
Next increment: (a) Mac full-run `rung2_moves.py --backend openai` to label the remaining ~63
pairs; (b) decide whether to point the instrument at rival-traditions dialogue to get the
MacIntyrean move alphabet; (c) flag the replay-dup bug to OpenStory + check metabolism counts.

---

# Session 10 close (2026-06-30) — SIMULATED rival-tradition study DESIGNED + HARNESS BUILT + ANALYSIS VALIDATED.

Decision (b) above is taken: there are no human rival-tradition (dialectical) transcripts in the
corpus, so we **simulate** a Carroll vs Hoffman debate and apply Rungs 1 & 2 — a literal small
instance of the C2A2 accelerator/detector. The seam is the vault's own (ontological closure vs.
epistemic openness; `traditions/carroll/wiki.md`, `traditions/hoffman/wiki.md`).

**Pre-registered first (commit-before-run):** `openstory-legibility/sim_preregistration.md`.
Conditions LISTEN / DEAF (control) / BRIDGE; panel k=5 conversations/condition, ~16 exchanges,
one fixed seam. Falsifiers: **P1** listen cross-agent lift > deaf with separated distributions
(else instrument tracks topic not listening -> STOP); **P2** steelman+concede+build_on share
higher in listen than deaf; **P3** bridge > listen (else a publishable negative for the
second-first-language-bridge claim). Scope fixed in writing: measures AI SIMULATIONS under one
generator family, not the human thinkers.

**Built (all in `openstory-legibility/`):**
- `sim_harness.py` — two vault-grounded interlocutors (C/H seeded ONLY from `traditions/<key>/`
  wiki+prs), conditions listen/deaf(asymmetric H-blind default; `--deaf C,H` for mutual)/bridge,
  writes `sim/transcripts/<cond>/<seed>.json`, idempotent, backend anthropic|openai (needs key ->
  Mac). Hold-the-frame / no-cheap-concede persona instructions.
- `sim_analyze.py` — transcript loader + Rung-1 CROSS-AGENT role-matched lift (reuses
  rung1_uptake TF-IDF/cos, 200-shuffle perm p) over the panel; reports P1/P3 contrasts. NO model
  for Rung 1.
- Self-test fixture `sim/_toy/transcripts/{listen,deaf}/*.json` + it VALIDATES the pipeline:
  toy listen mean lift **+0.079 (3/3 sig)** vs toy deaf **+0.004 (0/3)**, P1 delta +0.075,
  distributions separated -> PASS. So the analysis detects the gap when real and would show
  overlap (fire the falsifier) when not — proven before any spend.

**One honest gap (task #12):** `sim_analyze` Rung 2 (P2 move scoring) is STUBBED — Rung 1
(P1/P3) is complete + validated. Wiring the blind rung2 classifier (roles anonymized A/B, no
condition tag) over the transcripts is the remaining contained piece; needs the API key -> Mac.

**Mac runbook (paste-safe, zsh):**
```
cd "/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project/openstory-legibility"
export OPENAI_API_KEY="sk-REPLACE"
python3 sim_harness.py --condition listen --seeds 0-4 --backend openai
python3 sim_harness.py --condition deaf   --seeds 0-4 --backend openai
python3 sim_harness.py --condition bridge --seeds 0-4 --backend openai
python3 sim_analyze.py sim/transcripts . --backend manual
```
(Then wire+run Rung 2 blind for P2.) **No push; all local.**
**Resume cue:** "resume the listening sim" / "run the Carroll-Hoffman sim".

---

# Session 11 close (2026-06-30) — SIM PANEL RAN (k=5 x3 on the Mac, Sonnet-4-6). P1 PASS, P3 NEGATIVE, P2 wired/pending.

Panel generated on physmini02 (Anthropic backend) after three fixes: clean 401/preflight, 429
retry-backoff, and a deaf-condition message sanitizer (deaf agent's filtered history ended on an
assistant turn -> Anthropic 400 "must end with a user message"; `_sanitize` merges consecutive
assistant turns + appends a user nudge; verified NO-OP on listen so conditions stay comparable).
Transcripts in `openstory-legibility/sim/transcripts/{listen,deaf,bridge}/0-4.json`. Smoke-tested
listen/0: agents hold frames, open each turn by naming the prior move, concede specific sub-points
while pressing — the steelman/concede/build-on genre we couldn't find in the coding corpus.

**Rung 1 results (deterministic, no model) — `sim_report.md`:**
- **P1 (listen > deaf): PASS, decisively.** listen +0.152 [0.138,0.165] vs deaf +0.065
  [0.059,0.075], delta +0.087, distributions FULLY SEPARATED, all 10 individually sig. The rich
  uptake is not a generator politeness artifact — cut the info flow and it drops to ~0.065.
  Caveat: deaf is ASYMMETRIC (only H blind; C still hears H), so +0.065 is a one-sided floor, not
  zero. A `--deaf C,H` (mutual) run would give the absolute floor + a dose-response (cheap follow-on).
- **P3 (bridge raises C<->H uptake): NEGATIVE — and it's the interesting result.** All-pairs looked
  +0.026, BUT that was the bridge B paraphrasing both sides (B inflates cross-agent cosine by
  construction). The registered **principals-only** test (drop B, measure C<->H) is bridge +0.143
  vs listen +0.152 = **delta -0.009, overlapping**. The interposed running-translator bridge does
  NOT accelerate the principals' mutual uptake; it slightly dilutes it. Publishable negative, and it
  sharpens the question: MacIntyre's second-first-language figure PARTICIPATES as a mature member,
  not as a paraphraser between turns — so the next bridge design to test is a participating
  bilingual interlocutor, not an interposed restater. (sim_analyze now reports BOTH all-pairs and
  principals-only; the principals correction is the registered P3.)

**P2 (move alphabet) — WIRED, not yet run (needs key -> Mac).** `sim_analyze.py --backend anthropic`
now classifies each adjacent cross-agent move (blind: classifier sees only the two texts), tallies
per condition, and tests whether the **steelman+concede+build_on** share is higher in listen than
deaf. Idempotent cache `sim/labels_sim.json`. This is the test of whether the MacIntyrean moves —
absent in the coding corpus — actually appear and track engagement in the debate genre.
Mac command: `python3 sim_analyze.py sim/transcripts . --backend anthropic` (re-reads transcripts;
no regeneration; ~ a few hundred cheap Haiku calls).

**Proof-of-concept status:** baseline capacity is built and the headline (P1) holds — we can
construct machine-speed rival-tradition dialectic AND detect listening in it, separating it from a
deaf control, fully model-free. P3-negative + the deaf-asymmetry + P2-pending are the honest open
edges. **Scope (registered):** this is detection in SIMULATED engagement under one generator family.

**No push; all local under `openstory-legibility/`.**

**Amendment 1 committed (2026-06-30, `sim_preregistration.md` bottom) — convener redesign.** Tom's
conceptual correction: MacIntyre denies general translatability, so the translator-BRIDGE was a
category error (P3-negative confirms it) — RETIRED. Replaced by a **civility-CONVENER (T)**: a
pass-through that carries content AND tone/civility (RC core), takes no side, judges nothing; runs a
checking protocol ("C said X; H, restate so C would certify it"). **Certification is by the ORIGINAL
speaker.** New measurable = certified restatement; new detector outputs = certification rate,
restatement fidelity (reuses Rung-1 cosine), and **failed-certification loci = located
incommensurability** (P3'b: failures should concentrate on the hard joints — spacetime-fundamentality,
consciousness fundamental-vs-derived — not scatter). GATE **C0** = anti-rubber-stamp: 1-in-3
restatements are deliberate strawmen the original speaker must REFUSE; if agents certify strawmen ≈ as
often as faithful, certification is void → STOP. Plus P-civility (convene vs listen civil-register share).
Registered knobs (Tom approved defaults, "will tune if promising"): strawman fraction 1/3, cert-floor
>0.6, hard-joints list. Design approved 2026-06-30; NOT yet built.

**Two runnable-now items still open:** (1) P2 on the existing sim panel —
`python3 sim_analyze.py sim/transcripts . --backend anthropic` (needs key, Mac; steelman+concede+build_on
share listen vs deaf). (2) mutual-deaf floor — `sim_harness.py --condition deaf --deaf C,H`.
**Next build:** convener harness (`--condition convene`, emit `cert_events[]`, strawman injection) +
`sim_analyze` convener block (C0 gate first, then cert-rate/fidelity/failed-loci/civility).

**Resume cue:** "build the convener" / "run P2 on the sim" / "resume the listening sim".
