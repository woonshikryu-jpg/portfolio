// 포로 경주 엔진 — 시뮬레이션(node)과 프로토타입(브라우저)이 같은 파일을 씀
(function (root) {
  const P = {
    L: 1000, laps: 2, seg: 8, v0: 22, dt: 0.1,
    apt: 0.025,                // 적성: 맞는 구간 +2.5%, 안 맞는 구간 -2.5% (직진형·코너형 대칭)
    styles: {                  // 각질: 경주 진행도별 속도 배수
      '깡총': [[0, .35, 1.10], [.35, .75, 1.00], [.75, 1.01, 0.96]],
      '앞장': [[0, .35, 1.04], [.35, .75, 1.00], [.75, 1.01, 1.01]],
      '눈치': [[0, .35, 0.99], [.35, .75, 1.02], [.75, 1.01, 1.03]],
      '뒷심': [[0, .35, 0.94], [.35, .75, 1.00], [.75, 1.01, 1.16]]
    },
    stamina: 100, drain: 1.0, drainPow: 7, tiredMult: 0.84, snack: 25,
    slipP: 0.012, slipT: 1.2, slipMult: 0.3, accel: 0.22,   // 미끄러짐: 커브에서 초당 1.2%, 1.2초 동안 속도 30%(멈추지 않고 휘청) · 속도 변화는 부드럽게
    inside: 0.04, draft: 0.04, closerCurve: 0.92,   // 커브 인코스(1~3위 +4%) · 직선 바람막이(4위 아래 +4%) · 뒷심 막판 폭발은 커브에서 약함
    cheer: { minRank: 5, base: 0.045, cap: 2, mult: 1.22, t: 1.6, cd: 6 },
    form: 0.07, noise: 0.03
  };
  function rng(seed) { let s = (Math.imul(seed >>> 0 ^ 0x9E3779B9, 0x85EBCA6B) >>> 0) || 1; const f = () => { s ^= s << 13; s >>>= 0; s ^= s >> 17; s ^= s << 5; s >>>= 0; return s / 4294967296; }; for (let k = 0; k < 8; k++) f(); return f; }
  function makeCourse(curveRatio, R) {
    const n = P.seg, nc = Math.round(n * curveRatio);
    const kinds = Array(n - 1).fill('S');
    let c = 0; while (c < nc) { const i = Math.floor(R() * (n - 1)); if (kinds[i] === 'S') { kinds[i] = 'C'; c++; } }
    kinds.push('S');                           // 매 바퀴 마지막은 직선(홈 직선)
    return { curveRatio, kinds };
  }
  function segAt(course, d) { const x = d % P.L; return course.kinds[Math.min(P.seg - 1, Math.floor(x / (P.L / P.seg)))]; }
  function styleMult(st, p) { for (const [a, b, m] of P.styles[st]) if (p >= a && p < b) return m; return 1; }
  function newRace(entries, course, seed) {
    const R = rng(seed);
    return {
      R, course, t: 0, done: false, total: P.L * P.laps, finished: [],
      poros: entries.map((e, i) => ({ i, name: e.name, apt: e.apt, style: e.style, d: 0, st: P.stamina, tired: false, recovered: false,
        slip: 0, dash: 0, cd: 0, fin: null, v: 0, nz: 0, form: 1 + (R() * 2 - 1) * P.form, cheer: 0, tiredAt: null, snackOk: null, slips: 0, dashes: 0 }))
    };
  }
  function ranks(race) { return race.poros.slice().sort((a, b) => (a.fin ?? 1e9) - (b.fin ?? 1e9) || b.d - a.d); }
  // cheerShare: 포로별 최근 응원 비율 (합 1). 없으면 응원 없음
  function step(race, cheerShare) {
    const dt = P.dt, R = race.R, order = ranks(race);
    order.forEach((p, k) => p.rank = k + 1);
    const want = {};
    for (const p of race.poros) {
      if (p.fin !== null) continue;
      const prog = p.d / race.total, seg = segAt(race.course, p.d);
      p.nz += ((R() * 2 - 1) - p.nz) * .15;                       // 흔들림도 부드럽게(갑자기 튀지 않음)
      let m = styleMult(p.style, prog) * p.form * (1 + p.nz * P.noise * 2);
      m *= (p.apt === '직진') === (seg === 'S') ? 1 + P.apt : 1 - P.apt;
      if (p.style === '뒷심' && prog >= .75 && seg === 'C') m *= P.closerCurve;   // 뒷심의 막판 폭발은 직선에서
      if (seg === 'C' && p.rank <= 3) m *= 1 + P.inside;          // 커브: 앞쪽 포로가 인코스를 잡아 유리
      if (seg === 'S' && p.rank >= 4) m *= 1 + P.draft;           // 직선: 뒤쪽 포로가 바람을 피해 따라붙음
      if (p.tired) m *= P.tiredMult;
      // 응원: 5~8위일 때만 질주 확률
      if (p.cd > 0) p.cd -= dt;
      if (cheerShare && p.dash <= 0 && p.cd <= 0 && p.rank >= P.cheer.minRank) {
        const c = Math.min(P.cheer.cap, (cheerShare[p.i] || 0) * race.poros.length);
        if (R() < P.cheer.base * c * dt) { p.dash = P.cheer.t; p.cd = P.cheer.cd; p.dashes++; }
      }
      if (p.dash > 0) { m *= P.cheer.mult; p.dash -= dt; }
      // 미끄러짐: 커브에서 모두 같은 확률
      if (p.slip > 0) { p.slip -= dt; m *= P.slipMult; }
      else if (seg === 'C' && R() < P.slipP * dt) { p.slip = P.slipT; p.slips++; m *= P.slipMult; }
      const tv = P.v0 * m; p.v = race.t === 0 ? tv * .5 : p.v + (tv - p.v) * P.accel;   // 가속 · 감속을 부드럽게
      want[p.i] = p.v;
      // 스태미나
      if (!p.tired) { p.st -= P.drain * Math.pow(prog < .75 ? styleMult(p.style, prog) : 1, P.drainPow) * (p.dash > 0 ? 1.5 : 1) * dt; if (p.st <= 0) { p.tired = true; p.tiredAt = race.t; } }
    }
    for (const p of race.poros) {
      if (p.fin !== null) continue;
      p.d += want[p.i] * dt;
      if (p.d >= race.total) { p.d = race.total; p.fin = race.t + dt; race.finished.push(p.i); }
    }
    race.t += dt;
    if (race.finished.length === race.poros.length) race.done = true;
  }
  function giveSnack(race, i) {           // 포로당 한 판 1회 회복. 지쳤을 때만 효과, 아니면 효과 없음(느려지지 않음)
    const p = race.poros[i];
    if (p.tired && !p.recovered) { p.tired = false; p.recovered = true; p.st = P.snack; p.snackOk = race.t; return 'ok'; }
    return p.recovered ? 'used' : 'early';
  }
  const api = { P, rng, makeCourse, segAt, newRace, step, ranks, giveSnack, styleMult };
  if (typeof module !== 'undefined') module.exports = api; else root.PoroEngine = api;
})(this);
