# v36 -> v37: 「비계」(공사장 발판) 표현을 「새 깃발 · 작업대」로. 3위 카드 · 장식 세트 · 낮은 순위도 밝게
# (광장은 시즌이 끝날 때 한 번 바뀌므로 「하나씩 걷히는」 표현도 정리)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v36.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert old in s, old[:60]; s = s.replace(old, new, 1)
s = s.replace('v36</title>', 'v37</title>')
rep('<p class="one">비계 · 「다음엔 우리 차례」</p>', '<p class="one">새 깃발 준비 · 「다음엔 우리 차례」</p>')
rep('(깃발, 조명, 노점, 비계, 현수막, 배경음)', '(깃발, 조명, 노점, 작업대, 현수막, 배경음)')
rep('비계가 하나씩 걷히는 모습이 곧 다음 판을 할 이유가 됩니다.', '작업대 위에서 새 깃발을 준비하는 모습이 곧 다음 시즌을 기다릴 이유가 됩니다.')
assert '비계' not in s
s = s.replace('lol-plan-v36', 'lol-plan-v37')
open('versions/lol-plan-v37.html', 'w', encoding='utf-8').write(s)
print('ok')
