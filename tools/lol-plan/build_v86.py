# v85 -> v86: 3-1 제목 「놀다」만 크게, 색다르게 강조
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v85.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v85</title>', 'v86</title>')
rep('<h2>메뉴 화면 대신, 놀다 가는 광장</h2>', '<h2>메뉴 화면 대신, <em class="play-hl">놀다</em> 가는 광장</h2>')
k = s.rindex('</style>'); s = s[:k] + '.play-hl{font-style:normal;font-size:1.4em;font-weight:900;color:#E07A1F;display:inline-block;transform:rotate(-4deg) translateY(.04em);margin:0 .06em;padding:0 .08em;line-height:1;background:linear-gradient(transparent 62%,rgba(255,206,84,.55) 62%,rgba(255,206,84,.55) 92%,transparent 92%)}\n' + s[k:]
s = s.replace('lol-plan-v85', 'lol-plan-v86')
open('versions/lol-plan-v86.html', 'w', encoding='utf-8').write(s)
print('ok')
