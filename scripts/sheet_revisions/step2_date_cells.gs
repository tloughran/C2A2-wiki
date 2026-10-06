/**
 * RC Sandbox dates -- STEP 2 (revised 2026-09-21): date each cell of the TL sandbox tab by SNAPSHOT DIFF.
 *
 * Why this replaces the first step 2: step 1 showed that the Drive API exposes only 13 revisions of the
 * master (2025-08-22 onward). The ~720 versions in the Sheets version-history panel are not reachable by
 * any API. They ARE reachable by hand: the panel can "Make a copy" of any version, and a copy is an
 * ordinary spreadsheet this script can open. So the dates come from SNAPSHOTS:
 *
 *   - every spreadsheet in your Drive named  "RC snapshot YYYY-MM-DD"  (copies you make from the panel,
 *     named with the date of the version you copied);
 *   - the dated copies already in your Drive, found by title:
 *       "Resurrecting Civility Master 12-28-20"         -> 2020-12-28
 *       "Resurrecting Civility Master April 2021 Backup" -> sometime in April 2021 (day unknown)
 *       "Resurrecting Civility Master(AutoRecovered)"    -> content date unknown; copy date is an upper bound
 *       "Resurrecting Civility Master" created 2023-05-29 (not the live one) -> 2023-05-29
 *   - the live master itself = today.
 *
 * For each cell of the LIVE tab, the script finds the earliest snapshot that already contains that cell's
 * text (present_by) and the latest earlier snapshot that does not (absent_at). The honest claim is then:
 * "written after absent_at and on or before present_by". Cells are matched by TEXT, not position, because
 * rows were inserted over the years: a live cell counts as present in a snapshot if its whitespace-
 * normalised text, or its first 60 characters (to survive later appending), appears as a cell there.
 * Cells shorter than 12 characters are not dated on their own (too easily matched by accident); step 3
 * gives them their row's date.
 *
 * Every snapshot carries two dates, lo and hi: its content was saved somewhere in [lo, hi]. present_by
 * uses hi, absent_at uses lo, so an uncertain snapshot can never make a bracket narrower than the truth.
 * A snapshot with no known lo (AutoRecovered) is used only for present_by.
 *
 * Nothing in any spreadsheet is changed. Needs no advanced service beyond what step 1 already added.
 * Uses FILE_ID from step 1 (same Apps Script project).
 *
 * RUN: pick "dateCellsFromSnapshots" and press Run. Read the Execution log; paste it to Claude.
 * OUTPUT (Drive folder "RC Sandbox cell dates"): cell_dates.json, and a Sheet "RC Sandbox cell dates"
 * with a "cells" tab (one row per live cell) and a "snapshots" tab (what each snapshot contributed).
 */
var TAB_2 = 'TL sandbox';
/** Older names of the same tab, tried ONLY for snapshots: before ~mid-2020 the tab was 'sandbox/Qs'
 *  (seen in the Dec 2017 .. Mar 2020 copies). Matching is by cell text, so the tab name is only a locator. */
var TAB_2_OLD = ['sandbox/Qs'];
var SNAP_PREFIX = 'RC snapshot ';
var OUT_FOLDER = 'RC Sandbox cell dates';
var MIN_CHARS = 12, PREFIX_CHARS = 60;

function norm_(s) { return String(s).replace(/\s+/g, ' ').trim(); }
function day_(d) { return Utilities.formatDate(d, 'UTC', 'yyyy-MM-dd'); }

/** All snapshots with their [lo, hi] content dates, oldest hi first. */
function snapshots_() {
  var out = [], seen = {};
  function add(file, lo, hi, label) {
    if (seen[file.getId()] || file.getId() === FILE_ID) return;
    seen[file.getId()] = 1;
    var s = { id: file.getId(), name: file.getName(), lo: lo, hi: hi, label: label };
    // Pre-2014 "old Sheets" files keep ids beginning 0A; the script service cannot open them at all,
    // and a failed open is re-reported as an error at the end of the run even when caught. Skip, say so.
    if (/^0A/.test(s.id)) s.error = 'old-format (pre-2014) Sheets file; scripts cannot open it. Open it in the browser and Make a copy if it matters.';
    out.push(s);
  }
  var it = DriveApp.searchFiles("title contains '" + SNAP_PREFIX + "' and mimeType = 'application/vnd.google-apps.spreadsheet' and trashed = false");
  while (it.hasNext()) {
    var f = it.next(), m = /^RC snapshot (\d{4}-\d{2}-\d{2})/.exec(f.getName());
    if (m) add(f, m[1], m[1], 'your copy of the ' + m[1] + ' version');
    else Logger.log('SKIPPED (name not "RC snapshot YYYY-MM-DD"): ' + f.getName());
  }
  // Google's own name for a copy made from the version-history panel carries the version's timestamp:
  //   "Copy of Resurrecting Civility Master - November 30, 2024, 11:32 AM"  -> 2024-11-30
  var MON = { January: 1, February: 2, March: 3, April: 4, May: 5, June: 6, July: 7, August: 8, September: 9, October: 10, November: 11, December: 12 };
  var vc = DriveApp.searchFiles("title contains 'Copy of Resurrecting Civility Master - ' and mimeType = 'application/vnd.google-apps.spreadsheet' and trashed = false");
  while (vc.hasNext()) {
    var g = vc.next(), v = /^Copy of Resurrecting Civility Master - ([A-Z][a-z]+) (\d{1,2}), (\d{4}), \d{1,2}:\d{2}/.exec(g.getName());
    if (v && MON[v[1]]) { var d2 = v[3] + '-' + ('0' + MON[v[1]]).slice(-2) + '-' + ('0' + v[2]).slice(-2); add(g, d2, d2, 'panel copy of the ' + d2 + ' version'); }
    else Logger.log('SKIPPED (unrecognised copy name): ' + g.getName());
  }
  var fixed = [
    { name: 'Resurrecting Civility Master 12-28-20', lo: '2020-12-28', hi: '2020-12-28', label: 'dated copy "12-28-20"' },
    { name: 'Resurrecting Civility Master April 2021 Backup', lo: '2021-04-01', hi: '2021-04-30', label: 'April 2021 backup (day unknown)' },
    { name: 'Resurrecting Civility Master(AutoRecovered)', lo: null, hi: null, label: 'AutoRecovered (content date unknown; copy date used as upper bound only)' }
  ];
  fixed.forEach(function (x) {
    var fi = DriveApp.getFilesByName(x.name);
    while (fi.hasNext()) { var f = fi.next(); add(f, x.lo, x.hi || day_(f.getDateCreated()), x.label); }
  });
  var same = DriveApp.getFilesByName('Resurrecting Civility Master');
  while (same.hasNext()) {
    var f = same.next();
    if (f.getId() !== FILE_ID) { var d = day_(f.getDateCreated()); add(f, d, d, 'copy made ' + d); }
  }
  out.sort(function (a, b) { return a.hi < b.hi ? -1 : a.hi > b.hi ? 1 : 0; });
  return out;
}

/** The tab's non-empty cells as {id: 'r<row>c<col>' (0-based, the notebook's shelfmark), t: normalised text}. */
function readTab_(id, allowOld) {
  var ss = SpreadsheetApp.openById(id), sh = ss.getSheetByName(TAB_2), used = TAB_2;
  if (!sh && allowOld) TAB_2_OLD.some(function (n) { sh = ss.getSheetByName(n); used = n; return !!sh; });
  if (!sh) return { missing: true, tabs: ss.getSheets().map(function (s) { return s.getName(); }).join(' | ') };
  var v = sh.getDataRange().getDisplayValues(), cells = [];
  for (var r = 0; r < v.length; r++) for (var c = 0; c < v[r].length; c++) {
    var t = norm_(v[r][c]); if (t) cells.push({ id: 'r' + r + 'c' + c, t: t });
  }
  return { cells: cells, tab: used };
}

function dateCellsFromSnapshots() {
  if (typeof FILE_ID === 'undefined' || String(FILE_ID).indexOf('PASTE') === 0) throw new Error('Set FILE_ID in step 1 first.');
  var t0 = Date.now(), live = readTab_(FILE_ID);
  if (live.missing) throw new Error('live master has no tab "' + TAB_2 + '"; tabs: ' + live.tabs);
  Logger.log('live tab: ' + live.cells.length + ' non-empty cells');

  var snaps = snapshots_(), report = [];
  Logger.log('snapshots found: ' + snaps.length);
  var sigs = {};
  snaps.forEach(function (s) {
    var got;
    if (!s.error) { try { got = readTab_(s.id, true); if (got && got.tab && got.tab !== TAB_2) s.tab = got.tab; } catch (e) { s.error = e.message; } }
    if (got && got.missing) s.error = 'no "' + TAB_2 + '" tab; tabs: ' + got.tabs;
    if (!s.error) {
      s.exact = {}; s.pref = {};
      got.cells.forEach(function (c) { s.exact[c.t] = 1; s.pref[c.t.slice(0, PREFIX_CHARS)] = 1; });
      s.n = got.cells.length;
      // A copy whose cells are IDENTICAL to an earlier snapshot's is a re-copy of that snapshot, not a
      // picture of the sheet on its own date (2026-09-21: three such copies, proven by cells dated in
      // their own text that they lack). Ignored: it adds no cells, and its date would be a false lower bound.
      var sig = s.n + ':' + Utilities.base64Encode(Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_1,
                  Object.keys(s.exact).sort().join('\u0001'), Utilities.Charset.UTF_8));
      if (sigs[sig]) { s.error = 'DUPLICATE of "' + sigs[sig] + '" (identical cells) -- its own date is not its content date; ignored'; s.dup = true; }
      else sigs[sig] = s.name + ' [' + s.hi + ']';
    }
    Logger.log((s.dup ? 'DUPLICATE ' : s.error ? 'UNUSABLE  ' : 'ok  ') + s.hi + '  ' + s.name + (s.error ? '  -> ' + s.error : '  (' + s.n + ' cells' + (s.tab ? ', tab "' + s.tab + '"' : '') + ')'));
  });
  var usable = snaps.filter(function (s) { return !s.error; });

  var rows = [], brackets = {}, shortN = 0;
  live.cells.forEach(function (c) {
    if (c.t.length < MIN_CHARS) { shortN++; rows.push({ cell_id: c.id, present_by: '', absent_at: '', match: 'short', chars: c.t.length }); return; }
    var k = -1, how = '';
    for (var i = 0; i < usable.length; i++) {
      var s = usable[i];
      if (s.exact[c.t]) { k = i; how = 'exact'; break; }
      if (c.t.length >= PREFIX_CHARS && s.pref[c.t.slice(0, PREFIX_CHARS)]) { k = i; how = 'prefix'; break; }
    }
    var present = k >= 0 ? usable[k].hi : 'live', absent = '';
    for (var j = (k >= 0 ? k : usable.length) - 1; j >= 0; j--) { if (usable[j].lo) { absent = usable[j].lo; break; } }
    var key = (absent || '(start)') + ' .. ' + present;
    brackets[key] = (brackets[key] || 0) + 1;
    rows.push({ cell_id: c.id, present_by: present, absent_at: absent, match: how || 'none', chars: c.t.length });
  });
  // absent_at must be the lo of the latest usable snapshot BEFORE the first one containing the cell.
  // The loop above takes the nearest earlier snapshot with a known lo; a snapshot with unknown lo is skipped,
  // which widens the bracket (never narrows it).

  usable.forEach(function (s) { s.present = rows.filter(function (r) { return r.present_by === s.hi; }).length; });
  Logger.log('--- first appearance, by snapshot (cells first seen in it) ---');
  usable.forEach(function (s) { Logger.log(s.hi + '  ' + s.present + '  ' + s.label); });
  Logger.log('live only (in no snapshot): ' + rows.filter(function (r) { return r.present_by === 'live'; }).length +
             '   short (<' + MIN_CHARS + ' chars, dated by row in step 3): ' + shortN);
  Logger.log('--- brackets ---');
  Object.keys(brackets).sort().forEach(function (k) { Logger.log(k + '  ' + brackets[k]); });

  var folder = (function () { var f = DriveApp.getFoldersByName(OUT_FOLDER); return f.hasNext() ? f.next() : DriveApp.createFolder(OUT_FOLDER); })();
  var json = JSON.stringify({ generated: new Date().toISOString(), tab: TAB_2, live_cells: live.cells.length,
    snapshots: snaps.map(function (s) { return { name: s.name, lo: s.lo, hi: s.hi, label: s.label, cells: s.n || 0, error: s.error || '' }; }),
    cells: rows });
  var jf = folder.getFilesByName('cell_dates.json');
  if (jf.hasNext()) jf.next().setContent(json); else folder.createFile('cell_dates.json', json, 'application/json');

  var name = 'RC Sandbox cell dates', it = folder.getFilesByName(name), ss;
  if (it.hasNext()) ss = SpreadsheetApp.open(it.next());
  else { ss = SpreadsheetApp.create(name); DriveApp.getFileById(ss.getId()).moveTo(folder); }
  var sh = ss.getSheetByName('cells') || ss.getSheets()[0]; sh.setName('cells'); sh.clear();
  var hdr = ['cell_id', 'absent_at', 'present_by', 'match', 'chars'];
  var vals = [hdr].concat(rows.map(function (r) { return [r.cell_id, r.absent_at, r.present_by, r.match, r.chars]; }));
  sh.getRange(1, 1, vals.length, hdr.length).setValues(vals);
  var sn = ss.getSheetByName('snapshots') || ss.insertSheet('snapshots'); sn.clear();
  var sv = [['name', 'lo', 'hi', 'label', 'cells', 'first_seen_here', 'error']].concat(
    snaps.map(function (s) { return [s.name, s.lo || '', s.hi, s.label, s.n || 0, s.present || 0, s.error || '']; }));
  sn.getRange(1, 1, sv.length, 7).setValues(sv);
  Logger.log('written: ' + ss.getUrl() + '  (' + Math.round((Date.now() - t0) / 1000) + ' s)');
}
