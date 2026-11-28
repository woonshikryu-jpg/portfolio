# v109 -> v110: 한 장 요약 제목 강조색 탁한 황토 → 보라(밝은 배경용만 바꿈, 핵심 · 결론 띠의 금색은 그대로)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v109.html', encoding='utf-8').read()
s = s.replace('v109</title>', 'v110</title>')
k = s.rindex('</style>'); s = s[:k] + '.kp0{--kl:#7048E8}\n' + s[k:]
s = s.replace('lol-plan-v109', 'lol-plan-v110')
open('versions/lol-plan-v110.html', 'w', encoding='utf-8').write(s)
print('ok')
