# v17 -> v18: 4-3 한 소환사의 하루 삭제(지어낸 반응 대사 · 한 장 요약 「유저의 하루」와 겹침), 목차 이름 정리
#  PART 03 1단계 설계 → 광장 모드 설계 / PART 04 캐주얼 모드와 하루 → 캐주얼 모드 / PART 05 단계별 확장 → 확장 계획
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v17.html', encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) >= n, old[:60]; s = s.replace(old, new, n)
s = s.replace('v17</title>', 'v18</title>')

# 4-3 섹션 삭제
i = s.find('id="day"'); a = s.rfind('<section', 0, i); b = s.find('</section>', a) + len('</section>')
s = s[:a] + s[b:]

# PART 이름
rep('PART 03 · 1단계 설계', 'PART 03 · 광장 모드 설계', s.count('PART 03 · 1단계 설계'))
rep('<div class="sec-no">3-0 · 1단계에서 만드는 것</div>', '<div class="sec-no">3-0 · 만드는 것</div>')
rep('<h2>협곡의 결과가 학회의 이야기로</h2>', '<h2>협곡의 결과가 학회의 기록으로</h2>')
rep('PART 04 · 캐주얼 모드와 하루', 'PART 04 · 캐주얼 모드', s.count('PART 04 · 캐주얼 모드와 하루'))
rep('<p>가볍게 노는 모드, 그리고 한 소환사의 하루</p>', '<p>협곡의 숨바꼭질, 광장의 즉석 놀이</p>')
rep('PART 05 · 단계별 확장', 'PART 05 · 확장 계획', s.count('PART 05 · 단계별 확장'))
# 목차(왼쪽 진행 표시)
rep('<i>1단계 설계</i>', '<i>광장 모드 설계</i>')
rep('<i>캐주얼 모드와 하루</i>', '<i>캐주얼 모드</i>')
rep('<i>단계별 확장</i>', '<i>확장 계획</i>')

assert 'id="day"' not in s and '석 달 만에 돌아온 소환사' not in s
s = s.replace('lol-plan-v17', 'lol-plan-v18')
open('versions/lol-plan-v18.html', 'w', encoding='utf-8').write(s)
print('ok')
