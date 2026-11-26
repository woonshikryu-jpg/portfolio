# v9 = v8 + 정리: 장면은 분위기만, 글이 뜨면 배경이 물러남, 빈 그림 자리 없는 촘촘한 설명
# 사용: python3 tools/lol-plan/build_v8.py && python3 tools/lol-plan/build_v9.py
import re

s = open('versions/lol-plan-v8.html', encoding='utf-8').read()
s = s.replace('기획서 v8', '기획서 v9')


def bal(t, a):
    d = 0
    for m in re.finditer(r'<div\b|</div>', t[a:]):
        d += 1 if m.group(0) == '<div' else -1
        if d == 0:
            return a + m.end()


def kids(block):
    inner = block[block.index('>') + 1:block.rindex('</div>')]
    out = []; k = 0
    while True:
        m = re.search(r'<div\b', inner[k:])
        if not m: break
        st = k + m.start(); en = bal(inner, st); out.append(inner[st:en]); k = en
    return out


def section(sid):
    i = s.index(f'id="{sid}"'); return s.rfind('<section', 0, i), s.index('</section>', i)


# ---------- 1. 눈 장면: 원칙 네 개를 장면에서 빼고 제목만 ----------
a = s.index('data-mode="snow"'); a = s.rfind('<div class="scene', 0, a); b = bal(s, a)
sc = s[a:b]
marks = [m.start() for m in re.finditer(r'<div class="mark', sc)]
keep = []
for st in marks:
    en = bal(sc, st); blk = sc[st:en]
    keep.append((st, en, 'PART 04' in blk))
for st, en, k in reversed(keep):
    if not k:
        sc = sc[:st] + sc[en:]
sc = sc.replace('data-to="0.17"', 'data-to="1.0"')
sc = re.sub(r'(<div class="mark[^"]*"[^>]*data-from="[\d.]+" data-to=")[\d.]+(")', r'\g<1>1.0\2', sc)
sc = sc.replace('style="height:720vh"', 'style="height:300vh"', 1)
s = s[:a] + sc + s[b:]

# ---------- 2. 그림 자리가 비어 있는 장: 스크롤 이야기 → 촘촘한 2단 ----------
def flatten(sid, intro=''):
    global s
    A, B = section(sid); sec = s[A:B]
    i = sec.index('<div class="story'); j = bal(sec, i)
    vis, steps = kids(sec[i:j])
    items = [kids(x)[0] if kids(x) else x for x in kids(steps)]
    # .step 안의 내용 꺼내기
    items = [x[x.index('>') + 1:x.rindex('</div>')] for x in kids(steps)]
    extra = ''
    if sid == 'season':
        vis_inner = vis[vis.index('>') + 1:vis.rindex('</div>')]
        vis_inner = re.sub(r'<div class="ph"[^>]*>.*?</div>', '', vis_inner)
        extra = '<div class="flat-rank">' + vis_inner + '</div>'
        flat = '<div class="flat flat4">' + ''.join(f'<div class="fi">{x}</div>' for x in items) + '</div>' + extra
    else:
        flat = '<div class="flat">' + ''.join(f'<div class="fi">{x}</div>' for x in items) + '</div>'
    sec = sec[:i] + intro + flat + sec[j:]
    s = s[:A] + sec + s[B:]

for sid in ['plaza', 'season', 'reward', 'hide', 'poro']:
    flatten(sid)

# ---------- 3. 보고서 같은 꼬리표 정리 ----------
s = re.sub(r'<div class="rules"><span class="who-l">네 원칙</span>.*?</div>', '', s, flags=re.S)
A, B = section('hide')
s = s[:A] + s[A:B].replace('<p>관객만 아는 긴장. 아레나처럼 새 모드로 추가합니다.</p>',
                           '<p>실력보다 눈치와 운. 패치를 몰라도, 3~5분이면 한 판. 보기만 해도 긴장되는 모드.</p>') + s[B:]
s = s.replace('<span class="who-l">누구를 위해</span>', '<span class="who-l">이런 사람을 위해</span>')
s = s.replace('<span class="who-l">먼저 알아 둘 두 단어</span>', '<span class="who-l">롤을 모른다면</span>')

# ---------- 4. 연출 장면엔 글 하나만 (제목). 나머지 글은 설명 부분이 맡는다 ----------
HEIGHT = {'mist': 300, 'frame': 480, 'doors': 320, 'harbor': 300, 'dawn': 360}
for mode in ['mist', 'frame', 'doors', 'harbor', 'dawn']:
    a = s.index(f'data-mode="{mode}"'); a = s.rfind('<div class="scene', 0, a); b = bal(s, a)
    sc = s[a:b]
    pos = [m.start() for m in re.finditer(r'<div class="mark', sc)]
    for st in reversed(pos[1:]):
        sc = sc[:st] + sc[bal(sc, st):]
    WIN = {'mist': ('0.42', '1.0'), 'frame': ('0.33', '0.46'), 'dawn': ('0.55', '1.0')}
    if pos:
        f, t = WIN.get(mode, (None, '1.0'))
        if f:
            sc = re.sub(r'(<div class="mark[^"]*"[^>]*data-from=")[\d.]+(" data-to=")[\d.]+(")', lambda m: m.group(1) + f + m.group(2) + t + m.group(3), sc, count=1)
        else:
            sc = re.sub(r'(<div class="mark[^"]*"[^>]*data-from="[\d.]+" data-to=")[\d.]+(")', r'\g<1>1.0\2', sc, count=1)
    sc = re.sub(r'style="height:\d+vh"', f'style="height:{HEIGHT[mode]}vh"', sc, count=1)
    s = s[:a] + sc + s[b:]

css = '''
/* ===== v9 ===== */
/* 글이 뜨면 배경이 물러난다 */
.scene .world>img,.scene .pan,.scene .race-img img,.scene .harbor-frame>img{transition:filter .7s ease}
.scene .sticky:has(.mark.on:not(.scene-cap)) .world>img,
.scene .sticky:has(.mark.on) .pan{filter:blur(5px) brightness(.72) saturate(.85)}
.scene[data-mode="harbor"] .sticky:has(.mark.on) .harbor-frame>img{filter:blur(3px) brightness(.75)}
.scene[data-mode="snow"] .sticky:has(.mark.on) .world>img{filter:blur(4px) brightness(.8) saturate(.85)}
.scene .fx-light{transition:opacity .7s}
.scene .sticky:has(.mark.on) .fx-light{opacity:.25!important}
/* 필터를 스크립트가 쓰는 장면(안개·해돋이)은 막을 덮어 물러나게 */
.scene[data-mode="mist"] .world .mark,.scene[data-mode="dawn"] .world .mark{z-index:3}
.scene[data-mode="mist"] .world::after,.scene[data-mode="dawn"] .world::after{content:'';position:absolute;inset:0;z-index:2;pointer-events:none;background:radial-gradient(ellipse at 50% 55%,rgba(24,16,8,.5),rgba(24,16,8,.25) 60%,rgba(24,16,8,.12));backdrop-filter:blur(4px);opacity:0;transition:opacity .7s}
.scene[data-mode="mist"] .sticky:has(.mark.on) .world::after,.scene[data-mode="dawn"] .sticky:has(.mark.on) .world::after{opacity:1}
/* 촘촘한 설명 */
.flat{display:grid;grid-template-columns:1fr 1fr;gap:14px;align-items:start}
.flat4{grid-template-columns:repeat(4,1fr)}
.flat .fi>.acc,.flat .fi>.card{width:100%;height:100%}
.flat .fi:has(.acc.must){grid-column:1/-1}
.flat-rank{margin-top:22px}
.flat-rank .grid{grid-template-columns:repeat(3,1fr)!important}
.flat-rank .card{flex-direction:column!important;align-items:flex-start!important;padding:20px!important}
@media(max-width:900px){.flat,.flat4,.flat-rank .grid{grid-template-columns:1fr!important}}
/* 스크롤 이야기 빈 공간 줄이기 */
.story-steps{padding:8vh 0 14vh}
.story.pair .step{min-height:30vh}
.step{opacity:.38}
'''
j = s.rindex('</style>'); s = s[:j] + css + s[j:]
open('versions/lol-plan-v9.html', 'w', encoding='utf-8').write(s)
print('ok')
