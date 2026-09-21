/**
 * RC Sandbox dates -- STEP 2: when did each cell of the TL sandbox tab first appear?
 *
 * Walks the Sheet's version history in your Google account (Apps Script + Drive API v3),
 * exports the TL sandbox tab of ONE revision PER CALENDAR DAY (the last of that day), and
 * diffs each day's cells against the day before. A cell first seen on day D gets the
 * bracket (last revision before D, that revision of D). Nothing in the Sheet is changed.
 *
 * Why one per day: day-level dates need at most one snapshot per day, and your own
 * history panel (720 versions, 2017-11 to 2026) makes that roughly 450 fetches instead
 * of 720. Free Google accounts cap UrlFetch at ~100 MB/day; a TL-sandbox CSV is well
 * under 1 MB, and early revisions are far smaller, so this typically finishes in one
 * to three days of trigger runs. It stops cleanly when the quota is hit and resumes.
 *
 * Setup (once), in the SAME Apps Script project as step 1:
 *   1. Paste this file as a second script file (File > New > Script) or below step 1.
 *   2. Services (+) -> Drive API v3 must already be added (step 1 needed it too).
 *   3. FILE_ID is shared with step 1 (set there). TAB_NAME is the tab to track.
 *   4. Run "probeOne" FIRST. It fetches ONE revision's CSV and logs the HTTP status, the
 *      byte count, the cell count and the first row. If the status is not 200 or the cell
 *      count is 0, stop and tell Claude what it logged -- nothing else should run.
 *   5. Run "installTrigger". It runs dateCells now and then every 10 minutes until done,
 *      then removes itself and writes the results (see OUTPUT below).
 *   6. Watch progress in the log or in the state file; "startOver" wipes the state.
 *
 * OUTPUT (in a Drive folder "RC Sandbox cell dates"):
 *   - cell_dates.json  -- one record per tracked cell; Claude reads this to stamp dates
 *                         into the notebook (step 3).
 *   - a Sheet "RC Sandbox cell dates" -- the same, readable, one row per cell.
 *   - state.json       -- the walker's checkpoint (safe to leave; startOver deletes it).
 *
 * Keys: a cell is tracked by its row's SERIAL (column A, the sheet's own row id) and its
 * column, so rows inserted or deleted over the years do not shift identities. A row with
 * no numeric serial falls back to its position. The final position of every cell is
 * recorded too (cell_id_now = r<row>c<col>, 0-based, the notebook's own shelfmark).
 */
var TAB_NAME_2 = 'TL sandbox';
var FOLDER_NAME = 'RC Sandbox cell dates';
var TIME_BUDGET_MS = 270 * 1000;     // Apps Script kills a run at 6 min; stop at 4.5
var SAVE_EVERY = 15;                 // checkpoint the state every N revisions

function fileId_() {
  if (typeof FILE_ID === 'undefined' || String(FILE_ID).indexOf('PASTE') === 0) throw new Error('Set FILE_ID in step 1 first.');
  return FILE_ID;
}
function tabGid_() {
  var sh = SpreadsheetApp.openById(fileId_()).getSheetByName(TAB_NAME_2);
  if (!sh) throw new Error('tab "' + TAB_NAME_2 + '" not found');
  return String(sh.getSheetId());
}
function folder_() {
  var it = DriveApp.getFoldersByName(FOLDER_NAME);
  return it.hasNext() ? it.next() : DriveApp.createFolder(FOLDER_NAME);
}
function fileIn_(folder, name) {
  var it = folder.getFilesByName(name);
  return it.hasNext() ? it.next() : null;
}
function writeText_(folder, name, text, mime) {
  var f = fileIn_(folder, name);
  if (f) { f.setContent(text); return f; }
  return folder.createFile(name, text, mime || 'application/json');
}

/** Every surviving revision, oldest first, then one per calendar day (the last that day). */
function dailyRevisions_() {
  var all = [], pageToken = null, page = 0;
  do {
    var res = Drive.Revisions.list(fileId_(), { pageSize: 1000, pageToken: pageToken, fields: 'nextPageToken,revisions(id,modifiedTime,exportLinks)' });
    (res.revisions || []).forEach(function (v) { all.push(v); });
    pageToken = res.nextPageToken; page++;
  } while (pageToken && page < 50);
  all.sort(function (a, b) { return a.modifiedTime < b.modifiedTime ? -1 : 1; });
  var byDay = {}, days = [];
  all.forEach(function (v) { var d = v.modifiedTime.slice(0, 10); if (!byDay[d]) days.push(d); byDay[d] = v; });
  return days.map(function (d) { return byDay[d]; });
}

function csvUrl_(rev, gid) {
  var base = (rev.exportLinks && rev.exportLinks['text/csv']) ||
             ('https://docs.google.com/spreadsheets/export?id=' + fileId_() + '&revision=' + rev.id + '&exportFormat=csv');
  return base + '&gid=' + gid;
}

/** Fetch one revision's tab as a map key -> {t: text, r: rowIndex, c: colIndex, s: serial}. */
function fetchCells_(rev, gid) {
  var resp = UrlFetchApp.fetch(csvUrl_(rev, gid), { headers: { Authorization: 'Bearer ' + ScriptApp.getOAuthToken() }, muteHttpExceptions: true });
  var code = resp.getResponseCode();
  if (code !== 200) throw new Error('HTTP ' + code + ' for revision ' + rev.id + ' (' + rev.modifiedTime + '): ' + resp.getContentText().slice(0, 200));
  var rows = Utilities.parseCsv(resp.getContentText()), cells = {}, n = 0;
  for (var r = 0; r < rows.length; r++) {
    var serial = rows[r][0] !== undefined && /^\d+$/.test(String(rows[r][0]).trim()) ? String(rows[r][0]).trim() : null;
    for (var c = 0; c < rows[r].length; c++) {
      var t = rows[r][c];
      if (t === null || t === undefined || String(t).trim() === '') continue;
      var key = (serial !== null ? 'S' + serial : 'p' + r) + 'c' + c;
      cells[key] = { t: String(t), r: r, c: c, s: serial }; n++;
    }
  }
  return { cells: cells, n: n, bytes: resp.getContentText().length, firstRow: rows.length ? rows[0].slice(0, 6) : [] };
}

/** Step 4 of the setup: prove the export works on ONE revision before anything else runs. */
function probeOne() {
  var revs = dailyRevisions_(), gid = tabGid_();
  Logger.log('daily revisions: ' + revs.length + ' (of all surviving); first ' + revs[0].modifiedTime + ' last ' + revs[revs.length - 1].modifiedTime);
  var mid = revs[Math.floor(revs.length / 2)];
  Logger.log('probing revision ' + mid.id + ' @ ' + mid.modifiedTime + ' gid=' + gid);
  Logger.log('export link offered: ' + ((mid.exportLinks && mid.exportLinks['text/csv']) ? 'text/csv' : 'NONE (constructed URL will be used)'));
  var got = fetchCells_(mid, gid);
  Logger.log('OK: ' + got.bytes + ' bytes, ' + got.n + ' non-empty cells, first row: ' + JSON.stringify(got.firstRow));
  if (got.n === 0) Logger.log('WARNING: zero cells -- the gid may be wrong for that revision, or the tab did not exist yet. Tell Claude.');
}

function loadState_(folder) {
  var f = fileIn_(folder, 'state.json');
  if (!f) return { next: 0, prev: {}, prevTime: null, first: {}, changed: {}, seen: 0 };
  return JSON.parse(f.getBlob().getDataAsString());
}
function saveState_(folder, st) { writeText_(folder, 'state.json', JSON.stringify(st)); }

/** The walker. Safe to call repeatedly; each call does as much as fits in the time budget. */
function dateCells() {
  var start = Date.now(), folder = folder_(), st = loadState_(folder), revs = dailyRevisions_(), gid = tabGid_();
  if (st.next >= revs.length) { finish_(folder, st, revs); return; }
  var done = 0;
  try {
    while (st.next < revs.length && Date.now() - start < TIME_BUDGET_MS) {
      var rev = revs[st.next], got = fetchCells_(rev, gid), cur = got.cells, now = rev.modifiedTime;
      for (var k in cur) {
        if (!st.prev[k]) st.first[k] = { rev: rev.id, time: now, prevTime: st.prevTime, r: cur[k].r, c: cur[k].c, s: cur[k].s, chars: cur[k].t.length };
        else if (st.prev[k] !== hash_(cur[k].t)) st.changed[k] = now;
        // keep the latest position for every live key
        if (st.first[k]) { st.first[k].r = cur[k].r; st.first[k].c = cur[k].c; }
      }
      for (var k2 in st.prev) if (!cur[k2] && st.first[k2] && !st.first[k2].gone) st.first[k2].gone = now;
      var nextPrev = {}; for (var k3 in cur) nextPrev[k3] = hash_(cur[k3].t);
      st.prev = nextPrev; st.prevTime = now; st.next++; st.seen++; done++;
      if (done % SAVE_EVERY === 0) saveState_(folder, st);
    }
  } catch (e) {
    saveState_(folder, st);
    Logger.log('stopped at revision index ' + st.next + ' after ' + done + ' this run: ' + e.message + (/quota|too many times/i.test(e.message) ? '  (UrlFetch quota -- the trigger will resume tomorrow)' : ''));
    return;
  }
  saveState_(folder, st);
  Logger.log('processed ' + done + ' this run; ' + st.next + ' of ' + revs.length + ' daily revisions done');
  if (st.next >= revs.length) finish_(folder, st, revs);
}
function hash_(t) { return Utilities.base64Encode(Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_1, t, Utilities.Charset.UTF_8)).slice(0, 12); }

function finish_(folder, st, revs) {
  var out = [], keys = Object.keys(st.first).sort();
  keys.forEach(function (k) { var f = st.first[k];
    out.push({ key: k, cell_id_now: f.gone ? '' : ('r' + f.r + 'c' + f.c), row_serial: f.s, col: f.c, first_seen: f.time, first_seen_rev: f.rev,
               prev_rev: f.prevTime, last_changed: st.changed[k] || '', gone: f.gone || '', chars: f.chars }); });
  writeText_(folder, 'cell_dates.json', JSON.stringify({ generated: new Date().toISOString(), tab: TAB_NAME_2, daily_revisions: revs.length, cells: out }));
  var name = 'RC Sandbox cell dates', it = DriveApp.getFilesByName(name), ss = it.hasNext() ? SpreadsheetApp.open(it.next()) : SpreadsheetApp.create(name);
  var sh = ss.getActiveSheet(); sh.clear();
  var hdr = ['key', 'cell_id_now', 'row_serial', 'col', 'first_seen', 'first_seen_rev', 'prev_rev', 'last_changed', 'gone', 'chars'];
  var rows = [hdr].concat(out.map(function (o) { return hdr.map(function (h) { return o[h] === null || o[h] === undefined ? '' : o[h]; }); }));
  sh.getRange(1, 1, rows.length, hdr.length).setValues(rows);
  removeTriggers_();
  Logger.log('DONE: ' + out.length + ' cells dated over ' + revs.length + ' daily revisions. ' + ss.getUrl());
}

function installTrigger() {
  removeTriggers_();
  ScriptApp.newTrigger('dateCells').timeBased().everyMinutes(10).create();
  Logger.log('trigger installed (every 10 min); running once now');
  dateCells();
}
function removeTriggers_() {
  ScriptApp.getProjectTriggers().forEach(function (t) { if (t.getHandlerFunction() === 'dateCells') ScriptApp.deleteTrigger(t); });
}
function startOver() {
  removeTriggers_();
  var f = fileIn_(folder_(), 'state.json'); if (f) f.setTrashed(true);
  Logger.log('state cleared; run installTrigger to begin again');
}
