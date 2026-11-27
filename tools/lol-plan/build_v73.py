# v72 -> v73: 3-1 맨 위에 본단 맵 그림(번호 표시 + 범례). 맵 구성 설명을 그림 배치에 맞춤
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v72.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v72</title>', 'v73</title>')
pins = [('1','50%','46%','가운데 광장'),('2','17%','44%','포로 서킷'),('3','50%','86%','1:1 구역'),('4','51%','13%','데마시아'),('5','86%','14%','녹서스'),('6','81%','64%','필트오버')]
pin_html = ''.join(f'<span class="mp" style="left:{x};top:{y}"><b>{n}</b>{t}</span>' for n,x,y,t in pins)
rep('<div><div class="sec-no">3-1 · 학회 광장</div><h2>메뉴 화면 대신, 놀다 가는 광장</h2></div>\n    </div>\n',
    '<div><div class="sec-no">3-1 · 학회 광장</div><h2>메뉴 화면 대신, 놀다 가는 광장</h2></div>\n    </div>\n'
    '    <div class="pm card">\n'
    f'      <figure class="pm-fig"><div class="pm-box"><img src="img/lol/plaza-map.jpg" alt="학회 본단 맵: 가운데 광장, 왼쪽 포로 서킷, 아래 1:1 구역, 위와 오른쪽에 세 학회 구역" loading="lazy">{pin_html}</div><span class="shot-cap">학회 본단 맵 · 구상 이미지 (데마시아 우승 시즌 예시)</span></figure>\n'
    '      <div class="pm-legend">\n'
    '        <div class="cs-fact"><span class="k">① 가운데 광장</span><b>소환진 · 게시판</b><span>챔피언을 바꾸고 순위표를 보는 곳. 모든 길이 여기로 모입니다.</span></div>\n'
    '        <div class="cs-fact"><span class="k">② 포로 서킷 · ③ 1:1 구역</span><b>보는 놀이와 붙는 놀이</b><span>왼쪽엔 관람 구역이 두른 포로 서킷, 아래엔 원형 결투장 여러 개.</span></div>\n'
    '        <div class="cs-fact"><span class="k">④ ⑤ ⑥ 학회 구역</span><b>데마시아 · 녹서스 · 필트오버</b><span>각자 양식을 지키고, 내 학회 구역에서 시작합니다. 나머지 본단은 우승 학회 양식.</span></div>\n'
    '        <div class="cs-fact"><span class="k">크기 · 이동</span><b>협곡의 약 2배 · 이동탑</b><span>곳곳의 푸른 수정 이동탑으로 포탑 텔레포트처럼 옮겨 갑니다.</span></div>\n'
    '      </div>\n    </div>\n')
rep('가운데 광장에 1:1 구역 · 포로 트랙 · 게시판 · 소환진이 모여 있어 모든 소환사가 지나가고, 그 둘레에 데마시아 · 녹서스 · 필트오버 학회 구역이 있습니다.',
    '가운데 광장(소환진 · 게시판)을 중심으로 왼쪽에 포로 서킷, 아래에 1:1 구역, 위와 오른쪽에 데마시아 · 녹서스 · 필트오버 학회 구역이 있습니다.')
rep('포로 경주 관람석은 트랙을 두른 고리 모양, 1:1 구역은 가운데 광장 둘레에 여러 개.', '포로 서킷은 관람 구역이 트랙을 따라 길게 두르고, 1:1 구역은 여러 개로 나눕니다.')
k = s.rfind('</style>')
s = s[:k] + '''.pm{padding:20px!important;margin-bottom:22px!important;display:flex!important;flex-direction:column;gap:16px}
.pm-fig{margin:0;display:flex;flex-direction:column;gap:8px}.pm-box{position:relative}.pm-box img{width:100%;display:block;border-radius:12px}
.mp{position:absolute;transform:translate(-50%,-50%);display:flex;align-items:center;gap:6px;background:rgba(17,20,24,.82);color:#fff;font:700 13px/1 'Pretendard Variable',Pretendard,sans-serif;padding:5px 11px 5px 5px;border-radius:999px;border:1.5px solid #C9A24E;white-space:nowrap}
.mp b{display:grid;place-items:center;width:20px;height:20px;border-radius:50%;background:#C9A24E;color:#111;font-size:12px}
.pm-legend{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.pm-legend .cs-fact b{font-size:16.5px}.pm-legend .cs-fact>span:last-child{font-size:13.5px}
@media (max-width:900px){.pm-legend{grid-template-columns:1fr 1fr}.mp{font-size:11px}}
''' + s[k:]
s = s.replace('lol-plan-v72', 'lol-plan-v73')
open('versions/lol-plan-v73.html', 'w', encoding='utf-8').write(s)
print('ok')
