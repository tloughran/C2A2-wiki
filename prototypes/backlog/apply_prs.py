#!/usr/bin/env python3
"""Track A part 3 — deterministic COMMIT of vetted staged PRS blocks into the vault.

The model-judgment (vet / dedup / drop / route) happens BEFORE this script: the
operator decides which staged PRS-N to keep per unit and passes drops in. This
script only does the mechanical, error-prone parts (Rule 5: code answers):
  - strip the staging '#' header, insert kept blocks BEFORE the
    '---' / '*Total PRS triplets: N*' footer of traditions/<trad>/prs_triplets.md
  - bump the footer count by the number actually inserted (preserving any
    parenthetical suffix, e.g. stump's re-home note)
  - append one PROCESSED_LOG line per unit under a single dated Track-A header
  - mark the unit DONE in prs_qc_trace.csv (triplets_emitted, first_prs_n, notes)

It is idempotent: a unit already DONE in qc_trace, or whose first kept PRS-N is
already present in the tradition file, is skipped. Default DRY-RUN; pass --apply
to write. Cross-tradition routing into master/cross_program_index.md is a separate
attended step (flagged per-unit in qc_trace notes), not done here.

Usage:
  python3 apply_prs.py <vault> <manifest.json> <staging_dir> <qc_trace.csv> \
      [--tradition T | --units id1,id2] [--drop UNIT:PRS-25,UNIT2:PRS-30] [--apply]
"""
import sys, os, re, json, csv, argparse, datetime

def parse_staged(path):
    """Return (header_pid, [(prs_n, block_text), ...]) from a staged .txt."""
    lines = open(path, errors="ignore").read().splitlines()
    # drop leading '#' header + blanks; keep from first 'PRS-NN:'
    i = 0
    while i < len(lines) and not re.match(r'^PRS-\d+:', lines[i]):
        i += 1
    body = lines[i:]
    blocks, cur, cur_n = [], [], None
    for ln in body:
        m = re.match(r'^PRS-(\d+):', ln)
        if m:
            if cur:
                blocks.append((cur_n, "\n".join(cur).rstrip()))
            cur, cur_n = [ln], "PRS-%s" % m.group(1)
        else:
            if cur is not None:
                cur.append(ln)
    if cur:
        blocks.append((cur_n, "\n".join(cur).rstrip()))
    return blocks

def insert_blocks(trad_path, blocks):
    """Insert block texts before the footer '---'; bump '*Total PRS triplets: N*'.
    Returns (new_text, old_count, new_count). Raises if footer not found."""
    txt = open(trad_path, errors="ignore").read()
    lines = txt.split("\n")
    foot_i = None
    for i, ln in enumerate(lines):
        if re.match(r'^\*Total PRS triplets:\s*\d+', ln):
            foot_i = i
    if foot_i is None:
        raise SystemExit("no footer in %s" % trad_path)
    # bump the SAME (last) total line we insert before — bump by index, not
    # re.sub first-match (arkanihamed/hoffman carry a stray mid-file total too).
    m = re.match(r'^\*Total PRS triplets:\s*(\d+)(.*)$', lines[foot_i])
    old_count = int(m.group(1)); new_count = old_count + len(blocks)
    lines[foot_i] = "*Total PRS triplets: %d%s" % (new_count, m.group(2))
    # find the '---' separator immediately preceding the footer (search upward)
    sep_i = foot_i - 1
    while sep_i > 0 and lines[sep_i].strip() == "":
        sep_i -= 1
    has_sep = lines[sep_i].strip() == "---"
    # each new block is closed by exactly one '---'
    seg = []
    for _, b in blocks:
        seg.extend(b.split("\n"))
        seg.append("")
        seg.append("---")
    if has_sep:
        # existing '---' separates last-existing from first-new; seg closes before footer
        new_lines = lines[:sep_i + 1] + seg + lines[sep_i + 1:]
    else:
        # no separator before footer: add one before the first new block too
        new_lines = lines[:foot_i] + ["---"] + seg + lines[foot_i:]
    return "\n".join(new_lines), old_count, new_count

def slug_of(unit, vault):
    f = unit.get("primary_file") or (unit.get("files") or [""])[0]
    base = os.path.basename(f)[:-3] if f.endswith(".md") else os.path.basename(f)
    return re.sub(r'^\d{4}-\d{2}-\d{2}_', '', base)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("vault"); ap.add_argument("manifest")
    ap.add_argument("staging"); ap.add_argument("qc")
    ap.add_argument("--tradition"); ap.add_argument("--units")
    ap.add_argument("--drop", default="")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    units = json.load(open(a.manifest))
    drops = {}
    for tok in [t for t in a.drop.split(",") if t]:
        u, n = tok.split(":"); drops.setdefault(u, set()).add(n)
    sel = None
    if a.units: sel = set(a.units.split(","))

    # qc rows
    rows = list(csv.DictReader(open(a.qc)))
    # key by (tradition, unit_id): proposal_ids are NOT globally unique
    # (e.g. PROP-2026-05-18-002 exists for both levin and wright)
    done = {(r["tradition"], r["unit_id"]) for r in rows if r["status"] == "DONE"}
    today = datetime.date.today().isoformat()
    log_lines, qc_updates = [], {}

    for u in units:
        uid = u["unit_id"]; trad = u["tradition"]
        if a.tradition and trad != a.tradition: continue
        if sel and uid not in sel: continue
        if (trad, uid) in done:
            print("skip (DONE):", trad, uid); continue
        sp = os.path.join(a.staging, "%s__%s.txt" % (trad, uid))
        if not os.path.exists(sp):
            print("skip (no staged file):", uid); continue
        blocks = parse_staged(sp)
        keep = [(n, b) for (n, b) in blocks if n not in drops.get(uid, set())]
        trad_path = os.path.join(a.vault, "traditions", trad, "prs_triplets.md")
        cur = open(trad_path, errors="ignore").read()
        if keep and keep[0][0] + ":" in cur:
            print("skip (already present %s):" % keep[0][0], uid); continue
        slug = slug_of(u, a.vault)
        if not keep:
            log_lines.append("- %s %s → %s no-net-new / duplicate / citation-upgrade (+0)" % (uid, slug, trad))
            qc_updates[(trad, uid)] = dict(triplets_emitted=0, first_prs_n="",
                                   notes="all candidates dropped (vet)")
            print("ZERO-emit (logged only):", trad, uid); continue
        new_txt, oc, nc = insert_blocks(trad_path, keep)
        first_n = keep[0][0]; last_n = keep[-1][0]
        rng = first_n if first_n == last_n else "%s..%s" % (first_n, last_n)
        log_lines.append("- %s %s → %s %s (+%d)" % (uid, slug, trad, rng, len(keep)))
        qc_updates[(trad, uid)] = dict(triplets_emitted=len(keep), first_prs_n=first_n[4:],
                               notes=("dropped " + ",".join(sorted(drops[uid]))) if uid in drops else "")
        if a.apply:
            open(trad_path, "w").write(new_txt)
        print("%s %s: +%d (%s) footer %d->%d%s" %
              ("APPLIED" if a.apply else "DRYRUN", uid, len(keep), rng, oc, nc,
               ("  DROP " + ",".join(sorted(drops[uid]))) if uid in drops else ""))

    if not log_lines:
        print("nothing to do."); return

    if a.apply:
        # PROCESSED_LOG
        lp = os.path.join(a.vault, "inbox", "PROCESSED_LOG.md")
        hdr = "\n## %s — Track A PRS backlog clear (attended apply_prs)\n" % today
        with open(lp, "a") as fh:
            if hdr.strip() not in open(lp, errors="ignore").read():
                fh.write(hdr)
            fh.write("\n".join(log_lines) + "\n")
        # qc_trace
        for r in rows:
            if (r["tradition"], r["unit_id"]) in qc_updates:
                up = qc_updates[(r["tradition"], r["unit_id"])]
                r["processed_by"] = "apply_prs"; r["date_processed"] = today
                r["triplets_emitted"] = up["triplets_emitted"]
                r["first_prs_n"] = up["first_prs_n"]; r["status"] = "DONE"
                r["notes"] = up["notes"]
        with open(a.qc, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
        # fail-loud guard: qc must keep exactly the same (tradition,unit_id) set
        chk = list(csv.DictReader(open(a.qc)))
        keys_in = sorted((r["tradition"], r["unit_id"]) for r in rows)
        keys_out = sorted((r["tradition"], r["unit_id"]) for r in chk)
        if keys_in != keys_out or len(chk) != len(rows):
            print("WARNING: qc_trace row set changed on write (in=%d out=%d) — "
                  "vault writes are unaffected (keyed per-tradition), but audit is "
                  "suspect; re-derive from PROCESSED_LOG." % (len(rows), len(chk)),
                  file=sys.stderr)
        print("APPLIED %d units; PROCESSED_LOG + qc_trace updated." % len(qc_updates))
    else:
        print("\nDRY-RUN. log lines that would be written:")
        for l in log_lines: print("  ", l)

if __name__ == "__main__":
    main()
