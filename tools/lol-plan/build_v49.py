# v48 -> v49: 4-2 숨바꼭질 장면 · 설명 뒤 배경을 포로 → 니코(덤불에서 모습을 드러내는 니코)로, 글귀는 얼굴을 피해 오른쪽으로, 움직이는 니코 영상(정지 그림은 대기 화면), 「모두 니코가 된다」
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v48.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v48</title>', 'v49</title>')
rep('<!-- 숨바꼭질 · 숨어 있던 포로가 드러남 -->', '<!-- 숨바꼭질 · 덤불 속 니코가 드러남 -->')
rep('<div class="race-img"><img src="img/lol/poro-hq.jpg" alt="눈밭에서 모습을 드러낸 포로들"></div>',
    '<div class="race-img"><video poster="img/lol/neeko-hq.jpg" autoplay muted loop playsinline preload="auto" aria-label="덤불 속에서 모습을 드러낸 니코"><source src="img/lol/neeko-anim.webm" type="video/webm"><source src="img/lol/neeko-anim.mp4" type="video/mp4"></video></div>')
rep('<img src="img/lol/poro-hq.jpg" alt=""></div><section class="r-frel" id="hide">', '<img src="img/lol/neeko-hq.jpg" alt=""></div><section class="r-frel" id="hide">')
rep('<div class="mark scene-cap pop" style="left:76%;top:24%;', '<div class="mark scene-cap pop" style="left:82%;top:24%;')
rep('<p>협곡에서, 모두가 니코가 된다</p>', '<p>협곡에서, 모두 니코가 된다</p>')
rep('<h2>숨바꼭질: 협곡에서,<br>모두가 니코가 된다</h2>', '<h2>숨바꼭질: 협곡에서,<br>모두 니코가 된다</h2>')
rep("ri.querySelector('img').style.transform", "ri.querySelector('img,video').style.transform")
rep('.race-img img{width:100%;height:100%;object-fit:cover}', '.race-img img,.race-img video{width:100%;height:100%;object-fit:cover;display:block}')
rep('.race-img img{transition:none;will-change:transform}', '.race-img img,.race-img video{transition:none;will-change:transform}')
s = s.replace('lol-plan-v48', 'lol-plan-v49')
open('versions/lol-plan-v49.html', 'w', encoding='utf-8').write(s)
print('ok')
