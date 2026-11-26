# v8 = v7 + (1) 장면 그림이 설명 뒤에 계속 남음 (2) 순서가 있는 내용은 한 화면 한 생각(스크롤 이야기)
# 사용: python3 tools/lol-plan/build_v8.py   (versions/lol-plan-v7.html -> versions/lol-plan-v8.html)
import re

s = open('versions/lol-plan-v7.html', encoding='utf-8').read()
s = s.replace('기획서 v7', '기획서 v8')

# ---------- (1) 장면 그림을 설명 뒤 배경으로 ----------
BG = {'summary': 'cover-hq.jpg', 'loop': 'ionia-rest.jpg', 'academy': 'noxus-city-hq.jpg', 'build': 'harbor-hq.jpg',
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

# ---------- 포로 경주 장면: 줄무늬 빼고, 동그랗게 열리는(아이리스) 연출 + 글이 통 튀어나옴 ----------
s = s.replace('    <div class="race-lines"></div>\n', '', 1)
s = s.replace('<div class="mark scene-cap" style="left:30%;top:40%', '<div class="mark scene-cap pop" style="left:30%;top:40%', 1)
old = "if(mode==='race'){var r1=ease(Math.min(1,p/0.32));var ri=sc.querySelector('.race-img');ri.style.transform='translateX('+((1-r1)*100)+'%)';ri.style.filter='blur('+((1-r1)*8)+'px)';sc.querySelector('.race-lines').style.opacity=(1-r1)*.9;marks(sc,p);return}"
assert old in s
s = s.replace(old, "if(mode==='race'){var r1=ease(Math.min(1,p/0.38));var ri=sc.querySelector('.race-img');ri.style.clipPath='circle('+(4+r1*78)+'% at 52% 58%)';ri.querySelector('img').style.transform='scale('+(1.18-0.18*r1)+')';marks(sc,p);return}")

# ---------- PART 01: 제목은 사막 장면, 네 벽은 다음 화면에서 '왼쪽 그림 고정 · 오른쪽 글' ----------
a = s.index('data-mode="sweep"'); a = s.rfind('<div class="scene', 0, a); b = s.index('<div class="hall">', a)
B = s[a:b]
w2 = B.index('    <div class="world world2"'); end = B.rindex('    </div>\n  </div>\n</div>')
walls_html = B[w2:end]
B = B[:w2] + B[end:]
B = B.replace('<img src="img/lol/d1-hq.jpg" alt="정오의 슈리마 사구">\n', '<img src="img/lol/d1-hq.jpg" alt="정오의 슈리마 사구">\n      <div class="fx fx-shade"></div>\n      <div class="fx fx-light"></div>\n', 1)
B = B.replace('style="height:780vh"', 'style="height:240vh"', 1).replace('data-from="0.0" data-to="0.14"', 'data-from="0.0" data-to="1.0"', 1)
def wall(h3):
    i = walls_html.index(f'<h3>{h3}</h3>'); j = walls_html.index('</div>\n      </div>', i)
    return walls_html[i:j]
shot = re.search(r'<figure class="real-shot">[\s\S]*?</figure>', walls_html).group(0)
vis = ('<div class="wall-vis">'
       '<div class="wv" data-k="1"><figure class="illu"><img src="img/lol/fatigue.jpg" alt="늦은 밤 퇴근 복장 그대로 모니터 앞에 웅크려 게임하는 사람"></figure></div>'
       '<div class="wv" data-k="2"><figure class="real-shot"><img src="img/lol/patch-notes.png" alt="실제 LoL 26.23 패치 노트 — 챔피언 수치 변경 목록"><figcaption>실제 패치 노트 · 26.23 · 2주마다 이만큼씩</figcaption></figure></div>'
       '<div class="wv" data-k="3"><figure class="real-shot"><img src="img/lol/solokill.jpg" alt="실제 LoL 게임 화면 — 시작 2분 43초, 라인전에서 상대 다리우스에게 솔킬당해 회색 화면으로 부활을 기다리는 모습"><figcaption>실제 게임 화면 · 2분 43초 · 라인전 솔킬 → <b>부활 대기</b></figcaption></figure></div>'
       f'<div class="wv" data-k="4">{shot}</div>'
       '<div class="wv" data-k="5"><div class="q-big">?</div></div>'
       '</div>')
items = [wall('한 판의 피로'), wall('패치 공부'), wall('복귀 격차'), wall('남는 건 점수뿐'),
         '<span class="pn">핵심 질문</span><h2>한 판을 하지 않아도<br>머물 이유가 있는 LoL은 가능할까?</h2><p>경쟁은 협곡에 → 쉼과 기록은 그 바깥에</p>']
steps = ''.join(f'<div class="step" data-k="{k+1}"><div class="wtxt">{t}</div></div>' for k, t in enumerate(items))
walls_sec = ('<div class="ex r-shurima walls-ex"><div class="ex-bg" aria-hidden="true"><img src="img/lol/noxus-hq.jpg" alt=""></div>'
             '<section class="r-shurima" id="walls"><div class="wrap">'
             '<div class="sec-head"><div><div class="sec-no">1-1 · 네 개의 벽</div><h2>왜 남는 게 없을까</h2></div><p>이겨도 져도 점수 하나. 그 앞에 놓인 네 개의 벽.</p></div>'
             f'<div class="story pair walls" data-k="1"><div class="story-vis">{vis}</div><div class="story-steps">{steps}</div></div>'
             '</div></section></div>\n')
s = s[:a] + B + walls_sec + s[b:]

# ---------- 진행 표시 목차 (오른쪽 가장자리) ----------
rail = ('<nav class="rail" aria-label="목차"><b class="rail-t">PART</b><div class="rail-line"><i></i></div>'
        + ''.join(f'<a href="#" data-go="{sel}"><span><em>{name.split(" ",1)[0]}</em><i>{name.split(" ",1)[1]}</i></span></a>' for sel, name in [
            ('.scene[data-mode=sweep]', '01 문제 정의'),
            ('.scene[data-mode=frame]', '02 핵심 콘셉트'),
            ('.scene[data-mode=harbor]', '03 1단계 설계'),
            ('.scene[data-mode=snow]', '04 캐주얼 모드와 하루'),
            ('.scene[data-mode=dawn]', '05 단계별 확장'),
            ('#feasible', '06 실행 가능성'),
            ('#compare', '07 결론')])
        + '</nav>')
_k = s.rindex('<script>'); s = s[:_k] + rail + '\n' + s[_k:]

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

/* 포로 경주: 아이리스 + 통 튀는 글 */
.scene[data-mode="race"] .sticky{background:radial-gradient(ellipse at 50% 60%,#FFFFFF,#E8F0F8)}
.race-img img{transition:none;will-change:transform}
.mark.pop{transform:translate(-50%,-50%) scale(.55);transition:opacity .35s ease,transform .75s cubic-bezier(.34,1.9,.5,1)}
.mark.pop.on{transform:translate(-50%,-50%) scale(1)}

/* 떠오르는 상세가 아래 칸 뒤로 숨지 않게 */
.ex .acc.peek{z-index:60!important}
.ex .step:has(.acc.peek),.ex .story:has(.acc.peek){position:relative;z-index:60}
.ex .acc.peek .acc-btn[aria-expanded="false"]+.acc-body{background:#fff!important;backdrop-filter:none}

/* PART 01 네 벽 스크롤 이야기 */
.wall-vis{position:relative;width:100%;height:100%}
.wv{position:absolute;inset:0;display:grid;place-items:center;opacity:0;transform:translateY(16px) scale(.98);transition:opacity .55s ease,transform .55s ease}
.story.walls[data-k="1"] .wv[data-k="1"],.story.walls[data-k="2"] .wv[data-k="2"],.story.walls[data-k="3"] .wv[data-k="3"],.story.walls[data-k="4"] .wv[data-k="4"],.story.walls[data-k="5"] .wv[data-k="5"]{opacity:1;transform:none}
.wv .ph{width:100%;height:78%}
.wv .real-shot{width:96%;max-width:640px;margin:0;transform:rotate(-1.2deg);background:#fff;padding:8px 8px 6px;border-radius:8px;box-shadow:0 22px 44px rgba(17,20,24,.22)}
.wv .real-shot img{display:block;width:100%;border-radius:4px}
.wv .real-shot figcaption{font:600 13px/1.6 'Pretendard Variable',Pretendard,sans-serif;color:#3A424C;padding-top:6px;text-align:center}
.wv .real-shot figcaption b{color:#B3322A}
.wv .illu{width:100%;margin:0;border-radius:14px;overflow:hidden;box-shadow:0 22px 44px rgba(17,20,24,.22)}
.wv .illu img{display:block;width:100%}
.q-big{font:900 220px/1 'Pretendard Variable',Pretendard,sans-serif;color:var(--accent);opacity:.18}
.wtxt h3{font:800 34px/1.25 'Pretendard Variable',Pretendard,sans-serif;color:#111418;letter-spacing:-.02em}
.wtxt h2{font:800 34px/1.35 'Pretendard Variable',Pretendard,sans-serif;color:#111418;letter-spacing:-.02em;margin-top:8px}
.wtxt p{font:600 17px/1.6 'Pretendard Variable',Pretendard,sans-serif;color:#3A424C;margin-top:10px}
.wtxt .pn{font:700 13px/1.2 'Pretendard Variable',Pretendard,sans-serif;letter-spacing:.06em;color:var(--accent)}
.wtxt .feel{font:800 22px/1.45 'Pretendard Variable',Pretendard,sans-serif;color:var(--accent);margin-top:16px}
.wtxt .ev{display:inline-block;margin-top:14px;font:600 13.5px/1.4 'Pretendard Variable',Pretendard,sans-serif;color:#5B6470;background:rgba(255,255,255,.85);border:1px solid #E6E8EB;border-radius:999px;padding:6px 12px}

/* 진행 표시 목차 */
.rail{position:fixed;left:18px;top:50%;transform:translateY(-50%);z-index:90;display:flex;flex-direction:column;gap:22px;padding:10px 6px;opacity:.35;transition:opacity .4s}
.rail.lit,.rail:hover{opacity:1}
.rail-line{position:absolute;left:11px;top:14px;bottom:14px;width:2px;background:rgba(255,255,255,.55);box-shadow:0 0 0 1px rgba(0,0,0,.08);border-radius:2px;overflow:hidden}
.rail-line i{position:absolute;left:0;right:0;top:0;height:var(--fill,0%);background:#C9A24E}
.rail a{position:relative;display:block;width:12px;height:12px;margin-left:6px;border-radius:50%;background:rgba(255,255,255,.9);border:2px solid rgba(60,50,40,.35);box-sizing:border-box;transition:transform .3s,background .3s,border-color .3s}
.rail a.on{background:#C9A24E;border-color:#fff;transform:scale(1.35)}
.rail a span{position:absolute;left:22px;top:50%;transform:translate(-6px,-50%);white-space:nowrap;font:700 12.5px/1 'Pretendard Variable',Pretendard,'Noto Sans KR',sans-serif;color:#fff;background:rgba(30,26,22,.78);padding:7px 10px;border-radius:999px;opacity:0;pointer-events:none;transition:opacity .25s,transform .25s}
.rail:hover a span,.rail a:focus-visible span{opacity:1;transform:translate(0,-50%)}
.rail a.on span{background:#8A5A1E}
@media(max-width:700px){.rail{left:6px}.rail a span{display:none}}

/* 목차 이름 항상 보이기 */
.rail{opacity:.9!important;gap:20px}
.rail-t{font:800 11px/1 'Pretendard Variable',Pretendard,sans-serif;letter-spacing:.14em;color:#fff;text-shadow:0 1px 3px rgba(0,0,0,.6);margin:0 0 -4px 2px}
.rail-line{top:34px!important;left:17px!important;width:2px}
.rail a{margin-left:6px!important;width:12px;height:12px}
.rail a.on{transform:scale(1.25)!important;transform-origin:center}
.rail a span{opacity:1!important;transform:translate(0,-50%)!important;background:rgba(30,26,22,.55);font-size:11.5px;padding:5px 9px}
.rail a.on span{background:#8A5A1E}
.rail a.on{transform:scale(1.2)}
.rail a.on span{transform:translate(0,-50%) scale(.84)!important;transform-origin:left center}

/* 평소엔 번호만, 올리거나 누르면 이름 */
.rail a span em{font-style:normal}
.rail a span i{font-style:normal;display:inline-block;max-width:0;overflow:hidden;white-space:nowrap;vertical-align:bottom;opacity:0;transition:max-width .3s ease,opacity .25s ease,margin .3s}
.rail a:hover span i,.rail a.open span i,.rail a:focus-visible span i{max-width:160px;opacity:1;margin-left:5px}
@media(max-width:900px){.story{grid-template-columns:1fr}.story-vis{position:relative;top:0;height:auto}.step{min-height:auto;padding:18px 0;opacity:1;transform:none}.story.day .q{position:static;opacity:1;transform:none;font-size:22px}}
'''
j = s.rindex('</style>'); s = s[:j] + css + s[j:]

js2 = r'''
  // 진행 표시 목차
  (function(){
    var rail=document.querySelector('.rail'); if(!rail)return;
    var links=[].slice.call(rail.querySelectorAll('a')),tg=links.map(function(a){return document.querySelector(a.dataset.go)});
    links.forEach(function(a,i){a.addEventListener('click',function(e){e.preventDefault();a.classList.add('open');clearTimeout(a._t);a._t=setTimeout(function(){a.classList.remove('open')},2500);if(tg[i])scrollTo({top:tg[i].getBoundingClientRect().top+scrollY,behavior:'smooth'})})});
    function upd(){var y=scrollY+innerHeight*.4,cur=-1;tg.forEach(function(t,i){if(t&&t.getBoundingClientRect().top+scrollY<=y)cur=i});
      links.forEach(function(a,i){a.classList.toggle('on',i===cur)});
      var h=document.documentElement.scrollHeight-innerHeight;rail.style.setProperty('--fill',(h>0?scrollY/h*100:0)+'%');
      var inEx=document.elementFromPoint(innerWidth/2,innerHeight/2);rail.classList.toggle('lit',!!(inEx&&inEx.closest&&inEx.closest('.ex')))}
    addEventListener('scroll',upd,{passive:true});addEventListener('resize',upd);upd();
  })();
'''
js = '''
  // 스크롤 이야기: 매 스크롤마다 '화면 가운데에 가장 가까운 칸'을 계산 (건너뜀·늦은 반응 없음)
  (function(){
    var stories=[].slice.call(document.querySelectorAll('.story')),ticking=false;
    function upd(){ticking=false;var line=innerHeight*.5;
      stories.forEach(function(st){var steps=st.querySelectorAll('.step'),k=0;
        var best=1e9;for(var i=0;i<steps.length;i++){var r=steps[i].getBoundingClientRect(),d=Math.abs(r.top+r.height/2-line);if(d<best){best=d;k=i}}
        var cur=st.getAttribute('data-k');if(cur!==String(k+1)){st.setAttribute('data-k',k+1);for(var j=0;j<steps.length;j++)steps[j].classList.toggle('on',j===k)}})}
    function req(){if(!ticking){ticking=true;requestAnimationFrame(upd)}}
    addEventListener('scroll',req,{passive:true});addEventListener('resize',req);
    stories.forEach(function(st){var f=st.querySelector('.step');if(f)f.classList.add('on')});upd();
  })();
'''
k = s.rindex('})();'); s = s[:k] + js + js2 + s[k:]
open('versions/lol-plan-v8.html', 'w', encoding='utf-8').write(s)
print('ok')
