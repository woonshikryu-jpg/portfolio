# v91 -> v92: 왼쪽 위 「← 버전 모음」 버튼 삭제 (완성본)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v91.html', encoding='utf-8').read()
s = s.replace('v91</title>', 'v92</title>')
old = '<a class="back" href="index.html">← 버전 모음</a>'
assert s.count(old) == 1; s = s.replace(old, '')
s = s.replace('lol-plan-v91', 'lol-plan-v92')
open('versions/lol-plan-v92.html', 'w', encoding='utf-8').write(s)
print('ok')
