# v29 -> v30: 비유로 쓴 '벽' 표현 정리 — 1-1 「네 개의 벽」→「네 가지 문제」, 2-1 「문제마다 어떤 장치가 대응하나」,
# 결론 표 「실력 격차」, 신규 유저 「막막해진다」. 1-1 제목 옆 한 줄 문구(v19에서 빠진 것) 삭제.
# 2-1 대응 표의 장치 · 위치를 지금 규칙에 맞춤(숨바꼭질은 더 이상 '관찰 · 운 중심'이 아님)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v29.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert old in s, old[:60]; s = s.replace(old, new, 1)
s = s.replace('v29</title>', 'v30</title>')
rep('<div class="sec-no">1-1 · 네 개의 벽</div><h2>왜 남는 게 없을까</h2></div><p>이겨도 져도 점수 하나. 그 앞에 놓인 네 개의 벽.</p>',
    '<div class="sec-no">1-1 · 네 가지 문제</div><h2>왜 남는 게 없을까</h2></div>')
rep('<span>벽마다 어떤 장치가 대응하나<span class="sum">PART 01의 네 벽 → 해결 장치</span>',
    '<span>문제마다 어떤 장치가 대응하나<span class="sum">PART 01의 네 가지 문제 → 해결 장치</span>')
rep('''<tr><th style="width:30%">벽</th><th>장치</th><th>어디서</th></tr>
        <tr><td>한 판의 피로 · 갈등</td><td>관전형 캐주얼 · 머무는 광장</td><td>3-1 · 4-2 광장 즉석 놀이</td></tr>
        <tr><td>패치 공부</td><td>패치와 무관한 캐주얼 규칙</td><td>숨바꼭질 · 포로 경주</td></tr>
        <tr><td>복귀 격차</td><td>관찰 · 운 중심 모드</td><td>숨바꼭질</td></tr>
        <tr><td>남는 건 점수뿐</td><td>학회 순위 · 광장 · 외형</td><td>3-2 · 3-3</td></tr></table>''',
'''<tr><th style="width:30%">문제</th><th>장치</th><th>어디서</th></tr>
        <tr><td>한 판의 피로 · 갈등</td><td>놀다가 큐가 잡히면 떠나는 광장 · 보기만 해도 되는 포로 경주</td><td>3-1 · 4-2</td></tr>
        <tr><td>패치 공부</td><td>1레벨 · Q 하나로 하는 1:1 구역 · 사물을 복제해 숨는 숨바꼭질</td><td>4-1 · 4-2</td></tr>
        <tr><td>복귀 격차</td><td>바뀐 협곡 · 아이템 · 조작을 랭크 점수 부담 없이 다시 익히는 숨바꼭질</td><td>4-1</td></tr>
        <tr><td>남는 건 점수뿐</td><td>학회 순위 · 시즌 광장 · 외형</td><td>3-2 · 3-3</td></tr></table>''')
rep('<td>실력 격차의 벽</td>', '<td>실력 격차</td>')
rep('첫 판부터 배울 것에 막혀 벽을 느낀다.', '첫 판부터 배울 것이 많아 막막해진다.')
s = s.replace('lol-plan-v29', 'lol-plan-v30')
open('versions/lol-plan-v30.html', 'w', encoding='utf-8').write(s)
print('ok')
