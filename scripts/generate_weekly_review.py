#!/usr/bin/env python3
"""
generate_weekly_review.py — Generates a self-contained HTML weekly review page.

Usage:
    python3 generate_weekly_review.py [--week YYYY-WNN] [--summa-vault PATH] [--output PATH]

Defaults:
    --week       current ISO week (Mon–Sun)
    --summa-vault  ~/Documents/Claude/Projects/Summa 2026 in a Year/vault
    --output     <wiki>/review/YYYY-WNN_weekly_review.html

The generated page shows:
  - Week summary (days processed, Summa questions, Pars, word count)
  - QC dashboard (one row per day: outcome, fidelity, QC timestamp)
  - Representative synthesis (last day of week, rendered)
  - Approve button → POST /api/approve → serve_wiki.py writes to QC log
"""

import argparse
import datetime
import json
import os
import re
import sys


# ── Helpers ──────────────────────────────────────────────────────────────────

def iso_week_bounds(iso_year, iso_week):
    """Return (monday, sunday) as date objects for the given ISO week."""
    jan4 = datetime.date(iso_year, 1, 4)
    start_of_w1 = jan4 - datetime.timedelta(days=jan4.weekday())
    monday = start_of_w1 + datetime.timedelta(weeks=iso_week - 1)
    sunday = monday + datetime.timedelta(days=6)
    return monday, sunday


def parse_frontmatter(path):
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
        m = re.match(r'^(\w[\w_]*):\s*(.*)', line)
        if m:
            meta[m.group(1).strip()] = m.group(2).strip().strip('"')
    return meta


def read_pace_tracker(vault_dir):
    """Return list of dicts for each row: {date, day_range, cumulative, pars, done}."""
    path = os.path.join(vault_dir, "_index", "Pace tracker.md")
    rows = []
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                # Match table rows like: | 2026-05-07 | Thu | 56–60 | 60 | Prima Pars (I) | ... | ✅ |
                m = re.match(
                    r'\|\s*(202\d-\d{2}-\d{2})\s*\|[^|]+\|\s*(\d+)[–-](\d+)\s*\|\s*(\d+)\s*\|([^|]+)\|[^|]*\|([^|]*)\|',
                    line)
                if m:
                    rows.append({
                        "date": datetime.date.fromisoformat(m.group(1)),
                        "day_start": int(m.group(2)),
                        "day_end":   int(m.group(3)),
                        "cumulative": int(m.group(4)),
                        "pars":       m.group(5).strip(),
                        "done":       "✅" in m.group(6),
                    })
    except OSError:
        pass
    return rows


def read_qc_log(vault_dir):
    """Return set of day numbers that have a human QC log entry."""
    path = os.path.join(vault_dir, "_index", "QC log.md")
    logged_days = set()
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                m = re.match(r'\|\s*[\d\-T:]+\s*\|\s*(\d+)\s*\|', line)
                if m:
                    logged_days.add(int(m.group(1)))
    except OSError:
        pass
    return logged_days


def get_transcript_meta(vault_dir, day):
    """Return frontmatter dict for the given day's transcript."""
    trans_dir = os.path.join(vault_dir, "transcripts")
    for fname in os.listdir(trans_dir):
        if re.match(rf"Day-{day:03d}", fname):
            return parse_frontmatter(os.path.join(trans_dir, fname)), fname
    return {}, None


def get_synthesis_text(vault_dir, day):
    """Return (filename, text) for the given day's synthesis."""
    synth_dir = os.path.join(vault_dir, "synthesis")
    for fname in sorted(os.listdir(synth_dir)):
        if re.match(rf"Day-{day:03d}", fname):
            path = os.path.join(synth_dir, fname)
            try:
                with open(path, encoding="utf-8") as f:
                    return fname, f.read()
            except OSError:
                pass
    return None, ""


def week_word_count(vault_dir, days):
    total = 0
    for day in days:
        meta, _ = get_transcript_meta(vault_dir, day)
        wc = meta.get("word_count") or meta.get("raw_asr_word_count") or "0"
        try:
            total += int(str(wc).split()[0])
        except (ValueError, IndexError):
            pass
    return total


# ── HTML generation ───────────────────────────────────────────────────────────

QC_PILL = {
    "pass":    ('<span style="background:#1a4a1a;color:#4ec94e;padding:2px 8px;border-radius:12px;font-size:0.85em">pass</span>'),
    "fail":    ('<span style="background:#4a1a1a;color:#e05050;padding:2px 8px;border-radius:12px;font-size:0.85em">fail</span>'),
    "pending": ('<span style="background:#2a2a1a;color:#c8b840;padding:2px 8px;border-radius:12px;font-size:0.85em">pending</span>'),
}

FIDELITY_PILL = {
    True:  '<span style="color:#4ec94e;font-size:1.1em" title="checked">✓</span>',
    False: '<span style="color:#888;font-size:1.1em" title="not checked">—</span>',
}


def build_qc_rows(vault_dir, days, logged_days):
    rows_html = ""
    all_pass = True
    for day in days:
        meta, fname = get_transcript_meta(vault_dir, day)
        title    = meta.get("title", f"Day {day}")
        qc_out   = (meta.get("last_qc_outcome") or "pending").lower().strip()
        fid_raw  = str(meta.get("fidelity_checked", "false")).lower()
        fid      = fid_raw in ("true", "1", "yes")
        qc_at    = meta.get("last_qc_at", "—")
        summa_ref = meta.get("summa_ref", "—")
        human    = "✓" if day in logged_days else "—"
        if qc_out != "pass":
            all_pass = False
        qc_pill  = QC_PILL.get(qc_out, QC_PILL["pending"])
        fid_pill = FIDELITY_PILL.get(fid, FIDELITY_PILL[False])
        rows_html += (
            f'<tr>'
            f'<td style="padding:6px 10px;color:#ccc">Day {day}</td>'
            f'<td style="padding:6px 10px;color:#e8d5a0">{title}</td>'
            f'<td style="padding:6px 10px;color:#888;font-size:0.85em">{summa_ref}</td>'
            f'<td style="padding:6px 10px;text-align:center">{qc_pill}</td>'
            f'<td style="padding:6px 10px;text-align:center">{fid_pill}</td>'
            f'<td style="padding:6px 10px;color:#666;font-size:0.8em">{qc_at[:10] if qc_at != "—" else "—"}</td>'
            f'<td style="padding:6px 10px;text-align:center;color:#4ec94e">{human}</td>'
            f'</tr>\n'
        )
    return rows_html, all_pass


def escape_js_string(s):
    return s.replace("\\", "\\\\").replace("`", "\\`").replace("$", "\\$")


def generate_html(week_label, iso_year, iso_week, monday, sunday,
                  batch_rows, all_days, qc_rows_html, all_pass,
                  synth_fname, synth_text, total_words,
                  pars_label, vault_dir, output_path):

    day_range_str = f"Days {all_days[0]}–{all_days[-1]}" if all_days else "No days"
    q_refs = []
    for day in all_days:
        meta, _ = get_transcript_meta(vault_dir, day)
        ref = meta.get("summa_ref", "")
        qs = re.findall(r"Q\.(\d+)", ref)
        q_refs.extend(qs)
    q_range = f"Q.{min(q_refs)}–Q.{max(q_refs)}" if q_refs else "—"

    status_color = "#4ec94e" if all_pass else "#e08840"
    status_text  = "All QC checks passed" if all_pass else "⚠ Some QC checks need attention"

    synth_escaped = escape_js_string(synth_text)
    rep_day = all_days[-1] if all_days else 0
    rep_meta, _ = get_transcript_meta(vault_dir, rep_day) if all_days else ({}, None)
    rep_title = rep_meta.get("title", f"Day {rep_day}")

    approve_payload = json.dumps({
        "week": week_label,
        "days": all_days,
        "reviewer": "Tom Loughran",
        "timestamp": datetime.datetime.now().isoformat()[:19],
        "qc_status": "pass" if all_pass else "needs-attention",
    })

    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Weekly Review — """ + week_label + """</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/9.1.6/marked.min.js"></script>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { background: #0a0a0f; color: #d4c9a8; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; padding: 32px; }
  h1 { color: #e8d5a0; font-size: 1.6em; font-weight: 600; }
  h2 { color: #c8b840; font-size: 1.1em; font-weight: 600; margin: 28px 0 12px; text-transform: uppercase; letter-spacing: 0.08em; }
  .subtitle { color: #888; font-size: 0.9em; margin-top: 4px; }
  .stats-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin: 20px 0; }
  .stat { background: #12121a; border: 1px solid #2a2a3a; border-radius: 8px; padding: 14px 18px; }
  .stat-val { font-size: 1.6em; color: #e8d5a0; font-weight: 600; }
  .stat-lbl { font-size: 0.8em; color: #888; margin-top: 4px; }
  .qc-status { padding: 10px 16px; border-radius: 6px; font-size: 0.9em; display: inline-block; margin-bottom: 12px; }
  table { width: 100%; border-collapse: collapse; background: #12121a; border-radius: 8px; overflow: hidden; }
  th { background: #1a1a2a; color: #888; font-size: 0.8em; text-transform: uppercase; letter-spacing: 0.06em; padding: 8px 10px; text-align: left; }
  tr:nth-child(even) { background: #0f0f18; }
  .synthesis-box { background: #12121a; border: 1px solid #2a2a3a; border-radius: 8px; padding: 24px; margin-top: 12px; max-height: 520px; overflow-y: auto; font-size: 0.92em; line-height: 1.7; }
  .synthesis-box h1, .synthesis-box h2, .synthesis-box h3 { color: #c8b840; margin: 18px 0 8px; }
  .synthesis-box p { margin-bottom: 12px; }
  .synthesis-box strong { color: #e8d5a0; }
  .synthesis-box em { color: #b8a878; }
  .synthesis-box li { margin-left: 20px; margin-bottom: 6px; }
  .synthesis-box a { color: #8899cc; }
  .approve-btn { display: block; width: 100%; padding: 18px; margin-top: 32px; background: #2a4a1a; border: 1px solid #4a8a2a; border-radius: 10px; color: #8ade5a; font-size: 1.15em; font-weight: 600; cursor: pointer; transition: all 0.15s; letter-spacing: 0.03em; }
  .approve-btn:hover { background: #3a6a22; border-color: #6aca3a; }
  .approve-btn:disabled { background: #1a2a14; border-color: #2a3a1a; color: #4a6a3a; cursor: default; }
  .approve-msg { margin-top: 14px; padding: 12px 16px; border-radius: 6px; font-size: 0.9em; display: none; }
  .week-badge { display: inline-block; background: #1a1a2a; border: 1px solid #3a3a5a; border-radius: 4px; padding: 2px 10px; font-size: 0.85em; color: #8899cc; margin-left: 10px; vertical-align: middle; }
</style>
</head>
<body>

<div style="max-width:900px;margin:0 auto">

  <h1>Weekly Review <span class="week-badge">""" + week_label + """</span></h1>
  <p class="subtitle">""" + monday.strftime("%B %-d") + "–" + sunday.strftime("%-d, %Y") + " &nbsp;·&nbsp; " + pars_label + """</p>

  <h2>Progress this week</h2>
  <div class="stats-grid">
    <div class="stat"><div class="stat-val">""" + str(len(all_days)) + """</div><div class="stat-lbl">Days processed</div></div>
    <div class="stat"><div class="stat-val">""" + day_range_str + """</div><div class="stat-lbl">Episode range</div></div>
    <div class="stat"><div class="stat-val">""" + q_range + """</div><div class="stat-lbl">Summa questions</div></div>
    <div class="stat"><div class="stat-val">""" + f"{total_words:,}" + """</div><div class="stat-lbl">Transcript words</div></div>
  </div>

  <h2>QC controls</h2>
  <div class="qc-status" style="background:""" + ("#1a3a1a" if all_pass else "#3a2a0a") + """;border:1px solid """ + (status_color) + """;color:""" + status_color + """">
    """ + status_text + """
  </div>
  <table>
    <thead><tr>
      <th>Day</th><th>Title</th><th>Summa ref</th>
      <th style="text-align:center">Auto QC</th>
      <th style="text-align:center">Fidelity</th>
      <th>Last checked</th>
      <th style="text-align:center">Human log</th>
    </tr></thead>
    <tbody>
""" + qc_rows_html + """    </tbody>
  </table>

  <h2>Representative sample — Day """ + str(rep_day) + """: """ + rep_title + """</h2>
  <p style="color:#888;font-size:0.85em;margin-bottom:8px">""" + (synth_fname or "synthesis not found") + """</p>
  <div class="synthesis-box" id="synthesis-box">Loading…</div>

  <button class="approve-btn" id="approve-btn" onclick="approveWeek()">
    ✓ &nbsp; Approve """ + week_label + """ — """ + day_range_str + """
  </button>
  <div class="approve-msg" id="approve-msg"></div>

</div>

<script>
const synthText = `""" + synth_escaped + """`;

document.addEventListener('DOMContentLoaded', function() {
  const box = document.getElementById('synthesis-box');
  if (typeof marked !== 'undefined') {
    box.innerHTML = marked.parse(synthText);
  } else {
    box.textContent = synthText;
  }
});

function approveWeek() {
  const btn = document.getElementById('approve-btn');
  const msg = document.getElementById('approve-msg');
  btn.disabled = true;
  btn.textContent = 'Saving approval…';

  const payload = """ + approve_payload + """;

  fetch('/api/approve', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(payload)
  })
  .then(r => r.json())
  .then(data => {
    if (data.ok) {
      btn.textContent = '✓ Approved — ' + payload.week;
      msg.style.display = 'block';
      msg.style.background = '#1a3a1a';
      msg.style.border = '1px solid #4ec94e';
      msg.style.color = '#4ec94e';
      msg.textContent = 'Approval recorded in QC log at ' + payload.timestamp + '.';
    } else {
      throw new Error(data.error || 'Unknown error');
    }
  })
  .catch(err => {
    btn.disabled = false;
    btn.textContent = '✓  Approve """ + week_label + """';
    msg.style.display = 'block';
    msg.style.background = '#3a1a1a';
    msg.style.border = '1px solid #e05050';
    msg.style.color = '#e05050';
    msg.textContent = 'Error: ' + err.message + ' — make sure the wiki server is running (launch_summa.command).';
  });
}
</script>
</body>
</html>"""

    return html


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Generate weekly Summa review HTML")
    parser.add_argument("--week",        help="ISO week e.g. 2026-W20 (default: current week)")
    parser.add_argument("--summa-vault", help="Path to Summa 2026 vault",
                        default=os.path.expanduser(
                            "~/Documents/Claude/Projects/Summa 2026 in a Year/vault"))
    parser.add_argument("--wiki-dir",    help="Path to wiki/ dir (for output)",
                        default=os.path.expanduser(
                            "~/Documents/Claude/Projects/RC Karpathy Wiki Project/wiki"))
    parser.add_argument("--output",      help="Output HTML path (overrides default)")
    args = parser.parse_args()

    vault_dir = os.path.expanduser(args.summa_vault)
    wiki_dir  = os.path.expanduser(args.wiki_dir)

    # Parse target week
    today = datetime.date.today()
    if args.week:
        m = re.match(r"(\d{4})-W(\d{1,2})$", args.week)
        if not m:
            print(f"ERROR: --week must be YYYY-WNN, got: {args.week}", file=sys.stderr)
            sys.exit(1)
        iso_year, iso_week = int(m.group(1)), int(m.group(2))
    else:
        iso_year, iso_week, _ = today.isocalendar()

    week_label = f"{iso_year}-W{iso_week:02d}"
    monday, sunday = iso_week_bounds(iso_year, iso_week)

    # Find pace tracker rows for this week
    all_rows    = read_pace_tracker(vault_dir)
    week_rows   = [r for r in all_rows if monday <= r["date"] <= sunday]
    done_rows   = [r for r in week_rows if r["done"]]

    # Collect individual day numbers
    all_days = []
    for r in done_rows:
        all_days.extend(range(r["day_start"], r["day_end"] + 1))
    all_days = sorted(set(all_days))

    if not all_days:
        # Fallback: include all completed rows up to today even if outside window
        print(f"No completed days found in {week_label}. Including last 5 completed days.", file=sys.stderr)
        done_all = [r for r in all_rows if r["done"]][-5:]
        for r in done_all:
            all_days.extend(range(r["day_start"], r["day_end"] + 1))
        all_days = sorted(set(all_days))

    pars_labels = list(dict.fromkeys(r["pars"] for r in done_rows)) if done_rows else ["—"]
    pars_label  = " → ".join(pars_labels)

    logged_days = read_qc_log(vault_dir)
    qc_rows_html, all_pass = build_qc_rows(vault_dir, all_days, logged_days)

    total_words = week_word_count(vault_dir, all_days)

    rep_day = all_days[-1] if all_days else 0
    synth_fname, synth_text = get_synthesis_text(vault_dir, rep_day) if rep_day else (None, "")

    output_path = args.output or os.path.join(wiki_dir, "review", f"{week_label}_weekly_review.html")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    html = generate_html(
        week_label, iso_year, iso_week, monday, sunday,
        done_rows, all_days, qc_rows_html, all_pass,
        synth_fname, synth_text, total_words,
        pars_label, vault_dir, output_path
    )

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Weekly review written: {output_path}")
    print(f"  Week:  {week_label}  ({monday} – {sunday})")
    print(f"  Days:  {all_days}")
    print(f"  Words: {total_words:,}")
    print(f"  QC:    {'all pass' if all_pass else 'NEEDS ATTENTION'}")


if __name__ == "__main__":
    main()
