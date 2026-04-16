#!/usr/bin/env python3
"""
C2A2 Wiki — Daily Review Page Generator
Reads pending proposals, generates a self-contained HTML review page.
Usage: python3 generate_review_page.py [YYYY-MM-DD]
If date not provided, uses today.
"""

import os, sys, re, glob
from datetime import date, datetime

# ── Paths ────────────────────────────────────────────────────────────────────
SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))
WIKI_ROOT    = os.path.dirname(SCRIPT_DIR)
PROPOSALS_DIR = os.path.join(WIKI_ROOT, "inbox", "proposals", "pending")
REVIEW_DIR   = os.path.join(WIKI_ROOT, "review")
ARCHIVE_DIR  = os.path.join(REVIEW_DIR, "archive")
RECIPIENT    = "thomas.loughran@gmail.com"

run_date = sys.argv[1] if len(sys.argv) > 1 else date.today().isoformat()

# ── Load proposals ────────────────────────────────────────────────────────────
def parse_proposal(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()

    meta = {}
    fm = re.search(r"^---\n(.*?)\n---", text, re.DOTALL)
    if fm:
        for line in fm.group(1).splitlines():
            m = re.match(r"^(\w+):\s*(.+)$", line.strip())
            if m:
                meta[m.group(1)] = m.group(2).strip().strip('"')

    # Body sections
    summary     = _section(text, "Summary")
    why         = _section(text, "Why This Matters")
    cross       = _section(text, "Cross-Tradition Signals")
    prs_block   = _section(text, "Candidate PRS Triplets")

    # Parse individual PRS candidates
    candidates = []
    for block in re.split(r"\nPRS-CANDIDATE-\d+:", "\n" + prs_block):
        if not block.strip(): continue
        prob = _field(block, "Problem")
        res  = _field(block, "Resource")
        sol  = _field(block, "Solution")
        conf = _field(block, "Confidence")
        evid = _field(block, "Evidence")
        if prob:
            candidates.append({"P": prob, "R": res, "S": sol,
                                "conf": conf, "evidence": evid})

    return {
        **meta,
        "summary": summary,
        "why": why,
        "cross": cross,
        "candidates": candidates,
        "filename": os.path.basename(path),
        "path": path,
    }

def _section(text, heading):
    m = re.search(rf"##\s+{re.escape(heading)}.*?\n(.*?)(?=\n##|\Z)", text, re.DOTALL)
    return m.group(1).strip() if m else ""

def _field(block, name):
    m = re.search(rf"{name}:\s*(.+?)(?=\n\s+\w+:|\Z)", block, re.DOTALL)
    return m.group(1).strip() if m else ""

proposals = []
for p in sorted(glob.glob(os.path.join(PROPOSALS_DIR, "*.md"))):
    try:
        proposals.append(parse_proposal(p))
    except Exception as e:
        print(f"Warning: could not parse {p}: {e}")

if not proposals:
    print("No pending proposals found — no review page generated.")
    sys.exit(0)

# ── Thinker colors ────────────────────────────────────────────────────────────
THINKER_COLORS = {
    "levin":      "#1a6b3c",
    "friston":    "#8a4a00",
    "hoffman":    "#2a4a8a",
    "hawkins":    "#5a3000",
    "mcgilchrist":"#3a3a6a",
    "fredrickson":"#a0306a",
    "stump":      "#6a2a0a",
    "carroll":    "#7a1a1a",
    "arkanihamed":"#1a3a6a",
    "wolfram":    "#4a006a",
    "kastrup":    "#0a5a6a",
}

def color_for(prop):
    key = prop.get("tradition_key", "").lower()
    return THINKER_COLORS.get(key, "#555")

# ── Build HTML ────────────────────────────────────────────────────────────────
def badge(conf):
    colors = {"High": "#1a6b3c", "Medium": "#8a4a00", "Speculative": "#7a1a1a"}
    c = colors.get(conf, "#555")
    return f'<span style="background:{c};color:#fff;padding:1px 7px;border-radius:10px;font-size:10px;font-weight:700">{conf}</span>'

prop_cards = ""
sidebar_items = ""

for i, p in enumerate(proposals):
    pid   = f"PROP-{run_date}-{i+1:03d}"  # Always sequential — agent-assigned IDs collide
    thinker = p.get("thinker", "Unknown")
    title = p.get("source_title", "Untitled")
    stype = p.get("source_type", "source").upper()
    sdate = p.get("source_date", "")
    url   = p.get("source_url", "#")
    col   = color_for(p)

    cands_html = ""
    for j, c in enumerate(p["candidates"]):
        cands_html += f"""
        <div style="border-left:3px solid {col};padding:8px 12px;margin:8px 0;background:#fafafa;border-radius:0 4px 4px 0">
          <div style="font-size:10px;font-weight:700;color:#888;margin-bottom:4px">CANDIDATE PRS {j+1} — {badge(c['conf'])}</div>
          <div style="margin:3px 0"><span style="font-weight:900;color:#c0392b;width:14px;display:inline-block">P</span> {c['P']}</div>
          <div style="margin:3px 0"><span style="font-weight:900;color:#2a6496;width:14px;display:inline-block">R</span> {c['R']}</div>
          <div style="margin:3px 0"><span style="font-weight:900;color:#1a6b3c;width:14px;display:inline-block">S</span> {c['S']}</div>
          {f'<div style="margin-top:5px;font-size:11px;color:#666;font-style:italic">Evidence: {c["evidence"]}</div>' if c['evidence'] else ''}
        </div>"""

    cross_html = ""
    if p["cross"]:
        cross_html = f'<div style="margin-top:12px"><div style="font-size:10px;font-weight:700;color:#888;margin-bottom:4px">CROSS-TRADITION SIGNALS</div><div style="font-size:12.5px;color:#444">{p["cross"]}</div></div>'

    prop_cards += f"""
    <div class="prop-card" id="card-{pid}" style="display:none">
      <div style="background:{col}18;border-left:4px solid {col};padding:14px 18px;border-radius:0 6px 0 0">
        <div style="font-size:11px;font-weight:700;color:{col};letter-spacing:.05em">{thinker.upper()} · {stype}{(' · ' + sdate) if sdate else ''}</div>
        <div style="font-size:17px;font-weight:700;color:#222;margin:4px 0 2px">{title}</div>
        <a href="{url}" target="_blank" style="font-size:11px;color:{col};opacity:.8">{url[:80]}{'…' if len(url)>80 else ''}</a>
      </div>
      <div style="padding:16px 18px">
        <div style="font-size:11px;font-weight:700;color:#888;margin-bottom:4px">SUMMARY</div>
        <div style="font-size:13px;color:#333;line-height:1.5;margin-bottom:12px">{p['summary']}</div>
        {'<div style="font-size:11px;font-weight:700;color:#888;margin-bottom:4px">WHY IT MATTERS</div><div style="font-size:12.5px;color:#444;line-height:1.5;margin-bottom:12px">' + p['why'] + '</div>' if p['why'] else ''}
        <div style="font-size:11px;font-weight:700;color:#888;margin:12px 0 4px">CANDIDATE PRS TRIPLETS</div>
        {cands_html if cands_html else '<div style="color:#999;font-size:12px;font-style:italic">No candidates extracted</div>'}
        {cross_html}
      </div>
      <div style="padding:12px 18px 18px;border-top:1px solid #eee;display:flex;gap:10px;flex-wrap:wrap">
        <button onclick="decide('{pid}','APPROVE')"
          style="background:#1a6b3c;color:#fff;border:none;padding:8px 20px;border-radius:5px;cursor:pointer;font-weight:700;font-size:13px">
          ✓ Approve
        </button>
        <button onclick="decide('{pid}','CHECK')"
          style="background:#8a4a00;color:#fff;border:none;padding:8px 20px;border-radius:5px;cursor:pointer;font-weight:700;font-size:13px">
          ⚑ Double-check
        </button>
        <button onclick="decideChange('{pid}')"
          style="background:#2a4a8a;color:#fff;border:none;padding:8px 20px;border-radius:5px;cursor:pointer;font-weight:700;font-size:13px">
          ✎ Change
        </button>
        <button onclick="decide('{pid}','DENY')"
          style="background:#7a1a1a;color:#fff;border:none;padding:8px 20px;border-radius:5px;cursor:pointer;font-weight:700;font-size:13px">
          ✗ Deny
        </button>
        <div id="status-{pid}" style="font-size:12px;color:#666;align-self:center;font-style:italic"></div>
      </div>
    </div>"""

    sidebar_items += f"""
    <div class="sidebar-item" id="item-{pid}" onclick="showCard('{pid}')"
      style="padding:10px 14px;border-left:3px solid {col};margin-bottom:1px;cursor:pointer;background:#fff">
      <div style="font-size:10px;font-weight:700;color:{col};letter-spacing:.04em">{thinker.upper()}</div>
      <div style="font-size:12.5px;font-weight:600;color:#222;margin:2px 0;line-height:1.3">{title[:60]}{'…' if len(title)>60 else ''}</div>
      <div style="font-size:10px;color:#999">{stype} · {sdate}</div>
      <div id="badge-{pid}" style="margin-top:4px;font-size:10px;color:#999">⬜ Pending</div>
    </div>"""

n = len(proposals)
first_pid = proposals[0].get("proposal_id", f"PROP-{run_date}-001") if proposals else ""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>C2A2 Wiki Review — {run_date}</title>
<style>
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#f4f2ed;color:#222;height:100vh;display:flex;flex-direction:column}}
  #topbar{{background:#1a1a2e;color:#fff;padding:10px 20px;display:flex;align-items:center;justify-content:space-between;flex-shrink:0}}
  #topbar h1{{font-size:15px;font-weight:700;letter-spacing:.03em}}
  #topbar .meta{{font-size:12px;opacity:.7}}
  #main{{display:flex;flex:1;overflow:hidden}}
  #sidebar{{width:300px;flex-shrink:0;overflow-y:auto;background:#f9f7f2;border-right:1px solid #ddd}}
  #sidebar-header{{padding:10px 14px;background:#f0ede5;border-bottom:1px solid #ddd;font-size:11px;font-weight:700;color:#888;letter-spacing:.06em}}
  #content{{flex:1;overflow-y:auto;padding:20px}}
  .prop-card{{background:#fff;border-radius:8px;box-shadow:0 1px 4px rgba(0,0,0,.08);margin-bottom:20px;overflow:hidden}}
  .sidebar-item:hover{{background:#f0ede5!important}}
  .sidebar-item.active{{background:#e8e4d8!important}}
  #bottombar{{background:#fff;border-top:1px solid #ddd;padding:12px 20px;display:flex;align-items:center;gap:14px;flex-shrink:0}}
  #progress{{font-size:13px;color:#666}}
  #submit-btn{{background:#1a1a2e;color:#fff;border:none;padding:10px 24px;border-radius:6px;cursor:pointer;font-weight:700;font-size:14px;margin-left:auto}}
  #submit-btn:hover{{background:#2a2a4e}}
  #all-done{{color:#1a6b3c;font-weight:700;display:none}}
</style>
</head>
<body>
<div id="topbar">
  <h1>C2A2 Wiki — Daily Proposal Review</h1>
  <div class="meta">{run_date} &nbsp;·&nbsp; {n} proposal{'s' if n!=1 else ''} pending</div>
</div>
<div id="main">
  <div id="sidebar">
    <div id="sidebar-header">PROPOSALS — {run_date}</div>
    {sidebar_items}
  </div>
  <div id="content">
    <div id="welcome" style="color:#888;font-size:14px;padding:40px 20px;text-align:center;line-height:2">
      <div style="font-size:32px;margin-bottom:12px">📬</div>
      <strong>{n} new proposal{'s' if n!=1 else ''}</strong> from the C2A2 hunt agents.<br>
      Click any item on the left to review it.<br>
      Use the buttons to Approve, Double-check, Change, or Deny each one.<br>
      When done, hit <strong>Send Decisions</strong> below.
    </div>
    {prop_cards}
  </div>
</div>
<div id="bottombar">
  <div id="progress">0 / {n} reviewed</div>
  <div id="all-done">✓ All reviewed!</div>
  <button id="submit-btn" onclick="submitDecisions()">Send Decisions →</button>
</div>

<script>
const TOTAL = {n};
const decisions = {{}};
const notes = {{}};

function showCard(pid) {{
  document.querySelectorAll('.prop-card').forEach(c => c.style.display='none');
  document.querySelectorAll('.sidebar-item').forEach(s => s.classList.remove('active'));
  document.getElementById('card-'+pid).style.display='block';
  document.getElementById('item-'+pid).classList.add('active');
  document.getElementById('welcome').style.display='none';
}}

function decide(pid, decision) {{
  decisions[pid] = decision;
  notes[pid] = notes[pid] || '';
  updateBadge(pid, decision);
  updateProgress();
  // Auto-advance to next pending
  const items = Array.from(document.querySelectorAll('.sidebar-item'));
  const cur = items.findIndex(el => el.id === 'item-'+pid);
  const next = items.slice(cur+1).find(el => !decisions[el.id.replace('item-','')]);
  if (next) showCard(next.id.replace('item-',''));
}}

function decideChange(pid) {{
  const note = prompt('What should be changed?\\n(Your note will be sent with the decision)', '');
  if (note === null) return;
  decisions[pid] = 'CHANGE';
  notes[pid] = note;
  updateBadge(pid, 'CHANGE', note);
  updateProgress();
  const items = Array.from(document.querySelectorAll('.sidebar-item'));
  const cur = items.findIndex(el => el.id === 'item-'+pid);
  const next = items.slice(cur+1).find(el => !decisions[el.id.replace('item-','')]);
  if (next) showCard(next.id.replace('item-',''));
}}

function updateBadge(pid, decision, note='') {{
  const colors = {{APPROVE:'#1a6b3c',CHECK:'#8a4a00',CHANGE:'#2a4a8a',DENY:'#7a1a1a'}};
  const labels = {{APPROVE:'✓ Approved',CHECK:'⚑ Flagged for check',CHANGE:'✎ Change requested',DENY:'✗ Denied'}};
  const badge = document.getElementById('badge-'+pid);
  badge.style.color = colors[decision] || '#555';
  badge.style.fontWeight = '700';
  badge.textContent = labels[decision] + (note ? ' — '+note.slice(0,30) : '');
  const status = document.getElementById('status-'+pid);
  if (status) {{
    status.style.color = colors[decision];
    status.textContent = labels[decision] + (note ? ': '+note : '');
  }}
}}

function updateProgress() {{
  const done = Object.keys(decisions).length;
  document.getElementById('progress').textContent = done + ' / ' + TOTAL + ' reviewed';
  if (done >= TOTAL) {{
    document.getElementById('all-done').style.display='inline';
    document.getElementById('submit-btn').style.background='#1a6b3c';
  }}
}}

function submitDecisions() {{
  const lines = ['DECISIONS:'];
  const pids = {[f'PROP-{run_date}-{i+1:03d}' for i in range(len(proposals))]!r};
  pids.forEach(pid => {{
    const d = decisions[pid] || 'PENDING';
    const n = notes[pid] ? ' | ' + notes[pid] : '';
    lines.push(pid + ': ' + d + n);
  }});
  const body = lines.join('\\n');
  const subject = '[C2A2-review-decision] {run_date}';
  // Open Gmail compose directly — avoids Apple Mail / default mail client
  const gmailUrl = 'https://mail.google.com/mail/?view=cm&fs=1&to={RECIPIENT}&su='
    + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
  window.open(gmailUrl, '_blank');
}}

// Show first card on load
window.addEventListener('load', () => {{ showCard('{first_pid}'); }});
</script>
</body>
</html>"""

# ── Write output ──────────────────────────────────────────────────────────────
out_path = os.path.join(REVIEW_DIR, f"{run_date}_review.html")
os.makedirs(REVIEW_DIR, exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Review page written: {out_path}")
print(f"Proposals included: {n}")
for p in proposals:
    print(f"  {p.get('proposal_id','?')} — {p.get('thinker','?')}: {p.get('source_title','?')[:60]}")
