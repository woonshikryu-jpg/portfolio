# v76 -> v77: PART 06 카드 3장 글 정리 — 설명을 짧은 한 줄로, 띠 문구도 짧게
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v76.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v76</title>', 'v77</title>')
rep('<p class="one">롤은 능력치가 아니라 외형을 판다 · 지금은 협곡 30분 안에서만 보이는 스킨이, 광장 · 숨바꼭질 · 1:1 구역에서도 보인다</p>',
    '<p class="one">협곡 밖에서도 내 스킨이 보인다</p>')
rep('<p class="one">접속일 · 스킨 구매와 착용 · 협곡 경기 매너(항복 · 탈주 · 신고) · 복귀 재이탈 · 신규 정착</p>',
    '<p class="one">접속 · 스킨 · 경기 매너 · 복귀 · 신규</p>')
rep('<p class="one">큐 연결 · 저사양 PC · 개발 비용 · 고의 방해 플레이 · 랭크 스트레스</p>',
    '<p class="one">큐 연결 · 저사양 PC · 개발 비용 등</p>')
rep('<div class="banner" style="margin-top:18px">협곡 판 수가 줄어도, 접속 · 스킨 · 경기 매너가 유지되면 성공이다</div>',
    '<div class="banner" style="margin-top:18px">판 수가 줄어도, 유저가 남아 있으면 성공이다</div>')
s = s.replace('lol-plan-v76', 'lol-plan-v77')
open('versions/lol-plan-v77.html', 'w', encoding='utf-8').write(s)
print('ok')
