# v67 -> v68: 마지막 장면 결론 문장 「쉬어 간 자리에서, 다시 한 판을 할 힘이 난다.」→「롤의 즐거움은, 경쟁에만 있지 않다.」
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v67.html', encoding='utf-8').read()
s = s.replace('v67</title>', 'v68</title>')
old = '<h2>쉬어 간 자리에서,<br>다시 한 판을 할 힘이 난다.</h2>'
assert s.count(old) == 1
s = s.replace(old, '<h2>롤의 즐거움은,<br>경쟁에만 있지 않다.</h2>')
s = s.replace('lol-plan-v67', 'lol-plan-v68')
open('versions/lol-plan-v68.html', 'w', encoding='utf-8').write(s)
print('ok')
