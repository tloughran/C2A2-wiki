// Entry point. Loads the data files and wires the modules together.
// All DOM IDs live in index.html, all visual rules in styles.css.

import { setState, loadPersisted } from './state.js';
import { initGraph, renderGraph } from './graph.js';
import { renderNarration } from './narration.js';
import { initHeader, initFooter, initSettings, initDetailPanel, initKeyboard, initChat } from './ui.js';
import { error as toastError } from './toast.js';

async function loadJSON(url) {
  const resp = await fetch(url);
  if (!resp.ok) throw new Error(`${url}: ${resp.status}`);
  return resp.json();
}

async function main() {
  loadPersisted();

  try {
    const [nodes, links, narrations, metadata] = await Promise.all([
      loadJSON('./data/nodes.json'),
      loadJSON('./data/links.json'),
      loadJSON('./data/narrations.json'),
      loadJSON('./data/metadata.json'),
    ]);

    // Dates come from metadata when available. Fallback: narration keys,
    // minus internal __intro / __outro entries (those are phase markers,
    // not real dates).
    const dates = metadata.dates && metadata.dates.length
      ? metadata.dates
      : Object.keys(narrations).filter(k => !k.startsWith('__')).sort();

    setState({
      nodes, links, narrations, metadata,
      dates,
      currentDateIndex: Math.max(0, dates.length - 1),
    });
  } catch (err) {
    toastError(`Could not load data files: ${err.message}. Run \`npm run data\` to regenerate.`);
    console.error(err);
    return;
  }

  initHeader();
  initFooter();
  initSettings();
  initDetailPanel();
  initKeyboard();
  initChat();

  initGraph(document.getElementById('graph-container'));
  renderGraph();
  renderNarration();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', main);
} else {
  main();
}
