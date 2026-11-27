# v59 -> v60: 표지 부제를 두 줄로 — 「리그 오브 레전드 신규 콘텐츠 제안서」 / 「유운식」
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v59.html', encoding='utf-8').read()
s = s.replace('v59</title>', 'v60</title>')
old = '<p>리그 오브 레전드 신규 콘텐츠 제안서 · 게임기획 포트폴리오</p><p class="by">유운식 · 게임 기획</p>'
assert s.count(old) == 1
s = s.replace(old, '<p>리그 오브 레전드 신규 콘텐츠 제안서</p><p class="by">유운식</p>')
s = s.replace('lol-plan-v59', 'lol-plan-v60')
open('versions/lol-plan-v60.html', 'w', encoding='utf-8').write(s)
print('ok')
