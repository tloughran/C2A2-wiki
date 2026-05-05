#!/usr/bin/env python3
"""
Generate an interactive HTML visualization of a wiki vault's growth.
Usage: python generate_visualization.py <input.json> <output.html>
"""

import json
import sys
import os
from pathlib import Path


def load_json(filepath):
    """Load JSON data from file."""
    with open(filepath, 'r') as f:
        return json.load(f)


COLORS = {
    'master': '#C9A84C',
    'architecture': '#5B7FA5',
    'architecture/changelog': '#4A6580',
    'flags': '#B85450',
    'agents': '#8B6DAE',
    'inbox': '#7A8B8B',
    'review': '#5E9B76',
    'deferred': '#6B7B7B',
    'sessions': '#8A9098',
    'root': '#9A9A9A',
    'tools': '#4E9EA8',
    'traditions/levin':       '#C45B5B',
    'traditions/friston':     '#5A8EAF',
    'traditions/hoffman':     '#C08B3E',
    'traditions/kastrup':     '#8B5DAB',
    'traditions/mcgilchrist': '#3D9E89',
    'traditions/hawkins':     '#B87D3E',
    'traditions/wolfram':     '#4A5E6D',
    'traditions/carroll':     '#4E8A5E',
    'traditions/arkanihamed': '#A85D3A',
    'traditions/fredrickson': '#C47A9A',
    'traditions/stump':       '#A8923A',
    'traditions/macintyre':   '#7A6B8A',
    'traditions/rohr':        '#9A7A5A',
    'traditions/wright':      '#5A72A8',
    'traditions/loughran':    '#4A8A7A',
}

# Canonical labels for filter rows. Falls back to title-casing the path tail
# when not specified. Without this, e.g. 'mcgilchrist' rendered as 'Mcgilchrist'
# (lowercase g), which contradicts the body-text canonical 'McGilchrist'.
LABEL_OVERRIDES = {
    'master':                 'Master',
    'architecture/changelog': 'Changelog',
    'traditions/mcgilchrist': 'McGilchrist',
    'traditions/macintyre':   'MacIntyre',
    'traditions/arkanihamed': 'Arkani-Hamed',
}


def get_group(directory):
    """Map directory to a group name for coloring."""
    d = directory.lower().strip('/')
    if d in COLORS:
        return d
    # Handle sub-paths like inbox/proposals/approved -> inbox
    for key in COLORS:
        if d.startswith(key):
            return key
    return 'root'


def sanitize_braces(text):
    """Remove double-brace patterns that would trip the validator."""
    # Repeatedly collapse multiple braces to single braces
    while '{{' in text or '}}' in text:
        text = text.replace('{{', '{').replace('}}', '}')
    return text


def build_graph_data(data):
    """Build nodes and links arrays from vault data."""
    files = data.get('files', [])
    connections = data.get('connections', {})

    # Build a set of filepaths for valid nodes
    filepath_set = set()
    for f in files:
        filepath_set.add(f['filepath'])

    # Count connections per file
    conn_count = {}
    wikilink_edges = connections.get('wikilink_edges', [])
    reference_edges = connections.get('reference_edges', [])

    for edge in wikilink_edges:
        s, t = edge['source'], edge['target']
        conn_count[s] = conn_count.get(s, 0) + 1
        conn_count[t] = conn_count.get(t, 0) + 1

    for edge in reference_edges:
        s, t = edge['source'], edge['target']
        conn_count[s] = conn_count.get(s, 0) + 1
        conn_count[t] = conn_count.get(t, 0) + 1

    nodes = []
    for f in files:
        fp = f['filepath']
        group = get_group(f.get('directory', 'root'))
        color = COLORS.get(group, '#CCCCCC')
        cc = conn_count.get(fp, 0)
        size = max(2, min(5, 2 + min(cc, 3)))
        nodes.append({
            'id': fp,
            'label': f.get('title', f.get('filename', fp)),
            'directory': f.get('directory', ''),
            'date': f.get('date', ''),
            'color': color,
            'group': group,
            'size': size,
            'content': sanitize_braces(f.get('content', '')),
        })

    # Pass-A architecture: emit ALL edges with score COMPONENTS, not a single
    # score. The browser combines components per the active Mode picker so the
    # user can re-rank live. The browser also enforces the visibility budget
    # (top-N by score, where N varies with zoom × cuts) — we no longer cap here.
    import math
    links = []
    seen_links = set()
    mention_edges = connections.get('mention_edges', [])

    def _components(s, t, etype, bridge):
        """Per-edge score components.

        deg     — log-product of endpoint degrees (structural density)
        type    — wikilink=3, mention=2, reference=1 (editorial intent)
        bridge  — 1.0 if endpoints in different categories, else 0.0
        """
        deg_s = conn_count.get(s, 0)
        deg_t = conn_count.get(t, 0)
        deg = math.log(deg_s + 1) + math.log(deg_t + 1)
        type_w = {'wikilink': 3.0, 'mention': 2.0, 'reference': 1.0}.get(etype, 1.0)
        bridge_w = 1.0 if bridge == 'cross' else 0.0
        return {'deg': round(deg, 3), 'type': type_w, 'bridge': bridge_w}

    def _bridge_class(src_dir, tgt_dir):
        return 'same' if src_dir == tgt_dir else 'cross'

    # Build a fast lookup for directory category per filepath (used to compute
    # bridge when the source edge dict didn't carry it).
    fp_to_dir = {f['filepath']: f.get('directory', '') for f in files}

    def _emit(s, t, etype, base_bridge=None, reference=None):
        if s not in filepath_set or t not in filepath_set:
            return
        key = (s, t) if s < t else (t, s)
        if key in seen_links:
            return
        seen_links.add(key)
        bridge = base_bridge or _bridge_class(fp_to_dir.get(s, ''), fp_to_dir.get(t, ''))
        comp = _components(s, t, etype, bridge)
        edge = {
            'source': s, 'target': t, 'type': etype, 'bridge': bridge,
            'score_deg': comp['deg'],
            'score_type': comp['type'],
            'score_bridge': comp['bridge'],
        }
        if reference:
            edge['reference'] = reference
        links.append(edge)

    for e in wikilink_edges:
        _emit(e['source'], e['target'], 'wikilink', e.get('bridge'))
    for e in mention_edges:
        _emit(e['source'], e['target'], 'mention', e.get('bridge'))
    for e in reference_edges:
        _emit(e['source'], e['target'], 'reference', e.get('bridge'), reference=e.get('reference'))

    return nodes, links


def generate_html(data, nodes_json, links_json):
    """Generate the complete HTML visualization."""
    metadata = data.get('metadata', {})
    total_files = metadata.get('total_files', 0)
    findings = data.get('findings', [])
    decisions = data.get('decisions', [])
    cross_connections = data.get('cross_connections', [])
    changelogs = data.get('changelogs', {})
    cowork_summaries = data.get('cowork_summaries', {})
    timeline = data.get('timeline', [])

    findings_json = json.dumps(findings, ensure_ascii=False)
    decisions_json = json.dumps(decisions, ensure_ascii=False)
    cross_json = json.dumps(cross_connections, ensure_ascii=False)
    changelogs_json = json.dumps(changelogs, ensure_ascii=False)
    cowork_json = json.dumps(cowork_summaries, ensure_ascii=False)
    timeline_json = json.dumps(timeline, ensure_ascii=False)
    colors_json = json.dumps(COLORS, ensure_ascii=False)

    date_range = metadata.get('date_range', {})
    date_start = date_range.get('start', '')
    date_end = date_range.get('end', '')

    # Build filter groups for the left panel. Honor LABEL_OVERRIDES so canonical
    # spellings (McGilchrist / MacIntyre / Arkani-Hamed) appear in the UI rather
    # than the .title()-defaulted versions.
    tradition_groups = []
    structure_groups = []
    for key, color in COLORS.items():
        if key in LABEL_OVERRIDES:
            label = LABEL_OVERRIDES[key]
        else:
            label = key.split('/')[-1].title() if '/' in key else key.title()
        entry = {'key': key, 'color': color, 'label': label}
        if key.startswith('traditions/'):
            tradition_groups.append(entry)
        else:
            structure_groups.append(entry)

    tradition_groups_json = json.dumps(tradition_groups, ensure_ascii=False)
    structure_groups_json = json.dumps(structure_groups, ensure_ascii=False)

    num_findings = len(findings)
    num_decisions = len(decisions)

    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>C2A2 Wiki Narration</title>
<script src="https://d3js.org/d3.v7.min.js"></script>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: 100%; height: 100%; overflow: hidden; font-family: 'Segoe UI', system-ui, sans-serif; background: #0a0a0f; color: #e0e0e0; }
#app { display: flex; flex-direction: column; height: 100vh; }

/* HEADER */
#header { display: flex; align-items: center; justify-content: space-between; padding: 8px 16px; background: #111118; border-bottom: 1px solid #2a2a3a; height: 48px; flex-shrink: 0; }
#header .title { font-size: 16px; font-weight: 700; color: #FFD700; }
#header .stats { display: flex; gap: 12px; font-size: 12px; color: #999; }
#header .stats span { background: #1a1a2a; padding: 2px 8px; border-radius: 4px; }
#header .controls { display: flex; gap: 8px; align-items: center; }
#header .controls button { background: #1a1a2a; border: 1px solid #3a3a4a; color: #e0e0e0; padding: 4px 10px; border-radius: 4px; cursor: pointer; font-size: 12px; }
#header .controls button:hover { background: #2a2a3a; }
#header .controls button.active { background: #FFD700; color: #0a0a0f; border-color: #FFD700; }
.brightness-control { display: flex; align-items: center; gap: 4px; font-size: 12px; }
.brightness-control input { width: 60px; }

/* MAIN */
#main { display: flex; flex: 1; overflow: hidden; position: relative; }

/* LEFT PANEL */
#left-panel { width: 200px; flex-shrink: 0; background: #0e0e16; border-right: none; overflow-y: auto; padding: 8px; font-size: 12px; }
.resize-handle { width: 5px; flex-shrink: 0; background: #2a2a3a; cursor: col-resize; transition: background 0.15s; }
.resize-handle:hover, .resize-handle.dragging { background: #FFD700; }
#left-panel h3 { color: #888; font-size: 11px; text-transform: uppercase; margin: 8px 0 4px 0; letter-spacing: 1px; }
.select-files-header { display: flex; align-items: center; justify-content: space-between; cursor: pointer; padding: 4px 2px; margin-bottom: 4px; border-bottom: 1px solid #2a2a3a; }
.select-files-header span.sf-title { font-size: 13px; font-weight: 700; color: #ccc; }
.select-files-header span.sf-arrow { font-size: 14px; color: #888; transition: transform 0.2s; }
.select-files-header span.sf-arrow.collapsed { transform: rotate(-90deg); }
#filter-body.collapsed { display: none; }
#left-panel hr { border: none; border-top: 1px solid #2a2a3a; margin: 8px 0; }
.filter-item { display: flex; align-items: center; gap: 6px; padding: 2px 0; cursor: pointer; }
.filter-item input[type="checkbox"] { cursor: pointer; }
.filter-dot { width: 10px; height: 10px; border-radius: 50%; display: inline-block; flex-shrink: 0; }
.filter-label { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
#left-page-viewer { margin-top: 12px; border-top: 1px solid #2a2a3a; padding-top: 8px; display: none; }
#left-page-viewer .page-content { max-height: calc(100vh - 200px); overflow-y: auto; font-size: 11px; line-height: 1.5; }
#left-page-viewer .page-title { font-weight: 700; color: #FFD700; font-size: 13px; margin-bottom: 4px; }
#left-page-viewer .page-path { font-size: 10px; color: #666; margin-bottom: 8px; }
#left-page-viewer .dismiss-btn { background: none; border: none; color: #888; cursor: pointer; float: right; font-size: 14px; }

/* GRAPH AREA */
#graph-container { flex: 1; position: relative; overflow: hidden; }
#graph-container svg { width: 100%; height: 100%; }

/* RIGHT PANEL */
#right-panel { width: 300px; flex-shrink: 0; background: #0e0e16; border-left: 1px solid #2a2a3a; overflow-y: auto; padding: 12px; display: none; }
#right-panel .page-title { font-weight: 700; color: #FFD700; font-size: 15px; margin-bottom: 4px; }
#right-panel .page-path { font-size: 11px; color: #666; margin-bottom: 12px; }
#right-panel .page-content { font-size: 13px; line-height: 1.6; }
#right-panel .page-content h1 { font-size: 18px; color: #FFD700; margin: 12px 0 6px; }
#right-panel .page-content h2 { font-size: 16px; color: #ddd; margin: 10px 0 4px; }
#right-panel .page-content h3 { font-size: 14px; color: #ccc; margin: 8px 0 4px; }
#right-panel .page-content strong { color: #fff; }
#right-panel .page-content em { color: #aaa; font-style: italic; }
#right-panel .page-content code { background: #1a1a2a; padding: 1px 4px; border-radius: 3px; font-family: monospace; font-size: 12px; }
#right-panel .page-content pre { background: #1a1a2a; padding: 8px; border-radius: 4px; overflow-x: auto; margin: 8px 0; }
#right-panel .page-content pre code { padding: 0; background: none; }
#right-panel .page-content ul { padding-left: 16px; margin: 4px 0; }
#right-panel .page-content li { margin: 2px 0; }
#right-panel .page-content p { margin: 6px 0; }
#right-panel .page-content .wikilink { color: #4A90D9; cursor: pointer; text-decoration: underline; }
#right-panel .page-content .wikilink:hover { color: #6ab0f9; }
#right-panel .dismiss-btn { background: none; border: 1px solid #3a3a4a; color: #e0e0e0; cursor: pointer; font-size: 14px; float: right; padding: 2px 8px; border-radius: 4px; }
#right-panel .dismiss-btn:hover { background: #2a2a3a; }

/* TOOLTIP */
#tooltip { position: absolute; background: rgba(20,20,35,0.95); border: 1px solid #3a3a4a; border-radius: 6px; padding: 8px 12px; font-size: 12px; pointer-events: auto; z-index: 100; display: none; max-width: 250px; }
#tooltip .tt-title { font-weight: 700; color: #FFD700; cursor: pointer; text-decoration: underline; }
#tooltip .tt-dir { color: #888; font-size: 11px; }
#tooltip .tt-date { color: #666; font-size: 11px; }

/* FOOTER */
#footer-resize { height: 5px; flex-shrink: 0; background: #2a2a3a; cursor: row-resize; transition: background 0.15s; }
#footer-resize:hover, #footer-resize.dragging { background: #FFD700; }
/* Footer height: default 120 px (was 80) so the deep narration tracks have real
   reading room out of the box. User can drag the resize handle (#footer-resize)
   anywhere from 60 px up to 60 % of viewport height. A window-resize listener
   re-clamps if the window shrinks below the dragged height. */
#footer { display: flex; align-items: flex-start; gap: 12px; padding: 8px 16px; background: #111118; border-top: 1px solid #2a2a3a; min-height: 60px; height: 120px; flex-shrink: 0; overflow: hidden; }
#timeline-slider { flex: 0 0 200px; margin-top: 4px; }
#narration-text { flex: 1; font-size: 12px; color: #ccc; overflow-y: auto; padding: 4px 8px; background: #0e0e16; border-radius: 4px; line-height: 1.4; height: 100%; }
#footer .footer-controls { display: flex; gap: 6px; align-items: center; flex-shrink: 0; }
#footer .footer-controls button { background: #1a1a2a; border: 1px solid #3a3a4a; color: #e0e0e0; padding: 4px 8px; border-radius: 4px; cursor: pointer; font-size: 12px; }
#footer .footer-controls button:hover { background: #2a2a3a; }
#footer .footer-controls button.active { background: #FFD700; color: #0a0a0f; }
#footer .footer-controls select { background: #1a1a2a; border: 1px solid #3a3a4a; color: #e0e0e0; padding: 2px 4px; border-radius: 4px; font-size: 12px; }

/* SETTINGS MODAL */
#settings-modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.7); z-index: 1000; justify-content: center; align-items: center; }
#settings-modal.visible { display: flex; }
#settings-content { background: #15151f; border: 1px solid #3a3a4a; border-radius: 8px; padding: 24px; width: 400px; max-width: 90%; }
#settings-content h2 { color: #FFD700; margin-bottom: 16px; font-size: 18px; }
#settings-content label { display: block; font-size: 13px; margin: 8px 0 4px; color: #ccc; }
#settings-content select, #settings-content input[type="text"], #settings-content input[type="password"] { width: 100%; padding: 6px 8px; background: #1a1a2a; border: 1px solid #3a3a4a; color: #e0e0e0; border-radius: 4px; font-size: 13px; margin-bottom: 8px; }
#settings-content .btn-row { display: flex; gap: 8px; margin-top: 16px; }
#settings-content button { background: #1a1a2a; border: 1px solid #3a3a4a; color: #e0e0e0; padding: 6px 16px; border-radius: 4px; cursor: pointer; font-size: 13px; }
#settings-content button:hover { background: #2a2a3a; }
#settings-content button.primary { background: #FFD700; color: #0a0a0f; border-color: #FFD700; }
.error-text { color: #FF4444; font-size: 12px; margin-top: 4px; }
</style>
</head>
<body>
<div id="app">
  <!-- HEADER -->
  <div id="header">
    <div class="title">C2A2 Wiki Narration</div>
    <div class="stats">
      <span>""" + str(total_files) + """ files</span>
      <span>""" + str(num_findings) + """ findings</span>
      <span>""" + str(num_decisions) + """ decisions</span>
    </div>
    <div class="controls">
      <label style="font-size:11px;display:flex;align-items:center;gap:4px;cursor:pointer;"><input type="checkbox" id="chk-hold-forces" onchange="toggleHoldForces(this.checked)"> Hold</label>
      <label style="font-size:11px;display:flex;align-items:center;gap:4px;cursor:pointer;"><input type="checkbox" id="chk-hover-names" onchange="toggleHoverNames(this.checked)"> Names</label>
      <button id="btn-fit-all" onclick="fitAll()" style="font-size:11px;">Fit All</button>
      <span style="width:1px;height:20px;background:#3a3a4a;"></span>
      <label style="font-size:11px;display:flex;align-items:center;gap:4px;cursor:pointer;" title="Free: positions are emergent, no encoded meaning. Discipline×Year: X = thinker's discipline, Y = file date — spatial position carries readable meaning.">Mode:
        <select id="layout-mode" onchange="setLayoutMode(this.value)" style="font-size:11px;background:#1a1a2a;color:#e0e0e0;border:1px solid #3a3a4a;border-radius:3px;padding:1px 3px;">
          <option value="free" selected>Free</option>
          <option value="discipline-year">Discipline × Year</option>
        </select>
      </label>
      <span style="width:1px;height:20px;background:#3a3a4a;"></span>
      <button id="btn-history" onclick="startTour('history')">History</button>
      <button id="btn-recent" onclick="startTour('recent')">Recent</button>
      <button id="btn-latest" onclick="startTour('latest')">Latest</button>
      <div class="brightness-control">
        <label>Brightness</label>
        <input type="range" id="brightness-slider" min="0.1" max="2" step="0.05" value="1" oninput="setBrightness(this.value)">
      </div>
      <button id="btn-settings" onclick="openSettings()">&#9881;</button>
    </div>
  </div>

  <!-- MAIN -->
  <div id="main">
    <!-- LEFT PANEL -->
    <div id="left-panel">
      <div class="select-files-header" onclick="toggleFilterPanel()">
        <span class="sf-title">Select Files</span>
        <span class="sf-arrow" id="sf-arrow">&#9660;</span>
      </div>
      <div id="filter-body">
        <div class="filter-item"><input type="checkbox" id="chk-all" checked onchange="toggleAll(this.checked)"><label for="chk-all" class="filter-label">All</label></div>
        <div class="filter-item"><input type="checkbox" id="chk-none" onchange="toggleNone(this.checked)"><label for="chk-none" class="filter-label">None</label></div>
        <hr>
        <h3><input type="checkbox" id="chk-all-traditions" checked onchange="toggleSection('traditions', this.checked)" style="margin-right:4px;cursor:pointer;"> Traditions</h3>
        <div id="tradition-filters"></div>
        <hr>
        <h3><input type="checkbox" id="chk-all-structure" checked onchange="toggleSection('structure', this.checked)" style="margin-right:4px;cursor:pointer;"> Structure</h3>
        <div id="structure-filters"></div>
        <hr>
        <h3><input type="checkbox" id="chk-all-edges" checked onchange="toggleAllEdges(this.checked)" style="margin-right:4px;cursor:pointer;"> Edges</h3>
        <div style="font-size:10px;color:#888;margin:2px 0 2px 4px;">By type — color</div>
        <div class="filter-item"><input type="checkbox" id="chk-edge-wikilink" checked onchange="toggleEdgeType('wikilink', this.checked)"><span class="filter-dot" style="background:#C9A84C"></span><span class="filter-label">Wikilink</span></div>
        <div class="filter-item"><input type="checkbox" id="chk-edge-mention" checked onchange="toggleEdgeType('mention', this.checked)"><span class="filter-dot" style="background:#5B9A8B"></span><span class="filter-label">Mention</span></div>
        <div class="filter-item"><input type="checkbox" id="chk-edge-reference" checked onchange="toggleEdgeType('reference', this.checked)"><span class="filter-dot" style="background:#5A6878"></span><span class="filter-label">Reference</span></div>
        <div style="font-size:10px;color:#888;margin:6px 0 2px 4px;">By bridge — line style</div>
        <div class="filter-item"><input type="checkbox" id="chk-edge-cross" checked onchange="toggleEdgeBridge('cross', this.checked)"><span class="filter-label">Crosses categories <span style="color:#888;font-size:10px">(solid)</span></span></div>
        <div class="filter-item"><input type="checkbox" id="chk-edge-same" checked onchange="toggleEdgeBridge('same', this.checked)"><span class="filter-label">Within category <span style="color:#888;font-size:10px">(dashed)</span></span></div>
      </div>
      <div id="left-page-viewer">
        <button class="dismiss-btn" onclick="dismissLeftPage()">&times;</button>
        <div class="page-title" id="left-page-title"></div>
        <div class="page-path" id="left-page-path"></div>
        <div class="page-content" id="left-page-content"></div>
      </div>
    </div>

    <!-- LEFT RESIZE HANDLE -->
    <div class="resize-handle" id="left-resize" onmousedown="startResize(event, 'left')"></div>

    <!-- GRAPH -->
    <div id="graph-container">
      <svg id="graph-svg"></svg>
      <div id="tooltip"></div>
      <div id="limit-warning" style="display:none;position:absolute;bottom:8px;left:50%;transform:translateX(-50%);background:#8B4513;color:#fff;padding:6px 16px;border-radius:6px;font-size:12px;z-index:20;white-space:nowrap;"></div>
      <div id="graph-status" style="position:absolute;bottom:8px;left:8px;font-size:11px;color:#666;z-index:10;"></div>
      <div id="edge-legend" style="position:absolute;top:8px;right:8px;background:rgba(20,20,30,0.85);border:1px solid #2a2a3e;border-radius:5px;padding:6px 10px;font-size:10px;color:#ccc;line-height:1.6;z-index:15;pointer-events:none;">
        <div style="font-weight:600;color:#888;text-transform:uppercase;letter-spacing:0.5px;font-size:9px;margin-bottom:3px;">Edges</div>
        <div><span style="display:inline-block;width:18px;height:2px;background:#C9A84C;vertical-align:middle;margin-right:4px;"></span>Wikilink</div>
        <div><span style="display:inline-block;width:18px;height:2px;background:#5B9A8B;vertical-align:middle;margin-right:4px;"></span>Mention</div>
        <div><span style="display:inline-block;width:18px;height:2px;background:#5A6878;vertical-align:middle;margin-right:4px;"></span>Reference</div>
        <div style="border-top:1px solid #2a2a3e;margin:4px 0 3px;"></div>
        <div><span style="display:inline-block;width:18px;height:0;border-top:1.5px solid #aaa;vertical-align:middle;margin-right:4px;"></span>Crosses category</div>
        <div><span style="display:inline-block;width:18px;height:0;border-top:1.5px dashed #aaa;vertical-align:middle;margin-right:4px;"></span>Within category</div>
      </div>
    </div>

    <!-- RIGHT RESIZE HANDLE -->
    <div class="resize-handle" id="right-resize" style="display:none;" onmousedown="startResize(event, 'right')"></div>

    <!-- RIGHT PANEL -->
    <div id="right-panel">
      <button class="dismiss-btn" onclick="dismissRightPanel()">&times;</button>
      <div class="page-title" id="right-page-title"></div>
      <div class="page-path" id="right-page-path"></div>
      <div class="page-content" id="right-page-content"></div>
    </div>
  </div>

  <!-- FOOTER RESIZE HANDLE -->
  <div id="footer-resize" onmousedown="startFooterResize(event)"></div>
  <!-- FOOTER -->
  <div id="footer">
    <input type="range" id="timeline-slider" min="0" max="0" value="0" oninput="onTimelineSlide(this.value)">
    <div style="flex:1;display:flex;flex-direction:column;gap:4px;min-width:0;height:100%;">
      <div id="narration-text">Ready. Check groups in Select Files to explore.</div>
      <div style="display:flex;gap:4px;">
        <input type="text" id="search-input" placeholder="Search files, findings, connections..." style="flex:1;background:#1a1a2a;border:1px solid #3a3a4a;color:#e0e0e0;padding:3px 8px;border-radius:4px;font-size:12px;" onkeydown="if(event.key==='Enter')runSearch()">
        <button onclick="runSearch()" style="background:#1a1a2a;border:1px solid #3a3a4a;color:#e0e0e0;padding:3px 8px;border-radius:4px;cursor:pointer;font-size:11px;">Search</button>
        <button onclick="document.getElementById('search-input').value='';runSearch();" style="background:#1a1a2a;border:1px solid #3a3a4a;color:#e0e0e0;padding:3px 8px;border-radius:4px;cursor:pointer;font-size:11px;">Clear</button>
      </div>
    </div>
    <div class="footer-controls">
      <button id="btn-play" onclick="togglePlay()">Play</button>
      <button id="btn-reset" onclick="resetTour()">Reset</button>
      <select id="speed-select" onchange="setSpeed(this.value)">
        <option value="0.5">0.5x</option>
        <option value="1" selected>1x</option>
        <option value="1.5">1.5x</option>
        <option value="2">2x</option>
      </select>
      <button id="btn-mute" onclick="toggleMute()">&#128266;</button>
      <button id="btn-depth" onclick="toggleDepth()">Brief</button>
    </div>
  </div>
</div>

<!-- SETTINGS MODAL -->
<div id="settings-modal">
  <div id="settings-content">
    <h2>TTS Settings</h2>
    <label>Provider</label>
    <select id="tts-provider" onchange="applyFormToTTS()">
      <option value="browser">Browser (Web Speech API)</option>
      <option value="openai">OpenAI API</option>
    </select>
    <label>API Key (OpenAI)</label>
    <input type="password" id="tts-api-key" placeholder="sk-..." onchange="applyFormToTTS()">
    <label>Browser Voice</label>
    <select id="tts-browser-voice" onchange="applyFormToTTS()"></select>
    <label>OpenAI Voice</label>
    <select id="tts-openai-voice" onchange="applyFormToTTS()">
      <option value="alloy">Alloy</option>
      <option value="echo">Echo</option>
      <option value="fable">Fable</option>
      <option value="onyx">Onyx</option>
      <option value="nova">Nova</option>
      <option value="shimmer">Shimmer</option>
    </select>
    <div id="tts-error" class="error-text"></div>
    <div class="btn-row">
      <button class="primary" onclick="saveSettings()">Save</button>
      <button onclick="testTTS()">Test</button>
      <button onclick="closeSettings()">Cancel</button>
    </div>
  </div>
</div>

<script>
// ── DATA CONSTANTS ──
const NODES = """ + nodes_json + """;
const LINKS = """ + links_json + """;
const FINDINGS = """ + findings_json + """;
const DECISIONS = """ + decisions_json + """;
const CROSS_CONNECTIONS = """ + cross_json + """;
const CHANGELOGS = """ + changelogs_json + """;
const COWORK_SUMMARIES = """ + cowork_json + """;
const TIMELINE = """ + timeline_json + """;
const COLORS = """ + colors_json + """;
const TRADITION_GROUPS = """ + tradition_groups_json + """;
const STRUCTURE_GROUPS = """ + structure_groups_json + """;
var DATE_START = '""" + date_start + """';
var DATE_END = '""" + date_end + """';

// ── STATE ──
var showHoverNames = false;
var holdForces = false;
var edgesVisible = true;
var groupVisibility = {};
var currentTrack = null;
var currentSegmentIndex = 0;
var isPlaying = false;
var playTimer = null;
var playSpeed = 1;
var isMuted = false;
var isDeep = false;
var brightness = 1;
var narrationTracks = {};
var simulation = null;
var zoomBehavior = null;
var nodeById = {};
// (Sociogram-level Record button removed — recording lives at the explorer level now.)

// ── EDGE COLOR KEY (B-with-twist) ──
// type → color, bridge → line style. Both dimensions cut by checkbox AND-composed.
var EDGE_COLOR = {
  wikilink:  '#C9A84C',  // gold — explicit editorial intent
  mention:   '#5B9A8B',  // sage — narrative bridge (architecture prose names a thinker)
  reference: '#5A6878',  // slate — co-citation of a shared ID (DECISION-NNN, FINDING-NNN, …)
};
var showEdgeType   = { wikilink: true, mention: true, reference: true };
var showEdgeBridge = { cross: true, same: true };

// ── LAYOUT MODE (force semantics) ──
// 'free' = pure d3 force layout (positions are emergent, no encoded meaning).
// 'discipline-year' = gentle forceX/forceY pulling each node toward
//     X = its discipline angle, Y = its date. Spatial position becomes
//     readable: same horizontal band → same discipline; same vertical
//     band → same era.
var layoutMode = 'free';

// Mirror the THINKER_DISC table from prs_3d.html so the Sociogram can compute
// X-targets for tradition files. Update both tables together when adding a tradition.
var THINKER_DISC = {
  levin:        'Developmental Biology',
  friston:      'Computational Neuroscience',
  hoffman:      'Cognitive Science',
  kastrup:      'Philosophy of Mind',
  mcgilchrist:  'Neuropsychiatry',
  hawkins:      'Computational Neuroscience',
  wolfram:      'Mathematical Physics',
  carroll:      'Theoretical Physics',
  arkanihamed:  'Theoretical Physics',
  fredrickson:  'Positive Psychology',
  stump:        'Analytic Theology',
  rohr:         'Contemplative Theology',
  wright:       'Historical Theology',
  macintyre:    'Moral Philosophy',
  loughran:     'Systems Integration',
};
var DISCIPLINES = [
  'Analytic Theology', 'Cognitive Science', 'Computational Neuroscience',
  'Contemplative Theology', 'Developmental Biology', 'Historical Theology',
  'Mathematical Physics', 'Moral Philosophy', 'Neuropsychiatry',
  'Philosophy of Mind', 'Positive Psychology', 'Systems Integration',
  'Theoretical Physics',
];

// ── MARKDOWN RENDERER ──
function renderMarkdown(md) {
  if (!md) return '<p><em>No content</em></p>';
  var lines = md.split('\\n');
  var html = '';
  var inCodeBlock = false;
  var codeContent = '';
  var inList = false;
  for (var i = 0; i < lines.length; i++) {
    var line = lines[i];
    if (line.match(/^```/)) {
      if (inCodeBlock) {
        html += '<pre><code>' + escapeHtml(codeContent) + '</code></pre>';
        codeContent = '';
        inCodeBlock = false;
      } else {
        if (inList) { html += '</ul>'; inList = false; }
        inCodeBlock = true;
      }
      continue;
    }
    if (inCodeBlock) {
      codeContent += line + '\\n';
      continue;
    }
    if (line.match(/^### /)) {
      if (inList) { html += '</ul>'; inList = false; }
      html += '<h3>' + inlineFormat(line.slice(4)) + '</h3>';
    } else if (line.match(/^## /)) {
      if (inList) { html += '</ul>'; inList = false; }
      html += '<h2>' + inlineFormat(line.slice(3)) + '</h2>';
    } else if (line.match(/^# /)) {
      if (inList) { html += '</ul>'; inList = false; }
      html += '<h1>' + inlineFormat(line.slice(2)) + '</h1>';
    } else if (line.match(/^- /)) {
      if (!inList) { html += '<ul>'; inList = true; }
      html += '<li>' + inlineFormat(line.slice(2)) + '</li>';
    } else if (line.trim() === '') {
      if (inList) { html += '</ul>'; inList = false; }
      html += '<br>';
    } else {
      if (inList) { html += '</ul>'; inList = false; }
      html += '<p>' + inlineFormat(line) + '</p>';
    }
  }
  if (inList) html += '</ul>';
  if (inCodeBlock) html += '<pre><code>' + escapeHtml(codeContent) + '</code></pre>';
  return html;
}

function escapeHtml(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function inlineFormat(text) {
  text = escapeHtml(text);
  text = text.replace(/\\[\\[([^\\]]+)\\]\\]/g, '<span class="wikilink" onclick="openNodeByLabel(this.textContent)">$1</span>');
  text = text.replace(/`([^`]+)`/g, '<code>$1</code>');
  text = text.replace(/\\*\\*([^*]+)\\*\\*/g, '<strong>$1</strong>');
  text = text.replace(/\\*([^*]+)\\*/g, '<em>$1</em>');
  return text;
}

// ── RENDERING LIMITS ──
var MAX_NODES = 2000;
var MAX_EDGES = 3000;
var WARN_NODES = 1600;
var WARN_EDGES = 2500;

function showLimitWarning(msg) {
  var el = document.getElementById('limit-warning');
  el.textContent = msg;
  el.style.display = 'block';
  setTimeout(function() { el.style.display = 'none'; }, 5000);
}

// ── FILTER PANEL ──
var DEFAULT_ON = null; // null = all on
// Groups to default OFF and exclude from "All". Changelog is intentionally
// withheld from the Sociogram by default (12 noisy daily-change files would
// dominate the cluster otherwise).
var EXCLUDED_FROM_ALL = {'architecture/changelog': true};

function buildFilters() {
  var tradDiv = document.getElementById('tradition-filters');
  TRADITION_GROUPS.forEach(function(g) {
    var startOn = !EXCLUDED_FROM_ALL[g.key];
    groupVisibility[g.key] = startOn;
    tradDiv.innerHTML += '<div class="filter-item"><input type="checkbox" ' + (startOn ? 'checked' : '') + ' data-group="' + g.key + '" onchange="toggleGroup(\\'' + g.key + '\\', this.checked)"><span class="filter-dot" style="background:' + g.color + '"></span><span class="filter-label">' + g.label + '</span></div>';
  });
  var structDiv = document.getElementById('structure-filters');
  STRUCTURE_GROUPS.forEach(function(g) {
    var startOn = !EXCLUDED_FROM_ALL[g.key];
    groupVisibility[g.key] = startOn;
    structDiv.innerHTML += '<div class="filter-item"><input type="checkbox" ' + (startOn ? 'checked' : '') + ' data-group="' + g.key + '" onchange="toggleGroup(\\'' + g.key + '\\', this.checked)"><span class="filter-dot" style="background:' + g.color + '"></span><span class="filter-label">' + g.label + '</span></div>';
  });
}

function toggleGroup(key, checked) {
  if (checked) {
    var currentVisible = NODES.filter(function(n) { return groupVisibility[n.group]; }).length;
    var adding = NODES.filter(function(n) { return n.group === key; }).length;
    if (currentVisible + adding > MAX_NODES) {
      showLimitWarning('Cannot add ' + adding + ' nodes: would exceed limit of ' + MAX_NODES + '. Uncheck other groups first.');
      var cb = document.querySelector('[data-group="' + key + '"]');
      if (cb) cb.checked = false;
      return;
    }
    if (currentVisible + adding > WARN_NODES) {
      showLimitWarning('Approaching node limit: ' + (currentVisible + adding) + '/' + MAX_NODES);
    }
  }
  groupVisibility[key] = checked;
  syncSectionCheckboxes();
  rebuildGraph();
}

// Symmetric: every master checkbox responds to both check AND uncheck.
function toggleAll(checked) {
  document.getElementById('chk-none').checked = false;
  var boxes = document.querySelectorAll('[data-group]');
  if (!checked) {
    boxes.forEach(function(b) {
      b.checked = false;
      groupVisibility[b.dataset.group] = false;
    });
    syncSectionCheckboxes();
    rebuildGraph();
    return;
  }
  var nodeCount = 0;
  boxes.forEach(function(b) {
    var key = b.dataset.group;
    if (EXCLUDED_FROM_ALL[key]) {
      b.checked = false;
      groupVisibility[key] = false;
      return;
    }
    var groupNodes = NODES.filter(function(n) { return n.group === key; }).length;
    if (nodeCount + groupNodes <= MAX_NODES) {
      b.checked = true;
      groupVisibility[key] = true;
      nodeCount += groupNodes;
    } else {
      b.checked = false;
      groupVisibility[key] = false;
    }
  });
  if (nodeCount >= MAX_NODES) {
    showLimitWarning('Node limit reached (' + MAX_NODES + '). Some groups left unchecked for performance.');
  }
  syncSectionCheckboxes();
  rebuildGraph();
}

function syncSectionCheckboxes() {
  var tradBoxes = document.getElementById('tradition-filters').querySelectorAll('[data-group]');
  var allTradChecked = tradBoxes.length > 0;
  tradBoxes.forEach(function(b) { if (!b.checked) allTradChecked = false; });
  var trMaster = document.getElementById('chk-all-traditions');
  if (trMaster) trMaster.checked = allTradChecked;
  // Structure: ignore EXCLUDED_FROM_ALL (changelog) when judging "all checked"
  var structBoxes = document.getElementById('structure-filters').querySelectorAll('[data-group]');
  var allStructChecked = structBoxes.length > 0;
  structBoxes.forEach(function(b) {
    if (EXCLUDED_FROM_ALL[b.dataset.group]) return;
    if (!b.checked) allStructChecked = false;
  });
  var stMaster = document.getElementById('chk-all-structure');
  if (stMaster) stMaster.checked = allStructChecked;
  // All / None master state — ignore EXCLUDED_FROM_ALL
  var allBoxes = document.querySelectorAll('[data-group]');
  var allChecked = allBoxes.length > 0;
  var anyChecked = false;
  allBoxes.forEach(function(b) {
    if (EXCLUDED_FROM_ALL[b.dataset.group]) return;
    if (!b.checked) allChecked = false;
    if (b.checked) anyChecked = true;
  });
  var allCb = document.getElementById('chk-all');
  if (allCb) allCb.checked = allChecked;
  var noneCb = document.getElementById('chk-none');
  if (noneCb) noneCb.checked = !anyChecked;
}

function toggleNone(checked) {
  if (typeof checked === 'undefined') checked = document.getElementById('chk-none').checked;
  if (checked) {
    document.getElementById('chk-all').checked = false;
    var boxes = document.querySelectorAll('[data-group]');
    boxes.forEach(function(b) { b.checked = false; groupVisibility[b.dataset.group] = false; });
    var trM = document.getElementById('chk-all-traditions');
    if (trM) trM.checked = false;
    var stM = document.getElementById('chk-all-structure');
    if (stM) stM.checked = false;
    rebuildGraph();
  } else {
    toggleAll(true);
  }
}

function toggleSection(section, checked) {
  var isTraditions = (section === 'traditions');
  var container = document.getElementById(isTraditions ? 'tradition-filters' : 'structure-filters');
  var boxes = container.querySelectorAll('[data-group]');
  if (checked) {
    var nodeCount = NODES.filter(function(n) { return groupVisibility[n.group]; }).length;
    var adding = 0;
    boxes.forEach(function(b) {
      if (EXCLUDED_FROM_ALL[b.dataset.group]) return;
      if (!b.checked) {
        adding += NODES.filter(function(n) { return n.group === b.dataset.group; }).length;
      }
    });
    if (nodeCount + adding > MAX_NODES) {
      showLimitWarning('Cannot add entire section: would exceed limit of ' + MAX_NODES + '. Uncheck other groups first.');
      var sectionCheckbox = document.getElementById(isTraditions ? 'chk-all-traditions' : 'chk-all-structure');
      sectionCheckbox.checked = false;
      return;
    }
  }
  boxes.forEach(function(b) {
    if (checked && EXCLUDED_FROM_ALL[b.dataset.group]) return;
    b.checked = checked;
    groupVisibility[b.dataset.group] = checked;
  });
  syncSectionCheckboxes();
  rebuildGraph();
}

// ── EDGE FILTER HANDLERS (B-with-twist) ──
function toggleAllEdges(checked) {
  edgesVisible = checked;
  ['wikilink','mention','reference'].forEach(function(t) {
    showEdgeType[t] = checked;
    var cb = document.getElementById('chk-edge-' + t);
    if (cb) cb.checked = checked;
  });
  ['cross','same'].forEach(function(b) {
    showEdgeBridge[b] = checked;
    var cb = document.getElementById('chk-edge-' + b);
    if (cb) cb.checked = checked;
  });
  applyEdgeFilters();
}
function toggleEdgeType(t, checked) {
  showEdgeType[t] = checked;
  syncEdgesMaster();
  applyEdgeFilters();
}
function toggleEdgeBridge(b, checked) {
  showEdgeBridge[b] = checked;
  syncEdgesMaster();
  applyEdgeFilters();
}
function syncEdgesMaster() {
  var allOn =
    showEdgeType.wikilink && showEdgeType.mention && showEdgeType.reference &&
    showEdgeBridge.cross && showEdgeBridge.same;
  edgesVisible = allOn;
  var m = document.getElementById('chk-all-edges');
  if (m) m.checked = allOn;
}
function applyEdgeFilters() {
  d3.selectAll('.link-line')
    .attr('display', function(d) {
      var t = d.type || 'reference';
      var b = d.bridge || 'cross';
      var on = (showEdgeType[t] !== false) && (showEdgeBridge[b] !== false);
      return on ? null : 'none';
    });
}

// ── GRAPH CONTROLS ──
function toggleHoldForces(checked) {
  holdForces = checked;
  if (simulation) {
    if (checked) simulation.stop();
    else simulation.alpha(0.3).restart();
  }
}

function toggleHoverNames(checked) {
  showHoverNames = checked;
  if (!checked) hideTooltip();
}

function fitAll() {
  if (!zoomBehavior) return;
  var svgEl = document.getElementById('graph-svg');
  if (!svgEl) return;
  var w = svgEl.clientWidth, h = svgEl.clientHeight;
  if (w === 0 || h === 0) return;
  var xMin = Infinity, xMax = -Infinity, yMin = Infinity, yMax = -Infinity;
  // Only consider visible nodes
  NODES.forEach(function(n) {
    if (groupVisibility[n.group] && n.x !== undefined) {
      if (n.x < xMin) xMin = n.x;
      if (n.x > xMax) xMax = n.x;
      if (n.y < yMin) yMin = n.y;
      if (n.y > yMax) yMax = n.y;
    }
  });
  if (xMin === Infinity) return;
  var dx = xMax - xMin + 40, dy = yMax - yMin + 40;
  var scale = Math.min(w / dx, h / dy, 2) * 0.9;
  var cx = (xMin + xMax) / 2, cy = (yMin + yMax) / 2;
  var transform = d3.zoomIdentity.translate(w / 2 - cx * scale, h / 2 - cy * scale).scale(scale);
  d3.select('#graph-svg').transition().duration(750).call(zoomBehavior.transform, transform);
}

// ── LAYOUT MODE (force semantics) ──
function setLayoutMode(value) {
  layoutMode = (value === 'discipline-year') ? 'discipline-year' : 'free';
  if (simulation) {
    if (layoutMode === 'discipline-year') {
      var container = document.getElementById('graph-container');
      var w = container.clientWidth, h = container.clientHeight;
      simulation
        .force('encx', d3.forceX(function(d) { return targetX(d, w); }).strength(0.06))
        .force('ency', d3.forceY(function(d) { return targetY(d, h); }).strength(0.06));
    } else {
      simulation.force('encx', null).force('ency', null);
    }
    simulation.alpha(0.6).restart();
    setTimeout(fitAll, 1500);
  }
}
function _disciplineForNode(d) {
  var g = d.group || '';
  if (g.indexOf('traditions/') === 0) {
    var lastname = g.substring('traditions/'.length);
    return THINKER_DISC[lastname] || null;
  }
  return null;
}
function targetX(d, width) {
  var disc = _disciplineForNode(d);
  if (!disc) return width / 2;
  var idx = DISCIPLINES.indexOf(disc);
  if (idx < 0) return width / 2;
  var n = DISCIPLINES.length;
  var margin = 60;
  return margin + (idx + 0.5) * ((width - 2 * margin) / n);
}
var _dateBounds = null;
function _ensureDateBounds() {
  if (_dateBounds) return _dateBounds;
  var minD = Infinity, maxD = -Infinity;
  NODES.forEach(function(n) {
    var t = _dateToTime(n.date);
    if (t == null) return;
    if (t < minD) minD = t;
    if (t > maxD) maxD = t;
  });
  if (!isFinite(minD)) { minD = 0; maxD = 1; }
  _dateBounds = { min: minD, max: maxD };
  return _dateBounds;
}
function _dateToTime(s) {
  if (!s) return null;
  var m = String(s).match(/^(\\d{4})-(\\d{2})-(\\d{2})/);
  if (!m) return null;
  return Date.UTC(+m[1], +m[2] - 1, +m[3]);
}
function targetY(d, height) {
  var t = _dateToTime(d.date);
  if (t == null) return height / 2;
  var b = _ensureDateBounds();
  if (b.max === b.min) return height / 2;
  var frac = (t - b.min) / (b.max - b.min);
  var margin = 50;
  return margin + frac * (height - 2 * margin);
}

// ── BRIGHTNESS ──
function setBrightness(val) {
  brightness = parseFloat(val);
  d3.selectAll('.node-circle').attr('opacity', Math.min(brightness, 1));
  d3.selectAll('.link-line').attr('opacity', Math.min(0.5 * brightness, 1));
}

// ── NODE/EDGE CLICK ──
function openNodeByLabel(label) {
  var node = NODES.find(function(n) {
    return n.label === label || n.id.indexOf(label) !== -1;
  });
  if (node) showRightPanel(node);
}

function showRightPanel(node) {
  var panel = document.getElementById('right-panel');
  document.getElementById('right-page-title').textContent = node.label || node.id;
  document.getElementById('right-page-path').textContent = node.id;
  document.getElementById('right-page-content').innerHTML = renderMarkdown(node.content || '');
  panel.style.display = 'block';
  document.getElementById('right-resize').style.display = 'block';
}

function dismissRightPanel() {
  document.getElementById('right-panel').style.display = 'none';
  document.getElementById('right-resize').style.display = 'none';
}

function showLeftPage(node) {
  var viewer = document.getElementById('left-page-viewer');
  document.getElementById('left-page-title').textContent = node.label || node.id;
  document.getElementById('left-page-path').textContent = node.id;
  document.getElementById('left-page-content').innerHTML = renderMarkdown(node.content || '');
  viewer.style.display = 'block';
}

function dismissLeftPage() {
  document.getElementById('left-page-viewer').style.display = 'none';
}

function toggleFilterPanel() {
  var body = document.getElementById('filter-body');
  var arrow = document.getElementById('sf-arrow');
  body.classList.toggle('collapsed');
  arrow.classList.toggle('collapsed');
}

// ── TOOLTIP ──
function showTooltip(evt, content) {
  if (!showHoverNames) return;
  var tt = document.getElementById('tooltip');
  tt.innerHTML = content;
  tt.style.display = 'block';
  var x = evt.pageX + 12;
  var y = evt.pageY + 12;
  if (x + 250 > window.innerWidth) x = evt.pageX - 260;
  if (y + 100 > window.innerHeight) y = evt.pageY - 110;
  tt.style.left = x + 'px';
  tt.style.top = y + 'px';
}

function hideTooltip() {
  document.getElementById('tooltip').style.display = 'none';
}

// ── GRAPH ──
var graphG = null;
var linkG = null;
var nodeG = null;

function initGraph() {
  var container = document.getElementById('graph-container');
  var width = container.clientWidth;
  var height = container.clientHeight;
  var svg = d3.select('#graph-svg');

  graphG = svg.append('g');

  zoomBehavior = d3.zoom().scaleExtent([0.05, 8]).on('zoom', function(event) {
    graphG.attr('transform', event.transform);
  });
  svg.call(zoomBehavior);

  // Build node lookup
  NODES.forEach(function(n) { nodeById[n.id] = n; });

  linkG = graphG.append('g').attr('class', 'links');
  nodeG = graphG.append('g').attr('class', 'nodes');

  // Pre-seed ALL positions by group so they're stable across rebuilds
  var groupCenters = {};
  var gIdx = 0;
  var cols = Math.ceil(Math.sqrt(Object.keys(COLORS).length));
  Object.keys(COLORS).forEach(function(key) {
    var row = Math.floor(gIdx / cols), col = gIdx % cols;
    groupCenters[key] = {x: width * 0.2 + (col / cols) * width * 0.6, y: height * 0.2 + (row / cols) * height * 0.6};
    gIdx++;
  });
  NODES.forEach(function(n) {
    if (n.x === undefined) {
      var gc = groupCenters[n.group] || {x: width / 2, y: height / 2};
      n.x = gc.x + (Math.random() - 0.5) * 100;
      n.y = gc.y + (Math.random() - 0.5) * 100;
    }
  });

  rebuildGraph();
}

function rebuildGraph() {
  if (!linkG || !nodeG) return;
  // Stop existing simulation
  if (simulation) { simulation.stop(); simulation = null; }

  // Filter to visible nodes only
  var activeNodes = NODES.filter(function(n) { return groupVisibility[n.group]; });
  var activeIds = {};
  activeNodes.forEach(function(n) { activeIds[n.id] = true; });

  // Filter edges
  var activeLinks = [];
  if (edgesVisible) {
    LINKS.forEach(function(l) {
      var sid = typeof l.source === 'object' ? l.source.id : l.source;
      var tid = typeof l.target === 'object' ? l.target.id : l.target;
      if (activeIds[sid] && activeIds[tid]) activeLinks.push(l);
    });
    if (activeLinks.length > MAX_EDGES) {
      activeLinks = activeLinks.slice(0, MAX_EDGES);
      showLimitWarning('Edge limit reached: showing ' + MAX_EDGES + ' of available edges.');
    }
  }

  // Update status
  var statusEl = document.getElementById('graph-status');
  if (statusEl) statusEl.textContent = activeNodes.length + ' nodes, ' + activeLinks.length + ' edges';

  // Rebuild SVG elements — clear and recreate
  linkG.selectAll('*').remove();
  nodeG.selectAll('*').remove();

  var container = document.getElementById('graph-container');
  var width = container.clientWidth;
  var height = container.clientHeight;

  var link = linkG.selectAll('line')
    .data(activeLinks)
    .join('line')
    .attr('class', 'link-line')
    /* Color encodes edge type (wikilink/mention/reference); dash encodes whether
       the edge crosses content categories (solid) or stays within one (dashed).
       Legacy data without type/bridge fields defaults to reference + cross. */
    .attr('stroke', function(d) { return EDGE_COLOR[d.type || 'reference'] || '#777'; })
    .attr('stroke-width', 0.6)
    .attr('stroke-dasharray', function(d) { return (d.bridge === 'same') ? '3,3' : null; })
    .attr('opacity', Math.min(0.5 * brightness, 1))
    .attr('display', function(d) {
      var t = d.type || 'reference';
      var b = d.bridge || 'cross';
      var on = (showEdgeType[t] !== false) && (showEdgeBridge[b] !== false);
      return on ? null : 'none';
    })
    .on('mouseover', function(event, d) {
      if (!showHoverNames) return;
      var sn = nodeById[d.source.id || d.source];
      var tn = nodeById[d.target.id || d.target];
      if (sn && tn) {
        var typeLabel = (d.type || 'reference').replace('_',' ');
        var bridgeLabel = d.bridge === 'same' ? 'within category' : 'crosses categories';
        var ref = d.reference ? ' · ' + escapeHtml(d.reference) : '';
        showTooltip(event,
          '<span class="tt-title" onclick="openNodeByLabel(\\'' + escapeAttr(sn.label) + '\\')">' + escapeHtml(sn.label) + '</span> &#8596; ' +
          '<span class="tt-title" onclick="openNodeByLabel(\\'' + escapeAttr(tn.label) + '\\')">' + escapeHtml(tn.label) + '</span>' +
          '<div class="tt-dir" style="margin-top:3px;color:' + (EDGE_COLOR[d.type || 'reference'] || '#888') + ';">' +
          escapeHtml(typeLabel) + ' · ' + escapeHtml(bridgeLabel) + ref + '</div>'
        );
      }
    })
    .on('mouseout', hideTooltip)
    .on('click', function(event, d) {
      var sn = nodeById[d.source.id || d.source];
      var tn = nodeById[d.target.id || d.target];
      if (sn) showLeftPage(sn);
      if (tn) showRightPanel(tn);
    });

  var node = nodeG.selectAll('circle')
    .data(activeNodes)
    .join('circle')
    .attr('class', 'node-circle')
    .attr('r', function(d) { return d.size; })
    .attr('fill', function(d) { return d.color; })
    .attr('opacity', Math.min(brightness, 1))
    /* Invisible hit-test halo: expands per-node pickable area without changing
       how the node looks. Fixes the "Names is on but hover never fires" feel. */
    .attr('stroke', 'transparent')
    .attr('stroke-width', 8)
    .attr('pointer-events', 'all')
    .attr('cursor', 'pointer')
    .on('mouseover', function(event, d) {
      if (!showHoverNames) return;
      showTooltip(event, '<div class="tt-title" onclick="openNodeByLabel(\\'' + escapeAttr(d.label) + '\\')">' + escapeHtml(d.label) + '</div><div class="tt-dir">' + escapeHtml(d.directory) + '</div><div class="tt-date">' + escapeHtml(d.date) + '</div>');
    })
    .on('mouseout', hideTooltip)
    .on('click', function(event, d) {
      showRightPanel(d);
    })
    .call(d3.drag()
      .on('start', function(event, d) {
        if (!event.active && !holdForces && simulation) simulation.alphaTarget(0.3).restart();
        d.fx = d.x; d.fy = d.y;
      })
      .on('drag', function(event, d) {
        d.fx = event.x; d.fy = event.y;
      })
      .on('end', function(event, d) {
        if (!event.active && !holdForces && simulation) simulation.alphaTarget(0);
        d.fx = null; d.fy = null;
      })
    );

  // Only run simulation on active nodes
  if (activeNodes.length > 0) {
    simulation = d3.forceSimulation(activeNodes)
      .force('link', d3.forceLink(activeLinks).id(function(d) { return d.id; }).distance(60).strength(0.15))
      .force('charge', d3.forceManyBody().strength(-20).theta(0.9))
      .force('center', d3.forceCenter(width / 2, height / 2))
      .force('collide', d3.forceCollide().radius(function(d) { return d.size + 1; }).iterations(1))
      .alphaDecay(0.05);

    // Mode == 'discipline-year': add gentle forceX/forceY pulling each node
    // toward its encoded coordinate.
    if (layoutMode === 'discipline-year') {
      simulation
        .force('encx', d3.forceX(function(d) { return targetX(d, width); }).strength(0.06))
        .force('ency', d3.forceY(function(d) { return targetY(d, height); }).strength(0.06));
    }
    simulation.on('tick', function() {
        link.attr('x1', function(d) { return d.source.x; })
            .attr('y1', function(d) { return d.source.y; })
            .attr('x2', function(d) { return d.target.x; })
            .attr('y2', function(d) { return d.target.y; });
        node.attr('cx', function(d) { return d.x; })
            .attr('cy', function(d) { return d.y; });
      });
    if (holdForces) simulation.stop();
  }

  // Auto-narrate based on current visibility (unless in timeline tour mode)
  if (!currentTrack) generateContextNarration();
}

function escapeAttr(s) {
  return s.replace(/'/g, "\\\\'").replace(/"/g, '&quot;');
}

function syncGraphToDate(date) {
  d3.selectAll('.node-circle')
    .transition().duration(300)
    .attr('opacity', function(d) {
      if (!groupVisibility[d.group]) return 0;
      return (d.date <= date) ? brightness : brightness * 0.1;
    })
    .attr('r', function(d) {
      return (d.date <= date) ? d.size : d.size * 0.5;
    });
}

// ── SEMANTIC NARRATION ENGINE ──

// Map group keys to program name patterns for matching findings/cross-connections
var GROUP_TO_PROGRAMS = {};
Object.keys(COLORS).forEach(function(key) {
  if (key.startsWith('traditions/')) {
    var name = key.split('/')[1];
    // Match patterns like "Levin Agent", "Levin", "levin"
    GROUP_TO_PROGRAMS[key] = name.toLowerCase();
  }
});

// Pre-index: which findings mention which tradition?
var FINDINGS_BY_GROUP = {};
FINDINGS.forEach(function(f) {
  var progs = f.programs.toLowerCase();
  Object.keys(GROUP_TO_PROGRAMS).forEach(function(gk) {
    var pattern = GROUP_TO_PROGRAMS[gk];
    if (progs.indexOf(pattern) !== -1) {
      if (!FINDINGS_BY_GROUP[gk]) FINDINGS_BY_GROUP[gk] = [];
      FINDINGS_BY_GROUP[gk].push(f);
    }
  });
});

// Pre-index: which cross-connections mention which tradition?
var CROSSES_BY_GROUP = {};
CROSS_CONNECTIONS.forEach(function(c) {
  var progs = c.programs.toLowerCase();
  Object.keys(GROUP_TO_PROGRAMS).forEach(function(gk) {
    var pattern = GROUP_TO_PROGRAMS[gk];
    if (progs.indexOf(pattern) !== -1) {
      if (!CROSSES_BY_GROUP[gk]) CROSSES_BY_GROUP[gk] = [];
      CROSSES_BY_GROUP[gk].push(c);
    }
  });
});

// Extract wiki overview from a tradition's wiki.md node content
function extractOverview(group) {
  var wikiNode = NODES.find(function(n) {
    return n.group === group && n.id.indexOf('wiki.md') !== -1;
  });
  if (!wikiNode || !wikiNode.content) return '';
  // Pull the core claim and summary from the content
  var content = wikiNode.content;
  var claim = '';
  var lines = content.split('\\n');
  for (var li = 0; li < lines.length; li++) {
    if (!claim && lines[li].indexOf('Core claim:') !== -1) claim = lines[li].split('Core claim:')[1].trim();
    if (!paradigm && lines[li].indexOf('Paradigm:') !== -1) paradigm = lines[li].split('Paradigm:')[1].trim();
    if (!summary && lines[li].indexOf('Summary') !== -1 && lines[li].indexOf(':') !== -1) {
      var afterColon = lines[li].split(':').slice(1).join(':').trim();
      if (afterColon) { summary = afterColon; }
      else if (li + 1 < lines.length) { summary = lines[li + 1].trim(); }
    }
  }
  if (summary) summary = summary.split('.').slice(0, 3).join('.') + '.';
  var parts = [];
  if (claim) parts.push(claim);
  if (paradigm) parts.push('Paradigm: ' + paradigm);
  if (summary && !claim) parts.push(summary);
  return parts.join('. ');
}

// Find cross-connections that span exactly the set of visible traditions
function findSharedCrosses(visibleGroups) {
  if (visibleGroups.length < 2) return [];
  var seen = {};
  var shared = [];
  // Find crosses that involve at least 2 of the visible groups
  CROSS_CONNECTIONS.forEach(function(c) {
    var progs = c.programs.toLowerCase();
    var matching = visibleGroups.filter(function(gk) {
      return progs.indexOf(GROUP_TO_PROGRAMS[gk] || '') !== -1;
    });
    if (matching.length >= 2 && !seen[c.id]) {
      seen[c.id] = true;
      shared.push({cross: c, matchCount: matching.length, groups: matching});
    }
  });
  // Sort by how many visible groups are involved (most connected first)
  shared.sort(function(a, b) { return b.matchCount - a.matchCount; });
  return shared;
}

// Find findings that involve at least one visible tradition
function findRelevantFindings(visibleGroups) {
  var seen = {};
  var relevant = [];
  visibleGroups.forEach(function(gk) {
    (FINDINGS_BY_GROUP[gk] || []).forEach(function(f) {
      if (!seen[f.id]) {
        seen[f.id] = true;
        // Count how many visible groups this finding spans
        var progs = f.programs.toLowerCase();
        var matchCount = visibleGroups.filter(function(g) {
          return progs.indexOf(GROUP_TO_PROGRAMS[g] || '') !== -1;
        }).length;
        relevant.push({finding: f, matchCount: matchCount});
      }
    });
  });
  relevant.sort(function(a, b) { return b.matchCount - a.matchCount; });
  return relevant;
}

// Sentence-aware (then word-aware) truncation. Replaces hard `text.slice(0, N)`
// calls that produced run-on artifacts like "...regardless of whe Carroll Agent..."
// when char N landed mid-word and the next narration segment got concatenated.
function truncateAtBoundary(text, maxChars) {
  if (!text) return '';
  if (text.length <= maxChars) return text;
  var sliced = text.slice(0, maxChars);
  var lastSentence = Math.max(
    sliced.lastIndexOf('. '),
    sliced.lastIndexOf('? '),
    sliced.lastIndexOf('! ')
  );
  if (lastSentence > maxChars * 0.6) {
    return sliced.slice(0, lastSentence + 1);
  }
  var lastSpace = sliced.lastIndexOf(' ');
  if (lastSpace > maxChars * 0.5) {
    return sliced.slice(0, lastSpace) + '…';
  }
  return sliced + '…';
}

// Generate a dynamic narration based on currently visible groups
function generateContextNarration() {
  var visibleTraditions = [];
  var visibleStructure = [];
  Object.keys(groupVisibility).forEach(function(gk) {
    if (!groupVisibility[gk]) return;
    if (gk.startsWith('traditions/')) visibleTraditions.push(gk);
    else visibleStructure.push(gk);
  });

  var parts = [];
  var deep = isDeep;

  // No traditions visible — summarize structure groups
  if (visibleTraditions.length === 0) {
    if (visibleStructure.length === 0) {
      setNarrationText('No groups selected. Check groups in Select Files to explore.');
      return;
    }
    var structNodes = NODES.filter(function(n) { return groupVisibility[n.group]; });
    parts.push('Viewing ' + structNodes.length + ' files across ' + visibleStructure.map(function(s) { return s.split('/').pop(); }).join(', ') + '.');
    if (deep) {
      // Pull recent cowork summary
      var cwDates = Object.keys(COWORK_SUMMARIES).sort();
      if (cwDates.length > 0) {
        var latest = COWORK_SUMMARIES[cwDates[cwDates.length - 1]];
        if (latest && latest.accomplished) parts.push('Latest session: ' + latest.accomplished.split('.').slice(0, 3).join('.') + '.');
      }
    }
    setNarrationText(parts.join(' '));
    return;
  }

  // Single tradition — deep overview
  if (visibleTraditions.length === 1) {
    var gk = visibleTraditions[0];
    var name = gk.split('/')[1];
    var displayName = name.charAt(0).toUpperCase() + name.slice(1);
    var overview = extractOverview(gk);
    if (overview) {
      parts.push(displayName + ': ' + overview);
    } else {
      parts.push('Exploring ' + displayName + '.');
    }
    // Add findings for this tradition
    var tFindings = FINDINGS_BY_GROUP[gk] || [];
    if (tFindings.length > 0) {
      if (deep) {
        tFindings.slice(0, 4).forEach(function(f) {
          parts.push(f.id + ' (' + f.type + '): ' + (f.short || truncateAtBoundary(f.finding, 200)));
        });
      } else {
        parts.push(tFindings.length + ' findings: ' + tFindings.slice(0, 3).map(function(f) { return f.id; }).join(', ') + '.');
      }
    }
    // Cross-connections this thinker participates in
    var tCrosses = CROSSES_BY_GROUP[gk] || [];
    if (tCrosses.length > 0) {
      if (deep) {
        parts.push('Cross-program questions involving ' + displayName + ':');
        tCrosses.slice(0, 4).forEach(function(c) {
          parts.push(c.id + ': ' + c.question + (c.notes ? ' (' + c.notes.slice(0, 120) + ')' : ''));
        });
      } else {
        parts.push(tCrosses.length + ' cross-connections with other thinkers.');
      }
    }
    setNarrationText(parts.join(' '));
    return;
  }

  // Multiple traditions — overview of each + connections between them
  parts.push('Comparing ' + visibleTraditions.length + ' thinkers: ' +
    visibleTraditions.map(function(gk) {
      return gk.split('/')[1].charAt(0).toUpperCase() + gk.split('/')[1].slice(1);
    }).join(', ') + '.');

  // Brief overview of each
  visibleTraditions.forEach(function(gk) {
    var name = gk.split('/')[1];
    var displayName = name.charAt(0).toUpperCase() + name.slice(1);
    var overview = extractOverview(gk);
    if (overview) {
      if (deep) {
        parts.push(displayName + ': ' + overview);
      } else {
        // Just core claim for brief
        var claim = overview.split('.')[0];
        parts.push(displayName + ': ' + claim + '.');
      }
    }
  });

  // Shared cross-connections between visible thinkers
  var sharedCrosses = findSharedCrosses(visibleTraditions);
  if (sharedCrosses.length > 0) {
    parts.push('--- Connections between them ---');
    var limit = deep ? 6 : 3;
    sharedCrosses.slice(0, limit).forEach(function(sc) {
      if (deep) {
        parts.push(sc.cross.id + ' (' + sc.cross.nature + '): ' + sc.cross.question + (sc.cross.notes ? '. ' + truncateAtBoundary(sc.cross.notes, 200) : ''));
      } else {
        parts.push(sc.cross.question);
      }
    });
    if (sharedCrosses.length > limit) {
      parts.push('...and ' + (sharedCrosses.length - limit) + ' more shared questions.');
    }
  }

  // Shared findings
  var sharedFindings = findRelevantFindings(visibleTraditions).filter(function(rf) { return rf.matchCount >= 2; });
  if (sharedFindings.length > 0) {
    parts.push('--- Shared findings ---');
    var fLimit = deep ? 4 : 2;
    sharedFindings.slice(0, fLimit).forEach(function(rf) {
      if (deep) {
        parts.push(rf.finding.id + ': ' + (rf.finding.short || truncateAtBoundary(rf.finding.finding, 200)));
      } else {
        parts.push(rf.finding.id + ' (' + rf.finding.type + ')');
      }
    });
  }

  setNarrationText(parts.join(' '));
}

function setNarrationText(text) {
  document.getElementById('narration-text').textContent = text;
}

// ── TIMELINE NARRATION (History/Recent/Latest) ──
function buildNarrationTracks() {
  var allDates = TIMELINE.map(function(t) { return t.date; }).sort();
  if (allDates.length === 0) return;

  // Get currently visible tradition names for scoping
  var visibleTraditions = [];
  Object.keys(groupVisibility).forEach(function(gk) {
    if (groupVisibility[gk] && gk.startsWith('traditions/')) {
      visibleTraditions.push(gk);
    }
  });

  var findingsByDate = {};
  FINDINGS.forEach(function(f) {
    // Only include findings relevant to visible traditions
    var progs = f.programs.toLowerCase();
    var relevant = visibleTraditions.length === 0 || visibleTraditions.some(function(gk) {
      return progs.indexOf(GROUP_TO_PROGRAMS[gk] || '') !== -1;
    });
    if (!relevant) return;
    if (!findingsByDate[f.date]) findingsByDate[f.date] = [];
    findingsByDate[f.date].push(f);
  });

  var decisionsByDate = {};
  DECISIONS.forEach(function(d) {
    if (!decisionsByDate[d.date]) decisionsByDate[d.date] = [];
    decisionsByDate[d.date].push(d);
  });

  function buildTrack(dates, deep) {
    var segments = [];
    dates.forEach(function(date) {
      var entry = TIMELINE.find(function(t) { return t.date === date; });
      if (!entry) return;
      var cw = COWORK_SUMMARIES[date];
      var df = findingsByDate[date];
      var dd = decisionsByDate[date];
      var changelog = CHANGELOGS[date];

      if (!deep) {
        var briefText = '';
        if (cw && cw.accomplished) {
          briefText = date + ': ' + cw.accomplished.split('.').slice(0, 2).join('.') + '.';
        } else if (df && df.length > 0) {
          briefText = date + ': ' + df.map(function(f) { return f.id + ' (' + f.type + ')'; }).join('; ') + '.';
        } else if (changelog) {
          var clText = typeof changelog === 'string' ? changelog : (changelog.narrative || '');
          if (clText) briefText = date + ': ' + clText.split('.').slice(0, 2).join('.') + '.';
        }
        if (briefText) segments.push({date: date, text: briefText});
        return;
      }

      // Deep mode
      var parts = [];
      if (cw && cw.accomplished) parts.push(cw.accomplished);
      if (changelog) {
        var clText = typeof changelog === 'string' ? changelog : (changelog.narrative || '');
        if (clText) parts.push(clText.slice(0, 400));
      }
      if (df) df.forEach(function(f) {
        parts.push(f.id + ' (' + f.type + '): ' + (f.short || truncateAtBoundary(f.finding, 250)));
      });
      if (dd) dd.forEach(function(d) { parts.push('Decision ' + d.id + ': ' + d.title + '. ' + (d.summary || '')); });
      if (cw && cw.discussion) parts.push('Discussion: ' + cw.discussion.slice(0, 300));
      if (parts.length > 0) segments.push({date: date, text: date + ': ' + parts.join(' ')});
    });
    return segments;
  }

  narrationTracks['history_brief'] = buildTrack(allDates, false);
  narrationTracks['history_deep'] = buildTrack(allDates, true);

  var recent3 = allDates.slice(-3);
  narrationTracks['recent_brief'] = buildTrack(recent3, false);
  narrationTracks['recent_deep'] = buildTrack(recent3, true);

  var latest = allDates.slice(-1);
  narrationTracks['latest_brief'] = buildTrack(latest, false);
  narrationTracks['latest_deep'] = buildTrack(latest, true);

  // Add relevant cross-connections to deep tracks
  var visibleCrosses = findSharedCrosses(visibleTraditions);
  if (visibleCrosses.length > 0) {
    var ccText = 'Key questions: ' + visibleCrosses.slice(0, 5).map(function(sc) { return sc.cross.question; }).join('; ');
    ['history_deep', 'recent_deep', 'latest_deep'].forEach(function(key) {
      if (narrationTracks[key] && narrationTracks[key].length > 0) {
        var last = narrationTracks[key][narrationTracks[key].length - 1];
        last.text += ' ' + ccText;
      }
    });
  }

  var slider = document.getElementById('timeline-slider');
  slider.max = allDates.length - 1;
  slider.value = allDates.length - 1;
}

// ── SEARCH ──
function runSearch() {
  var query = document.getElementById('search-input').value.trim().toLowerCase();
  if (!query) {
    generateContextNarration();
    // Reset node highlights
    d3.selectAll('.node-circle').attr('opacity', brightness);
    return;
  }
  // Search across node content, titles, and IDs
  var matches = NODES.filter(function(n) {
    if (!groupVisibility[n.group]) return false;
    var haystack = (n.label + ' ' + n.id + ' ' + (n.content || '')).toLowerCase();
    return haystack.indexOf(query) !== -1;
  });

  // Highlight matching nodes
  d3.selectAll('.node-circle')
    .transition().duration(300)
    .attr('opacity', function(d) {
      if (!groupVisibility[d.group]) return 0;
      var haystack = (d.label + ' ' + d.id + ' ' + (d.content || '')).toLowerCase();
      return haystack.indexOf(query) !== -1 ? brightness : brightness * 0.1;
    });

  // Also search findings and cross-connections
  var matchedFindings = FINDINGS.filter(function(f) {
    return (f.finding + ' ' + f.programs + ' ' + f.type).toLowerCase().indexOf(query) !== -1;
  });
  var matchedCrosses = CROSS_CONNECTIONS.filter(function(c) {
    return (c.question + ' ' + c.programs + ' ' + c.notes + ' ' + c.nature).toLowerCase().indexOf(query) !== -1;
  });

  var parts = [];
  parts.push('Search "' + query + '": ' + matches.length + ' files');
  if (matchedFindings.length > 0) parts.push(matchedFindings.length + ' findings');
  if (matchedCrosses.length > 0) parts.push(matchedCrosses.length + ' cross-connections');
  parts[parts.length - 1] += '.';

  // Show semantic results
  if (matchedFindings.length > 0) {
    parts.push('Findings: ' + matchedFindings.slice(0, 3).map(function(f) {
      return f.id + ': ' + (isDeep ? (f.short || truncateAtBoundary(f.finding, 200)) : f.type);
    }).join('. '));
  }
  if (matchedCrosses.length > 0) {
    parts.push('Cross-connections: ' + matchedCrosses.slice(0, 3).map(function(c) {
      return isDeep ? (c.id + ': ' + c.question + ' (' + truncateAtBoundary(c.notes, 100) + ')') : c.question;
    }).join('. '));
  }
  if (matches.length > 0 && matches.length <= 10) {
    parts.push('Files: ' + matches.map(function(n) { return n.label; }).join(', '));
  } else if (matches.length > 10) {
    parts.push('Top files: ' + matches.slice(0, 6).map(function(n) { return n.label; }).join(', ') + '...');
  }

  setNarrationText(parts.join(' '));
}

// ── TOUR CONTROLS ──
function getTrackKey(mode) {
  return mode + '_' + (isDeep ? 'deep' : 'brief');
}

function startTour(mode) {
  // Rebuild tracks scoped to current visibility
  buildNarrationTracks();
  currentTrack = mode;
  currentSegmentIndex = 0;
  document.querySelectorAll('#header .controls button[id^="btn-h"], #header .controls button[id^="btn-r"], #header .controls button[id^="btn-l"]').forEach(function(b) { b.classList.remove('active'); });
  var btnId = 'btn-' + mode;
  var btn = document.getElementById(btnId);
  if (btn) btn.classList.add('active');
  showSegment();
}

function showSegment() {
  if (!currentTrack) return;
  var key = getTrackKey(currentTrack);
  var track = narrationTracks[key];
  if (!track || track.length === 0) {
    setNarrationText('No timeline data for this mode with current filters.');
    return;
  }
  if (currentSegmentIndex >= track.length) {
    stopPlay();
    return;
  }
  var seg = track[currentSegmentIndex];
  setNarrationText(seg.text);
  syncGraphToDate(seg.date);

  var allDates = TIMELINE.map(function(t) { return t.date; }).sort();
  var idx = allDates.indexOf(seg.date);
  if (idx >= 0) document.getElementById('timeline-slider').value = idx;

  if (!isMuted && TTS.enabled) {
    TTS.speak(seg.text);
  }
}

function togglePlay() {
  if (isPlaying) {
    stopPlay();
  } else {
    isPlaying = true;
    document.getElementById('btn-play').textContent = 'Pause';
    document.getElementById('btn-play').classList.add('active');
    advancePlay();
  }
}

function advancePlay() {
  if (!isPlaying) return;
  showSegment();
  currentSegmentIndex++;
  var key = getTrackKey(currentTrack || 'history');
  var track = narrationTracks[key];
  if (track && currentSegmentIndex < track.length) {
    playTimer = setTimeout(advancePlay, 5000 / playSpeed);
  } else {
    stopPlay();
  }
}

function stopPlay() {
  isPlaying = false;
  if (playTimer) clearTimeout(playTimer);
  playTimer = null;
  document.getElementById('btn-play').textContent = 'Play';
  document.getElementById('btn-play').classList.remove('active');
}

function resetTour() {
  stopPlay();
  currentTrack = null;
  currentSegmentIndex = 0;
  document.querySelectorAll('#header .controls button[id^="btn-h"], #header .controls button[id^="btn-r"], #header .controls button[id^="btn-l"]').forEach(function(b) { b.classList.remove('active'); });
  generateContextNarration();
  d3.selectAll('.node-circle').attr('opacity', function(d) {
    return groupVisibility[d.group] ? brightness : 0;
  });
}

function setSpeed(val) {
  playSpeed = parseFloat(val);
}

function toggleMute() {
  isMuted = !isMuted;
  document.getElementById('btn-mute').innerHTML = isMuted ? '&#128263;' : '&#128266;';
  if (isMuted) TTS.stop();
}

function toggleDepth() {
  isDeep = !isDeep;
  document.getElementById('btn-depth').textContent = isDeep ? 'Deep' : 'Brief';
  if (currentTrack) {
    buildNarrationTracks();
    showSegment();
  } else {
    generateContextNarration();
  }
}

function onTimelineSlide(val) {
  var allDates = TIMELINE.map(function(t) { return t.date; }).sort();
  var date = allDates[parseInt(val)];
  if (date) {
    syncGraphToDate(date);
    var key = getTrackKey(currentTrack || 'history');
    var track = narrationTracks[key];
    if (track) {
      var seg = track.find(function(s) { return s.date === date; });
      if (seg) document.getElementById('narration-text').textContent = seg.text;
    }
  }
}

// ── TTS ──
var TTS = {
  enabled: true,
  provider: (function() { try { return localStorage.getItem('tts_provider') || 'browser'; } catch(e) { return 'browser'; } })(),
  apiKey: (function() { try { return localStorage.getItem('tts_api_key') || ''; } catch(e) { return ''; } })(),
  browserVoice: null,
  openaiVoice: (function() { try { return localStorage.getItem('tts_openai_voice') || 'alloy'; } catch(e) { return 'alloy'; } })(),
  cache: {},
  audioEl: null,
  utterance: null,

  speak: function(text) {
    if (isMuted) return;
    this.stop();
    if (this.provider === 'browser') {
      this.speakBrowser(text);
    } else {
      this.speakOpenAI(text);
    }
  },

  speakBrowser: function(text) {
    if (!window.speechSynthesis) return;
    var u = new SpeechSynthesisUtterance(text);
    if (this.browserVoice) u.voice = this.browserVoice;
    u.rate = playSpeed;
    window.speechSynthesis.speak(u);
    this.utterance = u;
  },

  speakOpenAI: function(text) {
    var cacheKey = text.slice(0, 100) + '_' + this.openaiVoice;
    if (this.cache[cacheKey]) {
      this.playBlob(this.cache[cacheKey]);
      return;
    }
    var self = this;
    // Use XMLHttpRequest — more reliable from file:// origins than fetch
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'https://api.openai.com/v1/audio/speech', true);
    xhr.setRequestHeader('Authorization', 'Bearer ' + this.apiKey);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.responseType = 'blob';
    xhr.onload = function() {
      if (xhr.status === 200) {
        self.cache[cacheKey] = xhr.response;
        self.playBlob(xhr.response);
      } else {
        document.getElementById('narration-text').textContent = 'TTS API error ' + xhr.status + '. Falling back to browser voice.';
        self.speakBrowser(text);
      }
    };
    xhr.onerror = function() {
      document.getElementById('narration-text').textContent = 'TTS network error. If using file://, try launching Chrome with --allow-file-access-from-files or use browser voice.';
      self.speakBrowser(text);
    };
    xhr.send(JSON.stringify({
      model: 'tts-1-hd',
      input: text,
      voice: this.openaiVoice
    }));
  },

  playBlob: function(blob) {
    var url = URL.createObjectURL(blob);
    if (!this.audioEl) this.audioEl = new Audio();
    this.audioEl.src = url;
    this.audioEl.playbackRate = playSpeed;
    this.audioEl.play();
  },

  stop: function() {
    if (window.speechSynthesis) window.speechSynthesis.cancel();
    if (this.audioEl) { this.audioEl.pause(); this.audioEl.currentTime = 0; }
  }
};

function applyFormToTTS() {
  TTS.provider = document.getElementById('tts-provider').value;
  TTS.apiKey = document.getElementById('tts-api-key').value;
  var bvSel = document.getElementById('tts-browser-voice');
  if (bvSel.selectedIndex >= 0 && window.speechSynthesis) {
    var voices = window.speechSynthesis.getVoices();
    TTS.browserVoice = voices[bvSel.selectedIndex] || null;
  }
  TTS.openaiVoice = document.getElementById('tts-openai-voice').value;
  TTS.enabled = true;
  // Persist settings
  try {
    localStorage.setItem('tts_provider', TTS.provider);
    localStorage.setItem('tts_api_key', TTS.apiKey);
    localStorage.setItem('tts_openai_voice', TTS.openaiVoice);
  } catch(e) {}
}

// ── SETTINGS MODAL ──
function openSettings() {
  document.getElementById('settings-modal').classList.add('visible');
  populateVoices();
}

function closeSettings() {
  document.getElementById('settings-modal').classList.remove('visible');
}

function saveSettings() {
  applyFormToTTS();
  closeSettings();
}

function testTTS() {
  applyFormToTTS();
  TTS.speak('This is a test of the text to speech system.');
}

function populateVoices() {
  if (!window.speechSynthesis) return;
  var sel = document.getElementById('tts-browser-voice');
  var voices = window.speechSynthesis.getVoices();
  sel.innerHTML = '';
  voices.forEach(function(v, i) {
    var opt = document.createElement('option');
    opt.value = i;
    opt.textContent = v.name + ' (' + v.lang + ')';
    sel.appendChild(opt);
  });
}
if (window.speechSynthesis) {
  window.speechSynthesis.onvoiceschanged = populateVoices;
}

// ── PANEL RESIZE ──
var resizeSide = null;
function startResize(e, side) {
  e.preventDefault();
  resizeSide = side;
  document.getElementById(side + '-resize').classList.add('dragging');
  document.addEventListener('mousemove', doResize);
  document.addEventListener('mouseup', stopResize);
  document.body.style.cursor = 'col-resize';
  document.body.style.userSelect = 'none';
}
function doResize(e) {
  if (!resizeSide) return;
  if (resizeSide === 'left') {
    var newW = Math.max(120, Math.min(500, e.clientX));
    document.getElementById('left-panel').style.width = newW + 'px';
  } else {
    var newW = Math.max(200, Math.min(600, window.innerWidth - e.clientX));
    document.getElementById('right-panel').style.width = newW + 'px';
  }
}
function stopResize() {
  if (resizeSide) {
    document.getElementById(resizeSide + '-resize').classList.remove('dragging');
  }
  resizeSide = null;
  document.removeEventListener('mousemove', doResize);
  document.removeEventListener('mouseup', stopResize);
  document.body.style.cursor = '';
  document.body.style.userSelect = '';
}

// ── FOOTER RESIZE ──
function startFooterResize(e) {
  e.preventDefault();
  document.getElementById('footer-resize').classList.add('dragging');
  document.addEventListener('mousemove', doFooterResize);
  document.addEventListener('mouseup', stopFooterResize);
  document.body.style.cursor = 'row-resize';
  document.body.style.userSelect = 'none';
}
function doFooterResize(e) {
  var newH = Math.max(60, Math.min(window.innerHeight * 0.6, window.innerHeight - e.clientY));
  document.getElementById('footer').style.height = newH + 'px';
}
function stopFooterResize() {
  document.getElementById('footer-resize').classList.remove('dragging');
  document.removeEventListener('mousemove', doFooterResize);
  document.removeEventListener('mouseup', stopFooterResize);
  document.body.style.cursor = '';
  document.body.style.userSelect = '';
}

// Re-clamp footer height on window resize so the panel can't overflow when the
// window shrinks below the user's previously-dragged height.
function clampFooterHeight() {
  var footer = document.getElementById('footer');
  if (!footer) return;
  var current = footer.getBoundingClientRect().height;
  var maxAllowed = Math.max(60, window.innerHeight * 0.6);
  if (current > maxAllowed) {
    footer.style.height = maxAllowed + 'px';
  } else if (current < 60) {
    footer.style.height = '60px';
  }
}
window.addEventListener('resize', clampFooterHeight);

// ── INIT ──
document.addEventListener('DOMContentLoaded', function() {
  buildFilters();
  initGraph();
  // generateContextNarration is called automatically by rebuildGraph
  // Two-stage fit: first pass at 800ms gets the user onto a populated cluster
  // before the simulation has fully settled; second pass at 2500ms re-fits.
  setTimeout(fitAll, 800);
  setTimeout(fitAll, 2500);
});
</script>
</body>
</html>"""

    return html


def main():
    if len(sys.argv) < 3:
        print("Usage: python generate_visualization.py <input.json> <output.html>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    data = load_json(input_path)
    nodes, links = build_graph_data(data)
    nodes_json = json.dumps(nodes, ensure_ascii=False)
    links_json = json.dumps(links, ensure_ascii=False)

    html = generate_html(data, nodes_json, links_json)

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(html)

    print("Generated: " + output_path)
    print("Size: " + str(len(html)) + " chars")
    print("Nodes: " + str(len(nodes)) + ", Links: " + str(len(links)))


if __name__ == '__main__':
    main()
