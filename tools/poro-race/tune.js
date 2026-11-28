const E = require('./engine.js');
const STY = ['깡총','앞장','눈치','뒷심'], APT=['직진','코너'];
const over = JSON.parse(process.argv[3]||'{}'); for (const k in over) { const path=k.split('.'); let o=E.P; while(path.length>1) o=o[path.shift()]; o[path[0]]=over[k]; }
const N=+process.argv[2]||800, res={};
E.CIRCUITS.forEach((c, ci) => {
  const win={},cnt={}; let T=0, passes=0, lc=0, boostT=0, eEnd=0;
  for (let s=1;s<=N;s++){
    const R=E.rng(s*7919+13+ci);
    const en=Array.from({length:8},()=>({apt:APT[Math.floor(R()*2)],style:STY[Math.floor(R()*4)]}));
    const race=E.newRace(en,c,s+ci*99991), lowAt=en.map(()=>null), dl=en.map(()=>R()*3);
    while(!race.done){E.step(race,en.map(()=>1/8)); race.poros.forEach((p,i)=>{ if(p.e<20&&lowAt[i]===null) lowAt[i]=race.t; if(lowAt[i]!==null&&!p.snacked&&race.t-lowAt[i]>=dl[i]) E.giveSnack(race,i); if(p.boosting) boostT+=E.P.dt;});}
    en.forEach((e,i)=>{for(const k of [e.style,e.apt,e.apt+'·'+e.style]){cnt[k]=(cnt[k]||0)+1; if(race.finished[0]===i) win[k]=(win[k]||0)+1;}});
    T+=race.poros[race.finished[0]].fin; passes+=race.passes; lc+=race.leadChanges;
  }
  const r={T:+(T/N).toFixed(1), passes:+(passes/N).toFixed(1), lead:+(lc/N).toFixed(1), boost:+(boostT/N/8/(T/N)*100).toFixed(0)+'%'};
  for(const k of [...STY,...APT]) r[k]=+((win[k]||0)/cnt[k]*100).toFixed(1);
  r.best=Object.keys(win).filter(k=>k.includes('·')).map(k=>[k,+(win[k]/cnt[k]*100).toFixed(1)]).sort((a,b)=>b[1]-a[1]).slice(0,2);
  res[c.name+' '+Math.round(c.curveRatio*100)+'%']=r;
});
console.log(JSON.stringify(res,null,0).replace(/\},/g,'},\n'));
