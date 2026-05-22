// UI wiring: header, footer, settings modal, detail panel, brightness slider.
// Each concern is a small `init*()` function; main.js calls them once at startup.
//
// Keeps the DOM-side event handling in one place so the other modules
// (graph, narration, tts) stay free of DOM listeners beyond their own canvas.

import { getState, setState, savePersisted, loadPersisted, subscribe } from './state.js';
import * as narration from './narration.js';
import * as tts from './tts.js';
import { error as toastError, success as toastSuccess } from './toast.js';
import { registerNodeClick } from './graph.js';

// ---- Header stats ----
export function initHeader() {
  const s = getState();
  document.getElementById('stat-files').textContent = `${s.metadata.total_files} files`;
  document.getElementById('stat-traditions').textContent = `${s.metadata.traditions_count} traditions`;
  document.getElementById('stat-findings').textContent = `${s.metadata.findings_count} findings`;
  document.getElementById('stat-decisions').textContent = `${s.metadata.decisions_count} decisions`;

  // Tour buttons
  for (const btn of document.querySelectorAll('[data-tour]')) {
    btn.addEventListener('click', () => narration.startTour(btn.dataset.tour));
  }

  // Brightness
  const bright = document.getElementById('brightness-slider');
  bright.value = Math.round((s.brightness || 1.0) * 100);
  bright.addEventListener('input', (ev) => {
    const val = Number(ev.target.value) / 100;
    setState({ brightness: val });
    savePersisted();
  });

  // Intro/outro toggle — opt-in, persisted. Only affects History mode.
  const introToggle = document.getElementById('intro-toggle');
  introToggle.checked = !!s.wantsIntroOutro;
  introToggle.addEventListener('change', (ev) => {
    setState({ wantsIntroOutro: ev.target.checked });
    savePersisted();
  });

  // Legend checkboxes — per-category visibility.
  initLegend();

  // Settings button
  document.getElementById('settings-btn').addEventListener('click', openSettings);

  // Record button — placeholder for future MediaRecorder integration
  document.getElementById('record-btn').addEventListener('click', () => {
    toastError('Recording not yet implemented in modular build. Coming back in a later iteration.');
  });
}

function initLegend() {
  const rows = Array.from(document.querySelectorAll('#color-legend .legend-row'));
  const master = document.getElementById('legend-master');

  function syncRowStyle(row) {
    const checked = row.querySelector('input').checked;
    row.classList.toggle('off', !checked);
  }

  function applyCurrentHiddenSet() {
    const hidden = {};
    for (const row of rows) {
      if (!row.querySelector('input').checked) hidden[row.dataset.category] = true;
    }
    setState({ hiddenCategories: hidden });
    // Reflect into master: checked if all on, unchecked if all off, else indeterminate
    const allOn = rows.every(r => r.querySelector('input').checked);
    const allOff = rows.every(r => !r.querySelector('input').checked);
    master.checked = allOn;
    master.indeterminate = !allOn && !allOff;
  }

  for (const row of rows) {
    const input = row.querySelector('input');
    row.addEventListener('change', () => {
      syncRowStyle(row);
      applyCurrentHiddenSet();
    });
    syncRowStyle(row);
  }

  master.addEventListener('change', () => {
    const target = master.checked;  // true: show all, false: hide all
    for (const row of rows) {
      const input = row.querySelector('input');
      input.checked = target;
      syncRowStyle(row);
    }
    applyCurrentHiddenSet();
  });

  // Initial sync
  applyCurrentHiddenSet();
}

// ---- Footer ----
export function initFooter() {
  const s = getState();
  const slider = document.getElementById('date-slider');
  slider.max = Math.max(0, s.dates.length - 1);
  slider.value = s.currentDateIndex;
  slider.addEventListener('input', (ev) => {
    setState({ userInteracted: true });
    narration.setDateIndex(Number(ev.target.value));
  });

  document.getElementById('play-pause-btn').addEventListener('click', () => {
    narration.togglePlayPause();
  });
  document.getElementById('reset-btn').addEventListener('click', () => {
    narration.resetTour();
  });
  document.getElementById('speed-select').addEventListener('change', (ev) => {
    setState({ animationSpeed: Number(ev.target.value) });
  });
  document.getElementById('mute-btn').addEventListener('click', (ev) => {
    const cur = getState();
    setState({ isMuted: !cur.isMuted });
    ev.currentTarget.textContent = !cur.isMuted ? '🔇' : '🔊';
    if (!cur.isMuted) tts.stop();
  });
  document.getElementById('brief-deep-btn').addEventListener('click', (ev) => {
    narration.toggleBriefDeep();
    ev.currentTarget.textContent = getState().isBriefMode ? 'Brief' : 'Deep';
  });

  // Footer collapse toggle
  document.getElementById('footer-toggle').addEventListener('click', (ev) => {
    const bar = document.getElementById('narration-bar');
    bar.classList.toggle('collapsed');
    ev.currentTarget.textContent = bar.classList.contains('collapsed') ? '▴' : '▾';
  });

  // Reflect play/pause label when state changes externally
  subscribe((state, patch) => {
    if ('isPlaying' in patch) {
      document.getElementById('play-pause-btn').textContent = state.isPlaying ? 'Pause' : 'Play';
    }
  });
}

// ---- Settings modal ----
function openSettings() {
  const s = getState();
  document.getElementById('settings-overlay').classList.remove('hidden');
  document.getElementById('settings-modal').classList.remove('hidden');
  document.getElementById('tts-provider').value = s.ttsProvider;
  document.getElementById('tts-api-key').value = s.ttsApiKey;
  document.getElementById('tts-voice-openai').value = s.ttsVoiceOpenAI || 'nova';
  updateProviderUI();
  populateBrowserVoices();
  document.getElementById('tts-voice-browser').value = s.ttsVoiceBrowser || '';
  document.getElementById('tts-status').textContent = '';
}

function closeSettings() {
  document.getElementById('settings-overlay').classList.add('hidden');
  document.getElementById('settings-modal').classList.add('hidden');
}

function updateProviderUI() {
  const p = document.getElementById('tts-provider').value;
  document.getElementById('openai-group').hidden = (p !== 'openai');
  document.getElementById('browser-group').hidden = (p !== 'browser');
}

function populateBrowserVoices() {
  const voices = tts.listBrowserVoices();
  const sel = document.getElementById('tts-voice-browser');
  sel.innerHTML = '<option value="">Default</option>';
  for (const v of voices) {
    const opt = document.createElement('option');
    opt.value = v.name;
    opt.textContent = `${v.name} (${v.lang})`;
    sel.appendChild(opt);
  }
}

function applyFormToState() {
  setState({
    ttsProvider: document.getElementById('tts-provider').value,
    ttsApiKey: document.getElementById('tts-api-key').value.trim(),
    ttsVoiceOpenAI: document.getElementById('tts-voice-openai').value,
    ttsVoiceBrowser: document.getElementById('tts-voice-browser').value,
  });
}

export function initSettings() {
  document.getElementById('tts-provider').addEventListener('change', updateProviderUI);
  document.getElementById('settings-close').addEventListener('click', closeSettings);
  document.getElementById('settings-overlay').addEventListener('click', closeSettings);

  document.getElementById('tts-save-btn').addEventListener('click', () => {
    applyFormToState();
    savePersisted();
    toastSuccess('Settings saved');
    closeSettings();
  });

  document.getElementById('tts-test-btn').addEventListener('click', async () => {
    applyFormToState();
    const status = document.getElementById('tts-status');
    const s = getState();
    const shape = tts.describeKey(s.ttsApiKey);
    // Prove to the user what state the test is running against. If this line
    // shows the wrong provider, wrong key shape, or "(empty)", the test didn't
    // even leave the starting gate.
    status.textContent = `Testing… provider=${s.ttsProvider} voice=${s.ttsProvider === 'openai' ? s.ttsVoiceOpenAI : (s.ttsVoiceBrowser || 'default')} key=${shape}`;
    status.className = 'status';
    console.log('[UI] Test clicked', { provider: s.ttsProvider, voiceOpenAI: s.ttsVoiceOpenAI, voiceBrowser: s.ttsVoiceBrowser, keyShape: shape });
    try {
      await tts.test();
      status.textContent = `OK — heard voice? If silent but no error, check system volume / tab mute. (provider=${s.ttsProvider}, voice=${s.ttsProvider === 'openai' ? s.ttsVoiceOpenAI : s.ttsVoiceBrowser})`;
      status.classList.add('ok');
    } catch (err) {
      status.textContent = `Failed: ${err.message}  (provider=${s.ttsProvider}, key=${shape})`;
      status.classList.add('err');
      toastError(`TTS test failed: ${err.message}`);
    }
  });

  // speechSynthesis voices populate asynchronously on some browsers
  if (window.speechSynthesis) {
    window.speechSynthesis.onvoiceschanged = populateBrowserVoices;
  }
}

// ---- Detail panel ----
export function initDetailPanel() {
  const panel = document.getElementById('detail-panel');
  const content = document.getElementById('detail-content');
  const close = document.getElementById('detail-close');

  registerNodeClick((node) => {
    content.innerHTML = renderNodeDetail(node);
    panel.classList.remove('hidden');
  });

  close.addEventListener('click', () => {
    panel.classList.add('hidden');
    setState({ selectedNode: null });
  });
}

function renderNodeDetail(node) {
  const esc = (s) => String(s ?? '').replace(/[&<>"]/g, c => ({ '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;' }[c]));
  // Content is pre-rendered to HTML at build time (see build_data.py).
  // If it's missing (old cached data), fall back to file metadata.
  const content = node.contentHtml || '';
  const meta = [
    node.directory ? `<span class="meta-chip">${esc(node.directory)}</span>` : '',
    node.date     ? `<span class="meta-chip">${esc(node.date)}</span>` : '',
    node.tradition? `<span class="meta-chip">${esc(node.tradition)}</span>` : '',
  ].filter(Boolean).join(' ');
  const lines = [
    `<h3>${esc(node.label || node.id)}</h3>`,
    meta ? `<div class="detail-meta">${meta}</div>` : '',
    content
      ? `<div class="detail-content">${content}</div>`
      : `<div class="detail-content"><p class="md-fallback"><em>No preview available for this file.</em></p><dl><dt>Path</dt><dd><code>${esc(node.id)}</code></dd></dl></div>`,
    `<div class="detail-footer"><code>${esc(node.id)}</code></div>`,
  ].filter(Boolean);
  return lines.join('\n');
}

// ---- Keyboard shortcuts ----
export function initKeyboard() {
  document.addEventListener('keydown', (ev) => {
    // Ignore typing in form fields
    if (['INPUT', 'TEXTAREA', 'SELECT'].includes(ev.target.tagName)) return;
    if (ev.key === ' ') { ev.preventDefault(); narration.togglePlayPause(); }
    if (ev.key === 'Escape') {
      document.getElementById('detail-panel').classList.add('hidden');
      closeSettings();
    }
    if (ev.key === 'ArrowRight') narration.setDateIndex(getState().currentDateIndex + 1);
    if (ev.key === 'ArrowLeft') narration.setDateIndex(getState().currentDateIndex - 1);
  });
}

// ---- Chat input (stub — wires to nothing yet, placeholder for future) ----
export function initChat() {
  const input = document.getElementById('chat-input');
  const submit = document.getElementById('chat-submit');
  const handler = () => {
    const q = input.value.trim();
    if (!q) return;
    toastError('Chat is not wired up yet. Answering via the wiki will come in a later iteration.');
    input.value = '';
  };
  submit.addEventListener('click', handler);
  input.addEventListener('keydown', (ev) => { if (ev.key === 'Enter') handler(); });
}
