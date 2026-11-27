# v71 -> v72: 마무리를 결론이 분명한 강조 띠로 — 진한 초록 바탕 · 넓은 간격,
# 「롤의 즐거움은, 경쟁에만 있지 않다.」 + 결론 한 줄. 연락처는 밝은 바탕에 작게
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v71.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v71</title>', 'v72</title>')
rep('    <div class="closing"><p class="cl-a">협곡은 그대로,<br>광장 하나로 롤의 하루가 달라진다.</p></div>\n', '')
rep('<section class="contact" id="contact">',
    '<section class="finale"><div class="fn-wrap"><span class="fn-k">결론</span>'
    '<h2>롤의 즐거움은,<br>경쟁에만 있지 않다.</h2>'
    '<p>경쟁은 협곡에 그대로 두고, 지친 날엔 광장에서 쉬며 즐긴다.<br>회복한 유저는 다시 협곡으로 돌아온다.</p></div></section>\n'
    '<section class="contact" id="contact">')
rep('<h2>유운식 · 게임 기획</h2>\n    <div class="ct-list">', '<h3 class="ct-name">유운식 · 게임 기획</h3>\n    <div class="ct-list">')
k = s.rfind('</style>')
s = s[:k] + '''.finale{position:relative;z-index:1;background:#2F4A2C;color:#F4F1E6;padding:clamp(120px,16vh,190px) 20px}
.fn-wrap{max-width:900px;margin:0 auto;text-align:center}
.fn-k{display:inline-block;font:700 13px/1 'Pretendard Variable',Pretendard,sans-serif;letter-spacing:.24em;color:#E9C977;border:1.5px solid rgba(233,201,119,.6);border-radius:999px;padding:8px 16px}
.finale h2{margin:30px 0 0;font:800 clamp(34px,4.4vw,60px)/1.25 'Pretendard Variable',Pretendard,sans-serif;letter-spacing:-.02em;color:#fff}
.finale p{margin:34px auto 0;max-width:640px;font:500 clamp(16px,1.5vw,19px)/1.8 'Pretendard Variable',Pretendard,sans-serif;color:#D9DECF}
.contact{background:#F3F1EA!important;color:#1F2328!important;padding:56px 20px 40px!important}
.ct-wrap{max-width:720px!important}
.ct-k{color:#8A6A2A!important}
.ct-name{margin:10px 0 22px;font:800 20px/1.3 'Pretendard Variable',Pretendard,sans-serif;color:#1F2328}
.ct-item{background:#fff!important;border:1.5px solid #E3DDCC!important;border-radius:14px!important;padding:16px 18px!important;gap:6px!important}
.ct-l{color:#7A838E!important;font-size:12.5px!important}
.ct-v{font-size:18px!important;color:#1F2328!important}
.ct-v:hover{color:#8A6A2A!important}
.ct-btn{font-size:13px!important;padding:8px 13px!important;border-color:#D6D0BF!important;color:#1F2328!important}
.ct-btn.main{background:#2F4A2C!important;border-color:#2F4A2C!important;color:#fff!important}
.ct-resume{margin-top:18px!important;color:#2F4A2C!important;font-size:14px!important}
.end{background:#E8E5DC!important;color:#7A7468!important}
''' + s[k:]
s = s.replace('lol-plan-v71', 'lol-plan-v72')
open('versions/lol-plan-v72.html', 'w', encoding='utf-8').write(s)
print('ok')
