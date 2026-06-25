/* C2A2 Community AI Education — Heartbeat tab
 *
 * Data model:
 *   The "Pulse" view (metrics + signals) is DATA-DRIVEN. On load it tries to
 *   fetch ./data/digest.json (a static snapshot exported from the Heartbeat
 *   runtime's /api/digest endpoint). If that fetch fails — e.g. opened over
 *   file:// where fetch is blocked, or before any snapshot exists — it falls
 *   back to the embedded FALLBACK_DIGEST below so the tab always renders.
 *
 *   The structural sections (compiled-wiki cards, lens schema, federation
 *   cards) describe the architecture, not live signals, so they stay static.
 *
 * Safety: all values that originate from data are HTML-escaped before they
 * touch innerHTML (esc / escAttr), since digest.json may carry external text.
 */

"use strict";

// ── HTML escaping ───────────────────────────────────────────────────────────
function esc(value) {
  return String(value == null ? "" : value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}
// Only allow http(s) URLs through to href; anything else becomes "#".
function escAttrUrl(url) {
  var s = String(url == null ? "" : url).trim();
  return /^https?:\/\//i.test(s) ? esc(s) : "#";
}

// ── Embedded fallback (used only if data/digest.json can't be loaded) ────────
const FALLBACK_DIGEST = {
  seed: true,
  generated: "fallback",
  window: "weekly",
  metrics: {
    sources_reached: 5,
    items_checked: 95,
    high_relevance: 2,
    primary_themes: "Agents + Governance"
  },
  signals: [
    {
      title: "Distributed general-purpose agent networks",
      source: "arXiv cs.AI",
      url: "https://arxiv.org/list/cs.AI/recent",
      relevance: 2,
      tags: ["capability_jump", "governance_policy"],
      summary: "Agent networks are framed around local data, tool permissions, runtime environments, and governance boundaries.",
      implication: "Reassess role boundaries, human override, and cross-instance governance before community deployment."
    },
    {
      title: "LLM-as-judge in education",
      source: "arXiv cs.AI",
      url: "https://arxiv.org/list/cs.AI/recent",
      relevance: 2,
      tags: ["governance_policy"],
      summary: "Automated marking needs curriculum-grounded pipelines and authorized assessment artifacts.",
      implication: "Useful precedent for C2A2 education workflows that must cite local curricula and review standards."
    },
    {
      title: "Verbal reinforcement learning and insight governance",
      source: "arXiv cs.AI",
      url: "https://arxiv.org/list/cs.AI/recent",
      relevance: 1,
      tags: ["capability_jump", "governance_policy"],
      summary: "Agents update behavior through verbal rules extracted from experience, raising retention and forgetting questions.",
      implication: "Heartbeat memory should record when old rules are stale, superseded, or reactivated."
    },
    {
      title: "Dissecting model behavior through agent trajectories",
      source: "arXiv cs.AI",
      url: "https://arxiv.org/list/cs.AI/recent",
      relevance: 1,
      tags: ["capability_jump"],
      summary: "Agent performance is treated as a systems problem rather than only a model benchmark.",
      implication: "Community education should teach harnesses, permissions, logs, and review loops, not just model names."
    },
    {
      title: "AI prototypes from a university futures lab",
      source: "Google AI Blog",
      url: "https://blog.google/technology/ai/",
      relevance: 1,
      tags: ["education", "market_platform"],
      summary: "Student AI prototypes point toward education and work reshaping through practical demos.",
      implication: "Good candidate for a community-facing discussion of useful experimentation versus adoption pressure."
    }
  ]
};

// ── State ────────────────────────────────────────────────────────────────────
let DIGEST = FALLBACK_DIGEST;

// ── Preferences (the reader's lens) ──────────────────────────────────────────
// Shape matches data/preferences.schema.json. Stored per-device now; the SAME
// document will sync to a per-account row at sign-in (Phase 2b) with no change.
const PREFS_KEY = "c2a2_hb_prefs_v1";
function defaultPrefs() {
  return {
    version: 1,
    lens: { sources: [], exclude_sources: [], exclude_tags: [], keywords: [], min_relevance: 0 },
    ranking: { sort: "relevance", priority_tags: [], priority_boost: 1 },
    communication: { digest_cadence: "weekly", channel: "in_app", length: "brief" },
    consent: { share_stars: false, share_comments: false, contribute_aggregate_rank: false }
  };
}
let PREFS = defaultPrefs();

// Merge a saved/partial prefs object onto a fresh default so older or partial
// documents (from localStorage or the account row) stay valid.
function mergePrefs(saved) {
  const base = defaultPrefs();
  if (saved && typeof saved === "object") {
    ["lens", "ranking", "communication", "consent"].forEach(function (g) {
      if (saved[g] && typeof saved[g] === "object") base[g] = Object.assign(base[g], saved[g]);
    });
  }
  return base;
}
function loadPrefs() {
  try {
    const raw = window.localStorage.getItem(PREFS_KEY);
    if (raw) PREFS = mergePrefs(JSON.parse(raw));
  } catch (e) { PREFS = defaultPrefs(); }
}
function savePrefs() {
  try { window.localStorage.setItem(PREFS_KEY, JSON.stringify(PREFS)); } catch (e) { /* private mode */ }
  // optional account layer (auth.js) persists the same document to the user's row
  if (typeof window.HB_onPrefsSaved === "function") { try { window.HB_onPrefsSaved(PREFS); } catch (e) { /* ignore */ } }
}

// Seam for the optional account layer: read the live lens, or adopt one from the account.
window.HB_getPrefs = function () { return PREFS; };
window.HB_setPrefs = function (p) { PREFS = mergePrefs(p); renderAll(); };

function tagClass(tag) {
  if (tag.indexOf("governance") !== -1) return "gold";
  if (tag.indexOf("capability") !== -1) return "rose";
  return "teal";
}

// ── Render: metrics + hero status from the active digest ─────────────────────
function renderMetrics() {
  const m = DIGEST.metrics || {};
  const set = function (id, val) {
    const el = document.getElementById(id);
    if (el) el.textContent = String(val == null ? "—" : val);
  };
  set("m-sources", m.sources_reached);
  set("m-items", m.items_checked);
  set("m-high", m.high_relevance);
  set("m-themes", m.primary_themes);

  // Live hero + spine state (replaces the old asserted labels).
  const signals = Array.isArray(DIGEST.signals) ? DIGEST.signals : [];
  const withLong = signals.filter(function (s) { return s.long_summary; }).length;
  const genLabel = DIGEST.generated && DIGEST.generated !== "fallback" ? DIGEST.generated : "embedded fallback";
  set("hero-generated", genLabel);
  set("hero-signals", (signals.length) + " · " + (m.items_checked != null ? m.items_checked : "—"));
  set("hero-summaries", withLong + " of " + signals.length);
  set("spine-sources", (m.sources_reached != null ? m.sources_reached : "—") + " sources →");
  set("spine-items", (m.items_checked != null ? m.items_checked : "—") + " items · " + genLabel + " →");

  // Seed banner: visible only when the snapshot is seed/sample data.
  const banner = document.getElementById("seed-banner");
  if (banner) banner.hidden = !DIGEST.seed;

  // Provenance line under the metrics.
  const prov = document.getElementById("digest-provenance");
  if (prov) {
    const gen = DIGEST.generated && DIGEST.generated !== "fallback"
      ? "snapshot " + esc(DIGEST.generated)
      : "embedded fallback (no snapshot loaded)";
    const win = DIGEST.window ? esc(DIGEST.window) + " window · " : "";
    prov.innerHTML = win + gen;
  }
}

// Facets present in the current digest (drive the lens controls).
function facets() {
  const signals = Array.isArray(DIGEST.signals) ? DIGEST.signals : [];
  const sources = [], tags = [];
  signals.forEach(function (s) {
    if (s.source && sources.indexOf(s.source) === -1) sources.push(s.source);
    (Array.isArray(s.tags) ? s.tags : []).forEach(function (t) { if (tags.indexOf(t) === -1) tags.push(t); });
  });
  sources.sort(); tags.sort();
  return { sources: sources, tags: tags };
}

// Apply the reader's lens (+ optional text query) to a signal list. Shared by
// Pulse (live digest) and the lens-editor preview.
function applyLens(signals, query) {
  const L = PREFS.lens;
  const q = (query || "").trim().toLowerCase();
  return signals.filter(function (signal) {
    const sigTags = Array.isArray(signal.tags) ? signal.tags : [];
    const blob = [signal.title, signal.source, signal.summary, signal.implication, sigTags.join(" ")].join(" ").toLowerCase();
    if (q && blob.indexOf(q) === -1) return false;
    if (L.sources.length && L.sources.indexOf(signal.source) === -1) return false;
    if (L.exclude_sources && L.exclude_sources.length && L.exclude_sources.indexOf(signal.source) !== -1) return false;
    if ((signal.relevance || 0) < (L.min_relevance || 0)) return false;
    if (L.exclude_tags.length && sigTags.some(function (t) { return L.exclude_tags.indexOf(t) !== -1; })) return false;
    if (L.keywords && L.keywords.length && !L.keywords.some(function (k) { return blob.indexOf(String(k).toLowerCase()) !== -1; })) return false;
    return true;
  });
}

// Build one signal card (shared by Pulse + History).
function signalCardHTML(signal) {
  const tags = (Array.isArray(signal.tags) ? signal.tags : []).map(function (tag) {
    return '<span class="hb-pill ' + tagClass(tag) + '">' + esc(tag) + "</span>";
  }).join("");
  const title = signal.url
    ? '<a href="' + escAttrUrl(signal.url) + '" target="_blank" rel="noopener">' + esc(signal.title) + "</a>"
    : esc(signal.title);
  var fullSummary = "";
  if (signal.long_summary) {
    var prov = signal.summary_provenance || {};
    var provBits = [];
    if (prov.kind) provBits.push(esc(prov.kind));
    if (prov.model) provBits.push(esc(prov.model));
    if (prov.generated) provBits.push(esc(prov.generated));
    var provLine = provBits.length
      ? '<span class="hb-gen-tag" title="This summary was written by a model from the source text, and stored with provenance (honesty layer).">' + provBits.join(" · ") + "</span>"
      : "";
    fullSummary =
      '<details class="hb-fullsummary">' +
        "<summary>Full summary " + provLine + "</summary>" +
        "<p>" + esc(signal.long_summary) + "</p>" +
      "</details>";
  }
  return (
    '<article class="hb-signal">' +
      "<h4>" + title + "</h4>" +
      "<p>" + esc(signal.summary) + "</p>" +
      fullSummary +
      "<p><strong>Community implication:</strong> " + esc(signal.implication) + "</p>" +
      '<div class="hb-signal-meta">' +
        '<span class="hb-pill">' + esc(signal.source) + "</span>" +
        '<span class="hb-pill gold">relevance ' + esc(signal.relevance) + "</span>" +
        tags +
      "</div>" +
    "</article>"
  );
}

function renderSignals() {
  const target = document.getElementById("signal-list");
  if (!target) return;
  const input = document.getElementById("signal-search");
  const query = ((input && input.value) || "").trim().toLowerCase();
  const R = PREFS.ranking;
  const signals = Array.isArray(DIGEST.signals) ? DIGEST.signals : [];

  let rows = applyLens(signals, query);

  // ranking
  const boostOf = function (signal) {
    const sigTags = Array.isArray(signal.tags) ? signal.tags : [];
    const hits = sigTags.filter(function (t) { return R.priority_tags.indexOf(t) !== -1; }).length;
    return (signal.relevance || 0) + hits * (R.priority_boost || 0);
  };
  if (R.sort === "source") {
    rows.sort(function (a, b) { return String(a.source).localeCompare(String(b.source)); });
  } else if (R.sort === "recency") {
    // digest order is newest-first by convention; keep as-is
  } else { // relevance (default), with priority-tag boost
    rows = rows.slice().sort(function (a, b) { return boostOf(b) - boostOf(a); });
  }
  target.innerHTML = rows.map(signalCardHTML).join("") ||
    '<div class="hb-signal"><p>No signals match the current filter.</p></div>';
}

// ── History: browse past heartbeat snapshots (data/snapshots/index.json) ──────
var HISTORY = { list: null, current: null };
function loadHistory() {
  return fetch("data/snapshots/index.json?t=" + Date.now(), { cache: "no-store" })
    .then(function (r) { if (!r.ok) throw new Error("HTTP " + r.status); return r.json(); })
    .then(function (j) { HISTORY.list = (j && j.snapshots) || []; renderHistoryList(); })
    .catch(function () { HISTORY.list = []; renderHistoryList(); });
}
function renderHistoryList() {
  const box = document.getElementById("history-dates");
  if (!box) return;
  if (!HISTORY.list || !HISTORY.list.length) {
    box.innerHTML = '<p class="hb-dim">No saved snapshots yet. Each heartbeat refresh archives a dated snapshot here.</p>';
    return;
  }
  box.innerHTML = HISTORY.list.map(function (s) {
    return '<button type="button" class="hb-hist-item" data-file="' + esc(s.file) + '" data-date="' + esc(s.date) + '">' +
      '<strong>' + esc(s.date) + "</strong>" +
      '<span>' + esc(s.signals) + " signals · " + esc(s.items_checked == null ? "—" : s.items_checked) + " checked · " + esc(s.primary_themes || "") + "</span>" +
    "</button>";
  }).join("");
  box.querySelectorAll(".hb-hist-item").forEach(function (b) {
    b.addEventListener("click", function () { openSnapshot(b.dataset.file, b.dataset.date); });
  });
  // auto-open the newest on first view
  if (!HISTORY.current && HISTORY.list[0]) openSnapshot(HISTORY.list[0].file, HISTORY.list[0].date);
}
function openSnapshot(file, date) {
  HISTORY.current = file;
  document.querySelectorAll("#history-dates .hb-hist-item").forEach(function (b) {
    b.classList.toggle("active", b.dataset.file === file);
  });
  const detail = document.getElementById("history-detail");
  if (detail) detail.innerHTML = '<p class="hb-dim">Loading ' + esc(date) + "…</p>";
  fetch("data/snapshots/" + encodeURIComponent(file) + "?t=" + Date.now(), { cache: "no-store" })
    .then(function (r) { if (!r.ok) throw new Error("HTTP " + r.status); return r.json(); })
    .then(function (snap) { renderSnapshotDetail(snap, date); })
    .catch(function () { if (detail) detail.innerHTML = '<p class="hb-dim">Could not load this snapshot.</p>'; });
}
function renderSnapshotDetail(snap, date) {
  const detail = document.getElementById("history-detail");
  if (!detail) return;
  const m = snap.metrics || {};
  const signals = Array.isArray(snap.signals) ? snap.signals : [];
  detail.innerHTML =
    '<div class="hb-metric-row">' +
      '<div class="hb-metric"><span>Date</span><strong>' + esc(date) + "</strong></div>" +
      '<div class="hb-metric"><span>Sources reached</span><strong>' + esc(m.sources_reached == null ? "—" : m.sources_reached) + "</strong></div>" +
      '<div class="hb-metric"><span>Items checked</span><strong>' + esc(m.items_checked == null ? "—" : m.items_checked) + "</strong></div>" +
      '<div class="hb-metric"><span>Primary themes</span><strong>' + esc(m.primary_themes || "—") + "</strong></div>" +
    "</div>" +
    '<div class="hb-list">' + (signals.map(signalCardHTML).join("") || '<div class="hb-signal"><p>No signals in this snapshot.</p></div>') + "</div>";
}

// ── My Lens: full editor (the same PREFS the Pulse panel uses) ────────────────
function _setVal(id, v) { const el = document.getElementById(id); if (el && document.activeElement !== el) el.value = String(v == null ? "" : v); }
function _setChecked(id, v) { const el = document.getElementById(id); if (el) el.checked = !!v; }

function fillChips(boxId, all, selected) {
  const box = document.getElementById(boxId);
  if (!box) return;
  box.innerHTML = all.map(function (v) { return chip(v, selected.indexOf(v) !== -1); }).join("") ||
    '<span class="hb-chip-empty">none in current digest</span>';
  box.querySelectorAll(".hb-chip").forEach(function (b) {
    b.addEventListener("click", function () { toggleInList(selected, b.dataset.val); afterPrefChange(); });
  });
}

function updateLensEditorPreview() {
  const el = document.getElementById("le-preview");
  if (!el) return;
  const signals = Array.isArray(DIGEST.signals) ? DIGEST.signals : [];
  const n = applyLens(signals, "").length;
  el.textContent = n + " of " + signals.length + " current signals match this lens";
}

// Render the editor controls from PREFS. Static controls are bound once in
// wireEvents; only the chip rows (which are rebuilt here) get fresh handlers.
function renderLensEditor() {
  if (!document.getElementById("le-sources")) return;   // tab not in DOM
  const f = facets(), L = PREFS.lens, R = PREFS.ranking;
  fillChips("le-sources", f.sources, L.sources);
  fillChips("le-exsources", f.sources, L.exclude_sources);
  fillChips("le-extags", f.tags, L.exclude_tags);
  fillChips("le-pritags", f.tags, R.priority_tags);
  const kw = document.getElementById("le-keywords");
  if (kw && document.activeElement !== kw) kw.value = (L.keywords || []).join(", ");
  _setVal("le-minrel", L.min_relevance);
  _setVal("le-sort", R.sort);
  _setVal("le-cadence", PREFS.communication.digest_cadence);
  _setChecked("le-consent-stars", PREFS.consent.share_stars);
  _setChecked("le-consent-comments", PREFS.consent.share_comments);
  _setChecked("le-consent-rank", PREFS.consent.contribute_aggregate_rank);
  updateLensEditorPreview();
}

function exportLens() {
  try {
    const blob = new Blob([JSON.stringify(PREFS, null, 2)], { type: "application/json" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "c2a2-heartbeat-lens.json";
    document.body.appendChild(a); a.click(); document.body.removeChild(a);
    setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);
  } catch (e) { /* ignore */ }
}
function importLensFile(file) {
  const reader = new FileReader();
  reader.onload = function () {
    try {
      const obj = JSON.parse(reader.result);
      if (window.HB_setPrefs) window.HB_setPrefs(obj); else { PREFS = mergePrefs(obj); renderAll(); }
      savePrefs();
      setSaveStatus("saved");
    } catch (e) { /* invalid file, ignore */ }
  };
  reader.readAsText(file);
}

// ── Lens controls (the preferences panel) ────────────────────────────────────
function chip(label, active) {
  return '<button type="button" class="hb-chip' + (active ? " on" : "") +
         '" data-val="' + esc(label) + '">' + esc(label) + "</button>";
}
function renderLensControls() {
  const f = facets();
  const srcBox = document.getElementById("pref-sources");
  const tagBox = document.getElementById("pref-extags");
  if (srcBox) srcBox.innerHTML = f.sources.map(function (s) {
    return chip(s, PREFS.lens.sources.indexOf(s) !== -1);
  }).join("") || '<span class="hb-chip-empty">no sources</span>';
  if (tagBox) tagBox.innerHTML = f.tags.map(function (t) {
    return chip(t, PREFS.lens.exclude_tags.indexOf(t) !== -1);
  }).join("") || '<span class="hb-chip-empty">no tags</span>';

  // reflect current values into the selects
  const setVal = function (id, v) { const el = document.getElementById(id); if (el) el.value = String(v); };
  setVal("pref-minrel", PREFS.lens.min_relevance);
  setVal("pref-sort", PREFS.ranking.sort);
  setVal("pref-cadence", PREFS.communication.digest_cadence);

  // chip toggles
  if (srcBox) srcBox.querySelectorAll(".hb-chip").forEach(function (b) {
    b.addEventListener("click", function () { toggleInList(PREFS.lens.sources, b.dataset.val); afterPrefChange(); });
  });
  if (tagBox) tagBox.querySelectorAll(".hb-chip").forEach(function (b) {
    b.addEventListener("click", function () { toggleInList(PREFS.lens.exclude_tags, b.dataset.val); afterPrefChange(); });
  });
}
function toggleInList(list, val) {
  const i = list.indexOf(val);
  if (i === -1) list.push(val); else list.splice(i, 1);
}
function afterPrefChange() {
  savePrefs();
  renderLensControls();
  renderLensEditor();
  renderSignals();
  setSaveStatus("saved");
  updateLensStatus();
}

// ── Lens clarity: active-filter count + save/sync status ──────────────────────
function activeFilterCount() {
  var n = 0;
  if (PREFS.lens.sources.length) n += PREFS.lens.sources.length;
  if (PREFS.lens.exclude_sources && PREFS.lens.exclude_sources.length) n += PREFS.lens.exclude_sources.length;
  if (PREFS.lens.exclude_tags.length) n += PREFS.lens.exclude_tags.length;
  if (PREFS.lens.keywords && PREFS.lens.keywords.length) n += PREFS.lens.keywords.length;
  if (PREFS.ranking.priority_tags && PREFS.ranking.priority_tags.length) n += PREFS.ranking.priority_tags.length;
  if ((PREFS.lens.min_relevance || 0) > 0) n += 1;
  if (PREFS.ranking.sort && PREFS.ranking.sort !== "relevance") n += 1;
  var input = document.getElementById("signal-search");
  if (input && input.value.trim()) n += 1;
  return n;
}
function updateLensStatus() {
  var n = activeFilterCount();
  var countEl = document.getElementById("lens-active-count");
  if (countEl) countEl.textContent = n ? (n + " active") : "no filters";
  var reset = document.getElementById("pref-reset");
  if (reset) reset.textContent = n ? ("Reset lens (" + n + ")") : "Reset lens";
}
// Shows "Saving… / Saved ✓ · (synced|on this device)" so the silent save is visible.
var _saveStatusTimer = null;
function setSaveStatus(phase) {
  var el = document.getElementById("lens-save-status");
  if (!el) return;
  var synced = !!window.HB_signedIn;
  if (phase === "saving") {
    el.textContent = "Saving…";
    el.className = "hb-save-status saving";
    return;
  }
  el.textContent = "Saved ✓ · " + (synced ? "synced to account" : "on this device");
  el.className = "hb-save-status saved";
  if (_saveStatusTimer) clearTimeout(_saveStatusTimer);
  _saveStatusTimer = setTimeout(function () {
    if (el) { el.textContent = synced ? "synced to account" : "stored on this device — sign in to sync"; el.className = "hb-save-status idle"; }
  }, 2200);
}

// ── View switching ───────────────────────────────────────────────────────────
function activateView(name) {
  document.querySelectorAll(".hb-tab").forEach(function (button) {
    button.classList.toggle("active", button.dataset.view === name);
  });
  document.querySelectorAll(".hb-view").forEach(function (view) {
    view.classList.toggle("active", view.id === "view-" + name);
  });
}

// ── Init ─────────────────────────────────────────────────────────────────────
function wireEvents() {
  document.querySelectorAll(".hb-tab").forEach(function (button) {
    button.addEventListener("click", function () {
      activateView(button.dataset.view);
      if (button.dataset.view === "history" && !HISTORY.list) loadHistory();
      if (button.dataset.view === "lens") renderLensEditor();
    });
  });

  // Spine steps jump to the tab that realizes them (live) or the Roadmap (planned).
  document.querySelectorAll(".hb-spine-step[data-goto]").forEach(function (step) {
    step.addEventListener("click", function () {
      const v = step.dataset.goto;
      activateView(v);
      if (v === "history" && !HISTORY.list) loadHistory();
      if (v === "lens") renderLensEditor();
      const nav = document.querySelector(".hb-tabs");
      if (nav && nav.scrollIntoView) nav.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });

  // ── My Lens editor: bind static controls once (chips bind on each render) ──
  const leKw = document.getElementById("le-keywords");
  if (leKw) leKw.addEventListener("input", function () {
    PREFS.lens.keywords = leKw.value.split(",").map(function (s) { return s.trim(); }).filter(Boolean);
    afterPrefChange();
  });
  const bindSel = function (id, fn) { const el = document.getElementById(id); if (el) el.addEventListener("change", function () { fn(el.value); afterPrefChange(); }); };
  bindSel("le-minrel", function (v) { PREFS.lens.min_relevance = parseInt(v, 10) || 0; });
  bindSel("le-sort", function (v) { PREFS.ranking.sort = v; });
  bindSel("le-cadence", function (v) { PREFS.communication.digest_cadence = v; });
  const bindChk = function (id, key, grp) { const el = document.getElementById(id); if (el) el.addEventListener("change", function () { PREFS[grp][key] = el.checked; afterPrefChange(); }); };
  bindChk("le-consent-stars", "share_stars", "consent");
  bindChk("le-consent-comments", "share_comments", "consent");
  bindChk("le-consent-rank", "contribute_aggregate_rank", "consent");
  const leExport = document.getElementById("le-export");
  if (leExport) leExport.addEventListener("click", exportLens);
  const leImportBtn = document.getElementById("le-import");
  const leImportFile = document.getElementById("le-import-file");
  if (leImportBtn && leImportFile) {
    leImportBtn.addEventListener("click", function () { leImportFile.click(); });
    leImportFile.addEventListener("change", function () { if (leImportFile.files[0]) importLensFile(leImportFile.files[0]); leImportFile.value = ""; });
  }
  const leReset = document.getElementById("le-reset");
  if (leReset) leReset.addEventListener("click", function () { PREFS = defaultPrefs(); afterPrefChange(); });
  const search = document.getElementById("signal-search");
  if (search) search.addEventListener("input", function () { renderSignals(); updateLensStatus(); });

  // Refresh: re-fetch the snapshot (cache-busted) and repaint. The MVP of "live".
  const refresh = document.getElementById("hb-refresh");
  if (refresh) refresh.addEventListener("click", refreshDigest);

  // Lens help popover (the "?" next to "Your lens"). Toggle without flipping the
  // surrounding <details> open/closed.
  const help = document.getElementById("lens-help-btn");
  const pop = document.getElementById("lens-help-pop");
  if (help && pop) {
    help.addEventListener("click", function (e) {
      e.preventDefault(); e.stopPropagation();
      pop.hidden = !pop.hidden;
      help.setAttribute("aria-expanded", pop.hidden ? "false" : "true");
    });
    document.addEventListener("click", function (e) {
      if (!pop.hidden && e.target !== pop && !pop.contains(e.target) && e.target !== help) {
        pop.hidden = true;
        help.setAttribute("aria-expanded", "false");
      }
    });
  }

  const minrel = document.getElementById("pref-minrel");
  if (minrel) minrel.addEventListener("change", function () { PREFS.lens.min_relevance = parseInt(minrel.value, 10) || 0; afterPrefChange(); });
  const sort = document.getElementById("pref-sort");
  if (sort) sort.addEventListener("change", function () { PREFS.ranking.sort = sort.value; afterPrefChange(); });
  const cadence = document.getElementById("pref-cadence");
  if (cadence) cadence.addEventListener("change", function () { PREFS.communication.digest_cadence = cadence.value; afterPrefChange(); });
  const reset = document.getElementById("pref-reset");
  if (reset) reset.addEventListener("click", function () { PREFS = defaultPrefs(); afterPrefChange(); });
}

function renderAll() {
  renderMetrics();
  renderLensControls();
  renderLensEditor();
  renderSignals();
}

function loadDigest() {
  // Try the static snapshot first; fall back silently if unavailable.
  // Cache-busted so a Refresh always pulls the newest exported snapshot.
  return fetch("data/digest.json?t=" + Date.now(), { cache: "no-store" })
    .then(function (r) { if (!r.ok) throw new Error("HTTP " + r.status); return r.json(); })
    .then(function (json) {
      if (json && typeof json === "object") DIGEST = json;
    })
    .catch(function () { DIGEST = FALLBACK_DIGEST; });
}

// Refresh control: re-fetch the snapshot and repaint, with a small status line.
function refreshDigest() {
  var btn = document.getElementById("hb-refresh");
  var status = document.getElementById("hb-refresh-status");
  if (btn) btn.disabled = true;
  if (status) status.textContent = "Checking…";
  return loadDigest().then(function () {
    renderAll();
    if (status) {
      var when = new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
      var stamp = (DIGEST.generated && DIGEST.generated !== "fallback")
        ? "snapshot " + esc(DIGEST.generated) : "embedded fallback";
      status.textContent = "Updated " + when + " · " + stamp;
    }
    if (btn) btn.disabled = false;
  });
}

loadPrefs();
wireEvents();
renderAll();           // immediate paint from fallback
updateLensStatus();
loadDigest().then(function () { renderAll(); updateLensStatus(); }); // repaint if a snapshot loaded
