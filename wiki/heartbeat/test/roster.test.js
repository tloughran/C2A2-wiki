/**
 * Heartbeat CI gate — "Sources monitored" roster.
 *
 * This test encodes WHY the behavior matters, not just a frozen count:
 *   1. RENDER FIDELITY — the DOM must faithfully reflect data/sources_roster.json
 *      (lane count, total chips, summary text, every source name present). If the
 *      renderer silently drops or mangles sources, this fails — regardless of how
 *      many feeds we run. It will NOT spuriously fail when the feed list changes.
 *   2. OPEN-ACCESS INVARIANT — no paywalled source may appear (we removed The Verge
 *      and MIT Technology Review on 2026-06-26 on purpose). A regression that re-adds
 *      a subscription source must fail the build.
 *   3. SAFETY — every source chip links to a real https URL (escAttrUrl must not let
 *      a "#" through), and the honesty note ("filters what you see") must be present.
 *
 * Run: `npm ci && npm test` from this dir. Exit non-zero on any failure (CI gate).
 */
const fs = require("fs");
const path = require("path");
const { JSDOM } = require("jsdom");

const HB = path.resolve(__dirname, "..");
const html = fs.readFileSync(path.join(HB, "index.html"), "utf8");
const appjs = fs.readFileSync(path.join(HB, "app.js"), "utf8");
const roster = JSON.parse(fs.readFileSync(path.join(HB, "data", "sources_roster.json"), "utf8"));

// Sources we have deliberately excluded as subscription-gated. Re-adding any of
// these (by display name) must fail the gate. Extend this list, never silently drop it.
const PAYWALLED = [/\bThe Verge\b/i, /MIT Technology Review/i];

const dom = new JSDOM(html, { runScripts: "outside-only", url: "http://localhost:8080/heartbeat/index.html" });
const { window } = dom;
window.fetch = function (u) {
  let body = { ok: false };
  if (/sources_roster\.json/.test(u)) body = roster;
  else if (/snapshots\/index\.json/.test(u)) body = { snapshots: [] };
  else if (/digest\.json/.test(u)) body = { seed: false, generated: "ci", signals: [] };
  return Promise.resolve({ ok: true, status: 200, json: () => Promise.resolve(body) });
};
try {
  new window.Function(appjs).call(window);
} catch (e) {
  console.error("app.js threw on load:", e.message);
  process.exit(2);
}

setTimeout(function () {
  const doc = window.document;
  let pass = 0, fail = 0;
  const ok = (cond, label) => { cond ? pass++ : (fail++, console.error("FAIL:", label)); };

  const lanes = roster.lanes || [];
  const expectedTotal = roster.total != null
    ? roster.total
    : lanes.reduce((n, l) => n + (l.sources ? l.sources.length : 0), 0);
  const expectedNames = lanes.flatMap(l => (l.sources || []).map(s => s.name));

  const laneEls = doc.querySelectorAll("#roster-lanes .hb-lane");
  const chipEls = Array.from(doc.querySelectorAll("#roster-lanes .hb-src"));
  const chipNames = chipEls.map(a => a.textContent);
  const sumText = (doc.getElementById("roster-sum") || {}).textContent || "";
  const note = (doc.querySelector(".hb-roster-note") || {}).textContent || "";

  // (1) render fidelity — DOM mirrors the data file, whatever it contains
  ok(laneEls.length === lanes.length, `lane count matches data (dom ${laneEls.length} vs data ${lanes.length})`);
  ok(chipEls.length === expectedTotal, `chip count matches data total (dom ${chipEls.length} vs data ${expectedTotal})`);
  ok(sumText === `${expectedTotal} feeds across ${lanes.length} lanes`, `summary text matches data (got "${sumText}")`);
  ok(expectedNames.every(n => chipNames.includes(n)), "every data source renders a chip");

  // (2) open-access invariant — no paywalled source may appear
  PAYWALLED.forEach(rx => ok(!chipNames.some(n => rx.test(n)), `paywalled source absent: ${rx}`));

  // (3) safety — real https links + honesty note
  ok(chipEls.every(a => /^https:\/\//i.test(a.getAttribute("href") || "")), "all chips have https hrefs (no '#')");
  ok(/filters what you|never what is collected/i.test(note), "lens honesty note present");

  console.log(`heartbeat roster gate: ${pass} pass, ${fail} fail`);
  process.exit(fail ? 1 : 0);
}, 300);
