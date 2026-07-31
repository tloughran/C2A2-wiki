// scripts/test_sociogram_wave.cjs
//
//   node scripts/test_sociogram_wave.cjs
//
// Exercises the Sociogram's VoiceWave receiver outside a browser, by cutting the
// module straight out of the SHIPPED wiki/wiki_narration.html and running it
// against stub globals. Reading the artifact rather than the generator is the
// point: the artifact is what a visitor loads, and it has been edited in place
// before now.
//
// These assert the properties the feature depends on, not that it moves:
//
//   1. The wave never enters d.x/d.y. The force simulation reads those back on
//      every tick, so a displacement written there would be absorbed into the
//      layout and kept -- the graph would drift further from its own solution
//      every time the guide spoke, and nothing would put it back.
//   2. Silence settles EXACTLY on the simulation's positions and ends the rAF
//      loop. A wave that stalls mid-crest leaves the graph permanently wrong in
//      a way that looks deliberate.
//   3. A driver that vanishes mid-sentence is the same as silence -- the shell
//      can be closed, or the tab switched, at any moment.
//   4. prefers-reduced-motion means no motion, not less of it.
//   5. The origin is refused when it cannot be resolved, rather than quietly
//      falling back to centre: a wave emanating from the wrong place is a claim
//      about what is being talked about, and a wrong one is worse than none.
const fs = require('fs');
const path = require('path');

const ART = path.join(__dirname, '..', 'wiki', 'wiki_narration.html');
const html = fs.readFileSync(ART, 'utf8');
const A = html.indexOf('// ── PAINT LAYER ──');
const B = html.indexOf('// ── GRAPH ──');
if (A < 0 || B < 0 || B <= A) {
  console.error('FAIL  could not find the paint-layer/wave module in ' + ART);
  console.error('      (markers moved or the artifact was regenerated from an older template)');
  process.exit(2);
}
const src = html.slice(A, B);

let FAIL = 0;
function ok(name, cond, extra) {
  if (cond) { console.log('  PASS  ' + name); }
  else { FAIL++; console.log('  FAIL  ' + name + (extra !== undefined ? '  -> ' + extra : '')); }
}

// ---- environment ---------------------------------------------------------
function makeEnv(reducedMotion) {
  const env = {};
  let clock = 1000;
  const rafQueue = [];

  env.now = () => clock;
  env.advance = (ms) => { clock += ms; };
  env.painted = { nodes: 0, links: 0 };

  env.nodes = [
    { id: 'a', x: 0,   y: 0 },
    { id: 'b', x: 300, y: 0 },
    { id: 'c', x: 0,   y: 450 },
    { id: 'd', x: -700, y: -200 },
  ];
  env.nodes.forEach(n => { n._x0 = n.x; n._y0 = n.y; });

  const ctx = {
    activeNodes: env.nodes,
    nodeById: Object.fromEntries(env.nodes.map(n => [n.id, n])),
    linkSel: null,
    nodeSel: null,
    d3: { zoomTransform: () => ({ invert: (p) => [p[0], p[1]] }) },
    document: { hidden: false, getElementById: () => ({ clientWidth: 800, clientHeight: 600 }) },
    requestAnimationFrame: (fn) => { rafQueue.push(fn); return rafQueue.length; },
    Math, Number, isFinite, console,
  };
  ctx.window = {
    performance: { now: () => clock },
    matchMedia: (q) => ({ matches: reducedMotion && /reduce/.test(q) }),
  };
  ctx.window.window = ctx.window;

  // Selection stubs: record the coordinates the paint layer writes.
  const mkSel = (data, keys, sink) => {
    const sel = {
      attr(k, fn) {
        data.forEach((d, i) => { sink[i] = sink[i] || {}; sink[i][k] = typeof fn === 'function' ? fn(d, i) : fn; });
        return sel;
      }
    };
    return sel;
  };
  env.nodePaint = [];
  env.linkPaint = [];
  const links = [{ source: env.nodes[0], target: env.nodes[1] }];
  ctx.nodeSel = mkSel(env.nodes, null, env.nodePaint);
  ctx.linkSel = mkSel(links, null, env.linkPaint);

  const vm = require('vm');
  vm.createContext(ctx);
  vm.runInContext(src, ctx);
  env.ctx = ctx;
  env.VoiceWave = ctx.window.VoiceWave;
  // Drain one rAF generation per frame, the way a browser would.
  env.frame = (ms) => {
    env.advance(ms === undefined ? 16 : ms);
    const due = rafQueue.splice(0, rafQueue.length);
    due.forEach(fn => fn());
  };
  env.pending = () => rafQueue.length;
  return env;
}

// ---- 1. the wave never enters the simulation's own coordinates -----------
console.log('the wave is paint, not layout');
{
  const env = makeEnv(false);
  env.VoiceWave.speak(0.9);
  let moved = false;
  for (let i = 0; i < 40; i++) {
    env.frame();
    env.VoiceWave.speak(0.9);
    if (env.nodes.some(n => Math.abs(n._wx || 0) > 0.01)) moved = true;
  }
  ok('nodes are displaced while speaking', moved);
  ok('d.x is untouched by the wave',
     env.nodes.every(n => n.x === n._x0 && n.y === n._y0),
     JSON.stringify(env.nodes.map(n => [n.x, n._x0])));
  // The painted value is the sum, so the displacement is real on screen.
  const i = env.nodes.findIndex(n => Math.abs(n._wx) > 0.01);
  ok('painted cx equals d.x + d._wx',
     Math.abs(env.nodePaint[i].cx - (env.nodes[i].x + env.nodes[i]._wx)) < 1e-9);
  ok('edge endpoints are painted through the same offset',
     Math.abs(env.linkPaint[0].x1 - (env.nodes[0].x + (env.nodes[0]._wx || 0))) < 1e-9);
}

// ---- 2. silence settles exactly on the layout, and stops the loop --------
console.log('silence settles rather than freezes');
{
  const env = makeEnv(false);
  env.VoiceWave.speak(0.9);
  for (let i = 0; i < 20; i++) { env.frame(); env.VoiceWave.speak(0.9); }
  env.VoiceWave.silent();
  let frames = 0;
  while (env.pending() > 0 && frames < 600) { env.frame(); frames++; }
  ok('the rAF loop ends on its own', env.pending() === 0, 'frames=' + frames);
  ok('every offset is exactly zero at rest',
     env.nodes.every(n => n._wx === 0 && n._wy === 0),
     JSON.stringify(env.nodes.map(n => n._wx)));
  ok('the final paint is the simulation position, to the pixel',
     env.nodes.every((n, i) => env.nodePaint[i].cx === n.x && env.nodePaint[i].cy === n.y));
}

// ---- 3. a driver that goes away must not freeze the graph mid-crest ------
console.log('a driver that stops talking');
{
  const env = makeEnv(false);
  env.VoiceWave.speak(0.9);
  for (let i = 0; i < 20; i++) { env.frame(); env.VoiceWave.speak(0.9); }
  // No further samples at all -- simulates the shell disappearing.
  let frames = 0;
  while (env.pending() > 0 && frames < 600) { env.frame(); frames++; }
  ok('stale samples time out and the wave settles', env.pending() === 0, 'frames=' + frames);
  ok('settled to zero after the driver vanished', env.nodes.every(n => n._wx === 0));
}

// ---- 4. reduced motion means no motion ----------------------------------
console.log('prefers-reduced-motion');
{
  const env = makeEnv(true);
  ok('VoiceWave reports itself disabled', env.VoiceWave.enabled === false);
  env.VoiceWave.speak(1.0);
  ok('no rAF loop is started', env.pending() === 0);
  ok('no node is displaced', env.nodes.every(n => !n._wx));
  ok('demo() refuses too', typeof env.VoiceWave.demo(5) === 'string' && env.pending() === 0);
}

// ---- 5. origin resolution -----------------------------------------------
console.log('the origin is what the guide is talking about');
{
  const env = makeEnv(false);
  ok('a known node id is accepted', env.VoiceWave.origin('b') === true);
  ok('an unknown id is refused, not silently centred', env.VoiceWave.origin('nope') === false);
  ok('an explicit point is accepted', env.VoiceWave.origin({ x: 10, y: 10 }) === true);
  ok('null falls back to the view centre', env.VoiceWave.origin(null) === true);

  // A wave centred on 'b' must displace 'b' least (r=0 is the still point).
  env.VoiceWave.origin('b');
  env.VoiceWave.speak(0.9);
  for (let i = 0; i < 30; i++) { env.frame(); env.VoiceWave.speak(0.9); }
  const bi = env.nodes.findIndex(n => n.id === 'b');
  ok('the origin node itself does not move', env.nodes[bi]._wx === 0 && env.nodes[bi]._wy === 0);
  ok('nodes away from the origin do move', env.nodes.some((n, i) => i !== bi && Math.abs(n._wx) > 0.01));
}

// ---- 6. amplitude is clamped, and junk is ignored ------------------------
console.log('the driver cannot push junk in');
{
  const env = makeEnv(false);
  env.VoiceWave.speak(NaN);
  ok('NaN starts nothing', env.pending() === 0);
  env.VoiceWave.speak('loud');
  ok('a non-number starts nothing', env.pending() === 0);
  env.VoiceWave.speak(50);
  for (let i = 0; i < 40; i++) { env.frame(); env.VoiceWave.speak(50); }
  const peak = Math.max(...env.nodes.map(n => Math.hypot(n._wx || 0, n._wy || 0)));
  ok('an out-of-range sample is clamped to the declared peak', peak <= 14 + 1e-9, 'peak=' + peak);
}

// ---- 7. a hidden tab is not animated ------------------------------------
console.log('a hidden tab is not animated');
{
  const env = makeEnv(false);
  env.VoiceWave.speak(0.9);
  for (let i = 0; i < 20; i++) { env.frame(); env.VoiceWave.speak(0.9); }
  const before = env.nodes.map(n => n._wx);
  env.ctx.document.hidden = true;
  for (let i = 0; i < 10; i++) { env.frame(); env.VoiceWave.speak(0.9); }
  ok('offsets stop changing while hidden', env.nodes.every((n, i) => n._wx === before[i]));
  ok('the loop is still alive so it can settle on return', env.pending() > 0);
}

console.log(FAIL === 0 ? '\nALL PASS' : '\n' + FAIL + ' FAILING');
process.exit(FAIL === 0 ? 0 : 1);
