# v46 -> v47: 4-1 제목 「1:1 결투, 포로 경주」→「1:1 구역, 포로 경주」(본문 용어와 통일)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v46.html', encoding='utf-8').read()
s = s.replace('v46</title>', 'v47</title>')
assert s.count('<h2>1:1 결투, 포로 경주</h2>') == 1 and s.count('1:1 결투') == 1
s = s.replace('<h2>1:1 결투, 포로 경주</h2>', '<h2>1:1 구역, 포로 경주</h2>')
s = s.replace('lol-plan-v46', 'lol-plan-v47')
open('versions/lol-plan-v47.html', 'w', encoding='utf-8').write(s)
print('ok')
