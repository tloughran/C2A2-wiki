#!/bin/bash
# Tests for the Vault Life page (Metabolism > Vault Life).
# Why each assertion exists:
#  - the page is built from a template by substitution, so an unfilled marker
#    ships a page whose script will not parse and the subtab opens black;
#  - captions carry the narration's tallies, filled by code; an unfilled
#    placeholder or a stale hard-coded number is exactly the "stale every new
#    day" failure this page exists to end;
#  - the Metabolism page must still carry the subtab bar after its own regen,
#    because the builder rewrites it from a Python template every morning.
# Run from the repo root:  bash scripts/test_vault_life_page.sh
set -u
cd "$(dirname "$0")/.."
PASS=0; FAIL=0
ok()   { PASS=$((PASS+1)); echo "  ok   $1"; }
bad()  { FAIL=$((FAIL+1)); echo "  FAIL $1"; }

PAGE=wiki/metabolism/vault_life.html
TPL=wiki/metabolism/scripts/vault_life_template.html
BUILDER=wiki/metabolism/scripts/build_metabolism_view.py

echo "vault_life page"
[ -f "$PAGE" ] && ok "page exists" || { bad "page missing: $PAGE (run scripts/video/build_vault_timeline.py)"; }
for m in '/*__DATA__*/' '/*__CAPTIONS__*/' '/*__FILM_URL__*/'; do
  if grep -qF "$m" "$PAGE" 2>/dev/null; then bad "unfilled marker $m"; else ok "marker filled $m"; fi
  if [ "$(grep -cF "$m" "$TPL")" = "1" ]; then ok "template has $m once"; else bad "template must have $m exactly once"; fi
done

# captions: pull the CAPTIONS literal and check it in python
python3 - "$PAGE" <<'PY' && ok "captions parse, >=5, no unfilled {placeholders}, dated in order" || bad "captions check"
import json, re, sys
src = open(sys.argv[1], encoding="utf-8").read()
m = re.search(r"const CAPTIONS=(\[.*?\]);\n", src)
assert m, "CAPTIONS literal not found"
caps = json.loads(m.group(1).replace("<\\/", "</"))
assert len(caps) >= 5, len(caps)
for c in caps:
    assert set(c) == {"start", "title", "text"}, c
    assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", c["start"]), c["start"]
    assert "{" not in c["text"] and "}" not in c["text"], c["text"]
    assert c["text"].strip(), c
starts = [c["start"] for c in caps]
assert starts == sorted(starts), starts
m = re.search(r"const DATA=(\{.*?\});\nconst CAPTIONS", src, re.S)
assert m, "DATA literal not found"
d = json.loads(m.group(1).replace("<\\/", "</"))
assert d["_meta"]["files"] > 0 and d["_meta"]["last_file"] == caps[-1]["start"], "last caption must sit on the last file date"
assert str(d["_meta"]["files"]).replace("", "") and f"{d['_meta']['files']:,}" in caps[-1]["text"], "today caption must quote the live file count"
PY

# the page's script must parse
python3 - "$PAGE" > /tmp/vault_life_script.js <<'PY'
import re, sys
src = open(sys.argv[1], encoding="utf-8").read()
sys.stdout.write(re.search(r"<script>(.*)</script>", src, re.S).group(1))
PY
node --check /tmp/vault_life_script.js 2>/dev/null && ok "page script parses (node --check)" || bad "page script does not parse"

echo "metabolism subtab bar"
grep -q 'id="view-vault"' "$BUILDER" && ok "builder template carries the Vault Life view" || bad "builder template lacks #view-vault"
grep -q 'data-src="vault_life.html"' "$BUILDER" && ok "iframe is lazy (data-src)" || bad "iframe must be lazy: data-src, not src"
grep -q "dataset.src + '?v=' + Date.now()" "$BUILDER" && ok "iframe is force-freshed on open" || bad "iframe src must carry ?v= on open (iframe-asset rule)"
if [ -f wiki/metabolism/metabolism_view.html ]; then
  grep -q 'id="view-vault"' wiki/metabolism/metabolism_view.html && ok "built metabolism page carries the bar" || bad "built metabolism page lacks the bar (regen it)"
fi

echo "$PASS passed, $FAIL failed"
[ "$FAIL" = 0 ]
