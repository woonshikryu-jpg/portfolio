# v100 -> v101: 3-3 제목 「이긴 학회는 협곡에서 보인다」 → 「이긴 학회는 협곡에서도 보인다」 (광장 보상 다음, 협곡에서도 보상) — 강조 낱말 「협곡에서도」
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v100.html', encoding='utf-8').read()
s = s.replace('v100</title>', 'v101</title>')
old = '<h2>이긴 학회는 협곡에서 <em class="kw">보인다</em></h2>'
assert s.count(old) == 1
s = s.replace(old, '<h2>이긴 학회는 <em class="kw">협곡에서도</em> 보인다</h2>')
s = s.replace('lol-plan-v100', 'lol-plan-v101')
open('versions/lol-plan-v101.html', 'w', encoding='utf-8').write(s)
print('ok')
