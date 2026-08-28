# Lift Probe — oscillating fake-z in the existing SVG renderer

Answers one question: **does a candidate Z variable actually stratify the corpus?**
If it does not read here, it will not read in three.js either.

Target file: `wiki/c2a2-wiki-narration/scripts/generate_visualization.py`
NOT the built HTML — regen wipes HTML edits.

The embedded JS lives in a plain `"""` string (not an f-string), so `{`, `}` and `%`
are safe. Backslashes are NOT — this patch contains none. Keep it that way.

**Revised 2026-08-24** after measuring the live artifact. Two corrections from the
first draft are recorded at the bottom; read them before trusting anything here.

---

## STEP 0 — no regen needed

Measured on the live build (`wiki/wiki_narration.html`, 4,454 nodes / 125,372 links,
rebuilt 2026-08-24 13:30 ET). **The gate PASSES on raw bridge count:** 48.4% of nodes
off-floor against a 5% bar, 16 distinct levels, median degree 21, only 46 isolated nodes.

So the probe can run against what is already on disk. Do **not** trigger
`regen_sociogram.sh` for this — regen is gated on landing the Rohr univocity bridge
note ([[project_C2A2_push_audit_2026-08-23]], finding 1), and nothing here needs it.

Re-check any time with:

```
cd "$HOME/Documents/Claude/Projects/RC Karpathy Wiki Project/wiki"
python3 c2a2-wiki-narration/scripts/check_bridge_dist.py wiki_narration.html
```

---

## Metric choice — RAW COUNT is the recommendation

**Use `bridge_raw`.** A file connected to every tradition is making a real statement
about the corpus; it is connective tissue, not a table of contents. Hubs stay in.

An earlier draft of this file treated the registry files at the ceiling
(`open_questions.md`, `assumptions.md` at degree 2873, `for_lit_search.md` at 2949)
as a confound to be corrected away. That was wrong (Tom, 2026-08-24). The rule is
**include them unless they overwash other meaningful connection** — and overwash is
a separate axis of the design that is already handled.

### Why hubs on Z do not cause overwash

Z is node POSITION. Overwash is EDGE RENDERING. They are independent, and the edge
side already has a working guard — measured against the live 2,500-edge budget:

| score mode | surviving edges touching a top-10 hub | distinct nodes shown |
| --- | --- | --- |
| **editorial** (current default) | **11.3%** | 677 |
| cross-tradition | 48.8% | 556 |
| balanced | 77.6% | 476 |
| connected | 92.4% | 476 |

Edges touching a top-10 hub are **17.6%** of the full 125,372, so `editorial` holds
hubs *below* their base rate. The 2026-07-27 default already does this job. Run the
probe in `editorial`; if hubs ever look overwashing, that is the score-mode selector's
problem, not the Z variable's.

Honest caveats in those numbers: in editorial mode the top-**50** nodes still touch
70% of surviving edges, and 2,500 edges span only 677 of 4,454 nodes at 1x zoom — most
nodes render unconnected until you zoom (budget grows to 4x = 10,000 edges). Neither is
a defect introduced by the Z axis; both are pre-existing properties worth knowing.

### The alternates, kept as switches

Top-100 overlap between metrics is low — raw^density **7**, raw^cross **1**,
density^cross **26** — so these are near-orthogonal readings, worth a look before
committing:

| metric | what tops out | caveat |
| --- | --- | --- |
| **bridge_raw** (recommended) | registries and synthesis files | none that matters; hubs are signal |
| **bridge_density** — traditions / neighbours | degree-1 files scoring 1.000 | small denominator; rewards noise |
| **cross_fraction** — the generator's own `bridge: cross` field | the agent files | same denominator problem as density |

---

## EDIT 1 — two lines, at `generate_visualization.py:2171-2172`

Replace:

```js
function wpx(d) { return d.x + (d._wx || 0); }
function wpy(d) { return d.y + (d._wy || 0); }
```

With:

```js
function wpx(d) { return d.x + (d._wx || 0) + (d._lx || 0); }
function wpy(d) { return d.y + (d._wy || 0) + (d._ly || 0); }
```

That is the entire integration. Edges follow automatically because `linkSel`
already paints from `wpx`/`wpy` on its endpoints.

---

## EDIT 2 — insert immediately after `paintPositions()` ends

(after its closing brace, roughly line 2184, before the `// -- VOICE WAVE --` banner)

```js
// -- LIFT PROBE (temporary; delete when the Z question is settled) --
//
// Encodes a third variable as OSCILLATING FAKE DEPTH in the existing 2D SVG.
// No WebGL, no simulation changes, no pipeline changes.
//
// Why oscillate rather than hold: nodes sharing a Z value rise and fall
// together, and common fate (Gestalt) makes strata pop out perceptually without
// ever holding a static 3D scene the viewer has to parse.
//
// Depth cue is PARALLAX ONLY by default -- displacement away from / toward the
// viewport centre, proportional to distance from it, which is what perspective
// does. Size and brightness are stronger cues but collide with syncGraphToDate()
// and setBrightness(), which own r and opacity; they are opt-in via
// LiftProbe.cues(true), and the date slider must not be dragged while on.

var LIFT_PERIOD   = 6000;   // ms for a full down-up-down breath
var LIFT_PARALLAX = 0.22;   // peak radial displacement as a fraction of the
                            // node's distance from centre
var LIFT_RMIN     = 0.72;   // radius multiplier at the far plane (cues mode)
var LIFT_RMAX     = 1.35;   // radius multiplier at the near plane (cues mode)

var _liftRAF = null;
var _liftT0 = 0;
var _liftCues = false;

// Link endpoints are INTEGER INDICES into NODES as generated; d3 rewrites them
// to object refs once the simulation runs. Resolve all three forms or every
// node reads as degree 0 -- this bit me on the first draft.
function _liftAdjacency() {
  var byId = {};
  NODES.forEach(function(nd, i) { byId[nd.id] = i; });
  var resolve = function(v) {
    if (typeof v === 'number') return (v >= 0 && v < NODES.length) ? v : null;
    if (v && typeof v === 'object') { var r = byId[v.id]; return (r === undefined) ? null : r; }
    var s = byId[v];
    return (s === undefined) ? null : s;
  };
  var adj = [], crossN = [], degE = [];
  for (var i = 0; i < NODES.length; i++) { adj.push({}); crossN.push(0); degE.push(0); }
  LINKS.forEach(function(l) {
    var s = resolve(l.source), t = resolve(l.target);
    if (s === null || t === null) return;
    adj[s][t] = 1; adj[t][s] = 1;
    degE[s]++; degE[t]++;
    if (l.bridge === 'cross') { crossN[s]++; crossN[t]++; }
  });
  return { adj: adj, crossN: crossN, degE: degE };
}

function _liftTraditionsOf(i, A) {
  var seen = {}, count = 0;
  Object.keys(A.adj[i]).forEach(function(k) {
    var g = NODES[+k].group || '';
    if (g.indexOf('traditions/') !== 0) return;
    var key = g.split('/')[1];
    if (!seen[key]) { seen[key] = 1; count++; }
  });
  return count;
}

// --- Z EXTRACTORS -------------------------------------------------------
// Each returns an array of raw numbers, one per node, in NODES order.

var LIFT_VARS = {

  // Rich (48.4% nonzero, 16 levels) but its ceiling is registry files.
  bridge_raw: function() {
    var A = _liftAdjacency();
    return NODES.map(function(nd, i) { return _liftTraditionsOf(i, A); });
  },

  // Corrects the registry bias, introduces a small-denominator one.
  bridge_density: function() {
    var A = _liftAdjacency();
    return NODES.map(function(nd, i) {
      var deg = Object.keys(A.adj[i]).length;
      return deg ? _liftTraditionsOf(i, A) / deg : 0;
    });
  },

  // Same shape as density, but the numerator is the generator's own
  // cross/same edge classification rather than ours.
  cross_fraction: function() {
    var A = _liftAdjacency();
    return NODES.map(function(nd, i) {
      return A.degE[i] ? A.crossN[i] / A.degE[i] : 0;
    });
  },

  // Metabolic layer: raw intake at the floor, synthesis at the ceiling.
  // The CONTROL -- guaranteed non-degenerate, so it isolates whether the
  // oscillating-lift MECHANISM reads, separately from whether bridging does.
  layer: function() {
    var RANK = {
      inbox: 0, flags: 1, review: 2, sessions: 2, deferred: 2,
      root: 3, architecture: 4, agents: 5, 'agent-activity': 5,
      summa: 6, master: 8
    };
    return NODES.map(function(nd) {
      var g = nd.group || '';
      if (g.indexOf('traditions/') === 0) return 7;
      var r = RANK[g];
      return (r === undefined) ? 3 : r;
    });
  }

};

// --- INDEX + SELF-DIAGNOSIS ---------------------------------------------

function _liftIndex(varName) {
  var make = LIFT_VARS[varName];
  if (!make) {
    console.warn('[lift] unknown variable: ' + varName +
                 '. Options: ' + Object.keys(LIFT_VARS).join(', '));
    return false;
  }
  var raws = make();
  var lo = Infinity, hi = -Infinity;
  raws.forEach(function(v) {
    if (typeof v !== 'number' || !isFinite(v)) v = 0;
    if (v < lo) lo = v;
    if (v > hi) hi = v;
  });
  var span = (hi - lo) || 1;
  var levels = {}, offFloor = 0;
  NODES.forEach(function(nd, i) {
    var v = raws[i];
    if (typeof v !== 'number' || !isFinite(v)) v = 0;
    nd._lz = (v - lo) / span;    // normalised depth, 0 = far, 1 = near
    nd._lzRaw = v;
    levels[v] = 1;
    if (v > lo) offFloor++;
  });
  var nLevels = Object.keys(levels).length;
  var pct = 100 * offFloor / NODES.length;
  console.log('[lift] variable=' + varName + '  range=' + lo + '..' + hi +
              '  levels=' + nLevels + '  off-floor=' + pct.toFixed(1) + '%');
  if (nLevels < 3 || pct < 5) {
    console.warn('[lift] DEGENERATE -- fails the >=5% / >=3-levels gate. Do not ' +
                 'conclude the variable is unreadable; conclude this BUILD cannot ' +
                 'answer it.');
  }
  return true;
}

// --- ANIMATION ----------------------------------------------------------

function _liftApply(t) {
  var svg = document.getElementById('graph');
  var cx = (svg ? svg.clientWidth : window.innerWidth) / 2;
  var cy = (svg ? svg.clientHeight : window.innerHeight) / 2;
  NODES.forEach(function(nd) {
    if (nd.x === undefined) return;
    var lz = (nd._lz === undefined) ? 0.5 : nd._lz;
    var k = LIFT_PARALLAX * t * (lz - 0.5) * 2;
    nd._lx = (nd.x - cx) * k;
    nd._ly = (nd.y - cy) * k;
  });
  paintPositions();
  if (_liftCues && nodeSel) {
    nodeSel.attr('r', function(d) {
      var lz = (d._lz === undefined) ? 0.5 : d._lz;
      var m = LIFT_RMIN + (LIFT_RMAX - LIFT_RMIN) * (0.5 + (lz - 0.5) * t * 2);
      return d.size * m;
    }).attr('opacity', function(d) {
      if (!groupVisibility[d.group]) return 0;
      var lz = (d._lz === undefined) ? 0.5 : d._lz;
      return Math.min(brightness * (0.45 + 0.55 * (0.5 + (lz - 0.5) * t * 2)), 1);
    });
  }
}

function _liftTick(ts) {
  if (!_liftT0) _liftT0 = ts;
  var phase = ((ts - _liftT0) % LIFT_PERIOD) / LIFT_PERIOD;
  _liftApply(0.5 - 0.5 * Math.cos(2 * Math.PI * phase));   // smooth 0 -> 1 -> 0
  _liftRAF = requestAnimationFrame(_liftTick);
}

var LiftProbe = {

  start: function(varName) {
    this.stop();
    if (!_liftIndex(varName || 'bridge_raw')) return;
    _liftT0 = 0;
    _liftRAF = requestAnimationFrame(_liftTick);
    console.log('[lift] running. LiftProbe.stop() to clear, LiftProbe.cues(true) ' +
                'for size+brightness (do not drag the date slider while on).');
  },

  stop: function() {
    if (_liftRAF) cancelAnimationFrame(_liftRAF);
    _liftRAF = null;
    NODES.forEach(function(nd) { nd._lx = 0; nd._ly = 0; });
    if (nodeSel) nodeSel.attr('r', function(d) { return d.size; });
    if (typeof brightness !== 'undefined') setBrightness(brightness);
    paintPositions();
  },

  cues: function(on) { _liftCues = !!on; if (!on) this.stop(); },

  // Freeze at a chosen point in the breath, for screenshots / close reading.
  hold: function(t) {
    if (_liftRAF) { cancelAnimationFrame(_liftRAF); _liftRAF = null; }
    _liftApply(t);
  },

  // Top-N by the currently indexed variable -- read the ceiling without
  // squinting at the picture.
  top: function(k) {
    var order = NODES.slice().sort(function(a, b) { return b._lzRaw - a._lzRaw; });
    order.slice(0, k || 10).forEach(function(nd) {
      console.log('  ' + nd._lzRaw + '  ' + nd.id + '  [' + nd.group + ']');
    });
  }

};
// -- END LIFT PROBE --
```

---

## STEP 3 — run it

Open the built page, then in the console:

```js
LiftProbe.start('layer')            // 1. control: does the MECHANISM read at all?
LiftProbe.start('bridge_raw')       // 2. the recommendation
LiftProbe.top(15)                   // what is at the ceiling right now
LiftProbe.cues(true)                // stronger depth; conflicts with date slider
LiftProbe.hold(1.0)                 // freeze at peak lift for a screenshot
LiftProbe.stop()

LiftProbe.start('bridge_density')   // only if raw disappoints
LiftProbe.start('cross_fraction')   // only if raw disappoints
```

Run `layer` first. If the control does not read, nothing else you see means anything.
Leave the score mode on `editorial` — that is what keeps hub edges from overwashing.

## What counts as an answer

- **Control reads, `bridge_raw` visibly separates** -> done. Bridging goes on r in the
  2.5D build, hubs included.
- **Control reads, raw looks flat or muddy** -> try density and cross_fraction before
  concluding anything; they are near-orthogonal readings of the same idea.
- **Control reads, none of the three separate** -> bridging is real in the data but not
  spatially coherent. `layer` becomes the Z candidate instead.
- **Control does not read** -> oscillating parallax is too weak a cue at this density.
  Real finding, kills the 2.5D direction cheaply, which is the point.

If `bridge_raw` reads but the picture feels dominated by a handful of hubs, the lever is
the score-mode selector (try `cross-tradition`), **not** a change to the Z variable.

## Corrections from the first draft (2026-08-24)

1. **I measured the wrong file.** `c2a2-wiki-narration/output/wiki_narration.html` is a
   4MB leftover from May 7 at an old build location. The live artifact is
   `wiki/wiki_narration.html` (50MB) — the path `regen_sociogram.sh` actually writes.
   The first draft's "stale and mis-built, no summa, no mention edges" finding describes
   the dead file and should be disregarded. The live build is current and complete.
2. **Integer link endpoints.** Both the checker and the probe's adjacency builder
   assumed string or object endpoints. The generator emits integer indices, so every
   node read as degree 0 and the first measurement (0.2% nonzero) was my bug, not a
   property of the data. Fixed in `_liftAdjacency()` and in `check_bridge_dist.py`.

## Cleanup

Delete both edits when the question is settled. If the answer is "build it", the
oscillator becomes the easing for the lift slider and `LIFT_VARS` becomes the
Z-variable selector — neither is wasted.
