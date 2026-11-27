# v30 -> v31: 2-2 세계관 「이길 이유는 e스포츠에서 온다」→「소속감에서 온다」(아코디언 요약도 같이),
# 쏠림 대비의 「(세력 시즌 참고)」 삭제, PART 03 장면 부제 「세력 시즌」→「학회 시즌」
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v30.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert old in s, old[:60]; s = s.replace(old, new, 1)
s = s.replace('v30</title>', 'v31</title>')
rep('<b>이길 이유는 e스포츠에서 온다</b>', '<b>이길 이유는 소속감에서 온다</b>')
rep('룬테라에 영향 없이, 이길 이유를 e스포츠에서 가져온다', '룬테라에 영향 없이, 이길 이유를 소속감에서 가져온다')
rep('<b>학회원 1인당 평균 기여</b>로 정합니다(세력 시즌 참고).', '<b>학회원 1인당 평균 기여</b>로 정합니다.')
rep('<p>1단계 · 학회 광장과 세력 시즌</p>', '<p>1단계 · 학회 광장과 학회 시즌</p>')
assert '세력 시즌' not in s
s = s.replace('lol-plan-v30', 'lol-plan-v31')
open('versions/lol-plan-v31.html', 'w', encoding='utf-8').write(s)
print('ok')
