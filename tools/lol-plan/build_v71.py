# v70 -> v71: 마지막 그림 장면 삭제 — 결론 표 · 띠 바로 뒤에 글 한 줄로 담백하게 마무리(앞 비교표와 이어지는 문장)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v70.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v70</title>', 'v71</title>')
a = s.index('<!-- 마무리 · 멸망한 슈리마에서'); b = s.index('<section class="contact"', a)
s = s[:a] + s[b:]
rep('<div class="banner">접속 유지 · 스킨이 보일 무대 · 복귀와 신규의 입구 · IP 확장</div>\n',
    '<div class="banner">접속 유지 · 스킨이 보일 무대 · 복귀와 신규의 입구 · IP 확장</div>\n'
    '    <div class="closing"><p class="cl-a">협곡은 그대로,<br>광장 하나로 롤의 하루가 달라진다.</p></div>\n')
assert 'shurima-revived' not in s
s = s.replace('lol-plan-v70', 'lol-plan-v71')
open('versions/lol-plan-v71.html', 'w', encoding='utf-8').write(s)
print('ok')
