# v54 -> v55: 4-2 맵 옆 설명을 2-3 본단처럼 상자 4개(그대로 · 더한 것 · 바꾼 것 · 마지막 1분)로, 그림 높이에 맞춰 위아래 꽉 차게
import os, re
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v54.html', encoding='utf-8').read()
s = s.replace('v54</title>', 'v55</title>')
a = s.index('<div class="hs-map-t">'); b = s.index('</div>\n    </div>\n', a) + len('</div>\n')
new = '''<div class="hs-map-t">
        <div class="cs-fact"><span class="k">그대로</span><b>협곡 지도가 곧 숨바꼭질 지도</b><span>라인 · 정글 · 강 · 포탑 · 미니언 · 우물을 그대로 씁니다.</span></div>
        <div class="cs-fact"><span class="k">더한 것</span><b>세 라인 가장자리에 부쉬</b><span>라인에도 숨을 자리가 생깁니다. 협곡에 없던 부쉬는 색을 다르게 칠해 헷갈리지 않게 합니다.</span></div>
        <div class="cs-fact"><span class="k">바꾼 것</span><b>미니언 · 포탑은 챔피언을 안 때린다</b><span>골드 · 경험치도 주지 않습니다. 이동 속도는 모두 같게 조금 빠르게.</span></div>
        <div class="cs-fact"><span class="k">마지막 1분</span><b>바깥부터 구역이 닫힌다</b><span>숨은 사람도 가운데로 모여, 끝까지 긴장이 이어집니다.</span></div>
      </div>
'''
s = s[:a] + new + s[b:]
old_css = re.search(r'\.hs-map\{display:grid!important;[^\n]*\n', s).group(0)
s = s.replace(old_css, '.hs-map{display:grid!important;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:22px;align-items:stretch;margin-bottom:18px!important;padding:20px!important}.hs-map figure{margin:0;display:flex;align-items:center}.hs-map img{width:100%;display:block;border-radius:12px}.hs-map figcaption{font-size:13px;color:#777;margin-top:8px;text-align:center}.hs-map-t{display:grid;grid-template-rows:repeat(4,1fr);gap:12px}.hs-map-t .cs-fact{justify-content:center;padding:12px 18px}.hs-map-t .cs-fact b{font-size:17px}.hs-map-t .cs-fact>span:last-child{font-size:14px}@media (max-width:820px){.hs-map{grid-template-columns:1fr}.hs-map-t{grid-template-rows:none}}\n')
s = s.replace('<figcaption>숨바꼭질 맵 · 소환사의 협곡</figcaption>', '')
s = s.replace('lol-plan-v54', 'lol-plan-v55')
open('versions/lol-plan-v55.html', 'w', encoding='utf-8').write(s)
print('ok')
