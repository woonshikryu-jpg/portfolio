# v43 -> v44: 4-2 제목 「붙다가, 보다가」→「직접 겨루거나, 구경하며 즐기거나」(장면 · 설명 제목 둘 다)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v43.html', encoding='utf-8').read()
s = s.replace('v43</title>', 'v44</title>')
assert s.count('<h2>붙다가, 보다가</h2>') == 2
s = s.replace('<h2>붙다가, 보다가</h2>', '<h2>직접 겨루거나, 구경하며 즐기거나</h2>')
s = s.replace('lol-plan-v43', 'lol-plan-v44')
open('versions/lol-plan-v44.html', 'w', encoding='utf-8').write(s)
print('ok')
