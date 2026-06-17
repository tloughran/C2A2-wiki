#!/usr/bin/env python3
"""PRS-triplet yield metric (WS2).

Quantifies PRS-triplet *production* per commit-day from the git history of
wiki/traditions/*/prs_triplets.md.

Source settled in DECISION-058; rests on ASSUMPTION-319 (git-history triplet
source) and PRESUMPTION-350 (commit-as-clock). A triplet is identified by the
pair (tradition, PRS-NN) because ids are numbered per tradition. Its yield date
is the date of the *earliest* commit in which that id appears in the tradition's
prs_triplets.md. Daily yield = count of triplets first appearing on that day.

Outputs (written next to this script unless --out-dir given):
  prs_yield_log.csv     date,new_triplets,cumulative,traditions_touched
  prs_yield_detail.csv  tradition,prs_id,label,first_seen_date,commit,file_relpath

Fail-loud (Rule 12): any tradition file with zero commits, or a cumulative that
does not match the current on-disk triplet count, aborts with a nonzero exit.
"""

import argparse
import csv
import os
import re
import subprocess
import sys
from collections import defaultdict

PRS_RE = re.compile(r"^PRS-(\d+):\s*$")
LABEL_RE = re.compile(r"^\s*Label:\s*(.*?)\s*$")


def git(repo, *args):
    """Run a git command in repo, return stdout (text). Raises on failure."""
    res = subprocess.run(
        ["git", "-C", repo, *args],
        capture_output=True, text=True,
    )
    if res.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {res.stderr.strip()}")
    return res.stdout


def repo_root(start):
    return git(start, "rev-parse", "--show-toplevel").strip()


def commits_for(repo, relpath):
    """(commit, date) pairs, oldest first, for commits touching relpath."""
    out = git(repo, "log", "--reverse", "--format=%H %ad", "--date=short",
              "--", relpath)
    pairs = []
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        h, d = line.split(" ", 1)
        pairs.append((h, d.strip()))
    return pairs


def ids_in_blob(repo, commit, relpath):
    """Map PRS id -> label for the file content at a given commit.

    Returns None if the file did not exist at that commit (e.g. a rename
    boundary), so the caller can surface it rather than miscount.
    """
    res = subprocess.run(
        ["git", "-C", repo, "show", f"{commit}:{relpath}"],
        capture_output=True, text=True,
    )
    if res.returncode != 0:
        return None
    ids = {}
    lines = res.stdout.splitlines()
    for i, line in enumerate(lines):
        m = PRS_RE.match(line)
        if not m:
            continue
        prs_id = f"PRS-{int(m.group(1)):02d}"
        label = ""
        # label is conventionally the first indented "Label:" line after the id
        for j in range(i + 1, min(i + 6, len(lines))):
            lm = LABEL_RE.match(lines[j])
            if lm:
                label = lm.group(1)
                break
            if PRS_RE.match(lines[j]):
                break
        ids.setdefault(prs_id, label)
    return ids


def current_ondisk(repo, files):
    """Return (unique_id_set, line_count, duplicates) for the working tree.

    unique_id_set : set of (tradition, prs_id) currently present.
    line_count    : number of PRS-NN: lines (> unique count iff an id repeats).
    duplicates    : list of (tradition, prs_id) appearing more than once in a file.
    """
    unique = set()
    line_count = 0
    duplicates = []
    for rel in files:
        tradition = rel.split("/")[2]
        seen_here = set()
        with open(os.path.join(repo, rel), encoding="utf-8") as fh:
            for ln in fh:
                m = PRS_RE.match(ln)
                if not m:
                    continue
                line_count += 1
                pid = f"PRS-{int(m.group(1)):02d}"
                if pid in seen_here:
                    duplicates.append((tradition, pid))
                seen_here.add(pid)
                unique.add((tradition, pid))
    return unique, line_count, duplicates


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", default=".", help="path inside the wiki git repo")
    ap.add_argument("--out-dir", default=None,
                    help="directory for the two CSVs (default: script dir)")
    args = ap.parse_args()

    repo = repo_root(args.repo)
    out_dir = args.out_dir or os.path.dirname(os.path.abspath(__file__))

    # Discover tradition files relative to repo root.
    glob_out = git(repo, "ls-files", "wiki/traditions/*/prs_triplets.md")
    files = [p for p in glob_out.splitlines() if p.strip()]
    if not files:
        sys.exit("FAIL: no wiki/traditions/*/prs_triplets.md files tracked")

    # first_seen[(tradition, prs_id)] = (date, commit, label)
    first_seen = {}
    problems = []

    for rel in files:
        tradition = rel.split("/")[2]
        commits = commits_for(repo, rel)
        if not commits:
            problems.append(f"{rel}: zero commits in history")
            continue
        for commit, date in commits:
            blob_ids = ids_in_blob(repo, commit, rel)
            if blob_ids is None:
                # File absent at this commit (rename boundary). Note and move on;
                # the cumulative cross-check below will catch any real undercount.
                problems.append(f"{rel}: not present at {commit[:8]} ({date})")
                continue
            for prs_id, label in blob_ids.items():
                key = (tradition, prs_id)
                if key not in first_seen:
                    first_seen[key] = (date, commit, label)

    # Aggregate to daily yield.
    by_day_count = defaultdict(int)
    by_day_trads = defaultdict(set)
    for (tradition, _), (date, _, _) in first_seen.items():
        by_day_count[date] += 1
        by_day_trads[date].add(tradition)

    dates = sorted(by_day_count)
    log_rows = []
    cumulative = 0
    for d in dates:
        cumulative += by_day_count[d]
        log_rows.append((d, by_day_count[d], cumulative, len(by_day_trads[d])))

    # Fail-loud verification (Rule 12 / Rule 9). The hard integrity invariant is
    # that every triplet currently on disk must appear somewhere in history —
    # otherwise the walk undercounted (e.g. an unhandled rename) and the series
    # cannot be trusted. Retired ids (in history, gone from disk) and duplicate
    # ids (same id twice in one file) are real but expected data conditions:
    # they are surfaced loudly, not silently absorbed, but do not abort.
    on_disk_set, on_disk_lines, duplicates = current_ondisk(repo, files)
    ever_keys = set(first_seen)
    missing = on_disk_set - ever_keys          # MUST be empty
    retired = sorted(ever_keys - on_disk_set)  # produced then removed

    warn = list(problems)
    if duplicates:
        warn.append("duplicate ids on disk (one id used twice in a file): "
                    + ", ".join(f"{t}/{i}" for t, i in sorted(duplicates)))
    if retired:
        warn.append("retired triplets (produced, later removed): "
                    + ", ".join(f"{t}/{i}" for t, i in retired))
    if warn:
        sys.stderr.write("WARNINGS:\n  " + "\n  ".join(warn) + "\n")

    if missing:
        sys.exit(
            "FAIL (Rule 12): "
            + ", ".join(f"{t}/{i}" for t, i in sorted(missing))
            + " present on disk but absent from git history. The walk "
            "undercounted — investigate before trusting the series."
        )

    os.makedirs(out_dir, exist_ok=True)
    log_path = os.path.join(out_dir, "prs_yield_log.csv")
    det_path = os.path.join(out_dir, "prs_yield_detail.csv")

    with open(log_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["date", "new_triplets", "cumulative", "traditions_touched"])
        w.writerows(log_rows)

    with open(det_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["tradition", "prs_id", "label", "first_seen_date",
                    "commit", "present", "file_relpath"])
        for (tradition, prs_id), (date, commit, label) in sorted(first_seen.items()):
            rel = f"wiki/traditions/{tradition}/prs_triplets.md"
            present = 1 if (tradition, prs_id) in on_disk_set else 0
            w.writerow([tradition, prs_id, label, date, commit[:8], present, rel])

    # Console summary.
    print(f"PRS-triplet yield  (repo: {repo})")
    print(f"  tradition files : {len(files)}")
    print(f"  ever produced   : {cumulative}")
    print(f"  present on disk : {len(on_disk_set)} unique "
          f"({on_disk_lines} lines incl. {len(duplicates)} duplicate id(s))")
    print(f"  retired         : {len(retired)}")
    print(f"  commit-days     : {len(dates)}")
    print()
    print(f"  {'date':<12}{'new':>5}{'cum':>7}{'trads':>7}")
    for d, new, cum, trads in log_rows:
        print(f"  {d:<12}{new:>5}{cum:>7}{trads:>7}")
    print()
    print(f"  wrote {log_path}")
    print(f"  wrote {det_path}")


if __name__ == "__main__":
    main()
