import csv,json,re,collections
ROOT='wiki/inbox/rc_tome/'
U=list(csv.DictReader(open(ROOT+'tome_units.csv',encoding='utf-8')))
H=list(csv.DictReader(open(ROOT+'tome_headings.csv',encoding='utf-8')))
# (kind, title, p0, p1, seam_note)   kind: P part, C chapter, S section
T=[
('P','Project Launch and Research Foundations',1,40,'authored outline, phase I (p396)'),
('C','Opening: an AI-ethics mind map',1,3,'Tom: "Can you draw a mind map for AI ethics"'),
('C','Bibliographic deep dives, thinker by thinker',3,40,''),
('S','Michael Levin: comprehensive bibliography and overview',3,16,'existing H1 p4; Tom p16: "Now, based on these sources, can you provide a 1000 word overview"'),
('S','Donald Hoffman: bibliography, biography, podcasts',17,23,'NEW SEAM. No heading. Tom p17: "Yes, please do, but expect to backfill each section with his more recent work"'),
('S','Stephen Wolfram: biography, works, podcasts',24,26,'NEW SEAM. No heading. Model p24: "Stephen Wolfram is a distinguished computer scientist..."'),
('S','Jeff Hawkins: books, career, podcasts',27,30,'NEW SEAM. No heading. p27 "Books: 1. On Intelligence"; Tom p28: "you left out his podcast appearances"'),
('S','Sean Carroll: publications, Mindscape, biography',31,37,'NEW SEAM at p31 (Tom: "top 100 guests ... Mindscape ... After this fifth research set"); existing H3s p33-37 were filed under Levin'),
('S','Sabine Hossenfelder: a leading critic',38,40,'Tom p38: "Let us put a pause ... add another bio, not of a leading contributor but a leading commentator/critic"; existing H3 "Biography" p38 was under Levin'),
('P','Framework Integration and Thematic Convergence',41,103,'authored outline, phase II'),
('C','Sean Carroll\'s critique of consciousness-centric universe models',41,53,'existing H1 p41 (wrapped heading, reconstituted); includes QHT vs WPP comparison p51-53'),
('C','Current and potential research agendas, thinker by thinker',54,100,'Tom p54: "Now let us look over all these thinkers and their programs, using the lens of current actionable research"'),
('S','Structure (for each thinker)',54,54,'existing H3'),
('S','Donald Hoffman: research agenda',55,58,'existing H2, was buried under Carroll H1'),
('S','Michael Levin: research agenda; basins of morphological attraction',59,63,'existing H2 + H3s'),
('S','Karl Friston: biography and scientific contributions',64,67,'existing H2; Tom p64 pivot "shall we pivot now to..."'),
('S','Levin x Friston: extensions via free energy and least action',68,70,'existing H2 (reconstituted)'),
('S','Toward a theory of communal active inference and morphogenesis',71,76,'existing H2 (reconstituted)'),
('S','Theological reframing: N.T. Wright, Richard Rohr, Christic morphogenesis',77,84,'existing H2 p77; Tom p78: "Now, let us integrate this with theological language drawn from N.T. Wright and Richard Rohr"'),
('S','Barbara Fredrickson: biography, podcasts, Love 2.0',85,91,'existing H2 "Step 1: Bio/Bibliography of Barbara Fredrickson"; Tom p85 "I will peel out..."'),
('S','Reframing love across scientific and theological registers',92,96,'existing H2 p93; Tom p92-93 poses the three questions'),
('S','Stephen Wolfram: research agenda',97,100,'existing H2; Tom p97: "Now let us proceed" to Wolfram'),
('C','Reflecting on the turn: from synthesis to truth-seeking',101,103,'existing H2 p101; Tom p101: "I will want to draw on work by Alasdair MacIntyre and Thomas Aquinas. But first, let us pause to reflect on this change of direction"'),
('P','Methodological Strategy: Synergistic Planks and Traditions-in-Dialogue',104,167,'authored outline, phase III'),
('C','Aquinas, De Veritate q.2 a.14: God\'s knowledge as the cause of things',104,107,'existing H1 (reconstituted)'),
('C','Designated perspective, mind-to-mind correspondence, synergy planks',108,121,'existing H2s I-IV p109-111 (wrapped, reconstituted) + plank template Step 1/Step 2'),
('C','Summary of progress and strategic positioning',122,124,'existing H2 p122'),
('C','MacIntyre: traditions as social information processors; toward a tradition of inquiry',125,139,'Tom p125: "Let us proceed to weave in MacIntyre"; existing H2s 1-4, Summary Reflection, CNL summary, Next Steps'),
('C','Two uploaded papers: Four Models of Cultural Exchange; Computational Natural Law',140,144,'existing H2 Document 1 / Document 2; Tom p140 uploads the PDFs'),
('C','Reframing the arc: game and team; two amendments; adjusted working framework',145,150,'existing H2s p145-149'),
('C','Authorship, AI collaboration, and the graduate-student analogy',151,163,'Tom p151: "I had an outline, not yet shared with you, of each of two papers"; existing H2s p151-162'),
('C','The immediate paper project and a working structure',164,167,'existing H2 p164 "Understanding Your Immediate Paper Project"'),
('P','Structural Refinement and Presentation Development',168,371,'authored outline, phase IV'),
('C','The reformulated thesis: Being, Life, Intelligence (BLI)',168,172,'existing H1 "Step 1: Comparing Your Reformulated Thesis"'),
('C','Digression: podcast appearances by pair; Iain McGilchrist added',173,185,'Tom p173: "Back from exercise, but I would like to interject a research project"; McGilchrist bio p179 (existing H3s); revised joint table p181'),
('C','Mapping an emerging interdisciplinary network, 2014-2024 (deep research)',186,198,'existing H1 (reconstituted)'),
('C','Digression: the output-files gap — task fidelity, self-critique, working protocols',199,211,'Tom p199: "Have I missed links to the two output documents?"; model p203: "Let me be very direct"; p205-210 protocols'),
('C','Dataset of documented connections and a first sociogram',212,215,'existing H1 p212; Tom p212: "aim at the scientific dataset. Remove Rohr and Wright"'),
('C','Experiments in co-authorship: the submitted draft (Intro + Sections I-II) and the cold critical review',216,229,'NEW SEAM p216. Tom: "Let us put a pin in this portion of the research, and move on to the paper. I have thus far written an introduction and section 2"; his draft prose runs p216-220 ("Enter Mike Levin..."), VOICE=TL — confirmed by the model at p221: "You fulfill the planned content for the Introduction, Section I, and Section II"; existing H1s Task Fidelity Check, Cold Critical Review'),
('C','Critical action plan; rewritten Introduction and Sections I-II',230,242,'existing H1s p228-238 (Critical Action Plan, Rewritten Introduction/Section I/II)'),
('C','Plan for the full paper: structure, target, work method',243,254,'Tom p243 approves expanding the outline; existing H1s Here is the Plan / Work Method'),
('C','Section 1 draft and the corrected restatement of the model',255,268,'Tom p255: "Yes, do show me section 1"; existing H1 Section 1; Corrected Restatement / Ultimate Model p264-266'),
('C','Section 2: thinker profiles',269,298,'Tom-approved profiles: Levin, Hoffman (+NAH revision), Wolfram, Hawkins, Friston, McGilchrist, Fredrickson; assembled Parts 1-2 p290-298'),
('S','Levin and Hoffman profiles',269,273,'existing H1s p269-272'),
('S','Wolfram and Hawkins profiles',277,279,'existing H1s'),
('S','Friston, McGilchrist, Fredrickson profiles',283,289,'existing H1s'),
('S','Section 2 assembled: Part 1 (Levin, Hoffman, Wolfram, Hawkins), Part 2 (Friston, McGilchrist, Fredrickson)',290,298,'existing H1s Section 2 Part 1 / Part 2 (reconstituted)'),
('C','Section 1 rewritten; remaining work plan',299,308,'Tom p299: "Yes, please do that rewriting quickly ... then revisit the brutal reply set"'),
('C','Brutal replies reframed; revised scope; the 20-minute outline',309,319,'existing H1s Brutal Reply #1/#2, Revised Scope, New Brutally Precise Outline'),
('C','Wireframe first draft and self-evaluation',320,326,'Tom p320: "Let us sketch a wireframe first draft"'),
('C','Draft prose: Introduction (two passes), II, III, IV (two versions), V, VI',327,346,'existing H1s p327-346'),
('C','ACPQ submission: guidelines, abstract, objections and responses, targeted revisions, footnotes',347,371,'existing H1 ACPQ Submission Guidelines p347; footnotes 4-8 p367; Carroll-dominant p369-371'),
('P','Section IV Rewrite, Formatting, and Compliance',372,401,'authored outline phases IV (Section IV rewrite) and V (formatting)'),
('C','Revised Section IV: scholars table, individual summaries, interactions',372,381,'Tom p372: "brief introduction to each, alone ... then a separate paragraph highlighting interactions"; existing H1 is the 27k-word catch-all'),
('C','Section IV replaces IV (not V); Section V restored and revised',382,388,'Tom p382: "I transformed section iv, not v, and it should replace section iv"'),
('C','Manuscript formatting, footnotes (MacIntyre 3RV, Arkani-Hamed), ACPQ export',389,395,'Tom p389: "Let us add a couple of footnotes"; p393 Arkani-Hamed footnote'),
('C','Outline of the conversation\'s main phases; stages plan for what follows',396,401,'Tom p396: "reload this entire conversation, and add to it an outline of its main phases"; Tom p401 sets Stages 1-4'),
('P','Extending the Cluster and the Second Paper',402,471,'beyond the authored outline (which ends at p401)'),
('C','Bernardo Kastrup: biography, thought, relations to each researcher, integration, conversations',402,415,'Stage 1 (a)-(e); existing H2/H3s p402-415'),
('C','Alignment test: truth within the CR paradigm versus Kastrup',416,421,'Tom p416 asks how truth is understood in the CR paradigm'),
('C','Synergistic coils: the PRS table; one coil, multiple rows',422,424,'Stage 2; existing H3s'),
('C','Terrence Deacon: biography, core concepts; brainstorm in brutal mode',425,436,'existing H3 Biography p426; Tom p428: "I would like to brainstorm a bit here"'),
('C','Paper 2: Resurrecting Thomism at the dawn of the CR paradigm (DCEC)',437,449,'Tom p437 sets the goal; abstract p439; Kastrup/Friston/Walker parallels p443-445'),
('C','Experiments in co-authorship: the DCEC draft text',450,457,'NEW SEAM. Tom p450: "Let me re-present here not only the outline, but substantially more content"; VOICE=TL; currently filed under H3 "Suggested Next Steps"'),
('C','Response to the draft; status of the two papers; Introduction revised',458,463,'existing H3s p458-462'),
('C','Eleonore Stump\'s 2025 Maritain Lecture; twenty rich communities',464,471,'existing H3s p464-471; Tom p468 upload attempt'),
('P','Appendix: Works Consulted',472,472,'page marker page-appendix; 128 bibliography units; 22 unclassed h4 headings'),
]
# assign ids and parents
nodes=[]; pc=0; cc=0; sc=0; cur_p=None; cur_c=None
for kind,title,p0,p1,note in T:
    if kind=='P': pc+=1; cc_local=0; nid=f'P{pc}'; parent=''; cur_p=nid; depth=1
    elif kind=='C': cc+=1; nid=f'C{cc}'; parent=cur_p; cur_c=nid; depth=2
    else: sc+=1; nid=f'S{sc}'; parent=cur_c; depth=3
    nodes.append(dict(node_id=nid,parent_id=parent,depth=depth,title=title,page_start=p0,page_end=p1,note=note))
# anchors: first unit whose page>=p0 (appendix handled)
def pnum(p): return 472 if p=='appendix' else int(p)
for n in nodes:
    first=next(u for u in U if pnum(u['page'])>=n['page_start'])
    n['anchor_unit']=first['unit_id']
    # existing headings inside range
    hs=[h for h in H if h['page']!='' and (pnum(h['page']) if h['page']!='appendix' else 472)>=n['page_start'] and (pnum(h['page']) if h['page']!='appendix' else 472)<=n['page_end']]
    n['headings_inside']=len(hs)
    onpage=[h for h in hs if (pnum(h['page']) if h['page']!='appendix' else 472)==n['page_start']]
    top=[h for h in onpage if int(h['level'])<=2]
    n['anchor_heading']=(top or onpage or [{'heading_id':''}])[0]['heading_id']
    n['words']=sum(int(u['words']) for u in U if n['page_start']<=pnum(u['page'])<=n['page_end'])
with open(ROOT+'toc_v2.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(nodes[0].keys())); w.writeheader(); w.writerows(nodes)
# coverage check: chapters must tile each part; sections tile within chapter where present
def tiles(children,lo,hi):
    if not children: return True
    ok=children[0]['page_start']==lo and children[-1]['page_end']>=hi
    for a,b in zip(children,children[1:]):
        if b['page_start']<a['page_start'] : ok=False
    return ok
for p in [n for n in nodes if n['depth']==1]:
    ch=[n for n in nodes if n['parent_id']==p['node_id']]
    print(p['node_id'],p['page_start'],p['page_end'],'chapters',len(ch),'tiled' if tiles(ch,p['page_start'],p['page_end']) else 'GAP', sum(c['words'] for c in ch),'w')
print('nodes',len(nodes),'parts',pc,'chapters',cc,'sections',sc)
# current H1 breaks vs chapter starts
h1pages=set(pnum(h['page']) for h in H if h['level']=='1')
starts=[n['page_start'] for n in nodes if n['depth']==2]
print('chapter starts coinciding with an existing H1 page:',sum(1 for s in starts if s in h1pages),'/',len(starts))
print('existing H1s:',len(h1pages),'; H1 pages that are NOT chapter starts:',len(h1pages-set(starts)))
