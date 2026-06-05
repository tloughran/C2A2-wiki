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
</style>
</head>
<body>
<div id="header">
  <h1>Community Explorer</h1>
  <button class="subtab active" id="tab-graph">Graph</button>
  <button class="subtab" id="tab-cards">Cards</button>
  <div id="spacer"></div>
  <span id="stats"></span>
  <button class="ctrl" id="btn-hold">Hold Forces</button>
  <button class="ctrl" id="btn-names">Show Names</button>
  <button class="ctrl" id="btn-fit">Fit All</button>
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
<script>
const GRAPH = """

HTML_TAIL = """;
const TYPE_COLORS = """  # noqa — second injection point

HTML_BODY = """;

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

// ── Graph / Cards sub-tabs ─────────────────────────────────────────────────
const tabGraph = document.getElementById('tab-graph');
const tabCards = document.getElementById('tab-cards');
const cardsView = document.getElementById('cardsview');
const graphWrap = document.getElementById('graphwrap');
const leftPanel = document.getElementById('leftpanel');
tabGraph.addEventListener('click', () => {
  tabGraph.classList.add('active'); tabCards.classList.remove('active');
  cardsView.style.display = 'none';
  graphWrap.style.display = ''; leftPanel.style.display = '';
});
tabCards.addEventListener('click', () => {
  tabCards.classList.add('active'); tabGraph.classList.remove('active');
  const fr = cardsView.querySelector('iframe');
  if (!fr.getAttribute('src')) fr.setAttribute('src', fr.getAttribute('data-src'));
  graphWrap.style.display = 'none'; leftPanel.style.display = 'none';
  rp.classList.remove('open');
  cardsView.style.display = 'block';
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

    html = HTML_HEAD + graph_json + HTML_TAIL + colors_json + HTML_BODY

    OUTPUT_PATH.write_text(html, encoding="utf-8")
    kb = OUTPUT_PATH.stat().st_size / 1024
    print("Nodes:", graph["meta"]["node_count"], "Edges:", graph["meta"]["edge_count"])
    print("Written", OUTPUT_PATH, "(", round(kb, 1), "KB ) on", date.today())


if __name__ == "__main__":
    main()
