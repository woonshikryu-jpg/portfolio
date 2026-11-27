# v69 -> v70: 마지막 장면에서 「처음의 질문」 글귀 삭제, 결론 문장만 하늘 쪽 가운데에
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v69.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v69</title>', 'v70</title>')
rep('''      <div class="mark" style="left:50%;top:20%;font-size:var(--u)" data-from="0" data-to="1.0">
        <div class="carve"><span class="pn">처음의 질문</span><p>롤이, 지친 하루를 회복하는 곳이 될 수 있을까?</p></div>
      </div>
''', '')
rep('<div class="mark" style="left:50%;top:42%;font-size:calc(var(--u) * 1.15)" data-from="0.3" data-to="1.0">',
    '<div class="mark" style="left:50%;top:30%;font-size:calc(var(--u) * 1.15)" data-from="0.15" data-to="1.0">')
s = s.replace('<!-- 마무리 · 멸망한 슈리마에서 시작해, 사람이 모인 슈리마로 끝남 -->', '<!-- 마무리 · 멸망한 슈리마에서 시작해, 사람이 모인 슈리마로 끝남 · 결론 한 문장 -->')
s = s.replace('lol-plan-v69', 'lol-plan-v70')
open('versions/lol-plan-v70.html', 'w', encoding='utf-8').write(s)
print('ok')
