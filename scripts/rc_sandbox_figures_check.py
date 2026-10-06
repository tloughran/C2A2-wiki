#!/usr/bin/env python3
"""Verify the RC Sandbox figure bios' links and merge the whos_who entries.

Reads  scripts/rc_sandbox_figures_draft.json  (63 drafted entries, each with an ordered
'links' list and 'tokens' the page must contain) and  wiki/whos_who.json  (already-reviewed
entries, reused verbatim for the figures that overlap).
Writes wiki/rc_sandbox_figures.json  (the source of truth the notebook patch reads) and
       scripts/rc_sandbox_figures_review.md  (the table Tom reviews).

A link passes only if it fetches with HTTP 200 AND one of the entry's tokens appears in the
page text (case-insensitive, after stripping tags). The first passing candidate wins; an entry
with no passing candidate ships with link="" and is listed under NO LINK in the review file.
Nothing here writes into the notebook.
"""
import json, re, sys, time, html, urllib.request, urllib.error, datetime, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
DRAFT = ROOT / 'scripts' / 'rc_sandbox_figures_draft.json'
WW = ROOT / 'wiki' / 'whos_who.json'
OUT = ROOT / 'wiki' / 'rc_sandbox_figures.json'
REVIEW = ROOT / 'scripts' / 'rc_sandbox_figures_review.md'
NOTEBOOK = ROOT / 'wiki' / 'rc_sandbox_notebook.html'
UA = {'User-Agent': 'Mozilla/5.0 (C2A2 notebook link check; contact via github.com/tloughran)'}

def fetch(url):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=20) as r:
            body = r.read(1_500_000).decode('utf-8', 'ignore')
            return r.status, r.geturl(), body
    except urllib.error.HTTPError as e:
        return e.code, url, ''
    except Exception as e:
        return type(e).__name__, url, ''

def text_of(body):
    body = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', body, flags=re.S | re.I)
    return html.unescape(re.sub(r'<[^>]+>', ' ', body)).lower()

def label_for(url):
    m = re.match(r'https?://(?:www\.)?([^/]+)(/.*)?', url)
    host, path = m.group(1), (m.group(2) or '')
    if host == 'plato.stanford.edu': return 'Stanford Encyclopedia'
    if host == 'en.wikipedia.org': return 'Wikipedia'
    if host == 'vatican.va': return 'vatican.va'
    return host

# the 76 index figures with 3+ mentions, straight from the notebook (so the set cannot drift)
nb = NOTEBOOK.read_text(encoding='utf-8')
idx = nb[nb.index('id="index-figures"'):nb.index('id="index-disciplines"')]
index_rows = [(slug, html.unescape(name), int(n)) for slug, name, n in
              re.findall(r'<div class="idxrow" id="fig-([^"]+)"><b>(.*?)</b> <span class="n">(\d+)</span>', idx)]
wanted = {slug: (name, n) for slug, name, n in index_rows if n >= 3}

draft = json.load(open(DRAFT, encoding='utf-8'))
ww = json.load(open(WW, encoding='utf-8'))['people']
by_slug = {f['slug']: f for f in draft['figures']}
entries = []
# whos_who first: slug = index slug whose display name equals the whos_who 'name'
ww_by_name = {p['name']: p for p in ww}
for slug, (name, n) in wanted.items():
    if name in ww_by_name and slug not in by_slug:
        p = ww_by_name[name]
        entries.append({'slug': slug, 'name': name, 'full': p['full'], 'kind': 'whos_who', 'source': 'whos_who',
                        'blurb': p['blurb'], 'links': [p['link']], 'tokens': [p['full'].split()[-1]], 'mentions': n})
for slug, f in by_slug.items():
    if slug not in wanted:
        print('DRAFT SLUG NOT IN INDEX (>=3):', slug, file=sys.stderr); sys.exit(1)
    f = dict(f); f['mentions'] = wanted[slug][1]; entries.append(f)
missing = sorted(set(wanted) - {e['slug'] for e in entries})
if missing:
    print('INDEX FIGURES WITH NO ENTRY:', missing, file=sys.stderr); sys.exit(1)

today = datetime.date.today().isoformat()
rows, nolink = [], []
for e in sorted(entries, key=lambda x: -x['mentions']):
    e['link'] = ''; e['linkLabel'] = ''; e['link_checked'] = today; e['link_trace'] = []
    for url in e['links']:
        status, final, body = fetch(url)
        if status in (403, 429, 503):           # bot throttling: one retry after a pause
            time.sleep(2.5); status, final, body = fetch(url)
        t = text_of(body)
        hit = [tok for tok in e['tokens'] if tok.lower() in t]
        e['link_trace'].append({'url': url, 'status': status, 'final': final, 'token_found': bool(hit)})
        if status == 200 and hit:
            e['link'] = url                      # the address the person owns, not the redirect target
            e['linkLabel'] = label_for(url); break
        time.sleep(0.3)
    if not e['link'] and e['source'] == 'whos_who':
        # already reviewed on the Who's Who page; a throttled fetch does not unreview it
        e['link'] = e['links'][0]; e['linkLabel'] = label_for(e['link']); e['link_kept'] = 'whos_who link kept despite fetch status'
    used = e['links'].index(e['link']) if e['link'] else None
    rows.append((e['mentions'], e['name'], e['full'], e['source'], e['link'] or '(none)',
                 ('candidate %d of %d' % (used + 1, len(e['links'])) + (' (KEPT, fetch %s)' % e['link_trace'][0]['status'] if e.get('link_kept') else '')) if e['link'] else 'ALL %d FAILED' % len(e['links']),
                 e.get('note', ''), e['blurb']))
    if not e['link']: nolink.append(e)
    print('%-18s %-12s %s' % (e['name'][:18], 'OK' if e['link'] else 'NO LINK', e['link'] or [x['status'] for x in e['link_trace']]))

out = {'_comment': draft['_comment'], 'generated': today, 'count': len(entries),
       'figures': sorted(entries, key=lambda x: -x['mentions'])}
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')

with open(REVIEW, 'w', encoding='utf-8') as f:
    f.write('# RC Sandbox figure bios — review table (%s)\n\n' % today)
    f.write('%d figures with 3+ mentions. %d reused from whos_who.json, %d drafted. %d with no passing link.\n\n'
            % (len(entries), sum(1 for e in entries if e['source'] == 'whos_who'),
               sum(1 for e in entries if e['source'] == 'drafted'), len(nolink)))
    f.write('Link rule: living scholars = personal or institutional page (no social media); the dead and the fictional = Stanford Encyclopedia if an entry exists, else Wikipedia. A link is listed only if it returned 200 and the page names the person.\n\n')
    if nolink:
        f.write('## NO LINK (ship without, or supply one)\n\n')
        for e in nolink: f.write('- **%s** — tried: %s\n' % (e['full'], '; '.join('%s → %s%s' % (x['url'], x['status'], '' if x['token_found'] else ' (name not on page)') for x in e['link_trace'])))
        f.write('\n')
    f.write('## All entries (by mentions)\n\n')
    for n, name, full, src, link, how, note, blurb in rows:
        f.write('### %s (%d) — %s%s\n%s\n\n%s\n\n' % (full, n, link, ' — ' + how if link != '(none)' else '',
                ('_%s_  \n' % note) if note else '', blurb))
print('\nwrote', OUT, 'and', REVIEW, '| entries', len(entries), '| no link', len(nolink))
