import fitz, json, re, hashlib, sys, os
SRC = '/Users/tomloughran/Downloads/C2A2_Explorer_Complete_User_Guide.pdf'
OUT = sys.argv[1]
shots = os.path.join(OUT, 'shots'); os.makedirs(shots, exist_ok=True)
doc = fitz.open(SRC)
entries, hashes = [], {}
for pno in range(doc.page_count):
    page = doc[pno]
    imgs = page.get_images(full=True)
    if not imgs:
        continue
    lines = [l.strip() for l in page.get_text().strip().split('\n') if l.strip()]
    foot = lines[-1]
    m = re.match(r'^(\S+\.png)\s+·\s+page\s+(\d+)$', foot)
    if not m:
        print('!! no slug footer on pdf page', pno + 1, '->', foot); continue
    fname, printed_page = m.group(1), int(m.group(2))
    kicker, title = lines[0], lines[1]
    sec = re.match(r'^([\d.]+)\s+(.*)$', kicker)
    secnum, secname = (sec.group(1), sec.group(2)) if sec else ('', kicker)
    caption = ' '.join(l for l in lines[2:] if l != foot)
    xref = imgs[0][0]
    pix = doc.extract_image(xref)
    blob = pix['image']
    path = os.path.join(shots, fname)
    with open(path, 'wb') as f:
        f.write(blob)
    h = hashlib.sha256(blob).hexdigest()
    hashes.setdefault(h, []).append(fname)
    entries.append({
        'slug': fname[:-4],
        'file': fname,
        'section': secnum,
        'section_title': secname,
        'title': title,
        'caption': caption,
        'viewport': [pix['width'], pix['height']],
        'sha256': h,
        'pdf_page': printed_page,
    })
dupes = {h: v for h, v in hashes.items() if len(v) > 1}
manifest = {
    '_about': 'Recovered from C2A2_Explorer_Complete_User_Guide.pdf (117pp, captured 2026-07-26). '
              'Plates and captions are authoritative; reach-recipes are NOT yet present.',
    'schema': 'c2a2-guide-manifest/0',
    'recovered_from': os.path.basename(SRC),
    'captured': '2026-07-26',
    'counts': {'plates': len(entries), 'duplicate_hashes': len(dupes)},
    'plates': entries,
}
with open(os.path.join(OUT, 'manifest.json'), 'w') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)
print('plates:', len(entries), '| duplicate hashes:', len(dupes), dupes if dupes else '')
from collections import Counter
print('viewports:', Counter(tuple(e['viewport']) for e in entries))
