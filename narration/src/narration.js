// Narration tour: walks through dates, updates the bottom-bar text, speaks
// it via TTS, and advances only when speech finishes (no flat timers).
//
// Tour modes:
//   - history: intro → all dates from the start → outro
//   - recent:  last 3 days (no intro/outro)
//   - latest:  just the final date (no intro/outro)
//
// Phase machine (state.tourPhase):
//   null     no tour running
//   "intro"  speaking narrations.__intro; graph visible but no date selected
//   "body"   walking through state.dates; per-date narration as before
//   "outro"  speaking narrations.__outro; graph stays at the final date
//
// Only "history" mode uses intro/outro. Recent/Latest jump straight to "body".
//
// Design decisions carried forward:
//   - Brief vs Deep: same tour, different narration depth. Toggle at any time.
//   - Graph sync: every date advance also updates state.currentDateIndex so
//     graph.js applies opacity. If user is exploring (state.userInteracted),
//     graph sync pauses for 3s — but NARRATION keeps going.

import { getState, setState, subscribe } from './state.js';
import * as tts from './tts.js';
import { highlightByPrefix, highlightByDir } from './graph.js';

const TRADITION_KEYWORDS = [
  'friston', 'kastrup', 'levin', 'hoffman', 'mcgilchrist',
  'fredrickson', 'hawkins', 'stump', 'carroll', 'wolfram', 'arkanihamed',
];

// Pause between narration segments so listener can breathe.
const INTER_SEGMENT_MS = 600;

export function startTour(mode) {
  const s = getState();
  if (!s.dates.length) return;

  tts.stop();
  // Nuke any stale cached audio from prior sessions / provider switches /
  // HMR reloads. Prevents "ghost voices" accumulating across dev cycles.
  tts.clearCache();

  let firstIndex = 0;
  let firstPhase = 'body';

  if (mode === 'history') {
    firstIndex = 0;
    // Intro runs only if (a) user has opted in via the header toggle,
    // (b) the intro entry exists, and (c) it isn't a placeholder.
    // Otherwise fall straight through to body. Same gating applies at end
    // of body for the outro.
    firstPhase = (s.wantsIntroOutro && hasUsableEntry(s.narrations.__intro))
      ? 'intro' : 'body';
  } else if (mode === 'recent') {
    firstIndex = Math.max(0, s.dates.length - 3);
  } else if (mode === 'latest') {
    firstIndex = s.dates.length - 1;
  }

  setState({
    tourMode: mode,
    tourPhase: firstPhase,
    currentDateIndex: firstIndex,
    isPlaying: true,
  });
  advance();
}

export function togglePlayPause() {
  const s = getState();
  if (s.isPlaying) {
    setState({ isPlaying: false });
    tts.stop();
  } else {
    setState({ isPlaying: true });
    advance();
  }
}

export function resetTour() {
  tts.stop();
  setState({ isPlaying: false, tourMode: null, tourPhase: null, currentDateIndex: 0 });
  renderNarration();
}

export function setDateIndex(idx) {
  const s = getState();
  const clamped = Math.max(0, Math.min(s.dates.length - 1, idx));
  // Manual scrubbing always lands in body phase.
  setState({ currentDateIndex: clamped, tourPhase: s.tourMode ? 'body' : null });
  renderNarration();
}

export function toggleBriefDeep() {
  const s = getState();
  setState({ isBriefMode: !s.isBriefMode });
  renderNarration();
}

// Some entries may be placeholder text like "[INTRO PLACEHOLDER ...]".
// Treat anything starting with "[" and ending with "]" as missing, so
// unfinished intro/outro text doesn't get spoken.
function hasUsableEntry(entry) {
  if (!entry) return false;
  const text = entry.voice || entry.deep || entry.brief || '';
  const t = text.trim();
  if (!t) return false;
  if (t.startsWith('[') && t.endsWith(']')) return false;
  return true;
}

function advance() {
  const s = getState();
  if (!s.isPlaying) return;

  // ---- Intro phase ------------------------------------------------------
  if (s.tourPhase === 'intro') {
    const entry = s.narrations.__intro || {};
    if (!hasUsableEntry(entry)) {
      // Skip straight to body if intro missing.
      setState({ tourPhase: 'body' });
      advance();
      return;
    }
    renderNarration();
    const text = pickText(entry, s.isBriefMode);
    tts.speak(text, {
      onEnd: () => {
        setTimeout(() => {
          const now = getState();
          if (!now.isPlaying) return;
          setState({ tourPhase: 'body' });
          advance();
        }, INTER_SEGMENT_MS);
      },
    });
    return;
  }

  // ---- Outro phase ------------------------------------------------------
  if (s.tourPhase === 'outro') {
    const entry = s.narrations.__outro || {};
    if (!hasUsableEntry(entry)) {
      setState({ isPlaying: false, tourPhase: null });
      return;
    }
    renderNarration();
    const text = pickText(entry, s.isBriefMode);
    tts.speak(text, {
      onEnd: () => {
        setState({ isPlaying: false, tourPhase: null });
      },
    });
    return;
  }

  // ---- Body phase: per-date narration ----------------------------------
  if (s.currentDateIndex >= s.dates.length) {
    // End of body. History mode with opt-in toggle appends outro; other
    // modes and History-without-toggle just stop.
    if (s.tourMode === 'history' && s.wantsIntroOutro
        && hasUsableEntry(s.narrations.__outro)) {
      setState({ tourPhase: 'outro', currentDateIndex: s.dates.length - 1 });
      advance();
    } else {
      setState({ isPlaying: false, tourPhase: null });
    }
    return;
  }

  renderNarration();
  const date = s.dates[s.currentDateIndex];
  const entry = s.narrations[date] || {};
  const text = pickText(entry, s.isBriefMode) || `No narration for ${date}.`;

  // Highlight traditions mentioned in the text
  const lower = text.toLowerCase();
  for (const t of TRADITION_KEYWORDS) {
    if (lower.includes(t)) {
      highlightByPrefix(`traditions/${t}`);
      break;  // one highlight per date is enough
    }
  }
  if (/finding|flag/i.test(lower)) highlightByDir('flags');
  if (/architectur|decision/i.test(lower)) highlightByDir('architecture');

  tts.speak(text, {
    onEnd: () => {
      setTimeout(() => {
        const now = getState();
        if (!now.isPlaying) return;
        setState({ currentDateIndex: now.currentDateIndex + 1 });
        advance();
      }, INTER_SEGMENT_MS);
    },
  });
}

// Voice narration is preferred for speech; fall back to deep then brief.
// In brief-mode for on-screen text, the brief variant is preferred.
function pickText(entry, briefMode) {
  if (briefMode) return entry.brief || entry.voice || entry.deep || '';
  return entry.voice || entry.deep || entry.brief || '';
}

export function renderNarration() {
  const s = getState();
  const el = document.getElementById('narration-text');
  const label = document.getElementById('date-label');
  const slider = document.getElementById('date-slider');

  if (s.tourPhase === 'intro') {
    const entry = s.narrations.__intro || {};
    const text = pickText(entry, s.isBriefMode);
    if (el) el.textContent = text || '(intro)';
    if (label) label.textContent = '— intro —';
    if (slider) slider.value = 0;
    return;
  }

  if (s.tourPhase === 'outro') {
    const entry = s.narrations.__outro || {};
    const text = pickText(entry, s.isBriefMode);
    if (el) el.textContent = text || '(outro)';
    if (label) label.textContent = '— outro —';
    if (slider && s.dates.length) slider.value = s.dates.length - 1;
    return;
  }

  // Default / body phase.
  if (!s.dates.length) return;
  const date = s.dates[Math.min(s.currentDateIndex, s.dates.length - 1)];
  const entry = s.narrations[date] || {};
  const text = pickText(entry, s.isBriefMode) || '—';
  if (el) el.textContent = text;
  if (label) label.textContent = date || '—';
  if (slider) slider.value = s.currentDateIndex;
}
