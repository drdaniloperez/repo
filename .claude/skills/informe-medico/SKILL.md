---
name: informe-medico
description: Redacta documentos médicos de Danilo (informes médicos, ecosonogramas, informes de hospitalización, extensión de hospitalización, procedimientos quirúrgicos, constancias, referencias, récipes) copiando SU formato y estilo, a partir de los datos positivos que él dicte, y le pregunta lo que falta (medidas, hallazgos, procedimientos, diagnósticos omitidos). Si envía fotos de la pantalla del ecosonógrafo, las recorta a la medida exacta de la pantalla, las ordena, extrae las medidas y arma el informe con las imágenes. Úsala cuando pida "hazme un informe", "redacta un eco", "informe de hospitalización", "extensión", "informe operatorio", dicte datos de un paciente o mande fotos de un eco. También para "aprende mis formatos" / analizar sus ejemplos del disco Rodolfo SSD.
---

# Informe médico

Objetivo: que Danilo dicte solo lo positivo y relevante, y recibir un documento listo para firmar,
idéntico en estructura, vocabulario y tono a los que él redacta.

## 0. Antes de empezar
1. Mira si existe `formatos/<tipo>.md` aprendido de sus ejemplos reales (ver `formatos/README.md`).
   **Si existe, manda sobre las guías genéricas de `tipos/`**: orden de secciones, encabezados, frases
   de plantilla, mayúsculas, unidades, forma de la conclusión y del cierre/firma.
2. Si aún no hay formato aprendido para ese tipo, usa la guía de `tipos/` y avisa en una línea:
   "Uso formato genérico; cuando aprenda tus ejemplos de este tipo quedará idéntico al tuyo".
3. ¿Pide aprender o actualizar formatos? → sigue `aprender.md`.

## 1. Identificar el documento
Deduce el tipo por lo dictado; pregunta solo si es ambiguo.

| Tipo | Guía |
|---|---|
| Ecosonograma / ecografía / doppler (cualquier región) | `tipos/ecosonograma.md` |
| Informe médico (consulta, evolución, para seguro, para reposo, referencia) | `tipos/informe-medico.md` |
| Informe de hospitalización y de extensión de hospitalización | `tipos/hospitalizacion.md` |
| Informe de procedimiento quirúrgico / operatorio | `tipos/procedimiento-quirurgico.md` |
| Otro (constancia, récipe, reposo, carta) | El formato aprendido más parecido; si no hay, uno sobrio con los mismos datos de identificación y firma |

## 1b. Si envía fotos de la pantalla del ecosonógrafo
Sigue `imagenes-eco.md` de forma automática, sin esperar a que lo pida: recortar cada foto a la
medida exacta de la pantalla, verificar cada recorte, identificar y ordenar las imágenes, extraer las
medidas en pantalla y, con los datos del paciente, redactar el informe y armar el Word con las imágenes.

## 2. Extraer lo dictado
Ordena lo que Danilo dijo en: identificación del paciente, motivo/indicación, hallazgos positivos,
medidas, procedimientos, diagnósticos, plan/indicaciones. Interpreta abreviaturas y dictado por voz
(p. ej. "hache te a" = HTA, "de eme dos" = DM2, "por" = ×) y corrige errores obvios de transcripción.

## 3. Pedir lo que falta (paso obligatorio antes de redactar)
Compara lo dictado con la lista de "datos obligatorios" de la guía del tipo y con el formato aprendido.
Haz **una sola ronda de preguntas, numeradas y agrupadas**, en este orden:

1. **Faltantes obligatorios**: datos de identificación, fecha, medidas no dadas, tipo de intervención,
   técnica, anestesia, hallazgos operatorios, días de hospitalización, etc.
2. **Hallazgos posiblemente relacionados no mencionados**: lo que suele acompañar a lo dictado y conviene
   confirmar o descartar (p. ej. hígado graso → ¿esplenomegalia?, ¿vesícula?; litiasis renal → ¿hidronefrosis?,
   ¿grado?; nódulo tiroideo → ¿TI-RADS, vascularidad, adenopatías?).
3. **Diagnósticos posiblemente omitidos**: los que se desprenden de lo dictado pero no nombró
   (p. ej. medidas de hepatomegalia sin diagnóstico de hepatomegalia; IMC alto sin obesidad; Hb baja sin anemia).
4. **Datos opcionales con valor por defecto**: ofrece lo que pondrás si no responde
   ("si no me dices nada, pondré el resto del estudio como normal con su descripción habitual").

Reglas:
- Ofrece siempre opciones concretas para responder rápido (p. ej. "¿grado I, II o III?").
- Si Danilo dice "redáctalo así" o "lo demás normal", no vuelvas a preguntar: completa lo no dictado
  con su descripción **normal** habitual del formato aprendido.
- **Nunca inventes hallazgos patológicos, medidas ni datos del paciente.** Lo que no se sepa y sea
  necesario queda como `[___]` resaltado y se lista al final.
- Señala incongruencias (medida que contradice el diagnóstico, lateralidad distinta, fechas imposibles,
  edad/sexo incompatibles con el hallazgo).

## 4. Redactar
- Respeta el formato aprendido al pie de la letra: encabezado, orden, títulos en MAYÚSCULAS o no,
  frases fijas, viñetas, unidades (cm/mm), decimales, forma de "IMPRESIÓN DIAGNÓSTICA"/"CONCLUSIÓN",
  recomendaciones y bloque de firma.
- Lenguaje médico formal en español, tercera persona, frases que él usa (copia su vocabulario).
- Calcula lo calculable y dilo: volúmenes (largo × ancho × AP × 0,52), IMC, edad desde la fecha de
  nacimiento, días de hospitalización, edad gestacional/FPP, superficie corporal.
- Al final, fuera del documento: lista corta de los `[___]` pendientes y de lo que asumiste como normal.

## 5. Entregar
- Por defecto: el documento en texto, listo para copiar y pegar.
- Word: si hay un informe anterior suyo del mismo centro y tipo (ver `formatos/centros.md`), arma el
  documento con `scripts/informe_desde_modelo.py` (conserva membrete, tabla, firma y formato exactos).
  Pregunta el centro (Colinas, San José, PDVSA) si no lo dijo. Sin modelo, usa
  `scripts/armar_informe_docx.py`. Siempre en el directorio de trabajo o el scratchpad, nunca en el repo.
  Convierte a PDF/imagen (`soffice --headless --convert-to pdf`) y revisa la página antes de entregar.
- **Privacidad**: los informes con datos de pacientes nunca se guardan ni se suben a este repositorio.
  En el repo solo van plantillas anonimizadas.

## 6. Mejorar con el uso
Si Danilo corrige algo de estilo ("yo no pongo eso así", "siempre escribo…"), actualiza el
`formatos/<tipo>.md` correspondiente (sin datos de pacientes) y súbelo al cerebro (commit + push, ver `CLAUDE.md`).
