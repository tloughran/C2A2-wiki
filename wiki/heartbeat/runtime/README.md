# Heartbeat runtime (vendored)

This is the **cloud-runnable** copy of the heartbeat poller, vendored into the repo so a
GitHub Actions cron (or any runner) can refresh the public digest without a Mac in the loop.

## Contents
- `app.py` — the poller/export runtime. **Stdlib only** (argparse, json, sqlite3, urllib, xml,
  http.server …) — no pip install required. Identical to the reference runtime in the local
  delivery bundle (`C2A2_Heartbeat_Explorer_Update_*_bundle/`, which is gitignored because it
  also ships a stale `explorer.html` that clobbers; only `app.py` is vendored here).
- `config/sources.json` — the **canonical feed list** (19 feeds across 7 lanes as of
  2026-06-26). Schema is fixed by the `Source` dataclass in `app.py` (id, name, type, url,
  home_url, enabled) — **do not add a `category` key** (it would crash `load_sources()`; lane
  membership lives in `backend/build_roster.py`).

## How it's used
`backend/refresh_snapshot.sh` drives a one-shot poll in `HB_RUNTIME_DIR` mode:
```bash
HB_RUNTIME_DIR="wiki/heartbeat/runtime" \
HB_SOURCES_CONFIG="wiki/heartbeat/runtime/config/sources.json" \
  bash wiki/heartbeat/backend/refresh_snapshot.sh
```
It starts `app.py` on a local port, polls once, reads `/api/digest`, exports
`data/digest.json` (+ a changed-only snapshot), summarizes new items via the cc-broker,
rebuilds the roster, and stamps assets. SQLite runs on the runner's local disk (fine in CI;
the mounted-disk I/O error only happens inside the Cowork sandbox).

## ⚠️ Single source of truth — avoid drift
There are now potentially **two** `sources.json`: this vendored one and the bundle's local
copy. **This vendored copy is canonical.** Converge by pointing the Mac scheduled task /
`launchd` plist at `HB_RUNTIME_DIR=wiki/heartbeat/runtime` too, and retiring the bundle copy
for refresh purposes. Until then, keep them identical when you edit feeds. (`build_roster.py`
warns loudly if a configured source isn't assigned to a lane, so an out-of-sync feed can't
silently vanish from the roster.)

## Re-syncing from the bundle (if the reference runtime is updated)
```bash
cp "<bundle>/reference-runtime/c2a2_heartbeat/app.py" wiki/heartbeat/runtime/app.py
python3 -m py_compile wiki/heartbeat/runtime/app.py   # sanity
```
The `data/.broker_device_id` stays gitignored and per-environment; in CI it is written from
the `HB_BROKER_DEVICE_ID` secret so the cron has a stable, separately-metered broker identity.
