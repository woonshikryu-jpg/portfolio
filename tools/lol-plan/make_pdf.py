import base64, sys
from playwright.sync_api import sync_playwright

SRC = 'file:///home/claude/portfolio/versions/lol-plan-v10.html'
OUT = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/pdfmake/out.pdf'
W, H = 1440, 810

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
    pg = b.new_page(viewport={'width': W, 'height': H})
    pg.goto(SRC, wait_until='load')
    pg.wait_for_timeout(1500)
    pg.add_style_tag(content='.rail,.back,.credit{display:none!important}')
    n = pg.evaluate("document.querySelectorAll('.scene').length")
    shots = []
    for i in range(n):
        top, hgt = pg.evaluate(f"(()=>{{const s=document.querySelectorAll('.scene')[{i}];const r=s.getBoundingClientRect();return [r.top+scrollY,s.offsetHeight]}})()")
        best, best_score, best_y = None, -1, top
        steps = 24
        for k in range(steps + 1):
            y = top + (hgt - H) * k / steps
            pg.evaluate(f"window.scrollTo(0,{y})")
            pg.wait_for_timeout(120)
            sc = pg.evaluate(f"""(()=>{{const s=document.querySelectorAll('.scene')[{i}];
              let v=0;s.querySelectorAll('.mark.on').forEach(m=>v+=1);
              if(s.querySelector('.door.open'))v+=s.querySelectorAll('.door.open').length*0.5;
              return v}})()""")
            if sc > best_score:
                best_score, best_y = sc, y
        # settle at best position and wait for transitions
        pg.evaluate(f"window.scrollTo(0,{best_y})")
        pg.wait_for_timeout(1800)
        png = pg.screenshot(type='jpeg', quality=82)
        txt = pg.evaluate(f"(()=>{{const s=document.querySelectorAll('.scene')[{i}];return [...s.querySelectorAll('.mark')].map(m=>m.innerText.trim()).filter(Boolean).join(' / ')}})()")
        shots.append((base64.b64encode(png).decode(), txt))
        print(i, best_score, round(best_y), txt[:60].replace('\n', ' '))

    pg.evaluate("""(shots)=>{
      const sc=[...document.querySelectorAll('.scene')];
      sc.forEach((s,i)=>{
        const d=document.createElement('div');d.className='pscene';
        d.innerHTML='<img src="data:image/jpeg;base64,'+shots[i][0]+'"><div class="ptxt"></div>';
        d.querySelector('.ptxt').textContent=shots[i][1];
        s.replaceWith(d);
      });
      document.querySelectorAll('.acc-btn').forEach(b=>b.setAttribute('aria-expanded','true'));
      document.querySelectorAll('.step,.wv').forEach(e=>e.classList.add('on'));
      const st=document.createElement('style');st.textContent=`
        .back,.credit,.rail,.toc,nav,.ex-bg{display:none!important}
        .pscene{position:relative;width:100%;break-inside:avoid;break-after:page;line-height:0}
        .pscene img{width:100%;display:block}
        .pscene .ptxt{position:absolute;left:0;top:0;color:transparent;font-size:2px;line-height:1}
        .story{display:block!important}
        .story-vis{position:relative!important;top:0!important;height:auto!important;display:block!important;margin-bottom:24px}
        .story-vis .wv{position:relative!important;inset:auto!important;opacity:1!important;transform:none!important;margin:0 auto 18px;display:block!important}
        .story-vis .wv img{max-height:520px;width:auto;max-width:100%;display:block;margin:0 auto}
        .step{opacity:1!important;transform:none!important;min-height:0!important;padding:14px 0!important}
        .acc-body,.cmp-body{grid-template-rows:1fr!important;position:static!important}
        .fi,.reveal,[data-reveal]{opacity:1!important;transform:none!important}
        section{break-inside:auto}
        *{animation:none!important;transition:none!important}
      `;document.head.appendChild(st);
      document.querySelectorAll('.cmp-row').forEach(r=>r.classList.add('open'));
    }""", [list(s) for s in shots])
    pg.wait_for_timeout(800)
    pg.emulate_media(media='screen')
    pg.pdf(path=OUT, width=f'{W}px', height=f'{H}px', print_background=True, margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'})
    b.close()
print('saved', OUT)
