#!/usr/bin/env bash
# diagnose_openstory_db.sh — decide: transient (main-only snapshot artifact) vs real corruption.
#
# Copies main + -wal + -shm to a scratch copy and lets SQLite apply the WAL, then
# quick_checks the reconciled copy. The LIVE db is only read (cp); the running
# OpenStory runtime/sim is never paused or written. Operates entirely on the copy.
set -uo pipefail
DB="$HOME/Documents/Non-Claude Projects/OpenStory/data/open-story.db"
[ -f "$DB" ] || { echo "DB not found: $DB"; exit 2; }

T="$(mktemp -d)"; trap 'rm -rf "$T"' EXIT
echo "live db size: $(stat -f %z "$DB" 2>/dev/null || stat -c %s "$DB")  wal: $(stat -f %z "$DB-wal" 2>/dev/null || echo 0)"

# A) main-only copy (what connect_ro does today) — immutable, no WAL
cp "$DB" "$T/main_only.db"
echo "--- A) MAIN-ONLY (current snapshot strategy) ---"
python3 - "$T/main_only.db" <<'PY'
import sqlite3,sys,urllib.parse
p=sys.argv[1]
con=sqlite3.connect("file:%s?immutable=1"%urllib.parse.quote(p),uri=True)
print("quick_check:",con.execute("PRAGMA quick_check(1)").fetchone()[0]); con.close()
PY

# B) main + wal + shm, reconciled (apply committed WAL frames), then check
cp "$DB" "$T/recon.db"
cp "$DB-wal" "$T/recon.db-wal" 2>/dev/null || true
cp "$DB-shm" "$T/recon.db-shm" 2>/dev/null || true
echo "--- B) MAIN+WAL RECONCILED (proposed strategy) ---"
python3 - "$T/recon.db" <<'PY'
import sqlite3,sys
p=sys.argv[1]
try:
    con=sqlite3.connect(p)                       # RW on the COPY -> applies WAL
    con.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    qc=con.execute("PRAGMA quick_check(1)").fetchone()[0]
    print("quick_check:",qc)
    if qc=="ok":
        for t in ("sessions","events","patterns"):
            print("  %s=%d"%(t,con.execute("SELECT COUNT(*) FROM %s"%t).fetchone()[0]))
    con.close()
except Exception as e:
    print("ERROR:",e)
PY
echo "--- verdict ---"
echo "If A fails but B is 'ok' -> data intact; snapshot must include the WAL (transient/strategy)."
echo "If B also fails         -> genuine on-disk corruption; run sqlite3 '.recover' on the Mac."
