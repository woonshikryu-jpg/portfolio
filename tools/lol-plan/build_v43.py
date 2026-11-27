# v42 -> v43: 숨바꼭질 — 잡힌 도망자는 「그 자리」가 아니라 술래 팀 우물에서 부활
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v42.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert old in s, old[:60]; s = s.replace(old, new, 1)
s = s.replace('v42</title>', 'v43</title>')
rep('잡힌 도망자는 그 자리에서 술래 팀으로 부활. 술래가 점점 늘어남.', '잡힌 도망자는 술래 팀 우물에서 술래로 부활. 술래가 점점 늘어남.')
rep('잡힌 도망자는 그 자리에서 술래 팀으로 부활합니다. 술래로 바뀌니 위치가 드러나도 헷갈릴 일이 없고, 잡힌 사람도 쉬지 않고 계속 플레이합니다.',
    '잡힌 도망자는 <b>술래 팀 우물</b>에서 술래로 부활합니다. 잡힌 자리에서 바로 술래가 되면 근처에 숨은 동료를 곧장 덮칠 수 있어, 우물에서 다시 출발하게 합니다. 잡힌 사람도 쉬지 않고 계속 플레이합니다.')
assert '그 자리에서 술래' not in s
s = s.replace('lol-plan-v42', 'lol-plan-v43')
open('versions/lol-plan-v43.html', 'w', encoding='utf-8').write(s)
print('ok')
