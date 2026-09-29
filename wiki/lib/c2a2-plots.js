(function(){
  // Installed by the explorer shell as soon as the Sociogram loads (hidden, and
  // without Plotly, which loads on first show): the shell's facet cuts
  // (thinker:, between A and B, kind:, strength:, month:) are answered HERE, by
  // the same attribution rule the charts draw with, so a row of the heatmap
  // and a cut on the graph are one set, never two approximations of it.
  if (window.C2A2Plot && window.C2A2Plot.panel) { return; }
  // THE SOURCE (step 5, 2026-09-29): everything below reads the graph through
  // this one object, never through a page's globals. The Sociogram's globals
  // are one source; any tab can offer another as window.c2a2PlotSource():
  //   { nodes: [{id, group, date}], links: [{source, target (node objects),
  //     type, layer?, strength?, sig_date?, home?}],
  //     active?() -> {nodes, links} (the view; absent = the view IS the corpus),
  //     passes?(e), searchCut?() -> {ids, query}, since?() -> 'YYYY-MM-DD',
  //     stamp?() -> anything that changes when the view does,
  //     cuts?: false (the tab cannot be cut from the chart -- clicks say so) }
  // Attribution to thinkers is by slug in the node id (traditions/<slug>/...)
  // or group 'traditions/<slug>' -- one rule for every source.
  function sociogramSource(){ return { kind:'sociogram', nodes:NODES, links:LINKS,
    active:function(){ return {nodes:activeNodes, links:activeLinks}; },
    passes:function(e){ return edgePassesCuts(e); },
    searchCut:function(){ return (typeof SEARCH_CUT!=='undefined'&&SEARCH_CUT&&SEARCH_CUT.ids)?{ids:SEARCH_CUT.ids,query:SEARCH_CUT.query}:null; },
    since:function(){ return (typeof dateThreshold!=='undefined'&&dateThreshold)||''; },
    hiddenThinkers:function(){ return (typeof groupVisibility==='undefined')?[]:O.filter(function(t){ return groupVisibility['traditions/'+t]===false; }); },
    stamp:function(){ return typeof _lastEdgePass!=='undefined'?_lastEdgePass:''; } }; }
  var SRC = (typeof LINKS !== 'undefined' && typeof edgePassesCuts === 'function') ? sociogramSource()
          : (typeof window.c2a2PlotSource === 'function' ? window.c2a2PlotSource() : null);
  if (!SRC || !Array.isArray(SRC.nodes) || !Array.isArray(SRC.links)) return;
  var SN = SRC.nodes, SL = SRC.links;
  function act(){ return SRC.active ? SRC.active() : null; }
  function sinceOf(){ return SRC.since ? (SRC.since() || '') : ''; }
  var O=["levin","friston","hoffman","kastrup","mcgilchrist","hawkins","wolfram","carroll","arkanihamed","fredrickson","stump","rohr","wright","loughran","macintyre"];
  var TN=["Levin","Friston","Hoffman","Kastrup","McGilchrist","Hawkins","Wolfram","Carroll","Arkani-Hamed","Fredrickson","Stump","Rohr","Wright","Loughran","MacIntyre"];
  var P=O.map(function(t){return new RegExp('(?<![a-z])('+(t==='arkanihamed'?'arkanihamed|arkani-hamed|arkani_hamed':t)+')(?![a-z])');});
  function thOf(str){ var k=[]; str=(str||'').toLowerCase(); P.forEach(function(p,i){ if(p.test(str)) k.push(i); }); return k; }
  function thN(n){ if(n._th) return n._th; var k=thOf(n.id); var g=n.group||''; O.forEach(function(t,i){ if(g==='traditions/'+t && k.indexOf(i)<0) k.push(i); }); n._th=k; return k; }
  function ekind(e){ return e.layer ? ('layer:'+e.layer) : (e.type||'reference'); }
  var GROUPS=Object.keys(SN.reduce(function(a,n){ a[n.group||'-']=1; return a; },{})).sort();
  var KINDS=Object.keys(SL.reduce(function(a,e){ a[ekind(e)]=1; return a; },{})).sort();
  var STRS=['Strong','High','Moderate','Speculative','Unlabeled'];
  var MONTHS=Object.keys(SN.reduce(function(a,n){ if(n.date) a[n.date.slice(0,7)]=1; return a; },{})).sort();

  // THE SPEC: everything the panel shows is a function of this object. set() is the hook voice/CCL will use.
  var spec={plot:'lego', axis:'thinker', scope:'page', cut:'touching',
    kinds:KINDS.slice(), groups:GROUPS.slice(), strengths:STRS.slice(), from:'', to:''};

  function edate(e){ var s=e.source,t=e.target; return (e.sig_date||'').slice(0,7) || [(s&&s.date)||'',(t&&t.date)||''].sort()[1].slice(0,7); }
  function timeOk(e){ if(!spec.from&&!spec.to) return true; var m=edate(e); if(!m) return false; return (!spec.from||m>=spec.from)&&(!spec.to||m<=spec.to); }
  function nodeOk(n){ return spec.groups.indexOf(n.group||'-')>=0; }
  function edgeOk(e){
    var k=ekind(e); if(spec.kinds.indexOf(k)<0) return false;
    if(k==='signal' && spec.strengths.indexOf(e.strength||'Unlabeled')<0) return false;
    return true;
  }
  // WHICH CUT: in the explorer the shell's cut is the single truth (a compound
  // or facet cut clears the tab's own SEARCH_CUT and is enforced shell-side),
  // so once the shell has spoken (setCut) its word is final, null included.
  // Standalone, the tab's own SEARCH_CUT is all there is.
  var shellCut=null, shellSpoke=false;
  function curCut(){ if(shellSpoke) return shellCut; return SRC.searchCut ? SRC.searchCut() : null; }
  // A tradition ticked OFF in the left panel hides only that tradition's own files, but a thinker is
  // attributed by NAME wherever it appears (agents, flags, synthesis...). Without this, unticking Levin
  // left ~166 Levin-named files and the Levin towers barely moved. Ticked-off = out of the thinker axis.
  var HID={};
  function hiddenNames(){ return (spec.scope==='page'&&SRC.hiddenThinkers)?SRC.hiddenThinkers():[]; }
  function edges(){
    HID={}; hiddenNames().forEach(function(t){ HID[O.indexOf(t)]=1; });
    var cc=curCut(), out=[], cutIds=(spec.scope==='page'&&cc)?new Set(cc.ids):null;
    var src, live=null;
    var A=spec.scope==='page'?act():null;
    if(A){ src=A.links; live=new Set(A.nodes.map(function(n){return n.id;})); } else src=SL;
    for(var q=0;q<src.length;q++){ var e=src[q], s=e.source, t=e.target;
      if(typeof s!=='object') s=SN[s]; if(typeof t!=='object') t=SN[t]; if(!s||!t) continue; if(e.source!==s||e.target!==t) e={__proto__:e,source:s,target:t};
      if(live){ if((SRC.passes&&!SRC.passes(e))||!live.has(s.id)||!live.has(t.id)) continue; }
      if(!nodeOk(s)||!nodeOk(t)||!edgeOk(e)||!timeOk(e)) continue;
      if(cutIds){ var hs=cutIds.has(s.id),ht=cutIds.has(t.id); if(spec.cut==='inside'?!(hs&&ht):!(hs||ht)) continue; }
      out.push(e); }
    return out;
  }
  function keysOf(n,e,side){
    if(spec.axis==='group') return [GROUPS.indexOf(n.group||'-')];
    var k=thN(n).slice(); if(e && e.type==='signal' && side==='s' && e.home){ thOf(String(e.home)).forEach(function(i){ if(k.indexOf(i)<0) k.push(i); }); }
    return k.filter(function(i){ return !HID[i]; });
  }
  function labels(){ return spec.axis==='group' ? GROUPS : TN; }
  // ONE EDGE, ONE COUNT PER CELL. An edge whose two ends are each attributed to
  // both Levin and Friston used to add 2 to the Levin-Friston cell (once as
  // L->F, once as F->L). Each edge now counts once per unordered pair, so a cell
  // equals the number of edges a `between a and b` cut selects (2026-09-29).
  function matrix(E){ var L=labels().length, M=[], n=0; for(var i=0;i<L;i++){ M.push(new Array(L).fill(0)); }
    E.forEach(function(e){ var a=keysOf(e.source,e,'s'), b=keysOf(e.target,e,'t'); if(a.length&&b.length) n++;
      var seen={}; a.forEach(function(i){ b.forEach(function(j){ var lo=Math.min(i,j), hi=Math.max(i,j), k=lo+','+hi; if(seen[k]) return; seen[k]=1;
        M[lo][hi]++; if(lo!==hi) M[hi][lo]++; }); }); });
    return {M:M,n:n}; }

  var SUN=[[0,'#3b0f70'],[0.25,'#8c2981'],[0.5,'#de4968'],[0.75,'#fe9f6d'],[1,'#fcfdbf']];
  var FONT={size:9,color:'#ccc'};
  function base(){ return {paper_bgcolor:'#11131a',plot_bgcolor:'#11131a',font:FONT,margin:{l:90,r:10,t:10,b:90}}; }
  var PLOTS={
    lego:function(E){ var r=matrix(E), L=labels(), x=[],y=[],z=[],I=[],J=[],K=[],c=[],mx=1,w=0.42,v=0,cells=[];
      var F=[[0,1,2],[0,2,3],[4,5,6],[4,6,7],[0,1,5],[0,5,4],[1,2,6],[1,6,5],[2,3,7],[2,7,6],[3,0,4],[3,4,7]];
      r.M.forEach(function(row){ row.forEach(function(h){ if(h>mx) mx=h; }); });
      for(var i=0;i<L.length;i++) for(var j=0;j<L.length;j++){ var h=r.M[i][j]; if(!h) continue;
        [[i-w,j-w,0],[i+w,j-w,0],[i+w,j+w,0],[i-w,j+w,0],[i-w,j-w,h],[i+w,j-w,h],[i+w,j+w,h],[i-w,j+w,h]].forEach(function(p){ x.push(p[0]);y.push(p[1]);z.push(p[2]);c.push(h); });
        F.forEach(function(f){ I.push(v+f[0]);J.push(v+f[1]);K.push(v+f[2]); }); v+=8; cells.push([i,j]); }
      legoCells=cells;
      var tk={tickvals:L.map(function(_,k){return k;}),ticktext:L,title:'',tickfont:FONT,gridcolor:'#333'};
      var lay=base(); lay.margin={l:0,r:0,t:0,b:0}; lay.scene={xaxis:tk,yaxis:tk,zaxis:{title:'edges',tickfont:FONT,gridcolor:'#333'},aspectratio:{x:1,y:1,z:0.55},camera:{eye:{x:1.5,y:-1.25,z:1.05}}};
      return {n:r.n, data:[{type:'mesh3d',x:x,y:y,z:z,i:I,j:J,k:K,intensity:c,colorscale:SUN,cmin:0,cmax:mx,flatshading:true,showscale:false,lighting:{ambient:0.6,diffuse:0.6},hovertemplate:'%{intensity} edges<extra></extra>'}], layout:lay}; },
    heatmap:function(E){ var r=matrix(E), L=labels();
      return {n:r.n, data:[{type:'heatmap',z:r.M,x:L,y:L,colorscale:SUN,hovertemplate:'%{y} - %{x}: %{z}<extra></extra>'}], layout:Object.assign(base(),{yaxis:{autorange:'reversed'}})}; },
    totals:function(E){ var r=matrix(E), L=labels(), tot=r.M.map(function(row,i){ return row.reduce(function(a,b){return a+b;},0); });
      var idx=L.map(function(_,i){return i;}).sort(function(a,b){return tot[b]-tot[a];});
      return {n:r.n, data:[{type:'bar',x:idx.map(function(i){return L[i];}),y:idx.map(function(i){return tot[i];}),marker:{color:'#de4968'},hovertemplate:'%{x}: %{y}<extra></extra>'}], layout:base()}; },
    timeline:function(E){ var L=labels(), by={}, months={};
      E.forEach(function(e){ var m=edate(e); if(!m) return; months[m]=1; var ks=keysOf(e.source,e,'s').concat(keysOf(e.target,e,'t')).filter(function(v,i,a){return a.indexOf(v)===i;});
        ks.forEach(function(k){ by[k]=by[k]||{}; by[k][m]=(by[k][m]||0)+1; }); });
      var ms=Object.keys(months).sort();
      var data=Object.keys(by).map(function(k){ return {type:'scatter',mode:'lines',stackgroup:'one',name:L[k],x:ms,y:ms.map(function(m){return by[k][m]||0;})}; });
      var lay=base(); lay.showlegend=true; lay.legend={font:FONT}; lay.margin={l:50,r:10,t:10,b:40};
      var since=(spec.scope==='page'&&sinceOf())?sinceOf().slice(0,7):'';
      if(since&&ms.length) lay.shapes=[{type:'rect',xref:'x',yref:'paper',x0:ms[0],x1:since,y0:0,y1:1,fillcolor:'rgba(0,0,0,0.45)',line:{width:0}}];
      return {n:E.length, data:data, layout:lay}; },
    strength:function(E){ var L=labels(), S={}; STRS.forEach(function(s){ S[s]=new Array(L.length).fill(0); }); var n=0;
      E.forEach(function(e){ if(e.type!=='signal') return; n++; var s=e.strength||'Unlabeled';
        keysOf(e.source,e,'s').concat(keysOf(e.target,e,'t')).filter(function(v,i,a){return a.indexOf(v)===i;}).forEach(function(k){ S[s][k]++; }); });
      var col={Strong:'#fcfdbf',High:'#fe9f6d',Moderate:'#de4968',Speculative:'#8c2981',Unlabeled:'#555'};
      var lay=base(); lay.barmode='stack'; lay.showlegend=true; lay.legend={font:FONT};
      return {n:n, data:STRS.map(function(s){ return {type:'bar',name:s,x:L,y:S[s],marker:{color:col[s]}}; }), layout:lay}; },
    sankey:function(E){ var r=matrix(E), L=labels(), s=[],t=[],v=[];
      for(var i=0;i<L.length;i++) for(var j=0;j<L.length;j++){ if(i!==j && r.M[i][j] && i<j){ s.push(i); t.push(j+L.length); v.push(r.M[i][j]); } }
      return {n:r.n, data:[{type:'sankey',node:{label:L.concat(L),pad:6,thickness:10,color:'#8c2981'},link:{source:s,target:t,value:v,color:'rgba(222,73,104,0.35)'}}], layout:Object.assign(base(),{margin:{l:10,r:10,t:10,b:10}})}; }
  };
  var PLOT_NAMES={lego:'Lego (3D)',heatmap:'Heatmap',totals:'Totals (bars)',timeline:'Timeline (monthly)',strength:'Signal strength mix',sankey:'Flows (Sankey)'};

  // ---- FACETS: the shell's cut terms answered from the graph model ----------
  // f = {facet:'thinker'|'group'|'kind'|'strength'|'month'|'since'|'until'|'pair', value | a,b}
  // (parsed by CommandLine.parseFacet in the shell). Returns {ids, edges?, label}
  // or {error}. Node facets select nodes; edge facets (kind, strength, pair)
  // select the ENDPOINTS of the matching edges and say how many edges that was.
  function nodeOf(x){ return (typeof x==='object')?x:SN[x]; }
  function resolveThinker(v){ v=String(v||'').toLowerCase().replace(/[^a-z]/g,''); var i=O.indexOf(v); if(i<0) i=TN.map(function(t){return t.toLowerCase().replace(/[^a-z]/g,'');}).indexOf(v); return i; }
  function resolveGroup(v){ v=String(v||'').toLowerCase(); var g=GROUPS.filter(function(x){ var l=x.toLowerCase(); return l===v||l.split('/').pop()===v; }); return g.length?g:null; }
  function resolveKind(v){ v=String(v||'').toLowerCase().replace(/s$/,''); var k=KINDS.filter(function(x){ var l=x.toLowerCase(), b=l.replace(/^layer:/,''); return l===v||b===v; }); return k.length?k:null; }
  function resolveStr(v){ v=String(v||'').toLowerCase(); var k=STRS.filter(function(x){ return x.toLowerCase()===v; }); return k.length?k[0]:null; }
  function sideKeys(v){ // a side of a pair: a thinker first, else a group
    var ti=resolveThinker(v.replace(/^thinker:/,'')); if(!/^group:/.test(v) && ti>=0) return {axis:'thinker',i:ti,label:TN[ti]};
    var g=resolveGroup(v.replace(/^group:/,'')); if(g) return {axis:'group',i:GROUPS.indexOf(g[0]),label:g[0]};
    return null; }
  function sideHas(n,e,side,k){ if(k.axis==='group') return (n.group||'-')===GROUPS[k.i];
    var ks=thN(n).slice(); if(e && e.type==='signal' && side==='s' && e.home){ thOf(String(e.home)).forEach(function(i){ if(ks.indexOf(i)<0) ks.push(i); }); } return ks.indexOf(k.i)>=0; }
  function facetOne(f){
    var ids=[], seen={}, ne=0; function add(n){ if(n&&n.id&&!seen[n.id]){ seen[n.id]=1; ids.push(n.id); } }
    if(f.facet==='thinker'){ var ti=resolveThinker(f.value); if(ti<0) return {error:'no thinker called "'+f.value+'" (thinkers: '+O.join(', ')+')'};
      SN.forEach(function(n){ if(thN(n).indexOf(ti)>=0) add(n); }); return {ids:ids,label:TN[ti]}; }
    if(f.facet==='group'){ var g=resolveGroup(f.value); if(!g) return {error:'no node group called "'+f.value+'"'};
      SN.forEach(function(n){ if(g.indexOf(n.group||'-')>=0) add(n); }); return {ids:ids,label:g.join(', ')}; }
    if(f.facet==='month'||f.facet==='since'||f.facet==='until'){ var m=String(f.value||'');
      if(!/^\d{4}-\d{2}$/.test(m)) return {error:f.facet+':'+m+' needs a month like 2026-08'};
      SN.forEach(function(n){ var d=(n.date||'').slice(0,7); if(!d) return; if(f.facet==='month'?d===m:(f.facet==='since'?d>=m:d<=m)) add(n); });
      return {ids:ids,label:f.facet+' '+m}; }
    var test=null, label='';
    if(f.facet==='kind'){ var ks=resolveKind(f.value); if(!ks) return {error:'no edge kind called "'+f.value+'" (kinds: '+KINDS.join(', ')+')'};
      test=function(e){ return ks.indexOf(ekind(e))>=0; }; label=ks.join(', ')+' edges'; }
    else if(f.facet==='strength'){ var st=resolveStr(f.value); if(!st) return {error:'no signal strength called "'+f.value+'" (strengths: '+STRS.join(', ')+')'};
      test=function(e){ return e.type==='signal' && (e.strength||'Unlabeled')===st; }; label=st+' signals'; }
    else if(f.facet==='pair'){ var A=sideKeys(String(f.a||'').toLowerCase()), B=sideKeys(String(f.b||'').toLowerCase());
      if(!A||!B) return {error:'between needs two thinkers or node groups ("'+(A?f.b:f.a)+'" is neither)'};
      test=function(e,s,t){ return (sideHas(s,e,'s',A)&&sideHas(t,e,'t',B))||(sideHas(s,e,'s',B)&&sideHas(t,e,'t',A)); };
      label=(A.i===B.i&&A.axis===B.axis)?('within '+A.label):(A.label+'-'+B.label+' edges'); }
    else return {error:'unknown facet "'+f.facet+'"'};
    for(var q=0;q<SL.length;q++){ var e=SL[q], s=nodeOf(e.source), t=nodeOf(e.target); if(!s||!t) continue; if(test(e,s,t)){ ne++; add(s); add(t); } }
    return {ids:ids,edges:ne,label:label};
  }
  // NEIGHBOURS: nodes with an edge to any seed node (any edge kind, whole corpus,
  // one hop). A seed appears only when another seed links to it. Returns
  // {ids, edges} -- edges = how many edges touch a seed node.
  function neighborIds(seedIds){
    var seed={}, ids=[], seen={}, ne=0; [].concat(seedIds||[]).forEach(function(i){ seed[i]=1; });
    function add(n){ if(n&&n.id&&!seen[n.id]){ seen[n.id]=1; ids.push(n.id); } }
    for(var q=0;q<SL.length;q++){ var e=SL[q], s=nodeOf(e.source), t=nodeOf(e.target); if(!s||!t||s===t) continue;
      var hs=!!seed[s.id], ht=!!seed[t.id]; if(!hs&&!ht) continue; ne++; if(hs) add(t); if(ht) add(s); }
    return {ids:ids, edges:ne}; }
  // A '+' conjunction (thinker:levin+month:2026-08) is ONE term: the AND of its facets.
  function facetIds(fs){ fs=[].concat(fs); var acc=null, parts=[], edgesN=null;
    for(var i=0;i<fs.length;i++){ var r=facetOne(fs[i]); if(r.error) return r; parts.push(r.label); if(r.edges!=null) edgesN=r.edges;
      if(acc===null) acc=r.ids; else { var h={}; r.ids.forEach(function(x){ h[x]=1; }); acc=acc.filter(function(x){ return h[x]; }); } }
    return {ids:acc||[], edges:(fs.length===1?edgesN:null), label:parts.join(' & ')}; }

  // ---- CLICKS: the chart is a place to cut from, through the shell's one road --
  // plain click = find, shift = also (add), alt/option = except (remove),
  // ctrl/cmd = within (keep only the overlap). The command runs in the shell
  // (parent.CCLRun), so it is journaled, undoable, spoken, and the graph and
  // this chart both follow it. Standalone there is no shell: say so, do nothing.
  var pickHook=null, legoCells=[];
  function tokOf(label){ if(spec.axis==='group') return 'group:'+label; var i=TN.indexOf(label); return 'thinker:'+(i>=0?O[i]:String(label).toLowerCase()); }
  function sideOf(label){ if(spec.axis==='group') return 'group:'+label; var i=TN.indexOf(label); return i>=0?O[i]:String(label).toLowerCase(); }
  function pairTerm(a,b){ return a===b?tokOf(a):('between '+sideOf(a)+' and '+sideOf(b)); }
  function termFor(ev){ var pt=ev&&ev.points&&ev.points[0]; if(!pt) return null; var P=spec.plot;
    if(P==='heatmap') return pairTerm(pt.y,pt.x);
    if(P==='totals') return tokOf(pt.x);
    if(P==='strength') return tokOf(pt.x)+'+strength:'+String(pt.data&&pt.data.name||'').toLowerCase();
    if(P==='timeline') return tokOf(pt.data&&pt.data.name)+'+month:'+pt.x;
    if(P==='sankey'){ if(pt.source&&pt.target) return pairTerm(pt.source.label,pt.target.label); if(pt.label) return tokOf(pt.label); return null; }
    if(P==='lego'){ var c=legoCells[Math.floor((pt.pointNumber!=null?pt.pointNumber:(pt.i!=null?pt.i:-8))/8)]; if(!c) return null; var L=labels(); return pairTerm(L[c[0]],L[c[1]]); }
    return null; }
  function onClick(ev){ var term=termFor(ev); if(!term) return; var me=(ev&&ev.event)||{};
    var verb=me.shiftKey?'also':(me.altKey?'except':((me.ctrlKey||me.metaKey)?'within':'find'));
    var cmd=verb+' '+term;
    if(pickHook){ try{ pickHook(cmd); }catch(_){} return; }
    if(SRC.cuts===false){ $('cp-s').textContent='This view cannot be cut from the chart yet ('+cmd+' works on the Sociogram).'; return; }
    var sh=null; try{ if(window.parent!==window && typeof window.parent.CCLRun==='function') sh=window.parent.CCLRun; }catch(_){}
    if(!sh){ $('cp-s').textContent='(cutting from the chart needs the explorer: '+cmd+')'; return; }
    sh(cmd); }

  var panel=document.createElement('div');
  panel.style.cssText='position:fixed;right:12px;bottom:12px;width:min(640px, calc(100vw - 24px));height:min(560px, calc(100vh - 24px));z-index:2147483000;background:#11131a;border:1px solid #3a3f4b;border-radius:8px;box-shadow:0 8px 30px rgba(0,0,0,.6);font:12px system-ui,sans-serif;color:#ddd;display:none;flex-direction:column;overflow:visible';
  function sel(id,opts){ return '<select id="'+id+'" style="background:#1b1e27;color:#ddd;border:1px solid #3a3f4b;border-radius:4px">'+opts.map(function(o){return '<option value="'+o[0]+'">'+o[1]+'</option>';}).join('')+'</select>'; }
  function multi(id,title,vals){ return '<details style="position:relative"><summary style="cursor:pointer">'+title+' <span id="'+id+'-n"></span></summary><div id="'+id+'" style="position:absolute;z-index:3;background:#1b1e27;border:1px solid #3a3f4b;padding:6px;max-height:260px;overflow:auto;white-space:nowrap">'+
    '<a href="#" data-all="1" style="color:#fe9f6d">all</a> · <a href="#" data-none="1" style="color:#fe9f6d">none</a><br>'+vals.map(function(v){return '<label><input type="checkbox" value="'+v+'" checked> '+v+'</label><br>';}).join('')+'</div></details>'; }
  panel.innerHTML='<div id="cp-h" style="display:flex;gap:8px;align-items:center;padding:6px 10px;border-bottom:1px solid #2a2e38;cursor:move"><b style="flex:1">C2A2 plots (live)</b><button id="cp-x" style="background:none;border:0;color:#aaa;font-size:16px;cursor:pointer">x</button></div>'+
    '<div style="display:flex;flex-wrap:wrap;gap:8px;align-items:center;padding:6px 10px;border-bottom:1px solid #2a2e38">'+
    sel('cp-plot',Object.keys(PLOT_NAMES).map(function(k){return [k,PLOT_NAMES[k]];}))+
    sel('cp-axis',[['thinker','by thinker'],['group','by node group']])+
    sel('cp-scope',[['page','follow page view'],['corpus','whole corpus']])+
    sel('cp-cut',[['touching','cut: touching'],['inside','cut: inside']])+
    sel('cp-from',[['','from: start']].concat(MONTHS.map(function(m){return [m,'from '+m];})))+
    sel('cp-to',[['','to: now']].concat(MONTHS.map(function(m){return [m,'to '+m];})))+
    multi('cp-kinds','edges',KINDS)+multi('cp-groups','nodes',GROUPS)+multi('cp-str','signals',STRS)+'</div>'+
    '<div id="cp-s" style="padding:4px 10px;color:#9aa"></div><div id="cp-p" style="flex:1;min-height:0"></div>';
  document.body.appendChild(panel);
  function $(id){ return panel.querySelector('#'+id); }
  $('cp-x').onclick=function(){ var before=JSON.parse(JSON.stringify(spec)); panel.style.display='none'; subs.forEach(function(f){ try{ f(before,null); }catch(_){} }); };
  var MAP={'cp-kinds':'kinds','cp-groups':'groups','cp-str':'strengths'};
  function syncUI(){ $('cp-plot').value=spec.plot; $('cp-axis').value=spec.axis; $('cp-scope').value=spec.scope; $('cp-cut').value=spec.cut; $('cp-from').value=spec.from; $('cp-to').value=spec.to;
    Object.keys(MAP).forEach(function(id){ var arr=spec[MAP[id]], boxes=$(id).querySelectorAll('input'); boxes.forEach(function(b){ b.checked=arr.indexOf(b.value)>=0; }); $(id+'-n').textContent='('+arr.length+'/'+boxes.length+')'; }); }
  // A hand change on the panel is a change of state like any command: subscribers
  // (the shell) journal it, so `undo` and `what` see it. set() does NOT notify --
  // its caller journals, and notifying too would record the same change twice.
  var subs=[];
  function userChange(fn){ var before=JSON.parse(JSON.stringify(spec)); fn(); refresh(); var after=JSON.parse(JSON.stringify(spec));
    if(JSON.stringify(before)!==JSON.stringify(after)) subs.forEach(function(f){ try{ f(before,after); }catch(_){} }); }
  ['cp-plot','cp-axis','cp-scope','cp-cut','cp-from','cp-to'].forEach(function(id){ $(id).onchange=function(e){ userChange(function(){ spec[id.slice(3)]=e.target.value; }); }; });
  Object.keys(MAP).forEach(function(id){ var box=$(id);
    box.onchange=function(){ userChange(function(){ spec[MAP[id]]=[].slice.call(box.querySelectorAll('input:checked')).map(function(b){return b.value;}); }); };
    box.onclick=function(ev){ var a=ev.target; if(a.tagName!=='A') return; ev.preventDefault(); box.querySelectorAll('input').forEach(function(b){ b.checked=!!a.dataset.all; }); box.onchange(); }; });
  (function(){ var h=$('cp-h'),sx,sy,ox,oy; h.onmousedown=function(e){ if(e.target.tagName==='BUTTON') return; sx=e.clientX;sy=e.clientY; var r=panel.getBoundingClientRect(); ox=r.left;oy=r.top;
    document.onmousemove=function(ev){ panel.style.left=(ox+ev.clientX-sx)+'px'; panel.style.top=(oy+ev.clientY-sy)+'px'; panel.style.right='auto'; panel.style.bottom='auto'; };
    document.onmouseup=function(){ document.onmousemove=null; document.onmouseup=null; }; }; })();

  // A narrow window (a phone, the app's side pane) must still hold the whole panel.
  (function(){ var MINW=Math.min(460,window.innerWidth-24),MINH=Math.min(400,window.innerHeight-24),G=6,C=14;
    var H={n:'top:-3px;left:'+C+'px;right:'+C+'px;height:'+G+'px;cursor:ns-resize',s:'bottom:-3px;left:'+C+'px;right:'+C+'px;height:'+G+'px;cursor:ns-resize',
      e:'right:-3px;top:'+C+'px;bottom:'+C+'px;width:'+G+'px;cursor:ew-resize',w:'left:-3px;top:'+C+'px;bottom:'+C+'px;width:'+G+'px;cursor:ew-resize',
      ne:'top:-3px;right:-3px;width:'+C+'px;height:'+C+'px;cursor:nesw-resize',sw:'bottom:-3px;left:-3px;width:'+C+'px;height:'+C+'px;cursor:nesw-resize',
      nw:'top:-3px;left:-3px;width:'+C+'px;height:'+C+'px;cursor:nwse-resize',se:'bottom:-3px;right:-3px;width:'+C+'px;height:'+C+'px;cursor:nwse-resize'};
    Object.keys(H).forEach(function(d){ var g=document.createElement('div'); g.className='cp-grip'; g.dataset.dir=d;
      g.style.cssText='position:absolute;z-index:5;touch-action:none;'+H[d]+(d==='se'?';background:linear-gradient(135deg,transparent 55%,#6b7080 55%,#6b7080 65%,transparent 65%,transparent 75%,#6b7080 75%,#6b7080 85%,transparent 85%)':'');
      g.onpointerdown=function(e){ e.preventDefault(); e.stopPropagation();
        try{ g.setPointerCapture(e.pointerId); }catch(_){}
        var r=panel.getBoundingClientRect(), sx=e.clientX, sy=e.clientY, vw=window.innerWidth, vh=window.innerHeight;
        panel.style.left=r.left+'px'; panel.style.top=r.top+'px'; panel.style.right='auto'; panel.style.bottom='auto';
        function move(ev){ if(ev.buttons===0){ end(); return; } var dx=ev.clientX-sx, dy=ev.clientY-sy, L=r.left, T=r.top, W=r.width, Hh=r.height;
          if(d.indexOf('e')>=0) W=Math.min(Math.max(MINW,r.width+dx),vw-r.left);
          if(d.indexOf('s')>=0) Hh=Math.min(Math.max(MINH,r.height+dy),vh-r.top);
          if(d.indexOf('w')>=0){ W=Math.min(Math.max(MINW,r.width-dx),r.right); L=r.right-W; }
          if(d.indexOf('n')>=0){ Hh=Math.min(Math.max(MINH,r.height-dy),r.bottom); T=r.bottom-Hh; }
          panel.style.left=L+'px'; panel.style.top=T+'px'; panel.style.width=W+'px'; panel.style.height=Hh+'px'; ev.preventDefault(); }
        function end(){ document.removeEventListener('pointermove',move,true); document.removeEventListener('pointerup',end,true);
          document.removeEventListener('pointercancel',end,true); g.removeEventListener('lostpointercapture',end); window.removeEventListener('blur',end); }
        document.addEventListener('pointermove',move,true); document.addEventListener('pointerup',end,true);
        document.addEventListener('pointercancel',end,true); g.addEventListener('lostpointercapture',end); window.addEventListener('blur',end); };
      panel.appendChild(g); });
    var pend=0; if(window.ResizeObserver) new ResizeObserver(function(){ if(pend) return; pend=requestAnimationFrame(function(){ pend=0; var el=$('cp-p'); if(window.Plotly&&el&&el.data) Plotly.Plots.resize(el); }); }).observe($('cp-p'));
  })();

  var last='';
  function refresh(){ last=''; tick(); }
  document.addEventListener('change',function(ev){ var t=ev&&ev.target; if(t&&t.type==='checkbox'&&!panel.contains(t)){ setTimeout(tick,300); setTimeout(tick,1500); } },true);
  function draw(){ syncUI(); var E=edges(), out=PLOTS[spec.plot](E);
    Plotly.react($('cp-p'),out.data,out.layout,{displaylogo:false,responsive:true});
    var el=$('cp-p'); if(!el._c2a2Click && el.on){ el.on('plotly_click',onClick); el._c2a2Click=true; }
    var cc=curCut(), cut=(spec.scope==='page'&&cc)?('cut "'+cc.query+'" ('+spec.cut+') · '):'';
    var tw=[]; if(spec.scope==='page'&&sinceOf()) tw.push('page since '+sinceOf()); if(spec.from||spec.to) tw.push('edges '+(spec.from||'start')+' to '+(spec.to||'now')); var hn=hiddenNames(); if(hn.length) tw.push('unticked: '+hn.join(', ')); var tws=tw.length?tw.join(', ')+' · ':'';
    $('cp-s').textContent=cut+tws+((spec.scope==='page'&&act())?act().nodes.length+' nodes in view · ':'whole corpus · ')+out.n.toLocaleString()+(spec.plot==='strength'?' signals':spec.plot==='timeline'?' edges':' edges between '+(spec.axis==='group'?'groups':'thinkers'))+' · click to cut the graph (shift add, alt remove, ctrl overlap) · '+new Date().toLocaleTimeString(); }
  function sig(){ return JSON.stringify(spec)+'|'+(spec.scope==='page'?[(act()?act().nodes.length:SN.length),(SRC.stamp?SRC.stamp():''),(function(){ var cc=curCut(); return cc?cc.query+':'+cc.ids.length:''; })(),sinceOf(),hiddenNames().join('+')].join('|'):''); }
  function tick(){ if(panel.style.display==='none'||!window.Plotly) return; var s=sig(); if(s===last) return; last=s; try{ draw(); }catch(err){ $('cp-s').textContent='plot error: '+err.message; } }

  window.C2A2Plot={ panel:panel, refresh:refresh, plots:Object.keys(PLOTS), kinds:KINDS, groups:GROUPS, strengths:STRS, months:MONTHS,
    get:function(){ return JSON.parse(JSON.stringify(spec)); },
    visible:function(){ return panel.style.display!=='none'; },
    hide:function(){ panel.style.display='none'; },
    subscribe:function(f){ if(typeof f==='function' && subs.indexOf(f)<0) subs.push(f); },
    // THE NUMBERS BEHIND THE PICTURE, computed from the same edges() the chart
    // draws, so a spoken answer quotes what is on screen rather than a guess.
    summary:function(k){ k=k||5; var E=edges(), r=matrix(E), L=labels(), cells=[];
      for(var i=0;i<L.length;i++) for(var j=i;j<L.length;j++){ if(r.M[i][j]) cells.push({a:L[i],b:L[j],n:r.M[i][j]}); }
      cells.sort(function(x,y){ return y.n-x.n; });
      return {edges:E.length, attributed:r.n, axis:spec.axis, top:cells.slice(0,k)}; },
    set:function(p){ Object.keys(p||{}).forEach(function(k){ if(k in spec) spec[k]=p[k]; }); show(); return this.get(); },
    show:show, chartState:function(){ return plotlyState; }, source:SRC.kind||'tab',
    setCut:function(c){ shellSpoke=true; var nc=(c&&c.ids&&c.ids.length)?{ids:c.ids.slice(),query:c.query||''}:null;
      if(JSON.stringify(nc&&[nc.query,nc.ids.length])!==JSON.stringify(shellCut&&[shellCut.query,shellCut.ids.length])){ shellCut=nc; } },
    thinkers:O.slice(), thinkerNames:TN.slice(),
    facetIds:facetIds, neighborIds:neighborIds, onPick:function(f){ pickHook=f; },
    // One cell of the current chart's matrix, by axis label (tests and answers).
    count:function(a,b){ var L=labels(), i=L.indexOf(a), j=L.indexOf(b); if(i<0||j<0) return null; return matrix(edges()).M[i][j]; } };
  var plotlyState=window.Plotly?'ready':'none';
  function ensurePlotly(){
    if(plotlyState==='ready'){ return; }
    if(window.Plotly){ plotlyState='ready'; tick(); setInterval(tick,1000); return; }
    if(plotlyState==='loading'||plotlyState==='failed') return;
    plotlyState='loading'; $('cp-s').textContent='loading the chart library...';
    var sc=document.createElement('script'); sc.src='https://cdnjs.cloudflare.com/ajax/libs/plotly.js/2.34.0/plotly.min.js';
    sc.onload=function(){ plotlyState='ready'; tick(); setInterval(tick,1000); };
    sc.onerror=function(){ plotlyState='failed'; $('cp-s').textContent='Could not load Plotly from cdnjs.'; };
    document.head.appendChild(sc); }
  function show(){ panel.style.display='flex'; ensurePlotly(); refresh(); }
  if (window.Plotly) { plotlyState='ready'; setInterval(tick,1000); }
})();
