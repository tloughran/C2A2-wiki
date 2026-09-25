#!/usr/bin/env python3
"""
build_grounding_index.py -- the planner's grounding index (search-and-dialogue,
grounding increment, 2026-09-24).

Deterministic (Rule 5). Reads the model's own structure and writes ONE file the
explorer shell fetches when a question goes to the planner:

  wiki/voice_guide/grounding.json
    _meta        generated (ISO, self-dated -- never trust mtime), counts, sources
    traditions   slug -> {name, full, aliases, prs:[{id,label,p,r,s,c,d}]}
    bridges      "a|b" (slugs sorted) -> "synthesis/<a>_<b>_bridge.md"
    signals      [{a,b,d,st,w,t,n,src}]   Level-2 assertions, slugs sorted

Sources:
  wiki/whos_who.json (section "traditions")   names + full names
  wiki/traditions/<slug>/prs_triplets.md       PRS-NN blocks
  wiki/synthesis/*_bridge.md                   bridge essays (path only; text fetched live)
  prototypes/signals_grown.json                Level-2 signals (not served by Pages)

Fails loud (exit 1) when a source is missing or a count collapses to zero.

Runs daily at the end of scripts/regen_level2_signals.sh (daily run Phase 5.6).
Rewrites the file only when content moved, so a quiet day commits nothing.

Usage: python3 scripts/build_grounding_index.py [--check]
  --check  rebuild in memory and exit 1 if the committed file differs in content
           (ignores _meta.generated)
"""
import datetime, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, 'wiki')
OUT = os.path.join(WIKI, 'voice_guide', 'grounding.json')
FIELD_MAX = 320

def slugify(name):
    return re.sub(r'[^a-z]', '', name.lower())

def clip(s, n=FIELD_MAX):
    s = re.sub(r'\s+', ' ', (s or '')).strip()
    return s if len(s) <= n else s[:n - 1].rstrip() + '…'

PRS_HEAD = re.compile(r'^(PRS-\d+[a-z]?):\s*$', re.M)
FIELD = re.compile(r'^\s+(Label|Problem|Resource|Solution|Confidence|Date Added):\s*(.*)$')

def parse_prs(text):
    out = []
    heads = list(PRS_HEAD.finditer(text))
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        f = {}
        for line in text[h.end():end].splitlines():
            m = FIELD.match(line)
            if m:
                f[m.group(1)] = m.group(2)
        if not f.get('Problem'):
            continue
        out.append({'id': h.group(1), 'label': clip(f.get('Label', ''), 140),
                    'p': clip(f.get('Problem')), 'r': clip(f.get('Resource')),
                    's': clip(f.get('Solution')), 'c': f.get('Confidence', '').strip(),
                    'd': f.get('Date Added', '').strip()})
    return out

def die(msg):
    sys.stderr.write('build_grounding_index: FAIL: ' + msg + '\n')
    sys.exit(1)

def build():
    ww = json.load(open(os.path.join(WIKI, 'whos_who.json')))
    people = [p for p in ww.get('people', []) if p.get('section') == 'traditions']
    if not people:
        die('whos_who.json has no tradition entries')
    trad = {}
    for p in people:
        slug = slugify(p['name'])
        full = p.get('full', p['name'])
        aliases = sorted({slug, p['name'].lower(), p['name'].lower().replace('-', ' '),
                          full.lower(), full.lower().replace('-', ' ')})
        path = os.path.join(WIKI, 'traditions', slug, 'prs_triplets.md')
        if not os.path.exists(path):
            die('missing ' + os.path.relpath(path, ROOT))
        prs = parse_prs(open(path, encoding='utf-8').read())
        trad[slug] = {'name': p['name'], 'full': full, 'aliases': aliases, 'prs': prs}
    bridges = {}
    for fn in sorted(os.listdir(os.path.join(WIKI, 'synthesis'))):
        m = re.match(r'^([a-z]+)_([a-z]+)_bridge\.md$', fn)
        if m and m.group(1) in trad and m.group(2) in trad:
            bridges['|'.join(sorted([m.group(1), m.group(2)]))] = 'synthesis/' + fn
    name2slug = {v['name']: k for k, v in trad.items()}
    raw = json.load(open(os.path.join(ROOT, 'prototypes', 'signals_grown.json')))
    signals, unknown = [], set()
    for s in raw:
        a, b = name2slug.get(s.get('a')), name2slug.get(s.get('b'))
        if not a or not b:
            unknown.update([x for x in (s.get('a'), s.get('b')) if x not in name2slug])
            continue
        a, b = sorted([a, b])
        signals.append({'a': a, 'b': b, 'd': s.get('date', ''), 'st': s.get('strength', ''),
                        'w': s.get('weight', 0), 't': clip(s.get('text', ''), 400),
                        'n': clip(s.get('nature', ''), 90), 'src': s.get('source', '')})
    signals.sort(key=lambda x: (x['a'], x['b'], x['d'], x['t']))
    n_prs = sum(len(v['prs']) for v in trad.values())
    if not n_prs or not bridges or not signals:
        die('a source collapsed: prs=%d bridges=%d signals=%d' % (n_prs, len(bridges), len(signals)))
    empty = [k for k, v in trad.items() if not v['prs']]
    return {
        '_meta': {'generated': datetime.datetime.now().astimezone().isoformat(timespec='seconds'),
                  'builder': 'scripts/build_grounding_index.py',
                  'counts': {'traditions': len(trad), 'prs': n_prs, 'bridges': len(bridges),
                             'signals': len(signals), 'signals_skipped_unknown_name': len(raw) - len(signals)},
                  'traditions_without_prs': empty, 'unknown_signal_names': sorted(unknown)},
        'traditions': trad, 'bridges': bridges, 'signals': signals}

def main():
    idx = build()
    body = lambda d: json.dumps({k: v for k, v in d.items() if k != '_meta'}, sort_keys=True)
    if '--check' in sys.argv:
        try:
            old = json.load(open(OUT))
        except Exception:
            die('no committed grounding.json')
        if body(old) != body(idx):
            die('grounding.json is stale -- run scripts/build_grounding_index.py')
        print('grounding.json current')
        return
    try:
        if body(json.load(open(OUT))) == body(idx):
            print('grounding.json unchanged apart from _meta.generated -- not rewritten')
            return
    except Exception:
        pass
    with open(OUT + '.tmp', 'w', encoding='utf-8') as f:
        json.dump(idx, f, ensure_ascii=False, separators=(',', ':'))
    os.replace(OUT + '.tmp', OUT)
    print(json.dumps(idx['_meta']['counts']), os.path.getsize(OUT), 'bytes')
    if idx['_meta']['traditions_without_prs'] or idx['_meta']['unknown_signal_names']:
        sys.stderr.write('WARN: ' + json.dumps({k: idx['_meta'][k] for k in ('traditions_without_prs', 'unknown_signal_names')}) + '\n')

if __name__ == '__main__':
    main()
