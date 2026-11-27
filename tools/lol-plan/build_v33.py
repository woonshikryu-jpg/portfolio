# v32 -> v33: 2-3 소속 규칙 메모 첫 문장 「처음에는 인지도가 높은 세 지역의 학회로 시작합니다.」로 합침
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v32.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert old in s, old[:60]; s = s.replace(old, new, 1)
s = s.replace('v32</title>', 'v33</title>')
rep('처음에는 3개 학회로 시작합니다. 인지도를 기준으로 골랐습니다. 데마시아',
    '처음에는 인지도가 높은 세 지역의 학회로 시작합니다. 데마시아')
s = s.replace('lol-plan-v32', 'lol-plan-v33')
open('versions/lol-plan-v33.html', 'w', encoding='utf-8').write(s)
print('ok')
