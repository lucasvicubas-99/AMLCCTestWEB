/* Transición entre páginas · v9 (menú lateral)
   Al salir: el menú lateral blanco se extiende hasta el borde derecho y, ya a pantalla completa,
   el círculo de ondas AML se despliega de 0° a 360°. Duración total igual que antes: 700 ms.
   Al llegar: el panel vuelve a encogerse hasta el ancho del menú y desaparece sobre él. */
(function () {
  var CLAVE = 'aml-transicion-v9';
  var EXTENDER = 300;     // ms en que el menú cruza la pantalla
  var GIRO = 400;         // ms del despliegue del logo
  var TOTAL = EXTENDER + GIRO;
  var reducido = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var html = document.documentElement;
  var ease = 'cubic-bezier(.65,0,.35,1)';

  var css = [
    '@property --aml-ang{syntax:"<angle>";inherits:false;initial-value:0deg}',
    '#aml-velo{position:fixed;top:0;bottom:0;left:0;z-index:2147483000;width:var(--aml-ini,220px);overflow:hidden;',
    'display:flex;align-items:center;justify-content:center;background:#FFFFFF;border-right:1px solid #E5E5E5;',
    'visibility:hidden;pointer-events:none}',
    '@media (max-width:900px){#aml-velo{--aml-ini:0px}}',
    '#aml-velo::before{content:"";position:absolute;left:50%;top:50%;width:220px;height:220px;margin:-110px 0 0 -110px;border-radius:50%;',
    'background:radial-gradient(circle,rgba(1,31,103,.10) 0%,rgba(1,31,103,.04) 38%,transparent 68%);opacity:0}',
    '#aml-velo svg{position:relative;flex:none;width:64px;height:64px;display:block;--aml-ang:0deg;',
    '-webkit-mask-image:conic-gradient(from 0deg,#000 var(--aml-ang),transparent var(--aml-ang));',
    'mask-image:conic-gradient(from 0deg,#000 var(--aml-ang),transparent var(--aml-ang))}',
    /* salida */
    'html.aml-sale #aml-velo{visibility:visible;pointer-events:auto;animation:aml-extiende ' + EXTENDER + 'ms ' + ease + ' forwards}',
    'html.aml-sale #aml-velo svg{animation:aml-giro ' + GIRO + 'ms ' + ease + ' ' + EXTENDER + 'ms forwards}',
    'html.aml-sale #aml-velo::before{animation:aml-luz .25s ease ' + EXTENDER + 'ms forwards}',
    '@keyframes aml-extiende{from{width:var(--aml-ini,220px)}to{width:100vw;border-right-color:transparent}}',
    '@keyframes aml-giro{from{--aml-ang:0deg}to{--aml-ang:360deg}}',
    '@keyframes aml-luz{to{opacity:1}}',
    /* llegada */
    'html.aml-entra #aml-velo{visibility:visible;width:100vw;border-right-color:transparent}',
    'html.aml-entra #aml-velo svg{--aml-ang:360deg}',
    'html.aml-entra #aml-velo::before{opacity:1}',
    'html.aml-fuera #aml-velo{visibility:visible;animation:aml-recoge .35s ' + ease + ' forwards}',
    'html.aml-fuera #aml-velo svg{--aml-ang:360deg;opacity:0;transition:opacity .15s ease}',
    '@keyframes aml-recoge{from{width:100vw;opacity:1}85%{opacity:1}to{width:var(--aml-ini,220px);opacity:0}}',
    '@media (prefers-reduced-motion: reduce){html.aml-sale #aml-velo,html.aml-fuera #aml-velo{animation:none!important;width:100vw}',
    '#aml-velo svg{--aml-ang:360deg!important;animation:none!important}}'
  ].join('');

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
      setTimeout(function () { html.classList.remove('aml-fuera'); }, reducido ? 0 : 380);
    };
    var inicio = Date.now();
    var esperar = function () {
      var listo = document.body && document.body.querySelector('main, section');
      if (listo || Date.now() - inicio > 2500) requestAnimationFrame(function () { requestAnimationFrame(quitar); });
      else setTimeout(esperar, 40);
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
    setTimeout(function () { location.href = url.href; }, reducido ? 120 : TOTAL + 40);
  });

  window.addEventListener('pageshow', function (ev) {
    if (ev.persisted) html.classList.remove('aml-sale', 'aml-entra', 'aml-fuera');
  });
})();
