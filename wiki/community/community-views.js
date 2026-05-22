'use strict';
/*
 * community-views.js — Map + PRS Triplets views for the C2A2 Community Explorer.
 * Ports the Streamlit map_tab (country-centroid scatter with deterministic
 * jitter) and prs_tab (browsable Problem/Resource/Solution with focus filter)
 * into the static HTML chapter.
 *
 * Decoupled from app.js: it listens for the 'cc:rows' CustomEvent that app.js
 * dispatches at the end of update() with the current filtered slice, so the
 * Map and PRS views always reflect the active filters.
 *
 * DOM contract (provided by index.html):
 *   .cc-tab[data-view="explorer|map|prs"]   - the internal tab bar buttons
 *   #cc-view-explorer / #cc-view-map / #cc-view-prs - view containers
 *   #cc-map, #cc-map-status                  - Leaflet host + caption
 *   #cc-prs-search, .cc-prs-focus[data-focus], #cc-prs-count, #cc-prs-list
 * Data: window.CC_COORDS, window.CC_ALIASES (country_coordinates.js); Leaflet (window.L).
 */
(function () {
  var latestRows = [];
  var mapInited = false, map = null, markerLayer = null;
  var prsFocus = 'all', prsSearch = '';

  var TYPE_COLORS = {
    Academic: '#5A8EAF',
    Corporate: '#C9A84C',
    Ideological: '#4E8A5E',
    Religious: '#A85D3A'
  };
  function typeColor(t) { return TYPE_COLORS[t] || '#9a8f6a'; }

  // Deterministic [0,1) hash from a string seed (FNV-1a-ish), salted per axis.
  function hashFloat(str, salt) {
    var h = (2166136261 ^ salt) >>> 0;
    for (var i = 0; i < str.length; i++) {
      h ^= str.charCodeAt(i);
      h = Math.imul(h, 16777619) >>> 0;
    }
    return (h >>> 0) / 4294967295;
  }
  // Stable jitter in [-0.5,0.5]*scale so co-located communities separate on zoom.
  function jitter(seed, scale) {
    return [(hashFloat(seed, 1) - 0.5) * scale, (hashFloat(seed, 2) - 0.5) * scale];
  }

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function activeView() {
    var b = document.querySelector('.cc-tab.active');
    return b ? b.getAttribute('data-view') : 'cards';
  }

  // ── MAP ──────────────────────────────────────────────────────────────
  function renderMap(rows) {
    var host = document.getElementById('cc-map');
    if (!host) return;
    if (typeof L === 'undefined') {
      host.innerHTML = '<div class="cc-empty">Map library unavailable (no network?). The other views still work.</div>';
      return;
    }
    if (!mapInited) {
      map = L.map(host, { worldCopyJump: true, minZoom: 1, scrollWheelZoom: true }).setView([20, 5], 2);
      L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; OpenStreetMap &copy; CARTO',
        subdomains: 'abcd', maxZoom: 19
      }).addTo(map);
      markerLayer = L.layerGroup().addTo(map);
      mapInited = true;
    }
    markerLayer.clearLayers();
    var coords = window.CC_COORDS || {}, aliases = window.CC_ALIASES || {};
    var mapped = 0;
    rows.forEach(function (r) {
      var country = aliases[r.Country] || r.Country;
      var base = coords[country];
      if (!base) return;
      var wide = (r.Country === 'Global' || r.Country === 'Unspecified');
      var j = jitter(String(r.Community_ID || r.Community_Name || ''), wide ? 2.4 : 1.2);
      var color = typeColor(r.Type);
      var m = L.circleMarker([base[0] + j[0], base[1] + j[1]], {
        radius: 5, color: '#0a0a0f', weight: 1, fillColor: color, fillOpacity: 0.85
      });
      var link = (r.Verified_Link && r.Verified_Link !== 'none located')
        ? '<br><a href="' + esc(r.Verified_Link) + '" target="_blank" rel="noopener">Open website</a>' : '';
      m.bindPopup('<b>' + esc(r.Community_Name) + '</b><br>'
        + esc([r.Type, r.Subtype].filter(Boolean).join(' / ')) + '<br>'
        + esc(r.Country) + link);
      markerLayer.addLayer(m);
      mapped++;
    });
    var status = document.getElementById('cc-map-status');
    if (status) {
      status.textContent = mapped + ' of ' + rows.length
        + ' communities placed near their country centroid (points scatter on zoom; those without a known centroid are omitted).';
    }
    // Leaflet needs a size recalc when its container was hidden at init.
    setTimeout(function () { if (map) map.invalidateSize(); }, 0);
  }

  // ── PRS TRIPLETS ─────────────────────────────────────────────────────
  function prsMatches(r) {
    if (!prsSearch) return true;
    var blob = [r.Community_Name, r.Subtype, r.Problem_Statement, r.Resource_Statement, r.Solution_Statement]
      .join(' ').toLowerCase();
    return prsSearch.toLowerCase().split(/\s+/).every(function (t) { return !t || blob.indexOf(t) >= 0; });
  }
  function block(cls, label, txt) {
    if (!txt) return '';
    return '<div class="prs-card ' + cls + '"><span class="label">' + label + '</span><p>' + esc(txt) + '</p></div>';
  }
  function prsCard(r) {
    var meta = [r.Type, r.Subtype].filter(Boolean).join(' / ') + (r.Country ? ' · ' + r.Country : '');
    var head = '<div class="cc-prs-head"><strong>' + esc(r.Community_Name) + '</strong>'
      + '<span class="cc-prs-meta">' + esc(meta) + '</span></div>';
    var parts = '';
    if (prsFocus === 'all' || prsFocus === 'problems') parts += block('problem', 'Problem', r.Problem_Statement);
    if (prsFocus === 'all' || prsFocus === 'resources') parts += block('resource', 'Resource', r.Resource_Statement);
    if (prsFocus === 'all' || prsFocus === 'solutions') parts += block('solution', 'Solution', r.Solution_Statement);
    return '<div class="cc-prs-item">' + head + '<div class="prs-grid">' + parts + '</div></div>';
  }
  function renderPRS(rows) {
    var list = document.getElementById('cc-prs-list');
    if (!list) return;
    var filtered = rows.filter(prsMatches);
    var LIMIT = 150;
    var shown = filtered.slice(0, LIMIT);
    list.innerHTML = shown.map(prsCard).join('') || '<div class="cc-empty">No PRS records match the current filters and search.</div>';
    var count = document.getElementById('cc-prs-count');
    if (count) {
      count.textContent = filtered.length + ' communities'
        + (filtered.length > LIMIT ? ' (showing first ' + LIMIT + ')' : '');
    }
  }

  // ── TABS ─────────────────────────────────────────────────────────────
  function renderActive() {
    var v = activeView();
    if (v === 'map') renderMap(latestRows);
    else if (v === 'prs') renderPRS(latestRows);
    else if (v === 'cards' && window.CCCards && window.CCCards.render) window.CCCards.render(latestRows);
    // 'overview' content is rendered by app.js on every update(); nothing to do here.
  }
  function switchView(view) {
    document.querySelectorAll('.cc-tab').forEach(function (b) {
      b.classList.toggle('active', b.getAttribute('data-view') === view);
    });
    ['cards', 'map', 'prs', 'overview'].forEach(function (k) {
      var el = document.getElementById('cc-view-' + k);
      if (el) el.hidden = (k !== view);
    });
    renderActive();
  }
  function wire() {
    document.querySelectorAll('.cc-tab').forEach(function (b) {
      b.addEventListener('click', function () { switchView(b.getAttribute('data-view')); });
    });
    document.querySelectorAll('.cc-prs-focus').forEach(function (b) {
      b.addEventListener('click', function () {
        prsFocus = b.getAttribute('data-focus');
        document.querySelectorAll('.cc-prs-focus').forEach(function (x) { x.classList.toggle('active', x === b); });
        renderPRS(latestRows);
      });
    });
    var ps = document.getElementById('cc-prs-search');
    if (ps) ps.addEventListener('input', function () { prsSearch = ps.value.trim(); renderPRS(latestRows); });
  }

  document.addEventListener('cc:rows', function (e) {
    latestRows = (e.detail && e.detail.rows) || [];
    renderActive();
  });
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', wire);
  } else {
    wire();
  }
})();
