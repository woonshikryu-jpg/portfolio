# v45 -> v46: 4-1 광장 즉석 놀이 제목 「직접 겨루거나, 구경하며 즐기거나」→「1:1 결투, 포로 경주」
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v45.html', encoding='utf-8').read()
s = s.replace('v45</title>', 'v46</title>')
old = '<div class="sec-no">4-1 · 광장 즉석 놀이</div><h2>직접 겨루거나, 구경하며 즐기거나</h2>'
assert s.count(old) == 1
s = s.replace(old, '<div class="sec-no">4-1 · 광장 즉석 놀이</div><h2>1:1 결투, 포로 경주</h2>')
assert '직접 겨루거나' not in s
s = s.replace('lol-plan-v45', 'lol-plan-v46')
open('versions/lol-plan-v46.html', 'w', encoding='utf-8').write(s)
print('ok')
