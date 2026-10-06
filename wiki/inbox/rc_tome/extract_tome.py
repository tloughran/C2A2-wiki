import re, html, csv, hashlib, sys, os
SRC = sys.argv[1]; OUT = sys.argv[2]
os.makedirs(OUT, exist_ok=True)
raw = open(SRC, encoding='utf-8').read()
sha = hashlib.sha256(raw.encode('utf-8')).hexdigest()
tok = re.compile(r'<div class="page-marker" id="page-(\w+)"[^>]*>.*?</div>'
                 r'|<(h[1-4])([^>]*class="doc-h[1-4]"[^>]*)>(.*?)</\2>'
                 r'|<p class="doc-body"[^>]*>(.*?)</p>', re.S)
def clean(t):
    t = re.sub(r'<[^>]+>', '', t)
    t = html.unescape(t)
    return re.sub(r'\s+', ' ', t).strip()
page = 0; heads = []; units = []; ord_ = 0
hcount_on_page = 0; hid = None; hlvl = None; htext = None; seq = 0; hord = 0
unanch = 0
for m in tok.finditer(raw):
    if m.group(1):
        page = m.group(1); page = int(page) if page.isdigit() else 'appendix'; hcount_on_page = 0
    elif m.group(2):
        lvl = int(m.group(2)[1]); attrs = m.group(3); text = clean(m.group(4))
        idm = re.search(r'id="([^"]+)"', attrs)
        hcount_on_page += 1; hord += 1
        if idm: slug = idm.group(1)
        else:
            slug = f'p{page}-x{hcount_on_page}'; unanch += 1
        hid, hlvl, htext, seq = slug, lvl, text, 0
        heads.append(dict(heading_id=slug, page=page, level=lvl, ordinal=hord, heading_slug=slug if idm else '', text=text, reconstituted=0, anchored=1 if idm else 0))
    else:
        text = clean(m.group(5)); ord_ += 1; seq += 1
        h = hid if hid else f'p{page}-frontmatter'
        # heading ordinal within page: count of headings seen on this page so far (0 if none)
        pg = f'{page:03d}' if isinstance(page,int) else 'APP'
        uid = f'tome:p{pg}h{(hcount_on_page):02d}s{seq:02d}'
        units.append(dict(unit_id=uid, doc='tome', ord=ord_, page=page, heading_id=h, heading_level=hlvl or 0, seq=seq, words=len(text.split()), text=text))
with open(f'{OUT}/tome_units.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['unit_id','doc','ord','page','heading_id','heading_level','seq','words','text']); w.writeheader(); w.writerows(units)
with open(f'{OUT}/tome_headings.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['heading_id','page','level','ordinal','heading_slug','text','reconstituted','anchored']); w.writeheader(); w.writerows(heads)
print('sha256', sha); print('units', len(units), 'headings', len(heads), 'unanchored', unanch, 'words', sum(u['words'] for u in units))
