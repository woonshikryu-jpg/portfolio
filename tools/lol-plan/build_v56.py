# v55 -> v56: 4-1 1:1 구역 · 포로 경주 펼침 — 「핵심」 표시 빼고, 둘 다 처음부터 펼친 상태로
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v55.html', encoding='utf-8').read()
s = s.replace('v55</title>', 'v56</title>')
i = s.index('id="poro"'); j = s.index('</section>', i); seg = s[i:j]
a = '<div class="acc must"><button class="acc-btn" aria-expanded="true">'
b = '<div class="acc"><button class="acc-btn" aria-expanded="false">'
assert seg.count(a) == 1 and seg.count(b) == 1
seg = seg.replace('<div class="fi">' + a, '<div class="fi" style="grid-column:1/-1">' + a, 1)
seg = seg.replace(a, '<div class="acc"><button class="acc-btn" aria-expanded="true">').replace(b, '<div class="acc"><button class="acc-btn" aria-expanded="true">')
s = s[:i] + seg + s[j:]
s = s.replace('lol-plan-v55', 'lol-plan-v56')
open('versions/lol-plan-v56.html', 'w', encoding='utf-8').write(s)
print('ok')
