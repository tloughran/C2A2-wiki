#!/usr/bin/env python3
"""Put the figure bios from wiki/rc_sandbox_figures.json into the Figures index of
wiki/rc_sandbox_notebook.html. Idempotent: an existing <details class="bio"> on a row is
replaced, rows without an entry are left alone, and the CSS block is inserted once.
Run after rc_sandbox_figures_check.py. --dry-run reports without writing.
"""
import json, re, sys, html, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
NB = ROOT / 'wiki' / 'rc_sandbox_notebook.html'
SRC = ROOT / 'wiki' / 'rc_sandbox_figures.json'
DRY = '--dry-run' in sys.argv
CSS = '''.idxrow details.bio{margin:3px 0 6px;max-width:70ch}
.idxrow details.bio summary{cursor:pointer;color:var(--accent);font-family:var(--sans);font-size:11px;
 letter-spacing:.06em;text-transform:uppercase;list-style:none;user-select:none}
.idxrow details.bio summary::-webkit-details-marker{display:none}
.idxrow details.bio summary::before{content:"\\25B8  "}
.idxrow details.bio[open] summary::before{content:"\\25BE  "}
.idxrow details.bio p{margin:5px 0 2px;font-family:var(--sans);font-size:13.5px;line-height:1.5;color:var(--ink)}
.idxrow details.bio p b{font-weight:600}
.idxrow details.bio p a{font-family:var(--sans);font-size:12.5px;margin:0 0 0 6px;white-space:nowrap}
'''
h = NB.read_text(encoding='utf-8'); before = h
data = json.load(open(SRC, encoding='utf-8'))
if '.idxrow details.bio{' not in h:
    anchor = '.idxrow a{font-family:var(--mono);font-size:11px;margin-right:5px;white-space:nowrap}\n'
    assert h.count(anchor) == 1, 'idxrow CSS anchor not found'
    h = h.replace(anchor, anchor + CSS)
done, skipped = [], []
for f in data['figures']:
    pat = re.compile(r'(<div class="idxrow" id="fig-%s"><b>.*?</b> <span class="n">\d+</span>)(<details class="bio">.*?</details>)?' % re.escape(f['slug']), re.S)
    m = pat.search(h)
    if not m:
        skipped.append(f['slug']); continue
    link = ('<a href="%s" target="_blank" rel="noopener">%s ↗</a>' % (html.escape(f['link'], quote=True), html.escape(f['linkLabel']))) if f.get('link') else ''
    bio = ('<details class="bio"><summary>who</summary><p><b>%s</b> — %s%s</p></details>'
           % (html.escape(f['full']), html.escape(f['blurb']), link))
    h = h[:m.start()] + m.group(1) + bio + h[m.end():]
    done.append(f['slug'])
intro_old = '203 figures engaged across the corpus. Initialisms are resolved'
intro_new = ('203 figures engaged across the corpus; the %d named three times or more carry a one-paragraph bio and a checked link under <i>who</i>. Initialisms are resolved' % len(done))
if intro_old in h and 'carry a one-paragraph bio' not in h:
    h = h.replace(intro_old, intro_new, 1)
else:
    h = re.sub(r'203 figures engaged across the corpus; the \d+ named three times or more carry', '203 figures engaged across the corpus; the %d named three times or more carry' % len(done), h, count=1)
print('bios placed:', len(done), '| no matching index row:', skipped, '| bytes', len(before.encode()), '->', len(h.encode()))
if skipped: sys.exit(1)
if not DRY:
    NB.write_text(h, encoding='utf-8'); print('written', NB)
