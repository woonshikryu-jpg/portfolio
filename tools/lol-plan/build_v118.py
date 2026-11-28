# v117 -> v118: 포로 경주 「관객 개입(눈덩이 · 지름길 투표)」 삭제 — 관객이 끼어드는 방식은 「응원」 하나로. 관련 요약 문구도 응원으로
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v117.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v117</title>', 'v118</title>')
rep('<li><b>관객 개입</b>: 모든 관객이 한 판에 한 번씩 눈덩이를 던지거나 갈림길 지름길에 투표할 수 있습니다. 누구나 똑같이 한 번이라 공정하면서, 영상과 달리 "내가 한 일"이 생깁니다.</li>', '')
rep('결과를 정하지 않고 확률만 올리므로, 예측을 맞히는 재미는 그대로입니다.</li>',
    '결과를 정하지 않고 확률만 올리므로 예측을 맞히는 재미는 그대로이고, 영상과 달리 보는 사람에게도 "내가 한 일"이 생깁니다.</li>')
rep('<span class="k">한 번은 내가</span><b>눈덩이 · 지름길 투표</b><span>관객 모두 한 판에 한 번씩 경주에 끼어들어, 보는 사람도 "내가 한 일"이 생깁니다.</span>',
    '<span class="k">응원</span><b>감정표현으로 응원</b><span>응원을 많이 받은 포로일수록 질주할 확률이 올라, 보는 사람도 "내가 한 일"이 생깁니다.</span>')
rep('<span class="sum">보기만 해도, 한 번은 내가 개입한다</span>', '<span class="sum">보기만 해도, 내 응원이 닿는다</span>')
rep('<p class="one">응원 · 예측 · 관객도 한 번씩 개입</p>', '<p class="one">순위 예측 · 응원으로 질주</p>')
rep('누르면 바로 반응 · 관객도 한 번씩 개입 · 결과가', '누르면 바로 반응 · 내 응원이 경주를 바꿈 · 결과가')
assert '눈덩이' not in s and '지름길' not in s
s = s.replace('lol-plan-v117', 'lol-plan-v118')
open('versions/lol-plan-v118.html', 'w', encoding='utf-8').write(s)
print('ok')
