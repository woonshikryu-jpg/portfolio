# v44 -> v45: PART 04 순서 바꾸기 — 캐주얼 모드 장면 → 4-1 광장 즉석 놀이 → 포로 장면(숨었다 나타나는 연출) → 4-2 숨바꼭질.
# 포로 장면 글귀를 숨바꼭질로, 설명 뒤 흐린 배경도 순서에 맞게 교체, 장 번호 참조(2-1 표 · 3-1) 갱신
import os, re
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v44.html', encoding='utf-8').read()
s = s.replace('v44</title>', 'v45</title>')
def cut(a_mark, b_mark):
    a = s.index(a_mark); b = s.index(b_mark, a); return a, b
# 블록 경계
h_a = s.index('<div class="ex r-frel"><div class="ex-bg" aria-hidden="true"><img src="img/lol/d4-hq.jpg" alt=""></div><section class="r-frel alt" id="hide">')
sc_a = s.index('<!-- 포로 경주 · 달려 들어옴 -->')
p_a = s.index('<div class="ex r-frel"><div class="ex-bg" aria-hidden="true"><img src="img/lol/poro-hq.jpg" alt=""></div><section class="r-frel" id="poro">')
p_end = s.index('</section></div>', p_a) + len('</section></div>')
hide = s[h_a:sc_a]; scene = s[sc_a:p_a]; poro = s[p_a:p_end]
# 즉석 놀이 → 4-1, 프렐요드 배경 · alt
poro = poro.replace('<img src="img/lol/poro-hq.jpg" alt=""></div><section class="r-frel" id="poro">',
                    '<img src="img/lol/d4-hq.jpg" alt=""></div><section class="r-frel alt" id="poro">', 1)
assert poro.count('<div class="sec-no">4-2 · 광장 즉석 놀이</div>') == 1
poro = poro.replace('<div class="sec-no">4-2 · 광장 즉석 놀이</div>', '<div class="sec-no">4-1 · 광장 즉석 놀이</div>')
# 숨바꼭질 → 4-2, 포로 배경
hide = hide.replace('<img src="img/lol/d4-hq.jpg" alt=""></div><section class="r-frel alt" id="hide">',
                    '<img src="img/lol/poro-hq.jpg" alt=""></div><section class="r-frel" id="hide">', 1)
assert hide.count('<div class="sec-no">4-1 · 정식 모드</div>') == 1
hide = hide.replace('<div class="sec-no">4-1 · 정식 모드</div>', '<div class="sec-no">4-2 · 정식 모드</div>')
# 포로 장면 글귀
old_cap = '<div class="carve ice"><span class="pn">4-2 · 광장 즉석 놀이</span><h2>직접 겨루거나, 구경하며 즐기거나</h2><p>1:1 구역 · 포로 경주</p></div>'
assert old_cap in scene
scene = scene.replace('<!-- 포로 경주 · 달려 들어옴 -->', '<!-- 숨바꼭질 · 숨어 있던 포로가 드러남 -->')
scene = scene.replace(old_cap, '<div class="carve ice"><span class="pn">4-2 · 정식 모드</span><h2>숨바꼭질</h2><p>협곡에서, 모두가 니코가 된다</p></div>')
scene = scene.replace('alt="눈밭 위의 포로들"', 'alt="눈밭에서 모습을 드러낸 포로들"')
# 새 순서: (즉석 놀이) + 장면 + (숨바꼭질) — 원래 숨바꼭질 앞 구분 주석/여백은 장면 블록 쪽에 포함
s = s[:h_a] + poro + '\n\n\n' + scene.rstrip() + '\n' + hide.rstrip() + s[p_end:]
# PART 04 장면 부제
s = s.replace('<p>협곡의 숨바꼭질, 광장의 즉석 놀이</p>', '<p>광장의 즉석 놀이, 협곡의 숨바꼭질</p>', 1)
# 장 번호 참조
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old); s = s.replace(old, new)
rep('보기만 해도 되는 포로 경주</td><td>3-1 · 4-2</td>', '보기만 해도 되는 포로 경주</td><td>3-1 · 4-1</td>')
rep('랭크 점수 걱정 없이 바뀐 점을 직접 써 본다</td><td>4-1</td>', '랭크 점수 걱정 없이 바뀐 점을 직접 써 본다</td><td>4-2</td>')
rep('1:1 구역 · 포로 경주(4-2)', '1:1 구역 · 포로 경주(4-1)')
s = s.replace('lol-plan-v44', 'lol-plan-v45')
open('versions/lol-plan-v45.html', 'w', encoding='utf-8').write(s)
print('ok')
