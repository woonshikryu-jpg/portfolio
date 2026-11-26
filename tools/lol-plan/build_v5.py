import re, os
os.chdir('/home/claude/portfolio/versions')
p4 = open('lol-plan-proto4.html').read()
v3 = open('lol-plan-v3.html').read()
scene_css = re.search(r'<style>(.*?)</style>', p4, re.S).group(1)

byid = {}
for s in re.findall(r'(<section[^>]*>.*?</section>)', v3, re.S):
    tag = re.match(r'<section[^>]*>', s).group(0)
    m = re.search(r'id="([^"]*)"', tag)
    key = m.group(1) if m else ('problem' if '네 개의 벽' in s else 'concept' if '한 문장 콘셉트' in s else 'overview' if '3-0 · 개요' in s else '?')
    byid[key] = s

byid['academy'] = re.sub(r'<div class="grid g3">.*?<p class="small">이미지 출처: Riot Games</p>', '', byid['academy'], count=1, flags=re.S)
byid['poro'] = byid['poro'].replace('<div class="shot"><img src="img/lol/poro.jpg" alt="눈밭 위의 포로들"><p class="small">이미지 출처: Riot Games · 관전 화면 목업은 추후 교체</p></div>', '<div class="ph">관전 화면 목업 자리<br>트랙을 달리는 포로들 + 응원 · 예측 UI</div>')
def S(k): return byid[k]

expl_css = open('tools/lol-plan/expl.css').read()

def grab(pat):
    m = re.search(pat, p4, re.S)
    assert m, pat
    return m.group(1)

mist = grab(r'(<!-- 1 · 안개가 걷힘 -->.*?<div class="hint">스크롤 ↓</div>\n  </div>\n</div>\n)')
sweep = grab(r'(<!-- 2 · 햇빛이 훑고 지나감 -->.*?\n</div>\n)\n<!-- 기록관 복도 -->')
frame = grab(r'(<!-- 3 · 액자 속으로 -->.*?\n</div>\n)\n<div class="spacer">')
frame = re.sub(r'\s*<div class="mark inside" style="left:62%;top:80%[^>]*>\s*<button class="rune"[^\n]*\n\s*</div>', '', frame)
snow = grab(r'(<!-- 4 · 눈이 내리고 글이 서리처럼 -->.*?<canvas class="snow"></canvas>\n  </div>\n</div>\n)')
dawn = grab(r'(<!-- 5 · 해가 떠오름 -->.*?\n</div>\n)\n<div class="end">')
dawn = re.sub(r'\s*<div class="mark" style="left:53%;top:74%[^>]*>\s*<button class="rune"[^\n]*\n\s*</div>', '', dawn)

body = f'''<a class="back" href="index.html">← 버전 모음</a>
<span class="credit" style="position:fixed">이미지 출처: Riot Games</span>
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><filter id="ripple"><feTurbulence id="turb" type="fractalNoise" baseFrequency="0.008 0.05" numOctaves="2" seed="4"/><feDisplacementMap id="disp" in="SourceGraphic" in2="turb" scale="0"/></filter></svg>

{mist}
<div class="ex r-ionia">{S('summary')}</div>

{sweep}
<div class="hall"><p>숨은 소환사들의 학회 기록관<br><span>벽에 걸린 그림은 룬테라 각 지역으로 통하는 문입니다</span></p></div>

{frame}
<div class="ex r-ionia">{S('concept')}{S('world')}</div>

<!-- 학회 · 세 개의 문 -->
<div class="scene" data-mode="doors" style="height:300vh">
  <div class="sticky">
    <div class="doors">
      <div class="door" data-at="0.25"><img src="img/lol/demacia-hq.jpg" alt="데마시아 왕궁 전경"><div class="carve"><span class="pn">데마시아 학회</span><h3>흰 석회암 · 푸른 깃발</h3></div></div>
      <div class="door" data-at="0.45"><img src="img/lol/noxus-hq.jpg" alt="녹서스의 붉은 차양 시장"><div class="carve"><span class="pn">녹서스 학회</span><h3>붉은 깃발 · 데마시아의 맞수</h3></div></div>
      <div class="door" data-at="0.65"><img src="img/lol/piltover-hq.jpg" alt="필트오버 거리"><div class="carve"><span class="pn">필트오버 학회</span><h3>황동 · 톱니 · 발명</h3></div></div>
    </div>
    <div class="doors-title"><div class="carve"><span class="pn">2-3 · 학회</span><h2>거주 도시 = 학회 = 세력</h2><p>문을 열면, 그 도시의 학회원이 된다</p></div></div>
  </div>
</div>
<div class="ex r-ionia">{S('academy')}{S('view')}</div>

<!-- PART 03 · 데마시아 항구 (수면에 비친 글) -->
<div class="scene" data-mode="harbor" data-w="1000" data-h="562" style="height:360vh">
  <div class="sticky wall">
    <div class="harbor-frame">
      <img src="img/lol/harbor-hq.jpg" alt="데마시아 항구와 푸른 돛의 함대">
      <div class="mark ripple" style="left:50%;top:72%;font-size:var(--u)" data-from="0.18" data-to="0.42">
        <div class="carve"><span class="pn">PART 03 · 데마시아 항구</span><h2>사람이 모이는 항구</h2><p>1단계 · 학회 광장과 세력 시즌</p></div>
      </div>
      <div class="mark ripple" style="left:50%;top:72%;font-size:var(--u)" data-from="0.46" data-to="0.7">
        <div class="carve"><h2>새 게임이 아니라,<br>지금 클라이언트 위에</h2></div>
      </div>
      <div class="mark ripple" style="left:50%;top:72%;font-size:var(--u)" data-from="0.74" data-to="1">
        <div class="carve"><h2>첫 화면이<br>내가 사는 도시의 광장</h2></div>
      </div>
    </div>
  </div>
</div>
<div class="ex r-demacia">{S('overview')}{S('plaza')}{S('season')}{S('rank')}{S('reward')}</div>

{snow}
<div class="ex r-frel">{S('casual')}{S('hide')}</div>

<!-- 포로 경주 · 달려 들어옴 -->
<div class="scene" data-mode="race" style="height:260vh">
  <div class="sticky">
    <div class="race-img"><img src="img/lol/poro-hq.jpg" alt="눈밭 위의 포로들"></div>
    <div class="race-lines"></div>
    <div class="mark scene-cap" style="left:30%;top:40%;font-size:clamp(13px,1.5vw,24px)" data-from="0.45" data-to="1">
      <div class="carve ice"><span class="pn">3-7 · 관전형 모드</span><h2>포로 경주</h2><p>응원만 해도 한 판</p></div>
    </div>
  </div>
</div>
<div class="ex r-frel">{S('poro')}{S('day')}</div>

{dawn}
<div class="ex r-shurima">{S('roadmap')}{S('carry')}{S('bm')}{S('kpi')}{S('risk')}{S('compare')}</div>

<!-- 결말 · 뒤로 멀어짐 -->
<div class="scene still" data-mode="pull" data-w="2334" data-h="1080" style="height:260vh">
  <div class="sticky">
    <div class="world">
      <img src="img/lol/ionia-hq.jpg" alt="안개 낀 아이오니아 절벽 도시">
      <div class="mark" style="left:30%;top:26%;font-size:calc(var(--u) * 1.1)" data-from="0.4" data-to="1">
        <div class="carve"><span class="pn">HIDDEN SUMMONERS</span><h2>한 판의 승부가,<br>내가 사는 도시의 풍경이 된다.</h2><p>유운식 · 게임 기획</p></div>
      </div>
    </div>
  </div>
</div>
<div class="end">본 기획서는 라이엇 게임즈와 무관한 개인 기획안이며, 수록된 룬테라 이미지의 저작권은 Riot Games에 있습니다.</div>
'''
body = body.replace('<span class="credit">이미지 출처: Riot Games</span>\n', '')

js = grab(r'(<script>.*?</script>)')
def rep(a, b):
    global js
    assert a in js, a[:60]
    js = js.replace(a, b)
rep("    var k=Math.max(vw/iw,vh/ih),w=iw*k,h=ih*k;",
    "    if(sc.dataset.mode==='doors'||sc.dataset.mode==='race'){sc._w=vw;sc._h=vh;return}\n"
    "    if(sc.dataset.mode==='harbor'){var fw=Math.min(vw*.78,iw,vh*.74*iw/ih),fh=fw*ih/iw;var hf=sc.querySelector('.harbor-frame');hf.style.width=fw+'px';hf.style.height=fh+'px';hf.style.marginLeft=(-fw/2)+'px';hf.style.marginTop=(-fh/2)+'px';hf.style.setProperty('--u',(fh/562*14)+'px');sc._w=fw;return}\n"
    "    var k=Math.max(vw/iw,vh/ih),w=iw*k,h=ih*k;")
rep("    var vw=innerWidth,vh=innerHeight,world=sc.querySelector('.world'),mode=sc.dataset.mode;",
    "    var vw=innerWidth,vh=innerHeight,world=sc.querySelector('.world'),mode=sc.dataset.mode;\n"
    "    if(mode==='doors'){sc.querySelectorAll('.door').forEach(function(d){d.classList.toggle('open',p>=+d.dataset.at)});sc.querySelector('.doors-title').style.opacity=p<0.2?1:0;return}\n"
    "    if(mode==='harbor'){var g2=ease(Math.min(1,p/0.3)),s2=0.72+0.28*g2;sc.querySelector('.harbor-frame').style.transform='scale('+s2+')';marks(sc,p);return}\n"
    "    if(mode==='race'){var r1=ease(Math.min(1,p/0.32));var ri=sc.querySelector('.race-img');ri.style.transform='translateX('+((1-r1)*100)+'%)';ri.style.filter='blur('+((1-r1)*8)+'px)';sc.querySelector('.race-lines').style.opacity=(1-r1)*.9;marks(sc,p);return}")
rep("    if(mode==='dawn'){",
    "    if(mode==='pull'){var pz=ease(Math.min(1,p/0.6)),zs=1.16-0.16*pz;world.style.transformOrigin='50% 50%';world.style.transform='translate('+(vw-sc._w)/2+'px,'+(vh-sc._h)/2+'px) scale('+zs+')';}\n    if(mode==='dawn'){")
rep("  function marks(sc,p){sc.querySelectorAll('.mark').forEach(function(m){var v=p>=+m.dataset.from&&p<=+m.dataset.to;if(m.classList.contains('inside'))v=v&&sc._inside;m.classList.toggle('on',v)})}",
    "  var rippleT=0,disp=document.getElementById('disp'),turb=document.getElementById('turb');\n"
    "  function rip(){var t=(performance.now()-rippleT)/1800;if(t>1){disp.setAttribute('scale',0);return}var k=Math.pow(1-t,2);disp.setAttribute('scale',(36*k).toFixed(2));turb.setAttribute('baseFrequency',(0.008+0.004*Math.sin(t*9)).toFixed(4)+' 0.05');requestAnimationFrame(rip)}\n"
    "  function marks(sc,p){sc.querySelectorAll('.mark').forEach(function(m){var v=p>=+m.dataset.from&&p<=+m.dataset.to;if(m.classList.contains('inside'))v=v&&sc._inside;if(v&&!m.classList.contains('on')&&m.classList.contains('ripple')){rippleT=performance.now();rip()}m.classList.toggle('on',v)})}")
rep("document.querySelectorAll('[data-open]')",
    "document.querySelectorAll('.acc-btn').forEach(function(b){b.addEventListener('click',function(){b.setAttribute('aria-expanded',b.getAttribute('aria-expanded')==='true'?'false':'true')})});\n  document.querySelectorAll('[data-open]')")

head = p4[:p4.index('<style>')].replace('시안 4 (장면마다 다른 효과)', '기획서 v5 (판타지 연출 + 설명)')
html = head + '<style>' + scene_css + expl_css + '</style>\n</head>\n<body>\n' + body + js + '\n</body>\n</html>\n'
open('lol-plan-v5.html', 'w').write(html)
print(len(html), html.count('class="scene'), html.count('class="acc-btn"'))
