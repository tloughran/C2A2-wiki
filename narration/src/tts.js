// TTS abstraction. Two providers:
//   - browser: window.speechSynthesis (no setup, modest quality)
//   - openai:  /v1/audio/speech (natural, requires API key + CORS + net)
//
// Design principles learned from the previous silent-failure debugging:
//   1. Every failure surfaces to the UI via toast(). No silent fallbacks.
//   2. `speak()` is async and returns a promise that resolves when audio ends.
//   3. `test()` is a first-class method — it validates end-to-end and
//      throws a descriptive error if anything is wrong (no key, bad key,
//      CORS blocked, empty response).
//   4. Results are cached by (provider, voice, text[0..50]) so re-playing
//      a date doesn't re-hit the API.

import { getState } from './state.js';
import { error as toastError, success as toastSuccess, info as toastInfo } from './toast.js';

const cache = new Map();
let currentAudio = null;
let currentUtterance = null;
let currentAbort = null;
// Monotonically-increasing request id. Only the most recent speak() may
// actually play audio; stale resolutions are no-ops.
let requestSeq = 0;

function cacheKey(provider, voice, text, speed) {
  // Speed must be part of the key — OpenAI bakes speed into the audio at
  // generation time, so a cache entry generated at speed=1 will replay at
  // speed=1 even if the user has since moved to 1.5x.
  return `${provider}|${voice}|${speed}|${text.slice(0, 50)}`;
}

// Exposed so UI can nuke the cache on demand (e.g. after a provider switch
// or when silence accumulates from a rapid-iteration dev cycle).
export function clearCache() {
  for (const url of cache.values()) {
    try { URL.revokeObjectURL(url); } catch {}
  }
  cache.clear();
  console.log('[TTS] cache cleared');
}

export function stop() {
  // Bump the sequence so any in-flight speak() resolves into a no-op.
  requestSeq++;
  if (currentAbort) {
    try { currentAbort.abort(); } catch {}
    currentAbort = null;
  }
  if (currentAudio) {
    try { currentAudio.pause(); currentAudio.currentTime = 0; } catch {}
    currentAudio = null;
  }
  if (window.speechSynthesis) {
    try { window.speechSynthesis.cancel(); } catch {}
  }
  currentUtterance = null;
}

export async function speak(text, { onEnd } = {}) {
  const s = getState();
  if (s.isMuted || !text) {
    if (onEnd) setTimeout(onEnd, 0);
    return;
  }
  stop();  // cancel anything currently playing
  const mySeq = ++requestSeq;
  const provider = (s.ttsProvider === 'openai' && s.ttsApiKey) ? 'openai' : 'browser';
  try {
    if (provider === 'openai') {
      await speakOpenAI(text, s, onEnd, mySeq);
    } else {
      speakBrowser(text, s, onEnd, mySeq);
    }
  } catch (err) {
    // Intentional cancellations are silent — they happen on tour advance.
    if (err.name === 'AbortError' || err.message === 'superseded') {
      console.log('[TTS] request superseded, staying silent');
      return;
    }
    // If we were on OpenAI and it failed after retries, DO NOT fall back to
    // browser voice — mid-tour voice swapping is worse than silence. Advance
    // the tour so it keeps moving. User sees the failure via toast.
    console.error('TTS error (advancing silently):', err);
    toastError(`TTS: ${err.message}`);
    if (mySeq === requestSeq && onEnd) onEnd();
  }
}

async function speakOpenAI(text, s, onEnd, mySeq) {
  // Diagnostic: prove that state has what we expect. We log only key shape,
  // never the key itself.
  const keyShape = describeKey(s.ttsApiKey);
  console.log('[TTS] speakOpenAI start', { seq: mySeq, voice: s.ttsVoiceOpenAI, keyShape, textLen: text.length });

  if (!s.ttsApiKey) throw new Error('no api key in state');
  if (!/^sk-/.test(s.ttsApiKey)) throw new Error(`key does not start with "sk-" (got prefix "${s.ttsApiKey.slice(0,6)}")`);

  const cKey = cacheKey('openai', s.ttsVoiceOpenAI, text, s.animationSpeed || 1);
  let url = cache.get(cKey);
  if (!url) {
    // OpenAI's TTS endpoint intermittently returns 5xx during bursts. Retry
    // transient errors silently (short backoff) before giving up; hard errors
    // (4xx, aborts, empty blob) skip retry and throw immediately.
    const backoffs = [0, 500, 1500];
    let lastErr = null;
    for (let attempt = 0; attempt < backoffs.length; attempt++) {
      if (backoffs[attempt]) await sleep(backoffs[attempt]);
      if (mySeq !== requestSeq) throw new Error('superseded');
      try {
        url = await fetchOpenAIOnce(text, s, mySeq, attempt);
        if (url) break;
      } catch (err) {
        lastErr = err;
        // Don't retry aborts or authorization/quota-type errors
        if (err.name === 'AbortError' || err.message === 'superseded') throw err;
        if (err._hard) throw err;
        console.warn(`[TTS] attempt ${attempt + 1} failed (seq=${mySeq}): ${err.message} — retrying`);
      }
    }
    if (!url) throw lastErr || new Error('unknown TTS failure');
    cache.set(cKey, url);
  } else {
    console.log('[TTS] using cached audio (seq=' + mySeq + ')');
  }
  // Final guard before play
  if (mySeq !== requestSeq) { console.log('[TTS] superseded before play, seq=' + mySeq); throw new Error('superseded'); }
  await playUrl(url, onEnd, mySeq);
  console.log('[TTS] playback finished (seq=' + mySeq + ')');
}

const sleep = (ms) => new Promise(r => setTimeout(r, ms));

// Single fetch attempt. Returns object URL for the MP3 blob on success.
// Hard-error throws are marked with `err._hard = true` so the retry loop
// skips them. 5xx and network errors are retryable (plain throws).
async function fetchOpenAIOnce(text, s, mySeq, attempt) {
  const abort = new AbortController();
  currentAbort = abort;
  console.log(`[TTS] fetch POST /v1/audio/speech (seq=${mySeq}, attempt=${attempt + 1})`);
  let resp;
  try {
    resp = await fetch('https://api.openai.com/v1/audio/speech', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${s.ttsApiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: 'tts-1-hd',
        voice: s.ttsVoiceOpenAI,
        input: text,
        response_format: 'mp3',
        speed: s.animationSpeed,
      }),
      signal: abort.signal,
    });
  } catch (netErr) {
    if (netErr.name === 'AbortError') throw netErr;
    // Network / CORS failures are retryable.
    console.error('[TTS] network-level failure', netErr);
    const e = new Error(`network error: ${netErr.message}`);
    throw e;
  }
  if (mySeq !== requestSeq) throw new Error('superseded');
  console.log(`[TTS] response status ${resp.status} ${resp.statusText} (seq=${mySeq})`);
  if (!resp.ok) {
    let detail = '';
    try {
      const j = await resp.json();
      detail = j?.error?.message || '';
      console.error('[TTS] API error body', j);
    } catch {}
    const e = new Error(`${resp.status} ${resp.statusText}${detail ? ' — ' + detail : ''}`);
    // 4xx = hard error (bad key, invalid request, quota). 5xx = retryable.
    if (resp.status >= 400 && resp.status < 500) e._hard = true;
    throw e;
  }
  const blob = await resp.blob();
  if (mySeq !== requestSeq) throw new Error('superseded');
  console.log('[TTS] blob received', { type: blob.type, size: blob.size, seq: mySeq, attempt: attempt + 1 });
  if (blob.size === 0) {
    const e = new Error('empty audio response');
    e._hard = true;
    throw e;
  }
  return URL.createObjectURL(blob);
}

// Describe a key without leaking it: length + prefix + suffix only.
export function describeKey(k) {
  if (!k) return '(empty)';
  if (typeof k !== 'string') return `(non-string ${typeof k})`;
  const trimmed = k.trim();
  if (trimmed.length !== k.length) return `has whitespace (len=${k.length}, trimmed=${trimmed.length})`;
  if (trimmed.length < 20) return `too short (len=${trimmed.length})`;
  return `${trimmed.slice(0, 7)}…${trimmed.slice(-4)} (len=${trimmed.length})`;
}

function playUrl(url, onEnd, mySeq) {
  return new Promise((resolve) => {
    const audio = new Audio(url);
    currentAudio = audio;
    audio.onended = () => {
      // Only fire onEnd if we are still the current request. Prevents stale
      // audio from advancing the tour.
      if (mySeq === requestSeq && onEnd) onEnd();
      resolve();
    };
    audio.onerror = (e) => {
      if (mySeq === requestSeq) toastError('Audio playback failed');
      if (mySeq === requestSeq && onEnd) onEnd();
      resolve();
    };
    audio.play().catch((e) => {
      if (mySeq === requestSeq) toastError(`Audio play blocked: ${e.message}`);
      if (mySeq === requestSeq && onEnd) onEnd();
      resolve();
    });
  });
}

function speakBrowser(text, s, onEnd, mySeq) {
  if (!window.speechSynthesis) {
    toastError('This browser has no speech synthesis support.');
    if (onEnd) onEnd();
    return;
  }
  const u = new SpeechSynthesisUtterance(text);
  u.rate = 0.95 * (s.animationSpeed || 1);
  u.pitch = 1.0;
  u.volume = 0.9;

  const voices = window.speechSynthesis.getVoices();
  const preferred = s.ttsVoiceBrowser
    ? voices.find(v => v.name === s.ttsVoiceBrowser)
    : pickBestVoice(voices);
  if (preferred) u.voice = preferred;

  u.onend = () => {
    if (mySeq != null && mySeq !== requestSeq) return;
    if (onEnd) onEnd();
  };
  u.onerror = (e) => {
    if (mySeq != null && mySeq !== requestSeq) return;
    toastError(`Speech error: ${e.error || 'unknown'}`);
    if (onEnd) onEnd();
  };
  currentUtterance = u;
  window.speechSynthesis.speak(u);
}

// Preference order: premium/enhanced en-* voices, then well-known natural ones.
function pickBestVoice(voices) {
  const rank = (v) => {
    const name = v.name.toLowerCase();
    let score = 0;
    if (!v.lang?.startsWith('en')) score -= 100;
    if (/(premium|enhanced|neural)/.test(name)) score += 50;
    if (/(zoe|samantha|karen|ava|allison|kate|serena)/.test(name)) score += 20;
    if (/(nova|shimmer)/.test(name)) score += 10;   // unlikely locally but rank high if present
    if (/en[-_]us/i.test(v.lang)) score += 5;
    return score;
  };
  return [...voices].sort((a, b) => rank(b) - rank(a))[0];
}

// End-to-end test; used by the "Test Voice" button.
export async function test() {
  const sample = 'This is a test of the C2A2 narration voice. If you hear this clearly, your voice settings are working.';
  const s = getState();
  if (s.ttsProvider === 'openai' && !s.ttsApiKey) {
    throw new Error('No API key entered. Paste your OpenAI key and click Save.');
  }
  stop();
  const mySeq = ++requestSeq;
  if (s.ttsProvider === 'openai') {
    await speakOpenAI(sample, s, null, mySeq);
    toastSuccess('OpenAI TTS working — voice: ' + s.ttsVoiceOpenAI);
    return;
  }
  await new Promise((resolve) => speakBrowser(sample, s, resolve, mySeq));
  toastSuccess('Browser voice playing');
}

export function listBrowserVoices() {
  if (!window.speechSynthesis) return [];
  return window.speechSynthesis.getVoices().filter(v => v.lang?.startsWith('en'));
}
