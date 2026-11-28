const E = require('./engine.js');
const STY = ['깡총', '앞장', '눈치', '뒷심'], APT = ['직진', '코너'];
function runOne(seed, curve, opt = {}) {
  const R = E.rng(seed * 7919 + 13);
  const course = E.makeCourse(curve, R);
  const entries = Array.from({ length: 8 }, (_, i) => ({ name: 'P' + i, apt: APT[Math.floor(R() * 2)], style: STY[Math.floor(R() * 4)] }));
  if (opt.focal) Object.assign(entries[0], opt.focal);
  // 관객 응원 비율(무작위) — 포로 0번은 옵션으로 고정
  let w = entries.map(() => 0.3 + R()); if (opt.share0 !== undefined) { const rest = w.slice(1).reduce((a, b) => a + b, 0); w = w.map((x, i) => i === 0 ? opt.share0 : x / rest * (1 - opt.share0)); }
  const sum = w.reduce((a, b) => a + b, 0), share = w.map(x => x / sum);
  const race = E.newRace(entries, course, seed);
  const delay = entries.map(() => 0.5 + R() * 3.5);
  if (opt.snack0 !== undefined) delay[0] = opt.snack0;     // null = 간식 안 줌
  let guard = 0;
  while (!race.done && guard++ < 5000) {
    E.step(race, opt.noCheer ? null : share);
    race.poros.forEach((p, i) => { if (p.tired && !p.recovered && delay[i] !== null && race.t - p.tiredAt >= delay[i]) E.giveSnack(race, i); });
  }
  return { race, entries, order: race.finished };
}
function pct(x) { return (x * 100).toFixed(1) + '%'; }
const N = +process.argv[2] || 6000, out = {};
// 1) 코스별 각질 · 적성 1등 확률 (포로 1마리 기준, 평균 12.5%)
out.course = {};
for (const curve of [0.3, 0.5, 0.7]) {
  const win = {}, cnt = {}; let tAvg = 0, tiredAt = 0, tiredN = 0, slips = 0, dashes = 0;
  for (let s = 1; s <= N; s++) {
    const { race, entries, order } = runOne(s, curve);
    entries.forEach((e, i) => { for (const k of [e.style, e.apt, e.apt + '·' + e.style]) { cnt[k] = (cnt[k] || 0) + 1; if (order[0] === i) win[k] = (win[k] || 0) + 1; } });
    tAvg += race.poros[order[0]].fin; race.poros.forEach(p => { if (p.tiredAt !== null) { tiredAt += p.tiredAt; tiredN++; } slips += p.slips; dashes += p.dashes; });
  }
  const r = {}; for (const k in cnt) r[k] = +(win[k] / cnt[k] * 100 || 0).toFixed(1);
  out.course[curve] = { win: r, winTime: +(tAvg / N).toFixed(1), tiredAt: +(tiredAt / tiredN).toFixed(1), tiredShare: +(tiredN / N / 8 * 100).toFixed(0), slipsPerRace: +(slips / N).toFixed(2), dashesPerRace: +(dashes / N).toFixed(2) };
}
// 2) 간식 타이밍: 0번 포로(앞장 · 코너, 보통 길) 1등 · 3등 안 확률
out.snack = {};
for (const [lab, v] of [['바로(0.3초)', 0.3], ['늦게(4초)', 4], ['아주 늦게(10초)', 10], ['안 줌', null]]) {
  let w = 0, t3 = 0;
  for (let s = 1; s <= N; s++) { const { order } = runOne(s + 99991, 0.5, { focal: { apt: '코너', style: '깡총' }, snack0: v }); if (order[0] === 0) w++; if (order.slice(0, 3).includes(0)) t3++; }
  out.snack[lab] = { win: pct(w / N), top3: pct(t3 / N) };
}
// 3) 응원 몰림: 0번 포로가 받은 응원 비율별
out.cheer = {};
for (const [lab, v] of [['응원 없음', 'none'], ['0%', 0], ['12.5%(고르게)', 0.125], ['35%', 0.35], ['70%(몰빵)', 0.7]]) {
  let w = 0, t3 = 0, last = 0;
  for (let s = 1; s <= N; s++) { const o = Object.assign({ focal: { apt: '직진', style: '눈치' } }, v === 'none' ? { noCheer: true } : { share0: v }); const { order } = runOne(s + 55555, 0.5, o); if (order[0] === 0) w++; if (order.slice(0, 3).includes(0)) t3++; if (order[7] === 0) last++; }
  out.cheer[lab] = { win: pct(w / N), top3: pct(t3 / N), last: pct(last / N) };
}
console.log(JSON.stringify(out, null, 1));
