const E = require('./engine.js');
const STY = ['깡총', '앞장', '눈치', '뒷심'], APT = ['직진', '코너'];
// opt.focal: 0번 포로 고정, opt.snackAt: 0번 포로에게 간식을 줄 기운 기준(null = 안 줌), opt.share0: 0번 포로가 받는 응원 비율
function runOne(seed, ci, opt = {}) {
  const R = E.rng(seed * 7919 + 13 + ci), course = E.CIRCUITS[ci];
  const en = Array.from({ length: 8 }, () => ({ apt: APT[Math.floor(R() * 2)], style: STY[Math.floor(R() * 4)] }));
  if (opt.focal) Object.assign(en[0], opt.focal);
  let w = en.map(() => 0.3 + R()); if (opt.share0 !== undefined) { const rest = w.slice(1).reduce((a, b) => a + b, 0); w = w.map((x, i) => i === 0 ? opt.share0 : x / rest * (1 - opt.share0)); }
  const sum = w.reduce((a, b) => a + b, 0), share = w.map(x => x / sum);
  const race = E.newRace(en, course, seed + ci * 99991), lowAt = en.map(() => null), dl = en.map(() => R() * 3);
  while (!race.done) {
    E.step(race, opt.noCheer ? null : share);
    race.poros.forEach((p, i) => {
      if (i === 0 && 'snackAt' in opt) { if (opt.snackAt !== null && !p.snacked && Math.max(0, p.d) / race.total > .25 && p.e >= opt.snackAt[0] && p.e <= opt.snackAt[1]) E.giveSnack(race, 0); return; }
      if (p.e < 20 && lowAt[i] === null) lowAt[i] = race.t; if (lowAt[i] !== null && !p.snacked && race.t - lowAt[i] >= dl[i]) E.giveSnack(race, i);
    });
  }
  return { race, en, order: race.finished };
}
const pct = x => (x * 100).toFixed(1) + '%', N = +process.argv[2] || 4000, out = { circuits: [], snack: {}, cheer: {} };
E.CIRCUITS.forEach((c, ci) => {
  const win = {}, cnt = {}; let T = 0, passes = 0, lc = 0;
  for (let s = 1; s <= N; s++) { const { race, en, order } = runOne(s, ci); en.forEach((e, i) => { for (const k of [e.style, e.apt, e.apt + '·' + e.style]) { cnt[k] = (cnt[k] || 0) + 1; if (order[0] === i) win[k] = (win[k] || 0) + 1; } }); T += race.poros[order[0]].fin; passes += race.passes; lc += race.leadChanges; }
  const w = {}; for (const k in cnt) w[k] = +((win[k] || 0) / cnt[k] * 100).toFixed(1);
  out.circuits.push({ key: c.key, name: c.name, curve: Math.round(c.curveRatio * 100), corners: c.corners, win: w, winTime: +(T / N).toFixed(1), passes: +(passes / N).toFixed(1), leadChanges: +(lc / N).toFixed(1) });
});
// 간식 타이밍: 균형 서킷의 직진형 깡총(초반에 기운을 다 쓰는 포로)
for (const [lab, v] of [['기운이 바닥일 때', [0, 10]], ['절반쯤 남았을 때', [45, 55]], ['거의 가득일 때', [88, 100]], ['안 줌', null]]) {
  let w = 0, t3 = 0; for (let s = 1; s <= N; s++) { const { order } = runOne(s + 77777, 1, { focal: { apt: '직진', style: '깡총' }, snackAt: v }); if (order[0] === 0) w++; if (order.slice(0, 3).includes(0)) t3++; }
  out.snack[lab] = { win: pct(w / N), top3: pct(t3 / N) };
}
// 응원: 균형 서킷의 직진형 눈치, 전체 응원 중 받은 비율
for (const [lab, v] of [['0%', 0], ['12.5%(고르게)', 0.125], ['35%', 0.35], ['70%(몰빵)', 0.7]]) {
  let w = 0, last = 0, t3 = 0; for (let s = 1; s <= N; s++) { const { order } = runOne(s + 55555, 1, { focal: { apt: '직진', style: '눈치' }, share0: v }); if (order[0] === 0) w++; if (order[7] === 0) last++; if (order.slice(0, 3).includes(0)) t3++; }
  out.cheer[lab] = { win: pct(w / N), top3: pct(t3 / N), last: pct(last / N) };
}
console.log(JSON.stringify(out, null, 1));
