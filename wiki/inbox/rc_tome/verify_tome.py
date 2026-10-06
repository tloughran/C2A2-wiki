import re, html, csv, sys, hashlib, collections
SRC, OUT = sys.argv[1], sys.argv[2]
raw = open(SRC, encoding='utf-8').read()
def clean(t): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',t))).strip()
norm_src = clean(raw)
units = list(csv.DictReader(open(f'{OUT}/tome_units.csv',encoding='utf-8')))
heads = list(csv.DictReader(open(f'{OUT}/tome_headings.csv',encoding='utf-8')))
fails=[]
def check(name, ok, detail=''):
    print(('PASS' if ok else 'FAIL'), name, detail)
    if not ok: fails.append(name)
# V1 independent count via grep-like
n_src = len(re.findall(r'<p class="doc-body[^>]*>', raw))
check('V1 counts', len(units)==n_src==1106, f'{len(units)} vs src {n_src}')
# V2 ids
ids=[u['unit_id'] for u in units]
check('V2 unique', len(set(ids))==len(ids))
check('V2 format', all(re.fullmatch(r'tome:p(\d{3}|APP)h\d{2}s\d{2}',i) for i in ids))
# V3 verbatim
bad=[u['unit_id'] for u in units if u['text'] not in norm_src]
check('V3 verbatim', not bad, f'{len(bad)} missing e.g. {bad[:3]}')
# V4
tot=sum(int(u['words']) for u in units); print('V4 word total', tot, 'delta vs 120810 =', tot-120810)
# V5 monotonic
pages=[u['page'] for u in units]; ok=True; prev=0
for p in pages:
    v = 10**6 if p=='appendix' else int(p)
    if v<prev: ok=False; break
    prev=v
check('V5 monotonic page', ok)
# V6 parentage
check('V6 parentage', all(u['page'] and u['heading_id'] for u in units))
# V7 ToC closure
hids=set(h['heading_id'] for h in heads)|set(x for h in heads for x in h.get('absorbed','').split(';') if x)|set(re.findall(r'id="(page-\w+)"',raw))
hrefs=re.findall(r'<a[^>]*class="toc-link[^"]*"[^>]*href="#([^"]+)"',raw) or re.findall(r'<a[^>]*href="#([^"]+)"[^>]*class="toc-link',raw)
miss=[h for h in hrefs if h not in hids]
check('V7 toc closure', len(hrefs)==615 and not miss, f'{len(hrefs)} hrefs, {len(miss)} unresolved {miss[:5]}')
print('SHA', hashlib.sha256(raw.encode()).hexdigest())
sys.exit(1 if fails else 0)
