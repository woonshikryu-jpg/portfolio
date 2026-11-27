# v34 -> v35: 한 장 요약 두 번째 기둥 「광장 놀이 & 소통 · 숨바꼭질 모드」,
# 3-2 01 「시즌 갈등 · 녹서스 vs 데마시아」→「시즌 개막 · 세 학회가 0점에서 출발」(룬테라 이야기 속 대립이 아니라 학회 리그),
# 시즌 리그 진행의 「데마시아 vs 녹서스 라이벌전」 예시도 같은 이유로 수정
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v34.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert old in s, old[:60]; s = s.replace(old, new, 1)
s = s.replace('v34</title>', 'v35</title>')
rep('<p class="one">광장 즉석 놀이 · 숨바꼭질 모드 · 패치 공부 0</p>', '<p class="one">광장 놀이 &amp; 소통 · 숨바꼭질 모드</p>')
rep('<h3>시즌 갈등</h3><p class="one">녹서스 vs 데마시아</p>', '<h3>시즌 개막</h3><p class="one">세 학회가 0점에서 출발</p>')
rep('<li><b>시즌 시작</b>: 광장 소식판에 이번 시즌 리그가 열립니다. 예: "데마시아 학회 vs 녹서스 학회, 이번 시즌 라이벌전."</li>',
    '<li><b>시즌 시작</b>: 광장 소식판에 이번 시즌 리그가 열립니다. 세 학회 모두 0점에서 출발하고, 지난 시즌 순위는 이어지지 않습니다.</li>')
s = s.replace('lol-plan-v34', 'lol-plan-v35')
open('versions/lol-plan-v35.html', 'w', encoding='utf-8').write(s)
print('ok')
