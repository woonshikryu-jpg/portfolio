# v18 -> v19: 설명 부분 제목 옆(오른쪽)의 한 줄 문구를 모두 삭제 — 사용자: 역효과
import os, re
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v18.html', encoding='utf-8').read()
s = s.replace('v18</title>', 'v19</title>')
n = 0
def strip(m):
    global n
    blk = m.group(0)
    new = re.sub(r'\n\s*<p>.*?</p>', '', blk, flags=re.S)
    if new != blk: n += 1
    return new
s = re.sub(r'<div class="sec-head">.*?\n    </div>', strip, s, flags=re.S)
print('removed', n)
assert n == 11
s = s.replace('lol-plan-v18', 'lol-plan-v19')
open('versions/lol-plan-v19.html', 'w', encoding='utf-8').write(s)
