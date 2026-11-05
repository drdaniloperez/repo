# Fotos de la pantalla del ecosonógrafo → recorte, orden, medidas e informe

Danilo envía fotos tomadas con el teléfono de la pantalla del ecosonógrafo. Hay que:
recortarlas **a la medida exacta de la pantalla** (sin marco del monitor, mesa, pared ni reflejos
externos), ordenarlas, **leer las medidas** que aparecen en pantalla y armar el informe con las imágenes,
todo de forma automática en cuanto haya datos del paciente.

Scripts (requieren `pip install opencv-python-headless numpy pillow python-docx`; para .heic también `pillow-heif`):
- `scripts/recortar_pantalla.py` — detección de la pantalla, corrección de perspectiva, vista previa, ampliación de regiones.
- `scripts/informe_desde_modelo.py` — Word idéntico a un informe anterior del centro (membrete, firma) con los datos nuevos.
- `scripts/armar_informe_docx.py` — Word genérico con texto + imágenes en cuadrícula (si no hay modelo).

Trabaja en el scratchpad (o el directorio de trabajo), **nunca dentro del repo**: son datos de pacientes.

## 1. Recortar
```
python3 .claude/skills/informe-medico/scripts/recortar_pantalla.py recortar <fotos o carpeta> --salida <dir>/recortes [--aspecto 4:3]
```
- Usa `--aspecto` con la proporción de la pantalla del equipo si está en `formatos/eco-imagenes.md`
  (aprendida de sus informes); así todas las imágenes quedan con el mismo tamaño.
- **Verifica cada recorte mirándolo** (Read de la imagen). Correcto = se ve la pantalla completa
  (incluidos los rótulos, la escala y el recuadro de medidas en los bordes) y nada de lo que hay
  fuera de ella. Si quedan restos del marco: repite con `--margen 4..15`.
- Si un recorte está mal (o la confianza es < 0,75): abre `recortes/previa/<nombre>`, que tiene una
  cuadrícula con coordenadas, estima las 4 esquinas de la pantalla y repite solo esa foto con
  `--esquinas "x1,y1;x2,y2;x3,y3;x4,y4"` (conserva su número). Vuelve a verificar.

## 2. Identificar y ordenar
Para cada recorte determina órgano/estructura y corte usando, por este orden: el rótulo o
anotación en pantalla (p. ej. "LIVER", "RT KIDNEY", "TIROIDES LD"), el pictograma/body marker,
el preset del equipo, la anatomía visible y, por último, la hora de captura (EXIF).
Ordena según `formatos/eco-imagenes.md`. Ojo: el equipo de San José mide en mm (convertir a cm). Si no está aprendido, usa el orden anatómico habitual del estudio:
- Abdominal: hígado (LD, LI) → porta → vesícula → colédoco → páncreas → bazo → riñón derecho →
  riñón izquierdo → aorta/vejiga.
- Renal: riñón derecho (long./transv.) → riñón izquierdo → vejiga pre → vejiga post → próstata.
- Tiroides: lóbulo derecho (long./transv.) → istmo → lóbulo izquierdo → nódulos → adenopatías.
- Pélvico: útero (long./transv.) → endometrio → ovario derecho → ovario izquierdo → fondo de saco.
- Obstétrico: biometría (DBP/CC, CA, LF) → FCF/modo M → placenta → líquido amniótico → otras.
- Mamas: derecha por cuadrantes horarios → axila derecha → izquierda → axila izquierda.
Las imágenes repetidas o desenfocadas de la misma estructura: conserva la mejor y pregunta si descartar las demás.

## 3. Extraer las medidas
- Lee el recuadro de medidas de cada imagen (p. ej. `D1 14.2 cm`, `Dist`, `L/W/H`, `Vol`, `Area`,
  `FHR`, `BPD/HC/AC/FL` con su EG, `PSV/EDV/RI`). Si el texto es pequeño, amplíalo:
  `recortar_pantalla.py ampliar <recorte> --region 0.7,0.75,0.3,0.25 --factor 3 --salida zoom.png`
  (fracciones x,y,ancho,alto) y léelo.
- Asocia cada medida a la estructura medida (por los calipers +/× sobre la imagen y la numeración D1, D2…).
  Tres diámetros de una misma estructura → calcula el volumen (× 0,52) si el equipo no lo da.
- Convierte al formato de Danilo (coma decimal, cm o mm según su costumbre).
- Presenta la tabla **imagen → estructura → medida** y marca con ⚠ lo dudoso (dígito ilegible,
  medida que no corresponde a la estructura, valor fisiológicamente improbable). **Nunca adivines un dígito.**
- Señala lo que falta para el estudio según `tipos/ecosonograma.md` (p. ej. hay foto del bazo sin medir).

## 4. Redactar y armar
1. Con los datos del paciente y lo que dictó, sigue el flujo normal de `SKILL.md` (pasos 2–4): las
   medidas extraídas cuentan como datos dictados. Haz la ronda de preguntas incluyendo las medidas ⚠
   y las que faltan.
2. **Con modelo del centro** (preferido): escribe `datos.json` (ver cabecera de
   `scripts/informe_desde_modelo.py`: titulo, px, ci, edad, fecha, introduccion, hallazgos [[etiqueta, texto]],
   conclusion [...], despues_conclusion, imagenes en orden, columnas, ancho_imagen_cm) y ejecuta
   `python3 .claude/skills/informe-medico/scripts/informe_desde_modelo.py --modelo <informe anterior del centro>.docx --datos datos.json --salida "<nuevo>.docx"`.
   Revisa el resultado convertido a PDF. Si no hay modelo, sigue con los pasos 2b–4.
2b. Escribe el texto en marcado sencillo (`# título`, `## sección`, `**negrita**`, `- viñeta`, y
   `[[IMAGENES]]` donde van las imágenes según su formato).
3. Crea el manifiesto `[{"ruta": "...", "pie": "Hígado - longitudinal"}, …]` en el orden decidido.
4. Arma el Word:
   ```
   python3 .claude/skills/informe-medico/scripts/armar_informe_docx.py --texto informe.md --manifiesto imagenes.json \
       --salida "<Tipo de eco> - <Paciente> - <fecha>.docx" [--plantilla <membrete.docx>] [--columnas N] [--imagenes-en pagina-nueva] [--pies]
   ```
   Columnas, tamaño, posición y pies según `formatos/eco-imagenes.md`. Si hay PDF/imagen de
   control, conviértelo (`soffice --headless --convert-to pdf`) y revisa visualmente la página.
5. Entrega el .docx (SendUserFile si está disponible) más el texto, la tabla de medidas y los pendientes.
