# v79 -> v80: PART 06 리스크 카드 설명을 「큐 연결 · 저사양 PC · 개발 비용 등」으로 되돌림
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v79.html', encoding='utf-8').read()
s = s.replace('v79</title>', 'v80</title>')
old = '<p class="one">기존 시스템을 다시 써서 위험이 작다</p>'
assert s.count(old) == 1
s = s.replace(old, '<p class="one">큐 연결 · 저사양 PC · 개발 비용 등</p>')
s = s.replace('lol-plan-v79', 'lol-plan-v80')
open('versions/lol-plan-v80.html', 'w', encoding='utf-8').write(s)
print('ok')
