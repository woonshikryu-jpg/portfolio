# v50 -> v51: PART 06 표현 정리 — 「한 판의 질」→「경기 매너」, 「먼저 물을 질문에, 먼저 답한다」→「예상되는 우려와 대응」,
# 「큐는 어떻게」→「큐 연결」, 「방플」→「고의 방해 플레이」(리스크 표 · 지표 표 포함)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v50.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v50</title>', 'v51</title>')
rep('협곡 한 판의 질(항복 · 탈주) · 복귀 재이탈', '협곡 경기 매너(항복 · 탈주 · 신고) · 복귀 재이탈')
rep('<h3>먼저 물을 질문에, 먼저 답한다</h3><p class="one">큐는 어떻게 · 저사양 PC · 개발 비용 · 방플 · 랭크 스트레스</p>',
    '<h3>예상되는 우려와 대응</h3><p class="one">큐 연결 · 저사양 PC · 개발 비용 · 고의 방해 플레이 · 랭크 스트레스</p>')
rep('접속 · 스킨 · 한 판의 질이 유지되면 성공이다', '접속 · 스킨 · 경기 매너가 유지되면 성공이다')
rep('<tr><td>협곡 한 판의 질</td>', '<tr><td>협곡 경기 매너</td>')
rep('<tr><td>방플</td>', '<tr><td>고의 방해 플레이</td>')
rep('<tr><td>큐는 어떻게?</td>', '<tr><td>큐 연결</td>')
rep('<span class="sum">먼저 묻게 될 질문에, 먼저 답한다</span>', '<span class="sum">우려마다 어떻게 막는지</span>')
assert '한 판의 질' not in s and '방플' not in s
s = s.replace('lol-plan-v50', 'lol-plan-v51')
open('versions/lol-plan-v51.html', 'w', encoding='utf-8').write(s)
print('ok')
