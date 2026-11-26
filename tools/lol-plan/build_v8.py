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


# ---------- (2-c) 그림 + 항목이 짝인 장: 왼쪽 그림 고정, 오른쪽 항목 한 화면씩 ----------
def bal(t, a):
    d = 0
    for m in re.finditer(r'<div\b|</div>', t[a:]):
        d += 1 if m.group(0) == '<div' else -1
        if d == 0:
            return a + m.end()
def kids(block):
    inner_a = block.index('>') + 1; inner = block[inner_a:block.rindex('</div>')]
    out = []; k = 0
    while True:
        m = re.search(r'<div\b', inner[k:])
        if not m: break
        st = k + m.start(); en = bal(inner, st); out.append(inner[st:en]); k = en
    return out
def section(sid):
    i = s.index(f'id="{sid}"'); return s.rfind('<section', 0, i), s.index('</section>', i)
def story(vis, items, cls=''):
    st = ''.join(f'<div class="step" data-k="{j+1}">{it}</div>' for j, it in enumerate(items))
    return f'<div class="story {cls}" data-k="1"><div class="story-vis">{vis}</div><div class="story-steps">{st}</div></div>'
def grab(sec, start_pat):
    a = sec.index(start_pat); b = bal(sec, a); return a, b

for sid in ['plaza', 'poro', 'reward']:
    A, B = section(sid); sec = s[A:B]
    a, b = grab(sec, '<div class="split">'); ph, right = kids(sec[a:b]); items = kids(right)
    rest = sec[b:]
    if sid == 'reward':
        ma = rest.index('<div style="margin-top:18px"><div class="acc must">'); mb = bal(rest, ma)
        items.append(kids(rest[ma:mb])[0]); rest = rest[:ma] + rest[mb:]
    sec = sec[:a] + story(ph, items, 'pair') + rest
    s = s[:A] + sec + s[B:]

A, B = section('hide'); sec = s[A:B]
a, b = grab(sec, '<div class="split hide-top">'); left, mustwrap = kids(sec[a:b]); must = kids(mustwrap)[0]
ga, gb = grab(sec, '<div class="acc-grid">'); grid = kids(sec[ga:gb])
sec = sec[:a] + story(left, [must] + grid, 'pair') + sec[b:ga] + sec[gb:]
s = s[:A] + sec + s[B:]

A, B = section('season'); sec = s[A:B]
a, b = grab(sec, '<div class="flow4">'); cards = kids(sec[a:b])
ra, rb = grab(sec, '<div style="margin-top:28px"><div class="grid g3">'); rank = kids(sec[ra:rb])[0]
sec = sec[:ra] + sec[rb:]
sec = sec[:a] + story(rank, cards, 'pair season') + sec[b:]
s = s[:A] + sec + s[B:]

A, B = section('roadmap'); sec = s[A:B]
a, b = grab(sec, '<div class="steps">'); cards = kids(sec[a:b])
stair = '<div class="stair"><b data-k="1">1단계<span>클라이언트 광장</span></b><b data-k="2">2단계<span>광장 확장</span></b><b data-k="3">3단계<span>룬테라 여행</span></b></div>'
sec = sec[:a] + story(stair, cards, 'pair road') + sec[b:]
s = s[:A] + sec + s[B:]

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

.story.pair{grid-template-columns:1fr 1fr}
.story.pair .story-vis{height:70vh}
.story-vis>.ph{width:100%;height:100%;min-height:0!important}
.story-vis>div:not(.ph){width:100%}
.story.pair .step{min-height:40vh}
.story.pair .step>.acc,.story.pair .step>.card{width:100%}
.story.season .story-vis .grid{grid-template-columns:1fr;gap:10px}
.story.season .story-vis .card{flex-direction:row;align-items:center;gap:14px;padding:12px}
.story.season .story-vis .card .ph{min-height:90px!important;width:42%;flex:none}
.story.road .num{width:auto!important;height:auto!important;border-radius:999px!important;padding:7px 14px}
.stair{display:flex;flex-direction:column;gap:14px;width:100%}
.stair b{display:flex;justify-content:space-between;align-items:center;padding:22px 26px;border-radius:12px;border:1px solid #E6E8EB;background:rgba(255,255,255,.85);font:800 22px/1 'Pretendard Variable',Pretendard,sans-serif;color:#9AA1AA;transition:all .4s}
.stair b span{font:600 16px/1 'Pretendard Variable',Pretendard,sans-serif}
.stair b:nth-child(2){margin-left:12%}.stair b:nth-child(3){margin-left:24%}
.story.road[data-k="1"] .stair b[data-k="1"],.story.road[data-k="2"] .stair b[data-k="2"],.story.road[data-k="3"] .stair b[data-k="3"]{background:var(--accent);color:#fff;border-color:var(--accent)}
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
