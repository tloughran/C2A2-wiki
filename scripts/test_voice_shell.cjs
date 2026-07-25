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
  const gd = (a.gestures && a.gestures.deferred) || 0;
  if (expectGestureDeferred !== undefined && gd !== expectGestureDeferred) {
    problems.push('gestures deferred=' + gd + ' expected ' + expectGestureDeferred);
  }
  record('audit ' + tabName, problems.length === 0,
    problems.join(' | ') || (a.total + ' controls: ' + a.covered + ' covered, ' + a.excluded + ' excluded, ' +
      a.deferred.length + ' deferred, 0 uncovered  ||  gestures: ' + JSON.stringify(a.gestures)));
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
  await auditTab(page, 'sociogram', 21, 3);
  const bootGroups = await onGroupCount(page);
  await row(page, 'A1 only levin friston -> 2 groups AND nodes actually on screen', 'only levin friston',
    { ok: true, spoken: /-> 2 groups on/, groups: function (n) { return n === 2; }, view: function (v) { return v > 0; } });
  // The 2026-07-25 regression: 'architecture' is both a group and a section
  // parent. Asserting the RENDER is the whole point -- the old code passed a
  // groups-on assertion while showing an empty graph.
  await row(page, 'A2 undo -> boot filter set restored', 'undo',
    { ok: true, spoken: /undid \(filters\)/, groups: function (n) { return n === bootGroups; } });
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
  await row(page, 'A3 fit', 'fit', { ok: true, spoken: /^fit$/ });
  await row(page, 'A4 what -> names the live view', 'what', { ok: true, spoken: /view: Sociogram/ });
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

  // ---- report ----
  const failed = results.filter(function (r) { return !r.ok; });
  process.stdout.write('\n' + '-'.repeat(70) + '\n');
  process.stdout.write('rows: ' + results.length + '   passed: ' + (results.length - failed.length) + '   failed: ' + failed.length + '\n');
  process.stdout.write('page exceptions: ' + page.exceptions.length + '   console errors: ' + page.consoleErrors.length + '\n');
  page.exceptions.forEach(function (e) { process.stdout.write('  EXCEPTION  ' + e.split('\n')[0] + '\n'); });
  page.consoleErrors.forEach(function (e) { process.stdout.write('  CONSOLE    ' + e.slice(0, 200) + '\n'); });
  process.stdout.write('screenshots:\n  ' + [shotA, shotB, shotB2, shotC].join('\n  ') + '\n');

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
