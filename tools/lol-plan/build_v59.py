# v58 -> v59: 이름은 표지로(「유운식 · 게임 기획」), 맨 끝은 연락처 영역(이메일 · 전화 크게, 메일 보내기 · 복사 · 이력서), 저작권 안내는 그 아래 작게
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v58.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v58</title>', 'v59</title>')
rep('<p>리그 오브 레전드 신규 콘텐츠 제안서 · 게임기획 포트폴리오</p></div>',
    '<p>리그 오브 레전드 신규 콘텐츠 제안서 · 게임기획 포트폴리오</p><p class="by">유운식 · 게임 기획</p></div>')
rep('<div class="end"><b>유운식 · 게임 기획</b><br>본 기획서는 라이엇 게임즈와 무관한 개인 기획안이며, 수록된 룬테라 이미지의 저작권은 Riot Games에 있습니다.</div>',
'''<section class="contact" id="contact">
  <div class="ct-wrap">
    <span class="ct-k">CONTACT</span>
    <h2>유운식 · 게임 기획</h2>
    <div class="ct-list">
      <div class="ct-item"><span class="ct-l">이메일</span><a class="ct-v" href="mailto:wolf1205@naver.com">wolf1205@naver.com</a><div class="ct-act"><a class="ct-btn main" href="mailto:wolf1205@naver.com?subject=%5B%ED%8F%AC%ED%8A%B8%ED%8F%B4%EB%A6%AC%EC%98%A4%5D%20%EC%88%A8%EC%96%B4%20%EC%82%AC%EB%8A%94%20%EC%86%8C%ED%99%98%EC%82%AC%EB%93%A4">메일 보내기</a><button class="ct-btn" type="button" data-copy="wolf1205@naver.com">복사</button></div></div>
      <div class="ct-item"><span class="ct-l">전화</span><a class="ct-v" href="tel:01097197184">010-9719-7184</a><div class="ct-act"><button class="ct-btn" type="button" data-copy="010-9719-7184">복사</button></div></div>
    </div>
    <a class="ct-resume" href="resume.html">이력서 보기 →</a>
  </div>
</section>
<div class="end">본 기획서는 라이엇 게임즈와 무관한 개인 기획안이며, 수록된 룬테라 이미지의 저작권은 Riot Games에 있습니다.</div>
<script>document.querySelectorAll('.ct-btn[data-copy]').forEach(function(b){b.addEventListener('click',function(){var t=b.dataset.copy,d=function(){var o=b.textContent;b.textContent='복사됨';setTimeout(function(){b.textContent=o},1400)};try{navigator.clipboard.writeText(t).then(d,function(){d()})}catch(e){d()}})})</script>''')
k = s.rfind('</style>')
s = s[:k] + '''.carve.title .by{margin-top:.5em;font-size:.82em;opacity:.95;letter-spacing:.02em}
.contact{position:relative;z-index:1;background:#1F2A1D;color:#F4F1E6;padding:90px 20px 70px}
.ct-wrap{max-width:860px;margin:0 auto;text-align:center}
.ct-k{font:700 13px/1 'Pretendard Variable',Pretendard,sans-serif;letter-spacing:.24em;color:#C9A24E}
.contact h2{font:800 clamp(28px,3.4vw,40px)/1.25 'Pretendard Variable',Pretendard,sans-serif;margin:14px 0 34px;color:#fff}
.ct-list{display:grid;grid-template-columns:1fr 1fr;gap:16px;text-align:left}
.ct-item{background:rgba(255,255,255,.06);border:1.5px solid rgba(201,162,78,.45);border-radius:18px;padding:22px 24px;display:flex;flex-direction:column;gap:8px}
.ct-l{font:700 13px/1 'Pretendard Variable',Pretendard,sans-serif;color:#C9C3AE}
.ct-v{font:800 clamp(20px,2.2vw,26px)/1.3 'Pretendard Variable',Pretendard,sans-serif;color:#fff;text-decoration:none;word-break:break-all}
.ct-v:hover{color:#E9C977}
.ct-act{display:flex;gap:8px;margin-top:6px}
.ct-btn{font:700 14px/1 'Pretendard Variable',Pretendard,sans-serif;padding:11px 16px;border-radius:999px;border:1.5px solid rgba(255,255,255,.35);background:transparent;color:#fff;cursor:pointer;text-decoration:none}
.ct-btn.main{background:#C9A24E;border-color:#C9A24E;color:#1F2A1D}
.ct-btn:hover{border-color:#E9C977}
.ct-resume{display:inline-block;margin-top:28px;color:#E9C977;font:700 15px/1 'Pretendard Variable',Pretendard,sans-serif;text-decoration:none}
.end{padding:22px 20px 28px!important;font-size:13px!important;background:#18211A!important;color:#8E9688!important}
@media (max-width:700px){.ct-list{grid-template-columns:1fr}}
''' + s[k:]
s = s.replace('lol-plan-v58', 'lol-plan-v59')
open('versions/lol-plan-v59.html', 'w', encoding='utf-8').write(s)
print('ok')
