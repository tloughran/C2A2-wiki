#!/usr/bin/env python3
"""
assemble_review_log.py — Chronological, lossless Review Log for C2A2.

Built on the DURABLE-SOURCE model (review pages were ephemeral local files and
are NOT the source of truth): every proposal *card* comes from its proposal file,
every *response* from the harvested decision emails + decisions.md. Zero-drop:
every proposal file and every decision email is rendered in full; nothing summarized.

Emits a single self-contained wiki/review_log.html with two chronological streams
(Cards / Your Responses) plus a Preservation note. Supporting provenance (which
candidate became a visualized triplet, and the proposed->ingested lag) is attached
per card from triplet_provenance.json — as an index, not the target.

Usage:
  python3 assemble_review_log.py <vault_dir> <provenance_dir> <out_html>
"""
import sys, os, re, json, glob, html
from datetime import datetime
from collections import defaultdict

PROP_DATE_RE = re.compile(r"PROP-(\d{4}-\d{2}-\d{2})-\d{3}")


def esc(s):
    return html.escape(s or "")


def parse_frontmatter(text):
    fm = {}
    if not text.startswith("---"):
        return fm, text
    end = text.find("\n---", 3)
    if end == -1:
        return fm, text
    for line in text[3:end].splitlines():
        m = re.match(r"^([a-z_]+):\s*(.*)$", line.strip())
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"')
    return fm, text[end + 4:]


def md_lite(body):
    """Minimal, lossless markdown render: every line is emitted (escaped)."""
    out = []
    for line in body.splitlines():
        s = line.rstrip()
        if re.match(r"^##+\s", s):
            out.append('<h4 class="sec">%s</h4>' % esc(re.sub(r"^##+\s", "", s)))
        elif re.match(r"^PRS-CANDIDATE-\d+:", s):
            out.append('<div class="cand-h">%s</div>' % esc(s))
        elif re.match(r"^\s*(Problem|Resource|Solution|Confidence|Evidence|Label|Date Added|Source):", s):
            k, _, v = s.partition(":")
            out.append('<div class="kv"><span class="k">%s:</span> %s</div>' % (esc(k.strip()), esc(v.strip())))
        elif s.strip() == "":
            out.append('<div class="sp"></div>')
        else:
            out.append('<div class="ln">%s</div>' % esc(s))
    return "\n".join(out)


def expand_decision_body(body):
    """Expand compacted 'NNN through MMM: ALL X' ranges to one line per item."""
    def repl(m):
        a, b, disp = int(m.group(2)), int(m.group(4)), m.group(5)
        stem = m.group(1)
        return "\n".join("%s-%03d: %s" % (stem, i, disp) for i in range(a, b + 1))
    pat = re.compile(r"(PROP-\d{4}-\d{2}-\d{2})-(\d{3}) through PROP-\d{4}-\d{2}-\d{2}-(\d{3}): ALL (\w+)")
    # rewrite to a form the lambda can read groups from
    pat = re.compile(r"(PROP-\d{4}-\d{2}-\d{2})-(\d{3}) through (PROP-\d{4}-\d{2}-\d{2})-(\d{3}): ALL (\w+)")
    return pat.sub(repl, body)


def load_proposals(vault):
    props = []
    for path in glob.glob(os.path.join(vault, "inbox", "proposals", "**", "*.md"), recursive=True):
        text = open(path, encoding="utf-8", errors="replace").read()
        fm, body = parse_frontmatter(text)
        pid = fm.get("proposal_id") or fm.get("prop_id")
        if not pid:
            continue
        dm = PROP_DATE_RE.match(pid)
        altid = ""
        for k in ("prop_id", "proposal_id"):
            v = fm.get(k, "")
            if v and v != pid:
                altid = v
        props.append({
            "pid": pid, "altid": altid, "date": dm.group(1) if dm else "0000-00-00",
            "thinker": fm.get("thinker", ""), "tradition": fm.get("tradition_key", ""),
            "source_title": fm.get("source_title", ""), "source_url": fm.get("source_url", ""),
            "source_type": fm.get("source_type", ""), "source_date": fm.get("source_date", ""),
            "status": fm.get("status", ""), "folder": os.path.basename(os.path.dirname(path)),
            "decision": fm.get("decision", ""), "decided_at": fm.get("decided_at", ""),
            "body": body.strip(), "path": os.path.relpath(path, vault),
        })
    return props


def prog_to_key(name):
    return re.sub(r"[^a-z0-9]", "", name.lower().replace(" agent", ""))


def field_block(body, field, stops):
    """Capture a field's value from its label up to the next stop label (multi-line safe)."""
    stop = "|".join(re.escape(s) for s in stops)
    pat = re.compile(r"(?ms)^\s*%s:[ \t]*(.*?)(?=\n\s*(?:%s):|\Z)" % (re.escape(field), stop))
    m = pat.search(body)
    return re.sub(r"\s*\n\s*", " ", m.group(1).strip()) if m else ""


def parse_triplets_by_tradition(vault):
    out = {}
    for path in sorted(glob.glob(os.path.join(vault, "traditions", "*", "prs_triplets.md"))):
        trad = os.path.basename(os.path.dirname(path))
        text = open(path, encoding="utf-8", errors="replace").read()
        parts = re.split(r"(?m)^(PRS-\d+):\s*$", text)
        items = []
        for i in range(1, len(parts), 2):
            body = re.split(r"(?m)^PRS-\d+:\s*$", parts[i + 1] if i + 1 < len(parts) else "")[0]
            lab = re.search(r"(?m)^\s*Label:\s*(.+)$", body)
            prob = re.search(r"(?m)^\s*Problem:\s*(.+)$", body)
            items.append((parts[i], lab.group(1).strip() if lab else "", prob.group(1).strip() if prob else ""))
        out[trad] = items
    return out


def parse_cross(vault, valid_keys):
    path = os.path.join(vault, "master", "cross_program_index.md")
    if not os.path.exists(path):
        return []
    text = open(path, encoding="utf-8", errors="replace").read()
    parts = re.split(r"(?m)^(CROSS-\d+):\s*$", text)
    items = []
    for i in range(1, len(parts), 2):
        body = re.split(r"(?m)^CROSS-\d+:\s*$", parts[i + 1] if i + 1 < len(parts) else "")[0]
        progs = [p.strip() for p in field_block(body, "Programs involved", ["Nature of connection", "First appeared"]).split(",") if p.strip()]
        keys = sorted(k for k in {prog_to_key(p) for p in progs} if k in valid_keys)
        items.append({"id": parts[i], "insight": field_block(body, "Question/Insight", ["Programs involved"]),
                      "programs": progs, "keys": keys,
                      "nature": field_block(body, "Nature of connection", ["First appeared", "Last updated"]),
                      "status": field_block(body, "Status", ["Notes", "First appeared"]),
                      "notes": field_block(body, "Notes", ["CROSS-"])})
    return items


def parse_synthesis(vault):
    out = {}
    for path in glob.glob(os.path.join(vault, "synthesis", "*_bridge.md")):
        a, _, b = os.path.basename(path)[:-len("_bridge.md")].partition("_")
        out[tuple(sorted((a, b)))] = open(path, encoding="utf-8", errors="replace").read().strip()
    return out


def parse_findings(vault):
    path = os.path.join(vault, "flags", "pattern_detector_findings.md")
    if not os.path.exists(path):
        return []
    text = open(path, encoding="utf-8", errors="replace").read()
    parts = re.split(r"(?m)^(FINDING-\d+):\s*$", text)
    items = []
    for i in range(1, len(parts), 2):
        body = re.split(r"(?m)^FINDING-\d+:\s*$", parts[i + 1] if i + 1 < len(parts) else "")[0]
        items.append({"id": parts[i],
                      "date": field_block(body, "Date evaluated", ["Source candidate", "Programs"]),
                      "programs": field_block(body, "Programs", ["Evaluation type"]),
                      "etype": field_block(body, "Evaluation type", ["Finding"]),
                      "finding": field_block(body, "Finding", ["Confidence", "Recommended action"]),
                      "confidence": field_block(body, "Confidence", ["Recommended action"]),
                      "action": field_block(body, "Recommended action", ["EVALUATED", "FINDING-"])})
    return items


def action_class(a):
    a = a.lower()
    if "flag" in a and "tom" in a:
        return "flag", "Flag for Tom"
    if "escalate" in a:
        return "esc", "Escalate"
    if "monitor" in a:
        return "mon", "Monitor"
    if "archive" in a:
        return "arch", "Archive"
    return "neutral", (a[:24] or "—")


def main():
    vault, prov_dir, out_html = sys.argv[1], sys.argv[2], sys.argv[3]
    props = load_proposals(vault)
    prov = json.load(open(os.path.join(prov_dir, "triplet_provenance.json")))
    demails = json.load(open(os.path.join(prov_dir, "decision_emails.json")))

    # provenance index: proposal_id -> list of (tradition, triplet_id, candidate_id, lag)
    pidx = defaultdict(list)
    for r in prov["rows"]:
        if r.get("source_proposal_id"):
            pidx[r["source_proposal_id"]].append(r)

    # decisions.md narratives by date
    dnar = {}
    for p in glob.glob(os.path.join(vault, "review", "archive", "*_decisions.md")):
        d = re.search(r"(\d{4}-\d{2}-\d{2})", os.path.basename(p))
        if d:
            dnar[d.group(1)] = open(p, encoding="utf-8", errors="replace").read()

    # ---- Cards stream: group by proposal date ----
    by_date = defaultdict(list)
    for pr in props:
        by_date[pr["date"]].append(pr)

    cards_html = []
    for d in sorted(by_date):
        day = by_date[d]
        rows = []
        for pr in sorted(day, key=lambda x: x["pid"]):
            disp = pr["decision"] or pr["folder"]
            chip = {"approved": "ok", "approve": "ok", "pending": "wait",
                    "needs_review": "wait"}.get(disp.lower(), "neutral")
            ts = pidx.get(pr["pid"], [])
            if ts:
                lags = [t["lag_proposed_to_ingested_days"] for t in ts
                        if isinstance(t["lag_proposed_to_ingested_days"], int)]
                lag = (" · lag %dd" % min(lags)) if lags else ""
                prov_line = ('<div class="prov">→ visualized as %s%s</div>' %
                             (", ".join("%s/%s" % (t["tradition"], t["triplet_id"]) for t in ts), lag))
            else:
                prov_line = '<div class="prov gap">→ not visualized as a distinct triplet</div>'
            src = esc(pr["source_title"])
            if pr["source_url"]:
                src = '<a href="%s" target="_blank" rel="noopener">%s</a>' % (esc(pr["source_url"]), src or esc(pr["source_url"]))
            rows.append(
                '<details class="card"><summary>'
                '<span class="pid">%s</span>%s <span class="trad t-%s">%s</span> '
                '<span class="chip %s">%s</span>'
                '<span class="ctitle">%s</span></summary>'
                '<div class="meta">%s · %s · source date %s · folder <code>%s</code>%s</div>'
                '<div class="src">%s</div>%s'
                '<div class="body">%s</div></details>' % (
                    esc(pr["pid"]),
                    (' <span class="pid alt">alt %s</span>' % esc(pr["altid"])) if pr["altid"] else "",
                    esc(pr["tradition"]), esc(pr["thinker"] or pr["tradition"]),
                    chip, esc(disp or "—"), esc(pr["source_title"])[:120],
                    esc(pr["thinker"]), esc(pr["source_type"]), esc(pr["source_date"]),
                    esc(pr["folder"]),
                    (' · decided %s' % esc(pr["decided_at"])) if pr["decided_at"] else "",
                    src, prov_line, md_lite(pr["body"])))
        cards_html.append(
            '<details class="daygrp" open><summary class="dayhdr">%s '
            '<span class="cnt">%d card%s</span></summary>%s</details>' %
            (d, len(day), "s" if len(day) != 1 else "", "\n".join(rows)))

    # ---- Responses stream ----
    resp_html = []
    for em in sorted(demails["emails"], key=lambda x: x["date"]):
        body = expand_decision_body(em["body"])
        ddate = em["date"][:10]
        nar = dnar.get(ddate, "")
        nar_html = ('<details class="narr"><summary>processed decisions.md (%s)</summary>'
                    '<div class="body">%s</div></details>' % (ddate, md_lite(nar))) if nar else ""
        resp_html.append(
            '<details class="card resp" open><summary>'
            '<span class="pid">%s</span> <span class="emeta">%s · %s</span></summary>'
            '<div class="meta">thread <code>%s</code> · labels %s</div>'
            '<pre class="email">%s</pre>%s</details>' % (
                esc(em["subject"]), esc(em["date"]), esc(em["sender"]),
                esc(em["thread_id"]), esc(", ".join(em.get("labels", []))),
                esc(body), nar_html))
    resends = "".join(
        '<li>thread <code>%s</code> — %s (duplicate of <code>%s</code>)</li>' %
        (esc(r["thread_id"]), esc(r["date_note"]), esc(r["duplicate_of"]))
        for r in demails.get("_resend_threads", []))

    # ---- Triples panel (per tradition) ----
    trip = parse_triplets_by_tradition(vault)
    valid_keys = set(trip)
    n_triples = sum(len(v) for v in trip.values())
    triples_html = ['<div class="ptot">%d distinct PRS triples across %d traditions</div>' % (n_triples, len(trip))]
    for trad in sorted(trip, key=lambda k: -len(trip[k])):
        rows = "".join('<div class="trow"><span class="pid">%s</span> %s%s</div>' %
                       (esc(tid), esc(lab), (' <span class="tprob">— %s</span>' % esc(prob[:140])) if prob else "")
                       for tid, lab, prob in trip[trad])
        triples_html.append('<details class="card"><summary><span class="trad t-%s">%s</span> '
                            '<span class="cnt">%d triples</span></summary><div class="body">%s</div></details>'
                            % (esc(trad), esc(trad), len(trip[trad]), rows))

    # ---- Bridges panel (per tradition-pair + synthesis essay) ----
    cross = parse_cross(vault, valid_keys)
    syn = parse_synthesis(vault)
    pairs = set(syn)
    for c in cross:
        for a in range(len(c["keys"])):
            for b in range(a + 1, len(c["keys"])):
                pairs.add((c["keys"][a], c["keys"][b]))
    bridges_html = ['<div class="ptot">%d cross-program items · %d tradition-pairs · %d synthesis essays</div>'
                    % (len(cross), len(pairs), len(syn))]
    for pair in sorted(pairs):
        ci = [c for c in cross if pair[0] in c["keys"] and pair[1] in c["keys"]]
        if not ci and pair not in syn:
            continue
        cross_rows = "".join(
            '<div class="brow"><span class="pid">%s</span> <b>%s</b>'
            '<div class="bmeta">%s · status %s</div>%s</div>' %
            (esc(c["id"]), esc(c["insight"]), esc(c["nature"]), esc(c["status"]),
             ('<div class="bnotes">%s</div>' % esc(c["notes"])) if c["notes"] else "")
            for c in ci)
        essay = ('<details class="narr"><summary>synthesis essay — %s_%s_bridge.md</summary>'
                 '<div class="body">%s</div></details>' % (pair[0], pair[1], md_lite(syn[pair]))) if pair in syn else ""
        flag = ' <span class="chip neutral">essay</span>' if pair in syn else ""
        bridges_html.append('<details class="card"><summary><span class="trad t-%s">%s</span> '
                           '<span class="x">×</span> <span class="trad t-%s">%s</span> '
                           '<span class="cnt">%d item%s</span>%s</summary>'
                           '<div class="body">%s%s</div></details>' %
                           (esc(pair[0]), esc(pair[0]), esc(pair[1]), esc(pair[1]),
                            len(ci), "s" if len(ci) != 1 else "", flag, cross_rows, essay))

    # ---- Findings panel (all, labeled by action) ----
    findings = parse_findings(vault)
    facts = {}
    for f in findings:
        cls, lbl = action_class(f["action"])
        facts[cls] = facts.get(cls, 0) + 1
        f["_cls"], f["_lbl"] = cls, lbl
    fbar = '<div class="fbar"><button class="fb on" data-f="all" onclick="ff(this)">All (%d)</button>' % len(findings)
    for cls, lbl in [("flag", "Flag for Tom"), ("esc", "Escalate"), ("mon", "Monitor"), ("arch", "Archive")]:
        if facts.get(cls):
            fbar += '<button class="fb" data-f="%s" onclick="ff(this)">%s (%d)</button>' % (cls, lbl, facts[cls])
    fbar += "</div>"
    findings_html = [fbar]
    for f in sorted(findings, key=lambda x: x["id"]):
        findings_html.append(
            '<details class="card f-%s" data-f="%s"><summary>'
            '<span class="pid">%s</span> <span class="chip a-%s">%s</span>'
            '<span class="ctitle">%s</span></summary>'
            '<div class="meta">%s · %s · confidence %s</div>'
            '<div class="body"><div class="ln">%s</div></div></details>' %
            (f["_cls"], f["_cls"], esc(f["id"]), f["_cls"], esc(f["_lbl"]),
             esc(f["etype"]), esc(f["programs"]), esc(f["date"]), esc(f["confidence"]),
             esc(f["finding"])))

    # ---- stats ----
    n_cards = len(props)
    n_dates = len(by_date)
    n_resp = len(demails["emails"])
    span = "%s → %s" % (min(by_date), max(by_date)) if by_date else "—"
    gen = datetime.now().strftime("%Y-%m-%d %H:%M")

    PRESERVE = (
        "Review pages were ephemeral local files (never emailed), so this archive is "
        "assembled from the durable sources: each <b>card</b> from its proposal file, each "
        "<b>response</b> from the verbatim decision email (and the processed decisions.md where one exists). "
        "<b>Zero card is dropped</b> — every proposal file is rendered in full below. "
        "One page-snapshot (2026-06-16) was overwritten before archiving and its original layout is not "
        "retained; its 13 cards survive intact as proposal files and appear in the Cards stream under their "
        "original proposal dates.")

    doc = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>C2A2 Review Log — Historical Preservation Archive</title>
<style>
:root{--bg:#0a0a0f;--panel:#14141c;--panel2:#1b1b26;--ink:#e8e8f0;--mut:#9a9ab0;--line:#2a2a3a;
--ok:#4E8A5E;--wait:#A8923A;--neutral:#5B7FA5;--accent:#C9A84C;--gap:#A85D3A;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
header{padding:22px 26px;border-bottom:1px solid var(--line);position:sticky;top:0;background:var(--bg);z-index:10}
h1{margin:0 0 4px;font-size:20px;color:var(--accent)}
.sub{color:var(--mut);font-size:13px}
.stats{margin-top:10px;display:flex;gap:18px;flex-wrap:wrap;font-size:13px}
.stats b{color:var(--ink)} .stats span{color:var(--mut)}
.note{margin:14px 26px 0;padding:12px 14px;background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:6px;font-size:13px;color:var(--mut)}
.note b{color:var(--ink)}
.tabs{display:flex;gap:6px;padding:14px 26px 0}
.tab{padding:8px 16px;border:1px solid var(--line);border-bottom:none;border-radius:8px 8px 0 0;background:var(--panel);color:var(--mut);cursor:pointer;font-size:14px}
.tab.on{background:var(--panel2);color:var(--ink);font-weight:600}
.tools{padding:8px 26px;display:flex;gap:10px;align-items:center}
.tools button{background:var(--panel2);color:var(--ink);border:1px solid var(--line);border-radius:6px;padding:5px 11px;cursor:pointer;font-size:12px}
main{padding:6px 26px 60px}
.view{display:none} .view.on{display:block}
.daygrp{margin:12px 0;border:1px solid var(--line);border-radius:8px;background:var(--panel);overflow:hidden}
.dayhdr{padding:10px 14px;cursor:pointer;font-weight:600;color:var(--accent);background:var(--panel2);user-select:none}
.cnt{color:var(--mut);font-weight:400;font-size:12px;margin-left:8px}
.card{margin:8px 12px;border:1px solid var(--line);border-radius:7px;background:var(--panel2)}
.card>summary{padding:9px 12px;cursor:pointer;list-style:none;display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.card>summary::-webkit-details-marker{display:none}
.pid{font-family:ui-monospace,Menlo,monospace;font-size:11px;color:var(--mut)}
.trad{font-size:11px;padding:1px 7px;border-radius:10px;border:1px solid var(--line)}
.ctitle{color:var(--ink);font-size:13px;flex:1;min-width:160px}
.chip{font-size:10px;padding:1px 7px;border-radius:10px;text-transform:uppercase;letter-spacing:.4px}
.chip.ok{background:rgba(78,138,94,.2);color:#7ed09a;border:1px solid var(--ok)}
.chip.wait{background:rgba(168,146,58,.2);color:#e0c969;border:1px solid var(--wait)}
.chip.neutral{background:rgba(91,127,165,.2);color:#a7c4e0;border:1px solid var(--neutral)}
.meta{padding:2px 14px;color:var(--mut);font-size:12px}
.src{padding:2px 14px 6px;font-size:12px} .src a{color:#a7c4e0}
.prov{padding:2px 14px 8px;font-size:12px;color:#7ed09a} .prov.gap{color:var(--gap)}
.body{padding:6px 14px 12px;border-top:1px solid var(--line);font-size:13px}
.body .sec{margin:10px 0 4px;font-size:12px;color:var(--accent);text-transform:uppercase;letter-spacing:.5px}
.body .cand-h{margin:8px 0 2px;font-family:ui-monospace,Menlo,monospace;font-size:12px;color:#e0c969}
.body .kv{margin:1px 0} .body .kv .k{color:var(--mut)}
.body .ln{white-space:pre-wrap} .body .sp{height:7px}
.resp .email{margin:8px 14px;padding:10px 12px;background:#0d0d14;border:1px solid var(--line);border-radius:6px;white-space:pre-wrap;font-family:ui-monospace,Menlo,monospace;font-size:12px;color:#cfe0cf}
.emeta{color:var(--mut);font-size:12px}
.narr{margin:0 14px 12px} .narr>summary{cursor:pointer;color:var(--mut);font-size:12px}
.resends{margin:14px 0;padding:12px 16px;background:var(--panel);border:1px solid var(--line);border-radius:8px;font-size:12px;color:var(--mut)}
.resends code,.meta code{background:#0d0d14;padding:1px 5px;border-radius:4px;font-size:11px}
.t-levin{color:#C45B5B}.t-friston{color:#5A8EAF}.t-hoffman{color:#C08B3E}.t-kastrup{color:#8B5DAB}
.t-mcgilchrist{color:#3D9E89}.t-hawkins{color:#B87D3E}.t-wolfram{color:#8aa0b0}.t-carroll{color:#4E8A5E}
.t-arkanihamed{color:#A85D3A}.t-fredrickson{color:#C47A9A}.t-stump{color:#A8923A}.t-rohr{color:#9A7A5A}
.t-wright{color:#7e8fc0}.t-loughran{color:#4A8A7A}.t-macintyre{color:#b0a0c0}
.ptot{padding:10px 4px;color:var(--mut);font-size:13px}
.card>summary .x{color:var(--mut)}
.trow{padding:2px 0;font-size:13px;border-bottom:1px solid var(--line)}
.tprob{color:var(--mut)}
.brow{padding:8px 0;border-bottom:1px solid var(--line);font-size:13px}
.bmeta{color:var(--mut);font-size:12px;margin:2px 0}
.bnotes{color:var(--ink);font-size:12px;margin-top:3px}
.a-flag{background:rgba(196,91,91,.2);color:#e08a8a;border:1px solid #C45B5B}
.a-esc{background:rgba(168,93,58,.2);color:#d99a78;border:1px solid #A85D3A}
.a-mon{background:rgba(168,146,58,.2);color:#e0c969;border:1px solid #A8923A}
.a-arch{background:rgba(91,127,165,.2);color:#a7c4e0;border:1px solid #5B7FA5}
.fbar{display:flex;gap:6px;flex-wrap:wrap;padding:8px 0}
.fb{background:var(--panel2);color:var(--mut);border:1px solid var(--line);border-radius:14px;padding:4px 12px;cursor:pointer;font-size:12px}
.fb.on{background:var(--accent);color:#1a1a10;font-weight:600;border-color:var(--accent)}
.card.hide{display:none}
</style></head><body>
<header>
<h1>C2A2 Review Log — Historical Preservation Archive</h1>
<div class="sub">Every proposal card and every decision response, chronological, rendered in full. Generated """ + gen + """.</div>
<div class="stats"><span>Cards: <b>""" + str(n_cards) + """</b></span><span>Review dates: <b>""" + str(n_dates) + """</b></span><span>Decision emails: <b>""" + str(n_resp) + """</b></span><span>PRS triples: <b>""" + str(n_triples) + """</b></span><span>Bridges: <b>""" + str(len(cross)) + """</b></span><span>Findings: <b>""" + str(len(findings)) + """</b></span><span>Span: <b>""" + span + """</b></span></div>
</header>
<div class="note"><b>Preservation note.</b> """ + PRESERVE + """</div>
<div class="tabs"><div class="tab on" data-v="cards" onclick="sw(this)">Cards (chronological)</div><div class="tab" data-v="resp" onclick="sw(this)">Your Responses</div><div class="tab" data-v="trip" onclick="sw(this)">PRS Triples</div><div class="tab" data-v="bridge" onclick="sw(this)">Bridges</div><div class="tab" data-v="find" onclick="sw(this)">Findings</div></div>
<div class="tools"><button onclick="ex(1)">Expand all</button><button onclick="ex(0)">Collapse all</button></div>
<main>
<div class="view on" id="v-cards">""" + "\n".join(cards_html) + """</div>
<div class="view" id="v-resp">""" + "\n".join(resp_html) + ("""
<div class="resends"><b>Decision-email resends / duplicates preserved:</b><ul>""" + resends + "</ul></div>" if resends else "") + """</div>
<div class="view" id="v-trip">""" + "\n".join(triples_html) + """</div>
<div class="view" id="v-bridge">""" + "\n".join(bridges_html) + """</div>
<div class="view" id="v-find">""" + "\n".join(findings_html) + """</div>
</main>
<script>
function sw(t){
  var tabs=document.querySelectorAll('.tab');
  for(var i=0;i<tabs.length;i++){tabs[i].classList.remove('on');}
  t.classList.add('on');
  var views=document.querySelectorAll('.view');
  for(var j=0;j<views.length;j++){views[j].classList.remove('on');}
  document.getElementById('v-'+t.getAttribute('data-v')).classList.add('on');
}
function ex(open){
  var view=document.querySelector('.view.on');
  var ds=view.querySelectorAll('details');
  for(var i=0;i<ds.length;i++){ds[i].open=!!open;}
}
function ff(btn){
  var bs=document.querySelectorAll('.fb');
  for(var i=0;i<bs.length;i++){bs[i].classList.remove('on');}
  btn.classList.add('on');
  var f=btn.getAttribute('data-f');
  var cards=document.querySelectorAll('#v-find .card');
  for(var j=0;j<cards.length;j++){
    var show=(f==='all'||cards[j].getAttribute('data-f')===f);
    cards[j].classList.toggle('hide',!show);
  }
}
</script>
</body></html>"""

    # Privacy: strike every email address from the PUBLISHED html (the local
    # provenance/decision_emails.json keeps the raw data, but it is gitignored).
    doc, n_scrub = re.subn(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", "[email removed]", doc)

    open(out_html, "w", encoding="utf-8").write(doc)
    print("wrote %s  (cards=%d dates=%d responses=%d, scrubbed %d email addresses)"
          % (out_html, n_cards, n_dates, n_resp, n_scrub))


if __name__ == "__main__":
    main()
