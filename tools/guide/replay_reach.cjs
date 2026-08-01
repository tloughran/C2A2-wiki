#!/usr/bin/env node
/**
 * Execute every plate's `reach` in a real browser, and fail when one does not land.
 *
 * check_coverage.py asserts the routes STATICALLY -- that the selectors and tab ids named
 * in the manifest still exist in explorer.html and start_here.html. That is necessary and
 * not sufficient: earlier this session eleven plates carried
 * `a.launch[data-target='review-cards']`, which exists as two true substrings and matches
 * no element, and the static gate was green. Only a browser can tell you a recipe arrives.
 *
 * Deliberately NOT a new harness. scripts/test_voice_shell.cjs already serves the wiki,
 * drives a real Chrome over raw CDP with no dependencies, and exports its plumbing behind
 * a `require.main === module` guard, so this file borrows it and adds nothing to it. That
 * also means reach steps can be CCL COMMANDS -- `go cards`, `pick first` -- and not just
 * selectors: commands are the app's own declared vocabulary, policed by the coverage audit,
 * so a command that stops working fails loudly where a dead selector fails silently.
 *
 * Distinct reaches are replayed once each, not once per plate: 110 plates currently share
 * 20 routes, and replaying the same route 110 times would buy nothing but wall-clock.
 *
 *   node tools/guide/replay_reach.cjs [--port 8080] [--cdp 9222] [--only <slug-prefix>]
 */
const fs = require('fs');
const path = require('path');

const HERE = __dirname;
const REPO = path.resolve(HERE, '../..');
const H = require(path.join(REPO, 'scripts/test_voice_shell.cjs'));

function arg(name, dflt) {
  const i = process.argv.indexOf('--' + name);
  return i > -1 && process.argv[i + 1] ? process.argv[i + 1] : dflt;
}
const ONLY = arg('only', null);
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

/** The frame src a reach is supposed to end on. */
function expectedSrc(reach, chapterSrc) {
  let src = null;
  for (const step of reach) {
    if (step.chapter && chapterSrc[step.chapter]) src = chapterSrc[step.chapter];
    if (step.tab) src = step.tab;
    if (step.loads) src = step.loads;
  }
  return src;
}

function chapterSources(explorerHtml) {
  const map = {};
  const re = /class="chap-btn[^"]*"\s+id="([^"]+)"(?:\s+data-src="([^"]+)")?/g;
  let m;
  while ((m = re.exec(explorerHtml))) { if (m[2]) map[m[1]] = m[2]; }
  return map;
}

/**
 * Which document is showing, asked the way the shell asks it.
 *
 * NOT `frame.src`. setFrame() navigates via `contentWindow.location.replace(url)`, so the
 * iframe ELEMENT's src attribute keeps its original value forever while the document
 * underneath changes -- a reader built on it reports the first page for the whole session.
 * explorer.html exports window.CCLFrameSrc as the one implementation precisely because its
 * own readers drifted apart six times; borrowing it means this harness cannot become the
 * seventh.
 */
function frameSrc(page) {
  return page.eval("return window.CCLFrameSrc ? window.CCLFrameSrc() : null;");
}

async function waitForSrc(page, want, limitMs) {
  const limit = limitMs || 20000;
  for (let waited = 0; waited <= limit; waited += 250) {
    if ((await frameSrc(page)) === want) return true;
    await sleep(250);
  }
  return false;
}

/** Resolve when the frame holds `want` AND that document has finished parsing. */
async function frameSettled(page, want, limitMs) {
  if (!(await waitForSrc(page, want, limitMs))) return false;
  return await poll(page, "var f=document.getElementById('content-frame');" +
                          "var d=f&&f.contentDocument;" +
                          "return !!(d && d.readyState==='complete');", limitMs);
}

async function poll(page, expr, limitMs) {
  const limit = limitMs || 20000;
  for (let waited = 0; waited <= limit; waited += 250) {
    if (await page.eval(expr)) return true;
    await sleep(250);
  }
  return false;
}

async function runStep(page, step, chapSrc) {
  if (step.chapter) {
    const r = await page.eval(
      "var b=document.getElementById(" + JSON.stringify(step.chapter) + ");" +
      "if(!b){return 'no such chapter button';}b.click();return 'ok';");
    if (r !== 'ok') throw new Error('chapter ' + step.chapter + ': ' + r);
    // A chapter click swaps the frame. The next step almost always reaches INTO that
    // document, and querying it mid-load finds nothing -- which reads as a dead selector
    // rather than as arriving early. This is the difference between a route that fails
    // and a route that fails one run in four.
    const want = chapSrc[step.chapter];
    if (want && !(await frameSettled(page, want, 20000))) {
      throw new Error('chapter ' + step.chapter + ' did not settle on ' + want +
                      ' (frame is ' + (await frameSrc(page)) + ')');
    }
    return;
  }
  if (step.tab) {
    const r = await H.activateTab(page, step.tab);
    if (r !== 'clicked' && r !== 'already-active') throw new Error('tab ' + step.tab + ': ' + r);
    if (!(await frameSettled(page, step.tab, 60000))) {
      throw new Error('tab ' + step.tab + ' did not settle (frame is ' + (await frameSrc(page)) + ')');
    }
    return;
  }
  if (step.frameClick) {
    // Click inside the loaded document, the way a reader would. A selector that matches
    // nothing must say so here rather than leave the frame quietly unchanged.
    const r = await page.eval(
      "var f=document.getElementById('content-frame');var d=f&&f.contentDocument;" +
      "if(!d){return 'no frame document';}" +
      "var e=d.querySelector(" + JSON.stringify(step.frameClick) + ");" +
      "if(!e){return 'selector matched nothing';}e.click();return 'ok';");
    if (r !== 'ok') throw new Error('frameClick ' + step.frameClick + ': ' + r);
    if (step.loads && !(await frameSettled(page, step.loads, 20000))) {
      throw new Error('frameClick ' + step.frameClick + ' did not load ' + step.loads +
                      ' (frame is ' + (await frameSrc(page)) + ')');
    }
    return;
  }
  if (step.cmd) {
    // Readiness is checked ONCE per route, not here. cclReady waits for #ccl-result to read
    // "CCL ready (...)", but that element is also where every command's reply lands -- so
    // after the first cmd it holds an answer, and a second readiness check waits forever for
    // a banner that will never come back.
    const r = await H.runCmd(page, step.cmd);
    if (!r || !r.ok) throw new Error('cmd "' + step.cmd + '" refused: ' + ((r && r.spoken) || 'no reply'));
    return;
  }
  throw new Error('unknown step kind: ' + JSON.stringify(step));
}

async function main() {
  const manifest = JSON.parse(fs.readFileSync(path.join(HERE, 'manifest.json'), 'utf8'));
  const explorer = fs.readFileSync(path.join(REPO, 'wiki/explorer.html'), 'utf8');
  const chapSrc = chapterSources(explorer);

  // One replay per distinct route; every plate sharing it inherits the verdict.
  const routes = new Map();
  for (const plate of manifest.plates) {
    if (ONLY && plate.slug.indexOf(ONLY) !== 0) continue;
    const key = JSON.stringify(plate.reach);
    if (!routes.has(key)) routes.set(key, { reach: plate.reach, slugs: [] });
    routes.get(key).slugs.push(plate.slug);
  }

  await H.startServer();
  const chrome = await H.startChrome();
  const cdp = await H.CDP.connect(chrome.wsUrl);
  const page = await H.Page.open(cdp);
  const base = 'http://127.0.0.1:' + H.PORT + '/explorer.html';

  let passed = 0;
  const failures = [];
  for (const [, route] of routes) {
    const label = route.slugs[0] + (route.slugs.length > 1 ? ' (+' + (route.slugs.length - 1) + ')' : '');
    const want = expectedSrc(route.reach, chapSrc);
    try {
      await page.navigate(base);
      // The shell boots its command layer before any button is wired; clicking earlier
      // reports "clicked" and does nothing, which reads as a broken route.
      await H.cclReady(page);
      for (const step of route.reach) await runStep(page, step, chapSrc);
      if (want && !(await waitForSrc(page, want, 20000))) {
        throw new Error('landed on ' + (await frameSrc(page)) + ', expected ' + want);
      }
      passed += route.slugs.length;
      process.stdout.write('  ok    ' + label + '  -> ' + want + '\n');
    } catch (e) {
      failures.push({ label: label, slugs: route.slugs, why: (e && e.message) || String(e) });
      process.stdout.write('  FAIL  ' + label + '  -- ' + ((e && e.message) || e) + '\n');
    }
  }

  const total = passed + failures.reduce((n, f) => n + f.slugs.length, 0);
  process.stdout.write('\nroutes: ' + routes.size + '   plates: ' + total +
                       '   passed: ' + passed + '   failed: ' + (total - passed) + '\n');
  H.cleanup();
  if (failures.length) {
    process.stdout.write('REPLAY RED\n');
    process.exit(1);
  }
  process.stdout.write('REPLAY GREEN\n');
}

main().catch(function (e) {
  process.stdout.write('\nHARNESS ERROR: ' + ((e && e.stack) || e) + '\n');
  try { H.cleanup(); } catch (_) {}
  process.exit(2);
});
