# v78 -> v79: PART 06 리스크 카드 설명 「큐가 잡히면 바로 협곡으로 간다」→「기존 시스템을 다시 써서 위험이 작다」
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v78.html', encoding='utf-8').read()
s = s.replace('v78</title>', 'v79</title>')
old = '<p class="one">큐가 잡히면 바로 협곡으로 간다</p>'
assert s.count(old) == 1
s = s.replace(old, '<p class="one">기존 시스템을 다시 써서 위험이 작다</p>')
s = s.replace('lol-plan-v78', 'lol-plan-v79')
open('versions/lol-plan-v79.html', 'w', encoding='utf-8').write(s)
print('ok')
