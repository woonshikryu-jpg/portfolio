# v74 -> v75: 3-1 본단 맵 그림 교체(더 가까운 구도), 번호 위치 다시 맞춤
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v74.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v74</title>', 'v75</title>')
rep('src="img/lol/plaza-map.jpg"', 'src="img/lol/plaza-map2.jpg"')
old = ''.join(f'<span class="mp" style="left:{x};top:{y}"><b>{n}</b>{t}</span>' for n,x,y,t in [('1','50%','46%','가운데 광장'),('2','17%','44%','포로 서킷'),('3','50%','86%','1:1 구역'),('4','51%','13%','학회 본단'),('5','86%','14%','녹서스'),('6','87%','40%','데마시아'),('7','81%','64%','필트오버')])
new = ''.join(f'<span class="mp" style="left:{x};top:{y}"><b>{n}</b>{t}</span>' for n,x,y,t in [('1','50%','55%','가운데 광장'),('2','17%','40%','포로 서킷'),('3','50%','90%','1:1 구역'),('4','50%','6%','학회 본단'),('5','84%','20%','녹서스'),('6','86%','40%','데마시아'),('7','80%','72%','필트오버')])
rep(old, new)
s = s.replace('lol-plan-v74', 'lol-plan-v75')
open('versions/lol-plan-v75.html', 'w', encoding='utf-8').write(s)
print('ok')
