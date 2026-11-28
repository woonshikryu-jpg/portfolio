# v88 -> v89: 표지 뒤 핵심 띠를 궁금하게 만드는 화법으로 — 답(광장)을 먼저 말하지 않고 질문으로 넘김. 답은 마지막 결론 띠에서
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v88.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v88</title>', 'v89</title>')
rep('<span class="fn-k">핵심</span><h2>롤의 즐거움은,<br><em class="kw">경쟁에만</em> 있지 않다.</h2><p>경쟁은 협곡에 그대로 두고, 지친 날엔 광장에서 쉬며 즐긴다.</p>',
    '<span class="fn-k">핵심</span><h2>롤의 즐거움은,<br><em class="kw">경쟁에만</em> 있지 않다.</h2><p>그렇다면 지친 날의 소환사는,<br><em class="kw">협곡 대신 어디로</em> 가야 할까?</p><span class="fn-down" aria-hidden="true">↓</span>')
k = s.rindex('</style>')
s = s[:k] + '.opener p{color:#F4F1E6}.fn-down{display:block;margin:44px auto 0;font:400 26px/1 sans-serif;color:#E9C977;animation:fnDown 1.8s ease-in-out infinite}@keyframes fnDown{0%,100%{transform:translateY(0);opacity:.55}50%{transform:translateY(8px);opacity:1}}\n' + s[k:]
s = s.replace('lol-plan-v88', 'lol-plan-v89')
open('versions/lol-plan-v89.html', 'w', encoding='utf-8').write(s)
print('ok')
