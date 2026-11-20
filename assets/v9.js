(function () {
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

  // Buscador de materiales
  document.querySelectorAll('.buscador').forEach(function (b) {
    var tabla = b.parentElement.querySelector('table.js-filtrable'); if (!tabla) return;
    var input = b.querySelector('.js-buscar'), chips = b.querySelectorAll('.chip'), res = b.querySelector('.buscador__res');
    var norm = function (t) { return String(t).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, ''); };
    var filas = [], fam = '', cabFam = null;
    tabla.querySelectorAll('tbody tr').forEach(function (tr) {
      if (tr.classList.contains('fam')) { fam = norm(tr.textContent.trim()); cabFam = tr; tr._hijos = []; return; }
      var f = tr.cells.length > 4 ? norm(tr.cells[1].textContent) : fam;
      var base = Array.prototype.slice.call(tr.cells, 0, tr.cells.length > 4 ? 4 : 3).map(function (c) { return c.textContent; }).join(' ');
      var item = { tr: tr, fam: f, txt: norm(base + ' ' + f), cab: cabFam };
      if (cabFam) cabFam._hijos.push(item);
      filas.push(item);
    });
    var elegido = '';
    function encaja(it) {
      if (!elegido) return true;
      if (elegido === 'carbono') return it.fam.indexOf('carbono') > -1;
      if (elegido === 'inoxidable') return it.fam.indexOf('inoxidable') > -1;
      if (elegido === 'duplex') return it.fam === 'duplex';
      return it.fam === 'superduplex';
    }
    function filtra() {
      var q = norm(input.value.trim()), n = 0;
      filas.forEach(function (it) { var ok = encaja(it) && (!q || it.txt.indexOf(q) > -1); it.tr.hidden = !ok; if (ok) n++; });
      tabla.querySelectorAll('tbody tr.fam').forEach(function (c) { c.hidden = !c._hijos.some(function (it) { return !it.tr.hidden; }); });
      if (!q && !elegido) { res.textContent = ''; return; }
      if (n) res.textContent = n + (n === 1 ? ' grado coincide.' : ' grados coinciden.');
      else res.innerHTML = 'Ningún grado coincide. <a href="v9-materiales.html#otras">Consulte otras aleaciones</a>.';
    }
    input.addEventListener('input', filtra);
    chips.forEach(function (c) { c.addEventListener('click', function () {
      elegido = elegido === c.dataset.fam ? '' : c.dataset.fam;
      chips.forEach(function (x) { x.setAttribute('aria-pressed', x.dataset.fam === elegido ? 'true' : 'false'); });
      filtra();
    }); });
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
