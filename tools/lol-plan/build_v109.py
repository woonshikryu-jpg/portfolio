# v108 -> v109: 3-2 제목 「협곡의 결과가, 학회의 역사로」(기록 → 역사), PART 03 강조색 주황 → 남색(인디고)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v108.html', encoding='utf-8').read()
s = s.replace('v108</title>', 'v109</title>')
old = '<h2>협곡의 결과가 학회의 <em class="kw kp3">기록</em>으로</h2>'
assert s.count(old) == 1
s = s.replace(old, '<h2>협곡의 결과가, 학회의 <em class="kw kp3">역사</em>로</h2>')
k = s.rindex('</style>'); s = s[:k] + '.kp3{--kl:#3B4FD8;--kd:#AEBBFF}\n' + s[k:]
s = s.replace('lol-plan-v108', 'lol-plan-v109')
open('versions/lol-plan-v109.html', 'w', encoding='utf-8').write(s)
print('ok')
