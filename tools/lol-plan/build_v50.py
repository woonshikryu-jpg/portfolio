# v49 -> v50: 남아 있던 「1단계」 표현을 모두 정리 — 짝인 「다음」에 맞춰 「먼저」, 나머지는 「광장 모드」로
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v49.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v49</title>', 'v50</title>')
rep('<span>다음 단계는 1단계의 지표가 좋아진 것을 확인한 뒤에 엽니다</span>', '<span>MMO 연결은 광장 모드의 지표가 좋아진 것을 확인한 뒤에 엽니다</span>')
rep('<span class="p3-n">1단계 · 롤 안의 광장 모드</span>', '<span class="p3-n">먼저 · 롤 안의 광장 모드</span>')
rep('<span class="sum">1단계 개발 범위를 한눈에</span>', '<span class="sum">처음 만드는 범위를 한눈에</span>')
rep('<span class="tag">1단계</span><h3>롤 안의 광장 모드</h3>', '<span class="tag">먼저</span><h3>롤 안의 광장 모드</h3>')
rep('기준의 구체적인 목표치는 1단계 출시 전 데이터로 정합니다.', '기준의 구체적인 목표치는 광장 모드 출시 전 데이터로 정합니다.')
rep('<span>1단계에 만든 것은 버려지지 않는다', '<span>광장 모드에 만든 것은 버려지지 않는다')
rep('<b>회사에게</b> 1단계 비용 = 다음의 기반', '<b>회사에게</b> 광장 모드 비용 = MMO의 기반')
rep('<b>나눠서 연다</b>: 1단계는 일부 서버·일부 계정에 먼저 열고', '<b>나눠서 연다</b>: 광장 모드는 일부 서버·일부 계정에 먼저 열고')
rep('학회 구역 분위기 3단계', '학회 구역 분위기 3종')
assert '1단계' not in s
s = s.replace('lol-plan-v49', 'lol-plan-v50')
open('versions/lol-plan-v50.html', 'w', encoding='utf-8').write(s)
print('ok')
