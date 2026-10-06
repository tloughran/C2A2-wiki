import csv,collections,re
A=list(csv.DictReader(open('assignments.csv',encoding='utf-8')))
# reading order = sheet_row, then seq_in_row
def key(a): return (int(a['sheet_row']),int(a['seq_in_row']))
A.sort(key=key)
# titles: authored outline v2/v3 (verbatim), amendments applied
T=[
('I','THE APPARATUS — the accelerator/detector complex','outline v2 division I; the rules of the inter-tradition-dialogue game'),
('I.1','The diagnosis — why civility failed; what is at stake',''),
('I.2','MacIntyre\'s algorithm — the structure of evidence to be produced',''),
('I.2.1','Traditions as the unit of rational enquiry',''),
('I.2.2','Epistemological crisis and its resolution',''),
('I.2.3','Incommensurability and vindication on the rival\'s own terms',''),
('I.2.4','Natural law and intractable dispute','the IDM / IDNL reading seam'),
('I.3','The detector — what is observed when traditions meet',''),
('I.3.1','Observables: what counts as a signal','12 cells — thin; see the seventh-entry finding'),
('I.3.2','Scoring: rubrics, and the quantitative model of inter-tradition information transfer',''),
('I.3.3','Provenance and the evidentiary record','12 cells — thin'),
('I.4','The accelerator — controlled contact between traditions',''),
('I.4.1','Conditions of encounter: in person/online, in print, AI-accelerated',''),
('I.4.2','Rhetoric, invitation, and the boundedness of argument',''),
('I.4.3','Community as the medium',''),
('I.5','Failure modes — what would falsify the design','cornerstone: MacIntyre AV2:277; 9 cells — thin'),
('II','SOURCES AND FIGURES','outline v2 division II (renamed from "The Players", amendment)'),
('II.1','Membership — the criterion and the set','TO BE WRITTEN, NOT HARVESTED (Tom, amendment); no source cells'),
('II.2','Figures engaged','one node per figure, populated from `about`'),
('II.3','Modes of interaction — in person/online, in print, AI-accelerated in the vault',''),
('II.4','Bibliography and source pointers','cited works, bare URLs, reading notes'),
('III','THE POSITION — mind-only metaphysics and the layered account','outline v2 division III'),
('III.1','The core claim — conscious realist monism',''),
('III.1.1','Against physicalist priority','incl. rival positions at full strength: IIT, GNW'),
('III.1.2','Prediction, modeling, interface, and the construction of ideas',''),
('III.1.3','Truth as an achieved relation between intellect and object',''),
('III.2','The layered account — "a comprehensive, hierarchical, computational theory of intelligence, both theoretical and practical"','authored: r251c5; rebuilt on TL\'s own ladder, sheet rows 247-250 (v3)'),
('III.2.0','The ladder itself — 8 rungs x 3 passes, rendered as a grid','AUTHORED STRUCTURE: header row 247 A I S N B P C S (r246c4..c11); passes at rows 248-250; a second, earlier ladder at row 292 (r291c3) — compare before writing'),
('III.2.A','L0 Awareness','A-I-S band: physics, CS, philosophy contribute (r251c5)'),
('III.2.I','L1 Information',''),
('III.2.S','L2 Space-Time','S appears twice in the header (Space-Time, Social) — never merge'),
('III.2.N','L5 Neuronal','S-N-B-P band (r253c6); sub-neuronal biology filed here pending the S->N rung question (L3 pre-biotic, L4 cellular proposed, no node yet)'),
('III.2.B','L6 Brain / neocortical column','NEW in v3; r247c8 "the thousand brains of TBT ... at the neocortical column"'),
('III.2.P','L7 Personal','P-C-S band: psychology, sociology, MacIntyre'),
('III.2.C','L8 Communal',''),
('III.2.SO','L9 Social',''),
('III.2.X','Cross-level claims','"Empirical everywhere. Philosophy and Computer science at every level."; computation as matrix multiplication'),
('III.3','Goods, freedom, and the will — the ethical spine; natural law',''),
('III.4','Love, community, and the person',''),
('X','SHEET APPARATUS — retained in the table, excluded from the reading document','apparatus division (= toc_role apparatus)'),
('X.1','Numeric and bookkeeping cells','bare numbers, subtotals, "Sum by row headers"'),
('X.2','In-sheet labels, stray table headers, numbered list items','row-header rule (Tom): a substantive row header confers content; bare items in that row are placed topically, not here'),
('Z','HOLDING PEN — unclassified content','visible, never hidden'),
]
byn=collections.defaultdict(list)
for a in A: byn[a['node']].append(a)
def members(nid):
    return [a for a in A if a['node']==nid or a['node'].startswith(nid+'.')]
rows=[]
for nid,title,note in T:
    depth=nid.count('.')+1
    parent='' if depth==1 else nid.rsplit('.',1)[0]
    m=members(nid)
    rows.append(dict(node_id=nid,parent_id=parent,depth=depth,title=title,
        page_start=min(int(a['sheet_row']) for a in m) if m else '',page_end=max(int(a['sheet_row']) for a in m) if m else '',
        note=note,anchor_unit=('sandbox:'+m[0]['cell_id']) if m else '',anchor_heading='',headings_inside=0,
        words=sum(int(a['words']) for a in m),
        toc_role='apparatus' if nid.split('.')[0]=='X' else 'structural',
        cells=len(byn.get(nid,[])),cells_incl=len(m)))
with open('toc_sandbox.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
# verify: every assignment node is a ToC node; division totals tile the corpus
nodes=set(r['node_id'] for r in rows); used=set(a['node'] for a in A)
print('assignment nodes not in ToC:',used-nodes)
tot=sum(int(a['words']) for a in A); div=sum(r['words'] for r in rows if r['depth']==1)
print('words total',tot,'sum over divisions',div,'cells',len(A),sum(r['cells_incl'] for r in rows if r['depth']==1))
print('empty nodes:',[r['node_id'] for r in rows if r['cells_incl']==0])
for r in rows:
    if r['depth']<=2: print(f"{r['node_id']:8s} {r['cells_incl']:5d} cells {r['words']:6d}w  {r['title'][:60]}")
