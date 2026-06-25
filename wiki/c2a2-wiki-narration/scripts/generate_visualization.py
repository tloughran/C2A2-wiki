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
    # Runtime agent ACTORS (OpenStory telemetry) — distinct from the agent
    # DEFINITION docs in the 'agents' group above. Set explicitly at merge time
    # (no vault directory maps here via get_group), so it only ever holds the
    # scheduled-task/human actor nodes from agent_node_edges.json.
    'agent-activity': '#C77DCB',
    'inbox': '#7A8B8B',
    'review': '#5E9B76',
    'deferred': '#6B7B7B',
    'sessions': '#8A9098',
    'root': '#9A9A9A',
    'tools': '#4E9EA8',
    'summa': '#A89B6E',           # parchment — Summa Theologiae companion vault (Pass B)
    # Tradition Index — the sewing-bootstrap hub (traditions/_index.md) linking
    # all 15 tradition wikis. Its own group so it earns a dedicated left-panel
    # checkbox and a bright, hub-sized node instead of a grey dot lost in 'root'.
    # No vault directory maps here via get_group; it's assigned in the node loop.
    'tradition-index': '#F2D43F',
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
    'summa':                  'Summa',
    'tradition-index':        'Tradition Index',
    # Relabel only — the group key stays 'agents' so nothing downstream
    # (get_group, edges, presets) changes. The 24 agent-definition docs now
    # read as "Agent identity"; the runtime actors live in "Agent activity".
    'agents':                 'Agent identity',
    'agent-activity':         'Agent activity',
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


def build_graph_data(data, agent_data=None):
    """Build nodes and links arrays from vault data.

    If agent_data (parsed agent_node_edges.json) is supplied, its runtime
    actor nodes and three edge layers (coref_substrate / coref_projected /
    flow) are merged in as a first-class 'agent-activity' group before the
    integer-interning pass, so agent edges intern identically to wiki edges.
    """
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
        # Promote the Tradition Index hub out of the catch-all 'root' group into
        # its own first-class group (dedicated checkbox + distinct color) and
        # size it as the largest node so it reads as the structural center
        # rather than a grey size-2 dot buried among ~600 root nodes.
        if fp == 'traditions/_index.md':
            group = 'tradition-index'
            color = COLORS['tradition-index']
            size = 8
        nodes.append({
            'id': fp,
            'label': f.get('title', f.get('filename', fp)),
            'directory': f.get('directory', ''),
            'date': f.get('date', ''),
            'color': color,
            'group': group,
            'size': size,
            'content': sanitize_braces(f.get('content', '')),
            # Pass G — surface the per-file content tag kinds so the left-panel
            # "Content tags" cut can filter on them. Empty list = no tagged refs.
            'has_tags': f.get('has_tags', []),
            # Pass G — surface raw refs so the dynamic banner can count distinct
            # FINDING-/DECISION-/CROSS-/OPEN- IDs visible in the cut survivors.
            'references': f.get('references', []),
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

    # ── AGENT LAYER MERGE (OpenStory) ──────────────────────────────────────
    # Append runtime actor nodes (group 'agent-activity') and the three edge
    # layers. Agent edges are exempt from the wiki type/bridge cuts (they carry
    # no wikilink/mention/reference type) and are gated solely by per-layer
    # toggles in the browser via their 'layer' field. score_deg = log(weight)
    # so heavier interactions rank higher under the existing visibility budget.
    if agent_data:
        _agent_color = COLORS['agent-activity']
        _existing_ids = filepath_set  # wiki node ids already present
        _agent_ids = set()
        for an in agent_data.get('agent_nodes', []):
            aid = an['id']
            _agent_ids.add(aid)
            sessions = an.get('sessions', 0)
            events = an.get('events', 0)
            node_refs = an.get('node_refs', 0)
            # Size: a touch larger than wiki nodes (2–5) so actors read as hubs.
            size = max(3, min(11, 3 + int(round(math.log(sessions + 1) * 1.4))))
            profile = (
                "# " + an.get('label', aid) + "\n\n"
                "**Kind:** " + str(an.get('kind', '')) + " · "
                "**Category:** " + str(an.get('category', '')) + "\n\n"
                "- Sessions: " + str(sessions) + "\n"
                "- Events: " + str(events) + "\n"
                "- Distinct vault nodes touched: " + str(node_refs) + "\n\n"
                "*Runtime agent actor (OpenStory telemetry). Edge layers: "
                "co-reference substrate (→ wiki nodes it touched), projected "
                "co-reference (↔ agents sharing nodes), and directed "
                "write→read flow.*"
            )
            nodes.append({
                'id': aid,
                'label': an.get('label', aid),
                'directory': 'agent-activity',
                'date': '',
                'color': _agent_color,
                'group': 'agent-activity',
                'size': size,
                'content': profile,
                'has_tags': [],
                'references': [],
                'kind': an.get('kind', ''),
                'category': an.get('category', ''),
            })

        def _agent_edge(s, t, layer, weight):
            return {
                'source': s, 'target': t, 'layer': layer,
                'weight': weight,
                'score_deg': round(math.log(weight + 1), 3),
                'score_type': 1.0,
                'score_bridge': 0.0,
            }

        skipped_substrate = 0
        for e in agent_data.get('coref_substrate', []):
            s, t, w = e['source'], e['target'], e.get('weight', 1)
            # source is an agent actor; target must be an existing wiki node.
            if s in _agent_ids and t in _existing_ids:
                links.append(_agent_edge(s, t, 'substrate', w))
            else:
                skipped_substrate += 1
        for e in agent_data.get('coref_projected', []):
            s, t, w = e['source'], e['target'], e.get('weight', 1)
            if s in _agent_ids and t in _agent_ids:
                links.append(_agent_edge(s, t, 'projected', w))
        for e in agent_data.get('flow', []):
            s, t, w = e['source'], e['target'], e.get('weight', 1)
            if s in _agent_ids and t in _agent_ids:
                links.append(_agent_edge(s, t, 'flow', w))  # directed (source→target)

        print("Agent layer merged: " + str(len(_agent_ids)) + " actor nodes; "
              + "substrate=" + str(sum(1 for l in links if l.get('layer') == 'substrate'))
              + " (skipped " + str(skipped_substrate) + " w/ missing wiki target), "
              + "projected=" + str(sum(1 for l in links if l.get('layer') == 'projected'))
              + ", flow=" + str(sum(1 for l in links if l.get('layer') == 'flow')))

    # ── PAYLOAD COMPRESSION: intern link source/target as integer indices ──
    # Each link previously stored two ~80-char filepath strings. Replacing them
    # with integer indices into NODES drops ~165 bytes per link; with ~14k links
    # that's ~2.3 MB off the inline JSON. The HTML template restores the string
    # IDs once at script load (single pass before any code touches LINKS), so
    # this is purely a payload-size optimization — no behavior change.
    path_to_idx = {n['id']: i for i, n in enumerate(nodes)}
    for link in links:
        s = link['source']
        t = link['target']
        if isinstance(s, str) and s in path_to_idx:
            link['source'] = path_to_idx[s]
        if isinstance(t, str) and t in path_to_idx:
            link['target'] = path_to_idx[t]

    return nodes, links


def generate_html(data, nodes_json, links_json):
    """Generate the complete HTML visualization."""
    # Inline the shared C2A2 search-pipeline module so the Sociogram remains
    # self-contained. Single source of truth lives in wiki/lib/c2a2-search.js
    # (loaded by every C2A2 surface; see app.js -> c2a2-search.js in the
    # Community Explorer). DO NOT duplicate the module body in this template.
    _script_dir = os.path.dirname(os.path.abspath(__file__))
    _c2a2_search_path = os.path.normpath(os.path.join(_script_dir, '..', '..', 'lib', 'c2a2-search.js'))
    with open(_c2a2_search_path, 'r', encoding='utf-8') as _f:
        c2a2_search_js = _f.read()

    metadata = data.get('metadata', {})
    total_files = metadata.get('total_files', 0)
    findings = data.get('findings', [])
    decisions = data.get('decisions', [])
    cross_connections = data.get('cross_connections', [])
    changelogs = data.get('changelogs', {})
    cowork_summaries = data.get('cowork_summaries', {})
    tradition_summaries = data.get('tradition_summaries', {})
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
        if tradition_summaries.get(key):
            entry['summary'] = tradition_summaries[key]
        if key.startswith('traditions/'):
            tradition_groups.append(entry)
        else:
            structure_groups.append(entry)

    # The Tradition-concept meta pop-up (the '?' on the Traditions section
    # header) is not a group, so it rides along as its own injected string.
    tradition_concept = tradition_summaries.get('__tradition_concept__', '')

    tradition_groups_json = json.dumps(tradition_groups, ensure_ascii=False)
    structure_groups_json = json.dumps(structure_groups, ensure_ascii=False)
    tradition_concept_json = json.dumps(tradition_concept, ensure_ascii=False)

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
/* Friendly-label typeahead (navigation increment 1.5) — opens upward from the footer search box */
#search-suggest { background: #14141f; border: 1px solid #3a3a4a; border-radius: 4px; max-height: 180px; overflow-y: auto; box-shadow: 0 -4px 12px rgba(0,0,0,0.5); z-index: 50; }
#search-suggest .sg-head { font-size: 10px; text-transform: uppercase; letter-spacing: 1px; color: #888; padding: 4px 8px; border-bottom: 1px solid #2a2a3a; }
#search-suggest .sg-row { display: flex; align-items: center; gap: 6px; padding: 4px 8px; cursor: pointer; font-size: 12px; color: #e0e0e0; }
#search-suggest .sg-row:hover, #search-suggest .sg-row.active { background: #2a2a3a; }
.filter-label { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.sum-q { color: #C9A84C; cursor: pointer; font-weight: 700; font-size: 12px; margin-left: 4px; flex-shrink: 0; opacity: 0.8; }
.sum-q:hover { opacity: 1; }
.sum-q-head { color: #C9A84C; cursor: pointer; font-weight: 700; font-size: 12px; margin-left: 6px; opacity: 0.85; }
.sum-q-head:hover { opacity: 1; }
#sum-pop { position: fixed; max-width: 380px; max-height: 70vh; overflow-y: auto; background: #14141f; border: 1px solid #3a3a4a; border-radius: 6px; padding: 12px 14px; font-size: 12px; line-height: 1.5; color: #d8d8e0; box-shadow: 0 6px 24px rgba(0,0,0,0.6); z-index: 9999; display: none; }
#sum-pop h4 { font-size: 13px; color: #f0f0f0; margin-bottom: 8px; }
#sum-pop p { margin-bottom: 8px; }
#left-page-viewer { margin-top: 12px; border-top: 1px solid #2a2a3a; padding-top: 8px; display: none; }
#left-page-viewer .page-content { max-height: calc(100vh - 200px); overflow-y: auto; font-size: 11px; line-height: 1.5; }
#left-page-viewer .page-title { font-weight: 700; color: #FFD700; font-size: 13px; margin-bottom: 4px; }
#left-page-viewer .page-path { font-size: 10px; color: #666; margin-bottom: 8px; }
#left-page-viewer .dismiss-btn { background: none; border: none; color: #888; cursor: pointer; float: right; font-size: 14px; }
#left-page-viewer .popout-btn { background: none; border: 1px solid #3a3a4a; color: #888; cursor: pointer; float: right; font-size: 11px; padding: 1px 6px; border-radius: 4px; margin-right: 4px; }
#left-page-viewer .popout-btn:hover { background: #2a2a3a; color: #ccc; }

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
#right-panel .popout-btn { background: none; border: 1px solid #3a3a4a; color: #888; cursor: pointer; float: right; font-size: 12px; padding: 2px 8px; border-radius: 4px; margin-right: 4px; }
#right-panel .popout-btn:hover { background: #2a2a3a; color: #ccc; }

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

/* Mobile notice strip — hidden by default; revealed at ≤640px (see media block). */
#mobile-notice { display: none; }

/* ── MOBILE READABILITY (≤640px) ──
   First-pass mobile pathway, 2026-05-19. Honest scope: the Sociogram is
   viewable on a phone (pan, pinch, tap nodes, play tours, read articles),
   but filtering and the heavier edge-density controls require a desktop.
   A small notice strip explains this. Above 640px nothing changes. */
@media (max-width: 640px) {
  /* HEADER — keep, but reduce overcrowding and bump touch targets */
  #header {
    padding: 6px 10px;
    height: 52px;
    gap: 6px;
    overflow-x: auto;
    overflow-y: hidden;
    -webkit-overflow-scrolling: touch;
  }
  #header .title { font-size: 14px; flex-shrink: 0; }
  #header .controls { gap: 6px; flex-shrink: 0; align-items: center; }
  /* Hide the secondary controls — filtering happens on desktop */
  #header .controls .brightness-control,
  #header .controls .date-control,
  #header .controls label[title*="Free: positions"],
  #header .controls label[title*="which edges"],
  #header .controls #btn-edge-help {
    display: none;
  }
  /* Hide the vertical separators between control groups */
  #header .controls span[style*="background:#3a3a4a"] { display: none; }
  #header .controls button {
    min-height: 38px;
    padding: 6px 10px;
    font-size: 13px;
  }

  /* LEFT PANEL — hidden on mobile (filtering requires a larger screen) */
  #left-panel { display: none; }
  .resize-handle#left-resize { display: none; }

  /* GRAPH CONTAINER fills the freed space */
  #graph-container { width: 100%; }

  /* RIGHT PANEL — full-screen overlay when shown by existing JS */
  #right-panel {
    position: fixed;
    top: 52px;
    left: 0;
    right: 0;
    bottom: 0;
    width: 100%;
    z-index: 250;
    padding: 14px 16px;
  }
  #right-panel .page-title { font-size: 17px; }
  #right-panel .page-content { font-size: 15px; line-height: 1.7; }
  #right-panel .page-content h1 { font-size: 19px; }
  #right-panel .page-content h2 { font-size: 17px; }
  #right-panel .page-content h3 { font-size: 15px; }
  #right-panel .dismiss-btn {
    min-height: 44px; min-width: 44px;
    font-size: 18px; padding: 6px 14px;
  }
  #right-panel .popout-btn {
    min-height: 44px; min-width: 44px;
    font-size: 14px; padding: 6px 12px;
  }
  .resize-handle#right-resize { display: none; }

  /* TOOLTIP — wider on mobile so titles don't truncate awkwardly */
  #tooltip { font-size: 13px; padding: 10px 14px; max-width: 88vw; }

  /* EDGE LEGEND — smaller, move out of common tap zones.
     !important needed because the element has inline top/right in the body markup. */
  #edge-legend {
    font-size: 9px !important;
    padding: 4px 7px !important;
    top: auto !important;
    bottom: 80px !important;
    right: 6px !important;
    left: auto !important;
  }

  /* HELP POPOVERS — undo hardcoded desktop positions */
  #edges-help-popover,
  #tags-help-popover,
  #edge-help-popover {
    position: fixed !important;
    top: 76px !important;
    left: 6px !important;
    right: 6px !important;
    width: auto !important;
    max-width: none !important;
    font-size: 13px;
  }

  /* FOOTER — collapse to essentials: narration text + tour controls only */
  #footer-resize { display: none; }
  #footer {
    height: 76px;
    min-height: 76px;
    padding: 6px 10px;
    gap: 8px;
  }
  #narration-text { font-size: 13px; padding: 4px 6px; }
  /* Hide the search row on mobile.
     !important needed because the div has inline display:flex in the body markup. */
  #footer-search-row { display: none !important; }
  #footer .footer-controls { gap: 4px; }
  #footer .footer-controls button {
    min-height: 40px;
    padding: 6px 10px;
    font-size: 13px;
  }
  #footer .footer-controls select {
    min-height: 40px;
    padding: 4px 6px;
    font-size: 13px;
  }

  /* SETTINGS MODAL — full-width on phone */
  #settings-content { width: 92%; padding: 20px 18px; }
  #settings-content h2 { font-size: 16px; }
  #settings-content button { min-height: 40px; padding: 8px 14px; }

  /* MOBILE NOTICE STRIP — visible only at this breakpoint */
  #mobile-notice {
    display: block;
    position: fixed;
    top: 52px;
    left: 0;
    right: 0;
    background: rgba(20, 20, 35, 0.92);
    color: #C9A84C;
    font-size: 11px;
    padding: 4px 10px;
    text-align: center;
    z-index: 50;
    border-bottom: 1px solid #3a3a4a;
    pointer-events: none;
    letter-spacing: 0.2px;
  }
  /* Push the graph below the notice strip */
  #main { padding-top: 24px; }
}
</style>
</head>
<body>
<div id="sum-pop"></div>
<!-- Mobile preview notice — visible only at ≤640px (see #mobile-notice in CSS).
     Sized and positioned by the mobile media block. Single short line, no controls. -->
<div id="mobile-notice">Mobile preview · pan and tap nodes · filters require a larger screen</div>
<div id="app">
  <!-- HEADER -->
  <div id="header">
    <div class="title">C2A2 Wiki Narration</div>
    <!-- Stats pills removed 2026-05-11: header was overflowing at 1200px viewport
         and the same numbers are echoed at the bottom-left of the canvas
         ("N nodes, E edges") and update with filters there. -->

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
      <label style="font-size:11px;display:flex;align-items:center;gap:4px;cursor:pointer;" title="Picks which edges count as 'top' when there are more edges than fit on screen. Zoom in to see weaker edges.">Score:
        <select id="score-mode" onchange="setScoreMode(this.value)" style="font-size:11px;background:#1a1a2a;color:#e0e0e0;border:1px solid #3a3a4a;border-radius:3px;padding:1px 3px;">
          <option value="balanced" selected>Balanced</option>
          <option value="connected">Connected</option>
          <option value="cross-tradition">Cross-tradition</option>
          <option value="editorial">Editorial</option>
        </select>
      </label>
      <button id="btn-edge-help" onclick="toggleEdgeHelp(event)" style="width:18px;height:18px;border-radius:50%;background:#1a1a2a;color:#888;border:1px solid #3a3a4a;font-size:11px;font-weight:600;cursor:pointer;padding:0;line-height:16px;text-align:center;" title="How adaptive edge density works">?</button>
      <div class="brightness-control">
        <label>Brightness</label>
        <input type="range" id="brightness-slider" min="0.1" max="2" step="0.05" value="1" oninput="setBrightness(this.value)">
      </div>
      <!-- Date threshold slider (Pass G). Show only files added on or after the
           selected date. Default leftmost = no threshold (all files). -->
      <div class="date-control" style="display:flex;align-items:center;gap:6px;font-size:11px;">
        <label title="Hide files added before this date" style="cursor:pointer;">Since:
          <input type="range" id="date-slider" min="0" max="0" value="0" step="1" style="width:90px;vertical-align:middle;" oninput="setDateThreshold(this.value)">
        </label>
        <span id="date-slider-label" style="color:#888;font-size:10px;min-width:80px;">all dates</span>
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
        <h3><input type="checkbox" id="chk-all-traditions" checked onchange="toggleSection('traditions', this.checked)" style="margin-right:4px;cursor:pointer;"> Traditions<span class="sum-q-head" data-key="__tradition__" title="What is a tradition in C2A2?" onclick="showSummary(event,this)">?</span></h3>
        <div id="tradition-filters"></div>
        <hr>
        <h3><input type="checkbox" id="chk-all-structure" checked onchange="toggleSection('structure', this.checked)" style="margin-right:4px;cursor:pointer;"> Structure</h3>
        <div id="structure-filters"></div>
        <hr>
        <h3 style="display:flex;align-items:center;gap:4px;">
          <input type="checkbox" id="chk-all-edges" checked onchange="toggleAllEdges(this.checked)" style="margin-right:4px;cursor:pointer;">
          <span>Edges</span>
          <button id="btn-edges-help" onclick="toggleEdgesHelp(event)" style="margin-left:auto;width:16px;height:16px;border-radius:50%;background:#1a1a2a;color:#888;border:1px solid #3a3a4a;font-size:10px;font-weight:600;cursor:pointer;padding:0;line-height:14px;text-align:center;" title="How the Edges filters work">?</button>
        </h3>
        <div style="font-size:10px;color:#888;margin:2px 0 2px 4px;">By type — color</div>
        <div class="filter-item"><input type="checkbox" id="chk-edge-wikilink" checked onchange="toggleEdgeType('wikilink', this.checked)"><span class="filter-dot" style="background:#C9A84C"></span><span class="filter-label">Wikilink</span></div>
        <div class="filter-item"><input type="checkbox" id="chk-edge-mention" checked onchange="toggleEdgeType('mention', this.checked)"><span class="filter-dot" style="background:#5B9A8B"></span><span class="filter-label">Mention</span></div>
        <div class="filter-item"><input type="checkbox" id="chk-edge-reference" checked onchange="toggleEdgeType('reference', this.checked)"><span class="filter-dot" style="background:#5A6878"></span><span class="filter-label">Reference</span></div>
        <div style="font-size:10px;color:#888;margin:6px 0 2px 4px;">By bridge — line style</div>
        <div class="filter-item">
          <input type="checkbox" id="chk-edge-cross" checked onchange="toggleEdgeBridge('cross', this.checked)">
          <span style="display:inline-block;width:14px;height:0;border-top:1.5px solid #aaa;vertical-align:middle;flex-shrink:0;"></span>
          <span class="filter-label">Crosses categories</span>
        </div>
        <div class="filter-item">
          <input type="checkbox" id="chk-edge-same" checked onchange="toggleEdgeBridge('same', this.checked)">
          <span style="display:inline-block;width:14px;height:0;border-top:1.5px dashed #aaa;vertical-align:middle;flex-shrink:0;"></span>
          <span class="filter-label">Within category</span>
        </div>
        <div style="font-size:10px;color:#888;margin:6px 0 2px 4px;">Agent layers (OpenStory)</div>
        <div class="filter-item"><input type="checkbox" id="chk-layer-substrate" onchange="toggleLayer('substrate', this.checked)"><span class="filter-dot" style="background:#7A6E9E"></span><span class="filter-label">Co-ref substrate &middot; agent&rarr;wiki</span></div>
        <div class="filter-item"><input type="checkbox" id="chk-layer-projected" onchange="toggleLayer('projected', this.checked)"><span class="filter-dot" style="background:#5BC0BE"></span><span class="filter-label">Projected co-ref &middot; agent&harr;agent</span></div>
        <div class="filter-item"><input type="checkbox" id="chk-layer-flow" onchange="toggleLayer('flow', this.checked)"><span class="filter-dot" style="background:#E8954A"></span><span class="filter-label">Write&rarr;read flow &middot; directed</span></div>
        <div class="filter-item"><input type="checkbox" id="chk-substrate-context" onchange="toggleSubstrateContext(this.checked)"><span class="filter-dot" style="background:#444a5e"></span><span class="filter-label">Substrate context &middot; wiki files agents touch</span></div>
        <hr>
        <h3 style="display:flex;align-items:center;gap:4px;">
          <input type="checkbox" id="chk-all-tags" onchange="toggleAllTags(this.checked)" style="margin-right:4px;cursor:pointer;">
          <span>Content tags</span>
          <button id="btn-tags-help" onclick="toggleTagsHelp(event)" style="margin-left:auto;width:16px;height:16px;border-radius:50%;background:#1a1a2a;color:#888;border:1px solid #3a3a4a;font-size:10px;font-weight:600;cursor:pointer;padding:0;line-height:14px;text-align:center;" title="How Content-tag cuts work">?</button>
        </h3>
        <!-- Default-OFF: leaving the section unchecked means "no tag cut applies",
             so all files pass. Checking any tag NARROWS to files carrying ≥1 of
             the checked tags. -->
        <div class="filter-item"><input type="checkbox" id="chk-tag-finding" onchange="toggleTagKind('finding', this.checked)"><span class="filter-label">Findings <span style="color:#888;font-size:10px;">(FINDING-NN)</span></span></div>
        <div class="filter-item"><input type="checkbox" id="chk-tag-decision" onchange="toggleTagKind('decision', this.checked)"><span class="filter-label">Decisions <span style="color:#888;font-size:10px;">(DECISION-NN)</span></span></div>
        <div class="filter-item"><input type="checkbox" id="chk-tag-cross" onchange="toggleTagKind('cross', this.checked)"><span class="filter-label">Cross-connections <span style="color:#888;font-size:10px;">(CROSS-NN)</span></span></div>
        <div class="filter-item"><input type="checkbox" id="chk-tag-open" onchange="toggleTagKind('open', this.checked)"><span class="filter-label">Open questions <span style="color:#888;font-size:10px;">(OPEN-NN)</span></span></div>
      </div>
      <!-- Edges-section help popover. position:fixed so the panel's overflow:auto can't clip it. -->
      <div id="edges-help-popover" style="display:none;position:fixed;top:200px;left:212px;width:320px;background:#14141e;border:1px solid #3a3a4a;border-radius:6px;padding:12px 28px 12px 14px;z-index:300;font-size:11.5px;line-height:1.5;color:#d0d0d0;box-shadow:0 4px 16px rgba(0,0,0,0.55);" role="dialog" aria-label="Edges section help">
        <button onclick="toggleEdgesHelp(event)" aria-label="Close" style="position:absolute;top:4px;right:6px;background:transparent;border:none;color:#888;font-size:18px;line-height:1;cursor:pointer;padding:2px 6px;">&times;</button>
        <div style="font-size:11px;font-weight:600;color:#C9A84C;margin-bottom:8px;text-transform:uppercase;letter-spacing:0.6px;">Edges — how the filters compose</div>
        <p style="margin:4px 0;">Each checkbox here is a <strong style="color:#f0f0f0;">cut</strong>: a hard include/exclude on which edges are <em>allowed</em> to appear. They compose with AND.</p>
        <ul style="margin:6px 0;padding-left:18px;">
          <li style="margin-bottom:5px;"><strong>By type</strong> — color encodes how the edge was inferred. Wikilink (gold) = explicit <code>[[link]]</code> in source. Mention (sage) = architecture prose names a thinker. Reference (slate) = co-citation of a shared ID like <code>FINDING-NN</code>.</li>
          <li style="margin-bottom:5px;"><strong>By bridge</strong> — line style encodes scope. Solid = the edge crosses category boundaries (tradition ↔ architecture, Summa ↔ tradition). Dashed = both endpoints are in the same category (e.g. sibling files in one tradition).</li>
        </ul>
        <p style="margin:6px 0 4px 0;">An edge needs to pass <em>every</em> active cut to be allowed. Among allowed edges, the graph shows the highest-scored subset that fits the visibility budget.</p>
        <p style="margin:6px 0 0 0;font-size:10.5px;color:#aaa;">Adjacent controls: the <strong>Score</strong> picker (top toolbar) ranks the allowed edges; <strong>zoom</strong> sets the budget. The <strong>Mode</strong> picker is independent — it changes spatial layout, not which edges appear.</p>
      </div>
      <!-- Content-tags help popover (Pass G). -->
      <div id="tags-help-popover" style="display:none;position:fixed;top:280px;left:212px;width:320px;background:#14141e;border:1px solid #3a3a4a;border-radius:6px;padding:12px 28px 12px 14px;z-index:300;font-size:11.5px;line-height:1.5;color:#d0d0d0;box-shadow:0 4px 16px rgba(0,0,0,0.55);" role="dialog" aria-label="Content tags help">
        <button onclick="toggleTagsHelp(event)" aria-label="Close" style="position:absolute;top:4px;right:6px;background:transparent;border:none;color:#888;font-size:18px;line-height:1;cursor:pointer;padding:2px 6px;">&times;</button>
        <div style="font-size:11px;font-weight:600;color:#C9A84C;margin-bottom:8px;text-transform:uppercase;letter-spacing:0.6px;">Content tags</div>
        <p style="margin:4px 0;">A separate cut from Traditions/Structure: these checkboxes filter to files that <em>contain</em> a particular kind of reference ID, regardless of where they sit in the directory tree.</p>
        <ul style="margin:6px 0;padding-left:18px;">
          <li style="margin-bottom:4px;"><strong>Findings</strong> — files referencing <code>FINDING-NN</code>: pattern-detector outputs across traditions.</li>
          <li style="margin-bottom:4px;"><strong>Decisions</strong> — files referencing <code>DECISION-NN</code>: settled architectural commitments.</li>
          <li style="margin-bottom:4px;"><strong>Cross-connections</strong> — files referencing <code>CROSS-NN</code>: explicit inter-tradition dialogue moments.</li>
          <li style="margin-bottom:4px;"><strong>Open questions</strong> — files referencing <code>OPEN-NN</code>: unresolved inquiries.</li>
        </ul>
        <p style="margin:6px 0 0 0;font-size:10.5px;color:#aaa;">When no tag is checked, this section imposes no cut (everything passes). Checking any tag narrows to files carrying that tag (OR within the section). Combines with Tradition/Structure cuts via AND.</p>
      </div>
      <!-- Banner-stats help popover removed 2026-05-11 along with the stats pills. -->

      <div id="left-page-viewer">
        <button class="dismiss-btn" onclick="dismissLeftPage()" title="Close">&times;</button>
        <button class="popout-btn" onclick="popoutPage('left')" title="Open in new window">&#x2197;</button>
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
      <div id="edge-status" style="position:absolute;bottom:8px;left:50%;transform:translateX(-50%);font-size:11px;color:#888;z-index:10;background:rgba(20,20,30,0.7);padding:2px 8px;border-radius:3px;border:1px solid #2a2a3e;"></div>
      <!-- Adaptive-density help popover (anchor-positioned just below the toolbar) -->
      <div id="edge-help-popover" style="display:none;position:absolute;top:42px;right:8px;width:340px;background:#14141e;border:1px solid #3a3a4a;border-radius:6px;padding:12px 28px 12px 14px;z-index:250;font-size:11.5px;line-height:1.5;color:#d0d0d0;box-shadow:0 4px 16px rgba(0,0,0,0.55);">
        <button onclick="toggleEdgeHelp(event)" style="position:absolute;top:4px;right:6px;background:transparent;border:none;color:#888;font-size:18px;line-height:1;cursor:pointer;padding:2px 6px;">&times;</button>
        <div style="font-size:11px;font-weight:600;color:#C9A84C;margin-bottom:8px;text-transform:uppercase;letter-spacing:0.6px;">How edge density adapts</div>
        <p style="margin:4px 0;">The graph holds many more edges than fit on screen. The renderer shows the top edges by score, and weaker ones fade in as you (a) zoom in or (b) narrow filters by checking off types/traditions/structure.</p>
        <p style="margin:6px 0 4px 0;"><strong style="color:#f0f0f0;">Score modes</strong> change which edges count as "top":</p>
        <ul style="margin:6px 0 0 0;padding-left:18px;">
          <li style="margin-bottom:4px;"><strong>Balanced</strong>: combines structural density, edge type, multiplicity, and cross-bucket bridging.</li>
          <li style="margin-bottom:4px;"><strong>Connected</strong>: pure structural density — surfaces the hubs.</li>
          <li style="margin-bottom:4px;"><strong>Cross-tradition</strong>: privileges edges that bridge between traditions or between traditions and architecture.</li>
          <li style="margin-bottom:4px;"><strong>Editorial</strong>: privileges explicit connections (wikilinks > mentions > references).</li>
        </ul>
        <p style="margin:8px 0 0 0;font-size:10.5px;color:#888;">Edge counts shown bottom-center: visible / total surviving cuts. Hover any edge for its type, bridge, and reference ID.</p>
      </div>
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
      <button class="dismiss-btn" onclick="dismissRightPanel()" title="Close">&times;</button>
      <button class="popout-btn" onclick="popoutPage('right')" title="Open in new window">&#x2197;</button>
      <div class="page-title" id="right-page-title"></div>
      <div class="page-path" id="right-page-path"></div>
      <div class="page-content" id="right-page-content"></div>
    </div>
  </div>

  <!-- FOOTER RESIZE HANDLE -->
  <div id="footer-resize" onmousedown="startFooterResize(event)"></div>
  <!-- FOOTER -->
  <div id="footer">
    <div style="flex:1;display:flex;flex-direction:column;gap:4px;min-width:0;height:100%;">
      <div id="narration-text">This is a knowledge graph inside the C2A2 Explorer (v1.0). The Community Context for AI Alignment (C2A2) project seeks to empower consensus-sized communities with AI acceleration tools, thus rendering a meaningful and measurable context for AI alignment with common community goals. This first instance brings together a range of thinkers &mdash; 15 or more &mdash; whose research touches up against, in one way or another, an emerging conscious realist paradigm for cross-disciplinary integration. In this knowledge graph, each node is a wiki file and each edge a link or shared reference. Filter by thinker or structure on the left, click on nodes or edges in the graph to pull up associated files, or ask a question below. User input will either filter the graph immediately (if a simple search query) or produce a meaningful LLM-driven response. Each user has a limited number of free semantic queries, with the option to continue using your own API key.</div>
      <div id="footer-search-row" style="display:flex;gap:4px;align-items:center;flex-wrap:wrap;">
        <div id="search-wrap" style="position:relative;flex:1;min-width:200px;">
          <input type="text" id="search-input" autocomplete="off" placeholder="Search, or type focus: to isolate links between groups" style="width:100%;background:#1a1a2a;border:1px solid #3a3a4a;color:#e0e0e0;padding:3px 8px;border-radius:4px;font-size:12px;" oninput="onSearchInput()" onkeydown="onSearchKey(event)" onblur="setTimeout(hideSuggest,150)">
          <div id="search-suggest" style="display:none;position:absolute;bottom:calc(100% + 4px);left:0;right:0;"></div>
        </div>
        <button onclick="runSearch()" style="background:#1a1a2a;border:1px solid #3a3a4a;color:#e0e0e0;padding:3px 8px;border-radius:4px;cursor:pointer;font-size:11px;">Search</button>
        <button onclick="document.getElementById('search-input').value='';runSearch();" style="background:#1a1a2a;border:1px solid #3a3a4a;color:#e0e0e0;padding:3px 8px;border-radius:4px;cursor:pointer;font-size:11px;">Clear</button>
        <label style="display:flex;align-items:center;gap:4px;font-size:11px;color:#bbb;cursor:pointer;"><input type="checkbox" id="search-ai-mode"> Ask AI</label>
        <label style="display:flex;align-items:center;gap:4px;font-size:11px;color:#bbb;cursor:pointer;" title="Only used when Ask AI is on"><input type="checkbox" id="search-external"> Allow wider search</label>
      </div>
    </div>
    <div class="footer-controls">
      <button id="btn-voice" onclick="VOICE.start()" title="Voice input — click to speak a query">&#127908;</button>
      <button id="btn-mute" onclick="toggleMute()" title="Audio on/off: speak Ask-AI answers aloud">&#128266;</button>
    </div>
  </div>
</div>

<!-- SETTINGS MODAL -->
<div id="settings-modal">
  <div id="settings-content">
    <h2>TTS Settings</h2>
    <label>Provider</label>
    <select id="tts-provider" onchange="applyFormToTTS()">
      <option value="browser">Browser (basic)</option>
      <option value="kokoro">Kokoro (neural, no API key)</option>
      <option value="openai">OpenAI (premium)</option>
    </select>
    <div id="tts-section-browser">
      <label>Browser Voice</label>
      <select id="tts-browser-voice" onchange="applyFormToTTS()"></select>
    </div>
    <div id="tts-section-kokoro" style="display:none">
      <label>Kokoro Voice</label>
      <select id="tts-kokoro-voice" onchange="applyFormToTTS()">
        <option value="af_heart">Heart (Female, American)</option>
        <option value="af_sky">Sky (Female, American)</option>
        <option value="af_bella">Bella (Female, American)</option>
        <option value="af_nicole">Nicole (Female, American)</option>
        <option value="bf_emma">Emma (Female, British)</option>
        <option value="bf_isabella">Isabella (Female, British)</option>
        <option value="am_adam">Adam (Male, American)</option>
        <option value="am_michael">Michael (Male, American)</option>
        <option value="bm_george">George (Male, British)</option>
        <option value="bm_lewis">Lewis (Male, British)</option>
      </select>
      <p style="font-size:11px;color:#888;margin:4px 0 0;">First use downloads ~83 MB model (cached in browser after that).</p>
    </div>
    <div id="tts-section-openai" style="display:none">
      <label>API Key (OpenAI)</label>
      <input type="password" id="tts-api-key" placeholder="sk-..." onchange="applyFormToTTS()">
      <label>OpenAI Voice</label>
      <select id="tts-openai-voice" onchange="applyFormToTTS()">
        <option value="alloy">Alloy</option>
        <option value="echo">Echo</option>
        <option value="fable">Fable</option>
        <option value="onyx">Onyx</option>
        <option value="nova">Nova</option>
        <option value="shimmer">Shimmer</option>
      </select>
    </div>
    <hr style="border:none;border-top:1px solid #2a2a3a;margin:16px 0 12px;">
    <h3 style="color:#ccc;font-size:14px;font-weight:600;margin:0 0 8px;">AI Query</h3>
    <label>Provider</label>
    <select id="ai-provider" onchange="applyAISettings()">
      <option value="broker">C2A2 broker (shared free tier)</option>
      <option value="groq">Groq — free tier (groq.com)</option>
      <option value="ollama">Ollama — local, no key (ollama.com)</option>
      <option value="openai-direct">OpenAI direct</option>
    </select>
    <div id="ai-key-row" style="display:none">
      <label id="ai-key-label">API Key</label>
      <input type="password" id="ai-api-key" placeholder="gsk_...">
    </div>
    <div id="ai-model-row" style="display:none">
      <label>Model</label>
      <input type="text" id="ai-model" placeholder="llama-3.3-70b-versatile">
    </div>
    <p id="ai-hint" style="font-size:11px;color:#888;margin:4px 0 0;">Shared free quota — falls back to local search when exhausted.</p>
    <div id="tts-error" class="error-text"></div>
    <div class="btn-row">
      <button class="primary" onclick="saveSettings()">Save</button>
      <button onclick="testTTS()">Test</button>
      <button onclick="closeSettings()">Cancel</button>
    </div>
  </div>
</div>

<script>
""" + c2a2_search_js + """
</script>

<script>
// ── DATA CONSTANTS ──
const NODES = """ + nodes_json + """;
const LINKS = """ + links_json + """;
// Decode integer-interned link source/target back to string IDs. The extractor
// emits indices into NODES (saves ~2.3 MB of JSON payload over filepath strings);
// d3.forceSimulation expects string IDs once .id() is configured, so we restore
// them here in a single pass before any code reads LINKS. Mutates LINKS in place.
for (var __li = 0; __li < LINKS.length; __li++) {
  var __l = LINKS[__li];
  if (typeof __l.source === 'number') __l.source = NODES[__l.source].id;
  if (typeof __l.target === 'number') __l.target = NODES[__l.target].id;
}
const FINDINGS = """ + findings_json + """;
const DECISIONS = """ + decisions_json + """;
const CROSS_CONNECTIONS = """ + cross_json + """;
const CHANGELOGS = """ + changelogs_json + """;
const COWORK_SUMMARIES = """ + cowork_json + """;
const TIMELINE = """ + timeline_json + """;
const COLORS = """ + colors_json + """;
const TRADITION_GROUPS = """ + tradition_groups_json + """;
const STRUCTURE_GROUPS = """ + structure_groups_json + """;
const TRADITION_CONCEPT = """ + tradition_concept_json + """;
var DATE_START = '""" + date_start + """';
var DATE_END = '""" + date_end + """';

// ── STATE ──
var showHoverNames = false;
var holdForces = false;
var edgesVisible = true;
var groupVisibility = {};
// Hoisted to module scope so applyEdgeFilters() (also module-scoped) can read
// the current cut-survivors. Was function-local inside rebuildGraph(), causing
// every Score-mode change and Edge-type checkbox to throw ReferenceError.
var activeLinks = [];
var activeNodes = [];
// Live d3 selection of the currently rendered (budget-joined) edge <line>s.
// Owned by applyEdgeFilters(); read by the simulation tick handler.
var linkSel = null;
var playSpeed = 1;
var isMuted = false;
var brightness = 1;
var IDLE_NARRATION = '';
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

// ── AGENT EDGE LAYERS (OpenStory) ──
// Agent edges carry a 'layer' field instead of a wikilink/mention/reference
// 'type', so they're exempt from the type/bridge cuts and gated solely by
// these per-layer toggles. Default OFF in the master Sociogram; the Agent
// Explorer preset (applyAgentSociogramPreset / #agents hash) turns them on.
var LAYER_COLOR = { substrate: '#7A6E9E', projected: '#5BC0BE', flow: '#E8954A' };
var showLayer   = { substrate: false, projected: false, flow: false };
// Substrate context: when on, wiki nodes that are TARGETS of substrate edges
// pass the group cut even if their group is unchecked. This is what lets the
// Agent Explorer preset show the substrate layer (agent→wiki) — without it,
// hiding the wiki groups hides every substrate edge's far endpoint, and
// H-Admin's dominant centrality (hundreds of substrate edges) is invisible.
var substrateContextOn = false;
var _substrateTargetIds = null;  // lazily built Set of wiki node ids
function isSubstrateTarget(id) {
  if (_substrateTargetIds === null) {
    _substrateTargetIds = {};
    LINKS.forEach(function(l) {
      if (l.layer === 'substrate') {
        var tid = typeof l.target === 'object' ? l.target.id : l.target;
        _substrateTargetIds[tid] = true;
      }
    });
  }
  return _substrateTargetIds[id] === true;
}
// True for any edge that belongs to an agent layer (gated by showLayer, not
// the type/bridge cuts). Single source of truth for the three call sites that
// decide edge admissibility (applyEdgeFilters filter, paint, rebuildGraph).
function edgePassesCuts(e) {
  if (e.layer) return showLayer[e.layer] !== false;
  var t = e.type || 'reference';
  var b = e.bridge || 'cross';
  return (showEdgeType[t] !== false) && (showEdgeBridge[b] !== false);
}

// ── CONTENT TAG CUTS (Pass G) ──
// Each entry default-OFF. When ALL are off → no tag cut applies (every file
// passes the section). When any is on → only files whose has_tags array
// contains at least one of the on-kinds pass the cut. OR-within-section,
// AND-composes with Tradition/Structure cuts.
var showTagKind = { finding: false, decision: false, cross: false, open: false };

// ── DATE THRESHOLD CUT (Pass G) ──
// dateThreshold === null → no cut. Otherwise: a YYYY-MM-DD string; only files
// with date >= threshold are admitted. Sourced from the toolbar slider; the
// slider is auto-populated with the corpus's distinct date range.
var dateThreshold = null;
var ALL_DATES = [];                            // populated at init from NODES

// ── ADAPTIVE EDGE DENSITY (Pass A) ──
// Visible edge count = top-N by score from cut-survivors, where N grows with
// zoom. Mode picks the score formula. Switching mode/zoom/cuts re-evaluates
// visibility without rerunning the force simulation — positions stay stable.
var scoreMode = 'balanced';                  // 'balanced' | 'connected' | 'cross-tradition' | 'editorial'
var BASE_EDGE_BUDGET = 2500;                 // edges visible at 1× zoom
var currentZoomScale = 1.0;                  // updated by the zoom handler
var _zoomRafPending = false;                 // rAF debouncer for zoom→re-render

function computeEdgeScore(e) {
  var deg = e.score_deg || 0;
  var t   = e.score_type || 1;
  var b   = e.score_bridge || 0;
  switch (scoreMode) {
    case 'connected':       return deg;
    case 'cross-tradition': return b * 5 + deg;
    case 'editorial':       return t * 5 + deg;
    case 'balanced':
    default:                return deg + t + b;
  }
}
function visibilityBudget() {
  // Logarithmic growth: each ×2 zoom roughly doubles budget, capped at 4× base.
  var growth = Math.max(1, Math.min(4, currentZoomScale));
  return Math.floor(BASE_EDGE_BUDGET * growth);
}
function setScoreMode(value) {
  scoreMode = value;
  applyEdgeFilters();
}
function toggleEdgeHelp(ev) {
  // Top-toolbar Score-mode help popover (explains adaptive density / score modes).
  if (ev) ev.stopPropagation();
  var pop = document.getElementById('edge-help-popover');
  if (!pop) return;
  pop.style.display = (pop.style.display === 'block') ? 'none' : 'block';
}
function toggleEdgesHelp(ev) {
  // Left-panel Edges-section help popover (explains type/bridge cuts).
  if (ev) ev.stopPropagation();
  var pop = document.getElementById('edges-help-popover');
  if (!pop) return;
  pop.style.display = (pop.style.display === 'block') ? 'none' : 'block';
}
// Click-outside-to-close for both edge popovers.
document.addEventListener('click', function(ev) {
  // Click-outside-to-close for every popover that exists at module-init time.
  var POPOVER_BUTTON_IDS = {
    'edge-help-popover':  'btn-edge-help',
    'edges-help-popover': 'btn-edges-help',
    'stats-help-popover': 'btn-stats-help',
    'tags-help-popover':  'btn-tags-help',
  };
  Object.keys(POPOVER_BUTTON_IDS).forEach(function(id) {
    var pop = document.getElementById(id);
    if (!pop || pop.style.display !== 'block') return;
    if (pop.contains(ev.target)) return;
    var btn = document.getElementById(POPOVER_BUTTON_IDS[id]);
    if (btn && btn.contains(ev.target)) return;
    pop.style.display = 'none';
  });
});

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
  // Wikilinks: support the piped [[target|alias]] form. Show the alias but
  // resolve on the TARGET path (openNodeByLabel matches a node whose id
  // contains it, e.g. target "traditions/levin/wiki" -> "traditions/levin/wiki.md").
  // Passing the whole raw "target|alias" string here is why piped links used to
  // go nowhere. data-target keeps the click value off the visible text.
  text = text.replace(/\\[\\[([^\\]]+)\\]\\]/g, function(m, inner) {
    var parts = inner.split('|');
    var target = parts[0].trim();
    var alias = (parts.length > 1 ? parts.slice(1).join('|') : parts[0]).trim();
    return '<span class="wikilink" data-target="' + target.replace(/"/g, '&quot;') + '" onclick="openNodeByLabel(this.dataset.target)">' + alias + '</span>';
  });
  text = text.replace(/`([^`]+)`/g, '<code>$1</code>');
  text = text.replace(/\\*\\*([^*]+)\\*\\*/g, '<strong>$1</strong>');
  text = text.replace(/\\*([^*]+)\\*/g, '<em>$1</em>');
  return text;
}

// ── RENDERING LIMITS ──
var MAX_NODES = 20000;
// Safety ceiling on edges fed to the FORCE SIMULATION only. The DOM holds just
// the budget-joined subset (applyEdgeFilters: 2,500 at 1× zoom, growing with
// zoom), and counts/"pass" figures always come from the uncapped activeLinks.
// If the sim set would exceed this ceiling, the slice keeps the top by initial
// Balanced score rather than alphabetic order — so degradation is graceful.
var MAX_SIM_EDGES = 30000;
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
var EXCLUDED_FROM_ALL = {'architecture/changelog': true, 'agent-activity': true};

function buildFilters() {
  var tradDiv = document.getElementById('tradition-filters');
  TRADITION_GROUPS.forEach(function(g) {
    var startOn = !EXCLUDED_FROM_ALL[g.key];
    groupVisibility[g.key] = startOn;
    tradDiv.innerHTML += '<div class="filter-item"><input type="checkbox" ' + (startOn ? 'checked' : '') + ' data-group="' + g.key + '" onchange="toggleGroup(\\'' + g.key + '\\', this.checked)"><span class="filter-dot" style="background:' + g.color + '"></span><span class="filter-label">' + g.label + '</span>' + (g.summary ? '<span class="sum-q" data-key="' + g.key + '" title="Show summary" onclick="showSummary(event,this)">?</span>' : '') + '</div>';
  });
  var structDiv = document.getElementById('structure-filters');
  STRUCTURE_GROUPS.forEach(function(g) {
    var startOn = !EXCLUDED_FROM_ALL[g.key];
    groupVisibility[g.key] = startOn;
    structDiv.innerHTML += '<div class="filter-item"><input type="checkbox" ' + (startOn ? 'checked' : '') + ' data-group="' + g.key + '" onchange="toggleGroup(\\'' + g.key + '\\', this.checked)"><span class="filter-dot" style="background:' + g.color + '"></span><span class="filter-label">' + g.label + '</span>' + (g.summary ? '<span class="sum-q" data-key="' + g.key + '" title="Show summary" onclick="showSummary(event,this)">?</span>' : '') + '</div>';
  });
}

// --- Tradition / group summary pop-ups (yellow '?' next to each thinker) ---
var GROUP_SUMMARIES = {};
function initSummaries() {
  TRADITION_GROUPS.concat(STRUCTURE_GROUPS).forEach(function(g) {
    if (g.summary) { GROUP_SUMMARIES[g.key] = { label: g.label, text: g.summary }; }
  });
  if (typeof TRADITION_CONCEPT === 'string' && TRADITION_CONCEPT) {
    GROUP_SUMMARIES['__tradition__'] = { label: 'Tradition (in C2A2)', text: TRADITION_CONCEPT };
  }
}
function showSummary(ev, el) {
  ev.stopPropagation();
  var data = GROUP_SUMMARIES[el.getAttribute('data-key')];
  if (!data) { return; }
  var pop = document.getElementById('sum-pop');
  pop.innerHTML = '';
  var h = document.createElement('h4'); h.textContent = data.label; pop.appendChild(h);
  data.text.split('\\n\\n').forEach(function(para) {
    if (!para.trim()) { return; }
    var p = document.createElement('p'); p.textContent = para.trim(); pop.appendChild(p);
  });
  pop.style.display = 'block';
  var r = el.getBoundingClientRect();
  var left = Math.min(r.right + 8, window.innerWidth - 400);
  var top = Math.min(r.top, window.innerHeight - pop.offsetHeight - 10);
  pop.style.left = Math.max(8, left) + 'px';
  pop.style.top = Math.max(8, top) + 'px';
}
function hideSummary() {
  var p = document.getElementById('sum-pop'); if (p) { p.style.display = 'none'; }
}
document.addEventListener('click', function(e) {
  var p = document.getElementById('sum-pop');
  if (p && p.style.display === 'block' && !p.contains(e.target) &&
      !(e.target.classList && e.target.classList.contains('sum-q')) &&
      !(e.target.classList && e.target.classList.contains('sum-q-head'))) { hideSummary(); }
});

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
      // Preserve, don't force off. "All" must not surprise-add these groups in
      // the master view, but it also must not yank the actor group out from
      // under the Agent Explorer (where it is deliberately on).
      b.checked = !!groupVisibility[key];
      if (b.checked) {
        nodeCount += NODES.filter(function(n) { return n.group === key; }).length;
      }
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
  refreshSimLinks();
}
function toggleEdgeType(t, checked) {
  showEdgeType[t] = checked;
  syncEdgesMaster();
  refreshSimLinks();
}
function toggleEdgeBridge(b, checked) {
  showEdgeBridge[b] = checked;
  syncEdgesMaster();
  refreshSimLinks();
}
function syncEdgesMaster() {
  var allOn =
    showEdgeType.wikilink && showEdgeType.mention && showEdgeType.reference &&
    showEdgeBridge.cross && showEdgeBridge.same;
  edgesVisible = allOn;
  var m = document.getElementById('chk-all-edges');
  if (m) m.checked = allOn;
}
function toggleLayer(layer, checked) {
  // Agent edge layers are independent of the wiki edges master / type / bridge
  // cuts. Like the wiki cuts, toggling re-derives the sim link set (force
  // implication) and re-joins the budgeted DOM subset.
  showLayer[layer] = checked;
  refreshSimLinks();
}
// Agent Explorer preset: isolate the runtime-actor sociogram. Unchecks every
// node group except 'agent-activity', turns on all three agent edge layers,
// and leaves the wiki type/bridge cuts as-is (irrelevant once wiki nodes are
// hidden). Invoked by the #agents URL hash (so the agents_tab iframe just sets
// src="wiki_narration.html#agents") and exposed on window for direct calls.
function applyAgentSociogramPreset() {
  Object.keys(groupVisibility).forEach(function(k) { groupVisibility[k] = (k === 'agent-activity'); });
  document.querySelectorAll('[data-group]').forEach(function(b) {
    b.checked = (b.dataset.group === 'agent-activity');
  });
  ['substrate','projected','flow'].forEach(function(L) {
    showLayer[L] = true;
    var cb = document.getElementById('chk-layer-' + L);
    if (cb) cb.checked = true;
  });
  // Substrate context ON: reveal the wiki files agents touch, so the substrate
  // layer (where most of the signal lives, incl. H-Admin's centrality) renders.
  substrateContextOn = true;
  var ctx = document.getElementById('chk-substrate-context');
  if (ctx) ctx.checked = true;
  // Suppress wiki↔wiki edge types: context nodes are endpoints, not an excuse
  // to re-flood the view with high-scoring wiki hub edges that would out-rank
  // the agent layers under the visibility budget. (Collection stays alive via
  // the anyAgentLayer gate in rebuildGraph.)
  ['wikilink','mention','reference'].forEach(function(t) {
    showEdgeType[t] = false;
    var cb = document.getElementById('chk-edge-' + t);
    if (cb) cb.checked = false;
  });
  syncEdgesMaster();
  if (typeof syncSectionCheckboxes === 'function') syncSectionCheckboxes();
  rebuildGraph();
}
function toggleSubstrateContext(checked) {
  substrateContextOn = checked;
  rebuildGraph();
}
window.applyAgentSociogramPreset = applyAgentSociogramPreset;

// ── SCOPE-AWARE DATASET TOTALS (status denominators) ──
// This file backs two views: the Sociogram (default, no hash) and the Agent
// Map, which iframes wiki_narration.html#agents and calls
// applyAgentSociogramPreset() to turn the runtime-actor 'agent-activity' layer
// on (and the wiki groups off). The #graph-status / #edge-status "total" must
// count only the layer the current view can address, or the readout strands the
// other layer in the denominator forever — the Sociogram could never reach
// N / N, because the 26 agent-activity nodes (and their ~2k layer edges) are
// never showable here. Scope is read from live state: agent-activity visibility
// is set ONLY by the preset (it is in EXCLUDED_FROM_ALL, has no checkbox), so it
// is a reliable Sociogram-vs-Agent-Map signal. In agent scope the totals are
// left unchanged (the agent layer is the subject of that view). The non-agent
// totals are static, so they are computed once and memoized. Note: 'agents' (the
// agent-definition files) is a normal shown group and is intentionally NOT
// excluded — only the runtime 'agent-activity' layer is.
function inAgentScope() { return !!groupVisibility['agent-activity']; }
var _nonAgentNodeTotal = null;
var _nonAgentEdgeTotal = null;
function nodeTotalForScope() {
  if (inAgentScope()) return NODES.length;
  if (_nonAgentNodeTotal === null) {
    _nonAgentNodeTotal = NODES.filter(function(n) { return n.group !== 'agent-activity'; }).length;
  }
  return _nonAgentNodeTotal;
}
function edgeTotalForScope() {
  if (inAgentScope()) return LINKS.length;
  if (_nonAgentEdgeTotal === null) {
    _nonAgentEdgeTotal = LINKS.filter(function(e) { return !e.layer; }).length;
  }
  return _nonAgentEdgeTotal;
}

// Physics safety cap (simulation only). Score-aware so degradation is
// graceful. Agent-layer edges (≤~2k, low log-weight scores) are exempt and
// always retained — otherwise they'd be silently out-scored by wiki hubs and
// vanish from the layout.
function capForSim(list) {
  if (list.length <= MAX_SIM_EDGES) return list;
  var agentEdges = list.filter(function(e) { return e.layer; });
  var wikiEdges  = list.filter(function(e) { return !e.layer; });
  wikiEdges.forEach(function(e) {
    e._initialScore = (e.score_deg || 0) + (e.score_type || 1) + (e.score_bridge || 0);
  });
  wikiEdges.sort(function(a, b) { return b._initialScore - a._initialScore; });
  var room = Math.max(0, MAX_SIM_EDGES - agentEdges.length);
  return agentEdges.concat(wikiEdges.slice(0, room));
}

// Called by every edge-cut toggle (type/bridge/layer/master). Re-derives the
// simulation's link set from the edges passing the NEW cuts and reheats, so
// toggling an edge family has a force implication — the layout physically
// relaxes or tightens — rather than being a purely visual change.
function refreshSimLinks() {
  if (simulation) {
    var lf = simulation.force('link');
    if (lf) lf.links(capForSim((activeLinks || []).filter(edgePassesCuts)));
    if (!holdForces) simulation.alpha(0.3).restart();
  }
  applyEdgeFilters();
}

function applyEdgeFilters() {
  // Budgeted DOM join. Visibility = (passes type-cut) AND (passes bridge-cut)
  // AND (in top-N by score), where N grows with zoom. Only those N edges exist
  // as <line> elements — there are no hidden lines, so toggles never pay the
  // cost of building tens of thousands of invisible DOM nodes. Score is
  // recomputed per active mode each call so a mode change re-ranks instantly
  // without touching the force simulation.
  var bucket = activeLinks || [];
  // Key includes layer/type so a wiki edge and an agent edge (or two different
  // layers) between the same node pair can't collide in the visible set.
  function _edgeKey(e) {
    var s = (e.source && e.source.id) ? e.source.id : e.source;
    var t = (e.target && e.target.id) ? e.target.id : e.target;
    return (e.layer || e.type || '') + '|' + s + '|' + t;
  }
  // Step 1: filter by cuts (type/bridge for wiki edges, layer for agent edges)
  var allowed = bucket.filter(edgePassesCuts);
  // Step 2: rank by current-mode score
  allowed.forEach(function(e) { e._renderScore = computeEdgeScore(e); });
  allowed.sort(function(a, b) { return b._renderScore - a._renderScore; });
  // Step 3: top-N where N = visibility budget (zoom-scaled)
  var budget = Math.min(visibilityBudget(), allowed.length);
  var visible = allowed.slice(0, budget);
  // Step 4: keyed join of exactly the visible subset. Endpoints were resolved
  // to node objects in rebuildGraph, so edges outside the simulation's link
  // set still draw correctly; positions are set here for the settled-sim case
  // (the tick handler keeps them fresh while the sim runs).
  if (linkG) {
    linkSel = linkG.selectAll('line')
      .data(visible, _edgeKey)
      .join(
        function(enter) {
          return enter.append('line')
            .attr('class', 'link-line')
            .on('mouseover', function(event, d) {
              if (!showHoverNames) return;
              var sn = nodeById[d.source.id || d.source];
              var tn = nodeById[d.target.id || d.target];
              if (sn && tn) {
                var metaColor, metaText, arrow;
                if (d.layer) {
                  var LAYER_LABEL = { substrate: 'co-ref substrate', projected: 'projected co-ref', flow: 'write→read flow' };
                  metaColor = LAYER_COLOR[d.layer] || '#888';
                  metaText = (LAYER_LABEL[d.layer] || d.layer) + (d.weight ? ' · weight ' + d.weight : '');
                  arrow = (d.layer === 'flow') ? ' &#8594; ' : ' &#8596; ';  // flow is directed
                } else {
                  var typeLabel = (d.type || 'reference').replace('_',' ');
                  var bridgeLabel = d.bridge === 'same' ? 'within category' : 'crosses categories';
                  var ref = d.reference ? ' · ' + escapeHtml(d.reference) : '';
                  metaColor = EDGE_COLOR[d.type || 'reference'] || '#888';
                  metaText = escapeHtml(typeLabel) + ' · ' + escapeHtml(bridgeLabel) + ref;
                  arrow = ' &#8596; ';
                }
                showTooltip(event,
                  '<span class="tt-title" onclick="openNodeByLabel(\\'' + escapeAttr(sn.label) + '\\')">' + escapeHtml(sn.label) + '</span>' + arrow +
                  '<span class="tt-title" onclick="openNodeByLabel(\\'' + escapeAttr(tn.label) + '\\')">' + escapeHtml(tn.label) + '</span>' +
                  '<div class="tt-dir" style="margin-top:3px;color:' + metaColor + ';">' + metaText + '</div>'
                );
              }
            })
            .on('mouseout', hideTooltip)
            .on('click', function(event, d) {
              // Edge click: collapse the Select-Files panel so the file viewer
              // below it is immediately visible with the source node's content.
              event.stopPropagation();
              collapseFilterPanel();
              var sn = nodeById[d.source.id || d.source];
              var tn = nodeById[d.target.id || d.target];
              if (sn) showLeftPage(sn);
              if (tn) showRightPanel(tn);
            });
        },
        function(update) { return update; },
        function(exit) { return exit.remove(); }
      );
    /* Color encodes edge type (wikilink/mention/reference); dash encodes whether
       the edge crosses content categories (solid) or stays within one (dashed).
       Agent-layer edges colour by layer; wiki edges keep the type colour.
       Set on the merged selection so brightness changes apply to re-entrants. */
    linkSel
      .attr('stroke', function(d) { return d.layer ? (LAYER_COLOR[d.layer] || '#999') : (EDGE_COLOR[d.type || 'reference'] || '#777'); })
      .attr('stroke-width', function(d) { return d.layer ? 0.9 : 0.6; })
      .attr('stroke-dasharray', function(d) { return (!d.layer && d.bridge === 'same') ? '3,3' : null; })
      .attr('opacity', Math.min(0.5 * brightness, 1))
      .attr('x1', function(d) { return d.source.x; })
      .attr('y1', function(d) { return d.source.y; })
      .attr('x2', function(d) { return d.target.x; })
      .attr('y2', function(d) { return d.target.y; });
  }
  // Step 5: status indicator + dynamic banner counts (Pass G)
  // Three-part readout: shown (top-N rendered, the ONLY edges in the DOM) /
  // passing all active cuts (uncapped) / total (whole dataset, incl. agents).
  var statusEl = document.getElementById('edge-status');
  if (statusEl) {
    statusEl.textContent = budget + ' shown / ' + allowed.length + ' pass / ' + edgeTotalForScope() + ' total edges';
    statusEl.title = 'Edges — shown (top-scored that fit the zoom budget; nothing else is rendered) / passing all active cuts / total addressable in this view';
  }
  updateBannerCounts();
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

// ── CONTENT TAG CUTS (Pass G) — handlers + node-passes-tag-cut helper ──
function toggleAllTags(checked) {
  ['finding','decision','cross','open'].forEach(function(k) {
    showTagKind[k] = checked;
    var cb = document.getElementById('chk-tag-' + k);
    if (cb) cb.checked = checked;
  });
  rebuildGraph();
}
function toggleTagKind(kind, checked) {
  showTagKind[kind] = checked;
  // Sync section master
  var anyOn = ['finding','decision','cross','open'].some(function(k) { return showTagKind[k]; });
  var allOn = ['finding','decision','cross','open'].every(function(k) { return showTagKind[k]; });
  var master = document.getElementById('chk-all-tags');
  if (master) {
    master.checked = allOn;
    master.indeterminate = anyOn && !allOn;
  }
  rebuildGraph();
}
function nodePassesTagCut(node) {
  // Default behaviour when no tag is checked: section imposes no cut.
  var anyOn = showTagKind.finding || showTagKind.decision || showTagKind.cross || showTagKind.open;
  if (!anyOn) return true;
  var tags = node.has_tags || [];
  for (var i = 0; i < tags.length; i++) {
    if (showTagKind[tags[i]]) return true;
  }
  return false;
}

// ── DATE THRESHOLD (Pass G) ──
function setDateThreshold(idx) {
  idx = parseInt(idx, 10);
  if (!ALL_DATES.length || idx <= 0) {
    dateThreshold = null;
    var lbl0 = document.getElementById('date-slider-label');
    if (lbl0) lbl0.textContent = 'all dates';
  } else {
    dateThreshold = ALL_DATES[Math.min(idx, ALL_DATES.length - 1)];
    var lbl = document.getElementById('date-slider-label');
    if (lbl) lbl.textContent = '≥ ' + dateThreshold;
  }
  rebuildGraph();
}
function nodePassesDateCut(node) {
  if (!dateThreshold) return true;
  // Actor nodes are cumulative telemetry, not single-dated events — they carry
  // no date, so without this exemption any threshold instantly hides all of
  // them (and every agent edge with them).
  if (node.group === 'agent-activity') return true;
  var d = node.date || '';
  return d && d >= dateThreshold;
}

// ── BANNER COUNT UPDATER (Pass G) ──
// Recomputes visible-vs-total counts for files / findings / decisions /
// crosses / opens. Visible = referenced by a visible node.
function updateBannerCounts() {
  if (!activeNodes) return;
  // Files
  var fCur = activeNodes.length;
  var fTot = NODES.length;
  // Distinct ID kinds visible in the active set
  var visFinding = new Set(), visDecision = new Set(), visCross = new Set(), visOpen = new Set();
  activeNodes.forEach(function(n) {
    var refs = n.references || [];
    for (var i = 0; i < refs.length; i++) {
      var r = refs[i];
      if (r.indexOf('FINDING-') === 0) visFinding.add(r);
      else if (r.indexOf('DECISION-') === 0) visDecision.add(r);
      else if (r.indexOf('CROSS-') === 0) visCross.add(r);
      else if (r.indexOf('OPEN-') === 0) visOpen.add(r);
    }
  });
  // Totals (whole corpus)
  var totFinding = new Set(), totDecision = new Set(), totCross = new Set(), totOpen = new Set();
  NODES.forEach(function(n) {
    var refs = n.references || [];
    for (var i = 0; i < refs.length; i++) {
      var r = refs[i];
      if (r.indexOf('FINDING-') === 0) totFinding.add(r);
      else if (r.indexOf('DECISION-') === 0) totDecision.add(r);
      else if (r.indexOf('CROSS-') === 0) totCross.add(r);
      else if (r.indexOf('OPEN-') === 0) totOpen.add(r);
    }
  });
  function setStat(id, cur, tot) {
    var el = document.getElementById(id);
    if (!el) return;
    var c = el.querySelector('.stat-cur'); if (c) c.textContent = cur;
    var t = el.querySelector('.stat-tot'); if (t) t.textContent = tot;
  }
  setStat('stat-files',     fCur,             fTot);
  setStat('stat-findings',  visFinding.size,  totFinding.size);
  setStat('stat-decisions', visDecision.size, totDecision.size);
  setStat('stat-crosses',   visCross.size,    totCross.size);
  setStat('stat-opens',     visOpen.size,     totOpen.size);
}

// ── BANNER + TAGS HELP POPOVER TOGGLES (Pass G) ──
function toggleStatsHelp(ev) {
  if (ev) ev.stopPropagation();
  var pop = document.getElementById('stats-help-popover');
  if (!pop) return;
  pop.style.display = (pop.style.display === 'block') ? 'none' : 'block';
}
function toggleTagsHelp(ev) {
  if (ev) ev.stopPropagation();
  var pop = document.getElementById('tags-help-popover');
  if (!pop) return;
  pop.style.display = (pop.style.display === 'block') ? 'none' : 'block';
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

// Track currently-displayed nodes in each panel so the pop-out button has
// the data it needs to open a standalone reading window.
var currentLeftNode = null;
var currentRightNode = null;

function showRightPanel(node) {
  currentRightNode = node;
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
  currentLeftNode = node;
  var viewer = document.getElementById('left-page-viewer');
  document.getElementById('left-page-title').textContent = node.label || node.id;
  document.getElementById('left-page-path').textContent = node.id;
  document.getElementById('left-page-content').innerHTML = renderMarkdown(node.content || '');
  viewer.style.display = 'block';
}

// Pop-out: open the current panel's file in a separate browser window for
// distraction-free, full-width reading. Especially useful for long Curriculum
// Tools content (Summa commentaries up to 10K chars). Window is self-contained
// (inline CSS, no cross-origin), closes via its own button or browser chrome.
function popoutPage(side) {
  var node = (side === 'right') ? currentRightNode : currentLeftNode;
  if (!node) return;
  var w = window.open('', '_blank', 'width=900,height=720');
  if (!w) {
    alert('Popup was blocked by the browser. Allow popups for this site to use the pop-out window.');
    return;
  }
  var title = escapeHtml(node.label || node.id || 'Untitled');
  var path  = escapeHtml(node.id || '');
  var body  = renderMarkdown(node.content || '');
  var html = '<!DOCTYPE html><html><head>' +
    '<meta charset="utf-8">' +
    '<title>' + title + '</title>' +
    '<style>' +
      'body{background:#0a0a0f;color:#e0e0e0;font-family:"Segoe UI",system-ui,sans-serif;max-width:760px;margin:0 auto;padding:28px 32px 80px;line-height:1.6;}' +
      'h1{color:#FFD700;font-size:22px;margin:0 0 4px;}' +
      'h2{color:#ddd;font-size:18px;margin:18px 0 6px;}' +
      'h3{color:#ccc;font-size:15px;margin:14px 0 4px;}' +
      '.path{color:#666;font-size:12px;margin-bottom:18px;padding-bottom:12px;border-bottom:1px solid #2a2a3a;font-family:monospace;word-break:break-all;}' +
      '.close{position:fixed;top:12px;right:16px;background:#1a1a2a;color:#ccc;border:1px solid #3a3a4a;border-radius:4px;padding:4px 12px;cursor:pointer;font-size:13px;z-index:1000;}' +
      '.close:hover{background:#2a2a3a;color:#fff;}' +
      'strong{color:#fff;}em{color:#aaa;font-style:italic;}' +
      'code{background:#1a1a2a;padding:1px 5px;border-radius:3px;font-family:monospace;font-size:13px;}' +
      'pre{background:#1a1a2a;padding:10px 14px;border-radius:4px;overflow-x:auto;}' +
      'pre code{padding:0;background:none;}' +
      'a,.wikilink{color:#4A90D9;}' +
      'ul,ol{padding-left:22px;}li{margin:3px 0;}' +
      'p{margin:8px 0;}hr{border:none;border-top:1px solid #2a2a3a;margin:18px 0;}' +
    '</style></head><body>' +
    '<button class="close" onclick="window.close()">&times; Close</button>' +
    '<h1>' + title + '</h1>' +
    '<div class="path">' + path + '</div>' +
    body +
    '</body></html>';
  w.document.open();
  w.document.write(html);
  w.document.close();
}

function dismissLeftPage() {
  document.getElementById('left-page-viewer').style.display = 'none';
  // Restore filters when the file viewer is dismissed.
  expandFilterPanel();
}

function toggleFilterPanel() {
  var body = document.getElementById('filter-body');
  var arrow = document.getElementById('sf-arrow');
  body.classList.toggle('collapsed');
  arrow.classList.toggle('collapsed');
}

// Programmatic collapse/expand. Edge click → collapse so the file viewer
// pane below it is immediately visible. Node click or graph-background click
// → expand so the color key / cut checkboxes return automatically.
function collapseFilterPanel() {
  var body = document.getElementById('filter-body');
  var arrow = document.getElementById('sf-arrow');
  if (body && !body.classList.contains('collapsed')) body.classList.add('collapsed');
  if (arrow && !arrow.classList.contains('collapsed')) arrow.classList.add('collapsed');
}
function expandFilterPanel() {
  var body = document.getElementById('filter-body');
  var arrow = document.getElementById('sf-arrow');
  if (body) body.classList.remove('collapsed');
  if (arrow) arrow.classList.remove('collapsed');
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
    // Track current zoom so the adaptive-density renderer can grow the visible
    // edge budget as the user zooms in. Debounced via rAF below.
    currentZoomScale = event.transform.k;
    if (!_zoomRafPending) {
      _zoomRafPending = true;
      requestAnimationFrame(function() {
        _zoomRafPending = false;
        applyEdgeFilters();
      });
    }
  });
  svg.call(zoomBehavior);

  // Background click on the SVG (not bubbled from a node or edge — those use
  // event.stopPropagation()) restores the Select-Files filter panel. Pairs
  // with the edge-click collapse: clicking an edge hides filters to show the
  // file viewer; clicking anywhere else on the graph brings filters back.
  svg.on('click.expandfilters', function(event) {
    expandFilterPanel();
  });

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

  // Filter to visible nodes only — assign to the module-scoped variable so
  // applyEdgeFilters() can see it. Was `var activeNodes = ...` (function-local).
  // Pass G — node admission requires passing every active cut: group, content
  // tag (default-no-cut), and date threshold (default-no-cut).
  activeNodes = NODES.filter(function(n) {
    if (!groupVisibility[n.group]) {
      // Substrate-context override: admit hidden-group wiki nodes that agents
      // actually touch, so substrate edges have a visible far endpoint. Gated
      // on the actor group being visible — context exists to serve agent
      // edges, so "None" (or unchecking Agent activity) blanks it too.
      if (!(substrateContextOn && groupVisibility['agent-activity'] && isSubstrateTarget(n.id))) return false;
    }
    if (!nodePassesTagCut(n)) return false;
    if (!nodePassesDateCut(n)) return false;
    return true;
  });
  var activeIds = {};
  activeNodes.forEach(function(n) { activeIds[n.id] = true; });

  // Filter edges — activeLinks holds the FULL cut-surviving edge set, uncapped.
  // It is the honest "pass" pool: applyEdgeFilters() counts it and joins only
  // the budgeted top-N into the DOM, so no hidden <line> elements ever exist.
  // A separate, capped simLinks set feeds the force layout only (physics cost).
  activeLinks = [];
  var simLinks = [];
  // Collect when wiki edges are on OR any agent layer is on. edgesVisible is
  // the wiki-edges master; previously it also gated agent-layer collection, so
  // unchecking all wiki edge types silently killed the agent sociogram too.
  var anyAgentLayer = showLayer.substrate || showLayer.projected || showLayer.flow;
  if (edgesVisible || anyAgentLayer) {
    LINKS.forEach(function(l) {
      var sid = typeof l.source === 'object' ? l.source.id : l.source;
      var tid = typeof l.target === 'object' ? l.target.id : l.target;
      if (activeIds[sid] && activeIds[tid]) {
        // Resolve endpoints to node objects up front so any budgeted edge can
        // be drawn even when it isn't part of the force-simulation link set.
        l.source = nodeById[sid];
        l.target = nodeById[tid];
        activeLinks.push(l);
      }
    });
    // The force layout follows the active edge cuts: only cut-passing edges
    // exert link force, so toggling an edge family physically loosens or
    // tightens the layout (capForSim applies the physics safety cap).
    simLinks = capForSim(activeLinks.filter(edgePassesCuts));
  }

  // Update status — nodes only. All edge counts live in #edge-status, written
  // by applyEdgeFilters(); the old "edges in view" here counted DOM-loaded
  // (capped) edges, contradicting the budgeted "shown" readout.
  var statusEl = document.getElementById('graph-status');
  if (statusEl) statusEl.textContent = activeNodes.length + ' / ' + nodeTotalForScope() + ' nodes';

  // Rebuild SVG elements — clear and recreate
  linkG.selectAll('*').remove();
  nodeG.selectAll('*').remove();

  var container = document.getElementById('graph-container');
  var width = container.clientWidth;
  var height = container.clientHeight;

  // Edge <line> elements are created by applyEdgeFilters() (budgeted DOM join),
  // invoked at the end of rebuildGraph once the simulation exists.

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
      // Node click: ensure filters are expanded again — the right-side panel
      // is the one being updated, so the color key / cuts return.
      event.stopPropagation();
      expandFilterPanel();
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
      .force('link', d3.forceLink(simLinks).id(function(d) { return d.id; }).distance(60).strength(0.15))
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
        // linkSel is the live budget-joined selection owned by applyEdgeFilters.
        if (linkSel) {
          linkSel.attr('x1', function(d) { return d.source.x; })
                 .attr('y1', function(d) { return d.source.y; })
                 .attr('x2', function(d) { return d.target.x; })
                 .attr('y2', function(d) { return d.target.y; });
        }
        node.attr('cx', function(d) { return d.x; })
            .attr('cy', function(d) { return d.y; });
      });
    if (holdForces) simulation.stop();
  }

  // Apply adaptive-density edge visibility once the DOM is in place. This is
  // the first render; subsequent calls happen on zoom / mode / cut changes.
  applyEdgeFilters();

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
  var paradigm = '';
  var summary = '';
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
function setNarrationText(text) {
  document.getElementById('narration-text').textContent = text;
}

// ── TIMELINE NARRATION (History/Recent/Latest) ──
// ── SEARCH ──
// ── RELATIONAL FOCUS ENGINE (navigation increment 1, 2026-05-29) ──
// Deterministic graph-state navigation. A "focus:" query isolates the node set
// computed by edge traversal: entity-group nodes linked to target-group nodes
// (and the target nodes they link to), heavy-fading everything else (and its
// links) to 5% opacity in place. No reflow, no LLM, fully reversible via the
// empty-query reset in runSearch(). Computes over the FULL link set (not the
// old 30-candidate cap, not visible-only).
// Syntax:  focus: <entityTokens> ~ <groupTokens>     e.g.  focus: levin ~ summa
//   left of '~'  = entity tokens, resolved to tradition group keys
//   right of '~' = structure-group tokens used as group keys
//   relation fixed to "linked", action fixed to "isolate" in this increment.
var LABEL_TO_KEY = null;
function labelToKey() {
  // Friendly-label -> group-key lookup (lazy, built once). Lets resolveGroupKeys
  // accept the human spellings the typeahead inserts ("Levin", "Arkani-Hamed",
  // "Summa") and also fixes hand-typed hyphenated names whose key drops the
  // hyphen ("Arkani-Hamed" -> traditions/arkanihamed, "McGilchrist" -> .../mcgilchrist).
  if (LABEL_TO_KEY) return LABEL_TO_KEY;
  LABEL_TO_KEY = {};
  function add(arr) {
    if (!arr) return;
    arr.forEach(function(g) { if (g && g.label) LABEL_TO_KEY[g.label.toLowerCase()] = g.key; });
  }
  if (typeof TRADITION_GROUPS !== 'undefined') add(TRADITION_GROUPS);
  if (typeof STRUCTURE_GROUPS !== 'undefined') add(STRUCTURE_GROUPS);
  return LABEL_TO_KEY;
}
function resolveGroupKeys(tokens) {
  // Map each whitespace token to a valid group key present in groupVisibility.
  // Exact key wins; else 'traditions/<token>'; else friendly label; else first
  // key containing token.
  var keys = Object.keys(groupVisibility);
  var labels = labelToKey();
  var out = [];
  tokens.forEach(function(tok) {
    tok = String(tok || '').trim().toLowerCase();
    if (!tok) return;
    if (groupVisibility.hasOwnProperty(tok)) { out.push(tok); return; }
    var trad = 'traditions/' + tok;
    if (groupVisibility.hasOwnProperty(trad)) { out.push(trad); return; }
    if (labels.hasOwnProperty(tok) && groupVisibility.hasOwnProperty(labels[tok])) { out.push(labels[tok]); return; }
    for (var i = 0; i < keys.length; i++) {
      if (keys[i].toLowerCase().indexOf(tok) !== -1) { out.push(keys[i]); return; }
    }
  });
  return out;
}
function linkEndpointId(end) {
  // Post-simulation, d3 swaps link source/target to node objects; pre-init they
  // are string ids (restored at load). Normalize to the string id either way.
  return (end && typeof end === 'object') ? end.id : end;
}
function runFocus(rawAfterPrefix) {
  var sides = String(rawAfterPrefix || '').split('~');
  if (sides.length < 2) {
    setNarrationText('Focus syntax: focus: <entity> ~ <group>   e.g.  focus: levin ~ summa');
    return;
  }
  var entityKeys = resolveGroupKeys(sides[0].split(/\\s+/));
  var groupKeys  = resolveGroupKeys(sides[1].split(/\\s+/));
  if (!entityKeys.length || !groupKeys.length) {
    setNarrationText('Focus: could not resolve entity or group. Use traditions/<name> (e.g. levin) and a structure group (e.g. summa, master, architecture).');
    return;
  }
  var A = {}, B = {};
  for (var i = 0; i < NODES.length; i++) {
    var g = NODES[i].group;
    if (entityKeys.indexOf(g) !== -1) A[NODES[i].id] = true;
    if (groupKeys.indexOf(g)  !== -1) B[NODES[i].id] = true;
  }
  var focus = {};
  for (var k = 0; k < LINKS.length; k++) {
    var sid = linkEndpointId(LINKS[k].source);
    var tid = linkEndpointId(LINKS[k].target);
    if (A[sid] && B[tid]) { focus[sid] = true; focus[tid] = true; }
    if (A[tid] && B[sid]) { focus[tid] = true; focus[sid] = true; }
  }
  var focusCount = Object.keys(focus).length;
  d3.selectAll('.node-circle')
    .interrupt()
    .attr('opacity', function(d) {
      if (!groupVisibility[d.group]) return 0;
      return focus[d.id] ? brightness : brightness * 0.05;
    });
  d3.selectAll('.link-line')
    .interrupt()
    .attr('opacity', function(d) {
      var ls = linkEndpointId(d.source), lt = linkEndpointId(d.target);
      return (focus[ls] && focus[lt]) ? Math.min(0.5 * brightness, 1) : (brightness * 0.05);
    });
  var lbl = entityKeys.join(', ') + ' ~ ' + groupKeys.join(', ');
  if (!focusCount) {
    setNarrationText('Focus "' + lbl + '": no linked pairs found (computed over the full graph). Check the group keys, or that both groups are enabled at left.');
  } else {
    setNarrationText('Focus "' + lbl + '": isolated ' + focusCount + ' nodes linked across the two sets. Clear the search box to restore.');
  }
}

// ── BARE-GUESS RELATIONAL NAVIGATION (navigation increment 1.6, 2026-05-29) ──
// Lets the user drive the focus engine WITHOUT the "focus:" prefix, by typing
// plain group names. Deterministic, no LLM — a strict parser in front of the
// existing runFocus machinery. STRICT resolution (group keys / directory leaves
// / friendly labels only, plus singular<->plural tolerance) and NO substring
// fallback, so ordinary free-text search is untouched unless the WHOLE query
// resolves to group names. One resolved group isolates it; two or more isolate
// the nodes that link across them. Tag-cut vocabulary (e.g. "PRS", finding/
// decision/cross/open) is intentionally NOT handled here — that lives in the
// separate content-tag-cut subsystem and is deferred to a later increment.
var BARE_INDEX = null;
function bareGuessIndex() {
  // Built once. Two passes so an exact spelling always beats a plural variant of
  // some other group, regardless of object-key iteration order. Only LIVE groups
  // (present in groupVisibility) are registered.
  if (BARE_INDEX) return BARE_INDEX;
  BARE_INDEX = {};
  var exact = [];  // [spelling, key]
  Object.keys(groupVisibility).forEach(function(key) {
    exact.push([key.toLowerCase(), key]);
    var leaf = (key.indexOf('/') !== -1) ? key.split('/').pop() : key;
    exact.push([leaf.toLowerCase(), key]);
  });
  function addLabels(arr) {
    if (!arr) return;
    arr.forEach(function(g) { if (g && g.label) exact.push([g.label.toLowerCase(), g.key]); });
  }
  if (typeof TRADITION_GROUPS !== 'undefined') addLabels(TRADITION_GROUPS);
  if (typeof STRUCTURE_GROUPS !== 'undefined') addLabels(STRUCTURE_GROUPS);
  // Pass 1: exact spellings (live groups only). First registration wins.
  exact.forEach(function(p) {
    if (groupVisibility.hasOwnProperty(p[1]) && !BARE_INDEX.hasOwnProperty(p[0])) BARE_INDEX[p[0]] = p[1];
  });
  // Pass 2: singular/plural variants, never overwriting an exact spelling.
  exact.forEach(function(p) {
    if (!groupVisibility.hasOwnProperty(p[1])) return;
    var s = p[0];
    var alt = (s.charAt(s.length - 1) === 's') ? s.slice(0, -1) : s + 's';
    if (alt && !BARE_INDEX.hasOwnProperty(alt)) BARE_INDEX[alt] = p[1];
  });
  return BARE_INDEX;
}
function strictResolveToken(tok) {
  tok = String(tok || '').trim().toLowerCase();
  if (!tok) return null;
  var idx = bareGuessIndex();
  return idx.hasOwnProperty(tok) ? idx[tok] : null;
}
function parseBareGuess(raw) {
  // Tokenize on quotes / commas / whitespace (NOT hyphens yet — hyphen trap:
  // "Arkani-Hamed" is one label). Resolve each whole token first; only if a token
  // fails do we split it on internal hyphens and resolve the parts ("Levin-Friston").
  // If ANY piece fails to resolve, return null so runSearch falls through to text
  // search. Returns a deduped list of group keys, or null.
  var pieces = String(raw).replace(/["']/g, ' ').split(/[\\s,]+/);
  var keys = [];
  function push(k) { if (k && keys.indexOf(k) === -1) keys.push(k); }
  for (var i = 0; i < pieces.length; i++) {
    var p = pieces[i];
    if (!p) continue;
    var k = strictResolveToken(p);
    if (k) { push(k); continue; }
    if (p.indexOf('-') !== -1) {
      var subs = p.split('-'), subKeys = [], ok = true;
      for (var j = 0; j < subs.length; j++) {
        if (!subs[j]) continue;
        var sk = strictResolveToken(subs[j]);
        if (sk) subKeys.push(sk); else { ok = false; break; }
      }
      if (ok && subKeys.length) { subKeys.forEach(push); continue; }
    }
    return null;  // a piece is not a group name → not a bare-guess command
  }
  return keys.length ? keys : null;
}
var NODE_GROUP = null;
function nodeGroupMap() {
  if (NODE_GROUP) return NODE_GROUP;
  NODE_GROUP = {};
  for (var i = 0; i < NODES.length; i++) NODE_GROUP[NODES[i].id] = NODES[i].group;
  return NODE_GROUP;
}
function isolateGroups(keys) {
  // Single-group (or unioned) isolate: named-group nodes bright, everything else
  // faded in place. Links bright only when both endpoints are in the named set.
  var inSet = {};
  keys.forEach(function(k) { inSet[k] = true; });
  var grp = nodeGroupMap();
  var count = 0;
  for (var i = 0; i < NODES.length; i++) {
    if (inSet[NODES[i].group] && groupVisibility[NODES[i].group]) count++;
  }
  d3.selectAll('.node-circle')
    .interrupt()
    .attr('opacity', function(d) {
      if (!groupVisibility[d.group]) return 0;
      return inSet[d.group] ? brightness : brightness * 0.05;
    });
  d3.selectAll('.link-line')
    .interrupt()
    .attr('opacity', function(d) {
      var s = linkEndpointId(d.source), t = linkEndpointId(d.target);
      return (inSet[grp[s]] && inSet[grp[t]]) ? Math.min(0.5 * brightness, 1) : (brightness * 0.05);
    });
  var lbl = keys.join(', ');
  if (!count) {
    setNarrationText('Isolate "' + lbl + '": that group has no visible nodes (is it enabled at left?). Clear the search box to restore.');
  } else {
    setNarrationText('Isolate "' + lbl + '": ' + count + ' nodes shown, the rest faded. Clear the search box to restore.');
  }
}
function linkGroups(keys) {
  // N-group generalization of runFocus: isolate nodes that sit in one named group
  // AND have at least one link to a node in a DIFFERENT named group. For exactly
  // two groups this equals the focus: A~B behavior; it also handles 3+ uniformly.
  var inSet = {};
  keys.forEach(function(k) { inSet[k] = true; });
  var grp = nodeGroupMap();
  var focus = {};
  for (var k = 0; k < LINKS.length; k++) {
    var s = linkEndpointId(LINKS[k].source), t = linkEndpointId(LINKS[k].target);
    var gs = grp[s], gt = grp[t];
    if (inSet[gs] && inSet[gt] && gs !== gt) { focus[s] = true; focus[t] = true; }
  }
  var focusCount = Object.keys(focus).length;
  d3.selectAll('.node-circle')
    .interrupt()
    .attr('opacity', function(d) {
      if (!groupVisibility[d.group]) return 0;
      return focus[d.id] ? brightness : brightness * 0.05;
    });
  d3.selectAll('.link-line')
    .interrupt()
    .attr('opacity', function(d) {
      var s = linkEndpointId(d.source), t = linkEndpointId(d.target);
      return (focus[s] && focus[t]) ? Math.min(0.5 * brightness, 1) : (brightness * 0.05);
    });
  var lbl = keys.join(' ↔ ');
  if (!focusCount) {
    setNarrationText('Link "' + lbl + '": no direct links found across these groups (computed over the full graph). Are all of them enabled at left?');
  } else {
    setNarrationText('Link "' + lbl + '": isolated ' + focusCount + ' nodes connecting the groups. Clear the search box to restore.');
  }
}

// ── FRIENDLY-LABEL TYPEAHEAD (navigation increment 1.5, 2026-05-29) ──
// Discoverability layer over the focus: grammar so no category memorization is
// needed. As the user types a "focus:" query, suggests real entity (tradition)
// labels left of '~' and group (structure) labels right of '~', drawn from
// TRADITION_GROUPS / STRUCTURE_GROUPS. Picking inserts the friendly label
// (resolved by resolveGroupKeys' label map) and advances to the next slot;
// completing the group slot auto-runs the focus. Deterministic, no LLM.
var SUGGEST_ITEMS = [];   // current suggestion list [{key,label,color}]
var SUGGEST_ACTIVE = -1;  // highlighted row index; -1 = none

function parseFocusSlot(raw) {
  // Which slot is the user editing? entity (before '~') or group (after it).
  var s = String(raw || '');
  if (s.toLowerCase().indexOf('focus:') !== 0) return { mode: 'none', token: '' };
  var after = s.slice(s.indexOf(':') + 1);
  var tildeAt = after.indexOf('~');
  if (tildeAt === -1) return { mode: 'entity', token: after.trim() };
  return { mode: 'group', token: after.slice(tildeAt + 1).trim() };
}

function onSearchInput() {
  var el = document.getElementById('search-input');
  var slot = parseFocusSlot(el.value);
  if (slot.mode === 'none') { hideSuggest(); return; }
  var source = (slot.mode === 'entity') ? TRADITION_GROUPS : STRUCTURE_GROUPS;
  var tok = slot.token.toLowerCase();
  var items = source.filter(function(g) {
    return !tok || g.label.toLowerCase().indexOf(tok) !== -1 || g.key.toLowerCase().indexOf(tok) !== -1;
  });
  showSuggest(items, slot.mode);
}

function showSuggest(items, mode) {
  SUGGEST_ITEMS = items;
  SUGGEST_ACTIVE = -1;
  var box = document.getElementById('search-suggest');
  if (!box) return;
  if (!items.length) { hideSuggest(); return; }
  var head = (mode === 'entity') ? 'Entity (tradition) - who' : 'Group (structure) - where';
  var html = '<div class="sg-head">' + head + '</div>';
  items.forEach(function(g, i) {
    html += '<div class="sg-row" data-i="' + i + '" onmousedown="acceptSuggest(' + i + ')">'
          + '<span class="filter-dot" style="background:' + g.color + '"></span>'
          + '<span>' + g.label + '</span></div>';
  });
  box.innerHTML = html;
  box.style.display = 'block';
}

function hideSuggest() {
  var box = document.getElementById('search-suggest');
  if (box) { box.style.display = 'none'; box.innerHTML = ''; }
  SUGGEST_ITEMS = [];
  SUGGEST_ACTIVE = -1;
}

function highlightSuggest() {
  var rows = document.querySelectorAll('#search-suggest .sg-row');
  for (var i = 0; i < rows.length; i++) {
    rows[i].className = 'sg-row' + (i === SUGGEST_ACTIVE ? ' active' : '');
  }
}

function acceptSuggest(i) {
  var g = SUGGEST_ITEMS[i];
  if (!g) return;
  var el = document.getElementById('search-input');
  var raw = el.value;
  var head = raw.slice(0, raw.indexOf(':') + 1);   // "focus:"
  var after = raw.slice(raw.indexOf(':') + 1);
  var tildeAt = after.indexOf('~');
  if (tildeAt === -1) {
    // entity slot: set it and advance to the group slot
    el.value = head + ' ' + g.label + ' ~ ';
    el.focus();
    onSearchInput();
  } else {
    // group slot: complete the query and run it
    var entitySide = after.slice(0, tildeAt).trim();
    el.value = head + ' ' + entitySide + ' ~ ' + g.label;
    hideSuggest();
    runSearch();
  }
}

function onSearchKey(e) {
  var box = document.getElementById('search-suggest');
  var open = box && box.style.display === 'block' && SUGGEST_ITEMS.length;
  if (open && (e.key === 'ArrowDown' || e.key === 'ArrowUp')) {
    e.preventDefault();
    var n = SUGGEST_ITEMS.length;
    SUGGEST_ACTIVE = (e.key === 'ArrowDown') ? (SUGGEST_ACTIVE + 1) % n : (SUGGEST_ACTIVE - 1 + n) % n;
    highlightSuggest();
    return;
  }
  if (e.key === 'Enter') {
    if (open && SUGGEST_ACTIVE >= 0) { e.preventDefault(); acceptSuggest(SUGGEST_ACTIVE); return; }
    hideSuggest();
    runSearch();
    return;
  }
  if (e.key === 'Escape') { hideSuggest(); }
}

function runSearch() {
  var raw = document.getElementById('search-input').value.trim();
  if (!raw) {
    setNarrationText(IDLE_NARRATION);
    // Reset node + link highlights (restores a prior focus: fade too).
    d3.selectAll('.node-circle').attr('opacity', brightness);
    d3.selectAll('.link-line').attr('opacity', Math.min(0.5 * brightness, 1));
    return;
  }
  // Deterministic relational focus command (navigation increment 1). Explicit
  // prefix never collides with substring search, and overrides AI mode.
  if (raw.toLowerCase().indexOf('focus:') === 0) {
    runFocus(raw.slice(raw.indexOf(':') + 1));
    return;
  }
  // When "Ask AI" is on, route through the shared C2A2 broker pipeline
  // (wiki/lib/c2a2-search.js, attached as window.C2A2Search). The external-
  // search checkbox toggles 'enrich' vs 'web_enrich' inside the module.
  var aiBox = document.getElementById('search-ai-mode');
  if (aiBox && aiBox.checked) {
    runSearchAI(raw);
    return;
  }
  // Bare-guess relational navigation (increment 1.6, no "focus:" prefix, no LLM).
  // Strict parse: only fires when EVERY token is a group name. One group isolates
  // it; two or more isolate the nodes linking across them. A non-group query (any
  // unresolved token) returns null and falls through to the text search below.
  var bareKeys = parseBareGuess(raw);
  if (bareKeys) {
    if (bareKeys.length === 1) isolateGroups(bareKeys);
    else linkGroups(bareKeys);
    return;
  }
  var query = raw.toLowerCase();
  // Search across node content, titles, and IDs
  var matches = NODES.filter(function(n) {
    if (!groupVisibility[n.group]) return false;
    var haystack = (n.label + ' ' + n.id + ' ' + (n.content || '')).toLowerCase();
    return haystack.indexOf(query) !== -1;
  });

  // Highlight matching nodes
  d3.selectAll('.node-circle')
    .interrupt()
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
      return f.id + ': ' + f.type;
    }).join('. '));
  }
  if (matchedCrosses.length > 0) {
    parts.push('Cross-connections: ' + matchedCrosses.slice(0, 3).map(function(c) {
      return c.question;
    }).join('. '));
  }
  if (matches.length > 0 && matches.length <= 10) {
    parts.push('Files: ' + matches.map(function(n) { return n.label; }).join(', '));
  } else if (matches.length > 10) {
    parts.push('Top files: ' + matches.slice(0, 6).map(function(n) { return n.label; }).join(', ') + '...');
  }

  setNarrationText(parts.join(' '));
}

// ── CURRENT VIEW STATE ──
// Reads the live D3 graph to describe which nodes are currently highlighted
// vs faded, and which traditions are active. Returns a short text block for
// injection into the AI prompt, or null when no meaningful focus is active
// (i.e. all nodes are at full brightness = no search has been run yet).
function getCurrentViewState() {
  var searchTerm = (document.getElementById('search-input').value || '').trim();
  var threshold = brightness * 0.4;
  var highlighted = [];
  d3.selectAll('.node-circle').each(function(d) {
    var op = parseFloat(d3.select(this).attr('opacity'));
    if (!isNaN(op) && op >= threshold) highlighted.push(d);
  });
  // If all (or nearly all) nodes are lit, no focus is active — don't inject noise
  if (!highlighted.length || highlighted.length > NODES.length * 0.85) return null;

  var parts = ['Graph currently shows ' + highlighted.length + ' highlighted node(s)' +
    (searchTerm ? ' (search: "' + searchTerm + '")' : '') + '.'];

  if (highlighted.length <= 20) {
    parts.push('Highlighted: ' + highlighted.map(function(d) {
      return '"' + d.label + '" [' + (String(d.group || '').split('/').pop()) + ']';
    }).join(', ') + '.');
  } else {
    parts.push('Sample: ' + highlighted.slice(0, 10).map(function(d) {
      return '"' + d.label + '" [' + (String(d.group || '').split('/').pop()) + ']';
    }).join(', ') + ' … and ' + (highlighted.length - 10) + ' more.');
  }

  var activeTraditions = Object.keys(groupVisibility).filter(function(k) {
    return k.indexOf('traditions/') === 0 && groupVisibility[k];
  }).map(function(k) { return k.split('/').pop(); });
  if (activeTraditions.length && activeTraditions.length < 14) {
    parts.push('Visible traditions: ' + activeTraditions.join(', ') + '.');
  }
  return parts.join(' ');
}

// runSearchAI: AI-routed search via the shared C2A2 broker pipeline.
// Selects the top-30 visible nodes by simple term overlap as candidates, sends
// them to the broker (action 'enrich' or 'web_enrich'), and renders the model's
// chosen ids by dimming the rest. The cap-hit / Tavily-down fallback lives
// inside window.C2A2Search.enrich (see wiki/lib/c2a2-search.js).
var C2A2_SOC_SYSTEM_DATASET = 'You are a retrieval assistant for the C2A2 wiki sociogram. Each candidate line is a vault file: id | label | group | excerpt. The group field is the graph cluster key (e.g. "traditions/levin", "summa", "architecture"). A CURRENT_VIEW block may appear in the user message describing which nodes are currently highlighted in the graph — use this to ground answers about what the user is looking at ("what am I seeing?", "why are these connected?", etc.). Pick the most relevant ids and write a brief grounded answer using ONLY the candidates. For navigational queries ("show me X", "find X", "highlight X", "go to X"), also include a "cmd" field with a graph command using the group leaf names from the candidates: a single leaf name isolates that cluster (e.g. "levin"), space-separated leaf names show cross-links ("levin friston"), and "focus: <tradition> ~ <structure>" highlights how a thinker connects to a structural type (e.g. "focus: friston ~ summa"). Omit "cmd" entirely for purely informational queries. Reply with ONE JSON object and nothing else: {"ids":["<id>", ... up to 12 most relevant], "answer":"2-3 sentence summary grounded in the candidates", "cmd":"<optional navigation command>"}.';
var C2A2_SOC_SYSTEM_WEB = 'You are a retrieval assistant for the C2A2 wiki sociogram. Each candidate line is a vault file: id | label | group | excerpt. The group field is the graph cluster key (e.g. "traditions/levin", "summa", "architecture"). A WEB_CONTEXT block of up to 5 web snippets will be appended. A CURRENT_VIEW block may appear in the user message describing which nodes are currently highlighted in the graph — use this to ground answers about what the user is looking at. Pick the most relevant candidate ids and write a brief answer; when you draw on a web snippet, cite it [1], [2], etc. Pick ids only from the candidates. For navigational queries ("show me X", "find X", "highlight X", "go to X"), also include a "cmd" field with a graph command using the group leaf names from the candidates: a single leaf name isolates that cluster (e.g. "levin"), space-separated leaf names show cross-links ("levin friston"), and "focus: <tradition> ~ <structure>" highlights how a thinker connects to a structural type. Omit "cmd" entirely for purely informational queries. Reply with ONE JSON object: {"ids":["<id>", ... up to 12 most relevant], "answer":"2-4 sentence summary with bracket citations where applicable", "cmd":"<optional navigation command>"}.';

// applyAIResult: parse an AI JSON response, highlight the chosen ids on the
// graph, and run any nav command. Returns the parsed object on success, or
// null if the response could not be parsed (caller stops; a narration error
// is already shown). Shared by the broker and direct-provider paths so the
// highlight/cmd logic has a single source of truth.
function applyAIResult(content, parseFailMsg) {
  var m = String(content || '').match(/\\{[\\s\\S]*\\}/);
  if (!m) { setNarrationText(parseFailMsg || 'AI returned a response that could not be parsed. Uncheck "Ask AI" to use local search.'); return null; }
  var parsed;
  try { parsed = JSON.parse(m[0]); } catch (e) { setNarrationText('AI response JSON parse failed.'); return null; }
  var pickedIds = Array.isArray(parsed.ids) ? parsed.ids : [];
  var pickedSet = {};
  for (var k = 0; k < pickedIds.length; k++) pickedSet[pickedIds[k]] = true;
  d3.selectAll('.node-circle').interrupt().attr('opacity', function(d) {
    if (!groupVisibility[d.group]) return 0;
    return pickedSet[d.id] ? brightness : brightness * 0.1;
  });
  // If the AI returned a navigation command, execute it (overrides id-based highlight above)
  if (parsed.cmd) { navigateByCmd(parsed.cmd); }
  return parsed;
}

function runSearchAI(rawQuery) {
  if (!window.C2A2Search || typeof window.C2A2Search.enrich !== 'function') {
    setNarrationText('Search module not loaded.');
    return;
  }
  var query = String(rawQuery || '').trim();
  if (!query) return;
  var extBox = document.getElementById('search-external');
  var useWeb = !!(extBox && extBox.checked);

  // Pre-rank visible nodes by term overlap; trim to 30 for the prompt budget.
  var qTerms = query.toLowerCase().split(/\\s+/).filter(Boolean);
  var scored = [];
  for (var i = 0; i < NODES.length; i++) {
    var n = NODES[i];
    if (!groupVisibility[n.group]) continue;
    var hay = (n.label + ' ' + n.id + ' ' + (n.content || '')).toLowerCase();
    var s = 0;
    for (var j = 0; j < qTerms.length; j++) { if (hay.indexOf(qTerms[j]) !== -1) s++; }
    if (s > 0) scored.push({n: n, s: s});
  }
  scored.sort(function(a, b) { return b.s - a.s; });
  scored = scored.slice(0, 30);
  if (!scored.length) {
    setNarrationText('No visible nodes match "' + query + '". Try a different query or expand the filters at left.');
    return;
  }
  var summary = scored.map(function(x) {
    var n = x.n;
    var snip = String(n.content || '').replace(/\\s+/g, ' ').slice(0, 200);
    return n.id + ' | ' + n.label + ' | ' + n.group + ' | ' + snip;
  }).join('\\n');
  var viewCtx = getCurrentViewState();
  var userBlock = 'Query: ' + query +
    (viewCtx ? '\\n\\nCURRENT_VIEW:\\n' + viewCtx : '') +
    '\\n\\nCandidates:\\n' + summary;

  // ── DIRECT PROVIDER PATH (Groq / Ollama / OpenAI direct) ──
  if (AI.provider !== 'broker') {
    var system = useWeb ? C2A2_SOC_SYSTEM_WEB : C2A2_SOC_SYSTEM_DATASET;
    setNarrationText('Asking ' + AI.provider + ' (' + AI.getModel() + ')...');
    AI.callDirect(system, userBlock).then(function(content) {
      var parsed = applyAIResult(content, 'AI response could not be parsed — check the model supports JSON output.');
      if (!parsed) return;
      var answer = parsed.answer || '(no answer text)';
      setNarrationText('Ask "' + query + '" [' + AI.provider + ']: ' + answer);
      TTS.speak(answer);
    }).catch(function(err) {
      var msg = (err && err.message) ? err.message : String(err);
      setNarrationText('Direct AI error (' + msg + '). Check Settings → AI Query provider / key.');
    });
    return;
  }

  setNarrationText('Asking C2A2 (' + (useWeb ? 'database + web' : 'database') + ') ...');

  window.C2A2Search.enrich({
    useWeb: useWeb,
    dataset: {system: C2A2_SOC_SYSTEM_DATASET, user: userBlock},
    web: useWeb ? {system: C2A2_SOC_SYSTEM_WEB, user: userBlock} : null,
  }).then(function(res) {
    var content = (res.payload && typeof res.payload.text === 'string') ? res.payload.text : '';
    var parsed = applyAIResult(content);
    if (!parsed) return;

    var modeLabel = res.mode === 'database-plus-web-cited' ? ' [web + database]'
      : res.mode === 'database-only-after-cap' ? ' [database -- web cap reached]'
      : res.mode === 'external-search-unavailable' ? ' [database -- web unavailable]'
      : ' [database]';
    var warning = res.warning ? (' ' + res.warning) : '';
    // Name the model that answered, when the broker echoes it in the payload.
    // (cc-broker must include payload.model for this to show; absent that it
    // stays blank rather than echoing a redundant transport label.)
    var modelLabel = (res.payload && res.payload.model) ? (' (model: ' + res.payload.model + ')') : '';
    var sourcesLine = '';
    if (Array.isArray(res.payload && res.payload.sources) && res.payload.sources.length) {
      sourcesLine = ' Sources: ' + res.payload.sources.map(function(s, i) {
        return '[' + (i + 1) + '] ' + (s.title || s.url || '');
      }).join(' | ');
    }
    var answer = parsed.answer || '(no answer text)';
    setNarrationText('Ask "' + query + '"' + modeLabel + modelLabel + ':' + warning + ' ' + answer + sourcesLine);
    TTS.speak(answer);
  }).catch(function(err) {
    var code = (err && err.message) || 'unknown';
    var isLimit = (code === 'free-limit' || code === 'rate-limited');
    if (isLimit) {
      // Quota exhausted — silently fall back to local text search and uncheck AI mode
      var aiBox = document.getElementById('search-ai-mode');
      if (aiBox) aiBox.checked = false;
      document.getElementById('search-input').value = query;
      setNarrationText('Free-tier AI limit reached — switching to local search for "' + query + '". Re-enable Ask AI later or add your own key in Settings.');
      runSearch();
    } else {
      setNarrationText('AI request failed (' + code + '). Uncheck "Ask AI" to fall back to local search.');
    }
  });
}

function toggleMute() {
  isMuted = !isMuted;
  document.getElementById('btn-mute').innerHTML = isMuted ? '&#128263;' : '&#128266;';
  if (isMuted) TTS.stop();
}

// ── TTS ──
var TTS = {
  enabled: true,
  provider: (function() { try { return localStorage.getItem('tts_provider') || 'browser'; } catch(e) { return 'browser'; } })(),
  apiKey: (function() { try { return localStorage.getItem('tts_api_key') || ''; } catch(e) { return ''; } })(),
  browserVoice: null,
  openaiVoice: (function() { try { return localStorage.getItem('tts_openai_voice') || 'alloy'; } catch(e) { return 'alloy'; } })(),
  kokoroVoice: (function() { try { return localStorage.getItem('tts_kokoro_voice') || 'af_heart'; } catch(e) { return 'af_heart'; } })(),
  kokoroInstance: null,
  kokoroLoading: false,
  cache: {},
  audioEl: null,
  utterance: null,
  _kokoroSrc: null,
  _kokoroCtx: null,

  speak: function(text) {
    if (isMuted) return;
    this.stop();
    if (this.provider === 'browser') {
      this.speakBrowser(text);
    } else if (this.provider === 'kokoro') {
      this.speakKokoro(text);
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

  speakKokoro: function(text) {
    var self = this;
    if (this.kokoroInstance) {
      this._kokoroGenerate(text);
      return;
    }
    if (this.kokoroLoading) return;
    this.kokoroLoading = true;
    // WebGPU is 5-10x faster than WASM and avoids "page unresponsive" dialogs,
    // but requires a secure context (https:// or localhost). Detect at runtime.
    var kokoroDevice = (typeof navigator !== 'undefined' && navigator.gpu) ? 'webgpu' : 'wasm';
    var narEl = document.getElementById('narration-text');
    narEl.textContent = 'Loading Kokoro neural TTS [' + kokoroDevice + '] (~83 MB, cached after first load)...';
    import('https://cdn.jsdelivr.net/npm/kokoro-js@1/+esm')
      .then(function(m) {
        return m.KokoroTTS.from_pretrained('onnx-community/Kokoro-82M-v1.0-ONNX', {
          dtype: 'q8',
          device: kokoroDevice,
          progress_callback: function(info) {
            if (info.status === 'progress' || info.status === 'download') {
              var pct = info.progress ? Math.round(info.progress) : 0;
              var fname = info.file ? info.file.split('/').pop() : '';
              narEl.textContent = 'Kokoro: loading ' + fname + (pct ? ' ' + pct + '%' : '...');
            }
          }
        });
      })
      .then(function(instance) {
        self.kokoroInstance = instance;
        self.kokoroLoading = false;
        narEl.textContent = 'Kokoro model ready.';
        self._kokoroGenerate(text);
      })
      .catch(function(e) {
        self.kokoroLoading = false;
        narEl.textContent = 'Kokoro failed to load (' + (e && e.message ? e.message : e) + '). Falling back to browser voice.';
        self.speakBrowser(text);
      });
  },

  _kokoroGenerate: function(text) {
    var self = this;
    this.kokoroInstance.generate(text, { voice: this.kokoroVoice })
      .then(function(result) {
        var AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (!AudioCtx) { self.speakBrowser(text); return; }
        var ctx = new AudioCtx();
        var samples = result.audio;
        var buf = ctx.createBuffer(1, samples.length, result.sampling_rate);
        buf.copyToChannel(samples, 0);
        var src = ctx.createBufferSource();
        src.buffer = buf;
        src.playbackRate.value = playSpeed;
        src.connect(ctx.destination);
        src.start();
        self._kokoroSrc = src;
        self._kokoroCtx = ctx;
        src.onended = function() {
          try { ctx.close(); } catch(e) {}
          self._kokoroSrc = null;
          self._kokoroCtx = null;
        };
      })
      .catch(function(e) {
        document.getElementById('narration-text').textContent = 'Kokoro generation error: ' + (e && e.message ? e.message : e);
        self.speakBrowser(text);
      });
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
    if (this._kokoroSrc) { try { this._kokoroSrc.stop(); } catch(e) {} this._kokoroSrc = null; }
    if (this._kokoroCtx) { try { this._kokoroCtx.close(); } catch(e) {} this._kokoroCtx = null; }
  }
};

// ── NAVIGATION COMMAND ENGINE ──
// Executes a graph navigation command string — the same vocabulary the search
// box understands — and mirrors the command in the search box so the user can
// see what fired. Called by runSearchAI (when the AI returns a "cmd" field)
// and by VOICE._route (for locally-resolved navigational voice queries).
function navigateByCmd(cmd) {
  var c = String(cmd || '').trim();
  if (!c) return;
  // Note: do NOT overwrite the search box here — when called from runSearchAI
  // the box already shows the user's original query; when called from VOICE._route
  // the box was already set to the stripped query before this call.
  if (c.toLowerCase().indexOf('focus:') === 0) {
    runFocus(c.slice(c.indexOf(':') + 1));
    return;
  }
  var bareKeys = parseBareGuess(c);
  if (bareKeys) {
    if (bareKeys.length === 1) isolateGroups(bareKeys);
    else linkGroups(bareKeys);
    return;
  }
  // Fallback: run as text search via the non-AI path (avoids re-entering runSearchAI)
  var aiBox = document.getElementById('search-ai-mode');
  var prev = aiBox ? aiBox.checked : false;
  if (aiBox) aiBox.checked = false;
  runSearch();
  if (aiBox) aiBox.checked = prev;
}

// ── NAVIGATION PREFIX STRIPPING ──
// Detects whether a voice query is navigational (starts with "show me",
// "find", "go to", etc.) and strips the prefix, returning the bare target.
// Returns null if the query is not navigational (caller should treat it
// as informational and route to AI).
var NAV_PREFIXES = [
  'show me ', 'take me to ', 'go to ', 'navigate to ',
  'highlight ', 'zoom to ', 'zoom in on ', 'look at ',
  'find ', 'open ', 'display ', 'bring up ', 'pull up '
];
function stripNavPrefix(text) {
  var t = String(text || '').trim();
  var tl = t.toLowerCase();
  for (var i = 0; i < NAV_PREFIXES.length; i++) {
    if (tl.indexOf(NAV_PREFIXES[i]) === 0) {
      return t.slice(NAV_PREFIXES[i].length).trim();
    }
  }
  return null;
}

// ── VOICE INPUT (Web Speech API) ──
// Click btn-voice to start listening; click again to cancel. On result:
//   • navigational query ("show me X") → stripNavPrefix → local graph command
//     if resolvable, else AI call (which will return a cmd field)
//   • informational query ("what is X?") → straight to runSearchAI
// Requires Chrome/Edge (file:// OK with mic permission granted).
var VOICE = {
  recognition: null,
  active: false,

  start: function() {
    var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SR) {
      setNarrationText('Voice input requires Chrome or Edge. (SpeechRecognition not found)');
      return;
    }
    if (this.active) { this.stop(); return; }
    var self = this;
    var rec = new SR();
    rec.lang = 'en-US';
    rec.interimResults = false;
    rec.maxAlternatives = 1;

    rec.onstart = function() {
      self.active = true;
      document.getElementById('btn-voice').innerHTML = '&#128308;';
      setNarrationText('Listening…');
    };
    rec.onresult = function(e) {
      var transcript = e.results[0][0].transcript.trim();
      setNarrationText('Heard: “' + transcript + '”');
      self._route(transcript);
    };
    rec.onend = function() {
      self.active = false;
      document.getElementById('btn-voice').innerHTML = '&#127908;';
    };
    rec.onerror = function(e) {
      self.active = false;
      document.getElementById('btn-voice').innerHTML = '&#127908;';
      var msg = e.error === 'not-allowed'
        ? 'Microphone permission denied. Allow mic access and try again.'
        : 'Voice error: ' + e.error + '.';
      setNarrationText(msg);
    };

    this.recognition = rec;
    rec.start();
  },

  stop: function() {
    if (this.recognition) { try { this.recognition.stop(); } catch(e) {} }
    this.active = false;
    var btn = document.getElementById('btn-voice');
    if (btn) btn.innerHTML = '&#127908;';
  },

  _route: function(text) {
    var stripped = stripNavPrefix(text);
    var isNav = (stripped !== null);
    var query = isNav ? stripped : text;
    if (!query) return;

    // Mirror the interpreted query in the search box
    document.getElementById('search-input').value = query;

    // Navigational: try local resolution first (instant, no API needed)
    if (isNav) {
      if (query.toLowerCase().indexOf('focus:') === 0) {
        runFocus(query.slice(query.indexOf(':') + 1));
        TTS.speak('Showing ' + query.slice(query.indexOf(':') + 1).trim() + '.');
        return;
      }
      var bareKeys = parseBareGuess(query);
      if (bareKeys) {
        if (bareKeys.length === 1) isolateGroups(bareKeys);
        else linkGroups(bareKeys);
        TTS.speak('Showing ' + query + '.');
        return;
      }
    }

    // Complex or informational query: route through AI only if Ask AI is on,
    // otherwise fall back to local text search (respects the free-tier quota).
    var aiBox = document.getElementById('search-ai-mode');
    if (aiBox && aiBox.checked) {
      runSearchAI(query);
    } else {
      // Local search: still useful for finding nodes by name without AI
      runSearch();
    }
  }
};

// ── AI QUERY PROVIDER ──
var AI_DEFAULTS = {
  'broker':        { key: false, model: '',                         hint: 'Shared free quota — falls back to local search when exhausted.' },
  'groq':          { key: true,  model: 'llama-3.3-70b-versatile',  hint: 'Free at console.groq.com — no credit card needed. ~14 400 req/day.' },
  'ollama':        { key: false, model: 'llama3.2',                 hint: 'No key needed. Run: ollama serve  then  ollama pull llama3.2' },
  'openai-direct': { key: true,  model: 'gpt-4o-mini',             hint: 'Pay-as-you-go. Key stored in session memory only (clears on tab close).' }
};
var AI_ENDPOINTS = {
  'groq':          'https://api.groq.com/openai/v1/chat/completions',
  'ollama':        'http://localhost:11434/v1/chat/completions',
  'openai-direct': 'https://api.openai.com/v1/chat/completions'
};
var AI = {
  provider: (function() { try { return localStorage.getItem('ai_provider') || 'broker'; } catch(e) { return 'broker'; } })(),
  apiKey:   (function() { try { return sessionStorage.getItem('ai_api_key') || ''; } catch(e) { return ''; } })(),
  model:    (function() { try { return localStorage.getItem('ai_model') || ''; } catch(e) { return ''; } })(),

  getModel: function() {
    return this.model || (AI_DEFAULTS[this.provider] || {}).model || '';
  },

  callDirect: function(systemPrompt, userMessage) {
    var self = this;
    var endpoint = AI_ENDPOINTS[this.provider];
    if (!endpoint) return Promise.reject(new Error('No endpoint configured for provider: ' + this.provider));
    var headers = {'Content-Type': 'application/json'};
    if (this.provider !== 'ollama' && this.apiKey) {
      headers['Authorization'] = 'Bearer ' + this.apiKey;
    }
    return fetch(endpoint, {
      method: 'POST',
      headers: headers,
      body: JSON.stringify({
        model: self.getModel(),
        messages: [
          {role: 'system', content: systemPrompt},
          {role: 'user',   content: userMessage}
        ],
        temperature: 0.1,
        max_tokens: 600
      })
    }).then(function(r) {
      if (!r.ok) {
        return r.json().then(function(e) {
          var msg = (e.error && (e.error.message || e.error.code)) || ('HTTP ' + r.status);
          throw new Error(msg);
        }).catch(function(inner) {
          if (inner instanceof Error && inner.message.indexOf('HTTP') === -1) throw inner;
          throw new Error('HTTP ' + r.status);
        });
      }
      return r.json();
    }).then(function(data) {
      if (data.error) throw new Error(data.error.message || JSON.stringify(data.error));
      var content = data.choices && data.choices[0] && data.choices[0].message && data.choices[0].message.content;
      if (!content) throw new Error('Empty response from model');
      return content;
    });
  }
};

function applyAISettings() {
  var p = document.getElementById('ai-provider').value;
  var def = AI_DEFAULTS[p] || AI_DEFAULTS['broker'];
  // Show/hide key and model rows
  document.getElementById('ai-key-row').style.display = def.key ? '' : 'none';
  document.getElementById('ai-model-row').style.display = (p === 'broker') ? 'none' : '';
  // Update key label and placeholder
  var keyLabel = document.getElementById('ai-key-label');
  var keyInput = document.getElementById('ai-api-key');
  if (p === 'groq') { keyLabel.textContent = 'Groq API Key'; keyInput.placeholder = 'gsk_...'; }
  else { keyLabel.textContent = 'OpenAI API Key'; keyInput.placeholder = 'sk-...'; }
  // Set default model when switching providers (if field is empty or held the old default)
  var modelEl = document.getElementById('ai-model');
  var prevDef = (AI_DEFAULTS[AI.provider] || {}).model || '';
  if (!modelEl.value || modelEl.value === prevDef) { modelEl.value = def.model; }
  // Update hint
  document.getElementById('ai-hint').textContent = def.hint;
  // Sync AI object
  AI.provider = p;
  AI.apiKey   = keyInput.value;
  AI.model    = modelEl.value;
  // Persist (key to sessionStorage only for security; provider/model to localStorage)
  try {
    localStorage.setItem('ai_provider', AI.provider);
    localStorage.setItem('ai_model', AI.model);
    if (AI.apiKey) sessionStorage.setItem('ai_api_key', AI.apiKey);
  } catch(e) {}
}

function applyFormToTTS() {
  TTS.provider = document.getElementById('tts-provider').value;
  TTS.apiKey = document.getElementById('tts-api-key').value;
  var bvSel = document.getElementById('tts-browser-voice');
  if (bvSel.selectedIndex >= 0 && window.speechSynthesis) {
    var voices = window.speechSynthesis.getVoices();
    TTS.browserVoice = voices[bvSel.selectedIndex] || null;
  }
  TTS.openaiVoice = document.getElementById('tts-openai-voice').value;
  TTS.kokoroVoice = document.getElementById('tts-kokoro-voice').value;
  TTS.enabled = true;
  // Show/hide provider-specific sections
  var p = TTS.provider;
  document.getElementById('tts-section-browser').style.display = (p === 'browser') ? '' : 'none';
  document.getElementById('tts-section-kokoro').style.display = (p === 'kokoro') ? '' : 'none';
  document.getElementById('tts-section-openai').style.display = (p === 'openai') ? '' : 'none';
  // Persist settings
  try {
    localStorage.setItem('tts_provider', TTS.provider);
    localStorage.setItem('tts_api_key', TTS.apiKey);
    localStorage.setItem('tts_openai_voice', TTS.openaiVoice);
    localStorage.setItem('tts_kokoro_voice', TTS.kokoroVoice);
  } catch(e) {}
}

// ── SETTINGS MODAL ──
function openSettings() {
  // Sync form from current TTS state before showing
  document.getElementById('tts-provider').value = TTS.provider;
  document.getElementById('tts-kokoro-voice').value = TTS.kokoroVoice;
  document.getElementById('tts-openai-voice').value = TTS.openaiVoice;
  document.getElementById('tts-api-key').value = TTS.apiKey;
  // Apply show/hide for the correct provider section
  var p = TTS.provider;
  document.getElementById('tts-section-browser').style.display = (p === 'browser') ? '' : 'none';
  document.getElementById('tts-section-kokoro').style.display = (p === 'kokoro') ? '' : 'none';
  document.getElementById('tts-section-openai').style.display = (p === 'openai') ? '' : 'none';
  // Sync AI query settings
  document.getElementById('ai-provider').value = AI.provider;
  document.getElementById('ai-api-key').value = AI.apiKey;
  document.getElementById('ai-model').value = AI.model || (AI_DEFAULTS[AI.provider] || {}).model || '';
  applyAISettings();
  document.getElementById('settings-modal').classList.add('visible');
  populateVoices();
}

function closeSettings() {
  document.getElementById('settings-modal').classList.remove('visible');
}

function saveSettings() {
  applyFormToTTS();
  applyAISettings();
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
  var _nt0 = document.getElementById('narration-text');
  IDLE_NARRATION = _nt0 ? _nt0.textContent : '';
  buildFilters();
  initSummaries();
  // Pass G — populate the date slider from NODES' distinct date set.
  var dateSet = new Set();
  NODES.forEach(function(n) { if (n.date) dateSet.add(n.date); });
  ALL_DATES = Array.from(dateSet).sort();
  var slider = document.getElementById('date-slider');
  if (slider) {
    slider.min = 0;
    slider.max = ALL_DATES.length;   // index N = "latest" (= showing only newest day)
    slider.value = 0;                // default: no threshold
  }
  initGraph();
  updateBannerCounts();
  // Agent Explorer entry point: wiki_narration.html#agents auto-applies the
  // runtime-actor preset (used by the agents_tab iframe). Master view (no hash)
  // is unchanged. Run after initGraph so groupVisibility/checkboxes exist.
  if (window.location.hash === '#agents') {
    applyAgentSociogramPreset();
  }
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
        print("Usage: python generate_visualization.py <input.json> <output.html> [agent_node_edges.json]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    agent_data_path = sys.argv[3] if len(sys.argv) > 3 else None

    data = load_json(input_path)
    agent_data = None
    if agent_data_path:
        # Fail loud: a supplied path that doesn't exist is an error, not a
        # silent skip (Rule 12).
        if not os.path.exists(agent_data_path):
            print("ERROR: agent data file not found: " + agent_data_path)
            sys.exit(1)
        agent_data = load_json(agent_data_path)
    nodes, links = build_graph_data(data, agent_data)
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
