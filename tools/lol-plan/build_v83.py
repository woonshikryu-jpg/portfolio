# v82 -> v83: 3-1 비교표 줄도 마우스를 올리면 설계가 펼쳐지게(다른 펼침과 같게). 누르면 고정
import os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = open('versions/lol-plan-v82.html', encoding='utf-8').read()
s = s.replace('v82</title>', 'v83</title>')
k = s.rfind('</style>')
s = s[:k] + '.cmp-row.peek>button+.cmp-body{grid-template-rows:1fr}.cmp-row.peek>button[aria-expanded="false"] .pl{background:#F3E1B2}\n' + s[k:]
k = s.rfind('</body>')
s = s[:k] + '''<script>(function(){if(!matchMedia('(hover:hover)').matches)return;document.querySelectorAll('.cmp-row').forEach(function(r){var t;r.addEventListener('mouseenter',function(){clearTimeout(t);t=setTimeout(function(){r.classList.add('peek')},140)});r.addEventListener('mouseleave',function(){clearTimeout(t);t=setTimeout(function(){r.classList.remove('peek')},160)});var b=r.querySelector('button');if(b)b.addEventListener('click',function(){r.classList.remove('peek')})})})();</script>
''' + s[k:]
s = s.replace('lol-plan-v82', 'lol-plan-v83')
open('versions/lol-plan-v83.html', 'w', encoding='utf-8').write(s)
print('ok')
