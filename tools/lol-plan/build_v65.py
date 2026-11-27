# v64 -> v65: 핵심 질문을 회복탄력성으로 — 「롤이, 지친 하루를 회복하는 곳이 될 수 있을까?」
# PART 01 핵심 질문 · PART 07 장면 · 마지막 마무리를 장면(표지 그림)으로: 질문 → 답 「쉬어 간 자리에서, 다시 한 판을 할 힘이 난다.」
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v64.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v64</title>', 'v65</title>')
rep('<span class="pn">핵심 질문</span><h2>한 판을 하지 않아도<br>머물 이유가 있는 LoL은 가능할까?</h2>',
    '<span class="pn">핵심 질문</span><h2>롤이, 지친 하루를<br>회복하는 곳이 될 수 있을까?</h2>')
rep('<span class="pn">PART 07 · 결론</span><h2>점수 하나 대신,<br>머물 이유를 남긴다.</h2><p>한 판을 하지 않아도 들르고 싶은 롤</p>',
    '<span class="pn">PART 07 · 결론</span><h2>점수 하나 대신,<br>다시 일어설 힘을 남긴다.</h2><p>지친 하루가 쉬어 가는 롤</p>')
rep('협곡을 하지 않고 광장 · 놀이만 이용한 접속이 꾸준히 생길 것. "머물 이유"가 증명된 상태입니다.',
    '협곡을 하지 않고 광장 · 놀이만 이용한 접속이 꾸준히 생길 것. 광장이 쉬어 가는 곳으로 쓰이고 있다는 증거입니다.')
rep('떠나려는 기존 유저에게는 머물 이유를,', '지친 기존 유저에게는 쉬어 갈 곳을,')
# 마무리: 본문 안 블록을 빼고 장면으로
rep('\n    <div class="closing"><span class="cl-k">처음의 질문</span><p class="cl-q">한 판을 하지 않아도 머물 이유가 있는 LoL은 가능할까?</p><p class="cl-a">가능합니다.<br>협곡 밖에, 머물 광장 하나를 더하면.</p></div>', '')
rep('</section></div>\n\n<section class="contact" id="contact">',
'''</section></div>

<!-- 마무리 · 처음의 질문에 답하며 표지 그림으로 돌아옴 -->
<div class="scene still" data-mode="mist" data-w="1832" data-h="837" style="height:260vh">
  <div class="sticky">
    <div class="world">
      <img src="img/lol/cover-hq.jpg" alt="아이오니아 들판을 걷는 여행자">
      <div class="mark" style="left:50%;top:30%;font-size:var(--u)" data-from="0" data-to="1.0">
        <div class="carve"><span class="pn">처음의 질문</span><p>롤이, 지친 하루를 회복하는 곳이 될 수 있을까?</p></div>
      </div>
      <div class="mark" style="left:50%;top:56%;font-size:calc(var(--u) * 1.15)" data-from="0.3" data-to="1.0">
        <div class="carve"><h2>쉬어 간 자리에서,<br>다시 한 판을 할 힘이 난다.</h2></div>
      </div>
    </div>
    <div class="fx fx-mist"></div>
  </div>
</div>

<section class="contact" id="contact">''')
s = s.replace('lol-plan-v64', 'lol-plan-v65')
open('versions/lol-plan-v65.html', 'w', encoding='utf-8').write(s)
print('ok')
