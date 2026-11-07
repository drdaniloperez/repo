# Informes ecográficos — lo que le gusta a Danilo y lecciones aprendidas

Se usa con la skill `informe-medico` (detalle técnico en `.claude/skills/informe-medico/`).
Nunca guardar aquí datos de pacientes (el repo es público).

## Cómo le gustan las imágenes (aprobado por Danilo el 2026-11-07)
- **Todas del mismo tamaño y uniformes**, tal como se le mostraron: 2 columnas, ~7.9 cm de ancho cada una,
  después del bloque de firma (6 por página; si son más, siguen en la página siguiente).
- **Solo la pantalla del ecógrafo**: sin marco del monitor/laptop, pared ni teclado. Encabezado (centro,
  nombre del paciente) y recuadro de medidas **completos y legibles**.
- Para igualar tamaños: rellenar con el tono oscuro de la pantalla. **Nunca estirar** (deforma la anatomía)
  ni recortar más (se pierden medidas).
- Orden abdominal: hígado → vesícula → páncreas → riñón derecho → riñón izquierdo → bazo → intestino
  (colitis) → vejiga (→ útero/ovarios o próstata).

## Flujo que funcionó
1. Danilo manda el informe (.docx) y las fotos del teléfono → recortar todas, **revisar cada recorte a la
   vista** y corregir con esquinas manuales los que traigan marco o pared (≈ la mitad en fotos de cerca de
   la laptop Mindray).
2. Leer las medidas de cada pantalla y hacer una **tabla órgano → pantalla → informe**; señalar las que no
   coinciden (los informes suelen partir de una plantilla anterior y quedan medidas viejas).
3. Entregar el informe con imágenes y una versión con las medidas de pantalla; preguntar lo dudoso en una
   sola lista numerada con opciones. Si responde "sí" a una pregunta con dos opciones, aplicar la primera y
   no inventar calificativos (p. ej. escribir el grosor medido en vez de "delgada/engrosada").
4. **Mostrar siempre la vista previa** (páginas como imagen) además de mandar el Word.

## Revisiones que siempre hay que hacer
- Medidas del texto vs. pantalla; diagnóstico coherente con la medida (p. ej. LD 15 cm sí es hepatomegalia).
- Órganos fotografiados que no tienen párrafo (p. ej. vejiga) y rótulos en pantalla que no están en la
  conclusión (p. ej. "COLITIS" → "Colitis moderada").
- Unidades en la conclusión ("RD: 0.4 cm, RI: 0.5 cm"), numeración seguida.
- Calipers en varios tramos (p. ej. bazo 5.70 + 6.84): el eje largo es la suma (12.5 cm).
- Volumen vesical = L × T × AP × 0.52; decimales de pantalla a 1 decimal truncando (10.26 → 10.2).

## Problemas técnicos ya resueltos (no repetir)
- Imágenes de 8.3 cm en 2 columnas no caben en carta → Word recorta el borde derecho y se pierden las
  medidas. Usar 7.9 cm.
- La firma/sello está anclada a la página: si el texto crece, tapa la conclusión → anclarla al párrafo
  previo a "Dr. …".
- Al editar un .docx suyo, cambiar solo los fragmentos de texto con números para no perder el formato.
