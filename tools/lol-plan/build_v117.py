# v116 -> v117: 포로 경주 관전 · 응원 규칙 추가(카메라만 경주로, 감정표현 3초 1회 응원 → 비율 게이지 → 질주 확률). PART 07 장면 「회복」 → 「유대감」
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v116.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v116</title>', 'v117</title>')
rep('누구나 똑같이 한 번이라 공정하면서, 영상과 달리 "내가 한 일"이 생깁니다.</li></ul>',
    '누구나 똑같이 한 번이라 공정하면서, 영상과 달리 "내가 한 일"이 생깁니다.</li>'
    '<li><b>관전</b>: 관람 구역에 서 있으면 내 캐릭터는 그 자리에 두고, 카메라만 경주로로 옮겨 가 봅니다. 큐가 잡히면 그대로 떠납니다.</li>'
    '<li><b>응원</b>: 감정표현 키를 누르면 응원이 됩니다(3초에 한 번). 포로마다 받은 응원 비율이 게이지로 보이고, 응원을 많이 받은 포로일수록 갑자기 질주할 확률이 올라갑니다. 결과를 정하지 않고 확률만 올리므로, 예측을 맞히는 재미는 그대로입니다.</li></ul>')
rep('<h2>경쟁만 있던 롤에,<br><em class="kw kp7">회복</em>을 더한다.</h2>', '<h2>경쟁만 있던 롤에,<br><em class="kw kp7">유대감</em>을 더한다.</h2>')
s = s.replace('lol-plan-v116', 'lol-plan-v117')
open('versions/lol-plan-v117.html', 'w', encoding='utf-8').write(s)
print('ok')
