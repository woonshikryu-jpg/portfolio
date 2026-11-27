# v13 -> v14: 한 장 요약 아래 초록 띠("기존 클라이언트 위 1단계 → 지표로 증명하며 확장")를
# 처음 보는 사람도 읽히는 3단계 띠로 교체.
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v13.html', encoding='utf-8').read()

def rep(old, new):
    global s
    assert old in s, old[:60]
    s = s.replace(old, new, 1)

s = s.replace('v13</title>', 'v14</title>')

rep('<div class="banner">기존 클라이언트 위 1단계 → 지표로 증명하며 확장</div>',
'''<div class="plan3">
      <div class="p3-head"><b>작게 시작해서, 반응을 확인하고 넓힌다</b><span>다음 단계는 앞 단계의 지표가 좋아진 것을 확인한 뒤에 엽니다</span></div>
      <ol class="p3-steps">
        <li><span class="p3-n">1단계 · 작게</span><b>롤 클라이언트 첫 화면을<br>학회 광장으로</b><span class="p3-d">지금 메뉴 화면 자리에 광장 하나 · 캐주얼 모드 추가</span></li>
        <li><span class="p3-n">2단계 · 넓게</span><b>TFT처럼 따로 여는<br>학회 본단</b><span class="p3-d">본단을 3인칭으로 걷고 · 버튼 하나로 롤 큐</span></li>
        <li><span class="p3-n">3단계 · 잇기</span><b>라이엇 MMO에<br>기록을 넘긴다</b><span class="p3-d">새로 만들지 않고 · 내 소환사와 학회 기록이 이어짐</span></li>
      </ol>
    </div>''')

rep('</head>', '''<style>
.plan3{margin-top:24px;border-radius:14px;background:var(--accent);color:#fff;padding:22px 24px 24px}
.p3-head{display:flex;align-items:baseline;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-bottom:16px}
.p3-head b{font:800 20px/1.4 'Pretendard Variable',Pretendard,'Noto Sans KR',sans-serif}
.p3-head span{font-size:14px;opacity:.82}
.p3-steps{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:28px;counter-reset:none}
.p3-steps li{position:relative;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.22);border-radius:10px;padding:16px 18px;display:flex;flex-direction:column;gap:6px}
.p3-steps li+li::before{content:"→";position:absolute;left:-22px;top:50%;transform:translateY(-50%);font-weight:800;opacity:.8}
.p3-n{font-size:13px;font-weight:700;opacity:.85}
.p3-steps b{font:800 18px/1.35 'Pretendard Variable',Pretendard,'Noto Sans KR',sans-serif}
.p3-d{font-size:14px;line-height:1.5;opacity:.85}
@media(max-width:760px){.p3-steps{grid-template-columns:1fr;gap:12px}.p3-steps li+li::before{display:none}}
</style>
</head>''')

s = s.replace('lol-plan-v13', 'lol-plan-v14')
open('versions/lol-plan-v14.html', 'w', encoding='utf-8').write(s)
print('ok')
