# v122 -> v123: PART 05 확장 계획을 한 장에서 세 장으로 — 5-1 전설이 출전(출전표 예시 그림), 5-2 넘어가는 기준(지표 4개 + 그림), 5-3 MMO로 잇기(구상 그림 + 이어지는 것 + 누구에게 좋은가)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v122.html', encoding='utf-8').read()
s = s.replace('v122</title>', 'v123</title>')
a = s.index('<section class="r-shurima" id="roadmap">'); b = s.index('</section>', a) + len('</section>')
old = s[a:b]
# 기존 전설이 표(펼침) 재사용
ta = old.index('<table><tr><th style="width:22%">항목</th><th>내용</th></tr>'); tb = old.index('</table>', ta) + len('</table>')
legend_table = old[ta:tb]
K = lambda w: '<em class="kw kp5">%s</em>' % w
def head(no, h2):
    return '<div class="sec-head kp5"><div><div class="sec-no">%s</div><h2>%s</h2></div></div>' % (no, h2)
def fact(k, b_, sp):
    return '<div class="cs-fact"><span class="k">%s</span><b>%s</b><span>%s</span></div>' % (k, b_, sp)
def acc(title, summ, inner, open_=False):
    return ('<div class="acc"><button class="acc-btn" aria-expanded="%s"><span>%s<span class="sum">%s</span></span><span class="plus" aria-hidden="true">+</span></button>'
            '<div class="acc-body"><div><div class="acc-inner">%s</div></div></div></div>') % ('true' if open_ else 'false', title, summ, inner)
# 출전표 예시(HTML 그림)
rows = [('1','눈송이','기본','코너','깡총','9',''),('2','솜뭉치','기본','코너','앞장','7',''),('3','털보','기본','코너','눈치','6',''),
        ('4','전설이 · 유저 A','유저','코너','앞장','8',''),('5','전설이 · 유저 B','유저','코너','뒷심','5',''),
        ('6','전설이 · 유저 C','유저','직진','뒷심','4','solo'),('7','콩떡','기본','코너','눈치','6',''),('8','찹쌀','기본','코너','깡총','5','')]
tr = ''.join('<div class="rc-row%s"><span class="rc-n">%s</span><span class="rc-name">%s%s</span><span class="rc-t %s">%s</span><span class="rc-g">%s</span><span class="rc-p">%s명</span></div>'
             % (' solo' if f else '', n, nm, ' <i>유저 출전</i>' if who == '유저' else '', 'st' if t == '직진' else 'co', t, g, p, ) for n, nm, who, t, g, p, f in rows)
racecard = ('<div class="racecard"><div class="rc-top"><b>출전표 · 3경기</b><span>오늘의 코스 · 커브 많은 길</span></div>'
            '<div class="rc-course"><span class="cv" style="flex:7">커브 70%</span><span class="sr" style="flex:3">직선 30%</span></div>'
            '<div class="rc-row rc-h"><span>#</span><span>포로</span><span>적성</span><span>각질</span><span>고른 사람</span></div>' + tr +
            '<div class="rc-tip">6번만 직진형 → 직선 구간에서 속도 효과를 더 받음. 커브에서는 인코스로 버티고 직선에서 따라잡는다</div></div>')
sec1 = ('<section class="r-shurima" id="roadmap"><div class="wrap">'
  + head('PART 05 · 확장 계획', '롤 안에서 %s하고, MMO로 잇는다' % K('증명'))
  + '<div class="grid g3">'
  + '<div class="card"><span class="tag">먼저</span><h3>롤 안의 광장 모드</h3><p class="one">학회 본단 · 즉석 놀이 2종 · 숨바꼭질 정식 모드 · 시즌 학회 순위</p></div>'
  + '<div class="card"><span class="tag">넓히기</span><h3>포로 경주에 내 전설이</h3><p class="one">이미 산 TFT 외형이 광장을 달린다 (5-1)</p></div>'
  + '<div class="card tint"><span class="tag">다음</span><h3>라이엇 MMO로 잇기</h3><p class="one">지표가 좋아지면 (5-2) · 광장의 기록이 MMO로 (5-3)</p></div>'
  + '</div></div></section>')
sec2 = ('<section class="r-shurima alt" id="ext-legend"><div class="wrap">'
  + head('5-1 · 광장 안에서 넓히기', '내 %s가 포로 경주에 나간다' % K('전설이'))
  + '<div class="hs-map shot-row card"><figure class="shot">' + racecard + '<span class="shot-cap">출전표 예시 · 커브 많은 길에서 혼자 직진형을 고른 경우</span></figure>'
  + '<div class="hs-map-t t3">'
  + fact('출전', '8자리 중 3자리는 유저의 전설이', 'TFT에서 모은 전설이가 그대로 달립니다. 외형만 내 것이고 능력치는 모두 같습니다.')
  + fact('직접 고른다', '코스를 보고 적성 · 각질을 정한다', '같은 「커브 많은 길」을 보고도 유저마다 판단이 갈립니다.')
  + fact('빈틈 공략', '남과 다르게 고르면 더 빠르다', '같은 선택이 적을수록 효과가 조금 커집니다. 한도가 있어 무조건 이기지는 않습니다.')
  + '</div></div>'
  + acc('전설이 출전 규칙', '출전 · 선택 · 빈틈 공략 · 공정 · 주인 보상', legend_table)
  + '</div></section>')
sec3 = ('<section class="r-shurima" id="ext-gate"><div class="wrap">'
  + head('5-2 · 다음으로 넘어가는 기준', '숫자가 %s해야, 다음 문을 연다' % K('증명'))
  + '<div class="grid g4">'
  + '<div class="card"><span class="tag">지표 1</span><h3>주간 접속일</h3><p class="one">한 주에 며칠 들어오는가</p></div>'
  + '<div class="card"><span class="tag">지표 2</span><h3>스킨 구매 · 착용</h3><p class="one">광장에서 보이니 더 사고 더 끼는가</p></div>'
  + '<div class="card"><span class="tag">지표 3</span><h3>복귀 유저 재이탈</h3><p class="one">돌아온 유저가 다시 떠나지 않는가</p></div>'
  + '<div class="card"><span class="tag">지표 4</span><h3>광장만 쓰는 접속</h3><p class="one">협곡 없이 쉬다 가는 접속이 꾸준한가</p></div>'
  + '</div><div class="cs-band">광장을 쓴 그룹이 안 쓴 그룹보다 <em>넷 중 둘 이상</em>에서 나아지면, MMO 연결을 제안한다.</div>'
  + '<div style="margin-top:18px">' + acc('기준을 이렇게 정한 이유', '판 수가 아니라 머무는 것을 본다',
      '<ul><li><b>판 수는 보지 않는다</b>: 이 기획은 협곡을 덜 해도 손해가 없게 만드는 것이 목표라, 판 수가 줄어도 실패가 아닙니다(PART 06).</li>'
      '<li><b>광장만 쓰는 접속</b>은 광장이 쉬어 가는 곳으로 쓰이고 있다는 가장 직접적인 증거입니다.</li>'
      '<li><b>복귀 유저 재이탈</b>은 「돌아와도 격차 때문에 다시 떠난다」(1-1)는 문제가 풀렸는지를 봅니다.</li></ul>'
      '<span class="note">기준의 구체적인 목표치는 광장 모드 출시 전 데이터로 정합니다.</span>') + '</div>'
  + '</div></section>')
sec4 = ('<section class="r-shurima alt" id="ext-mmo"><div class="wrap">'
  + head('5-3 · MMO로 잇기', '광장에서 쌓은 것은, %s으로 넘어간다' % K('MMO'))
  + '<div class="hs-map shot-row card"><figure class="shot"><img src="img/lol/stage3.jpg" alt="MMO 속 소환사들의 도시를 그린 구상 이미지" loading="lazy"><span class="shot-cap">MMO 속 소환사들의 도시 · 구상 이미지</span></figure>'
  + '<div class="hs-map-t t3">'
  + fact('새로 만들지 않는다', '라이엇이 개발 중인 롤 MMO에 잇는다', 'MMO가 나올 때 쌓인 것을 넘겨주는 연결입니다.')
  + fact('학회 기록', '시즌 기록 → MMO 속 학회의 역사', '처음부터 함께한 학회의 우승 기록이 그대로 이어집니다.')
  + fact('본단 디자인', '광장의 본단 → MMO의 소환사들의 도시', '광장 모드에 만든 맵과 건물이 버려지지 않습니다.')
  + '</div></div>'
  + '<div class="grid g3">'
  + '<div class="card"><span class="tag">회사에게</span><h3>광장 비용 = MMO의 기반</h3><p class="one">한 번 만든 것을 두 번 쓴다</p></div>'
  + '<div class="card"><span class="tag">라이엇에게</span><h3>MMO 전까지 유저를 붙잡는다</h3><p class="one">MMO 수요도 미리 확인한다</p></div>'
  + '<div class="card"><span class="tag">유저에게</span><h3>내 학회가 MMO로</h3><p class="one">처음부터 함께한 소속이 이어진다</p></div>'
  + '</div></div></section>')
s = s[:a] + sec1 + sec2 + sec3 + sec4 + s[b:]
css = ('.grid.g3{grid-template-columns:repeat(3,minmax(0,1fr))}.grid.g4{grid-template-columns:repeat(4,minmax(0,1fr))}'
       '#ext-gate .cs-band em{font-style:normal;color:var(--kl,#0A9BFF)}#ext-gate .cs-band{--kl:#0A84E0}'
       ".racecard{width:100%;background:#FFFDF7;border:1.5px solid #E3D6B4;border-radius:14px;padding:14px;font:600 13.5px/1.35 'Pretendard Variable',Pretendard,'Noto Sans KR',sans-serif;color:#1F2328;box-sizing:border-box}"
       '.rc-top{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px}.rc-top b{font-size:15px}.rc-top span{color:#7A6A4A;font-size:12.5px}'
       '.rc-course{display:flex;height:22px;border-radius:6px;overflow:hidden;margin-bottom:10px;font:800 11.5px/22px sans-serif;color:#fff;text-align:center}'
       '.rc-course .cv{background:#2BA36B}.rc-course .sr{background:#E07A1F}'
       '.rc-row{display:grid;grid-template-columns:26px 1fr 54px 52px 64px;gap:6px;align-items:center;padding:6px 8px;border-radius:8px}'
       '.rc-row:nth-child(even){background:rgba(0,0,0,.025)}.rc-h{font-size:11.5px;color:#8A7A5A;background:none!important}'
       '.rc-n{font-weight:800;color:#8A7A5A}.rc-name i{font-style:normal;font-size:10.5px;color:#fff;background:#6C5CE7;border-radius:999px;padding:2px 6px;margin-left:4px}'
       '.rc-t{font-size:12px;font-weight:800;border-radius:999px;padding:3px 0;text-align:center}.rc-t.co{background:#DDF3E8;color:#1E7A50}.rc-t.st{background:#FFE7D1;color:#B85A0C}'
       '.rc-g{font-size:12.5px}.rc-p{font-size:12.5px;color:#6B7480;text-align:right}'
       '.rc-row.solo{background:#FFF1E2!important;outline:2px solid #E07A1F;outline-offset:-2px}'
       '.rc-tip{margin-top:10px;font-size:12.5px;color:#B85A0C;font-weight:700}'
       '@media(max-width:800px){.grid.g3,.grid.g4{grid-template-columns:1fr 1fr}}\n')
k = s.rindex('</style>'); s = s[:k] + css + s[k:]
s = s.replace('lol-plan-v122', 'lol-plan-v123')
open('versions/lol-plan-v123.html', 'w', encoding='utf-8').write(s)
print('ok')
