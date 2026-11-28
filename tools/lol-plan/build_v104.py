# v103 -> v104: 마지막 결론 띠에도 첫 핵심 띠처럼 ↓ 스크롤 표시 — 질문 상태일 때만 보이고, 결론으로 바뀌면 사라짐
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v103.html', encoding='utf-8').read()
s = s.replace('v103</title>', 'v104</title>')
old = '</p></div><div class="fn-end">'
assert s.count(old) == 1
s = s.replace(old, '</p><span class="fn-down fn-down-end" aria-hidden="true">↓</span></div><div class="fn-end">')
css = '.fn-down-end{transition:opacity .4s}.fn-morph.done .fn-down-end{opacity:0!important;animation:none}\n'
k = s.rindex('</style>'); s = s[:k] + css + s[k:]
s = s.replace('lol-plan-v103', 'lol-plan-v104')
open('versions/lol-plan-v104.html', 'w', encoding='utf-8').write(s)
print('ok')
