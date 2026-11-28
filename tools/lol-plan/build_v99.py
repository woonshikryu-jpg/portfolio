# v98 -> v99: 전환 효과는 v97(흐려졌다 또렷해짐)로 되돌림, 화면 고정은 유지. 진행 막대 삭제
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v98.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v98</title>', 'v99</title>')
a = s.index('.fn-morph .fn-k>span,.fn-swap>span{transition:opacity .22s'); b = s.index('.fn-prog{', a)
s = s[:a] + ('.fn-morph .fn-k>span,.fn-swap>span{transition:opacity .6s ease,filter .6s ease,transform .6s ease}'
             '.fk-b,.fs-b{opacity:0;filter:blur(8px);transform:translateY(10px)}'
             '.fn-morph.done .fk-a,.fn-morph.done .fs-a{opacity:0;filter:blur(8px);transform:translateY(-10px)}'
             '.fn-morph.done .fk-b,.fn-morph.done .fs-b{opacity:1;filter:none;transform:none;transition-delay:.3s}') + s[b:]
rep('<div class="fn-prog" aria-hidden="true"><i></i></div>', '')
s = s.replace(',bar=w&&w.querySelector(".fn-prog i")', '').replace('if(bar)bar.style.transform="scaleX("+Math.min(1,p/.3)+")";', '')
assert 'fn-prog i"' not in s
s = s.replace('lol-plan-v98', 'lol-plan-v99')
open('versions/lol-plan-v99.html', 'w', encoding='utf-8').write(s)
print('ok')
