/* Transición de carga entre páginas · AML Centrifugal Casting
   Al pulsar un enlace interno: fondo claro + círculo de ondas AML que se despliega de 0° a 360°.
   Al llegar a la nueva página: el círculo completo se desvanece en cuanto la página está dibujada. */
(function () {
  var CLAVE = 'aml-transicion';
  var DURACION = 700;      // ms del giro de 0° a 360°
  var reducido = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var html = document.documentElement;

  var css = [
    '@property --aml-ang{syntax:"<angle>";inherits:false;initial-value:0deg}',
    '#aml-velo{position:fixed;inset:0;z-index:2147483000;display:flex;align-items:center;justify-content:center;',
    'background:#F4F6F5;opacity:0;visibility:hidden;pointer-events:none;transition:opacity .18s ease,visibility 0s linear .18s}',
    '#aml-velo::before{content:"";position:absolute;left:50%;top:50%;width:220px;height:220px;margin:-110px 0 0 -110px;border-radius:50%;',
    'background:radial-gradient(circle,rgba(1,31,103,.13) 0%,rgba(1,31,103,.05) 38%,transparent 68%);animation:aml-halo 1.6s ease-in-out infinite}',
    '@keyframes aml-halo{0%,100%{transform:scale(.85);opacity:.7}50%{transform:scale(1.08);opacity:1}}',
    '#aml-velo svg{position:relative;width:64px;height:64px;display:block;--aml-ang:0deg;',
    '-webkit-mask-image:conic-gradient(from 0deg,#000 var(--aml-ang),transparent var(--aml-ang));',
    'mask-image:conic-gradient(from 0deg,#000 var(--aml-ang),transparent var(--aml-ang))}',
    'html.aml-sale #aml-velo,html.aml-entra #aml-velo{opacity:1;visibility:visible;pointer-events:auto;transition:opacity .18s ease}',
    'html.aml-sale #aml-velo svg{animation:aml-giro ' + DURACION + 'ms cubic-bezier(.65,0,.35,1) forwards}',
    'html.aml-entra #aml-velo svg{--aml-ang:360deg}',
    'html.aml-fuera #aml-velo{transition:opacity .35s ease,visibility 0s linear .35s}',
    '@keyframes aml-giro{from{--aml-ang:0deg}to{--aml-ang:360deg}}',
    '@media (prefers-reduced-motion: reduce){#aml-velo svg{--aml-ang:360deg!important;animation:none!important}#aml-velo::before{animation:none}}'
  ].join('');

  // Círculo completo de ondas del logo: núcleo + tres anillos
  var svg = '<svg viewBox="-100 -100 200 200" aria-hidden="true">' +
    '<circle r="42.83" fill="#011F67"></circle>' +
    '<circle r="62.08" fill="none" stroke="#011F67" stroke-width="6.22"></circle>' +
    '<circle r="75.93" fill="none" stroke="#011F67" stroke-width="10.64"></circle>' +
    '<circle r="96.08" fill="none" stroke="#011F67" stroke-width="7.85"></circle></svg>';

  var estilo = document.createElement('style');
  estilo.textContent = css;
  document.head.appendChild(estilo);

  var velo = document.createElement('div');
  velo.id = 'aml-velo';
  velo.setAttribute('aria-hidden', 'true');
  velo.innerHTML = svg;
  html.appendChild(velo);

  // ---------- Llegada ----------
  var llegando = false;
  try { llegando = sessionStorage.getItem(CLAVE) === '1'; sessionStorage.removeItem(CLAVE); } catch (e) {}
  if (llegando) {
    html.classList.add('aml-entra');
    var quitar = function () {
      html.classList.add('aml-fuera');
      html.classList.remove('aml-entra');
      setTimeout(function () { html.classList.remove('aml-fuera'); }, 380);
    };
    var inicio = Date.now();
    var esperar = function () {
      var listo = document.body && document.body.querySelector('header, main, section');
      if (listo || Date.now() - inicio > 2500) {
        requestAnimationFrame(function () { requestAnimationFrame(quitar); });
      } else {
        setTimeout(esperar, 40);
      }
    };
    esperar();
  }

  // ---------- Salida ----------
  function esInterno(a, ev) {
    if (!a || ev.defaultPrevented || ev.button !== 0) return false;
    if (ev.metaKey || ev.ctrlKey || ev.shiftKey || ev.altKey) return false;
    if (a.target && a.target !== '_self') return false;
    if (a.hasAttribute('download')) return false;
    var href = a.getAttribute('href');
    if (!href || href.charAt(0) === '#' || /^(mailto:|tel:|javascript:)/i.test(href)) return false;
    var url = new URL(a.href, location.href);
    if (url.origin !== location.origin) return false;
    // mismo documento con ancla: desplazamiento normal, sin transición
    if (url.pathname === location.pathname && url.search === location.search) return false;
    return url;
  }

  document.addEventListener('click', function (ev) {
    var a = ev.target.closest ? ev.target.closest('a[href]') : null;
    var url = esInterno(a, ev);
    if (!url) return;
    ev.preventDefault();
    try { sessionStorage.setItem(CLAVE, '1'); } catch (e) {}
    html.classList.remove('aml-entra', 'aml-fuera');
    html.classList.add('aml-sale');
    setTimeout(function () { location.href = url.href; }, reducido ? 120 : DURACION + 40);
  });

  // Volver con el botón "atrás" (página restaurada de la caché): quitar el velo
  window.addEventListener('pageshow', function (ev) {
    if (ev.persisted) html.classList.remove('aml-sale', 'aml-entra', 'aml-fuera');
  });
})();
