#!/bin/bash
# Tests for scripts/voice_faq.py -- specifically the drop guard added 2026-08-05.
#
# The guard exists because `merge` rebuilds wiki/voice_guide_faq.json by iterating
# the knowledge/ inventory: any key holding Q&A that the inventory no longer names
# is not emitted, and its pairs disappear from the published file. Correct once, at
# the end of a key migration; silent data loss otherwise.
#
# voice_faq.py derives ROOT from its own location (parent.parent), so each case
# builds a throwaway tree with the script copied into $T/scripts/ and never touches
# the real repo. Every assertion below is driven through its failure path -- an
# assertion never watched failing is not one.
set -uo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$REPO/scripts/voice_faq.py"
PASS=0
FAIL=0

ok()   { echo "  ok   $1"; PASS=$((PASS + 1)); }
bad()  { echo "  FAIL $1"; FAIL=$((FAIL + 1)); }
check() { if [ "$1" = "$2" ]; then ok "$3"; else bad "$3 (want '$2', got '$1')"; fi; }

# Build a throwaway repo. $1 = the published FAQ's features array (JSON).
# Inventory is always the same two current keys.
make_tree() {
  T="$(mktemp -d)"
  mkdir -p "$T/scripts" "$T/wiki/voice_guide/knowledge" "$T/voice_faq"
  cp "$SCRIPT" "$T/scripts/voice_faq.py"

  cat > "$T/wiki/voice_guide/knowledge/cur.one.md" <<'EOF'
---
state_key: cur.one
title: Current One
---
Body of the first current feature.
EOF
  cat > "$T/wiki/voice_guide/knowledge/cur.two.md" <<'EOF'
---
state_key: cur.two
title: Current Two
---
Body of the second current feature.
EOF

  python3 - "$T" "$1" <<'PY'
import json, sys
t, feats = sys.argv[1], json.loads(sys.argv[2])
faq = {"generated_at": "2026-01-01 00:00", "feature_count": len(feats),
       "qa_count": sum(len(f.get("qa", [])) for f in feats),
       "target_total": 100, "features": feats}
open(t + "/wiki/voice_guide_faq.json", "w").write(json.dumps(faq, indent=2))
# State names both current keys with the hashes build_inventory will compute, so
# the diff is clean and `still_missing` is the only other gate in play.
open(t + "/voice_faq/state.json", "w").write(json.dumps({"features": {}, "qa_total": 0}))
PY

  # Authored Q&A covering both current keys, so the run is otherwise valid.
  cat > "$T/qa.json" <<'EOF'
{
  "cur.one": [{"q": "What is one?", "a": "The first."},
              {"q": "How does one work?", "a": "Like this."},
              {"q": "Why one?", "a": "Because."}],
  "cur.two": [{"q": "What is two?", "a": "The second."},
              {"q": "How does two work?", "a": "Like that."},
              {"q": "Why two?", "a": "Also because."}]
}
EOF
}

faq_qa_count() { python3 -c "import json,sys;print(json.load(open(sys.argv[1]))['qa_count'])" "$1"; }

echo
echo "the guard refuses when a merge would drop Q&A:"
make_tree '[{"key":"old.tab.html","title":"Old Tab","qa":[{"q":"a?","a":"b"},{"q":"c?","a":"d"}]},
            {"key":"cur.one","title":"Current One","qa":[{"q":"kept?","a":"yes"}]}]'
BEFORE="$(cat "$T/wiki/voice_guide_faq.json")"
OUT="$(python3 "$T/scripts/voice_faq.py" merge "$T/qa.json" 2>&1)"
RC=$?
check "$RC" "1" "exits 1 rather than dropping"
grep -q "REFUSING" <<<"$OUT" && ok "says REFUSING" || bad "no REFUSING in output"
grep -q "old.tab.html (2 pair(s))" <<<"$OUT" && ok "names the key and its pair count" \
  || bad "did not name old.tab.html with its count"
grep -q "would drop 2 pair(s)" <<<"$OUT" && ok "totals the pairs at risk" \
  || bad "did not total the pairs at risk"
grep -q "cur.one" <<<"$OUT" && bad "wrongly listed a key still in the inventory" \
  || ok "does not list keys the inventory still names"
check "$(cat "$T/wiki/voice_guide_faq.json")" "$BEFORE" "left the published FAQ untouched"
[ -f "$T/voice_faq/report.md" ] && bad "wrote a report on a refusal" || ok "wrote no report"
rm -rf "$T"

echo
echo "--dry-run predicts the refusal instead of reporting a clean run:"
make_tree '[{"key":"old.tab.html","title":"Old Tab","qa":[{"q":"a?","a":"b"}]}]'
OUT="$(python3 "$T/scripts/voice_faq.py" merge "$T/qa.json" --dry-run 2>&1)"
check "$?" "1" "--dry-run exits 1 too"
grep -q "REFUSING" <<<"$OUT" && ok "--dry-run says REFUSING" || bad "--dry-run reported a clean run"
rm -rf "$T"

echo
echo "--allow-drop permits it, and the drop stays legible:"
make_tree '[{"key":"old.tab.html","title":"Old Tab","qa":[{"q":"a?","a":"b"},{"q":"c?","a":"d"}]},
            {"key":"cur.one","title":"Current One","qa":[{"q":"kept?","a":"yes"}]}]'
OUT="$(python3 "$T/scripts/voice_faq.py" merge "$T/qa.json" --allow-drop 2>&1)"
check "$?" "0" "exits 0 with --allow-drop"
check "$(faq_qa_count "$T/wiki/voice_guide_faq.json")" "7" "published 7 pairs (1 kept + 6 authored)"
python3 -c "
import json,sys
ks={f['key'] for f in json.load(open(sys.argv[1]))['features']}
sys.exit(0 if ks=={'cur.one','cur.two'} else 1)" "$T/wiki/voice_guide_faq.json" \
  && ok "old key is gone from the published file" || bad "old key survived or a key is missing"
grep -q "Dropped from the published FAQ" "$T/voice_faq/report.md" \
  && ok "report names the drop" || bad "report is silent about the drop"
grep -q 'old.tab.html` — 2 pair(s)' "$T/voice_faq/report.md" \
  && ok "report names which key and how many pairs" || bad "report does not name the key/count"
rm -rf "$T"

echo
echo "the guard does not misfire:"
make_tree '[{"key":"cur.one","title":"Current One","qa":[{"q":"kept?","a":"yes"}]}]'
OUT="$(python3 "$T/scripts/voice_faq.py" merge "$T/qa.json" 2>&1)"
check "$?" "0" "no orphan keys -> merges without the flag"
check "$(faq_qa_count "$T/wiki/voice_guide_faq.json")" "7" "kept the existing pair and added six"
rm -rf "$T"

# An orphan key carrying an EMPTY list is not data; refusing on it would block a
# migration for nothing.
make_tree '[{"key":"old.tab.html","title":"Old Tab","qa":[]},
            {"key":"cur.one","title":"Current One","qa":[{"q":"kept?","a":"yes"}]}]'
OUT="$(python3 "$T/scripts/voice_faq.py" merge "$T/qa.json" 2>&1)"
check "$?" "0" "an orphan key with zero pairs is not a drop"
rm -rf "$T"

echo
echo "the pre-existing gate still fires:"
make_tree '[{"key":"cur.one","title":"Current One","qa":[{"q":"kept?","a":"yes"}]}]'
echo '{"cur.one":[{"q":"only one?","a":"yes"}]}' > "$T/qa.json"
OUT="$(python3 "$T/scripts/voice_faq.py" merge "$T/qa.json" 2>&1)"
check "$?" "1" "a feature with no Q&A at all still refuses"
grep -q "cur.two" <<<"$OUT" && ok "names the uncovered feature" || bad "did not name cur.two"
rm -rf "$T"

echo
echo "-------------------------------------------"
echo "$PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] || exit 1
