#!/usr/bin/env bash
# test_regen_guard.sh — drive regen_sociogram.sh's substrate-skip guard through
# its FAILURE path, then confirm it recovers.
#
# Run:  bash wiki/c2a2-wiki-narration/test_regen_guard.sh
#
# Why: the guard exists because on 2026-08-03 a namespace rename orphaned 1162
# of 3084 agent-activity substrate edges and every validator stayed green. The
# only signal was a "skipped N" line on stdout. A guard that has never been
# watched failing is not a guard, so this reproduces the exact condition by
# pointing the build at an agent_node_edges.json whose targets cannot resolve.
#
# Costs two full regens (~3-4 min). Restores every file it touches, including
# on failure, via the EXIT trap.

set -uo pipefail

AGD="$(cd "$(dirname "$0")" && pwd)"
WIKI="$(cd "$AGD/.." && pwd)"
AGENTS="$WIKI/agents/openstory/agent_node_edges.json"
META="$AGD/scripts/build_meta.json"
BACKUP_AGENTS="$(mktemp -t agents_real.XXXXXX)"
BACKUP_META=""

cleanup() {
  [ -f "$BACKUP_AGENTS" ] && cp "$BACKUP_AGENTS" "$AGENTS" && rm -f "$BACKUP_AGENTS"
  if [ -n "$BACKUP_META" ] && [ -f "$BACKUP_META" ]; then
    cp "$BACKUP_META" "$META"; rm -f "$BACKUP_META"
  fi
  echo "[test] restored agent_node_edges.json and build_meta.json"
}
trap cleanup EXIT

PASS=0; FAIL=0
ok()  { PASS=$((PASS+1)); echo "  ok   $1"; }
bad() { FAIL=$((FAIL+1)); echo "  FAIL $1"; }

[ -f "$AGENTS" ] || { echo "no agent_node_edges.json at $AGENTS"; exit 2; }
[ -f "$META" ]   || { echo "no build_meta.json — run regen_sociogram.sh once first"; exit 2; }
cp "$AGENTS" "$BACKUP_AGENTS"
BACKUP_META="$(mktemp -t meta_real.XXXXXX)"; cp "$META" "$BACKUP_META"

BASE_SKIPPED=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["substrate_skipped"])' "$META")
BASE_NODES=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["nodes"])' "$META")
echo "[test] baseline: substrate_skipped=$BASE_SKIPPED nodes=$BASE_NODES"

# ── Break it the way reality broke it: targets that resolve to nothing ───────
echo "[test] mangling substrate targets so they cannot resolve…"
python3 - "$AGENTS" <<'PY'
import json,sys
p=sys.argv[1]; d=json.load(open(p))
n=0
for e in d.get('coref_substrate',[]):
    e['target']='ZZZ-nonexistent/'+str(e.get('target',''))
    n+=1
json.dump(d,open(p,'w'))
print("  mangled %d substrate targets"%n)
PY

echo "[test] regen (must be REJECTED)…"
OUT1="$(mktemp -t guardtest1.XXXXXX)"
bash "$AGD/regen_sociogram.sh" > "$OUT1" 2>&1; RC=$?

if [ "$RC" -ne 0 ]; then ok "exited non-zero ($RC)"; else bad "exited 0 — guard did not fire"; fi
if grep -q 'substrate edges skipped jumped' "$OUT1"; then ok "named the skip jump"; else bad "no skip-jump message"; fi
if grep -q 'namespace change' "$OUT1"; then ok "pointed at the likely cause"; else bad "no cause hint"; fi
if grep -q 'must not be published' "$OUT1"; then ok "warned the artifact is untrustworthy"; else bad "no artifact warning"; fi

# The critical property: a rejected build must NOT become the new baseline.
NOW_SKIPPED=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["substrate_skipped"])' "$META")
if [ "$NOW_SKIPPED" = "$BASE_SKIPPED" ]; then
  ok "baseline preserved (still $BASE_SKIPPED, not the rejected value)"
else
  bad "baseline was overwritten by a REJECTED build ($BASE_SKIPPED -> $NOW_SKIPPED) — a re-run would now pass"
fi
rm -f "$OUT1"

# ── Restore reality and confirm the guard lets a good build through ──────────
echo "[test] restoring real agent data, regen (must PASS)…"
cp "$BACKUP_AGENTS" "$AGENTS"
OUT2="$(mktemp -t guardtest2.XXXXXX)"
bash "$AGD/regen_sociogram.sh" > "$OUT2" 2>&1; RC2=$?
if [ "$RC2" -eq 0 ]; then ok "good build accepted (rc 0)"; else bad "good build REJECTED (rc $RC2) — guard is too tight"; fi
if grep -q 'substrate skip delta OK' "$OUT2"; then ok "reported the delta on success"; else bad "no success delta line"; fi
FINAL=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["substrate_skipped"])' "$META")
if [ "$FINAL" = "$BASE_SKIPPED" ]; then ok "baseline back to $BASE_SKIPPED"; else bad "baseline drifted to $FINAL"; fi
rm -f "$OUT2"

echo
echo "passed: $PASS   failed: $FAIL"
[ "$FAIL" -eq 0 ]
