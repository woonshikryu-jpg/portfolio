# v23 -> v24: 2-3 「소환사들만의 도시, 학회 본단」 오른쪽 글 문단을 카드 3장으로(어디에 · 무엇을 하는 곳 · 시즌 보상), 그림 높이에 맞춤
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v23.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert old in s, old[:60]; s = s.replace(old, new, 1)
s = s.replace('v23</title>', 'v24</title>')
rep('''<p>밴들 시티가 요들만의 도시이듯, 소환사에게도 그들만의 도시가 있습니다. 룬테라와 닿지 않는 다른 차원, 그 한가운데에 학회 본단이 서 있습니다.</p>
        <p>협곡으로 가는 문도 이곳에 있습니다. 광장 모드에 들어가면 펼쳐지는 곳이 바로 <b>본단의 안뜰</b>입니다.</p>
        <div class="cs-punch small">''',
'''<div class="cs-fact"><span class="k">어디에 있나</span><b>룬테라 바깥, 소환사들만의 차원</b><span>밴들 시티가 요들만의 도시이듯. 룬테라 이야기와 닿지 않습니다.</span></div>
        <div class="cs-fact"><span class="k">무엇을 하는 곳인가</span><b>협곡으로 가는 문이 있는 곳</b><span>광장 모드에 들어가면 펼쳐지는 곳이 바로 본단의 안뜰입니다.</span></div>
        <div class="cs-punch small">''')
rep('</head>', '''<style>
.cs-hq{align-items:stretch}
.cs-hq-txt{display:flex;flex-direction:column;gap:12px}
.cs-hq-txt .cs-punch.small{margin-top:0;flex:1;justify-content:center}
.cs-fact{background:#fff;border:1.5px solid #E6E8EB;border-radius:16px;padding:16px 20px;display:flex;flex-direction:column;gap:5px}
.cs-fact .k{font:700 13px/1 'Pretendard Variable',Pretendard,sans-serif;color:#8A929C}
.cs-fact b{font:800 19px/1.35 'Pretendard Variable',Pretendard,sans-serif;color:#111418;letter-spacing:-.01em}
.cs-fact>span:last-child{font:500 14.5px/1.5 'Pretendard Variable',Pretendard,sans-serif;color:#5B6470}
</style>
</head>''')
s = s.replace('lol-plan-v23', 'lol-plan-v24')
open('versions/lol-plan-v24.html', 'w', encoding='utf-8').write(s)
print('ok')
