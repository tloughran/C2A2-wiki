(function(){
  if (window.C2A2Plot && window.C2A2Plot.panel) { window.C2A2Plot.panel.style.display='flex'; window.C2A2Plot.refresh(); return; }
  if (typeof LINKS === 'undefined' || typeof edgePassesCuts !== 'function') return;
  var O=["levin","friston","hoffman","kastrup","mcgilchrist","hawkins","wolfram","carroll","arkanihamed","fredrickson","stump","rohr","wright","loughran","macintyre"];
  var TN=["Levin","Friston","Hoffman","Kastrup","McGilchrist","Hawkins","Wolfram","Carroll","Arkani-Hamed","Fredrickson","Stump","Rohr","Wright","Loughran","MacIntyre"];
  var P=O.map(function(t){return new RegExp('(?<![a-z])('+(t==='arkanihamed'?'arkanihamed|arkani-hamed|arkani_hamed':t)+')(?![a-z])');});
  function thOf(str){ var k=[]; str=(str||'').toLowerCase(); P.forEach(function(p,i){ if(p.test(str)) k.push(i); }); return k; }
  function thN(n){ if(n._th) return n._th; var k=thOf(n.id); var g=n.group||''; O.forEach(function(t,i){ if(g==='traditions/'+t && k.indexOf(i)<0) k.push(i); }); n._th=k; return k; }
  function ekind(e){ return e.layer ? ('layer:'+e.layer) : (e.type||'reference'); }
  var GROUPS=Object.keys(NODES.reduce(function(a,n){ a[n.group||'-']=1; return a; },{})).sort();
  var KINDS=Object.keys(LINKS.reduce(function(a,e){ a[ekind(e)]=1; return a; },{})).sort();
  var STRS=['Strong','High','Moderate','Speculative','Unlabeled'];
  var MONTHS=Object.keys(NODES.reduce(function(a,n){ if(n.date) a[n.date.slice(0,7)]=1; return a; },{})).sort();

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
  function edges(){
    var out=[], cutIds=(spec.scope==='page'&&typeof SEARCH_CUT!=='undefined'&&SEARCH_CUT&&SEARCH_CUT.ids)?new Set(SEARCH_CUT.ids):null;
    var src, live=null;
    if(spec.scope==='page'){ src=activeLinks; live=new Set(activeNodes.map(function(n){return n.id;})); } else src=LINKS;
    for(var q=0;q<src.length;q++){ var e=src[q], s=e.source, t=e.target;
      if(typeof s!=='object') s=NODES[s]; if(typeof t!=='object') t=NODES[t]; if(!s||!t) continue; if(e.source!==s||e.target!==t) e={__proto__:e,source:s,target:t};
      if(live){ if(!edgePassesCuts(e)||!live.has(s.id)||!live.has(t.id)) continue; }
      if(!nodeOk(s)||!nodeOk(t)||!edgeOk(e)||!timeOk(e)) continue;
      if(cutIds){ var hs=cutIds.has(s.id),ht=cutIds.has(t.id); if(spec.cut==='inside'?!(hs&&ht):!(hs||ht)) continue; }
      out.push(e); }
    return out;
  }
  function keysOf(n,e,side){
    if(spec.axis==='group') return [GROUPS.indexOf(n.group||'-')];
    var k=thN(n).slice(); if(e && e.type==='signal' && side==='s' && e.home){ thOf(String(e.home)).forEach(function(i){ if(k.indexOf(i)<0) k.push(i); }); }
    return k;
  }
  function labels(){ return spec.axis==='group' ? GROUPS : TN; }
  function matrix(E){ var L=labels().length, M=[], n=0; for(var i=0;i<L;i++){ M.push(new Array(L).fill(0)); }
    E.forEach(function(e){ var a=keysOf(e.source,e,'s'), b=keysOf(e.target,e,'t'); if(a.length&&b.length) n++;
      a.forEach(function(i){ b.forEach(function(j){ M[i][j]++; if(i!==j) M[j][i]++; }); }); });
    return {M:M,n:n}; }

  var SUN=[[0,'#3b0f70'],[0.25,'#8c2981'],[0.5,'#de4968'],[0.75,'#fe9f6d'],[1,'#fcfdbf']];
  var FONT={size:9,color:'#ccc'};
  function base(){ return {paper_bgcolor:'#11131a',plot_bgcolor:'#11131a',font:FONT,margin:{l:90,r:10,t:10,b:90}}; }
  var PLOTS={
    lego:function(E){ var r=matrix(E), L=labels(), x=[],y=[],z=[],I=[],J=[],K=[],c=[],mx=1,w=0.42,v=0;
      var F=[[0,1,2],[0,2,3],[4,5,6],[4,6,7],[0,1,5],[0,5,4],[1,2,6],[1,6,5],[2,3,7],[2,7,6],[3,0,4],[3,4,7]];
      r.M.forEach(function(row){ row.forEach(function(h){ if(h>mx) mx=h; }); });
      for(var i=0;i<L.length;i++) for(var j=0;j<L.length;j++){ var h=r.M[i][j]; if(!h) continue;
        [[i-w,j-w,0],[i+w,j-w,0],[i+w,j+w,0],[i-w,j+w,0],[i-w,j-w,h],[i+w,j-w,h],[i+w,j+w,h],[i-w,j+w,h]].forEach(function(p){ x.push(p[0]);y.push(p[1]);z.push(p[2]);c.push(h); });
        F.forEach(function(f){ I.push(v+f[0]);J.push(v+f[1]);K.push(v+f[2]); }); v+=8; }
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
      var since=(spec.scope==='page'&&typeof dateThreshold!=='undefined'&&dateThreshold)?dateThreshold.slice(0,7):'';
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

  var panel=document.createElement('div');
  panel.style.cssText='position:fixed;right:16px;bottom:16px;width:640px;height:560px;z-index:2147483000;background:#11131a;border:1px solid #3a3f4b;border-radius:8px;box-shadow:0 8px 30px rgba(0,0,0,.6);font:12px system-ui,sans-serif;color:#ddd;display:flex;flex-direction:column;overflow:visible';
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
  $('cp-x').onclick=function(){ panel.style.display='none'; };
  var MAP={'cp-kinds':'kinds','cp-groups':'groups','cp-str':'strengths'};
  function syncUI(){ $('cp-plot').value=spec.plot; $('cp-axis').value=spec.axis; $('cp-scope').value=spec.scope; $('cp-cut').value=spec.cut; $('cp-from').value=spec.from; $('cp-to').value=spec.to;
    Object.keys(MAP).forEach(function(id){ var arr=spec[MAP[id]], boxes=$(id).querySelectorAll('input'); boxes.forEach(function(b){ b.checked=arr.indexOf(b.value)>=0; }); $(id+'-n').textContent='('+arr.length+'/'+boxes.length+')'; }); }
  ['cp-plot','cp-axis','cp-scope','cp-cut','cp-from','cp-to'].forEach(function(id){ $(id).onchange=function(e){ spec[id.slice(3)]=e.target.value; refresh(); }; });
  Object.keys(MAP).forEach(function(id){ var box=$(id);
    box.onchange=function(){ spec[MAP[id]]=[].slice.call(box.querySelectorAll('input:checked')).map(function(b){return b.value;}); refresh(); };
    box.onclick=function(ev){ var a=ev.target; if(a.tagName!=='A') return; ev.preventDefault(); box.querySelectorAll('input').forEach(function(b){ b.checked=!!a.dataset.all; }); box.onchange(); }; });
  (function(){ var h=$('cp-h'),sx,sy,ox,oy; h.onmousedown=function(e){ if(e.target.tagName==='BUTTON') return; sx=e.clientX;sy=e.clientY; var r=panel.getBoundingClientRect(); ox=r.left;oy=r.top;
    document.onmousemove=function(ev){ panel.style.left=(ox+ev.clientX-sx)+'px'; panel.style.top=(oy+ev.clientY-sy)+'px'; panel.style.right='auto'; panel.style.bottom='auto'; };
    document.onmouseup=function(){ document.onmousemove=null; document.onmouseup=null; }; }; })();

  (function(){ var MINW=460,MINH=400,G=6,C=14;
    var H={n:'top:-3px;left:'+C+'px;right:'+C+'px;height:'+G+'px;cursor:ns-resize',s:'bottom:-3px;left:'+C+'px;right:'+C+'px;height:'+G+'px;cursor:ns-resize',
      e:'right:-3px;top:'+C+'px;bottom:'+C+'px;width:'+G+'px;cursor:ew-resize',w:'left:-3px;top:'+C+'px;bottom:'+C+'px;width:'+G+'px;cursor:ew-resize',
      ne:'top:-3px;right:-3px;width:'+C+'px;height:'+C+'px;cursor:nesw-resize',sw:'bottom:-3px;left:-3px;width:'+C+'px;height:'+C+'px;cursor:nesw-resize',
      nw:'top:-3px;left:-3px;width:'+C+'px;height:'+C+'px;cursor:nwse-resize',se:'bottom:-3px;right:-3px;width:'+C+'px;height:'+C+'px;cursor:nwse-resize'};
    Object.keys(H).forEach(function(d){ var g=document.createElement('div'); g.className='cp-grip'; g.dataset.dir=d;
      g.style.cssText='position:absolute;z-index:5;touch-action:none;'+H[d]+(d==='se'?';background:linear-gradient(135deg,transparent 55%,#6b7080 55%,#6b7080 65%,transparent 65%,transparent 75%,#6b7080 75%,#6b7080 85%,transparent 85%)':'');
      g.onpointerdown=function(e){ e.preventDefault(); e.stopPropagation(); g.setPointerCapture(e.pointerId);
        var r=panel.getBoundingClientRect(), sx=e.clientX, sy=e.clientY, vw=window.innerWidth, vh=window.innerHeight;
        panel.style.left=r.left+'px'; panel.style.top=r.top+'px'; panel.style.right='auto'; panel.style.bottom='auto';
        var cover=document.createElement('div'); cover.style.cssText='position:absolute;inset:0;z-index:4'; panel.appendChild(cover);
        g.onpointermove=function(ev){ var dx=ev.clientX-sx, dy=ev.clientY-sy, L=r.left, T=r.top, W=r.width, Hh=r.height;
          if(d.indexOf('e')>=0) W=Math.min(Math.max(MINW,r.width+dx),vw-r.left);
          if(d.indexOf('s')>=0) Hh=Math.min(Math.max(MINH,r.height+dy),vh-r.top);
          if(d.indexOf('w')>=0){ W=Math.min(Math.max(MINW,r.width-dx),r.right); L=r.right-W; }
          if(d.indexOf('n')>=0){ Hh=Math.min(Math.max(MINH,r.height-dy),r.bottom); T=r.bottom-Hh; }
          panel.style.left=L+'px'; panel.style.top=T+'px'; panel.style.width=W+'px'; panel.style.height=Hh+'px'; };
        g.onpointerup=g.onpointercancel=function(){ g.onpointermove=null; g.onpointerup=null; g.onpointercancel=null; cover.remove(); }; };
      panel.appendChild(g); });
    var pend=0; if(window.ResizeObserver) new ResizeObserver(function(){ if(pend) return; pend=requestAnimationFrame(function(){ pend=0; var el=$('cp-p'); if(window.Plotly&&el&&el.data) Plotly.Plots.resize(el); }); }).observe($('cp-p'));
  })();

  var last='';
  function refresh(){ last=''; tick(); }
  function draw(){ syncUI(); var E=edges(), out=PLOTS[spec.plot](E);
    Plotly.react($('cp-p'),out.data,out.layout,{displaylogo:false,responsive:true});
    var cut=(spec.scope==='page'&&typeof SEARCH_CUT!=='undefined'&&SEARCH_CUT)?('cut "'+SEARCH_CUT.query+'" ('+spec.cut+') · '):'';
    var tw=[]; if(spec.scope==='page'&&typeof dateThreshold!=='undefined'&&dateThreshold) tw.push('page since '+dateThreshold); if(spec.from||spec.to) tw.push('edges '+(spec.from||'start')+' to '+(spec.to||'now')); var tws=tw.length?tw.join(', ')+' · ':'';
    $('cp-s').textContent=cut+tws+(spec.scope==='page'?activeNodes.length+' nodes in view · ':'whole corpus · ')+out.n.toLocaleString()+(spec.plot==='strength'?' signals':spec.plot==='timeline'?' edges':' edges between '+(spec.axis==='group'?'groups':'thinkers'))+' · '+new Date().toLocaleTimeString(); }
  function sig(){ return JSON.stringify(spec)+'|'+(spec.scope==='page'?[activeNodes.length,(typeof _lastEdgePass!=='undefined'?_lastEdgePass:''),(typeof SEARCH_CUT!=='undefined'&&SEARCH_CUT?SEARCH_CUT.query+':'+SEARCH_CUT.ids.length:''),(typeof dateThreshold!=='undefined'?dateThreshold:'')].join('|'):''); }
  function tick(){ if(panel.style.display==='none'||!window.Plotly) return; var s=sig(); if(s===last) return; last=s; try{ draw(); }catch(err){ $('cp-s').textContent='plot error: '+err.message; } }

  window.C2A2Plot={ panel:panel, refresh:refresh, plots:Object.keys(PLOTS), kinds:KINDS, groups:GROUPS, strengths:STRS, months:MONTHS,
    get:function(){ return JSON.parse(JSON.stringify(spec)); },
    set:function(p){ Object.keys(p||{}).forEach(function(k){ if(k in spec) spec[k]=p[k]; }); panel.style.display='flex'; refresh(); return this.get(); } };
  if (window.Plotly) { tick(); setInterval(tick,1000); }
  else { var sc=document.createElement('script'); sc.src='https://cdnjs.cloudflare.com/ajax/libs/plotly.js/2.34.0/plotly.min.js'; sc.onload=function(){ tick(); setInterval(tick,1000); }; sc.onerror=function(){ $('cp-s').textContent='Could not load Plotly from cdnjs.'; }; document.head.appendChild(sc); }
})();
