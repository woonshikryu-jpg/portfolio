# v65 -> v66: 마지막 장면 배경을 표지 그림 → 사람이 모여 활기를 되찾은 슈리마로(시작의 멸망한 슈리마와 짝)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v65.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v65</title>', 'v66</title>')
a = s.index('<!-- 마무리 · 처음의 질문에 답하며 표지 그림으로 돌아옴 -->'); b = s.index('<section class="contact"', a)
blk = s[a:b]
blk2 = blk.replace('<!-- 마무리 · 처음의 질문에 답하며 표지 그림으로 돌아옴 -->', '<!-- 마무리 · 멸망한 슈리마에서 시작해, 사람이 모인 슈리마로 끝남 -->')
blk2 = blk2.replace('data-w="1832" data-h="837"', 'data-w="1920" data-h="1080"')
blk2 = blk2.replace('<img src="img/lol/cover-hq.jpg" alt="아이오니아 들판을 걷는 여행자">', '<img src="img/lol/shurima-revived.jpg" alt="사람과 짐승의 행렬이 모여드는, 다시 살아난 슈리마의 도시">')
blk2 = blk2.replace('style="left:50%;top:30%;font-size:var(--u)"', 'style="left:50%;top:20%;font-size:var(--u)"')
blk2 = blk2.replace('style="left:50%;top:56%;font-size:calc(var(--u) * 1.15)"', 'style="left:50%;top:42%;font-size:calc(var(--u) * 1.15)"')
assert blk2 != blk and 'shurima-revived' in blk2
s = s[:a] + blk2 + s[b:]
s = s.replace('lol-plan-v65', 'lol-plan-v66')
open('versions/lol-plan-v66.html', 'w', encoding='utf-8').write(s)
print('ok')
