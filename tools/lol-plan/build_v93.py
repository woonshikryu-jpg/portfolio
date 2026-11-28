# v92 -> v93: 핵심 질문 「그렇다면 지친 날의 소환사는」 → 「경쟁에 지친 소환사는」 (첫 띠 + 마지막 띠 질문 둘 다)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v92.html', encoding='utf-8').read()
s = s.replace('v92</title>', 'v93</title>')
old = '그렇다면 지친 날의 소환사는,<br>'
assert s.count(old) == 2, s.count(old); s = s.replace(old, '경쟁에 지친 소환사는,<br>')
s = s.replace('lol-plan-v92', 'lol-plan-v93')
open('versions/lol-plan-v93.html', 'w', encoding='utf-8').write(s)
print('ok')
