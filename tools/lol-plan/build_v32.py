# v31 -> v32: 2-3 소속 규칙 아래 메모 — 「1단계」·「회수·기간은 예시」 삭제, 처음 3개 학회를 고른 이유(인지도) 추가
# PART 03 장면 부제 「1단계 · 」 삭제
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v31.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert old in s, old[:60]; s = s.replace(old, new, 1)
s = s.replace('v31</title>', 'v32</title>')
rep('<span class="note">1단계는 오랜 맞수인 두 세력(데마시아 · 녹서스)과 필트오버, 3개 학회로 시작합니다. 회수·기간은 예시이며 테스트로 확정합니다.</span>',
    '<span class="note">처음에는 3개 학회로 시작합니다. 인지도를 기준으로 골랐습니다. 데마시아 · 녹서스는 초창기부터 서로 맞서 온, 가장 널리 알려진 두 나라이고, 필트오버는 넷플릭스 시리즈 「아케인」으로 인지도가 크게 높아졌습니다.</span>')
rep('<p>1단계 · 학회 광장과 학회 시즌</p>', '<p>학회 광장과 학회 시즌</p>')
assert '회수' not in s
s = s.replace('lol-plan-v31', 'lol-plan-v32')
open('versions/lol-plan-v32.html', 'w', encoding='utf-8').write(s)
print('ok')
