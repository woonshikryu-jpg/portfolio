# v27 -> v28: 1-1 네 개의 벽 마지막 칸 「핵심 질문」 아래 보조 문장 삭제
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v27.html', encoding='utf-8').read()
old = '<p>경쟁은 협곡에 → 쉼과 기록은 그 바깥에</p>'
assert s.count(old) == 1
s = s.replace(old, '', 1).replace('v27</title>', 'v28</title>').replace('lol-plan-v27', 'lol-plan-v28')
open('versions/lol-plan-v28.html', 'w', encoding='utf-8').write(s)
print('ok')
