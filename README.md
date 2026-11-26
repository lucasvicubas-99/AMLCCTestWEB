# Web AML Centrifugal Casting

Web corporativa de AML Centrifugal Casting, S.L. Se publica con GitHub Pages en
https://lucasvicubas-99.github.io/AMLCCTestWEB/

La versión buena es la **v10** (`v10.html` y `v10-*.html`). Las demás (v6, v8, v9) se guardan como referencia.

## Páginas de la v10

- `v10.html`: inicio
- `v10-capacidades.html`: fresado, torneado, mandrinado y soldadura
- `v10-calidad.html`: ensayos, control dimensional y sistema de calidad
- `v10-sectores.html`: sectores, con fotos y piezas habituales
- `v10-materiales.html`: familias de materiales y buscador
- `v10-contacto.html`: ferias, formulario y carga y descarga

## Cómo está hecha

Las páginas de la v10 **no se editan a mano**: las genera un script de Python a partir de las fuentes.

- `fuentes/gen_v10.py`: el generador. Aquí están los textos, las listas de fotos, el CSS y el JavaScript.
- `fuentes/v9_base.css` y `fuentes/v9_parts.json`: piezas comunes que usa el generador.
- `fuentes/anteriores/`: los generadores de las versiones anteriores, solo como referencia.
- `assets/`: fotos (WebP), vídeo de portada, iconos y los `v10.css` y `v10.js` que crea el generador.

## Trabajar desde otro ordenador

Hace falta [Git](https://git-scm.com/) y [Python 3](https://www.python.org/) (no hay que instalar nada más).

1. Clonar el repositorio (solo la primera vez):

   ```
   git clone https://github.com/lucasvicubas-99/AMLCCTestWEB.git
   cd AMLCCTestWEB
   ```

2. Antes de empezar, traer los últimos cambios:

   ```
   git pull
   ```

3. Cambiar lo que haga falta en `fuentes/gen_v10.py` (o añadir fotos a `assets/`) y regenerar las páginas:

   ```
   python fuentes/gen_v10.py
   ```

4. Verlo en el navegador. Arrancar un servidor local y abrir http://localhost:8000/v10.html

   ```
   python -m http.server 8000
   ```

5. Guardar y subir los cambios:

   ```
   git add -A
   git commit -m "Qué he cambiado"
   git push
   ```

GitHub Pages publica los cambios en unos minutos. Si no se ven, recargar con Ctrl+F5.

## Pendiente

- Formulario conectado a un correo (Formspree o similar).
- Versiones en inglés, alemán, italiano y francés, con idioma automático según el navegador.
- Textos legales.
- Stand de DSEI Germany 2027.
