# v129 -> v130: 4-1 포로 경주 응원을 「기세」로 바꿈(기운은 간식만, 응원은 순위와 상관없이 상황에 따라 거듦)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v129.html', encoding='utf-8').read()
s = s.replace('v129</title>', 'v130</title>')
def rep(a, b):
    global s
    assert s.count(a) == 1, a[:60]
    s = s.replace(a, b)
rep('<span>응원과 간식은 포로의 기운을 채워 줍니다. 뒤처졌을 때만 응원이 통하고, 기운이 바닥일 때 준 간식이 가장 큰 힘이 됩니다.</span>',
    '<span>간식은 기운을 가득 채우고, 응원은 언제든 기세를 실어 줍니다. 막혔을 때 응원하면 틈을 더 빨리 찾습니다. 응원만으로 이기지는 못합니다.</span>')
rep('<b>내 포로가 5~8위일 때만</b> 받은 응원 비율만큼 기운이 조금씩 참. 1~4위일 때는 효과가 없음. 꼴찌가 될 확률은 크게 줄지만 1등 확률은 거의 그대로라, 응원을 많이 받아도 이긴다는 보장은 없음',
    '기운은 채우지 않고 <b>순위와 상관없이 기세</b>를 실어 줌. <b>앞이 막혔을 때</b> 틈을 더 빨리 찾아 비켜 나가고, <b>선두일 때</b> 맞바람을 덜 맞고, <b>뒤따를 때</b> 더 멀리서 슬립스트림을 탐. 뒤처질수록 효과가 커서 꼴찌가 될 확률은 크게 줄지만 1등 확률은 조금 오를 뿐이라, 응원을 많이 받아도 이긴다는 보장은 없음')
s = s.replace('lol-plan-v129', 'lol-plan-v130')
open('versions/lol-plan-v130.html', 'w', encoding='utf-8').write(s)
print('ok')
