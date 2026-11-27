# v47 -> v48: PART 04 장면 배경을 프렐요드 마을 → 스노우다운 눈싸움(챔피언들이 노는 장면)으로, 제목을 왼쪽 위 하늘로.
# 4-1 설명 뒤 흐린 배경도 같은 그림
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v47.html', encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v47</title>', 'v48</title>')
rep('<img src="img/lol/d4-hq.jpg" alt="프렐요드 설원의 마을">', '<img src="img/lol/d4-snowdown.jpg" alt="눈싸움을 하며 노는 챔피언들">')
rep('<div class="mark frost" style="left:50%;top:32%;font-size:var(--u)" data-from="0.0" data-to="1.0">\n        <div class="carve ice"><span class="pn">PART 04',
    '<div class="mark frost" style="left:27%;top:24%;font-size:var(--u)" data-from="0.0" data-to="1.0">\n        <div class="carve ice"><span class="pn">PART 04')
rep('<img src="img/lol/d4-hq.jpg" alt=""></div><section class="r-frel alt" id="poro">', '<img src="img/lol/d4-snowdown.jpg" alt=""></div><section class="r-frel alt" id="poro">')
s = s.replace('lol-plan-v47', 'lol-plan-v48')
open('versions/lol-plan-v48.html', 'w', encoding='utf-8').write(s)
print('ok')
