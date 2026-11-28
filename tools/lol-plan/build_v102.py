# v101 -> v102: 결론 띠를 맨 마지막 장으로(그 뒤로 스크롤할 내용 없음 → 바뀐 결론에서 멈춤).
# 연락처는 본문에서 빼서, 왼쪽 PART 목차 맨 아래 「연락처」 버튼을 누르면 창으로 뜨게. 저작권 한 줄은 결론 띠 맨 아래로
import os, re
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v101.html', encoding='utf-8').read()
s = s.replace('v101</title>', 'v102</title>')
# 1) 연락처 섹션 → 모달
a = s.index('<section class="contact" id="contact">'); b = s.index('</section>', a) + len('</section>')
contact = s[a:b]; s = s[:a] + s[b:]
contact = contact.replace('<div class="ct-wrap">', '<div class="ct-wrap"><button class="ct-x" type="button" aria-label="닫기">×</button>', 1)
modal = '<div class="ct-modal" id="ctModal" aria-hidden="true"><div class="ct-dim"></div><div class="ct-box" role="dialog" aria-label="연락처">' + contact + '</div></div>\n'
# 2) 저작권 줄 → 결론 띠 안 맨 아래
m = re.search(r'<div class="end">(.*?)</div>\n?', s, re.S); assert m
endtxt = m.group(1); s = s[:m.start()] + s[m.end():]
old = '</p></div></section></div>'
assert s.count(old) == 1
s = s.replace(old, '</p></div><div class="fn-end">' + endtxt + '</div></section></div>\n' + modal)
# 3) 목차 맨 아래 연락처 버튼
old = '<i>결론</i></span></a></nav>'
assert s.count(old) == 1
s = s.replace(old, '<i>결론</i></span></a><button class="rail-ct" type="button" aria-haspopup="dialog"><span>✉ 연락처</span></button></nav>')
css = ('.fn-end{position:absolute;left:0;right:0;bottom:18px;text-align:center;font:500 12.5px/1.5 \'Pretendard Variable\',Pretendard,sans-serif;color:rgba(244,241,230,.45);padding:0 20px}'
       '.rail-line{bottom:64px!important}.rail-ct{all:unset;cursor:pointer;margin:6px 0 0 1px;display:block}'
       '.rail-ct span{display:inline-block;font:700 11.5px/1 \'Pretendard Variable\',Pretendard,\'Noto Sans KR\',sans-serif;color:#fff;background:#2F4A2C;border:1.5px solid rgba(233,201,119,.7);padding:6px 10px;border-radius:999px;white-space:nowrap;transition:background .2s}'
       '.rail-ct:hover span,.rail-ct:focus-visible span{background:#3E6239}'
       '.ct-modal{position:fixed;inset:0;z-index:200;display:flex;align-items:center;justify-content:center;padding:20px;opacity:0;pointer-events:none;transition:opacity .25s}'
       '.ct-modal.open{opacity:1;pointer-events:auto}'
       '.ct-dim{position:absolute;inset:0;background:rgba(15,20,14,.55);backdrop-filter:blur(3px)}'
       '.ct-box{position:relative;width:min(720px,100%);transform:translateY(14px);transition:transform .25s}'
       '.ct-modal.open .ct-box{transform:none}'
       '.ct-box .contact{border-radius:20px;padding:40px 28px 34px!important;box-shadow:0 30px 70px rgba(0,0,0,.35)}'
       '.ct-x{position:absolute;right:14px;top:12px;all:unset;cursor:pointer;font:400 28px/1 sans-serif;color:#7A838E;padding:4px 10px}'
       '.ct-box .ct-wrap{position:relative}.ct-box .ct-x{position:absolute;right:-12px;top:-28px}'
       '.ct-x:hover{color:#1F2328}'
       '@media(max-width:700px){.rail-ct span{padding:5px 7px;font-size:10.5px}}\n')
k = s.rindex('</style>'); s = s[:k] + css + s[k:]
js = ('<script>(function(){var m=document.getElementById("ctModal"),b=document.querySelector(".rail-ct");if(!m||!b)return;'
      'function o(v){m.classList.toggle("open",v);m.setAttribute("aria-hidden",v?"false":"true")}'
      'b.addEventListener("click",function(){o(true)});m.querySelector(".ct-dim").addEventListener("click",function(){o(false)});'
      'm.querySelector(".ct-x").addEventListener("click",function(){o(false)});addEventListener("keydown",function(e){if(e.key==="Escape")o(false)})})();</script>\n')
k = s.rindex('</body>'); s = s[:k] + js + s[k:]
s = s.replace('lol-plan-v101', 'lol-plan-v102')
open('versions/lol-plan-v102.html', 'w', encoding='utf-8').write(s)
print('ok')
