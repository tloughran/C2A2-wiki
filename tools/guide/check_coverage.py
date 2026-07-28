#!/usr/bin/env python3
"""The contract between the guide and the app: one assertion, in both directions.

The guide's plates and the voice guide's per-tab declarations both describe how to reach a
view, and they must not drift. They do NOT share a file to achieve that -- tools/guide/
manifest.json is generated and rebuilt on recapture, wiki/voice_guide/manifests.json is
hand-authored and changes only when a tab gains a control. Merging them would make every
regeneration collide with a human edit. They share this assertion instead.

  Direction A -- no guide plate may claim a route the app does not have.
                 Catches a guide that has gone stale against a renamed tab.

  Direction B -- no destination the app declares may be undocumented.
                 Catches the opposite and more valuable failure: a page nobody wrote up.
                 This is the direction that finds the four Start Here pages no sub-tab
                 reaches -- the exact gap two capture passes missed by hand.

Destinations are read from wiki/explorer.html and wiki/start_here.html, not from
voice_guide/destinations.json, which is itself generated from explorer.html. Reading the
generated copy would let both sides agree while both were wrong.

Exit 0 clean, 1 on any gap, naming it.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_reach

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
WIKI = os.path.join(REPO, 'wiki')

# A destination may be legitimately undocumented, but never silently. Each entry needs a
# reason, and the reason is read by a human at review time -- an empty allowlist is the
# healthy state, and a growing one is the signal the guide has fallen behind.
UNDOCUMENTED = {
    # 'some-tab.html': 'why no plate exists',
}


def live_destinations(explorer, start_here):
    """Everything a user can reach from the shell, keyed the way reach steps key it.

    A chapter button that carries no data-src is a ROW-OPENER, not a page: clicking
    #chap-tools reveals row2 and loads a tab. It is documented through its tabs, so it is
    recorded here with the row it opens rather than demanding a plate of its own.
    """
    dests, rows = {}, {}
    for m in re.finditer(r'class="chap-btn[^"]*"\s+id="([^"]+)"(?:\s+data-src="([^"]+)")?', explorer):
        cid, src = m.group(1), m.group(2)
        dests['chapter:' + cid] = 'chapter %s' % cid
        if not src:
            rows['chapter:' + cid] = None  # resolved below, once the rows are known
    for row in ('row2', 'row2-edu'):
        seg = re.search(r'id="%s"(.*?)</div>' % row, explorer, re.S)
        if not seg:
            continue
        for m in re.finditer(r'data-src="([^"]+)"[^>]*>([^<]*)', seg.group(1)):
            dests['tab:' + m.group(1)] = '%s tab "%s"' % (row, m.group(2).strip())
    # Which row each row-opening chapter reveals. Expressed in explorer.html's JS rather
    # than its markup, so it is taken from the routes build_reach.py already asserts.
    for _sec, (chapter, row, _src) in build_reach.SECTION_ROUTE.items():
        key = 'chapter:' + chapter
        if key in rows and row:
            rows[key] = row
    # Start here's launch links -- the pages no sub-tab row can reach. There are two link
    # classes; keying off only one is how these went missing in the first place.
    for m in re.finditer(r'<a class="(launch|door)"([^>]*)>', start_here):
        href = re.search(r'href="([^"]+)"', m.group(2))
        if href and href.group(1).endswith('.html') and not href.group(1).startswith('http'):
            dests['launch:' + href.group(1)] = ('Start here a.%s -> %s'
                                                % (m.group(1), href.group(1)))
    return dests, rows


def plate_destination(reach):
    """The destination key a plate's reach lands on: its deepest addressable step."""
    key = None
    for step in reach:
        if 'chapter' in step:
            key = 'chapter:' + step['chapter']
        if 'tab' in step:
            key = 'tab:' + step['tab']
        if 'loads' in step:
            key = 'launch:' + step['loads']
    return key


def main():
    explorer = open(os.path.join(WIKI, 'explorer.html')).read()
    start_here = open(os.path.join(WIKI, 'start_here.html')).read()
    manifest = json.load(open(os.path.join(HERE, 'manifest.json')))

    dests, row_openers = live_destinations(explorer, start_here)
    covered = {}
    problems = []

    for plate in manifest['plates']:
        key = plate_destination(plate.get('reach') or [])
        if key is None:
            problems.append('A  %s has no route at all' % plate['slug'])
            continue
        if key not in dests:
            problems.append('A  %s routes to %s, which the app no longer declares'
                            % (plate['slug'], key))
            continue
        covered.setdefault(key, []).append(plate['slug'])

    # The Sociogram is reachable both as a tab and as a Start here link; a plate documents
    # the view, not the doorway, so either doorway counts as covered.
    for key in list(dests):
        if key.startswith('launch:'):
            twin = 'tab:' + key.split(':', 1)[1]
            if twin in covered:
                covered.setdefault(key, []).extend(covered[twin])
    # A row-opening chapter is documented by any plate of a tab in the row it opens.
    for key, row in row_openers.items():
        for tab_key, label in dests.items():
            if tab_key.startswith('tab:') and label.startswith(row + ' ') and tab_key in covered:
                covered.setdefault(key, []).extend(covered[tab_key])

    for key, label in sorted(dests.items()):
        if key in covered:
            continue
        target = key.split(':', 1)[1]
        if target in UNDOCUMENTED:
            print('  allowed  %-46s %s' % (label, UNDOCUMENTED[target]))
            continue
        problems.append('B  %s is undocumented -- no guide plate reaches it' % label)

    print('destinations: %d   documented: %d   plates: %d'
          % (len(dests), len(covered), len(manifest['plates'])))

    if problems:
        print()
        for p in sorted(problems):
            print('FAIL', p)
        sys.exit('%d gap(s) between the guide and the app' % len(problems))
    print('guide and app agree in both directions')


if __name__ == '__main__':
    main()
