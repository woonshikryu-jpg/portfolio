# v120 -> v121: 적성 차이는 미끄러짐이 아니라 속도로 — 직진형은 직선에서, 코너형은 커브에서 같은 만큼 빠름. 미끄러짐은 모든 포로에게 같은 확률
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v120.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:70]); s = s.replace(old, new)
s = s.replace('v120</title>', 'v121</title>')
rep('눈길이라 커브에서 미끄러지면 잠깐 멈춤. 잘 달리던 선두도 뒤집히는 변수. 직진형이 코너형보다 잘 미끄러짐',
    '눈길이라 커브에서 미끄러지면 잠깐 멈춤. 모든 포로에게 같은 확률이라, 잘 달리던 선두도 뒤집히는 변수')
rep('<b>직진형</b>: 직선에서 빠름 · <b>코너형</b>: 커브에서 빠르고 덜 미끄러짐',
    '<b>직진형</b>: 직선에서 빠르고 커브에서 느림 · <b>코너형</b>: 커브에서 빠르고 직선에서 느림. 빠르고 느린 차이는 둘이 같아서, 오늘 코스의 직선 · 커브 비율이 유불리를 가름')
s = s.replace('lol-plan-v120', 'lol-plan-v121')
open('versions/lol-plan-v121.html', 'w', encoding='utf-8').write(s)
print('ok')
