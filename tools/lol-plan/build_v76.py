# v75 -> v76: 3-1 본단 맵 그림 교체(새 화풍), 번호 위치 다시 맞춤
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v75.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v75</title>', 'v76</title>')
rep('src="img/lol/plaza-map2.jpg"', 'src="img/lol/plaza-map3.jpg"')
old = ''.join(f'<span class="mp" style="left:{x};top:{y}"><b>{n}</b>{t}</span>' for n,x,y,t in [('1','50%','55%','가운데 광장'),('2','17%','40%','포로 서킷'),('3','50%','90%','1:1 구역'),('4','50%','6%','학회 본단'),('5','84%','20%','녹서스'),('6','86%','40%','데마시아'),('7','80%','72%','필트오버')])
new = ''.join(f'<span class="mp" style="left:{x};top:{y}"><b>{n}</b>{t}</span>' for n,x,y,t in [('1','52%','56%','가운데 광장'),('2','17%','42%','포로 서킷'),('3','52%','92%','1:1 구역'),('4','52%','6%','학회 본단'),('5','86%','16%','녹서스'),('6','86%','49%','데마시아'),('7','80%','71%','필트오버')])
rep(old, new)
s = s.replace('lol-plan-v75', 'lol-plan-v76')
open('versions/lol-plan-v76.html', 'w', encoding='utf-8').write(s)
print('ok')
