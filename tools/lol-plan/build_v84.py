# v83 -> v84: 「왜 지금인가」를 PART 02 2-2에서 PART 01 1-2로 옮김(네 가지 문제 바로 뒤). 세계관 2-3 → 2-2, 참조 번호 갱신
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v83.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v83</title>', 'v84</title>')
a = s.index('<section class="cs cs-tint" id="whynow">'); b = s.index('</section>', a) + len('</section>')
why = s[a:b]
s = s[:a] + s[b:]
rep('<div class="sec-no">2-2 · 왜 지금인가</div>', '<div class="sec-no">1-2 · 왜 지금인가</div>') if False else None
why = why.replace('<div class="sec-no">2-2 · 왜 지금인가</div>', '<div class="sec-no">1-2 · 왜 지금인가</div>')
assert '1-2 · 왜 지금인가' in why
i = s.index('id="walls"'); j = s.index('</section></div>', i) + len('</section>')
s = s[:j] + why + s[j:]
rep('<div class="sec-no">2-3 · 세계관</div>', '<div class="sec-no">2-2 · 세계관</div>')
rep('내 손짓에 바로 반응이 옵니다(2-2 참고)', '내 손짓에 바로 반응이 옵니다(1-2 참고)')
rep('우승 학회의 양식으로 꾸며져 있습니다(2-3 참고)', '우승 학회의 양식으로 꾸며져 있습니다(2-2 참고)')
s = s.replace('lol-plan-v83', 'lol-plan-v84')
open('versions/lol-plan-v84.html', 'w', encoding='utf-8').write(s)
print('ok')
