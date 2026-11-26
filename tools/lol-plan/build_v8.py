# v8 = v7 + (1) 장면 그림이 설명 뒤에 계속 남음 (2) 순서가 있는 내용은 한 화면 한 생각(스크롤 이야기)
# 사용: python3 tools/lol-plan/build_v8.py   (versions/lol-plan-v7.html -> versions/lol-plan-v8.html)
import re

s = open('versions/lol-plan-v7.html', encoding='utf-8').read()
s = s.replace('기획서 v7', '기획서 v8')

# ---------- (1) 장면 그림을 설명 뒤 배경으로 ----------
BG = {'summary': 'cover-hq.jpg', 'loop': 'd2-hq.jpg', 'academy': 'noxus-city-hq.jpg', 'build': 'harbor-hq.jpg',
      'hide': 'd4-hq.jpg', 'poro': 'poro-hq.jpg', 'roadmap': 'd5-hq.jpg'}
out = []; k = 0
for m in re.finditer(r'<div class="ex ([a-z-]+)">', s):
    sid = re.search(r'id="([a-z]+)"', s[m.end():m.end() + 300]).group(1)
    out.append((m.end(), BG[sid]))
for pos, img in reversed(out):
    s = s[:pos] + f'<div class="ex-bg" aria-hidden="true"><img src="img/lol/{img}" alt=""></div>' + s[pos:]

# ---------- (2-a) 머무는 고리: 왼쪽 고리 고정 + 오른쪽 한 단계씩 ----------
i = s.index('id="loop"')
a = s.index('<div class="loop-wrap">', i)
d = 0
for t in re.finditer(r'<div\b|</div>', s[a:]):
    d += 1 if t.group(0) == '<div' else -1
    if d == 0:
        b = a + t.end(); break
lw = s[a:b]
svg = re.search(r'<svg class="loop"[\s\S]*?</svg>', lw).group(0)
n = [0]
def tag(m):
    n[0] += 1
    return f'<g class="node n{n[0]}">'
svg = re.sub(r'<g class="node">', tag, svg)
steps = [
    ('1', '① 광장에 접속', '큐를 돌려 놓고 광장을 걷습니다. 친구가 저기 서 있습니다.', '메뉴 화면 대신, 사람이 있는 장소에서 시작한다.'),
    ('2', '② 한 판 — A', '포탈에 들어서면 카메라가 하늘로 솟습니다. 이제 지휘할 시간.', '로딩 화면이 "역할이 바뀌었다"는 신호가 된다.'),
    ('3', '③ 학회 기여 — B', '이겨도 져도, 내 이름이 우리 도시의 승부에 더해집니다.', '직접 뛰지 않는 날에도 결과가 궁금해진다.'),
    ('4', '④ 광장이 바뀐다 — C', '다음 주 접속하면, 광장의 깃발이 한 칸 바뀌어 있습니다.', '점수 대신 풍경이 결과를 보여 준다 → 다시 ①로.'),
]
st = ''.join(f'<div class="step" data-k="{k}"><span class="sk">{h}</span><p class="sl">{l}</p><p class="sm">{m}</p></div>' for k, h, l, m in steps)
story = f'<div class="story" data-k="1"><div class="story-vis">{svg}</div><div class="story-steps">{st}</div></div>'
s = s[:a] + story + s[b:]

# ---------- (2-b) 한 소환사의 하루: 왼쪽 큰 속마음 + 오른쪽 행동 ----------
i = s.index('id="day"')
a = s.index('<div class="timeline">', i)
d = 0
for t in re.finditer(r'<div\b|</div>', s[a:]):
    d += 1 if t.group(0) == '<div' else -1
    if d == 0:
        b = a + t.end(); break
tl = s[a:b]
rows = re.findall(r'<div class="tl"><b>(.*?)</b><span>(.*?)</span><span class="f">(.*?)</span></div>', tl)
quotes = ''.join(f'<p class="q" data-k="{j+1}">{f}</p>' for j, (_, _, f) in enumerate(rows))
st = ''.join(f'<div class="step" data-k="{j+1}"><span class="sk">{j+1:02d} · {b_}</span><p class="sl">{sp}</p></div>' for j, (b_, sp, _) in enumerate(rows))
story = f'<div class="story day" data-k="1"><div class="story-vis"><div class="quotes">{quotes}</div></div><div class="story-steps">{st}</div></div>'
s = s[:a] + story + s[b:]

css = '''
/* ===== v8 ===== */
/* (1) 장면 그림이 설명 뒤에 남는다 */
.ex{position:relative;isolation:isolate}
.ex-bg{position:sticky;top:0;height:100vh;margin-bottom:-100vh;z-index:-1;overflow:hidden;pointer-events:none}
.ex-bg img{width:100%;height:100%;object-fit:cover;filter:blur(14px) saturate(1.05);transform:scale(1.08)}
.ex-bg::after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(255,255,255,.58),rgba(255,255,255,.74) 40%,rgba(255,255,255,.80))}
.ex section,.ex section.alt,.ex section:nth-of-type(even){background:transparent!important}
.ex .card,.ex .acc,.ex table,.ex .timeline,.ex .chip,.ex .wc{background:rgba(255,255,255,.9)!important;backdrop-filter:blur(6px)}
.ex .ph{background:rgba(255,255,255,.55);border-color:rgba(120,130,140,.45)}
.ex section+section{border-top:1px solid rgba(17,20,24,.06)}
/* (2) 한 화면 한 생각 */
.story{display:grid;grid-template-columns:1.25fr 1fr;gap:40px;align-items:start}
.story-vis{position:sticky;top:12vh;height:76vh;display:grid;place-items:center}
.story-steps{padding:16vh 0 26vh}
.step{min-height:46vh;display:flex;flex-direction:column;justify-content:center;opacity:.28;transition:opacity .5s ease,transform .5s ease;transform:translateX(8px)}
.step.on{opacity:1;transform:none}
.step .sk{font:700 13px/1.2 'Pretendard Variable',Pretendard,sans-serif;letter-spacing:.06em;color:var(--accent)}
.step .sl{font:800 26px/1.45 'Pretendard Variable',Pretendard,sans-serif;color:#111418;letter-spacing:-.02em;margin-top:10px}
.step .sm{font:500 16px/1.6 'Pretendard Variable',Pretendard,sans-serif;color:#5B6470;margin-top:10px}
.story svg.loop{width:100%}
.story svg.loop .node rect{transition:fill .4s,stroke .4s,stroke-width .4s}
.story svg.loop .node{transition:opacity .4s}
.story:not([data-k="0"]) svg.loop .node{opacity:.4}
.story[data-k="1"] .n1,.story[data-k="2"] .n2,.story[data-k="3"] .n3,.story[data-k="4"] .n4{opacity:1!important}
.story[data-k="1"] .n1 rect,.story[data-k="2"] .n2 rect,.story[data-k="3"] .n3 rect,.story[data-k="4"] .n4 rect{stroke:var(--accent)!important;stroke-width:3!important;fill:color-mix(in srgb,var(--accent) 8%,#fff)!important}
.story.day .quotes{position:relative;width:100%;height:100%}
.story.day .q{position:absolute;inset:0;display:grid;place-items:center;text-align:center;margin:0;font:800 clamp(30px,3.4vw,46px)/1.35 'Pretendard Variable',Pretendard,sans-serif;color:var(--accent);letter-spacing:-.03em;opacity:0;transform:translateY(14px);transition:opacity .6s,transform .6s}
.story.day[data-k="1"] .q[data-k="1"],.story.day[data-k="2"] .q[data-k="2"],.story.day[data-k="3"] .q[data-k="3"],.story.day[data-k="4"] .q[data-k="4"],.story.day[data-k="5"] .q[data-k="5"],.story.day[data-k="6"] .q[data-k="6"]{opacity:1;transform:none}
@media(max-width:900px){.story{grid-template-columns:1fr}.story-vis{position:relative;top:0;height:auto}.step{min-height:auto;padding:18px 0;opacity:1;transform:none}.story.day .q{position:static;opacity:1;transform:none;font-size:22px}}
'''
j = s.rindex('</style>'); s = s[:j] + css + s[j:]

js = '''
  // v8: 스크롤 이야기 — 화면 가운데 온 단계를 켠다
  document.querySelectorAll('.story').forEach(function(st){
    var steps=[].slice.call(st.querySelectorAll('.step'));
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){steps.forEach(function(x){x.classList.toggle('on',x===e.target)});st.setAttribute('data-k',e.target.getAttribute('data-k'))}})},{rootMargin:'-45% 0px -45% 0px'});
    steps.forEach(function(x){io.observe(x)});
  });
'''
k = s.rindex('})();'); s = s[:k] + js + s[k:]
open('versions/lol-plan-v8.html', 'w', encoding='utf-8').write(s)
print('ok')
