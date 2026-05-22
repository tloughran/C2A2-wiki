'use strict';
/*
 * community-cards.js — Cards mode + GPRS self-articulation reader for the
 * C2A2 Community Explorer rebuild.
 *
 * The rebuild puts the substance on the surface: a responsive grid of community
 * cards (the discovery + peer-finding canvas, default mode) whose click opens a
 * right-side drawer presenting the fuller GPRS schema —
 *   Goals · Problems · Resources(have/tap/need) · Solutions(effected/proposed)
 * — with every field marked inferred-seed vs community-claimed (Pathway 14
 * honesty layer), plus provenance and the verified link.
 *
 * Decoupled from app.js exactly like community-views.js: the 4-tab controller
 * (community-views.js) calls window.CCCards.render(rows) with the current
 * filtered slice (originally carried on the 'cc:rows' CustomEvent). This module
 * never touches app.js internals.
 *
 * Broker-readiness: this module performs NO key/LLM access. Claim, visibility,
 * and progress are designed-in but non-persistent stubs; every such action is
 * routed through the single brokerStub() seam so the Pathway-00 broker can drop
 * in real persistence + selective per-peer sharing with no caller changes.
 *
 * DOM contract (provided by index.html):
 *   #cc-card-grid, #cc-card-status            - card grid host + count line
 *   #cc-reader (+ .cc-reader-backdrop, [data-cc-reader-close]),
 *   #cc-reader-body                           - the drawer + its body
 *   #toggle-filter-panel, #filter-panel       - slim chip-row "+ Filter" toggle
 *   #toast                                    - transient message host
 */
(function () {
  var CARD_LIMIT = 60;

  // Matches the C2A2 muted palette (see CLAUDE.md / community-views.js).
  var TYPE_COLORS = {
    Academic: '#5A8EAF',
    Corporate: '#C9A84C',
    Ideological: '#4E8A5E',
    Religious: '#A85D3A'
  };
  function typeColor(t) { return TYPE_COLORS[t] || '#9a8f6a'; }

  var latestRows = [];
  var byId = {};

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }
  function truncate(s, n) {
    s = String(s == null ? '' : s).trim();
    return s.length > n ? s.slice(0, n - 1).trimEnd() + '…' : s;
  }
  function hasText(v) { return !!(v && String(v).trim()); }

  function showToast(msg) {
    var el = document.getElementById('toast');
    if (!el) return;
    el.textContent = msg;
    el.classList.add('show');
    clearTimeout(showToast._t);
    showToast._t = setTimeout(function () { el.classList.remove('show'); }, 2800);
  }

  // ── Honesty layer ────────────────────────────────────────────────────
  // Today every record is inferred seed. fieldState is future-proof: a record
  // (or a per-field marker the broker will write) can declare community-claimed
  // state, and the reader will badge it accordingly with no further changes.
  function fieldState(record, key) {
    if (record && record.Claim_State === 'community-claimed') {
      var perField = record[key + '_Source'];
      if (perField === 'inferred') return 'inferred';
      return 'community-claimed';
    }
    return 'inferred';
  }
  function badge(state) {
    return state === 'community-claimed'
      ? '<span class="cc-badge cc-badge-claimed">community-claimed</span>'
      : '<span class="cc-badge cc-badge-inferred">inferred seed</span>';
  }

  // ── GPRS transform (pure; code answers, not the model) ────────────────
  // Seeds the richer schema from the flat record: Problem→Problems,
  // Resource→Resources.have, Solution→Solutions.effected; Goals, Resources.tap,
  // Resources.need, Solutions.proposed start empty/inferred.
  function buildGPRS(r) {
    return {
      goals:     { text: r.Goals || '', state: fieldState(r, 'Goals') },
      problems:  { text: r.Problem_Statement || '', state: fieldState(r, 'Problem_Statement') },
      resources: {
        have: { text: r.Resource_Statement || '', state: fieldState(r, 'Resource_Statement') },
        tap:  { text: r.Resource_Tap || '',  state: fieldState(r, 'Resource_Tap') },
        need: { text: r.Resource_Need || '', state: fieldState(r, 'Resource_Need') }
      },
      solutions: {
        effected: { text: r.Solution_Statement || '', state: fieldState(r, 'Solution_Statement') },
        proposed: { text: r.Solution_Proposed || '',  state: fieldState(r, 'Solution_Proposed') }
      }
    };
  }

  // ── CARD GRID ─────────────────────────────────────────────────────────
  function prsGlance(label, cls, txt) {
    if (!hasText(txt)) return '';
    return '<div class="cc-card-prs ' + cls + '"><span>' + label + '</span>' + esc(truncate(txt, 96)) + '</div>';
  }
  function cardHTML(r) {
    var color = typeColor(r.Type);
    var meta = [r.Subtype, r.Country].filter(Boolean).join(' · ');
    return '<button class="cc-card" type="button" data-cc-card-id="' + esc(r.Community_ID) + '" style="--type-color:' + color + '">'
      + '<div class="cc-card-top">'
      + '<span class="cc-card-type" style="background:' + color + '">' + esc(r.Type || 'Community') + '</span>'
      + '<span class="cc-badge cc-badge-inferred cc-card-seed">inferred seed</span>'
      + '</div>'
      + '<h3 class="cc-card-name">' + esc(r.Community_Name) + '</h3>'
      + '<div class="cc-card-meta">' + esc(meta) + '</div>'
      + '<div class="cc-card-prsstack">'
      + prsGlance('P', 'p', r.Problem_Statement)
      + prsGlance('R', 'r', r.Resource_Statement)
      + prsGlance('S', 's', r.Solution_Statement)
      + '</div>'
      + '<span class="cc-card-open">View G·P·R·S profile →</span>'
      + '</button>';
  }

  function render(rows) {
    latestRows = Array.isArray(rows) ? rows : [];
    byId = {};
    latestRows.forEach(function (r) { byId[r.Community_ID] = r; });

    var grid = document.getElementById('cc-card-grid');
    var status = document.getElementById('cc-card-status');
    if (!grid) return;

    if (!latestRows.length) {
      grid.innerHTML = '<div class="cc-empty">No communities match the current search and filters.</div>';
      if (status) status.textContent = '';
      return;
    }
    var shown = latestRows.slice(0, CARD_LIMIT);
    grid.innerHTML = shown.map(cardHTML).join('');
    if (status) {
      status.textContent = latestRows.length > CARD_LIMIT
        ? 'Showing the first ' + CARD_LIMIT + ' of ' + latestRows.length + ' communities — refine search or filters to narrow.'
        : latestRows.length + (latestRows.length === 1 ? ' community' : ' communities');
    }
  }

  // ── GPRS READER (right-side drawer) ───────────────────────────────────
  function fieldBlock(label, field) {
    var body = hasText(field.text)
      ? '<p>' + esc(field.text) + '</p>'
      : '<p class="cc-empty-field">Not yet articulated — open for the community to claim.</p>';
    var state = hasText(field.text) ? field.state : 'inferred';
    return '<div class="cc-gprs-field">'
      + '<div class="cc-gprs-field-head"><span class="cc-gprs-label">' + esc(label) + '</span>' + badge(state) + '</div>'
      + body + '</div>';
  }

  function provenanceRow(k, v) {
    if (!hasText(v)) return '';
    return '<div class="cc-prov-row"><div class="cc-prov-key">' + esc(k) + '</div><div class="cc-prov-val">' + esc(v) + '</div></div>';
  }

  function readerHTML(r) {
    var g = buildGPRS(r);
    var color = typeColor(r.Type);
    var meta = [r.Subtype, r.Country].filter(Boolean).join(' · ');
    var linkBtn = (hasText(r.Verified_Link) && r.Verified_Link !== 'none located')
      ? '<button type="button" class="cc-reader-link" data-open-url="' + esc(r.Verified_Link) + '">Open verified site ↗</button>'
      : '<span class="subtle">No verified site located.</span>';

    return ''
      + '<header class="cc-reader-head">'
      +   '<span class="cc-card-type" style="background:' + color + '">' + esc(r.Type || 'Community') + '</span>'
      +   '<h2>' + esc(r.Community_Name) + '</h2>'
      +   '<div class="cc-reader-meta">' + esc(meta) + '</div>'
      +   '<div class="cc-reader-links">' + linkBtn + '</div>'
      + '</header>'

      + '<div class="cc-honesty">This profile is <strong>inferred seed</strong> — assembled from public sources, not yet articulated by the community itself. Each field is badged below; a community can claim and refine its own GPRS.</div>'

      + '<section class="cc-gprs">'
      +   fieldBlock('Goals', g.goals)
      +   fieldBlock('Problems', g.problems)
      +   '<div class="cc-gprs-group"><div class="cc-gprs-group-title">Resources</div>'
      +     fieldBlock('Have', g.resources.have)
      +     fieldBlock('Tap', g.resources.tap)
      +     fieldBlock('Need', g.resources.need)
      +   '</div>'
      +   '<div class="cc-gprs-group"><div class="cc-gprs-group-title">Solutions</div>'
      +     fieldBlock('Effected', g.solutions.effected)
      +     fieldBlock('Proposed', g.solutions.proposed)
      +   '</div>'
      + '</section>'

      + (hasText(r.Narrative_Description)
          ? '<section class="cc-reader-narrative"><h4>Central organizing principle</h4><p>' + esc(r.Narrative_Description) + '</p></section>'
          : '')

      // ── Claim / visibility / progress — designed-in, non-persistent stubs.
      + '<section class="cc-stub" data-cc-stub>'
      +   '<div class="cc-stub-banner">Not yet wired — these arrive with the broker (Pathways 19/20). Nothing here is saved.</div>'
      +   '<button type="button" class="cc-claim-btn" data-cc-claim="' + esc(r.Community_ID) + '">This is our community — claim &amp; refine</button>'
      +   '<div class="cc-vis"><span class="cc-vis-label">Visibility</span>'
      +     '<div class="cc-seg" role="group" aria-label="Visibility (stub)">'
      +       '<button type="button" class="cc-seg-btn active" data-cc-vis="self">Self</button>'
      +       '<button type="button" class="cc-seg-btn" data-cc-vis="peers">Peers</button>'
      +       '<button type="button" class="cc-seg-btn" data-cc-vis="public">Public</button>'
      +     '</div>'
      +   '</div>'
      +   '<div class="cc-progress"><span class="cc-vis-label">Progress (illustrative)</span>'
      +     '<div class="cc-progress-strip">'
      +       '<span class="cc-prog-node done" title="Seed snapshot"></span>'
      +       '<span class="cc-prog-link"></span>'
      +       '<span class="cc-prog-node done" title="Articulated"></span>'
      +       '<span class="cc-prog-link"></span>'
      +       '<span class="cc-prog-node ai" title="AI assistance applied">AI</span>'
      +       '<span class="cc-prog-link"></span>'
      +       '<span class="cc-prog-node" title="Future snapshot"></span>'
      +     '</div>'
      +     '<div class="subtle cc-progress-note">Snapshots over time mark where AI was applied — the Detector half. Real tracking lands with the broker.</div>'
      +   '</div>'
      + '</section>'

      + '<section class="cc-prov"><h4>Provenance</h4>'
      +   provenanceRow('Community ID', r.Community_ID)
      +   provenanceRow('Source directory', r.Source_Directory)
      +   provenanceRow('Source link', r.Source_Link)
      +   provenanceRow('Verification', r.Verification_Method)
      +   provenanceRow('Characterization', r.Narrative_Grounding)
      + '</section>';
  }

  function openReader(id) {
    var r = byId[id];
    var reader = document.getElementById('cc-reader');
    var body = document.getElementById('cc-reader-body');
    if (!r || !reader || !body) return;
    body.innerHTML = readerHTML(r);
    body.scrollTop = 0;
    reader.hidden = false;
    reader.setAttribute('aria-hidden', 'false');
    document.body.classList.add('cc-reader-open');
  }
  function closeReader() {
    var reader = document.getElementById('cc-reader');
    if (!reader) return;
    reader.hidden = true;
    reader.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('cc-reader-open');
  }

  // ── Broker seam: the single place real persistence/sharing drops in. ──
  function brokerStub(action) {
    showToast('“' + action + '” is not yet wired — it arrives with the broker (Pathways 19/20).');
  }

  // ── WIRING ────────────────────────────────────────────────────────────
  function wire() {
    // Card click → open reader (ignore clicks on the external-link affordance,
    // which app.js handles via [data-open-url]).
    document.addEventListener('click', function (e) {
      if (e.target.closest('[data-open-url]')) return;
      if (e.target.closest('[data-cc-reader-close]')) { closeReader(); return; }
      var card = e.target.closest('[data-cc-card-id]');
      if (card) { openReader(card.getAttribute('data-cc-card-id')); return; }

      var claim = e.target.closest('[data-cc-claim]');
      if (claim) { brokerStub('Claim & refine'); return; }
      var vis = e.target.closest('[data-cc-vis]');
      if (vis) {
        var seg = vis.parentElement;
        if (seg) seg.querySelectorAll('.cc-seg-btn').forEach(function (b) { b.classList.toggle('active', b === vis); });
        brokerStub('Set visibility: ' + vis.getAttribute('data-cc-vis'));
        return;
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeReader();
    });

    // Slim chip-row "+ Filter" toggle (own this here; app.js doesn't know it).
    var toggle = document.getElementById('toggle-filter-panel');
    var panel = document.getElementById('filter-panel');
    if (toggle && panel) {
      toggle.addEventListener('click', function () {
        var open = panel.hasAttribute('hidden');
        if (open) panel.removeAttribute('hidden'); else panel.setAttribute('hidden', '');
        toggle.setAttribute('aria-expanded', String(open));
        toggle.classList.toggle('active', open);
      });
    }
  }

  window.CCCards = { render: render };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', wire);
  } else {
    wire();
  }
})();
