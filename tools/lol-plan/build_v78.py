# v77 -> v78: PART 06 카드 설명에서 「 · 」 나열 없애고 항목당 하나만
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v77.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v77</title>', 'v78</title>')
rep('<p class="one">접속 · 스킨 · 경기 매너 · 복귀 · 신규</p>', '<p class="one">주간 접속일로 본다</p>')
rep('<p class="one">큐 연결 · 저사양 PC · 개발 비용 등</p>', '<p class="one">큐가 잡히면 바로 협곡으로 간다</p>')
s = s.replace('lol-plan-v77', 'lol-plan-v78')
open('versions/lol-plan-v78.html', 'w', encoding='utf-8').write(s)
print('ok')
