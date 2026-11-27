# v16 -> v17: 4-2 광장 즉석 놀이 장면 제목을 오른쪽 위(빈 하늘)로 옮기고 글씨를 약 20% 줄임 — 가운데 큰 포로를 가리지 않게
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v16.html', encoding='utf-8').read()
old = '<div class="mark scene-cap pop" style="left:30%;top:40%;font-size:clamp(13px,1.5vw,24px)"'
assert old in s
s = s.replace(old, '<div class="mark scene-cap pop" style="left:76%;top:24%;font-size:clamp(12px,1.2vw,19px)"', 1)
s = s.replace('v16</title>', 'v17</title>').replace('lol-plan-v16', 'lol-plan-v17')
open('versions/lol-plan-v17.html', 'w', encoding='utf-8').write(s)
print('ok')
