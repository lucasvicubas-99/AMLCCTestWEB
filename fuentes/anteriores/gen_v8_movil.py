"""Copias de las páginas v8 para ver en el lienzo a ancho de móvil (390 px)."""
import json, re
from playwright.sync_api import sync_playwright
P='/home/claude/web-aml/project/'
PAGS=[('Inicio','v8'),('Capacidades','v8-capacidades'),('Calidad','v8-calidad'),('Sectores','v8-sectores'),('Materiales','v8-materiales'),('Contacto','v8-contacto')]
H={}
with sync_playwright() as p:
    b=p.chromium.launch(); pa=b.new_page(viewport={'width':390,'height':844}, is_mobile=True)
    for n,url in PAGS:
        pa.goto(f'http://localhost:8765/{url}.html'); pa.wait_for_timeout(1200); H[n]=pa.evaluate('document.documentElement.scrollHeight')+40
    b.close()
c=json.load(open(P+'canvas.json'))
base=c['boards']['Capacidades-v8.dc.html']; y=base['y']+max(c['boards'][f'{n}-v8.dc.html']['h'] for n,_ in PAGS[1:])+400
x=c['boards']['Inicio-v8.dc.html']['x']
for n,_ in PAGS:
    t=open(P+f'{n}-v8.dc.html',encoding='utf-8').read()
    for m,_ in PAGS: t=t.replace(f'{m}-v8.dc.html',f'{m}-v8-movil.dc.html')
    t=re.sub(r'"\$preview":\{"width":\d+,"height":\d+\}',f'"$preview":{{"width":390,"height":{H[n]}}}',t,count=1)
    t=t.replace('<title>','<title>Móvil · ',1)
    open(P+f'{n}-v8-movil.dc.html','w',encoding='utf-8').write(t)
    c['boards'][f'{n}-v8-movil.dc.html']={'x':x,'y':y,'w':390,'h':H[n],'title':f'v8 · {n} · móvil','expand':'fill','is_interactive':True}
    x+=470
json.dump(c,open(P+'canvas.json','w'),ensure_ascii=False,indent=1)
print(H)
