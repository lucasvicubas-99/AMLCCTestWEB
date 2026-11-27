"""Genera la web v9 (menú lateral, estilo técnico): portada + 5 subpáginas con CSS y JS comunes."""
import json

import os
AQUI = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(os.path.dirname(AQUI), '')
P = json.load(open(os.path.join(AQUI, 'v9_parts.json'), encoding='utf-8'))
import re as _re
P['ops'] = _re.sub(r'<figcaption>.*?</figcaption>', '', P['ops'])
for _a, _b in [('Geometrías complejas en centros de mecanizado y 5 ejes.', 'Fresado en 5 ejes.'), ('Piezas de revolución y torneado esférico de gran volteo.', 'Torneado de gran volteo.'), ('Alojamientos de precisión en piezas de gran tamaño.', 'Mandrinado de piezas grandes.'), ('Soldadura certificada de piezas de acero fundido.', 'Soldadura certificada.')]:
    P['ops'] = P['ops'].replace(_a, _b)
ASIDE = P['aside'][:P['aside'].rindex('    </div>')].rstrip() + '\n'
_LLEGAR = ASIDE[ASIDE.index('        <div><a class="link" href="https://www.google.com/maps/dir/'):ASIDE.index('</a></div>', ASIDE.index('maps/dir/')) + len('</a></div>\n')]
ASIDE = ASIDE.replace(_LLEGAR, '').replace('</address>\n', '</address>\n' + _LLEGAR.replace('<div>', '<div class="aside__llegar">'), 1)

# ------------------------------------------------------------------ CSS común
CSS = open(os.path.join(AQUI, 'v9_base.css'), encoding='utf-8').read()
CSS += r'''
/* ---------- añadidos para la web de varias páginas ---------- */
.side__item > a[aria-current] { color: var(--title); }

/* cabecera de subpágina */
.cab { position: relative; isolation: isolate; min-height: clamp(420px, 62svh, 600px); display: flex; align-items: flex-end; overflow: hidden; background: var(--title); }
.cab__img { position: absolute; inset: 0; z-index: -2; width: 100%; height: 100%; object-fit: cover; }
.cab::before { content: ""; position: absolute; inset: 0; z-index: -1; background: linear-gradient(to right, rgba(10, 10, 10, 0.6) 0%, rgba(10, 10, 10, 0.25) 50%, rgba(10, 10, 10, 0) 75%), linear-gradient(to top, rgba(10, 10, 10, 0.8) 0%, rgba(10, 10, 10, 0.4) 55%, rgba(10, 10, 10, 0.15) 100%); }
.cab::after { content: ""; position: absolute; inset: 0; z-index: 3; background: var(--bg); pointer-events: none; animation: desde-blanco 1.2s cubic-bezier(0.25, 1, 0.5, 1) 0.05s forwards; }
.cab__in { padding-block: 0 72px; display: grid; gap: 24px; }
.cab .label { color: var(--white); }
.cab .label::before { background: var(--white); }
.cab h1 { font-size: clamp(40px, 5vw, 72px); font-weight: 500; letter-spacing: -0.025em; line-height: 1.1; color: var(--white); max-width: 14em; }
.cab p { max-width: 36em; color: rgba(255, 255, 255, 0.82); }
.ruta { display: flex; gap: 10px; font-size: 12px; letter-spacing: 0.15em; text-transform: uppercase; color: rgba(255, 255, 255, 0.7); }
.ruta a { color: var(--white); text-decoration: none; border-bottom: 1px solid rgba(255, 255, 255, 0.5); }

/* fases del proceso */
.grid5 { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); margin-top: 72px; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); }
.grid5 > li { min-width: 0; display: grid; }
.grid5 > li + li { border-left: 1px solid var(--line); }
.grid5 .cell { padding-right: 24px; }
.grid5 > li + li .cell { padding-left: 28px; }
.cell .num { font-size: 13px; font-weight: 500; letter-spacing: 0.2em; color: var(--accent); }
.cell .mas { margin-top: 4px; font-size: 11px; font-weight: 500; letter-spacing: 0.18em; text-transform: uppercase; color: var(--title); border-bottom: 2px solid var(--accent); justify-self: start; padding-bottom: 3px; }
a.cell { color: inherit; }

/* tarjetas con foto */
.cards4 { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 32px; margin-top: 72px; }
.card { display: grid; gap: 14px; align-content: start; text-decoration: none; min-width: 0; }
.card img { width: 100%; height: auto; aspect-ratio: 4 / 5; object-fit: cover; transition: opacity 0.3s; }
.card h3 { font-size: 20px; font-weight: 500; color: var(--title); letter-spacing: -0.01em; margin-top: 8px; }
.card p { font-size: 15px; line-height: 1.65; }
.card:hover img { opacity: 0.88; }
.card:hover h3 { color: var(--accent); }

/* filas con línea */
.filas { border-top: 1px solid var(--line); }
.filas li { display: grid; grid-template-columns: minmax(0, 2fr) minmax(0, 3fr); gap: 8px 32px; padding: 20px 0; border-bottom: 1px solid var(--line); }
.filas strong { font-weight: 500; color: var(--title); }
.filas span { font-size: 16px; }
.filas a { text-decoration: none; }
.filas a:hover strong { color: var(--accent); }

/* mini galería */
.mini { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; margin-top: 8px; }
.mini figure { display: grid; gap: 6px; min-width: 0; }
.mini img { width: 100%; height: auto; aspect-ratio: 4 / 3; object-fit: cover; }
.mini__btn { display: block; width: 100%; padding: 0; border: 0; background: none; cursor: zoom-in; }
.mini__btn img { transition: opacity 0.2s; }
.mini__btn:hover img { opacity: 0.8; }
.mini__btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.split__media img.cambia { animation: aparece 0.35s ease; }
@keyframes aparece { from { opacity: 0.2; } to { opacity: 1; } }
.mini figcaption { font-size: 12px; color: var(--muted); }

/* datos destacados por operación */
.datos { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); border-top: 1px solid var(--line); }
.datos div { padding: 18px 16px 0 0; min-width: 0; }
.datos div + div { padding-left: 16px; border-left: 1px solid var(--line); }
.datos b { display: block; font-size: 22px; font-weight: 500; letter-spacing: -0.01em; color: var(--title); line-height: 1.25; }
.datos span { display: block; margin-top: 6px; font-size: 11px; font-weight: 500; letter-spacing: 0.18em; text-transform: uppercase; color: var(--muted); }

.split--ancho { grid-template-columns: minmax(0, 7fr) minmax(0, 5fr); gap: 64px; }
.split--ancho .split__media img { aspect-ratio: 4 / 5; }


/* buscador de materiales */
.buscador { margin-top: 72px; padding: 36px 40px; background: var(--bg-alt); border: 1px solid var(--line); display: grid; gap: 24px; }
.sec--alt .buscador { background: var(--bg); }
.buscador__fila { display: flex; flex-wrap: wrap; align-items: flex-end; gap: 24px 40px; }
.buscador__campo { flex: 1 1 320px; min-width: 0; display: grid; grid-template-columns: minmax(0, 1fr); gap: 10px; font-size: 11px; font-weight: 500; letter-spacing: 0.2em; text-transform: uppercase; color: var(--muted); }
.buscador__input { display: flex; align-items: center; gap: 12px; border-bottom: 1px solid var(--title); color: var(--title); }
.buscador__input input { flex: 1; width: 100%; min-width: 0; min-height: 48px; border: 0; border-radius: 0; background: transparent; color: var(--title); font: 400 20px/1.3 var(--font); letter-spacing: -0.01em; text-transform: none; }
.buscador__input input:focus-visible { outline: none; }
.buscador__input:focus-within { border-bottom-color: var(--accent); box-shadow: 0 1px 0 var(--accent); }
.buscador__input input::placeholder { color: var(--muted); opacity: 1; }
.chips { display: flex; flex-wrap: wrap; gap: 8px; }
.chip { min-height: 44px; padding: 0 18px; border: 1px solid var(--field); border-radius: 0; background: var(--bg); color: var(--title); font: 500 11px/1 var(--font); letter-spacing: 0.15em; text-transform: uppercase; cursor: pointer; transition: border-color 0.2s, background-color 0.2s, color 0.2s; }
.chip:hover { border-color: var(--title); }
.chip[aria-pressed="true"] { background: var(--accent); border-color: var(--accent); color: var(--white); }
.buscador__res { min-height: 1.6em; font-size: 14px; color: var(--text); }
.buscador__res a { color: var(--title); text-decoration: none; border-bottom: 2px solid var(--accent); }
.buscador + .tabla-wrap { margin-top: 32px; }


/* materiales: cabecera con foto y escala de corrosión */
.mat-top { display: grid; grid-template-columns: minmax(0, 1fr); gap: 48px; align-items: start; }
.mat-top__img { width: 100%; height: auto; max-width: 300px; justify-self: end; }
.escala { margin: 72px 0 0; }
.escala__cab { display: flex; justify-content: space-between; gap: 16px; font-size: 11px; font-weight: 500; letter-spacing: 0.2em; text-transform: uppercase; color: var(--muted); }
.escala__fila { position: relative; display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); margin: 32px 0 0; padding: 0; list-style: none; }
.escala__fila::before { content: ""; position: absolute; left: 10%; right: 10%; top: 66px; height: 1px; background: var(--title); }
.escala__fila li { position: relative; display: grid; justify-items: center; text-align: center; gap: 4px; min-width: 0; }
.escala__fila b { font-size: 36px; font-weight: 500; letter-spacing: -0.02em; line-height: 1.2; color: var(--title); }
.escala__fila i { display: block; width: 13px; height: 13px; margin: 14px 0 16px; border: 1px solid var(--title); border-radius: 50%; background: var(--bg); }
.escala__fila li.alta i { background: var(--accent); border-color: var(--accent); }
.escala__fila strong { font-size: 14px; font-weight: 500; color: var(--title); }
.escala__fila span { font-size: 14px; color: var(--text); line-height: 1.5; }
.escala .nota { margin-top: 28px; }
.sec--alt .escala__fila i { background: var(--bg-alt); }
.sec--alt .escala__fila li.alta i { background: var(--accent); }
.escala + .buscador { margin-top: 48px; }
.resultados { border-top: 1px solid var(--line); }
.resultados li { display: grid; grid-template-columns: minmax(0, 1.2fr) minmax(0, 2fr); gap: 4px 24px; padding: 14px 0; border-bottom: 1px solid var(--line); font-size: 15px; }
.resultados b { font-weight: 500; color: var(--title); }

.tabla-fam { min-width: 640px; }
.tabla-fam td:first-child { white-space: normal; width: 42%; }
.tabla-fam td:last-child { color: var(--title); }


/* campo de archivo con botón para quitarlo */
.archivo { position: relative; display: block; }
.archivo input[type="file"] { padding-right: 60px; }
.archivo__quitar { position: absolute; top: 50%; right: 6px; transform: translateY(-50%); width: 44px; height: 44px; display: grid; place-items: center; padding: 0; border: 0; background: transparent; color: var(--title); cursor: pointer; transition: color 0.2s, background-color 0.2s; }
.archivo__quitar:hover { color: var(--white); background: var(--accent); }
.archivo__quitar:focus-visible { outline: 2px solid var(--accent); outline-offset: 0; }

/* barra de resistencia a la corrosión */
.barra { display: inline-block; width: 96px; height: 3px; background: var(--line); vertical-align: middle; }
.barra i { display: block; height: 100%; background: var(--accent); }

/* tablas de ferias */
td a.link { white-space: nowrap; }
.ph { color: var(--muted); }


/* ---------- microanimaciones (v10) ---------- */
.card, a.cell, .mini__btn { transition: transform 0.25s cubic-bezier(0.25, 1, 0.5, 1); }
.card:hover, a.cell:hover { transform: translateY(-2px); }
.card__foto, .split__media, .mini__btn { overflow: hidden; }
.card__foto { display: block; }
.card img, .split__media img, .mini__btn img, .franja__img { transition: transform 0.5s cubic-bezier(0.25, 1, 0.5, 1), opacity 0.3s; }
.card:hover img { transform: scale(1.03); opacity: 1; }
.split__media:hover img { transform: scale(1.02); }
.mini__btn:hover img { transform: scale(1.03); opacity: 1; }
.franja:hover .franja__img { transform: scale(1.02); }
.link { border-bottom: 0; padding-bottom: 6px; background: linear-gradient(var(--accent), var(--accent)) left bottom / 100% 2px no-repeat; transition: color 0.2s, background-size 0s; }
.link--light { background-image: linear-gradient(var(--white), var(--white)); }
.link:hover { animation: dibuja 0.45s cubic-bezier(0.25, 1, 0.5, 1); }
@keyframes dibuja { from { background-size: 0 2px; } to { background-size: 100% 2px; } }
.btn { transition: background-color 0.2s, color 0.2s, transform 0.15s; }
.btn:active, .chip:active, .carrusel__btn:active { transform: translateY(1px); }
.side__item > a:hover::before { transform: scaleY(0.5); }
.side__item.is-active > a:hover::before { transform: scaleY(1); }
.hero__in { animation: entra 0.9s cubic-bezier(0.25, 1, 0.5, 1) 0.4s both; }
@keyframes entra { from { opacity: 0; transform: translateY(16px); } to { opacity: 1; transform: none; } }
@media (prefers-reduced-motion: reduce) { .hero__in { animation: none; } .card:hover, a.cell:hover { transform: none; } .card:hover img, .split__media:hover img, .mini__btn:hover img, .franja:hover .franja__img { transform: none; } .link:hover { animation: none; } }
/* objetivos táctiles en móvil */
@media (max-width: 900px) {
  .foot__links a, .foot p a, .foot__base a, .side__langs a { display: inline-flex; align-items: center; min-height: 44px; }
  .link { display: inline-flex; align-items: flex-end; min-height: 44px; }
  .panel nav a { min-height: 44px; display: flex; align-items: center; }
  .chip { min-height: 44px; }
  .filas a, .ruta a { display: inline-flex; align-items: center; min-height: 44px; }
  .buscador__input input { min-height: 48px; }
}

@media (max-width: 1180px) {
  .grid5 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .grid5 > li:nth-child(4) { border-left: 0; }
  .grid5 > li:nth-child(4) .cell { padding-left: 0; }
  .grid5 > li:nth-child(n+4) { border-top: 1px solid var(--line); }
  .cards4 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (max-width: 900px) {
  .cab__in { padding-bottom: 48px; }
  .filas li { grid-template-columns: minmax(0, 1fr); }
  .split--ancho { grid-template-columns: minmax(0, 1fr); }
  .split--ancho .split__media img { aspect-ratio: 4 / 3; }
}
@media (max-width: 600px) {
  .grid5 { grid-template-columns: minmax(0, 1fr); }
  .grid5 > li, .grid5 > li + li { border-left: 0; }
  .grid5 > li .cell, .grid5 > li + li .cell { padding-left: 0; }
  .grid5 > li + li { border-top: 1px solid var(--line); }
  .cards4 { grid-template-columns: minmax(0, 1fr); gap: 48px; }
  .card img { aspect-ratio: 4 / 3; }
  .datos { grid-template-columns: minmax(0, 1fr); }
  .datos div, .datos div + div { padding: 14px 0; border-left: 0; border-bottom: 1px solid var(--line); }
  .mini { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .buscador { padding: 24px 20px; }
  .buscador__campo { flex-basis: 100%; }
  .mat-top { grid-template-columns: minmax(0, 1fr); }
  .mat-top__img { max-width: 200px; justify-self: start; order: -1; }
  .escala__fila { grid-template-columns: minmax(0, 1fr); gap: 0; }
  .escala__fila::before { left: 6px; right: auto; top: 22px; bottom: 22px; width: 1px; height: auto; }
  .escala__fila li { grid-template-columns: 24px 88px minmax(0, 1fr); grid-template-rows: auto auto; justify-items: start; text-align: left; gap: 0 12px; padding: 12px 0; align-items: center; }
  .escala__fila i { grid-row: 1 / 3; grid-column: 1; margin: 0; }
  .escala__fila b { grid-row: 1 / 3; grid-column: 2; font-size: 26px; }
  .escala__fila strong { grid-column: 3; }
  .escala__fila span { grid-column: 3; font-size: 13px; }
  .escala__fila span + span { display: none; }
  .resultados li { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); }
}
'''

# ------------------------------------------------------------------ JS común
CSS += r"""
/* sectores: fotos enteras, sin recorte ni zoom */
.sector .split__media img { aspect-ratio: auto; height: auto; object-fit: contain; }
.sector .split__media:hover img, .sector .mini__btn:hover img { transform: none; }
.sector .mini img { object-fit: contain; background: var(--bg-alt); }
.sec--alt.sector .mini img { background: var(--bg); }
"""
CSS += r"""
/* contacto: columna lateral alineada con el formulario */
.js-form { position: relative; }
.form__aviso:empty { position: absolute; }
@media (min-width: 1025px) {
  .contact { align-items: stretch; }
  .aside { display: flex; flex-direction: column; gap: 40px; }
  .aside__llegar { margin-top: -24px; }
  .mapa { flex: 1; aspect-ratio: auto; min-height: 0; }
}
"""
CSS += r"""
/* sectores en móvil: carrusel con las fotos enteras */
.scar { display: none; }
@media (max-width: 900px) {
  .sector--car .mini, .sector--car .split__media { display: none; }
  .scar { display: grid; gap: 12px; margin-top: 8px; }
  .scar__pista { display: flex; overflow-x: auto; scroll-snap-type: x mandatory; scrollbar-width: none; }
  .scar__pista::-webkit-scrollbar { display: none; }
  .scar__pista:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
  .scar__foto { flex: 0 0 100%; margin: 0; scroll-snap-align: start; aspect-ratio: 1 / 1; background: var(--bg-alt); }
  .sec--alt .scar__foto { background: var(--bg); }
  .scar__foto img { width: 100%; height: 100%; object-fit: contain; display: block; }
  .scar__ctrl { display: flex; align-items: center; gap: 8px; }
  .scar__n { margin-right: auto; font-size: 14px; color: var(--muted); }
  .scar__btn { width: 44px; height: 44px; display: grid; place-items: center; border: 1px solid var(--line); background: var(--bg); color: var(--title); cursor: pointer; }
  .scar__btn:active { transform: scale(0.96); }
  .scar__btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
}
@media (max-width: 900px) and (prefers-reduced-motion: no-preference) { .scar__pista { scroll-behavior: smooth; } }
"""
CSS += r"""
/* fotos que se ven enteras, sin recorte */
.foto-entera .split__media img { aspect-ratio: auto; height: auto; }
"""
CSS += r"""
/* próximas ferias */
.ferias { list-style: none; margin: 8px 0 0; padding: 0; border-top: 1px solid var(--line); }
.ferias__item { display: grid; grid-template-columns: 8.5rem minmax(0, 1fr) auto; gap: 8px 32px; align-items: baseline; padding: 24px 0; border-bottom: 1px solid var(--line); }
.ferias__fecha { margin: 0; font-size: 15px; font-weight: 500; color: var(--title); white-space: nowrap; }
.ferias__item h3 { margin: 0 0 4px; font-size: 18px; font-weight: 500; color: var(--title); }
.ferias__item p { margin: 0; font-size: 15px; color: var(--muted); }
.ferias__stand { white-space: nowrap; }
@media (max-width: 600px) {
  .ferias__item { grid-template-columns: minmax(0, 1fr); gap: 6px; }
  .ferias__stand { white-space: normal; }
}
"""
open(R + 'assets/v10.css', 'w', encoding='utf-8').write(CSS)
JS = r'''(function () {
  var cuerpo = document.body;
  // Portada: alterna Inicio / Quiénes somos según la sección visible
  var emp = document.getElementById('empresa');
  var itInicio = document.querySelector('.side__item[data-pag="inicio"]');
  var itEmp = document.querySelector('.side__item[data-pag="empresa"]');
  var arriba = document.getElementById('arriba');
  function al_desplazar() {
    if (emp && itInicio && itEmp && cuerpo.dataset.pag === 'inicio') {
      var r = emp.getBoundingClientRect(), dentro = r.top < window.innerHeight * 0.4 && r.bottom > window.innerHeight * 0.4;
      itEmp.classList.toggle('is-active', dentro); itInicio.classList.toggle('is-active', !dentro);
    }
    if (arriba) arriba.classList.toggle('is-on', window.scrollY > window.innerHeight * 0.8);
  }
  window.addEventListener('scroll', al_desplazar, { passive: true }); al_desplazar();

  // Panel de menú en móvil
  var panel = document.getElementById('panel'), abrir = document.getElementById('abrir'), cerrar = document.getElementById('cerrar');
  if (panel && abrir && cerrar) {
    var cierra = function () { panel.hidden = true; abrir.setAttribute('aria-expanded', 'false'); cuerpo.style.overflow = ''; };
    abrir.addEventListener('click', function () { panel.hidden = false; abrir.setAttribute('aria-expanded', 'true'); cuerpo.style.overflow = 'hidden'; cerrar.focus(); });
    cerrar.addEventListener('click', function () { cierra(); abrir.focus(); });
    panel.addEventListener('click', function (e) { if (e.target.tagName === 'A') cierra(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !panel.hidden) { cierra(); abrir.focus(); } });
  }

  // Desplegables enlazados desde el menú o desde otra página
  function abre(id) { var d = document.getElementById(id); if (d && d.tagName === 'DETAILS') d.open = true; }
  document.querySelectorAll('a[href*="#"]').forEach(function (a) { a.addEventListener('click', function () { var h = a.getAttribute('href').split('#')[1]; if (h) abre(h); }); });
  if (location.hash) abre(location.hash.slice(1));

  // Vídeo de portada
  var v = document.getElementById('video'), p = document.getElementById('pausa');
  if (v && p) {
    var estado = function () { p.setAttribute('aria-label', v.paused ? 'Reproducir el vídeo' : 'Pausar el vídeo'); p.innerHTML = v.paused ? '<svg width="14" height="14" viewBox="0 0 14 14" aria-hidden="true"><path d="M3 1l9 6-9 6z" fill="currentColor"/></svg>' : '<svg width="14" height="14" viewBox="0 0 14 14" aria-hidden="true"><path d="M3 1v12M11 1v12" stroke="currentColor" stroke-width="1.5"/></svg>'; };
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) { v.removeAttribute('autoplay'); v.pause(); }
    p.addEventListener('click', function () { if (v.paused) v.play(); else v.pause(); estado(); });
    v.addEventListener('play', estado); v.addEventListener('pause', estado); estado();
  }

  // Buscador de materiales: filas o elementos con data-grupo
  document.querySelectorAll('.buscador').forEach(function (b) {
    var lista = b.querySelector('.resultados');
    var cont = lista || (b.parentElement.querySelector('table.js-filtrable tbody'));
    if (!cont) return;
    var input = b.querySelector('.js-buscar'), chips = b.querySelectorAll('.chip'), res = b.querySelector('.buscador__res');
    var norm = function (t) { return String(t).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, ''); };
    var items = Array.prototype.map.call(cont.querySelectorAll('[data-grupo]'), function (el) { return { el: el, g: el.dataset.grupo, txt: norm(el.textContent) }; });
    var elegido = '';
    function filtra() {
      var q = norm(input.value.trim()), n = 0;
      items.forEach(function (it) { var ok = (!elegido || it.g === elegido) && (!q || it.txt.indexOf(q) > -1); it.el.hidden = !ok; if (ok) n++; });
      if (lista) lista.hidden = (!q && !elegido) || n === 0;
      if (!q && !elegido) { res.textContent = ''; return; }
      if (n) res.textContent = n + (n === 1 ? ' familia coincide.' : ' familias coinciden.');
      else res.innerHTML = 'Ninguna familia coincide. <a href="v10-materiales.html#otras">Consulte otras aleaciones</a>.';
    }
    input.addEventListener('input', filtra);
    chips.forEach(function (c) { c.addEventListener('click', function () {
      elegido = elegido === c.dataset.fam ? '' : c.dataset.fam;
      chips.forEach(function (x) { x.setAttribute('aria-pressed', x.dataset.fam === elegido ? 'true' : 'false'); });
      filtra();
    }); });
  });

  // Carrusel de sectores en móvil
  document.querySelectorAll('.scar').forEach(function (c) {
    var pista = c.querySelector('.scar__pista'), n = c.querySelector('.scar__n'), total = pista.children.length;
    function actual() { return Math.round(pista.scrollLeft / pista.clientWidth); }
    pista.addEventListener('scroll', function () { n.textContent = (actual() + 1) + ' / ' + total; }, { passive: true });
    c.querySelectorAll('.scar__btn').forEach(function (b) {
      b.addEventListener('click', function () {
        var i = (actual() + Number(b.getAttribute('data-dir')) + total) % total;
        pista.scrollTo({ left: i * pista.clientWidth });
      });
    });
  });

  // Galería de sectores: la miniatura pulsada pasa a la foto grande
  document.querySelectorAll('.mini__btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var sec = btn.closest('section'), grande = sec && sec.querySelector('.split__media img');
      if (!grande) return;
      var peq = btn.querySelector('img');
      var s1 = grande.getAttribute('src'), a1 = grande.getAttribute('alt');
      grande.setAttribute('src', peq.getAttribute('src')); grande.setAttribute('alt', peq.getAttribute('alt'));
      peq.setAttribute('src', s1); peq.setAttribute('alt', a1);
      btn.setAttribute('aria-label', 'Ver en grande: ' + a1);
      grande.classList.remove('cambia'); void grande.offsetWidth; grande.classList.add('cambia');
    });
  });

  // Campo de archivo: botón para quitar el archivo elegido
  document.querySelectorAll('input[type="file"]').forEach(function (inp) {
    var caja = document.createElement('span'); caja.className = 'archivo';
    inp.parentNode.insertBefore(caja, inp); caja.appendChild(inp);
    var x = document.createElement('button'); x.type = 'button'; x.className = 'archivo__quitar'; x.hidden = true;
    x.setAttribute('aria-label', 'Quitar el archivo seleccionado'); x.title = 'Quitar archivo';
    x.innerHTML = '<svg width="14" height="14" viewBox="0 0 14 14" aria-hidden="true"><path d="M2 2l10 10M12 2L2 12" stroke="currentColor" stroke-width="1.5"/></svg>';
    caja.appendChild(x);
    var estado = function () { x.hidden = !(inp.files && inp.files.length); };
    inp.addEventListener('change', estado);
    x.addEventListener('click', function () { inp.value = ''; estado(); inp.focus(); });
    var f = inp.form; if (f) f.addEventListener('reset', function () { setTimeout(estado, 0); });
  });

  // Formularios (pendientes de conectar)
  document.querySelectorAll('form.js-form').forEach(function (f) {
    var aviso = f.querySelector('.form__aviso');
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      f.querySelectorAll('[aria-invalid]').forEach(function (x) { x.removeAttribute('aria-invalid'); });
      var malo = f.querySelector(':invalid');
      if (malo) { malo.setAttribute('aria-invalid', 'true'); malo.focus(); aviso.textContent = 'Faltan datos obligatorios: nombre, email válido y aceptación de la política de privacidad.'; return; }
      aviso.textContent = 'Formulario pendiente de conexión. Escriba a info@amlcentrifugal.com.';
    });
  });
})();
'''
open(R + 'assets/v10.js', 'w', encoding='utf-8').write(JS)

import hashlib
VER = hashlib.md5((CSS + JS).encode()).hexdigest()[:8]

# ------------------------------------------------------------------ piezas comunes
LOGO = '''<svg width="0" height="0" style="position: absolute" aria-hidden="true">
  <symbol id="logo-aml" viewBox="0 0 474.2 243">
    <path d="M0.00 100.00L0.00 57.17A42.83 42.83 0 0 1 0.00 142.83ZM0.00 34.81A65.19 65.19 0 0 1 0.00 165.19L0.00 158.97A58.97 58.97 0 0 0 0.00 41.03ZM0.00 18.75A81.25 81.25 0 0 1 0.00 181.25L0.00 170.61A70.61 70.61 0 0 0 0.00 29.39ZM0.00 0.00A100.0 100.0 0 0 1 0.00 200.00L0.00 192.15A92.15 92.15 0 0 0 0.00 7.85Z" fill="#011F67" fill-rule="evenodd"/>
    <path d="M41.32 0H436.20A38 38 0 0 1 474.20 38V162A38 38 0 0 1 436.20 200H41.32A108.20 108.20 0 0 0 41.32 0Z" fill="#011F67"/>
    <text x="154.2" y="152.0" font-size="149.0" font-weight="600" fill="#FFFFFF" textLength="262.0" lengthAdjust="spacing" font-family="'IBM Plex Sans', system-ui, sans-serif">AML</text>
    <text x="1.0" y="241.0" font-size="27.2" font-weight="500" fill="#011F67" textLength="472.2" lengthAdjust="spacing" font-family="'IBM Plex Sans', system-ui, sans-serif">CENTRIFUGAL CASTING</text>
  </symbol>
  <symbol id="ondas" viewBox="0 0 400 200">
    <g fill="none" stroke="currentColor" stroke-width="1"><path d="M120 200A80 80 0 0 1 280 200"/><path d="M80 200A120 120 0 0 1 320 200"/><path d="M60 200A140 140 0 0 1 340 200"/><path d="M20 200A180 180 0 0 1 380 200"/><path d="M0 200A200 200 0 0 1 400 200"/></g>
  </symbol>
</svg>'''

MENU = [
    ('inicio', 'Inicio', 'v10.html', [('#proceso', 'cómo trabajamos'), ('#ferias', 'ferias')]),
    ('empresa', 'Quiénes somos', 'v10.html#empresa', []),
    ('capacidades', 'Capacidades', 'v10-capacidades.html', [('#fresado', 'fresado'), ('#torneado', 'torneado'), ('#mandrinado', 'mandrinado'), ('#soldadura', 'soldadura')]),
    ('materiales', 'Materiales', 'v10-materiales.html', [('#grados', 'grados y normas'), ('#otras', 'otras aleaciones'), ('#consulta', 'consulta')]),
    ('sectores', 'Sectores', 'v10-sectores.html', [('#s-petroleo', 'petróleo y gas'), ('#s-nuclear', 'nuclear'), ('#s-naval', 'naval'), ('#s-ferroviario', 'ferroviario'), ('#s-industrial', 'industrial'), ('#s-sanitario', 'sanitario'), ('#s-estructural', 'estructural')]),
    ('calidad', 'Calidad', 'v10-calidad.html', [('#ensayos', 'ensayos'), ('#metrologia', 'control dimensional'), ('#sistema', 'sistema de calidad')]),
    ('contacto', 'Contacto', 'v10-contacto.html', [('#ferias', 'ferias'), ('#formulario', 'formulario'), ('#llegar', 'carga y descarga')]),
]
LANGS = ''
_LANGS_OFF = '<div class="side__langs" role="group" aria-label="Idioma"><a href="#" aria-current="true" lang="es">ES</a><a href="#" lang="en">EN</a><a href="#" lang="de">DE</a><a href="#" lang="it">IT</a><a href="#" lang="fr">FR</a></div>'


def lateral(pag):
    items = ''
    for k, nombre, href, sub in MENU:
        act = k == pag
        cur = ' aria-current="page"' if act and k != 'empresa' else ''
        h = sub_html = ''
        if act and sub:
            sub_html = '<ul class="side__sub">' + ''.join(f'<li><a href="{a}">{t}</a></li>' for a, t in sub) + '</ul>'
        if pag == 'inicio' and k == 'inicio':
            href = '#inicio'
        if pag == 'inicio' and k == 'empresa':
            href = '#empresa'
        items += f'<li class="side__item{" is-active" if act else ""}" data-pag="{k}"><a href="{href}"{cur}>{nombre}</a>{sub_html}</li>\n'
    return f'''<aside class="side" aria-label="Navegación principal">
  <a class="side__logo" href="v10.html" aria-label="AML Centrifugal Casting, inicio"><svg viewBox="0 0 474.2 243" aria-hidden="true"><use href="#logo-aml"/></svg></a>
  <nav class="side__nav"><ul>
{items}  </ul></nav>
  {LANGS}
</aside>
<header class="topbar">
  <a href="v10.html" aria-label="AML Centrifugal Casting, inicio"><svg viewBox="0 0 474.2 243" aria-hidden="true"><use href="#logo-aml"/></svg></a>
  <button class="menu-btn" type="button" aria-expanded="false" aria-controls="panel" id="abrir">Menú <i aria-hidden="true"></i></button>
</header>
<div class="panel" id="panel" hidden role="dialog" aria-modal="true" aria-label="Menú">
  <div class="panel__top"><svg viewBox="0 0 474.2 243" aria-hidden="true"><use href="#logo-aml"/></svg><button class="menu-btn" type="button" id="cerrar">Cerrar</button></div>
  <nav aria-label="Navegación principal"><ul>
    {''.join(f'<li><a href="{h}"{" aria-current=" + chr(34) + "page" + chr(34) if k == pag and k != "empresa" else ""}>{n}</a></li>' for k, n, h, _ in MENU)}
  </ul></nav>
  {LANGS}
</div>'''


PIE = '''<section class="cta" aria-labelledby="t-cta">
  <div class="ondas" style="right: 0; bottom: 0; width: 420px; transform: translate(25%, 0); opacity: 0.5"><svg aria-hidden="true"><use href="#ondas"/></svg></div>
  <div class="wrap cta__in">
    <div class="head">
      <p class="label">Solicitud de oferta</p>
      <h2 class="title" id="t-cta">Presupuesto bajo plano.</h2>
      <p class="text">Estudio de viabilidad técnica y plazo para cada referencia.</p>
    </div>
    <div class="actions"><a class="btn" href="v10-contacto.html#formulario">Solicitar oferta</a></div>
  </div>
</section>
'''

FOOT = '''</main>
<footer class="foot">
  <div class="wrap">
    <div class="foot__cols">
      <div><h2>Contacto</h2><p><a href="tel:+34948461603">+34 948 46 16 03</a><br><a href="mailto:info@amlcentrifugal.com">info@amlcentrifugal.com</a></p></div>
      <div><h2>Dirección</h2><p>Industrialdea, A-7<br>31870 Lecumberri (Navarra)<br>España</p></div>
      <div><h2>Enlaces</h2><nav class="foot__links" aria-label="Enlaces del pie"><a href="v10.html#empresa">Quiénes somos</a><a href="v10-capacidades.html">Capacidades</a><a href="v10-materiales.html">Materiales</a><a href="v10-sectores.html">Sectores</a><a href="v10-calidad.html">Calidad</a><a href="v10-contacto.html">Contacto</a></nav></div>
    </div>
    <div class="foot__base"><p>AML Centrifugal Casting, S.L. Sistema de gestión certificado ISO 9001.</p></div>
  </div>
</footer>
<a class="arriba" id="arriba" href="#top" aria-label="Volver arriba"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M3 10l5-5 5 5"/></svg></a>
<script src="./assets/v10.js?v={VER}"></script>
</body>
</html>
'''


def doc(pag, titulo, desc, cuerpo, cta=True):
    return (f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="./assets/planta-multistage-casing.webp">
<meta property="og:locale" content="es_ES">
<link rel="icon" href="./favicon.ico?v=3" sizes="any">
<link rel="icon" href="./assets/iconos/favicon.svg?v=3" type="image/svg+xml">
<link rel="apple-touch-icon" href="./assets/iconos/apple-touch-icon.png?v=3">
<meta name="theme-color" content="#011F67">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=IBM+Plex+Sans:wght@500;600&display=swap">
<link rel="stylesheet" href="./assets/v10.css?v={VER}">
<script src="./assets/transicion-v9.js"></script>
</head>
<body data-pag="{pag}" id="top">
<a class="skip" href="#contenido">Saltar al contenido</a>
{LOGO}
{lateral(pag)}
<main id="contenido">
{cuerpo}{PIE if cta else ''}''' + FOOT).replace('{VER}', VER)


def cab(img, alt, pos, ruta, label, h1, texto):
    return f'''<section class="cab" aria-labelledby="t-cab">
  <!-- FOTO DE CABECERA: {alt} -->
  <img class="cab__img" src="./assets/{img}" alt="" aria-hidden="true" style="object-position: {pos}">
  <div class="wrap cab__in">
    <nav class="ruta" aria-label="Ruta"><a href="v10.html">Inicio</a><span aria-hidden="true">/</span><span aria-current="page">{ruta}</span></nav>
    <p class="label">{label}</p>
    <h1 id="t-cab">{h1}</h1>
    <p>{texto}</p>
  </div>
</section>
'''


def fig(img, alt, w, h, cap='', cls=''):
    return (f'<figure class="split__media{cls}"><img src="./assets/{img}" alt="{alt}" width="{w}" height="{h}" loading="lazy">'
            + '</figure>')


FORM = P['form'].replace('<form id="formulario" novalidate>', '<form class="js-form" novalidate>').replace('<p class="form__aviso" id="aviso" aria-live="polite"></p>', '<p class="form__aviso" aria-live="polite"></p>')

FORM = FORM.replace('>Enviar solicitud</button>', '>Solicitar oferta</button>')
FERIAS_DATOS = [
    ('1–3 dic. 2026', 'Valve World Expo 2026', 'Düsseldorf, Alemania. Válvulas industriales.', 'Pabellón 3, stand E27'),
    ('9–12 mar. 2027', 'DSEI Germany 2027', 'Hannover, Alemania. Defensa.', 'Stand por confirmar'),
]
TABLA_FERIAS = ('<ul class="ferias" aria-label="Próximas ferias">'
                + ''.join(f'<li class="ferias__item"><p class="ferias__fecha">{f}</p><div><h3 lang="en">{n}</h3><p>{d}</p></div><p class="ferias__stand">{st}</p></li>' for f, n, d, st in FERIAS_DATOS)
                + '</ul>')

ICON = {
    'fresado': '<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1" aria-hidden="true"><rect x="15" y="3" width="10" height="10"/><path d="M17 13v15l3 4 3-4V13"/><path d="M17 17l6 3M17 22l6 3"/><path d="M4 36h32"/></svg>',
    'torneado': '<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1" aria-hidden="true"><circle cx="16" cy="20" r="13"/><circle cx="16" cy="20" r="5"/><path d="M16 7v4M16 29v4M3 20h4M25 20h4"/><path d="M30 26l7 5"/></svg>',
    'mandrinado': '<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1" aria-hidden="true"><rect x="4" y="10" width="22" height="22"/><circle cx="15" cy="21" r="6"/><path d="M15 21h22M31 17v8"/></svg>',
    'soldadura': '<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1" aria-hidden="true"><path d="M6 6l16 16"/><path d="M22 22l4 4"/><path d="M4 34h32"/><path d="M28 28l-2 4M30 27l3 3M29 30l4-1"/></svg>',
    'presion': '<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1" aria-hidden="true"><circle cx="20" cy="22" r="14"/><path d="M20 22l7-7"/><path d="M14 4h12M20 4v4"/></svg>',
    'penetrantes': '<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1" aria-hidden="true"><path d="M20 4c6 9 10 15 10 20a10 10 0 0 1-20 0c0-5 4-11 10-20z"/><path d="M15 26c1 3 3 4 6 4"/></svg>',
    'helio': '<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1" aria-hidden="true"><circle cx="20" cy="20" r="5"/><circle cx="20" cy="20" r="11"/><circle cx="20" cy="20" r="17"/></svg>',
    'cmm': '<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1" aria-hidden="true"><path d="M6 36V8h28v28"/><path d="M20 8v14"/><circle cx="20" cy="24" r="2"/><path d="M2 36h36"/></svg>',
}

BUSCADOR = """    <div class="buscador" role="search">
      <div class="buscador__fila">
        <label class="buscador__campo">Buscar material
          <span class="buscador__input"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg><input type="search" class="js-buscar" placeholder="WCB, CF8M, CA6NM, 1.4470…" autocomplete="off"></span></label>
        <div class="chips" role="group" aria-label="Filtrar por familia">
          <button type="button" class="chip" aria-pressed="false" data-fam="carbono">Al carbono</button>
          <button type="button" class="chip" aria-pressed="false" data-fam="aleados">Aleados</button>
          <button type="button" class="chip" aria-pressed="false" data-fam="inoxidables">Inoxidables</button>
          <button type="button" class="chip" aria-pressed="false" data-fam="niquel">Base níquel</button>
        </div>
      </div>
      <p class="buscador__res" aria-live="polite"></p>
    </div>
"""

ESCALA = """    <figure class="escala">
      <figcaption class="escala__cab"><span>Resistencia a la corrosión</span><span>De menor a mayor</span></figcaption>
      <ol class="escala__fila">
        <li><b>WCB</b><i aria-hidden="true"></i><strong>Acero al carbono</strong><span>A216 WCB</span><span>EN 1.0619</span></li>
        <li><b>CF8</b><i aria-hidden="true"></i><strong>Inoxidable</strong><span>A351 CF8</span><span>EN 1.4308</span></li>
        <li><b>CF8M</b><i aria-hidden="true"></i><strong>Inoxidable con Mo</strong><span>A351 CF8M</span><span>EN 1.4408</span></li>
        <li class="alta"><b>4A</b><i aria-hidden="true"></i><strong>Dúplex</strong><span>A890 4A</span><span>EN 1.4470</span></li>
        <li class="alta"><b>5A</b><i aria-hidden="true"></i><strong>Superdúplex</strong><span>A890 5A</span><span>EN 1.4469</span></li>
      </ol>
      <p class="nota">Normas ASTM y equivalentes EN orientativos.</p>
    </figure>
"""
FAMILIAS = [
    ('carbono', 'Aceros al carbono para usos generales', ['WCB', 'WCC', '1.0619', 'GS45', 'GS52', 'GS60']),
    ('carbono', 'Aceros al carbono para baja temperatura', ['LCB', 'LCC', 'GS20Mn5', 'GS212Mn5']),
    ('aleados', 'Aceros aleados', ['WC1', 'WC6', 'WC9', 'C5', 'C12']),
    ('aleados', 'Aceros aleados para baja temperatura', ['LC1', 'LC2', 'LC3']),
    ('aleados', 'Aceros de herramientas', ['GS42CrMo4']),
    ('inoxidables', 'Aceros martensíticos y martensítico-ferríticos, para servicios generales y baja temperatura', ['CA15', 'CA6NM', '1.4008']),
    ('inoxidables', 'Aceros inoxidables austeníticos, dúplex y superdúplex, para usos generales y baja temperatura', ['1.4408', '1.4468', '1.4470', '1.4519', '1.4308', '1.4552', '1.4581', 'CF3', 'CF3M', 'CF8', 'CF8M', 'CF8C', 'CN7M', 'CN3M', 'dúplex', 'superdúplex']),
    ('niquel', 'Aleaciones base níquel', ['2.4883', '2.4697']),
]
def grados_html(lst):
    return ', '.join(lst)

BUSCADOR_LISTA = BUSCADOR.replace('<div class="buscador" role="search">', '<div class="buscador buscador--lista" role="search">').replace(
    '      <p class="buscador__res" aria-live="polite"></p>\n',
    '      <p class="buscador__res" aria-live="polite"></p>\n      <ul class="resultados" hidden>' + ''.join(
        f'<li data-grupo="{gr}"><b>{nom}</b><span>{grados_html(lst)}</span></li>' for gr, nom, lst in FAMILIAS) + '</ul>\n')

TABLA_FAM = ('    <div class="tabla-wrap" role="region" aria-label="Familias de materiales" tabindex="0">\n      <table class="js-filtrable tabla-fam">\n'
             '        <caption class="sr">Familias de acero fundido y aleaciones que mecanizamos</caption>\n'
             '        <thead><tr><th scope="col">Familia</th><th scope="col">Grados de ejemplo</th></tr></thead>\n        <tbody>\n'
             + ''.join(f'          <tr data-grupo="{gr}"><td>{nom}</td><td>{grados_html(lst)}, …</td></tr>\n' for gr, nom, lst in FAMILIAS)
             + '        </tbody>\n      </table>\n    </div>\n')

# ================================================================== PORTADA
INICIO = f'''<section class="hero" id="inicio" aria-labelledby="t-inicio">
  <!-- VÍDEO DE PORTADA: mecanizado en planta (sin la sierra) -->
  <video class="hero__media" id="video" autoplay muted loop playsinline preload="metadata" poster="./assets/portada-poster.webp" aria-hidden="true">
    <source src="./assets/portada-v2.mp4" type="video/mp4">
  </video>
  <div class="wrap hero__in">
    <p class="label">Lecumberri, Navarra</p>
    <h1 id="t-inicio">Mecanizado de piezas de acero fundido bajo plano.</h1>
    <p>Mecanizado CNC, control dimensional y ensayos en nuestra planta, 24 horas en tres turnos. Piezas de hasta 12.000 kg.</p>
    <div class="actions"><a class="btn" href="#contacto">Solicitar oferta</a><a class="link link--light" href="v10-contacto.html#llegar">Cómo llegar</a></div>
  </div>
  <button class="hero__pausa" type="button" id="pausa" aria-label="Pausar el vídeo"></button>
</section>

<section class="sec" id="empresa" aria-labelledby="t-empresa">
  <div class="ondas" style="right: 0; top: 0; width: 360px; transform: translate(30%, -10%) rotate(180deg)"><svg aria-hidden="true"><use href="#ondas"/></svg></div>
  <div class="wrap split">
    <div class="head">
      <p class="label">Quiénes somos</p>
      <h2 class="title" id="t-empresa">Planta propia en Lecumberri desde 2012.</h2>
      <div>
        <p class="text">Somos AML Centrifugal Casting. Desde 2012, en nuestra planta de Lecumberri (Navarra), mecanizamos con precisión piezas de acero fundido con tolerancias ajustadas, y nosotros mismos las medimos y ensayamos antes de entregarlas.</p>
        <p class="text">Trabajamos bajo pedido, desde una sola pieza hasta series con entregas programadas. Tratamos planos y documentación técnica con estricta confidencialidad y seguimos cada pieza de principio a fin, con trazabilidad completa. Clientes en toda España y fuerte presencia internacional.</p>
      </div>
          </div>
    <!-- FOTO: carcasa de bomba amarrada en el centro de mecanizado -->
    {fig('mandrinado-carcasa-nave.webp', 'Cabezal de la mandrinadora trabajando una carcasa de acero fundido en la nave', 819, 1024)}
  </div>
  <div class="wrap">
    <div class="figs" role="list">
      <div class="fig" role="listitem"><span class="fig__bg" aria-hidden="true">15</span><p class="fig__n">+15</p><p class="fig__l">Años de actividad</p></div>
      <div class="fig" role="listitem"><span class="fig__bg" aria-hidden="true">24</span><p class="fig__n">24 h</p><p class="fig__l">Planta en tres turnos</p></div>
      <div class="fig" role="listitem"><span class="fig__bg" aria-hidden="true">12</span><p class="fig__n">12.000 kg</p><p class="fig__l">Peso máximo de pieza</p></div>
      <div class="fig" role="listitem"><span class="fig__bg" aria-hidden="true">5</span><p class="fig__n">± 0,005 mm</p><p class="fig__l">Tolerancia en 5 ejes</p></div>
    </div>
  </div>
</section>

<section class="sec sec--alt" id="proceso" aria-labelledby="t-proceso">
  <div class="wrap">
    <div class="head">
      <p class="label">Cómo trabajamos</p>
      <h2 class="title" id="t-proceso">Proceso de fabricación.</h2>
      <p class="text">Trabajamos 24 horas, en tres turnos. Cada pieza pasa por cinco fases, todas en nuestra planta, y la tenemos identificada en cada una.</p>
      <div class="actions"><a class="btn" href="#contacto">Solicitar oferta</a></div>
    </div>
    <ol class="grid5" style="list-style: none; padding: 0">
      <li><a class="cell" href="#materiales"><span class="num">01</span><h3>Recepción</h3><p>Recibimos la pieza en bruto y la identificamos.</p></a></li>
      <li><a class="cell" href="#capacidades"><span class="num">02</span><h3>Mecanizado</h3><p>Mecanizamos en CNC según plano, con programación CAM en Siemens NX.</p></a></li>
      <li><a class="cell" href="#calidad"><span class="num">03</span><h3>Control dimensional</h3><p>Medimos cada pieza en tridimensional y emitimos su informe.</p></a></li>
      <li><a class="cell" href="#calidad"><span class="num">04</span><h3>Ensayos</h3><p>Pruebas de presión, líquidos penetrantes y pruebas de helio.</p></a></li>
      <li><a class="cell" href="#contacto"><span class="num">05</span><h3>Expedición</h3><p>Preparamos la documentación, embalamos y enviamos.</p></a></li>
    </ol>
  </div>
</section>

<section class="sec" id="capacidades" aria-labelledby="t-cap">
  <div class="wrap">
    <div class="head">
      <p class="label">Capacidades</p>
      <h2 class="title" id="t-cap">Fresado, torneado, mandrinado y soldadura.</h2>
      <p class="text">Mecanizamos, inspeccionamos y ensayamos en nuestra propia planta. Todo el proceso se hace aquí, según su plano y su especificación.</p>
      <div class="actions"><a class="btn" href="v10-capacidades.html">Ver capacidades</a></div>
    </div>
    <div class="cards4">
      <a class="card" href="v10-capacidades.html#fresado"><span class="card__foto"><img src="./assets/fresado-carcasa.webp" alt="Husillo del centro de mecanizado trabajando una carcasa de bomba de acero fundido amarrada en escuadra" width="900" height="1125" loading="lazy"></span><h3>Fresado</h3><p>Centros de mecanizado y 5 ejes. Hasta Ø 2.000 × 1.500 mm y 4.500 kg.</p></a>
      <a class="card" href="v10-capacidades.html#torneado"><span class="card__foto"><img src="./assets/m-torneado-anillo.webp" alt="Anillo de acero amarrado en el plato de un torno CNC" width="576" height="720" loading="lazy"></span><h3>Torneado</h3><p>Gran volteo y torneado esférico. Volteo hasta Ø 1.600 mm.</p></a>
      <a class="card" href="v10-capacidades.html#mandrinado"><span class="card__foto"><img src="./assets/mandrinado.webp" alt="Mandrinadora TOS Varnsdorf WHN 13 CNC con una pieza amarrada en la mesa" width="960" height="1200" loading="lazy"></span><h3>Mandrinado</h3><p>Columna móvil. Hasta 12.000 kg sobre mesa giratoria.</p></a>
      <a class="card" href="v10-capacidades.html#soldadura"><span class="card__foto"><img src="./assets/soldadura-brida-v2.webp" alt="Soldador trabajando el interior de una brida de acero fundido en el taller" width="1200" height="1500" loading="lazy"></span><h3>Soldadura</h3><p>Soldadores certificados UNE-EN ISO 9606-1. Procedimientos RCC-M.</p></a>
    </div>
  </div>
</section>

<section class="sec sec--alt" id="materiales" aria-labelledby="t-mat">
  <div class="wrap">
    <div class="mat-top">
      <div class="head">
        <p class="label">Materiales</p>
        <h2 class="title" id="t-mat">Materiales que mecanizamos.</h2>
        <p class="text">Mecanizamos aceros al carbono, aleados, de herramientas, martensíticos, inoxidables austeníticos, dúplex y superdúplex en estado fundido, y aleaciones base níquel. Si trabaja con otra aleación, consúltenos con el plano y la especificación.</p>
        <div class="actions"><a class="btn" href="v10-materiales.html">Ver materiales</a></div>
      </div>
    </div>
{ESCALA}
{BUSCADOR_LISTA}  </div>
</section>

<section class="sec" id="calidad" aria-labelledby="t-cal">
  <div class="ondas" style="left: 0; bottom: 0; width: 320px; transform: translate(-35%, 0)"><svg aria-hidden="true"><use href="#ondas"/></svg></div>
  <div class="wrap split split--rev">
    <div class="head">
      <p class="label">Calidad</p>
      <h2 class="title" id="t-cal">Control dimensional y ensayos.</h2>
      <p class="text">Controlamos cada fase, desde el plano hasta la expedición. Nuestro sistema de gestión de la calidad está certificado según ISO 9001.</p>
      <ul class="filas">
        <li><strong>Control dimensional</strong><span>En máquina tridimensional, con informe por pieza.</span></li>
        <li><strong>Plano globeado</strong><span>Previo a la fabricación de cada referencia nueva.</span></li>
        <li><strong>Trazabilidad</strong><span>De cada pieza durante todo el proceso.</span></li>
        <li><strong>Ensayos</strong><span>Pruebas de presión, líquidos penetrantes y pruebas de helio.</span></li>
      </ul>
      <div class="actions"><a class="btn" href="v10-calidad.html">Ver calidad</a></div>
    </div>
    <!-- FOTO: carcasa en la máquina tridimensional -->
    {fig('metrologia-cmm.webp', 'Carcasa de acero fundido en la mesa de granito de la máquina de medición por coordenadas', 1000, 1000, 'Control dimensional en máquina de medición por coordenadas.', ' split__media--sq')}
  </div>
</section>

<section class="sec sec--alt" id="sectores" aria-labelledby="t-sec">
  <div class="wrap">
    <div class="head">
      <p class="label">Sectores</p>
      <h2 class="title" id="t-sec">Sectores con los que trabajamos.</h2>
      <p class="text">Mecanizamos piezas para petróleo y gas, naval, nuclear, ferroviario, sanitario, industria y estructuras.</p>
      <div class="actions"><a class="link" href="v10-sectores.html">Ver sectores</a></div>
    </div>
    <!-- FOTO ANCHA: cuerpos de válvula mecanizados en la nave -->
    <div class="franja">
      <img class="franja__img" src="./assets/materiales-pieza-bridas.webp" alt="" aria-hidden="true" width="1333" height="868" loading="lazy" style="object-position: 50% 45%">
      <div class="franja__col"><h3>Petróleo y gas</h3><p>Válvulas, bombas y componentes para extracción, refino y transporte.</p><a class="link link--light" href="v10-sectores.html#s-petroleo">Ver sector</a></div>
      <div class="franja__col"><h3>Nuclear</h3><p>Componentes con trazabilidad completa y ensayos.</p><a class="link link--light" href="v10-sectores.html#s-nuclear">Ver sector</a></div>
      <div class="franja__col"><h3>Naval y ferroviario</h3><p>Buques, instalaciones marinas, material rodante e infraestructura.</p><a class="link link--light" href="v10-sectores.html#s-naval">Ver sector</a></div>
      <div class="franja__col"><h3>Industrial</h3><p>Maquinaria y equipos de proceso.</p><a class="link link--light" href="v10-sectores.html#s-industrial">Ver sector</a></div>
    </div>
    <ul class="filas" style="margin-top: 56px">
      <li><a href="v10-sectores.html#s-sanitario"><strong>Sanitario</strong></a><span>Piezas para equipos del sector sanitario.</span></li>
      <li><a href="v10-sectores.html#s-estructural"><strong>Estructural</strong></a><span>Piezas de acero fundido para estructuras y uniones.</span></li>
      <li><a href="v10-contacto.html#formulario"><strong>Otros sectores</strong></a><span>Consulte su aplicación.</span></li>
    </ul>
  </div>
</section>


<section class="sec" id="ferias" aria-labelledby="t-fer">
  <div class="wrap split split--ancho">
    <div class="head" style="max-width: none">
      <p class="label">Ferias</p>
      <h2 class="title" id="t-fer">Próximas ferias.</h2>
      <p class="text">Estas son las próximas ferias en las que estaremos. Si va a asistir, pídanos una reunión y le reservaremos un tiempo en nuestro stand.</p>
      {TABLA_FERIAS}
      <div class="actions"><a class="btn" href="v10-contacto.html#ferias">Solicitar reunión</a></div>
    </div>
    <!-- FOTO: stand de AML en feria -->
    {fig('stand.webp', 'Stand de AML Centrifugal Casting en una feria internacional', 1200, 900)}
  </div>
</section>

<section class="sec sec--alt" id="contacto" aria-labelledby="t-con">
  <div class="wrap">
    <div class="head">
      <p class="label">Solicitud de información</p>
      <h2 class="title" id="t-con">Solicitud de oferta.</h2>
      <p class="text">Escríbanos para pedir una oferta, hacernos una consulta técnica o presentarse como proveedor.</p>
      <div class="actions"><a class="link" href="mailto:info@amlcentrifugal.com">info@amlcentrifugal.com</a><a class="link" href="tel:+34948461603">+34 948 46 16 03</a></div>
    </div>
    <div class="contact">
{FORM}
{ASIDE}    </div>
  </div>
</section>
'''
open(R + 'v10.html', 'w', encoding='utf-8').write(doc('inicio', 'AML Centrifugal Casting · Mecanizado y control de calidad de piezas de acero fundido',
    'Mecanizado CNC, control dimensional y ensayos de piezas de acero fundido bajo plano, en planta propia en Lecumberri.', INICIO, cta=False))

# ================================================================== CAPACIDADES
OPS = P['ops']
datos = {
    'fresado': [('Ø 2.000 × 1.500 mm', 'Dimensión máx.'), ('4.500 kg', 'Peso máx.'), ('± 0,005 mm', 'Tolerancia 5 ejes')],
    'torneado': [('Ø 1.600 mm', 'Volteo máx.'), ('1.966 mm', 'Longitud máx.'), ('3.000 kg', 'Peso máx.')],
    'mandrinado': [('12.000 kg', 'Peso máx.'), ('2.500 × 1.800 mm', 'Mesa giratoria'), ('360°', 'Giro de mesa')],
    'soldadura': [('111', 'Proceso'), ('ISO 9606-1', 'Soldadores'), ('RCC-M', 'Procedimientos')],
}
for k, lst in datos.items():
    bloque = '<div class="datos">' + ''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in lst) + '</div>'
    marca = f'<div class="split{" split--rev" if k in ("torneado", "soldadura") else ""}" id="{k}">\n      <div class="head">'
    i = OPS.index(marca)
    j = OPS.index('<div class="acc">', i)
    OPS = OPS[:j] + bloque + '\n        ' + OPS[j:]
_bloques = [b for b in _re.split(r'\n    <!-- [^\n]*-->\n', '\n' + OPS) if b.strip()]
OPS_SECS = ''.join(f'<section class="sec{" sec--alt" if i % 2 == 0 else ""}" aria-label="{["Fresado", "Torneado", "Mandrinado", "Soldadura"][i]}">\n  <div class="wrap">\n    {b.strip()}\n  </div>\n</section>\n' for i, b in enumerate(_bloques))
CAP = cab('m-fresado-valvebody.webp', 'cabezal del centro de mecanizado trabajando un cuerpo de válvula', '50% 45%', 'Capacidades', 'Capacidades',
          'Parque de máquinas y capacidades.', 'Fresado, torneado y mandrinado CNC, y soldadura certificada, en planta propia. Dimensiones y pesos máximos por operación y por máquina.')
CAP += f'''<section class="sec" aria-labelledby="t-res">
  <div class="wrap">
    <div class="head">
      <p class="label">Resumen</p>
      <h2 class="title" id="t-res">Nueve máquinas CNC y soldadura certificada.</h2>
      <p class="text">Programación CAM en Siemens NX. Planta operativa 24 horas en tres turnos.</p>
      <div class="actions"><a class="btn" href="v10-contacto.html#formulario">Solicitar oferta</a></div>
    </div>
    <div class="grid4">
      <a class="cell" href="#fresado">{ICON['fresado']}<h3>Fresado</h3><p>Centros de mecanizado y 5 ejes. Hasta Ø 2.000 × 1.500 mm y 4.500 kg.</p></a>
      <a class="cell" href="#torneado">{ICON['torneado']}<h3>Torneado</h3><p>Gran volteo y torneado esférico. Volteo hasta Ø 1.600 mm.</p></a>
      <a class="cell" href="#mandrinado">{ICON['mandrinado']}<h3>Mandrinado</h3><p>Columna móvil. Hasta 12.000 kg sobre mesa giratoria.</p></a>
      <a class="cell" href="#soldadura">{ICON['soldadura']}<h3>Soldadura</h3><p>Soldadores certificados UNE-EN ISO 9606-1. Procedimientos RCC-M.</p></a>
    </div>
  </div>
</section>
{OPS_SECS}'''
open(R + 'v10-capacidades.html', 'w', encoding='utf-8').write(doc('capacidades', 'Capacidades · AML Centrifugal Casting',
    'Fresado 5 ejes, torneado de gran volteo, mandrinado hasta 12.000 kg y soldadura certificada de piezas de acero fundido.', CAP))

# ================================================================== CALIDAD
CAL = cab('calidad-cuerpos.webp', 'cuerpos de válvula mecanizados', '50% 45%', 'Calidad', 'Calidad',
          'Ensayos y control dimensional.', 'Ninguna pieza sale de nuestra planta sin medir ni ensayar.')
CAL += f'''<section class="sec foto-entera" id="ensayos" aria-labelledby="t-ens">
  <div class="wrap split">
    <div class="head">
      <p class="label">Ensayos</p>
      <h2 class="title" id="t-ens">Ensayos en planta.</h2>
      <p class="text">Ensayamos cada pieza en nuestra planta antes de enviarla, según la especificación de su pedido.</p>
      <div class="actions"><a class="link" href="v10-contacto.html#formulario">Solicitar oferta</a></div>
    </div>
    <!-- FOTO: prueba de presión -->
    {fig('ensayo-presion-cuerpo.webp', 'Cuerpo de acero fundido con las tapas de prueba atornilladas y la manguera conectada, en la prueba de presión', 1333, 868)}
  </div>
  <div class="wrap" style="margin-top: 72px">
    <div class="grid4" style="grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr))">
      <div class="cell">{ICON['presion']}<h3>Pruebas de presión</h3><p>Estanqueidad con presión hidrostática o neumática, según su especificación.</p></div>
      <div class="cell">{ICON['penetrantes']}<h3>Líquidos penetrantes</h3><p>Grietas, poros y faltas de fusión abiertas a la superficie. Certificación EN ISO 9712, nivel II.</p></div>
      <div class="cell">{ICON['helio']}<h3>Pruebas de helio</h3><p>Detección de fugas con helio en piezas que exigen una estanqueidad muy alta.</p></div>
    </div>
  </div>
</section>
<section class="sec sec--alt foto-entera" id="metrologia" aria-labelledby="t-met">
  <div class="wrap split split--rev">
    <div class="head">
      <p class="label">Control dimensional</p>
      <h2 class="title" id="t-met">Control dimensional certificado.</h2>
      <p class="text">Medimos cada pieza en máquina tridimensional sobre plano globeado y entregamos su informe de cotas. Si usted tiene una especificación propia, la seguimos.</p>
      <ul class="filas">
        <li><strong>Equipo</strong><span>Trimek Spark 16.10.12, máquina de medición por coordenadas tipo puente.</span></li>
        <li><strong>Volumen de medida</strong><span>1.600 × 1.000 × 1.200 mm.</span></li>
        <li><strong>Entorno</strong><span>Sala climatizada, temperatura controlada, mesa de granito.</span></li>
      </ul>
    </div>
    <!-- FOTO: carcasa en la máquina tridimensional -->
    {fig('tridimensional-pieza.webp', 'Palpador de la máquina tridimensional midiendo el alojamiento mecanizado de una pieza de acero fundido', 1649, 1125)}
  </div>
</section>
<section class="sec" id="sistema" aria-labelledby="t-sis">
  <div class="wrap split">
    <div class="head">
      <p class="label">Sistema de calidad</p>
      <h2 class="title" id="t-sis">Sistema de calidad ISO 9001.</h2>
      <p class="text">Globeamos cada referencia nueva antes de fabricarla. Seguimos cada pieza durante todo el proceso y la expedimos con la documentación de control que pida su pedido.</p>
      <ul class="filas">
        <li><strong>Plano globeado</strong><span>Previo a la fabricación.</span></li>
        <li><strong>Trazabilidad</strong><span>De cada pieza.</span></li>
        <li><strong>Control</strong><span>Según su plano y su especificación.</span></li>
        <li><strong>Documentación</strong><span>Informe dimensional y de ensayos con la expedición.</span></li>
        <li><strong>Soldadura</strong><span>UNE-EN ISO 9606-1:2017, TÜV SÜD ATISAE. Procedimientos RCC-M.</span></li>
      </ul>
    </div>
    <!-- FOTO: esfera de válvula en la máquina de medición -->
    {fig('car-pg-valve-sphere-cmm.webp', 'Esfera de válvula en la máquina de medición por coordenadas', 610, 457, 'Esfera de válvula en medición.')}
  </div>
</section>
'''
open(R + 'v10-calidad.html', 'w', encoding='utf-8').write(doc('calidad', 'Calidad · AML Centrifugal Casting',
    'Control dimensional en tridimensional, pruebas de presión, líquidos penetrantes, pruebas de helio y sistema ISO 9001.', CAL))

# ================================================================== SECTORES
SECT = [
    ('s-petroleo', 'Petróleo y gas', 'Esferas y cuerpos de válvula, carcasas de bomba y componentes para extracción, refino y transporte, sobre todo en aceros inoxidables, dúplex y superdúplex.',
     'Valve bodies (6″ to 24″), valve spheres, flowmeters',
     [('petroleo-carcasa-centrada.webp', 'Carcasa de bomba de acero fundido amarrada en la mesa de la mandrinadora', 'Pump casing'), ('petroleo-carcasa-partida.webp', 'Carcasa de bomba partida de acero fundido en la mandrinadora, con la barra de mandrinar dentro de la boca', 'Pump casing'), ('flowmeter-cmm-vertical.webp', 'Caudalímetro en la máquina de medición', 'Flowmeter'), ('sector-petroleo-valvula.webp', 'Cuerpo de válvula amarrado en el centro de mecanizado', 'Valve body'), ('car-pg-valve-body-2.webp', 'Cuerpo de válvula mecanizado', 'Valve body')]),
    ('s-nuclear', 'Nuclear', 'Componentes para instalaciones nucleares con trazabilidad completa, control dimensional y ensayos documentados. Soldadura con procedimientos según el código RCC-M y soldadores certificados según UNE-EN ISO 9606-1.',
     '<span lang="en">Multi-stage pump, frame expander casing, compressor case, volute valves, suction case, stuffing box, impeller</span>, rueda de turbina, anillos',
     [('sector-nuclear-voluta.webp', 'Voluta para la industria nuclear en mecanizado', 'Volute'), ('m-voluta-5a-v2.webp', 'Voluta de acero superdúplex 5A con la tapa de prueba atornillada, preparada para la prueba de presión', 'Volute casing'), ('car-nu-multistage-casing.webp', 'Carcasa de bomba multietapa preparada para la prueba hidrostática', 'Multi-stage pump casing')]),
    ('s-naval', 'Naval', 'Componentes para buques e instalaciones marinas, donde el agua de mar exige materiales muy resistentes a la corrosión.',
     'Álabes de hélice, <span lang="en">pump casings</span>, <span lang="fr">corps de compresseur</span>, <span lang="en">nozzles</span>, difusores',
     [('sector-naval-propulsion.webp', 'Pieza mecanizada para propulsión marina por chorro de agua', 'Marine jet propulsion component'), ('naval-rodete-43.webp', 'Rodete de acero fundido mecanizado, apoyado en un palé en la nave', 'Impeller')]),
    ('s-ferroviario', 'Ferroviario', 'Componentes para material rodante e infraestructura ferroviaria, en series con entregas programadas.',
     'Soportes patín, cajas de grasa, consolas de enganche, soportes de enganche elástico',
     [('ferroviario-mecanizado-43.webp', 'Pieza ferroviaria de acero fundido amarrada en el centro de mecanizado, con el reloj comparador en el husillo', ''), ('sector-ferroviario-axlebox.webp', 'Caja de grasa ferroviaria en control dimensional', 'Caja de grasa')]),
    ('s-industrial', 'Industrial', 'Componentes para maquinaria y equipos de proceso: bombas, válvulas y carcasas.',
     'Multi-stage casings, volutes, impellers, bowls, suction cases, barrels for centrifugal pumps, manifolds, compressor cases, motor casings',
     [('sector-industrial-impeller.webp', 'Rodete de bomba mecanizado', 'Impeller'), ('industrial-barrel.webp', 'Barrel de bomba centrífuga de acero fundido amarrado en la mesa de la mandrinadora, con el palpador midiendo la boca', 'Barrel'), ('industrial-suction-case-entera.webp', 'Dos carcasas de aspiración mecanizadas', 'Suction case'), ('car-in-compressor-case.webp', 'Carcasa de compresor', 'Compressor case')]),
    ('s-sanitario', 'Sanitario', 'Piezas para equipos del sector sanitario, con los acabados y las tolerancias que pida su especificación.', '',
     [('sector-sanitario-filtro.webp', 'Cuerpo de acero inoxidable con brida montado en su bancada para la prueba de presión', '')]),
    ('s-estructural', 'Estructural', 'Piezas de acero fundido para estructuras y uniones que trabajan bajo carga.', '',
     []),
]
SEC = cab('rueda-pump.webp', 'rueda de bomba mecanizada en la nave', '60% 50%', 'Sectores', 'Sectores',
          'Sectores con los que trabajamos.', 'Sectores exigentes con el material, la estanqueidad y la trazabilidad.')
for n, (sid, nom, d, piezas, fotos) in enumerate(SECT):
    principal = fotos[0] if fotos else None
    extra = fotos[1:4]
    mini = ('<div class="mini" role="group" aria-label="Más fotos de {nom}">'.replace('{nom}', nom) + ''.join(f'<figure><button type="button" class="mini__btn" aria-label="Ver en grande: {a}"><img src="./assets/{f}" alt="{a}" loading="lazy" width="1200" height="900"></button></figure>' for f, a, c in extra) + '</div>') if extra else ''
    todas = fotos[:4]
    car = (f'<div class="scar" role="group" aria-roledescription="carrusel" aria-label="Fotos de {nom}">'
           f'<div class="scar__pista" tabindex="0">'
           + ''.join(f'<figure class="scar__foto"><img src="./assets/{f}" alt="{a}" loading="lazy"></figure>' for f, a, c in todas)
           + f'</div><div class="scar__ctrl"><span class="scar__n" aria-live="polite">1 / {len(todas)}</span>'
           '<button type="button" class="scar__btn" data-dir="-1" aria-label="Foto anterior"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg></button>'
           '<button type="button" class="scar__btn" data-dir="1" aria-label="Foto siguiente"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg></button></div></div>') if len(todas) > 1 else ''
    filas = f'<ul class="filas"><li><strong>Piezas habituales</strong><span{"" if ("lang=" in piezas or piezas.startswith("Soportes patín")) else ' lang="en"'}>{piezas}</span></li></ul>' if piezas else ''
    SEC += f'''<section class="sec sector{" sector--car" if car else ""}{" sec--alt" if n % 2 else ""}" id="{sid}" aria-labelledby="t-{sid}">
  <div class="wrap{(" split" + (" split--rev" if n % 2 else "")) if principal else ""}">
    <div class="head">
      <p class="label">Sector</p>
      <h2 class="title" id="t-{sid}">{nom}</h2>
      <p class="text">{d}</p>
      {filas}
      {mini}
      {car}
      <div class="actions"><a class="link" href="v10-contacto.html#formulario">Solicitar oferta</a></div>
    </div>
    {fig(principal[0], principal[1], 1200, 900) if principal else '<!-- FOTO PENDIENTE: pieza estructural de AML -->'}
  </div>
</section>
'''
open(R + 'v10-sectores.html', 'w', encoding='utf-8').write(doc('sectores', 'Sectores · AML Centrifugal Casting',
    'Mecanizado de piezas de acero fundido para petróleo y gas, nuclear, naval, ferroviario, industrial, sanitario y estructural.', SEC))

# ================================================================== MATERIALES
TB = P['tbody']
MAT = cab('materiales-piezas-fila.webp', 'fila de piezas de acero fundido en la nave', '50% 50%', 'Materiales', 'Materiales',
          'Materiales que mecanizamos.', 'Aceros al carbono, aleados, inoxidables, dúplex y superdúplex en estado fundido, y aleaciones base níquel. Otras aleaciones, bajo consulta.')
MAT += f'''<section class="sec" id="grados" aria-labelledby="t-gra">
  <div class="wrap">
    <div class="head">
      <p class="label">Familias y grados</p>
      <h2 class="title" id="t-gra">Familias de materiales que mecanizamos.</h2>
      <p class="text">Siete familias de acero fundido y las aleaciones base níquel, con grados de ejemplo de cada una.</p>
    </div>
{BUSCADOR}{TABLA_FAM}    <p class="nota">Ejemplos no exhaustivos. Consulte otros grados con su especificación.</p>
  </div>
</section>
<section class="sec" id="corrosion" aria-labelledby="t-cor">
  <div class="wrap">
    <div class="head">
      <p class="label">Resistencia a la corrosión</p>
      <h2 class="title" id="t-cor">Grados de referencia por resistencia.</h2>
      <p class="text">Cinco grados habituales ordenados de menor a mayor resistencia a la corrosión.</p>
    </div>
{ESCALA}  </div>
</section>
<section class="sec sec--alt" id="otras" aria-labelledby="t-otr">
  <div class="wrap split split--rev">
    <div class="head">
      <p class="label">Otras aleaciones</p>
      <h2 class="title" id="t-otr">Otras aleaciones.</h2>
      <p class="text">Le confirmaremos la viabilidad del mecanizado y de los ensayos. Para valorar su consulta, indíquenos:</p>
      <ul class="filas">
        <li><strong>Material</strong><span>Grado o especificación (p. ej. ASTM A890 5A).</span></li>
        <li><strong>Plano</strong><span>PDF, STEP o DWG, con su revisión.</span></li>
        <li><strong>Cantidades</strong><span>Unidades y calendario de entregas previsto.</span></li>
        <li><strong>Ensayos</strong><span>Ensayos y documentación de calidad requeridos.</span></li>
        <li><strong>Plazo</strong><span>Fecha de necesidad de las piezas.</span></li>
      </ul>
      <div class="actions"><a class="btn" href="#consulta">Solicitar oferta</a></div>
    </div>
    <!-- FOTO: voluta en superdúplex 5A -->
    {fig('m-voluta-5a-v2.webp', 'Voluta de acero superdúplex 5A preparada para la prueba hidrostática', 960, 1200, 'Voluta en superdúplex 5A, preparada para la prueba hidrostática.')}
  </div>
</section>
<section class="sec" id="consulta" aria-labelledby="t-cons">
  <div class="wrap">
    <div class="head">
      <p class="label">Consulta de material</p>
      <h2 class="title" id="t-cons">Consulta técnica de materiales.</h2>
      <p class="text">Adjunte el plano y la especificación del material.</p>
    </div>
    <div class="contact">
{FORM}
      <div class="aside"><address class="aside__dir">info@amlcentrifugal.com<br>+34 948 46 16 03</address></div>
    </div>
  </div>
</section>
'''
open(R + 'v10-materiales.html', 'w', encoding='utf-8').write(doc('materiales', 'Materiales · AML Centrifugal Casting',
    'Mecanizado de aceros fundidos al carbono, inoxidables, dúplex y superdúplex: grados ASTM y equivalentes EN.', MAT, cta=False))

# ================================================================== CONTACTO
CON = cab('stand.webp', 'stand de AML en feria', '50% 40%', 'Contacto', 'Contacto',
          'Contacto.', 'Solicitudes de oferta, consultas técnicas, proveedores y transporte.')
CON += f'''<section class="sec" id="ferias" aria-labelledby="t-fer">
  <div class="wrap">
    <div class="head" style="max-width: none">
      <p class="label">Ferias</p>
      <h2 class="title" id="t-fer">Próximas ferias.</h2>
      <p class="text">Estas son las próximas ferias en las que estaremos. Si va a asistir, solicite una reunión con el formulario y le reservaremos un tiempo en nuestro stand.</p>
      {TABLA_FERIAS}
      <div class="actions"><a class="btn" href="#formulario">Solicitar reunión</a></div>
    </div>
  </div>
</section>
<section class="sec sec--alt" id="formulario" aria-labelledby="t-form">
  <div class="wrap">
    <div class="head">
      <p class="label">Formulario</p>
      <h2 class="title" id="t-form">Formulario de contacto.</h2>
      <p class="text">Adjunte el plano con su revisión y la especificación de material y ensayos. Respondemos con la viabilidad técnica y el plazo.</p>
      <div class="actions"><a class="link" href="mailto:info@amlcentrifugal.com">info@amlcentrifugal.com</a><a class="link" href="tel:+34948461603">+34 948 46 16 03</a></div>
    </div>
    <div class="contact">
{FORM}
{ASIDE}    </div>
  </div>
</section>
'''
open(R + 'v10-contacto.html', 'w', encoding='utf-8').write(doc('contacto', 'Contacto · AML Centrifugal Casting',
    'Contacto de AML Centrifugal Casting en Lecumberri: solicitudes de oferta, consultas técnicas, proveedores y transporte.', CON, cta=False))
print('ok')
