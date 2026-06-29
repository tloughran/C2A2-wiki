#!/usr/bin/env python3
"""Backlog manifest + QC-tracer scaffold for the cross-signal backlog clear.
Targets APPROVED cards not yet cross-signal-processed (review gate intact).
Pure deterministic accounting — no model calls. Emits:
  backlog_manifest.json  (the 159 to process, ordered by source_date)
  qc_trace.csv           (one empty row per card; the standing pass fills it)
"""
import glob,os,re,json,csv,sys
VAULT=sys.argv[1] if len(sys.argv)>1 else "."
OUT=sys.argv[2] if len(sys.argv)>2 else "/tmp"
sig=json.load(open(sys.argv[3])) if len(sys.argv)>3 else []
def base(p):
    m=re.match(r'(PROP-2026-\d{2}-\d{2}-?\d*)',p or ''); return m.group(1) if m else (p or '')
processed=set(base(s['card']) for s in sig if s.get('card'))
rows=[]
for f in glob.glob(os.path.join(VAULT,'inbox/proposals/approved/*.md')):
    txt=open(f,errors='ignore').read()
    pid=(re.search(r'proposal_id:\s*(PROP-2026-\d{2}-\d{2}-?\d*)',txt) or
         re.search(r'(PROP-2026-\d{2}-\d{2}-?\d*)',os.path.basename(f)))
    if not pid: continue
    pid=pid.group(1)
    if base(pid) in processed: continue   # already has signals
    trad=(re.search(r'tradition_key:\s*(\w+)',txt) or [None,''])[1] if re.search(r'tradition_key:\s*(\w+)',txt) else ''
    sdate=(re.search(r'source_date:\s*([0-9-]+)',txt) or [None,''])[1] if re.search(r'source_date:\s*([0-9-]+)',txt) else ''
    title=(re.search(r'source_title:\s*"?([^"\n]+)',txt) or [None,''])[1] if re.search(r'source_title:',txt) else ''
    rows.append({'card':pid,'tradition':trad,'source_date':sdate or pid[5:15],
                 'title':title.strip()[:90],'file':os.path.relpath(f,VAULT),'processed':False})
rows.sort(key=lambda r:r['source_date'])
json.dump(rows,open(os.path.join(OUT,'backlog_manifest.json'),'w'),indent=1)
with open(os.path.join(OUT,'qc_trace.csv'),'w',newline='') as fh:
    w=csv.writer(fh)
    w.writerow(['card','tradition','source_date','processed_by','date_processed',
                'signals_emitted','cross_refs','finding_refs','dup_check','status','notes'])
    for r in rows:
        w.writerow([r['card'],r['tradition'],r['source_date'],'','','', '','','','PENDING',''])
from collections import Counter
bm=Counter(r['source_date'][:7] for r in rows)
print('APPROVED backlog to process:',len(rows))
print('by month:',dict(sorted(bm.items())))
print('by tradition:',dict(Counter(r['tradition'] for r in rows).most_common()))
print('wrote backlog_manifest.json + qc_trace.csv to',OUT)
