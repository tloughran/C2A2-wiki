# Shell patch — wire `start_here.html` into `explorer.html`

Four small edits, all in `wiki/explorer.html`. Line numbers are from the
2026-06-19 version (the one currently on disk); the anchor text is given so
you can place each edit even if lines have drifted. Nothing existing is
removed — these are pure inserts.

After applying: serve `wiki/` over HTTP and visually verify per the
constitutional rule before any push.

---

## EDIT 1 — add the chapter button (Row 1)

In the `<div id="row1">` block, add `chap-intro` as the **first** chapter,
just before `chap-community`.

**Find:**
```html
    <button class="chap-btn" id="chap-community" data-src="community_explorer.html">Community Explorer</button>
```
**Insert immediately above it:**
```html
    <button class="chap-btn" id="chap-intro" data-src="start_here.html">Start here</button>
```

---

## EDIT 2 — chapter variable + click handler

Inside the main IIFE, near the other `chap*` vars (the block beginning
`var chapCommunity = document.getElementById('chap-community');`), add the
intro var and its handler. Mirrors the `chapCommunity` pattern exactly
(loads a full page into the iframe, hides both sub-tab rows).

**Find:**
```js
  if (chapCommunity) chapCommunity.addEventListener('click', function() {
    setFrame(chapCommunity.getAttribute('data-src') + '?v=' + Date.now());
    if (row2) row2.style.display = 'none';
    if (row2edu) row2edu.style.display = 'none';
    setActiveChapter(chapCommunity);
  });
```
**Insert immediately above it:**
```js
  var chapIntro = document.getElementById('chap-intro');
  if (chapIntro) chapIntro.addEventListener('click', function() {
    setFrame(chapIntro.getAttribute('data-src') + '?v=' + Date.now());
    if (row2) row2.style.display = 'none';
    if (row2edu) row2edu.style.display = 'none';
    setActiveChapter(chapIntro);
  });
```

---

## EDIT 3 — listen for launch messages from start_here.html

Add this just before the IIFE closes (the line `})();` that follows
the `pageshow` listener). It reuses the shell's own `setFrame`,
`setActiveChapter`, `row2`, `row2edu`, `chapTools`, and `chapIntro`.

**Find:**
```js
  frame.addEventListener('load', syncShellToFrame, { once: true });
  window.addEventListener('pageshow', function(e) { if (e.persisted) syncShellToFrame(); });
})();
```
**Insert the listener between the `pageshow` line and `})();`:**
```js

  // ── START-HERE LAUNCH LINKS ──
  // start_here.html posts {source:'c2a2-start-here', action:'navigate', target}.
  // We switch chapter/tab here; the pinned tab bar is the way back.
  function lightTab(rowId, src) {
    var row = document.getElementById(rowId);
    if (!row) return;
    row.querySelectorAll('.tab-btn').forEach(function(b) {
      b.classList.toggle('active', b.getAttribute('data-src') === src);
    });
  }
  window.addEventListener('message', function(e) {
    var d = e.data;
    if (!d || d.source !== 'c2a2-start-here' || d.action !== 'navigate') return;
    switch (d.target) {
      case 'fifteen':                                 // What's this? → 15 framings
        setFrame('what_is_c2a2.html?v=' + Date.now());
        if (row2) row2.style.display = 'none';
        if (row2edu) row2edu.style.display = 'none';
        if (chapIntro) setActiveChapter(chapIntro);
        break;
      case 'review-cards':                            // So what? → review cards
        setFrame('review_log.html?v=' + Date.now());
        if (row2) row2.style.display = 'none';
        if (row2edu) row2edu.style.display = 'none';
        if (chapIntro) setActiveChapter(chapIntro);
        break;
      case 'sociogram':                               // Who's who? → sociogram
        if (row2) row2.style.display = '';
        if (row2edu) row2edu.style.display = 'none';
        lightTab('row2', 'wiki_narration.html');
        setFrame('wiki_narration.html?v=' + Date.now());
        setActiveChapter(chapTools);
        break;
      case 'summa-commentary':                        // So what? → Summa commentary
        if (row2) row2.style.display = '';
        if (row2edu) row2edu.style.display = 'none';
        lightTab('row2', 'summa_explorer.html');
        setFrame('summa_explorer.html?v=' + Date.now());
        setActiveChapter(chapTools);
        break;
    }
  });
```

---

## EDIT 4 (optional polish) — back-button resync

So the browser Back button re-lights the "Start here" chapter when the
iframe is showing `start_here.html`. In `syncShellToFrame`, add a branch.

**Find:**
```js
    } else if (chapCommunity && chapCommunity.getAttribute('data-src') === path) {
      if (row2) row2.style.display = 'none';
      if (row2edu) row2edu.style.display = 'none';
      setActiveChapter(chapCommunity);
    }
```
**Insert another branch just above the `chapCommunity` one:**
```js
    } else if (chapIntro && chapIntro.getAttribute('data-src') === path) {
      if (row2) row2.style.display = 'none';
      if (row2edu) row2edu.style.display = 'none';
      setActiveChapter(chapIntro);
```
(Note: the existing `chapCommunity` branch keeps its leading `} else if` — you're
inserting a new `} else if … {` block immediately before it.)

---

## OPTIONAL — make "Start here" the landing screen

First-time visitors would then land on the intro instead of the Sociogram.
Two one-line changes:

1. The `<iframe id="content-frame" … src="wiki_narration.html">` → `src="start_here.html"`.
2. In Row 1, move `class="active"` off `chap-tools` and onto `chap-intro`;
   and set `<div id="row2" style="display:none">` so the Accelerator sub-tabs
   start hidden (the intro chapter has no sub-tab row).

Hold this one until you've eyeballed the page — it changes what everyone sees on load.

---

## Smoke test (local, before push)

```bash
cd "wiki" && python3 -m http.server 8080
# open http://localhost:8080/explorer.html
```
Check: "Start here" appears leftmost; clicking it loads the 3-section page;
each of the 4 launch links switches the view (15 framings, sociogram with the
Sociogram sub-tab lit, review cards, Curriculum/Summa); the tab bar persists so
clicking "Start here" again returns you. No console errors.
