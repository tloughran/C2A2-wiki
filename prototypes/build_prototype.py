#!/usr/bin/env python3
"""Build a self-contained Level-2 cross-tradition signal-stream prototype.
Reads signals.json (from extract_signals.py), inlines it, emits one HTML file.
No external dependencies (vanilla JS + inline SVG) so it loads offline from file://.
"""
import json, os, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "signals_grown.json")
sig = json.load(open(src))
out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "level2_signal_stream.html")

PALETTE = {
 "Levin":"#C45B5B","Friston":"#5A8EAF","Hoffman":"#C08B3E","Kastrup":"#8B5DAB",
 "McGilchrist":"#3D9E89","Hawkins":"#B87D3E","Wolfram":"#4A5E6D","Carroll":"#4E8A5E",
 "Arkani-Hamed":"#A85D3A","Fredrickson":"#C47A9A","Stump":"#A8923A","Rohr":"#9A7A5A",
 "Wright":"#5A72A8","Loughran":"#4A8A7A",
}

data_json = json.dumps(sig, separators=(",",":"))
palette_json = json.dumps(PALETTE)
n_pairs = len(set((s["a"],s["b"]) for s in sig))
span = (sig[0]["date"], sig[-1]["date"])
n_card = sum(1 for s in sig if s["card"])

HTML = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Level 2 — Searchers Becoming Mutually Informed</title>
<style>
  :root{ --bg:#0a0a0f; --panel:#13131c; --panel2:#191923; --ink:#e8e6ef; --dim:#9a98a8;
         --line:#2a2a38; --accent:#C9A84C; }
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--ink);
       font:14px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
  header{padding:18px 22px 10px}
  h1{margin:0 0 2px;font-size:19px;font-weight:650;letter-spacing:.2px}
  .sub{color:var(--dim);font-size:13px;max-width:760px}
  .stats{margin-top:8px;color:var(--dim);font-size:12.5px}
  .stats b{color:var(--accent);font-weight:600}
  .wrap{display:grid;grid-template-columns:minmax(440px,1.1fr) minmax(360px,1fr);
        gap:16px;padding:8px 22px 26px;align-items:start}
  .panel{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px 16px}
  .panel h2{margin:0 0 4px;font-size:13px;font-weight:600;letter-spacing:.4px;text-transform:uppercase;color:var(--dim)}
  .panel .note{color:var(--dim);font-size:12px;margin:0 0 10px}
  .controls{display:flex;gap:14px;flex-wrap:wrap;align-items:center;padding:2px 22px 4px;color:var(--dim);font-size:12.5px}
  .controls label{cursor:pointer;user-select:none}
  .controls select{background:var(--panel2);color:var(--ink);border:1px solid var(--line);
                   border-radius:6px;padding:3px 7px;font:inherit}
  svg{display:block;width:100%;height:auto;overflow:visible}
  .cell{cursor:pointer;stroke:var(--bg);stroke-width:1}
  .cell:hover{stroke:var(--accent);stroke-width:1.5}
  .cell.sel{stroke:#fff;stroke-width:2}
  .axlab{font-size:11px;fill:var(--dim)}
  .axlab.row{text-anchor:end}
  .cellnum{font-size:9.5px;fill:#0a0a0f;font-weight:600;pointer-events:none}
  .tl-area{opacity:.85}
  .tl-line{fill:none;stroke:var(--accent);stroke-width:2}
  .tl-axis{stroke:var(--line)}
  .tl-tick{font-size:10px;fill:var(--dim)}
  #detail{max-height:560px;overflow:auto}
  .sigcard{border:1px solid var(--line);border-radius:8px;padding:9px 11px;margin-bottom:9px;background:var(--panel2)}
  .sigcard .top{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-bottom:4px}
  .pill{font-size:10.5px;padding:1px 7px;border-radius:20px;border:1px solid var(--line);color:var(--dim)}
  .pill.date{color:var(--accent);border-color:#4a4326}
  .pill.High{color:#e7c95a;border-color:#5a4f1e}
  .pill.Strong{color:#bfe0a8;border-color:#3a5226}
  .pill.Moderate{color:#9ab8d6;border-color:#2a3e52}
  .pill.Speculative{color:#b79ad6;border-color:#3e2a52}
  .pill.src{font-style:italic}
  .sigcard .txt{font-size:12.5px;color:var(--ink);opacity:.92}
  .sigcard .meta{font-size:11px;color:var(--dim);margin-top:5px}
  .dyad{font-weight:600}
  .empty{color:var(--dim);font-size:12.5px;padding:20px 4px}
  .legend{display:flex;gap:14px;flex-wrap:wrap;font-size:11.5px;color:var(--dim);margin-top:8px}
  .legend i{display:inline-block;width:11px;height:11px;border-radius:3px;margin-right:4px;vertical-align:-1px}
  .foot{padding:0 22px 30px;color:var(--dim);font-size:11.5px;max-width:900px}
  .foot code{background:var(--panel2);padding:1px 5px;border-radius:4px}
</style></head>
<body>
<header>
  <h1>Level 2 &mdash; Searchers Becoming Mutually Informed</h1>
  <div class="sub">Cross-tradition <b style="color:var(--accent)">signals</b>: each is a dated event in which one tradition&rsquo;s agent, reading another lineage&rsquo;s material, registered a connection. Not the static similarity geometry of the connectome &mdash; the <em>event stream of formation</em> as builders become mutually informed.</div>
  <div class="stats">__STATS__</div>
</header>

<div class="controls">
  <label>Strength
    <select id="fStrength">
      <option value="">all</option><option>High</option><option>Strong</option>
      <option>Moderate</option><option>Speculative</option>
    </select></label>
  <label>Source layer
    <select id="fSource">
      <option value="">all</option>
      <option value="finding">pattern-detector findings</option>
      <option value="index">cross-program index</option>
      <option value="card">per-card resonances</option>
    </select></label>
  <label><input type="checkbox" id="fCard"> only signals with a source card</label>
  <span id="selnote" style="margin-left:auto;color:var(--accent)"></span>
</div>

<div class="wrap">
  <div class="panel">
    <h2>Where formation is happening</h2>
    <p class="note">Tradition &times; tradition. Cell darkness = number of signals on that seam. Click a cell to read its signals.</p>
    <svg id="matrix"></svg>
  </div>
  <div>
    <div class="panel" style="margin-bottom:16px">
      <h2>Interactions accumulating over time</h2>
      <p class="note"><b style="color:var(--accent)">Formation activity</b> &mdash; cumulative signals dated by <em>when the agent registered the connection</em> (proposal date). The slope is the proof of life.</p>
      <svg id="timeline" viewBox="0 0 520 180"></svg>
      <div class="legend" id="tllegend"></div>
      <p class="note" style="margin:12px 0 2px">Source-material vintage &mdash; <em>when the underlying talk/paper was published</em> (card-backed signals only). A different clock from formation: old ideas can be freshly engaged.</p>
      <svg id="srcvintage" viewBox="0 0 520 96"></svg>
    </div>
    <div class="panel">
      <h2 id="dethead">Signals</h2>
      <div id="detail"><div class="empty">Click a matrix cell (a tradition pair) to read the actual dated signals on that seam.</div></div>
    </div>
  </div>
</div>

<div class="foot">
  Prototype built from the live review-card layer: <code>pattern_detector_findings.md</code>,
  <code>cross_program_index.md</code>, and the <code>cross_signals</code> batches. Multi-tradition
  index items are expanded to all pairs. This is distinct from the narrative-connectome cross-edges,
  which are computed PRS-similarity (static, undated). Data is inlined; regenerate with
  <code>extract_signals.py</code> + <code>build_prototype.py</code>.
</div>

<script>
const SIG = __DATA__;
const PAL = __PAL__;
let selPair = null;

const $ = s => document.querySelector(s);
function filtered(){
  const st=$('#fStrength').value, sr=$('#fSource').value, oc=$('#fCard').checked;
  return SIG.filter(s =>
    (!st || s.strength===st) && (!sr || s.source===sr) && (!oc || s.card));
}

// ---- matrix ----
function traditions(rows){
  const tot={};
  rows.forEach(s=>{tot[s.a]=(tot[s.a]||0)+1;tot[s.b]=(tot[s.b]||0)+1;});
  return Object.keys(tot).sort((x,y)=>tot[y]-tot[x]);
}
function drawMatrix(){
  const rows=filtered();
  const T=traditions(rows);
  const counts={};
  rows.forEach(s=>{const k=s.a<s.b?s.a+'|'+s.b:s.b+'|'+s.a; counts[k]=(counts[k]||0)+1;});
  const max=Math.max(1,...Object.values(counts));
  const n=T.length, cell=Math.min(34, Math.max(20, Math.floor(520/Math.max(n,8))));
  const m={l:96,t:96};
  const W=m.l+n*cell+8, H=m.t+n*cell+8;
  const svg=$('#matrix'); svg.setAttribute('viewBox',`0 0 ${W} ${H}`);
  let h='';
  // labels
  T.forEach((t,i)=>{
    h+=`<text class="axlab row" x="${m.l-6}" y="${m.t+i*cell+cell/2+3}" fill="${PAL[t]||'#9a98a8'}">${t}</text>`;
    h+=`<text class="axlab" transform="translate(${m.l+i*cell+cell/2},${m.t-6}) rotate(-55)" fill="${PAL[t]||'#9a98a8'}">${t}</text>`;
  });
  for(let i=0;i<n;i++)for(let j=0;j<n;j++){
    if(i===j){h+=`<rect x="${m.l+j*cell}" y="${m.t+i*cell}" width="${cell}" height="${cell}" fill="#101019" stroke="var(--bg)"/>`;continue;}
    const a=T[i],b=T[j], k=a<b?a+'|'+b:b+'|'+a, c=counts[k]||0;
    const o = c? (0.18+0.82*Math.pow(c/max,0.6)) : 0;
    const sel = selPair && ((selPair[0]===a&&selPair[1]===b)||(selPair[0]===b&&selPair[1]===a));
    h+=`<rect class="cell${sel?' sel':''}" data-a="${a}" data-b="${b}" x="${m.l+j*cell}" y="${m.t+i*cell}" width="${cell}" height="${cell}" `+
       `fill="${c?`rgba(201,168,76,${o.toFixed(3)})`:'#0e0e16'}"><title>${a} × ${b}: ${c} signal${c!==1?'s':''}</title></rect>`;
    if(c && cell>=22) h+=`<text class="cellnum" x="${m.l+j*cell+cell/2}" y="${m.t+i*cell+cell/2+3.5}" text-anchor="middle" fill="${o>0.5?'#0a0a0f':'#8a7a3a'}">${c}</text>`;
  }
  svg.innerHTML=h;
  svg.querySelectorAll('.cell').forEach(r=>r.onclick=()=>{
    selPair=[r.dataset.a,r.dataset.b]; drawMatrix(); showPair();
  });
}

// ---- timeline ----
function drawTimeline(){
  const rows=filtered().slice().sort((a,b)=>a.date<b.date?-1:1);
  const svg=$('#timeline'); const W=520,H=180,m={l:34,r:10,t:10,b:24};
  if(!rows.length){svg.innerHTML='';return;}
  const t0=+new Date(rows[0].date), t1=+new Date(rows[rows.length-1].date);
  const span=Math.max(1,t1-t0);
  const x=d=>m.l+(W-m.l-m.r)*((+new Date(d))-t0)/span;
  const N=rows.length, y=i=>H-m.b-(H-m.t-m.b)*i/N;
  let d=`M ${m.l} ${H-m.b}`;
  rows.forEach((s,i)=>{d+=` L ${x(s.date).toFixed(1)} ${y(i+1).toFixed(1)}`;});
  let area=d+` L ${x(rows[rows.length-1].date).toFixed(1)} ${H-m.b} Z`;
  // month ticks
  let ticks='';
  const seen=new Set();
  rows.forEach(s=>{const mo=s.date.slice(0,7); if(!seen.has(mo)){seen.add(mo);
    const xx=x(s.date); ticks+=`<line class="tl-axis" x1="${xx}" y1="${m.t}" x2="${xx}" y2="${H-m.b}" stroke-dasharray="2 3" opacity=".4"/>`+
      `<text class="tl-tick" x="${xx+2}" y="${H-m.b+13}">${mo}</text>`;}});
  // y labels
  let yl='';[0,Math.round(N/2),N].forEach(v=>{const yy=y(v);yl+=`<text class="tl-tick" x="2" y="${yy+3}">${v}</text>`;});
  svg.innerHTML=`<line class="tl-axis" x1="${m.l}" y1="${H-m.b}" x2="${W-m.r}" y2="${H-m.b}"/>`+
    `<line class="tl-axis" x1="${m.l}" y1="${m.t}" x2="${m.l}" y2="${H-m.b}"/>`+ticks+
    `<path class="tl-area" d="${area}" fill="rgba(201,168,76,0.14)"/>`+
    `<path class="tl-line" d="${d}"/>`+yl;
  // legend by source
  const c={}; filtered().forEach(s=>c[s.source]=(c[s.source]||0)+1);
  const names={finding:'findings',index:'cross-index',card:'card resonances'};
  $('#tllegend').innerHTML=Object.keys(names).map(k=>`<span><i style="background:rgba(201,168,76,.5)"></i>${names[k]}: <b style="color:var(--ink)">${c[k]||0}</b></span>`).join('');
}

// ---- detail ----
function esc(s){return (s||'').replace(/[&<>]/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[m]));}
function showPair(){
  if(!selPair){return;}
  const [a,b]=selPair;
  const rows=filtered().filter(s=>(s.a===a&&s.b===b)||(s.a===b&&s.b===a))
    .sort((x,y)=>x.date<y.date?1:-1);
  $('#selnote').textContent = `${a} × ${b} — ${rows.length} signal${rows.length!==1?'s':''}`;
  $('#dethead').innerHTML = `<span class="dyad" style="color:${PAL[a]}">${a}</span> &times; <span class="dyad" style="color:${PAL[b]}">${b}</span> &mdash; ${rows.length} signals`;
  if(!rows.length){$('#detail').innerHTML='<div class="empty">No signals match the current filters on this seam.</div>';return;}
  $('#detail').innerHTML = rows.map(s=>{
    const card = s.card? `<span class="pill src">${esc(s.card)}</span>`:'';
    const nat = s.nature? `<span class="pill">${esc(s.nature)}</span>`:'';
    return `<div class="sigcard"><div class="top">`+
      `<span class="pill date">${esc(s.date)}</span>`+
      `<span class="pill ${s.strength}">${s.strength}</span>`+nat+card+
      `<span class="pill src">${({finding:'pattern-detector',index:'cross-index',card:'card'})[s.source]}</span>`+
      `</div><div class="txt">${esc(s.text)||'<em style=opacity:.6>(no text)</em>'}</div>`+
      (s.action?`<div class="meta">&rarr; ${esc(s.action)}</div>`:'')+`</div>`;
  }).join('');
}

// ---- source-material vintage (dual encoding: different clock) ----
function drawVintage(){
  const rows=filtered().filter(s=>s.source==='card' && s.source_date && /^\d{4}-\d{2}/.test(s.source_date));
  const svg=$('#srcvintage'); const W=520,H=96,m={l:34,r:10,t:8,b:22};
  if(!rows.length){svg.innerHTML='<text class="tl-tick" x="34" y="40">no card-backed signals in filter</text>';return;}
  const bins={}; rows.forEach(s=>{const k=s.source_date.slice(0,7); bins[k]=(bins[k]||0)+1;});
  const keys=Object.keys(bins).sort();
  const months=[]; let [y0,m0]=keys[0].split('-').map(Number); const [y1,m1]=keys[keys.length-1].split('-').map(Number);
  while(y0<y1||(y0===y1&&m0<=m1)){months.push(`${y0}-${String(m0).padStart(2,'0')}`); m0++; if(m0>12){m0=1;y0++;}}
  const max=Math.max(...Object.values(bins));
  const bw=(W-m.l-m.r)/months.length;
  let h=`<line class="tl-axis" x1="${m.l}" y1="${H-m.b}" x2="${W-m.r}" y2="${H-m.b}"/>`;
  months.forEach((mo,i)=>{
    const v=bins[mo]||0, bh=(H-m.t-m.b)*v/max, x=m.l+i*bw;
    if(v) h+=`<rect x="${(x+1).toFixed(1)}" y="${(H-m.b-bh).toFixed(1)}" width="${(bw-1.5).toFixed(1)}" height="${bh.toFixed(1)}" fill="rgba(90,142,175,0.55)"><title>${mo}: ${v}</title></rect>`;
    if(mo.endsWith('-01')||i===0) h+=`<text class="tl-tick" x="${(x).toFixed(1)}" y="${H-m.b+12}">${mo.slice(0,4)}</text>`;
  });
  [0,max].forEach(v=>{const yy=H-m.b-(H-m.t-m.b)*v/max; h+=`<text class="tl-tick" x="2" y="${yy+3}">${v}</text>`;});
  svg.innerHTML=h;
}

['#fStrength','#fSource','#fCard'].forEach(id=>$(id).addEventListener('change',()=>{drawMatrix();drawTimeline();drawVintage();if(selPair)showPair();}));
drawMatrix(); drawTimeline(); drawVintage();
</script>
</body></html>"""

stats = ('<b>%d</b> signals across <b>%d</b> tradition pairs &middot; '
         '<b>%s</b> &rarr; <b>%s</b> &middot; <b>%d</b> trace to a source card'
         ) % (len(sig), n_pairs, span[0], span[1], n_card)

HTML = (HTML.replace("__DATA__", data_json)
            .replace("__PAL__", palette_json)
            .replace("__STATS__", stats))
open(out, "w").write(HTML)
print("wrote", out, "(%d bytes)" % os.path.getsize(out))
