# v12 -> v13: 타깃 유저에 신규 유저(e스포츠로 관심이 생겨 롤을 처음 시작하는 뉴비) 추가,
# 시즌 상세 제목의 옛 세계관 문구 정리, 지표에 신규 정착 추가.
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v12.html', encoding='utf-8').read()

def rep(old, new):
    global s
    assert old in s, old[:60]
    s = s.replace(old, new, 1)

s = s.replace('v12</title>', 'v13</title>')

# 타깃 칩
rep('<span class="chip">랭크가 부담스러운 캐주얼 유저</span>',
    '<span class="chip">랭크가 부담스러운 캐주얼 유저</span><span class="chip">e스포츠를 보고 처음 시작한 신규 유저</span>')
rep('<span>세 유저의 하루<span class="sum">같은 클라이언트, 다른 이유로 접속한다</span>',
    '<span>네 유저의 하루<span class="sum">같은 클라이언트, 다른 이유로 접속한다</span>')
rep('<td>학회원으로 이름만 올려도 시즌 이야기에 참여한다</td></tr></table>',
    '<td>학회원으로 이름만 올려도 시즌 리그에 참여한다</td></tr>'
    '<tr><td>신규 유저</td><td>e스포츠를 보고 시작했지만, 첫 판부터 배울 것에 막혀 벽을 느낀다. TFT · 레전드 오브 룬테라는 조작이 달라 다른 게임처럼 느껴진다</td>'
    '<td>학습 없이 숨바꼭질 · 포로 경주로 협곡의 부쉬 · 와드 · 포로를 먼저 즐기고, 학회로 응원할 팀이 생긴다</td></tr></table>')
rep('<span class="note">세 유저 모두 기존 LoL 유저입니다. 새 유저를 데려오는 기획이 아니라, 떠나려는 유저가 머물 이유를 만드는 기획입니다.</span>',
    '<span class="note">떠나려는 기존 유저에게는 머물 이유를, e스포츠로 관심이 생긴 신규 유저에게는 학습 없이 롤을 즐기는 입구를 만듭니다.</span>')

# 시즌 상세 제목 (옛 세계관)
rep('<span>시즌 이야기 진행<span class="sum">미리 정한 결말 대신, 유저의 승부로 완성</span>',
    '<span>시즌 리그 진행<span class="sum">개막 → 주간 순위 → 우승, 기록이 쌓인다</span>')

# 지표
rep('주간 판 수 · 패배 후 종료 · 복귀 재이탈 · 협곡 없는 접속 · 항복률',
    '주간 판 수 · 패배 후 종료 · 복귀 재이탈 · 신규 정착 · 협곡 없는 접속 · 항복률')
rep('<tr><td>끝까지 하는 판</td>',
    '<tr><td>신규 정착</td><td>쉬운 입구가 있으면 협곡까지 간다</td><td>첫 주 캐주얼 경험 유무별 협곡 진입 · 잔존</td></tr><tr><td>끝까지 하는 판</td>')

s = s.replace('lol-plan-v12', 'lol-plan-v13')
open('versions/lol-plan-v13.html', 'w', encoding='utf-8').write(s)
print('ok')
