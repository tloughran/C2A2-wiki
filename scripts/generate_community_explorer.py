#!/usr/bin/env python3
"""
generate_community_explorer.py
Builds wiki/community_explorer.html from wiki/community/community_graph.json.

Self-contained D3 v7 force-directed graph following the sociogram pattern:
dark #0a0a0f, left-panel checkbox filters, right-panel detail renderer,
upper-right Hold Forces / Show Names / Fit All controls.
Includes a Cards sub-tab that iframes the existing community/index.html.

Template rules (per project CLAUDE.md):
  - Regular strings only (NOT f-strings) for the HTML template
  - Data injection via "" + json_var + "" concatenation only
  - CSS/JS use single braces only

Usage:
    python3 scripts/generate_community_explorer.py
"""

import json
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
INPUT_PATH = REPO_ROOT / "wiki" / "community" / "community_graph.json"
SEARCHLIB_PATH = REPO_ROOT / "wiki" / "lib" / "c2a2-search.js"
OUTPUT_PATH = REPO_ROOT / "wiki" / "community_explorer.html"

TYPE_COLORS = {
    "Tradition-Constituted Enquiry": "#C9A84C",
    "Practice Communities": "#4A8A7A",
    "Contemplative & Spiritual": "#8B5DAB",
    "Civic & Political": "#5A72A8",
    "Scientific Frontier": "#C45B5B",
    "Interdisciplinary Synthesis": "#3D9E89",
    "Local & Embodied": "#9A7A5A",
    "Professional Guilds": "#B87D3E",
}

HTML_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Community Explorer — C2A2</title>
<script src="https://d3js.org/d3.v7.min.js"></script>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body { width: 100%; height: 100%; overflow: hidden; }
  body {
    background: #0a0a0f;
    color: #c8c8d0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    display: flex; flex-direction: column;
  }
  /* ── Header ── */
  #header {
    display: flex; align-items: center; gap: 14px;
    padding: 8px 14px; background: #11111a; border-bottom: 1px solid #22222e;
    flex: 0 0 auto;
  }
  #header h1 { font-size: 14px; font-weight: 600; color: #e8e8f0; white-space: nowrap; }
  .subtab {
    padding: 4px 14px; border: 1px solid #33334a; border-radius: 5px;
    background: #16161f; color: #9a9ab0; font-size: 12px; cursor: pointer;
  }
  .subtab.active { background: #28283a; color: #e8e8f0; border-color: #5b7fa5; }
  #tabs-help {
    width: 20px; height: 20px; line-height: 18px; text-align: center;
    border: 1px solid #33334a; border-radius: 50%; background: #16161f;
    color: #9a9ab0; font-size: 12px; cursor: pointer; padding: 0;
  }
  #tabs-help:hover { color: #c9a84c; border-color: #4a4a5a; }
  #spacer { flex: 1; }
  .ctrl {
    padding: 4px 12px; border: 1px solid #33334a; border-radius: 5px;
    background: #16161f; color: #9a9ab0; font-size: 12px; cursor: pointer;
  }
  .ctrl.on { background: #28283a; color: #e8e8f0; border-color: #c9a84c; }
  #stats { font-size: 11px; color: #66667a; white-space: nowrap; }
  /* ── Main layout ── */
  #main { flex: 1 1 auto; display: flex; min-height: 0; position: relative; }
  #leftpanel {
    flex: 0 0 230px; background: #11111a; border-right: 1px solid #22222e;
    overflow-y: auto; padding: 12px;
  }
  #leftpanel h2 { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #66667a; margin: 10px 0 6px; }
  .allnone { font-size: 11px; color: #5b7fa5; cursor: pointer; margin-left: 6px; }
  .filter-row { display: flex; align-items: center; gap: 7px; padding: 3px 0; font-size: 12.5px; cursor: pointer; }
  .filter-row input { cursor: pointer; }
  .swatch { width: 10px; height: 10px; border-radius: 3px; flex: 0 0 auto; }
  .fcount { color: #66667a; font-size: 11px; margin-left: auto; }
  #qualrow { margin-top: 12px; border-top: 1px solid #22222e; padding-top: 10px; }
  /* ── Graph ── */
  #graphwrap { flex: 1 1 auto; position: relative; min-width: 0; }
  #graph { width: 100%; height: 100%; display: block; cursor: grab; }
  #tooltip {
    position: absolute; pointer-events: none; background: #1a1a26; color: #e8e8f0;
    border: 1px solid #33334a; border-radius: 5px; padding: 4px 9px; font-size: 12px;
    opacity: 0; transition: opacity 0.12s; max-width: 280px; z-index: 10;
  }
  /* ── Right panel ── */
  #rightpanel {
    flex: 0 0 360px; background: #11111a; border-left: 1px solid #22222e;
    overflow-y: auto; padding: 16px; display: none;
  }
  #rightpanel.open { display: block; }
  #rp-close { float: right; cursor: pointer; color: #66667a; font-size: 16px; padding: 0 4px; }
  #rp-close:hover { color: #e8e8f0; }
  #rightpanel h3 { font-size: 15px; color: #e8e8f0; margin-bottom: 8px; padding-right: 24px; }
  #rightpanel h3 a { color: #7fa5c9; text-decoration: none; }
  #rightpanel h3 a:hover { text-decoration: underline; }
  .badge {
    display: inline-block; font-size: 10.5px; padding: 2px 8px; border-radius: 9px;
    background: #1e1e2c; border: 1px solid #33334a; margin: 0 4px 5px 0; color: #aaaabe;
  }
  .rp-section { margin-top: 12px; }
  .rp-section h4 {
    font-size: 10.5px; text-transform: uppercase; letter-spacing: 1px;
    margin-bottom: 4px;
  }
  .rp-section p { font-size: 12.5px; line-height: 1.55; color: #b8b8c6; }
  .h-problem { color: #c45b5b; } .h-resource { color: #c9a84c; } .h-solution { color: #4e8a5e; }
  .h-desc { color: #66667a; } .h-conn { color: #5b7fa5; }
  .conn-row { font-size: 12px; padding: 3px 0; cursor: pointer; color: #9a9ab0; display: flex; gap: 8px; }
  .conn-row:hover { color: #e8e8f0; }
  .conn-w { color: #66667a; flex: 0 0 auto; font-size: 11px; }
  /* ── Cards sub-view ── */
  #cardsview { flex: 1 1 auto; display: none; }
  #cardsview iframe { width: 100%; height: 100%; border: 0; }
  svg .lbl { font-size: 9.5px; fill: #b8b8c6; pointer-events: none; }
  /* ── Search footer ── */
  #footer { flex: 0 0 auto; background: #11111a; border-top: 1px solid #22222e; padding: 6px 14px; }
  #search-status { font-size: 12px; color: #9a9ab0; line-height: 1.5; padding: 0 0 6px; display: none; }
  #search-row { display: flex; gap: 8px; align-items: center; }
  #search-row input[type="text"] {
    flex: 1; min-width: 160px; background: #16161f; border: 1px solid #33334a;
    color: #e8e8f0; padding: 4px 10px; border-radius: 5px; font-size: 12.5px;
  }
  .chk { display: flex; align-items: center; gap: 5px; font-size: 11.5px; color: #9a9ab0; cursor: pointer; white-space: nowrap; }
  /* ── Tabs help modal ── */
  #help-modal { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.7); z-index: 1200; justify-content: center; align-items: center; }
  #help-modal.open { display: flex; }
  #help-card { background: #12121c; border: 1px solid #2a2a3a; border-radius: 10px; padding: 26px 30px; width: 540px; max-width: 92%; max-height: 86%; overflow-y: auto; position: relative; box-shadow: 0 8px 32px rgba(0,0,0,0.6); }
  #help-card h3 { color: #c9a84c; font-size: 16px; font-family: Georgia, serif; margin: 0 0 14px; padding-right: 24px; }
  #help-card .note { color: #c79a5a; font-size: 12px; line-height: 1.55; margin: 0 0 14px; padding: 8px 11px; border: 1px solid #3a3320; border-radius: 6px; background: #1b180f; }
  #help-card p { color: #ccc; font-size: 13px; line-height: 1.65; margin: 0 0 11px; }
  #help-card p:last-child { margin-bottom: 0; }
  #help-card strong { color: #e8e8f0; }
  #help-close { position: absolute; top: 10px; right: 14px; background: transparent; border: none; color: #666; font-size: 20px; cursor: pointer; line-height: 1; padding: 2px 6px; }
  #help-close:hover { color: #c9a84c; }
</style>
</head>
<body>
<div id="header">
  <h1>Community Explorer</h1>
  <button class="subtab active" id="tab-graph">Graph</button>
  <button class="subtab" id="tab-cards">Cards</button>
  <button id="tabs-help" title="How Graph and Cards relate">?</button>
  <div id="spacer"></div>
  <span id="graph-controls">
    <span id="stats"></span>
    <button class="ctrl" id="btn-hold">Hold Forces</button>
    <button class="ctrl" id="btn-names">Show Names</button>
    <button class="ctrl" id="btn-fit">Fit All</button>
  </span>
</div>
<div id="main">
  <div id="leftpanel">
    <h2>Community Type <span class="allnone" id="types-all">all</span><span class="allnone" id="types-none">none</span></h2>
    <div id="typefilters"></div>
    <div id="qualrow">
      <label class="filter-row"><input type="checkbox" id="q3only"> Exemplary (Q3) only <span class="fcount" id="q3count"></span></label>
    </div>
  </div>
  <div id="graphwrap">
    <svg id="graph"></svg>
    <div id="tooltip"></div>
  </div>
  <div id="rightpanel">
    <span id="rp-close">&times;</span>
    <div id="rp-content"></div>
  </div>
  <div id="cardsview"><iframe data-src="community/index.html"></iframe></div>
</div>
<div id="footer">
  <div id="search-status"></div>
  <div id="search-row">
    <input type="text" id="search-input" autocomplete="off"
      placeholder='Search communities &mdash; or "focus: civic ~ scientific" to isolate cross-type links'>
    <button class="ctrl" id="btn-search">Search</button>
    <button class="ctrl" id="btn-clear">Clear</button>
    <label class="chk"><input type="checkbox" id="search-ai-mode"> Ask AI</label>
    <label class="chk"><input type="checkbox" id="search-external"> Allow wider search</label>
  </div>
</div>
<div id="help-modal">
  <div id="help-card">
    <button id="help-close" title="Close">&#x00D7;</button>
    <h3>Graph and Cards &mdash; two surfaces, one instrument</h3>
    <p class="note">This tool is currently still under construction, and has been seeded with publicly-available information about communities without their express consent.</p>
    <p>The <strong>Cards</strong> directory is the wide door. It holds every community we've found &mdash; the full directory &mdash; each an inferred <em>seed</em> until the community itself claims the record and sharpens its own Goals, Problems, Resources, and Solutions. Its work is breadth and self-articulation: a place to be found, to find peers, and to say in your own words what you are about.</p>
    <p>The <strong>Graph</strong> is the narrow, relational view. It shows the 156 communities articulated to a quality bar, positioned by how kindred their problems are &mdash; so you can see which traditions sit near one another and where one type reaches across to another. Its work is depth and detection: making the relationships between communities visible, and eventually measurable.</p>
    <p>The two are complementary and mutually upbuilding. The directory feeds the graph: a seed record, once a community articulates it well, earns its place in the relational map and grows edges to its neighbors. The graph gives the directory its purpose: a destination worth articulating toward, and a picture of the whole that no single card can show. Breadth invites; depth reveals &mdash; each makes the other more truthful.</p>
  </div>
</div>
<script>
const GRAPH = """

HTML_TAIL = """;
const TYPE_COLORS = """  # noqa — second injection point

HTML_AFTER_COLORS = """;
</script>
<script>
// ── Inlined shared module: wiki/lib/c2a2-search.js ─────────────────────────
// Single source of truth is that file; edit it and regenerate this page
// (same convention as the Sociogram / generate_visualization.py).
"""  # noqa — third injection point (search lib)

HTML_BODY = """
</script>
<script>

// ── State ──────────────────────────────────────────────────────────────────
const allNodes = GRAPH.nodes;
const allEdges = GRAPH.edges;
const degree = {};
allNodes.forEach(n => degree[n.id] = 0);
allEdges.forEach(e => { degree[e.source] += 1; degree[e.target] += 1; });
const nodeById = {};
allNodes.forEach(n => nodeById[n.id] = n);
const neighbors = {};
allNodes.forEach(n => neighbors[n.id] = []);
allEdges.forEach(e => {
  neighbors[e.source].push({ id: e.target, w: e.weight });
  neighbors[e.target].push({ id: e.source, w: e.weight });
});

const activeTypes = new Set(Object.keys(TYPE_COLORS));
let q3Only = false;
let holdForces = false;
let showNames = false;

// ── Filters panel ──────────────────────────────────────────────────────────
const typeCounts = {};
allNodes.forEach(n => typeCounts[n.type] = (typeCounts[n.type] || 0) + 1);
const tf = document.getElementById('typefilters');
Object.keys(TYPE_COLORS).forEach(t => {
  const row = document.createElement('label');
  row.className = 'filter-row';
  row.innerHTML = '<input type="checkbox" checked data-type="' + t + '">' +
    '<span class="swatch" style="background:' + TYPE_COLORS[t] + '"></span>' +
    '<span>' + t + '</span><span class="fcount">' + (typeCounts[t] || 0) + '</span>';
  row.querySelector('input').addEventListener('change', ev => {
    if (ev.target.checked) activeTypes.add(t); else activeTypes.delete(t);
    rebuild();
  });
  tf.appendChild(row);
});
document.getElementById('types-all').addEventListener('click', () => {
  Object.keys(TYPE_COLORS).forEach(t => activeTypes.add(t));
  tf.querySelectorAll('input').forEach(i => i.checked = true);
  rebuild();
});
document.getElementById('types-none').addEventListener('click', () => {
  activeTypes.clear();
  tf.querySelectorAll('input').forEach(i => i.checked = false);
  rebuild();
});
document.getElementById('q3count').textContent = allNodes.filter(n => n.prs_quality >= 3).length;
document.getElementById('q3only').addEventListener('change', ev => { q3Only = ev.target.checked; rebuild(); });

// ── SVG / simulation ───────────────────────────────────────────────────────
const svg = d3.select('#graph');
const gRoot = svg.append('g');
const gLinks = gRoot.append('g');
const gNodes = gRoot.append('g');
const gLabels = gRoot.append('g');
const tooltip = document.getElementById('tooltip');

const zoom = d3.zoom().scaleExtent([0.15, 8]).on('zoom', ev => gRoot.attr('transform', ev.transform));
svg.call(zoom);

let sim = null;
let visNodes = [], visEdges = [];

function nodeVisible(n) {
  if (!activeTypes.has(n.type)) return false;
  if (q3Only && n.prs_quality < 3) return false;
  return true;
}

function rebuild() {
  const visSet = new Set();
  visNodes = allNodes.filter(n => nodeVisible(n));
  visNodes.forEach(n => visSet.add(n.id));
  visEdges = allEdges
    .filter(e => visSet.has(idOf(e.source)) && visSet.has(idOf(e.target)))
    .map(e => ({ source: idOf(e.source), target: idOf(e.target), weight: e.weight }));
  document.getElementById('stats').textContent = visNodes.length + ' communities · ' + visEdges.length + ' edges';
  render();
}

function idOf(x) { return (typeof x === 'object') ? x.id : x; }

function render() {
  if (sim) sim.stop();

  const links = gLinks.selectAll('line').data(visEdges, e => idOf(e.source) + '|' + idOf(e.target));
  links.exit().remove();
  const linksEnter = links.enter().append('line')
    .attr('stroke', '#3a3a52')
    .attr('stroke-opacity', e => Math.min(0.85, 0.25 + e.weight * 2.2))
    .attr('stroke-width', e => 0.6 + e.weight * 5)
    .style('cursor', 'pointer')
    .on('click', (ev, e) => { showEdge(e); ev.stopPropagation(); });
  const allLinks = linksEnter.merge(links);

  const nodes = gNodes.selectAll('circle').data(visNodes, n => n.id);
  nodes.exit().remove();
  const nodesEnter = nodes.enter().append('circle')
    .attr('r', n => 4 + Math.sqrt(degree[n.id] || 0) * 1.6)
    .attr('fill', n => TYPE_COLORS[n.type] || '#888')
    .attr('stroke', n => n.prs_quality >= 3 ? '#e8d9a0' : '#0a0a0f')
    .attr('stroke-width', n => n.prs_quality >= 3 ? 1.6 : 1)
    .style('cursor', 'pointer')
    .on('mouseover', (ev, n) => {
      tooltip.textContent = n.name;
      tooltip.style.opacity = 1;
      const r = document.getElementById('graphwrap').getBoundingClientRect();
      tooltip.style.left = (ev.clientX - r.left + 14) + 'px';
      tooltip.style.top = (ev.clientY - r.top - 8) + 'px';
    })
    .on('mousemove', ev => {
      const r = document.getElementById('graphwrap').getBoundingClientRect();
      tooltip.style.left = (ev.clientX - r.left + 14) + 'px';
      tooltip.style.top = (ev.clientY - r.top - 8) + 'px';
    })
    .on('mouseout', () => tooltip.style.opacity = 0)
    .on('click', (ev, n) => { showNode(n); ev.stopPropagation(); })
    .call(d3.drag()
      .on('start', (ev, n) => { if (!ev.active && sim && !holdForces) sim.alphaTarget(0.25).restart(); n.fx = n.x; n.fy = n.y; })
      .on('drag', (ev, n) => { n.fx = ev.x; n.fy = ev.y; })
      .on('end', (ev, n) => { if (!ev.active && sim) sim.alphaTarget(0); n.fx = null; n.fy = null; }));
  const allCircles = nodesEnter.merge(nodes);

  gLabels.selectAll('text').remove();
  let allLabelSel = null;
  if (showNames) {
    allLabelSel = gLabels.selectAll('text').data(visNodes, n => n.id).enter().append('text')
      .attr('class', 'lbl')
      .text(n => n.name.length > 34 ? n.name.slice(0, 32) + '…' : n.name);
  }

  sim = d3.forceSimulation(visNodes)
    .force('link', d3.forceLink(visEdges).id(n => n.id).distance(e => 60 + (1 - e.weight) * 80).strength(e => Math.min(1, e.weight * 4)))
    .force('charge', d3.forceManyBody().strength(-140))
    .force('center', d3.forceCenter(width() / 2, height() / 2))
    .force('collide', d3.forceCollide().radius(n => 8 + Math.sqrt(degree[n.id] || 0) * 1.6))
    .on('tick', () => {
      allLinks
        .attr('x1', e => e.source.x).attr('y1', e => e.source.y)
        .attr('x2', e => e.target.x).attr('y2', e => e.target.y);
      allCircles.attr('cx', n => n.x).attr('cy', n => n.y);
      if (allLabelSel) allLabelSel.attr('x', n => n.x + 9).attr('y', n => n.y + 3);
    });
  if (holdForces) sim.stop();
}

function width() { return document.getElementById('graphwrap').clientWidth; }
function height() { return document.getElementById('graphwrap').clientHeight; }

// ── Right panel ────────────────────────────────────────────────────────────
const rp = document.getElementById('rightpanel');
const rpc = document.getElementById('rp-content');
document.getElementById('rp-close').addEventListener('click', () => rp.classList.remove('open'));
svg.on('click', () => rp.classList.remove('open'));

function esc(s) {
  return String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function showNode(n) {
  let h = '<h3>' + (n.url ? '<a href="' + esc(n.url) + '" target="_blank" rel="noopener">' + esc(n.name) + '</a>' : esc(n.name)) + '</h3>';
  h += '<span class="badge" style="border-color:' + (TYPE_COLORS[n.type] || '#33334a') + '">' + esc(n.type) + '</span>';
  if (n.subtype) h += '<span class="badge">' + esc(n.subtype) + '</span>';
  if (n.country) h += '<span class="badge">' + esc(n.country) + '</span>';
  h += '<span class="badge">' + (n.prs_quality >= 3 ? 'Q3 exemplary' : 'Q2 good') + '</span>';
  if (n.description) h += '<div class="rp-section"><h4 class="h-desc">About</h4><p>' + esc(n.description) + '</p></div>';
  if (n.problem) h += '<div class="rp-section"><h4 class="h-problem">Problem</h4><p>' + esc(n.problem) + '</p></div>';
  if (n.resource) h += '<div class="rp-section"><h4 class="h-resource">Resource</h4><p>' + esc(n.resource) + '</p></div>';
  if (n.solution) h += '<div class="rp-section"><h4 class="h-solution">Solution</h4><p>' + esc(n.solution) + '</p></div>';
  const conns = (neighbors[n.id] || []).slice().sort((a, b) => b.w - a.w).slice(0, 10);
  if (conns.length) {
    h += '<div class="rp-section"><h4 class="h-conn">Connected communities</h4>';
    conns.forEach(c => {
      h += '<div class="conn-row" data-id="' + esc(c.id) + '"><span class="conn-w">' + c.w.toFixed(2) + '</span><span>' + esc(nodeById[c.id].name) + '</span></div>';
    });
    h += '</div>';
  }
  rpc.innerHTML = h;
  rpc.querySelectorAll('.conn-row').forEach(el => el.addEventListener('click', () => {
    const t = nodeById[el.getAttribute('data-id')];
    if (t) showNode(t);
  }));
  rp.classList.add('open');
}

function showEdge(e) {
  const a = nodeById[idOf(e.source)], b = nodeById[idOf(e.target)];
  let h = '<h3>Edge — PRS similarity ' + e.weight.toFixed(3) + '</h3>';
  [a, b].forEach(n => {
    h += '<div class="rp-section"><h4 class="h-conn">' + esc(n.type) + '</h4>' +
      '<div class="conn-row" data-id="' + esc(n.id) + '"><span>' + esc(n.name) + '</span></div>' +
      '<p>' + esc((n.problem || '').slice(0, 220)) + (n.problem && n.problem.length > 220 ? '…' : '') + '</p></div>';
  });
  rpc.innerHTML = h;
  rpc.querySelectorAll('.conn-row').forEach(el => el.addEventListener('click', () => {
    const t = nodeById[el.getAttribute('data-id')];
    if (t) showNode(t);
  }));
  rp.classList.add('open');
}

// ── Header controls ────────────────────────────────────────────────────────
document.getElementById('btn-hold').addEventListener('click', ev => {
  holdForces = !holdForces;
  ev.target.classList.toggle('on', holdForces);
  if (sim) { if (holdForces) sim.stop(); else sim.alpha(0.3).restart(); }
});
document.getElementById('btn-names').addEventListener('click', ev => {
  showNames = !showNames;
  ev.target.classList.toggle('on', showNames);
  render();
});
document.getElementById('btn-fit').addEventListener('click', () => {
  if (!visNodes.length) return;
  const xs = visNodes.map(n => n.x), ys = visNodes.map(n => n.y);
  const minX = Math.min(...xs), maxX = Math.max(...xs);
  const minY = Math.min(...ys), maxY = Math.max(...ys);
  const w = width(), h = height();
  const scale = Math.min(8, 0.88 / Math.max((maxX - minX) / w, (maxY - minY) / h));
  const tx = w / 2 - scale * (minX + maxX) / 2;
  const ty = h / 2 - scale * (minY + maxY) / 2;
  svg.transition().duration(500).call(zoom.transform, d3.zoomIdentity.translate(tx, ty).scale(scale));
});

// ── Search (highlight lens — NEVER a filter; 2026-05-29 LOCK) ──────────────
// Mirrors the Sociogram search semantics: empty query restores all opacities,
// "focus:" is a deterministic relational command over the 8 community types,
// "Ask AI" routes through the shared C2A2 broker pipeline (c2a2-search.js,
// inlined above). The lens only touches opacity on already-rendered nodes;
// it never changes activeTypes / q3Only and silently resets on rebuild().
const searchInput = document.getElementById('search-input');
const statusEl = document.getElementById('search-status');

function setStatus(msg) {
  statusEl.textContent = msg || '';
  statusEl.style.display = msg ? 'block' : 'none';
}

function lensReset() {
  gNodes.selectAll('circle').interrupt().attr('opacity', 1);
  gLinks.selectAll('line').interrupt().attr('opacity', 1);
}

// Highlight nodes passing matchFn; dim the rest. Edges stay lit only when
// both endpoints are highlighted (same rule as the Sociogram focus engine).
function applyLens(matchFn) {
  const inSet = {};
  visNodes.forEach(n => { if (matchFn(n)) inSet[n.id] = true; });
  gNodes.selectAll('circle').interrupt().attr('opacity', n => inSet[n.id] ? 1 : 0.08);
  gLinks.selectAll('line').interrupt().attr('opacity', e => (inSet[idOf(e.source)] && inSet[idOf(e.target)]) ? 1 : 0.05);
  return Object.keys(inSet).length;
}

function nodeHaystack(n) {
  return (n.name + ' ' + n.id + ' ' + n.type + ' ' + (n.subtype || '') + ' ' + (n.country || '') + ' ' +
    (n.description || '') + ' ' + (n.problem || '') + ' ' + (n.resource || '') + ' ' + (n.solution || '')).toLowerCase();
}

const TYPE_LIST = Object.keys(TYPE_COLORS);

// Resolve one side of a focus expression to a set of type names.
// Comma-separated segments, each a case-insensitive substring of a type name.
function resolveTypeSide(txt) {
  const out = new Set();
  String(txt || '').split(',').map(s => s.trim().toLowerCase()).filter(Boolean).forEach(seg => {
    TYPE_LIST.forEach(t => { if (t.toLowerCase().indexOf(seg) !== -1) out.add(t); });
  });
  return out;
}

function runFocus(afterPrefix) {
  const sides = String(afterPrefix || '').split('~');
  if (sides.length < 2) {
    const one = resolveTypeSide(sides[0]);
    if (!one.size) {
      setStatus('Focus syntax: focus: <type> ~ <type> (e.g. "focus: civic ~ scientific") or focus: <type> to isolate one. Types: ' + TYPE_LIST.join(', ') + '.');
      return;
    }
    const count = applyLens(n => one.has(n.type));
    setStatus('Focus "' + [...one].join(', ') + '": highlighted ' + count + ' communities. Clear to restore.');
    return;
  }
  const A = resolveTypeSide(sides[0]);
  const B = resolveTypeSide(sides[1]);
  if (!A.size || !B.size) {
    setStatus('Focus: could not resolve a community type on each side of "~". Types: ' + TYPE_LIST.join(', ') + '.');
    return;
  }
  const cross = {};
  visEdges.forEach(e => {
    const s = nodeById[idOf(e.source)], t = nodeById[idOf(e.target)];
    if ((A.has(s.type) && B.has(t.type)) || (A.has(t.type) && B.has(s.type))) { cross[s.id] = true; cross[t.id] = true; }
  });
  const lbl = [...A].join(', ') + ' ~ ' + [...B].join(', ');
  const count = applyLens(n => cross[n.id]);
  if (!count) setStatus('Focus "' + lbl + '": no cross-type links among visible communities. Check the type filters at left.');
  else setStatus('Focus "' + lbl + '": isolated ' + count + ' communities linked across the two type sets. Clear to restore.');
}

const C2A2_CE_SYSTEM_DATASET = 'You are a retrieval assistant for the C2A2 Community Explorer. Each candidate line is a community: id | name | type | excerpt. Pick the most relevant ids and write a brief grounded answer using ONLY the candidates. Reply with ONE JSON object and nothing else: {"ids":["<id>", ... up to 12 most relevant], "answer":"2-3 sentence summary grounded in the candidates"}.';
const C2A2_CE_SYSTEM_WEB = 'You are a retrieval assistant for the C2A2 Community Explorer. Each candidate line is a community: id | name | type | excerpt. A WEB_CONTEXT block of up to 5 web snippets will be appended. Pick the most relevant candidate ids and write a brief answer; when you draw on a web snippet, cite it [1], [2], etc. Pick ids only from the candidates. Reply with ONE JSON object: {"ids":["<id>", ... up to 12 most relevant], "answer":"2-4 sentence summary with bracket citations where applicable"}.';

function runSearchAI(rawQuery) {
  if (!window.C2A2Search || typeof window.C2A2Search.enrich !== 'function') {
    setStatus('Search module not loaded.');
    return;
  }
  const query = String(rawQuery || '').trim();
  if (!query) return;
  const extBox = document.getElementById('search-external');
  const useWeb = !!(extBox && extBox.checked);

  // Pre-rank visible nodes by term overlap; trim to 30 for the prompt budget.
  const qTerms = query.toLowerCase().split(/\\s+/).filter(Boolean);
  let scored = [];
  visNodes.forEach(n => {
    const hay = nodeHaystack(n);
    let s = 0;
    qTerms.forEach(t => { if (hay.indexOf(t) !== -1) s += 1; });
    if (s > 0) scored.push({ n: n, s: s });
  });
  scored.sort((a, b) => b.s - a.s);
  scored = scored.slice(0, 30);
  if (!scored.length) {
    setStatus('No visible communities match "' + query + '". Try a different query or expand the type filters at left.');
    return;
  }
  const summary = scored.map(x => {
    const n = x.n;
    const snip = String((n.description || '') + ' ' + (n.problem || '')).replace(/\\s+/g, ' ').slice(0, 200);
    return n.id + ' | ' + n.name + ' | ' + n.type + ' | ' + snip;
  }).join('\\n');
  const userBlock = 'Query: ' + query + '\\n\\nCandidates:\\n' + summary;

  setStatus('Asking C2A2 (' + (useWeb ? 'database + web' : 'database') + ') ...');

  window.C2A2Search.enrich({
    useWeb: useWeb,
    dataset: { system: C2A2_CE_SYSTEM_DATASET, user: userBlock },
    web: useWeb ? { system: C2A2_CE_SYSTEM_WEB, user: userBlock } : null,
  }).then(res => {
    const content = (res.payload && typeof res.payload.text === 'string') ? res.payload.text : '';
    const m = content.match(/\\{[\\s\\S]*\\}/);
    if (!m) { setStatus('AI returned a response that could not be parsed. Uncheck "Ask AI" to use local search.'); return; }
    let parsed;
    try { parsed = JSON.parse(m[0]); } catch (e) { setStatus('AI response JSON parse failed.'); return; }
    const pickedIds = Array.isArray(parsed.ids) ? parsed.ids : [];
    const pickedSet = {};
    pickedIds.forEach(id => pickedSet[id] = true);
    applyLens(n => pickedSet[n.id]);

    const modeLabel = res.mode === 'database-plus-web-cited' ? ' [web + database]'
      : res.mode === 'database-only-after-cap' ? ' [database -- web cap reached]'
      : res.mode === 'external-search-unavailable' ? ' [database -- web unavailable]'
      : ' [database]';
    const warning = res.warning ? (' ' + res.warning) : '';
    const modelLabel = (res.payload && res.payload.model) ? (' (model: ' + res.payload.model + ')') : '';
    let sourcesLine = '';
    if (Array.isArray(res.payload && res.payload.sources) && res.payload.sources.length) {
      sourcesLine = ' Sources: ' + res.payload.sources.map((s, i) => '[' + (i + 1) + '] ' + (s.title || s.url || '')).join(' | ');
    }
    const answer = parsed.answer || '(no answer text)';
    setStatus('Ask "' + query + '"' + modeLabel + modelLabel + ':' + warning + ' ' + answer + sourcesLine);
  }).catch(err => {
    const code = (err && err.message) || 'unknown';
    setStatus('AI request failed (' + code + '). Uncheck "Ask AI" to fall back to local search.');
  });
}

function runSearch() {
  const raw = searchInput.value.trim();
  if (!raw) { lensReset(); setStatus(''); return; }
  // Deterministic relational focus command; explicit prefix never collides
  // with substring search, and overrides AI mode (same rule as Sociogram).
  if (raw.toLowerCase().indexOf('focus:') === 0) {
    runFocus(raw.slice(raw.indexOf(':') + 1));
    return;
  }
  const aiBox = document.getElementById('search-ai-mode');
  if (aiBox && aiBox.checked) { runSearchAI(raw); return; }
  const q = raw.toLowerCase();
  const count = applyLens(n => nodeHaystack(n).indexOf(q) !== -1);
  setStatus('Search "' + raw + '": ' + count + ' of ' + visNodes.length + ' visible communities. Clear to restore.');
}

// ── Tabs help modal ("?" beside the Graph|Cards toggle) ───────────────────
// Text mirrors wiki/architecture/explorer_tabs_complementarity.md (the source
// of truth); edit that doc and regenerate to keep them aligned.
const helpModal = document.getElementById('help-modal');
document.getElementById('tabs-help').addEventListener('click', () => helpModal.classList.add('open'));
document.getElementById('help-close').addEventListener('click', () => helpModal.classList.remove('open'));
helpModal.addEventListener('click', ev => { if (ev.target === helpModal) helpModal.classList.remove('open'); });
document.addEventListener('keydown', ev => { if (ev.key === 'Escape') helpModal.classList.remove('open'); });

document.getElementById('btn-search').addEventListener('click', runSearch);
document.getElementById('btn-clear').addEventListener('click', () => { searchInput.value = ''; runSearch(); });
searchInput.addEventListener('keydown', ev => { if (ev.key === 'Enter') runSearch(); });

// ── Graph / Cards sub-tabs ─────────────────────────────────────────────────
const tabGraph = document.getElementById('tab-graph');
const tabCards = document.getElementById('tab-cards');
const cardsView = document.getElementById('cardsview');
const graphWrap = document.getElementById('graphwrap');
const leftPanel = document.getElementById('leftpanel');
const footerEl = document.getElementById('footer');
// The Hold/Names/Fit buttons + node/edge stats are graph-only; the Cards app has
// its own controls, so this group is hidden on the Cards sub-tab.
const graphControls = document.getElementById('graph-controls');
tabGraph.addEventListener('click', () => {
  tabGraph.classList.add('active'); tabCards.classList.remove('active');
  cardsView.style.display = 'none';
  graphWrap.style.display = ''; leftPanel.style.display = '';
  footerEl.style.display = '';
  graphControls.style.display = '';
});
tabCards.addEventListener('click', () => {
  tabCards.classList.add('active'); tabGraph.classList.remove('active');
  const fr = cardsView.querySelector('iframe');
  if (!fr.getAttribute('src')) fr.setAttribute('src', fr.getAttribute('data-src'));
  graphWrap.style.display = 'none'; leftPanel.style.display = 'none';
  rp.classList.remove('open');
  cardsView.style.display = 'block';
  // The cards app carries its own search + Ask AI pipeline + controls; hide ours.
  footerEl.style.display = 'none';
  graphControls.style.display = 'none';
});

window.addEventListener('resize', () => { if (sim) sim.force('center', d3.forceCenter(width() / 2, height() / 2)); });

rebuild();
</script>
</body>
</html>
"""


def main():
    with open(INPUT_PATH, encoding="utf-8") as f:
        graph = json.load(f)

    graph_json = json.dumps(graph, ensure_ascii=False)
    colors_json = json.dumps(TYPE_COLORS, ensure_ascii=False)
    searchlib_js = SEARCHLIB_PATH.read_text(encoding="utf-8")

    html = (HTML_HEAD + graph_json + HTML_TAIL + colors_json
            + HTML_AFTER_COLORS + searchlib_js + HTML_BODY)

    OUTPUT_PATH.write_text(html, encoding="utf-8")
    kb = OUTPUT_PATH.stat().st_size / 1024
    print("Nodes:", graph["meta"]["node_count"], "Edges:", graph["meta"]["edge_count"])
    print("Written", OUTPUT_PATH, "(", round(kb, 1), "KB ) on", date.today())


if __name__ == "__main__":
    main()
