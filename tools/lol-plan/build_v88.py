# v87 -> v88: 표지 바로 뒤(한 장 요약 앞)에 결론과 같은 진한 초록 띠를 「핵심」으로 넣음 — 결론까지 안 읽어도 첫 부분에서 메시지가 보이게
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v87.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v87</title>', 'v88</title>')
band = ('<section class="finale opener"><div class="fn-wrap"><span class="fn-k">핵심</span>'
        '<h2>롤의 즐거움은,<br><em class="kw">경쟁에만</em> 있지 않다.</h2>'
        '<p>경쟁은 협곡에 그대로 두고, 지친 날엔 광장에서 쉬며 즐긴다.</p></div></section>\n\n')
rep('<div class="ex r-ionia"><div class="ex-bg" aria-hidden="true"><img src="img/lol/cover-hq.jpg" alt=""></div><section id="summary"',
    band + '<div class="ex r-ionia"><div class="ex-bg" aria-hidden="true"><img src="img/lol/cover-hq.jpg" alt=""></div><section id="summary"')
s = s.replace('lol-plan-v87', 'lol-plan-v88')
open('versions/lol-plan-v88.html', 'w', encoding='utf-8').write(s)
print('ok')
