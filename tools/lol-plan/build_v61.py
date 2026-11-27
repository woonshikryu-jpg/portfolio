# v60 -> v61: 첫 화면에서 스크롤 없이 바로 표지 — 안개 효과 없이 처음부터 선명, 제목도 처음부터, 표지 구간 길이 300vh → 150vh
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v60.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v60</title>', 'v61</title>')
rep('<div class="scene still" data-mode="mist" data-w="1832" data-h="837" style="height:300vh">', '<div class="scene still" data-mode="mist" data-w="1832" data-h="837" style="height:150vh">')
rep('<div class="mark" style="left:40%;top:52%;font-size:var(--u)" data-from="0.42" data-to="1.0">\n        <div class="carve title">', '<div class="mark" style="left:40%;top:52%;font-size:var(--u)" data-from="0" data-to="1.0">\n        <div class="carve title">')
rep("var q=Math.min(1,p/0.42),e=ease(q);", "var q=1,e=1;")
s = s.replace('lol-plan-v60', 'lol-plan-v61')
open('versions/lol-plan-v61.html', 'w', encoding='utf-8').write(s)
print('ok')
