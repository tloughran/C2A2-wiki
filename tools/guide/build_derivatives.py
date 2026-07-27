#!/usr/bin/env python3
"""Build the WebP derivatives the guide actually serves.

The 1440-px PNGs in shots/ are build inputs, not shipped assets: they are gitignored,
and the PDF regenerates them (see recover_from_pdf.py). What ships is web/, and only
web/ is committed.

Each plate becomes two files, so the guide can serve a srcset:

    web/2x/<slug>.webp   native capture width (1440, or 390 for the phone plates)
    web/1x/<slug>.webp   half width, for the ~720 CSS px the guide displays at

Quality 86 is deliberate. These are screenshots of dark UI with small anti-aliased
label text, which is the case WebP handles worst; below ~80 the sub-tab row and the
Sociogram's foot counters start to smear, and an unreadable control in a manual that
exists to point at controls is not a saving.

Writes the derivative paths and byte sizes back into manifest.json.
"""
import json
import os
import sys

from PIL import Image

QUALITY = 86
METHOD = 6

HERE = os.path.dirname(os.path.abspath(__file__))


def main(root=HERE):
    shots = os.path.join(root, 'shots')
    manifest_path = os.path.join(root, 'manifest.json')
    with open(manifest_path) as f:
        manifest = json.load(f)

    for scale in ('1x', '2x'):
        os.makedirs(os.path.join(root, 'web', scale), exist_ok=True)

    total = {'1x': 0, '2x': 0, 'png': 0}
    for entry in manifest['plates']:
        src = os.path.join(shots, entry['file'])
        if not os.path.exists(src):
            sys.exit('missing plate: %s -- run recover_from_pdf.py first' % entry['file'])
        total['png'] += os.path.getsize(src)
        im = Image.open(src).convert('RGB')

        out2 = os.path.join(root, 'web', '2x', entry['slug'] + '.webp')
        im.save(out2, 'WEBP', quality=QUALITY, method=METHOD)

        out1 = os.path.join(root, 'web', '1x', entry['slug'] + '.webp')
        im.resize((im.width // 2, im.height // 2), Image.LANCZOS).save(
            out1, 'WEBP', quality=QUALITY, method=METHOD)

        entry['web'] = {
            '1x': 'web/1x/%s.webp' % entry['slug'],
            '2x': 'web/2x/%s.webp' % entry['slug'],
            'bytes_1x': os.path.getsize(out1),
            'bytes_2x': os.path.getsize(out2),
        }
        total['1x'] += entry['web']['bytes_1x']
        total['2x'] += entry['web']['bytes_2x']

    manifest['derivatives'] = {
        'quality': QUALITY,
        'total_bytes_1x': total['1x'],
        'total_bytes_2x': total['2x'],
    }
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    mb = lambda b: '%.1f MB' % (b / 1048576.0)
    print('plates: %d' % len(manifest['plates']))
    print('  png (gitignored) %s' % mb(total['png']))
    print('  webp 2x          %s' % mb(total['2x']))
    print('  webp 1x          %s' % mb(total['1x']))
    print('  committed total  %s' % mb(total['1x'] + total['2x']))


if __name__ == '__main__':
    main()
