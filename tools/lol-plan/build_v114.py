# v113 -> v114: 검정 테두리 취소(v112 기준으로 되돌림), PART 02 연두만 유지 — 밝은 배경용은 글씨가 읽히는 진한 연두
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v112.html', encoding='utf-8').read()
s = s.replace('v112</title>', 'v114</title>')
k = s.rindex('</style>'); s = s[:k] + '.kp2{--kl:#58A800;--kd:#B6F25A}\n' + s[k:]
s = s.replace('lol-plan-v112', 'lol-plan-v114')
open('versions/lol-plan-v114.html', 'w', encoding='utf-8').write(s)
print('ok')
