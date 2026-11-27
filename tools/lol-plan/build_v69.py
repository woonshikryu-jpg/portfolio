# v68 -> v69: 4-1 포로 경주 이미지 추가 — 1:1 구역 펼침과 포로 경주 펼침 사이, 문도 피구 줄과 같은 모양(그림 + 상자 3개)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v68.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v68</title>', 'v69</title>')
anchor = '<div class="fi" style="grid-column:1/-1"><div class="acc"><button class="acc-btn" aria-expanded="true"><span class="n">2</span><span>포로 경주'
rep(anchor, '''<div class="fi" style="grid-column:1/-1"><div class="hs-map shot-row card">
      <figure class="shot"><img src="img/lol/poro-race.jpg" alt="포로 경주: 눈 덮인 트랙을 달리는 포로들과 관람 구역에서 응원하는 챔피언들" loading="lazy"><span class="shot-cap">포로 경주 · 구상 이미지</span></figure>
      <div class="hs-map-t t3">
        <div class="cs-fact"><span class="k">보기만 해도</span><b>약 90초, 포로들이 알아서 달린다</b><span>조작 없이 관람 구역에 서서 보고, 큐가 잡히면 그대로 떠납니다.</span></div>
        <div class="cs-fact"><span class="k">예측</span><b>1~10등 순서를 통째로</b><span>맞힌 등수마다 학회 기여가 겹쳐 쌓이고, 10등을 모두 맞히면 +20.</span></div>
        <div class="cs-fact"><span class="k">한 번은 내가</span><b>눈덩이 · 지름길 투표</b><span>관객 모두 한 판에 한 번씩 경주에 끼어들어, 보는 사람도 "내가 한 일"이 생깁니다.</span></div>
      </div>
    </div></div>''' + anchor)
s = s.replace('lol-plan-v68', 'lol-plan-v69')
open('versions/lol-plan-v69.html', 'w', encoding='utf-8').write(s)
print('ok')
