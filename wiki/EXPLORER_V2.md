# C2A2 Explorer — Branch `explorer-shell-v2`
*Last updated: 2026-05-02*

## What this branch contains

### `explorer.html` — Shell redesign ✅

The outer tab-bar shell was renamed and restructured to reflect the system's full purpose.

**Title:** C2A2 Community Dialogue Accelerator/Detector System

**New two-row tab bar:**
- Row 1 (48 px): System brand + four chapter-level tabs + Record button
- Row 2 (40 px): Sub-tool tabs scoped to the active chapter

**Four chapter tabs:**

| Tab | Status | Notes |
|-----|--------|-------|
| Community Explorer | 🚧 Stub | Dimmed, unresponsive; 🚧 tooltip on hover |
| Community AI Education | 🚧 Stub | Dimmed, unresponsive; 🚧 tooltip on hover |
| Community Accelerator Tools | ✅ Active | Houses the four working sub-tools |
| Community Interaction | 🚧 Stub | Dimmed, unresponsive; 🚧 tooltip on hover |

**Community Accelerator Tools sub-tabs** (row 2, all functional):
- **Sociogram** → `wiki_narration.html`
- **3D PRS** → `prs_3d.html`
- **Agent Map** → `agents_tab.html`
- **Curriculum Tools** → `summa_explorer.html` (Summa Explorer)

Record button remains at far right of row 1; screen+mic recording pipeline unchanged.

---

### `wiki_narration.html` — Narration engine (attempted fix) ⚠️ NOT YET RESOLVED

**Symptom (Tom's description):** The narration engine has temporal/semantic mode state leakage. Starting in temporal mode and switching to semantic does not properly reset the speech queue or position cursor — the engine continues from wherever temporal left off, often choking mid-utterance, rather than re-reading the scene from the beginning in the new mode.

**Attempted fixes in this branch:**

1. `toggleNarrationMode()` — Added full stop before mode switch: clears `isPlaying`, `isPaused`, `playTimer`, and calls `TTS.stop()` (which clears `TTS.onFinished` and calls `speechSynthesis.cancel()`). Rationale: without this, the old utterance's `onend` fires `scheduleNextSegment()` after the mode variable is already flipped, stomping the fresh `currentSegmentIndex = 0`.

2. `TTS.speak()` — Added 50 ms `setTimeout` gap between `cancel()` and the next `speak()` call. Rationale: Chrome's `speechSynthesis.cancel()` is asynchronous; calling `speak()` in the same tick can silently fail or stutter.

3. `TTS.stop()` — Added silent flush utterance (volume 0) followed by a second `cancel()`. Rationale: Chrome leaves stale utterances in its internal queue even after `cancel()`; the double-cancel with a zero-volume utterance is a known workaround.

**Result:** Fixes did not resolve the issue in testing. The choking and state-leakage behavior persists.

---

## What remains to be done

### Priority 1 — Narration engine temporal/semantic mode repair

The three fixes above addressed the most obvious causes but the behavior is unchanged. The likely remaining issues:

- **Speech synthesis queue depth:** Chrome may have already queued multiple utterances before the first `cancel()` fires. The 50 ms delay helps but may not be enough; the queue may need to be drained across multiple ticks.
- **`advancePlay()` re-entry:** After mode switch and a manual Play press, `advancePlay()` may be entering before the synthesis engine has fully settled. Needs a state guard (e.g., a `isSwitching` flag that blocks `advancePlay()` for one animation frame after mode change).
- **`currentTrack` stale reference:** Switching modes while a track is playing preserves `currentTrack` (e.g., `'history'`). The semantic track for `'history'` is structurally different from temporal `'history'` — it may be empty or pointing at wrong segments, causing silent failures rather than audible errors.
- **Full audit needed:** Both `buildNarrationTracks()` and the semantic track-building logic need a line-by-line read to confirm the semantic track is actually being populated correctly before attempting further speech-engine fixes.

**Suggested next approach:** Add `console.log` instrumentation to `toggleNarrationMode()`, `scheduleNextSegment()`, `advancePlay()`, and `TTS.speakBrowser()` to trace the actual execution order during a mode switch mid-playback. The fix should follow the trace, not further speculation.

### Priority 2 — Chapter tab population (future sessions)

- **Community Explorer (Tab 1):** Already written — needs integration into the tab
- **Community AI Education (Tab 2):** AI Heartbeat tool — already developed, needs integration
- **Community Interaction (Tab 4):** Cross-tradition dialogue tools (prefigured in PRS framework)
- **Curriculum Tools sub-menu:** Expand to show Aquinas comparison alongside Summa Explorer

### Priority 3 — Sociogram expansion

Add Aquinas as the 16th thinker to the sociogram in `wiki_narration.html`, connecting to the Summa Explorer.
