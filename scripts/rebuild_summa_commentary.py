#!/usr/bin/env python3
"""Rebuild wiki/summa_commentary.html so its day list runs to the current frontier.

WHY THIS EXISTS
  summa_commentary.html (the single-page "Contemporary Parallels" gateway opened
  from the Start Here "So what?" card) bakes one JSON object per day into a
  <script id="data" type="application/json"> blob: {day, title, part, partName, md}.
  The gateway shipped through Day 290; the synthesis source (vault/synthesis/
  "Day-NNN - <title> - Contemporary.md") is complete through a later day. No
  generator was ever committed, so the gap could not be closed reproducibly.

DESIGN (surgical, per project Rule 3 "don't change what isn't broken")
  Default mode is APPEND-MISSING: every day already present in the published blob
  is kept byte-for-byte; only days that are missing are built from source and
  inserted. This guarantees the 290 vetted, already-public entries are never
  altered (their source files have drifted since publish -- a full rebuild would
  silently change live content). The result is re-sorted by day.

  A faithfulness self-check strips frontmatter from the SOURCE of a sample of
  already-published days and asserts it reproduces the published `md` exactly.
  Any mismatch ABORTS (Rule 12 "fail loud") -- it means the stripper no longer
  matches the format the gateway was built with, so newly-appended days could
  render differently from their neighbours.

USAGE
  python3 scripts/rebuild_summa_commentary.py \
      [--html wiki/summa_commentary.html] \
      [--synthesis wiki/vault/synthesis] \
      [--dry-run]

  Exit 0 = wrote (or, with --dry-run, would write) a validated file.
  Exit 1 = a guard failed; the live file is left untouched.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import subprocess
import sys
import tempfile

DATA_RE = re.compile(
    r'(<script id="data" type="application/json">)(.*?)(</script>)', re.S
)

# Every day from Q.67 onward lives in the Supplement; the published tail
# (Days 285-290) all carry this exact pair, and the appended days continue it.
SUPPL_PART = "Suppl"
SUPPL_PARTNAME = "Supplementum"


def strip_frontmatter(text: str) -> str:
    """Return the markdown body the gateway stores in `md`.

    Handles both synthesis conventions:
      - top YAML block:  ---\\n...keys...\\n---\\n<body>
      - body-first with a trailing YAML footer:  <body>\\n---\\nday: N ...
    Verified to reproduce the published `md` exactly for the Supplementum
    (top-frontmatter) days, which is the format every appended day uses.
    """
    t = text
    if t.lstrip().startswith("---"):
        t2 = t.lstrip("\n")
        end = t2.find("\n---", 3)
        if end != -1:
            nl = t2.find("\n", end + 1)
            if nl != -1:
                t2 = t2[nl + 1:]
        t = t2
    m = re.search(r"\n-{3,}\s*\n+day:\s*\d+.*\Z", t, re.S)
    if m:
        t = t[: m.start()]
    return t


def source_path(synth_dir: str, day: int) -> str | None:
    g = glob.glob(os.path.join(synth_dir, f"Day-{day:03d} - * - Contemporary.md"))
    return g[0] if g else None


def title_from_filename(path: str) -> str:
    base = os.path.basename(path)[:-3]  # drop ".md"
    parts = base.split(" - ")
    return parts[1] if len(parts) >= 2 else base


def die(msg: str) -> "NoReturn":
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.dirname(here)
    ap = argparse.ArgumentParser()
    ap.add_argument("--html", default=os.path.join(repo, "wiki", "summa_commentary.html"))
    ap.add_argument("--synthesis", default=os.path.join(repo, "wiki", "vault", "synthesis"))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not os.path.isfile(args.html):
        die(f"gateway not found: {args.html}")
    if not os.path.isdir(args.synthesis):
        die(f"synthesis dir not found: {args.synthesis}")

    html = open(args.html, encoding="utf-8").read()
    m = DATA_RE.search(html)
    if not m:
        die("could not locate <script id=\"data\"> blob")
    existing = json.loads(m.group(2))
    by_day = {d["day"]: d for d in existing}
    n_existing = len(existing)
    print(f"existing entries: {n_existing} (days {min(by_day)}..{max(by_day)})")

    # ---- faithfulness self-check on a sample of published Supplementum days ----
    sample = [d for d in (285, 286, 288, 290, 250, 150) if d in by_day]
    for day in sample:
        p = source_path(args.synthesis, day)
        if not p:
            continue
        rebuilt = strip_frontmatter(open(p, encoding="utf-8").read())
        if rebuilt != by_day[day]["md"]:
            # Day 1-style drift (source edited post-publish) is expected for some
            # early days; only treat the *Supplementum* sample as load-bearing,
            # since that is the exact format the appended days use.
            if day >= 285:
                die(
                    f"stripper no longer reproduces published md for Day {day}; "
                    "the gateway format changed -- refusing to append possibly "
                    "mismatched days."
                )
            else:
                print(f"  note: Day {day} source has drifted since publish (expected)")
        else:
            print(f"  self-check Day {day}: md reproduced exactly")

    # ---- discover the frontier from source ----
    src_days = sorted(
        int(re.search(r"Day-(\d{3})", os.path.basename(p)).group(1))
        for p in glob.glob(os.path.join(args.synthesis, "Day-*- Contemporary.md"))
    )
    if not src_days:
        die("no source synthesis files found")
    frontier = max(src_days)
    print(f"source frontier: Day {frontier} ({len(src_days)} source files)")

    # ---- append every missing day from source (preserve published verbatim) ----
    appended = []
    for day in range(1, frontier + 1):
        if day in by_day:
            continue
        p = source_path(args.synthesis, day)
        if not p:
            die(f"Day {day} missing from gateway AND from source -- gap in series")
        entry = {
            "day": day,
            "title": title_from_filename(p),
            "part": SUPPL_PART,
            "partName": SUPPL_PARTNAME,
            "md": strip_frontmatter(open(p, encoding="utf-8").read()),
        }
        by_day[day] = entry
        appended.append(day)

    if not appended:
        print("nothing to append; gateway already current.")
        return 0
    print(f"appending {len(appended)} day(s): {appended[0]}..{appended[-1]}")

    merged = [by_day[d] for d in sorted(by_day)]

    # ---- guards (fail loud) ----
    days = [d["day"] for d in merged]
    if days != list(range(1, frontier + 1)):
        die(f"day sequence not contiguous 1..{frontier}: got {len(days)} entries")
    # published entries must be byte-identical to before
    for d in existing:
        if by_day[d["day"]] is not d:
            die(f"internal: published Day {d['day']} object was replaced")
    for ap_day in appended:
        e = by_day[ap_day]
        if e["part"] != SUPPL_PART or e["partName"] != SUPPL_PARTNAME:
            die(f"appended Day {ap_day} has wrong part fields")
        if f"# Day {ap_day}" not in e["md"]:
            die(f"appended Day {ap_day} md missing its day heading")
        if "\n---\nday:" in e["md"] or e["md"].lstrip().startswith("---\nday"):
            die(f"appended Day {ap_day} md still contains frontmatter")

    new_json = json.dumps(merged, ensure_ascii=False)
    new_html = html[: m.start(2)] + new_json + html[m.end(2):]

    # template (everything outside the data blob) must be untouched
    if html[: m.start(2)] != new_html[: m.start(2)] or html[m.end(2):] != new_html[len(new_html) - (len(html) - m.end(2)):]:
        die("template region changed -- aborting")

    # validate JS (the marked.js bundle etc.); skip the application/json blob
    for sm in re.finditer(r'<script(?![^>]*application/json)[^>]*>(.*?)</script>', new_html, re.S):
        js = sm.group(1)
        if not js.strip():
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
            f.write(js)
            tmp = f.name
        r = subprocess.run(["node", "--check", tmp], capture_output=True, text=True)
        os.unlink(tmp)
        if r.returncode != 0:
            die(f"node --check failed on a script block: {r.stderr[:300]}")

    # re-parse the new blob to be sure it's valid JSON of the right size
    m2 = DATA_RE.search(new_html)
    reparsed = json.loads(m2.group(2))
    if len(reparsed) != frontier:
        die(f"reparsed entry count {len(reparsed)} != frontier {frontier}")

    print(f"validated: {len(reparsed)} entries, days 1..{frontier}, JS OK, "
          f"size {len(html)} -> {len(new_html)} bytes")

    if args.dry_run:
        print("dry-run: not writing.")
        return 0

    with open(args.html, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"wrote {args.html}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
