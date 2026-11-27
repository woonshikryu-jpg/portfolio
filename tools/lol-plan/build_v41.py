# v40 -> v41: 펼침 버튼의 +/× 를 글자 대신 CSS 선으로 그림 — 글꼴 기준선 때문에 ×가 원 가운데서 살짝 내려가던 것 수정(모든 펼침 · 비교표 줄 공통)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v40.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert old in s, old[:60]; s = s.replace(old, new, 1)
s = s.replace('v40</title>', 'v41</title>')
i = s.rfind('</style>')
s = s[:i] + ".plus,.cmp-row .pl{position:relative;font-size:0!important;line-height:0!important}.plus::before,.cmp-row .pl::before{content:'';position:absolute;inset:0;margin:auto;width:12px;height:12px;background:linear-gradient(currentColor,currentColor) center/12px 2.4px no-repeat,linear-gradient(currentColor,currentColor) center/2.4px 12px no-repeat}\n" + s[i:]
s = s.replace('lol-plan-v40', 'lol-plan-v41')
open('versions/lol-plan-v41.html', 'w', encoding='utf-8').write(s)
print('ok')
