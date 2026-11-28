# v94 -> v95: 결론 아래 문장에 팀과의 유대 — 광장에서 만난 학회원과 한 팀이 된다
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v94.html', encoding='utf-8').read()
s = s.replace('v94</title>', 'v95</title>')
old = '<span class="fs-b">경쟁에 지친 소환사는,<br>학회 사람들이 기다리는 <em class="kw">광장</em>으로 간다.</span>'
assert s.count(old) == 1
s = s.replace(old, '<span class="fs-b">경쟁에 지친 소환사는,<br><em class="kw">광장</em>에서 만난 학회원과 <em class="kw">한 팀</em>이 된다.</span>')
s = s.replace('lol-plan-v94', 'lol-plan-v95')
open('versions/lol-plan-v95.html', 'w', encoding='utf-8').write(s)
print('ok')
