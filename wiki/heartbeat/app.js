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

// ── Static structural content (architecture, not live signals) ───────────────
const wikiPages = [
  { type: "Source note", title: "Weekly heartbeat digest", text: "Immutable run output: sources reached, items checked, top stories, tags, relevance scores, and source health.", pills: ["raw-backed", "run-log", "citable"] },
  { type: "Topic page", title: "Agent governance boundaries", text: "Compiled synthesis of agent runtime permissions, human override, local data limits, and governance checkpoints.", pills: ["compiled", "cross-source", "updates"] },
  { type: "Community page", title: "STEM educator AI literacy lens", text: "A local view over the heartbeat for educators, including classroom risk, curriculum relevance, and review cadence.", pills: ["local-lens", "preferences", "roles"] },
  { type: "Contradiction log", title: "Automated assessment promises versus high-stakes risk", text: "Tracks tensions between AI grading utility, curriculum authority, student agency, and accountability.", pills: ["honesty-layer", "review-needed"] },
  { type: "Decision record", title: "Email-first notification baseline", text: "Preserves why email is enabled before SMS, WhatsApp, or Signal in the production rollout sequence.", pills: ["provenance", "operations"] },
  { type: "Index", title: "Heartbeat wiki map", text: "A human-readable map of source notes, topic pages, community lenses, decision records, and federation exports.", pills: ["navigation", "schema"] }
];

const lensItems = [
  ["Filtering lens", "Sources, keywords, topic priorities, excluded categories, and local relevance rules."],
  ["Ranking criteria", "Urgency, community impact, evidence quality, novelty, and actionability."],
  ["Communication preferences", "Digest cadence, channel, length, tone, and escalation threshold."],
  ["Memory controls", "Accepted recommendations, rejected patterns, standing community context, and reset/export controls."],
  ["Consent boundaries", "What stays local, what can be shared with peers, and what can enter the public graph."]
];

const federationItems = [
  { type: "Local-first instance", title: "Community-owned heartbeat", text: "Each community stores its own sources, user preferences, summaries, rankings, and review history.", pills: ["autonomy", "local-data"] },
  { type: "Federated search", title: "Parallel query across instances", text: "A search request can ask multiple community instances for allowed summaries, then aggregate results without centralizing all data.", pills: ["scale", "edge"] },
  { type: "Selective contribution", title: "Stars, rationale, and public graph edges", text: "Communities can contribute high-value signals, comments, and rankings while withholding private user data.", pills: ["consent", "shared-graph"] },
  { type: "Permission hierarchy", title: "Owner, admin, editor, reader, public", text: "Every export and action is constrained by role, policy version, and explicit community-level sharing rules.", pills: ["roles", "audit"] },
  { type: "Computation persistence", title: "Summaries are durable artifacts", text: "Useful computations are stored, searched historically, and revised with provenance instead of being rederived every query.", pills: ["memory", "search"] },
  { type: "10k-instance shape", title: "Simple protocols before heavy centralization", text: "Design favors small, reliable local nodes plus narrow shared protocols for discovery, search, and public graph updates.", pills: ["resilience", "replicable"] }
];

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
  set("hero-digest", m.items_checked != null ? m.items_checked + " updates" : "—");

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

function renderSignals() {
  const target = document.getElementById("signal-list");
  if (!target) return;
  const input = document.getElementById("signal-search");
  const query = ((input && input.value) || "").trim().toLowerCase();
  const L = PREFS.lens, R = PREFS.ranking;
  const signals = Array.isArray(DIGEST.signals) ? DIGEST.signals : [];

  let rows = signals.filter(function (signal) {
    const sigTags = Array.isArray(signal.tags) ? signal.tags : [];
    // text search
    const blob = [signal.title, signal.source, signal.summary, signal.implication, sigTags.join(" ")].join(" ").toLowerCase();
    if (query && blob.indexOf(query) === -1) return false;
    // lens: source include / min relevance / excluded tags
    if (L.sources.length && L.sources.indexOf(signal.source) === -1) return false;
    if ((signal.relevance || 0) < (L.min_relevance || 0)) return false;
    if (L.exclude_tags.length && sigTags.some(function (t) { return L.exclude_tags.indexOf(t) !== -1; })) return false;
    return true;
  });

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
  target.innerHTML = rows.map(function (signal) {
    const tags = (Array.isArray(signal.tags) ? signal.tags : []).map(function (tag) {
      return '<span class="hb-pill ' + tagClass(tag) + '">' + esc(tag) + "</span>";
    }).join("");
    const title = signal.url
      ? '<a href="' + escAttrUrl(signal.url) + '" target="_blank" rel="noopener">' + esc(signal.title) + "</a>"
      : esc(signal.title);
    return (
      '<article class="hb-signal">' +
        "<h4>" + title + "</h4>" +
        "<p>" + esc(signal.summary) + "</p>" +
        "<p><strong>Community implication:</strong> " + esc(signal.implication) + "</p>" +
        '<div class="hb-signal-meta">' +
          '<span class="hb-pill">' + esc(signal.source) + "</span>" +
          '<span class="hb-pill gold">relevance ' + esc(signal.relevance) + "</span>" +
          tags +
        "</div>" +
      "</article>"
    );
  }).join("") || '<div class="hb-signal"><p>No signals match the current filter.</p></div>';
}

function renderCards(id, items) {
  const target = document.getElementById(id);
  if (!target) return;
  target.innerHTML = items.map(function (item) {
    const pills = item.pills.map(function (pill) {
      return '<span class="hb-pill">' + esc(pill) + "</span>";
    }).join("");
    return (
      '<article class="hb-card">' +
        '<div class="hb-card-type">' + esc(item.type) + "</div>" +
        "<h3>" + esc(item.title) + "</h3>" +
        "<p>" + esc(item.text) + "</p>" +
        "<footer>" + pills + "</footer>" +
      "</article>"
    );
  }).join("");
}

function renderLens() {
  const target = document.getElementById("lens-list");
  if (!target) return;
  target.innerHTML = lensItems.map(function (pair) {
    return '<div class="hb-lens-item"><strong>' + esc(pair[0]) + "</strong><span>" + esc(pair[1]) + "</span></div>";
  }).join("");
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
  renderSignals();
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
    button.addEventListener("click", function () { activateView(button.dataset.view); });
  });
  const search = document.getElementById("signal-search");
  if (search) search.addEventListener("input", renderSignals);

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
  renderSignals();
  renderCards("wiki-pages", wikiPages);
  renderCards("federation-list", federationItems);
  renderLens();
}

function loadDigest() {
  // Try the static snapshot first; fall back silently if unavailable.
  return fetch("data/digest.json", { cache: "no-store" })
    .then(function (r) { if (!r.ok) throw new Error("HTTP " + r.status); return r.json(); })
    .then(function (json) {
      if (json && typeof json === "object") DIGEST = json;
    })
    .catch(function () { DIGEST = FALLBACK_DIGEST; });
}

loadPrefs();
wireEvents();
renderAll();           // immediate paint from fallback
loadDigest().then(renderAll); // repaint if a snapshot loaded
