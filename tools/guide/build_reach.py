#!/usr/bin/env python3
"""Add page-level `reach` to every plate, and refuse to invent the rest.

`reach` is the plan's state recipe: the steps that drive the app to what a plate shows,
replayed by the capture harness AND by the guide's "open this view in the app" link, so
the two cannot drift.

This script authors only the part that is DERIVABLE and CHECKABLE right now:

  * which chapter and sub-tab a plate lives under -- derived from its section, and
    validated against the real DOM in wiki/explorer.html and the real files on disk
  * the four Start Here launch links, validated against wiki/start_here.html

It does NOT author the within-page steps (open this modal, expand this level, select this
node). Those were encoded in stage_a.py .. stage_l.py, which did not survive the transfer,
and guessing them would produce recipes that look authoritative and silently reach the
wrong state -- the exact failure mode IN_APP_GUIDE_PLAN.md was written about. Plates whose
state is deeper than the page default get `reach_exact: false` and are counted loudly.

Every selector below is asserted against the live source. A rename fails the run.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
WIKI = os.path.join(REPO, 'wiki')

# section number -> the chapter, and (for the two sub-tab rows) the tab's data-src.
SECTION_ROUTE = {
    '1':  ('chap-tools', 'row2', 'wiki_narration.html'),          # the shell's own default load
    '2':  ('chap-intro', None, None),
    '7':  ('chap-community', None, None),
    '8':  ('chap-education', 'row2-edu', 'rc_document_explorer.html'),
    '9':  ('chap-education', 'row2-edu', 'physics_explorer.html'),
    '10': ('chap-education', 'row2-edu', 'commentary-explorer/commentary_explorer.html'),
    '11': ('chap-education', 'row2-edu', 'heartbeat/index.html'),
    '12': ('chap-tools', 'row2', 'wiki_narration.html'),
    '13': ('chap-tools', 'row2', 'prs_3d.html'),
    '14': ('chap-tools', 'row2', 'agents_tab.html'),
    '15': ('chap-tools', 'row2', 'metabolism/metabolism_view.html'),
    '16': ('chap-tools', 'row2', 'summa_explorer.html'),
    '17': ('chap-tools', 'row2', 'interT_study.html'),
    '18': ('chap-interaction', None, None),
}

# Sections 3-6 are the four pages no sub-tab reaches, opened by links inside start_here.html.
# There are TWO link classes, not one: `a.launch` for the inline calls to action and `a.door`
# for the two big section doors. Getting this wrong is easy and silent, so the assertion below
# checks the class and the attribute on the SAME anchor rather than anywhere in the file.
# Three post {source:'c2a2-start-here', action:'navigate', target} to the shell; Who's Who
# carries no data-target and navigates the frame directly -- see NOTES in README.md.
#   section: (css class, distinguishing attribute, page it loads, postMessage target or None)
START_HERE_LAUNCH = {
    '3': ('launch', ('data-target', 'fifteen'), 'what_is_c2a2.html', 'fifteen'),
    '4': ('launch', ('href', 'whos_who.html'), 'whos_who.html', None),
    '5': ('door', ('data-target', 'review-cards'), 'review_log.html', 'review-cards'),
    '6': ('door', ('data-target', 'summa-commentary'), 'summa_commentary.html', 'summa-commentary'),
}


def anchor_exists(html, cls, attr, value):
    """True only if ONE anchor carries both the class and the attribute.

    Substring checks are what let a wrong selector pass review: `data-target="review-cards"`
    is present in start_here.html, but on an a.door, not the a.launch an earlier version of
    this file claimed. A selector that matches nothing must fail here, not in the browser.
    """
    for m in re.finditer(r'<a\b([^>]*)>', html):
        tag = m.group(1)
        cm = re.search(r'class="([^"]*)"', tag)
        if not cm or cls not in cm.group(1).split():
            continue
        if re.search(r'\b%s="%s"' % (re.escape(attr), re.escape(value)), tag):
            return True
    return False

# Declared in IN_APP_GUIDE_PLAN.md Part 4. Their content legitimately changes every run, so
# a pixel diff on them is noise; the weekly job must diff structure only.
VOLATILE_PREFIXES = ('c30', 'c31', 'c32', 'c33', 'c34', 'c35', 'c36', 'c37',
                     'b30', 'b31', 'b32', 'b33',
                     'b20', 'b21', 'b22', 'b23', 'b24')
# The only plates that spend model credits: the four Physics Explorer AI actions.
COST_PREFIXES = ('c16', 'c17', 'c18')

errors = []


def require(cond, msg):
    if not cond:
        errors.append(msg)


def main(wiki=WIKI):
    explorer = open(os.path.join(wiki, 'explorer.html')).read()
    start_here = open(os.path.join(wiki, 'start_here.html')).read()
    globals()['WIKI'] = wiki

    # --- assert the routes against the live DOM, before writing anything ---
    for sec, (chapter, row, src) in sorted(SECTION_ROUTE.items(), key=lambda kv: int(kv[0])):
        require('id="%s"' % chapter in explorer,
                'chapter id %s not in explorer.html' % chapter)
        if src:
            require('data-src="%s"' % src in explorer,
                    'no tab with data-src="%s" in explorer.html' % src)
            require(os.path.exists(os.path.join(WIKI, src)),
                    'tab target missing on disk: wiki/%s' % src)
        if row:
            require('id="%s"' % row in explorer, 'row id %s not in explorer.html' % row)

    for sec, (cls, (attr, value), page, post_target) in sorted(START_HERE_LAUNCH.items()):
        require(anchor_exists(start_here, cls, attr, value),
                'start_here.html has no <a class="%s" %s="%s">' % (cls, attr, value))
        require(os.path.exists(os.path.join(WIKI, page)), 'missing on disk: wiki/%s' % page)
        if post_target:
            require("case '%s':" % post_target in explorer,
                    "explorer.html message switch has no case '%s'" % post_target)

    if errors:
        for e in errors:
            print('FAIL:', e)
        sys.exit('contract broken: %d assertion(s) failed, manifest not written' % len(errors))

    # --- write reach ---
    manifest_path = os.path.join(HERE, 'manifest.json')
    manifest = json.load(open(manifest_path))
    exact = 0
    seen_section = set()

    for entry in manifest['plates']:
        sec = entry['section'].split('.')[0]
        steps = []
        if sec in START_HERE_LAUNCH:
            cls, (attr, value), page, post_target = START_HERE_LAUNCH[sec]
            steps.append({'chapter': 'chap-intro'})
            steps.append({'frameClick': "a.%s[%s='%s']" % (cls, attr, value), 'loads': page})
        else:
            chapter, row, src = SECTION_ROUTE[sec]
            steps.append({'chapter': chapter})
            if src:
                steps.append({'tab': src, 'row': row})
        entry['reach'] = steps
        # The first plate of a section is that page as it loads; everything after it is a
        # deeper state whose steps are not recoverable from the PDF.
        entry['reach_exact'] = sec not in seen_section
        seen_section.add(sec)
        if entry['reach_exact']:
            exact += 1
        entry['volatile'] = entry['slug'].startswith(VOLATILE_PREFIXES)
        entry['cost'] = 'model' if entry['slug'].startswith(COST_PREFIXES) else 'free'

    manifest['schema'] = 'c2a2-guide-manifest/1'
    manifest['counts'].update({
        'reach_exact': exact,
        'reach_page_only': len(manifest['plates']) - exact,
        'volatile': sum(1 for e in manifest['plates'] if e['volatile']),
        'cost_model': sum(1 for e in manifest['plates'] if e['cost'] == 'model'),
    })
    manifest['_reach'] = (
        'reach drives the app to the plate. reach_exact=false means these steps reach the '
        'plate PAGE but not its exact state -- the within-page steps were lost with the '
        'capture harness and are deliberately not guessed. Every selector here is asserted '
        'against wiki/explorer.html and wiki/start_here.html by build_reach.py, which fails '
        'the run rather than writing a stale manifest.')
    json.dump(manifest, open(manifest_path, 'w'), indent=2, ensure_ascii=False)

    print('all %d route assertions passed' % (len(SECTION_ROUTE) + len(START_HERE_LAUNCH)))
    for k, v in manifest['counts'].items():
        print('  %-18s %d' % (k, v))


if __name__ == '__main__':
    main()
