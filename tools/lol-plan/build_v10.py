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
        <li class="mine"><span class="when">이 기획</span><b>소환사들은 도시에 숨어 산다</b><span class="what">신들처럼 몰래 섞여 산다 · 주민은 정체를 모른다</span></li>
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
    <p class="cs-line">공식 이야기는 하나도 바꾸지 않고 → <em>그 옆에 숨은 소환사만 더한다</em></p>
    <div style="margin-top:18px">{why_world}{rule}</div>
  </div>
</section>'''
s = s[:A] + academy + s[B:]

# ---------- 3. 3-1 광장 (Crazy Splash 03 '원작 계승' 방식: 지금 vs 이 기획 비교표, 줄을 누르면 이유) ----------
A, B = section('plaza'); old = s[A:B]
pa = accs(old)
b1, b2, b3, b4 = [body(x) for x in pa[:4]]
bview = body(pa[4]) if len(pa) > 4 else ''
rows = [
    ('첫 화면', '메뉴 버튼이 늘어선 화면', '내가 사는 도시의 광장', b1),
    ('큐 대기', '타이머만 보며 기다린다', '광장을 걸으며 기다린다', b2),
    ('친구', '목록 속 이름 한 줄', '광장에 서 있는 소환사 · 클릭하면 파티', b3),
    ('출전', '수락 → 로딩 화면', '포탈로 걸어 들어가면 카메라가 하늘로', b4),
    ('귀환', '결과 화면 → 메뉴', '내 소환사 곁으로 · 기여가 쌓이는 연출', bview),
]
rh = ''.join(f'''<div class="cmp-row"><button aria-expanded="false"><span class="c0">{a}</span><span class="c1">{b}</span><span class="c2">{c}</span><span class="pl">+</span></button><div class="cmp-body"><div><div class="cmp-in">{d}</div></div></div></div>''' for a, b, c, d in rows)
plaza = f'''<section class="cs" id="plaza">
  <div class="wrap">
    <div class="sec-head">
      <div><div class="sec-no">3-1 · 학회 광장</div><h2>메뉴 화면 대신, 내가 사는 도시의 광장</h2></div>
      <p>지금 클라이언트에서 하던 일은 그대로. 하는 장소만 광장으로 옮깁니다. 줄을 누르면 설계가 열립니다.</p>
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
js = '''
  document.querySelectorAll('.cmp-row>button').forEach(function(b){b.addEventListener('click',function(){b.setAttribute('aria-expanded',b.getAttribute('aria-expanded')==='true'?'false':'true')})});
'''
k = s.rindex('})();'); s = s[:k] + js + s[k:]
open('versions/lol-plan-v10.html', 'w', encoding='utf-8').write(s)
print('ok')
