# v90 -> v91: 연락처의 「이력서 보기 →」 링크 삭제
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v90.html', encoding='utf-8').read()
s = s.replace('v90</title>', 'v91</title>')
old = '    <a class="ct-resume" href="resume.html">이력서 보기 →</a>\n'
assert s.count(old) == 1; s = s.replace(old, '')
s = s.replace('lol-plan-v90', 'lol-plan-v91')
open('versions/lol-plan-v91.html', 'w', encoding='utf-8').write(s)
print('ok')
