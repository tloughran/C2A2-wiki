import csv,re,collections,json
U=list(csv.DictReader(open('wiki/inbox/rc_tome/tome_units.csv',encoding='utf-8')))
H={h['heading_id']:h for h in csv.DictReader(open('wiki/inbox/rc_tome/tome_headings.csv',encoding='utf-8'))}
names=['Levin','Friston','Hoffman','Hawkins','McGilchrist','Fredrickson','Stump','Carroll','Arkani-Hamed','Wolfram','Kastrup','MacIntyre','Rohr','Wright','Aquinas','Hossenfelder','Deacon','Walker','Tononi','Whitehead','Goff','Kuhn','Solms','Penrose']
rx={n:re.compile(r'\b'+n.replace('-','[- ]')+r'\b') for n in names}
rx['Aquinas']=re.compile(r'\bAquinas\b|\bThomis(t|m)')
byp=collections.OrderedDict()
for u in U:
    if u['page']=='appendix': continue
    byp.setdefault(int(u['page']),[]).append(u)
pages=[]
for p,us in byp.items():
    c=collections.Counter()
    for u in us:
        for n,r in rx.items(): c[n]+=len(r.findall(u['text']))
    tot=sum(c.values()); top=c.most_common(1)[0] if tot else (None,0)
    dom = top[0] if top[1]>=3 and top[1]>=0.5*tot else ('MIXED' if tot>=4 else 'NONE')
    heads=list(dict.fromkeys(H[u['heading_id']]['text'] for u in us if u['heading_id'] in H and H[u['heading_id']]['page']==str(p)))
    pages.append(dict(page=p,words=sum(int(u['words']) for u in us),dom=dom,top=c.most_common(3),heads=heads,open=us[0]['text'][:90]))
# runs on dom, treating NONE as transparent (joins to previous)
runs=[]
for pg in pages:
    d=pg['dom']
    if runs and (d==runs[-1]['dom'] or d=='NONE'):
        runs[-1]['pages'].append(pg)
    else:
        runs.append(dict(dom=d,pages=[pg]))
out=[]
for r in runs:
    ps=r['pages']; w=sum(p['words'] for p in ps)
    heads=[h for p in ps for h in p['heads']]
    out.append(dict(dom=r['dom'],p0=ps[0]['page'],p1=ps[-1]['page'],words=w,nheads=len(heads),first_heads=heads[:3],open=ps[0]['open']))
json.dump(pages,open('wiki/inbox/rc_tome/page_profiles.json','w'),indent=0,ensure_ascii=False)
for o in out:
    print(f"p{o['p0']:>3}-{o['p1']:>3} {o['words']:6d}w {o['dom']:12s} heads={o['nheads']:2d} {str(o['first_heads'])[:70]:70s} | {o['open'][:60]}")
