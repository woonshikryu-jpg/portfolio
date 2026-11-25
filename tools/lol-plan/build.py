import json, base64, re, io, sys
from PIL import Image

root = '/home/claude/deck/project'
out = sys.argv[1]
d = json.load(open(root + '/deck.json'))
css = open(root + '/deck.css').read()
det = json.load(open('/home/claude/site/details.json'))
m = {'32ae8a62513d80163975037cc95b979f': 'cover', '74ad96ecff0364269a7d71b6d8644280': 'd1', '55d24f603c30629006ca01b872a2852f': 'd2', '89de7ce1e1627dc79b101e5148e030fe': 'd3b', 'b5c64142ef4d31a516bfadbf812412dc': 'd4', 'e3a00313fee8abc8a2356783c2a6cd61': 'd5', 'f96cf9d30d874f34d66dca7f190ccc83': 'closing', '9442195e2f1f658a21d725336d69c866': 'demacia', '23131aeb50422599c2fa826088e9fcbb': 'piltover', 'ea0bc0d38f9e871515e387d7c9445968': 'poro', 'f6efea43da20b8eed34246152c124466': 'noxus'}
uri = {}
for k, v in m.items():
    im = Image.open(f'/home/claude/imgwork/up_{v}.jpg'); im.thumbnail((1600, 1600)); b = io.BytesIO(); im.save(b, 'JPEG', quality=78)
    uri[k] = 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()

OPEN = re.compile(r'<div class="(card[^"]*|feat|row)"( style="[^"]*")?>')

def inject(html, tips):
    # walk the html, find each hoverable opening tag, then its matching </div>, insert tip before it
    out, pos, n = [], 0, 0
    while True:
        mo = OPEN.search(html, pos)
        if not mo or n >= len(tips):
            out.append(html[pos:]); break
        start = mo.start(); depth = 0; i = start
        tagre = re.compile(r'<div\b|</div>')
        for t in tagre.finditer(html, start):
            depth += 1 if t.group() == '<div' else -1
            if depth == 0:
                end = t.start(); break
        cls, sty = mo.group(1), mo.group(2) or ''
        opening = f'<div class="{cls} hov" tabindex="0"{sty}>'
        out.append(html[pos:start] + opening + html[mo.end():end] + '<span class="plus" aria-hidden="true">+</span><div class="tip" role="note">' + tips[n] + '</div></div>')
        pos = end + len('</div>'); n += 1
    return ''.join(out)

secs = []
for i in d['order']:
    s = open(f'{root}/slides/{i}.html').read()
    s = re.sub(r'<aside>.*?</aside>', '', s, flags=re.S)
    for k, u in uri.items(): s = s.replace('/_blob/' + k, u)
    if i in det: s = inject(s, det[i])
    secs.append('<div class="frame"><div class="scaler">' + s.strip() + '</div></div>')

fonts = 'https://fonts.googleapis.com/css2?family=Hahmlet:wght@400..800&family=Noto+Sans+KR:wght@400;500;700&family=Gaegu:wght@400;700&display=swap'
extra = '''
.hov{animation-fill-mode:backwards !important;position:relative;cursor:pointer;transition:border-color .2s,box-shadow .2s;outline:none}
.card.hov:hover,.card.hov:focus{border-color:var(--accent);box-shadow:0 18px 40px rgba(31,42,38,.14)}
.feat.hov:hover,.feat.hov:focus,.row.hov:hover,.row.hov:focus{background:rgba(255,253,248,.7)}
.plus{position:absolute;right:20px;top:20px;width:44px;height:44px;border-radius:50%;background:var(--accent-soft);color:var(--accent);font:700 30px/44px 'Noto Sans KR',sans-serif;text-align:center;transition:transform .3s,background .3s,color .3s}
.feat .plus,.row .plus{top:50%;margin-top:-22px;right:8px}
.hov:hover .plus,.hov:focus .plus{transform:rotate(45deg);background:var(--accent);color:#FFFDF8}
.tip{position:fixed;left:128px;right:128px;bottom:120px;z-index:20;background:#FFFDF8;border:3px solid var(--accent);border-radius:22px;padding:26px 34px;font:500 30px/1.55 'Noto Sans KR',sans-serif;color:var(--ink);box-shadow:0 20px 50px rgba(31,42,38,.18);opacity:0;transform:translateY(16px);transition:opacity .25s,transform .25s;pointer-events:none}
.hov:hover .tip,.hov:focus .tip{opacity:1;transform:none}
'''
html = f'''<!DOCTYPE html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>숨어 사는 소환사들 — 소환사의 도시 기획서 v2</title>
<link rel="stylesheet" href="{fonts}">
<style>
html,body{{margin:0;background:#E9E5DA}}
body{{counter-reset:page}}
*{{box-sizing:border-box}}
p,h1,h2,h3{{margin:0}}
.back{{position:fixed;left:16px;top:16px;z-index:30;background:rgba(255,253,248,.92);color:#1F2A26;font:600 15px/1 'Noto Sans KR',sans-serif;padding:10px 16px;border-radius:999px;text-decoration:none;box-shadow:0 4px 14px rgba(0,0,0,.12)}}
.hint{{text-align:center;font:500 15px/1.6 'Noto Sans KR',sans-serif;color:#555;margin:0}}
.deck{{max-width:1600px;margin:0 auto;padding:72px 24px 48px;display:flex;flex-direction:column;gap:28px}}
.frame{{position:relative;width:100%;aspect-ratio:16/9;overflow:hidden;border-radius:14px;box-shadow:0 10px 30px rgba(31,42,38,.12)}}
.scaler{{position:absolute;left:0;top:0;width:1920px;height:1080px;transform-origin:0 0}}
.scaler>section{{width:1920px;height:1080px;position:relative;overflow:hidden}}
.note{{text-align:center;font:14px/1.6 'Noto Sans KR',sans-serif;color:#6b6b6b;padding:8px 0 24px}}
{css}
{extra}
</style></head><body>
<a class="back" href="index.html">← 버전 모음</a>
<main class="deck">
<p class="hint">＋ 표시가 있는 카드에 마우스를 올리면 세부 설계가 펼쳐집니다</p>
{chr(10).join(secs)}
<p class="note">본 기획서는 라이엇 게임즈와 무관한 개인 기획안이며, 수록된 룬테라 이미지의 저작권은 Riot Games에 있습니다.</p>
</main>
<script>
(function(){{function f(){{document.querySelectorAll('.frame').forEach(function(fr){{fr.firstElementChild.style.transform='scale('+(fr.clientWidth/1920)+')'}})}}addEventListener('resize',f);f();}})();
</script>
</body></html>'''
open(out, 'w').write(html)
print(len(html) // 1024, 'KB', html.count('class="tip"'), 'tips')
