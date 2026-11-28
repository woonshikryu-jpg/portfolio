# v115 -> v116: 색 정돈 — 제목 위 작은 번호(sec-no)와 제목 밑줄을 그 PART 강조색으로. 제목 뒤 흐린 배경을 은은하게 밝혀 글씨를 또렷하게
import os, re
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v115.html', encoding='utf-8').read()
s = s.replace('v115</title>', 'v116</title>')
b = s.index('<body')
marks = {'sweep': 1, 'frame': 2, 'harbor': 3, 'snow': 4, 'dawn': 5, 'pull': 7}
pos = [(re.search(r'class="scene[^"]*"[^>]*data-mode="%s"' % k, s).start(), v) for k, v in marks.items()]
pos.append((s.index('id="feasible"'), 6)); pos.sort()
def part(p):
    n = 0
    for q, v in pos:
        if p > q: n = v
    return n
out = []; last = 0; cnt = 0
for m in re.finditer(r'<div class="sec-head"', s):
    if m.start() < b: continue
    out.append(s[last:m.start()]); out.append('<div class="sec-head kp%d"' % part(m.start())); last = m.end(); cnt += 1
out.append(s[last:]); s = ''.join(out)
css = ('.ex .sec-head[class*=kp] .sec-no{color:color-mix(in srgb,var(--kl) 80%,#000)}'
       '.ex .sec-head[class*=kp] h2::after{background:var(--kl)}'
       '.ex .sec-head{position:relative;isolation:isolate}'
       '.ex .sec-head::before{content:"";position:absolute;left:-90px;right:-40px;top:-50px;bottom:-40px;z-index:-1;pointer-events:none;'
       'background:radial-gradient(closest-side at 45% 50%,rgba(255,255,255,.72),rgba(255,255,255,.45) 50%,rgba(255,255,255,0) 100%)}\n')
k = s.rindex('</style>'); s = s[:k] + css + s[k:]
s = s.replace('lol-plan-v115', 'lol-plan-v116')
open('versions/lol-plan-v116.html', 'w', encoding='utf-8').write(s)
print('ok', cnt)
