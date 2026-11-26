"""Genera las subpáginas de la versión 8 con el mismo sistema que Inicio-v8 (tokens, cabecera, pie)."""
import re
import gen_v8 as g

P = g.P

CSS_SUB = r'''
/* Subpáginas: portada corta, secciones, tablas, cifras, mapa */
.slab__nav a[aria-current="page"] { text-decoration: underline; text-underline-offset: 0.3em; }
.banner { position: relative; isolation: isolate; min-height: clamp(380px, 52svh, 520px); display: flex; align-items: flex-end; background: var(--color-ink); color: var(--color-paper); overflow: clip; }
.banner__bg { position: absolute; inset: 0; z-index: -2; width: 100%; height: 100%; object-fit: cover; }
.banner::after { content: ""; position: absolute; inset: 0; z-index: -1; background: linear-gradient(to top, var(--color-veil) 0%, color-mix(in oklch, var(--color-ink) 72%, transparent) 100%); }
.banner--derecha .banner__bg { left: auto; right: 0; width: 72%; -webkit-mask-image: linear-gradient(to right, transparent 0, var(--color-ink) 30%); mask-image: linear-gradient(to right, transparent 0, var(--color-ink) 30%); }
.banner--derecha::after { background: linear-gradient(to bottom, color-mix(in oklch, var(--color-ink) 85%, transparent) 0%, transparent 22%), linear-gradient(to right, var(--color-ink) 0%, color-mix(in oklch, var(--color-ink) 88%, transparent) 38%, color-mix(in oklch, var(--color-ink) 62%, transparent) 70%, color-mix(in oklch, var(--color-ink) 55%, transparent) 100%); }
.banner__inner { width: 100%; padding-block: var(--space-3xl) var(--space-2xl); display: grid; gap: var(--space-md); animation: settle 0.6s var(--ease-out) both; }
.banner h1 { color: var(--color-paper); max-width: 18ch; }
.banner .lead { color: var(--color-on-ink-2); max-width: 56ch; }
.crumbs { display: flex; gap: var(--space-xs); font-size: var(--text-sm); color: var(--color-on-ink-2); }
.crumbs a { color: var(--color-paper); }
.sec { padding-block: var(--section-gap-s); }
.sec + .sec { border-top: 1px solid var(--color-rule); }
.sec--tint { background: var(--color-paper-2); }
.sec--tint + .sec, .sec + .sec--tint { border-top: 0; }
.head { display: grid; grid-template-columns: minmax(0, 1fr); gap: var(--space-md); align-content: start; min-width: 0; }
.op { row-gap: var(--space-xl); }
.op .photo { aspect-ratio: 16 / 9; }
.op__body { grid-column: 1 / -1; display: grid; gap: var(--space-lg); min-width: 0; }
.c-1-7 { grid-column: 1 / 8; } .c-8-12 { grid-column: 8 / -1; }
.head .meta { font-size: var(--text-sm); color: var(--color-muted); }
.head p:not(.meta) { color: var(--color-ink-2); }
.photo { width: 100%; aspect-ratio: 4 / 3; object-fit: cover; border-radius: var(--radius-card); }
.note { font-size: var(--text-sm); color: var(--color-muted); }
.figs { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); border-top: 1px solid var(--color-ink); }
.fig { display: grid; gap: var(--space-2xs); align-content: start; padding: var(--space-lg) var(--space-lg) 0; border-left: 1px solid var(--color-rule); min-width: 0; }
.fig:first-child { padding-left: 0; border-left: 0; }
.fig__val { font-family: var(--font-display); font-size: var(--text-xl); line-height: 1.15; font-variant-numeric: tabular-nums; }
.fig__lbl { font-size: var(--text-sm); color: var(--color-ink-2); }
.fig__src { font-size: var(--text-sm); color: var(--color-muted); }
.table-wrap { min-width: 0; overflow-x: auto; }
.table--data { min-width: 640px; }
.table--data th[scope="row"] { font-weight: 500; color: var(--color-ink); font-size: var(--text-md); border-bottom: 1px solid var(--color-rule); vertical-align: top; }
.table--data thead th:last-child { text-align: left; }
.table--data td, .table--data th[scope="row"] { padding: var(--space-md) var(--space-md) var(--space-md) 0; text-align: left !important; }
.table--data td:last-child { padding-right: 0; }
.table--data .sub { display: block; font-size: var(--text-sm); color: var(--color-muted); }
.table--data tr.grupo th { text-align: left; padding: var(--space-lg) 0 var(--space-xs); font-family: var(--font-display); font-size: var(--text-lg); font-weight: 500; color: var(--color-ink); border-bottom: 1px solid var(--color-ink); }
.spec { margin: 0; border-top: 1px solid var(--color-rule); }
.spec div { display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); gap: var(--space-2xs) var(--gap-columns); padding-block: var(--space-md); border-bottom: 1px solid var(--color-rule); }
.spec dt { font-weight: 500; }
.spec dd { margin: 0; color: var(--color-ink-2); }
.fill { padding: 0 0.25em; border: 1px dashed var(--color-muted); border-radius: 3px; color: var(--color-muted); -webkit-box-decoration-break: clone; box-decoration-break: clone; }
.bar { display: inline-block; width: 96px; height: 6px; border-radius: 3px; background: var(--color-rule); vertical-align: middle; overflow: hidden; }
.bar > span { display: block; height: 100%; background: var(--color-ink); }
.cta { display: grid; grid-template-columns: minmax(0, 7fr) minmax(0, 5fr); gap: var(--space-lg) var(--gap-columns); align-items: end; }
.cta .actions { justify-content: flex-end; }
.anchors { display: flex; flex-wrap: wrap; gap: var(--space-xs); list-style: none; margin: 0; padding: 0; }
.anchors a { display: inline-flex; align-items: center; min-height: 44px; padding: 0 var(--space-md); border: 1px solid var(--color-muted); border-radius: var(--radius-card); text-decoration: none; font-size: var(--text-sm); }
.anchors a:hover { border-color: var(--color-ink); background: var(--color-paper-2); }
.sectors { list-style: none; margin: 0; padding: 0; display: grid; gap: var(--space-lg); }
.sector { position: relative; isolation: isolate; overflow: hidden; border-radius: var(--radius-card); background: var(--color-ink); min-height: clamp(460px, 40vw, 600px); display: grid; scroll-margin-top: calc(var(--nav-h) + var(--space-md)); }
.sector .carrusel__pista { position: absolute; top: 0; bottom: 0; right: 0; left: 30%; z-index: -2; }
.carrusel__pista { display: grid; grid-auto-flow: column; grid-auto-columns: 100%; overflow-x: auto; scroll-snap-type: x mandatory; overscroll-behavior-x: contain; scrollbar-width: none; }
.carrusel__pista::-webkit-scrollbar { display: none; }
.carrusel__pista:focus-visible { outline: 2px solid var(--color-focus); outline-offset: -4px; }
.carrusel__foto { position: relative; margin: 0; scroll-snap-align: start; min-width: 0; height: 100%; }
.carrusel__foto img { width: 100%; height: 100%; object-fit: cover; object-position: 50% 50%; display: block; }
.carrusel__foto figcaption { position: absolute; top: var(--space-md); right: var(--space-md); padding: var(--space-3xs) var(--space-xs); border-radius: var(--radius-card); background: color-mix(in oklch, var(--color-ink) 72%, transparent); color: var(--color-paper); font-size: var(--text-sm); }
.sector__velo { position: absolute; inset: 0; z-index: -1; pointer-events: none; background: linear-gradient(to right, var(--color-ink) 0%, var(--color-ink) 30%, color-mix(in oklch, var(--color-ink) 70%, transparent) 40%, color-mix(in oklch, var(--color-ink) 15%, transparent) 55%, transparent 65%); }
.sector__txt { align-self: end; display: grid; gap: var(--space-sm); max-width: 32rem; padding: var(--space-2xl) var(--space-xl); color: var(--color-paper); pointer-events: none; }
.sector__txt h2 { font-size: var(--text-section); color: var(--color-paper); }
.sector__txt p { color: var(--color-on-ink-2); }
.piezas { display: grid; gap: var(--space-3xs); padding-top: var(--space-sm); border-top: 1px solid var(--color-on-ink-rule); }
.sector__txt .piezas span:last-child { color: var(--color-paper); }
.piezas__lbl { font-size: var(--text-sm); color: var(--color-sage); }
.carrusel__ctrl { position: absolute; right: var(--space-md); bottom: var(--space-md); display: flex; align-items: center; gap: var(--space-xs); }
.carrusel__n { margin-right: var(--space-2xs); font-size: var(--text-sm); color: var(--color-paper); font-variant-numeric: tabular-nums; text-shadow: 0 1px 2px color-mix(in oklch, var(--color-ink) 60%, transparent); }
.carrusel__btn { display: inline-flex; align-items: center; justify-content: center; width: 48px; height: 48px; padding: 0; border: 0; border-radius: 50%; background: color-mix(in oklch, var(--color-paper) 88%, transparent); color: var(--color-ink); cursor: pointer; transition: background-color 0.15s var(--ease-out), transform 0.15s var(--ease-out); }
.carrusel__btn:hover { background: var(--color-paper); transform: scale(1.06); }
.carrusel__btn:focus-visible { outline: 2px solid var(--color-paper); outline-offset: 2px; }
.carrusel__btn:active { transform: scale(0.96); }
.checklist { margin: 0; padding: 0; list-style: none; border-top: 1px solid var(--color-rule); }
.checklist li { display: grid; grid-template-columns: minmax(0, 2fr) minmax(0, 5fr); gap: var(--space-2xs) var(--space-lg); padding-block: var(--space-sm); border-bottom: 1px solid var(--color-rule); }
.checklist strong { font-weight: 500; }
.checklist span { color: var(--color-ink-2); }
.ondas { position: absolute; left: 0; bottom: 0; z-index: -1; width: 260px; height: auto; opacity: 0.18; pointer-events: none; }
.rel { position: relative; isolation: isolate; overflow: clip; }
.where { display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); gap: 0; border: 1px solid var(--color-ink); border-radius: var(--radius-card); overflow: hidden; }
.transport { background: var(--color-ink); color: var(--color-paper); padding: var(--space-xl); display: grid; gap: var(--space-md); align-content: center; }
.transport address { font-style: normal; font-size: var(--text-lg); line-height: 1.45; }
.transport .spec { border-top-color: var(--color-on-ink-rule); }
.transport .spec div { border-bottom-color: var(--color-on-ink-rule); }
.transport .spec dt { color: var(--color-sage); }
.transport .spec dd { color: var(--color-paper); }
.map { position: relative; min-height: 440px; background: var(--color-paper-2); }
.map iframe { position: absolute; inset: 0; width: 100%; height: 100%; border: 0; }
.fairs2 { align-items: start; }
.fairs2__photo { grid-row: 1; grid-column: 1 / 6; }
.fairs2__photo img { aspect-ratio: 1 / 1; }
.fairs2__body { grid-row: 1; grid-column: 7 / -1; display: grid; gap: var(--space-xl); align-content: start; min-width: 0; }
.field input[type="file"] { padding: var(--space-sm); }
@media (max-width: 60rem) {
  .op > div[style] { grid-row: auto !important; }
  .banner--derecha .banner__bg { width: 100%; -webkit-mask-image: none; mask-image: none; }
  .banner--derecha::after { background: linear-gradient(to top, var(--color-veil) 0%, color-mix(in oklch, var(--color-ink) 72%, transparent) 100%); }
  .op .c-8-12 { order: -1; }
  .fairs2__photo, .fairs2__body { grid-row: auto; grid-column: 1 / -1; }
  .fairs2__photo img { aspect-ratio: 4 / 3; }
  .map { min-height: 320px; }
  .c-1-7, .c-8-12 { grid-column: 1 / -1; }
  .figs { grid-template-columns: minmax(0, 1fr); }
  .fig { padding: var(--space-md) 0; border-left: 0; border-bottom: 1px solid var(--color-rule); }
  .cta { grid-template-columns: minmax(0, 1fr); }
  .cta .actions { justify-content: flex-start; }
  .sector { min-height: 0; background: var(--color-paper); }
  .sector .carrusel__pista { position: relative; inset: auto; left: auto; z-index: auto; aspect-ratio: 4 / 3; border-radius: var(--radius-card); }
  .carrusel__foto img { object-position: 50% 50%; }
  .sector__velo { display: none; }
  .sector__txt { order: 2; padding: var(--space-md) 0 0; max-width: none; color: var(--color-ink); pointer-events: auto; }
  .sector__txt h2 { color: var(--color-ink); }
  .sector__txt p { color: var(--color-ink-2); }
  .sector__txt .piezas span:last-child { color: var(--color-ink); }
  .piezas { border-top-color: var(--color-rule); }
  .piezas__lbl { color: var(--color-muted); }
  .carrusel__ctrl { top: auto; bottom: auto; }
  .sector { display: flex; flex-direction: column; overflow: visible; }
  .sector .carrusel__ctrl { position: absolute; right: var(--space-sm); top: calc((100vw - 2 * var(--gutter)) * 0.75 - 60px); }
  .where { grid-template-columns: minmax(0, 1fr); }
  .spec div, .checklist li { grid-template-columns: minmax(0, 1fr); }
  .ondas { display: none; }
}
@media (max-width: 40rem) {
  .table-wrap { overflow: visible; }
  .table--data { min-width: 0; }
  .table--data tr { gap: var(--space-xs); padding-block: var(--space-lg); }
  .table--data th[scope="row"] { padding: 0 0 var(--space-2xs); border: 0; font-size: var(--text-lg); }
  .table--data td { display: grid; grid-template-columns: 8.5rem minmax(0, 1fr); gap: 0 var(--space-md); padding: 0; border: 0; }
  .table--data td::before { content: attr(data-label); color: var(--color-muted); font-size: var(--text-sm); padding-top: var(--space-3xs); }
  .table--data td .sub { grid-column: 2; }
  .table--data tr.grupo { padding-block: var(--space-xl) 0; border-bottom: 0; }
  .table--data tr.grupo th { padding: 0 0 var(--space-xs); }
  .figs { border-top-width: 1px; }
  .fig__val { font-size: var(--text-lg); }
  .banner { min-height: 340px; }
  .banner__inner { padding-block: var(--space-2xl) var(--space-xl); }
  .sec { padding-block: var(--space-3xl); }
  .sector__txt h2 { font-size: var(--text-2xl); }
  .transport { padding: var(--space-lg); }
  .transport address { font-size: var(--text-md); }
  .anchors { gap: var(--space-2xs); }
  .anchors a { padding: 0 var(--space-sm); }
}
'''

SCRIPT = '''<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":%%ALTO%%}}'>
class Component extends DCLogic {
constructor(props) {
super(props);
this.state = { menu: false, aviso: '' };
}
moverCarrusel(ev, d) {
const c = ev.currentTarget && ev.currentTarget.closest('.carrusel');
const p = c && c.querySelector('.carrusel__pista');
if (!p) return;
const w = p.clientWidth;
let x = p.scrollLeft + d * w;
if (x > p.scrollWidth - w + 2) x = 0;
if (x < -2) x = p.scrollWidth - w;
const quieto = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
p.scrollTo({ left: x, behavior: quieto ? 'auto' : 'smooth' });
}
renderVals() {
return {
menuAbierto: this.state.menu ? 'true' : 'false',
navClase: this.state.menu ? 'slab__nav is-open' : 'slab__nav',
toggleMenu: () => this.setState({ menu: !this.state.menu }),
cerrarMenu: (ev) => { if (ev && ev.target && ev.target.tagName === 'A') this.setState({ menu: false }); },
avisoForm: this.state.aviso,
carruselAnt: (ev) => this.moverCarrusel(ev, -1),
carruselContar: (ev) => { const p = ev.currentTarget; const c = p.closest('.carrusel'); const n = c && c.querySelector('.carrusel__n'); if (!n) return; const tot = p.children.length; const k = Math.round(p.scrollLeft / Math.max(1, p.clientWidth)) + 1; n.textContent = Math.min(tot, Math.max(1, k)) + ' / ' + tot; },
carruselSig: (ev) => this.moverCarrusel(ev, 1),
enviar: (ev) => {
ev.preventDefault();
const f = ev.currentTarget || ev.target;
const malo = f.querySelector(':invalid');
f.querySelectorAll('[aria-invalid]').forEach((x) => x.removeAttribute('aria-invalid'));
if (malo) { malo.setAttribute('aria-invalid', 'true'); malo.focus(); this.setState({ aviso: 'Falta un dato obligatorio: nombre, un email válido y la casilla de privacidad.' }); return; }
this.setState({ aviso: 'No se ha enviado nada: este formulario todavía no está conectado.' });
}
};
}
}
</script>'''


def stamp(shape, signature, extra=''):
    return ('/* Hallmark · shape: ' + shape + ' · genre: modern-minimal · theme: brand (locked from Inicio v8) · redesign: full\n'
            ' * paper: oklch(100% 0 0) · accent: oklch(27.8% 0.131 263) · display: Space Grotesk · body: IBM Plex Sans · hero: Banner · nav: slab · footer: statement · signature: ' + signature + '\n'
            ' * axes: light/grotesk-sans/cool · posture: committed (navy nav, banner, footer) · contrast: pass · fold: pass · v2.0.0 */\n'
            '/* Hallmark · pre-emit critique: P4 H4 E4 S4 R5 V3 · weakest: V, the subpages share the Inicio v8 system by design and differ only in shape */\n'
            '/* Hallmark · dismissed 77 · a subpage is one deep topic under the Inicio v8 page, not a landing page, so it runs four or five sections */\n'
            '/* Hallmark · dismissed render · the sandbox cannot reach fonts.googleapis.com; the published page loads Space Grotesk and IBM Plex Sans */\n' + extra)


def css_comun():
    c = g.CSS
    c = c[c.index(':root {'):]  # sin el sello de la portada
    return c


def banner(bg, pos, actual_txt, h1, lead, extra=''):
    return (f'<main id="contenido">\n<section class="banner on-ink{extra}" aria-labelledby="titulo">\n'
            f'<img class="banner__bg" src="/_blob/{bg}" alt="" aria-hidden="true" style="object-position: {pos}">\n'
            f'<div class="container banner__inner">\n'
            f'<nav aria-label="Ruta" class="crumbs"><a href="Inicio-v8.dc.html">Inicio</a><span aria-hidden="true">/</span><span aria-current="page">{actual_txt}</span></nav>\n'
            f'<h1 id="titulo">{h1}</h1>\n<p class="lead">{lead}</p>\n</div>\n</section>\n')


def cta(h2, p, href='Contacto-v8.dc.html', txt='Solicitar información'):
    return (f'<section class="sec sec--tint" aria-label="{h2}">\n<div class="container cta">\n'
            f'<div class="head"><h2>{h2}</h2><p>{p}</p></div>\n'
            f'<div class="actions"><a href="{href}" class="btn btn--ink">{txt}</a></div>\n</div>\n</section>\n')


def figs(lista):
    return '<div class="figs">' + ''.join(
        f'<div class="fig"><span class="fig__val">{v}</span><span class="fig__lbl">{l}</span>' + (f'<span class="fig__src">{s}</span>' if s else '') + '</div>'
        for v, l, s in lista) + '</div>'


def tabla_maquinas(caption, filas):
    cab = '<thead><tr><th scope="col">Máquina</th><th scope="col">Tipo</th><th scope="col">Dimensiones máx. de pieza</th><th scope="col">Peso máx.</th><th scope="col">Tolerancia habitual</th></tr></thead>'
    cuerpo = ''.join(f'<tr><th scope="row">{m}</th><td data-label="Tipo">{t}</td><td data-label="Dimensiones máx.">{d}<span class="sub">{ds}</span></td><td data-label="Peso máx.">{p}' + (f'<span class="sub">{ps}</span>' if ps else '') + f'</td><td class="num" data-label="Tolerancia">{tol}</td></tr>'
                     for m, t, d, ds, p, ps, tol in filas)
    return (f'<div class="table-wrap" role="region" aria-label="{caption}" tabindex="0"><table class="table table--data"><caption class="visually-hidden">{caption}</caption>'
            + cab + '<tbody>' + cuerpo + '</tbody></table></div>')


def spec(pares):
    return '<dl class="spec">' + ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in pares) + '</dl>'


def documento(titulo, nombre, css_extra, cuerpo, alto):
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="description" content="AML Centrifugal Casting: {titulo.lower()}. Mecanizado de alta precisión, ensayos y control de calidad de piezas de acero fundido.">
<title>{titulo} · AML Centrifugal Casting · v8</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&amp;family=Space+Grotesk:wght@500&amp;display=swap">
<style>
{css_extra}{css_comun()}{CSS_SUB}</style>
</helmet>
<div class="pagina">
{cuerpo}</div>
</x-dc>
{SCRIPT.replace('%%ALTO%%', str(alto))}
</body>
</html>
'''


def escribir(nombre, doc):
    open(P + nombre, 'w', encoding='utf-8').write(doc)
    print(nombre, len(doc))


# =================== Capacidades ===================
fres = [('Trevisan II DS-600 RAM', 'Centro de mecanizado', 'Ø 2.000 × 1.500 mm', 'Ø 900 mm en torneado', '2.600 kg', '4.500 kg opcional', '± 0,010 mm'),
        ('Trevisan I DS-600', 'Centro de mecanizado', 'Ø 2.000 × 1.100 mm', 'Ø 900 mm en torneado', '2.600 kg', '', '± 0,010 mm'),
        ('Johnford SV-48H', 'Centro de mecanizado vertical', '1.300 × 700 × 630 mm', 'Mesa y recorrido Z', '1.500 kg', '', '± 0,015 mm'),
        ('Deckel Maho DMC 80 U duoBLOCK', 'Centro de mecanizado 5 ejes', 'Ø 900 × 1.450 mm', 'Mesa Ø 800 × 630 mm', '1.200 a 1.400 kg', '', '± 0,005 mm')]
torn = [('Heller TS 1600 × 1500', 'Torno esférico de gran volteo', 'Ø 1.600 × 1.500 mm', 'Ø 900 mm esférico exterior', '2.500 kg', '', '± 0,015 mm'),
        ('Doosan Puma 700', 'Torno CNC horizontal pesado', 'Ø 900 × 1.600 mm', 'Hasta 3.200 mm en versión L', '2.500 a 3.000 kg', '', '± 0,008 mm'),
        ('Takisawa LS-1000 M', 'Torno CNC con herramienta motorizada', 'Ø 850 × 1.966 mm', 'Hasta 2.966 mm en L30', '2.000 a 2.500 kg', '', '± 0,008 mm'),
        ('Sprint D600 (Spinner TC 600)', 'Torno CNC horizontal', 'Ø 310 a 400 × 650 mm', 'Volteo Ø 600 mm', '400 a 600 kg', '', '± 0,005 mm')]
NOTA_RANGO = ''

def op(id_, h2, meta, desc, img, alt, pos, cuerpo, espejo=False):
    cab = f'<div class="head"><h2>{h2}</h2><p class="meta">{meta}</p><p>{desc}</p></div>'
    foto = f'<img loading="lazy" class="photo" src="/_blob/{img}" alt="{alt}" width="800" height="600" style="object-position: {pos}">'
    if espejo:
        arriba = f'<div class="c-1-7" style="grid-row: 1">{foto}</div>\n<div class="c-8-12" style="grid-row: 1">{cab}</div>\n'
    else:
        arriba = f'<div class="c-1-5" style="grid-row: 1">{cab}</div>\n<div class="c-6-12" style="grid-row: 1">{foto}</div>\n'
    return (f'<section id="{id_}" class="sec">\n<div class="container grid op">\n{arriba}'
            f'<div class="body op__body">{cuerpo}</div>\n</div>\n</section>\n')

cap = (g.cabecera('CAP', False)
       + banner('26b761a79e1de3ed046de82e75375c91', '30% 55%', 'Capacidades', 'Parque de máquinas y capacidades',
                'Fresamos, torneamos, mandrinamos y soldamos en nuestra propia planta. Aquí tiene las dimensiones y los pesos máximos de cada operación y de cada máquina.')
       + op('fresado', 'Fresado', '4 máquinas', 'Mecanizamos caras, ranuras, taladros y geometrías complejas en centros de mecanizado, también en 5 ejes.',
            'ad49bf58dcc6353447a48badae9a81a5', 'Husillo del centro de mecanizado trabajando una carcasa de bomba de acero fundido amarrada en escuadra', 'center 50%',
            figs([('Ø 2.000 × 1.500 mm', 'Dimensión máx.', 'Trevisan II'), ('4.500 kg', 'Peso máx. de pieza', 'Con carga reforzada'), ('± 0,005 mm', 'Tolerancia', 'Desde, en 5 ejes')])
            + tabla_maquinas('Máquinas de fresado', fres) + NOTA_RANGO)
       + op('torneado', 'Torneado', '4 máquinas', 'Torneamos piezas de revolución: exteriores e interiores, refrentado, roscado y torneado esférico de gran volteo.',
            '639bb75abbd449f7e28a2d62569149c0', 'Torneado en el taller de AML', 'center 55%',
            figs([('Ø 1.600 mm', 'Volteo máx.', 'Heller TS 1600'), ('1.966 mm', 'Longitud máx.', 'Takisawa LS-1000 M'), ('3.000 kg', 'Peso máx. de pieza', 'Doosan Puma 700')])
            + tabla_maquinas('Máquinas de torneado', torn) + NOTA_RANGO, espejo=True)
       + op('mandrinado', 'Mandrinado', '1 máquina', 'Mecanizamos alojamientos y diámetros interiores de precisión en piezas de gran tamaño.',
            '46df578761517afff779d32923caaf40', 'Mandrinadora CNC con una pieza de acero fundido amarrada', 'center 50%',
            figs([('12.000 kg', 'Peso máx. de pieza', ''), ('2.500 × 1.800 mm', 'Mesa giratoria', ''), ('360°', 'Giro de mesa', '')])
            + '<div class="head"><h3>TOS Varnsdorf WHN 13 CNC</h3><p>Mandrinadora horizontal de columna móvil</p></div>'
            + spec([('Eje X, longitudinal', '3.500 a 4.200 mm'), ('Eje Y, vertical del cabezal', '2.000 a 2.500 mm'), ('Eje Z, carnero', '800 a 1.250 mm'),
                    ('Eje W, husillo de mandrinar', '800 mm'), ('Dimensiones de mesa', '1.800 × 1.800 a 2.500 × 1.800 mm'), ('Peso máximo sobre mesa', '12.000 kg'),
                    ('Giro de mesa', '360°, indexado o continuo')]))
       + op('soldadura', 'Soldadura', 'Certificada', 'Soldamos piezas de acero fundido con soldadores y procedimientos certificados.',
            '33e2b4e1c7b603938d281bfd884ed387', 'Soldadura de una pieza de acero en el taller', '30% 45%',
            '<div class="head"><h3>Datos de soldadura</h3><p>Le enviamos los certificados si los necesita</p></div>'
            + spec([('Proceso', 'Soldeo por arco con electrodo revestido (111)'), ('Materiales', 'Aceros al carbono, inoxidables, dúplex y superdúplex'),
                    ('Certificación de soldadores', 'UNE-EN ISO 9606-1:2017, certificada por TÜV SÜD ATISAE (organismo notificado n.º 0053)'),
                    ('Rango de cualificación', 'Chapa y tubo, soldadura a tope'),
                    ('Procedimientos de soldeo (WPS)', 'Según el código RCC-M, para componentes de instalaciones nucleares')]))
       + cta('¿Tiene un plano o una especificación?', 'Envíenoslo y le diremos si podemos hacerlo y en qué plazo.')
       + '</main>\n' + g.pie_html(False))
escribir('Capacidades-v8.dc.html', documento('Capacidades', 'Capacidades-v8', stamp('Feature Stack', 'the machine table under each photograph, the real capacities set as figures'), cap, 5200))

# =================== Calidad ===================
cal = (g.cabecera('CAL', False)
       + banner('446431df4fc614826b6882cdc400c008', '50% 45%', 'Calidad', 'Calidad',
                'Ninguna pieza sale de nuestra planta sin medir ni ensayar. Lo hacemos con un sistema de calidad certificado.')
       + '''<section class="sec" aria-labelledby="ensayos-titulo">
<div class="container grid">
<div class="head c-1-5"><h2 id="ensayos-titulo">Ensayos que hacemos en nuestra planta</h2><p>Ensayamos cada pieza en nuestra planta antes de enviarla, según la especificación de su pedido.</p></div>
<div class="body c-6-12"><div class="tests">
<div class="test"><h3>Pruebas de presión</h3><p class="muted">Comprobamos la estanqueidad con presión hidrostática o neumática, según su especificación.</p></div>
<div class="test"><h3>Líquidos penetrantes</h3><p class="muted">Detectamos discontinuidades abiertas a la superficie: grietas, poros y faltas de fusión.</p><p class="small">Certificación: EN ISO 9712, nivel II</p></div>
<div class="test"><h3>Pruebas de helio</h3><p class="muted">Detectamos fugas con helio en piezas que exigen una estanqueidad muy alta.</p></div>
</div></div>
</div>
</section>
<section id="metrologia" class="sec" aria-labelledby="metro-titulo">
<div class="container grid">
<div class="c-1-6"><img loading="lazy" class="photo" style="aspect-ratio: 1 / 1" src="/_blob/d769c662c1de2be375a7ff7301bd9d1e" alt="Carcasa de acero fundido en la mesa de granito de la máquina de medición por coordenadas, con el palpador sobre la pieza" width="1000" height="1000"></div>
<div class="body c-7-12">
<div class="head"><h2 id="metro-titulo">Control dimensional certificado</h2><p>Medimos cada pieza en máquina tridimensional sobre plano globeado y le entregamos su informe de cotas. Si usted tiene una especificación propia, la seguimos.</p></div>
''' + spec([('Equipo', 'Trimek Spark 16.10.12, máquina de medición por coordenadas tipo puente<br><span class="small muted">Volumen de medida 1.600 × 1.000 × 1.200 mm</span>'),
            ('Entorno', 'Sala climatizada, temperatura controlada, mesa de granito')]) + '''
</div>
</div>
</section>
<section class="sec" aria-labelledby="iso-titulo">
<div class="container grid">
<div class="head c-1-5"><h2 id="iso-titulo">Sistema de gestión certificado según ISO 9001</h2><p>Globeamos cada referencia nueva antes de fabricarla. Seguimos cada pieza durante todo el proceso y la expedimos con la documentación de control que pida su pedido.</p><div><a href="#" download="" class="btn btn--line">''' + g.ICON_DESCARGA + '''Certificado ISO 9001 (PDF)</a></div></div>
<div class="body c-6-12"><ul class="rows">
<li><h3>Plano globeado</h3><p>Previo a fabricación.</p></li>
<li><h3>Trazabilidad</h3><p>De cada pieza.</p></li>
<li><h3>Control</h3><p>Según su plano y su especificación.</p></li>
<li><h3>Informe dimensional y de ensayos</h3><p>Con la expedición.</p></li>
</ul></div>
</div>
</section>
''' + cta('¿Su pieza requiere un ensayo concreto?', 'Díganos la norma o la especificación y le confirmaremos si podemos hacerlo en nuestra planta.')
       + '</main>\n' + g.pie_html(False))
escribir('Calidad-v8.dc.html', documento('Calidad', 'Calidad-v8', stamp('Feature Stack', 'the two tests set large, the metrology spec beside the CMM photograph', '/* Hallmark · waive 77 · the own test list of AML · the plant runs two authorised tests and has no photograph of them yet, so the section stays two items until Calidad sends one */\n'), cal, 3700))

# =================== Sectores ===================
secs = [('s1', 'Petróleo y gas', 'Mecanizamos esferas y cuerpos de válvula, carcasas de bomba y componentes para extracción, refino y transporte, sobre todo en aceros inoxidables, dúplex y superdúplex.', 'd65d5cc5289447730fdd58ef599aca4c', 'Carcasa de bomba de acero fundido amarrada en la mesa de la mandrinadora'),
        ('s2', 'Naval', 'Hacemos componentes para buques e instalaciones marinas, donde el agua de mar exige materiales muy resistentes a la corrosión.', 'bef63af4d8affc677728347bbd8ce6d1', 'Pieza mecanizada para propulsión marina por chorro de agua'),
        ('s3', 'Nuclear', 'Mecanizamos componentes para instalaciones nucleares con trazabilidad completa, control dimensional y ensayos documentados. Soldamos con procedimientos según el código nuclear RCC-M y con soldadores certificados según UNE-EN ISO 9606-1.', 'adf15f215d0ddf830ceff1fb843f069d', 'Voluta para la industria nuclear durante su mecanizado'),
        ('s4', 'Ferroviario', 'Servimos componentes para material rodante e infraestructura ferroviaria, en series con entregas programadas.', 'f93368d377d333d21f18780a7ba287dd', 'Caja de grasa ferroviaria en control dimensional con brazo de medición'),
        ('s5', 'Sanitario', 'Mecanizamos piezas para equipos del sector sanitario, con los acabados y las tolerancias que pida su especificación.', '0b199555e961d8fb690f60d4ccf1b0f2', 'Cuerpo de acero inoxidable con brida montado en su bancada para la prueba de presión'),
        ('s6', 'Industrial', 'Hacemos componentes para maquinaria y equipos de proceso: bombas, válvulas y carcasas.', '242556ff58e4c1a3d42edee320c67914', 'Rodete de bomba de acero fundido mecanizado'),
        ('s7', 'Estructural', 'Mecanizamos piezas de acero fundido para estructuras y uniones que trabajan bajo carga.', 'b3328804d8c220af4e73c389b91db6f2', 'Puente en arco de hormigón con tirantes')]
PIEZAS = {'s1': 'Valve bodies (6″ to 24″), valve spheres, flowmeters',
          's2': 'Álabes de hélice, <span lang="en">pump casings</span>, <span lang="fr">corps de compresseur</span>, <span lang="en">nozzles</span>, difusores',
          's3': '<span lang="en">Multi-stage pump, frame expander casing, compressor case, volute valves, suction case, stuffing box, impeller</span>, rueda de turbina, anillos',
          's4': 'Soportes patín, cajas de grasa, consolas de enganche, soportes de enganche elástico',
          's6': 'Multi-stage casings, volutes, impellers, bowls, suction cases, barrels for centrifugal pumps, manifolds, compressor cases, motor casings'}
GAL = {'s1': [('d65d5cc5289447730fdd58ef599aca4c', 'Carcasa de bomba de acero fundido amarrada en la mesa de la mandrinadora', 'Pump casing'), ('dab1ed35b8b3e669807859fda54ecaf0', 'Carcasa de bomba partida de acero fundido en la mandrinadora, con la barra de mandrinar dentro de la boca', 'Pump casing'), ('f30b4b5940fd49bf18f0e9e231ce7da1', 'Cuerpo de caudalímetro en la máquina de medición por coordenadas', 'Flowmeter'), ('1ad00e791a34e705e4cfdb635cdcbc46', 'Cuerpo de válvula de acero fundido amarrado en el centro de mecanizado', 'Valve body'), ('cbbdb4bea3ffe26e764c02ab6f8fc03d', 'Cuerpo de válvula de acero fundido mecanizado', 'Valve body')], 's2': [('bef63af4d8affc677728347bbd8ce6d1', 'Pieza mecanizada para propulsión marina por chorro de agua', 'Marine jet propulsion component'), ('6ac429a70670a8bd9779adb032b24bda', 'Rodete de acero fundido mecanizado, apoyado en un palé en la nave', 'Impeller')], 's3': [('adf15f215d0ddf830ceff1fb843f069d', 'Voluta para la industria nuclear durante su mecanizado', 'Volute'), ('d8aa2dd2239315a997be1df7d344b86b', 'Voluta de acero superdúplex 5A con la tapa de prueba atornillada, preparada para la prueba de presión', 'Volute casing'), ('5acb77b89d9abb6d137c2c501fc725ff', 'Carcasa de bomba multietapa preparada para la prueba hidrostática', 'Multi-stage pump casing')], 's4': [('0407f2a2ce7557500c6a4b49ea71aacb', 'Pieza ferroviaria de acero fundido amarrada en el centro de mecanizado, con el reloj comparador en el husillo', ''), ('f93368d377d333d21f18780a7ba287dd', 'Caja de grasa ferroviaria en control dimensional con brazo de medición', 'Axlebox housing')], 's6': [('242556ff58e4c1a3d42edee320c67914', 'Rodete de bomba de acero fundido mecanizado', 'Impeller'), ('0b0076e60e3821c0bec24600fd4a72f0', 'Carcasa multietapa amarrada en la mesa de mecanizado', 'Multi-stage casing'), ('9cb41a0981fb29eb0dc37656fd331165', 'Carcasa de compresor preparada para la prueba hidrostática', 'Compressor case'), ('19f098cf86edd222d162d3dd7212d600', 'Dos carcasas de aspiración mecanizadas', 'Suction case'), ('624f0d549e58cc056be9b97322839a50', 'Rodete y difusor preparados para el escaneo 3D de los álabes', 'Impeller & bowl')]}
CHEV_IZQ = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>'
CHEV_DER = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg>'

def fotos(i, n, b, a):
    lst = GAL.get(i) or ([(b, a, '')] if b else [])
    figs = ''.join(f'<figure class="carrusel__foto"><img loading="lazy" src="/_blob/{t[0]}" alt="{t[1]}" width="1200" height="900"'
                   + (f' style="object-position: {t[3]}"' if len(t) > 3 else '') + '>'
                   + (f'<figcaption lang="en">{t[2]}</figcaption>' if t[2] else '') + '</figure>' for t in lst)
    if len(lst) <= 1:
        return f'<div class="carrusel__pista">{figs}</div>'
    return (f'<div class="carrusel__pista" tabindex="0" aria-label="Fotos de piezas: {n}" onScroll="{{{{carruselContar}}}}">{figs}</div>'
            f'<div class="carrusel__ctrl"><span class="carrusel__n" aria-live="polite">1 / {len(lst)}</span>'
            f'<button type="button" class="carrusel__btn" aria-label="Foto anterior" onClick="{{{{carruselAnt}}}}">{CHEV_IZQ}</button>'
            f'<button type="button" class="carrusel__btn" aria-label="Foto siguiente" onClick="{{{{carruselSig}}}}">{CHEV_DER}</button></div>')

def sector(i, n, d, b, a):
    txt = (f'<div class="sector__txt on-ink"><h2>{n}</h2><p>{d}</p>'
           + (f'<p class="piezas"><span class="piezas__lbl">Piezas habituales</span><span{"" if i in ("s2", "s3", "s4") else ' lang="en"'}>{PIEZAS[i]}</span></p>' if i in PIEZAS else '')
           + '</div>')
    varias = len(GAL.get(i, [])) > 1
    return (f'<li id="{i}" class="sector carrusel"' + (' role="region" aria-roledescription="carrusel"' if varias else '') + f' aria-label="{n}">'
            + fotos(i, n, b, a) + '<div class="sector__velo" aria-hidden="true"></div>' + txt + '</li>\n')

filas = ''.join(sector(*x) for x in secs)
sec = (g.cabecera('SEC', False)
       + banner('33c33c750dbdfdb983ee872208e67539', '50% 40%', 'Sectores', 'Sectores con los que trabajamos',
                'Todos son exigentes con el material, la estanqueidad y la trazabilidad, y así es como trabajamos nosotros.', ' banner--derecha')
       + '<section class="sec" aria-label="Sectores">\n<div class="container" style="display: grid; gap: var(--space-2xl)">\n'
       + '<nav aria-label="Sectores en esta página"><ul class="anchors">' + ''.join(f'<li><a href="#{i}">{n}</a></li>' for i, n, *_ in secs) + '</ul></nav>\n'
       + '<ul class="sectors">\n' + filas + '</ul>\n</div>\n</section>\n'
       + cta('¿Su sector no aparece?', 'Trabajamos según su plano y su especificación. Cuéntenos su aplicación y la estudiamos.')
       + '</main>\n' + g.pie_html(False))
escribir('Sectores-v8.dc.html', documento('Sectores', 'Sectores-v8', stamp('Index-First', 'the seven sectors as an index with their own photographs'), sec, 4300))

# =================== Materiales ===================
mats = [('Acero al carbono', [('WCB', 'ASTM A216', '1.0619', 1, 'Válvulas y piezas a presión'), ('WCC', 'ASTM A216', 'Sin dato', 1, 'Válvulas y piezas a presión'),
                              ('LCB', 'ASTM A352', 'Sin dato', 1, 'Servicio a baja temperatura'), ('LCC', 'ASTM A352', 'Sin dato', 1, 'Servicio a baja temperatura')]),
        ('Inoxidable austenítico', [('CF8', 'ASTM A351', '1.4308', 2.5, 'Válvulas, bombas, industria química'), ('CF3', 'ASTM A351', 'Sin dato', 2.5, 'Versión bajo carbono de CF8'),
                                    ('CF8M', 'ASTM A351', '1.4408', 2.5, 'Medios con cloruros, química'), ('CF3M', 'ASTM A351', 'Sin dato', 2.5, 'Versión bajo carbono de CF8M')]),
        ('Dúplex', [('4A (CD3MN)', 'ASTM A890 / A995', '1.4470', 4, 'Petróleo y gas, desalación'), ('1B (CD4MCuN)', 'ASTM A890 / A995', 'Sin dato', 4, 'Bombas y medios abrasivos')]),
        ('Superdúplex', [('5A (CE3MN)', 'ASTM A890 / A995', '1.4469', 5, 'Agua de mar, offshore'), ('6A (CD3MWCuN)', 'ASTM A890 / A995', 'Sin dato', 5, 'Agua de mar, alta presión')])]
filas_m = ''
for fam, lst in mats:
    filas_m += f'<tr class="grupo"><th colspan="5" scope="colgroup">{fam}</th></tr>'
    for c, n, en, r, u in lst:
        rs = str(r).replace('.', ',').replace(',0', '')
        filas_m += (f'<tr><th scope="row">{c}</th><td data-label="Norma ASTM">{n}</td><td class="num" data-label="Equivalente EN">{en}</td>'
                    f'<td data-label="Corrosión"><span class="bar" role="img" aria-label="Resistencia a la corrosión {rs} de 5"><span style="width: {r / 5 * 100:.0f}%"></span></span></td><td data-label="Usos">{u}</td></tr>')
CAMPO = 'class="field"'
mat = (g.cabecera('MAT', False)
       + banner('597616a036eb7bc7b983449e654d5b10', '50% 50%', 'Materiales', 'Materiales que mecanizamos',
                'Mecanizamos aceros al carbono, inoxidables, dúplex y superdúplex en estado fundido. Si trabaja con otra aleación, consúltenos con el plano y la especificación.')
       + '''<section class="sec" aria-labelledby="grados-titulo">
<div class="container" style="display: grid; gap: var(--space-xl)">
<div class="cta"><div class="head"><h2 id="grados-titulo">Grados y normas</h2></div><div class="actions"><a href="#" download="" class="btn btn--line">''' + g.ICON_DESCARGA + '''Descargar tabla (PDF)</a></div></div>
<div class="table-wrap" role="region" aria-label="Tabla de materiales" tabindex="0"><table class="table table--data"><caption class="visually-hidden">Tabla de materiales que mecaniza AML</caption>
<thead><tr><th scope="col">Grado</th><th scope="col">Norma ASTM</th><th scope="col">Equivalente EN</th><th scope="col">Resistencia a la corrosión</th><th scope="col">Usos habituales</th></tr></thead>
<tbody>''' + filas_m + '''</tbody></table></div>
<p class="note">Equivalencias EN y resistencia a la corrosión orientativas.</p>
</div>
</section>
<section id="consulta" class="sec sec--tint rel" aria-labelledby="consulta-titulo">
<div class="container grid">
<div class="head c-1-5"><h2 id="consulta-titulo">¿Trabaja con otra aleación?</h2><p>Le confirmaremos la viabilidad del mecanizado y de los ensayos. Para valorar su consulta con rapidez, indíquenos:</p>
<ul class="checklist">
<li><strong>Material</strong><span>Grado o especificación (p. ej. ASTM A890 5A)</span></li>
<li><strong>Plano</strong><span>PDF, STEP o DWG, con su revisión</span></li>
<li><strong>Cantidades</strong><span>Unidades y calendario de entregas previsto</span></li>
<li><strong>Ensayos</strong><span>Ensayos y documentación de calidad requeridos</span></li>
<li><strong>Plazo</strong><span>Fecha de necesidad de las piezas</span></li>
</ul></div>
<form class="form c-7-12" data-endpoint="" novalidate="" onSubmit="{{enviar}}">
<div class="form__pair">
<label class="field">Nombre<input type="text" name="nombre" autocomplete="name" required=""></label>
<label class="field">Empresa<input type="text" name="empresa" autocomplete="organization"></label>
<label class="field">Email<input type="email" name="email" autocomplete="email" required=""></label>
<label class="field">Material o especificación<input type="text" name="material"></label>
</div>
<label class="field">Mensaje<textarea name="mensaje" rows="4"></textarea></label>
<label class="field">Plano (opcional)<input type="file" name="plano" accept=".pdf,.step,.stp,.dwg"></label>
<label class="check"><input type="checkbox" name="privacidad" required="">He leído y acepto la política de privacidad.</label>
<div><button type="submit" class="btn btn--ink">Enviar consulta</button></div>
<p class="form__help" aria-live="polite">{{avisoForm}}</p>
</form>
</div>
</section>
</main>
''' + g.pie_html(False))
escribir('Materiales-v8.dc.html', documento('Materiales', 'Materiales-v8', stamp('Catalogue', 'the grade table with one corrosion bar per grade'), mat, 3300))

# =================== Contacto ===================
fila_f = ('<tr><td class="table__fecha num">[DD al DD MES]</td><td><span class="table__feria">[Nombre de la feria]</span><span class="muted small">[Ciudad, País], [sector]</span></td>'
          '<td class="muted">Stand [nº]</td><td><a href="#formulario" class="link" style="white-space: nowrap">Solicitar reunión</a></td></tr>')
Q = 'AML+Centrifugal+Casting,+Industrialdea+A-7,+31870+Lekunberri,+Navarra'
con = (g.cabecera('CON', False)
       + banner('7f788c0badd0760fd48912e94f453d1d', '50% 40%', 'Contacto', 'Contacto',
                'Escríbanos para pedir una oferta, hacernos una consulta técnica o coordinar un transporte. También puede visitarnos en las ferias en las que participamos.')
       + '''<section class="sec" aria-labelledby="ferias-titulo">
<div class="container grid fairs2">
<div class="fairs2__body">
<div class="head"><h2 id="ferias-titulo">Venga a conocernos en persona</h2><p>Estas son las próximas ferias en las que estaremos. Si va a asistir, pídanos una reunión con el formulario y le reservaremos un momento en nuestro stand.</p></div>
<table class="table"><caption class="visually-hidden">Próximas ferias</caption>
<thead><tr><th scope="col">Fechas</th><th scope="col">Feria</th><th scope="col">Stand</th><th scope="col"><span class="visually-hidden">Acción</span></th></tr></thead>
<tbody>''' + fila_f * 3 + '''</tbody></table>
</div>
<div class="fairs2__photo"><img loading="lazy" class="photo" src="/_blob/7f788c0badd0760fd48912e94f453d1d" alt="Stand de AML Centrifugal Casting en una feria internacional" width="800" height="1000" style="object-position: 50% 45%"></div>
</div>
</section>
<section id="formulario" class="sec sec--tint" aria-labelledby="form-titulo">
<div class="container grid">
<div class="head c-1-5"><h2 id="form-titulo">Escríbanos</h2><div class="contact__facts"><a href="tel:+34948461603">+34 948 46 16 03</a><a href="mailto:info@amlcentrifugal.com">info@amlcentrifugal.com</a></div></div>
<form class="form c-7-12" data-endpoint="" novalidate="" onSubmit="{{enviar}}">
<div class="form__pair">
<label class="field">Nombre<input type="text" name="nombre" autocomplete="name" required=""></label>
<label class="field">Empresa<input type="text" name="empresa" autocomplete="organization"></label>
<label class="field">Email<input type="email" name="email" autocomplete="email" required=""></label>
<label class="field">Motivo
<select name="motivo">
<option>Solicitud de oferta</option>
<option>Consulta técnica</option>
<option>Soy proveedor</option>
<option>Transporte o recogida de piezas</option>
<option>Trabajar en AML</option>
<option>Reunión en feria</option>
<option>Otro</option>
</select></label>
</div>
<label class="field">Mensaje<textarea name="mensaje" rows="4"></textarea></label>
<label class="check"><input type="checkbox" name="privacidad" required="">He leído y acepto la política de privacidad.</label>
<div><button type="submit" class="btn btn--ink">Enviar solicitud</button></div>
<p class="form__help" aria-live="polite">{{avisoForm}}</p>
</form>
</div>
</section>
<section id="como-llegar" class="sec" aria-labelledby="llegar-titulo">
<div class="container" style="display: grid; gap: var(--space-xl)">
<h2 id="llegar-titulo">Ubicación y acceso</h2>
<div class="where">
<div id="transporte" class="transport on-ink">
<h3>Proveedores y transportistas</h3>
<address>AML Centrifugal Casting, S.L.<br>Industrialdea, A-7<br>31870 Lecumberri (Navarra)</address>
''' + spec([('Carga y descarga', 'Lunes a viernes, de 8:00 a 17:00'), ('Acceso camiones', 'Entrada principal'), ('Al llegar', 'Llame al timbre de la entrada principal')]) + f'''
</div>
<div class="map"><iframe title="Mapa de la ubicación de AML Centrifugal Casting en Lecumberri" src="https://www.google.com/maps?q={Q}&amp;z=15&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
</div>
<div><a href="https://www.google.com/maps/dir/?api=1&amp;destination={Q}" target="_blank" rel="noopener" class="btn btn--line">Obtener indicaciones en Google Maps</a></div>
</div>
</section>
</main>
''' + g.pie_html(False))
escribir('Contacto-v8.dc.html', documento('Contacto', 'Contacto-v8', stamp('Split Studio', 'the truck access beside the live map'), con, 3200))
