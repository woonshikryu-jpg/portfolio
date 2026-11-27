# v20 -> v21: PART 07 결론 표 문구 — 지친 날 「포로 경주 관전 · 캐주얼 모드 플레이(숨바꼭질)」,
# MMO 마을 비교 「시즌 순위로 학회 광장이 바뀐다」(매주 맵 업데이트는 현실적으로 어려움)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v20.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert old in s, old[:60]; s = s.replace(old, new, 1)
s = s.replace('v20</title>', 'v21</title>')
rep('<td>1~3분 놀이 · 보기만 해도 개입</td>', '<td>포로 경주 관전 · 캐주얼 모드 플레이(숨바꼭질)</td>')
rep('<td>새 게임 없이 롤 안의 모드 하나 · 매주 학회 순위로 모습이 바뀐다</td>', '<td>새 게임 없이 롤 안의 모드 하나 · 시즌 순위로 학회 광장이 바뀐다</td>')
s = s.replace('lol-plan-v20', 'lol-plan-v21')
open('versions/lol-plan-v21.html', 'w', encoding='utf-8').write(s)
print('ok')
