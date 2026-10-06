#!/usr/bin/env python3
"""Block-parser scan of for_lit_search.md (v2, 2026-09-22).
Header forms recognised (all three are in live use in this file):
  1.  ITEM: ASSUMPTION-NNN [TAGS]
  2.  ASSUMPTION-NNN:            (followed by an indented 'Status:' line)
  3.  [ASSUMPTION] ASSUMPTION-NNN: ...   (15d RE-TRIGGER cohort form)
A block runs to the next header. An item COUNTS only if the block contains an indented
'Status:' line or a tag bracket on the header -- this excludes prose paragraphs that merely
mention an ID, which is what inflates naive greps. Tags are matched across the WHOLE block,
because 15a/15b summaries wrap onto continuation lines; a line-anchored grep misses them and
reports items as unsearched that were searched and dispositioned months ago."""
import re, sys
p = sys.argv[1] if len(sys.argv) > 1 else 'for_lit_search.md'
L = open(p, encoding='utf-8').read().split('\n')
hdr = re.compile(r'^(?:ITEM:\s*|\[(?:ASSUMPTION|PRESUMPTION)\]\s*)?((?:ASSUMPTION|PRESUMPTION)-\d+)\b\s*[:\[]')
starts = [i for i, l in enumerate(L) if hdr.match(l)]
blocks = []
for n, i in enumerate(starts):
    j = starts[n+1] if n+1 < len(starts) else len(L)
    body = '\n'.join(L[i:j])
    if not (re.search(r'^\s+Status:', body, re.M) or '[' in L[i]):
        continue                                   # prose mention, not an item
    blocks.append((hdr.match(L[i]).group(1), i+1, body))
Q = [b for b in blocks if '[QUEUED]' in b[2] or '[QUEUED-EMPIRICAL]' in b[2]]
def sel(f): return [b for b in Q if f(b[2])]
lit  = sel(lambda t: '[QUEUED-EMPIRICAL]' not in t and '[IN-HOUSE]' not in t
                     and 'NO-LIT-OWED' not in t and 'NOT-SEARCHED' not in t)
emp  = [b for b in Q if b not in lit]
undisp = [b for b in lit if 'SEARCHED-15a' in b[2] and 'SEARCHED-15b' in b[2] and 'DISPOSITIONED-15c' not in b[2]]
halfa  = [b for b in lit if 'SEARCHED-15a' in b[2] and 'SEARCHED-15b' not in b[2] and 'DISPOSITIONED-15c' not in b[2]]
bare   = [b for b in lit if not any(t in b[2] for t in ('SEARCHED-15a','SEARCHED-15b','DISPOSITIONED-15c'))]
print(f'item blocks parsed (Status-bearing)        : {len(blocks)}')
print(f'  carrying [QUEUED] or [QUEUED-EMPIRICAL]  : {len(Q)}')
print(f'  ..literature lane                        : {len(lit)}')
print(f'  ..empirical / in-house / no-lit-owed     : {len(emp)}')
print()
print(f'SEARCHED BY BOTH, NOT DISPOSITIONED        : {len(undisp)}   <- must be 0')
for x in undisp[:25]: print(f'    {x[0]} @ line {x[1]}')
print(f'15a only, no 15b, not dispositioned        : {len(halfa)}')
for x in halfa[:25]: print(f'    {x[0]} @ line {x[1]}')
print(f'BARE [QUEUED], literature lane, unsearched : {len(bare)}   <- THE BACKLOG')
from collections import Counter
yrs = Counter(re.search(r'20\d\d-\d\d-\d\d', b[2]).group(0)[:7] if re.search(r'20\d\d-\d\d-\d\d', b[2]) else '??' for b in bare)
print('  by first date appearing in block:', dict(sorted(yrs.items())))
