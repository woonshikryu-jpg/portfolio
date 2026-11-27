# v26 -> v27: 한 장 요약 「유저의 하루」 표 — 복귀 · 캐주얼 · 신규 유저 줄 수정
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v26.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert old in s, old[:60]; s = s.replace(old, new, 1)
s = s.replace('v26</title>', 'v27</title>')
rep('<td>공부가 필요 없는 숨바꼭질로 손을 풀고, 소식판으로 바뀐 것만 훑는다</td>',
    '<td>숨바꼭질에서 바뀐 협곡 지형 · 아이템과 내 챔피언 조작을 랭크 점수 부담 없이 다시 익히고, 1:1 구역에서 손을 푼 뒤 협곡으로 간다</td>')
rep('<td>학회원으로 이름만 올려도 시즌 리그에 참여한다</td>',
    '<td>학회원으로 이름만 올려도 시즌 리그에 참여하고, 랭크 대신 숨바꼭질 · 광장 즉석 놀이 같은 캐주얼 모드로 부담 없이 즐긴다</td>')
rep('<td>숨바꼭질로 협곡 지도 · 와드 · 렌즈를, 광장 놀이로 스킬 감각을 학습 없이 먼저 익히고, 학회로 응원할 팀이 생긴다</td>',
    '<td>숨바꼭질로 협곡 지도 · 와드 · 렌즈를, 광장 놀이로 조작 감각을 부담 없이 먼저 익히고, 학회로 소속감이 생긴다</td>')
s = s.replace('lol-plan-v26', 'lol-plan-v27')
open('versions/lol-plan-v27.html', 'w', encoding='utf-8').write(s)
print('ok')
