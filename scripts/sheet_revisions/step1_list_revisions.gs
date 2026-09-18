/**
 * RC Sandbox dates -- STEP 1: count what survives in the Sheet's version history.
 *
 * Runs inside your Google account (Apps Script), because revision history is only
 * readable with your login. Nothing is exported or changed by this step: it LISTS
 * the revisions, reports how many per year, and writes the list to a new Sheet
 * named "RC Master revisions list" in My Drive so the next step can read it.
 *
 * Setup (about five minutes, once):
 *   1. script.google.com  ->  New project  ->  paste this whole file over the default code.
 *   2. Left rail, "Services" (+)  ->  Drive API  ->  version v3  ->  Add.
 *   3. Set FILE_ID below to the master sheet's id (the long string in its URL).
 *   4. Pick the function "listRevisions" in the toolbar and press Run.
 *      Google asks you to authorise the script for your Drive: that is you, granting
 *      your own script, in your own browser.
 *   5. Read the Execution log (View -> Logs). Copy the per-year line into the chat.
 *
 * What the numbers mean: a year with hundreds of revisions can be dated to the day;
 * a year with a dozen can only be dated to week- or month-wide brackets. Google merges
 * old auto-saved versions to save space, so the early years are the ones to check.
 */
var FILE_ID = 'PASTE_THE_SHEET_ID_HERE';
var TAB_NAME = 'TL sandbox';

function listRevisions() {
  if (FILE_ID.indexOf('PASTE') === 0) throw new Error('Set FILE_ID first.');
  var rows = [], pageToken = null, page = 0;
  do {
    var res = Drive.Revisions.list(FILE_ID, {
      pageSize: 1000, pageToken: pageToken,
      fields: 'nextPageToken,revisions(id,modifiedTime,keepForever,size,exportLinks,lastModifyingUser/displayName)'
    });
    (res.revisions || []).forEach(function (v) {
      rows.push([v.id, v.modifiedTime, v.keepForever ? 'yes' : '', v.size || '',
                 Object.keys(v.exportLinks || {}).join(' '),
                 v.lastModifyingUser ? v.lastModifyingUser.displayName : '']);
    });
    pageToken = res.nextPageToken; page++;
  } while (pageToken && page < 50);

  var byYear = {};
  rows.forEach(function (r) { var y = String(r[1]).slice(0, 4); byYear[y] = (byYear[y] || 0) + 1; });
  var years = Object.keys(byYear).sort();
  Logger.log('revisions surviving: ' + rows.length);
  Logger.log('per year: ' + years.map(function (y) { return y + '=' + byYear[y]; }).join('  '));
  if (rows.length) Logger.log('first: ' + rows[0][1] + '   last: ' + rows[rows.length - 1][1]);

  var ss = SpreadsheetApp.openById(FILE_ID);
  var tab = ss.getSheetByName(TAB_NAME);
  Logger.log(tab ? ('tab "' + TAB_NAME + '" gid=' + tab.getSheetId() + ' rows=' + tab.getLastRow() + ' cols=' + tab.getLastColumn())
                 : ('tab "' + TAB_NAME + '" NOT FOUND; tabs are: ' + ss.getSheets().map(function (s) { return s.getName(); }).join(' | ')));

  var out = SpreadsheetApp.create('RC Master revisions list');
  var sh = out.getActiveSheet();
  sh.getRange(1, 1, 1, 6).setValues([['revision_id', 'modifiedTime', 'keepForever', 'size', 'exportFormats', 'modifiedBy']]);
  if (rows.length) sh.getRange(2, 1, rows.length, 6).setValues(rows);
  sh.getRange(1, 8, 1, 2).setValues([['tab_gid', tab ? String(tab.getSheetId()) : '']]);
  Logger.log('written: ' + out.getUrl());
}
