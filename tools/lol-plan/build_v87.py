# v86 -> v87: 모든 제목(h2)에서 강조할 단어만 색을 달리함 (밝은 배경 = 주황, 그림·어두운 배경 = 금색). 「놀다」는 v86 그대로
import os, re
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v86.html', encoding='utf-8').read()
s = s.replace('v86</title>', 'v87</title>')
KW = {
 '숨어 사는 소환사들': ['숨어 사는'],
 'LoL에 머무는 광장과': ['머무는 광장', '쉬어 가는 모드'],
 '경쟁에 지친 소환사': ['지친'],
 '왜 남는 게 없을까': ['남는 게'],
 '롤이, 지친 하루를': ['회복하는 곳'],
 '사람들은 게임을 떠나': ['영상'],
 '탁 트인 쉼터를 세운다': ['쉼터'],
 '경쟁은 협곡에서,<br>쉼과 기록은': ['쉼과 기록'],
 '이번 시즌,<br>어느 문을': ['어느 문'],
 '전쟁의 학회가 사라진 뒤': ['자기들만의 도시'],
 '사람이 모이는 항구': ['모이는'],
 '새 게임이 아니라': ['롤 안의 모드 하나'],
 '협곡의 결과가 학회의 기록으로': ['학회의 기록'],
 '이긴 학회는 협곡에서 보인다': ['보인다'],
 '배울 것 없이, 바로 노는 롤': ['바로 노는'],
 '숨바꼭질: 협곡에서': ['모두 니코가 된다'],
 '다시 떠오르는 태양': ['다시'],
 '롤 안에서 증명하고': ['증명하고', 'MMO로 잇는다'],
 '협곡을 덜 해도': ['손해 보지 않는다'],
 '경쟁만 있던 롤에': ['회복'],
 '경기로 끝나던 LoL에서': ['머무는 LoL'],
 '롤의 즐거움은,<br>경쟁에만': ['경쟁에만'],
}
used = set()
def fix(m):
    inner = m.group(2)
    for key, words in KW.items():
        if inner.startswith(key) and key not in used:
            used.add(key)
            for w in words:
                assert inner.count(w) == 1, (key, w)
                inner = inner.replace(w, '<em class="kw">%s</em>' % w)
            break
    return '<h2%s>%s</h2>' % (m.group(1), inner)
s = re.sub(r'<h2([^>]*)>(.*?)</h2>', fix, s, flags=re.S)
assert used == set(KW), set(KW) - used
css = ('.kw{font-style:normal;color:#E07A1F}'
       '.carve .kw,.cloth .kw,.mark .kw,.finale .kw,.contact .kw,.doors-title .kw{color:#FFC24D}\n')
k = s.rindex('</style>'); s = s[:k] + css + s[k:]
s = s.replace('lol-plan-v86', 'lol-plan-v87')
open('versions/lol-plan-v87.html', 'w', encoding='utf-8').write(s)
print('ok', len(used))
