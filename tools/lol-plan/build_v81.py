# v80 -> v81: PART 06 리스크 카드 설명 「기존 시스템 활용」
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v80.html', encoding='utf-8').read()
s = s.replace('v80</title>', 'v81</title>')
old = '<p class="one">큐 연결 · 저사양 PC · 개발 비용 등</p>'
assert s.count(old) == 1
s = s.replace(old, '<p class="one">기존 시스템 활용</p>')
s = s.replace('lol-plan-v80', 'lol-plan-v81')
open('versions/lol-plan-v81.html', 'w', encoding='utf-8').write(s)
print('ok')
