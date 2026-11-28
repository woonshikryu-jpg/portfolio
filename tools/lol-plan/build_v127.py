# v126 -> v127: 결론 문장 흐름 — 질문 「협곡 대신 어디로?」에 바로 답하는 제목 「경쟁하지 않아도, 함께라서 즐거운 광장.」,
# 아래 문장은 PART 01 「왜 남는 게 없을까 / 끝나면 남이 되는 팀원」과 짝: 「점수만 남던 롤에, 이제 함께한 사람이 남는다.」
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v126.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:70]); s = s.replace(old, new)
s = s.replace('v126</title>', 'v127</title>')
rep('<span class="fs-b">경쟁하지 않아도,<br><em class="kw kp0">함께</em>라서 즐겁다.</span>',
    '<span class="fs-b">경쟁하지 않아도,<br>함께라서 즐거운 <em class="kw kp0">광장</em>.</span>')
rep('<span class="fs-b">경쟁에 지친 소환사는,<br>사람들이 기다리는 <em class="kw kp0">광장</em>으로 간다.</span>',
    '<span class="fs-b">점수만 남던 롤에,<br>이제 함께한 <em class="kw kp0">사람</em>이 남는다.</span>')
s = s.replace('lol-plan-v126', 'lol-plan-v127')
open('versions/lol-plan-v127.html', 'w', encoding='utf-8').write(s)
print('ok')
