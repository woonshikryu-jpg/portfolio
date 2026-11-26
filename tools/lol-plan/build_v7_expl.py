# v7 설명 부분 재구성: 20장 -> 13장, 빠진 6가지 흡수, 필수 상세만 펼침
# 사용: python3 tools/lol-plan/build_v7_expl.py  (versions/lol-plan-v7.html 을 제자리에서 고침, 한 번만 실행)
import re, sys

P = 'versions/lol-plan-v7.html'
s = open(P, encoding='utf-8').read()
if 'id="loop"' in s:
    sys.exit('already applied')


def sec(marker):
    i = s.index(marker)
    a = s.rfind('<section', 0, i)
    b = s.index('</section>', i) + len('</section>')
    return a, b


def accs(block):
    """block 안의 .acc 덩어리들을 순서대로 돌려준다 (div 짝 맞추기)."""
    out = []
    for m in re.finditer(r'<div class="acc[ "]', block):
        i = m.start(); depth = 0; j = i
        for t in re.finditer(r'<div\b|</div>', block[i:]):
            depth += 1 if t.group(0) == '<div' else -1
            if depth == 0:
                j = i + t.end(); break
        out.append(block[i:j])
    # 바깥 것만 (안쪽 중복 제거)
    res = []
    for a in out:
        if not any(a != b and a in b for b in out):
            res.append(a)
    return res


def must(acc):
    acc = acc.replace('<div class="acc">', '<div class="acc must">', 1)
    return acc.replace('aria-expanded="false"', 'aria-expanded="true"', 1)


def replace_sec(marker, new):
    global s
    a, b = sec(marker)
    s = s[:a] + new + s[b:]


def get(marker):
    a, b = sec(marker)
    return s[a:b]


def acc_html(title, summary, inner, n=None, essential=False):
    nn = f'<span class="n">{n}</span>' if n else ''
    exp = 'true' if essential else 'false'
    cls = 'acc must' if essential else 'acc'
    return (f'<div class="{cls}"><button class="acc-btn" aria-expanded="{exp}">{nn}<span>{title}'
            f'<span class="sum">{summary}</span></span><span class="plus" aria-hidden="true">+</span></button>'
            f'<div class="acc-body"><div><div class="acc-inner">{inner}</div></div></div></div>')


# ---------- 원래 조각 모으기 ----------
world = get('id="world"'); world_accs = accs(world)
academy = get('id="academy"'); academy_accs = accs(academy)
view = get('id="view"'); view_accs = accs(view)
season = get('id="season"'); season_accs = accs(season)
rank = get('id="rank"'); rank_accs = accs(rank)
casual = get('id="casual"'); casual_accs = accs(casual)
roadmap = get('id="roadmap"')
carry = get('id="carry"')
bm = get('id="bm"'); bm_accs = accs(bm)
kpi = get('id="kpi"'); kpi_accs = accs(kpi)
risk = get('id="risk"')
kpi_table = re.search(r'<table>[\s\S]*?</table>', kpi).group(0)
risk_table = re.search(r'<table>[\s\S]*?</table>', risk).group(0)
world_cards = re.search(r'<div class="grid g2">[\s\S]*?</div>\s*</div>', world).group(0)
rank_grid = re.search(r'<div class="grid g3">[\s\S]*?</div>\s*</div>', rank).group(0)
season_flow = re.search(r'<div class="flow4">[\s\S]*?</div>\s*</div>', season).group(0)
carry_tl = re.search(r'<div class="timeline">[\s\S]*?</div>\s*</div>', carry).group(0)

# ---------- 1. 한 장 요약: 타깃 유저 ----------
a, b = sec('id="summary"')
summ = s[a:b]
summ = summ.replace('<div class="grid g3">',
    '<div class="who"><span class="who-l">누구를 위해</span>'
    '<span class="chip">지친 기존 유저</span><span class="chip">석 달 쉬다 온 복귀 유저</span>'
    '<span class="chip">랭크가 부담스러운 캐주얼 유저</span>'
    + acc_html('세 유저의 하루', '같은 클라이언트, 다른 이유로 접속한다',
        '<table><tr><th style="width:26%">누구</th><th>지금</th><th>이 기획에서</th></tr>'
        '<tr><td>지친 기존 유저</td><td>퇴근 후 30분 집중할 힘이 없어 접속을 미룬다</td><td>광장에서 친구를 만나고, 보기만 해도 되는 포로 경주로 쉬다 간다</td></tr>'
        '<tr><td>복귀 유저</td><td>바뀐 메타·아이템 앞에서 첫 판부터 무너진다</td><td>공부가 필요 없는 숨바꼭질로 손을 풀고, 소식판으로 바뀐 것만 훑는다</td></tr>'
        '<tr><td>캐주얼 유저</td><td>랭크의 긴장과 팀원 갈등이 부담스럽다</td><td>학회원으로 이름만 올려도 시즌 이야기에 참여한다</td></tr></table>'
        '<span class="note">세 유저 모두 기존 LoL 유저입니다. 새 유저를 데려오는 기획이 아니라, 떠나려는 유저가 머물 이유를 만드는 기획입니다.</span>')
    + '</div>\n    <div class="grid g3">', 1)
s = s[:a] + summ + s[b:]

# ---------- 2. 2-1 → 머무는 고리 (코어 루프 + 몰입 설계 + 문제→해결) ----------
loop_svg = '''<svg class="loop" viewBox="0 0 900 430" role="img" aria-label="머무는 고리: 광장 접속, 한 판, 학회 기여, 광장 변화가 다시 접속으로 이어진다">
  <defs><marker id="ah" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#A9792A"/></marker></defs>
  <ellipse cx="450" cy="215" rx="300" ry="150" fill="none" stroke="#E3CF9F" stroke-width="14"/>
  <path d="M575 62 Q690 70 735 145" fill="none" stroke="#A9792A" stroke-width="3" marker-end="url(#ah)"/>
  <path d="M765 225 Q745 330 578 372" fill="none" stroke="#A9792A" stroke-width="3" marker-end="url(#ah)"/>
  <path d="M322 372 Q160 335 140 228" fill="none" stroke="#A9792A" stroke-width="3" marker-end="url(#ah)"/>
  <path d="M140 145 Q170 62 325 52" fill="none" stroke="#A9792A" stroke-width="3" marker-end="url(#ah)"/>
  <g class="node"><rect x="330" y="20" width="240" height="70" rx="16"/><text x="450" y="50">① 광장에 접속</text><text class="s" x="450" y="74">큐 대기 = 산책 · 친구가 서 있다</text></g>
  <g class="node"><rect x="640" y="150" width="240" height="70" rx="16"/><text x="760" y="180">② 한 판</text><text class="s" x="760" y="204">협곡 또는 쉬어 가는 캐주얼</text></g>
  <g class="node"><rect x="330" y="340" width="240" height="70" rx="16"/><text x="450" y="370">③ 학회 기여</text><text class="s" x="450" y="394">이겨도 져도 이름이 남는다</text></g>
  <g class="node"><rect x="20" y="150" width="240" height="70" rx="16"/><text x="140" y="180">④ 광장이 바뀐다</text><text class="s" x="140" y="204">주간 정산 · 한 주에 한 칸</text></g>
  <g class="imm"><circle cx="690" cy="78" r="17"/><text x="690" y="84">A</text></g>
  <g class="imm"><circle cx="712" cy="318" r="17"/><text x="712" y="324">B</text></g>
  <g class="imm"><circle cx="188" cy="318" r="17"/><text x="188" y="324">C</text></g>
  <text class="mid" x="450" y="205">다시 접속할 이유가</text><text class="mid" x="450" y="235">풍경으로 보인다</text>
</svg>'''

loop_sec = f'''<section class="r-ionia" id="loop">
  <div class="wrap">
    <div class="sec-head">
      <div><div class="sec-no">2-1 · 머무는 고리</div><h2>경쟁은 협곡에서,<br>쉼과 기록은 도시에서</h2></div>
      <p>한 판이 끝나도 고리는 끝나지 않는다. 협곡 규칙은 그대로, 바뀌는 건 바깥의 시간.</p>
    </div>
    <div class="loop-wrap">
      {loop_svg}
      <div class="imm-list">
        <div class="imm-item"><span class="b">A</span><div><h3>시점이 역할을 바꾼다</h3><p class="one">출전 = 카메라가 하늘로 · 귀환 = 내 소환사 곁으로</p></div></div>
        <div class="imm-item"><span class="b">B</span><div><h3>우리 도시의 승부</h3><p class="one">내 한 판이 내가 사는 도시의 운명에 더해진다</p></div></div>
        <div class="imm-item"><span class="b">C</span><div><h3>눈에 보이는 결과</h3><p class="one">LP 숫자 대신, 광장의 풍경이 한 칸씩 바뀐다</p></div></div>
      </div>
    </div>
    <div style="margin-top:18px">
      {acc_html('몰입을 만드는 세 장치', '안내문 대신, 공간과 카메라가 다음 행동을 알려 준다', """
<h4>A · 시점이 역할을 바꾼다</h4><ul>
<li>광장에서는 소환사 자신이 걷습니다. 포탈에 들어서면 카메라가 등 뒤에서 하늘로 솟아올라 위에서 내려다보는 시점이 되고, 그대로 기존 로딩 화면으로 이어집니다.</li>
<li>로딩 화면이라는 '끊김'이 '이제 지휘한다'는 신호로 바뀝니다. 경기가 끝나면 카메라가 내려와 내 소환사 곁에 붙어 '다시 나로 돌아왔다'는 쉼의 신호가 됩니다.</li></ul>
<h4>B · 우리 도시의 승부</h4><ul>
<li>내 한 판은 학회 기여가 되어 도시의 분쟁 방향에 더해집니다. 월드컵처럼 직접 뛰지 않는 날에도 '우리 도시의 승부'라서 결과가 궁금해집니다.</li>
<li>세계관이 이길 이유를 만들기 때문에, 보상을 크게 덧붙이지 않아도 됩니다.</li></ul>
<h4>C · 눈에 보이는 결과</h4><ul>
<li>순위는 숫자가 아니라 광장의 장식(깃발·노점·비계·꽃가루)으로 보입니다. 클라이언트를 켤 때마다 '조금 달라졌다'는 변화가 먼저 눈에 들어옵니다.</li>
<li>한 주에 한 칸씩만 바뀌어서, 다음 주를 기다리게 됩니다.</li></ul>
<span class="note">세 장치 모두 새 화면을 만들지 않고, 이미 있는 순간(로딩·결과·클라이언트 첫 화면)의 의미를 바꾸는 방식입니다.</span>""", essential=True)}
      {acc_html('벽마다 어떤 장치가 대응하나', 'PART 01의 네 벽 → 해결 장치', """<table>
        <tr><th style="width:30%">벽</th><th>장치</th><th>어디서</th></tr>
        <tr><td>한 판의 피로 · 갈등</td><td>관전형 캐주얼 · 머무는 광장</td><td>3-1 · 포로 경주</td></tr>
        <tr><td>패치 공부</td><td>패치와 무관한 캐주얼 규칙</td><td>숨바꼭질 · 포로 경주</td></tr>
        <tr><td>복귀 격차</td><td>관찰 · 운 중심 모드</td><td>숨바꼭질</td></tr>
        <tr><td>LP뿐인 보상</td><td>학회 순위 · 광장 · 외형</td><td>3-2 · 3-3</td></tr></table>""")}
    </div>
  </div>
</section>'''
a, b = sec('2-1 · 한 문장 콘셉트')
s = s[:a] + loop_sec + s[b:]
# 액자 뒤의 세계관 장은 학회 장으로 옮기므로 삭제
a, b = sec('id="world"')
s = s[:a] + s[b:]

# ---------- 3. 세계관 + 학회 (2-2) ----------
acad_sec = f'''<section class="r-ionia" id="academy">
  <div class="wrap">
    <div class="sec-head">
      <div><div class="sec-no">2-2 · 세계관과 학회</div><h2>거주 도시 = 학회 = 세력</h2></div>
      <p>전쟁의 학회가 사라진 뒤 숨어 사는 소환사들. 시즌마다 사는 도시를 고르면 그 도시의 학회원이 됩니다.</p>
    </div>
    {world_cards}
    <div style="margin-top:18px">
      {world_accs[0]}
      {academy_accs[0]}
    </div>
  </div>
</section>'''
replace_sec('id="academy"', acad_sec)
a, b = sec('id="view"')
s = s[:a] + s[b:]

# ---------- 4. 3-0 → 1단계에서 만드는 것 (개발 범위) ----------
build_sec = f'''<section class="r-demacia" id="build">
  <div class="wrap">
    <div class="sec-head">
      <div><div class="sec-no">3-0 · 1단계에서 만드는 것</div><h2>새 게임이 아니라,<br>지금 클라이언트 위에</h2></div>
      <p>새로 만드는 것은 다섯 가지. 챔피언 · 맵 · 스킨 · 매칭은 그대로 씁니다.</p>
    </div>
    <div class="grid g5">
      <div class="card"><span class="num">1</span><h3>학회 광장</h3><p class="one">쿼터뷰 광장 1종 + 학회별 장식 세트</p></div>
      <div class="card"><span class="num">2</span><h3>소환사</h3><p class="one">클릭 이동 · 감정표현 · 꾸밈 슬롯</p></div>
      <div class="card"><span class="num">3</span><h3>시즌 집계</h3><p class="one">기여 계산 · 주간 정산 · 소식판</p></div>
      <div class="card"><span class="num">4</span><h3>캐주얼 2종</h3><p class="one">숨바꼭질 · 포로 경주</p></div>
      <div class="card"><span class="num">5</span><h3>승리 이펙트</h3><p class="one">챔피언 오라 · 귀환 · 우물</p></div>
    </div>
    <div style="margin-top:18px">
      {acc_html('만드는 것과 다시 쓰는 것', '1단계 개발 범위를 한눈에', """<table>
        <tr><th style="width:18%">항목</th><th>새로 만드는 것</th><th>그대로 다시 쓰는 것</th></tr>
        <tr><td>학회 광장</td><td>광장 맵 1종 (모든 학회 공용 구조) · 학회별 장식 세트 × 분위기 3단계</td><td>클라이언트 화면 틀 · 큐 · 친구 목록 · 파티 기능</td></tr>
        <tr><td>소환사</td><td>기본 소환사 캐릭터 · 걷기/감정표현 애니메이션 · 꾸밈 슬롯</td><td>TFT 전설이의 클릭 이동 방식</td></tr>
        <tr><td>시즌 집계</td><td>학회 기여 계산 · 주간 정산 · 광장 소식판 글</td><td>기존 경기 결과 데이터 · 시즌 일정</td></tr>
        <tr><td>캐주얼 2종</td><td>숨바꼭질 규칙 · 포로 경주 트랙</td><td>소환사의 협곡 부쉬 · 와드 · 시야 규칙, 포로 모델, 아레나처럼 '새 모드' 추가 경로</td></tr>
        <tr><td>승리 이펙트</td><td>학회 색 오라 · 귀환 문양 · 우물 깃발 연출</td><td>기존 스킨 (덮어쓰지 않고 위에 얹음)</td></tr></table>
        <h4>1단계에서 만들지 않는 것</h4><ul>
        <li>3인칭으로 걷는 도시, 포탈 여행, 새 지역 맵 → 3단계에서 지표를 확인한 뒤.</li>
        <li>광장 채팅, 거래 → 광장이 또 하나의 갈등 공간이 되지 않도록.</li></ul>""", essential=True)}
    </div>
  </div>
</section>'''
replace_sec('3-0 · 개요', build_sec)

# ---------- 5. 광장 + 시점 규칙 ----------
a, b = sec('id="plaza"')
pl = s[a:b]
v = view_accs[0].replace('<button class="acc-btn" aria-expanded="false"><span>',
                         '<button class="acc-btn" aria-expanded="false"><span class="n">+</span><span>')
last = accs(pl)[-1]
pl = pl.replace(last, last + '\n        ' + v)
pl = pl.replace('<p>번호를 누르면 설계가 펼쳐집니다.</p>', '<p>메뉴 화면 대신, 친구가 서 있는 내 도시의 광장.</p>')
s = s[:a] + pl + s[b:]

# ---------- 6. 세력 시즌 + 순위별 광장 ----------
season_sec = f'''<section class="r-demacia" id="season">
  <div class="wrap">
    <div class="sec-head">
      <div><div class="sec-no">3-2 · 시즌과 광장 변화</div><h2>협곡의 결과가 학회의 이야기로</h2></div>
      <p>결말은 유저의 승부가 씁니다. 순위는 숫자가 아니라 광장의 풍경으로.</p>
    </div>
    {season_flow}
    <div style="margin-top:18px">
      {must(season_accs[0])}
    </div>
    <div style="margin-top:28px">{rank_grid}</div>
    <div style="margin-top:18px">
      {season_accs[1]}
      {rank_accs[0]}
    </div>
  </div>
</section>'''
replace_sec('id="season"', season_sec)
a, b = sec('id="rank"')
s = s[:a] + s[b:]

# ---------- 7. 승리 보상: '왜 외형인가' 펼침 ----------
a, b = sec('id="reward"')
rw = s[a:b]
why = [x for x in accs(rw) if '왜 능력치가 아니라 외형인가' in x][0]
rw = rw.replace(why, must(why))
s = s[:a] + rw + s[b:]

# ---------- 8. 캐주얼 원칙 → 숨바꼭질 머리 ----------
a, b = sec('id="casual"')
s = s[:a] + s[b:]
a, b = sec('id="hide"')
hd = s[a:b]
hd = hd.replace('<div class="sec-no">3-6 · 대표 모드 · 탑다운</div><h2>부쉬 숨바꼭질</h2>',
                '<div class="sec-no">3-4 · 캐주얼 모드</div><h2>부쉬 숨바꼭질</h2>')
hd = hd.replace('<p>관객만 아는 긴장. LoL의 부쉬 · 와드 · 시야를 그대로 씁니다.</p>',
                '<p>관객만 아는 긴장. 아레나처럼 새 모드로 추가합니다.</p>')
hd = hd.replace('<div class="split">',
    '<div class="rules"><span class="who-l">네 원칙</span><span class="chip">실력보다 관찰과 운</span>'
    '<span class="chip">패치 무관 · 버튼 1개</span><span class="chip">3~5분 짧은 판</span><span class="chip">관객이 더 안다</span></div>\n    <div class="split">', 1)
first = accs(hd)[0]
hd = hd.replace(first, must(first))
last = accs(hd)[-1]
hd = hd.replace(last, last + '\n        ' + casual_accs[0])
s = s[:a] + hd + s[b:]
s = s.replace('<div class="sec-no">3-7 · 관전형 모드 · 탑다운</div>', '<div class="sec-no">3-5 · 관전형 모드</div>')

# ---------- 9. 로드맵 + 이어지는 자산 ----------
a, b = sec('id="roadmap"')
rm = s[a:b]
rm = rm.replace('<div class="sec-no">5-1 · 단계별 확장</div>', '<div class="sec-no">5 · 단계별 확장</div>')
last = accs(rm)[-1]
rm = rm.replace(last, last + '\n        ' + acc_html('1단계에 만든 것은 버려지지 않는다', '소환사 · 학회 기록 · 광장이 다음 단계로 그대로',
    carry_tl + '<p style="margin-top:10px"><b>회사에게</b> 1단계 비용 = 다음 단계의 기반 · <b>유저에게</b> 처음부터 함께한 소환사가 넓은 세상으로</p>'))
s = s[:a] + rm + s[b:]
a, b = sec('id="carry"')
s = s[:a] + s[b:]

# ---------- 10. 수익 · 지표 · 리스크 → 실행 가능성 ----------
feas = f'''<section class="r-shurima alt" id="feasible">
  <div class="wrap">
    <div class="sec-head">
      <div><div class="sec-no">6 · 실행 가능성</div><h2>팔 것, 잴 것, 먼저 답할 것</h2></div>
      <p>수치는 지어내지 않습니다. 단계마다 측정해서 다음 단계를 엽니다.</p>
    </div>
    <div class="grid g3">
      <div class="card"><span class="tag">수익 모델</span><h3>스킨에게, 보여 줄 무대를</h3><p class="one">소환사 꾸미기 · 광장 감정표현 · 학회 의상 — 경쟁에 영향 주는 상품 0</p></div>
      <div class="card"><span class="tag">지표 가설</span><h3>남는 게 있으면 한 판 더</h3><p class="one">주간 판 수 · 패배 후 종료 · 복귀 재이탈 · 협곡 없는 접속 · 항복률</p></div>
      <div class="card"><span class="tag">리스크</span><h3>협곡의 경쟁은 그대로 둔다</h3><p class="one">비용 · 저사양 PC · 공정성 · 학회 쏠림 · 학회 간 대립</p></div>
    </div>
    <div style="margin-top:18px">
      {bm_accs[0]}
      {acc_html('지표 가설 표', '무엇이 좋아지는지, 무엇과 비교하나', kpi_table)}
      {kpi_accs[0]}
      {acc_html('리스크와 대응', '먼저 묻게 될 질문에, 먼저 답한다', risk_table)}
    </div>
  </div>
</section>'''
replace_sec('id="bm"', feas)
for m in ['id="kpi"', 'id="risk"']:
    a, b = sec(m); s = s[:a] + s[b:]

# ---------- 11. 결론: 비슷한 시도와 다른 점 ----------
a, b = sec('id="compare"')
cp = s[a:b]
cp = cp.replace('<section class="r-shurima alt" id="compare">', '<section class="r-shurima" id="compare">')
cp = cp.replace('<div class="banner">판 수',
    '<h3 class="sub">비슷한 시도와 다른 점</h3>\n    <table class="cmp">'
    '<tr><th style="width:24%">비슷한 시도</th><th>같은 점</th><th>이 기획이 다른 점</th></tr>'
    '<tr><td>TFT 전설이</td><td>클릭으로 움직이는 작은 캐릭터 · 꾸밈 상품</td><td>경기 결과가 광장의 풍경과 학회 순위로 남는다</td></tr>'
    '<tr><td>LoL 아레나 등 기간 모드</td><td>기존 클라이언트에 새 모드로 추가</td><td>조작 · 패치 공부가 필요 없고, 보기만 해도 참여</td></tr>'
    '<tr><td>MMO의 마을 · 소셜 허브</td><td>활동 사이에 머무는 공간</td><td>새 게임 없이 기존 클라이언트 위 · 매주 순위로 모습이 바뀐다</td></tr>'
    '</table>\n    <div class="banner">판 수', 1)
s = s[:a] + cp + s[b:]

# ---------- 12. 섹션 번호 정리 ----------
for old, new in [('3-4 · 승리 보상', '3-3 · 승리 보상'), ('PART 04 · 한 소환사의 하루', '4 · 한 소환사의 하루')]:
    s = s.replace(f'<div class="sec-no">{old}</div>', f'<div class="sec-no">{new}</div>')

# ---------- 13. 스타일 + 마우스 올리면 떠오르는 상세 ----------
css = '''
/* v7 설명 부분 */
.who,.rules{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin:0 0 22px}
.who .acc{flex-basis:100%;margin-top:6px}
.who-l{font:900 13px/1 'Cinzel','Hahmlet',serif;letter-spacing:.14em;color:var(--accent);margin-right:6px}
.chip{font:700 15px/1 'Noto Sans KR',sans-serif;color:#3A2E20;background:#FFF8E8;border:1px solid #E3CF9F;border-radius:999px;padding:10px 16px}
.g5{grid-template-columns:repeat(5,1fr)}
@media(max-width:980px){.g5{grid-template-columns:repeat(2,1fr)}}
.loop-wrap{display:grid;grid-template-columns:1.5fr 1fr;gap:26px;align-items:center}
@media(max-width:900px){.loop-wrap{grid-template-columns:1fr}}
svg.loop{width:100%;height:auto}
svg.loop .node rect{fill:#FFFCF4;stroke:#C9A24E;stroke-width:2}
svg.loop .node text{font:800 20px 'Hahmlet',serif;fill:#2A2118;text-anchor:middle}
svg.loop .node text.s{font:600 14px 'Noto Sans KR',sans-serif;fill:#6A5A44}
svg.loop .imm circle{fill:#A9792A}
svg.loop .imm text{font:900 16px 'Cinzel',serif;fill:#FFF6DE;text-anchor:middle}
svg.loop text.mid{font:800 19px 'Hahmlet',serif;fill:#8A5A1E;text-anchor:middle}
.imm-list{display:flex;flex-direction:column;gap:12px}
.imm-item{display:flex;gap:14px;align-items:flex-start;background:linear-gradient(180deg,#FFFCF4,#FBF3E2);border:1px solid #E3CF9F;border-radius:14px;padding:16px 18px}
.imm-item .b{flex:none;width:34px;height:34px;border-radius:50%;display:grid;place-items:center;font:900 15px/1 'Cinzel',serif;color:#FFF6DE;background:radial-gradient(circle at 35% 30%,#E8C46E,#A9792A 70%)}
.imm-item h3{font:800 18px/1.3 'Hahmlet',serif;color:#2A2118;margin-bottom:4px}
h3.sub{font:800 22px/1.3 'Hahmlet',serif;color:#2A2118;margin:34px 0 12px}
/* 필수 상세: 처음부터 펼쳐 둠 */
.acc.must{border-color:#C9A24E;box-shadow:0 8px 22px rgba(90,60,20,.10)}
.acc.must .acc-btn::before{content:'핵심';flex:none;font:800 11px/1 'Noto Sans KR',sans-serif;color:#FFF6DE;background:#A9792A;border-radius:999px;padding:5px 8px}
/* 나머지 상세: 마우스를 올리면 떠오르고, 누르면 그 자리에 고정 */
.acc{overflow:visible;position:relative}
.acc:not(.must) .acc-btn .plus::after{content:''}
.acc.peek .acc-btn[aria-expanded="false"]+.acc-body{position:absolute;left:0;right:0;top:calc(100% + 6px);z-index:40;grid-template-rows:1fr;
  background:#FFFCF4;border:1px solid #C9A24E;border-radius:14px;box-shadow:0 22px 48px rgba(60,40,10,.28);max-height:min(62vh,560px);overflow:auto;animation:peekin .22s ease}
.acc.peek .acc-btn[aria-expanded="false"]+.acc-body .acc-inner{border-top:0;padding-top:16px}
@keyframes peekin{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:none}}
.peek-hint{font:600 13px/1.4 'Noto Sans KR',sans-serif;color:#8A7458;margin:0 0 10px}
'''
i = s.index('</style>'); s = s[:i] + css + s[i:]

js = '''
  // v7: 마우스를 올리면 상세가 떠오르고(밀어내지 않음), 누르면 그 자리에 고정
  var canHover=matchMedia('(hover:hover)').matches;
  document.querySelectorAll('.acc:not(.must)').forEach(function(a){
    if(!canHover)return; var t;
    a.addEventListener('mouseenter',function(){clearTimeout(t);t=setTimeout(function(){a.classList.add('peek')},140)});
    a.addEventListener('mouseleave',function(){clearTimeout(t);t=setTimeout(function(){a.classList.remove('peek')},120)});
    a.querySelector('.acc-btn').addEventListener('click',function(){a.classList.remove('peek')});
  });
'''
k = s.rindex('})();')
s = s[:k] + js + s[k:]

open(P, 'w', encoding='utf-8').write(s)
print('ok', s.count('<section'))
