# v93 -> v94: 마지막 띠 — 큰 제목과 아래 문장 둘 다 바뀌며 결론. 승리만이 아니라 사람과의 유대로도 즐겁다는 것
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v93.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v93</title>', 'v94</title>')
rep('<span class="fk-b">결론</span></span><h2>롤의 즐거움은,<br><em class="kw">경쟁에만</em> 있지 않다.</h2>'
    '<p class="fn-swap"><span class="fs-a">경쟁에 지친 소환사는,<br><em class="kw">협곡 대신 어디로</em> 가야 할까?</span>'
    '<span class="fs-b">경쟁은 협곡에 그대로 두고,<br>지친 날엔 <em class="kw">광장에서 쉬며</em> 즐긴다.</span></p>',
    '<span class="fk-b">결론</span></span>'
    '<h2 class="fn-swap"><span class="fs-a">롤의 즐거움은,<br><em class="kw">경쟁에만</em> 있지 않다.</span>'
    '<span class="fs-b">이기지 않아도,<br><em class="kw">함께라서</em> 즐겁다.</span></h2>'
    '<p class="fn-swap"><span class="fs-a">경쟁에 지친 소환사는,<br><em class="kw">협곡 대신 어디로</em> 가야 할까?</span>'
    '<span class="fs-b">경쟁에 지친 소환사는,<br>학회 사람들이 기다리는 <em class="kw">광장</em>으로 간다.</span></p>')
s = s.replace('lol-plan-v93', 'lol-plan-v94')
open('versions/lol-plan-v94.html', 'w', encoding='utf-8').write(s)
print('ok')
