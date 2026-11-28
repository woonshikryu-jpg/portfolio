# v107 -> v108: 강조색 조정 — 표지 「숨어」는 강조 없이 제목 아이보리로, PART 04 노랑, PART 05 하늘색(보라 대신), PART 06 분홍, PART 07 초록
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v107.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v107</title>', 'v108</title>')
rep('<h2><em class="kw kp0">숨어</em> 사는 소환사들</h2>', '<h2>숨어 사는 소환사들</h2>')
css = ('.kp4{--kl:#C99A00;--kd:#FFDF4A}'   # 캐주얼 모드 — 노랑
       '.kp5{--kl:#1A84D6;--kd:#8ED4FF}'   # 확장 계획 — 하늘색
       '.kp6{--kl:#D02A72;--kd:#FF9EC6}'   # 실행 가능성 — 분홍
       '.kp7{--kl:#1F8A3E;--kd:#7BE38E}\n') # 결론 PART — 초록
k = s.rindex('</style>'); s = s[:k] + css + s[k:]
s = s.replace('lol-plan-v107', 'lol-plan-v108')
open('versions/lol-plan-v108.html', 'w', encoding='utf-8').write(s)
print('ok')
