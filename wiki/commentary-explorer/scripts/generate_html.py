#!/usr/bin/env python3
"""
Commentary Explorer — HTML generator.

Reads bundle.json (produced by build_bundle.py) and emits a single
self-contained HTML file with:
  - D3 force-directed graph (chapter nodes + satellite halos)
  - Right panel reader with breadcrumb / nav stack (Esc, Shift+Esc, Back)
  - Markdown rendering via marked.js (CDN)
  - Auto-rendered [[wiki-links]] inside satellite bodies
  - Filters: chapter/satellite-kind toggles
  - Graph pulse / centering when navigating cross-link

Usage:
  python3 generate_html.py BUNDLE_JSON OUT_HTML

Per CLAUDE.md template rules:
  - The HTML template is a regular string (NOT an f-string)
  - JSON is injected via "" + json_var + "" concatenation
  - All CSS/JS uses single braces { } (never {{ }})
"""

import argparse, json, pathlib, sys

# ---------- HTML template (regular string; do NOT make this an f-string) ------

TEMPLATE_HEAD = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Commentary Explorer — Three Rival Versions of Moral Enquiry</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.9.0/d3.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js"></script>
<style>
:root {
  --bg: #0a0a0f;
  --bg-panel: #111118;
  --bg-panel-2: #181822;
  --fg: #e8e8ee;
  --fg-dim: #9b9ba8;
  --fg-muted: #6e6e7e;
  --accent: #c9a84c;
  --border: #2a2a36;
  --link: #8ec5ff;
  --warn: #ff9f43;
  --chapter: #5B7FA5;
  --thinker: #C45B5B;
  --prs: #8B6DAE;
  --summa: #C9A84C;
}
* { box-sizing: border-box; }
html, body {
  margin: 0; padding: 0; height: 100%;
  background: var(--bg);
  color: var(--fg);
  font: 14px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
}
header {
  position: fixed; top: 0; left: 0; right: 0; height: 44px;
  background: var(--bg-panel);
  border-bottom: 1px solid var(--border);
  display: flex; align-items: center; padding: 0 14px; z-index: 50;
  gap: 14px;
}
header h1 { font-size: 14px; font-weight: 600; margin: 0; color: var(--fg); letter-spacing: 0.02em; }
header h1 .sub { color: var(--fg-dim); font-weight: 400; margin-left: 8px; }
header .stats { color: var(--fg-muted); font-size: 12px; margin-left: auto; }
.layout {
  position: fixed; top: 44px; left: 0; right: 0; bottom: 0;
  display: grid; grid-template-columns: 220px 1fr 460px;
}
#filters {
  background: var(--bg-panel);
  border-right: 1px solid var(--border);
  padding: 12px 14px; overflow-y: auto;
}
#filters h2 { font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--fg-muted); margin: 14px 0 6px; }
#filters h2:first-child { margin-top: 0; }
.filter-row {
  display: flex; align-items: center; gap: 8px;
  font-size: 12px; padding: 3px 0; cursor: pointer; user-select: none;
}
.filter-row input { accent-color: var(--accent); }
.filter-row .swatch { width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }
.filter-row .label { flex: 1; color: var(--fg); }
.filter-row .count { color: var(--fg-muted); font-variant-numeric: tabular-nums; }
.filter-row:hover .label { color: var(--accent); }

#graph { position: relative; background: var(--bg); overflow: hidden; }
#graph svg { width: 100%; height: 100%; display: block; cursor: grab; }
#graph svg:active { cursor: grabbing; }
#graph .controls {
  position: absolute; top: 12px; right: 12px; display: flex; gap: 6px;
  background: var(--bg-panel); border: 1px solid var(--border);
  padding: 6px; border-radius: 6px; z-index: 10;
}
#graph .controls button {
  background: var(--bg-panel-2); color: var(--fg); border: 1px solid var(--border);
  padding: 4px 10px; border-radius: 4px; font-size: 11px; cursor: pointer;
}
#graph .controls button:hover { border-color: var(--accent); color: var(--accent); }

.node-label {
  font-size: 11px; fill: var(--fg-dim); pointer-events: none;
  paint-order: stroke; stroke: var(--bg); stroke-width: 3;
}
.node-label.chapter { fill: var(--fg); font-weight: 600; }
.node-label.hidden { display: none; }

.link { stroke-opacity: 0.35; }
.link.hi { stroke-opacity: 0.95; }
.node circle { stroke: rgba(255,255,255,0.18); stroke-width: 1; cursor: pointer; }
.node:hover circle { stroke: var(--accent); stroke-width: 2; }
.node.selected circle { stroke: var(--accent); stroke-width: 2.5; }
.node.pulse circle { animation: pulse 0.9s ease-out; }
@keyframes pulse {
  0% { stroke-width: 2; stroke: var(--accent); }
  50% { stroke-width: 8; stroke: var(--accent); }
  100% { stroke-width: 2.5; stroke: var(--accent); }
}

#panel {
  background: var(--bg-panel);
  border-left: 1px solid var(--border);
  display: flex; flex-direction: column;
  overflow: hidden;
}
#crumbs {
  padding: 10px 14px;
  border-bottom: 1px solid var(--border);
  background: var(--bg-panel-2);
  font-size: 12px;
  display: flex; align-items: center; gap: 6px;
  overflow-x: auto; white-space: nowrap;
}
#crumbs .back-btn {
  background: var(--bg-panel); color: var(--fg); border: 1px solid var(--border);
  padding: 2px 8px; border-radius: 4px; font-size: 11px; cursor: pointer;
  font-family: inherit;
}
#crumbs .back-btn:disabled { opacity: 0.35; cursor: default; }
#crumbs .back-btn:hover:not(:disabled) { border-color: var(--accent); color: var(--accent); }
#crumbs .crumb { color: var(--fg-dim); cursor: pointer; padding: 1px 4px; border-radius: 3px; }
#crumbs .crumb:hover { background: var(--bg); color: var(--fg); }
#crumbs .crumb.current { color: var(--accent); cursor: default; }
#crumbs .sep { color: var(--fg-muted); }
#crumbs .esc-hint { color: var(--fg-muted); margin-left: auto; font-size: 11px; padding-left: 12px; }

#body { flex: 1; padding: 18px 22px; overflow-y: auto; }
#body h1 { font-size: 18px; margin: 0 0 6px; color: var(--fg); }
#body h2 { font-size: 14px; margin: 18px 0 6px; color: var(--accent); border-bottom: 1px solid var(--border); padding-bottom: 4px; }
#body h3 { font-size: 13px; margin: 14px 0 4px; color: var(--fg); }
#body h4 { font-size: 12px; margin: 10px 0 2px; color: var(--fg-dim); }
#body p { margin: 6px 0; color: var(--fg); }
#body em { color: var(--fg-dim); }
#body code { background: var(--bg); padding: 1px 4px; border-radius: 3px; font-size: 12px; }
#body blockquote {
  margin: 8px 0; padding: 6px 12px; background: var(--bg);
  border-left: 3px solid var(--accent); color: var(--fg-dim);
  font-size: 12px; border-radius: 3px;
}
#body ul, #body ol { padding-left: 22px; }
#body a { color: var(--link); text-decoration: none; }
#body a:hover { text-decoration: underline; }
#body .wikilink {
  color: var(--accent); cursor: pointer; border-bottom: 1px dotted currentColor;
}
#body .wikilink:hover { background: rgba(201,168,76,0.12); }
#body .wikilink.dead { color: var(--fg-muted); border-bottom-style: dashed; cursor: not-allowed; }

.page-block {
  margin: 14px 0; border: 1px solid var(--border); border-radius: 4px;
  background: var(--bg-panel-2); overflow: hidden;
}
.page-block summary {
  padding: 8px 12px; cursor: pointer; user-select: none;
  background: var(--bg-panel); display: flex; align-items: center; gap: 10px;
  font-size: 12px;
}
.page-block summary .pno { color: var(--accent); font-weight: 600; min-width: 60px; }
.page-block summary .pdesc { color: var(--fg-dim); flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.page-block summary .acount { color: var(--fg-muted); font-size: 11px; }
.page-block .page-summary {
  padding: 8px 12px; color: var(--fg-dim); font-size: 12px; font-style: italic;
  border-bottom: 1px solid var(--border);
}
.ann {
  border-top: 1px solid var(--border); padding: 8px 12px;
}
.ann:first-of-type { border-top: 0; }
.ann .ann-head {
  font-size: 11px; color: var(--fg-muted); margin-bottom: 4px;
  display: flex; align-items: center; gap: 8px;
}
.ann .ann-head .annid { color: var(--accent); font-weight: 600; }
.ann .ann-head .anntype {
  background: var(--bg); padding: 1px 6px; border-radius: 3px;
  text-transform: lowercase; font-size: 10px; letter-spacing: 0.04em;
}
.ann .anchor {
  font-style: italic; color: var(--fg);
  border-left: 2px solid var(--accent); padding-left: 8px; margin: 4px 0;
  font-size: 12px;
}
.ann .interp { font-size: 12px; color: var(--fg); margin: 4px 0; }
.ann .rcrel  { font-size: 12px; color: var(--fg-dim); margin: 4px 0; }
.ann .rcrel::before { content: "RC: "; color: var(--accent); font-weight: 600; }

.ocr-block {
  margin: 8px 12px 0; border: 1px solid var(--border); border-radius: 4px;
  background: var(--bg); overflow: hidden;
}
.ocr-block summary {
  padding: 6px 10px; cursor: pointer; user-select: none;
  font-size: 11px; color: var(--fg-muted);
  background: var(--bg-panel-2); display: flex; gap: 8px; align-items: center;
}
.ocr-block summary .ocr-tag {
  background: var(--bg); padding: 1px 6px; border-radius: 3px;
  color: var(--accent); font-size: 10px; letter-spacing: 0.04em;
}
.ocr-block summary .ocr-stat { color: var(--fg-muted); font-size: 10px; }
.ocr-text {
  font: 11px/1.4 ui-monospace, "SF Mono", Menlo, monospace;
  white-space: pre-wrap; word-wrap: break-word;
  color: var(--fg-dim); padding: 8px 12px; max-height: 360px; overflow-y: auto;
}
.ocr-text mark {
  background: rgba(201,168,76,0.28); color: var(--fg);
  padding: 0 2px; border-radius: 2px; cursor: pointer;
}
.ocr-text mark.exact { background: rgba(78,138,94,0.32); }
.ocr-text mark:hover { background: rgba(201,168,76,0.55); }
.ocr-text mark.flash { animation: flash 1.2s ease-out; }
@keyframes flash {
  0% { background: rgba(201,168,76,0.95); }
  100% { background: rgba(201,168,76,0.28); }
}
.ocr-disclaimer {
  font-size: 10px; color: var(--fg-muted); padding: 4px 12px;
  border-top: 1px solid var(--border); font-style: italic;
}
.ann.flash { background: rgba(201,168,76,0.06); transition: background 1s; }

.satellite-meta {
  font-size: 11px; color: var(--fg-muted);
  background: var(--bg); padding: 6px 10px; border-radius: 4px; margin-bottom: 10px;
  display: flex; gap: 12px; flex-wrap: wrap;
}
.satellite-meta b { color: var(--fg-dim); font-weight: 500; }

.empty-hint { color: var(--fg-muted); font-style: italic; padding: 30px 0; text-align: center; }
</style>
</head>
<body>
<header>
  <h1>Commentary Explorer <span class="sub">— Three Rival Versions of Moral Enquiry · MacIntyre 1990</span></h1>
  <div class="stats" id="stats"></div>
</header>
<div class="layout">
  <aside id="filters"></aside>
  <main id="graph">
    <div class="controls">
      <button id="btn-fit">Fit</button>
      <button id="btn-freeze">Freeze</button>
      <button id="btn-labels">Labels</button>
    </div>
    <svg></svg>
  </main>
  <aside id="panel">
    <div id="crumbs">
      <button class="back-btn" id="btn-back" title="Esc — go back">← Back</button>
      <div id="crumb-trail"></div>
      <span class="esc-hint">Esc · Shift+Esc</span>
    </div>
    <div id="body">
      <div class="empty-hint">Click a chapter or satellite node to begin.</div>
    </div>
  </aside>
</div>
<script>
window.BUNDLE = """

TEMPLATE_TAIL = r""";
// ============================================================================
// Commentary Explorer — frontend
// ============================================================================
(function(){
  const B = window.BUNDLE;

  // --- Chapter labelling ---
  // Convention from TRV 1990 Notre Dame edition:
  //   number = -1  → Preface (front matter)
  //   number =  0  → Introduction
  //   number 1..10 → Chapter I, Chapter II, ... Chapter X
  const ROMAN = ['', 'I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII'];
  function chapterShortLabel(c){
    if (c.number === -1) return 'Preface';
    if (c.number === 0)  return 'Introduction';
    return 'Ch. ' + (ROMAN[c.number] || c.number);
  }
  function chapterLabel(c){
    if (c.number === -1) return 'Preface';
    if (c.number === 0)  return 'Introduction';
    return 'Chapter ' + (ROMAN[c.number] || c.number);
  }

  // --- Stats ---
  const stats = document.getElementById('stats');
  const totalAnn = B.chapters.reduce((s,c)=>s+c.annotation_count, 0);
  stats.textContent = B.chapters.length + ' chapters · '
    + totalAnn + ' annotations · '
    + B.satellites.length + ' satellites · '
    + B.edges.length + ' edges';

  // --- Build node + link arrays for D3 ---
  // Chapter nodes (centered cluster)
  const chapColor = '#5B7FA5';
  const chapNodes = B.chapters.map((c, i) => ({
    id: c.id, kind: 'chapter', label: c.title,
    color: chapColor,
    chapter: c,
    radius: Math.max(14, Math.min(34, 8 + Math.sqrt(c.annotation_count))),
    initX: 0, initY: (i - B.chapters.length/2) * 60,
  }));
  // Satellite nodes (halo around chapters)
  const satNodes = B.satellites.map(s => ({
    id: s.id, kind: s.kind, label: s.title,
    color: s.color || '#888', satellite: s,
    radius: 9 + (s.kind === 'thinker' ? 3 : 0),
    initX: 350, initY: 0,
  }));
  const allNodes = chapNodes.concat(satNodes);
  const idx = new Map(allNodes.map(n => [n.id, n]));
  const links = B.edges
    .filter(e => idx.has(e.from) && idx.has(e.to))
    .map(e => ({
      source: e.from, target: e.to, weight: e.weight,
      evidence: e.evidence || [],
    }));

  // --- Filter UI ---
  const filtersEl = document.getElementById('filters');
  const chapShown = new Set(B.chapters.map(c => c.id));
  const satKindShown = new Set(['thinker', 'prs', 'summa', 'summa-transcript']);

  function renderFilters(){
    let html = '<h2>Chapters</h2>';
    for (const c of B.chapters){
      html += '<label class="filter-row">'
        + '<input type="checkbox" data-kind="chap" data-id="' + c.id + '" '
        + (chapShown.has(c.id) ? 'checked' : '') + '>'
        + '<span class="swatch" style="background:' + chapColor + '"></span>'
        + '<span class="label">' + (chapterLabel(c)) + '</span>'
        + '<span class="count">' + c.annotation_count + '</span>'
        + '</label>';
    }
    html += '<h2>Satellites</h2>';
    const kindLabels = {
      'thinker': 'Thinker wikis',
      'prs': 'PRS triplets',
      'summa': 'Summa entries',
      'summa-transcript': 'Summa transcripts',
    };
    const kindCounts = {};
    for (const s of B.satellites){ kindCounts[s.kind] = (kindCounts[s.kind] || 0) + 1; }
    for (const kind of Object.keys(kindLabels)){
      if (!(kind in kindCounts)) continue;
      const sample = B.satellites.find(s => s.kind === kind);
      html += '<label class="filter-row">'
        + '<input type="checkbox" data-kind="sat" data-id="' + kind + '" '
        + (satKindShown.has(kind) ? 'checked' : '') + '>'
        + '<span class="swatch" style="background:' + (sample ? sample.color : '#888') + '"></span>'
        + '<span class="label">' + kindLabels[kind] + '</span>'
        + '<span class="count">' + kindCounts[kind] + '</span>'
        + '</label>';
    }
    filtersEl.innerHTML = html;
    filtersEl.querySelectorAll('input').forEach(inp => {
      inp.addEventListener('change', e => {
        const k = e.target.dataset.kind, id = e.target.dataset.id;
        if (k === 'chap'){
          if (e.target.checked) chapShown.add(id); else chapShown.delete(id);
        } else {
          if (e.target.checked) satKindShown.add(id); else satKindShown.delete(id);
        }
        applyFilters();
      });
    });
  }
  renderFilters();

  // --- D3 graph ---
  const svg = d3.select('#graph svg');
  const W = svg.node().clientWidth, H = svg.node().clientHeight;
  svg.attr('viewBox', [-W/2, -H/2, W, H]);
  const root = svg.append('g').attr('class', 'root');

  // zoom
  const zoom = d3.zoom().scaleExtent([0.2, 4])
    .on('zoom', ev => root.attr('transform', ev.transform));
  svg.call(zoom);

  // Initial positions: chapters in vertical column at left-center, satellites scattered to right
  for (const n of chapNodes){
    n.x = -180; n.y = (n.chapter.number - B.chapters.length/2) * 70;
  }
  for (const n of satNodes){
    const ang = (Math.random() - 0.5) * Math.PI;
    const r = 280 + Math.random()*140;
    n.x = Math.cos(ang) * r + 80; n.y = Math.sin(ang) * r;
  }

  const linkSel = root.append('g')
    .attr('class', 'links')
    .selectAll('line')
    .data(links, d => d.source + '|' + d.target)
    .join('line')
      .attr('class', 'link')
      .attr('stroke', d => idx.get(d.target).color)
      .attr('stroke-width', d => 0.6 + Math.log(1 + d.weight) * 0.8);

  const nodeSel = root.append('g')
    .attr('class', 'nodes')
    .selectAll('g')
    .data(allNodes, d => d.id)
    .join('g')
      .attr('class', d => 'node ' + d.kind)
      .on('click', (e, d) => {
        e.stopPropagation();
        if (d.kind === 'chapter') openChapter(d.chapter, true);
        else openSatellite(d.satellite, true);
      })
      .call(d3.drag()
        .on('start', (e, d) => {
          if (!e.active) simulation.alphaTarget(0.3).restart();
          d.fx = d.x; d.fy = d.y;
        })
        .on('drag', (e, d) => { d.fx = e.x; d.fy = e.y; })
        .on('end', (e, d) => {
          if (!e.active) simulation.alphaTarget(0);
          if (!frozen){ d.fx = null; d.fy = null; }
        })
      );
  nodeSel.append('circle')
    .attr('r', d => d.radius)
    .attr('fill', d => d.color);

  const labelSel = root.append('g')
    .attr('class', 'labels')
    .selectAll('text')
    .data(allNodes, d => d.id)
    .join('text')
      .attr('class', d => 'node-label ' + d.kind)
      .attr('text-anchor', 'middle')
      .attr('dy', d => -d.radius - 4)
      .text(d => {
        if (d.kind === 'chapter'){
          return chapterShortLabel(d.chapter);
        }
        return d.label;
      });

  const simulation = d3.forceSimulation(allNodes)
    .force('charge', d3.forceManyBody().strength(d => d.kind === 'chapter' ? -380 : -180))
    .force('link', d3.forceLink(links).id(d => d.id).distance(d => 110 + 4 / Math.log(2 + d.weight)).strength(0.4))
    .force('collide', d3.forceCollide().radius(d => d.radius + 6).strength(0.85))
    .force('x', d3.forceX(d => d.kind === 'chapter' ? -180 : 100).strength(0.04))
    .force('y', d3.forceY(0).strength(0.03))
    .on('tick', () => {
      linkSel
        .attr('x1', d => d.source.x).attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x).attr('y2', d => d.target.y);
      nodeSel.attr('transform', d => 'translate(' + d.x + ',' + d.y + ')');
      labelSel.attr('transform', d => 'translate(' + d.x + ',' + d.y + ')');
    });

  let frozen = false;
  let labelsVisible = true;

  function applyFilters(){
    nodeSel.style('display', d => {
      if (d.kind === 'chapter') return chapShown.has(d.id) ? null : 'none';
      return satKindShown.has(d.kind) ? null : 'none';
    });
    labelSel.style('display', d => {
      const visible = d.kind === 'chapter' ? chapShown.has(d.id) : satKindShown.has(d.kind);
      return (visible && labelsVisible) ? null : 'none';
    });
    linkSel.style('display', d => {
      const sv = d.source.kind === 'chapter' ? chapShown.has(d.source.id) : satKindShown.has(d.source.kind);
      const tv = d.target.kind === 'chapter' ? chapShown.has(d.target.id) : satKindShown.has(d.target.kind);
      return (sv && tv) ? null : 'none';
    });
  }
  applyFilters();

  document.getElementById('btn-fit').addEventListener('click', () => {
    const bbox = root.node().getBBox();
    const cx = bbox.x + bbox.width/2, cy = bbox.y + bbox.height/2;
    const scale = Math.min(W / (bbox.width + 80), H / (bbox.height + 80), 1.5);
    svg.transition().duration(500)
      .call(zoom.transform, d3.zoomIdentity.translate(-cx*scale, -cy*scale).scale(scale));
  });
  document.getElementById('btn-freeze').addEventListener('click', e => {
    frozen = !frozen;
    e.target.textContent = frozen ? 'Unfreeze' : 'Freeze';
    if (frozen){
      allNodes.forEach(n => { n.fx = n.x; n.fy = n.y; });
      simulation.alphaTarget(0).stop();
    } else {
      allNodes.forEach(n => { n.fx = null; n.fy = null; });
      simulation.alphaTarget(0.1).restart();
    }
  });
  document.getElementById('btn-labels').addEventListener('click', e => {
    labelsVisible = !labelsVisible;
    e.target.textContent = labelsVisible ? 'Labels' : 'Labels (hidden)';
    applyFilters();
  });

  // --- Navigation stack ---
  const navStack = [];   // history (back stack)
  const fwdStack = [];   // forward stack

  function pushFrame(frame, fromUserClick){
    if (fromUserClick) fwdStack.length = 0;
    navStack.push(frame);
    renderFrame(frame);
    selectNodeOnGraph(frame.nodeId, fromUserClick);
  }
  function back(){
    if (navStack.length <= 1) return;
    const cur = navStack.pop();
    fwdStack.push(cur);
    const prev = navStack[navStack.length - 1];
    renderFrame(prev);
    selectNodeOnGraph(prev.nodeId, false);
  }
  function forward(){
    if (!fwdStack.length) return;
    const f = fwdStack.pop();
    navStack.push(f);
    renderFrame(f);
    selectNodeOnGraph(f.nodeId, false);
  }

  document.getElementById('btn-back').addEventListener('click', back);

  document.addEventListener('keydown', e => {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
    if (e.key === 'Escape'){
      e.preventDefault();
      if (e.shiftKey) forward(); else back();
    }
  });

  function openChapter(c, fromUserClick){
    pushFrame({
      kind: 'chapter', nodeId: c.id, title: c.title,
      crumbLabel: chapterShortLabel(c),
    }, fromUserClick);
  }
  function openSatellite(s, fromUserClick){
    pushFrame({
      kind: 'satellite', nodeId: s.id, title: s.title,
      crumbLabel: s.title,
    }, fromUserClick);
  }
  function jumpToChapterPage(chapId, page){
    const c = B.chapters.find(c => c.id === chapId);
    if (!c) return;
    openChapter(c, true);
    setTimeout(() => {
      const det = document.querySelector('details[data-page="' + page + '"]');
      if (det){ det.open = true; det.scrollIntoView({behavior:'smooth', block:'center'}); }
    }, 50);
  }

  // --- Render frame to right panel ---
  const trailEl = document.getElementById('crumb-trail');
  const bodyEl = document.getElementById('body');
  const backBtn = document.getElementById('btn-back');

  function renderFrame(frame){
    // Crumbs
    const parts = [];
    parts.push('<span class="sep">⌂</span>');
    for (let i = 0; i < navStack.length; i++){
      const f = navStack[i];
      const cls = (i === navStack.length - 1) ? 'crumb current' : 'crumb';
      parts.push('<span class="' + cls + '" data-i="' + i + '">' + escapeHtml(f.crumbLabel) + '</span>');
      if (i < navStack.length - 1) parts.push('<span class="sep">›</span>');
    }
    trailEl.innerHTML = parts.join(' ');
    trailEl.querySelectorAll('.crumb').forEach(el => {
      el.addEventListener('click', () => {
        const i = +el.dataset.i;
        if (i === navStack.length - 1) return;
        const target = navStack[i];
        // Pop everything after i onto fwdStack in reverse order
        while (navStack.length - 1 > i){
          fwdStack.push(navStack.pop());
        }
        renderFrame(target);
        selectNodeOnGraph(target.nodeId, false);
      });
    });
    backBtn.disabled = (navStack.length <= 1);

    // Body
    if (frame.kind === 'chapter'){
      bodyEl.innerHTML = renderChapterBody(B.chapters.find(c => c.id === frame.nodeId));
    } else {
      bodyEl.innerHTML = renderSatelliteBody(B.satellites.find(s => s.id === frame.nodeId));
    }
    bodyEl.scrollTop = 0;
    wireWikilinks();
    wireOcrMarks();
  }

  // Build the OCR block for a page — collapsible <details> with the OCR text
  // and inline <mark> spans for every annotation that has an ocr_match.
  function renderOcrBlock(p){
    const text = p.ocr_text;
    // Collect non-overlapping matches, sorted by start ascending.
    // If two matches overlap, keep the one with lower fuzziness; on tie, the longer.
    const candidates = [];
    for (const a of p.annotations){
      if (a.ocr_match){
        candidates.push({
          start: a.ocr_match.start,
          end: a.ocr_match.end,
          fuzz: a.ocr_match.fuzziness,
          ann_id: a.id,
        });
      }
    }
    candidates.sort((x, y) => x.start - y.start || x.end - y.end);
    const accepted = [];
    for (const c of candidates){
      if (accepted.length && c.start < accepted[accepted.length-1].end){
        // overlapping — keep whichever is "better"
        const prev = accepted[accepted.length-1];
        const prevSize = prev.end - prev.start;
        const curSize = c.end - c.start;
        if ((c.fuzz < prev.fuzz) || (c.fuzz === prev.fuzz && curSize > prevSize)){
          accepted[accepted.length-1] = c;
        }
        continue;
      }
      accepted.push(c);
    }
    // Build HTML by walking text; insert <mark> at accepted boundaries
    let html = '';
    let i = 0;
    for (const m of accepted){
      if (m.start > i) html += escapeHtml(text.slice(i, m.start));
      const cls = (m.fuzz === 0 ? 'exact' : '');
      html += '<mark class="' + cls + '" data-ann-id="' + m.ann_id + '" title="ann ' + m.ann_id + (m.fuzz>0 ? ' (fuzzy match)' : '') + '">'
            + escapeHtml(text.slice(m.start, m.end)) + '</mark>';
      i = m.end;
    }
    if (i < text.length) html += escapeHtml(text.slice(i));
    const matched = accepted.length;
    const total = p.annotations.length;
    let s = '<details class="ocr-block">';
    s += '<summary>'
       + '<span class="ocr-tag">PAGE TEXT (OCR)</span>'
       + '<span style="flex:1"></span>'
       + '<span class="ocr-stat">' + matched + ' / ' + total + ' anchors located</span>'
       + '</summary>';
    s += '<div class="ocr-text" id="ocr-' + p.page + '">' + html + '</div>';
    s += '<div class="ocr-disclaimer">Tesseract OCR of a scanned 1990 print — column drift and broken words are typical. Click a highlight to jump to its annotation; click an annotation\'s 📍 to flash its OCR location.</div>';
    s += '</details>';
    return s;
  }

  function renderChapterBody(c){
    let s = '<h1>' + escapeHtml(c.title) + '</h1>';
    s += '<div class="satellite-meta">';
    s += '<span><b>' + (chapterLabel(c)) + '</b></span>';
    s += '<span><b>PDF pp.</b> ' + c.pdf_pages[0] + '–' + c.pdf_pages[1] + '</span>';
    s += '<span><b>Annotated pages:</b> ' + c.annotated_page_count + '</span>';
    s += '<span><b>Annotations:</b> ' + c.annotation_count + '</span>';
    s += '<span><b>Title confidence:</b> ' + c.title_confidence + '</span>';
    s += '</div>';

    // Connection list (incoming/outgoing edges)
    const myEdges = B.edges.filter(e => e.from === c.id);
    if (myEdges.length){
      s += '<h2>Connections</h2><ul>';
      for (const e of myEdges){
        const sat = B.satellites.find(x => x.id === e.to);
        if (!sat) continue;
        s += '<li><span class="wikilink" data-target="' + sat.id + '">' + escapeHtml(sat.title) + '</span> '
           + '<span style="color:var(--fg-muted)">— ' + e.weight + ' references</span></li>';
      }
      s += '</ul>';
    }

    s += '<h2>Pages and Annotations</h2>';
    if (!c.pages.length){
      s += '<div class="empty-hint">No annotated pages in this chapter.</div>';
    }
    for (const p of c.pages){
      s += '<details class="page-block" data-page="' + p.page + '">';
      s += '<summary>'
         + '<span class="pno">p. ' + p.page + '</span>'
         + '<span class="pdesc">' + escapeHtml(p.summary.slice(0, 140)) + '…</span>'
         + '<span class="acount">' + p.annotations.length + ' ann</span>'
         + '</summary>';
      s += '<div class="page-summary">' + escapeHtml(p.summary) + '</div>';
      if (p.ocr_text){
        s += renderOcrBlock(p);
      }
      for (const a of p.annotations){
        s += '<div class="ann" id="ann-' + p.page + '-' + a.id.replace('.','_') + '" data-ann-id="' + a.id + '">';
        s += '<div class="ann-head">'
           + '<span class="annid">Ann ' + a.id + '</span>'
           + '<span class="anntype">' + escapeHtml(a.type || '?') + '</span>'
           + (a.ocr_match ? '<span class="anntype" title="anchor located in OCR">📍 located</span>' : '')
           + '</div>';
        if (a.anchor_text){
          let at = a.anchor_text.replace(/^_(.+)_$/, '$1');
          s += '<div class="anchor">' + escapeHtml(at) + '</div>';
        }
        if (a.content && a.content !== (a.anchor_text || '').replace(/^_(.+)_$/, '$1')){
          s += '<div class="ann" style="border:0;padding:0;color:var(--fg-dim);font-size:11px;margin:2px 0;">'
             + 'content: ' + escapeHtml(a.content.slice(0, 280)) + '</div>';
        }
        if (a.interpretation) s += '<div class="interp">' + linkifyBody(escapeHtml(a.interpretation)) + '</div>';
        if (a.rc_relevance)   s += '<div class="rcrel">' + linkifyBody(escapeHtml(a.rc_relevance)) + '</div>';
        s += '</div>';
      }
      s += '</details>';
    }
    return s;
  }

  function renderSatelliteBody(sat){
    if (!sat) return '<div class="empty-hint">Satellite not found.</div>';
    let s = '<div class="satellite-meta">';
    s += '<span><b>Kind:</b> ' + sat.kind + '</span>';
    if (sat.thinker) s += '<span><b>Thinker:</b> ' + sat.thinker + '</span>';
    if (sat.day !== undefined && sat.day !== null) s += '<span><b>Summa Day:</b> ' + sat.day + '</span>';
    s += '<span><b>Source:</b> <code>' + escapeHtml(sat.source_path.split('/').slice(-3).join('/')) + '</code></span>';
    s += '</div>';

    // Show evidence: which chapters connect to this satellite
    const incoming = B.edges.filter(e => e.to === sat.id);
    if (incoming.length){
      s += '<h2>Referenced from</h2><ul>';
      for (const e of incoming){
        const c = B.chapters.find(x => x.id === e.from);
        const cl = chapterShortLabel(c);
        s += '<li><span class="wikilink" data-target="' + e.from + '">'
           + escapeHtml(cl + ' — ' + c.title) + '</span> '
           + '<span style="color:var(--fg-muted)">— ' + e.weight + ' annotations</span>';
        // Top 3 evidence snippets
        if (e.evidence && e.evidence.length){
          s += '<ul style="margin-top:4px;">';
          for (const ev of e.evidence.slice(0, 3)){
            s += '<li style="font-size:11px;color:var(--fg-dim)">'
               + '<span class="wikilink" data-jump="' + e.from + ':' + ev.page + '">p. ' + ev.page + ' · ' + ev.ann + '</span>'
               + ' — “' + escapeHtml(ev.snippet.slice(0, 160)) + '…” '
               + '<i style="color:var(--fg-muted)">[matched: ' + escapeHtml(ev.key) + ']</i>'
               + '</li>';
          }
          s += '</ul>';
        }
        s += '</li>';
      }
      s += '</ul>';
    }

    s += '<h2>Bundled body</h2>';
    s += '<div class="md-body">' + linkifyBody(marked.parse(sat.body_md)) + '</div>';
    return s;
  }

  // --- Auto-link [[wiki-links]] and bare thinker names in body content ---
  // Build a map of likely targets: thinker surnames + Summa day titles + chapter titles
  const linkTargets = new Map();
  for (const sat of B.satellites){
    linkTargets.set(sat.title.toLowerCase(), sat.id);
    if (sat.thinker){
      // Map surname (last word of title) to satellite id
      const surname = sat.title.split(/[\s—–-]/).filter(Boolean).pop();
      if (surname) linkTargets.set(surname.toLowerCase(), sat.id);
    }
  }
  for (const c of B.chapters){
    linkTargets.set(c.title.toLowerCase(), c.id);
  }

  function linkifyBody(html){
    // Only convert [[Wiki Style]] links — leave plain text alone to avoid corrupting prose
    return html.replace(/\[\[([^\]]+)\]\]/g, (m, inner) => {
      const target = linkTargets.get(inner.trim().toLowerCase());
      if (target){
        return '<span class="wikilink" data-target="' + target + '">' + escapeHtml(inner) + '</span>';
      }
      return '<span class="wikilink dead" title="No node for this reference">' + escapeHtml(inner) + '</span>';
    });
  }

  // OCR <mark> ↔ annotation cross-flashing
  function wireOcrMarks(){
    document.querySelectorAll('.ocr-text mark[data-ann-id]').forEach(el => {
      el.addEventListener('click', () => {
        const annId = el.dataset.annId;
        // Find the page wrapping this mark, then the matching .ann inside
        const pageBlock = el.closest('.page-block');
        if (!pageBlock) return;
        pageBlock.open = true;
        const ann = pageBlock.querySelector('.ann[data-ann-id="' + annId + '"]');
        if (ann){
          ann.scrollIntoView({behavior: 'smooth', block: 'center'});
          ann.classList.remove('flash');
          void ann.offsetWidth;
          ann.classList.add('flash');
          setTimeout(() => ann.classList.remove('flash'), 1500);
        }
      });
    });
    // 📍 located badge: click to flash the OCR mark
    document.querySelectorAll('.ann').forEach(ann => {
      const annId = ann.dataset.annId;
      ann.querySelectorAll('.anntype').forEach(t => {
        if (t.textContent.includes('located')){
          t.style.cursor = 'pointer';
          t.addEventListener('click', () => {
            const pageBlock = ann.closest('.page-block');
            if (!pageBlock) return;
            const ocrBlock = pageBlock.querySelector('.ocr-block');
            if (ocrBlock) ocrBlock.open = true;
            const mark = pageBlock.querySelector('.ocr-text mark[data-ann-id="' + annId + '"]');
            if (mark){
              mark.scrollIntoView({behavior: 'smooth', block: 'center'});
              mark.classList.remove('flash');
              void mark.offsetWidth;
              mark.classList.add('flash');
              setTimeout(() => mark.classList.remove('flash'), 1500);
            }
          });
        }
      });
    });
  }

  function wireWikilinks(){
    document.querySelectorAll('.wikilink[data-target]').forEach(el => {
      el.addEventListener('click', () => {
        const id = el.dataset.target;
        const node = idx.get(id);
        if (!node) return;
        if (node.kind === 'chapter') openChapter(node.chapter, true);
        else openSatellite(node.satellite, true);
      });
    });
    document.querySelectorAll('.wikilink[data-jump]').forEach(el => {
      el.addEventListener('click', () => {
        const [cid, page] = el.dataset.jump.split(':');
        jumpToChapterPage(cid, +page);
      });
    });
  }

  // --- Graph node selection / pulse ---
  function selectNodeOnGraph(id, doPulse){
    nodeSel.classed('selected', d => d.id === id);
    nodeSel.classed('pulse', false);
    if (doPulse){
      nodeSel.filter(d => d.id === id).classed('pulse', true);
      // Recenter on the node
      const n = idx.get(id);
      if (n && typeof n.x === 'number'){
        const t = d3.zoomTransform(svg.node());
        const targetScale = Math.max(0.9, t.k);
        svg.transition().duration(500)
          .call(zoom.transform,
            d3.zoomIdentity.translate(-n.x * targetScale, -n.y * targetScale).scale(targetScale)
          );
      }
    }
    // Highlight incident edges
    linkSel.classed('hi', d => d.source.id === id || d.target.id === id);
  }

  // --- Helpers ---
  function escapeHtml(s){
    return String(s).replace(/[&<>"']/g, ch =>
      ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
  }

  // --- Initial fit after layout settles ---
  setTimeout(() => {
    document.getElementById('btn-fit').click();
  }, 1500);
})();
</script>
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("bundle_json")
    ap.add_argument("out_html")
    args = ap.parse_args()

    bundle_text = pathlib.Path(args.bundle_json).read_text(encoding="utf-8")
    # Sanity: must be valid JSON
    json.loads(bundle_text)

    html = TEMPLATE_HEAD + bundle_text + TEMPLATE_TAIL
    pathlib.Path(args.out_html).write_text(html, encoding="utf-8")
    print(f"[write] {args.out_html} ({pathlib.Path(args.out_html).stat().st_size} bytes)", file=sys.stderr)

if __name__ == "__main__":
    main()
