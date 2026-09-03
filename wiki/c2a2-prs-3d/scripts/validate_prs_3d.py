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


def js_func_body(html, name):
    """Return the source of `function <name>(...)` up to its matching closing brace,
    or '' if absent. Lets a check be scoped to one function instead of the whole file
    (e.g. 'resetCamera restores the orbit', not 'the file mentions autoOrbit')."""
    i = html.find("function %s(" % name)
    if i < 0:
        return ""
    j = html.find("{", i)
    if j < 0:
        return ""
    depth = 0
    for k in range(j, len(html)):
        if html[k] == "{":
            depth += 1
        elif html[k] == "}":
            depth -= 1
            if depth == 0:
                return html[i:k + 1]
    return ""


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

    # [3b] Readouts must be POPULATED, not merely present. The triplet counter
    # shipped reading "Showing ... triplets" for months because updatePrsCount()
    # was only ever called from applyPRSFilters() — nothing ran it on load, so a
    # viewer who touched no filter never saw a number. Assert the init call, not
    # the element. (2026-09-03)
    check(html.count("updatePrsCount();") >= 2, "updatePrsCount called on load, not only from applyPRSFilters")
    check('id="prs-build-stamp"' in html and "PRS_BUILD_TS" in html, "build stamp present and timestamped")
    check("Cross-tradition link (' +" in html, "legend cross-connection count present")
    check("Pattern-detector findings: ' +" in html, "legend findings count present")
    check("prs-filter-count" in html, "per-tradition counts present")
    # [3c] Time control must be month-resolution over `date`. A year-step slider
    # over pub_year cannot separate the 560 triplets that share pub_year 2026.
    check('id="prs-month-slider"' in html, "month-resolution time slider present")
    check("function setMonthThreshold(" in html, "setMonthThreshold defined")
    check("yearThreshold" not in html, "no residual year-resolution threshold")

    # [3d] Load profile + camera orbit (2026-09-03). Three defects this guards:
    #  (a) the old default radius of 50 framed only ~95% of node centres, so the
    #      view opened on a wall of nodes and the structure's shape was invisible;
    #  (b) a per-frame rotation constant makes the rate a function of the viewer's
    #      hardware — measured 2.6fps headless vs 60fps on a GPU, a 23x spread —
    #      so the orbit MUST integrate against elapsed time;
    #  (c) an orbit that does not yield fights the viewer the moment they drag.
    reset_fn = js_func_body(html, "resetCamera")
    animate_fn = js_func_body(html, "animate")
    theta_lines = [l for l in animate_fn.splitlines() if "cameraTheta" in l and "+=" in l]

    check("PRS_LOAD_RADIUS = 50 + 2 * PRS_ZOOM_STEP" in html,
          "load radius derived from the zoom step, not a bare literal")
    check("var cameraRadius = PRS_LOAD_RADIUS;" in html,
          "camera opens at the load radius")
    check(bool(reset_fn) and "PRS_LOAD_RADIUS" in reset_fn and "autoOrbit = true" in reset_fn,
          "resetCamera restores the load profile, orbit included")
    check(len(theta_lines) == 1 and "dt" in theta_lines[0],
          "orbit integrates elapsed time, not frames (rate must not depend on fps)")
    check("Math.min((nowT - orbitLastT) / 1000, 0.25)" in html,
          "orbit dt clamped, so a backgrounded tab does not resume with a jump")
    check(html.count("autoOrbit = false;") >= 2,
          "orbit yields to the viewer on both drag and wheel")

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
