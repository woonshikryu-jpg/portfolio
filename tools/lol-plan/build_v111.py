# v110 -> v111: 밝은 배경 강조색을 전부 채도 높은 선명한 색으로(흐릿한 계열 제거). 그림 장면용 밝은 색은 그대로
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v110.html', encoding='utf-8').read()
s = s.replace('v110</title>', 'v111</title>')
L = {0: '#7A3CF5', 1: '#EC2218', 2: '#00B0C2', 3: '#3A47FF', 4: '#E8AC00', 5: '#0A9BFF', 6: '#F2287C', 7: '#14AA48'}
k = s.rindex('</style>'); s = s[:k] + ''.join('.kp%d{--kl:%s}' % (n, c) for n, c in L.items()) + '\n' + s[k:]
s = s.replace('lol-plan-v110', 'lol-plan-v111')
open('versions/lol-plan-v111.html', 'w', encoding='utf-8').write(s)
print('ok')
