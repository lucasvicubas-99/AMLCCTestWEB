"""Convierte las mesas .dc.html del diseño en el sitio estático del repositorio AMLCCTestWEB."""
import re, sys
P='/home/claude/web-aml/project/'
OUT=sys.argv[1] if len(sys.argv)>1 else '/home/claude/AMLCCTestWEB'
M={'26b761a79e1de3ed046de82e75375c91':'nave.webp','2b01d6b376e26653403f35cc5560a3d4':'portada.mp4','2409eea66314255b1920c51d63c3dd04':'portada-v2.mp4','2d1f70f1daf16b807f55be93c811dd32':'portada-poster.webp',
'33e2b4e1c7b603938d281bfd884ed387':'soldadura.webp','393f1ffdd689e9fa86c96ee1aec6b8af':'sector-ferroviario.webp','3d5131550f33cf0871c52171a4ed835d':'sector-petroleo.webp',
'40908ec8da767f9510ae250fe042fd5f':'sector-naval.webp','446431df4fc614826b6882cdc400c008':'calidad-cuerpos.webp','46df578761517afff779d32923caaf40':'mandrinado.webp',
'504e694caa396737df4740377de4a23e':'fresado.webp','53d77afd689a06c63870c34c85920fc5':'control-dimensional.webp','597616a036eb7bc7b983449e654d5b10':'valvula.jpg',
'639bb75abbd449f7e28a2d62569149c0':'torneado.webp','63aac01922710c39a2e7be6303632d3a':'esferas.webp','7f788c0badd0760fd48912e94f453d1d':'stand.webp',
'aa1844d273d07d0df9434083e970546a':'ondas-cuarto.svg','b3328804d8c220af4e73c389b91db6f2':'sector-estructural.webp','94b603af55890ffd1f5aaedd52042adc':'sector-sanitario.webp','ad49bf58dcc6353447a48badae9a81a5':'fresado-carcasa-43.webp','0b199555e961d8fb690f60d4ccf1b0f2':'sector-sanitario-filtro-43.webp','d65d5cc5289447730fdd58ef599aca4c':'petroleo-carcasa-centrada-43.webp','0407f2a2ce7557500c6a4b49ea71aacb':'ferroviario-mecanizado-43.webp','dab1ed35b8b3e669807859fda54ecaf0':'petroleo-carcasa-partida-43.webp','d8aa2dd2239315a997be1df7d344b86b':'nuclear-voluta-entera-v3.webp','6ac429a70670a8bd9779adb032b24bda':'naval-rodete-43.webp','1ad00e791a34e705e4cfdb635cdcbc46':'sector-petroleo-valvula.webp','bef63af4d8affc677728347bbd8ce6d1':'sector-naval-propulsion.webp','adf15f215d0ddf830ceff1fb843f069d':'sector-nuclear-voluta.webp','f93368d377d333d21f18780a7ba287dd':'sector-ferroviario-axlebox.webp','242556ff58e4c1a3d42edee320c67914':'sector-industrial-impeller.webp','d769c662c1de2be375a7ff7301bd9d1e':'metrologia-cmm.webp','b9144035a3fb7307c9d845da076b2fbf':'planta-multistage-casing.webp','029d5f194fb533530434a70e12986662':'planta-casing-mecanizado.webp','19bdd675133aa9f07033a646f6389fe4':'planta-impeller.webp','9cb41a0981fb29eb0dc37656fd331165':'car-in-compressor-case.webp','624f0d549e58cc056be9b97322839a50':'car-in-impeller-bowl.webp','0b0076e60e3821c0bec24600fd4a72f0':'car-in-multistage-casing.webp','19f098cf86edd222d162d3dd7212d600':'car-in-suction-case.webp','c916b0a68f7effdc6fb0a1632c3deb22':'car-in-volute.webp','5acb77b89d9abb6d137c2c501fc725ff':'car-nu-multistage-casing.webp','f30b4b5940fd49bf18f0e9e231ce7da1':'car-pg-flowmeter.webp','cbbdb4bea3ffe26e764c02ab6f8fc03d':'car-pg-valve-body-2.webp','5bbbb579f870d134f8095c0c258909ef':'car-pg-valve-sphere-cmm.webp','6613d77b7526aedce93d3f7fbe7578c9':'car-pg-valve-spheres-2.webp','962c3021e9dfc63e1b267e2dbd86cb2d':'car-pg-valve-spheres.webp','33c33c750dbdfdb983ee872208e67539':'esfera-trevisan-invertida.webp','bc075f2c7e21d857269451011cff03c2':'ondas-semicirculo.svg',
'c93e85418899e45068af2033a2e4c83a':'ondas-lineal-cuarto.svg','defb66a730bcba562a1f247a64244154':'esfera-trevisan.webp','e280934bf4a0700b14669aaccd114880':'sector-nuclear.webp'}
PAGES={'Inicio-v6.dc.html':'index.html','Capacidades.dc.html':'capacidades.html','Ensayos.dc.html':'calidad.html',
       'Sectores.dc.html':'sectores.html','Materiales.dc.html':'materiales.html','Contacto.dc.html':'contacto.html','Inicio-v8.dc.html':'v8.html',
       'Capacidades-v8.dc.html':'v8-capacidades.html','Calidad-v8.dc.html':'v8-calidad.html','Sectores-v8.dc.html':'v8-sectores.html',
       'Materiales-v8.dc.html':'v8-materiales.html','Contacto-v8.dc.html':'v8-contacto.html'}
HEAD=('<meta name="viewport" content="width=device-width, initial-scale=1">\n<link rel="icon" href="./favicon.ico?v=3" sizes="any">\n<link rel="icon" href="./assets/iconos/favicon.svg?v=3" type="image/svg+xml">\n'
      '<link rel="apple-touch-icon" href="./assets/iconos/apple-touch-icon.png?v=3">\n<link rel="manifest" href="./site.webmanifest">\n'
      '<meta name="theme-color" content="#011F67">\n<script src="./assets/transicion.js"></script>\n'
      '<script src="./vendor/react.js"></script>\n<script src="./vendor/react-dom.js"></script>\n<script src="./vendor/support.js"></script>')
NOMBRES={'#011F67':'navy','#FFFFFF':'white','#EDF1F6':'band','#EEF1F0':'grey','#B3C3C0':'sage','#5A6A92':'label',
 '#3A4A75':'text-2','#1E2D55':'text','#DCE2EA':'line','#C9D2E0':'line-2','#C9D2D0':'line-3','#3D5AA8':'link-hover','#000':'black'}
def tokenizar(s, stamp):
    tokens={}
    def nombre(lit):
        k=lit.upper() if lit.startswith('#') else lit
        if k in NOMBRES: n=NOMBRES[k]
        else: n=re.sub(r'[^a-z0-9]+','-',lit.lower()).strip('-')
        tokens.setdefault('--color-'+n,lit); return 'var(--color-'+n+')'
    COL=re.compile(r'#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b|rgba?\([^)]*\)')
    def fuentes(t):
        t=t.replace("font-family: 'Space Grotesk', sans-serif","font-family: var(--font-display)")
        return t.replace("font-family: 'IBM Plex Sans', system-ui, sans-serif","font-family: var(--font-body)")
    s=re.sub(r'style="([^"]*)"',lambda m:'style="'+COL.sub(lambda c:nombre(c.group(0)),fuentes(m.group(1)))+'"',s)
    a=s.index('<style>')+7; b=s.index('</style>',a)
    css=COL.sub(lambda c:nombre(c.group(0)),s[a:b])
    raiz=('\n'+stamp+'\n:root{\n--font-display:\'Space Grotesk\', sans-serif;\n--font-body:\'IBM Plex Sans\', system-ui, sans-serif;\n'
          +''.join(f'{k}:{v};\n' for k,v in tokens.items())+'}\n')
    return s[:a]+raiz+css+s[b:]
STAMP=('/* Hallmark · checked: 2026-11-19 · genre: modern-minimal (inferred)\n'
       ' * floor: 0 FAIL · fixed: 9 (7b, 15, 19, 24b, 26a, 26b, 34, 39b, 48, 49b, 54, 67, 69) · structural: 3 printed (42, 58, 59)\n'
       ' * built: the project · redesign: polish · v2.0.0 */\n'
       '/* Hallmark · waive 80 · the user\'s logo · the circles are the AML logo waves, the company brand mark, set behind the Capacidades heading */\n'
       '/* Hallmark · reworded "Mecanizado de alta precisión, ensayos y control de calidad bajo un mismo techo." to "Quiénes somos" · 54 and 69 name it: the eyebrow folds into its heading and the line echoed the hero */\n'
       '/* Hallmark · reworded "Del bruto a la expedición." to "Cómo trabajamos" · 54 names it: figurative head, the plain label becomes the heading and the line moves into the lede */\n'
       '/* Hallmark · reworded "Mecanizado, inspección y ensayos en planta propia." to "Capacidades" · 54 names it: the line moves into the lede under the heading */\n'
       '/* Hallmark · dismissed render · the audit sandbox cannot reach fonts.googleapis.com; the published site loads Space Grotesk and IBM Plex Sans */')
for src,dst in PAGES.items():
    s=open(P+src,encoding='utf-8').read()
    assert s.count('<script src="./support.js"></script>')==1
    s=s.replace('<script src="./support.js"></script>',HEAD)
    for a,b in PAGES.items(): s=s.replace(f'href="{a}',f'href="{b}')
    s=re.sub(r'/_blob/([a-f0-9]{32})',lambda m:'./assets/'+M[m.group(1)],s)
    s=s.replace('<title>AML Centrifugal Casting · Inicio v6</title>','<title>AML Centrifugal Casting · Mecanizado de alta precisión, ensayos y control de calidad</title>')
    assert '_blob' not in s and '.dc.html' not in s, src
    if not dst.startswith('v8'): s=tokenizar(s, STAMP if dst=='index.html' else '/* Tokens de color y tipografía generados al exportar */')
    open(f'{OUT}/{dst}','w',encoding='utf-8').write(s)
print('ok')
