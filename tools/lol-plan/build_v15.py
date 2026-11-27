# v14 -> v15: 11/27 오후 결정 반영
# - 광장 = 클라이언트 화면이 아니라 롤 안의 "전투 없는 게임 모드". 놀다가 큐가 잡히면 떠난다.
# - 단계: 1단계 광장 모드 → 다음은 라이엇 MMO로 잇기 (2단계 삭제). 학회 팀 매칭은 이번 기획서에서 뺌.
# - 숨바꼭질 = 정식 모드(5:5 · 약 15분 공수 교대 · 협곡 맵 · 니코처럼 사물 복제 · 미니언 행렬 · 와드 · 렌즈 · 일반/랭크)
# - 광장 즉석 놀이 = 포로 경주(관객 개입) + 점프 레이스 + 1:1 구역(문도 피구 · 카서스 1:1)
# - 협곡을 적게 해도 손해 없음(스킨이 보일 무대) · 영상의 편함 + 게임의 반응 · 스킨 광장용 경량화 · 하루 첫 판 기여 가중
import os, re
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v14.html', encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    assert s.count(old) >= n, old[:70]
    s = s.replace(old, new, n)

def section(id_, new):
    global s
    i = s.find(f'id="{id_}"'); assert i > 0, id_
    a = s.rfind('<section', 0, i); b = s.find('</section>', a) + len('</section>')
    s = s[:a] + new.strip() + s[b:]

def between(start_marker, open_tag, close_tag, new):
    """start_marker 다음에 처음 나오는 open_tag ~ close_tag 를 new 로 교체"""
    global s
    i = s.find(start_marker); assert i > 0, start_marker
    a = s.find(open_tag, i); b = s.find(close_tag, a) + len(close_tag)
    s = s[:a] + new + s[b:]

s = s.replace('v14</title>', 'v15</title>')

# ---------- 한 장 요약 ----------
rep('<p class="one">관전형 · 패치 무관 캐주얼 모드</p>', '<p class="one">광장 즉석 놀이 · 숨바꼭질 모드 · 패치 공부 0</p>')
rep('<h3>스킨의 무대</h3><p class="one">광장 = 꾸밈 상설 무대 · 능력치 영향 0</p>',
    '<h3>협곡을 덜 해도 손해 없음</h3><p class="one">광장 · 놀이 모두 내 스킨으로 · 스킨이 보일 무대</p>')
rep('<td>학습 없이 숨바꼭질 · 포로 경주로 협곡의 부쉬 · 와드 · 포로를 먼저 즐기고, 학회로 응원할 팀이 생긴다</td>',
    '<td>숨바꼭질로 협곡 지도 · 와드 · 렌즈를, 광장 놀이로 스킬 감각을 학습 없이 먼저 익히고, 학회로 응원할 팀이 생긴다</td>')
between('<div class="plan3">', '<div class="plan3">', '</ol>\n    </div>', '''<div class="plan3">
      <div class="p3-head"><b>작게 시작해서, 반응을 확인하고 잇는다</b><span>다음 단계는 1단계의 지표가 좋아진 것을 확인한 뒤에 엽니다</span></div>
      <ol class="p3-steps" style="grid-template-columns:repeat(2,1fr)">
        <li><span class="p3-n">1단계 · 롤 안의 광장 모드</span><b>학회 본단 안뜰에서 놀다가,<br>큐가 잡히면 떠난다</b><span class="p3-d">전투 없는 광장 · 즉석 놀이 3종 · 숨바꼭질 정식 모드</span></li>
        <li><span class="p3-n">다음 · 잇기</span><b>라이엇 MMO에<br>기록을 넘긴다</b><span class="p3-d">새로 만들지 않고 · 내 소환사와 학회 기록이 이어짐</span></li>
      </ol>
    </div>''')

# ---------- 1-1 네 개의 벽 표 ----------
rep('<td>3-1 · 4-2 포로 경주</td>', '<td>3-1 · 4-2 광장 즉석 놀이</td>')

# ---------- 2-1 머무는 고리 ----------
rep('<p class="sl">포탈에 들어서면 카메라가 하늘로 솟습니다. 이제 지휘할 시간.</p><p class="sm">로딩 화면이 "역할이 바뀌었다"는 신호가 된다.</p>',
    '<p class="sl">큐가 잡히면 광장을 떠나 협곡으로. 안 잡혀도 즉석 놀이 한 판.</p><p class="sm">기다리던 시간이 노는 시간이 된다.</p>')
rep('''<h4>A · 시점이 역할을 바꾼다</h4><ul>
<li>광장에서는 소환사 자신이 걷습니다. 포탈에 들어서면 카메라가 등 뒤에서 하늘로 솟아올라 위에서 내려다보는 시점이 되고, 그대로 기존 로딩 화면으로 이어집니다.</li>
<li>로딩 화면이라는 '끊김'이 '이제 지휘한다'는 신호로 바뀝니다. 경기가 끝나면 카메라가 내려와 내 소환사 곁에 붙어 '다시 나로 돌아왔다'는 쉼의 신호가 됩니다.</li></ul>''',
'''<h4>A · 언제 와도 바로 놀고, 큐가 잡히면 떠난다</h4><ul>
<li>광장에 들어오면 내 챔피언 · 스킨으로 바로 놀 수 있습니다. 즉석 놀이는 1~3분이고, 큐가 잡히면 언제 떠나도 남에게 피해가 없습니다.</li>
<li>영상처럼 아무 때나 켜고 끌 수 있으면서, 영상과 달리 내 손짓에 바로 반응이 옵니다(2-2 참고).</li></ul>''')
rep("클라이언트를 켤 때마다 '조금 달라졌다'는 변화가 먼저 눈에 들어옵니다.", "광장에 들어올 때마다 '조금 달라졌다'는 변화가 먼저 눈에 들어옵니다.")
rep('세 장치 모두 새 화면을 만들지 않고, 이미 있는 순간(로딩·결과·클라이언트 첫 화면)의 의미를 바꾸는 방식입니다.',
    '세 장치 모두 협곡 규칙은 건드리지 않고, 협곡 바깥의 시간(대기 · 결과 · 쉬는 날)에 의미를 더하는 방식입니다.')

# ---------- 2-2 왜 지금인가 ----------
rep('<div class="cs-band">게임과 시간을 다투지 않는다. <em>짧은 틈과 \'보는 시간\'</em>을 게임 안으로 가져온다.</div>',
'''<table class="why-t" style="margin-top:18px">
      <tr><th style="width:38%">사람들이 영상으로 간 이유</th><th>광장이 갖춘 것</th></tr>
      <tr><td>아무 때나 켜고 끈다</td><td>언제 들어와도 되고, 큐가 잡혀 떠나도 손해 없음</td></tr>
      <tr><td>누워서도 본다</td><td>클릭 몇 번이면 되는 놀이</td></tr>
      <tr><td>짧게 끊어 본다</td><td>1~3분 즉석 놀이</td></tr>
      <tr><td>남 탓할 일이 없다</td><td>혼자 해도 되는 놀이 · 진 사람도 참여분</td></tr>
      <tr><td><b>그런데 내가 한 일에 반응이 없다</b></td><td><b>누르면 바로 반응 · 관객도 한 번씩 개입 · 결과가 학회 기록에 남음</b></td></tr>
    </table>
    <div class="cs-band">영상의 편함에, 게임의 반응을 더한다. <em>보는 사람을 하는 사람으로.</em></div>''')

# ---------- 2-3 세계관 ----------
rep('1단계에서 클라이언트를 켜면 처음 보이는 광장이 바로 <b>본단의 안뜰</b>입니다.',
    '광장 모드에 들어가면 펼쳐지는 곳이 바로 <b>본단의 안뜰</b>입니다.')

# ---------- 3-0 만드는 것 ----------
section('build', '''
<section class="r-demacia" id="build">
  <div class="wrap">
    <div class="sec-head">
      <div><div class="sec-no">3-0 · 1단계에서 만드는 것</div><h2>새 게임이 아니라,<br>롤 안의 모드 하나</h2></div>
      <p>챔피언 · 스킨 · 협곡 맵 · 매칭은 그대로 씁니다. 대부분은 아레나 등 이미 있는 기능을 다시 씁니다.</p>
    </div>
    <div class="grid g5">
      <div class="card"><span class="num">1</span><h3>광장 모드</h3><p class="one">본단 안뜰 1종 · 채널 · 전투 없음</p></div>
      <div class="card"><span class="num">2</span><h3>큐 연결</h3><p class="one">광장 안에서 큐 · 수락</p></div>
      <div class="card"><span class="num">3</span><h3>놀이</h3><p class="one">즉석 놀이 3종 · 숨바꼭질</p></div>
      <div class="card"><span class="num">4</span><h3>시즌 집계</h3><p class="one">기여 계산 · 주간 정산 · 게시판</p></div>
      <div class="card"><span class="num">5</span><h3>승리 이펙트</h3><p class="one">챔피언 오라 · 귀환 · 우물</p></div>
    </div>
    <div style="margin-top:18px">
      <div class="acc must"><button class="acc-btn" aria-expanded="true"><span>만드는 것과 다시 쓰는 것<span class="sum">1단계 개발 범위를 한눈에</span></span><span class="plus" aria-hidden="true">+</span></button><div class="acc-body"><div><div class="acc-inner"><table>
        <tr><th style="width:16%">항목</th><th>새로 만드는 것</th><th>그대로 다시 쓰는 것</th></tr>
        <tr><td>광장 모드</td><td>광장 맵 1종(모든 학회 공용 구조) · 학회별 장식 × 분위기 3단계 · 채널</td><td>아레나처럼 '새 모드' 추가 경로 · 탑다운 이동 · 감정표현 · 귀환 · 같은 팀끼리는 스킬이 안 맞는 규칙(그래서 전투 판정이 없음)</td></tr>
        <tr><td>큐 연결</td><td>광장과 클라이언트를 잇는 큐 통로 · 광장 화면의 큐 버튼과 수락 창</td><td>기존 큐 · 매칭 · 챔피언 선택 · 상점처럼 클릭하는 게임 내 창</td></tr>
        <tr><td>스킨 표시</td><td>광장용 가벼운 스킨을 자동으로 뽑는 도구(겉모습 · 걷기 · 감정표현 · 귀환만)</td><td>기존 스킨 · 저사양 품질 옵션 · MMO 마을의 채널 · 표시 인원 제한 방식</td></tr>
        <tr><td>놀이</td><td>1:1 구역 안에서 챔피언 바꾸기 · 점프 코스 · 포로 트랙 · 숨바꼭질 규칙(복제 · 목표)</td><td>아레나의 경기장 벽 · 라운드 초기화 · 한 게임 여러 팀 구조, 협곡 맵 · 미니언 · 와드 · 렌즈, 솔방울 · 점멸</td></tr>
        <tr><td>시즌 집계</td><td>학회 기여 계산 · 주간 정산 · 광장 게시판</td><td>기존 경기 결과 데이터 · 시즌 일정</td></tr>
        <tr><td>승리 이펙트</td><td>학회 색 오라 · 귀환 문양 · 우물 깃발 연출</td><td>기존 스킨 (덮어쓰지 않고 위에 얹음)</td></tr></table>
        <h4>만들지 않는 것</h4><ul>
        <li>협곡의 규칙 · 매칭 → 건드리지 않습니다. 광장은 협곡 바깥만 바꿉니다.</li>
        <li>룬테라 도시 → 만들지 않고 라이엇 MMO로 잇습니다.</li>
        <li>광장 채팅 · 거래 → 광장이 또 하나의 갈등 공간이 되지 않도록.</li></ul></div></div></div></div>
    </div>
  </div>
</section>''')

# ---------- 3-1 학회 광장 ----------
def row(c0, c1, c2, items):
    lis = ''.join(f'\n            <li>{x}</li>' for x in items)
    return (f'<div class="cmp-row"><button aria-expanded="false"><span class="c0">{c0}</span><span class="c1">{c1}</span>'
            f'<span class="c2">{c2}</span><span class="pl">+</span></button><div class="cmp-body"><div><div class="cmp-in"><ul>{lis}\n          </ul></div></div></div></div>')
rows = ''.join([
  row('들어가기', '메뉴 화면', '광장 모드 입장 · 내 챔피언과 스킨으로 걷는다', [
    '광장은 롤의 <b>게임 모드 하나</b>입니다. 들어가면 학회 본단 안뜰이 펼쳐지고, 원하는 챔피언을 스킨째 소환해 걷습니다.',
    '조작은 협곡 그대로입니다. 탑다운 · 우클릭 이동 · 감정표현 · 귀환. <b>새로 배울 것이 없습니다.</b>',
    '광장에서는 <b>모두 같은 팀</b>입니다. 롤은 같은 팀끼리 스킬이 맞지 않으니, 따로 막지 않아도 전투가 일어나지 않습니다. 서버는 걷기와 감정표현만 전하면 됩니다.',
    '안뜰은 지난 시즌 우승 학회의 양식으로 꾸며져 있습니다(2-3 참고).']),
  row('큐 대기', '타이머만 보며 기다린다', '광장에서 놀며 기다린다', [
    '광장 화면 구석에 큐 버튼과 대기 시간이 있습니다. 롤 게임 화면에는 이미 마우스 커서와 상점 창이 있어, 창 하나를 더하는 수준입니다.',
    '<b>새로 만드는 것은 하나</b>: 광장의 큐 신호를 뒤에서 대기 중인 클라이언트로 전하는 연결 통로입니다. 지금은 게임 중이면 큐가 막히는데, 광장만 예외로 둡니다.',
    '매칭이 잡히면 수락 창이 광장에 뜨고, 수락하면 광장을 닫고 챔피언 선택으로 넘어갑니다. 원래 있던 챔피언 선택 시간 외에 늘어나는 건 광장을 닫는 몇 초입니다.',
    '<b>왜</b>: 매칭 대기는 롤에서 가장 할 일이 없는 시간입니다. 그 시간을 노는 시간으로 바꿉니다.']),
  row('할 것', '없음', '즉석 놀이 · 스킨 무대 · 학회 게시판', [
    '<b>즉석 놀이</b>: 포로 경주 · 점프 레이스 · 1:1 구역(4-2). 1~3분, 언제 빠져도 남에게 피해가 없습니다.',
    '<b>스킨 무대</b>: 귀환 무대에 서면 카메라가 다가가 내 스킨의 귀환 모션을 크게 보여 줍니다. 협곡에서는 한순간 지나가는 장면이 여기서는 주인공입니다.',
    '<b>학회 게시판</b>: 이번 주 학회 순위와 내 기여가 보입니다.']),
  row('친구', '목록 속 이름 한 줄', '광장에 서 있는 챔피언 · 클릭하면 파티', [
    '같은 채널에는 <b>온라인 친구</b>와 같은 학회원이 우선 모입니다.',
    '친구를 클릭하면 <b>파티 초대 · 프로필</b> 메뉴가 뜹니다. 친구 목록에서 하던 일을 광장에서 그대로 합니다.',
    '<b>모르는 사람과는 채팅 없이 감정표현만</b> 됩니다. 광장이 또 하나의 갈등 공간이 되지 않게 하기 위해서입니다.']),
  row('사람이 많으면', '협곡은 10명', '채널 20~40명 · 가까운 사람만 자세히', [
    '<b>MMO 마을 방식 그대로</b>: 광장을 20~40명 채널로 나누고, 내 주변 사람의 움직임만 자주 받습니다. 가까운 10~15명만 스킨 그대로, 멀리 있는 사람은 가벼운 모습으로 보입니다.',
    '<b>광장용 가벼운 스킨</b>: 광장에서는 싸우지 않으니 스킬 · 평타 · 피격 부분은 빼고 겉모습 · 걷기 · 감정표현 · 귀환만 불러옵니다. 1,000개가 넘는 스킨에 맞춰 도구로 자동 생성합니다.',
    '<b>이펙트 제한</b>: 동시에 터지는 화려한 이펙트 수를 제한하고, 귀환 무대처럼 보여 주는 자리에서만 전부 보여 줍니다.']),
])
section('plaza', f'''
<section class="cs" id="plaza">
  <div class="wrap">
    <div class="sec-head">
      <div><div class="sec-no">3-1 · 학회 광장</div><h2>메뉴 화면 대신, 놀다 가는 광장</h2></div>
      <p>광장은 전투가 없는 롤의 게임 모드입니다. 학회 본단 안뜰에서 놀다가, 큐가 잡히면 떠납니다. 줄을 누르면 설계가 열립니다.</p>
    </div>
    <div class="cmp">
      <div class="cmp-head"><span></span><span>지금 롤</span><span>광장 모드</span><span></span></div>
      {rows}
    </div>
    <div class="cs-band">새로 배울 것은 없습니다. 기다리던 시간이 <em>노는 시간</em>이 됩니다.</div>
  </div>
</section>''')

# ---------- 3-2 시즌 · 기여 ----------
rep('클라이언트를 켤 때마다 기분이 나빠집니다.', '광장에 들어올 때마다 기분이 나빠집니다.')
rep('<li><b>1인 하루 상한</b>: 하루 기여는 예시로 10판분까지만 셉니다. 시간이 많은 소수가 학회 순위를 좌우하지 않게 하고, 과몰입도 막습니다.</li>',
    '<li><b>하루 첫 1~2판은 크게</b>: 그날 첫 두 판의 기여를 크게 쳐 주고, 그 뒤로는 점점 줄어듭니다. 협곡 한두 판만 몰입해서 해도 학회에 확실히 보탬이 됩니다.</li>\n'
    '            <li><b>1인 하루 상한</b>: 하루 기여는 예시로 10판분까지만 셉니다. 시간이 많은 소수가 학회 순위를 좌우하지 않게 하고, 과몰입도 막습니다.</li>')

# ---------- PART 04 장면 ----------
rep('<p>경쟁 없는 놀이, 그리고 한 소환사의 하루</p>', '<p>가볍게 노는 모드, 그리고 한 소환사의 하루</p>')
rep('<span class="pn">4-2 · 관전형 모드</span><h2>포로 경주</h2><p>응원만 해도 한 판</p>',
    '<span class="pn">4-2 · 광장 즉석 놀이</span><h2>보다가, 뛰다가, 붙다가</h2><p>포로 경주 · 점프 레이스 · 1:1 구역</p>')

# ---------- 4-1 숨바꼭질 ----------
def acc(n, title, sum_, body, must=False, wide=False):
    num = f'<span class="n">{n}</span>' if n else ''
    return (f'<div class="fi"{" style=\"grid-column:1/-1\"" if wide else ""}><div class="acc{" must" if must else ""}"><button class="acc-btn" aria-expanded="{"true" if must else "false"}">{num}'
            f'<span>{title}<span class="sum">{sum_}</span></span><span class="plus" aria-hidden="true">+</span></button>'
            f'<div class="acc-body"><div><div class="acc-inner">{body}</div></div></div></div></div>')
def ul(items): return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'

hide_body = ''.join([
  acc(1, '한 판 흐름', '공수 교대 두 라운드, 약 15분', '''<table>
              <tr><th>단계</th><th>시간</th><th>일어나는 일</th></tr>
              <tr><td>준비</td><td>15초</td><td>블루팀 · 레드팀 공개. 1라운드는 블루팀이 숨고 레드팀이 찾음</td></tr>
              <tr><td>숨기</td><td>45초</td><td>숨는 팀만 움직임. 찾는 팀은 우물에서 화면이 가려진 채 대기</td></tr>
              <tr><td>수색</td><td>6분</td><td>찾는 팀 출발. 마지막 2분은 맵 바깥쪽부터 구역이 닫힘</td></tr>
              <tr><td>교대</td><td>15초</td><td>역할을 바꿔 2라운드 (같은 흐름)</td></tr>
              <tr><td>결과</td><td>20초</td><td>두 라운드 합산 점수 공개 · 마지막 생존자의 귀환 무대</td></tr>
            </table><span class="note">시간은 예시이며 테스트로 확정합니다.</span>''', must=True),
  acc(2, '숨는 팀', '니코처럼 사물을 복제한다', ul([
    '<b>[복제]</b>: 가까운 사물을 클릭하면 그 모습이 됩니다. 와드 · 정글 몹 · 솔방울 같은 식물 · 미니언. 니코 패시브와 같은 방식이라 설명이 필요 없습니다. 쿨타임 10초.',
    '<b>미니언 행렬에 섞이기</b>: 미니언은 움직이니 미니언 모습이면 걸어도 자연스럽습니다. 대신 행렬 속도에 맞춰 걸어야 하고, 라인을 벗어나면 그 자체가 단서입니다.',
    '<b>가만히 있는 사물</b>은 원래 없던 자리에 하나 더 있으면 들킵니다. 부쉬는 복제 쿨타임 동안 잠깐 피하는 곳입니다.',
    '<b>와드 · 렌즈</b>도 씁니다. 찾는 팀이 오는 길에 와드를 박고, 렌즈로 상대 와드를 지웁니다.'])),
  acc(3, '찾는 팀', '와드 · 렌즈로 찾고, 클릭으로 잡는다', ul([
    '<b>렌즈</b>: 범위 안의 복제한 사람이 잠깐 드러납니다. 협곡에서 렌즈로 와드를 찾는 것과 같은 감각입니다.',
    '<b>와드</b>: 숨는 팀이 지나갈 길목을 봅니다.',
    '<b>잡기</b>: 의심 가는 대상을 클릭합니다. 사람이면 잡고, 진짜 사물 · 미니언이면 3초 동안 못 움직입니다. 아무거나 누르는 것을 막습니다.',
    '잡힌 사람은 협곡에서 죽었을 때처럼 <b>우리 팀 시야만</b> 봅니다. 같은 팀끼리 말하는 건 원래 팀플레이라 따로 막지 않습니다.'])),
  acc(4, '협곡 맵에서 바꾸는 것', '시야만 끄고, 부쉬를 더한다', ul([
    '<b>포탑 · 미니언 시야를 끕니다.</b> 미니언은 싸우지 않고 서로 지나쳐 라인 끝까지 걸어간 뒤 다시 생깁니다. 세 라인에 행렬이 끊이지 않습니다.',
    '<b>라인 부쉬를 더합니다.</b> 숨을 공간을 확보합니다.',
    '<b>이동 속도는 협곡보다 조금 빠르게, 모두 같게</b>. 넓은 맵이 답답하지 않고, 챔피언 운이 없습니다.',
    '<b>구역 닫힘</b>: 수색 마지막 2분, 탑 · 바텀 바깥쪽부터 안개 벽이 닫히고 미드와 강가만 남습니다. 끝까지 한 자리에 박혀 있을 수 없습니다.'])),
  acc(5, '승패와 점수', '버틴 시간 + 목표', ul([
    '숨는 팀은 <b>잡히지 않고 버틴 시간</b>과, 숨은 채 해낸 <b>목표</b>(정찰 열매 따기, 정해진 자리에 와드 박기, 미니언 행렬과 라인 끝까지 가기)로 점수를 얻습니다. 목표를 하려면 숨은 자리에서 나와야 해서, 가만히 서 있기만 하는 판이 되지 않습니다.',
    '두 라운드 합산 점수가 높은 팀이 이깁니다. 역할을 한 번씩 바꾸니 어느 팀이 먼저 찾느냐의 운이 없습니다.',
    '잡히는 순간 복제가 펑 풀리며 내 스킨이 드러나고, 마지막 생존자는 결과 화면에서 귀환 무대에 섭니다.'])),
  acc(6, '일반전과 랭크전', '랭크는 따로, 잘 안 깎이게', wide=True, body=ul([
    '<b>일반전</b>이 기본입니다. 신규 유저는 여기서 시작합니다.',
    '<b>랭크전</b>은 따로 둡니다. 시즌제 등급이고, 이기면 크게 오르고 져도 조금만 내려갑니다. 올라가는 재미는 주고, 떨어지는 스트레스는 줄입니다.',
    '랭크전은 레벨 · 일반전 판 수 조건을 둡니다. 보상은 학회 기여와 등급별 꾸밈입니다.'])),
  acc('', '놀면서 익히는 협곡', '숨바꼭질이 협곡의 입구가 되는 이유', '''<table>
              <tr><th style="width:30%">숨바꼭질에서</th><th>협곡에서 쓰는 감각</th></tr>
              <tr><td>와드 박을 길목 고르기</td><td>시야 장악</td></tr>
              <tr><td>렌즈로 숨은 사람 찾기</td><td>상대 와드 지우기</td></tr>
              <tr><td>미니언 행렬과 걷기</td><td>라인 · 웨이브</td></tr>
              <tr><td>정글 몹으로 복제하기</td><td>정글 캠프 위치</td></tr>
              <tr><td>맵 전체를 15분 동안 누비기</td><td>라인 · 강 · 정글 · 부쉬 지도</td></tr>
            </table>''', must=True),
])
section('hide', f'''
<section class="r-frel alt" id="hide">
  <div class="wrap">
    <div class="sec-head">
      <div><div class="sec-no">4-1 · 정식 모드</div><h2>숨바꼭질: 협곡에서,<br>모두가 니코가 된다</h2></div>
      <p>5:5 · 약 15분 · 협곡 맵 그대로. 사물을 복제해 숨고, 와드와 렌즈로 찾는다. 놀다 보면 협곡 지도가 머리에 들어온다.</p>
    </div>
    <div class="grid g4" style="margin-bottom:18px">
      <div class="card"><span class="tag">맵</span><h3>협곡 그대로</h3><p class="one">포탑 · 미니언 시야만 끔 · 라인 부쉬 추가</p></div>
      <div class="card"><span class="tag">숨기</span><h3>사물 복제</h3><p class="one">니코처럼 · 미니언 행렬에 섞이기</p></div>
      <div class="card"><span class="tag">찾기</span><h3>와드 · 렌즈</h3><p class="one">잘못 잡으면 3초 멈춤</p></div>
      <div class="card"><span class="tag">승패</span><h3>공수 교대</h3><p class="one">2라운드 · 버틴 시간 + 목표</p></div>
    </div>
    <div class="flat">{hide_body}</div>
  </div>
</section>''')

# ---------- 4-2 광장 즉석 놀이 ----------
poro_body = ''.join([
  acc(1, '1:1 구역', '둘만 가둬 놓고, 죽일 때까지', '''<table>
              <tr><th style="width:22%">항목</th><th>규칙</th></tr>
              <tr><td>종목</td><td>문도 피구 · 카서스 1:1. 유저들이 사용자 설정 게임으로 직접 만들어 즐겨 온 놀이를 정식으로</td></tr>
              <tr><td>가두기</td><td>대결이 시작되면 원형 구역에 벽이 올라와 두 명만 가둠. 밖에서는 끼어들 수 없고 구경만</td></tr>
              <tr><td>전투 판정</td><td>원 안의 두 명만 잠시 서로 다른 팀으로 나뉘어 스킬이 맞음. 한 게임 여러 팀 구조는 아레나가 이미 씀</td></tr>
              <tr><td>스펙</td><td>1레벨 · Q 하나만 · 신발 + 수정 하나(카서스 사파이어, 문도 루비) · 패시브 끔</td></tr>
              <tr><td>자원</td><td>문도 체력 소모 · 카서스 마나 그대로, 자연 회복은 켬. 언제 던질지가 실력</td></tr>
              <tr><td>승패</td><td>죽이면 승리. 3분이 지나면 남은 체력 비율이 높은 쪽</td></tr>
              <tr><td>줄 서기</td><td>구역 앞에 서면 대기열. 이긴 사람은 남고 다음 도전자가 들어옴(○연승 표시)</td></tr>
              <tr><td>끝난 뒤</td><td>이긴 사람의 내 챔피언 · 스킨이 구역 위에 서서 감정표현</td></tr>
            </table><span class="note">새로 만드는 것은 "구역 안에서만 챔피언을 바꾸는 처리" 하나입니다. 큐가 잡히면 바로 나갈 수 있고, 상대 승리로 처리합니다.</span>''', must=True),
  acc(2, '점프 레이스', '솔방울 · 점멸로 건너는 허공 길', ul([
    '광장 한쪽에서 시작하는 허공 위 얇은 길. 우클릭으로 걷다가도 길 밖으로 나가면 떨어지고, 마지막 체크포인트에서 다시 시작합니다.',
    '틈은 <b>솔방울</b>로 날아서, 먼 틈은 <b>점멸</b>로 건넙니다. 밀어내는 포탄 · 사라지는 발판도 있습니다. 협곡의 솔방울 · 점멸 감각이 놀면서 익습니다.',
    '<b>혼자 타임 어택</b>은 아무 때나, <b>단체 출발</b>은 2분마다. 개인 레이스라 큐가 잡혀 떠나도 아무 영향이 없습니다.',
    '모두 같은 이동 속도 · 돌진 스킬 없음. 다른 건 스킨뿐입니다. 주간 최고 기록은 학회별로 게시판에 오릅니다.',
    '<b>선례</b>: 탑다운 엔진에서 지형 판정만으로 떨어짐을 처리하는 놀이는 워크래프트 3의 탈출 · 슬라이드 유즈맵에서 오래 즐겨 온 장르입니다.'])),
  acc(3, '포로 경주', '보기만 해도, 한 번은 내가 개입한다', ul([
    '포로들이 트랙을 자동으로 달리는 약 90초 레이스. 광장 한쪽에서 정해진 간격으로 열립니다.',
    '경주 전 1등 포로를 <b>무료 포인트</b>로 예측합니다. 포인트는 돈으로 살 수 없고 현금으로 바꿀 수 없습니다.',
    '<b>관객 개입</b>: 모든 관객이 한 판에 한 번씩 눈덩이를 던지거나 갈림길 지름길에 투표할 수 있습니다. 누구나 똑같이 한 번이라 공정하면서, 영상과 달리 "내가 한 일"이 생깁니다.'])),
])
section('poro', f'''
<section class="r-frel" id="poro">
  <div class="wrap">
    <div class="sec-head">
      <div><div class="sec-no">4-2 · 광장 즉석 놀이</div><h2>보다가, 뛰다가, 붙다가</h2></div>
      <p>짧고, 언제 빠져도 남에게 피해가 없다. 큐가 잡히면 그냥 떠난다.</p>
    </div>
    <div class="grid g3" style="margin-bottom:18px">
      <div class="card"><span class="tag">붙기</span><h3>1:1 구역</h3><p class="one">문도 피구 · 카서스 1:1 · 둘만 가둬 놓고 죽일 때까지</p></div>
      <div class="card"><span class="tag">뛰기</span><h3>점프 레이스</h3><p class="one">솔방울 · 점멸 · 떨어지면 체크포인트</p></div>
      <div class="card"><span class="tag">보기</span><h3>포로 경주</h3><p class="one">응원 · 예측 · 관객도 한 번씩 개입</p></div>
    </div>
    <div class="flat">{poro_body}</div>
  </div>
</section>''')

# ---------- 4-3 하루 ----------
rep('<p class="q" data-k="4">“이건 실력 차이가 안 나네.”</p>', '<p class="q" data-k="4">“떨어져도 웃기네.”</p>')
rep('<span class="sk">01 · 접속</span><p class="sl">1위 학회 광장 · 꽃가루</p>', '<span class="sk">01 · 광장 입장</span><p class="sl">1위 학회 안뜰 · 꽃가루</p>')
rep('<span class="sk">02 · 소식판</span><p class="sl">바뀐 것 · 시즌 상황 훑기</p>', '<span class="sk">02 · 게시판</span><p class="sl">이번 주 순위 · 바뀐 것 훑기</p>')
rep('<span class="sk">03 · 친구</span><p class="sl">클릭 → 파티</p>', '<span class="sk">03 · 친구</span><p class="sl">광장에 선 친구 클릭 → 파티 · 큐</p>')
rep('<span class="sk">04 · 숨바꼭질</span><p class="sl">5분 · 공부 없이 손 풀기</p>', '<span class="sk">04 · 점프 레이스</span><p class="sl">큐 돌리며 한 판 · 공부 없이 손 풀기</p>')
rep('<span class="sk">05 · 협곡</span><p class="sl">가렌 + 승리 학회 효과</p>', '<span class="sk">05 · 큐 잡힘</span><p class="sl">광장을 떠나 협곡 · 가렌 + 승리 학회 효과</p>')

# ---------- PART 05 확장 ----------
section('roadmap', '''
<section class="r-shurima" id="roadmap">
  <div class="wrap">
    <div class="sec-head">
      <div><div class="sec-no">PART 05 · 단계별 확장</div><h2>롤 안에서 증명하고, MMO로 잇는다</h2></div>
      <p>1단계 지표가 좋아야 다음으로 갑니다.</p>
    </div>
    <div class="grid g2">
      <div class="card"><span class="tag">1단계</span><h3>롤 안의 광장 모드</h3><p class="one">학회 본단 안뜰 · 즉석 놀이 3종 · 숨바꼭질 정식 모드 · 시즌 학회 순위</p></div>
      <div class="card tint"><span class="tag">다음</span><h3>라이엇 MMO로 잇기</h3><p class="one">새로 만들지 않는다 · 내 소환사 · 학회 소속 · 시즌 기록이 MMO로 넘어간다</p></div>
    </div>
    <div style="margin-top:18px">
      <div class="acc">
        <button class="acc-btn" aria-expanded="false"><span>다음으로 넘어가는 기준<span class="sum">무엇이 좋아져야 MMO 연결을 제안하나</span></span><span class="plus" aria-hidden="true">+</span></button>
        <div class="acc-body"><div><div class="acc-inner">
          <ul>
            <li>광장을 쓴 그룹이 안 쓴 그룹보다 <b>주간 판 수, 패배 후 바로 종료 비율, 복귀 유저 재이탈</b> 중 둘 이상에서 나아질 것.</li>
            <li>협곡을 하지 않고 광장 · 놀이만 이용한 접속이 꾸준히 생길 것. "머물 이유"가 증명된 상태입니다.</li>
            <li>MMO 연결은 새로 만드는 게임이 아닙니다. 라이엇이 개발 중인 롤 MMO가 나올 때, 쌓인 소환사 · 학회 기록을 넘겨주는 연결입니다.</li>
          </ul>
          <span class="note">기준의 구체적인 목표치는 1단계 출시 전 데이터로 정합니다.</span>
        </div></div></div>
      </div>
      <div class="acc"><button class="acc-btn" aria-expanded="false"><span>1단계에 만든 것은 버려지지 않는다<span class="sum">소환사 · 학회 기록이 MMO로 그대로</span></span><span class="plus" aria-hidden="true">+</span></button><div class="acc-body"><div><div class="acc-inner"><div class="timeline">
      <div class="tl" style="grid-template-columns:160px 1fr"><b>학회 기록</b><span>시즌 기록 → MMO 속 학회의 역사</span></div>
      <div class="tl" style="grid-template-columns:160px 1fr"><b>본단 디자인</b><span>광장 안뜰 → MMO의 소환사들의 도시</span></div>
    </div><p style="margin-top:10px"><b>회사에게</b> 1단계 비용 = 다음의 기반 · <b>라이엇에게</b> MMO가 나오기 전까지 유저를 붙잡고, MMO 수요를 미리 확인 · <b>유저에게</b> 처음부터 함께한 학회가 MMO로</p></div></div></div></div>
    </div>
  </div>
</section>''')

# ---------- PART 06 실행 가능성 ----------
rep('<p class="one">소환사 꾸미기 · 광장 감정표현 · 학회 의상 — 경쟁에 영향 주는 상품 0</p>',
    '<p class="one">협곡 밖에서도 스킨이 보인다 · 감정표현 · 학회 장식 — 경쟁에 영향 주는 상품 0</p>')
between('<span>판매 구조', '<ul>', '</ul>', '''<ul>
          <li><b>스킨이 주인공</b>: 광장 · 즉석 놀이 · 숨바꼭질 모두 내 챔피언 · 스킨으로 합니다. 협곡을 덜 해도 스킨을 살 이유가 줄지 않습니다. 롤의 주 수익원을 그대로 지키는 구조입니다.</li>
          <li><b>스킨 무대</b>: 귀환 무대 · 1:1 구역 시상 · 숨바꼭질 생존자 무대처럼, 스킨의 귀환 모션과 이펙트가 크게 보이는 자리를 곳곳에 둡니다.</li>
          <li><b>상점 단품</b>: 광장용 감정표현 · 걸음 이펙트를 단품으로 팝니다.</li>
          <li><b>시즌 한정 학회 장식</b>: 학회 색 · 문양을 담은 감정표현 · 깃발. 승리 보상(협곡 외형)과는 별개입니다.</li>
          <li><b>무료로도 얻는다</b>: 시즌 참여, 포로 경주 포인트 교환으로 기본 꾸밈을 얻습니다.</li>
          <li><b>팔지 않는 것</b>: 학회 기여, 순위, 협곡 능력치, 예측 포인트. 경쟁과 결과에 닿는 것은 팔지 않습니다.</li>
        </ul>''')
rep('<span class="sum">광장을 켠 그룹과 끈 그룹을 나란히 본다</span>', '<span class="sum">광장을 쓴 그룹과 안 쓴 그룹을 나란히 본다</span>')
rep('<li><b>부작용도 본다</b>: 광장을 끄는 비율, 신고율, 랭크 매칭 시간이 나빠지지 않는지 함께 봅니다.</li>',
    '<li><b>부작용도 본다</b>: 광장에서 큐가 잡혔을 때 수락을 놓치는 비율, 신고율, 랭크 매칭 시간이 나빠지지 않는지 함께 봅니다.</li>')
between('<span>리스크와 대응', '<table>', '</table>', '''<table>
      <tr><th style="width:30%">우려</th><th>대응</th></tr>
      <tr><td>개발 비용</td><td>새 게임이 아니라 롤 안의 모드 하나 · 아레나의 경기장 · 라운드 초기화 · 여러 팀 구조와 협곡 맵 · 와드 · 렌즈를 다시 씀 · 룬테라 도시는 만들지 않고 MMO로</td></tr>
      <tr><td>큐는 어떻게?</td><td>광장과 클라이언트를 잇는 큐 통로 하나 · 잡히면 광장을 닫고 챔피언 선택으로 · 늘어나는 건 광장 종료 몇 초</td></tr>
      <tr><td>스킨 여러 개, 저사양 PC</td><td>MMO 마을 방식(채널 20~40명 · 가까운 사람만 자세히 · 이펙트 제한) · 광장용 가벼운 스킨(겉모습 · 걷기 · 감정표현 · 귀환만)</td></tr>
      <tr><td>방플</td><td>숨바꼭질은 같은 파티가 같은 팀 · 잡힌 사람은 우리 팀 시야만 · 1:1 구역은 개인전이라 영향 작음</td></tr>
      <tr><td>랭크 스트레스</td><td>숨바꼭질 일반전이 기본 · 랭크는 따로, 져도 조금만 내려감 · 신규 유저는 조건을 채운 뒤</td></tr>
      <tr><td>경쟁 공정성</td><td>보상은 외형뿐 · 놀이는 이동 속도 · 스펙을 모두 같게</td></tr>
      <tr><td>협곡 시간 잠식</td><td>대기 시간 활용 · 협곡 한두 판의 기여를 크게 · 복귀 · 신규 유입</td></tr>
      <tr><td>라이엇 MMO와 겹침</td><td>경쟁하지 않는다 · MMO 전까지 유저를 붙잡고, 기록을 MMO로 넘긴다</td></tr>
      <tr><td>학회 쏠림</td><td>1인당 평균 기여로 순위</td></tr>
    </table>''')

# ---------- PART 07 결론 ----------
rep('<tr><td>지친 날</td><td>접속 이유 없음</td><td>보기만 해도 되는 모드</td></tr>',
    '<tr><td>대기 시간</td><td>타이머만 본다</td><td>광장에서 놀다가 떠난다</td></tr>\n      <tr><td>지친 날</td><td>접속 이유 없음 · 영상으로</td><td>1~3분 놀이 · 보기만 해도 개입</td></tr>')
rep('<tr><td>TFT 전설이</td><td>클릭으로 움직이는 작은 캐릭터 · 꾸밈 상품</td><td>경기 결과가 광장의 풍경과 학회 순위로 남는다</td></tr>',
    '<tr><td>유저가 만든 사용자 설정 놀이</td><td>문도 피구 · 카서스 1:1 같은 규칙</td><td>방을 만들고 사람을 모을 필요 없이, 광장에서 줄 서면 바로 한다</td></tr>')
rep('<tr><td>LoL 아레나 등 기간 모드</td><td>기존 클라이언트에 새 모드로 추가</td><td>조작 · 패치 공부가 필요 없고, 보기만 해도 참여</td></tr>',
    '<tr><td>LoL 아레나 등 기간 모드</td><td>새 모드로 추가 · 경기장 · 라운드 초기화</td><td>전투 없는 광장이 바탕 · 놀이는 짧고 언제 떠나도 된다</td></tr>')
rep('<td>새 게임 없이 기존 클라이언트 위 · 매주 순위로 모습이 바뀐다</td>', '<td>새 게임 없이 롤 안의 모드 하나 · 매주 학회 순위로 모습이 바뀐다</td>')
rep('<td>협곡 밖</td><td>메뉴 화면</td><td>친구가 있는 학회 광장</td>', '<td>협곡 밖</td><td>메뉴 화면</td><td>친구가 있는 광장 · 내 스킨의 무대</td>')

rep('<span class="sum">같은 클라이언트, 다른 이유로 접속한다</span>', '<span class="sum">같은 광장, 다른 이유로 들어온다</span>')

rep('<em>3~5분이면 끝나는 한 판</em>', '<em>1~3분이면 끝나는 즉석 놀이</em>')

# 표 스타일 (2-2 비교표)
rep('</head>', '<style>.why-t{width:100%;border-collapse:collapse;background:#fff;border:1px solid #E6E8EB;border-radius:14px;overflow:hidden;font-size:15px}.why-t th,.why-t td{padding:12px 16px;border-top:1px solid #EEF0F2;text-align:left}.why-t th{background:#F7F8FA;border-top:0}</style>\n</head>')

for bad in ['쿼터뷰', '전설이', '꾸밈 슬롯', '독립 클라이언트', '2단계', '광장을 켠', '관전형 모드', '포탈에 들어서면', 'stage1.jpg']:
    assert bad not in re.sub(r'<script.*?</script>|<style.*?</style>', '', s, flags=re.S), bad

s = s.replace('lol-plan-v14', 'lol-plan-v15')
open('versions/lol-plan-v15.html', 'w', encoding='utf-8').write(s)
print('ok')
