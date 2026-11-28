# v114 -> v115: PART 01 4번 카드 「남는 건 점수뿐」에 사람이 남지 않는 문제 추가 — 결론 「사람들이 기다리는 광장」과 짝
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v114.html', encoding='utf-8').read()
s = s.replace('v114</title>', 'v115</title>')
old = '<h3>남는 건 점수뿐</h3><p>30분의 긴장 · 스트레스 → 보상은 숫자 하나</p>'
assert s.count(old) == 1
s = s.replace(old, '<h3>남는 건 점수뿐</h3><p>30분의 긴장 → 남는 건 숫자 하나, 끝나면 남이 되는 팀원</p>')
s = s.replace('lol-plan-v114', 'lol-plan-v115')
open('versions/lol-plan-v115.html', 'w', encoding='utf-8').write(s)
print('ok')
