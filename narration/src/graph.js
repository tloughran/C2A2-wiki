// D3 force-graph with temporal reveal, brightness control, and mention-based
// highlighting. Ported from the single-HTML version.
//
// Important D3 gotcha we hit before: `d3.forceLink().id(fn)` tells D3 to resolve
// source/target by looking up an id property — but our links use numeric
// indices. So we do NOT pass `.id()`. D3 defaults to numeric-index resolution
// which matches our data shape.

import * as d3 from 'd3';
import { getState, setState, subscribe } from './state.js';

let svg, g, linkSel, nodeSel, labelSel;
let simulation = null;
let zoom = null;
let width = 0, height = 0;

// Callbacks registered by other modules
let onNodeClick = () => {};

export function registerNodeClick(fn) { onNodeClick = fn; }

export function initGraph(container) {
  const rect = container.getBoundingClientRect();
  width = rect.width;
  height = rect.height;
  svg = d3.select('#graph')
    .attr('width', width)
    .attr('height', height)
    .attr('viewBox', [0, 0, width, height]);

  // Zoom + pan
  zoom = d3.zoom()
    .scaleExtent([0.2, 8])
    .on('zoom', (ev) => {
      g.attr('transform', ev.transform);
      // zoom/pan = user interaction; narration graph-sync should pause briefly
      setState({ userInteracted: true });
      clearTimeout(zoom._resetTimer);
      zoom._resetTimer = setTimeout(() => setState({ userInteracted: false }), 3000);
    });
  svg.call(zoom);

  g = svg.append('g');

  // Resize handler
  window.addEventListener('resize', () => {
    const r = container.getBoundingClientRect();
    width = r.width; height = r.height;
    svg.attr('width', width).attr('height', height).attr('viewBox', [0, 0, width, height]);
    if (simulation) simulation.force('center', d3.forceCenter(width / 2, height / 2)).alpha(0.2).restart();
  });

  subscribe((state, patch) => {
    if ('brightness' in patch) applyOpacity();
    if ('currentDateIndex' in patch || 'tourMode' in patch || 'tourPhase' in patch) applyOpacity();
    if ('hiddenCategories' in patch) applyOpacity();
  });
}

export function renderGraph() {
  const { nodes, links } = getState();
  // Clone so d3 can mutate without polluting state
  const N = nodes.map(n => ({ ...n }));
  const L = links.map(l => ({ ...l }));

  simulation = d3.forceSimulation(N)
    // NOTE: no .id() — links reference nodes by numeric index
    .force('link', d3.forceLink(L).distance(40).strength(0.5))
    .force('charge', d3.forceManyBody().strength(-60))
    .force('center', d3.forceCenter(width / 2, height / 2))
    .force('collide', d3.forceCollide().radius(d => (d.size || 5) + 2));

  linkSel = g.append('g').attr('class', 'links')
    .selectAll('line').data(L).enter().append('line')
    .attr('class', 'link');

  nodeSel = g.append('g').attr('class', 'nodes')
    .selectAll('circle').data(N).enter().append('circle')
    .attr('class', 'node')
    .attr('r', d => d.size || 5)
    .attr('fill', d => d.color || '#888')
    .call(drag(simulation))
    .on('click', (ev, d) => {
      ev.stopPropagation();
      setState({ userInteracted: true, selectedNode: d });
      onNodeClick(d);
    });

  nodeSel.append('title').text(d => `${d.label || d.id}\n${d.directory}\n${d.date || ''}`);

  simulation.on('tick', () => {
    linkSel
      .attr('x1', d => d.source.x).attr('y1', d => d.source.y)
      .attr('x2', d => d.target.x).attr('y2', d => d.target.y);
    nodeSel.attr('cx', d => d.x).attr('cy', d => d.y);
  });

  applyOpacity();
}

function drag(sim) {
  function started(ev, d) {
    if (!ev.active) sim.alphaTarget(0.3).restart();
    d.fx = d.x; d.fy = d.y;
    setState({ userInteracted: true });
  }
  function dragged(ev, d) { d.fx = ev.x; d.fy = ev.y; }
  function ended(ev, d) {
    if (!ev.active) sim.alphaTarget(0);
    d.fx = null; d.fy = null;
  }
  return d3.drag().on('start', started).on('drag', dragged).on('end', ended);
}

// Opacity has two inputs:
//   - temporal reveal (nodes in the future are ghosted during a tour)
//   - brightness slider (user-controlled, applied as whole-graph multiplier)
//
// Brightness is applied as opacity on the root <g> so a slider drag
// visibly affects the entire canvas — you cannot miss it. Per-node/link
// opacity is used only for the temporal reveal (past vs future).
function applyOpacity() {
  if (!nodeSel) return;
  const { tourMode, tourPhase, currentDateIndex, dates, brightness, hiddenCategories } = getState();

  // Brightness slider drives a CSS filter on the whole graph <g>. Unlike
  // SVG opacity (capped at 1.0), filter: brightness() works in both
  // directions — 0.2 = 20% of normal, 2.0 = doubled. Slider drag is visible
  // across the full range.
  const b = Math.max(0.2, Math.min(2.5, brightness || 1.0));
  g.style('filter', `brightness(${b.toFixed(2)})`);

  // Determine effective "current date" based on phase.
  // - intro: pretend we're before day 1 → ghost all dated nodes
  // - outro: pretend we're after the last day → reveal everything
  // - body / no tour: use currentDateIndex as before
  let currentDate = null;
  if (tourPhase === 'intro') {
    currentDate = '';  // sorts before every real date → everything ghosted
  } else if (tourPhase === 'outro') {
    currentDate = '9999-12-31';  // sorts after every real date → everything revealed
  } else if (tourMode && dates.length) {
    currentDate = dates[Math.min(currentDateIndex, dates.length - 1)];
  }

  // Temporal reveal: 1.0 for past/no-date, ghosted for future during tour.
  const pastBase   = 1.0;
  const ghostFloor = 0.12;
  // Category hide: user unchecked a legend row. These fade further than
  // temporal-future ghosting so the user can distinguish the two states.
  const hiddenOpacity = 0.04;
  const hiddenLinkOp  = 0.02;

  const hidden = hiddenCategories || {};
  const isHidden = (d) => !!hidden[d.group];

  nodeSel.attr('opacity', d => {
    if (isHidden(d)) return hiddenOpacity;
    if (!currentDate || !d.date) return pastBase;
    return d.date <= currentDate ? pastBase : ghostFloor;
  });
  linkSel.attr('opacity', d => {
    if (isHidden(d.source) || isHidden(d.target)) return hiddenLinkOp;
    // Reference links are visually softer than explicit wikilinks.
    const base = d.type === 'wikilink' ? 0.45 : 0.22;
    if (!currentDate) return base;
    const srcDate = d.source.date, tgtDate = d.target.date;
    if (!srcDate || !tgtDate) return base;
    if (srcDate <= currentDate && tgtDate <= currentDate) return base;
    return base * 0.15;
  });
}

// Pulse nodes that match a directory prefix (e.g. "traditions/friston")
// Called by narration module when the text mentions a tradition.
export function highlightByPrefix(prefix, duration = 2500) {
  if (!nodeSel) return;
  nodeSel
    .classed('mentioned', d => d.directory && d.directory.startsWith(prefix));
  setTimeout(() => {
    if (nodeSel) nodeSel.classed('mentioned', false);
  }, duration);
}

// Highlight by directory equality (e.g. flags, architecture)
export function highlightByDir(dir, duration = 2500) {
  if (!nodeSel) return;
  nodeSel.classed('mentioned', d => d.directory === dir);
  setTimeout(() => {
    if (nodeSel) nodeSel.classed('mentioned', false);
  }, duration);
}

// Zoom/recenter on a date's nodes (helper for future work)
export function fitToDate(dateStr) {
  if (!nodeSel) return;
  // Leave for future polish; current version just applies opacity
  applyOpacity();
}
