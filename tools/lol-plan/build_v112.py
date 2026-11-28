# v111 -> v112: 2-1 제목 「쉼과 기록은 소환사의 도시에서」 → 「휴식은 소환사의 도시에서」 (강조 낱말 휴식)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v111.html', encoding='utf-8').read()
s = s.replace('v111</title>', 'v112</title>')
old = '<h2>경쟁은 협곡에서,<br><em class="kw kp2">쉼</em>과 기록은 소환사의 도시에서</h2>'
assert s.count(old) == 1
s = s.replace(old, '<h2>경쟁은 협곡에서,<br><em class="kw kp2">휴식</em>은 소환사의 도시에서</h2>')
s = s.replace('lol-plan-v111', 'lol-plan-v112')
open('versions/lol-plan-v112.html', 'w', encoding='utf-8').write(s)
print('ok')
