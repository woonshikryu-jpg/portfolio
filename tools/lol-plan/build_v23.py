# v22 -> v23: 4-1 숨바꼭질 규칙 재작성 (사용자 결정)
#  - 18분은 길다(챔피언 선택도 있음) → 라운드 최대 5분, 전체 최대 약 11분
#  - 미니언 · 포탑은 기존 시스템 그대로(웨이브끼리 싸움, 포탑 파괴) → 위치 변수
#  - 술래 팀만 무적, 골드가 많아 템이 앞섬. 잡기 = 협곡 전투로 체력을 0으로
#  - 잡히면 그 자리에서 술래 팀으로 부활(감염식). 5명 다 잡으면 바로 공수 교대
#  - 점수 = 버틴 시간 + 미션 점수
import os, re
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v22.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert old in s, old[:60]; s = s.replace(old, new, 1)
def section(id_, new):
    global s
    i = s.find(f'id="{id_}"'); a = s.rfind('<section', 0, i); b = s.find('</section>', a) + len('</section>')
    s = s[:a] + new.strip() + s[b:]
s = s.replace('v22</title>', 'v23</title>')

def acc(n, title, sum_, body, must=False, wide=False):
    num = f'<span class="n">{n}</span>' if n else ''
    st = ' style="grid-column:1/-1"' if wide else ''
    return (f'<div class="fi"{st}><div class="acc{" must" if must else ""}"><button class="acc-btn" aria-expanded="{"true" if must else "false"}">{num}'
            f'<span>{title}<span class="sum">{sum_}</span></span><span class="plus" aria-hidden="true">+</span></button>'
            f'<div class="acc-body"><div><div class="acc-inner">{body}</div></div></div></div></div>')
def ul(items): return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'

body = ''.join([
  acc(1, '한 판 흐름', '라운드 최대 5분, 전체 최대 약 11분', '''<table>
              <tr><th>단계</th><th>시간</th><th>일어나는 일</th></tr>
              <tr><td>챔피언 선택</td><td>약 1분</td><td>투명 · 위장 스킬이 있는 챔피언은 고를 수 없음</td></tr>
              <tr><td>숨기</td><td>30초</td><td>1라운드는 블루팀이 숨음. 술래 팀은 우물에서 화면이 가려진 채 대기</td></tr>
              <tr><td>수색</td><td>최대 4분 30초</td><td>잡힌 도망자는 그 자리에서 술래 팀으로 부활. 술래가 점점 늘어남. 마지막 1분은 바깥쪽부터 구역이 닫힘</td></tr>
              <tr><td>교대</td><td>즉시</td><td>도망자 5명을 다 잡거나 시간이 끝나면 바로 역할을 바꿔 2라운드</td></tr>
              <tr><td>결과</td><td>15초</td><td>두 라운드 점수 비교 · 마지막 생존자의 귀환 무대</td></tr>
            </table><span class="note">빨리 다 잡을수록 판이 짧아집니다. 시간은 예시이며 테스트로 확정합니다.</span>''', must=True),
  acc(2, '도망자 팀', '니코처럼 숨고, 스킬로 도망친다', ul([
    '<b>[복제]</b>: 가까운 사물을 클릭하면 그 모습이 됩니다. 와드 · 정글 몹 · 식물 · 미니언. 니코 패시브와 같아서 챔피언에게 피해를 받으면 풀립니다. 쿨타임 10초.',
    '<b>미니언 웨이브에 섞이기</b>: 미니언은 기존처럼 싸우고 죽습니다. 웨이브가 다 죽었는데 나만 남아 있거나, 혼자 걸음이 다르면 들킵니다. 웨이브가 어디서 부딪히느냐가 매번 달라서 숨을 자리도 매번 바뀝니다.',
    '<b>들키면 도망친다</b>: 술래는 무적이라 맞서 싸워도 소용없습니다. 돌진 · 둔화 · 점멸로 시야 밖으로 빠져나가 다시 숨습니다.',
    '<b>와드 · 렌즈</b>: 술래가 오는 길목에 와드를 박고, 렌즈로 술래의 와드를 지웁니다.'])),
  acc(3, '술래 팀', '무적 · 골드가 많아 템이 앞선다', ul([
    '<b>무적</b>: 술래 팀만 체력이 줄지 않습니다. 잡는 데만 집중합니다.',
    '<b>잡기 = 협곡 전투 그대로</b>: 스킬과 공격으로 도망자의 체력을 0으로 만들면 잡힙니다. 따로 배울 규칙이 없습니다.',
    '<b>찾기</b>: 렌즈로 복제한 사람을 드러내고, 의심 가는 사물 · 미니언을 스킬로 때려 봅니다. 마나와 쿨타임이 있어 아무 데나 난사할 수는 없습니다.',
    '<b>잡힌 사람이 합류</b>: 잡힌 도망자는 그 자리에서 술래 팀으로 부활합니다. 술래로 바뀌니 위치가 드러나도 헷갈릴 일이 없고, 잡힌 사람도 쉬지 않고 계속 플레이합니다.'])),
  acc(4, '협곡 맵에서 바꾸는 것', '미니언 · 포탑은 그대로, 챔피언만 안 때린다', ul([
    '<b>미니언 · 포탑은 기존 시스템 그대로</b>: 웨이브끼리 싸우고, 포탑도 부서집니다. 포탑이 무너지면 그 주변 지형이 열려 숨는 판도가 바뀝니다.',
    '<b>단, 미니언 · 포탑은 챔피언을 공격하지 않습니다.</b> 한쪽 팀 미니언이 숨은 사람을 때려 위치를 알려 주거나, 포탑이 한 팀만 막아 주는 일을 막습니다.',
    '<b>골드 · 경험치</b>: 미니언 · 정글 몹으로는 얻지 않습니다. 레벨은 양 팀 같게 고정(예: 11레벨)합니다.',
    '<b>라인 부쉬 추가</b> · <b>이동 속도는 협곡보다 조금 빠르게, 모두 같게</b>.'])),
  acc(5, '골드', '술래가 더 벌고, 미니언으로는 안 번다', '''<table>
              <tr><th style="width:22%"></th><th>술래 팀</th><th>도망자 팀</th></tr>
              <tr><td>시작 골드</td><td>1,400</td><td>500</td></tr>
              <tr><td>시간당</td><td>초당 4</td><td>초당 1</td></tr>
              <tr><td>추가</td><td>잡을 때 +300(도운 사람과 나눔)</td><td>미션 완료 +150</td></tr>
              <tr><td>상점</td><td colspan="2">협곡과 같이 우물에서 삽니다</td></tr>
            </table><span class="note">수치는 예시이며 테스트로 확정합니다. 술래는 시간이 갈수록 템이 앞서 후반엔 들키면 거의 잡힙니다.</span>'''),
  acc(6, '승패와 점수', '버틴 시간 + 미션 점수', ul([
    '<b>도망자의 미션 = 끝까지 안 잡히기.</b> 한 명이 1초 버틸 때마다 1점입니다.',
    '<b>추가 미션</b>: 정찰 열매 따기, 정해진 자리에 와드 박기, 미니언 웨이브와 함께 라인 끝까지 가기. 하나에 30점 + 골드 150. 숨은 자리에서 나와야 해서, 한곳에 박혀만 있는 판이 되지 않습니다.',
    '<b>술래의 미션 = 다 잡기.</b> 빨리 다 잡을수록 상대 점수가 낮아지고 바로 우리 차례가 옵니다. 잡을 이유가 분명합니다.',
    '<b>라운드 점수 = 도망자 팀의 버틴 시간 + 미션 점수.</b> 두 라운드에서 각 팀이 도망자로서 얻은 점수를 비교합니다.'])),
  acc(7, '일반전과 랭크전', '랭크는 따로, 잘 안 깎이게', ul([
    '<b>일반전</b>이 기본입니다. 신규 유저는 여기서 시작합니다.',
    '<b>랭크전</b>은 따로 둡니다. 시즌제 등급이고, 이기면 크게 오르고 져도 조금만 내려갑니다.',
    '랭크전은 레벨 · 일반전 판 수 조건을 둡니다. 보상은 학회 기여와 등급별 꾸밈입니다.'])),
  acc('', '놀면서 익히는 협곡', '숨바꼭질이 협곡의 입구가 되는 이유', '''<table>
              <tr><th style="width:30%">숨바꼭질에서</th><th>협곡에서 쓰는 감각</th></tr>
              <tr><td>와드 박을 길목 고르기</td><td>시야 장악</td></tr>
              <tr><td>렌즈로 숨은 사람 찾기</td><td>상대 와드 지우기</td></tr>
              <tr><td>미니언 웨이브에 섞여 다니기</td><td>라인 · 웨이브가 부딪히는 자리</td></tr>
              <tr><td>정글 몹으로 복제하기</td><td>정글 캠프 위치</td></tr>
              <tr><td>들키면 스킬로 빠져나가기</td><td>내 챔피언의 돌진 · 둔화 쓰임새</td></tr>
              <tr><td>협곡 전체를 누비기</td><td>라인 · 강 · 정글 · 부쉬 지도</td></tr>
            </table>''', must=True),
])

section('hide', f'''
<section class="r-frel alt" id="hide">
  <div class="wrap">
    <div class="sec-head">
      <div><div class="sec-no">4-1 · 정식 모드</div><h2>숨바꼭질: 협곡에서,<br>모두가 니코가 된다</h2></div>
    </div>
    <div class="grid g4" style="margin-bottom:18px">
      <div class="card"><span class="tag">맵</span><h3>협곡 그대로</h3><p class="one">미니언 · 포탑 기존대로 · 라인 부쉬 추가</p></div>
      <div class="card"><span class="tag">숨기</span><h3>사물 복제</h3><p class="one">니코처럼 · 미니언 웨이브에 섞이기</p></div>
      <div class="card"><span class="tag">찾기</span><h3>무적 술래</h3><p class="one">골드가 많아 템이 앞선다 · 잡히면 술래가 된다</p></div>
      <div class="card"><span class="tag">승패</span><h3>5명 다 잡으면 교대</h3><p class="one">2라운드 · 버틴 시간 + 미션 점수</p></div>
    </div>
    <div class="flat">{body}</div>
  </div>
</section>''')

rep('방플</td><td>숨바꼭질은 같은 파티가 같은 팀 · 잡힌 사람은 우리 팀 시야만 · 1:1 구역은 개인전이라 영향 작음',
    '방플</td><td>숨바꼭질은 같은 파티가 같은 팀 · 잡히면 술래 팀으로 합류 · 1:1 구역은 개인전이라 영향 작음')

for bad in ['3초 멈춤', '15분', '우리 팀 시야만', '+ 목표']:
    assert bad not in re.sub(r'<script.*?</script>|<style.*?</style>', '', s, flags=re.S), bad
s = s.replace('lol-plan-v22', 'lol-plan-v23')
open('versions/lol-plan-v23.html', 'w', encoding='utf-8').write(s)
print('ok')
