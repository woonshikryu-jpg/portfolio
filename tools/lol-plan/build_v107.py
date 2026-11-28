# v106 -> v107: 결론으로 바뀐 뒤 화면 맨 아래에 「✉ 연락처」 — 커서를 올리거나 누르면 바로 위로 연락처 카드가 뜸(이메일 · 전화, 메일 보내기 · 복사)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v106.html', encoding='utf-8').read()
s = s.replace('v106</title>', 'v107</title>')
mail = 'mailto:wolf1205@naver.com?subject=%5B%ED%8F%AC%ED%8A%B8%ED%8F%B4%EB%A6%AC%EC%98%A4%5D%20%EC%88%A8%EC%96%B4%20%EC%82%AC%EB%8A%94%20%EC%86%8C%ED%99%98%EC%82%AC%EB%93%A4'
pop = ('<div class="fn-ct"><button class="fn-ct-btn" type="button" aria-expanded="false">✉ 연락처</button>'
       '<div class="fn-ct-pop" role="dialog" aria-label="연락처"><b class="fc-name">유운식 · 게임 기획</b>'
       '<div class="fc-row"><span class="fc-l">이메일</span><a class="fc-v" href="mailto:wolf1205@naver.com">wolf1205@naver.com</a>'
       '<a class="fc-b main" href="' + mail + '">메일 보내기</a><button class="fc-b" type="button" data-copy="wolf1205@naver.com">복사</button></div>'
       '<div class="fc-row"><span class="fc-l">전화</span><a class="fc-v" href="tel:01097197184">010-9719-7184</a>'
       '<button class="fc-b" type="button" data-copy="010-9719-7184">복사</button></div></div></div>')
old = '<div class="fn-end">'
assert s.count(old) == 1
s = s.replace(old, pop + old)
F = "'Pretendard Variable',Pretendard,'Noto Sans KR',sans-serif"
css = ('.fn-ct{position:absolute;left:50%;bottom:58px;transform:translateX(-50%);z-index:3;opacity:0;visibility:hidden;transition:opacity .5s .6s,visibility 0s 1.1s}'
       '.fn-morph.done .fn-ct{opacity:1;visibility:visible;transition:opacity .5s .6s,visibility 0s}'
       '.fn-ct-btn{all:unset;cursor:pointer;display:block;font:700 14px/1 ' + F + ';color:#1F2A1D;background:#E9C977;padding:10px 18px;border-radius:999px;box-shadow:0 6px 18px rgba(0,0,0,.25);transition:background .2s}'
       '.fn-ct-btn:hover,.fn-ct.open .fn-ct-btn{background:#F4DA93}'
       '.fn-ct-pop{position:absolute;left:50%;bottom:calc(100% + 12px);width:min(460px,90vw);transform:translate(-50%,8px);opacity:0;pointer-events:none;transition:opacity .2s,transform .2s;'
       'background:#F3F1EA;color:#1F2328;border-radius:16px;padding:18px 20px;box-shadow:0 20px 50px rgba(0,0,0,.35);text-align:left}'
       '.fn-ct-pop::after{content:"";position:absolute;left:50%;bottom:-7px;width:14px;height:14px;margin-left:-7px;background:#F3F1EA;transform:rotate(45deg)}'
       '.fn-ct:hover .fn-ct-pop,.fn-ct:focus-within .fn-ct-pop,.fn-ct.open .fn-ct-pop{opacity:1;pointer-events:auto;transform:translate(-50%,0)}'
       '.fn-ct:hover::before,.fn-ct.open::before{content:"";position:absolute;left:-40px;right:-40px;bottom:100%;height:16px}'
       '.fc-name{display:block;font:800 15px/1.3 ' + F + ';margin-bottom:12px}'
       '.fc-row{display:flex;align-items:center;gap:8px;padding:10px 0;border-top:1px solid #E3DDCC;flex-wrap:wrap}'
       '.fc-l{font:700 12px/1 ' + F + ';color:#7A838E;width:42px}'
       '.fc-v{font:800 16px/1.3 ' + F + ';color:#1F2328;text-decoration:none;margin-right:auto}.fc-v:hover{color:#8A6A2A}'
       '.fc-b{all:unset;cursor:pointer;font:700 12.5px/1 ' + F + ';padding:7px 11px;border-radius:999px;border:1.5px solid #D6D0BF;color:#1F2328}'
       '.fc-b.main{background:#2F4A2C;border-color:#2F4A2C;color:#fff}.fc-b:hover{border-color:#8A6A2A}\n')
k = s.rindex('</style>'); s = s[:k] + css + s[k:]
js = ('<script>(function(){var c=document.querySelector(".fn-ct");if(!c)return;var b=c.querySelector(".fn-ct-btn");'
      'b.addEventListener("click",function(e){e.stopPropagation();var v=!c.classList.contains("open");c.classList.toggle("open",v);b.setAttribute("aria-expanded",v)});'
      'document.addEventListener("click",function(e){if(!c.contains(e.target)){c.classList.remove("open");b.setAttribute("aria-expanded",false)}});'
      'c.querySelectorAll(".fc-b[data-copy]").forEach(function(x){x.addEventListener("click",function(){var t=x.dataset.copy,d=function(){var o=x.textContent;x.textContent="복사됨";setTimeout(function(){x.textContent=o},1400)};try{navigator.clipboard.writeText(t).then(d,d)}catch(e){d()}})})})();</script>\n')
k = s.rindex('</body>'); s = s[:k] + js + s[k:]
s = s.replace('lol-plan-v106', 'lol-plan-v107')
open('versions/lol-plan-v107.html', 'w', encoding='utf-8').write(s)
print('ok')
