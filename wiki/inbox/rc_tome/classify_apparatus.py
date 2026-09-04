import csv,re,json
ROOT='wiki/inbox/rc_tome/'
H=list(csv.DictReader(open(ROOT+'tome_headings.csv',encoding='utf-8')))
W={r['hid']:r['words'] for r in json.load(open(ROOT+'heading_profiles.json'))}
APP=re.compile(r'^(word count|current progress|current word|estimated time|timeline to|status\b|immediate (status|next|focus|work)|quick (preview|reassurance|confirmation|recap|reminder|praise)|next (step|move|action|output)s?\b|target\b|here.s (the plan|what|how|the sequence|the structure)|i am now ready|ready\b|posting plan|final step|work method|action plan|what i.ll do|what i propose|would you|let.s address|summary of this entry|total section|full section 2|word counts?\b|revised word count|notes on style|key differences|features of this|reminder\b|estimated\b|current\b|summary:$|in summary$|conclusion:$|closing (thought|transition|critical)|final comment|tools for revision|full work plan|remaining work plan|section iv revision underway|concrete targets|suggested next steps|suggested immediate)',re.I)
KEEP=re.compile(r'^(corrected|ultimate model|philosophical ancestry|brutal reply|task fidelity|my recommendation|updated recommended fix)',re.I)
n=0
for h in H:
    t=h['text'].strip(); w=W.get(h['heading_id'],0)
    app=bool(APP.match(t)) and not KEEP.match(t) and w<250
    h['toc_role']='apparatus' if app else 'structural'; n+=app
with open(ROOT+'tome_headings.csv','w',newline='',encoding='utf-8') as f:
    wr=csv.DictWriter(f,fieldnames=list(H[0].keys())); wr.writeheader(); wr.writerows(H)
print('apparatus',n,'structural',len(H)-n)
