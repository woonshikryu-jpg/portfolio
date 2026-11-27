# v38 -> v39: 3-3 보상 카드 3장을 한 줄 3칸으로(3번 카드 혼자 반 칸 남던 것) · 「왜 능력치가 아니라 외형인가」 제목 앞 「+」 원(번호 자리) 삭제 — 다른 핵심 펼침과 같은 모양으로
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v38.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert old in s, old[:60]; s = s.replace(old, new, 1)
s = s.replace('v38</title>', 'v39</title>')
rep('<span class="n">+</span><span>왜 능력치가 아니라 외형인가', '<span>왜 능력치가 아니라 외형인가')
assert 'class="n">+</span>' not in s
rep('</style>', '@media (min-width:900px){#reward .flat{grid-template-columns:repeat(3,1fr)}#reward .flat .fi:has(.acc.must){grid-column:1/-1}}\n</style>')
s = s.replace('lol-plan-v38', 'lol-plan-v39')
open('versions/lol-plan-v39.html', 'w', encoding='utf-8').write(s)
print('ok')
