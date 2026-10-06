"""Render ToC v2 into wiki/rc_document_explorer.html. Deterministic; re-run after editing toc_v2.csv.
Replaces the <ul class="toc-root"> block; adds id="u-<unit>" to paragraphs that ToC nodes anchor to.
Body text untouched. Old heading ids untouched."""
import csv,re,html,sys
ROOT='wiki/inbox/rc_tome/'; HTML='wiki/rc_document_explorer.html'
N=list(csv.DictReader(open(ROOT+'toc_v2.csv',encoding='utf-8')))
H=list(csv.DictReader(open(ROOT+'tome_headings.csv',encoding='utf-8')))
U=list(csv.DictReader(open(ROOT+'tome_units.csv',encoding='utf-8')))
s=open(HTML,encoding='utf-8').read()
def pn(p): return 472 if p=='appendix' else int(p)
# --- 1. ids on anchored paragraphs
need={n['anchor_unit'] for n in N if not n['anchor_heading']}
ord_of={u['unit_id']:int(u['ord']) for u in U}
ps=list(re.finditer(r'<p class="doc-body"(?: style="[^"]*")?>',s))
assert len(ps)==1106
edits=[]
for uid in need:
    m=ps[ord_of[uid]-1]
    uid_attr=f' id="u-{uid.replace(":","-")}"'
    if uid_attr in s: continue
    edits.append((m.start(),m.end(),m.group(0)[:-1]+uid_attr+'>'))
for a,b,rep in sorted(edits,reverse=True): s=s[:a]+rep+s[b:]
def href(n):
    return '#'+n['anchor_heading'] if n['anchor_heading'] else '#u-'+n['anchor_unit'].replace(':','-')
# --- 1b. ids on the appendix h3s (synthetic pappendix-xN, in document order)
ap=s.find('<!-- APPENDIX')
k=0
def _addid(m):
    global k; k+=1; return f'<h3 id="pappendix-x{k}" class="doc-h3">'
if 'id="pappendix-x1"' not in s:
    s=s[:ap]+re.sub(r'<h3 class="doc-h3">',_addid,s[ap:])+''
# --- 2. build the list
kids={}
for n in N: kids.setdefault(n['parent_id'],[]).append(n)
Hs=sorted(H,key=lambda h:(pn(h['page']),int(h['ordinal'])))
def headings_in(p0,p1,exclude_ids):
    return [h for h in Hs if p0<=pn(h['page'])<=p1 and h['heading_id'] not in exclude_ids]
def li(cls,hrf,text,page,extra=''):
    return f'<li class="{cls}"><a href="{hrf}" class="toc-link" data-page="{page}"><span class="toc-text">{html.escape(text)}</span><span class="toc-page">{page}</span></a>{extra}</li>\n'
out=[]
used=set()
def render_headings(hs,base):
    st=[h for h in hs if h['toc_role']=='structural']; ap=[h for h in hs if h['toc_role']!='structural']
    o=''
    for h in st:
        lvl=min(int(h['level']),3)  # h1..h3 -> depth offsets
        o+=li(f'toc-l{min(base+lvl-1,4)} toc-h',f"#{h['heading_id']}",h['text'],h['page'] if h['page']!='appendix' else 'A')
    if ap:
        inner=''.join(li('toc-l4 toc-app',f"#{h['heading_id']}",h['text'],h['page']) for h in ap)
        o+=f'<li class="toc-app-group"><details><summary>working apparatus ({len(ap)})</summary><ul>{inner}</ul></details></li>\n'
    return o
for P in kids['']:
    p0,p1=int(P['page_start']),int(P['page_end'])
    out.append(f'<li class="toc-part"><a href="{href(P)}" class="toc-link" data-page="{P["page_start"]}"><span class="toc-text">{html.escape(P["title"])}</span><span class="toc-page">{P["page_start"]}</span></a></li>\n')
    chs=kids.get(P['node_id'],[])
    if not chs:
        out.append(render_headings(headings_in(p0,p1,set()),2)); continue
    for i,C in enumerate(chs):
        c0,c1=int(C['page_start']),int(C['page_end'])
        # chapter's own page range but exclude pages claimed by the NEXT chapter's start (overlap on p3)
        out.append(li('toc-l1',href(C),C['title'],C['page_start']))
        if C['anchor_heading']: used.add(C['anchor_heading'])
        secs=kids.get(C['node_id'],[])
        if not secs:
            hs=headings_in(c0,c1,{C['anchor_heading']} if C['anchor_heading'] else set())
            hs=[h for h in hs if h['heading_id'] not in used]; used.update(h['heading_id'] for h in hs)
            out.append(render_headings(hs,2))
        else:
            for S in secs:
                s0,s1=int(S['page_start']),int(S['page_end'])
                out.append(li('toc-l2',href(S),S['title'],S['page_start']))
                if S['anchor_heading']: used.add(S['anchor_heading'])
                hs=headings_in(s0,s1,{S['anchor_heading']} if S['anchor_heading'] else set())
                hs=[h for h in hs if h['heading_id'] not in used]; used.update(h['heading_id'] for h in hs)
                out.append(render_headings(hs,3))
            # headings in chapter range not covered by any section (gaps between sections)
            hs=[h for h in headings_in(c0,c1,set()) if h['heading_id'] not in used and h['heading_id']!=C['anchor_heading']]
            used.update(h['heading_id'] for h in hs); out.append(render_headings(hs,2))
ul='<ul class="toc-root">\n'+''.join(out)+'</ul>'
a=s.find('<ul class="toc-root">'); b=s.find('</ul>',a)
# the old list may contain nested? it is flat: verify no inner <ul>
assert '<ul' not in s[a+5:b]
s=s[:a]+ul+s[b+5:]
# --- 3. CSS
css='''
.toc-part>a{padding:8px 10px 4px;font-weight:800;font-size:11px;text-transform:uppercase;letter-spacing:.08em;color:var(--accent2);border-left:3px solid var(--accent2);margin-top:6px}
.toc-l4>a{padding:2px 10px 2px 38px;font-size:11px;color:var(--muted);border-left:3px solid transparent}
.toc-app-group{padding-left:28px}
.toc-app-group details summary{cursor:pointer;font-size:10.5px;color:#999;font-family:system-ui,sans-serif;padding:2px 10px;list-style:none}
.toc-app-group details summary::before{content:"\\25B8 ";font-size:9px}
.toc-app-group details[open] summary::before{content:"\\25BE "}
.toc-app-group ul{list-style:none;padding-left:0}
.toc-app>a{padding-left:16px!important;font-style:italic;color:#aaa}
.toc-app-group.toc-hidden{display:none}
'''
if '.toc-part>a' not in s:
    s=s.replace('.toc-hidden{display:none}','.toc-hidden{display:none}'+css,1)
open(HTML,'w',encoding='utf-8').write(s)
print('ids added',len(edits),'headings placed',len(used),'of',len(H),'toc-links',s.count('class="toc-link"'))
