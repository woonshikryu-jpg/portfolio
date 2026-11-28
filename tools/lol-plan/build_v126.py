# v125 -> v126: 결론 「함께라서」 → 「함께」만 강조
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v125.html', encoding='utf-8').read()
s = s.replace('v125</title>', 'v126</title>')
old = '<em class="kw kp0">함께라서</em>'
assert s.count(old) == 1; s = s.replace(old, '<em class="kw kp0">함께</em>라서')
s = s.replace('lol-plan-v125', 'lol-plan-v126')
open('versions/lol-plan-v126.html', 'w', encoding='utf-8').write(s)
print('ok')
