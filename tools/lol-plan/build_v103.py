# v102 -> v103: 제목 강조색을 PART마다 고유색으로(같은 PART 안은 통일). 밝은 배경용 진한 색 / 그림·어두운 배경용 밝은 색 한 쌍씩.
# 표지·핵심·요약·마지막 결론 띠는 처음과 끝을 잇는 금색(P0)
import os, re
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v102.html', encoding='utf-8').read()
s = s.replace('v102</title>', 'v103</title>')
PAL = {  # 밝은 배경, 어두운 배경
 0: ('#B9790A', '#FFC24D'),  # 표지 · 핵심 · 결론 — 금색
 1: ('#D7322A', '#FF8C80'),  # 문제 정의 — 빨강
 2: ('#0B8A78', '#62E6D2'),  # 핵심 콘셉트 — 청록
 3: ('#E2580C', '#FFAE5E'),  # 광장 모드 설계 — 주황
 4: ('#1F5FE0', '#93BEFF'),  # 캐주얼 모드 — 파랑
 5: ('#7A3CD6', '#CDAEFF'),  # 확장 계획 — 보라
 6: ('#178A3E', '#83E6A0'),  # 실행 가능성 — 초록
 7: ('#D02A72', '#FF9EC6'),  # 결론 PART — 분홍
}
b = s.index('<body')
marks = {'sweep': 1, 'frame': 2, 'harbor': 3, 'snow': 4, 'dawn': 5, 'pull': 7}
pos = [(re.search(r'class="scene[^"]*"[^>]*data-mode="%s"' % k, s).start(), v) for k, v in marks.items()]
pos.append((s.index('id="feasible"'), 6)); pos.sort()
fm = s.index('<section class="finale fn-morph">')
def part(p):
    if p > fm: return 0
    n = 0
    for q, v in pos:
        if p > q: n = v
    return n
out = []; last = 0
for m in re.finditer(r'class="(kw|play-hl)"', s):
    if m.start() < b: continue
    out.append(s[last:m.start()]); out.append('class="%s kp%d"' % (m.group(1), part(m.start()))); last = m.end()
out.append(s[last:]); s = ''.join(out)
css = ''.join('.kp%d{--kl:%s;--kd:%s}' % (k, a, d) for k, (a, d) in PAL.items())
css += ('.kw{color:var(--kl)}.play-hl{color:var(--kl)}'
        '.carve .kw,.cloth .kw,.mark .kw,.finale .kw,.contact .kw,.doors-title .kw{color:var(--kd)}\n')
k = s.rindex('</style>'); s = s[:k] + css + s[k:]
s = s.replace('lol-plan-v102', 'lol-plan-v103')
open('versions/lol-plan-v103.html', 'w', encoding='utf-8').write(s)
print('ok', len(out)//2)
