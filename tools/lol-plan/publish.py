# 완성 링크로 내보내기: 최신 versions/lol-plan-vN.html → hidden-summoners/index.html
# 주소: https://woonshikryu-jpg.github.io/portfolio/hidden-summoners/
# 사용: python3 tools/lol-plan/publish.py 90   (버전 번호 생략 시 가장 큰 번호)
import os, re, sys
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
if len(sys.argv) > 1: n = int(sys.argv[1])
else: n = max(int(m.group(1)) for f in os.listdir('versions') for m in [re.match(r'lol-plan-v(\d+)\.html$', f)] if m)
s = open('versions/lol-plan-v%d.html' % n, encoding='utf-8').read()
s = re.sub(r'(src|href)="img/', r'\1="../versions/img/', s)
s = re.sub(r"url\((['\"]?)img/", r"url(\1../versions/img/", s)
s = s.replace('href="index.html"', 'href="../"').replace('href="resume.html"', 'href="../versions/resume.html"')
s = re.sub(r'<title>[^<]*</title>', '<title>숨어 사는 소환사들 · 리그 오브 레전드 신규 콘텐츠 제안서 · 유운식</title>', s, count=1)
assert '"img/' not in s and "'img/" not in s
os.makedirs('hidden-summoners', exist_ok=True)
open('hidden-summoners/index.html', 'w', encoding='utf-8').write(s)
print('published v%d -> hidden-summoners/index.html' % n)
