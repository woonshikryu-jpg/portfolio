# v61 -> v62: 한 장 요약 아래 「작게 시작해서」 띠를 눈에 띄게 — 초록 띠 안에 흰 카드, 「먼저 / 다음」 이름표, 큰 제목, 가운데 둥근 화살표
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v61.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v61</title>', 'v62</title>')
rep('<li><span class="p3-n">먼저 · 롤 안의 광장 모드</span>', '<li><span class="p3-n"><i class="p3-chip first">먼저</i>롤 안의 광장 모드</span>')
rep('<li><span class="p3-n">다음 · 잇기</span>', '<li><span class="p3-n"><i class="p3-chip">다음</i>라이엇 MMO로 잇기</span>')
k = s.rfind('</style>')
s = s[:k] + '''.plan3{padding:28px 30px 30px!important;box-shadow:0 14px 34px rgba(30,60,30,.22)}
.p3-head{margin-bottom:20px!important}
.p3-head b{font-size:clamp(20px,1.9vw,25px)!important}
.p3-head span{font-size:15px!important;opacity:.95!important;background:rgba(255,255,255,.14);padding:7px 12px;border-radius:999px}
.plan3 .p3-steps{gap:56px!important}
.plan3 .p3-steps li{background:#fff!important;border:0!important;border-radius:16px!important;padding:22px 24px!important;color:#1F2328;gap:8px!important;box-shadow:0 6px 16px rgba(0,0,0,.12)}
.plan3 .p3-steps li+li::before{display:grid!important;content:"→";place-items:center;left:-46px!important;width:36px;height:36px;border-radius:50%;background:#fff;color:var(--accent);font-size:18px;opacity:1!important}
.plan3 .p3-n{display:flex;align-items:center;gap:8px;font-size:14px!important;opacity:1!important;color:#5B6470}
.p3-chip{font-style:normal;font-weight:800;font-size:13px;padding:5px 10px;border-radius:999px;background:#EEF1EC;color:var(--accent)}
.p3-chip.first{background:var(--accent);color:#fff}
.plan3 .p3-steps b{font-size:clamp(19px,1.7vw,23px)!important;color:#111418}
.plan3 .p3-d{font-size:14.5px!important;opacity:1!important;color:#5B6470}
@media (max-width:760px){.plan3 .p3-steps{grid-template-columns:1fr!important;gap:14px!important}.plan3 .p3-steps li+li::before{display:none!important}}
''' + s[k:]
s = s.replace('lol-plan-v61', 'lol-plan-v62')
open('versions/lol-plan-v62.html', 'w', encoding='utf-8').write(s)
print('ok')
