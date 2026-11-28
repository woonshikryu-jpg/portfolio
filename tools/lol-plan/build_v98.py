# v97 -> v98: 결론 띠를 화면 가운데 고정(스크롤 핀) — 문구가 바뀌기 전엔 못 지나감. 스크롤 진행 30%에서 옆으로 휙 바뀜(빠른 가로 전환)
import os, re
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v97.html', encoding='utf-8').read()
s = s.replace('v97</title>', 'v98</title>')
a = s.index('<section class="finale fn-morph">'); b = s.index('</section>', a) + len('</section>')
s = s[:a] + '<div class="fn-pin">' + s[a:b] + '</div>' + s[b:]
# 예전 전환 스크립트(IntersectionObserver) 제거
old_js = re.search(r'<script>\(function\(\)\{var f=document\.querySelector\("\.fn-morph"\).*?</script>\n', s, re.S)
assert old_js; s = s[:old_js.start()] + s[old_js.end():]
css = ('.fn-pin{position:relative;height:230vh}'
       '.fn-pin .finale{position:sticky;top:0;height:100vh;padding:0 20px;display:flex;align-items:center;justify-content:center;overflow:hidden}'
       '.fn-pin .fn-wrap{width:100%}'
       '.fn-morph .fn-k>span,.fn-swap>span{transition:opacity .22s ease,transform .32s cubic-bezier(.2,.9,.25,1);filter:none!important}'
       '.fk-b,.fs-b{opacity:0;transform:translateX(90px)}'
       '.fn-morph.done .fk-a,.fn-morph.done .fs-a{opacity:0;transform:translateX(-90px);transition-delay:0s}'
       '.fn-morph.done .fk-b,.fn-morph.done .fs-b{opacity:1;transform:none;transition-delay:.06s}'
       '.fn-morph.done p.fn-swap .fs-b{transition-delay:.14s}'
       '.fn-prog{position:absolute;left:50%;bottom:34px;width:120px;height:3px;margin-left:-60px;border-radius:3px;background:rgba(233,201,119,.25);overflow:hidden}'
       '.fn-prog i{position:absolute;inset:0;background:#E9C977;transform-origin:left;transform:scaleX(0)}\n')
k = s.rindex('</style>'); s = s[:k] + css + s[k:]
s = s.replace('<section class="finale fn-morph"><div class="fn-wrap">', '<section class="finale fn-morph"><div class="fn-wrap">', 1)
s = s.replace('</div></section></div>', '</div><div class="fn-prog" aria-hidden="true"><i></i></div></section></div>', 1) if '<div class="fn-pin">' in s else s
js = ('<script>(function(){var w=document.querySelector(".fn-pin"),f=w&&w.querySelector(".fn-morph"),bar=w&&w.querySelector(".fn-prog i");if(!f)return;'
      'function u(){var r=w.getBoundingClientRect(),h=w.offsetHeight-innerHeight,p=Math.min(1,Math.max(0,-r.top/h));'
      'if(bar)bar.style.transform="scaleX("+Math.min(1,p/.3)+")";f.classList.toggle("done",p>=.3)}'
      'addEventListener("scroll",u,{passive:true});addEventListener("resize",u);u()})();</script>\n')
k = s.rindex('</body>'); s = s[:k] + js + s[k:]
s = s.replace('lol-plan-v97', 'lol-plan-v98')
open('versions/lol-plan-v98.html', 'w', encoding='utf-8').write(s)
print('ok')
