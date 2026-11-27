# v53 -> v54: 4-2 숨바꼭질에 맵 그림 추가(협곡 그대로, 라인에 부쉬만 조금 추가, 새 부쉬는 색을 달리해 구분) — 카드 4장 아래, 펼침 위
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v53.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v53</title>', 'v54</title>')
anchor = '<div class="card"><span class="tag">승패</span><h3>5명 다 잡으면 교대</h3><p class="one">2라운드 · 버틴 시간 + 미션 점수</p></div>\n    </div>\n'
block = anchor + '''    <div class="hs-map card">
      <figure><img src="img/lol/hide-map.jpg" alt="숨바꼭질 맵: 소환사의 협곡에 라인 부쉬를 조금 더한 모습" loading="lazy"><figcaption>숨바꼭질 맵 · 소환사의 협곡</figcaption></figure>
      <div class="hs-map-t">
        <span class="tag">맵</span><h3>새 맵이 아니라, 협곡 그대로</h3>
        <ul>
          <li><b>그대로</b>: 라인 · 정글 · 강 · 포탑 · 미니언 · 우물. 협곡 지도가 곧 숨바꼭질 지도입니다.</li>
          <li><b>더한 것</b>: 세 라인 가장자리에 부쉬를 조금. 라인에도 숨을 자리가 생깁니다. 협곡에 없던 자리의 부쉬는 <b>색을 다르게 칠해</b>, 협곡을 아는 유저가 헷갈리지 않게 합니다.</li>
          <li><b>바꾼 것</b>: 미니언 · 포탑은 챔피언을 공격하지 않고, 골드 · 경험치도 주지 않습니다. 이동 속도는 모두 같게 조금 빠르게.</li>
          <li><b>마지막 1분</b>: 바깥쪽부터 구역이 닫혀 가운데로 모입니다.</li>
        </ul>
      </div>
    </div>
'''
rep(anchor, block)
i = s.rfind('</style>'); s = s[:i] + ('.hs-map{display:grid!important;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);gap:28px;align-items:center;margin-bottom:18px!important}.hs-map figure{margin:0}.hs-map img{width:100%;display:block;border-radius:10px}.hs-map figcaption{font-size:13px;color:#777;margin-top:8px;text-align:center}.hs-map ul{margin:10px 0 0;padding-left:18px;display:grid;gap:8px}.hs-map li{line-height:1.6}@media (max-width:820px){.hs-map{grid-template-columns:1fr}}\n') + s[i:]
rep('<b>라인 부쉬 추가</b>', '<b>라인 부쉬 추가</b>(협곡에 없던 부쉬는 색을 달리해 구분)')
s = s.replace('lol-plan-v53', 'lol-plan-v54')
open('versions/lol-plan-v54.html', 'w', encoding='utf-8').write(s)
print('ok')
