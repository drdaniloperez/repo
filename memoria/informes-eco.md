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

## Bloque de firma (pedido por Danilo el 2026-11-08)
- "Dr. Danilo Pérez T." / "CIRUJANO PEDIATRA-ECOGRAFISTA" **pegadito**: interlineado sencillo, espacio
  antes/después 0, centrado, para que no ocupe espacio. Si no hay imagen de firma/sello ni MPPS/CMA/RIF, solo esas dos líneas.
- La imagen de firma y sello va justo después de la conclusión (la tomará de un eco suyo que enviará).

## Fotos del MediSono P12Exp (Policlínica San José), aprendido 2026-11-08
- Foto vertical 2252×4000; la pantalla ocupa todo el ancho y se sale por la izquierda. El recorte automático dejó el marco
  blanco/base del monitor en la mitad. Lo que funcionó: recorte recto por foto (x de 0 al borde derecho de la pantalla,
  y desde ~10 px sobre la barra azul "POLICLINICA SAN JOSE" hasta justo bajo la fila de miniaturas), y luego igualar.
- Medidas arriba a la derecha en **mm** ("1 D: 81.88 mm") → cm truncando (8.1). El bazo suele medirse en dos tramos
  (3 + 4) → sumar para el eje largo. Rótulos en pantalla: H, VB, P, RD, RI, B, "APENDICE CECAL".

## Mismo flujo en todos los centros (Danilo, 2026-11-08)
El flujo del eco de San José (recorte verificado de cada foto, tabla pantalla → informe, su redacción literal, modelo .docx
del centro con firma y sello, firma compacta, imágenes iguales, vista previa y PDF) es **el mismo para el Centro de
Especialidades Médicas Colina** (y los demás centros). Diferencias de Colina: logo COLINA a la izquierda con el título a
su derecha, equipo Mindray portátil que mide en **cm** ("1 Distancia 5.06 cm", abajo a la derecha) y fotos tomadas de cerca de
la laptop (≈ la mitad trae marco o pared → esquinas manuales). Pedirle un eco anterior suyo de Colina en .docx como modelo
si no lo tengo en la sesión.

## Ejemplos aprobados (usar como referencia)
- **Eco abdominal con apendicitis aguda** (aprobado 2026-11-07): mismo texto en San José y en Colina, cambiando solo
  el logo/membrete de la institución. Plantilla: `formatos/plantillas/eco-abdominal-apendicitis.json`; detalle y
  ejemplo en `formatos/eco-abdominal.md` → "Ejemplo APROBADO". 8 imágenes (6 órganos + 2 del apéndice).

- **Eco abdominopélvico de mujer** (aprobado 2026-11-08): hígado graso, vesícula con barro biliar, litiasis renal
  bilateral y enteritis moderada con abundante gas. Ejemplo y lecciones en `formatos/eco-abdominopelvico.md` →
  "Ejemplo APROBADO". 10 imágenes (H, VB, P, RD, RI, B, COLITIS, V/U, OD, OI).

- **Eco vesical con descripción ampliada** (aprobado 2026-11-08): forma, capacidad, contornos, paredes, trabeculaciones/
  divertículos, contenido (detritos, litos, coágulos, masas), piso vesical, meatos y uréteres distales, medidas en 3 ejes y
  volumen. Texto y valores de referencia en `formatos/eco-vesical.md` → "Descripción ampliada". Usarla siempre en vesicales.

- **Eco tiroideo** (aprobados 2026-11-08): rótulos LTD / LTI / I (istmo); en la foto de lóbulos los números 1-3 y 4-6
  van al lóbulo cuyo rótulo está debajo (mirar el rótulo, no el lado de la pantalla), 7 = istmo. En tiroides las medidas van
  con 2 decimales (no truncar) e istmo en cm. Quistes simples: "Se evidencian quistes simples de paredes delgadas, de
  contenido anecoico… de bordes definidos, que no deforman anatomía del órgano" + doppler "con flujo doppler positivo con
  flujo laminar sin alteraciones" → `Tirads 2`. Hashimoto: patrón pseudo nodular difuso, bordes irregulares poco definidos,
  parénquima heterogéneo hipoecogénico moteado con septos ecogénicos "en manchas de jirafa", doppler con aumento difuso de
  la vascularidad; ganglios en "Nota:" (dispersos bilaterales < 1 cm, ovalados, hilio graso conservado) → `Tirads 3`.
  Si pide la imagen de la tiroides "más grande": 14 cm de ancho sola arriba en la página de imágenes, el resto debajo.
- **Eco de mama** (aprobado 2026-11-08): fotos panorámicas "MAMA DER"/"MAMA IZQ" (4 cuadrantes) + foto de cada lesión con
  rótulo y hora ("QUISTE MAMARIO HORA 12"). Varios quistes: "se evidencian 2 quistes simples… Quiste 1: a x b cm Quiste 2: …".
  Ganglio axilar reactivo: ovalado, hilio graso conservado, no doloroso. `Birads 2.` + (si lo pide) "Se sugiere realización
  de mamografía complementaria." Orden de imágenes: panorámica der → lesión der → panorámica izq → lesión izq.
- **Varios estudios del mismo paciente** (renal + vesical + prostático): un informe y un PDF por estudio, cada uno con sus
  fotos. Prostático: medidas y volumen tomados del cálculo del equipo ("Vol 70.94 cm³" → 70.9), IPP de otra foto; grado III
  si > 60 cm³. Renal con edema: "con edema perirenal leve" en cada riñón ("perineal" dictado = perirrenal).

- **Partes blandas: hernia inguinal pediátrica sin imágenes** (2026-11-12, PDVSA): introducción "… examinando región
  inguinal bilateral:", un párrafo por lado ("Region inguinal derecha:" con Valsalva, protrusión de epiplón por anillo
  permeable que no alcanza bolsa escrotal y regresa a cavidad; lado sano con anillo no permeable; testículos en bolsa) →
  `1) Hernia inguinal derecha no complicada.` `2) Región inguinal izquierda sin hallazgos patológicos.` Sin imágenes cabe en
  una página; dejar un párrafo de separación antes de la firma para que la imagen del sello no toque la conclusión.
- **Hernia umbilical hallada en un eco abdominal** (2026-11-12): no como conclusión aparte sino en una `Nota:` tras la
  conclusión: "se explora pared abdominal encontrando hernia umbilical no complicada, con defecto aponeurótico de [X] cm.
  Se sugiere valoración por cirugía pediátrica."

- **Tiroides pequeña / tiroiditis crónica atrófica en obeso** (aprobado 2026-11-13): lóbulos "de tamaño disminuido, de
  bordes regulares poco definidos, parénquima heterogéneo, discretamente hipoecogénico, de ecogenicidad similar a la
  musculatura pretiroidea… sin quistes ni nódulos"; `Nota:` "glándula sin efecto compresivo, tráquea central, sin extensión
  retroesternal. Estudio con limitación técnica por abundante tejido adiposo cervical en paciente con obesidad mórbida."
  (no "hábito corporal"). Conclusión: "Glándula tiroidea de tamaño disminuido con parénquima heterogéneo, hallazgos
  ecográficos sugestivos de tiroiditis crónica, a correlacionar con perfil tiroideo (TSH, T4 libre, anticuerpos anti-TPO)."
  + "Sin signos de bocio ni compresión de la vía aérea." (útil si hay apnea del sueño) → `Tirads 1`. Sin longitud no hay volumen.

## Rótulos en la pantalla (dictado por Danilo el 2026-11-08) — identificar cada foto por su rótulo
| Rótulo | Órgano | Medidas que toma en esa foto |
|---|---|---|
| **H** | Hígado | 1 = LD, 2 = LI |
| **VB** | Vesícula biliar | long × transv |
| **P** | Páncreas | cabeza, cuerpo, cola (1, 2, 3) |
| **RD** | Riñón derecho | long × transv (+ litos: medidas extra, p. ej. "3 Distancia 0.55 cm") |
| **RI** | Riñón izquierdo | long × transv (+ litos) |
| **B** | Bazo | long × transv (a veces en dos tramos → sumar) |
| **COLITIS** | Intestino | siempre pone una imagen rotulada "COLITIS" cuando hay colitis → va en Intestino y en la conclusión |
| **V** | Vejiga | 3 diámetros → volumen = × 0.52 (± grosor de pared) |
| APENDICE CECAL | Apéndice | grosor/diámetro (San José) |
Tomar SIEMPRE las medidas de los órganos de estas fotos. Si falta la foto de un órgano del informe (p. ej. no hay "B"),
avisar y pedirla; no inventar la medida. Sin foto "COLITIS" → intestino normal salvo que lo dicte.

## Flujo que funcionó
0. Si no tengo en la sesión el modelo .docx del centro (Colina, San José…), pedírselo **al empezar**, junto con las fotos
   (los modelos no se guardan en el repo público; ver `memoria/aprendizajes.md`).
1. Danilo manda el informe (.docx) y las fotos del teléfono → recortar todas, **revisar cada recorte a la
   vista** y corregir con esquinas manuales los que traigan marco o pared (≈ la mitad en fotos de cerca de
   la laptop Mindray).
2. Leer las medidas de cada pantalla y hacer una **tabla órgano → pantalla → informe**; señalar las que no
   coinciden (los informes suelen partir de una plantilla anterior y quedan medidas viejas).
3. Entregar el informe con imágenes y una versión con las medidas de pantalla; preguntar lo dudoso en una
   sola lista numerada con opciones. Si responde "sí" a una pregunta con dos opciones, aplicar la primera y
   no inventar calificativos (p. ej. escribir el grosor medido en vez de "delgada/engrosada").
4. **Mostrar siempre la vista previa** (páginas como imagen).
5. **Entregar en PDF** (pedido por Danilo el 2026-11-07), y el Word solo si quiere editarlo:
   `soffice --headless --convert-to pdf "<informe>.docx"`. La fuente Carlito sustituye a Calibri con las mismas
   medidas, así que el PDF queda igual que el Word (comprobar con `pdffonts`). Nombre:
   "<Paciente> - Eco <tipo> - <fecha>.pdf". Un abdominal con 8 imágenes pesa ≈ 1 MB, apto para WhatsApp.

## Revisiones que siempre hay que hacer
- **Primero vista previa, PDF después** (Danilo, 2026-11-14): enviar solo las páginas como imagen para que corrija;
  el PDF final únicamente cuando diga "sí"/apruebe.
- **Abdominopélvico**: siempre incluir Vejiga y Útero y ovarios (anexos pélvicos), aunque no los dicte.
- Colina tiene **dos equipos**: la laptop Mindray (C5-2s) y un **Mindray Consona N9** (SC5-1N, pantalla gris oscura,
  medidas en recuadro abajo a la derecha, en cm). En el mismo estudio pueden venir fotos de ambos.
- **Riñones: parénquima HETEROGÉNEO por defecto** (Danilo, 2026-11-13) en ambos riñones, salvo que dicte otra cosa.
- **Fecha**: si Danilo dice que todos los informes del día son de una fecha (p. ej. la del estudio), usarla en todos;
  coincide con la fecha de la pantalla (formato AAAAMMDD en el código del estudio).
- **Nombre**: el que dicta Danilo manda sobre la grafía de la pantalla; si solo da el apellido, tomar el nombre de la pantalla.
- Lo que no está en las fotos ni dictado (lito sin medir, ganglio sin foto, medidas de próstata): preguntar en una sola ronda
  y, si quiere avanzar, entregar borrador con [___] y completar cuando responda.
- Al final de la jornada puede pedir "borrar todo y dejar solo los finales": dejar PDF+Word finales en una carpeta
  `informes-<fecha>` y reenviar todos los PDF finales juntos.
- **No añadir "Se sugiere valoración por…" si Danilo no la dicta** (2026-11-08: pidió quitar una de urología
  pediátrica que puse por defecto). Por defecto el cierre es solo "Resto de estructuras dentro de límites normales."
- Medidas del texto vs. pantalla; diagnóstico coherente con la medida (p. ej. LD 15 cm sí es hepatomegalia).
- **Vesícula según el diagnóstico** (Danilo, 2026-11-08): por defecto "plenificada, de paredes delgadas". Solo se escribe
  "de paredes engrosadas" (± distendida) cuando hay **barro biliar o litos** en su interior, y entonces van también en el
  párrafo y en la conclusión. Si el borrador dice "engrosadas" sin barro ni litos → preguntar o poner la frase normal.
- Órganos fotografiados que no tienen párrafo (p. ej. vejiga) y rótulos en pantalla que no están en la
  conclusión (p. ej. "COLITIS" → "Colitis moderada").
- Unidades en la conclusión ("RD: 0.4 cm, RI: 0.5 cm"), numeración seguida.
- Calipers en varios tramos (p. ej. bazo 5.70 + 6.84): el eje largo es la suma (12.5 cm).
- Volumen vesical = L × T × AP × 0.52; decimales de pantalla a 1 decimal truncando (10.26 → 10.2).

## Problemas técnicos ya resueltos (no repetir)
- (2026-11-08) Abdominopélvico con útero y ovarios: el texto es largo y la firma se pasaba a la página 2. Bajar el
  espacio después de cada párrafo de hallazgos a 2 pt y quitar el párrafo vacío antes de la conclusión: firma y RIF
  quedan en la página 1. Comprobar con `pdftotext -f 1 -l 1` que "RIF" está en la página 1.
- Rótulos de pelvis en pantalla: U = útero, OD / OI = ovario derecho / izquierdo (orden de imágenes: … COLITIS → V/U → OD → OI).
- Imágenes de 8.3 cm en 2 columnas no caben en carta → Word recorta el borde derecho y se pierden las
  medidas. Usar 7.9 cm.
- La firma/sello está anclada a la página: si el texto crece, tapa la conclusión → anclarla al párrafo
  previo a "Dr. …".
- Al editar un .docx suyo, cambiar solo los fragmentos de texto con números para no perder el formato.
- (2026-11-08) `informe_desde_modelo.py` ya corrige solo (probado con un abdominal de San José): imágenes ≤ 7.6 cm
  (las celdas miden 8.26 cm y a 7.9 se cortaba la columna de medidas), todas igualadas de tamaño, borra las imágenes
  viejas del modelo (antes quedaban las de < 7 cm de ancho), firma/sello en línea y centrada, bloque de firma compacto.
- Danilo puede mandar como "modelo" su propio informe ya redactado del paciente: sus hallazgos de texto (p. ej. detalles del
  apéndice, vejiga) mandan; sus medidas suelen ser de plantilla vieja → usar las de pantalla y señalar las diferencias.
