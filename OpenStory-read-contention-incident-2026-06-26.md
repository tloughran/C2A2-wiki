# OpenStory external-read contention — incident & engineering history

**Date:** 2026-06-26
**Component:** C2A2 wiki "Agent Map" + Sociogram agent-activity layer, both derived from OpenStory's `open-story.db`
**Audience:** OpenStory architects (and the C2A2 maintainer)
**Status:** Fix shipped locally (not yet published); awaiting a clean run at the quiet 06:15 window to confirm.

---

## 1. One-paragraph summary

C2A2 reads OpenStory's live SQLite database (`open-story.db`) from a separate process, over a FUSE mount, to build two wiki views. Those views silently froze for ~18 days. Root cause: our extractor ran a whole-file integrity scan (`PRAGMA quick_check`) against the **live, WAL-mode, actively-written** database, and over the mount that scan reliably trips with *"database disk image is malformed / Page N is never used"* whenever a write lands mid-scan. The extractor correctly refused to emit data (fail-loud), but the failure only went to a run log, so the staleness was invisible. We have re-architected our reader to copy the DB to local disk and read the copy, and we fail loud + surface a status file. **The deeper issue is generic: reading a hot WAL database over a mount, from a different process, is not safely doable without a consistent-snapshot contract — and that's where we'd value your input.**

---

## 2. Environment / facts

- `open-story.db`: SQLite in **WAL mode**. Main file ≈ **2.0 GB**; uncheckpointed **`-wal` ≈ 363 MB**; live `-shm`. Continuously written by the OpenStory runtime.
- Event volume: ≈ **261,000+ events**, spanning 2026-03-30 → present; per-day writes every day (tens of sessions/day).
- Reader (C2A2) is a **different process**, in a sandbox, reaching the DB over a **FUSE mount** (`/sessions/<id>/mnt/Documents/.../open-story.db`). Read-only intent.
- Reader workload: full scans of `sessions` and `events` (the `events` scan reads the `payload` blob per row and does regex/JSON parsing → the connection is held **~30–40 s** per extraction).
- All failure reproductions below were run **~22:00–22:45 local time — OpenStory's peak write/checkpoint churn.** The production reader runs at **06:15** (overnight quiet window).

---

## 3. Symptom & root cause

**Symptom.** The "Agent Map" tab (`agents_tab.html`) showed no new agent runs after ~June 6; its embedded telemetry was frozen at `generated: 2026-06-08`. The Sociogram's agent-activity layer (`agent_node_edges.json`) was frozen at June 11. The daily refresh task *reported as having run every day.*

**Root cause (confirmed from the task's own run transcript).** Our connect helper opened the live DB `?mode=ro` and ran `PRAGMA quick_check` as an integrity guard. Over the mount, while OpenStory was mid-write, that whole-file scan returned:

```
sqlite3.DatabaseError: database disk image is malformed
PRAGMA quick_check -> "... Page 413694 is never used ...", "Rowid N out of order"
```

So the extractor aborted (correctly — house rule is "fail loud, never emit garbage"), the injector saw no new data ("No change"), and the HTML kept serving June-8 data. A second, independent gap: **no scheduled task ran the node-edges extractor at all**, so that feed had no refresher even when the DB was readable.

Our read of the signature: the `-malformed / page never used / rowid out of order` family here is **not on-disk corruption** — it's an **inconsistent point-in-time view**. WAL-mode correctness depends on the `-wal` + `-shm` shared-memory coordination between writer and reader. Across the FUSE boundary (native writer ↔ sandboxed reader), that coordination isn't honored, so a long read can observe main-file pages and WAL state from different instants.

---

## 4. What we tried (chronological), and results

| # | Approach | Result at peak churn | Why |
|---|----------|----------------------|-----|
| 1 | Plain `mode=ro`, single aggregate read (`COUNT`/`MAX`) | **OK** earlier (~21:00, quieter); intermittent | Short read; low odds of overlapping a write |
| 2 | SQLite **backup API** (`src.backup(dst)`) from `mode=ro` source | **FAIL** — `malformed` | Whole-file page copy, same exposure as `quick_check` |
| 3 | **File copy** of `db`+`-wal`+`-shm` to local `/tmp`, then open | **FAIL** — `malformed` | 2 GB copy ≈ 14 s; writer commits during copy → `db`/`wal` mismatch (torn) |
| 4 | `mode=ro` + **retry whole extraction** (5×) | **FAIL 5/5** | The ~35 s `events` scan reliably overlaps a write; every attempt tears |
| 5 | `immutable=1`, **short** scan (`length(payload)` only) | **OK 3/3**, ~minutes behind | Ignores `-wal`; reads stable main file; short hold avoids checkpoints |
| 6 | `immutable=1`, **full** extractor (~35 s, reads full payloads) | **FAIL 5/5** | Long hold overlaps a **checkpoint** that rewrites main-file pages → tears even immutable |
| 7 | Copy **main file only** (no `-wal`) to local, open `immutable`, local `quick_check`, retry | **FAIL 4/4** at peak; **correctly detected** torn copy and refused | 2 GB copy still torn by ongoing checkpoints; local check caught it (`Rowid out of order`) |

Key empirical takeaways:
- **Ordinary reads succeed; whole-file scans and long reads fail** — proportional to how long the reader is exposed to the live writer.
- `immutable=1` (read main file, ignore WAL) is **immune to ordinary commits** but **not to checkpoints** that rewrite the main file during a long read.
- A **local copy decouples** the long read from the writer, but **the copy itself is a long exposure** (~14 s for 2 GB) and is torn if a checkpoint lands during it.
- We never observed a green full run during the 22:00–22:45 peak window. The sibling **metabolism** consumer (same DB, backup-API snapshot) succeeds at **05:57** — consistent with this being a **timing/contention** problem, not corruption.

---

## 5. What we're settling for (shipped fix)

A shared reader (`openstory_db.py`) used by both extractors:

1. **Copy the main DB file (only, no `-wal`) to local disk.**
2. **Open the local copy `immutable=1`** and run a **local** `quick_check(1)`.
3. If the local copy fails the check (a checkpoint tore it mid-copy), **raise → `run_with_retry` re-copies**; after N tries, **fail loud** (and we now classify persistent failure against a quiet DB as genuine corruption needing `.recover`).
4. The extractor does all slow work **against the static local copy**, so the long read has zero exposure to the live writer.
5. We dropped the `quick_check` on the *live* file entirely (it was the tripwire).
6. The daily task now **also runs the node-edges extractor**, writes a `REFRESH_STATUS.md` (PASS/FAIL) every run, and that status is **surfaced in the morning system-health report** so a stall can't hide again.

**Accepted tradeoffs / residual risk:**
- **Freshness = last checkpoint.** Omitting `-wal` means we lose the uncheckpointed tail (empirically only **~minutes / tens of events** behind — fine for a daily snapshot, but bounded by *your* checkpoint cadence; see §6).
- **At peak write+checkpoint churn the copy can still tear**, and we fail loud rather than publish. We rely on running at the **quiet 06:15 window**. This is robust but not "any-time."
- **Cost:** a 2 GB copy per attempt is heavy. Acceptable for a once-daily background job; not acceptable for frequent/interactive reads.

---

## 6. Questions / asks for the OpenStory architects

These would let external consumers read **safely and at any time**, and would shrink our freshness gap:

1. **Checkpoint cadence.** What are your WAL settings (`PRAGMA wal_autocheckpoint`, `journal_size_limit`, `synchronous`, `mmap_size`, `busy_timeout`)? A 363 MB uncheckpointed WAL suggests autocheckpoint is off or very large. More frequent **TRUNCATE checkpoints** would (a) shrink the `immutable`-reader staleness gap and (b) narrow the torn-copy window.
2. **A consistent snapshot contract — the clean fix.** Could OpenStory periodically publish a consistent read copy that external consumers target instead of the hot file? Options, roughly in order of our preference:
   - a cadence'd **`VACUUM INTO` / `.backup`** to a sidecar path (e.g., `open-story.snapshot.db`) that we read instead of the live file;
   - a tiny **read endpoint / query API** so consumers never touch the file;
   - a **read replica** or WAL-shipping target.
3. **WAL over a mount.** Can you confirm our read of the failure — that WAL `-shm` coordination is not valid across the native-writer ↔ mounted-reader boundary, so any concurrent long read is unsafe? If you already expose a safe external-read mode, we'd switch to it.
4. **Writer transaction shape.** Does the runtime hold **long write transactions** (which extend the contention window), or many short commits? Affects how risky any concurrent read is.
5. **Is WAL even the right mode here** given known external readers, or would a different journal mode + a published snapshot serve consumers better without changing your write path?

We're happy to adapt the C2A2 side to whatever contract you prefer — a published snapshot file on a cadence would let us delete all of the copy/retry machinery above and just read a clean file.

---

## 7. Files touched (C2A2 side, local only — not yet published)

- **NEW** `wiki/agents/openstory/openstory_db.py` — shared copy-to-local + retry/fail-loud reader.
- `wiki/agents/openstory/extract_openstory_agent_data.py`, `extract_agent_node_refs.py` — route through it; removed the live-file `quick_check` guard.
- `Scheduled/openstory-agents-telemetry-refresh/SKILL.md` — wires the node-edges feed; explicit mount paths; writes `REFRESH_STATUS.md`.
- `Scheduled/morning-system-health/SKILL.md` — surfaces `REFRESH_STATUS.md`.

Verification still open: a clean full end-to-end run at the quiet 06:15 window (peak-churn testing only ever exercised the fail-loud path, which behaved correctly).
