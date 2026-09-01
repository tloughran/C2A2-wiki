#!/usr/bin/env python3
"""
generate_prs_3d.py — Rebuild prs_3d.html from extracted vault data.

Strategy: TEMPLATE INJECTION. We start from the existing prs_3d.html (which holds
the proven Three.js scene) and (a) swap the data arrays for fresh vault data and
(b) add a first-class COILS layer (distinguished cyan arcs + legend count + a
left-panel toggle) by mirroring the existing cross-connection arc machinery.

Every edit is a fail-loud, single-match replacement: if an anchor is missing or
ambiguous the script raises instead of producing a silently-broken file.

Usage:
  python3 generate_prs_3d.py <prs_data.json> <template_prs_3d.html> <out.html>
"""
import datetime
import json
import re
import sys


def jsdata(obj):
    """Serialize for safe embedding inside a <script> tag."""
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")


def replace_once(text, pattern, repl, label, flags=0):
    # repl may be a literal string OR a callable(match)->str. Either way the
    # returned text is used literally (no backreference expansion), which is what
    # we want because the JSON payload contains backslashes (e.g. '<\\/').
    fn = repl if callable(repl) else (lambda m: repl)
    new, n = re.subn(pattern, fn, text, flags=flags)
    if n != 1:
        raise SystemExit("FAIL: anchor '%s' matched %d times (expected 1)" % (label, n))
    return new


# ---- injected JS: the coil layer (single-brace JS per CLAUDE.md template rules) ----
COIL_FUNCS = r"""
// == SYNERGISTIC COIL LINES (structural-bridge cross-connections) ==
function buildCoilLines() {
  var thinkerResourceIdx = {};
  meshes.forEach(function(m, i) {
    if (m.userData.type === 'prs' && m.userData.prsType === 'resource'
        && thinkerResourceIdx[m.userData.thinker] === undefined) {
      thinkerResourceIdx[m.userData.thinker] = i;
    }
  });
  COILS.forEach(function(coil) {
    var cy = yearToZ(coil.year || maxYear);  // coil sits at its discovery-year altitude
    var progs = (coil.programs || '').split(',').map(function(p) {
      return p.trim().replace(/ Agent$/, '').replace(/ \(.*$/, '').toLowerCase();
    });
    var thinkers = progs.filter(function(p) { return THINKER_COLORS[p]; });
    for (var i = 0; i < thinkers.length; i++) {
      for (var j = i + 1; j < thinkers.length; j++) {
        var a = thinkerResourceIdx[thinkers[i]];
        var b = thinkerResourceIdx[thinkers[j]];
        if (a === undefined || b === undefined) continue;
        var pa = meshes[a].position, pb = meshes[b].position;
        var p1 = new THREE.Vector3(pa.x, cy, pa.z);
        var p2 = new THREE.Vector3(pb.x, cy, pb.z);
        var mid = p1.clone().add(p2).multiplyScalar(0.5);
        mid.y += 4;  // gentle arch within the discovery-year band
        var curve = new THREE.QuadraticBezierCurve3(p1, mid, p2);
        var arcGeo = new THREE.BufferGeometry().setFromPoints(curve.getPoints(24));
        var arcMat = new THREE.LineBasicMaterial({
          color: 0x3FE0D0, transparent: true, opacity: 0.55
        });
        var arc = new THREE.Line(arcGeo, arcMat);
        arc.userData = {
          type: 'coil', coil: coil,
          thinker1: thinkers[i], thinker2: thinkers[j],
          mesh1: meshes[a], mesh2: meshes[b]
        };
        scene.add(arc);
        coilLines.push(arc);
      }
    }
  });
}

function prsToggleCoils(checked) {
  showCoils = checked;
  applyPRSFilters();
}

// == DIRECTED GENERATIVE COILS (a solution feeding another tradition's resource) ==
function buildGenerativeChains() {
  var solNode = {}, resNode = {};
  meshes.forEach(function(m) {
    if (m.userData.type === 'prs' && m.userData.triplet) {
      if (m.userData.prsType === 'solution') solNode[m.userData.triplet.id] = m;
      if (m.userData.prsType === 'resource') resNode[m.userData.triplet.id] = m;
    }
  });
  GENERATIVE.forEach(function(gc) {
    var s = solNode[gc.source], r = resNode[gc.target];
    if (!s || !r) return;
    var geo = new THREE.BufferGeometry().setFromPoints([s.position.clone(), r.position.clone()]);
    var c1 = new THREE.Color(0x6A3A12), c2 = new THREE.Color(0xF09A3C);  // dim source -> bright target = direction
    geo.setAttribute('color', new THREE.Float32BufferAttribute([c1.r, c1.g, c1.b, c2.r, c2.g, c2.b], 3));
    var mat = new THREE.LineBasicMaterial({ vertexColors: true, transparent: true, opacity: 0.5 });
    var line = new THREE.Line(geo, mat);
    line.userData = { type: 'generative', chain: gc, mesh1: s, mesh2: r };
    scene.add(line);
    generativeLines.push(line);
  });
}

function prsToggleGenerative(checked) {
  showGenerative = checked;
  applyPRSFilters();
}

// == BRIGHTNESS + TIME SLIDER (control schema mirrored from the Sociogram) ==
function setBrightness(v) {
  var cc = document.getElementById('canvas-container');
  if (cc) cc.style.filter = 'brightness(' + v + ')';
}

function setYearThreshold(v) {
  v = parseInt(v, 10);
  yearThreshold = v;
  var lbl = document.getElementById('prs-year-slider-label');
  if (lbl) lbl.textContent = (v <= minYear) ? 'all years' : ('≥ ' + v);
  applyPRSFilters();
}

function prsTogglePop(id, ev) {
  if (ev) ev.stopPropagation();
  var pop = document.getElementById(id);
  if (!pop) return;
  var open = pop.style.display === 'block';
  var all = document.querySelectorAll('.prs-pop');
  for (var i = 0; i < all.length; i++) all[i].style.display = 'none';
  pop.style.display = open ? 'none' : 'block';
}

"""

COIL_FILTER_PASS = r"""
  // Pass 3 - coils: their own gate; never connect to a hidden node.
  coilLines.forEach(function(l) {
    if (!showCoils) { l.visible = false; return; }
    var cm1 = l.userData && l.userData.mesh1;
    var cm2 = l.userData && l.userData.mesh2;
    l.visible = !!(cm1 && cm2 && cm1.visible && cm2.visible);
  });
  // Pass 4 - generative chains: own gate; endpoints must be visible.
  generativeLines.forEach(function(l) {
    if (!showGenerative) { l.visible = false; return; }
    var gm1 = l.userData && l.userData.mesh1;
    var gm2 = l.userData && l.userData.mesh2;
    l.visible = !!(gm1 && gm2 && gm1.visible && gm2.visible);
  });
"""

NEW_LEGEND = r"""function buildLegend() {
  var legendEl = document.getElementById('legend');
  var html = '<h4>Node Shapes</h4>';
  html += '<div class="legend-item"><span style="color:#E87070;font-size:14px">&#9670;</span> Problem</div>';
  html += '<div class="legend-item"><span style="color:#7AB0CF;font-size:14px">&#9679;</span> Resource</div>';
  html += '<div class="legend-item"><span style="color:#5DC0AB;font-size:14px">&#11206;</span> Solution</div>';
  html += '<h4 style="margin-top:10px">Connections</h4>';
  html += '<div class="legend-item"><span style="color:#3FE0D0;font-size:15px">&#10026;</span> Synergistic coil (' + (typeof COILS !== 'undefined' ? COILS.length : 0) + ')</div>';
  html += '<div class="legend-item"><span style="color:#C9A84C;font-size:15px">&#8722;</span> Cross-tradition link</div>';
  var nConv = 0; for (var k in resourceTraditions) { if (Object.keys(resourceTraditions[k]).length >= 2) nConv++; }
  html += '<div class="legend-item"><span style="color:#C9A84C;font-size:15px">&#9673;</span> Convergence hub &#8212; resource shared across &#8805;2 traditions (' + nConv + ')</div>';
  html += '<div class="legend-item"><span style="color:#F09A3C;font-size:15px">&#8594;</span> Generative coil &#8212; a solution feeding a downstream resource (' + (typeof GENERATIVE !== 'undefined' ? GENERATIVE.length : 0) + ')</div>';
  legendEl.innerHTML = html;
}"""

COIL_CHECKBOX = """  <div class="prs-filter-item">
    <input type="checkbox" id="prs-chk-edges" checked onchange="prsToggleEdges(this.checked)">
    <span class="prs-filter-label" style="font-weight:600">Edges (threads)</span>
  </div>
  <div class="prs-filter-item">
    <input type="checkbox" id="prs-chk-coils" checked onchange="prsToggleCoils(this.checked)">
    <span class="prs-filter-dot" style="background:#3FE0D0"></span>
    <span class="prs-filter-label" style="font-weight:600">Coils</span>
  </div>
  <div class="prs-filter-item">
    <input type="checkbox" id="prs-chk-generative" checked onchange="prsToggleGenerative(this.checked)">
    <span class="prs-filter-dot" style="background:#F09A3C"></span>
    <span class="prs-filter-label" style="font-weight:600">Generative</span>
  </div>
"""


# ---- Edge-picking (Tom 2026-05-20): click a coil/cross/generative edge for info ----
OLD_ONCLICK = '''function onClick(e) {
  var rect = renderer.domElement.getBoundingClientRect();
  mouse.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
  mouse.y = -((e.clientY - rect.top) / rect.height) * 2 + 1;
  raycaster.setFromCamera(mouse, camera);

  var intersects = raycaster.intersectObjects(meshes);

  if (intersects.length > 0) {
    var hit = intersects[0].object;
    if (hit.userData.type === 'prs') {
      showNodeInfo(hit);
    }
  } else {
    closePanel();
  }
}'''

NEW_ONCLICK = '''function onClick(e) {
  var rect = renderer.domElement.getBoundingClientRect();
  mouse.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
  mouse.y = -((e.clientY - rect.top) / rect.height) * 2 + 1;
  raycaster.setFromCamera(mouse, camera);
  prsClosePops();
  // Nodes take priority; fall through to edges (coils, generative, threads/cross).
  var nodeHits = raycaster.intersectObjects(meshes);
  if (nodeHits.length > 0 && nodeHits[0].object.userData.type === 'prs') {
    if (selectedMesh === nodeHits[0].object) { closePanel(); return; }
    showNodeInfo(nodeHits[0].object);
    return;
  }
  var edgeHits = raycaster.intersectObjects(coilLines.concat(generativeLines, threadLines));
  if (edgeHits.length > 0) {
    showEdgeInfo(edgeHits[0].object);
    return;
  }
  closePanel();
}'''

SHOW_EDGE_INFO = r'''function prsClosePops() {
  var all = document.querySelectorAll('.prs-pop');
  for (var i = 0; i < all.length; i++) all[i].style.display = 'none';
}
function prsCollapseFilters() {
  var lp = document.getElementById('prs-left-page');
  if (lp) lp.style.display = 'block';
}
function prsExpandFilters() {
  var lp = document.getElementById('prs-left-page');
  if (lp) lp.style.display = 'none';
}
function narrativeHTML(triplet, thinker) {
  var tn = THINKER_DISPLAY[thinker] || thinker;
  var tc = THINKER_COLORS[thinker] || '#888';
  var disc = THINKER_DISC[thinker] || '';
  var h = '<h3>' + (triplet.label || triplet.id) + '</h3>';
  h += '<span class="thinker-tag" style="background:' + tc + '33;color:' + tc + '">' + tn + '</span>';
  h += '<div class="field-label">Discipline</div><div class="field-value">' + disc + '</div>';
  h += '<div class="field-label">Problem</div><div class="field-value">' + (triplet.problem || '') + '</div>';
  h += '<div class="field-label">Resource</div><div class="field-value">' + (triplet.resource || '') + '</div>';
  h += '<div class="field-label">Solution</div><div class="field-value">' + (triplet.solution || '') + '</div>';
  h += '<div class="field-label">Publication Year</div><div class="field-value">' + (triplet.pub_year || 'Unknown') + '</div>';
  return h;
}
function edgeLabelHTML(d) {
  var txt = 'PRS thread', col = '#888';
  if (d.type === 'coil' && d.coil) { col = '#3FE0D0'; txt = 'Synergistic coil &#8212; ' + (d.coil.nature || '') + (d.coil.year ? ' &#183; ' + d.coil.year : ''); }
  else if (d.type === 'generative') { col = '#F09A3C'; txt = 'Generative coil &#8212; solution &#8594; resource'; }
  else if (d.type === 'cross' && d.finding) { col = '#C9A84C'; txt = 'Cross-tradition link &#8212; ' + (d.finding.type || ''); }
  return '<div style="font-size:11px;color:' + col + ';border-bottom:1px solid #2a2a3e;padding-bottom:6px;margin-bottom:8px">' + txt + '</div>';
}
function showEdgeInfo(edge) {
  var d = edge.userData;
  var m1 = d.mesh1, m2 = d.mesh2;
  var t1 = (m1 && m1.userData) ? m1.userData.triplet : null;
  var t2 = (m2 && m2.userData) ? m2.userData.triplet : null;
  var th1 = (m1 && m1.userData) ? m1.userData.thinker : null;
  var th2 = (m2 && m2.userData) ? m2.userData.thinker : null;
  var rightPanel = document.getElementById('info-panel');
  var rightContent = document.getElementById('info-content');
  var leftPage = document.getElementById('prs-left-page');
  var leftContent = document.getElementById('prs-left-page-content');
  var header = edgeLabelHTML(d);
  if (t1 && t2 && t1.id !== t2.id && leftPage && leftContent) {
    selectedMesh = null;
    leftContent.innerHTML = header + '<div class="field-label">Source narrative</div>' + narrativeHTML(t1, th1);
    rightContent.innerHTML = header + '<div class="field-label">Target narrative</div>' + narrativeHTML(t2, th2);
    prsCollapseFilters();
    leftPage.style.display = 'block';
    rightPanel.style.display = 'block';
  } else if (m1) {
    showNodeInfo(m1);
  }
}

'''


def parse_tau(argv):
    """--tau <days|linear>. Returns (value_or_None, remaining_argv).

    The template ships TAU_DAYS = 90, chosen for a corpus that lives in the last
    three months. That is a PRIOR, not a neutral axis: it spends the column on
    whatever is most recent. On a long-baseline corpus it crushes the old material
    into a mat on the floor -- measured 2026-09-01, a 32-year tradition got 1.66 of
    40 units against 22.66 for a 13-year one, a 33x rate distortion that renders the
    comparison backwards. tau is therefore a per-corpus choice. Default stays 90 so
    the live build is unchanged; 'linear' (tau -> inf) is the regression control.
    """
    rest, tau = [], None
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--tau" and i + 1 < len(argv):
            tau, i = argv[i + 1], i + 2
            continue
        if a.startswith("--tau="):
            tau, i = a.split("=", 1)[1], i + 1
            continue
        rest.append(a)
        i += 1
    if tau is None:
        return None, rest
    if tau.lower() in ("linear", "inf", "infinity"):
        return 1e9, rest
    try:
        v = float(tau)
    except ValueError:
        raise SystemExit("FAIL: --tau expects a number of days or 'linear', got %r" % tau)
    if v <= 0:
        raise SystemExit("FAIL: --tau must be positive, got %r" % tau)
    return v, rest


def baseline_years(triplets):
    """Span of the corpus in years, from the dates the renderer actually places on."""
    ds = []
    for t in triplets:
        d = (t.get("date") or "")[:10]
        try:
            ds.append(datetime.date.fromisoformat(d).toordinal())
        except ValueError:
            continue
    return (max(ds) - min(ds)) / 365.25 if len(ds) >= 2 else 0.0


def main():
    tau, argv = parse_tau(sys.argv[1:])
    if len(argv) != 3:
        raise SystemExit("usage: generate_prs_3d.py [--tau days|linear] "
                         "<prs_data.json> <template.html> <out.html>")
    data = json.load(open(argv[0], encoding="utf-8"))
    html = open(argv[1], encoding="utf-8").read()

    if tau is not None:
        html = replace_once(html, r"^var TAU_DAYS = .*;[ \t]*$",
                            "var TAU_DAYS = %r;" % tau, "axis:TAU_DAYS", flags=re.M)

    # 1) Swap data arrays (single-line `var NAME = ...;`).
    for name in ["DISCIPLINES", "THINKER_DISC", "THINKER_COLORS", "THINKER_DISPLAY",
                 "PRS_TRIPLETS", "CROSS_CONNECTIONS", "FINDINGS"]:
        html = replace_once(
            html, r"^var " + name + r" = .*;[ \t]*$",
            "var " + name + " = " + jsdata(data[name]) + ";",
            "data:" + name, flags=re.M)

    # 2) Inject COILS right after the FINDINGS array line.
    extra_js = ("\nvar COILS = " + jsdata(data["COILS"]) + ";"
                + "\nvar GENERATIVE = " + jsdata(data.get("GENERATIVE", [])) + ";")
    html = replace_once(
        html, r"^var FINDINGS = .*;[ \t]*$",
        lambda m: m.group(0) + extra_js,
        "insert:COILS+GEN", flags=re.M)

    # 3) Globals for the coil layer.
    html = replace_once(
        html, r"^var showThreads = true;[ \t]*$",
        "var showThreads = true;\nvar showCoils = true;\nvar coilLines = [];\nvar showGenerative = true;\nvar generativeLines = [];\nvar yearThreshold = null;",
        "globals:coils", flags=re.M)

    # 4) Call buildCoilLines() after the cross-connection build.
    html = replace_once(
        html, r"^  buildCrossConnectionLines\(\);[ \t]*$",
        "  buildCrossConnectionLines();\n  buildCoilLines();\n  buildGenerativeChains();",
        "init:buildCoilLines", flags=re.M)

    # 5) Define the coil functions just before the THREADS VISIBILITY marker.
    html = replace_once(
        html, r"// .{0,4} THREADS VISIBILITY .{0,4}\n",
        COIL_FUNCS + "// -- THREADS VISIBILITY --\n",
        "funcs:coils")

    # 6) Add the coil visibility pass to applyPRSFilters (anchor on Pass-2 block).
    pass2_anchor = ("  threadLines.forEach(function(l) {\n"
                    "    if (!showThreads) { l.visible = false; return; }\n"
                    "    var m1 = l.userData && l.userData.mesh1;\n"
                    "    var m2 = l.userData && l.userData.mesh2;\n"
                    "    // Both endpoints must exist and be visible after Pass 1.\n"
                    "    l.visible = !!(m1 && m2 && m1.visible && m2.visible);\n"
                    "  });\n")
    if html.count(pass2_anchor) != 1:
        raise SystemExit("FAIL: applyPRSFilters Pass-2 anchor not uniquely found")
    html = html.replace(pass2_anchor, pass2_anchor + COIL_FILTER_PASS, 1)

    # 7) Replace buildLegend with the version that lists coil/cross counts.
    old_legend = ("function buildLegend() {\n"
                  "  var legendEl = document.getElementById('legend');\n"
                  "  var html = '<h4>Node Shapes</h4>';\n"
                  "  html += '<div class=\"legend-item\"><span style=\"color:#E87070;font-size:14px\">&#9670;</span> Problem</div>';\n"
                  "  html += '<div class=\"legend-item\"><span style=\"color:#7AB0CF;font-size:14px\">&#9679;</span> Resource</div>';\n"
                  "  html += '<div class=\"legend-item\"><span style=\"color:#5DC0AB;font-size:14px\">&#11206;</span> Solution</div>';\n"
                  "  legendEl.innerHTML = html;\n"
                  "}")
    if html.count(old_legend) != 1:
        raise SystemExit("FAIL: buildLegend anchor not uniquely found")
    html = html.replace(old_legend, NEW_LEGEND, 1)

    # 8) Add the coil toggle checkbox under the Edges section.
    edges_anchor = ("  <div class=\"prs-filter-item\">\n"
                    "    <input type=\"checkbox\" id=\"prs-chk-edges\" checked onchange=\"prsToggleEdges(this.checked)\">\n"
                    "    <span class=\"prs-filter-label\" style=\"font-weight:600\">Edges (threads)</span>\n"
                    "  </div>\n")
    if html.count(edges_anchor) != 1:
        raise SystemExit("FAIL: Edges checkbox anchor not uniquely found")
    html = html.replace(edges_anchor, COIL_CHECKBOX, 1)

    # 8b) Convergence: cross-tradition shared-resource hubs (data + helper).
    rc_anchor = ("var resourceConnections = {};\n"
                 "PRS_TRIPLETS.forEach(function(t) {\n"
                 "  var rKey = t.resource.toLowerCase().trim().slice(0, 60);\n"
                 "  if (!resourceConnections[rKey]) resourceConnections[rKey] = [];\n"
                 "  resourceConnections[rKey].push(t.id);\n"
                 "});\n")
    conv_data = ("var resourceTraditions = {};\n"
                 "PRS_TRIPLETS.forEach(function(t) {\n"
                 "  var rKey = t.resource.toLowerCase().trim().slice(0, 60);\n"
                 "  if (!resourceTraditions[rKey]) resourceTraditions[rKey] = {};\n"
                 "  resourceTraditions[rKey][t.thinker] = true;\n"
                 "});\n"
                 "function convergenceCount(rKey) { return Object.keys(resourceTraditions[rKey] || {}).length; }\n")
    if html.count(rc_anchor) != 1:
        raise SystemExit("FAIL: resourceConnections anchor not uniquely found")
    html = html.replace(rc_anchor, rc_anchor + conv_data, 1)

    # 8c) Convergence: emphasize hub resource nodes (gold glow + slight scale).
    ud_anchor = ("      mesh.userData = {\n"
                 "        type: 'prs',\n"
                 "        prsType: pType,\n"
                 "        triplet: triplet,\n"
                 "        text: prsTexts[pi],\n"
                 "        thinker: triplet.thinker,\n"
                 "      };\n"
                 "      scene.add(mesh);\n")
    ud_new = ("      mesh.userData = {\n"
              "        type: 'prs',\n"
              "        prsType: pType,\n"
              "        triplet: triplet,\n"
              "        text: prsTexts[pi],\n"
              "        thinker: triplet.thinker,\n"
              "      };\n"
              "      if (pType === 'resource') {\n"
              "        var rk = triplet.resource.toLowerCase().trim().slice(0, 60);\n"
              "        var ct = convergenceCount(rk);\n"
              "        if (ct >= 2) {\n"
              "          mesh.userData.convergence = ct;\n"
              "          mat.emissive = new THREE.Color(0xC9A84C).multiplyScalar(0.35 + 0.12 * Math.min(ct, 4));\n"
              "          mesh.scale.multiplyScalar(1.25);\n"
              "        }\n"
              "      }\n"
              "      scene.add(mesh);\n")
    if html.count(ud_anchor) != 1:
        raise SystemExit("FAIL: mesh.userData anchor not uniquely found")
    html = html.replace(ud_anchor, ud_new, 1)

    # 9) Rename the view -> Narrative (PRS) Connectome (page <title> and <h1>).
    html = replace_once(html, re.escape("C2A2 — 3D PRS Landscape"),
                        "C2A2 — Narrative (PRS) Connectome", "rename:title")
    html = replace_once(html, re.escape("C2A2 &mdash; 3D PRS Landscape"),
                        "C2A2 &mdash; Narrative (PRS) Connectome", "rename:h1")

    # 10) Layer fix (Tom 2026-05-20): the 3D vis should ride OVER the legend.
    #     Make the canvas transparent (body is already #0a0a0f) so the legend
    #     reads BEHIND the nodes instead of being hidden by an opaque scene bg.
    html = replace_once(
        html, re.escape("scene.background = new THREE.Color(0x0a0a0f);"),
        "scene.background = null;  // transparent: vis composites over the legend",
        "layer:scene-bg")
    html = replace_once(
        html, re.escape("border-radius: 8px;\n  padding: 12px 14px;\n  z-index: 90;"),
        "border-radius: 8px;\n  padding: 12px 14px;\n  z-index: -1;",
        "layer:legend-z")

    # 11) Cleanup controls (Tom 2026-05-20): brightness filter + year-threshold slider.
    # 11a) default canvas brightness so the muted palette reads less dim.
    html = replace_once(
        html,
        re.escape("#canvas-container {\n  position: absolute;\n  top: 0; left: 0; right: 0; bottom: 0;\n  overflow: hidden;\n}"),
        "#canvas-container {\n  position: absolute;\n  top: 0; left: 0; right: 0; bottom: 0;\n  overflow: hidden;\n  filter: brightness(1.35);\n}",
        "ctrl:canvas-brightness")
    # 11b) year-threshold cut folded into the node-visibility predicate.
    html = replace_once(
        html,
        re.escape("    if (prsYearState[dec] === false) return false;\n  }\n  return true;\n}"),
        "    if (prsYearState[dec] === false) return false;\n  }\n  if (yearThreshold && triplet && triplet.pub_year && triplet.pub_year < yearThreshold) return false;\n  return true;\n}",
        "ctrl:year-cut")
    # 11c) initialise the year slider range from the data + sync brightness on load.
    html = replace_once(
        html, r"^  buildLegend\(\);[ \t]*$",
        "  buildLegend();\n"
        "  var _ys = document.getElementById('prs-year-slider'); if (_ys) { _ys.min = minYear; _ys.max = maxYear; _ys.value = minYear; }\n"
        "  var _b = document.getElementById('prs-brightness'); if (_b) setBrightness(_b.value);",
        "ctrl:slider-init", flags=re.M)
    # 11d) header controls: brightness + year sliders beside Labels.
    html = replace_once(
        html,
        re.escape('    <button id="btn-labels" onclick="toggleLabels()" class="active">Labels</button>'),
        '    <button id="btn-labels" onclick="toggleLabels()" class="active">Labels</button>\n'
        '    <span style="margin-left:12px;font-size:11px;color:#9a9a9a">Bright</span>\n'
        '    <input type="range" id="prs-brightness" min="0.6" max="2.5" step="0.05" value="1.35" style="vertical-align:middle;width:80px" oninput="setBrightness(this.value)">\n'
        '    <span style="margin-left:12px;font-size:11px;color:#9a9a9a">Year &#8805;</span>\n'
        '    <input type="range" id="prs-year-slider" min="0" max="0" value="0" step="1" style="vertical-align:middle;width:90px" oninput="setYearThreshold(this.value)">\n'
        '    <span id="prs-year-slider-label" style="font-size:11px;color:#9a9a9a">all years</span>',
        "ctrl:header-sliders")

    # 12) Edge-picking: raycast the edge lines (nodes still take priority).
    html = replace_once(
        html, re.escape("  raycaster.params.Points = { threshold: 0.5 };"),
        "  raycaster.params.Points = { threshold: 0.5 };\n  raycaster.params.Line = { threshold: 1.0 };",
        "edge:raycaster")
    html = replace_once(html, re.escape(OLD_ONCLICK), NEW_ONCLICK, "edge:onclick")
    html = replace_once(
        html, re.escape("function closePanel() {"),
        SHOW_EDGE_INFO + "function closePanel() {", "edge:showEdgeInfo")
    # 12b) Two-panel edge cluster (Sociogram parity): filters expand on node, collapse on edge.
    html = replace_once(
        html,
        re.escape("function showNodeInfo(mesh) {\n  selectedMesh = mesh;"),
        "function showNodeInfo(mesh) {\n  prsExpandFilters();\n  selectedMesh = mesh;",
        "edge:node-expand")
    html = replace_once(
        html,
        re.escape("function closePanel() {\n  document.getElementById('info-panel').style.display = 'none';"),
        "function closePanel() {\n  document.getElementById('info-panel').style.display = 'none';\n  prsExpandFilters();",
        "edge:close-expand")
    html = replace_once(
        html,
        re.escape('<div style="flex:1;position:relative;overflow:hidden">'),
        '<div id="prs-left-page" style="display:none"><button class="close-btn" onclick="closePanel()" style="position:absolute;top:8px;right:10px;z-index:1;background:none;border:none;color:#888;font-size:18px;cursor:pointer">&times;</button><div id="prs-left-page-content"></div></div>\n<div style="flex:1;position:relative;overflow:hidden">',
        "edge:left-page-html")
    html = replace_once(
        html,
        re.escape("#prs-left-panel {"),
        "#prs-left-page { position:absolute; left:0; top:0; bottom:0; width:320px; background:#0e0e16; border-right:1px solid #1a1a2e; overflow-y:auto; padding:12px; z-index:150; }\n"
        "#prs-left-page h3 { color:#f0f0f0; font-size:14px; margin:6px 0; }\n"
        "#prs-left-page .field-label { color:#888; font-size:10px; text-transform:uppercase; letter-spacing:1px; margin-top:10px; }\n"
        "#prs-left-page .field-value { color:#c0c0c0; font-size:12px; line-height:1.5; }\n"
        "#prs-left-page .thinker-tag { display:inline-block; padding:2px 8px; border-radius:10px; font-size:11px; margin:2px 4px 2px 0; }\n"
        "#prs-left-panel {",
        "edge:left-page-css")

    # 13) "?" help pop-ups (Tom 2026-05-20): title + legend, click-on/click-off toggle.
    html = replace_once(
        html, re.escape("  max-height: 300px;\n  overflow-y: auto;\n}"),
        "  max-height: 300px;\n  overflow-y: auto;\n}\n"
        ".prs-pop-btn { background:#1a1a2e; color:#C9A84C; border:1px solid #2a2a3e; border-radius:50%; width:18px; height:18px; font-size:11px; line-height:16px; cursor:pointer; padding:0; margin-left:6px; }\n"
        ".prs-pop-btn:hover { background:#2a2a3e; }\n"
        ".prs-pop { position:absolute; background:rgba(12,12,20,0.96); backdrop-filter:blur(8px); border:1px solid #2a2a3e; border-radius:8px; padding:12px 14px; font-size:11px; line-height:1.5; max-width:320px; z-index:400; color:#d0d0d0; }\n"
        ".prs-pop h4 { margin:0 0 6px 0; color:#C9A84C; font-size:12px; }\n"
        ".prs-pop b { color:#f0f0f0; }",
        "pop:css")
    html = replace_once(
        html, re.escape('  <div class="controls">'),
        '  <button class="prs-pop-btn" title="What is this view?" onclick="prsTogglePop(\'prs-title-pop\', event)">?</button>\n  <div class="controls">',
        "pop:title-btn")
    html = replace_once(
        html, re.escape('<div id="tooltip"></div>'),
        '<div id="tooltip"></div>\n'
        '<div id="prs-title-pop" class="prs-pop" style="display:none;top:54px;left:24px">'
        '<h4>Narrative (PRS) Connectome</h4>'
        '<p>Each <b>node</b> is an agentic PRS narrative &#8212; a small model (problem &#8594; resource &#8594; solution). '
        '<b>Edges</b> wire narratives together: shared threads within a tradition; across traditions, the <b>coils</b> (association fibers). '
        'Read it as the emergence of rival <b>master sciences</b>. Axes: angle = discipline, height = year.</p>'
        '</div>'
        '<div id="prs-legend-pop" class="prs-pop" style="display:none;bottom:54px;left:24px">'
        '<h4>Legend key</h4>'
        '<p><b>Problem / Resource / Solution</b> &#8212; the three node shapes of one narrative.</p>'
        '<p><b>Synergistic coil</b> (teal) &#8212; a cross-tradition bridge: a shared resource linking programs, placed at its discovery year.</p>'
        '<p><b>Cross-tradition link</b> (gold) &#8212; a finding-driven connection between traditions.</p>'
        '<p><b>Convergence hub</b> (gold glow) &#8212; a resource shared across &#8805;2 traditions; a candidate master-science seed.</p>'
        '<p><b>Generative coil</b> (orange &#8594;) &#8212; one narrative\'s solution feeding another\'s resource: the directed spiral.</p>'
        '</div>',
        "pop:divs")
    # 13b) Legend "?" must float ABOVE the canvas (legend body sits behind it at z -1).
    html = replace_once(
        html,
        re.escape('<div id="prs-legend-pop" class="prs-pop" style="display:none;bottom:54px;left:24px">'),
        '<button id="prs-legend-help-btn" class="prs-pop-btn" title="Legend key" style="position:absolute;display:none;z-index:401" onclick="prsTogglePop(\'prs-legend-pop\', event)">?</button>\n<div id="prs-legend-pop" class="prs-pop" style="display:none;bottom:54px;left:24px">',
        "pop:legend-floatbtn")
    html = replace_once(
        html,
        re.escape("  var _b = document.getElementById('prs-brightness'); if (_b) setBrightness(_b.value);"),
        "  var _b = document.getElementById('prs-brightness'); if (_b) setBrightness(_b.value);\n"
        "  var _lg = document.getElementById('legend'); var _lb = document.getElementById('prs-legend-help-btn');\n"
        "  if (_lg && _lb) { _lb.style.left = (_lg.offsetLeft + 4) + 'px'; _lb.style.top = (_lg.offsetTop - 22) + 'px'; _lb.style.display = 'block'; }",
        "pop:legend-floatbtn-init")

    open(argv[2], "w", encoding="utf-8").write(html)
    s = data.get("summary", {})
    print("wrote %s" % argv[2])
    print("  triplets=%s cross=%s coils=%s findings=%s"
          % (s.get("triplets"), s.get("cross_connections"), s.get("coils"), s.get("findings")))
    span = baseline_years(data.get("PRS_TRIPLETS", []))
    print("  axis: TAU_DAYS=%s  corpus baseline=%.1f years"
          % ("90 (template default)" if tau is None else tau, span))
    if tau is None and span > 5:
        sys.stderr.write(
            "WARN: corpus spans %.1f years but TAU_DAYS is 90 days. The log-on-age axis\n"
            "      will compress the older traditions toward the floor. Pass --tau to choose\n"
            "      deliberately, and check the per-tradition rate spread:\n"
            "        python3 scripts/prs_axis_max_share.py %s\n" % (span, argv[2]))


if __name__ == "__main__":
    main()
