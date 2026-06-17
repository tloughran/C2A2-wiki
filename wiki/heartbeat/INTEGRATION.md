# Heartbeat → Community Education tab — surgical integration

**Do NOT apply the original update bundle's `explorer.html`, `EXPLORER_V2.md`, or
`c2a2-wiki-shell-changes.patch`.** They were built against an older shell where
"Community AI Education" was a dead stub, and they would *revert* your current
Education chapter (RC Document Explorer / Physics Explorer / TRV Commentary in
`#row2-edu`). Heartbeat belongs as a **fourth Education Tools sub-tab**, not a
chapter takeover.

Your live `explorer.html` already does all the wiring generically: the `.tab-btn`
click handler, the `#row2-edu` active-state scoping, and the `syncShellToFrame`
back-nav resync all pick up any new button automatically. So the integration is
**two small insertions**. No JS changes.

---

## Edit 1 — add the sub-tab button

In `wiki/explorer.html`, in the `#row2-edu` row (around line 345), add one button
after the TRV Commentary button:

```html
    <button class="tab-btn" data-src="commentary-explorer/commentary_explorer.html">TRV Commentary</button>
    <button class="tab-btn" data-src="heartbeat/index.html">AI Heartbeat</button>   <!-- ADD THIS LINE -->
    <button class="btn-help-row" onclick="showHelp()" title="About this view">?</button>
```

## Edit 2 — add the help-modal entry

In the `descriptions` object inside `showHelp()` (around line 746), add an entry
after the `commentary-explorer/commentary_explorer.html` block:

```js
    'heartbeat/index.html': {
      title: 'AI Heartbeat',
      body: 'A Karpathy-style compiled wiki over fast-moving AI developments, reframed for community AI education. Raw sources stay immutable; heartbeat runs fetch, dedupe, summarize, tag, and score relevance; a compiled markdown layer preserves durable synthesis, contradictions, and decisions; each community applies its own lens, roles, and consent rules; selected stars and rankings can flow to a shared graph. The Pulse view loads from a static digest snapshot (data/digest.json) with an embedded fallback, so the tab is GitHub Pages-safe with no live backend. Fourth Education tool.'
    },
```

(Optionally update the `<!-- ROW 2-EDU ... -->` comment above the row from
"All three planned tools" to four.)

---

## Why nothing else is needed

- **Routing:** the generic `.tab-btn` handler calls `setFrame(data-src + '?v=' + Date.now())`
  and scopes `active` to the button's own row — works for the new button as-is.
- **Chapter switch:** `chapEducation`'s click handler already selects the first
  non-disabled `#row2-edu .tab-btn`, so RC Document Explorer stays the default.
- **Back-nav resync:** `syncShellToFrame` matches by filename, so landing on
  `heartbeat/index.html` lights up the right tab and row.
- **Iframe sandbox:** `heartbeat/index.html` is plain HTML/CSS/vanilla JS plus a
  same-origin `fetch('data/digest.json')`; the existing iframe `sandbox`
  (`allow-scripts allow-same-origin ...`) already permits it.

## Verify before any push (per the no-blind-push rule)

```bash
cd "/Users/tloughr1/Documents/GitHub/C2A2-wiki/wiki"   # or your project wiki/
python3 -m http.server 8080
# open http://localhost:8080/explorer.html
# → Community Education → AI Heartbeat
```

Expect: metrics row shows 5 / 95 / 2 / "Agents + Governance", a gold "Sample / seed
data" banner, a provenance line ("weekly window · snapshot 2026-06-17"), and five
signal cards. The five inner mode tabs (Pulse / Compiled Wiki / Community Lens /
Federation / Integration) switch. Over `file://` the fetch is blocked and the tab
falls back to the embedded copy (banner still shows) — that is expected; serve over
HTTP for the true snapshot path.
