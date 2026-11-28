const E = require('./engine.js');
const STY = ['깡총','앞장','눈치','뒷심'], APT=['직진','코너'];
const over = JSON.parse(process.argv[3]||'{}'); for (const k in over) { const path=k.split('.'); let o=E.P; while(path.length>1) o=o[path.shift()]; o[path[0]]=over[k]; }
const N=+process.argv[2]||1500, res={};
for (const curve of [0.3,0.5,0.7]) {
  const win={},cnt={}; let tired={}, tn={}, T=0;
  for (let s=1;s<=N;s++){
    const R=E.rng(s*7919+13), course=E.makeCourse(curve,R);
    const en=Array.from({length:8},()=>({apt:APT[Math.floor(R()*2)],style:STY[Math.floor(R()*4)]}));
    const sh=en.map(()=>1/8), race=E.newRace(en,course,s), dl=en.map(()=>0.5+R()*3.5);
    while(!race.done){E.step(race,sh); race.poros.forEach((p,i)=>{ if(p.tired&&!p.recovered&&race.t-p.tiredAt>=dl[i]) E.giveSnack(race,i);});}
    en.forEach((e,i)=>{for(const k of [e.style,e.apt]){cnt[k]=(cnt[k]||0)+1; if(race.finished[0]===i) win[k]=(win[k]||0)+1;}
      const p=race.poros[i]; if(p.tiredAt!==null){tired[e.style]=(tired[e.style]||0)+p.tiredAt; tn[e.style]=(tn[e.style]||0)+1;}});
    T+=race.poros[race.finished[0]].fin;
  }
  res[curve]={T:+(T/N).toFixed(1)}; for(const k of [...STY,...APT]) res[curve][k]=+((win[k]||0)/cnt[k]*100).toFixed(1);
  res[curve].tired=STY.map(k=>tn[k]?(tired[k]/tn[k]).toFixed(0)+'s/'+(tn[k]/cnt[k]*100).toFixed(0)+'%':'-').join(' ');
}
console.log(JSON.stringify(res));
