# v52 -> v53: 1:1 구역 스펙에서 「+ 수정 하나(카서스 사파이어, 문도 루비)」 삭제
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v52.html', encoding='utf-8').read()
s = s.replace('v52</title>', 'v53</title>')
old = '<td>1레벨 · Q 하나만 · 신발 + 수정 하나(카서스 사파이어, 문도 루비) · 패시브 끔</td>'
assert s.count(old) == 1
s = s.replace(old, '<td>1레벨 · Q 하나만 · 신발 · 패시브 끔</td>')
assert '사파이어' not in s
s = s.replace('lol-plan-v52', 'lol-plan-v53')
open('versions/lol-plan-v53.html', 'w', encoding='utf-8').write(s)
print('ok')
