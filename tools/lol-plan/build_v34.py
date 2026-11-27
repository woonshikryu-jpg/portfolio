# v33 -> v34: 2-1 「문제마다 어떤 장치가 대응하나」 — 패치 공부는 숨바꼭질만(지금 패치 그대로 쓰는 협곡),
# 복귀 격차는 협곡 규칙 · 시야(숨바꼭질) + 손 감각(1:1 구역)으로 나눔
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v33.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert old in s, old[:60]; s = s.replace(old, new, 1)
s = s.replace('v33</title>', 'v34</title>')
rep('<tr><td>패치 공부</td><td>1레벨 · Q 하나로 하는 1:1 구역 · 사물을 복제해 숨는 숨바꼭질</td><td>4-1 · 4-2</td></tr>',
    '<tr><td>패치 공부</td><td>지금 패치의 챔피언 · 아이템을 그대로 쓰는 숨바꼭질. 랭크 점수 걱정 없이 바뀐 점을 직접 써 본다</td><td>4-1</td></tr>')
rep('<tr><td>복귀 격차</td><td>바뀐 협곡 · 아이템 · 조작을 랭크 점수 부담 없이 다시 익히는 숨바꼭질</td><td>4-1</td></tr>',
    '<tr><td>복귀 격차</td><td>바뀐 협곡 규칙 · 시야를 다시 익히는 숨바꼭질 · Q 하나로 손 감각을 되찾는 1:1 구역</td><td>4-1 · 4-2</td></tr>')
s = s.replace('lol-plan-v33', 'lol-plan-v34')
open('versions/lol-plan-v34.html', 'w', encoding='utf-8').write(s)
print('ok')
