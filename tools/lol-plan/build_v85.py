# v84 -> v85: 결론 띠에서 「회복한 유저는 다시 협곡으로 돌아온다.」 삭제, 결론 아래 문장 글자 크기 키움
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v84.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:60]); s = s.replace(old, new)
s = s.replace('v84</title>', 'v85</title>')
rep('지친 날엔 광장에서 쉬며 즐긴다.<br>회복한 유저는 다시 협곡으로 돌아온다.</p>', '지친 날엔 광장에서 쉬며 즐긴다.</p>')
rep(".finale p{margin:34px auto 0;max-width:640px;font:500 clamp(16px,1.5vw,19px)/1.8",
    ".finale p{margin:38px auto 0;max-width:760px;font:500 clamp(19px,1.9vw,24px)/1.7")
s = s.replace('lol-plan-v84', 'lol-plan-v85')
open('versions/lol-plan-v85.html', 'w', encoding='utf-8').write(s)
print('ok')
