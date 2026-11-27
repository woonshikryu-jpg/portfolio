# v56 -> v57: 실제 게임 화면 2장 — 4-1 문도 피구(사용자 설정 게임), 4-2 니코가 바위게로 변신한 모습. 맵 줄과 같은 모양(그림 + 상자)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v56.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v56</title>', 'v57</title>')
# 4-1 문도 피구
a41 = '<div class="card"><span class="tag">보기</span><h3>포로 경주</h3><p class="one">응원 · 예측 · 관객도 한 번씩 개입</p></div>\n    </div>\n'
rep(a41, a41 + '''    <div class="hs-map shot-row card">
      <figure class="shot"><img src="img/lol/mundo-dodgeball.jpg" alt="실제 게임 화면: 사용자 설정 게임으로 하는 문도 피구" loading="lazy"><span class="shot-cap">실제 게임 화면 · 사용자 설정 게임의 문도 피구</span></figure>
      <div class="hs-map-t t3">
        <div class="cs-fact"><span class="k">지금</span><b>방을 만들고 사람을 모아야 한다</b><span>유저들이 사용자 설정 게임으로 직접 규칙을 정해 즐겨 온 놀이입니다.</span></div>
        <div class="cs-fact"><span class="k">광장에서는</span><b>구역 앞에 서면 바로 한 판</b><span>대기열에 서면 다음 도전자로 들어가고, 큐가 잡히면 그냥 떠납니다.</span></div>
        <div class="cs-fact"><span class="k">그대로</span><b>1레벨 · Q 하나 · 둘만</b><span>유저들이 이미 다듬어 온 규칙을 그대로 정식으로 옮깁니다.</span></div>
      </div>
    </div>
''')
# 4-2 니코 바위게 — 맵 줄 바로 아래
i = s.index('<div class="hs-map card">'); j = s.index('</div>\n    </div>\n', s.index('<div class="hs-map-t">', i)) + len('</div>\n    </div>\n')
s = s[:j] + '''    <div class="hs-map shot-row card">
      <figure class="shot"><div class="shot-box"><img src="img/lol/neeko-scuttle.jpg" alt="실제 게임 화면: 니코가 패시브로 바위게로 변신해 진짜 바위게 옆에 있는 모습" loading="lazy"><span class="pin" style="left:29%;top:74%">니코</span><span class="pin real" style="left:58%;top:57%">진짜 바위게</span></div><span class="shot-cap">실제 게임 화면 · 니코 패시브로 바위게가 된 모습</span></figure>
      <div class="hs-map-t t3">
        <div class="cs-fact"><span class="k">이미 되는 것</span><b>니코는 지금도 몹으로 변한다</b><span>숨바꼭질은 새 기술이 아니라, 니코 패시브를 모두에게 나눠 주는 것입니다.</span></div>
        <div class="cs-fact"><span class="k">숨바꼭질에서는</span><b>와드 · 정글 몹 · 식물 · 미니언으로</b><span>가까운 사물을 누르면 그 모습이 되고, 피해를 받으면 풀립니다.</span></div>
        <div class="cs-fact"><span class="k">들키지 않게</span><b>술래에게는 복제한 대상의 체력 바 · 이름만</b><span>내 이름과 체력 바는 우리 팀에게만 보여, 진짜와 가짜를 겉모습으로 가려낼 수 없습니다.</span></div>
      </div>
    </div>
''' + s[j:]
k = s.rfind('</style>')
s = s[:k] + '.shot-row .hs-map-t.t3{grid-template-rows:repeat(3,1fr)}.shot{margin:0;display:flex;flex-direction:column;justify-content:center;gap:8px}.shot img{width:100%;display:block;border-radius:12px}.shot-box{position:relative}.shot-cap{font-size:13px;color:#6B7480;text-align:center}.shot .pin{position:absolute;transform:translate(-50%,0);background:rgba(17,20,24,.82);color:#fff;font:700 12.5px/1 \'Pretendard Variable\',Pretendard,sans-serif;padding:6px 9px;border-radius:999px;white-space:nowrap;border:1.5px solid #C9A24E}.shot .pin.real{border-color:#fff}\n' + s[k:]
s = s.replace('lol-plan-v56', 'lol-plan-v57')
open('versions/lol-plan-v57.html', 'w', encoding='utf-8').write(s)
print('ok')
