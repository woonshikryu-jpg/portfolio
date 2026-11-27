# v81 -> v82: 펼침 버튼 + 가 원 가운데서 살짝 어긋나 보이던 것 — + 를 SVG 마스크로 그려 화면 배율과 관계없이 정확히 가운데, 빈 ::after 제거
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v81.html', encoding='utf-8').read()
s = s.replace('v81</title>', 'v82</title>')
k = s.rfind('</style>')
s = s[:k] + ".plus::before,.cmp-row .pl::before{width:14px!important;height:14px!important;background:currentColor!important;-webkit-mask:url(\"data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 14 14%27%3E%3Cpath d=%27M7 1v12M1 7h12%27 stroke=%27%23000%27 stroke-width=%272%27 stroke-linecap=%27round%27/%3E%3C/svg%3E\") center/14px 14px no-repeat;mask:url(\"data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 14 14%27%3E%3Cpath d=%27M7 1v12M1 7h12%27 stroke=%27%23000%27 stroke-width=%272%27 stroke-linecap=%27round%27/%3E%3C/svg%3E\") center/14px 14px no-repeat}.plus::after,.cmp-row .pl::after{display:none!important}\n" + s[k:]
s = s.replace('lol-plan-v81', 'lol-plan-v82')
open('versions/lol-plan-v82.html', 'w', encoding='utf-8').write(s)
print('ok')
