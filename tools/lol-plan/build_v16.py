# v15 -> v16: 한 장 요약 — 오른쪽 위 문구 삭제, 「롤을 모른다면」→「용어 정리」, 「이런 사람을 위해」→「타깃 유저」, 「네 유저의 하루」→「유저의 하루」
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v15.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert old in s, old[:60]; s = s.replace(old, new, 1)
s = s.replace('v15</title>', 'v16</title>')
rep('\n      <p>룬테라 바깥, 소환사들만의 도시에서<br>아끼는 세력의 이름을 걸고 프로와 같은 협곡에 선다.<br><b>e스포츠에서만 느끼던 소속감을, 내 솔로 랭크 한 판에도.</b></p>', '')
rep('<span class="who-l">롤을 모른다면</span>', '<span class="who-l">용어 정리</span>')
rep('<span class="who-l">이런 사람을 위해</span>', '<span class="who-l">타깃 유저</span>')
rep('<span>네 유저의 하루<span class="sum">', '<span>유저의 하루<span class="sum">')
s = s.replace('lol-plan-v15', 'lol-plan-v16')
open('versions/lol-plan-v16.html', 'w', encoding='utf-8').write(s)
print('ok')
