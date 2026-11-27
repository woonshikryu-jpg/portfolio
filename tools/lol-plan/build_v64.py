# v63 -> v64: 왼쪽 PART 목차 — 점뿐 아니라 번호(01~07) 알약을 눌러도 그 PART로 이동
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v63.html', encoding='utf-8').read()
s = s.replace('v63</title>', 'v64</title>')
k = s.rfind('</style>')
s = s[:k] + '.rail a span{pointer-events:auto!important;cursor:pointer}.rail a span:hover{background:rgba(30,26,22,.85)}\n' + s[k:]
s = s.replace('lol-plan-v63', 'lol-plan-v64')
open('versions/lol-plan-v64.html', 'w', encoding='utf-8').write(s)
print('ok')
