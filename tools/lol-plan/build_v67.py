# v66 -> v67: PART 07 장면 — 제목 「경쟁만 있던 롤에, 회복을 더한다.」 / 부제 「새로운 안식처」
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v66.html', encoding='utf-8').read()
s = s.replace('v66</title>', 'v67</title>')
old = '<span class="pn">PART 07 · 결론</span><h2>점수 하나 대신,<br>다시 일어설 힘을 남긴다.</h2><p>지친 하루가 쉬어 가는 롤</p>'
assert s.count(old) == 1
s = s.replace(old, '<span class="pn">PART 07 · 결론</span><h2>경쟁만 있던 롤에,<br>회복을 더한다.</h2><p>새로운 안식처</p>')
s = s.replace('lol-plan-v66', 'lol-plan-v67')
open('versions/lol-plan-v67.html', 'w', encoding='utf-8').write(s)
print('ok')
