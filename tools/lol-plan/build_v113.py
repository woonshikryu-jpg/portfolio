# v112 -> v113: PART 02 연두로, 모든 제목 강조 낱말에 얇은 검정 테두리. 테두리가 생겨 밝은 배경에서도 더 밝고 쨍한 색을 씀
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v112.html', encoding='utf-8').read()
s = s.replace('v112</title>', 'v113</title>')
L = {0: '#8A55FF', 1: '#FF3B30', 2: '#8FD400', 3: '#4F5BFF', 4: '#FFC800', 5: '#1EA7FF', 6: '#FF3D8B', 7: '#22C55E'}
css = ''.join('.kp%d{--kl:%s}' % (n, c) for n, c in L.items()) + '.kp2{--kd:#B6F25A}'
o = '.032em'; c = '#111'
sh = ','.join('%s %s 0 %s' % (x, y, c) for x, y in [(o,'0'),('-'+o,'0'),('0',o),('0','-'+o),(o,o),('-'+o,'-'+o),(o,'-'+o),('-'+o,o)])
css += '.kw,.play-hl,.carve .kw,.mark .kw,.cloth .kw,.finale .kw,.doors-title .kw{text-shadow:%s!important}\n' % sh
k = s.rindex('</style>'); s = s[:k] + css + s[k:]
s = s.replace('lol-plan-v112', 'lol-plan-v113')
open('versions/lol-plan-v113.html', 'w', encoding='utf-8').write(s)
print('ok')
