# v99 -> v100: 문구 전환 속도까지 v97과 똑같이(0.9초, 답은 0.45초 뒤). 화면 고정(큰 초록 배경)은 유지
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v99.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v99</title>', 'v100</title>')
rep('transition:opacity .6s ease,filter .6s ease,transform .6s ease}', 'transition:opacity .9s ease,filter .9s ease,transform .9s ease}')
rep('.fn-morph.done .fk-b,.fn-morph.done .fs-b{opacity:1;filter:none;transform:none;transition-delay:.3s}',
    '.fn-morph.done .fk-b,.fn-morph.done .fs-b{opacity:1;filter:none;transform:none;transition-delay:.45s}')
s = s.replace('lol-plan-v99', 'lol-plan-v100')
open('versions/lol-plan-v100.html', 'w', encoding='utf-8').write(s)
print('ok')
