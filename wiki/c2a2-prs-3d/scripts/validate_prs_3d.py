#!/usr/bin/env python3
"""
validate_prs_3d.py — Validate a generated prs_3d.html before delivery.

Checks (any failure exits non-zero):
  1. Inline JS passes `node --check` (real syntax check).
  2. Embedded data arrays parse as JSON and their counts match the source bundle.
  3. The coil layer is fully wired (COILS var, buildCoilLines, prsToggleCoils,
     coil filter pass, legend count, toggle checkbox).
  4. Brace/bracket balance of the JS body (advisory).

Usage:
  python3 validate_prs_3d.py <prs_3d.html> --source-data <prs_data.json>
"""
import argparse
import json
import re
import subprocess
import sys
import tempfile

FAIL = []


def check(cond, msg):
    print(("  ok  " if cond else " FAIL ") + msg)
    if not cond:
        FAIL.append(msg)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--source-data", required=True)
    args = ap.parse_args()

    html = open(args.html, encoding="utf-8").read()
    src = json.load(open(args.source_data, encoding="utf-8"))

    # --- pull the inline script body (the one holding the data) ---
    bodies = re.findall(r"<script>(.*?)</script>", html, re.S)
    js = next((b for b in bodies if "PRS_TRIPLETS" in b), "")
    check(bool(js), "inline JS block located")

    print("\n[1] node --check")
    try:
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
            f.write(js)
            tmp = f.name
        r = subprocess.run(["node", "--check", tmp], capture_output=True, text=True)
        check(r.returncode == 0, "node --check passes" + ("" if r.returncode == 0 else ": " + r.stderr.strip()[:300]))
    except FileNotFoundError:
        check(False, "node is available on PATH")

    print("\n[2] data counts match source")
    for name in ["PRS_TRIPLETS", "CROSS_CONNECTIONS", "FINDINGS", "COILS", "GENERATIVE"]:
        m = re.search(r"var " + name + r" = (\[.*?\]);", html, re.S)
        if not m:
            check(False, "%s array present" % name)
            continue
        try:
            arr = json.loads(m.group(1).replace("<\\/", "</"))
        except Exception as e:
            check(False, "%s parses as JSON (%s)" % (name, e))
            continue
        want = len(src[name])
        check(len(arr) == want, "%s count = %d (source %d)" % (name, len(arr), want))

    print("\n[2b] data content populated (guards against empty-field parse regressions)")
    def field_filled(name, key):
        m = re.search(r"var " + name + r" = (\[.*?\]);", html, re.S)
        if not m:
            return None
        arr = json.loads(m.group(1).replace("<\\/", "</"))
        if not arr:
            return 0.0
        return sum(1 for r in arr if str(r.get(key, "")).strip()) / len(arr)
    for name, key in [("PRS_TRIPLETS", "resource"), ("CROSS_CONNECTIONS", "question"),
                      ("FINDINGS", "programs"), ("FINDINGS", "finding"), ("COILS", "label"),
                      ("GENERATIVE", "source"), ("GENERATIVE", "target")]:
        frac = field_filled(name, key)
        check(frac is not None and frac >= 0.95,
              "%s.%s populated on %s of records" % (name, key, "n/a" if frac is None else "%.0f%%" % (frac * 100)))

    print("\n[3] coil layer wired")
    check("function buildCoilLines()" in html, "buildCoilLines defined")
    check("buildCoilLines();" in html, "buildCoilLines called in init")
    check("function prsToggleCoils(" in html, "prsToggleCoils defined")
    check("coilLines.forEach" in html, "coil visibility pass present")
    check('id="prs-chk-coils"' in html, "coil toggle checkbox present")
    check("function buildGenerativeChains()" in html, "buildGenerativeChains defined")
    check("buildGenerativeChains();" in html, "buildGenerativeChains called in init")
    check('id="prs-chk-generative"' in html, "generative toggle checkbox present")
    check("Synergistic coil (' +" in html or "Synergistic coil ('+" in html, "legend coil count present")

    # Advisory only: literal parens/braces inside data strings make raw counts
    # uneven even when the JS is valid. node --check (above) is authoritative.
    print("\n[4] brace/bracket balance (advisory only - node --check is authoritative)")
    for op, cl in [("{", "}"), ("(", ")"), ("[", "]")]:
        bal = js.count(op) - js.count(cl)
        print(("  ok  " if bal == 0 else " note ") + "'%s%s' raw balance = %d" % (op, cl, bal))

    print("\n=== %s ===" % ("PASS" if not FAIL else "FAILED: %d issue(s)" % len(FAIL)))
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
