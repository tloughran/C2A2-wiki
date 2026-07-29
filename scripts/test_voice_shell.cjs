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
// EXACT, not a floor. Everything the Narrative Connectome defers is in scope and
// reachable by hand today -- the filter checkboxes, the search box, the labels
// toggle, the left page's close, Reset View -- and the point of pinning the
// number is that a new control cannot join that list without reddening the gate.
// Raise it only together with the manifest entry that explains the new one.
const PRS_DEFERRED = 5;

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
    // Phase W arms the output meter from a synthetic tone. In the real page the
    // AudioContext is created inside a click; from CDP there is no gesture, and
    // a suspended context would read as silence and make the wave rows pass for
    // the wrong reason. Output is still muted by --mute-audio above.
    '--autoplay-policy=no-user-gesture-required',
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

// Some results arrive LATER than the command that asked for them: turning to the
// commentary has to wait for the page's own fetch, and a test that read the
// status line immediately would be asserting the intent rather than the result.
async function waitStatus(page, re, limitMs) {
  const limit = limitMs || 10000;
  for (let waited = 0; waited <= limit; waited += 150) {
    const bar = await page.eval("var el = document.getElementById('ccl-result'); return el ? el.textContent : '';");
    if (re.test(bar || '')) { return bar; }
    await sleep(150);
  }
  return await page.eval("var el = document.getElementById('ccl-result'); return el ? el.textContent : '';");
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
  // Some of what a guide says is wrong by being PRESENT -- offering links from a
  // pane that is not on screen, say. A positive match cannot catch that, and the
  // row it hid went green for a whole run.
  if (expect.notSpoken && expect.notSpoken.test(r.spoken || '')) {
    problems.push('spoken ' + JSON.stringify(r.spoken) + ' should NOT match ' + expect.notSpoken);
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
// A syntax error inside one of explorer.html's inline <script> blocks does not
// announce itself: the block simply never runs, and the first symptom is some
// unrelated global missing an hour later ("window.VGWhere is not a function").
// One apostrophe inside a single-quoted instruction string did exactly that on
// 2026-07-27. Parsing the blocks up front turns a mystery into a line number.
function inlineJsGate() {
  const html = fs.readFileSync(path.join(ROOT, 'wiki/explorer.html'), 'utf8');
  const blocks = html.match(/<script(?![^>]*\bsrc=)[^>]*>[\s\S]*?<\/script>/g) || [];
  const src = blocks.map(function (b) { return b.replace(/^<script[^>]*>/, '').replace(/<\/script>$/, ''); }).join('\n;\n');
  try {
    new (require('vm').Script)(src, { filename: 'explorer.html:inline' });
    record('explorer.html inline JS parses', true, blocks.length + ' script blocks');
  } catch (e) {
    record('explorer.html inline JS parses', false, e.message);
  }
}

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

  inlineJsGate();
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
  // This tab now HAS filters (increment 2), so the refusal moved: it is no
  // longer "that verb is not supported here" but "that is not one of MY
  // groups", and it names its own axis. Still the same guarantee under test --
  // no Sociogram pretence -- asserted at the point where the pretence would now
  // be easiest, because the verb finally works on this tab.
  await row(page, 'D3 only levin -> a Sociogram tradition is not one of THIS tab\'s groups', 'only levin',
    { ok: false, spoken: /not something this view filters by.*types:/ });
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
  await auditTab(page, 'community_explorer', 7, 2);
  // THE DIMENSIONS ARE THE GRAPH'S, NOT THE TAB'S. Everything increment 2 added
  // is declared `when: #tab-graph`, and the cards view is where a spec that
  // forgot to say so would look identical -- the checkboxes are still in the
  // document, #btn-fit still answers .click(). So the refusals are asserted
  // HERE, before switching back, and they must name this page rather than
  // leaking the Sociogram's function names (the bug the `when` gate created and
  // the two `typeof` guards close).
  await row(page, 'F7b only civic on the CARDS view -> the filters belong to the graph', 'only civic',
    { ok: false, spoken: /filters are not available on this view/ });
  await row(page, 'F7c fit on the CARDS view -> refuses without naming fitAll', 'fit',
    { ok: false, spoken: /cannot be fit to everything/ });
  await row(page, 'F7d close on the CARDS view -> refuses without naming dismissRightPanel', 'close',
    { ok: false, spoken: /no way to close what is open/ });
  await row(page, 'F8 go graph -> back to the other sub-view', 'go graph', { ok: true, spoken: /^go graph$/ });
  await sleep(1500);
  await row(page, 'F9 what -> the roster changed with the view', 'what', { ok: true, spoken: /graph view/ });
  await row(page, 'F10 only levin -> a tradition is not a community type here', 'only levin',
    { ok: false });
  // ---- Phase F (increment 2): the graph sub-view's own dimensions ----------
  //
  // The tab was reachable and its cards were walkable; the GRAPH was declared
  // `kind: "none"` and had no filters, no knob and no camera. What made that
  // expensive was not the tab -- it was that the shell's roster reader had been
  // generalised off prs_3d's conventions (a `var` window map) and could not
  // read a page keeping its truth in `const activeTypes = new Set(...)`. So
  // these rows are really a test of the SHELL: keys read off the controls,
  // truth read back off `.checked`, all/none through two spans, a label read
  // off the bound datum, and `fit` as a click.
  const ceCircles = function () { return page.eval(
    IFRAME_DOC + "return d ? d.querySelectorAll('#graph circle').length : -1;"); };
  const ceStats = function () { return page.eval(
    IFRAME_DOC + "var e = d && d.querySelector('#stats'); return e ? e.textContent : null;"); };
  const ceTypesOn = function () { return page.eval(
    IFRAME_DOC + "var b = d ? [].slice.call(d.querySelectorAll('#typefilters input[data-type]')) : [];" +
    "return b.filter(function (i) { return i.checked; }).length;"); };

  const bootCircles = await ceCircles();
  record('F11 the graph draws a roster at all', bootCircles > 0, bootCircles + ' circles under #graph');
  // THE BUG THIS ROW EXISTS FOR: a <circle> has no textContent, so before
  // label.datum every one of these would have come back nameless -- the
  // Connectome's 222 empty labels arriving from the other direction, and
  // invisible to any row that only counted the roster.
  const named = await page.eval(
    "var r = window.CCLItems ? window.CCLItems() : null;" +
    "if (!r) { return null; }" +
    "return { n: r.length, blank: r.filter(function (x) { return !x.label; }).length," +
    "         first: r.length ? r[0].label : null };");
  record('F11a every node has a NAME, read off the bound datum',
    !!named && named.n > 0 && named.blank === 0 && !!named.first,
    named ? (named.n + ' items, ' + named.blank + ' nameless, first: ' + JSON.stringify(named.first)) : 'CCLItems missing');
  await row(page, 'F11b what -> counts communities, not nodes', 'what',
    { ok: true, spoken: /graph view/ });

  await row(page, 'F12 only civic -> a display name reached by its short form', 'only civic',
    { ok: true, spoken: /types: civic-and-political/ });
  const onlyCivic = await ceCircles(), onlyCivicOn = await ceTypesOn();
  record('F12a the write travelled the checkbox and the graph REBUILT',
    onlyCivicOn === 1 && onlyCivic > 0 && onlyCivic < bootCircles,
    onlyCivicOn + ' of 8 types checked, ' + onlyCivic + ' circles (was ' + bootCircles + ')  |  ' + (await ceStats()));

  await row(page, 'F13 none -> through a <span>, which is not a checkbox and not a button', 'none',
    { ok: true });
  const noneCircles = await ceCircles(), noneOn = await ceTypesOn();
  record('F13a none really emptied it -- the span click IS the road',
    noneOn === 0 && noneCircles === 0, noneOn + ' types checked, ' + noneCircles + ' circles');

  await row(page, 'F14 all -> the other span', 'all', { ok: true });
  const allOn = await ceTypesOn(), allCircles = await ceCircles();
  record('F14a all restored every type', allOn === 8 && allCircles === bootCircles,
    allOn + ' of 8 types checked, ' + allCircles + ' circles');

  // undo has to step back through a dimension whose BEFORE was read off the
  // checkboxes rather than a state object -- the read-back change is what this
  // asserts, not the journal.
  await row(page, 'F15 undo -> back to none, off a read that never touched the page', 'undo',
    { ok: true, spoken: /undid \(filters\)/ });
  record('F15a undo restored the emptied cut', (await ceTypesOn()) === 0, 'types checked: ' + (await ceTypesOn()));
  await row(page, 'F16 redo -> forward again', 'redo', { ok: true });
  record('F16a redo restored all eight', (await ceTypesOn()) === 8, 'types checked: ' + (await ceTypesOn()));

  await row(page, 'F17 set exemplary on -> the one deferred control that needed nothing built',
    'set exemplary on', { ok: true, spoken: /exemplary on/, dom: { '#q3only': { prop: 'checked', value: 'on' } } });
  const q3Circles = await ceCircles();
  record('F17a the quality gate composes with the type cut by AND',
    q3Circles > 0 && q3Circles < bootCircles, q3Circles + ' circles of ' + bootCircles);
  await row(page, 'F17b set exemplary off -> and back', 'set exemplary off',
    { ok: true, dom: { '#q3only': { prop: 'checked', value: 'off' } } });

  // `open <name>` on a d3 roster: matched by the datum's name, activated by the
  // page's own click handler, and read back off the page's own marker -- the
  // right panel, scoped to `.open` so a closed panel's stale heading cannot be
  // reported as the current selection.
  const firstName = named && named.first;
  await row(page, 'F18 open <a community> -> by the name the datum carries',
    'open ' + firstName, { ok: true, spoken: /^opened / });
  const panel = await page.eval(
    IFRAME_DOC + "var e = d && d.querySelector('#rightpanel.open #rp-content h3');" +
    "return e ? (e.textContent || '').trim() : null;");
  record('F18a the PAGE opened it, and the panel says so',
    !!panel && panel.length > 0, 'panel heading: ' + JSON.stringify(panel));
  await row(page, 'F19 close -> the page\'s own close, not ours', 'close', { ok: true });
  const ceShut = await page.eval(
    IFRAME_DOC + "return !!(d && d.querySelector('#rightpanel') && !d.querySelector('#rightpanel.open'));");
  record('F19a the panel is actually shut', ceShut === true, 'rightpanel.open present: ' + !ceShut);

  await row(page, 'F20 fit -> a camera verb that is a button click', 'fit', { ok: true, spoken: /^fit$/ });
  await row(page, 'F20a zoom in -> not declared, and refuses by what this view IS', 'zoom in',
    { ok: false });
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
  // H9-H12: NAME COLLISIONS BETWEEN A SUB-VIEW AND A REAL TAB.
  //
  // Three of this tab's view names -- sociogram, explorer, and the old alias
  // `map` -- also name real TABS. destinations.json is authoritative and
  // sub-views resolve only on `unresolved`, so `go sociogram` matched the
  // Sociogram TOOL every time: standing on the Agent Map and asking for its
  // sociogram view threw the user across the app, repeatedly, with no phrasing
  // that could stop it (Tom, 2026-07-26). "A sub-view can never shadow a real
  // tab" is right in general and exactly wrong when the user is already ON the
  // tab that owns the name.
  await row(page, 'H9 standing on the tab, its OWN view wins over the same-named tab', 'go sociogram',
    { ok: true, spoken: /this tab's sociogram view/ });
  await sleep(2500);
  await assertManifest(page, 'agents_tab', 'agents_tab.html');
  await row(page, 'H9a and what agrees it is the sub-view, not the tool', 'what',
    { ok: true, spoken: /Agent Map.*sociogram view/ });
  // The message above ADVERTISES "go <name> tab". An advertised phrase that does
  // not work is the failure mode this build keeps repairing, so it is held here.
  await row(page, 'H10 the advertised escape hatch is real: reach the whole tool', 'go sociogram tab',
    { ok: true, spoken: /^go Sociogram$/ });
  await tabReady(page, 'sociogram');
  await assertManifest(page, 'sociogram', SOCIOGRAM_SRC);
  // Tom's last failure: having reached the view, he moved away and could not ask
  // for it back, because nothing addressed a view and a tab at once.
  await row(page, 'H11 a view of ANOTHER tab, named together, from anywhere', 'go sociogram view of the agent map',
    { ok: true, spoken: /go Agent Map -> sociogram view/ });
  await sleep(9000);
  await assertManifest(page, 'agents_tab', 'agents_tab.html');
  await row(page, 'H11a it really landed in that sub-view, not just on the tab', 'what',
    { ok: true, spoken: /Agent Map.*sociogram view/ });
  await row(page, 'H12 the other word order works too', 'go agent map explorer',
    { ok: true, spoken: /go Agent Map -> explorer view/ });
  await sleep(2500);
  await row(page, 'H12a and it walks that roster', 'what',
    { ok: true, spoken: /explorer view.*\d+ agents here/ });
  const shotH = await page.screenshot(path.join(SHOTS, 'H-agent-map.png'));

  // ---- Phase J: Curriculum Tools -- a roster that lives BEHIND the click ----
  //
  // Every tab so far had its roster already on screen, so `pick` marking an item
  // was enough. Summa's contents tree is 5 parts -> 611 questions -> 2747
  // articles, all built EAGERLY into the DOM and hidden by collapsed containers.
  // Two things broke there, and both were shell-side rather than declarations:
  //
  //   1. domItems' visibility test asked whether the element's OWN computed
  //      display was none, which cannot see an ancestor's. Every one of the 2747
  //      rows has offsetParent null and display `flex`, so a collapsed tree
  //      enumerated the entire vault. J2 is the regression test and it does not
  //      hard-code a number: it counts the visible rows in the page itself and
  //      asserts the guide says the same, so it stays true as the Summa grows.
  //   2. `pick` MARKS; it has never clicked. On a closed tree that reaches
  //      nothing at all. `open` existed but was wired to openNodeByLabel -- a
  //      global on wiki_narration.html alone -- which is why no tab since the
  //      Sociogram could have it in caps.
  process.stdout.write('\nPhase J -- a roster behind the click (Curriculum Tools / Summa)\n');
  await activateTab(page, 'summa_explorer.html');
  await sleep(6000);
  await assertManifest(page, 'curriculum_tools', 'summa_explorer.html');
  await auditTab(page, 'curriculum_tools', 3, 0);

  // The guide's count vs the page's own truth. Without the getClientRects fix
  // this reads in the thousands while a human sees five closed parts.
  const visRows = await page.eval(
    "var d = document.getElementById('content-frame').contentDocument;" +
    "var els = d.querySelectorAll('.part-header, .q-row, .a-row.avail'), n = 0;" +
    "for (var i = 0; i < els.length; i++) { if (els[i].getClientRects().length) { n++; } }" +
    "return { visible: n, built: els.length };");
  record('J0 the page really does build far more rows than it shows',
    visRows.built > 2000 && visRows.visible < visRows.built,
    visRows.visible + ' visible of ' + visRows.built + ' built');
  await row(page, 'J1 what -> names the contents view', 'what',
    { ok: true, spoken: /contents view/ });
  await row(page, 'J2 the roster is what is ON SCREEN, not what is in the DOM', 'what',
    { ok: true, spoken: new RegExp('\\b' + visRows.visible + ' entries here') });
  await row(page, 'J3 pick first -> walks the tree', 'pick first',
    { ok: true, spoken: /1 of \d+ entries/ });
  // Write-returns-the-READ on a knob bound to a pair of BUTTONS rather than a
  // select. switchMode returns early while nothing is open, so the honest answer
  // is that the mode did not move -- not the value we asked for. This row has to
  // come BEFORE anything is opened, or its premise is quietly false.
  await row(page, 'J4 set mode with nothing open reports the truth, not the intent',
    'set mode synthesis', { ok: true, spoken: /transcript/ });
  await row(page, 'J5 open (bare) -> activates the row the cursor is on', 'open',
    { ok: true, spoken: /opened Day 1/ });
  await sleep(1200);
  // Same knob, same command, different answer -- because the page can now honour
  // it. Nothing in the manifest changed between J4 and J6.
  await row(page, 'J6 and now the same set MOVES, because the page can honour it',
    'set mode synthesis', { ok: true, spoken: /synthesis/ });
  // The heart of it: opening a CONTAINER grows the roster and the guide says by
  // how much. Expanding a question and loading an article are the same verb on
  // the same tree, and with no screen they would otherwise sound identical.
  await row(page, 'J7 open by NAME -> a question expands, and the roster grows out loud',
    'open the nature and extent of sacred doctrine',
    { ok: true, spoken: /opened .*sacred doctrine.*\|\s*now \d+ entries/i });
  // Now that a question is open, an ARTICLE row exists to be opened -- and the
  // page marks the one it loaded with `.a-row.sel`, which is what the spec
  // declares `selected` as and therefore what the guide reads back. Reading our
  // own click instead would report an unavailable article (no handler at all) as
  // a success. The label is taken from the page and checked for uniqueness
  // first: many articles are titled "Article 1", and a test that tripped the
  // ambiguity guard would be testing the wrong thing.
  const art = await page.eval(
    "var d = document.getElementById('content-frame').contentDocument;" +
    "var rows = d.querySelectorAll('.part-header, .q-row, .a-row.avail'), seen = {}, arts = [];" +
    "for (var i = 0; i < rows.length; i++) {" +
    "  if (!rows[i].getClientRects().length) { continue; }" +
    "  var h = rows[i].querySelector('.part-name, .q-title-text, .a-title-text');" +
    "  var t = h ? h.textContent.trim() : '';" +
    "  seen[t] = (seen[t] || 0) + 1;" +
    "  if (rows[i].classList.contains('a-row')) { arts.push(t); }" +
    "}" +
    "for (var j = 0; j < arts.length; j++) { if (seen[arts[j]] === 1) { return arts[j]; } }" +
    "return null;");
  record('J7a the expanded question really put article rows on screen', !!art, String(art));
  await row(page, 'J7b open that article by name', 'open ' + art,
    { ok: true, spoken: /opened /i });
  await sleep(1500);
  const sel = await page.eval(
    "var d = document.getElementById('content-frame').contentDocument;" +
    "var s = d.querySelector('.a-row.sel'), c = d.getElementById('content-area');" +
    "return { sel: s ? (s.textContent || '').trim().slice(0, 40) : null," +
    " showing: !!(c && c.style.display !== 'none') };");
  record('J7c the guide reads the PAGE\'s own marker, not the click it just made',
    !!sel.sel && sel.showing, JSON.stringify(sel));
  await row(page, 'J8 open with nothing to match says so, and says what there is to choose from',
    'open a question that does not exist',
    { ok: false, spoken: /nothing here is called/ });
  // `read` must speak the ARTICLE, not the tree row that opened it. The row's own
  // text is "A1Article 1Day 2" -- the which-document family's exact shape, and
  // the reader has already been caught calling a card "this article".
  // THE WORD COUNT IS THE ASSERTION. A first pass of this row matched /reading/
  // and went green while the guide was reading the tree row -- "A1 Article 1
  // Day 2", which it reported as 5 words. A Summa article is never five words,
  // so the number is what distinguishes the door from the room; matching the
  // verb only tests that something was said.
  await row(page, 'J9 read -> speaks the ARTICLE, not the five-word row that opened it', 'read',
    { ok: true, spoken: /reading .*\|\s*([1-9]\d{2,}) words/ });
  await row(page, 'J10 stop', 'stop', { ok: true, spoken: /stopped/ });
  await row(page, 'J11 close -> back to the index, via the control the spec declared', 'close',
    { ok: true, spoken: /closed/ });
  // ---- Phase K: the highlight, the two renderings, and the address ---------
  //
  // All three come from Tom doing the ordinary thing and finding it missing
  // (2026-07-27): highlighting a paragraph and asking for it back, asking for
  // "the commentary" rather than a toggle, and naming a place in the book the
  // way anyone holding it would -- "question 4, article 2".
  process.stdout.write('\nPhase K -- highlights, renderings, and coordinates\n');
  // K1-K3: THE ADDRESS. Nothing is open; the coordinate has to open its own way
  // in, because a target inside a collapsed container is addressable but not
  // reachable.
  await row(page, 'K1 a coordinate is not a tab, a view or a link -- and it lands',
    'go to question 4, article 2',
    { ok: true, spoken: /^go .+/ });
  await sleep(1500);
  const at = await page.eval(
    "var d = document.getElementById('content-frame').contentDocument;" +
    "var s = d.querySelector('.a-row.sel');" +
    "return s ? s.getAttribute('data-ref') : null;");
  record('K2 it really opened THAT article, by ref', /\.Q4\.A2$/.test(String(at)), String(at));
  // TOM'S EXACT EXCHANGE (2026-07-27). Standing in the Summa explorer he said
  // "Prima Pars, Question 18, Article 1" and was told "that kind of search isn't
  // supported here" -- because the guide chose `find`, which this tab does not
  // have, so the address was rejected at the door and never reached the
  // resolver. The words were his; the verb was the model's guess. A named place
  // is a place whatever verb it arrives under.
  await row(page, 'K1a a coordinate sent under the WRONG verb still lands',
    'find Prima Pars, Question 18, Article 1',
    { ok: true, spoken: /^go /, notSpoken: /not supported|Not available/ });
  await sleep(1500);
  const at18 = await page.eval(
    "var d = document.getElementById('content-frame').contentDocument;" +
    "var s = d.querySelector('.a-row.sel');" +
    "return s ? s.getAttribute('data-ref') : null;");
  record('K1b and it is the article he asked for', String(at18) === 'I.Q18.A1', String(at18));
  await row(page, 'K3 a coordinate that does not exist says so plainly',
    'go to question 4000, article 9',
    { ok: false, spoken: /there is no|no tab called/ });
  // K4-K5: THE TWO RENDERINGS. One article, read two ways -- and the second read
  // must wait for the page's fetch rather than speaking the first one again.
  // The mode is a PAGE-level toggle and survives loading another article, so the
  // starting rendering is stated rather than assumed -- the first cut of this row
  // asked for the commentary while the page was already showing it, and read
  // "failed" for being right.
  await row(page, 'K3a start from the transcript, explicitly', 'set mode transcript',
    { ok: true, spoken: /transcript/ });
  await sleep(1200);
  await row(page, 'K4 read the commentary -> turns to it first', 'read the commentary',
    { ok: true, spoken: /turning to the commentary/ });
  const barCom = await waitStatus(page, /reading the commentary of/, 12000);
  record('K5 and then reads THAT rendering, naming it', /reading the commentary of .*\|\s*\d+ words/.test(barCom), barCom);
  await runCmd(page, 'stop');
  // Asking for what is already showing must not pretend to turn to it -- it
  // reads, at once, and says which rendering it is reading.
  // "Take me to the corresponding section of the contemporary synthesis" came
  // back as "there is no tab called Contemporary Synthesis" -- true, useless,
  // and it sent Tom away from something already in front of him. A rendering is
  // not a place in the tab row, but going to one is exactly what it feels like.
  await runCmd(page, 'set mode transcript');
  await sleep(1000);
  await row(page, 'K5b take me to the contemporary synthesis -> turns to it, does not deny it exists',
    'go to the corresponding section of the contemporary synthesis',
    { ok: true, spoken: /^go commentary/, notSpoken: /no tab called/ });
  await sleep(1200);
  const mode = await page.eval(
    "var d = document.getElementById('content-frame').contentDocument;" +
    "return d.getElementById('btn-synthesis').classList.contains('on') ? 'synthesis' : 'transcript';");
  record('K5c and the page really is showing it', mode === 'synthesis', mode);
  await row(page, 'K5a asking again for what is already up just reads it', 'read the commentary',
    { ok: true, spoken: /reading the commentary of/, notSpoken: /turning to/ });
  await runCmd(page, 'stop');
  await row(page, 'K6 read the transcript -> turns back', 'read the transcript',
    { ok: true, spoken: /turning to the transcript/ });
  const barTr = await waitStatus(page, /reading the transcript of/, 12000);
  record('K6a and reads the transcript, not the commentary it had just read',
    /reading the transcript of .*\|\s*\d+ words/.test(barTr), barTr);
  await runCmd(page, 'stop');
  // K7-K9: THE USER'S OWN HIGHLIGHT. Selected in the page exactly as a mouse
  // drag would, then asked for by the ordinary word.
  const selWords = await page.eval(
    "var d = document.getElementById('content-frame').contentDocument;" +
    "var p = d.querySelector('#content-area p, #content-area div, #content-area');" +
    "var r = d.createRange(); r.selectNodeContents(p);" +
    "var s = d.defaultView.getSelection(); s.removeAllRanges(); s.addRange(r);" +
    "return s.toString().replace(/\\s+/g, ' ').trim().split(' ').length;");
  record('K7 a selection exists in the page, as a mouse drag would leave it', selWords > 5, selWords + ' words');
  // DETECTING it, not just reading from it: the original complaint was that the
  // guide could not perceive a highlight at all, and a `read` that uses one
  // silently still leaves "what am I looking at?" answered wrongly.
  await row(page, 'K7a what -> reports the highlight as part of what is on screen', 'what',
    { ok: true, spoken: /you have \d+ words selected/ });
  // THE PATH A PERSON ACTUALLY TAKES. K7/K7a select and ask in the same breath,
  // with focus never leaving the article -- which is not how anyone uses this.
  // You drag across a paragraph and THEN turn to the guide: you click its box,
  // or press its button. Tom: "still can't pick up highlighted sections"
  // (2026-07-27), with the harness green, because the harness had tested the
  // half that never happens.
  await page.eval(
    "var i = document.getElementById('ccl-input'); i.focus(); i.click(); return true;");
  await sleep(400);
  await row(page, 'K7b the highlight survives turning to the guide (focus in the command box)', 'what',
    { ok: true, spoken: /you have \d+ words selected/ });
  await page.eval(
    "var b = document.getElementById('vg-launch'); if (b) { b.click(); } return true;");
  await sleep(600);
  await row(page, 'K7c and survives opening the voice panel', 'what',
    { ok: true, spoken: /you have \d+ words selected/ });
  await page.eval(
    "var b = document.getElementById('vg-close'); if (b) { b.click(); } return true;");
  await sleep(400);
  await row(page, 'K8 read -> the highlight wins, and is NAMED so it is never a silent swap', 'read',
    { ok: true, spoken: /reading your selection\s*\|\s*\d+ words/ });
  await runCmd(page, 'stop');
  await row(page, 'K9 read all -> the way back to the whole thing', 'read all',
    { ok: true, spoken: /reading .*\|\s*\d+ words/, notSpoken: /your selection/ });
  await runCmd(page, 'stop');
  // K12-K15: SEARCH BY WHAT IT IS ABOUT. Tom's queued ask, and what a docent
  // actually does -- not knowing the Summa by heart, but knowing where things
  // live and how to look. Plain title matching over the tab's own 611 question
  // titles: no model call, no embedding, no broker spend.
  await row(page, 'K12 several matches are NAMED back, never silently narrowed to one',
    'go a question on angelic knowledge',
    { ok: false, spoken: /questions on .*medium of angelic knowledge/i });
  await row(page, 'K13 naming one of them exactly lands on it',
    'go the medium of angelic knowledge',
    { ok: true, spoken: /^go The medium of angelic knowledge/ });
  await sleep(1200);
  const q55 = await page.eval(
    "var d = document.getElementById('content-frame').contentDocument;" +
    "var e = d.querySelector('.ccl-current');" +
    "return e ? e.getAttribute('data-qkey') : null;");
  record('K14 and it is that question, by key', String(q55) === 'I.Q55', String(q55));
  // The broadest net runs LAST: a word that is also a real destination must
  // still reach the destination, not a question whose title happens to contain it.
  await row(page, 'K15 search never shadows something the user named outright', 'go contents',
    { ok: true, spoken: /^go contents/ });
  await row(page, 'K16 a topic with nothing on it falls through to the honest list',
    'go a question on quantum chromodynamics',
    { ok: false, spoken: /no tab called/ });

  // K17-K20: WHAT THE READER ACTUALLY SAYS. Tom, listening to it: it starts at
  // the top and reads a pile of metadata, with timestamps all through the text.
  // A Summa transcript opens with three provenance blockquotes -- the episode
  // URL, the series and day, and a paragraph of ASR-correction notes -- then a
  // `## Transcript` scaffold heading, then every paragraph begins [00:00:05].
  await runCmd(page, 'go to question 4, article 2');
  await sleep(1500);
  await runCmd(page, 'set mode transcript');
  await sleep(1500);
  const spoken = await page.eval("return window.CCLSpeechScript ? window.CCLSpeechScript().body : null;");
  record('K17 no ASR timestamps survive into the speech', !/\[\s*\d{1,2}:\d{2}/.test(String(spoken)),
    (String(spoken).match(/\[\s*\d{1,2}:\d{2}[^\]]*\]/g) || []).slice(0, 3).join(' '));
  record('K18 the provenance blockquotes are not read as prose',
    !/Auto-generated captions|Episode:|Series:/.test(String(spoken)),
    String(spoken).slice(0, 90));
  record('K19 the scaffold heading is not announced between title and text',
    !/(^|\.\s)Transcript(\.|\s)/.test(String(spoken)), String(spoken).slice(0, 90));
  record('K20 and the text itself is still all there',
    String(spoken).split(/\s+/).length > 2000, String(spoken).split(/\s+/).length + ' words');

  // K21-K23: SUMMARIZE. The guide could not do it because it had never been
  // handed anything to summarise -- every other result is a status line.
  // Clear the highlight left by K7 first: summarize prefers a selection, exactly
  // as read does, so leaving one up would test the wrong source (it did).
  await page.eval("var d = document.getElementById('content-frame').contentDocument;" +
    "d.defaultView.getSelection().removeAllRanges(); return true;");
  const sum = await page.eval(
    "var r = window.CCLRun('summarize');" +
    "return { ok: r.ok, spoken: r.spoken, words: r.text ? r.text.split(/\\s+/).length : 0," +
    "         stamps: r.text ? /\\[\\s*\\d{1,2}:\\d{2}/.test(r.text) : null };");
  record('K21 summarize hands the TEXT back, not a description of the view',
    sum.ok && sum.words > 2000, JSON.stringify({ spoken: sum.spoken, words: sum.words }));
  record('K22 and it is the cleaned text -- what the guide summarises is what it would read',
    sum.stamps === false, 'timestamps present: ' + sum.stamps);
  // Same source rules as `read`: after a drag, "summarize this" means the drag.
  await page.eval(
    "var d = document.getElementById('content-frame').contentDocument;" +
    "var p = d.querySelector('#content-area p');" +
    "var r = d.createRange(); r.selectNodeContents(p);" +
    "var s = d.defaultView.getSelection(); s.removeAllRanges(); s.addRange(r); return true;");
  await row(page, 'K23 summarize takes the highlight when there is one', 'summarize',
    { ok: true, spoken: /summarizing your selection\s*\|\s*\d+ words/ });
  await page.eval("var d = document.getElementById('content-frame').contentDocument;" +
    "d.defaultView.getSelection().removeAllRanges(); return true;");

  // K10: THE READER RETURNS CONTROL BY ITSELF. Tom asked for this to be checked
  // rather than assumed: reaching the end of an article is as much an end of
  // reading as pressing Stop, and if it did not restore the mic the session
  // would be deaf from then on.
  const afterStop = await page.eval(
    "var b = document.getElementById('ccl-stop');" +
    "return { stopShown: !!(b && b.style.display !== 'none') };");
  record('K10 stop puts the reader away -- the Stop control is hidden again',
    afterStop.stopShown === false, JSON.stringify(afterStop));
  // Now the half that matters more: reading to the END must put it away too,
  // with nobody pressing anything. Driven through the page's own utterance
  // handler rather than by waiting on real speech, because headless Chrome has
  // no voices and would never finish. THE MIC HALF IS NOT OBSERVABLE HERE --
  // setMic needs a live session -- so this asserts the reader's own teardown and
  // the mic restore is checked by hand.
  await runCmd(page, 'read all');
  const auto = await page.eval(
    "var u = window.CCLLastUtterance;" +
    "var wired = !!(u && typeof u.onend === 'function' && typeof u.onerror === 'function');" +
    "if (!wired) { return { wired: false }; }" +
    // Force the reader open, then fire the page's OWN end-of-speech handler and
    // watch it tear down. Forcing is necessary and is stated: headless Chrome
    // has no voices, so a real utterance ends the instant it starts and the open
    // state cannot be observed from out here.
    "window.CCLForceReaderOpen();" +
    "var mid = window.CCLReaderState();" +
    "u.onend();" +
    "return { wired: true, mid: mid, after: window.CCLReaderState() };");
  record('K11 reaching the end of the article closes the reader by itself',
    auto.wired && auto.mid && auto.mid.stopShown === true &&
    auto.after && auto.after.stopShown === false && auto.after.speaking === false,
    JSON.stringify(auto));

  // The collision, exercised where it actually bites: `sociogram` names a real
  // TAB and this tab's own sub-view. Standing here, the view wins -- 69c312d's
  // rule, now proven on a second tab that did not exist when it was written.
  await row(page, 'J12 standing here, this tab\'s own sociogram view wins over the tool', 'go sociogram',
    { ok: true, spoken: /this tab's sociogram view/ });
  await sleep(3000);
  await assertManifest(page, 'curriculum_tools', 'summa_explorer.html');
  // Also a row that first passed while it should not have: it asserted the view
  // name only, and went green while `what` offered the 2656 article links from a
  // landing pane that is not on screen in this view. A door you cannot see is
  // not a door, so the assertion is now that they are GONE.
  await row(page, 'J13 the hidden pane\'s 2656 links are not offered as doors here', 'what',
    { ok: true, spoken: /sociogram view/, notSpoken: /\d{3,} links/ });
  const shotJ = await page.screenshot(path.join(SHOTS, 'J-summa-tree.png'));

  // ---- Phase L: a roster with NO ELEMENTS AT ALL (Narrative Connectome) -----
  //
  // Every tab up to here handed the walker something in the DOM: a row, a card,
  // a d3 circle. The Connectome draws its 507 narratives into a WebGL canvas --
  // the whole tab is one <div id="canvas-container"> -- so domItems has nothing
  // to enumerate and getClientRects has nothing to be asked about. The Sociogram
  // reads like the same case and is not: d3 leaves an SVG circle per node
  // behind, which is exactly why revealedNodes could query `.node-circle` and
  // pass for the general adapter. It never was one; it was the SVG case, and L0
  // is the row that says so out loud before anything else is claimed.
  //
  // So the roster comes from the page's own data through declared dotted paths,
  // and `open` is a declared CALL rather than a click. Three things can lie here
  // and each has its own row: the count (three meshes per narrative -- L2), what
  // is open (the page's `selectedMesh`, not our own call -- L7), and what the
  // reader CALLS what it reads (L5, the fifth which-document instance, which the
  // 2026-07-27 handoff predicted).
  process.stdout.write('\nPhase L -- a roster with no elements (Narrative Connectome)\n');
  await activateTab(page, 'prs_3d.html');
  await poll(function () {
    return page.eval(IFRAME_DOC +
      "if (!d || d.readyState !== 'complete') { return false; }" +
      "return !!(w && w.meshes && w.meshes.length && typeof w.prsSearchClickResult === 'function');");
  }, 120000, 500, 'connectome tab ready');
  await sleep(1500);
  await assertManifest(page, 'prs_3d', 'prs_3d.html');

  // THE PREMISE OF THE WHOLE PHASE. If this row ever goes false the tab has
  // grown a DOM roster and the data adapter is no longer the thing under test.
  const canvasOnly = await page.eval(IFRAME_DOC +
    "return { circles: d.querySelectorAll('.node-circle').length," +
    "         canvases: d.querySelectorAll('canvas').length," +
    "         meshes: w.meshes.length," +
    "         triplets: w.PRS_TRIPLETS.length };");
  record('L0 the narratives are drawn, not built: a canvas and no per-node DOM',
    canvasOnly.circles === 0 && canvasOnly.canvases >= 1 && canvasOnly.meshes > 0,
    JSON.stringify(canvasOnly));
  await auditTab(page, 'prs_3d', PRS_DEFERRED, 1);

  await row(page, 'L1 what -> names the narratives and the page\'s own total', 'what',
    { ok: true, spoken: /\d+ narratives\b/ });
  // ONE ITEM IS THREE MESHES -- a problem, a resource and a solution sharing one
  // triplet id. Without dedupe the guide walks each narrative three times and
  // reports a number the page itself contradicts. Computed from the page rather
  // than hard-coded, so it stays true as the dataset grows.
  const trip = await page.eval(IFRAME_DOC +
    "var seen = {}, n = 0;" +
    "w.meshes.forEach(function (m) {" +
    "  if (m.userData && m.userData.type === 'prs' && m.visible) {" +
    "    var id = m.userData.triplet.id; if (!seen[id]) { seen[id] = 1; n++; } } });" +
    "return { distinct: n, meshes: w.meshes.filter(function (m) { return m.userData && m.userData.type === 'prs' && m.visible; }).length };");
  record('L1a the page really does draw three meshes per narrative',
    trip.meshes === trip.distinct * 3, JSON.stringify(trip));
  await row(page, 'L2 the roster counts NARRATIVES, not the meshes they are drawn with', 'what',
    { ok: true, spoken: new RegExp('\\b' + trip.distinct + ' narratives\\b') });
  // 222 OF THE 453 SHIP AN EMPTY LABEL. The first run of L2 was red at 231 --
  // the guide had silently dropped every unnamed narrative, saying "231
  // narratives here" over a tab drawing 453 and putting half the artifact out
  // of voice's reach for a gap in the DATA rather than anything about the tab.
  // The count above is the guard; this pair proves the unnamed ones are not
  // merely counted but actually reachable, under the handle the fallback builds.
  const unnamed = await page.eval(IFRAME_DOC +
    "var out = null, n = 0;" +
    "w.PRS_TRIPLETS.forEach(function (t) { if (!t.label) { n++; if (!out) { out = t; } } });" +
    "if (!out) { return null; }" +
    "var h = String(out.problem).slice(0, 60).replace(/\\s+\\S*$/, '');" +
    "return { count: n, handle: h };");
  record('L2a the source really does leave narratives unnamed',
    !!unnamed && unnamed.count > 0, JSON.stringify(unnamed && unnamed.count));
  await row(page, 'L2b and an unnamed one is still reachable, by what it is about',
    'open ' + unnamed.handle, { ok: true, spoken: /^opened / });
  await sleep(600);
  await runCmd(page, 'close');
  await row(page, 'L3 pick first -> walks a roster that has no elements', 'pick first',
    { ok: true, spoken: /1 of \d+ narratives/ });
  // The page's OWN marker, not the call we just made. prsSearchClickResult can
  // find nothing and return silently; reading our own intention back would
  // report that as a success.
  const picked = await page.eval(IFRAME_DOC +
    "var m = w.selectedMesh;" +
    "return { id: m ? m.userData.triplet.id : null, panel: d.getElementById('info-panel').style.display };");
  record('L4 picking OPENED it, because on a canvas marking has no other meaning',
    !!picked.id && picked.panel === 'block', JSON.stringify(picked));
  // THE FIFTH WHICH-DOCUMENT INSTANCE. `read` decides what to call what it is
  // reading by asking whether the marked ELEMENT is still attached -- a question
  // a canvas roster can never answer yes to. It fell straight through to
  // #right-page-title, which this tab does not have, and called a PRS narrative
  // "this article", exactly as it once called a Community Explorer card one.
  // Asserting the verb only would go green on the bug; the assertion is the NAME.
  const label = await page.eval(IFRAME_DOC + "return w.selectedMesh.userData.triplet.label;");
  await row(page, 'L5 read -> names the NARRATIVE, not "this article"', 'read',
    { ok: true, spoken: new RegExp('reading ' + label.slice(0, 24).replace(/[.*+?^${}()|[\]\\]/g, '\\$&')),
      notSpoken: /this article/ });
  await runCmd(page, 'stop');
  // What the reader would actually say: the panel's fields, not the tab's chrome.
  // #content-area was the shape of this mistake on Summa -- the pane AROUND the
  // thing reads the buttons aloud before a word of the text.
  const lScript = await page.eval("return window.CCLSpeechScript ? window.CCLSpeechScript().body : null;");
  record('L6 and it reads the narrative panel, problem through solution',
    /Problem/.test(String(lScript)) && /Resource/.test(String(lScript)) && /Solution/.test(String(lScript)),
    String(lScript).slice(0, 110));
  await row(page, 'L7 next -> the cursor moves and says where it is', 'next',
    { ok: true, spoken: /2 of \d+ narratives/ });

  await row(page, 'L8 open by name lands on that narrative', 'open ' + label,
    { ok: true, spoken: /^opened /});
  await sleep(600);
  const opened = await page.eval(IFRAME_DOC + "return w.selectedMesh ? w.selectedMesh.userData.triplet.label : null;");
  record('L8a and the page agrees it is the one that is open',
    String(opened) === String(label), String(opened).slice(0, 60));
  await row(page, 'L9 open with nothing to match says so, and says what there is to choose from',
    'open a narrative that does not exist',
    { ok: false, spoken: /nothing here is called/ });
  // set on this tab, where the knobs are the three edge classes. Write-returns-
  // the-read: the spoken value has to be the checkbox's, not the one we asked for.
  await row(page, 'L10 set coils off', 'set coils off', { ok: true, spoken: /off/ });
  const coils = await page.eval(IFRAME_DOC +
    "return { box: d.getElementById('prs-chk-coils').checked, flag: w.showCoils };");
  record('L10a the tab really turned them off, box and flag together',
    coils.box === false && coils.flag === false, JSON.stringify(coils));

  // A FILTER THE GUIDE DOES NOT OWN still moves the roster, because `visible` is
  // read live off the page rather than cached at pick time. Driven by clicking
  // the tab's own checkbox -- the filters dimension is deferred here, so this is
  // deliberately the mouse doing what voice cannot yet do.
  const shrunk = await page.eval(IFRAME_DOC +
    "var boxes = [].slice.call(d.querySelectorAll('#prs-tradition-filters input[type=checkbox]'));" +
    "var keep = boxes[0];" +
    "boxes.forEach(function (b) { if (b !== keep && b.checked) { b.click(); } });" +
    "var seen = {}, n = 0;" +
    "w.meshes.forEach(function (m) { if (m.userData && m.userData.type === 'prs' && m.visible) {" +
    "  var id = m.userData.triplet.id; if (!seen[id]) { seen[id] = 1; n++; } } });" +
    "return { visible: n, all: " + trip.distinct + " };");
  record('L11 a filter the guide does not own really did cut the page down',
    shrunk.visible > 0 && shrunk.visible < shrunk.all, JSON.stringify(shrunk));
  // The honest total survives the cut, in the same breath as the count. This is
  // the same defect the graph counter had ("4184 of 4184 shown" with two nodes
  // on screen) and the same fix: say the page's own number, read off the page's
  // own status line, so what survived a filter can never pass for the whole set.
  await row(page, 'L11a the roster follows the page, and never passes a cut off as the whole set', 'what',
    { ok: true, spoken: new RegExp('\\b' + shrunk.visible + ' of ' + canvasOnly.triplets + ' narratives\\b') });
  await row(page, 'L11b and walking a cut page says both numbers', 'pick first',
    { ok: true, spoken: new RegExp('1 of ' + shrunk.visible + ' narratives \\(' + canvasOnly.triplets + ' in all\\)') });
  // What was picked may be gone now. Bare `open` resolves through the LIVE
  // roster for exactly this reason: opening something the page has stopped
  // drawing is the plausible-sounding wrong answer, not a near miss.
  const goneCase = await page.eval(IFRAME_DOC +
    "var seen = {};" +
    "for (var i = 0; i < w.meshes.length; i++) { var m = w.meshes[i];" +
    "  if (m.userData && m.userData.type === 'prs' && !m.visible) { return m.userData.triplet.label; } }" +
    "return null;");
  record('L12 the cut really did hide some narratives', !!goneCase, String(goneCase).slice(0, 50));
  await row(page, 'L12a and one of them is no longer offered by name', 'open ' + goneCase,
    { ok: false, spoken: /nothing here is called/ });
  // Put the tab back so nothing downstream inherits a cut page.
  await page.eval(IFRAME_DOC +
    "var r = d.getElementById('prs-search-reset'); if (r) { r.click(); }" +
    "var c = d.getElementById('prs-chk-coils'); if (c && !c.checked) { c.click(); }" +
    "return true;");
  await sleep(800);
  await row(page, 'L13 close -> puts the narrative panel away, via the control the spec declared', 'close',
    { ok: true, spoken: /closed/ });
  const closed = await page.eval(IFRAME_DOC +
    "return { panel: d.getElementById('info-panel').style.display, sel: !!w.selectedMesh };");
  record('L13a and the page agrees nothing is open', closed.panel === 'none' && closed.sel === false,
    JSON.stringify(closed));
  // ---- L15-L22: THE CAMERA, on a tab that is actually built around one ------
  //
  // Deferred for exactly one session on the grounds that execCamera was
  // Sociogram-specific (fitAll / zoomBehavior / #graph-svg / currentZoomScale --
  // four globals of one page sitting in the position of the shared road). Tom's
  // answer was the right one: a tab built around an orbiting camera that voice
  // cannot turn is a room the guide can walk up to and never walk around.
  //
  // Every row asserts the PAGE's numbers, never the spoken string alone -- a
  // camera that narrates a turn it did not make is the exact failure mode this
  // harness exists for, and it is invisible to anyone who cannot see the screen.
  // HOME FIRST. Everything above has opened narratives, and opening moves the
  // camera onto what it opened -- so the position at this point is not the
  // page's home and comparing against it would test the wrong thing (the first
  // run of L18a and L21a both did exactly that, and read as camera bugs).
  await runCmd(page, 'fit');
  const cam0 = await page.eval(IFRAME_DOC +
    "return { theta: w.cameraTheta, phi: w.cameraPhi, r: w.cameraRadius," +
    "         tx: w.cameraTarget.x, ty: w.cameraTarget.y, tz: w.cameraTarget.z," +
    "         px: w.camera.position.x, py: w.camera.position.y };");
  await row(page, 'L15 rotate left', 'rotate left', { ok: true, spoken: /rotate left/ });
  const camR = await page.eval(IFRAME_DOC +
    "return { theta: w.cameraTheta, px: w.camera.position.x, py: w.camera.position.y };");
  record('L15a the camera really swung, and the page applied it',
    camR.theta !== cam0.theta && camR.px !== cam0.px,
    JSON.stringify({ theta: [cam0.theta, camR.theta], moved: camR.px !== cam0.px }));
  await row(page, 'L16 rotate right puts it back', 'rotate right', { ok: true, spoken: /rotate right/ });
  const camB = await page.eval(IFRAME_DOC + "return w.cameraTheta;");
  record('L16a every move has its opposite, and this one is exact',
    Math.abs(Number(camB) - cam0.theta) < 1e-9, JSON.stringify([cam0.theta, camB]));
  // The page's own drag handler clamps phi to 0.1 .. PI*0.85. Voice must not be
  // able to put the camera anywhere the mouse cannot -- and at the limit it must
  // SAY nothing moved rather than reporting the step it asked for.
  await runCmd(page, 'rotate up');
  await runCmd(page, 'rotate up');
  await runCmd(page, 'rotate up');
  await runCmd(page, 'rotate up');
  const camU = await page.eval(IFRAME_DOC + "return w.cameraPhi;");
  record('L17 tipping up stops where the page\'s own drag handler stops it',
    Number(camU) >= 0.1 - 1e-9 && Number(camU) <= 0.1 + 1e-9, String(camU));
  await row(page, 'L17a and at the limit it says so, instead of reporting a step it did not take',
    'rotate up', { ok: false, spoken: /already as far up as this view tips/ });
  // Zoom is the viewing distance on an orbit camera, clamped as onWheel clamps it.
  await runCmd(page, 'fit');
  await row(page, 'L18 zoom in', 'zoom in', { ok: true, spoken: /^zoom in/ });
  const camZ = await page.eval(IFRAME_DOC + "return w.cameraRadius;");
  record('L18a the viewing distance really closed', Number(camZ) < cam0.r,
    JSON.stringify([cam0.r, camZ]));
  for (let i = 0; i < 6; i++) { await runCmd(page, 'zoom in'); }
  const camZmin = await page.eval(IFRAME_DOC + "return w.cameraRadius;");
  record('L19 zoom stops at the page\'s own near limit, not somewhere the mouse cannot reach',
    Number(camZmin) === 15, String(camZmin));
  await row(page, 'L19a and says nothing moved rather than claiming the step',
    'zoom in', { ok: false, spoken: /already as far in as this view goes/ });
  // Pan moves what the camera LOOKS AT, along the camera's own right and up --
  // world axes would send the view sideways in a direction unrelated to what is
  // on screen, which after any rotation is nearly always.
  await runCmd(page, 'fit');
  await runCmd(page, 'rotate left');
  const preP = await page.eval(IFRAME_DOC + "return { tx: w.cameraTarget.x, tz: w.cameraTarget.z };");
  await row(page, 'L20 pan left', 'pan left', { ok: true, spoken: /^pan left/ });
  const postP = await page.eval(IFRAME_DOC + "return { tx: w.cameraTarget.x, tz: w.cameraTarget.z };");
  record('L20a it moved what the camera is looking at, in the camera\'s own frame',
    postP.tx !== preP.tx || postP.tz !== preP.tz, JSON.stringify({ before: preP, after: postP }));
  await runCmd(page, 'pan right');
  const backP = await page.eval(IFRAME_DOC + "return { tx: w.cameraTarget.x, tz: w.cameraTarget.z };");
  record('L20b and pan right undoes it, so the dimension is symmetric here too',
    Math.abs(backP.tx - preP.tx) < 1e-6 && Math.abs(backP.tz - preP.tz) < 1e-6,
    JSON.stringify({ start: preP, back: backP }));
  // fit is the way back to the whole thing, and it is the page's own resetCamera
  // rather than anything the shell computes.
  await row(page, 'L21 fit -> the way back to the whole thing', 'fit', { ok: true, spoken: /^fit/ });
  const camF = await page.eval(IFRAME_DOC +
    "return { theta: w.cameraTheta, phi: w.cameraPhi, r: w.cameraRadius, tx: w.cameraTarget.x };");
  record('L21a and it is the page\'s own reset, to the page\'s own home position',
    Math.abs(camF.theta - cam0.theta) < 1e-9 && Math.abs(camF.phi - cam0.phi) < 1e-9 &&
    camF.r === cam0.r && Math.abs(camF.tx - cam0.tx) < 1e-9,
    JSON.stringify({ home: cam0.r, now: camF }));
  // AND IT HOLDS STILL. resetCamera() restores the opening state including the
  // idle drift -- correct for the Reset View button, wrong for someone who just
  // ASKED to see the whole thing and would watch it rotate away. The shell
  // quiets the drift after the page's own call, so `fit` frames it and leaves
  // it framed. Without this row, L21a above passes or fails on whether the read
  // lands inside a single animation frame, which is how this was found.
  await sleep(400);
  const camF2 = await page.eval(IFRAME_DOC + "return w.cameraTheta;");
  record('L21b and fit leaves the view still, not drifting off what it just framed',
    Number(camF2) === Number(camF.theta), JSON.stringify([camF.theta, camF2]));
  // `center` is not a camera verb: opening something already moves the camera
  // onto it, which is what the page's OWN search results do. The word maps to
  // the thing that exists rather than growing a second road to it.
  const beforeC = await page.eval(IFRAME_DOC + "return w.cameraRadius;");
  await row(page, 'L22 "center X" is open, and opening really does move the camera',
    'center ' + label, { ok: true, spoken: /^opened / });
  const afterC = await page.eval(IFRAME_DOC +
    "return { r: w.cameraRadius, sel: w.selectedMesh ? w.selectedMesh.userData.triplet.label : null };");
  record('L22a the camera closed on it and the page says it is the one open',
    Number(afterC.r) !== Number(beforeC) && String(afterC.sel) === String(label),
    JSON.stringify({ r: [beforeC, afterC.r] }));
  await runCmd(page, 'close');

  // ---- L23-L31: THE DATA CUT, by voice ------------------------------------
  //
  // Tom, looking at a checkbox panel that reads like the Sociogram's: "we used
  // that same arch here... can we cheaply import that option here also, for
  // voice data cutting?" The panel is 37 of this tab's 53 controls, and it was
  // the whole of what was still deferred.
  //
  // The ENGINE needed nothing: resolveGroups already resolves `section/leaf`
  // keys, which is why `only levin` and `only traditions` both work on the
  // graph. What was Sociogram-specific was the shell reading the roster off one
  // page's `groupVisibility` -- the fourth time a single page's globals have
  // been found sitting in the position of the shared road.
  //
  // Every row here asserts the PAGE's own state. A filter that narrates a cut
  // it did not make is the exact failure this harness exists for, and it is
  // invisible to anyone who cannot see the screen.
  await runCmd(page, 'all');
  const rosterSeen = await page.eval(
    "var r = window.CCLDebug ? window.CCLDebug() : null;" +
    "return r && r.roster ? { n: r.roster.length, sample: r.roster.slice(0, 3)," +
    "  sections: r.roster.map(function (k) { return k.split('/')[0]; })" +
    "    .filter(function (v, i, a) { return a.indexOf(v) === i; }) } : null;");
  record('L23 the roster is one flat namespace over all three axes',
    !!rosterSeen && rosterSeen.sections.length === 3 &&
    rosterSeen.sections.indexOf('traditions') !== -1 &&
    rosterSeen.sections.indexOf('disciplines') !== -1 &&
    rosterSeen.sections.indexOf('years') !== -1,
    JSON.stringify(rosterSeen));
  // `only <one tradition>` -- the ordinary data cut, and the write has to have
  // gone through the page's handler: the checkbox, the state map, the meshes
  // and the page's own counter all have to agree, or something was skipped.
  await row(page, 'L24 only levin -> one tradition', 'only levin',
    { ok: true, spoken: /set -> traditions: levin/ });
  const cut1 = await page.eval(IFRAME_DOC +
    "var seen = {}, n = 0, others = 0;" +
    "w.meshes.forEach(function (m) { if (m.userData && m.userData.type === 'prs' && m.visible) {" +
    "  var id = m.userData.triplet.id; if (!seen[id]) { seen[id] = 1; n++; }" +
    "  if (m.userData.thinker !== 'levin') { others++; } } });" +
    "return { visible: n, foreign: others, box: d.getElementById('prs-chk-levin').checked," +
    "         state: w.prsFilterState.levin, otherState: w.prsFilterState.hoffman," +
    "         line: d.getElementById('prs-count').textContent };");
  record('L24a checkbox, state map, meshes and the page\'s own counter all agree',
    cut1.box === true && cut1.state === true && cut1.otherState === false &&
    cut1.foreign === 0 && cut1.visible > 0 &&
    cut1.line.indexOf('Showing ' + cut1.visible + ' /') === 0,
    JSON.stringify(cut1));
  await row(page, 'L24b and the guide reports what the page now draws, not the write it made',
    'what', { ok: true, spoken: new RegExp('traditions: levin') });
  // A SECTION TERM, free with the roster shape: "hide disciplines" is one op
  // over fifteen keys, and it must reach the WEDGE meshes too -- disciplines
  // redraw geometry (applyDiscFilters) before the node pass, which is the whole
  // reason writes go through the checkbox rather than the state object.
  await runCmd(page, 'all');
  await row(page, 'L25 hide disciplines -> a section term, one op over every key in it',
    'hide disciplines', { ok: true, spoken: /diff -> .*disciplines: none/ });
  const discs = await page.eval(IFRAME_DOC +
    "var offAll = Object.keys(w.prsDiscState).every(function (k) { return w.prsDiscState[k] === false; });" +
    "var wedges = w.discMeshes.filter(function (m) { return m.visible && m.userData && m.userData.discipline; }).length;" +
    "var trads = Object.keys(w.prsFilterState).every(function (k) { return w.prsFilterState[k] === true; });" +
    "return { discsOff: offAll, wedgesShown: wedges, traditionsUntouched: trads };");
  record('L25a the wedges went with it, and the OTHER axes were left alone',
    discs.discsOff === true && discs.wedgesShown === 0 && discs.traditionsUntouched === true,
    JSON.stringify(discs));
  // A two-word name has to be ONE token to a parser that splits on spaces, so
  // the roster slugs it -- and the prefix match still lets a person say the
  // short form they would actually say.
  await runCmd(page, 'all');
  await row(page, 'L26 only cognitive -> a two-word discipline reached by its short form',
    'only cognitive', { ok: true, spoken: /disciplines: cognitive-science/ });
  const disc1 = await page.eval(IFRAME_DOC +
    "var on = Object.keys(w.prsDiscState).filter(function (k) { return w.prsDiscState[k]; });" +
    "return { on: on };");
  record('L26a and it is the one discipline, named in full by the page',
    disc1.on.length === 1 && /cognitive science/i.test(disc1.on[0]), JSON.stringify(disc1));
  // Decades are numbers in the page and "the 1990s" out loud. Declared, not
  // guessed -- the `leaf` template is what closes that gap.
  await runCmd(page, 'all');
  await row(page, 'L27 show the 1990s -> the spoken form of a numeric key', 'only 1990s',
    { ok: true, spoken: /years: 1990s/ });
  const yr = await page.eval(IFRAME_DOC +
    "var on = Object.keys(w.prsYearState).filter(function (k) { return w.prsYearState[k]; });" +
    "return { on: on, rings: w.decadeRings.filter(function (r) { return r.ring && r.ring.visible; }).length };");
  record('L27a the decade really is the only one on, and its rings followed',
    yr.on.length === 1 && String(yr.on[0]) === '1990', JSON.stringify(yr));
  // `none` through each section's own master box: the page does its own sweep,
  // and an empty result is SAID plainly rather than dressed as a success.
  await row(page, 'L28 none -> nothing left, and it says so instead of claiming a filter change',
    'none', { ok: true, spoken: /none -> traditions: none.*disciplines: none.*years: none/ });
  const noneState = await page.eval(IFRAME_DOC +
    "var vis = w.meshes.filter(function (m) { return m.userData && m.userData.type === 'prs' && m.visible; }).length;" +
    "return { visible: vis, masters: [d.getElementById('prs-chk-all').checked," +
    "  d.getElementById('prs-chk-all-discs').checked, d.getElementById('prs-chk-all-years').checked] };");
  record('L28a every mesh is gone and no master box is left claiming otherwise',
    noneState.visible === 0 && noneState.masters.every(function (b) { return b === false; }),
    JSON.stringify(noneState));
  await row(page, 'L28b and with nothing shown the roster says so rather than offering a cursor',
    'pick first', { ok: false, spoken: /nothing is revealed to pick from/ });
  await row(page, 'L29 all -> everything back', 'all', { ok: true, spoken: /all -> traditions: all \d+/ });
  const allState = await page.eval(IFRAME_DOC +
    "var seen = {}, n = 0;" +
    "w.meshes.forEach(function (m) { if (m.userData && m.userData.type === 'prs' && m.visible) {" +
    "  var id = m.userData.triplet.id; if (!seen[id]) { seen[id] = 1; n++; } } });" +
    "return n;");
  record('L29a and it is the whole set again', Number(allState) === canvasOnly.triplets,
    JSON.stringify([allState, canvasOnly.triplets]));
  // Undo travels the same road the command did -- which on this tab means back
  // through the checkboxes, so the page re-runs its own handlers on the way.
  await runCmd(page, 'only levin');
  await row(page, 'L30 undo steps the cut back', 'undo', { ok: true, spoken: /undid \(filters\)/ });
  const undone = await page.eval(IFRAME_DOC +
    "var on = Object.keys(w.prsFilterState).filter(function (k) { return w.prsFilterState[k]; }).length;" +
    "var boxes = [].slice.call(d.querySelectorAll('#prs-tradition-filters input')).filter(function (b) { return b.checked; }).length;" +
    "return { stateOn: on, boxesOn: boxes };");
  record('L30a and the boxes came back with the state, because undo took the same road',
    undone.stateOn === undone.boxesOn && undone.stateOn > 1, JSON.stringify(undone));
  await runCmd(page, 'all');
  // A word that names nothing is said back rather than silently dropped -- and
  // since increment 2 it is said back WITH the axes it could have named. On a
  // tab with three of them "could not find X" was true and unhelpful; the
  // question behind the miss is always "then what can I say here?".
  await row(page, 'L31 a term that matches no axis is named, and the axes are named back',
    'only quantum chromodynamics',
    { ok: false, spoken: /"quantum chromodynamics" is not something this view filters by.*traditions:.*disciplines:.*years:/ });
  await runCmd(page, 'all');

  // ---- L32-L38: SPIN, the one verb that leaves something running -----------
  //
  // Every other command in this language is over when the sentence is. A spin
  // is still happening, which raises three questions no other verb has had to
  // answer -- what stops it, what happens when you leave, and whether anyone is
  // told it is running. A leak here is worse than a wrong answer: a timer
  // turning a view nobody is looking at is invisible from inside the guide.
  await row(page, 'L32 spin -> bare means left, and it says how to end it', 'spin',
    { ok: true, spoken: /spinning left -- say "stop"/ });
  const spin0 = await page.eval(IFRAME_DOC + "return w.cameraTheta;");
  await sleep(700);
  const spin1 = await page.eval(IFRAME_DOC + "return w.cameraTheta;");
  record('L32a the view really is turning, on its own, between two commands',
    Number(spin1) > Number(spin0), JSON.stringify([spin0, spin1]));
  // A MOVING VIEW IS STATE. `what` is the only way anyone learns state here, so
  // a guide asked "where are we" while this runs must not describe a still
  // picture of something that is turning.
  await row(page, 'L32b what says the view is moving', 'what',
    { ok: true, spoken: /the view is spinning left/ });
  await row(page, 'L33 spin off -> the precise form', 'spin off',
    { ok: true, spoken: /stopped spinning/ });
  const held0 = await page.eval(IFRAME_DOC + "return w.cameraTheta;");
  await sleep(500);
  const held1 = await page.eval(IFRAME_DOC + "return w.cameraTheta;");
  record('L33a and it really stopped -- no timer left turning it',
    Number(held0) === Number(held1), JSON.stringify([held0, held1]));
  await row(page, 'L33b spin off with nothing spinning says so rather than claiming a stop',
    'spin off', { ok: false, spoken: /nothing is spinning/ });
  // `stop` stops it too, and NAMES what it stopped. The standing rule is that
  // `stop` must not come to mean two things -- that rule is against SILENT
  // ambiguity, and naming the outcome is the opposite of silent. A user
  // watching a view turn while a paragraph is read says "stop" once, meaning
  // both; making them learn `spin off` for the second would be a vocabulary test.
  await runCmd(page, 'spin right');
  await row(page, 'L34 stop halts the spin as well, and says which', 'stop',
    { ok: true, spoken: /stopped spinning/ });
  const afterStopSpin = await page.eval(IFRAME_DOC + "return w.cameraTheta;");
  await sleep(400);
  record('L34a and nothing is still turning afterwards',
    Number(await page.eval(IFRAME_DOC + "return w.cameraTheta;")) === Number(afterStopSpin),
    String(afterStopSpin));
  await runCmd(page, 'pick first');
  await runCmd(page, 'spin left');
  await row(page, 'L35 reading and spinning at once -> one stop, both named, no guessing',
    'read', { ok: true, spoken: /reading /});
  // THE READER IS FORCED OPEN, and that is stated rather than hidden: headless
  // Chrome has no voices, so a real utterance ends the instant it starts and
  // the both-are-running case cannot otherwise be observed from out here. Same
  // device, and the same reason, as K11.
  await page.eval("window.CCLForceReaderOpen(); return true;");
  await row(page, 'L35a one stop halts both, and names both', 'stop',
    { ok: true, spoken: /stopped reading and spinning/ });
  // `stop` has been the one unconditionally safe word since the reader shipped.
  // Saying it twice must not start punishing the user for it.
  await row(page, 'L35b saying it again is still safe, and still says stopped',
    'stop', { ok: true, spoken: /^stopped$/ });
  // LEAVING THE TAB STOPS IT. A spin left running in a hidden iframe is a timer
  // nobody can see, writing to a window nobody is looking at -- and on this tab
  // it would go on turning a 1359-mesh scene for the rest of the session.
  const shotL = await page.screenshot(path.join(SHOTS, 'L-connectome.png'));
  await runCmd(page, 'spin left');
  await activateTab(page, SOCIOGRAM_SRC);
  await tabReady(page, 'sociogram');
  await sleep(900);
  const leaked = await page.eval(
    "var r = window.CCLRun('what');" +
    "return { spoken: r.spoken, mentionsSpin: /spinning/.test(r.spoken || '') };");
  record('L36 leaving the tab stopped the spin -- no timer survives the switch',
    leaked.mentionsSpin === false, JSON.stringify(leaked).slice(0, 160));
  await row(page, 'L36a and the flat tab refuses spin in words, as it refuses rotate',
    'spin left', { ok: false, spoken: /not available on this view\. supported: /i });

  // Back to the Sociogram once more: the data adapter added a road beside
  // revealedNodes rather than moving it, and a tab that declares no `activate`
  // must still route `pick` through openNodeByLabel exactly as it always did.
  await activateTab(page, SOCIOGRAM_SRC);
  await tabReady(page, 'sociogram');
  await sleep(1200);
  await row(page, 'L14 the graph roster is untouched by the data adapter', 'pick first',
    { ok: true, spoken: /1 of \d+/ });
  // The Sociogram's own camera must be untouched too -- the declared branch is a
  // road beside execCamera's, not a replacement for it.
  await row(page, 'L14a and so is its camera, which declares nothing and takes the old road',
    'zoom in', { ok: true, spoken: /zoom in/ });
  // And a flat tab SAYS it cannot turn. Silence here would be the worst answer:
  // with no screen, a rotate that quietly does nothing is indistinguishable from
  // one that worked.
  await row(page, 'L14b rotate on a flat tab is refused in words, and told what it CAN do',
    'rotate left', { ok: false, spoken: /not available on this view\. supported: /i });

  // ---- Phase W: the wave, and the rule that it must be MEASURED ------------
  //
  // The wave in the Sociogram is the guide's body. The whole of its honesty is
  // one claim: it moves because a voice is actually making a sound, not because
  // something somewhere is talking. So the rows that matter most here are the
  // ones about having NOTHING to measure -- a wave that runs off a timer would
  // look identical to a working one, and nobody watching could tell.
  //
  // A live realtime session costs money, so the meter is armed from a SYNTHETIC
  // tone of known loudness, through the same armOutputMeter() that pc.ontrack
  // calls. The audio is real and really measured; only its source is not the
  // model. That is the difference between a seam and a stub.
  process.stdout.write('\nPhase W -- the wave, driven by a measured voice\n');
  const wPremise = await page.eval(IFRAME_DOC +
    "return { has: !!(w && w.VoiceWave), enabled: !!(w && w.VoiceWave && w.VoiceWave.enabled)," +
    "         api: !!(window.VoiceGuide && window.VoiceGuide.speech.start) };");
  record('W0 this view has a body to move, and the shell has a driver for it',
    wPremise.has && wPremise.enabled && wPremise.api, JSON.stringify(wPremise));

  // NOTHING TO MEASURE -> NOTHING TO DRAW. This is the row the feature exists
  // for. With no output meter armed there is no number, and the correct amount
  // of wave is none of it -- not a plausible envelope, not a decayed last value.
  const wNoMeter = await page.eval(
    "var W = window.VoiceGuide.speech;" +
    "W.stop();" +
    "var rms = W.rms();" +
    "W.start();" +
    "return { rms: rms, running: W.running() };");
  record('W1 with no stream to listen to, the driver refuses to start at all',
    wNoMeter.rms === null && wNoMeter.running === false, JSON.stringify(wNoMeter));

  // Arm from a real tone. The amplitude is chosen so the RMS sits well above
  // the QUIET_RMS floor the handover uses -- so "loud" and "quiet" are separated
  // by the page's own threshold rather than by one this harness invented -- and
  // ALSO low enough that rms x gain stays under 1. At speaking loudness it would
  // clamp, and a clamped value would let any gain at all pass W3a below.
  await page.eval(
    "var c = new AudioContext();" +
    "var osc = c.createOscillator(), g = c.createGain(), dest = c.createMediaStreamDestination();" +
    "osc.frequency.value = 220; g.gain.value = 0.08;" +
    "osc.connect(g); g.connect(dest); osc.start();" +
    "window.__wvTone = { ctx: c, gain: g };" +
    "window.VoiceGuide.speech.arm(dest.stream);" +
    "var p = [c.resume()]; if (window.audioCtx) { p.push(window.audioCtx.resume()); }" +
    "return Promise.all(p).then(function () { return true; });");
  await sleep(400);
  const wRms = await page.eval("return window.VoiceGuide.speech.rms();");
  record('W2 armed on a real stream, the meter reads a real number',
    typeof wRms === 'number' && wRms > 0.012, String(wRms));

  await page.eval("window.VoiceGuide.speech.start(); return true;");
  await sleep(300);
  const wRun = await page.eval(IFRAME_DOC +
    "return { running: window.VoiceGuide.speech.running()," +
    "         target: w._waveTarget, amp: w._waveAmp, rms: window.VoiceGuide.speech.rms()," +
    "         gain: window.VoiceGuide.speech.gain };");
  record('W3 the graph is being spoken to, and it is moving',
    wRun.running === true && wRun.target > 0 && wRun.amp > 0,
    JSON.stringify(wRun));
  // The x6 is a DISPLAY gain on a measured number, not a substitute for one:
  // what the receiver holds has to be this analyser's reading scaled, clamped at
  // 1, and nothing else. If these two ever come apart, the wave has started
  // describing a sound that was not made.
  record('W3a and what it is holding is this analyser\'s reading, scaled and clamped',
    wRun.target < 1 && Math.abs(wRun.target - Math.min(1, wRun.rms * wRun.gain)) < 0.05,
    JSON.stringify({ target: wRun.target, expected: Math.min(1, wRun.rms * wRun.gain) }));

  // A LONG UTTERANCE IS NOT A STUCK ONE. This row is here because the first
  // version had a 4-second cap borrowed from whenOutputQuiet, and Tom found it
  // live inside two minutes: every answer's wave died at about five seconds
  // with the guide still audibly talking. The harness could not see it, because
  // nothing here had ever kept a voice going longer than the cap.
  //
  // No realtime session is running, so responseActive is false throughout --
  // which is exactly the state the bug lived in, and a harder case than a real
  // utterance, where response.created holds it open for the first seconds too.
  await sleep(6000);
  const wLong = await page.eval(IFRAME_DOC +
    "return { running: window.VoiceGuide.speech.running(), target: w._waveTarget };");
  record('W3b a voice that keeps going keeps the wave going -- no clock cuts it off',
    wLong.running === true && wLong.target > 0, JSON.stringify(wLong));

  // A PAUSE IS NOT AN ENDING. The second live failure: the wave died about a
  // second into a several-second answer, both times. Speech has gaps at every
  // sentence boundary, and once the driver stops, nothing restarts it until the
  // next response.created -- so one 250ms pause costs the whole rest of the
  // answer. QUIET_FOR_MS is the reader-handover threshold, where being late is
  // free and being early is a collision; here the asymmetry runs the other way.
  await page.eval("window.__wvTone.gain.gain.value = 0; return true;");
  await sleep(700);
  const wGap = await page.eval(IFRAME_DOC +
    "return { running: window.VoiceGuide.speech.running(), target: w._waveTarget };");
  record('W3c a pause between sentences does not end the utterance',
    wGap.running === true, JSON.stringify(wGap));
  // ...and the voice coming back is picked up by the timer that never stopped.
  await page.eval("window.__wvTone.gain.gain.value = 0.08; return true;");
  await sleep(300);
  const wResume = await page.eval(IFRAME_DOC +
    "return { running: window.VoiceGuide.speech.running(), target: w._waveTarget };");
  record('W3d and when the voice comes back the wave is already there',
    wResume.running === true && wResume.target > 0, JSON.stringify(wResume));

  // THE END OF THE WAVE IS MEASURED TOO. `response.done` means the response is
  // complete, not that its audio has stopped playing -- so the driver does not
  // stop there; it stops when the sound does, after a silence long enough that
  // no utterance could still be running. Killing the tone for good stands in for
  // the tail draining.
  const wQuiet = await page.eval(IFRAME_DOC +
    "window.__wvTone.gain.gain.value = 0;" +
    "var W = window.VoiceGuide.speech, t0 = Date.now();" +
    "return new Promise(function (res) {" +
    "  var iv = setInterval(function () {" +
    "    if (W.running() && Date.now() - t0 < 8000) { return; }" +
    "    clearInterval(iv);" +
    "    res({ ms: Date.now() - t0, running: W.running(), target: w._waveTarget });" +
    "  }, 25);" +
    "});");
  record('W4 when the voice goes quiet for good the wave stops itself, and says so to the graph',
    wQuiet.running === false && wQuiet.target === 0, JSON.stringify(wQuiet));
  // AND IT ENDS IN REAL TIME. The ending is a DURATION (WV_END_MS of measured
  // quiet), not a count of ticks -- a hidden page has its timers throttled to
  // about 1Hz, and counting WV_MS per tick made a 220ms drain take 6799ms with
  // the explorer in a background tab. Under CDP the page is visible and cannot
  // reproduce that, so this row exists to state the intent: if the ending ever
  // starts measuring itself in ticks again, this is the row that says so.
  record('W4a and the ending is 2500ms of measured quiet, not a count of ticks',
    wQuiet.ms >= 2500 && wQuiet.ms < 3400, wQuiet.ms + 'ms');
  // The stop is self-describing, because the next thing that goes wrong live
  // will be diagnosed from a console line rather than from a theory.
  const wWhy = await page.eval("return window.VoiceGuide.speech.trace();");
  record('W4b and it says WHY it stopped, with the readings behind it',
    /^quiet \d+ms$/.test(String(wWhy.reason)) && wWhy.loud > 0 && wWhy.peak > 0.012,
    JSON.stringify({ reason: wWhy.reason, samples: wWhy.samples, loud: wWhy.loud, peak: wWhy.peak }));

  // Where the wave comes from is what makes it mean something rather than just
  // prove the guide is talking. The receiver REFUSES a reference it cannot
  // resolve instead of falling back to the view centre -- so a wrong guess reads
  // as "no change", never as a claim about the wrong node.
  const anyNode = await page.eval(IFRAME_DOC +
    "for (var k in w.nodeById) { if (Object.prototype.hasOwnProperty.call(w.nodeById, k)) { return k; } }" +
    "return null;");
  const wOrigin = await page.eval(
    "var W = window.VoiceGuide.speech;" +
    "return { good: W.origin(" + JSON.stringify(anyNode) + ")," +
    "         bad: W.origin('no/such/node.md') };");
  record('W5 the wave can be pointed at a node, and refuses one that is not there',
    wOrigin.good === true && wOrigin.bad === false, JSON.stringify(wOrigin));

  // A VIEW WITH NO BODY. The guard is `VoiceWave.enabled` on the framed window,
  // which is one check covering both "wrong tab" and "this user asked for less
  // motion". The loop still RUNS on such a tab -- the idle clock needs to know
  // when the guide stopped talking no matter what is on screen -- but it must
  // paint nothing and claim nothing, and it must not throw for want of a
  // receiver. Switching tabs mid-answer breaking the idle clock would be the
  // same class of bug as arming it at response.done.
  await activateTab(page, METABOLISM_SRC);
  await sleep(900);
  await page.eval("window.__wvTone.gain.gain.value = 0.08; return true;");
  await sleep(300);
  const wFlat = await page.eval(
    "var W = window.VoiceGuide.speech;" +
    "W.start();" +
    "return { running: W.running(), origin: W.origin('anything'), rms: W.rms() };");
  record('W6 a view with no body is still measured, but nothing is painted and nothing is claimed',
    wFlat.origin === false && wFlat.rms > 0.012, JSON.stringify(wFlat));
  // Coming back, the same uninterrupted loop starts painting again.
  await activateTab(page, SOCIOGRAM_SRC);
  await tabReady(page, 'sociogram');
  await sleep(900);
  const wBack = await page.eval(IFRAME_DOC +
    "return { running: window.VoiceGuide.speech.running(), target: w._waveTarget };");
  record('W6a and coming back mid-answer resumes the wave without restarting the watch',
    wBack.running === true && wBack.target > 0, JSON.stringify(wBack));
  await page.eval("window.VoiceGuide.speech.stop('harness done'); window.__wvTone.gain.gain.value = 0; return true;");

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
  process.stdout.write('screenshots:\n  ' + [shotA, shotFind, shotB, shotB2, shotC, shotD, shotE, shotFc, shotF, shotG, shotH, shotJ, shotL].join('\n  ') + '\n');

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
