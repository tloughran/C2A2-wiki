const http = require('http');
const get = u => new Promise((res, rej) => http.get(u, r => { let b=''; r.on('data',c=>b+=c); r.on('end',()=>res(JSON.parse(b))); }).on('error', rej));
(async () => {
  const tabs = await get('http://127.0.0.1:9222/json');
  const page = tabs.find(t => t.type === 'page' && t.url.includes('wiki_narration'));
  const ws = new WebSocket(page.webSocketDebuggerUrl);
  let id = 0; const pend = new Map();
  const send = (m,p) => new Promise(r => { const i=++id; pend.set(i,r); ws.send(JSON.stringify({id:i,method:m,params:p})); });
  ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && pend.has(m.id)) { pend.get(m.id)(m.result); pend.delete(m.id); } };
  const ev = async x => { const r = await send('Runtime.evaluate',{expression:x,returnByValue:true,awaitPromise:true}); return r&&r.result?r.result.value:r; };
  await new Promise(r => ws.onopen = r);
  await send('Runtime.enable', {});
  await new Promise(r => setTimeout(r, 2500));

  // Ask the bus the way the shell does: postMessage describe_view, await the reply.
  const askBus = `new Promise(function(resolve){
      var done=false;
      function onMsg(e){
        var d=e.data;
        if(!d||d.source!=='c2a2-tab'||d.type!=='view_descriptor')return;
        done=true; window.removeEventListener('message',onMsg);
        var c=d.payload&&d.payload.state&&d.payload.state.counts;
        resolve(JSON.stringify({counts:c, dom:(document.getElementById('graph-status')||{}).textContent}));
      }
      window.addEventListener('message',onMsg);
      window.postMessage({source:'c2a2-voice',type:'describe_view',requestId:'t'+Date.now()},'*');
      setTimeout(function(){ if(!done){window.removeEventListener('message',onMsg); resolve('NO REPLY');} },2500);
   })`;

  // Reset to a known-good view first -- a prior run may have left the tab zoomed
  // away, which would make "at rest" already read zero and the test vacuous.
  await ev(`(function(){var el=document.getElementById('graph-svg');
      var t=d3.zoomIdentity.translate(470,291).scale(0.204); el.__zoom=t;
      if(typeof gRoot!=='undefined'&&gRoot)gRoot.attr('transform',t);
      try{updateViewportCounts();}catch(e){} return 'reset';})()`);
  await new Promise(r => setTimeout(r, 500));

  const before = await ev(askBus);
  console.log('AT REST         :', before);

  await ev(`(function(){var el=document.getElementById('graph-svg');
      var t=d3.zoomIdentity.translate(-900000,-900000).scale(12); el.__zoom=t;
      if(typeof gRoot!=='undefined'&&gRoot)gRoot.attr('transform',t);
      try{updateViewportCounts();}catch(e){} return 'ok';})()`);
  await new Promise(r => setTimeout(r, 500));
  const after = await ev(askBus);
  console.log('ZOOMED TO EMPTY :', after);

  const b = JSON.parse(before), a = JSON.parse(after);
  const held = a.counts.passingNodes === b.counts.passingNodes && b.counts.passingNodes > 0;
  const dropped = b.counts.inViewNodes > 0 && a.counts.inViewNodes === 0;
  console.log('\npassingNodes held :', held, `(${b.counts.passingNodes} -> ${a.counts.passingNodes})`);
  console.log('inViewNodes -> 0  :', dropped, `(${b.counts.inViewNodes} -> ${a.counts.inViewNodes})`);
  console.log('legacy visibleNodes present:', 'visibleNodes' in a.counts);
  console.log(held && dropped ? '\nPASS' : '\nFAIL');
  process.exit(held && dropped ? 0 : 1);
})();
