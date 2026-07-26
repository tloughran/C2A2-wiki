'use strict';

/**
 * Tier-1 SHELL test for the CCL command surface (voice_guide_redesign.md sections 5, 8, 9).
 *
 * WHY THIS EXISTS (and why it is not scripts/test_voice_ccl.cjs):
 *   test_voice_ccl.cjs proves the PURE engine -- parse/plan/journal -- with no DOM.
 *   Everything that can actually lie to a user lives in the other half: the shell
 *   wiring inline in wiki/explorer.html (activeManifest/knobBind/readKnob/writeKnob/
 *   execKnob) driving a REAL tab's REAL controls inside the iframe. That half was
 *   only ever verified by a human typing commands into a browser, which does not
 *   scale to a 12-tab fan-out and is what blocked increment 4 step 2.
 *
 *   The contract under test is write-returns-the-read: after any command, what the
 *   bar SAYS must equal what the tab's DOM actually IS. A test that only asserted
 *   the spoken string would pass even if the write silently no-opped; a test that
 *   only asserted the DOM would pass even if the guide narrated a different value.
 *   Every row therefore asserts BOTH, and the metabolism interlock row (view leaves
 *   wave -> the tab resets a yield metric to events, entirely the tab's own code)
 *   is the row that can only pass if the read-back is real.
 *
 * COST: zero. It drives window.CCLRun, the same entry point the voice guide's
 * run_command uses -- but never touches the voice pill, so no realtime session is
 * ever minted. Runs fully headless.
 *
 * DEPS: none. Chrome is driven over CDP through Node's built-in global WebSocket
 * (Node >= 22). C2A2-dev has no package.json and this must not add one.
 *
 * Run:
 *   node scripts/test_voice_shell.cjs [--port 8083] [--shots DIR] [--headful]
 * Exits non-zero on any failed row, any page exception, or any console error.
 */

const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');
const os = require('os');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

const argv = process.argv.slice(2);
function arg(name, dflt) {
  const i = argv.indexOf('--' + name);
  return i === -1 ? dflt : argv[i + 1];
}
const PORT = parseInt(arg('port', '8083'), 10);
const CDP_PORT = parseInt(arg('cdp', '9333'), 10);
const SHOTS = arg('shots', path.join(os.tmpdir(), 'ccl-shots'));
const HEADFUL = argv.indexOf('--headful') !== -1;

const SOCIOGRAM_SRC = 'wiki_narration.html';
const METABOLISM_SRC = 'metabolism/metabolism_view.html';

// ---------------------------------------------------------------- tiny CDP ---

function getJson(url) {
  return new Promise(function (resolve, reject) {
    http.get(url, function (res) {
      let body = '';
      res.on('data', function (d) { body += d; });
      res.on('end', function () {
        try { resolve(JSON.parse(body)); } catch (e) { reject(e); }
      });
    }).on('error', reject);
  });
}

function sleep(ms) { return new Promise(function (r) { setTimeout(r, ms); }); }

async function poll(fn, timeoutMs, intervalMs, what) {
  const deadline = Date.now() + timeoutMs;
  let last = null;
  while (Date.now() < deadline) {
    try {
      const v = await fn();
      if (v) { return v; }
      last = v;
    } catch (e) { last = e.message; }
    await sleep(intervalMs || 200);
  }
  throw new Error('timed out waiting for ' + what + (last ? ' (last: ' + JSON.stringify(last) + ')' : ''));
}

class CDP {
  constructor(ws) {
    this.ws = ws;
    this.id = 0;
    this.pending = new Map();
    this.listeners = [];
    const self = this;
    ws.addEventListener('message', function (ev) {
      const msg = JSON.parse(ev.data);
      if (msg.id && self.pending.has(msg.id)) {
        const p = self.pending.get(msg.id);
        self.pending.delete(msg.id);
        if (msg.error) { p.reject(new Error(msg.method + ': ' + msg.error.message)); }
        else { p.resolve(msg.result); }
      } else if (msg.method) {
        self.listeners.forEach(function (fn) { fn(msg); });
      }
    });
  }
  static async connect(url) {
    const ws = new WebSocket(url);
    await new Promise(function (resolve, reject) {
      ws.addEventListener('open', resolve, { once: true });
      ws.addEventListener('error', function () { reject(new Error('CDP websocket failed: ' + url)); }, { once: true });
    });
    return new CDP(ws);
  }
  on(fn) { this.listeners.push(fn); }
  send(method, params, sessionId) {
    const id = ++this.id;
    const self = this;
    const payload = { id: id, method: method, params: params || {} };
    if (sessionId) { payload.sessionId = sessionId; }
    return new Promise(function (resolve, reject) {
      self.pending.set(id, { resolve: resolve, reject: reject });
      self.ws.send(JSON.stringify(payload));
      setTimeout(function () {
        if (self.pending.has(id)) { self.pending.delete(id); reject(new Error('CDP timeout: ' + method)); }
      }, 180000);
    });
  }
}

// --------------------------------------------------------------- processes ---

const children = [];
function cleanup() {
  children.forEach(function (c) { try { c.kill('SIGTERM'); } catch (e) { /* already gone */ } });
}
process.on('exit', cleanup);
process.on('SIGINT', function () { cleanup(); process.exit(130); });

async function startServer() {
  const p = spawn('python3', [path.join(ROOT, 'scripts/serve_wiki.py'), '--port', String(PORT)], {
    cwd: ROOT, stdio: ['ignore', 'pipe', 'pipe']
  });
  children.push(p);
  const log = [];
  p.stdout.on('data', function (d) { log.push(String(d)); });
  p.stderr.on('data', function (d) { log.push(String(d)); });
  try {
    await poll(function () {
      return new Promise(function (resolve) {
        http.get('http://127.0.0.1:' + PORT + '/explorer.html', function (res) {
          res.resume();
          resolve(res.statusCode === 200);
        }).on('error', function () { resolve(false); });
      });
    }, 15000, 250, 'serve_wiki.py on :' + PORT);
  } catch (e) {
    // Most common cause is a stale server from an aborted run still holding the
    // port; python's traceback says so exactly, so surface it rather than a
    // bare timeout. Re-run with --port <n> or kill the stray.
    throw new Error(e.message + (log.length ? '\n  server said: ' + log.join('').trim() : ''));
  }
  return p;
}

async function startChrome() {
  const userDir = fs.mkdtempSync(path.join(os.tmpdir(), 'ccl-chrome-'));
  const flags = [
    '--remote-debugging-port=' + CDP_PORT,
    '--user-data-dir=' + userDir,
    '--no-first-run', '--no-default-browser-check', '--disable-extensions',
    '--disable-background-networking', '--disable-sync', '--mute-audio',
    '--window-size=1600,1000', '--hide-scrollbars',
    // The Sociogram is a 45MB single file with a 4k-node force sim.
    '--js-flags=--max-old-space-size=4096',
    'about:blank'
  ];
  if (!HEADFUL) { flags.unshift('--headless=new'); }
  const p = spawn(CHROME, flags, { stdio: ['ignore', 'ignore', 'pipe'] });
  children.push(p);
  const ver = await poll(function () {
    return getJson('http://127.0.0.1:' + CDP_PORT + '/json/version').catch(function () { return null; });
  }, 20000, 250, 'Chrome DevTools endpoint');
  return { proc: p, wsUrl: ver.webSocketDebuggerUrl, userDir: userDir };
}

// ------------------------------------------------------------- page driver ---

class Page {
  constructor(cdp, sessionId) {
    this.cdp = cdp;
    this.sid = sessionId;
    this.consoleErrors = [];
    this.exceptions = [];
    const self = this;
    cdp.on(function (msg) {
      if (msg.sessionId !== self.sid) { return; }
      if (msg.method === 'Runtime.consoleAPICalled' && msg.params.type === 'error') {
        self.consoleErrors.push(msg.params.args.map(function (a) {
          return a.value !== undefined ? String(a.value) : (a.description || a.type);
        }).join(' '));
      } else if (msg.method === 'Runtime.exceptionThrown') {
        const d = msg.params.exceptionDetails;
        self.exceptions.push((d.exception && d.exception.description) || d.text);
      } else if (msg.method === 'Log.entryAdded' && msg.params.entry.level === 'error') {
        const en = msg.params.entry;
        // Headless Chrome always requests /favicon.ico and the wiki ships none.
        // That 404 is the browser's, not the page's -- ignoring it keeps the
        // gate meaningful instead of permanently red for a non-defect.
        if (/\/favicon\.ico$/.test(en.url || '')) { return; }
        self.consoleErrors.push('[' + en.source + '] ' + en.text + (en.url ? '  <- ' + en.url : ''));
      }
    });
  }
  static async open(cdp) {
    const t = await cdp.send('Target.createTarget', { url: 'about:blank' });
    const a = await cdp.send('Target.attachToTarget', { targetId: t.targetId, flatten: true });
    const page = new Page(cdp, a.sessionId);
    await page.cdp.send('Page.enable', {}, page.sid);
    await page.cdp.send('Runtime.enable', {}, page.sid);
    await page.cdp.send('Log.enable', {}, page.sid);
    return page;
  }
  async navigate(url) {
    const cdp = this.cdp, sid = this.sid;
    const done = new Promise(function (resolve) {
      cdp.on(function (msg) {
        if (msg.sessionId === sid && msg.method === 'Page.loadEventFired') { resolve(true); }
      });
    });
    await cdp.send('Page.navigate', { url: url }, sid);
    await done;
  }
  async eval(expr) {
    const r = await this.cdp.send('Runtime.evaluate', {
      expression: '(function(){ ' + expr + ' })()',
      returnByValue: true, awaitPromise: true
    }, this.sid);
    if (r.exceptionDetails) {
      const d = r.exceptionDetails;
      throw new Error('eval threw: ' + ((d.exception && d.exception.description) || d.text));
    }
    return r.result.value;
  }
  async screenshot(file) {
    const r = await this.cdp.send('Page.captureScreenshot', { format: 'png' }, this.sid);
    fs.mkdirSync(path.dirname(file), { recursive: true });
    fs.writeFileSync(file, Buffer.from(r.data, 'base64'));
    return file;
  }
}

// ------------------------------------------------------- shell interactions ---

// Everything below reaches the iframe from the top frame. Same-origin over http,
// so contentDocument is readable -- this is the same access path the shell's own
// ifWin()/ifDoc() use, deliberately: if the harness can't reach it, neither can CCL.

const IFRAME_DOC = "var f=document.getElementById('content-frame'); var d=f&&f.contentDocument; var w=f&&f.contentWindow;";

function activateTab(page, src) {
  return page.eval(
    "var bs=[].slice.call(document.querySelectorAll('.tab-btn[data-src]'));" +
    "var b=bs.filter(function(x){return x.getAttribute('data-src')===" + JSON.stringify(src) + ";})[0];" +
    "if(!b){return 'no such tab button: ' + " + JSON.stringify(src) + ";}" +
    "if(b.classList.contains('active')){return 'already-active';}" +
    "b.click(); return 'clicked';"
  );
}

function tabReady(page, kind) {
  const probe = kind === 'metabolism'
    ? "return !!(d && d.querySelector('#view') && d.querySelector('#metric') && d.querySelector('#logy'));"
    : "return !!(w && w.groupVisibility && typeof w.rebuildGraph==='function' && d && d.getElementById('search-input'));";
  return poll(function () {
    return page.eval(IFRAME_DOC + "if(!d||d.readyState!=='complete'){return false;} " + probe);
  }, 180000, 500, kind + ' tab ready');
}

function cclReady(page) {
  return poll(function () {
    return page.eval("var el=document.getElementById('ccl-result'); return !!(el && /^CCL ready \\(/.test(el.textContent));");
  }, 60000, 250, 'CCL bar loaded');
}

// Run one command through the SAME entry point voice uses, and return both what
// the bar said and what the bar's own return value claimed. Divergence between
// them would itself be a bug, so we capture both rather than trusting one.
function runCmd(page, cmd) {
  return page.eval(
    "var r = window.CCLRun(" + JSON.stringify(cmd) + ");" +
    "var el = document.getElementById('ccl-result');" +
    "return { spoken: (r && r.spoken) || null, ok: !!(r && r.ok), shown: (r && typeof r.shown === 'number') ? r.shown : null," +
    // inView is the CAMERA count -- the only field a claim about visibility may
    // rest on. Carried separately from `shown` precisely because they disagree.
    "         inView: (r && typeof r.inView === 'number') ? r.inView : null," +
    "         total: (r && typeof r.total === 'number') ? r.total : null, bar: el ? el.textContent : null, cls: el ? el.className : null };"
  );
}

function readDom(page, sel, prop) {
  return page.eval(
    IFRAME_DOC +
    "var e = d && d.querySelector(" + JSON.stringify(sel) + ");" +
    "if(!e){return '(no element ' + " + JSON.stringify(sel) + " + ')';}" +
    "return " + (prop === 'checked' ? "(e.checked ? 'on' : 'off')" : "e.value") + ";"
  );
}

// Which manifest the shell's resolver picked for the CURRENTLY active tab.
// Asserted per phase because a resolver that silently returns the wrong (or the
// first) manifest makes every downstream row fail for the wrong reason -- exactly
// the aka[i] === key bug this harness found on its first run.
async function assertManifest(page, expectedTab, expectedSrc) {
  let d;
  try { d = await page.eval('return window.CCLDebug ? window.CCLDebug() : null;'); }
  catch (e) { return record('resolver -> ' + expectedTab, false, 'CCLDebug threw: ' + e.message); }
  if (!d) { return record('resolver -> ' + expectedTab, false, 'window.CCLDebug missing'); }
  const problems = [];
  if (d.src !== expectedSrc) { problems.push('activeSrc=' + JSON.stringify(d.src)); }
  if (d.tab !== expectedTab) { problems.push('resolved manifest=' + JSON.stringify(d.tab) + ' expected ' + JSON.stringify(expectedTab)); }
  record('resolver -> ' + expectedTab, problems.length === 0, problems.join(' | ') || ('caps=' + (d.caps || []).length + ' knobs=' + JSON.stringify(d.knobs)));
}

// What the graph SHOWS, read off its own status line. Asserting this instead of
// (only) the filter state is the difference between "the command ran" and "the
// user can see what they asked for" -- the gap that let `only architecture`
// report success over an empty graph.
function nodesShown(page) {
  return page.eval(
    IFRAME_DOC +
    "var el = d && d.getElementById('graph-status');" +
    "if (!el) { return null; }" +
    "var m = /([0-9,]+)\\s*\\/\\s*([0-9,]+)\\s+nodes/.exec(el.textContent || '');" +
    "return m ? parseInt(m[1].replace(/,/g, ''), 10) : null;"
  );
}


// IN VIEW is the camera's number -- how many of the shown nodes are actually on
// screen. Nothing ever asserted it, which is how a reveal could leave every
// matching node off-screen and still pass. Framing animates, so reads are taken
// until two agree.
function inViewCount(page) {
  return page.eval(
    IFRAME_DOC +
    "var el = d && d.getElementById('graph-status');" +
    "if (!el) { return null; }" +
    "var m = /([0-9,]+)\\s+in view/.exec(el.textContent || '');" +
    "return m ? parseInt(m[1].replace(/,/g, ''), 10) : null;"
  );
}
async function settledInView(page) {
  // Framing animates (400ms) and then re-frames once the force sim settles
  // (~900ms), so an early "two reads agree" can latch onto a mid-transition
  // value -- it read 0 while the camera was still travelling through empty
  // space. Wait out both stages before looking for stability.
  await sleep(1600);
  let prev = await inViewCount(page);
  for (let i = 0; i < 20; i++) {
    await sleep(150);
    const now = await inViewCount(page);
    if (now === prev) { return now; }
    prev = now;
  }
  return prev;
}
// Shove the camera far away, so a reveal that does not reframe leaves the user
// staring at empty space -- the exact condition that produced "you said it was
// showing and I could see nothing".
async function derangeCamera(page) {
  // Let any pending settle re-frame from the previous command fire first,
  // otherwise it lands mid-test and undoes the derangement.
  await sleep(1400);
  return page.eval(
    IFRAME_DOC +
    "var svg = d.getElementById('graph-svg');" +
    // Dispatch a real mousedown first: this stands in for the user grabbing the
    // graph, and asserts the contract that a manual camera move cancels any
    // pending settle re-frame instead of being yanked back a moment later.
    "w.d3.select(svg).call(w.zoomBehavior.transform, w.d3.zoomIdentity.translate(-9000, -9000).scale(3));" +
    "return true;"
  );
}


// How much of the graph is actually drawn after a search: the point of cutting
// rather than dimming is that the 113,765 edges STOP BEING DRAWN, not that they
// get fainter. Counting only nodes would pass on a dim.
function drawn(page) {
  return page.eval(
    IFRAME_DOC +
    "if (!d) { return null; }" +
    "var vis = function (sel) { var a = d.querySelectorAll(sel), n = 0;" +
    "  for (var i = 0; i < a.length; i++) { if (!a[i].classList.contains('ccl-cut')) { n++; } } return n; };" +
    "return { nodes: vis('.node-circle'), links: vis('.link-line')," +
    "         nodesTotal: d.querySelectorAll('.node-circle').length, linksTotal: d.querySelectorAll('.link-line').length };"
  );
}

function onGroupCount(page) {
  return page.eval(
    IFRAME_DOC +
    "if(!w||!w.groupVisibility){return -1;}" +
    "var n=0; for(var k in w.groupVisibility){ if(w.groupVisibility[k]){n++;} } return n;"
  );
}


// The section-9 gate. `uncovered` is the loud failure: a control a user can
// operate that voice cannot reach and nobody has declared. `deferred` is the
// honest middle -- in scope, not yet built -- so it is asserted as an EXACT
// count: a newly added control cannot drift into it unnoticed, and a fixed one
// must be removed from the manifest for this to stay green.
async function auditTab(page, tabName, expectDeferred, expectGestureDeferred) {
  let a;
  try { a = await page.eval('return window.CCLAudit ? window.CCLAudit() : null;'); }
  catch (e) { return record('audit ' + tabName, false, 'CCLAudit threw: ' + e.message); }
  if (!a) { return record('audit ' + tabName, false, 'window.CCLAudit missing'); }
  if (a.error) { return record('audit ' + tabName, false, a.error); }

  const problems = [];
  if (a.uncovered.length) { problems.push('UNCOVERED (' + a.uncovered.length + '): ' + a.uncovered.slice(0, 12).join(', ')); }
  if (a.staleBinds.length) { problems.push('manifest binds a control the tab no longer has: ' + a.staleBinds.join(', ')); }
  if (a.deferred.length !== expectDeferred) {
    problems.push('deferred=' + a.deferred.length + ' expected ' + expectDeferred + ' -- update manifests.json, do not widen the expectation');
  }
  // Gestures have no element to sweep, so this asserts the DECLARATION: any
  // problem is a lie in the manifest (most importantly a gesture claiming
  // coverage by a verb the tab does not have), and the deferred count is
  // exact so an unreachable modality cannot sit quietly in the list.
  if (a.gestureProblems && a.gestureProblems.length) { problems.push('GESTURES: ' + a.gestureProblems.join(' | ')); }
  // A tab whose content is a nested app hides most of its surface one document
  // down (21 controls in the tab, 2294 in the frame). Asserted as "nothing
  // UNDECLARED" rather than an exact count: the nested overview is a 158x11
  // heatmap of buttons, so a count would go red on every data refresh and the
  // gate would be trained to be ignored.
  let frameNote = '';
  (a.frames || []).forEach(function (f) {
    if (f.error) { problems.push('FRAME ' + f.sel + ': ' + f.error); return; }
    if (f.uncovered.length) {
      problems.push('FRAME ' + f.sel + ' UNCOVERED (' + f.uncovered.length + '): ' + f.uncovered.slice(0, 10).join(', '));
    }
    frameNote += '  ||  frame ' + f.sel + ': ' + f.total + ' controls, ' + f.covered + ' covered, ' +
                 f.excluded + ' excluded, ' + f.deferred + ' deferred, ' + f.uncovered.length + ' uncovered';
  });
  const gd = (a.gestures && a.gestures.deferred) || 0;
  if (expectGestureDeferred !== undefined && gd !== expectGestureDeferred) {
    problems.push('gestures deferred=' + gd + ' expected ' + expectGestureDeferred);
  }
  record('audit ' + tabName, problems.length === 0,
    problems.join(' | ') || (a.total + ' controls: ' + a.covered + ' covered, ' + a.excluded + ' excluded, ' +
      a.deferred.length + ' deferred, 0 uncovered  ||  gestures: ' + JSON.stringify(a.gestures) + frameNote));
}

// ------------------------------------------------------------------- rows ----

// Each row: what we send, what the bar must say, and what the tab's DOM must be.
// `dom` is checked AFTER the command, so a spoken claim with no DOM change fails.
const results = [];
function record(name, ok, detail) {
  results.push({ name: name, ok: ok, detail: detail });
  process.stdout.write((ok ? '  PASS  ' : '  FAIL  ') + name + (detail ? '   -- ' + detail : '') + '\n');
}

async function row(page, name, cmd, expect) {
  let r;
  try { r = await runCmd(page, cmd); }
  catch (e) { return record(name, false, 'command threw: ' + e.message); }

  const problems = [];
  if (expect.spoken && !expect.spoken.test(r.spoken || '')) {
    problems.push('spoken ' + JSON.stringify(r.spoken) + ' !~ ' + expect.spoken);
  }
  if (expect.ok !== undefined && r.ok !== expect.ok) {
    problems.push('ok=' + r.ok + ' expected ' + expect.ok);
  }
  if (r.bar !== null && r.spoken !== null && r.bar !== r.spoken) {
    problems.push('bar text diverges from returned spoken: ' + JSON.stringify(r.bar));
  }
  for (const [sel, spec] of Object.entries(expect.dom || {})) {
    const got = await readDom(page, sel, spec.prop);
    if (got !== spec.value) {
      problems.push(sel + (spec.prop ? '.' + spec.prop : '.value') + '=' + JSON.stringify(got) + ' expected ' + JSON.stringify(spec.value));
    }
  }
  if (expect.groups !== undefined) {
    const n = await onGroupCount(page);
    if (!expect.groups(n)) { problems.push('groups-on=' + n + ' failed its check'); }
  }
  // The number the VOICE tool will forward. Asserting the prose alone would let
  // the spoken layer diverge from the render again.
  if (expect.shown !== undefined && !expect.shown(r.shown)) {
    problems.push('result.shown=' + r.shown + ' (the value the voice tool forwards) failed its check');
  }
  if (expect.inView !== undefined) {
    const iv = await settledInView(page);
    if (!expect.inView(iv)) { problems.push('ON SCREEN nodes-in-view=' + iv + ' failed its check'); }
  }
  if (expect.view !== undefined) {
    const v = await nodesShown(page);
    if (!expect.view(v)) { problems.push('RENDERED nodes-shown=' + v + ' failed its check'); }
  }
  record(name, problems.length === 0, problems.join(' | ') || (r.spoken || ''));
}

// The other half of a No-Blind-Push: the page can be perfect in this headless
// run (fresh profile, empty cache) and still ship a stale asset to a browser
// that has the old c2a2-commandline.js cached. Only a content hash catches
// that, so the gate runs here rather than living in a human's memory.
function stampGate() {
  return new Promise(function (resolve) {
    const p = spawn('python3', [path.join(ROOT, 'wiki/heartbeat/backend/stamp_assets.py'), '--target', 'all', '--check'],
      { cwd: ROOT, stdio: ['ignore', 'pipe', 'pipe'] });
    let out = '';
    p.stdout.on('data', function (d) { out += d; });
    p.stderr.on('data', function (d) { out += d; });
    p.on('close', function (code) {
      const stale = out.split('\n').filter(function (l) { return /STALE|ERROR/.test(l); }).join(' | ');
      record('asset stamps current (pre-push gate)', code === 0, stale || 'heartbeat + explorer includes match their content hashes');
      resolve();
    });
  });
}

// ------------------------------------------------------------------- main ----

async function main() {
  process.stdout.write('CCL shell test -- headless Chrome, no realtime session, no npm deps\n\n');

  await startServer();
  const chrome = await startChrome();
  const cdp = await CDP.connect(chrome.wsUrl);
  const page = await Page.open(cdp);

  await page.navigate('http://127.0.0.1:' + PORT + '/explorer.html');
  await cclReady(page);
  await tabReady(page, 'sociogram');   // boot tab; 45MB, give it room

  // ---- Phase A: Sociogram regression (the verified baseline must not move) ----
  process.stdout.write('\nPhase A -- Sociogram regression (inc 1/2 baseline)\n');
  await assertManifest(page, 'sociogram', SOCIOGRAM_SRC);
  await auditTab(page, 'sociogram', 6, 1);
  const bootGroups = await onGroupCount(page);
  await row(page, 'A1 only levin friston -> 2 groups, shown, AND on screen', 'only levin friston',
    { ok: true, spoken: /-> 2 groups on/, groups: function (n) { return n === 2; },
      view: function (v) { return v > 0; }, inView: function (v) { return v === 4; } });
  // The invariant, tested where it actually broke: move the camera into empty
  // space first. Without auto-framing this row reads 0 nodes on screen while
  // every other assertion in the suite still passes.
  // The 2026-07-25 regression: 'architecture' is both a group and a section
  // parent. Asserting the RENDER is the whole point -- the old code passed a
  // groups-on assertion while showing an empty graph.
  await row(page, 'A2 undo -> boot filter set restored', 'undo',
    { ok: true, spoken: /undid \(filters\)/, groups: function (n) { return n === bootGroups; } });
  // The invariant, tested where it actually broke: shove the camera into empty
  // space first. Without auto-framing this row reads 0 nodes on screen while
  // every other assertion in the suite still passes.
  await derangeCamera(page);
  const stranded = await settledInView(page);
  record('A2a precondition: the camera really was stranded', stranded === 0, 'in-view before the reveal was ' + stranded);
  // THE EMPTY SCREEN, SAID OUT LOUD. With the camera stranded, every number the
  // guide used to report was true and the user could still see nothing: `shown`
  // is a filter result and knows nothing about where the camera points, so the
  // guide "had no idea where the middle of my screen is" and called things
  // visible that were not (Tom, 2026-07-26). `shown` must NOT move -- the filter
  // really did pass 4 -- while the visibility claim flips.
  const strandedWhat = await runCmd(page, 'what');
  // Asserting the RELATIONSHIP, not two literals: whatever the filter passed, it
  // stays passed while the camera is elsewhere, and only the visibility claim
  // flips. A hardcoded pair would break every time an earlier row's filter state
  // changed, and would say nothing about the thing that was actually wrong.
  record('A2b what admits the screen is empty while the filter count stays honest',
    /NONE of them are on screen/.test(strandedWhat.spoken || '') &&
    strandedWhat.inView === 0 && strandedWhat.shown > 0,
    strandedWhat.spoken.slice(0, 90) + ' ...  [inView=' + strandedWhat.inView + ' shown=' + strandedWhat.shown + ']');
  await row(page, 'A2a a reveal reframes a camera left in empty space', 'only levin friston',
    { ok: true, spoken: /centred/, inView: function (v) { return v === 4; } });
  await row(page, 'A2a2 undo again, back to boot', 'undo',
    { ok: true, groups: function (n) { return n === bootGroups; } });
  // The other half of the contract: a camera the USER moved must stay moved.
  // A settle re-frame that lands after a manual zoom reads as the view having
  // a mind of its own.
  await row(page, 'A2a3 reveal, then the user zooms', 'only levin friston', { ok: true });
  const afterWheel = await page.eval(
    IFRAME_DOC +
    "var svg = d.getElementById('graph-svg');" +
    "svg.dispatchEvent(new WheelEvent('wheel', { deltaY: -240, bubbles: true, clientX: 400, clientY: 300 }));" +
    "return (d.querySelector('#graph-svg g') || {}).getAttribute ? d.querySelector('#graph-svg g').getAttribute('transform') : null;"
  );
  await sleep(1600);
  const afterSettle = await page.eval(
    IFRAME_DOC + "var g = d.querySelector('#graph-svg g'); return g ? g.getAttribute('transform') : null;"
  );
  record('A2a3 a user zoom is not undone by the settle re-frame',
    afterWheel !== null && afterWheel === afterSettle,
    afterWheel === afterSettle ? 'camera held at the user position' : ('camera moved: ' + afterWheel + ' -> ' + afterSettle));
  // The 2026-07-25 regression: 'architecture' is BOTH a group and a section
  // parent. These rows assert the RENDER, which is the whole point -- the old
  // code passed a groups-on assertion while showing an empty graph.
  await row(page, 'A2b only architecture -> parent group kept, nodes actually shown', 'only architecture',
    { ok: true, spoken: /groups on: architecture, architecture\/changelog/, groups: function (n) { return n === 2; },
      view: function (v) { return v > 0; }, shown: function (n) { return n > 0; } });
  await row(page, 'A2c what -> the spoken answer carries the rendered count', 'what',
    { ok: true, spoken: /nodes shown/ });
  await row(page, 'A2d none -> an honest zero, stated plainly', 'none',
    { ok: true, spoken: /0 of \d+ nodes shown/, view: function (v) { return v === 0; }, shown: function (n) { return n === 0; } });
  await row(page, 'A2e all -> the whole graph is back', 'all',
    { ok: true, view: function (v) { return v > 4000; } });
  // `fit` is the deliberate escape hatch from the legibility floor: it means
  // "show everything, however small", so it must NOT be floored.
  await row(page, 'A3 fit -> unfloored, the whole graph on screen', 'fit',
    { ok: true, spoken: /^fit$/, inView: function (v) { return v > 3900; } });
  await row(page, 'A4 what -> names the live view', 'what', { ok: true, spoken: /view: Sociogram/ });
  // ---- find/focus must CUT, not dim (interim shell-side implementation) ----
  await row(page, 'A5 find levin -> a cut, not a haystack', 'find levin', { ok: true, spoken: /\d+ nodes shown/ });
  // Measured AFTER the settle window on purpose: the first implementation
  // passed an immediate count and then let the haze re-render behind it.
  await settledInView(page);
  await sleep(600);
  const afterFind = await drawn(page);
  record('A5a find hides the non-matching nodes',
    afterFind.nodes > 0 && afterFind.nodes < afterFind.nodesTotal * 0.5,
    afterFind.nodes + ' of ' + afterFind.nodesTotal + ' nodes still drawn');
  record('A5b find stops DRAWING the non-matching edges',
    afterFind.links < Math.max(1, afterFind.linksTotal * 0.2),
    afterFind.links + ' of ' + afterFind.linksTotal + ' edges still drawn');
  const shotFind = await page.screenshot(path.join(SHOTS, 'A-find-cut.png'));
  await row(page, 'A5c what -> reports the cut as part of the view', 'what', { ok: true, spoken: /cut to \d+ nodes matching "levin"/ });
  await row(page, 'A5d find friston -> a different cut', 'find friston', { ok: true, spoken: /\d+ nodes shown/ });
  await row(page, 'A5e undo -> the PREVIOUS cut comes back, query and all', 'undo',
    { ok: true, spoken: /undid \(cut\)/ });
  await row(page, 'A5f what -> confirms the earlier cut was restored exactly', 'what',
    { ok: true, spoken: /cut to \d+ nodes matching "levin"/ });
  await row(page, 'A6 clear -> everything restored, nothing left hidden', 'clear', { ok: true });
  const afterClear = await drawn(page);
  record('A6a clear leaves no cut elements behind',
    afterClear.nodes === afterClear.nodesTotal && afterClear.links === afterClear.linksTotal,
    afterClear.nodes + '/' + afterClear.nodesTotal + ' nodes, ' + afterClear.links + '/' + afterClear.linksTotal + ' edges drawn');

  // ---- cursor + read: exploring with no mouse and no screen ---------------
  await row(page, 'A19 only levin friston (a small revealed set to walk)', 'only levin friston', { ok: true });
  await row(page, 'A20 pick first -> names what it landed on and where', 'pick first',
    { ok: true, spoken: /\|\s*1 of 4 nodes/ });
  const picked1 = await page.eval(IFRAME_DOC + "return (w.currentRightNode || {}).label || null;");
  record('A20a pick actually opens that node', !!picked1, 'right panel holds: ' + picked1);
  await row(page, 'A21 next -> moves one along', 'next', { ok: true, spoken: /\|\s*2 of 4 nodes/ });
  const picked2 = await page.eval(IFRAME_DOC + "return (w.currentRightNode || {}).label || null;");
  record('A21a next lands on a DIFFERENT node', picked1 !== picked2, picked1 + ' -> ' + picked2);
  await row(page, 'A22 previous -> and back', 'previous', { ok: true, spoken: /\|\s*1 of 4 nodes/ });
  await row(page, 'A23 pick random -> stays inside the revealed set', 'pick random',
    { ok: true, spoken: /of 4 nodes/ });
  // read: the PAGE speaks. Assert it took the article text, not that audio came
  // out -- headless Chrome has no speech engine, so the claim under test is that
  // the right text was handed to the right system.
  const readRes = await runCmd(page, 'read');
  record('A24 read takes the open article, by word count', /reading .+\s*\|\s*\d+ words/.test(readRes.spoken || ''), readRes.spoken);
  // REVERSED 2026-07-26 (Tom's call). This row used to demand the words
  // 'say "stop" to interrupt' -- and passed for a month while NOTHING routed a
  // spoken stop to run_command. A test can only hold a promise the build keeps,
  // so it now holds the opposite: name the button, never ask the user to speak
  // at a microphone that is muted.
  record('A24b the offered interrupt is one that WORKS (the button, not a voice command)',
    /Stop reading/.test(readRes.spoken || '') && !/say "stop"/i.test(readRes.spoken || ''), readRes.spoken);
  record('A24d the reader waits for a live guide rather than talking over it',
    await page.eval("return typeof window.CCLDeferSpeak === 'function' || !document.getElementById('vg-launch');"),
    'CCLDeferSpeak hook present (or no voice UI on this build)');
  // Was "a visible Stop appears while reading". That passed only because nothing
  // tore the reader down when speech FAILED -- so headless, where there is no
  // speech engine at all, the button sat there offering to stop a read that was
  // never happening. The utterance's onerror now ends the read properly, which
  // means visibility is no longer observable in this environment. What is still
  // checkable, and is what actually matters, is that the control and its help
  // exist and are wired to something.
  record('A24c the Stop control and its instructions exist and are wired',
    await page.eval(
      "var s=document.getElementById('ccl-stop'), h=document.getElementById('ccl-readhelp');" +
      "return !!s && !!h && typeof window.showReaderHelp === 'function';"),
    'ccl-stop + ccl-readhelp present, showReaderHelp defined');
  // The speech script is a pure text transformation over the real article DOM,
  // so it IS testable headlessly -- unlike the voice itself.
  const script = await page.eval(
    IFRAME_DOC +
    "var el = d.getElementById('right-page-content');" +
    "var raw = (el.textContent || '').replace(/\\s+/g, ' ').trim();" +
    "return { raw: raw.slice(0, 160), childCount: el.children.length };"
  );
  record('A24e the raw DOM text really does run blocks together (the bug being fixed)',
    /TripletsMaintained|[a-z][A-Z]/.test(script.raw), script.raw.slice(0, 90) + '...');
  const spoken24 = readRes.spoken || '';
  record('A24f the reader holds provenance back and says so',
    /metadata held back/.test(spoken24), spoken24);
  await row(page, 'A24g read details -> the held-back provenance, on request only', 'read details',
    { ok: true, spoken: /\(metadata\)/ });
  await row(page, 'A25 stop -> interruptible', 'stop', { ok: true, spoken: /^stopped$/ });
  record('A25a the Stop control goes away again',
    await page.eval("var b=document.getElementById('ccl-stop'); return !!b && b.style.display === 'none';"),
    'ccl-stop hidden after stop');
  await row(page, 'A26 close, then read -> honest refusal, not silence', 'close', { ok: true });
  await row(page, 'A27 read with nothing open says so', 'read',
    { ok: false, spoken: /nothing is open to read/ });
  await row(page, 'A28 none, then pick -> nothing revealed to pick from', 'none', { ok: true });
  await row(page, 'A29 pick random over an empty reveal', 'pick random',
    { ok: false, spoken: /nothing is revealed/ });
  await row(page, 'A30 all (restore)', 'all', { ok: true });

  // ---- second filter families: the edges Tom could not remove --------------
  const edgesOf = function (page) {
    return page.eval(IFRAME_DOC + "var el = d && d.getElementById('edge-status');" +
      "if (!el) { return null; }" +
      "var m = /([0-9,]+)\\s+pass/.exec(el.textContent || '');" +
      "return m ? parseInt(m[1].replace(/,/g, ''), 10) : null;");
  };
  const edgesBefore = await edgesOf(page);
  await row(page, 'A12 hide edges mention -> a family the filters dim cannot name', 'hide edges mention',
    { ok: true, spoken: /edges: wikilink, reference/ });
  await sleep(400);
  const edgesAfter = await edgesOf(page);
  record('A12a hiding an edge type actually removes edges',
    edgesAfter !== null && edgesAfter < edgesBefore, edgesBefore + ' -> ' + edgesAfter + ' edges passing');
  await row(page, 'A13 none edges -> every edge gone', 'none edges', { ok: true, spoken: /edges: none/ });
  await sleep(400);
  const edgesNone = await edgesOf(page);
  record('A13a none edges leaves no edges drawn', edgesNone === 0, edgesNone + ' edges drawn');
  await row(page, 'A14 undo -> the edge family comes back', 'undo', { ok: true, spoken: /undid \(family:edges\)/ });
  await sleep(400);
  const edgesUndone = await edgesOf(page);
  record('A14a undo restores the edge family', edgesUndone > 0, edgesNone + ' -> ' + edgesUndone + ' edges drawn');
  await row(page, 'A15 all edges -> back to every type', 'all edges', { ok: true, spoken: /wikilink, mention, reference/ });
  record('A15a the tab checkboxes agree with the graph',
    await page.eval(IFRAME_DOC + "return !!(d.getElementById('chk-edge-mention') || {}).checked;"),
    'chk-edge-mention reflects the voice command');
  await row(page, 'A16 hide edges banana -> names the allowed members', 'hide edges banana',
    { ok: false, spoken: /wikilink.*mention.*reference/ });
  await row(page, 'A17 hide bridges same -> the fourth edge sub-family', 'hide bridges same',
    { ok: true, spoken: /bridges: cross/ });
  await row(page, 'A18 all bridges', 'all bridges', { ok: true, spoken: /bridges: cross, same/ });

  // ---- camera verbs: zoom in/out and pan, the gestures that had no verb ----
  const camBefore = await page.eval(IFRAME_DOC + "return { k: w.currentZoomScale };");
  await row(page, 'A7 zoom in -> the graph actually magnifies', 'zoom in', { ok: true, spoken: /^zoom in/ });
  await sleep(600);
  const camIn = await page.eval(IFRAME_DOC + "return { k: w.currentZoomScale };");
  record('A7a zoom in raises the scale', camIn.k > camBefore.k, camBefore.k.toFixed(2) + ' -> ' + camIn.k.toFixed(2));
  await row(page, 'A8 zoom out -> and back down', 'zoom out', { ok: true, spoken: /^zoom out/ });
  await sleep(600);
  const camOut = await page.eval(IFRAME_DOC + "return { k: w.currentZoomScale };");
  record('A8a zoom out lowers it again (symmetric)', camOut.k < camIn.k, camIn.k.toFixed(2) + ' -> ' + camOut.k.toFixed(2));

  const panBefore = await page.eval(IFRAME_DOC + "var g = d.querySelector('#graph-svg g'); return g.getAttribute('transform');");
  await row(page, 'A9 pan left -> the view moves', 'pan left', { ok: true, spoken: /^pan left/ });
  await sleep(600);
  const panAfter = await page.eval(IFRAME_DOC + "var g = d.querySelector('#graph-svg g'); return g.getAttribute('transform');");
  record('A9a pan left moves the camera', panBefore !== panAfter, panBefore + ' -> ' + panAfter);
  await row(page, 'A10 pan right -> back the other way (symmetric)', 'pan right', { ok: true, spoken: /^pan right/ });
  await sleep(600);
  const panBack = await page.eval(IFRAME_DOC + "var g = d.querySelector('#graph-svg g'); return g.getAttribute('transform');");
  // Compared with tolerance, not by string: transforms carry float noise and a
  // transition can still be easing when the read lands. The claim under test is
  // that the pair is symmetric, not that it is bit-identical.
  const xy = function (t) { const m = /translate\(([-\d.]+),\s*([-\d.]+)\)/.exec(t || ''); return m ? [parseFloat(m[1]), parseFloat(m[2])] : null; };
  const a = xy(panBefore), b = xy(panBack);
  record('A10a pan right returns the camera to where it started',
    !!a && !!b && Math.abs(a[0] - b[0]) < 8 && Math.abs(a[1] - b[1]) < 8,
    'left then right: ' + (a && b ? 'dx=' + (b[0] - a[0]).toFixed(1) + ' dy=' + (b[1] - a[1]).toFixed(1) : 'unparsed'));
  await row(page, 'A11 pan sideways -> refused by the grammar, not guessed', 'pan sideways', { ok: false });

  const shotA = await page.screenshot(path.join(SHOTS, 'A-sociogram.png'));

  // ---- Phase B: metabolism, the first knob tab (inc 4 step 2, unreviewed) ----
  process.stdout.write('\nPhase B -- metabolism knobs (inc 4 step 2)\n');
  await activateTab(page, METABOLISM_SRC);
  await tabReady(page, 'metabolism');
  await assertManifest(page, 'metabolism', METABOLISM_SRC);
  await auditTab(page, 'metabolism', 0, 0);

  await row(page, 'B1 set view waveform -> alias resolves to DOM value wave', 'set view waveform',
    { ok: true, spoken: /^set view wave$/, dom: { '#view': { value: 'wave' } } });
  await row(page, 'B2 set metric output -> out', 'set metric output',
    { ok: true, spoken: /^set metric out$/, dom: { '#metric': { value: 'out' } } });
  await row(page, 'B2b set amplitude output -> the LABEL on the control resolves', 'set amplitude output',
    { ok: true, spoken: /^set metric out$/, dom: { '#metric': { value: 'out' } } });
  await row(page, 'B3 set logy on', 'set logy on',
    { ok: true, spoken: /^set logy on$/, dom: { '#logy': { prop: 'checked', value: 'on' } } });
  await row(page, 'B4 set metric yield files (arms the interlock)', 'set metric yield files',
    { ok: true, spoken: /^set metric yield_files$/, dom: { '#metric': { value: 'yield_files' } } });

  // THE row: metabolism's own code drops a yield metric back to events when the
  // view leaves wave. Write-returns-read means the bar must report the value the
  // DOM actually holds, and the metric must visibly have been clamped by the tab.
  await row(page, 'B5 set view raster -> interlock clamps metric (write-returns-read)', 'set view raster',
    { ok: true, spoken: /^set view raster$/, dom: { '#view': { value: 'raster' }, '#metric': { value: 'events' } } });
  const shotB = await page.screenshot(path.join(SHOTS, 'B-metabolism-interlock.png'));

  await row(page, 'B6 undo -> view back to wave', 'undo',
    { ok: true, spoken: /undid \(knob:view\)/, dom: { '#view': { value: 'wave' } } });
  await row(page, 'B7 only levin -> honest unsupported_here, not faked', 'only levin',
    { ok: false, spoken: /Not available on this view/ });
  await row(page, 'B8 set view banana -> names the allowed values', 'set view banana',
    { ok: false, spoken: /raster.*wave.*dual/ });
  await row(page, 'B9 set banana wave -> names the available knobs', 'set banana wave',
    { ok: false, spoken: /view.*metric.*color.*logy/ });
  await row(page, 'B10 reset -> honest unsupported until step 2b', 'reset',
    { ok: false, spoken: /Not available on this view/ });
  const shotB2 = await page.screenshot(path.join(SHOTS, 'B-metabolism-final.png'));

  // ---- Phase C: back to Sociogram, prove the tab-aware path did not regress ---
  process.stdout.write('\nPhase C -- return to Sociogram (tab-aware run() must not leak knob state)\n');
  await activateTab(page, SOCIOGRAM_SRC);
  await tabReady(page, 'sociogram');
  await assertManifest(page, 'sociogram', SOCIOGRAM_SRC);
  await row(page, 'C1 only levin friston still works after a knob tab', 'only levin friston',
    { ok: true, spoken: /-> 2 groups on/, groups: function (n) { return n === 2; } });
  await row(page, 'C2 set view wave -> unsupported on Sociogram', 'set view wave',
    { ok: false, spoken: /Not available on this view/ });
  const shotC = await page.screenshot(path.join(SHOTS, 'C-sociogram-return.png'));

  await stampGate();

  // ---- Phase D: chapter pages and moving around -----------------------------
  //
  // Nothing had ever exercised a CHAPTER page. Two defects lived there: every
  // chapter button was unreachable by name (its two spans concatenate to
  // "CommunityExplorer", with no space, so the resolver's "community explorer"
  // never matched), and an unmapped view fell back to SOCIOGRAM caps -- so a
  // chapter page advertised filtering it cannot do.
  process.stdout.write('\nPhase D -- chapter pages, tab order, honest caps\n');
  await page.eval("var b = document.getElementById('chap-intro'); if (b) { b.click(); } return true;");
  await sleep(2500);
  await row(page, 'D1 go community explorer -> reachable BY NAME from a chapter page', 'go community explorer',
    { ok: true, spoken: /go community explorer/i });
  await sleep(2500);
  await row(page, 'D2 what -> names the view and its position in the row', 'what',
    { ok: true, spoken: /\(\d+ of \d+, left to right\)/ });
  await row(page, 'D3 only levin -> unsupported here, NOT a Sociogram pretence', 'only levin',
    { ok: false, spoken: /Not available on this view/ });
  await row(page, 'D4 go banana -> names what IS reachable', 'go banana',
    { ok: false, spoken: /no tab called "banana"\. Here: .+/ });
  await row(page, 'D5 go first -> jump to the start of the visible row', 'go first', { ok: true, spoken: /1 of \d+/ });
  await sleep(2000);
  await row(page, 'D6 go next -> walk it left to right', 'go next', { ok: true, spoken: /2 of \d+/ });
  await sleep(2000);
  await row(page, 'D7 go previous -> and back', 'go previous', { ok: true, spoken: /1 of \d+/ });

  // D8-D10: ARRIVING AT A TOOL TAB BY VOICE, which nothing had ever done -- every
  // earlier row reached the Sociogram by clicking a button that was already on
  // screen. `go sociogram` from a chapter page clicks a button in a HIDDEN row,
  // a thing no human can do, and the shell used to leave the chapter selected
  // and the row hidden. Everything downstream then resolved to the CHAPTER:
  // graph verbs came back unsupported (Tom, 2026-07-26 -- "zooming isn't
  // available in this view" while looking straight at the Sociogram), and worse,
  // `what` read the Sociogram's real filters out of the iframe and narrated them
  // under the title "Start here". Assert the RESOLVED MANIFEST, not the spoken
  // line: the old bug said "go Sociogram" perfectly and still left the shell
  // pointing at Start Here.
  await page.eval("var b = document.getElementById('chap-intro'); if (b) { b.click(); } return true;");
  await sleep(2500);
  await assertManifest(page, 'start_here', 'start_here.html');
  await row(page, 'D8 go sociogram FROM a chapter page', 'go sociogram', { ok: true, spoken: /go sociogram/i });
  await tabReady(page, 'sociogram');
  await assertManifest(page, 'sociogram', SOCIOGRAM_SRC);
  const shellChrome = await page.eval(
    "var r2=document.getElementById('row2'), c=document.querySelector('.chap-btn.active');" +
    "return { rowShown: !!r2 && r2.style.display !== 'none', chap: c ? c.textContent.replace(/\\s+/g,' ').trim() : '(none)' };");
  record('D9 the visible chrome agrees: tools row shown, chapter follows the tab',
    shellChrome.rowShown === true && /Accelerator Tools/.test(shellChrome.chap),
    'row2 shown: ' + shellChrome.rowShown + ', chapter: ' + shellChrome.chap);
  await row(page, 'D10 and the graph verbs actually work once you are there', 'zoom in',
    { ok: true, spoken: /zoom in/ });
  const shotD = await page.screenshot(path.join(SHOTS, 'D-chapter.png'));

  // ---- Phase E: the item model on a CONTENT tab ---------------------------
  //
  // The Sociogram was deep because it had addressable items; every other tab
  // was a dead end for "show me the cards". Items are declared per tab now, so
  // the same cursor and the same reader work on a page with no graph at all.
  process.stdout.write('\nPhase E -- items on a content tab (Start Here)\n');
  await page.eval("var b = document.getElementById('chap-intro'); if (b) { b.click(); } return true;");
  await sleep(2500);
  await assertManifest(page, 'start_here', 'start_here.html');
  await row(page, 'E1 what -> counts the walkable sections', 'what',
    { ok: true, spoken: /\d+ sections here/ });
  await row(page, 'E2 pick first -> names the section it landed on', 'pick first',
    { ok: true, spoken: /1 of \d+ sections/ });
  const sel1 = await page.eval(IFRAME_DOC + "var e = d.querySelector('.ccl-current h2'); return e ? e.textContent.trim() : null;");
  record('E2a the section is marked and scrolled to', !!sel1, 'current section: ' + sel1);
  await row(page, 'E3 next -> walks to the following section', 'next',
    { ok: true, spoken: /2 of \d+ sections/ });
  const sel2 = await page.eval(IFRAME_DOC + "var e = d.querySelector('.ccl-current h2'); return e ? e.textContent.trim() : null;");
  record('E3a it moved to a different section', !!sel2 && sel1 !== sel2, sel1 + ' -> ' + sel2);
  const readE = await runCmd(page, 'read');
  record('E4 read reads THE SECTION the cursor is on, and names it',
    /reading Who's who\?/.test(readE.spoken || '') && /\d+ words/.test(readE.spoken || ''), readE.spoken);
  await row(page, 'E5 stop', 'stop', { ok: true, spoken: /^stopped$/ });
  await row(page, 'E6 only levin -> still honestly unsupported on a content tab', 'only levin',
    { ok: false, spoken: /Not available on this view/ });

  // E7-E9: the phrasings from Tom's 2026-07-26 live review. `pick first` had
  // always worked; every way he actually SAID it was rejected, which is what
  // made the sections feel unreachable. Held here, on a real tab, because the
  // engine test can prove the parse but not that the cursor moved.
  await row(page, 'E7 "open the first card" reaches the cursor (open ~ pick, by arg shape)', 'open the first card',
    { ok: true, spoken: /1 of \d+ sections/ });
  await row(page, 'E8 "choose the last section" -- a synonym plus a redundant noun', 'choose the last section',
    { ok: true, spoken: /3 of 3 sections/ });
  await row(page, 'E9 "what is this" asks the same question as "what"', 'what is this',
    { ok: true, spoken: /\d+ sections here/ });

  // E10: THE READER'S PROMISE. The bar used to say 'say "stop" to interrupt'
  // while nothing routed a spoken stop anywhere -- an advertised capability the
  // build did not have. The mic is muted during a read (Tom's call, 2026-07-26),
  // so the message must name the button, and must NOT tell anyone to speak.
  const readPromise = await runCmd(page, 'read');
  record('E10 the reading message names the interrupt that actually works',
    /Stop reading/.test(readPromise.spoken || '') && !/say "stop"/i.test(readPromise.spoken || ''),
    readPromise.spoken);
  // The MUTE itself, spied at the seam rather than inferred. Deliberately not
  // asserting that #ccl-stop is on screen: headless Chrome has no speech engine,
  // so the utterance errors immediately and the (correct) teardown hides the
  // button again before anything can observe it. The mic contract does not
  // depend on an engine, so that is what is held here.
  const micCalls = await page.eval(
    "var real = window.CCLSetMic, seen = [];" +
    "window.CCLSetMic = function (on) { seen.push(!!on); return real.apply(this, arguments); };" +
    "window.CCLRun('read'); var out = seen.slice(); window.CCLSetMic = real; return out;");
  // The trailing `true` seen headless is the no-speech-engine teardown handing
  // the mic straight back, which is correct: nothing is being read, so nothing
  // should stay muted. The claim under test is only that starting a read mutes.
  record('E10a reading mutes the mic (the guide goes deaf on purpose)',
    Array.isArray(micCalls) && micCalls.indexOf(false) !== -1,
    'CCLSetMic calls during read: ' + JSON.stringify(micCalls));
  const micBack = await page.eval(
    "var real = window.CCLSetMic, seen = [];" +
    "window.CCLSetMic = function (on) { seen.push(!!on); return real.apply(this, arguments); };" +
    "window.CCLRun('stop'); var out = seen.slice(); window.CCLSetMic = real; return out;");
  record('E10b stop hands the mic back (a session that read once is not deaf forever)',
    Array.isArray(micBack) && micBack.indexOf(true) !== -1,
    'CCLSetMic calls during stop: ' + JSON.stringify(micBack));
  const helpWired = await page.eval(
    "var b=document.getElementById('ccl-readhelp'); if(!b){return 'no ? button';}" +
    "b.click(); var m=document.getElementById('help-modal'), t=document.getElementById('help-title');" +
    "var open = m && m.style.display === 'flex'; var title = t ? t.textContent : '';" +
    "if (typeof closeHelp === 'function') { closeHelp(); }" +
    "return open ? title : 'modal did not open';");
  record('E11 the ? opens reader instructions', helpWired === 'Reading aloud', 'help title: ' + helpWired);

  const shotE = await page.screenshot(path.join(SHOTS, 'E-items.png'));

  // ---- Phase F: a tab with SUB-VIEWS, and items one document deeper --------
  //
  // "Show me the cards" was the motivating failure, and Community Explorer is
  // where it is hardest: the cards are a separate app in a NESTED iframe, they
  // are only there under one of two sub-views, and the grid draws 60 of 1006 --
  // so a count taken from the DOM is a lie by a factor of seventeen. All three
  // are declared, not branched on, which is what makes the next tab cheap.
  process.stdout.write('\nPhase F -- sub-views, a nested roster, and an honest total (Community Explorer)\n');
  await page.eval("var b = document.getElementById('chap-intro'); if (b) { b.click(); } return true;");
  await sleep(2000);
  await row(page, 'F1 go community explorer', 'go community explorer', { ok: true, spoken: /go community explorer/i });
  await sleep(6000);
  await assertManifest(page, 'community_explorer', 'community_explorer.html');
  await row(page, 'F2 what -> names the sub-view it is on, not just the tab', 'what',
    { ok: true, spoken: /graph view/ });
  await row(page, 'F3 go banana -> names the SUB-VIEWS as well as the tabs', 'go banana',
    { ok: false, spoken: /On this view: graph, cards/ });
  await row(page, 'F4 go cards -> a sub-view is reachable by name, on `go`', 'go cards',
    { ok: true, spoken: /^go cards$/ });
  // The nested app loads and fetches its own data; the shell announces the
  // roster when it arrives, so wait for that rather than asserting on nothing.
  await poll(function () {
    return page.eval(
      "var f=document.getElementById('content-frame'); var d=f&&f.contentDocument;" +
      "var fr=d&&d.querySelector('#cardsview iframe'); var id=fr&&fr.contentDocument;" +
      "return !!(id && id.querySelector('#cc-card-grid > button.cc-card'));");
  }, 60000, 500, 'nested cards grid rendered');
  await row(page, 'F5 what -> counts the cards HONESTLY: drawn, and how many there really are', 'what',
    { ok: true, spoken: /cards view\s+\|\s+\d+ of \d+ communities here/ });
  const honest = await runCmd(page, 'what');
  const mF = /(\d+) of (\d+) communities here/.exec(honest.spoken || '');
  record('F5a the two numbers differ -- the render is a truncation, and it says so',
    !!mF && parseInt(mF[2], 10) > parseInt(mF[1], 10), honest.spoken);
  await row(page, 'F6 pick first -> walks a roster that lives TWO documents down', 'pick first',
    { ok: true, spoken: /\|\s+1 of \d+ communities \(\d+ in all\)/ });
  const cardSel = await page.eval(
    "var f=document.getElementById('content-frame'); var d=f&&f.contentDocument;" +
    "var fr=d&&d.querySelector('#cardsview iframe'); var id=fr&&fr.contentDocument;" +
    "var e=id&&id.querySelector('.ccl-current .cc-card-name'); return e?e.textContent.trim():null;");
  record('F6a the card is marked IN THE NESTED DOCUMENT', !!cardSel, 'current card: ' + cardSel);
  // Marking it is not enough: the point of scrolling to the cursor is that a
  // sighted user can follow what the voice is doing, and the grid starts well
  // below a masthead and a filter panel. Assert the card is ON SCREEN in the
  // nested frame -- the same "check the render, not the claim" rule the graph
  // rows follow with nodes-in-view.
  // scrollIntoView is SMOOTH, so like the graph's framing this settles before it
  // is read -- see settledInView, which exists for the same reason.
  const cardOnScreen = function () { return page.eval(
    "var f=document.getElementById('content-frame'); var d=f&&f.contentDocument;" +
    "var fr=d&&d.querySelector('#cardsview iframe'); var id=fr&&fr.contentDocument; var iw=fr&&fr.contentWindow;" +
    "var cur=id&&id.querySelector('.ccl-current'); if(!cur||!iw){return false;}" +
    "var r=cur.getBoundingClientRect(); return r.top >= 0 && r.top < iw.innerHeight;"); };
  let cardSettled = false;
  try { cardSettled = await poll(cardOnScreen, 5000, 250, 'picked card scrolled on screen'); }
  catch (e) { cardSettled = false; }
  const cardSeen = await page.eval(
    "var f=document.getElementById('content-frame'); var d=f&&f.contentDocument;" +
    "var fr=d&&d.querySelector('#cardsview iframe'); var id=fr&&fr.contentDocument; var iw=fr&&fr.contentWindow;" +
    "var cur=id&&id.querySelector('.ccl-current'); if(!cur||!iw){return null;}" +
    "var r=cur.getBoundingClientRect();" +
    "return { top: Math.round(r.top), vh: iw.innerHeight, scrolled: id.scrollingElement.scrollTop };");
  record('F6b the picked card is actually ON SCREEN, not just tagged',
    cardSettled && !!cardSeen,
    cardSeen ? ('card top ' + cardSeen.top + 'px of ' + cardSeen.vh + ' viewport, frame scrolled ' + cardSeen.scrolled + 'px') : 'no marked card');
  await row(page, 'F7 next -> moves along it', 'next', { ok: true, spoken: /\|\s+2 of \d+ communities/ });
  const readF = await runCmd(page, 'read');
  record('F7a read speaks THE CARD the cursor is on, across the frame boundary',
    /\d+ words/.test(readF.spoken || '') && !/no text/i.test(readF.spoken || ''), readF.spoken);
  await runCmd(page, 'stop');
  // The state worth LOOKING at: a card marked and scrolled to, two documents down.
  const shotFc = await page.screenshot(path.join(SHOTS, 'F-cards.png'));
  // The gate that makes the declaration honest: 21 controls in the tab, 2294 in
  // the nested app, and every one of them covered, excluded or deferred by name.
  await auditTab(page, 'community_explorer', 17, 0);
  await row(page, 'F8 go graph -> back to the other sub-view', 'go graph', { ok: true, spoken: /^go graph$/ });
  await sleep(1500);
  await row(page, 'F9 what -> the roster changed with the view', 'what', { ok: true, spoken: /graph view/ });
  await row(page, 'F10 only levin -> still no Sociogram pretence on a different graph', 'only levin',
    { ok: false, spoken: /Not available on this view/ });
  const shotF = await page.screenshot(path.join(SHOTS, 'F-subviews.png'));

  // ---- Phase G: a page reached by an IN-PAGE LINK, and the way back ---------
  //
  // Start Here's "See all 15 framings" postMessages the shell to swap the frame
  // while the Start Here chapter button stays lit. Nothing in the shell watched
  // the frame, so: the guide could not see the new page, would not believe the
  // user who said they had opened it, and `read` read the OLD document's cursor
  // (Tom, 2026-07-26). Every phase before this one navigated by clicking a tab
  // button, which is exactly why no phase caught it.
  process.stdout.write('\nPhase G -- in-page navigation, frame-derived identity, and frame history\n');
  await page.eval("var b = document.getElementById('chap-intro'); if (b) { b.click(); } return true;");
  await sleep(2500);
  await assertManifest(page, 'start_here', 'start_here.html');
  // G0a-G0e: FOLLOWING A LINK BY VOICE. Both content manifests excluded links
  // with the reason "voice reaches those by name via `go`" -- false for every
  // link that is not a tab, which is most of them, and Tom found it by having to
  // reach for the mouse to open the framings page (2026-07-26). Links resolve
  // AFTER tabs and sub-views, so one can never shadow a real destination.
  const whatLinks = await runCmd(page, 'what');
  record('G0a what lists the page\'s links -- a link nobody mentions does not exist to a voice user',
    /\d+ links: "See all 15 framings"/.test(whatLinks.spoken || ''), whatLinks.spoken);
  await row(page, 'G0b go <link text> follows it', 'go see all 15 framings',
    { ok: true, spoken: /go See all 15 framings/ });
  await sleep(3000);
  await assertManifest(page, 'what_is_c2a2', 'what_is_c2a2.html');
  // The two kinds that are NAMED but never followed. Silently omitting them
  // would be the old lie in a new place: the user would hear that a link they
  // can plainly see is not there.
  await row(page, 'G0c a new-window link is named and refused, with the reason', 'go macintyre tradition page',
    { ok: false, spoken: /opens in a new browser window.*open that one yourself/ });
  await row(page, 'G0d an unknown term names the links that ARE here', 'go nonexistent thing',
    { ok: false, spoken: /Links on this page: / });
  await page.eval("var b=document.getElementById('nav-back'); if(b && !b.disabled){b.click();} return 1;");
  await sleep(2500);
  await assertManifest(page, 'start_here', 'start_here.html');

  const linkText = await page.eval(
    IFRAME_DOC + "var a = d.querySelector('a[data-target=\"fifteen\"]');" +
    "if (!a) { return '(link missing)'; } a.click(); return a.textContent.replace(/\\s+/g,' ').trim();");
  record('G1 the framings link is where the user says it is', /15 framings/.test(linkText), 'clicked: ' + linkText);
  await sleep(3000);
  // The whole point: identity now follows the FRAME, so a page with no tab
  // button of its own still resolves to its own manifest.
  await assertManifest(page, 'what_is_c2a2', 'what_is_c2a2.html');
  await row(page, 'G2 what -> names the page it is ACTUALLY on, not the lit chapter', 'what',
    { ok: true, spoken: /view: What Is C2A2\?/ });
  const gWhat = await runCmd(page, 'what');
  record('G2a and it drops a row position that belongs to a different document',
    !/left to right/.test(gWhat.spoken || ''), gWhat.spoken);
  await row(page, 'G3 pick first -> walks THIS page, numbered by its own headings', 'pick first',
    { ok: true, spoken: /1\.Fulfillment.*\|\s*1 of 16 sections/ });
  await row(page, 'G4 next', 'next', { ok: true, spoken: /2 of 16 sections/ });
  const gRead = await runCmd(page, 'read');
  record('G5 read reads THIS document, not the previous one',
    /reading 2\.Accelerator/.test(gRead.spoken || ''), gRead.spoken);
  await runCmd(page, 'stop');

  // G5b-G5d: THE PATH THE VOICE GUIDE ACTUALLY ANSWERS FROM.
  //
  // Everything above this drives window.CCLRun. The guide's `what` and `where`
  // deliberately bypassed CCLRun for the bus, so this whole phase could pass --
  // and did -- while the guide told Tom "you're now on the Start here page,
  // under the 'intro' tab" with the framings page in front of him, and then
  // argued when he said otherwise. `intro` was chap.id minus its prefix: the
  // frame-derived src reached activeTabSrc and was thrown away one function
  // later. Testing the path I had fixed instead of the path the user talks to
  // is exactly how this shipped, so the perception verbs are now held here.
  const vgWhere = await page.eval("return window.VGWhere();");
  record('G5b where_am_i names the page the user is on, not the lit chapter',
    !!vgWhere && vgWhere.tab === 'what_is_c2a2' && /What Is C2A2/.test(vgWhere.title || ''),
    JSON.stringify(vgWhere));
  record('G5c and it never falls back to a chapter id while a frame document exists',
    !!vgWhere && vgWhere.tab !== 'intro' && !/Start here/i.test(vgWhere.title || ''),
    'tab=' + (vgWhere && vgWhere.tab) + ' title=' + (vgWhere && vgWhere.title));
  // A page with no bus listener answers supported:false -- that is honest and
  // expected. What must NOT happen is it identifying itself as somewhere else.
  const vgDesc = await page.eval("return window.VGDescribe().then(function (d) { return d; });");
  record('G5d describe_view carries the right identity even when the tab cannot answer',
    !!vgDesc && vgDesc.tab === 'what_is_c2a2' && /What Is C2A2/.test(vgDesc.title || ''),
    JSON.stringify(vgDesc));

  // The way back. setFrame uses location.replace on purpose, so there was no
  // browser history to lean on and a page like this was a one-way door.
  const backOk = await page.eval("var b=document.getElementById('nav-back'); if(!b||b.disabled){return 'disabled';} b.click(); return 'clicked';");
  record('G6 the back button is live on a page reached by a link', backOk === 'clicked', 'nav-back: ' + backOk);
  await sleep(2500);
  await assertManifest(page, 'start_here', 'start_here.html');
  await row(page, 'G7 and the guide agrees it is back on Start Here', 'what',
    { ok: true, spoken: /view: Start here.*3 sections here/ });
  const vgBack = await page.eval("return window.VGWhere();");
  record('G7a where_am_i agrees too -- one answer, not two',
    !!vgBack && vgBack.tab === 'start_here', JSON.stringify(vgBack));
  const fwdOk = await page.eval("var f=document.getElementById('nav-fwd'); if(!f||f.disabled){return 'disabled';} f.click(); return 'clicked';");
  record('G8 forward is offered only after going back', fwdOk === 'clicked', 'nav-fwd: ' + fwdOk);
  await sleep(2500);
  await assertManifest(page, 'what_is_c2a2', 'what_is_c2a2.html');
  // Voice and the button must share ONE history, or `back` means two things.
  await row(page, 'G9 the back VERB rides the same stack as the button', 'back', { ok: true, spoken: /^back$/ });
  await sleep(2500);
  await assertManifest(page, 'start_here', 'start_here.html');
  const shotG = await page.screenshot(path.join(SHOTS, 'G-inpage-nav.png'));

  // ---- Phase H: Agent Map -- sub-views on a SECOND tab ---------------------
  //
  // Tom asked whether the Agent Map's sub-tabs should be navigable now, since
  // sub-views were built generically for Community Explorer. They were not:
  // sub-views are DECLARED per tab and this was one of the nine tabs with no
  // manifest at all, so it degraded to shell caps. That is the machinery working
  // as designed, not a bug -- but it is the first proof that the design ports,
  // since this tab needed a declaration and NO new code.
  //
  // Its roster genuinely differs per view, which is why the items-list-with-when
  // form earns its keep a second time: a table of agents under Explorer, and
  // under Schedule only the legend's CATEGORIES -- the agents there are drawn
  // into a canvas and are honestly not reachable yet.
  process.stdout.write('\nPhase H -- a second tab with sub-views (Agent Map)\n');
  await activateTab(page, 'agents_tab.html');
  await sleep(6000);
  await assertManifest(page, 'agents_tab', 'agents_tab.html');
  await auditTab(page, 'agents_tab', 10, 1);
  await row(page, 'H1 what -> names the sub-view it booted into', 'what',
    { ok: true, spoken: /schedule view/ });
  await row(page, 'H2 go explorer -> a sub-view on a tab that never had one', 'go explorer',
    { ok: true, spoken: /^go explorer$/ });
  await sleep(1500);
  await row(page, 'H3 what -> the roster CHANGED with the view', 'what',
    { ok: true, spoken: /explorer view.*\d+ agents here/ });
  await row(page, 'H4 pick first -> walks the agent table', 'pick first',
    { ok: true, spoken: /1 of \d+ agents/ });
  await row(page, 'H5 next', 'next', { ok: true, spoken: /2 of \d+ agents/ });
  await row(page, 'H6 go schedule -> back, and the roster changes again', 'go schedule',
    { ok: true, spoken: /^go schedule$/ });
  await sleep(1500);
  // The honest half: the schedule view's agents are canvas-drawn, so what is
  // addressable there is the legend's categories. Saying "categories" and not
  // "agents" is the declaration refusing to overclaim.
  await row(page, 'H7 what -> categories, NOT a pretence that canvas agents are walkable', 'what',
    { ok: true, spoken: /schedule view\s*\|\s*\d+ categories here/ });
  await row(page, 'H8 an unknown destination names this tab\'s three views', 'go banana',
    { ok: false, spoken: /On this view: schedule, sociogram, explorer/ });
  const shotH = await page.screenshot(path.join(SHOTS, 'H-agent-map.png'));

  // ---- Idle listening cutoff: what can honestly be checked without a session --
  //
  // The 10s behaviour itself needs a LIVE realtime session to observe, and
  // minting one costs money -- so it is NOT verified here and must be checked by
  // hand. Saying that plainly beats a row that asserts something adjacent and
  // reads like coverage. What IS checkable headlessly: the control exists, it
  // starts hidden (it may only appear once silence has switched listening off),
  // and resume with no session is a harmless no-op rather than a throw.
  const idleUi = await page.eval(
    "var r = document.getElementById('vg-resume');" +
    "if (!r) { return 'no resume button'; }" +
    "if (r.style.display !== 'none') { return 'resume button visible with no session'; }" +
    "if (!window.VoiceGuide || typeof window.VoiceGuide.resume !== 'function') { return 'VoiceGuide.resume missing'; }" +
    "try { window.VoiceGuide.resume(); } catch (e) { return 'resume threw with no session: ' + e.message; }" +
    "return document.getElementById('vg-resume').style.display === 'none' ? 'ok' : 'resume revealed itself with no session';");
  record('I1 the Resume control exists, starts hidden, and is inert with no session',
    idleUi === 'ok', 'vg-resume: ' + idleUi);

  // ---- report ----
  const failed = results.filter(function (r) { return !r.ok; });
  process.stdout.write('\n' + '-'.repeat(70) + '\n');
  process.stdout.write('rows: ' + results.length + '   passed: ' + (results.length - failed.length) + '   failed: ' + failed.length + '\n');
  process.stdout.write('page exceptions: ' + page.exceptions.length + '   console errors: ' + page.consoleErrors.length + '\n');
  page.exceptions.forEach(function (e) { process.stdout.write('  EXCEPTION  ' + e.split('\n')[0] + '\n'); });
  page.consoleErrors.forEach(function (e) { process.stdout.write('  CONSOLE    ' + e.slice(0, 200) + '\n'); });
  process.stdout.write('screenshots:\n  ' + [shotA, shotFind, shotB, shotB2, shotC, shotD, shotE, shotFc, shotF, shotG, shotH].join('\n  ') + '\n');

  const clean = failed.length === 0 && page.exceptions.length === 0 && page.consoleErrors.length === 0;
  process.stdout.write(clean ? '\nSHELL TEST GREEN\n' : '\nSHELL TEST RED\n');
  cleanup();
  process.exit(clean ? 0 : 1);
}

// Exported so sibling harnesses (the section-9 live coverage audit, per-tab
// fan-out rows) reuse this rig instead of re-implementing a CDP client.
module.exports = {
  CDP: CDP, Page: Page, startServer: startServer, startChrome: startChrome,
  activateTab: activateTab, tabReady: tabReady, cclReady: cclReady,
  runCmd: runCmd, readDom: readDom, onGroupCount: onGroupCount,
  cleanup: cleanup, PORT: PORT, SOCIOGRAM_SRC: SOCIOGRAM_SRC, METABOLISM_SRC: METABOLISM_SRC
};

if (require.main === module) {
  main().catch(function (e) {
    process.stdout.write('\nHARNESS ERROR: ' + (e && e.stack || e) + '\n');
    cleanup();
    process.exit(2);
  });
}
