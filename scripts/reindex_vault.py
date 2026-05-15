#!/usr/bin/env python3
"""
reindex_vault.py — Scans vault transcripts/synthesis and updates summa_index.json
in-place so that any newly-added days are marked available=true with correct paths.

Usage:
    python3 reindex_vault.py <vault_dir> [--index <path_to_summa_index.json>]

If --index is omitted, defaults to <vault_dir>/refs/summa_index.json.

The script:
  1. Reads every transcript frontmatter to get day number + summa_ref (question numbers)
  2. Builds a question→day mapping
  3. For every index entry whose question number is now mapped to a day:
       - Sets available=true
       - Sets day=N
       - Sets transcript=transcripts/Day-NNN - Title.md
       - Sets synthesis=synthesis/Day-NNN - Title - Contemporary.md
  4. Writes the updated index back to the same file

Safe to re-run — idempotent. Only modifies entries that need updating.
"""

import json
import os
import re
import sys
import argparse


def parse_frontmatter(path):
    """Extract key: value pairs from YAML frontmatter (--- blocks)."""
    meta = {}
    try:
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
    except OSError:
        return meta

    if not lines or lines[0].strip() != "---":
        return meta

    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = re.match(r'^(\w+):\s*(.+)', line)
        if m:
            value = m.group(2).strip()
            # Strip YAML inline comments: "...value...  # comment" → "...value..."
            # (must be at least one space before the #, to keep '#' inside strings).
            if ' #' in value:
                value = value.split(' #', 1)[0].rstrip()
            meta[m.group(1).strip()] = value.strip('"')

    return meta


def scan_vault(vault_dir):
    """Return dicts: day->transcript_path, day->synthesis_path, day->question_set."""
    trans_dir  = os.path.join(vault_dir, "transcripts")
    synth_dir  = os.path.join(vault_dir, "synthesis")

    day_trans   = {}
    day_synth   = {}
    day_questions = {}

    for fname in sorted(os.listdir(trans_dir)):
        m = re.match(r"Day-(\d+)", fname)
        if not m:
            continue
        day = int(m.group(1))
        meta = parse_frontmatter(os.path.join(trans_dir, fname))
        ref = meta.get("summa_ref", "")
        if not ref:
            continue

        # Parse pars-aware (pars, question) pairs from summa_ref.
        # Supports multi-part transition days where one episode spans a part
        # boundary, e.g. "Prima Pars, Q.119 + Prima Secundae, Q.1" (Day 61
        # in the podcast — Volume 2 opener). Each '+'-segment is parsed
        # independently for its own part marker; questions within a segment
        # inherit that segment's part. Order-sensitive lookup of part names
        # (longer keys first) so "secunda secundae" wins over "secundae".
        # Order matters: longer Latin forms first, then abbreviations
        # ordered longest-prefix-first ("ii-ii" before "i-ii" so the inner
        # "i-ii" substring of "ii-ii" doesn't mis-match). Bare "i" is
        # deliberately omitted — too ambiguous given how it appears inside
        # "i-ii" and "ii-ii"; Prima Pars days should use the full form.
        pars_map = [
            ("prima pars",       "I"),
            ("prima secundae",   "I-II"),
            ("secunda secundae", "II-II"),
            ("tertia pars",      "III"),
            ("ii-ii",            "II-II"),
            ("i-ii",             "I-II"),
            ("iii",              "III"),
        ]

        qs_pairs = set()
        # Walk segments left-to-right, carrying the most recently declared
        # part forward. This handles three common shapes:
        #   "Prima Pars, Q.117 + Q.118"          → both Q's attribute to I
        #   "Prima Secundae, Q.2 + Q.3"          → both Q's attribute to I-II
        #   "Prima Pars, Q.119 + Prima Secundae, Q.1"  → Q.119→I, Q.1→I-II
        current_pars = None
        for segment in ref.split("+"):
            seg_lower = segment.lower()
            seg_pars = next((code for pat, code in pars_map
                             if pat in seg_lower), None)
            if seg_pars:
                current_pars = seg_pars
            if current_pars is None:
                continue  # haven't seen any part name yet — skip
            # Parse Q-numbers: handles "Q.9 + Q.10", "Q.9-10", "Q.65 + Q.66"
            for token in re.findall(r"Q\.(\d+)(?:-(\d+))?", segment):
                start = int(token[0])
                end   = int(token[1]) if token[1] else start
                for q in range(start, end + 1):
                    qs_pairs.add((current_pars, q))
        if not qs_pairs:
            continue

        day_trans[day]     = "transcripts/" + fname
        day_questions[day] = qs_pairs  # set of (pars_code, q) tuples

    for fname in sorted(os.listdir(synth_dir)):
        m = re.match(r"Day-(\d+)", fname)
        if not m:
            continue
        day = int(m.group(1))
        day_synth[day] = "synthesis/" + fname

    return day_trans, day_synth, day_questions


def reindex(vault_dir, index_path):
    day_trans, day_synth, day_questions = scan_vault(vault_dir)

    # Build (pars, question) -> day mapping; first-wins for duplicates (lower day)
    q_to_day = {}
    for day in sorted(day_questions.keys()):
        for key in day_questions[day]:    # set of (pars_code, q) tuples
            if key not in q_to_day:
                q_to_day[key] = day

    with open(index_path, encoding="utf-8") as f:
        index = json.load(f)

    updated = 0
    for key, entry in index.items():
        km = re.match(r"([^.]+)\.Q(\d+)\.", key)
        if not km:
            continue
        pars_prefix = km.group(1)
        qnum        = int(km.group(2))
        lookup      = (pars_prefix, qnum)
        if lookup not in q_to_day:
            continue

        day    = q_to_day[lookup]
        t_path = day_trans.get(day)
        s_path = day_synth.get(day)

        changed = False
        if not entry.get("available"):
            entry["available"] = True
            changed = True
        if entry.get("day") != day:
            entry["day"] = day
            changed = True
        if t_path and entry.get("transcript") != t_path:
            entry["transcript"] = t_path
            changed = True
        if s_path and entry.get("synthesis") != s_path:
            entry["synthesis"] = s_path
            changed = True

        if changed:
            updated += 1

    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, separators=(",", ":"))

    total_available = sum(1 for v in index.values() if v.get("available"))
    print(f"reindex_vault: {updated} entries updated, {total_available} total available")

    # ─── Gap audit: warn on suspicious holes in availability ─────────────
    # For each part, if any question in [1..max_available_q] is *not* marked
    # available, surface it. This catches the failure mode where a transcript's
    # summa_ref drops a part (e.g. a part-transition day declaring only
    # "Prima Pars, Q.119" when it actually covers Q.119 + I-II.Q.1).
    # Soft warning to stderr — doesn't fail the run; the launchd job continues.
    by_part_qs = {}
    for key, entry in index.items():
        km = re.match(r"([^.]+)\.Q(\d+)\.", key)
        if not km:
            continue
        pars_prefix = km.group(1)
        qnum        = int(km.group(2))
        by_part_qs.setdefault(pars_prefix, {}).setdefault(qnum, []).append(entry)
    for pars_prefix, qs in sorted(by_part_qs.items()):
        avail_qs = [q for q, entries in qs.items()
                    if any(e.get("available") for e in entries)]
        if not avail_qs:
            continue
        max_q = max(avail_qs)
        missing = sorted(q for q in range(1, max_q + 1)
                         if q in qs and q not in avail_qs)
        if missing:
            print(f"reindex_vault: WARNING {pars_prefix} has gap(s) below "
                  f"highest available Q.{max_q}: missing Q.{missing} — "
                  f"check whether a transition day's summa_ref is incomplete",
                  file=sys.stderr)

    return updated


def main():
    parser = argparse.ArgumentParser(description="Reindex summa_index.json from vault files")
    parser.add_argument("vault_dir", help="Path to vault directory (contains transcripts/ and synthesis/)")
    parser.add_argument("--index", help="Path to summa_index.json (default: <vault_dir>/refs/summa_index.json)")
    args = parser.parse_args()

    vault_dir  = os.path.expanduser(args.vault_dir)
    index_path = args.index or os.path.join(vault_dir, "refs", "summa_index.json")

    if not os.path.isdir(vault_dir):
        print(f"ERROR: vault_dir not found: {vault_dir}", file=sys.stderr)
        sys.exit(1)
    if not os.path.isfile(index_path):
        print(f"ERROR: index not found: {index_path}", file=sys.stderr)
        sys.exit(1)

    updated = reindex(vault_dir, index_path)
    sys.exit(0)


if __name__ == "__main__":
    main()
