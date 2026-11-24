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
