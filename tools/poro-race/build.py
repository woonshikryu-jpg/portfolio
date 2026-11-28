# 포로 경주 프로토타입 · 상세 기획서 빌드: 엔진을 페이지에 넣고 두 곳(versions 기록본, hidden-summoners 완성본)에 씀
import os, sys
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
v = sys.argv[1] if len(sys.argv) > 1 else '1'
eng = open('tools/poro-race/engine.js', encoding='utf-8').read()
os.makedirs('hidden-summoners/poro-race', exist_ok=True)
for src, name in [('play.src.html', 'play'), ('spec.src.html', 'spec')]:
    path = 'tools/poro-race/' + src
    if not os.path.exists(path): continue
    s = open(path, encoding='utf-8').read().replace('__ENGINE__', eng)
    import json
    sim = json.load(open('tools/poro-race/sim-result.json', encoding='utf-8'))
    best = max(v for c in sim['circuits'] for k, v in c['win'].items() if '·' in k)
    s = s.replace('__SIM__', json.dumps(sim, ensure_ascii=False)).replace('__BEST__', '%.1f%%' % best)
    open('versions/poro-race-%s-v%s.html' % (name, v), 'w', encoding='utf-8').write(s.replace('__IMG__', 'img/lol/poro-hq.jpg').replace('__IMGDIR__', 'img/lol/'))
    out = 'hidden-summoners/poro-race/' + ('play.html' if name == 'play' else 'index.html')
    open(out, 'w', encoding='utf-8').write(s.replace('__IMG__', '../../versions/img/lol/poro-hq.jpg').replace('__IMGDIR__', '../../versions/img/lol/'))
    print('built', name, '->', out)
