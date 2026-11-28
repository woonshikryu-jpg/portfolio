// 포로 경주 엔진 v2 — 시뮬레이션(node)과 프로토타입(브라우저)이 같은 파일을 씀
// 핵심: 기운(배터리처럼 생각). 직선에서 기운을 쓰면 더 빨라지고, 코너에서 기운이 찬다. 지치는 일은 없음.
(function (root) {
  const P = {
    L: 1000, laps: 2, seg: 8, v0: 24, dt: 0.1,
    apt: 0.02,                      // 적성: 직진형은 직선 +2% · 코너 −2%, 코너형은 반대
    energy: { cap: 100, start: 100, boost: 0.16, use: 22, charge: 9, cornerCharge: 1.6 },   // 기운: 쓰는 동안 +16% · 초당 22 소모 · 코너에서 초당 9 충전
    slip: { gap: 14, bonus: 0.035 }, // 슬립스트림: 직선에서 앞 포로 14 안쪽이면 +3.5%
    slipP: 0.012, slipT: 1.2, slipMult: 0.3, accel: 0.22,   // 미끄러짐: 커브에서 초당 1.2%, 1.2초 동안 속도 30% · 속도 변화는 부드럽게
    cheer: { minRank: 5, rate: 1.2, cap: 1.6 },             // 응원: 5~8위일 때만, 응원 비율만큼 기운 충전(평균 초당 1.2, 몰려도 최대 1.9)
    snack: 100,                                             // 간식: 기운을 가득(100) 충전(최대 100 — 넘치는 만큼은 버려짐)
    form: 0.03, noise: 0.015
  };
  // 각질 = 기운을 언제 쓰는가(경주 진행도 prog, 남은 기운 e)
  const STRAT = {
    '깡총': (prog, e) => prog < .5 ? e > 0 : e > 50,         // 처음부터 다 쓰며 달아남
    '앞장': (prog, e) => e > 45,                              // 직선마다 조금씩, 늘 반쯤 남김
    '눈치': (prog, e) => prog < .35 ? e >= 99 : e > 20,       // 초반엔 넘치는 만큼만, 중반부터 씀
    '뒷심': (prog, e) => prog < .62 ? e >= 99 : e > 0         // 끝까지 아꼈다가 마지막 바퀴에 몰아 씀
  };
  // ── 서킷: 직선(S 길이) · 코너(C 각도°, 반지름, +왼쪽 −오른쪽). 표시(1)한 두 직선 길이를 풀어 정확히 닫음
  const CIRCUITS = [
    { key: 'fast', name: '고속 서킷', desc: '긴 직선 둘, 시케인 둘', segs: [['S', 8, 1], ['C', -90, 1.0], ['S', 3, 1], ['C', -30, .8], ['C', 30, .8], ['S', 2], ['C', -90, .9], ['S', 7], ['C', -90, 1.0], ['S', 1.5], ['C', 40, .6], ['C', -40, .6], ['S', 1], ['C', -90, .9]] },
    { key: 'mid', name: '균형 서킷', desc: '헤어핀 하나, 직선과 코너가 고루', segs: [['S', 6, 1], ['C', -90, .8], ['S', 2.5, 1], ['C', -60, 1.0], ['S', 1.5], ['C', 80, .8], ['C', -150, .6], ['S', 3.5], ['C', -50, 1.3], ['S', 2], ['C', -60, .8], ['S', 2.5], ['C', 70, 1.0], ['C', -100, 1.1]] },
    { key: 'tech', name: '테크니컬 서킷', desc: '좌우 코너가 쉬지 않고 이어짐', segs: [['S', 4.5, 1], ['C', -100, .55], ['C', 70, .55], ['S', 1, 1], ['C', -90, .55], ['C', -60, .6], ['S', 1.5], ['C', 100, .5], ['C', -120, .55], ['S', 1.2], ['C', -80, .6], ['C', 60, .6], ['C', -90, .6], ['S', 1.4], ['C', -60, .6], ['S', .8], ['C', 40, .7], ['C', -30, .7]] }
  ];
  function walk(segs, extra) {
    let x = 0, y = 0, a = 0; const pts = [], kinds = [], sgn = [];
    segs.forEach(([t, v, r], i) => {
      if (t === 'S') { const L = v + (extra[i] || 0), n = Math.max(2, Math.round(L * 40)); for (let k = 0; k < n; k++) { pts.push([x, y]); kinds.push('S'); sgn.push(0); x += Math.cos(a) * L / n; y += Math.sin(a) * L / n; } }
      else { const ang = v * Math.PI / 180, L = Math.abs(ang) * r, n = Math.max(3, Math.round(L * 40)); for (let k = 0; k < n; k++) { pts.push([x, y]); kinds.push('C'); sgn.push(Math.sign(v)); a += ang / n * .5; x += Math.cos(a) * L / n; y += Math.sin(a) * L / n; a += ang / n * .5; } }
    });
    return { pts, kinds, sgn, end: [x, y] };
  }
  const N = 480;
  function buildCircuit(c) {
    const adj = c.segs.map((s, i) => s[0] === 'S' && s[2] === 1 ? i : -1).filter(i => i >= 0);
    const b = walk(c.segs, {}), d1 = walk(c.segs, { [adj[0]]: 1 }), d2 = walk(c.segs, { [adj[1]]: 1 });
    const ax = d1.end[0] - b.end[0], ay = d1.end[1] - b.end[1], bx = d2.end[0] - b.end[0], by = d2.end[1] - b.end[1], det = ax * by - ay * bx;
    const u = (-b.end[0] * by + b.end[1] * bx) / det, v = (-ax * b.end[1] + ay * b.end[0]) / det;
    const w = walk(c.segs, { [adj[0]]: u, [adj[1]]: v }), Pp = w.pts, cum = [0];
    for (let i = 1; i <= Pp.length; i++) { const a = Pp[i - 1], q = Pp[i % Pp.length]; cum.push(cum[i - 1] + Math.hypot(q[0] - a[0], q[1] - a[1])); }
    const Lt = cum[Pp.length]; let pts = [], kinds = [], sgn = [], j = 0;
    for (let k = 0; k < N; k++) { const t = k / N * Lt; while (cum[j + 1] < t) j++; const a = Pp[j], q = Pp[(j + 1) % Pp.length], f = (t - cum[j]) / (cum[j + 1] - cum[j] || 1); pts.push([(a[0] + (q[0] - a[0]) * f) / Lt * 8, (a[1] + (q[1] - a[1]) * f) / Lt * 8]); kinds.push(w.kinds[j]); sgn.push(w.sgn[j]); }
    // 출발 · 결승선을 가장 긴 직선의 3/4 지점에 둠(결승 앞에 긴 직선)
    const runs = []; for (let k = 0; k < N; k++) if (kinds[k] !== kinds[(k - 1 + N) % N]) runs.push(k);
    let best = { len: 0, s: 0 }; runs.forEach((s, r) => { const e = runs[(r + 1) % runs.length], len = ((e - s) + N) % N; if (kinds[s] === 'S' && len > best.len) best = { len, s }; });
    const sh = (best.s + Math.round(best.len * .75)) % N, rot = arr => arr.slice(sh).concat(arr.slice(0, sh));
    pts = rot(pts); kinds = rot(kinds); sgn = rot(sgn);
    const rr = []; for (let k = 0; k < N; k++) if (k === 0 || kinds[k] !== kinds[k - 1]) rr.push({ from: k / N * P.L, k: kinds[k], sgn: sgn[k] });
    rr.forEach((r, i) => r.to = i + 1 < rr.length ? rr[i + 1].from : P.L);
    const longest = Math.max(...rr.filter(r => r.k === 'S').map(r => r.to - r.from));
    return { key: c.key, name: c.name, desc: c.desc, pts, kinds, sgn, runs: rr, curveRatio: kinds.filter(k => k === 'C').length / N, corners: rr.filter(r => r.k === 'C').length, longest };
  }
  const BUILT = CIRCUITS.map(buildCircuit);
  function rng(seed) { let s = (Math.imul(seed >>> 0 ^ 0x9E3779B9, 0x85EBCA6B) >>> 0) || 1; const f = () => { s ^= s << 13; s >>>= 0; s ^= s >> 17; s ^= s << 5; s >>>= 0; return s / 4294967296; }; for (let k = 0; k < 8; k++) f(); return f; }
  function makeCourse(idx) { return BUILT[idx]; }
  function segAt(course, d) { const x = ((d % P.L) + P.L) % P.L; return course.kinds[Math.min(N - 1, Math.floor(x / P.L * N))]; }
  function newRace(entries, course, seed) {
    const R = rng(seed);
    return { R, course, t: 0, done: false, total: P.L * P.laps, finished: [], passes: 0, leadChanges: 0, lastLead: -1,
      poros: entries.map((e, i) => ({ i, name: e.name, apt: e.apt, style: e.style, d: -i * 0.4, e: P.energy.start, boosting: false, drafting: false, snacked: false,
        slip: 0, fin: null, v: 0, nz: 0, form: 1 + (R() * 2 - 1) * P.form, slips: 0, cheerE: 0, snackAt: null, snackGain: 0, rank: i + 1 })) };
  }
  function ranks(race) { return race.poros.slice().sort((a, b) => (a.fin ?? 1e9) - (b.fin ?? 1e9) || b.d - a.d); }
  // cheerShare: 포로별 최근 응원 비율(합 1). 없으면 응원 없음
  function step(race, cheerShare) {
    const dt = P.dt, R = race.R, order = ranks(race), E = P.energy;
    const prevRank = race.poros.map(p => p.rank);
    order.forEach((p, k) => p.rank = k + 1);
    const live = race.poros.filter(p => p.fin === null).sort((a, b) => b.d - a.d);
    for (const p of race.poros) {
      if (p.fin !== null) continue;
      const prog = Math.max(0, p.d) / race.total, seg = segAt(race.course, p.d);
      p.nz += ((R() * 2 - 1) - p.nz) * .15;
      let m = p.form * (1 + p.nz * P.noise * 2);
      m *= (p.apt === '직진') === (seg === 'S') ? 1 + P.apt : 1 - P.apt;
      // 기운: 직선에서 각질 전략대로 쓰면 빨라지고, 코너에서 찬다
      p.boosting = seg === 'S' && p.e > 0 && STRAT[p.style](prog, p.e);
      if (p.boosting) { m *= 1 + E.boost; p.e = Math.max(0, p.e - E.use * dt); }
      if (seg === 'C') p.e = Math.min(E.cap, p.e + E.charge * (p.apt === '코너' ? E.cornerCharge : 1) * dt);   // 코너형은 코너에서 더 빨리 참
      // 슬립스트림: 직선에서 바로 앞 포로 뒤에 붙으면 빨라짐
      const k = live.indexOf(p), f = k > 0 ? live[k - 1] : null;
      p.drafting = seg === 'S' && !!f && f.d - p.d < P.slip.gap && f.d - p.d > 0;
      if (p.drafting) m *= 1 + P.slip.bonus;
      // 응원: 5~8위일 때만 기운 충전
      if (cheerShare && p.rank >= P.cheer.minRank) { const c = Math.min(P.cheer.cap, (cheerShare[p.i] || 0) * race.poros.length) * P.cheer.rate * dt; const add = Math.min(E.cap - p.e, c); p.e += add; p.cheerE += add; }
      // 미끄러짐: 커브에서 모두 같은 확률, 멈추지 않고 휘청
      if (p.slip > 0) { p.slip -= dt; m *= P.slipMult; }
      else if (seg === 'C' && R() < P.slipP * dt) { p.slip = P.slipT; p.slips++; m *= P.slipMult; }
      const tv = P.v0 * m; p.v = race.t === 0 ? tv * .5 : p.v + (tv - p.v) * P.accel;
    }
    for (const p of race.poros) {
      if (p.fin !== null) continue;
      p.d += p.v * dt;
      if (p.d >= race.total) { p.d = race.total; p.fin = race.t + dt; race.finished.push(p.i); }
    }
    race.t += dt;
    // 추월 · 선두 교체는 앞선 차이가 2 이상 벌어졌을 때만 셈(나란히 달리며 엎치락뒤치락하는 건 한 번)
    const o2 = ranks(race), lead = o2[0];
    if (race.lastLead < 0) race.lastLead = lead.i;
    else if (lead.i !== race.lastLead && lead.d - race.poros[race.lastLead].d > 2 && race.t > 3) { race.leadChanges++; race.lastLead = lead.i; race.leadEvent = lead.i; }
    if (!race.ahead) race.ahead = {};
    for (let a = 0; a < o2.length; a++) for (let b = a + 1; b < o2.length; b++) { const x = o2[a], y = o2[b], key = x.i < y.i ? x.i + '-' + y.i : y.i + '-' + x.i, gap = x.d - y.d, cur = race.ahead[key];
      if (cur === undefined) { race.ahead[key] = x.i; continue; }
      if (cur !== x.i && gap > 2 && x.fin === null && race.t > 3) { race.ahead[key] = x.i; race.passes++; } }
    if (race.finished.length === race.poros.length) race.done = true;
  }
  function giveSnack(race, i) {        // 한 판에 한 번, 기운을 가득 채움. 기운이 많이 남아 있으면 넘치는 만큼 버려짐
    const p = race.poros[i];
    if (p.snacked) return { res: 'used', gain: 0 };
    const gain = Math.min(P.snack, P.energy.cap - p.e); p.e += gain; p.snacked = true; p.snackAt = race.t; p.snackGain = gain;
    return { res: gain >= P.snack * .8 ? 'ok' : gain >= P.snack * .4 ? 'half' : 'waste', gain };
  }
  const api = { P, STRAT, CIRCUITS: BUILT, rng, makeCourse, segAt, newRace, step, ranks, giveSnack };
  if (typeof module !== 'undefined') module.exports = api; else root.PoroEngine = api;
})(this);
