# v123 -> v124: PART 07 비교표 위에 「기존 LoL vs 본 기획」 그림 비교 — 실제 결과 화면(점수 하나로 끝) vs 학회 광장 맵(끝나면 광장으로), 하루 흐름 한 줄씩
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v123.html', encoding='utf-8').read()
s = s.replace('v123</title>', 'v124</title>')
def flow(steps, loop=False):
    out = '<div class="vs-flow">' + '<i>→</i>'.join('<span%s>%s</span>' % (' class="fin"' if (i == len(steps)-1) else '', t) for i, t in enumerate(steps))
    return out + ('<em class="loop">↺ 다시 광장으로</em>' if loop else '') + '</div>'
vs = ('<div class="vs">'
      '<div class="vs-col before"><span class="vs-tag">기존 LoL</span><figure><img src="img/lol/result-screen.png" alt="실제 결과 화면: S+를 받고도 랭크 점수 −23" loading="lazy"></figure>'
      '<b class="vs-h">경기가 끝나면, 점수 하나만 남고 끝</b>'
      + flow(['접속', '메뉴 화면', '대기', '협곡 30분', '점수 −23', '종료']) +
      '<span class="vs-cap">실제 결과 화면 · S+를 받고도 −23</span></div>'
      '<div class="vs-arrow" aria-hidden="true">→</div>'
      '<div class="vs-col after"><span class="vs-tag">본 기획</span><figure><img src="img/lol/plaza-map3.jpg" alt="학회 광장 맵: 포로 서킷, 가운데 광장, 1:1 구역, 학회 본단과 세 학회 구역" loading="lazy"></figure>'
      '<b class="vs-h">경기가 끝나도, 사람들이 있는 광장으로</b>'
      + flow(['접속', '광장에서 놀기', '큐 잡힘', '협곡', '학회 기여', '다시 광장 ↺']) +
      '<span class="vs-cap">학회 광장 맵 · 구상 이미지 (3-1)</span></div>'
      '</div>')
anchor = '<h2>경기로 끝나던 LoL에서, <em class="kw kp7">머무는</em> LoL로</h2></div></div>\n    <table>'
assert s.count(anchor) == 1
s = s.replace(anchor, anchor[:-len('<table>')] + vs + '\n    <table>')
F = "'Pretendard Variable',Pretendard,'Noto Sans KR',sans-serif"
css = ('.vs{display:grid;grid-template-columns:1fr 44px 1fr;gap:10px;align-items:stretch;margin:6px 0 22px}'
       '.vs-col{background:rgba(255,255,255,.92);border:1.5px solid #E3E6EA;border-radius:18px;padding:16px;display:flex;flex-direction:column;gap:10px}'
       '.vs-col.after{border-color:#22C55E;box-shadow:0 10px 26px rgba(20,120,60,.12)}'
       '.vs-tag{align-self:flex-start;font:800 12.5px/1 ' + F + ';padding:6px 11px;border-radius:999px;background:#E9ECEF;color:#495057}'
       '.vs-col.after .vs-tag{background:#14AA48;color:#fff}'
       '.vs-col figure{margin:0;border-radius:12px;overflow:hidden;aspect-ratio:16/9;background:#111}'
       '.vs-col img{width:100%;height:100%;object-fit:cover;display:block}'
       '.vs-col.before img{filter:grayscale(.35)}'
       '.vs-h{font:800 18px/1.35 ' + F + ';color:#111418}'
       '.vs-flow{display:flex;flex-wrap:wrap;align-items:center;gap:5px;font:700 12.5px/1 ' + F + '}'
       '.vs-flow span{padding:6px 9px;border-radius:8px;background:#F1F3F5;color:#343A40}'
       '.vs-flow i{font-style:normal;color:#ADB5BD}'
       '.vs-col.before .vs-flow span.fin{background:#495057;color:#fff}'
       '.vs-col.after .vs-flow span{background:#E8F7EE;color:#146C38}.vs-col.after .vs-flow span.fin{background:#14AA48;color:#fff}'
       '.vs-flow .loop{font-style:normal;color:#14AA48;font-weight:800;margin-left:4px}'
       '.vs-cap{font:500 12.5px/1.4 ' + F + ';color:#7A838E}'
       '.vs-arrow{display:flex;align-items:center;justify-content:center;font:800 28px/1 sans-serif;color:#14AA48}'
       '@media(max-width:800px){.vs{grid-template-columns:1fr}.vs-arrow{transform:rotate(90deg)}}\n')
k = s.rindex('</style>'); s = s[:k] + css + s[k:]
s = s.replace('lol-plan-v123', 'lol-plan-v124')
open('versions/lol-plan-v124.html', 'w', encoding='utf-8').write(s)
print('ok')
