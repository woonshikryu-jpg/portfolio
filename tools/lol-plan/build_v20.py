# v19 -> v20: PART 04 장면 제목 교체(「포로의 고향에서 쉬어 간다」는 내용과 맞지 않음),
# 점프 레이스 전부 삭제(만들기 까다롭고 롤 기본 규칙에서 벗어남) → 광장 즉석 놀이 2종(1:1 구역 · 포로 경주)
import os, re
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v19.html', encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) >= n, old[:60]; s = s.replace(old, new, n)
s = s.replace('v19</title>', 'v20</title>')

# PART 04 장면
rep('<h2>포로의 고향에서 쉬어 간다</h2><p>협곡의 숨바꼭질, 광장의 즉석 놀이</p>',
    '<h2>배울 것 없이, 바로 노는 롤</h2><p>협곡의 숨바꼭질, 광장의 즉석 놀이</p>')

# 4-2 장면 · 제목
rep('<h2>보다가, 뛰다가, 붙다가</h2><p>포로 경주 · 점프 레이스 · 1:1 구역</p>', '<h2>붙다가, 보다가</h2><p>1:1 구역 · 포로 경주</p>')
rep('<div><div class="sec-no">4-2 · 광장 즉석 놀이</div><h2>보다가, 뛰다가, 붙다가</h2></div>',
    '<div><div class="sec-no">4-2 · 광장 즉석 놀이</div><h2>붙다가, 보다가</h2></div>')
# 카드
rep('\n      <div class="card"><span class="tag">뛰기</span><h3>점프 레이스</h3><p class="one">솔방울 · 점멸 · 떨어지면 체크포인트</p></div>', '')
i = s.find('id="poro"'); j = s.find('<div class="grid g3" style="margin-bottom:18px">', i)
assert 0 < j - i < 400
s = s[:j] + '<div class="grid g2" style="margin-bottom:18px">' + s[j+len('<div class="grid g3" style="margin-bottom:18px">'):]
# 상세
a = s.find('<div class="fi"><div class="acc"><button class="acc-btn" aria-expanded="false"><span class="n">2</span><span>점프 레이스')
b = s.find('<div class="fi">', a + 10)
assert a > 0 and b > a
s = s[:a] + s[b:]
rep('<div class="fi"><div class="acc"><button class="acc-btn" aria-expanded="false"><span class="n">3</span><span>포로 경주',
    '<div class="fi" style="grid-column:1/-1"><div class="acc"><button class="acc-btn" aria-expanded="false"><span class="n">2</span><span>포로 경주')

# 다른 장의 언급
rep('1:1 구역 안에서 챔피언 바꾸기 · 점프 코스 · 포로 트랙 · 숨바꼭질 규칙(복제 · 목표)', '1:1 구역 안에서 챔피언 바꾸기 · 포로 트랙 · 숨바꼭질 규칙(복제 · 목표)')
rep('협곡 맵 · 미니언 · 와드 · 렌즈, 솔방울 · 점멸</td>', '협곡 맵 · 미니언 · 와드 · 렌즈</td>')
rep('<b>즉석 놀이</b>: 포로 경주 · 점프 레이스 · 1:1 구역(4-2).', '<b>즉석 놀이</b>: 1:1 구역 · 포로 경주(4-2).')
rep('즉석 놀이 3종', '즉석 놀이 2종', 3)

for bad in ['점프', '뛰다가', '뛰기', '3종', '포로의 고향']:
    assert bad not in re.sub(r'<script.*?</script>|<style.*?</style>', '', s, flags=re.S), bad
s = s.replace('lol-plan-v19', 'lol-plan-v20')
open('versions/lol-plan-v20.html', 'w', encoding='utf-8').write(s)
print('ok')
