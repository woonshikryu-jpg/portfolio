# v96 -> v97: 제목 강조를 구절이 아니라 낱말 하나로 줄임. 밝은 배경 강조색을 더 또렷한 주홍(#E4480A, 굵게)으로
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v96.html', encoding='utf-8').read()
s = s.replace('v96</title>', 'v97</title>')
K = lambda w: '<em class="kw">%s</em>' % w
M = {
 '숨어 사는': K('숨어') + ' 사는',
 '머무는 광장': '머무는 ' + K('광장'),
 '쉬어 가는 모드': K('쉬어') + ' 가는 모드',
 '남는 게': K('남는') + ' 게',
 '회복하는 곳': K('회복') + '하는 곳',
 '쉼과 기록': K('쉼') + '과 기록',
 '어느 문': '어느 ' + K('문'),
 '자기들만의 도시': '자기들만의 ' + K('도시'),
 '롤 안의 모드 하나': '롤 안의 ' + K('모드') + ' 하나',
 '학회의 기록': '학회의 ' + K('기록'),
 '바로 노는': '바로 ' + K('노는'),
 '모두 니코가 된다': '모두 ' + K('니코') + '가 된다',
 '증명하고': K('증명') + '하고',
 'MMO로 잇는다': 'MMO로 잇는다',
 '손해 보지 않는다': K('손해') + ' 보지 않는다',
 '머무는 LoL': K('머무는') + ' LoL',
}
for old, new in M.items():
    n = s.count(K(old)); assert n >= 1, old
    s = s.replace(K(old), new)
k = s.rindex('</style>')
s = s[:k] + '.kw{color:#E4480A;font-weight:900}.carve .kw,.cloth .kw,.mark .kw,.finale .kw,.contact .kw,.doors-title .kw{color:#FFC24D}\n' + s[k:]
s = s.replace('lol-plan-v96', 'lol-plan-v97')
open('versions/lol-plan-v97.html', 'w', encoding='utf-8').write(s)
import re
for m in re.finditer(r'<h2[^>]*>(.*?)</h2>', s, re.S):
    ws = re.findall(r'class="(?:kw|play-hl)">([^<]*)<', m.group(1))
    print(re.sub('<[^>]+>', '', m.group(1))[:34].replace('\n',' '), ws)
