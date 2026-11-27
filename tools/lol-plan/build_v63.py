# v62 -> v63: 결론 띠 다음에 마무리 — PART 01 핵심 질문을 다시 띄우고 답하며 매듭
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v62.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v62</title>', 'v63</title>')
rep('<div class="banner">접속 유지 · 스킨이 보일 무대 · 복귀와 신규의 입구 · IP 확장</div>\n  </div>\n</section></div>\n',
    '<div class="banner">접속 유지 · 스킨이 보일 무대 · 복귀와 신규의 입구 · IP 확장</div>\n'
    '    <div class="closing"><span class="cl-k">처음의 질문</span><p class="cl-q">한 판을 하지 않아도 머물 이유가 있는 LoL은 가능할까?</p>'
    '<p class="cl-a">가능합니다.<br>협곡 밖에, 머물 광장 하나를 더하면.</p></div>\n  </div>\n</section></div>\n')
k = s.rfind('</style>')
s = s[:k] + '''.closing{text-align:center;padding:110px 0 40px}
.cl-k{display:inline-block;font:700 13px/1 'Pretendard Variable',Pretendard,sans-serif;letter-spacing:.14em;color:var(--accent);border:1.5px solid currentColor;border-radius:999px;padding:7px 14px}
.cl-q{margin:22px 0 0;font:600 clamp(17px,1.6vw,21px)/1.6 'Pretendard Variable',Pretendard,sans-serif;color:#5B6470}
.cl-a{margin:18px 0 0;font:800 clamp(30px,3.6vw,48px)/1.3 'Pretendard Variable',Pretendard,sans-serif;color:#111418;letter-spacing:-.02em}
''' + s[k:]
s = s.replace('lol-plan-v62', 'lol-plan-v63')
open('versions/lol-plan-v63.html', 'w', encoding='utf-8').write(s)
print('ok')
