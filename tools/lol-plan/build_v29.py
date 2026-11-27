# v28 -> v29: 2-1 머무는 고리 ④ 단계 문장 끝 「→ 다시 ①로.」 삭제
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v28.html', encoding='utf-8').read()
old = '<p class="sm">점수 대신 풍경이 결과를 보여 준다 → 다시 ①로.</p>'
assert s.count(old) == 1
s = s.replace(old, '<p class="sm">점수 대신 풍경이 결과를 보여 준다.</p>', 1)
s = s.replace('v28</title>', 'v29</title>').replace('lol-plan-v28', 'lol-plan-v29')
open('versions/lol-plan-v29.html', 'w', encoding='utf-8').write(s)
print('ok')
