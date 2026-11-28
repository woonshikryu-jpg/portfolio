# v104 -> v105: 목차 맨 위에 「00 · 표지 · 요약」 추가 — PART 01 앞(표지 · 핵심 띠 · 한 장 요약)으로 이동
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v104.html', encoding='utf-8').read()
s = s.replace('v104</title>', 'v105</title>')
old = '<div class="rail-line"><i></i></div><a href="#" data-go=".scene[data-mode=sweep]">'
assert s.count(old) == 1
s = s.replace(old, '<div class="rail-line"><i></i></div><a href="#" data-go=".scene[data-mode=mist]"><span><em>00</em><i>표지 · 요약</i></span></a><a href="#" data-go=".scene[data-mode=sweep]">')
s = s.replace('lol-plan-v104', 'lol-plan-v105')
open('versions/lol-plan-v105.html', 'w', encoding='utf-8').write(s)
print('ok')
