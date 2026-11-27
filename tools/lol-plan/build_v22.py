# v21 -> v22: PART 06 전면 수정 — "협곡을 덜 해도 회사는 손해 보지 않는다"를 증명하는 장으로
#  (판 수 ↑ 대신 접속 · 스킨 · 한 판의 질 · 복귀 · 신규를 지표로, 협곡 판 수는 목표가 아님)
# + PART 07 아래 띠, 결말 문구를 PART 01의 문제(점수 하나)와 핵심 질문(머물 이유)에 대한 답으로
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v21.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert old in s, old[:60]; s = s.replace(old, new, 1)
s = s.replace('v21</title>', 'v22</title>')

# ---- PART 06 머리 · 카드 ----
rep('<h2>팔 것, 잴 것, 먼저 답할 것</h2>', '<h2>협곡을 덜 해도,<br>회사는 손해 보지 않는다</h2>')
rep('''<div class="card"><span class="tag">수익 모델</span><h3>스킨에게, 보여 줄 무대를</h3><p class="one">협곡 밖에서도 스킨이 보인다 · 감정표현 · 학회 장식 — 경쟁에 영향 주는 상품 0</p></div>
      <div class="card"><span class="tag">지표 가설</span><h3>남는 게 있으면 한 판 더</h3><p class="one">주간 판 수 · 패배 후 종료 · 복귀 재이탈 · 신규 정착 · 협곡 없는 접속 · 항복률</p></div>
      <div class="card"><span class="tag">리스크</span><h3>협곡의 경쟁은 그대로 둔다</h3><p class="one">비용 · 저사양 PC · 공정성 · 학회 쏠림 · 학회 간 대립</p></div>
    </div>''',
'''<div class="card"><span class="tag">수익</span><h3>스킨이 보일 무대가 늘어난다</h3><p class="one">롤은 능력치가 아니라 외형을 판다 · 지금은 협곡 30분 안에서만 보이는 스킨이, 광장 · 숨바꼭질 · 1:1 구역에서도 보인다</p></div>
      <div class="card"><span class="tag">지표</span><h3>판 수가 아니라, 남아 있는가</h3><p class="one">접속일 · 스킨 구매와 착용 · 협곡 한 판의 질(항복 · 탈주) · 복귀 재이탈 · 신규 정착</p></div>
      <div class="card"><span class="tag">리스크</span><h3>먼저 물을 질문에, 먼저 답한다</h3><p class="one">큐는 어떻게 · 저사양 PC · 개발 비용 · 방플 · 랭크 스트레스</p></div>
    </div>
    <div class="banner" style="margin-top:18px">협곡 판 수가 줄어도, 접속 · 스킨 · 한 판의 질이 유지되면 성공이다</div>''')

# ---- 지표 가설 표 ----
i = s.find('<span>지표 가설 표'); a = s.find('<table>', i); b = s.find('</table>', a) + len('</table>')
s = s[:a] + '''<table>
      <tr><th style="width:22%">지표</th><th>가설</th><th style="width:30%">비교</th></tr>
      <tr><td>주간 접속일</td><td>협곡을 안 하는 날에도 들른다</td><td>광장 이용 그룹 vs 아닌 그룹</td></tr>
      <tr><td>스킨 구매 · 착용</td><td>보여 줄 무대가 늘면 협곡을 덜 해도 줄지 않는다</td><td>광장 이용 그룹 vs 아닌 그룹</td></tr>
      <tr><td>협곡 한 판의 질</td><td>짧게 몰입하면 끝까지 한다 → 항복 · 탈주 · 신고 감소</td><td>도입 전후</td></tr>
      <tr><td>복귀 재이탈</td><td>캐주얼로 감을 되찾으면 덜 떠난다</td><td>캐주얼 경험 유무</td></tr>
      <tr><td>신규 정착</td><td>쉬운 입구가 있으면 협곡까지 간다</td><td>첫 주 캐주얼 경험 유무</td></tr>
      <tr><td>협곡 판 수</td><td><b>목표가 아니다.</b> 줄어도 위 지표가 유지되면 성공</td><td>참고로만 본다</td></tr>
    </table>''' + s[b:]
rep('<span>지표 가설 표<span class="sum">무엇이 좋아지는지, 무엇과 비교하나</span>', '<span>지표 가설 표<span class="sum">무엇을 성공으로 보나</span>')

# ---- PART 07 아래 띠 ----
rep('<div class="banner">판 수 ↑ · 유지 ↑ · 복귀 ↑ · IP 확장</div>', '<div class="banner">접속 유지 · 스킨이 보일 무대 · 복귀와 신규의 입구 · IP 확장</div>')

# ---- 결말 ----
rep('<span class="pn">HIDDEN SUMMONERS</span><h2>내 한 판이,<br>우리 학회의 경기가 된다.</h2><p>유운식 · 게임 기획</p>',
    '<span class="pn">HIDDEN SUMMONERS</span><h2>점수 하나 대신,<br>머물 이유를 남긴다.</h2><p>한 판을 하지 않아도 들르고 싶은 롤<br>유운식 · 게임 기획</p>')
rep('<div class="mark" style="left:30%;top:26%;font-size:calc(var(--u) * 1.1)" data-from="0.4"', '<div class="mark" style="left:34%;top:28%;font-size:calc(var(--u) * 1.1)" data-from="0.4"')

for bad in ['판 수 ↑', '남는 게 있으면 한 판 더', '학회 간 대립']:
    assert bad not in s, bad
s = s.replace('lol-plan-v21', 'lol-plan-v22')
open('versions/lol-plan-v22.html', 'w', encoding='utf-8').write(s)
print('ok')
