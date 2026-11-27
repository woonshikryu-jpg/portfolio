# v25 -> v26: 3-1 「친구」 줄 — 친구뿐 아니라 처음 보는 소환사와도 친해질 수 있게, 채팅 허용(막으면 친구가 될 수 없음)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v25.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert old in s, old[:60]; s = s.replace(old, new, 1)
s = s.replace('v25</title>', 'v26</title>')
rep('<span class="c2">광장에 서 있는 챔피언 · 클릭하면 파티</span>', '<span class="c2">친구도, 처음 보는 소환사도 · 대화하고 친구가 된다</span>')
rep('''<li>같은 채널에는 <b>온라인 친구</b>와 같은 학회원이 우선 모입니다.</li>
            <li>친구를 클릭하면 <b>파티 초대 · 프로필</b> 메뉴가 뜹니다. 친구 목록에서 하던 일을 광장에서 그대로 합니다.</li>
            <li><b>모르는 사람과는 채팅 없이 감정표현만</b> 됩니다. 광장이 또 하나의 갈등 공간이 되지 않게 하기 위해서입니다.</li>''',
'''<li>채널에는 <b>친구 · 같은 학회원 · 처음 보는 소환사</b>가 함께 있습니다. 친구가 있는 채널로 바로 따라갈 수도 있고, 늘 새로운 사람도 섞여 있습니다.</li>
            <li>누구든 클릭하면 <b>대화 · 친구 추가 · 파티 초대 · 프로필</b> 메뉴가 뜹니다. 같이 놀다 마음이 맞으면 친구가 되고, 그대로 같이 큐를 잡습니다.</li>
            <li><b>채팅은 열어 둡니다.</b> 주변에 말풍선으로 뜨는 광장 채팅과 귓속말이 있고, 처음 보는 사람과도 대화할 수 있습니다. 광장은 새 친구를 만드는 곳입니다.</li>
            <li><b>갈등 대비</b>: 롤에 이미 있는 채팅 필터 · 차단 · 신고 · 제재를 그대로 씁니다. 말풍선 채팅은 설정에서 끌 수 있습니다.</li>''')
rep('<li>광장 채팅 · 거래 → 광장이 또 하나의 갈등 공간이 되지 않도록.</li>', '<li>유저 간 거래 → 롤에 원래 없는 기능이라 만들지 않습니다.</li>')
rep('<tr><td>학회 쏠림</td><td>1인당 평균 기여로 순위</td></tr>',
    '<tr><td>광장 채팅 갈등</td><td>기존 채팅 필터 · 차단 · 신고 · 제재 그대로 · 말풍선 채팅은 끌 수 있음</td></tr>\n      <tr><td>학회 쏠림</td><td>1인당 평균 기여로 순위</td></tr>')
assert '모르는 사람과는' not in s and '갈등 공간이 되지' not in s
s = s.replace('lol-plan-v25', 'lol-plan-v26')
open('versions/lol-plan-v26.html', 'w', encoding='utf-8').write(s)
print('ok')
