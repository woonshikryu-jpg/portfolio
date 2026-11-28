# v127 -> v128: 4-1 포로 경주 아래에 상세 기획서 · 플레이 프로토타입 바로가기. 5-1 출전표 예시 코스 비율을 엔진과 맞춤(커브 75%)
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v127.html', encoding='utf-8').read()
s = s.replace('v127</title>', 'v128</title>')
i = s.index('<span class="sum">내 포로 한 마리를 고르고, 응원하며 본다</span>')
j = s.index('</table><span class="note">큐가 잡히면 언제든', i); k = s.index('</span>', j) + len('</span>')
close = '</div></div></div></div>'
assert s[k:k + len(close)] == close
cta = ('<div class="poro-cta"><div><b>포로 경주는 상세 기획서와 프로토타입까지 만들었습니다</b><span>화면 흐름 · 수치 · 예외 처리 · 4,000판 밸런스 시뮬레이션, 그리고 직접 해 볼 수 있는 경주</span></div>'
       '<a class="pc-doc" href="/portfolio/hidden-summoners/poro-race/">상세 기획서 →</a><a class="pc-play" href="/portfolio/hidden-summoners/poro-race/play.html">▶ 직접 해 보기</a></div>')
s = s[:k + len(close)] + cta + s[k + len(close):]
s = s.replace('<span class="cv" style="flex:7">커브 70%</span><span class="sr" style="flex:3">직선 30%</span>', '<span class="cv" style="flex:3">커브 75%</span><span class="sr" style="flex:1">직선 25%</span>')
F = "'Pretendard Variable',Pretendard,'Noto Sans KR',sans-serif"
css = ('.poro-cta{margin-top:16px;display:flex;align-items:center;gap:12px;flex-wrap:wrap;background:#14301f;color:#fff;border-radius:16px;padding:16px 20px}'
       '.poro-cta>div{flex:1;min-width:240px;display:flex;flex-direction:column;gap:2px}'
       '.poro-cta b{font:800 16.5px/1.4 ' + F + '}.poro-cta span{font:500 13px/1.5 ' + F + ';color:#CFE3D6}'
       '.poro-cta a{text-decoration:none;font:800 14.5px/1 ' + F + ';padding:12px 16px;border-radius:12px;white-space:nowrap}'
       '.pc-doc{background:rgba(255,255,255,.12);color:#fff;border:1px solid rgba(255,255,255,.35)}.pc-play{background:#14AA48;color:#fff}\n')
k2 = s.rindex('</style>'); s = s[:k2] + css + s[k2:]
s = s.replace('lol-plan-v127', 'lol-plan-v128')
open('versions/lol-plan-v128.html', 'w', encoding='utf-8').write(s)
print('ok', s.count('커브 75%'))
