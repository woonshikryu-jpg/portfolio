# v57 -> v58: 마무리 장면(아이오니아 절벽, 「점수 하나 대신, 머물 이유를 남긴다.」)을 맨 끝에서 PART 07 결론의 여는 장면으로 옮김.
# 결론 표 뒤에는 장면 없이 끝맺음 한 줄(이름 + 저작권 안내)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v57.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v57</title>', 'v58</title>')
a = s.index('<!-- 결말 · 뒤로 멀어짐 -->'); b = s.index('<div class="end">', a)
scene = s[a:b]
s = s[:a] + s[b:]
scene = scene.replace('<!-- 결말 · 뒤로 멀어짐 -->', '<!-- 7 · 결론 · 뒤로 멀어짐 -->')
old_cap = '<div class="carve"><span class="pn">HIDDEN SUMMONERS</span><h2>점수 하나 대신,<br>머물 이유를 남긴다.</h2><p>한 판을 하지 않아도 들르고 싶은 롤<br>유운식 · 게임 기획</p></div>'
assert old_cap in scene
scene = scene.replace(old_cap, '<div class="carve"><span class="pn">PART 07 · 결론</span><h2>점수 하나 대신,<br>머물 이유를 남긴다.</h2><p>한 판을 하지 않아도 들르고 싶은 롤</p></div>')
rep('</section><section class="r-shurima" id="compare">',
    '</section></div>\n\n' + scene.strip() + '\n<div class="ex r-ionia"><div class="ex-bg" aria-hidden="true"><img src="img/lol/ionia-hq.jpg" alt=""></div><section class="r-ionia" id="compare">')
rep('<div class="end">본 기획서는', '<div class="end"><b>유운식 · 게임 기획</b><br>본 기획서는')
k = s.rfind('</style>'); s = s[:k] + '.end{position:relative;z-index:1}\n' + s[k:]
rep('data-go="#compare"', 'data-go=".scene[data-mode=pull]"')
s = s.replace('lol-plan-v57', 'lol-plan-v58')
open('versions/lol-plan-v58.html', 'w', encoding='utf-8').write(s)
print('ok')
