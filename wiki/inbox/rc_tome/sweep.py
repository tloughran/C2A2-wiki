import csv,re,collections,json
U=list(csv.DictReader(open('wiki/inbox/rc_tome/tome_units.csv',encoding='utf-8')))
H=list(csv.DictReader(open('wiki/inbox/rc_tome/tome_headings.csv',encoding='utf-8')))
FIG={ # key: regex
 'Levin':r"\bLevin\b",'Friston':r"\bFriston\b",'Hoffman':r"\bHoffman\b",'Hawkins':r"\bHawkins\b",'McGilchrist':r"\bMcGilchrist\b",
 'Fredrickson':r"\bFredrickson\b",'Stump':r"\bStump\b",'Carroll':r"\bCarroll\b",'Arkani-Hamed':r"\bArkani[- ]Hamed\b",'Wolfram':r"\bWolfram\b",
 'Kastrup':r"\bKastrup\b",'MacIntyre':r"\bMacIntyre\b",'Rohr':r"\bRohr\b",'Wright':r"\bN\.?\s?T\.? Wright\b|\bWright\b",'Aquinas':r"\bAquinas\b|\bThomistic\b|\bThomism\b",
 'Hossenfelder':r"\bHossenfelder\b",'Deacon':r"\bDeacon\b",'Walker':r"\bSara Walker\b|\bWalker\b",'Kuhn':r"\bKuhn\b",'Whitehead':r"\bWhitehead\b",
 'Chalmers':r"\bChalmers\b",'Tononi':r"\bTononi\b|\bIIT\b",'Penrose':r"\bPenrose\b",'Solms':r"\bSolms\b",'Kauffman':r"\bKauffman\b",'Bohm':r"\bBohm\b",
 'Teilhard':r"\bTeilhard\b",'Goff':r"\bGoff\b",'Dennett':r"\bDennett\b",'Aristotle':r"\bAristotle\b|\bAristotelian\b",'Plato':r"\bPlato\b|\bPlatonic\b",
 'Kant':r"\bKant\b|\bKantian\b",'Nagel':r"\bNagel\b",'Seth':r"\bAnil Seth\b",'Clark':r"\bAndy Clark\b",'Fields':r"\bChris Fields\b",'Bongard':r"\bBongard\b",
 'Habash':r"\bHabash\b",'Karpathy':r"\bKarpathy\b",'Pieper':r"\bPieper\b",'Wittgenstein':r"\bWittgenstein\b",'Polanyi':r"\bPolanyi\b",'Lonergan':r"\bLonergan\b",
 'Freddoso':r"\bFreddoso\b",'Augustine':r"\bAugustine\b",'Girard':r"\bGirard\b",'Taylor':r"\bCharles Taylor\b",'Hegel':r"\bHegel\b",'Heidegger':r"\bHeidegger\b",
}
RX={k:re.compile(v) for k,v in FIG.items()}
for u in U:
    u['fig']={k:len(r.findall(u['text'])) for k,r in RX.items()}; u['fig']={k:v for k,v in u['fig'].items() if v}
tot=collections.Counter()
for u in U: tot.update(u['fig'])
print('figure totals (mentions):'); print(tot.most_common())
# per-heading aggregation, in heading order
hid_order=[h['heading_id'] for h in H]; byh=collections.defaultdict(list)
for u in U: byh[u['heading_id']].append(u)
rows=[]
for h in H:
    us=byh.get(h['heading_id'],[]); c=collections.Counter()
    for u in us: c.update(u['fig'])
    words=sum(int(u['words']) for u in us)
    dom=c.most_common(3)
    rows.append(dict(hid=h['heading_id'],page=h['page'],level=h['level'],text=h['text'],units=len(us),words=words,top=dom))
json.dump(rows,open('wiki/inbox/rc_tome/heading_profiles.json','w'),indent=0,ensure_ascii=False)
# print h1 list with profile
print('\n=== current H1s with cumulative span profile until next H1')
i=0
while i<len(rows):
    if rows[i]['level']!='1': i+=1; continue
    j=i+1
    while j<len(rows) and rows[j]['level']!='1': j+=1
    c=collections.Counter(); w=0
    for r in rows[i:j]:
        for k,v in r['top']: c[k]+=v
        w+=r['words']
    print(f"p{rows[i]['page']:>3} {w:6d}w  {rows[i]['text'][:60]:60s} | {c.most_common(4)}")
    i=j
