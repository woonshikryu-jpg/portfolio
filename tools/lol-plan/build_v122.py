# v121 -> v122: PART 05 확장 계획에 「포로 경주에 내 전설이 출전」 — 출전자가 코스를 보고 적성 · 각질을 직접 고름, 적게 고른 쪽일수록 효과가 커지는 빈틈 공략, 외형만 내 것(공정)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v121.html', encoding='utf-8').read()
s = s.replace('v121</title>', 'v122</title>')
T = lambda k, v: '<tr><td>%s</td><td>%s</td></tr>' % (k, v)
acc = ('<div class="acc"><button class="acc-btn" aria-expanded="false"><span>광장 안에서 먼저 넓힐 것<span class="sum">포로 경주에 내 전설이가 출전한다</span></span><span class="plus" aria-hidden="true">+</span></button>'
 '<div class="acc-body"><div><div class="acc-inner"><table><tr><th style="width:22%">항목</th><th>내용</th></tr>'
 + T('무엇', 'TFT의 <b>전설이</b>를 포로 경주에 출전시킴. 8자리 중 <b>3자리</b>는 유저 출전, 나머지 5자리는 기본 포로. 출전 신청은 온 순서대로')
 + T('직접 고른다', '출전표에 코스가 공개되면, 출전자가 <b>적성</b>(직진 · 코너)과 <b>각질</b>(깡총 · 앞장 · 눈치 · 뒷심)을 직접 정함. 같은 코스를 보고도 유저마다 판단이 갈림')
 + T('빈틈 공략', '같은 적성 · 각질을 고른 포로가 <b>적을수록 그 효과가 조금 더 커짐</b>. 예: 커브 많은 길에서 모두 코너형을 고를 때 혼자 직진형이면, 직선 구간에서 속도 효과를 더 받음. 커브에서는 조금 따라잡혀도 인코스를 타면 순위를 어느 정도 지키고, 직선에서 한꺼번에 따라잡는 그림. 더해지는 효과에는 한도가 있어 무조건 이기지는 않음. 남들이 무엇을 고를지 읽는 싸움')
 + T('공정', '외형만 내 것. 어떤 전설이 스킨이든 능력치는 같음. 「능력치가 아니라 외형」 원칙 그대로')
 + T('주인 보상', '내 전설이가 1등 하면 출전 기록 · 칭호 같은 <b>꾸밈만</b>. 학회 기여는 다른 관객과 똑같이 내 포로를 골라 받음')
 + T('왜', '이미 판매한 전설이 스킨이 광장에서도 보임. TFT 유저가 광장에 들러 숨바꼭질 · 1:1 구역까지 접하게 됨')
 + '</table></div></div></div></div>')
anchor = '<div style="margin-top:18px">\n      <div class="acc">\n        <button class="acc-btn" aria-expanded="false"><span>다음으로 넘어가는 기준'
assert s.count(anchor) == 1
s = s.replace(anchor, '<div style="margin-top:18px">\n      ' + acc + '\n      <div class="acc">\n        <button class="acc-btn" aria-expanded="false"><span>다음으로 넘어가는 기준')
old2 = '매 판 직선과 커브의 비율이 바뀌어 출전표와 함께 공개(예: 「커브 많은 길」)'
assert s.count(old2) == 1
s = s.replace(old2, old2 + '. 커브에서는 인코스(안쪽)를 탄 포로가 자리를 지키기 쉬워 추월이 어렵고, 직선에서 추월이 많이 일어남')
s = s.replace('lol-plan-v121', 'lol-plan-v122')
open('versions/lol-plan-v122.html', 'w', encoding='utf-8').write(s)
print('ok')
