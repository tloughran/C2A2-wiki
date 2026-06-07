#!/usr/bin/env python3
"""
Generate community_explorer.html — a self-contained D3.js v7 force-directed graph
of the C2A2 community network.

Usage:
    python3 generate_community_explorer.py <community_graph.json> <output.html>

Example:
    python3 generate_community_explorer.py \
        ../../community/community_graph.json \
        ../../community_explorer.html
"""

import json
import sys
import os
from pathlib import Path


# ── Color palette (by node type) ──────────────────────────────────────────────
TYPE_COLORS = {
    'Tradition-Constituted Enquiry': '#C9A84C',
    'Practice Communities':          '#3D9E89',
    'Contemplative & Spiritual':     '#8B5DAB',
    'Civic & Political':             '#5A72A8',
    'Scientific Frontier':           '#4A5E6D',
    'Interdisciplinary Synthesis':   '#5B7FA5',
    'Local & Embodied':              '#4A8A7A',
    'Professional Guilds':           '#C47A9A',
}

# Fallback for unknown types
DEFAULT_COLOR = '#888899'


def load_graph(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def build_filter_data(nodes):
    """Build type, quality, and subtype filter lists."""
    type_filters = []
    seen_types = set()
    for n in nodes:
        t = n.get('type', 'Unknown')
        if t not in seen_types:
            seen_types.add(t)
            type_filters.append({
                'key': t,
                'label': t,
                'color': TYPE_COLORS.get(t, DEFAULT_COLOR),
            })

    # Keep type order stable (use TYPE_COLORS key order as canonical)
    ordered = [t for t in TYPE_COLORS.keys() if t in seen_types]
    remainder = [t for t in seen_types if t not in TYPE_COLORS]
    type_filters = [
        {'key': t, 'label': t, 'color': TYPE_COLORS.get(t, DEFAULT_COLOR)}
        for t in ordered + sorted(remainder)
    ]

    # Subtypes — sorted alphabetically, deduplicated
    subtypes = sorted(set(
        n['subtype'] for n in nodes if n.get('subtype', '').strip()
    ))
    subtype_filters = [{'key': s, 'label': s} for s in subtypes]

    return type_filters, subtype_filters


def country_flag(country):
    """Return a flag emoji for well-known country strings, else globe."""
    mapping = {
        'USA': '🇺🇸', 'US': '🇺🇸', 'United States': '🇺🇸',
        'UK': '🇬🇧', 'United Kingdom': '🇬🇧',
        'Germany': '🇩🇪', 'DE': '🇩🇪',
        'France': '🇫🇷', 'FR': '🇫🇷',
        'Japan': '🇯🇵', 'JP': '🇯🇵',
        'Canada': '🇨🇦', 'CA': '🇨🇦',
        'Australia': '🇦🇺', 'AU': '🇦🇺',
        'Netherlands': '🇳🇱', 'NL': '🇳🇱',
        'Switzerland': '🇨🇭', 'CH': '🇨🇭',
        'India': '🇮🇳', 'IN': '🇮🇳',
        'China': '🇨🇳', 'CN': '🇨🇳',
        'Brazil': '🇧🇷', 'BR': '🇧🇷',
        'Spain': '🇪🇸', 'ES': '🇪🇸',
        'Italy': '🇮🇹', 'IT': '🇮🇹',
        'Sweden': '🇸🇪', 'SE': '🇸🇪',
        'Norway': '🇳🇴', 'NO': '🇳🇴',
        'Denmark': '🇩🇰', 'DK': '🇩🇰',
        'Belgium': '🇧🇪', 'BE': '🇧🇪',
        'Austria': '🇦🇹', 'AT': '🇦🇹',
        'Poland': '🇵🇱', 'PL': '🇵🇱',
        'Ireland': '🇮🇪', 'IE': '🇮🇪',
        'Israel': '🇮🇱', 'IL': '🇮🇱',
        'New Zealand': '🇳🇿', 'NZ': '🇳🇿',
        'South Korea': '🇰🇷', 'Korea': '🇰🇷',
        'Mexico': '🇲🇽', 'MX': '🇲🇽',
        'Argentina': '🇦🇷', 'AR': '🇦🇷',
        'South Africa': '🇿🇦', 'ZA': '🇿🇦',
        'Global': '🌐', 'International': '🌐', 'Worldwide': '🌐',
    }
    if not country:
        return '🌐'
    # Try exact match, then prefix match
    for key, flag in mapping.items():
        if country.strip().lower().startswith(key.lower()):
            return flag
    return '🌐'


def generate_html(graph_data):
    """Generate complete self-contained HTML with embedded data."""
    nodes = graph_data.get('nodes', [])
    edges = graph_data.get('edges', [])
    meta  = graph_data.get('meta', {})

    # Attach flag emoji to each node for the detail panel
    for n in nodes:
        n['_flag'] = country_flag(n.get('country', ''))

    type_filters, subtype_filters = build_filter_data(nodes)

    # Build color map JSON for JS
    type_colors_js = json.dumps(TYPE_COLORS, ensure_ascii=False)
    nodes_json     = json.dumps(nodes,   ensure_ascii=False)
    edges_json     = json.dumps(edges,   ensure_ascii=False)
    meta_json      = json.dumps(meta,    ensure_ascii=False)
    type_filters_json    = json.dumps(type_filters,    ensure_ascii=False)
    subtype_filters_json = json.dumps(subtype_filters, ensure_ascii=False)

    node_count = meta.get('node_count', len(nodes))
    edge_count = meta.get('edge_count', len(edges))

    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Community Explorer — C2A2</title>
<script src="https://d3js.org/d3.v7.min.js"></script>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: 100%; height: 100%; overflow: hidden; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background: #0a0a0f; color: #c8c8d0; }

/* ── Layout ── */
#shell { display: flex; width: 100%; height: 100vh; }

/* ── Left panel ── */
#left-panel {
  width: 220px; flex-shrink: 0; background: #0e0e18;
  border-right: 1px solid #1e1e2e; overflow-y: auto; padding: 12px 10px;
  display: flex; flex-direction: column; gap: 10px;
}
#left-panel::-webkit-scrollbar { width: 4px; }
#left-panel::-webkit-scrollbar-thumb { background: #2a2a3a; border-radius: 2px; }

.panel-title { font-size: 14px; font-weight: 700; color: #C9A84C; letter-spacing: 0.04em; padding: 2px 0 4px 0; border-bottom: 1px solid #1e1e2e; margin-bottom: 2px; }
.section-label { font-size: 11px; font-weight: 600; color: #888; text-transform: uppercase; letter-spacing: 0.08em; margin: 6px 0 4px 0; }

.filter-row { display: flex; align-items: flex-start; gap: 6px; cursor: pointer; padding: 2px 3px; border-radius: 3px; }
.filter-row:hover { background: #1a1a2a; }
.filter-row input[type=checkbox] { margin-top: 2px; accent-color: #C9A84C; flex-shrink: 0; cursor: pointer; }
.filter-dot { width: 9px; height: 9px; border-radius: 50%; flex-shrink: 0; margin-top: 3px; }
.filter-label { font-size: 11px; color: #b0b0c0; line-height: 1.35; }
.filter-row input:checked ~ .filter-label { color: #e0e0f0; }

#subtype-section { max-height: 260px; overflow-y: auto; }
#subtype-section::-webkit-scrollbar { width: 3px; }
#subtype-section::-webkit-scrollbar-thumb { background: #2a2a3a; border-radius: 2px; }

#btn-fit-all-panel {
  margin-top: 4px; padding: 5px 10px; background: #1a1a2a;
  border: 1px solid #3a3a4a; color: #e0e0e0; border-radius: 4px;
  cursor: pointer; font-size: 12px; text-align: center; width: 100%;
}
#btn-fit-all-panel:hover { background: #2a2a3a; color: #fff; }

/* ── Center canvas ── */
#canvas-wrap { flex: 1 1 auto; position: relative; overflow: hidden; }
svg#graph { width: 100%; height: 100%; display: block; }

/* ── Canvas controls (top-right) ── */
#canvas-controls {
  position: absolute; top: 10px; right: 12px;
  display: flex; gap: 6px; z-index: 10;
}
#canvas-controls button {
  background: rgba(14,14,24,0.88); border: 1px solid #3a3a4a;
  color: #c8c8d0; padding: 4px 10px; border-radius: 4px;
  cursor: pointer; font-size: 12px; backdrop-filter: blur(4px);
}
#canvas-controls button:hover { background: rgba(40,40,60,0.95); color: #fff; }
#canvas-controls button.active { background: #C9A84C; color: #0a0a0f; border-color: #C9A84C; }

/* ── Stats badge (bottom-left of canvas) ── */
#stats-badge {
  position: absolute; bottom: 10px; left: 10px;
  font-size: 11px; color: #555; background: rgba(14,14,24,0.7);
  padding: 3px 8px; border-radius: 4px; pointer-events: none;
}

/* ── Right panel ── */
#right-panel {
  width: 280px; flex-shrink: 0; background: #0e0e18;
  border-left: 1px solid #1e1e2e; overflow-y: auto;
  display: none; flex-direction: column;
  position: relative;
}
#right-panel::-webkit-scrollbar { width: 4px; }
#right-panel::-webkit-scrollbar-thumb { background: #2a2a3a; border-radius: 2px; }
#right-panel.open { display: flex; }

#panel-accent { height: 4px; flex-shrink: 0; }
#panel-body { padding: 12px 14px; flex: 1; }

#panel-close {
  position: absolute; top: 8px; right: 10px;
  background: none; border: none; color: #666; font-size: 18px;
  cursor: pointer; line-height: 1; z-index: 2;
}
#panel-close:hover { color: #ccc; }

#panel-name { font-size: 15px; font-weight: 700; color: #e8e8f0; margin: 0 0 6px 0; padding-right: 20px; }
#panel-type-badge {
  display: inline-block; font-size: 10px; font-weight: 600;
  padding: 2px 8px; border-radius: 10px; margin-bottom: 8px;
  text-transform: uppercase; letter-spacing: 0.06em;
}
#panel-location { font-size: 12px; color: #888; margin-bottom: 10px; }
#panel-desc { font-size: 12px; color: #b8b8c8; line-height: 1.55; margin-bottom: 12px; }

.panel-section-head { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #888; margin: 10px 0 4px 0; }
.panel-section-body { font-size: 12px; color: #a8a8b8; line-height: 1.5; margin-bottom: 2px; }

#panel-link {
  display: inline-block; margin-top: 14px; font-size: 12px;
  color: #C9A84C; text-decoration: none;
}
#panel-link:hover { text-decoration: underline; }

/* ── Tooltip ── */
#tooltip {
  position: absolute; background: rgba(14,14,24,0.92); border: 1px solid #2e2e3e;
  color: #e8e8f0; padding: 4px 9px; border-radius: 4px; font-size: 11px;
  pointer-events: none; display: none; z-index: 20; max-width: 200px;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}

/* ── SVG elements ── */
.node circle { cursor: pointer; transition: r 0.1s; }
.node circle:hover { filter: brightness(1.3); }
.node.selected circle { stroke: #fff; stroke-width: 2px; }
.node-label { font-size: 11px; fill: #ffffff; pointer-events: none; text-anchor: middle; dominant-baseline: central; paint-order: stroke; stroke: #0a0a0f; stroke-width: 3px; }
.link { pointer-events: none; }
</style>
</head>
<body>

<div id="shell">

  <!-- LEFT PANEL -->
  <div id="left-panel">
    <div class="panel-title">Communities</div>

    <div>
      <div class="section-label">Type</div>
      <div id="type-filters"></div>
    </div>

    <div>
      <div class="section-label">Quality</div>
      <div id="quality-filters">
        <label class="filter-row">
          <input type="checkbox" class="q-check" value="3" checked>
          <span class="filter-dot" style="background:#C9A84C"></span>
          <span class="filter-label">Exemplary (Q3)</span>
        </label>
        <label class="filter-row">
          <input type="checkbox" class="q-check" value="2" checked>
          <span class="filter-dot" style="background:#555566"></span>
          <span class="filter-label">Good (Q2)</span>
        </label>
      </div>
    </div>

    <div>
      <div class="section-label">Subtype</div>
      <div id="subtype-section" id="subtype-filters"></div>
    </div>

    <button id="btn-fit-all-panel">Fit All</button>
  </div>

  <!-- CANVAS -->
  <div id="canvas-wrap">
    <svg id="graph">
      <g id="graph-root">
        <g id="links-layer"></g>
        <g id="nodes-layer"></g>
        <g id="labels-layer"></g>
      </g>
    </svg>
    <div id="canvas-controls">
      <button id="btn-fit-all">Fit All</button>
      <button id="btn-hold">Hold Forces</button>
      <button id="btn-names">Show Names</button>
    </div>
    <div id="stats-badge" id="stats"></div>
    <div id="tooltip"></div>
  </div>

  <!-- RIGHT PANEL -->
  <div id="right-panel">
    <div id="panel-accent"></div>
    <button id="panel-close">&#215;</button>
    <div id="panel-body">
      <div id="panel-name"></div>
      <span id="panel-type-badge"></span>
      <div id="panel-location"></div>
      <div id="panel-desc"></div>
      <div class="panel-section-head">Problem</div>
      <div class="panel-section-body" id="panel-problem"></div>
      <div class="panel-section-head">Resource</div>
      <div class="panel-section-body" id="panel-resource"></div>
      <div class="panel-section-head">Solution</div>
      <div class="panel-section-body" id="panel-solution"></div>
      <a id="panel-link" href="#" target="_blank" rel="noopener">Link &#8594;</a>
    </div>
  </div>

</div><!-- #shell -->

<script>
// ── DATA ──────────────────────────────────────────────────────────────────────
const GRAPH_DATA = """ + json.dumps(graph_data, ensure_ascii=False) + """;
const TYPE_COLORS = """ + type_colors_js + """;
const TYPE_FILTERS = """ + type_filters_json + """;
const SUBTYPE_FILTERS = """ + subtype_filters_json + """;

// ── STATE ─────────────────────────────────────────────────────────────────────
var showNames = false;
var holdForces = false;
var selectedNodeId = null;

// Active filter sets
var activeTypes    = new Set(TYPE_FILTERS.map(function(f) { return f.key; }));
var activeQualities = new Set([2, 3]);
var activeSubtypes = new Set(SUBTYPE_FILTERS.map(function(f) { return f.key; }));

// ── HELPERS ───────────────────────────────────────────────────────────────────
function nodeColor(d) {
  return TYPE_COLORS[d.type] || '#888899';
}
function nodeRadius(d) {
  return d.prs_quality >= 3 ? 7 : 5;
}
function isVisible(d) {
  var typeOk    = activeTypes.has(d.type);
  var qualOk    = activeQualities.has(d.prs_quality);
  var subtypeOk = !d.subtype || activeSubtypes.has(d.subtype);
  return typeOk && qualOk && subtypeOk;
}

// ── BUILD LEFT PANEL ──────────────────────────────────────────────────────────
(function buildFilters() {
  var typeEl = document.getElementById('type-filters');
  TYPE_FILTERS.forEach(function(f) {
    var label = document.createElement('label');
    label.className = 'filter-row';
    label.innerHTML =
      '<input type="checkbox" class="t-check" value="' + escHtml(f.key) + '" checked>' +
      '<span class="filter-dot" style="background:' + f.color + '"></span>' +
      '<span class="filter-label">' + escHtml(f.label) + '</span>';
    typeEl.appendChild(label);
  });

  var subEl = document.getElementById('subtype-section');
  SUBTYPE_FILTERS.forEach(function(f) {
    var label = document.createElement('label');
    label.className = 'filter-row';
    label.innerHTML =
      '<input type="checkbox" class="s-check" value="' + escHtml(f.key) + '" checked>' +
      '<span class="filter-label">' + escHtml(f.label) + '</span>';
    subEl.appendChild(label);
  });
})();

function escHtml(str) {
  return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

// ── D3 SETUP ──────────────────────────────────────────────────────────────────
var svg    = d3.select('#graph');
var root   = d3.select('#graph-root');
var linksG = d3.select('#links-layer');
var nodesG = d3.select('#nodes-layer');
var labelsG = d3.select('#labels-layer');

// Zoom
var zoom = d3.zoom()
  .scaleExtent([0.05, 8])
  .on('zoom', function(event) { root.attr('transform', event.transform); });
svg.call(zoom);

// Nodes and edges from data
var allNodes = GRAPH_DATA.nodes;
var allEdges = GRAPH_DATA.edges;
var meta     = GRAPH_DATA.meta;

// Weight extent for edge opacity
var weightExtent = d3.extent(allEdges, function(e) { return e.weight || 0; });
var opacityScale = d3.scaleLinear()
  .domain(weightExtent)
  .range([0.06, 0.35])
  .clamp(true);

// ── SIMULATION ────────────────────────────────────────────────────────────────
var simulation = d3.forceSimulation(allNodes)
  .force('link', d3.forceLink(allEdges)
    .id(function(d) { return d.id; })
    .distance(80))
  .force('charge', d3.forceManyBody().strength(-120))
  .force('collision', d3.forceCollide().radius(function(d) { return nodeRadius(d) + 2; }))
  .force('center', d3.forceCenter(0, 0))
  .on('tick', ticked);

// ── RENDER ELEMENTS ───────────────────────────────────────────────────────────
// Links
var linkSel = linksG.selectAll('.link')
  .data(allEdges)
  .enter().append('line')
    .attr('class', 'link')
    .attr('stroke', '#ffffff')
    .attr('stroke-width', 1)
    .attr('stroke-opacity', function(d) { return opacityScale(d.weight || 0); });

// Nodes
var nodeSel = nodesG.selectAll('.node')
  .data(allNodes)
  .enter().append('g')
    .attr('class', 'node')
    .attr('data-id', function(d) { return d.id; })
    .call(d3.drag()
      .on('start', dragStarted)
      .on('drag',  dragged)
      .on('end',   dragEnded))
    .on('click', nodeClicked)
    .on('mouseover', showTooltip)
    .on('mousemove', moveTooltip)
    .on('mouseout',  hideTooltip);

nodeSel.append('circle')
  .attr('r', nodeRadius)
  .attr('fill', nodeColor)
  .attr('stroke', 'none');

// Labels (always present in DOM, visibility controlled by showNames flag)
var labelSel = labelsG.selectAll('.node-label')
  .data(allNodes)
  .enter().append('text')
    .attr('class', 'node-label')
    .text(function(d) { return d.name; })
    .style('display', 'none');

// ── TICK ──────────────────────────────────────────────────────────────────────
function ticked() {
  linkSel
    .attr('x1', function(d) { return d.source.x; })
    .attr('y1', function(d) { return d.source.y; })
    .attr('x2', function(d) { return d.target.x; })
    .attr('y2', function(d) { return d.target.y; });

  nodeSel.attr('transform', function(d) { return 'translate(' + d.x + ',' + d.y + ')'; });

  labelSel
    .attr('x', function(d) { return d.x; })
    .attr('y', function(d) { return d.y - nodeRadius(d) - 4; });
}

// ── VISIBILITY UPDATE ─────────────────────────────────────────────────────────
function applyVisibility() {
  // Nodes
  nodeSel.style('display', function(d) { return isVisible(d) ? null : 'none'; });

  // Labels
  labelSel.style('display', function(d) {
    if (!isVisible(d)) return 'none';
    return showNames ? null : 'none';
  });

  // Edges: hide if either endpoint is hidden
  linkSel.style('display', function(d) {
    var sNode = typeof d.source === 'object' ? d.source : null;
    var tNode = typeof d.target === 'object' ? d.target : null;
    if (!sNode || !tNode) return null;
    return (isVisible(sNode) && isVisible(tNode)) ? null : 'none';
  });

  updateStats();
}

function updateStats() {
  var visNodes = allNodes.filter(isVisible).length;
  var el = document.getElementById('stats-badge');
  if (el) el.textContent = visNodes + ' / ' + allNodes.length + ' communities';
}

// ── FILTER EVENTS ─────────────────────────────────────────────────────────────
document.getElementById('type-filters').addEventListener('change', function(e) {
  if (!e.target.classList.contains('t-check')) return;
  var val = e.target.value;
  if (e.target.checked) activeTypes.add(val); else activeTypes.delete(val);
  applyVisibility();
});

document.getElementById('quality-filters').addEventListener('change', function(e) {
  if (!e.target.classList.contains('q-check')) return;
  var val = parseInt(e.target.value, 10);
  if (e.target.checked) activeQualities.add(val); else activeQualities.delete(val);
  applyVisibility();
});

document.getElementById('subtype-section').addEventListener('change', function(e) {
  if (!e.target.classList.contains('s-check')) return;
  var val = e.target.value;
  if (e.target.checked) activeSubtypes.add(val); else activeSubtypes.delete(val);
  applyVisibility();
});

// ── CONTROLS ──────────────────────────────────────────────────────────────────
function fitAll() {
  var w = document.getElementById('canvas-wrap').clientWidth;
  var h = document.getElementById('canvas-wrap').clientHeight;
  var visNodes = allNodes.filter(isVisible);
  if (visNodes.length === 0) return;

  var xs = visNodes.map(function(d) { return d.x; });
  var ys = visNodes.map(function(d) { return d.y; });
  var minX = d3.min(xs), maxX = d3.max(xs);
  var minY = d3.min(ys), maxY = d3.max(ys);

  var pad = 40;
  var scaleX = (w - pad*2) / (maxX - minX || 1);
  var scaleY = (h - pad*2) / (maxY - minY || 1);
  var scale = Math.min(scaleX, scaleY, 3);

  var tx = w/2 - scale*(minX + maxX)/2;
  var ty = h/2 - scale*(minY + maxY)/2;

  svg.transition().duration(600)
    .call(zoom.transform, d3.zoomIdentity.translate(tx, ty).scale(scale));
}

document.getElementById('btn-fit-all').addEventListener('click', fitAll);
document.getElementById('btn-fit-all-panel').addEventListener('click', fitAll);

document.getElementById('btn-hold').addEventListener('click', function() {
  holdForces = !holdForces;
  this.classList.toggle('active', holdForces);
  if (holdForces) {
    simulation.stop();
  } else {
    simulation.alphaTarget(0.1).restart();
    setTimeout(function() { simulation.alphaTarget(0); }, 2000);
  }
});

document.getElementById('btn-names').addEventListener('click', function() {
  showNames = !showNames;
  this.classList.toggle('active', showNames);
  applyVisibility();
});

// ── DRAG ──────────────────────────────────────────────────────────────────────
function dragStarted(event, d) {
  if (!event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x; d.fy = d.y;
}
function dragged(event, d) {
  d.fx = event.x; d.fy = event.y;
}
function dragEnded(event, d) {
  if (!event.active) simulation.alphaTarget(0);
  if (!holdForces) { d.fx = null; d.fy = null; }
}

// ── TOOLTIP ───────────────────────────────────────────────────────────────────
var tooltip = document.getElementById('tooltip');
function showTooltip(event, d) {
  tooltip.textContent = d.name;
  tooltip.style.display = 'block';
  moveTooltip(event);
}
function moveTooltip(event) {
  var wrap = document.getElementById('canvas-wrap').getBoundingClientRect();
  tooltip.style.left = (event.clientX - wrap.left + 12) + 'px';
  tooltip.style.top  = (event.clientY - wrap.top  - 24) + 'px';
}
function hideTooltip() {
  tooltip.style.display = 'none';
}

// ── NODE CLICK → RIGHT PANEL ──────────────────────────────────────────────────
function nodeClicked(event, d) {
  event.stopPropagation();
  selectedNodeId = d.id;

  // Highlight selected
  nodesG.selectAll('.node').classed('selected', function(n) { return n.id === d.id; });

  // Fill panel
  var color = TYPE_COLORS[d.type] || '#888899';
  document.getElementById('panel-accent').style.background = color;
  document.getElementById('panel-name').textContent = d.name;

  var badge = document.getElementById('panel-type-badge');
  badge.textContent = d.type || '';
  badge.style.background = color + '33';
  badge.style.color = color;
  badge.style.border = '1px solid ' + color + '66';

  var flag = d._flag || '🌐';
  var country = d.country || '';
  document.getElementById('panel-location').textContent = flag + '  ' + country;

  document.getElementById('panel-desc').textContent     = d.description || '';
  document.getElementById('panel-problem').textContent  = d.problem     || '—';
  document.getElementById('panel-resource').textContent = d.resource    || '—';
  document.getElementById('panel-solution').textContent = d.solution    || '—';

  var link = document.getElementById('panel-link');
  if (d.url) {
    link.href = d.url;
    link.style.display = 'inline-block';
  } else {
    link.style.display = 'none';
  }

  document.getElementById('right-panel').classList.add('open');
}

// Close panel
document.getElementById('panel-close').addEventListener('click', function() {
  document.getElementById('right-panel').classList.remove('open');
  selectedNodeId = null;
  nodesG.selectAll('.node').classed('selected', false);
});

// Click on canvas background → deselect
svg.on('click', function(event) {
  if (event.target === svg.node() || event.target.closest('#graph-root') === null) {
    document.getElementById('right-panel').classList.remove('open');
    selectedNodeId = null;
    nodesG.selectAll('.node').classed('selected', false);
  }
});

// ── INITIAL FIT ───────────────────────────────────────────────────────────────
// Wait for simulation to settle a bit, then fit
simulation.on('end', function() {
  fitAll();
});
// Also fit after a short delay in case 'end' fires before DOM is ready
setTimeout(function() {
  fitAll();
  applyVisibility();
}, 1200);

// Initial stats
updateStats();

</script>
</body>
</html>"""

    return html


def main():
    if len(sys.argv) < 3:
        print('Usage: generate_community_explorer.py <input_graph.json> <output.html>', file=sys.stderr)
        sys.exit(1)

    input_path  = sys.argv[1]
    output_path = sys.argv[2]

    print(f'Reading {input_path}...', file=sys.stderr)
    graph_data = load_graph(input_path)

    print(f'Generating HTML ({graph_data["meta"]["node_count"]} nodes, '
          f'{graph_data["meta"]["edge_count"]} edges)...', file=sys.stderr)

    html = generate_html(graph_data)

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)

    size_kb = out.stat().st_size / 1024
    print(f'Written {output_path} ({size_kb:.1f} KB)', file=sys.stderr)


if __name__ == '__main__':
    main()
