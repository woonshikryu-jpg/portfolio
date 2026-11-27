# v37 -> v38: 3위 광장 = 「재정비」 대신 격려 현수막(「고생했다, 다음 시즌 더 힘내자」)으로 응원하는 모습
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v37.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert old in s, old[:60]; s = s.replace(old, new, 1)
s = s.replace('v37</title>', 'v38</title>')
rep('<h3>재정비</h3><p class="one">새 깃발 준비 · 「다음엔 우리 차례」</p>', '<h3>격려</h3><p class="one">현수막 · 「고생했다, 다음 시즌 더 힘내자」</p>')
rep('(깃발, 조명, 노점, 작업대, 현수막, 배경음)', '(깃발, 조명, 노점, 현수막, 배경음)')
rep('낮은 순위 학회의 광장은 다음 시즌을 준비하는 모습이 됩니다.', '3위 학회의 광장에는 학회원을 응원하는 격려 현수막이 걸립니다.')
rep('3위는 재정비 분위기로', '3위는 격려 현수막이 걸린 모습으로')
rep('그래서 재정비는 "진 학회"가 아니라 "준비 중인 학회"로 그립니다. 작업대 위에서 새 깃발을 준비하는 모습이 곧 다음 시즌을 기다릴 이유가 됩니다.',
    '그래서 3위 광장에는 「고생했다, 다음 시즌 더 힘내자」 현수막을 걸어, 진 학회를 깎아내리지 않고 응원합니다. 함께 고생한 학회원끼리 다음 시즌을 다시 해 볼 이유가 됩니다.')
rep('<p class="one">축제 or 재정비</p>', '<p class="one">축제 · 일상 · 격려</p>')
assert '재정비' not in s and '작업대' not in s
s = s.replace('lol-plan-v37', 'lol-plan-v38')
open('versions/lol-plan-v38.html', 'w', encoding='utf-8').write(s)
print('ok')
