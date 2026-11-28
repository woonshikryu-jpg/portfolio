# v124 -> v125: 핵심 · 결론 띠의 질문 강조를 낱말 하나로 — 「경쟁」, 「어디로」만
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v124.html', encoding='utf-8').read()
s = s.replace('v124</title>', 'v125</title>')
for old, new in [('<em class="kw kp0">경쟁에만</em>', '<em class="kw kp0">경쟁</em>에만'),
                 ('<em class="kw kp0">협곡 대신 어디로</em>', '협곡 대신 <em class="kw kp0">어디로</em>')]:
    assert s.count(old) == 2, (old, s.count(old)); s = s.replace(old, new)
s = s.replace('lol-plan-v124', 'lol-plan-v125')
open('versions/lol-plan-v125.html', 'w', encoding='utf-8').write(s)
print('ok')
