# v10 시안 = v9 + PART 02 이어지는 그림 제거 + 2-2 세계관 · 3-1 광장을 Crazy Splash 방식(질문 하나 → 연표/비교표/큰 카드)으로
# 사용: python3 tools/lol-plan/build_v8.py && python3 tools/lol-plan/build_v9.py && python3 tools/lol-plan/build_v10.py
import re

s = open('versions/lol-plan-v9.html', encoding='utf-8').read()
s = s.replace('기획서 v9', '기획서 v10')


def bal(t, a):
    d = 0
    for m in re.finditer(r'<div\b|</div>', t[a:]):
        d += 1 if m.group(0) == '<div' else -1
        if d == 0:
            return a + m.end()


def section(sid):
    i = s.index(f'id="{sid}"'); a = s.rfind('<section', 0, i); return a, s.index('</section>', i) + len('</section>')


def accs(block):
    out = []; k = 0
    while True:
        m = re.search(r'<div class="acc[ "]', block[k:])
        if not m: break
        st = k + m.start(); en = bal(block, st); out.append(block[st:en]); k = en
    return out


def body(acc):
    m = re.search(r'<div class="acc-inner[^"]*">([\s\S]*)</div></div></div>\s*</div>$', acc)
    return m.group(1) if m else ''


# ---------- 1. PART 02: 이어지는 두 번째 그림 빼기 ----------
s = s.replace('<img src="img/lol/ionia-rest2.jpg" alt="쉼터 오른쪽으로 이어지는 폭포 절벽과 정자">', '', 1)
s = s.replace("var pan=sc.querySelector('.pan');if(pan){", "var pan=null;if(pan){", 1)
s = s.replace('<div class="pan">', '<div class="pan one">', 1)
a = s.index('data-mode="frame"'); a = s.rfind('<div class="scene', 0, a)
hd = s[a:s.index('>', a)]
s = s[:a] + re.sub(r'style="height:\d+vh"', 'style="height:380vh"', hd) + s[a + len(hd):]

# PART 02 장면: 제목 뒤 카메라 추가 이동(버벅임 원인) 제거 — 들어간 뒤엔 멈춘 채 제목만
a = s.index('data-mode="frame"'); a = s.rfind('<div class="scene', 0, a); b = bal(s, a)
sc = s[a:b]
sc = re.sub(r"data-keys='[^']*'", "data-keys='" + '[{"p":0,"x":50,"y":50,"s":0},{"p":0.1,"x":50,"y":50,"s":0},{"p":0.38,"x":50,"y":46,"s":1.06},{"p":1,"x":50,"y":46,"s":1.06}]' + "'", sc, count=1)
sc = re.sub(r'(<div class="mark[^"]*"[^>]*data-from=")[\d.]+(" data-to=")[\d.]+(")', r'\g<1>0.42\g<2>0.92\3', sc, count=1)
s = s[:a] + sc + s[b:]

# ---------- PART 01 사막: 빛 대신 하단에 모래먼지가 바람에 날림 ----------
a = s.index('data-mode="sweep"'); a = s.rfind('<div class="scene', 0, a)
st = s.index('<div class="sticky">', a) + len('<div class="sticky">')
s = s[:st] + '<canvas class="dust" aria-hidden="true"></canvas><div class="haze" aria-hidden="true"></div>' + s[st:]

# ---------- 2. 2-2 세계관 (Crazy Splash 01 '기획 배경' 방식: 연표 + 큰 카드) ----------
A, B = section('academy'); old = s[A:B]
oa = accs(old)
why_world = [x for x in oa if '왜 세계관을' in x][0]
rule = [x for x in oa if '학회 소속 규칙' in x][0]
academy = f'''<section class="cs" id="academy">
  <div class="wrap">
    <div class="sec-head">
      <div><div class="sec-no">2-2 · 세계관</div><h2>전쟁의 학회가 사라진 뒤,<br>소환사들은 숨어 살았다</h2></div>
      <p>롤의 옛 설정을 이어받아, 협곡에서 싸울 이유를 다시 만듭니다.</p>
    </div>
    <div class="cs-two">
      <ol class="cs-tl">
        <li><span class="when">초창기 롤 설정</span><b>전쟁의 학회</b><span class="what">나라끼리 전쟁 대신, 소환사의 협곡 대결로 분쟁을 정했다</span></li>
        <li><span class="when">2014년 무렵</span><b>공식 설정에서 삭제</b><span class="what">"협곡에서 왜 싸우는가"가 비어 버렸다</span></li>
        <li class="mine"><span class="when">이 기획</span><b>소환사들은 도시에 숨어 산다</b><span class="what">신들처럼 몰래 섞여 산다 · 주민은 정체를 모른다 · 버려진 본단에서 다시 모인다</span></li>
        <li class="mine"><span class="when">그래서</span><b>숨은 학회가 협곡에서 겨룬다</b><span class="what">이긴 학회의 도시가 시즌의 주인공이 된다</span></li>
      </ol>
      <div class="cs-side">
        <div class="cs-punch"><span class="k">이길 이유</span><b>내 한 판 = <em>우리 도시의 승부</em></b><span>월드컵처럼, 직접 뛰지 않는 날에도 응원할 이유</span></div>
        <div class="cs-quote"><b>플레이어 = 소환사</b><span>롤은 원래 플레이어를 '소환사'라고 부릅니다. 여기에 몸(광장의 아바타)과 소속(학회)만 붙입니다.</span></div>
      </div>
    </div>
    <h3 class="cs-sub">시즌마다 사는 도시를 고르면, 그 도시의 학회원이 된다</h3>
    <div class="cs-cities">
      <figure><img src="img/lol/demacia-hq.jpg" alt="데마시아"><figcaption><b>데마시아 학회</b>흰 석회암 · 푸른 깃발</figcaption></figure>
      <figure><img src="img/lol/noxus-city-hq.jpg" alt="녹서스"><figcaption><b>녹서스 학회</b>붉은 깃발 · 데마시아의 맞수</figcaption></figure>
      <figure><img src="img/lol/piltover-hq.jpg" alt="필트오버"><figcaption><b>필트오버 학회</b>황동 · 톱니 · 발명</figcaption></figure>
    </div>
    <h3 class="cs-sub">모두가 모이는 곳, 숨겨진 전쟁의 학회 본단</h3>
    <div class="cs-hq">
      <div class="cs-hq-box"><div class="cs-hq-img" data-v="0"><img src="img/lol/hq.jpg" alt="덩굴과 안개에 덮인 채 다시 사람이 모이기 시작한 전쟁의 학회 본단 안뜰"><img class="win" src="img/lol/hq-demacia.jpg" alt="데마시아 학회가 우승한 시즌, 푸른 깃발과 흰 백합으로 꾸며진 본단 안뜰"></div>
        <div class="cs-hq-tabs"><button class="on" data-v="0">평소의 본단</button><button data-v="1">데마시아 우승 시즌</button></div></div>
      <div class="cs-hq-txt">
        <p>전쟁의 학회는 사라졌지만, 본단 건물은 남았습니다. 안개 낀 골짜기 깊은 곳, 주민들은 오래된 유적이라고만 알고 있는 곳입니다.</p>
        <p>숨어 살던 소환사들은 이곳에서 다시 모입니다. 1단계에서 클라이언트를 켜면 처음 보이는 광장이 바로 <b>본단의 안뜰</b>입니다.</p>
        <div class="cs-punch small"><span class="k">시즌 보상이 눈에 보이는 곳</span><b>지난 시즌 우승 학회가 <em>본단을 자기 도시 양식으로</em> 꾸민다</b><span>데마시아가 이기면 흰 석회암과 푸른 깃발, 녹서스가 이기면 붉은 깃발과 철 장식. 모든 소환사가 다음 시즌 내내 그 모습을 봅니다.</span></div>
      </div>
    </div>
    <p class="cs-line">공식 이야기는 하나도 바꾸지 않고 → <em>그 옆에 숨은 소환사와 그들의 본단만 더한다</em></p>
    <div style="margin-top:18px">{why_world}{rule}</div>
  </div>
</section>'''
s = s[:A] + academy + s[B:]

# ---------- 2-2 · 왜 지금인가 (따로 강조, 본문은 tools/lol-plan/whynow.html) ----------
A, B = section('loop'); lp = s[A:B]
for x in accs(lp):
    if '왜 지금인가' in x:
        lp = lp.replace(x, '')
why = open('tools/lol-plan/whynow.html', encoding='utf-8').read()
s = s[:A] + lp + why + s[B:]
s = s.replace('<div class="sec-no">2-2 · 세계관</div>', '<div class="sec-no">2-3 · 세계관</div>', 1)

# ---------- PART 05 확장: 왼쪽 계단 대신 단계별 실제 화면 ----------
st_old = re.search(r'<div class="stair">.*?</div>', s, re.S).group(0)
def stg(k, f, alt, cap):
    return ('<div class="wv stg" data-k="%d"><figure class="stage-shot"><div class="ss-img"><img src="img/lol/%s" alt="%s" '
            'onerror="this.parentNode.classList.add(\'empty\')"><span class="ph-t">%s 화면 자리</span></div>'
            '<figcaption>%s</figcaption></figure></div>') % (k, f, alt, cap.split(' · ')[0], cap)
st_new = ('<div class="wall-vis">'
          + stg(1, 'stage1.jpg', '본단 안뜰을 걷는 소환사의 3인칭 화면', '1단계 · 본단 안뜰')
          + stg(2, 'stage2.jpg', '넓어진 본단에서 함께 경기를 보는 소환사들', '2단계 · 넓어진 본단')
          + stg(3, 'stage3.jpg', '필트오버 거리를 직접 걷는 소환사의 3인칭 화면', '3단계 · 룬테라 여행 · 필트오버를 걷는 소환사')
          + '</div>')
s = s.replace(st_old, st_new, 1)

s = s.replace('<h3>클라이언트 광장</h3><p class="one">학회 광장 · 순위 변화 · 캐주얼</p>', '<h3>본단 안뜰</h3><p class="one">클라이언트 첫 화면 · 우승 학회 장식 · 캐주얼 모드</p>', 1)
s = s.replace('<h3>광장 확장</h3><p class="one">경기 같이 보기 · 숨은 소환사 찾기</p>', '<h3>넓어진 본단</h3><p class="one">함께 경기 보기 · 숨은 소환사 찾기 · 학회별 별관</p>', 1)
s = s.replace('<h3>룬테라 여행</h3><p class="one">3인칭 도시 · 포탈 여행</p>', '<h3>룬테라 여행</h3><p class="one">본단 포탈을 지나 학회의 도시를 직접 걷는다</p>', 1)

# ---------- 3. 3-1 광장 (Crazy Splash 03 '원작 계승' 방식: 지금 vs 이 기획 비교표, 줄을 누르면 이유) ----------
A, B = section('plaza'); old = s[A:B]
pa = accs(old)
b1, b2, b3, b4 = [body(x) for x in pa[:4]]
bview = body(pa[4]) if len(pa) > 4 else ''
rows = [
    ('첫 화면', '메뉴 버튼이 늘어선 화면', '본단 안뜰 · 우승 학회 양식으로 꾸며짐', b1),
    ('큐 대기', '타이머만 보며 기다린다', '광장을 걸으며 기다린다', b2),
    ('친구', '목록 속 이름 한 줄', '광장에 서 있는 소환사 · 클릭하면 파티', b3),
    ('출전', '수락 → 로딩 화면', '포탈로 걸어 들어가면 카메라가 하늘로', b4),
    ('귀환', '결과 화면 → 메뉴', '내 소환사 곁으로 · 기여가 쌓이는 연출', bview),
]
rh = ''.join(f'''<div class="cmp-row"><button aria-expanded="false"><span class="c0">{a}</span><span class="c1">{b}</span><span class="c2">{c}</span><span class="pl">+</span></button><div class="cmp-body"><div><div class="cmp-in">{d}</div></div></div></div>''' for a, b, c, d in rows)
plaza = f'''<section class="cs" id="plaza">
  <div class="wrap">
    <div class="sec-head">
      <div><div class="sec-no">3-1 · 학회 광장</div><h2>메뉴 화면 대신, 소환사들이 모이는 본단</h2></div>
      <p>1단계의 광장은 전쟁의 학회 본단 안뜰입니다. 클라이언트에서 하던 일은 그대로, 하는 장소만 이곳으로 옮깁니다. 줄을 누르면 설계가 열립니다.</p>
    </div>
    <div class="cmp">
      <div class="cmp-head"><span></span><span>지금 롤 클라이언트</span><span>학회 광장</span><span></span></div>
      {rh}
    </div>
    <div class="cs-band">새로 배울 것은 없습니다. 기다리던 시간이 <em>쉬는 시간</em>이 됩니다.</div>
  </div>
</section>'''
s = s[:A] + plaza + s[B:]

css = '''
/* ===== v10: Crazy Splash 방식 설명 ===== */
.story.road .wv{position:absolute}
.story.road[data-k="1"] .wv[data-k="1"],.story.road[data-k="2"] .wv[data-k="2"],.story.road[data-k="3"] .wv[data-k="3"]{opacity:1;transform:none}
.stage-shot{margin:0;width:100%}
.ss-img{position:relative;border-radius:16px;overflow:hidden;aspect-ratio:16/9;background:#F2F3F5;box-shadow:0 20px 44px rgba(17,20,24,.2)}
.ss-img img{display:block;width:100%;height:100%;object-fit:cover}
.ss-img .ph-t{display:none}
.ss-img.empty{border:1.5px dashed #C9CED4;box-shadow:none}
.ss-img.empty img{display:none}
.ss-img.empty .ph-t{display:grid;position:absolute;inset:0;place-items:center;font:600 14px 'Pretendard Variable',Pretendard,sans-serif;color:#8A929C}
.stage-shot figcaption{margin-top:10px;font:700 14px/1.4 'Pretendard Variable',Pretendard,sans-serif;color:#3A424C;text-align:center}

.ex section.cs.cs-tint{background:#F3F7F1!important}
#whynow .why-hero{margin:6px 0 28px}
#whynow .why-hero .to{font-size:76px}
#whynow .why3{gap:16px}
#whynow .wc{background:#fff!important;padding:24px 20px;gap:8px}
#whynow .wc .lab{font:700 13px/1.3 'Pretendard Variable',Pretendard,sans-serif;color:#8A929C}
#whynow .wc b{font-size:44px}
#whynow .wc .what{font:800 17px/1.4 'Pretendard Variable',Pretendard,sans-serif;color:#111418}
#whynow .wc em{font-size:15.5px}
#whynow .wc.hot{background:#1F3A5F!important;border-color:#1F3A5F}
#whynow .wc.hot .lab{color:#A9C4E8}
#whynow .wc.hot b{color:#fff}
#whynow .wc.hot .what{color:#FFE08A}
#whynow .wc.hot em{color:#fff;border-top-color:rgba(255,255,255,.25)}
#whynow .wc.hot em::before{color:#FFE08A}
#whynow .src{margin-top:12px;text-align:right;font:500 12.5px/1.4 'Pretendard Variable',Pretendard,sans-serif;color:#8A929C}

/* PART 01 모래바람 */
.scene[data-mode="sweep"] .fx-light,.scene[data-mode="sweep"] .fx-shade{display:none!important}
.scene[data-mode="sweep"] .world .mark{z-index:4}
.dust{position:absolute;inset:0;width:100%;height:100%;z-index:3;pointer-events:none}
.haze{position:absolute;left:0;right:0;bottom:0;height:46%;z-index:2;pointer-events:none;
  background:repeating-linear-gradient(100deg,rgba(225,196,150,0) 0 120px,rgba(225,196,150,.3) 190px,rgba(225,196,150,0) 300px),linear-gradient(0deg,rgba(214,182,132,.55),rgba(214,182,132,0));
  background-size:600px 100%,100% 100%;animation:hazeMove 9s linear infinite}
@keyframes hazeMove{from{background-position:0 0,0 0}to{background-position:600px 0,0 0}}
/* 머무는 고리 도식 크게 */
.story:has(svg.loop){grid-template-columns:1.9fr 1fr!important;gap:28px;width:min(1340px,calc(100vw - 200px));margin-left:calc(50% - min(1340px,calc(100vw - 200px))/2 + 40px)}
.story:has(svg.loop) .story-vis{height:84vh;top:8vh;display:flex;align-items:center}
.story:has(svg.loop) .story-vis svg.loop{width:100%!important;max-width:none!important;height:auto}
.story svg.loop .node text{font-size:23px!important}
.story svg.loop .node text.s{font-size:16px!important}
.story svg.loop text.mid{font-size:22px!important}
.story svg.loop .imm text{font-size:18px!important}
.story:not([data-k="0"]) svg.loop .node{opacity:.72!important}


.cs-hq-box{display:flex;flex-direction:column;gap:12px}
.cs-hq-img .win{position:absolute;inset:0;opacity:0;transition:opacity .8s ease}
.cs-hq-img[data-v="1"] .win{opacity:1}
.cs-hq-tabs{display:flex;gap:8px}
.cs-hq-tabs button{flex:1;padding:11px 14px;border-radius:999px;border:1.5px solid #E6E8EB;background:#fff;cursor:pointer;font:700 14.5px/1 'Pretendard Variable',Pretendard,sans-serif;color:#5B6470;transition:all .25s}
.cs-hq-tabs button.on{background:#2C55A8;border-color:#2C55A8;color:#fff}
.cs-hq-tabs button:first-child.on{background:#3A424C;border-color:#3A424C}
.cs-hq{display:grid;grid-template-columns:1.35fr 1fr;gap:26px;align-items:center}
.cs-hq-img{position:relative;border-radius:18px;overflow:hidden;aspect-ratio:16/9;background:#F2F3F5;border:1.5px solid #E6E8EB}
.cs-hq-img img{display:block;width:100%;height:100%;object-fit:cover}
.cs-hq-img .ph-t{display:none}
.cs-hq-img.empty img{display:none}
.cs-hq-img.empty{border-style:dashed;display:grid;place-items:center}
.cs-hq-img.empty .ph-t{display:block;font:600 14px 'Pretendard Variable',Pretendard,sans-serif;color:#8A929C}
.cs-hq-txt p{font:500 16px/1.75 'Pretendard Variable',Pretendard,sans-serif;color:#2A3038;margin:0 0 10px}
.cs-hq-txt p b{color:#111418;font-weight:800}
.cs-punch.small{margin-top:14px;padding:18px 20px}
.cs-punch.small b{font-size:21px}
@media(max-width:900px){.cs-hq{grid-template-columns:1fr}}

.pan.one img{transform:none!important}
.ex section.cs{position:relative;z-index:1;background:#fff!important;padding:96px 0}
.ex section.cs+section{border-top:0}
.cs .sec-head h2{font-size:clamp(30px,4vw,44px)!important}
.cs-two{display:grid;grid-template-columns:1.15fr 1fr;gap:28px;align-items:start}
.cs-tl{list-style:none;margin:0;padding:0;position:relative}
.cs-tl::before{content:'';position:absolute;left:11px;top:12px;bottom:12px;width:3px;background:#E6E8EB;border-radius:3px}
.cs-tl li{position:relative;padding:0 0 24px 44px;display:flex;flex-direction:column;gap:3px}
.cs-tl li::before{content:'';position:absolute;left:2px;top:4px;width:21px;height:21px;border-radius:50%;background:#fff;border:4px solid #B9C0C8;box-sizing:border-box}
.cs-tl li.mine::before{border-color:var(--accent);background:color-mix(in srgb,var(--accent) 20%,#fff)}
.cs-tl .when{font:700 13px/1.3 'Pretendard Variable',Pretendard,sans-serif;color:#8A929C}
.cs-tl li.mine .when{color:var(--accent)}
.cs-tl b{font:800 21px/1.35 'Pretendard Variable',Pretendard,sans-serif;color:#111418}
.cs-tl .what{font:500 15px/1.55 'Pretendard Variable',Pretendard,sans-serif;color:#5B6470}
.cs-side{display:flex;flex-direction:column;gap:14px}
.cs-punch{border:1.5px solid #E6E8EB;border-radius:18px;padding:24px 26px;display:flex;flex-direction:column;gap:6px;box-shadow:0 10px 26px rgba(17,20,24,.06)}
.cs-punch .k{font:700 13px/1 'Pretendard Variable',Pretendard,sans-serif;color:#8A929C}
.cs-punch b{font:900 28px/1.3 'Pretendard Variable',Pretendard,sans-serif;color:#111418;letter-spacing:-.02em}
.cs-punch b em{font-style:normal;color:#C2412D}
.cs-punch>span:last-child{font:500 14.5px/1.5 'Pretendard Variable',Pretendard,sans-serif;color:#5B6470}
.cs-quote{background:var(--accent);color:#fff;border-radius:18px;padding:22px 26px;display:flex;flex-direction:column;gap:6px}
.cs-quote b{font:800 22px/1.3 'Pretendard Variable',Pretendard,sans-serif}
.cs-quote span{font:500 14.5px/1.6 'Pretendard Variable',Pretendard,sans-serif;opacity:.92}
.cs-sub{font:800 22px/1.35 'Pretendard Variable',Pretendard,sans-serif;color:#111418;margin:44px 0 14px}
.cs-cities{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.cs-cities figure{margin:0;border-radius:16px;overflow:hidden;border:1.5px solid #E6E8EB;background:#fff}
.cs-cities img{display:block;width:100%;height:170px;object-fit:cover}
.cs-cities figcaption{padding:14px 16px;font:500 14px/1.5 'Pretendard Variable',Pretendard,sans-serif;color:#5B6470}
.cs-cities figcaption b{display:block;font:800 17px/1.3 'Pretendard Variable',Pretendard,sans-serif;color:#111418;margin-bottom:2px}
.cs-line{margin:24px 0 0;font:800 20px/1.5 'Pretendard Variable',Pretendard,sans-serif;color:#111418}
.cs-line em,.cs-band em{font-style:normal;color:var(--accent);background:linear-gradient(transparent 62%,color-mix(in srgb,var(--accent) 18%,#fff) 62%)}
.cmp{border-radius:20px;overflow:hidden;border:1.5px solid #E6E8EB;background:#fff}
.cmp-head,.cmp-row>button{display:grid;grid-template-columns:110px 1fr 1.2fr 40px;align-items:center;gap:12px;padding:17px 22px;text-align:left}
.cmp-head{background:#111418;color:#fff;font:700 14px/1.3 'Pretendard Variable',Pretendard,sans-serif}
.cmp-head span:nth-child(3){color:#F2CF84}
.cmp-row{border-top:1px solid #E6E8EB}
.cmp-row>button{width:100%;background:#fff;border:0;cursor:pointer;font:500 15.5px/1.5 'Pretendard Variable',Pretendard,sans-serif;color:#5B6470}
.cmp-row>button:hover{background:#F7F8FA}
.cmp-row .c0{font-weight:800;color:var(--accent)}
.cmp-row .c2{font-weight:800;color:#111418}
.cmp-row .pl{width:28px;height:28px;border-radius:50%;border:1.5px solid #E6E8EB;display:grid;place-items:center;color:var(--accent);font-weight:800;transition:transform .3s}
.cmp-row>button[aria-expanded="true"] .pl{transform:rotate(45deg);background:var(--accent);color:#fff;border-color:var(--accent)}
.cmp-body{display:grid;grid-template-rows:0fr;transition:grid-template-rows .45s ease}
.cmp-body>div{overflow:hidden}
.cmp-row>button[aria-expanded="true"]+.cmp-body{grid-template-rows:1fr}
.cmp-in{padding:4px 22px 22px 144px;font:15px/1.75 'Pretendard Variable',Pretendard,sans-serif;color:#2A3038}
.cmp-in ul{margin:0;padding-left:18px}
.cs-band{margin-top:22px;border-radius:14px;padding:18px 24px;background:#FFF4CC;font:800 19px/1.5 'Pretendard Variable',Pretendard,sans-serif;color:#111418}
@media(max-width:900px){.cs-two,.cs-cities{grid-template-columns:1fr}.cmp-head{display:none}.cmp-row>button{grid-template-columns:1fr 32px}.cmp-row .c0,.cmp-row .c1{grid-column:1}.cmp-in{padding-left:22px}}
'''
j = s.rindex('</style>'); s = s[:j] + css + s[j:]
js = r'''
  // 모래바람
  document.querySelectorAll('.scene[data-mode=sweep] canvas.dust').forEach(function(cv){
    var cx=cv.getContext('2d'),P=[],dpr=Math.min(2,devicePixelRatio||1);
    function rs(){cv.width=cv.clientWidth*dpr;cv.height=cv.clientHeight*dpr}rs();addEventListener('resize',rs);
    for(var i=0;i<280;i++)P.push({x:Math.random(),y:.45+Math.random()*.55,v:.0012+Math.random()*.003,r:.7+Math.random()*2.2,a:.3+Math.random()*.5,w:Math.random()*6.28,l:Math.random()<.25});
    (function f(){var r=cv.getBoundingClientRect();if(r.bottom>0&&r.top<innerHeight){var W=cv.width,H=cv.height;cx.clearRect(0,0,W,H);
      P.forEach(function(p){p.x+=p.v;p.w+=.02;if(p.x>1.05){p.x=-.05;p.y=.5+Math.random()*.5}var y=(p.y+Math.sin(p.w)*.012)*H,x=p.x*W;
        if(p.l){cx.strokeStyle='rgba(232,206,160,'+p.a*.6+')';cx.lineWidth=p.r*dpr*.6;cx.beginPath();cx.moveTo(x,y);cx.lineTo(x-38*dpr*p.v*400,y+2*dpr);cx.stroke()}
        else{cx.fillStyle='rgba(236,212,170,'+p.a+')';cx.beginPath();cx.arc(x,y,p.r*dpr,0,7);cx.fill()}})}
      requestAnimationFrame(f)})();
  });

  document.querySelectorAll('.cs-hq-tabs button').forEach(function(b){b.addEventListener('click',function(){var box=b.closest('.cs-hq-box');box.querySelector('.cs-hq-img').setAttribute('data-v',b.dataset.v);box.querySelectorAll('.cs-hq-tabs button').forEach(function(x){x.classList.toggle('on',x===b)})})});
  document.querySelectorAll('.cmp-row>button').forEach(function(b){b.addEventListener('click',function(){b.setAttribute('aria-expanded',b.getAttribute('aria-expanded')==='true'?'false':'true')})});
'''
k = s.rindex('})();'); s = s[:k] + js + s[k:]
open('versions/lol-plan-v10.html', 'w', encoding='utf-8').write(s)
print('ok')
