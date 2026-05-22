// Central state store. Pub-sub pattern so modules don't reach into each other.
// Keeps intent explicit: any state change flows through setState, which
// notifies subscribers. No framework needed.

const state = {
  // Data
  nodes: [],
  links: [],
  narrations: {},        // { "2026-04-08": { brief: "…", deep: "…" }, … }
  dates: [],             // sorted array of date strings
  metadata: {
    total_files: 0,
    traditions: 0,
    findings: 0,
    decisions: 0,
  },

  // Tour / narration
  tourMode: null,        // null | "history" | "recent" | "latest"
  tourPhase: null,       // null | "intro" | "body" | "outro"
  currentDateIndex: 0,
  isPlaying: false,
  isBriefMode: true,
  isMuted: false,
  animationSpeed: 1,
  userInteracted: false, // when true, graph sync pauses briefly
  wantsIntroOutro: false,// opt-in: play intro+outro wrapping History mode

  // Rendering
  brightness: 1.0,       // 0.2 – 2.0 (slider range)
  selectedNode: null,    // node object if detail panel is open
  hiddenCategories: {},  // { "<group>": true } when a legend checkbox is off

  // TTS
  ttsProvider: 'browser',
  ttsApiKey: '',
  ttsVoiceOpenAI: 'nova',
  ttsVoiceBrowser: '',
};

const subscribers = new Set();

export function getState() {
  // Return shallow copy so accidental mutation doesn't corrupt state
  return { ...state };
}

export function setState(patch) {
  Object.assign(state, patch);
  for (const fn of subscribers) fn(state, patch);
}

export function subscribe(fn) {
  subscribers.add(fn);
  return () => subscribers.delete(fn);  // unsubscribe
}

// Persist a subset to localStorage (settings only)
const PERSIST_KEYS = ['ttsProvider', 'ttsApiKey', 'ttsVoiceOpenAI', 'ttsVoiceBrowser', 'brightness', 'wantsIntroOutro'];

export function loadPersisted() {
  try {
    const raw = localStorage.getItem('c2a2-settings');
    if (!raw) return;
    const saved = JSON.parse(raw);
    const patch = {};
    for (const k of PERSIST_KEYS) if (k in saved) patch[k] = saved[k];
    setState(patch);
  } catch (e) {
    console.warn('Could not load persisted settings:', e);
  }
}

export function savePersisted() {
  try {
    const subset = {};
    for (const k of PERSIST_KEYS) subset[k] = state[k];
    localStorage.setItem('c2a2-settings', JSON.stringify(subset));
  } catch (e) {
    console.warn('Could not save settings:', e);
  }
}
