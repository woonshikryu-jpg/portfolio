# v105 -> v106: 핵심 띠 · 결론 띠의 ↓ 화살표를 「스크롤 ↓」 글자 표시로 (표지의 스크롤 안내와 같은 말)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v105.html', encoding='utf-8').read()
s = s.replace('v105</title>', 'v106</title>')
n = s.count('aria-hidden="true">↓</span>'); assert n == 2, n
s = s.replace('aria-hidden="true">↓</span>', 'aria-hidden="true">스크롤 ↓</span>')
css = (".fn-down{display:table;margin:44px auto 0;font:700 14px/1 'Pretendard Variable',Pretendard,'Noto Sans KR',sans-serif;"
       "letter-spacing:.04em;color:#E9C977;border:1.5px solid rgba(233,201,119,.6);border-radius:999px;padding:9px 16px}\n")
k = s.rindex('</style>'); s = s[:k] + css + s[k:]
s = s.replace('lol-plan-v105', 'lol-plan-v106')
open('versions/lol-plan-v106.html', 'w', encoding='utf-8').write(s)
print('ok')
