# v89 -> v90: 마지막 결론 띠가 처음엔 첫 부분 「핵심」 띠와 똑같이(질문) 나왔다가, 화면에 들어오면 질문이 답으로 바뀌며 결론 짓는 연출
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v89.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v89</title>', 'v90</title>')
rep('<section class="finale"><div class="fn-wrap"><span class="fn-k">결론</span><h2>롤의 즐거움은,<br><em class="kw">경쟁에만</em> 있지 않다.</h2><p>경쟁은 협곡에 그대로 두고, 지친 날엔 광장에서 쉬며 즐긴다.</p></div></section>',
    '<section class="finale fn-morph"><div class="fn-wrap">'
    '<span class="fn-k"><span class="fk-a">핵심</span><span class="fk-b">결론</span></span>'
    '<h2>롤의 즐거움은,<br><em class="kw">경쟁에만</em> 있지 않다.</h2>'
    '<p class="fn-swap"><span class="fs-a">그렇다면 지친 날의 소환사는,<br><em class="kw">협곡 대신 어디로</em> 가야 할까?</span>'
    '<span class="fs-b">경쟁은 협곡에 그대로 두고,<br>지친 날엔 <em class="kw">광장에서 쉬며</em> 즐긴다.</span></p>'
    '</div></section>')
css = ('.fn-morph .fn-k{display:inline-grid}.fn-morph .fn-k>span,.fn-swap>span{grid-area:1/1;transition:opacity .9s ease,filter .9s ease,transform .9s ease}'
       '.fn-swap{display:grid;justify-items:center}.fn-morph p.fn-swap{color:#F4F1E6}'
       '.fk-b,.fs-b{opacity:0;filter:blur(8px);transform:translateY(10px)}'
       '.fn-morph.done .fk-a,.fn-morph.done .fs-a{opacity:0;filter:blur(8px);transform:translateY(-10px)}'
       '.fn-morph.done .fk-b,.fn-morph.done .fs-b{opacity:1;filter:none;transform:none;transition-delay:.45s}\n')
k = s.rindex('</style>'); s = s[:k] + css + s[k:]
js = ('<script>(function(){var f=document.querySelector(".fn-morph");if(!f)return;var t;'
      'new IntersectionObserver(function(es){es.forEach(function(e){'
      'if(e.isIntersecting){t=setTimeout(function(){f.classList.add("done")},1300)}'
      'else{clearTimeout(t);if(e.boundingClientRect.top>0)f.classList.remove("done")}})},{threshold:.6}).observe(f)})();</script>\n')
k = s.rindex('</body>'); s = s[:k] + js + s[k:]
s = s.replace('lol-plan-v89', 'lol-plan-v90')
open('versions/lol-plan-v90.html', 'w', encoding='utf-8').write(s)
print('ok')
