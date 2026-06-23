#!/usr/bin/env python3
"""
build_provenance.py — Provenance/join layer for the C2A2 review process.

NON-DESTRUCTIVE. Reads the vault; writes only to an out-dir sidecar.
Joins each *visualized* PRS triplet (traditions/<key>/prs_triplets.md) back to
the *proposal* that produced it (inbox/proposals/**/*.md), so we can:
  - reconcile "reviewed" vs "visualized" counts exactly,
  - compute proposed -> approved -> ingested lag per triplet,
  - (later) hyperlink a triplet to its review/decision history.

Match tiers, in priority order:
  A  backref   : triplet Source line contains an explicit PROP-YYYY-MM-DD-NNN id
  B  text      : Problem-text similarity to a candidate within the same tradition
  C  seed      : RC-Pilot seed (Date Added 2026-04-03 / Source names RC Pilot)
  D  unmatched : FAIL-LOUD — no proposal found

Usage:
  python3 build_provenance.py <vault_dir> <out_dir> [--threshold 0.60]
"""
import sys, os, re, csv, json, glob, argparse
from datetime import date, datetime
from difflib import SequenceMatcher

SEED_DATE = "2026-04-03"
PROP_RE = re.compile(r"PROP-\d{4}-\d{2}-\d{2}-\d{3}")
PROP_DATE_RE = re.compile(r"PROP-(\d{4})-(\d{2})-(\d{2})-\d{3}")


def norm(s):
    """Lowercase, strip punctuation/whitespace for fuzzy text comparison."""
    s = (s or "").lower()
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def ratio(a, b):
    return SequenceMatcher(None, norm(a), norm(b)).ratio()


def parse_frontmatter(text):
    """Return dict of simple key: value YAML frontmatter (first --- block)."""
    fm = {}
    if not text.startswith("---"):
        return fm
    end = text.find("\n---", 3)
    if end == -1:
        return fm
    for line in text[3:end].splitlines():
        m = re.match(r"^([a-z_]+):\s*(.*)$", line.strip())
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"')
    return fm


def parse_candidates(text):
    """Parse PRS-CANDIDATE-NN blocks -> list of dicts with problem/resource/solution."""
    cands = []
    blocks = re.split(r"(?m)^PRS-CANDIDATE-(\d+):\s*$", text)
    # re.split keeps the captured id as interleaved tokens
    for i in range(1, len(blocks), 2):
        cid = blocks[i]
        body = blocks[i + 1] if i + 1 < len(blocks) else ""
        body = body.split("\n## ")[0]  # stop at next section header
        d = {"candidate_id": "PRS-CANDIDATE-%s" % cid}
        for field in ("Problem", "Resource", "Solution", "Confidence"):
            m = re.search(r"(?m)^\s*%s:\s*(.+)$" % field, body)
            d[field.lower()] = m.group(1).strip() if m else ""
        cands.append(d)
    return cands


def load_proposals(vault):
    """Return (props_by_id, candidates) from inbox/proposals/**/*.md."""
    props_by_id, candidates = {}, []
    for path in glob.glob(os.path.join(vault, "inbox", "proposals", "**", "*.md"), recursive=True):
        text = open(path, encoding="utf-8", errors="replace").read()
        fm = parse_frontmatter(text)
        pid = fm.get("proposal_id") or fm.get("prop_id")
        if not pid:
            continue
        disposition = os.path.basename(os.path.dirname(path))
        rec = {
            "proposal_id": pid,
            "tradition_key": fm.get("tradition_key", ""),
            "status": fm.get("status", ""),
            "disposition_folder": disposition,
            "decision": fm.get("decision", ""),
            "decided_at": fm.get("decided_at", ""),
            "source_date": fm.get("source_date", ""),
            "searched_on": fm.get("searched_on", ""),
            "path": os.path.relpath(path, vault),
        }
        props_by_id[pid] = rec
        for c in parse_candidates(text):
            c.update({"proposal_id": pid, "tradition_key": rec["tradition_key"],
                      "disposition_folder": disposition})
            candidates.append(c)
    return props_by_id, candidates


def parse_triplets(vault):
    """Parse traditions/<key>/prs_triplets.md -> list of triplet dicts."""
    triplets = []
    for path in sorted(glob.glob(os.path.join(vault, "traditions", "*", "prs_triplets.md"))):
        tradition = os.path.basename(os.path.dirname(path))
        text = open(path, encoding="utf-8", errors="replace").read()
        parts = re.split(r"(?m)^(PRS-\d+):\s*$", text)
        for i in range(1, len(parts), 2):
            tid = parts[i]
            body = parts[i + 1] if i + 1 < len(parts) else ""
            body = re.split(r"(?m)^PRS-\d+:\s*$", body)[0]
            d = {"tradition": tradition, "triplet_id": tid}
            for field in ("Label", "Problem", "Resource", "Solution",
                          "Date Added", "Source", "Confidence"):
                m = re.search(r"(?m)^\s*%s:\s*(.+)$" % re.escape(field), body)
                d[field.lower().replace(" ", "_")] = m.group(1).strip() if m else ""
            triplets.append(d)
    return triplets


def to_date(s):
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", s or "")
    if not m:
        return None
    try:
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def lag_days(a, b):
    da, db = to_date(a), to_date(b)
    return (db - da).days if (da and db) else ""


def is_seed(t):
    return t.get("date_added", "").startswith(SEED_DATE) or \
        re.search(r"RC Pilot|Resurrecting Civility", t.get("source", ""), re.I) is not None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("vault")
    ap.add_argument("out_dir")
    ap.add_argument("--threshold", type=float, default=0.60)
    args = ap.parse_args()

    props_by_id, candidates = load_proposals(args.vault)
    triplets = parse_triplets(args.vault)
    cands_by_trad = {}
    for c in candidates:
        cands_by_trad.setdefault(c["tradition_key"], []).append(c)
    # Traditions with zero proposals are authored scaffolding (loughran, macintyre):
    # their triplets are seed/authored, never review outputs.
    authored_traditions = {t["tradition"] for t in triplets} - set(cands_by_trad)

    rows = []
    matched_cand_ids = set()  # (proposal_id, candidate_id) that got visualized
    counts = {"A": 0, "B": 0, "C": 0, "D": 0}

    for t in triplets:
        row = {
            "tradition": t["tradition"], "triplet_id": t["triplet_id"],
            "label": t.get("label", ""), "ingested_date": t.get("date_added", ""),
            "source_proposal_id": "", "matched_candidate_id": "",
            "match_tier": "", "match_score": "",
            "proposed_date": "", "approved_date": "",
            "lag_proposed_to_approved_days": "", "lag_proposed_to_ingested_days": "",
        }

        # Tier A: explicit PROP- backref in Source OR Label
        m = PROP_RE.search(t.get("source", "") + " " + t.get("label", ""))
        if m and m.group(0) in props_by_id:
            pid = m.group(0)
            row["source_proposal_id"] = pid
            row["match_tier"] = "A"
            # pick best candidate within that proposal by problem text
            best, best_s = None, -1.0
            for c in candidates:
                if c["proposal_id"] == pid:
                    s = ratio(t.get("problem", ""), c.get("problem", ""))
                    if s > best_s:
                        best, best_s = c, s
            if best:
                row["matched_candidate_id"] = best["candidate_id"]
                row["match_score"] = round(best_s, 3)
                matched_cand_ids.add((pid, best["candidate_id"]))
            counts["A"] += 1

        # Tier C: RC-Pilot seed / authored scaffolding (no proposal expected)
        elif is_seed(t) or t["tradition"] in authored_traditions:
            row["match_tier"] = "C"
            counts["C"] += 1

        # Tier B: fuzzy Problem-text match within tradition
        else:
            best, best_s = None, -1.0
            for c in cands_by_trad.get(t["tradition"], []):
                s = ratio(t.get("problem", ""), c.get("problem", ""))
                if s > best_s:
                    best, best_s = c, s
            if best and best_s >= args.threshold:
                row["source_proposal_id"] = best["proposal_id"]
                row["matched_candidate_id"] = best["candidate_id"]
                row["match_tier"] = "B"
                row["match_score"] = round(best_s, 3)
                matched_cand_ids.add((best["proposal_id"], best["candidate_id"]))
                counts["B"] += 1
            else:
                row["match_tier"] = "D"
                row["match_score"] = round(best_s, 3) if best else ""
                counts["D"] += 1

        # dates + lags
        pid = row["source_proposal_id"]
        if pid:
            pm = PROP_DATE_RE.match(pid)
            row["proposed_date"] = "%s-%s-%s" % pm.groups() if pm else ""
            prop = props_by_id.get(pid, {})
            row["approved_date"] = prop.get("decided_at", "") or ""
            row["lag_proposed_to_approved_days"] = lag_days(row["proposed_date"], row["approved_date"])
            row["lag_proposed_to_ingested_days"] = lag_days(row["proposed_date"], row["ingested_date"])
        rows.append(row)

    # Reverse gap: approved candidates with no visualized triplet
    reverse_gap = []
    for c in candidates:
        if c["disposition_folder"] == "approved" and \
           (c["proposal_id"], c["candidate_id"]) not in matched_cand_ids:
            reverse_gap.append(c)

    os.makedirs(args.out_dir, exist_ok=True)
    cols = ["tradition", "triplet_id", "label", "match_tier", "match_score",
            "source_proposal_id", "matched_candidate_id", "proposed_date",
            "approved_date", "ingested_date",
            "lag_proposed_to_approved_days", "lag_proposed_to_ingested_days"]
    with open(os.path.join(args.out_dir, "triplet_provenance.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in cols})
    json.dump({"rows": rows, "counts": counts,
               "reverse_gap": reverse_gap},
              open(os.path.join(args.out_dir, "triplet_provenance.json"), "w"), indent=2)

    # ---- reconciliation report ----
    total = len(triplets)
    n_approved_files = len({c["proposal_id"] for c in candidates
                            if c["disposition_folder"] == "approved"})
    n_approved_cands = sum(1 for c in candidates if c["disposition_folder"] == "approved")
    pti = [r["lag_proposed_to_ingested_days"] for r in rows
           if isinstance(r["lag_proposed_to_ingested_days"], int)]
    pta = [r["lag_proposed_to_approved_days"] for r in rows
           if isinstance(r["lag_proposed_to_approved_days"], int)]

    def med(xs):
        xs = sorted(xs)
        n = len(xs)
        return "" if not n else (xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2)

    L = []
    L.append("# Provenance Reconciliation — generated %s" % datetime.now().strftime("%Y-%m-%d %H:%M"))
    L.append("")
    L.append("## Counts")
    L.append("")
    L.append("| Metric | Count |")
    L.append("|---|---|")
    L.append("| Visualized triplets (15 tradition files) | %d |" % total)
    L.append("| — Tier A (explicit PROP- backref) | %d |" % counts["A"])
    L.append("| — Tier B (fuzzy Problem-text match, >=%.2f) | %d |" % (args.threshold, counts["B"]))
    L.append("| — Tier C (RC-Pilot seed, no proposal) | %d |" % counts["C"])
    L.append("| — Tier D (UNMATCHED — fail loud) | %d |" % counts["D"])
    L.append("| Distinct approved proposal files | %d |" % n_approved_files)
    L.append("| Approved PRS candidate blocks | %d |" % n_approved_cands)
    L.append("| Approved candidates visualized (forward-traced) | %d |" % len(matched_cand_ids))
    L.append("| Approved candidates NOT visualized (reverse gap) | %d |" % len(reverse_gap))
    L.append("")
    L.append("**Identity check:** A+B+C+D = %d ; triplets = %d ; %s" %
             (sum(counts.values()), total,
              "OK" if sum(counts.values()) == total else "MISMATCH"))
    L.append("")
    L.append("## Lag (days)")
    L.append("")
    L.append("| Interval | n | median | min | max |")
    L.append("|---|---|---|---|---|")
    if pti:
        L.append("| proposed -> ingested | %d | %s | %d | %d |" % (len(pti), med(pti), min(pti), max(pti)))
    if pta:
        L.append("| proposed -> approved | %d | %s | %d | %d |" % (len(pta), med(pta), min(pta), max(pta)))
    L.append("")
    L.append("## FAIL-LOUD — Tier D unmatched triplets (%d)" % counts["D"])
    L.append("")
    for r in rows:
        if r["match_tier"] == "D":
            L.append("- %s/%s  best=%s  label: %s" %
                     (r["tradition"], r["triplet_id"], r["match_score"], r["label"][:80]))
    L.append("")
    L.append("## FAIL-LOUD — approved candidates with no visualized triplet (%d)" % len(reverse_gap))
    L.append("")
    for c in reverse_gap:
        L.append("- %s / %s  (%s)  problem: %s" %
                 (c["proposal_id"], c["candidate_id"], c["tradition_key"], c.get("problem", "")[:80]))
    open(os.path.join(args.out_dir, "RECONCILIATION.md"), "w").write("\n".join(L) + "\n")

    print("triplets=%d  A=%d B=%d C=%d D=%d  approved_files=%d approved_cands=%d visualized_cands=%d reverse_gap=%d"
          % (total, counts["A"], counts["B"], counts["C"], counts["D"],
             n_approved_files, n_approved_cands, len(matched_cand_ids), len(reverse_gap)))


if __name__ == "__main__":
    main()
