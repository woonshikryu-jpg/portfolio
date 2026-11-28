# v95 -> v96: 결론 문구 사용자 확정 — 「경쟁하지 않아도, 함께라서 즐겁다.」 / 「경쟁에 지친 소환사는, 사람들이 기다리는 광장으로 간다.」
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v95.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v95</title>', 'v96</title>')
rep('<span class="fs-b">이기지 않아도,<br><em class="kw">함께라서</em> 즐겁다.</span>',
    '<span class="fs-b">경쟁하지 않아도,<br><em class="kw">함께라서</em> 즐겁다.</span>')
rep('<span class="fs-b">경쟁에 지친 소환사는,<br><em class="kw">광장</em>에서 만난 학회원과 <em class="kw">한 팀</em>이 된다.</span>',
    '<span class="fs-b">경쟁에 지친 소환사는,<br>사람들이 기다리는 <em class="kw">광장</em>으로 간다.</span>')
s = s.replace('lol-plan-v95', 'lol-plan-v96')
open('versions/lol-plan-v96.html', 'w', encoding='utf-8').write(s)
print('ok')
