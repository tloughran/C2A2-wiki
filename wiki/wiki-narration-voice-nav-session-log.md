# Wiki Narration — Voice & Navigation Session Log

**Date**: 2026-06-24
**File modified**: `wiki_narration.html` (all changes inline, no new files)

---

## Session scope

Added four interconnected capabilities to the C2A2 sociogram's existing TTS/search system, then hardened error handling and extended the AI query backend options.

---

## 1. TTS — Three-provider system

Settings modal (⚙ button, footer) provider selector now offers three options.

| Provider | Quality | Cost | Privacy | First-run |
|---|---|---|---|---|
| Browser (basic) | Robotic, OS-dependent | Free | Local | Instant |
| Kokoro (neural) | Neural, consistent | Free | Local | ~83 MB download, then cached |
| OpenAI (premium) | Best | Pay-per-use | API call | API key in settings |

**Kokoro details**
- Model: `onnx-community/Kokoro-82M-v1.0-ONNX`, q8 quantisation, 82 M params
- Loaded via `https://cdn.jsdelivr.net/npm/kokoro-js@1/+esm` (dynamic import on first use — no build step, no upfront cost)
- Device: auto-detects `navigator.gpu` → WebGPU if available (fast, requires https:// or localhost), falls back to WASM
- WASM caveat: ~10–30 s inference on CPU, can trigger "page unresponsive" dialog during JIT compilation on first load. Serve over `http://localhost:8000` to unlock WebGPU and eliminate this.
- Progress shown in narration bar during download; cached across sessions by browser HTTP cache
- 10 voices: Heart, Sky, Bella, Nicole (US female) / Emma, Isabella (UK female) / Adam, Michael (US male) / George, Lewis (UK male)

**Key storage**: TTS provider and voice stored in `localStorage`; OpenAI TTS key stored in `sessionStorage` only (clears on tab close).

---

## 2. Voice input (Web Speech API)

**Mic button** 🎤 added to footer (left of mute button). Click to start listening; click again to cancel. Button turns 🔴 while recording.

Works in Chrome and Edge. Requires microphone permission. Works from `file://` with user permission granted.

**Routing logic — two tiers:**

```
Voice transcript
  ↓
stripNavPrefix()  — detects and strips navigational openers
  │
  ├─ NAV QUERY detected ("show me X", "find X", "go to X", …)
  │     stripped remainder → parseBareGuess()
  │       ├─ resolves (known group/thinker name) → graph command instantly, offline
  │       └─ doesn't resolve → runSearchAI() [only if Ask AI checkbox is on]
  │
  └─ INFO QUERY (no navigation prefix)
        → runSearchAI() if Ask AI on, else runSearch() (local, no quota)
```

**Navigation prefixes stripped**: `show me`, `take me to`, `go to`, `navigate to`, `highlight`, `zoom to`, `zoom in on`, `look at`, `find`, `open`, `display`, `bring up`, `pull up`

**Important**: Voice respects the Ask AI checkbox. With Ask AI off, voice queries run local text/graph search only — no API quota consumed.

---

## 3. Navigation command engine

**`navigateByCmd(cmd)`** — universal graph navigation dispatcher. Called by AI responses (when the AI returns a `cmd` field) and by voice routing (for locally-resolvable navigational queries).

| `cmd` value | Action |
|---|---|
| `"levin"` | `isolateGroups(['traditions/levin'])` — Levin nodes bright, rest faded |
| `"levin friston"` | `linkGroups([...])` — nodes bridging the two traditions |
| `"focus: levin ~ summa"` | `runFocus()` — links between thinker and structure group |
| plain text | local text search (non-AI, no recursion risk) |

The resolved command is mirrored in the search box so the user always sees what fired.

**`stripNavPrefix(text)`** — detects navigational openers, returns the bare target or `null` if informational.

---

## 4. AI prompt enhancements

### `cmd` field in AI responses

Both system prompts (`C2A2_SOC_SYSTEM_DATASET` and `C2A2_SOC_SYSTEM_WEB`) now instruct the model to include an optional `"cmd"` field for navigational queries, using the group leaf names visible in the candidate list. When present, `navigateByCmd(parsed.cmd)` fires after node highlighting — the graph moves in direct response to the query.

Informational queries (`"what is X?"`, `"compare X and Y"`) omit `cmd`.

### `CURRENT_VIEW` context injection

**`getCurrentViewState()`** reads live D3 node opacity at query time. If a meaningful focus is active (< 85% of nodes at full brightness), it builds a prose block listing the highlighted nodes with their group labels and active traditions. This is prepended to the AI prompt as `CURRENT_VIEW:`.

Enables queries like:
- *"What am I looking at?"*
- *"Why are these nodes connected?"*
- *"Describe the cluster I've isolated"*

When no focus is active (all nodes at full brightness), `viewCtx` is null and nothing extra is sent — no prompt bloat for standard queries.

---

## 5. Free-limit handling

C2A2 broker free tier returns error code `free-limit` when the daily quota is exhausted. Previously this showed a cryptic "AI request failed" message. Now:

- "Ask AI" checkbox is automatically unchecked
- Falls back to local text search for the same query (user still gets a result)
- Narration bar explains what happened and suggests re-enabling later or adding a personal key

`rate-limited` (HTTP 429) is handled identically.

---

## 6. AI Query Provider — Groq and Ollama

New **AI Query** section in Settings modal, below TTS settings. Bypasses the C2A2 broker with direct OpenAI-compatible API calls.

| Provider | Key required | Free tier | Notes |
|---|---|---|---|
| C2A2 broker | Shared (built-in) | Yes — limited | Default. Falls back to local search on cap. |
| **Groq** | Own key | **Yes, generous** | `console.groq.com`, no credit card. ~14,400 req/day free. |
| **Ollama** | None | **Unlimited** | Fully local, fully offline. Install at `ollama.com`. |
| OpenAI direct | Own key | No | Pay-as-you-go, your own rate limits. |

**Default models**
- Groq: `llama-3.3-70b-versatile`
- Ollama: `llama3.2` (run `ollama pull llama3.2` first, ~2 GB)
- OpenAI direct: `gpt-4o-mini`

Model field is editable — any OpenAI-compatible model string works.

**Key security**: API keys for Groq and OpenAI direct are stored in `sessionStorage` only (not `localStorage`) — cleared when the tab closes, never written to disk by the browser.

**Ollama setup** (one-time):
```bash
# Install from ollama.com, then:
ollama pull llama3.2
ollama serve          # starts at localhost:11434
```
Then select "Ollama — local" in Settings. No key, no network, completely private.

---

## Architecture notes

- All new JS lives in the single `wiki_narration.html` inline script block — no new files, no build step
- If regenerating via the Python generator: regular strings only, no f-strings, single `{` `}` braces throughout
- The search box (`#search-input`) is the universal navigation controller — `navigateByCmd()` routes through `runSearch()` which dispatches to `runFocus()`, `isolateGroups()`, or `linkGroups()`
- `TTS.speak()` is the single audio output point for all voice responses
- `getCurrentViewState()` reads D3 opacity live — no separate state variable needed
- The `AI` object mirrors the `TTS` object pattern: stored state + `callDirect()` method

---

## Open items / next session

- [ ] **WebGPU for Kokoro**: serve over `python3 -m http.server 8000` at `localhost:8000/wiki_narration.html` — unlocks WebGPU, eliminates page-freeze dialogs, dramatically faster TTS
- [ ] **Whisper offline STT**: replace Web Speech API with `openai/whisper-base` via transformers.js — same lazy-load pattern as Kokoro, ~150 MB, fully private, cross-browser
- [ ] **Screenshot → vision model** (Option B for graph-state queries): capture SVG as PNG, send to GPT-4o with query — for "what's unusual about this cluster?" style questions that need the visual, not just the data
- [ ] **ISME demo hardening**: test full voice → navigation → spoken-answer loop on a clean browser session with Groq as the AI provider
