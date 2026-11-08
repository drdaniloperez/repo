# Formato: Informe ecográfico ABDOMINAL (y variantes)

Aprendido de 30 informes reales (2025–2026) de Centro de Especialidades Médicas Colina, Policlínica San José y
Hospital Jesús Farías (PDVSA); ampliado (2026-11-07, disco) con 629 documentos `eco-abdominal` del disco
(01/2024 – 10/2026), instituciones: Colina (360), San José (261), sin logo reconocido (8); **ninguno de PDVSA**
(de PDVSA en el disco solo hay 3 ecos renales/"abdominal con énfasis renal"). 440 adultos, 158 niños de 1–17 años
y 30 menores de 1 año (desde 2 días de vida). Abdominopélvico y pélvico tienen ahora su propio formato:
`eco-abdominopelvico.md` y `eco-pelvico.md`. Variantes de título:
- `INFORME ECOGRÁFICO ABDOMINAL`
- `INFORME ECOGRÁFICO ABDOMINAL CON ÉNFASIS RENAL` (suele ser pediátrico; añade Vejiga)
- `INFORME ECOGRÁFICO ABDOMINOPELVICO` (añade Vejiga y Útero y ovarios / Próstata)
- `INFORME ECOGRÁFICO RENAL` (solo riñones ± vejiga)

El membrete, el título, la tabla de identificación y la firma salen del modelo `.docx` del centro
(ver `centros.md`). Aquí va el **texto**.

## Estructura
```
INFORME ECOGRÁFICO <TIPO>
| Px: <Nombre Apellido> | Ci: <cédula con puntos, o "menor"> | Edad: <52 años / 18 meses / 1 año 5 meses> | Fecha: <dd/mm/aaaa> |

Se realiza estudio ecográfico en tiempo real con transductor convex de 3.5MHz en múltiples proyecciones, donde se evidencian los siguientes hallazgos:

Hígado: …
Vesícula Biliar: …
Páncreas: …
Riñón Derecho: …
Riñón Izquierdo: …
Bazo: …
Intestino: …
[Vejiga: …]
[Útero y ovarios: … | Próstata: …]

Conclusión:	1) …
		2) …
	[Resto de estructuras dentro de limites normales.]
[Se sugiere …]

<firma y bloque de firma del modelo>
<imágenes del eco>
```
- Cada órgano en un párrafo, justificado; la etiqueta ("Hígado:") en **negrita**. En el formato
  PDVSA y San José todo el párrafo va en negrita (lo da el modelo).
- "Conclusión:" en negrita, ítems numerados `1)`, `2)` en negrita, alineados con tabulaciones.
- Decimales con **punto** (12.9 cm). Medidas "long: X cm transv: Y cm".
- Las medidas de la pantalla del ecógrafo (2 decimales) se pasan con **1 decimal, truncando**
  (10.48 → 10.4; 4.78 → 4.7; 11.73 → 11.7). ⚠ confirmar con Danilo si trunca o redondea.
  (ampliado 2026-11-07, disco) En el disco **no hay evidencia** para decidirlo: los textos no traen la medida de
  pantalla y las imágenes de los .docx del disco están dañadas (CRC). Sí se ve que en 115 de 779 informes
  abdominales/pélvicos copia a veces la cifra de pantalla con **2 decimales** sin acortar ("5.16 cm", "0.45 cm",
  "0.33 cm"): 10 628 medidas con 1 decimal frente a 174 con 2. Coma decimal solo en 1 documento.

## Frases normales (adulto) — literales
- **Hígado:** forma, tamaño habitual con patrón granular fino, de medidas LD: [X] cm y LI: [Y] cm, limites bien definidos, parénquima heterogeneo, ecogenicidad conservada, sin presencia de lesiones focales o expansivas, imágenes de vasos visibles y vías biliares intrahepaticas sin alteraciones.
- **Vesícula Biliar:** tamaño y forma habitual plenificada de medidas long: [X] cm trans: [Y] cm, de paredes delgadas, conducto biliar de calibre adecuado, sin imágenes patológicas en su interior.
- **Páncreas:** de forma y configuración habitual sin liquido peripancreatico, con medidas de cabeza cuerpo y cola [A]cm x [B]cm x [C]cm
- **Riñón Derecho:** adecuadamente visible con movilidad respiratoria normal, de medidas long: [X] cm, transv: [Y] cm, de tamaño dentro del rango normal, parénquima heterogéneo, ecogenicidad conservada, sin presencia de microlitiasis, sin presencia de Pielocalectasia, conservando la relación médula corteza.
- **Riñón Izquierdo:** (igual que el derecho)
- **Bazo:** parénquima homogéneo, de medidas long: [X] cm. transv: [Y] cm, de tamaño normal, sin evidencia de lesiones focales o expansivas ni liquido periesplenico.
- **Intestino:** peristaltismo conservado, con presencia de gases, sin evidencia de líquido libre en cavidad, no se observan ganglios linfáticos aumentados de tamaño ni otras masas ocupantes de espacio patológicas, aorta y cava inferior sin alteraciones.
- **Vejiga:** plenificada, de paredes delgadas, de contenido anecoico, sin imágenes patológicas en su interior vol. aprox [N] cc
- **Útero y ovarios:** se evidencia útero en posición anteversión, de bordes regulares, miometrio heterogéneo, de medidas [A]cm x [B]cm, ovario derecho de forma ovalada, bordes bien definidos, de medidas [A] cm x [B] cm, parénquima heterogéneo. ovario izquierdo de forma ovalada, bordes bien definidos, de medidas [A]cm x [B]cm, parénquima heterogéneo.
- **Próstata** (en abdominopélvico de hombre): ver `eco-prostatico.md`.
- Variante corta del páncreas (pediátrico/adolescente): "de tamaño y forma acorde a edad, conducto pancreático no dilatado, sin líquido peripancretico."

## Frases normales (pediátrico) — literales
- **Hígado:** forma, tamaño acorde a edad con patrón granular fino, de medidas LD:[X] cm y LI:[Y] cm, limites bien definidos, parénquima heterogeneo, ecogenicidad conservada, imágenes de vasos  y vías biliares visibles sin dilataciones ni calcificaciones.
- **Vesícula Biliar:** tamaño y forma acorde a edad, plenificada de medidas long: [X] cm trans: [Y] cm, de paredes finas, conducto biliar de calibre adecuado, sin imágenes patologícas en su interior.
- **Páncreas:** de tamaño y forma acorde a edad, conducto pancreático no dilatado, sin líquido peripancretico.
- **Riñones:** "… de tamaño acorde a edad, parénquima homogéneo, ecogenicidad conservada, sin presencia de litiasis, sin Pielocalectasia, conservando la relación médula corteza. No se observan anomalías estructurales."
- **Bazo:** "… de tamaño acorde a edad, sin evidencia de lesiones focales o expansivas ni liquido periesplenico."
- **Intestino:** peristaltismo conservado, sin evidencia de líquido libre, no se observan ganglios linfáticos aumentados de tamaño ni LOE, aorta y cava inferior sin alteraciones.
- **Vejiga:** de forma y tamaño acorde a edad, de contenido anecoico y paredes delgadas, sin imágenes patológicas en su interior, de volumen aprox [N] cc.

## Variantes patológicas → redacción en hallazgos → conclusión
| Hallazgo dictado | En el párrafo | En la conclusión |
|---|---|---|
| Hígado graso | "ecogenicidad aumentada" | `Hígado Graso Grado I.` (pedir grado si no lo dice) |
| Congestión | "vías biliares intra hepáticas con congestión vascular leve" | — (preguntar) |
| Quiste hepático | "con presencia de lesión ovalada tipo quística de [a] x [b] cm, de contenido anecoico, con refuerzo acústico posterior, localizada en el lóbulo [derecho] en el segmento [VI]" | `Quiste Hepatico de [a] x [b] cm.` + `Se sugiere eco control en 3 meses.` |
| Barro biliar | "de paredes engrosadas, … con presencia de barro biliar en su interior." | `Vesícula Biliar con paredes engrosadas y presencia de barro biliar en su interior` |
| Litiasis vesicular | "de paredes engrosadas, … con presencia de litos en su interior de [X] cm aprox." | `Vesícula Biliar con presencia de litos en su interior de [X] cm aprox.` |
| Vesícula calcificada | "de paredes engrosadas semicalcificadas [X] cm" | `Vesícula Biliar calcificada con barro biliar.` |
| Colecistectomía | "Vesícula Biliar: no posee por antecedente quirúrgico previo." | `No posee Vesícula Biliar por antecedente quirúrgico.` |
| Páncreas ecogénico | "ecogenicidad aumentada" | — (preguntar si quiere diagnóstico) |
| Litiasis renal (medida) | "con presencia de litiasis de [X] cm" | `Litiasis renal bilateral, RD: [X] cm, RI: [Y] cm.` / `Litiasis Renal derecha de [X] cm.` |
| Microlitiasis (sin medida o < 0.4) | "con presencia de microlitiasis [de X cm]" | `Microlitiasis renal bilateral [RD: X cm RI: Y cm].` |
| Pielocalectasia | "con Pielocalectasia leve/moderada" | `… con Dilatacion Pielocalicial bilateral leve.` / `Pielocalectasia Bilateral moderada.` |
| Pielocalectasia + uréter proximal dilatado (niño) | "se evidencia dilatación de uréter proximal." | `Reflujo vesicouretral bilateral grado 2` + `Pielocalectasia Bilateral leve.` |
| Edema interasas | "con presencia de edema interesa moderado sugestivo de colitis." | `Colitis moderada.` (o leve) |
| Gases/heces abundantes | "con presencia de gases y heces abundantes / en colon descendente" | `Colitis leve.` o `Presencia de abundantes heces en colon descendente.` |
| Aorta calcificada | "aorta y cava inferior semi calcificadas" | — (preguntar) |
| Vejiga engrosada | "de paredes engrosadas", "con detritos en su interior" | `Vejiga de paredes engrosadas` |
| Ovarios pequeños (posmenopausia) | "de forma ovalada hipotrofico" | — + `Se sugiere valoración por ginecología oportuna.` |

## Cierre de la conclusión
Opciones literales que usa (elige según el caso):
- `Resto de estructuras dentro de limites normales.`
- `Resto de estructuras dentro de límites normales al momento de evaluación.`
- `Resto de estudio ecográfico sin hallazgos patológicos`
- Recomendaciones: `Se sugiere eco control en 3 meses.`, `Se sugiere valoración por ginecología oportuna.`,
  `Se sugiere colonoscopia, valoración por gastroenterólogo …`

## Medidas que siempre reporta (pedir las que falten)
Hígado LD y LI · Vesícula long y trans · Páncreas cabeza × cuerpo × cola · RD long y transv ·
RI long y transv · Bazo long y transv · [Vejiga volumen] · [Útero A × B, ovarios A × B c/u] ·
[Próstata long, trans, oblicua, volumen, IPP] · tamaño de cada litiasis/lesión.

## Errores a vigilar (vistos en los ejemplos: el texto copiado de un informe anterior no se actualizó)
- Hallazgo "normal" en el párrafo pero patológico en la conclusión, o al revés (p. ej. próstata
  "aumentada, deforma piso de vejiga" con conclusión "normal"; "residuo post miccional alto" sin medida).
- Numeración de la conclusión que salta (1, 2, 4).
- Edad o cédula mal escrita (p. ej. edad "5. años" en un adulto, cédula con puntos fuera de lugar), tipeos ("estructurss", "vesiculoretral").
- Lateralidad o medidas que no cuadran con la conclusión.

## Preguntar si falta
- Datos del paciente: nombre, CI (o "menor"), edad (en niños, años y meses), fecha; institución (logo).
- Todas las medidas de "Medidas que siempre reporta"; si hay fotos, leerlas de la pantalla y contrastar.
- Hígado graso: grado. Litiasis: tamaño de cada lito y lado. Pielocalectasia: grado y si hay uréter dilatado.
- Vesícula: paredes (delgadas/engrosadas), contenido (barro, litos y tamaño), antecedente de colecistectomía.
- Intestino: gases/heces, edema interasas (leve/moderado) → colitis en la conclusión.
- Abdominopélvico: vejiga (volumen, paredes), útero y ovarios (medidas) o próstata (medidas, volumen, IPP).
- Recomendación final (control, valoración por especialista) si el hallazgo la amerita.
- (ampliado 2026-11-07, disco) Qué plantilla (A o B) — por defecto la del modelo elegido.
- Niño con dolor en FID: diámetro del apéndice y grosor de pared (mm), compresibilidad, líquido/grasa periapendicular,
  McBurney/Blumberg ecográfico → `Apendicitis aguda.` + evaluación por cirugía pediátrica.
- Ganglios mesentéricos: tamaño del mayor (→ adenitis mesentérica). Gastroenteritis vs colitis vs enterocolitis.
- Hepatomegalia/esplenomegalia: grado. Quiste renal/hepático: medidas y localización. Hernia: tamaño del defecto y contenido.
- Lactantes: edad en días/meses, catéteres o sondas visibles.

## Títulos en el disco (ampliado 2026-11-07, disco)
- `INFORME ECOGRÁFICO ABDOMINAL` (605) · con punto final `INFORME ECOGRÁFICO ABDOMINAL.` (15) · sin tilde `INFORME ECOGRAFICO ABDOMINAL` (4).
- Raros (1 cada uno): `INFORME ECOGRÁFICO FAST ABDOMINAL.` · `INFORME ECOGRÁFICO ABDOMINAL CON DOPPLER HEPATICO` ·
  `INFORME ECOGRÁFICO ABDOMINAL/ PANCREATICO` · `INFORME ECOGRÁFICO DE PARED ABDOMINAL` (transductor LINEAL de 7.5MHz; ver abajo).
- Imágenes por .docx: 5–10 (moda 7; incluye 2–3 de logo y firma/sello) → ≈ 4–6 del eco.

## Dos plantillas de texto (ampliado 2026-11-07, disco)
Danilo alterna **dos plantillas** en los dos centros y en todo el período (no es una por institución):
- **Plantilla A** (437 docs; Colina 292, San José 139): introducción "…transductor convex de 3.5MHz en múltiples
  proyecciones, donde se evidencian los siguientes hallazgos:" + las frases de arriba ("forma, tamaño habitual con patrón granular fino…").
- **Plantilla B** (190 docs; San José 122, Colina 68): introducción `Se realiza estudio ecográfico en tiempo real con transductor de 3.5MHz donde se evidencia:` y estas frases (literales, las más repetidas):
  - **Hígado:** tamaño y forma acorde a edad, de medidas LD: [X] cm y LI: [Y] cm, limites bien definidos, parénquima homogéneo, sin presencia de lesiones focales o expansivas, ecogenicidad conservada, imágenes de vasos y vías biliares intrahepaticas sin alteraciones.
  - **Vesícula Biliar:** de forma piriforme, plenificada, de paredes delgadas, de medidas long: [X] cm transv: [Y] cm, sin imagenes patologícas en su interior, coledoco no dilatado.
  - **Páncreas:** parénquima homogéneo, sin presencia de lesiones focales o inflamación, de medidas cabeza: [A] cm cuerpo: [B] cm cola: [C] cm, conducto pancreático no visible, sin líquido peripancreático a su alrededor.
  - **Riñón Derecho / Izquierdo:** adecuadamente visible con movilidad respiratoria normal, de medidas long: [X] cm  transv: [Y] cm, de tamaño [dentro del rango normal / acorde a edad], parénquima homogéneo, ecogenicidad conservada, sin microlitiasis, sin presencia de Pielocalectasia conservando la relación médula corteza.
  - **Bazo:** parénquima homogéneo, de acuerdo a la edad del paciente, de medidas long: [X] cm  transv: [Y] cm, de tamaño normal, sin evidencia de lesiones focales o expansivas.
  - **Intestino:** peristaltismo positivo, con presencia de gases, sin evidencia de líquido libre en cavidad, no se observan ganglios linfáticos aumentados de tamaño ni otras masas ocupantes de espacio patológicas, aorta y cava inferior sin alteraciones.
  - Patológico en B: hígado "tamaño aumentado y forma acorde a edad … limites mal definidos … ecogenicidad aumentada"; riñón "con presencia de litiasis de medida: [X] cm localizada en medula, con presencia de Pielocalectasia leve"; intestino "se evidencia edema interasa [leve/moderado] en marco colonico".
- Frases pediátricas más repetidas de la plantilla A (ya listadas arriba): páncreas "de tamaño y forma acorde a edad, conducto pancreático no dilatado, sin líquido peripancretico." (203 veces, la frase de páncreas más usada del disco) y bazo "… de tamaño acorde a edad, sin evidencia de lesiones focales o expansivas ni liquido periesplenico." (159).
- Variante de riñón (≈ 17): "de ubicación habitual, con movilidad respiratoria normal, de medidas long: …".

## Diferencias por institución (ampliado 2026-11-07, disco)
- El texto es el mismo en Colina y San José; lo que cambia es el membrete (lo da el modelo) y la proporción de plantillas
  (San José usa más la B: 122/261; Colina sobre todo la A: 292/360).
- **Negrita** (medida en el XML de los .docx): la plantilla B lleva siempre solo la etiqueta en negrita; la plantilla A lleva
  todo el párrafo en negrita en ≈ 70 % de los casos **en ambos centros** (Colina 229/328, San José 128/156).
  ⚠ en el disco también aparece Colina con todo en negrita y San José con solo la etiqueta en negrita: `centros.md` dice
  "San José: todo el texto en negrita"; en la práctica lo decide el modelo que se copie.
- PDVSA: no hay abdominales en el disco (solo renales); usar `centros.md`.

## Apendicitis + microlitiasis en niño (informe real de San José, 2026-11-08) — literal
- **Intestino:** peristaltismo positivo con disminución  del mismo en FID con presencia de gases, Apendice cecal con edema de pared [X] mm de medidas aumentadas, doloroso  a la movilización de transductor, escaso líquido periapendicular, grasa periapendicular hiperecogenica, no se observan ganglios linfáticos aumentados de tamaño ni otras masas ocupantes de espacio patológicas, aorta y cava inferior sin alteraciones.
- **Riñones:** "… ecogenicidad conservada, con microlitiasis, sin presencia de Pielocalectasia conservando la relación médula corteza." (sin medida).
- **Vejiga:** plenificada, de paredes delgadas, de contenido anecoico, sin imágenes patologícas en su interior.
- Conclusión: `1) Apendicitis aguda.` / `2) Microlitiasis renal bilateral.` y, sin número, `Se sugiere evaluación por cirugía pediatrica.`
  (no puso "Resto de estructuras…"). Plantilla B; páncreas, riñones y bazo con "de tamaño dentro del rango normal" / "de tamaño normal".
- ⚠ Su borrador traía medidas de plantilla (hígado 11 cm, riñones 9.2–9.4 cm) y "vesícula distendida, de paredes engrosadas"
  con 3.5 × 1.2 cm en pantalla: usar la pantalla y preguntar por la vesícula.

## Más variantes patológicas → conclusión (ampliado 2026-11-07, disco)
Frecuencia aproximada en las conclusiones de los 629 abdominales: colitis/edema interasa ≈ 390 · litiasis renal ≈ 350 ·
hígado graso ≈ 280 · barro biliar ≈ 200 · pielocalectasia/dilatación de cálices ≈ 190 · microlitiasis ≈ 160 · litos vesiculares ≈ 85 ·
adenitis mesentérica ≈ 45 · gastroenteritis/enterocolitis ≈ 32 · quiste renal ≈ 30 · hepatomegalia ≈ 27 · apendicitis ≈ 24 ·
vejiga engrosada ≈ 23 · esplenomegalia ≈ 16 · colecistectomía ≈ 11 · hernia umbilical ≈ 8 · pancreatitis 4 · pólipos 4 ·
contusión renal 4 · hemangioma 2 · estudio normal ≈ 16 (la mayoría de los normales cierran solo con "Resto de estructuras…").

| Hallazgo | En el párrafo | En la conclusión |
|---|---|---|
| Hígado graso (otras formas) | "ecogenicidad Aumentada" | `Hígado graso grado 1.` (arábigo, el más usado) · `Hígado Graso grado I.` · `Esteatosis hepatica grado [N].` · ⚠ tipeo frecuente `Hígado graso graso [N]` (≈ 19) |
| Colitis (formas del disco) | "Se evidencia edema Interasa sugestivo de colitis leve." · "con presencia de abundante gas y edema interasa moderado a predominio de marco colonico" | `Edema interasa sugestivo de colitis.` (66) · `Colitis moderada.` (≈ 76) · `Colitis leve.` · `Edema interasa moderado generalizado a predominio de marco colonico.` |
| Gastroenteritis / enterocolitis (niños) | "edema interasa … (abundante gas y heces semiliquidas intraluminales)" | `Edema interasas sugestivo de Gastroenteritis.` · `Edema interesas sugestivo de enterocolitis [N]A no complicada.` |
| Adenitis mesentérica (sobre todo San José, niños) | "se observan ganglios linfáticos aumentados de tamaño ([X] cm)" / "se observan ganglios Mesentericos aumentados de tamaño escasos dispersos < [X] cm" | `Adenitis mesenterica [X] cm y edema interesas sugestivo de colitis.` · `Adenitis mesenterica < a [X] cm …` · `Múltiples ganglios mesentéricos de < de [X] cm.` |
| Apendicitis (niños) | "Intestino: peristaltismo positivo con disminución  del mismo en FID con presencia de gases, Apendice cecal con edema de pared y medidas aumentadas [A]x [B] cm, doloroso  a la movilización de transductor, [escaso líquido periapendicular,] no se observan ganglios …" · "imagen tubular no compresible en FID … pared: [X]mm … grasa periapendicular hiperecogenica" · "Mcburney ecografico (+)" / "Blumberg ecografico (+)" | `Apendicitis aguda.` (16) + `Se sugiere evaluación por cirugía pediatrica.` · `Conglomerado de asas en FID sugestivo a plastron apendicular.` |
| Hepatomegalia / esplenomegalia | "tamaño aumentado y forma acorde a edad … limites mal definidos" / bazo "tamaño aumentado para edad" | `Hepatomegalia leve.` · `Hepatomegalia grado [1/I/II/3].` · `Esplenomegalia grado I.` · `Hepato-Esplenomegalia grado I` |
| Quiste renal | "se evidencia quiste renal simple de medidas [A]x [B] cm" / "con quiste renal en polo superior de [A]x [B]x [C] cm" | `Quiste renal derecho de [A]x[B] cm.` · `Quiste simple Renal izquierdo de [A]x [B] cm.` |
| Litiasis vesicular | "con litos en su interior de [X] cm" | `Litiasis vesicular de [X] cm.` · `Litiasis vesicular de [X] cm con paredes engrosadas.` · `Vesícula biliar con paredes engrosadas, barro biliar y lito en su interior de [X] cm.` |
| Pólipo vesicular | "se evidencia imagen hiperecogenica adherida a pared sugestiva de pólipos de [A]x[B] cm" | `Vesícula biliar edematizada con imagen hiperecogenica en su interior sugestiva de pólipo.` |
| Pancreatitis | "Páncreas aumentado de tamaño … conducto pancreático visible y focos hiperecogenicos" | `Páncreas aumentado de tamaño, conducto pancreático dilatado sugestivo de pancreatitis aguda.` |
| Hemangioma / nódulo hepático | "imagen hiperecogenica en lóbulo [izquierdo] … de bordes irregulares" | `Lesión hepática sugestiva de hemangioma de [X] cm.` |
| Hernia umbilical | "Región umbilical: se evidencia Defecto aponeurotico umbilical con contenido en su interior (epiplon)" / "Nota: se evalúa pared abdominal con sonda lineal encontrando defecto aponeurotico umbilical de [X] cm." | `Defecto aponeurotico umbilical sugestivo de Hernia umbilical [X] cm.` · `Hernia umbilical [X] cm.` |
| Litiasis + dilatación | "se evidencia litiasis renal [X] cm con dilatación pielocalocial leve" (sic) | `Litiasis renal bilateral [X] cm, con dilatación de calices renales bilaterales.` · `Litiasis renal Der [X] cm , Litiasis renal Ri [Y] cm. Con leve dilatación Pielocalicial bilateral.` |
| ITU alta (niños) | "con edema perirenal" | `Edema peri-renal bilateral y dilatacion de cálices renales Bilaterales sugestivo de ITU alta.` |
| Contusión renal (trauma) | "con edema de cápsula que impresiona contusión renal" | `Contusión renal bilateral.` |
| Hidronefrosis | "pielocalectasia moderada sugestiva de Hidronefrosis grado II con perdida parcial de la relación médula corteza" | `Hidronefrosis grado II bilateral.` |
| Nefrectomía | "no posee por antecedente quirúrgico previo" | `No posee riñón izquierdo por antecedente quirúrgico previo.` |
| Aorta calcificada | "aorta y cava inferior semicalcificadas" (≈ 37) | casi nunca va a la conclusión |

Recomendaciones del disco (sin número, al final): `Se sugiere evaluación por cirugía pediatrica.` (≈ 21) ·
`Se sugiere interconsulta con gastropediatra.` · `Se sugiere valoración Pediátrica.` · `Se sugiere TAC complementaria.` /
`Se sugiere TAC abdominopelvica.` / `Nota se sugiere TAC abdominal con doble contraste complementaria.` ·
`Se sugiere eco control en [N] meses.` · `Se sugiere control de amilasa / Lipasa en un 1 mes.` · `Se sugiere valoración por urología / nefrología`.
Cierres más frecuentes: `Resto de estructuras dentro de límites normales.` (≈ 100 con sus variantes de tilde y punto) ·
`Resto estructuras dentro de limites normales` · `Estudio ecografico sin Hallazgo patológicos.`

## Variantes de estudio (ampliado 2026-11-07, disco)
- **FAST abdominal** (1, niño con trauma): informe abdominal completo + `Nota: se explora mediante técnica de ecofast obteniendo 4 cuadrantes sin liquido libre.`
  y `Equipo de ecografía sin capacidad para fast- extendido.`; conclusión con el hallazgo (p. ej. contusión renal) + "Resto de estructuras…".
- **Abdominal con doppler hepático** (1, lactante): en Hígado añade "Se realiza medicion de arterias y venas hepáticas con flujo doppler …
  índice de resistencia vascular aumentado, onda doppler espectral rítmica con patrones de flujo de indice de resistencia promedio [IR] …";
  conclusión `Hepatoesplenomegalia grado I.` + `Vías Biliares intra y extrahepatica con dilatacion leve.` + `Se sugiere colangio resonancia o TAC abdominal con doble contraste para descartar …`.
- **Pared abdominal** (1): transductor LINEAL de 7.5MHz; un solo párrafo `Pared Abdominal: piel con grosor y ecogenicidad conservada, tejido celular subcutáneo sin alteraciones …, línea alba sin alteracion capa muscular con patron fibrilar (músculos rectos transversos y oblicuos) … Cicatriz umbilical no dolorosa a la exploración sin evidencia de defectos aponeurotico.` → `Estudio ecografico dentro de límites normales.` (ver también `eco-partes-blandas.md`).
- **Abdominal / pancreático** (1): abdominal normal con páncreas detallado "de medidas [A]x [B] x[C] cm cabeza cuerpo y cola respectivamente".
- **Emergencia / apendicitis**: a veces solo `Intestino:` + `Vejiga:` (sin los demás órganos) y conclusión `Apendicitis aguda.`.
- **Neonato / lactante** (30 < 1 año; edad "2 dias.", "8 meses", "1 mes 15 dias"): plantilla B con "tamaño … acorde a edad";
  se nombran catéteres ("evidenciando catéter de onfaloclisis" → `Catéter de onfaloclisis en vasos umbilicales.`).
- Vejiga en el abdominal (≈ 55): "Vejiga: plenificada, de paredes delgadas, de contenido anecoico, sin imágenes patologícas en su interior." (niños) y a veces "Vejiga y próstata:" en adultos.

## Más errores a vigilar (ampliado 2026-11-07, disco)
- Año mal tipeado en la fecha: "/226" por "/2026" (11 informes) → revisar siempre la fecha.
- Conclusiones con tipeos sistemáticos: "bilteral", "bilatera", "biateral", "Litasis", "Microlilitiasis", "litiasis de al bilateral"
  (autocorrección), "interesa/interesas" por "interasa", "graso graso", "pielocalocial", "Modeada", "Hepatolomegalia". Corregir al redactar.
- Líneas de conclusión pegadas a la etiqueta ("2) Litiasis renal bilateral RD: …" aparece como si fuera etiqueta) y numeración que salta.
- Medidas con unidad repetida ("10 cm cm") o punto suelto (".transv:", "2.4. cm").
- En 5 documentos .doc antiguos el texto viene con caracteres de control antes de "Ci/Edad/Fecha".

## Ejemplo anonimizado
```
INFORME ECOGRÁFICO ABDOMINAL
| Px: [NOMBRE] | Ci: [CI] | Edad: [EDAD] | Fecha: [FECHA] |

Se realiza estudio ecográfico en tiempo real con transductor convex de 3.5MHz en múltiples proyecciones, donde se evidencian los siguientes hallazgos:

Hígado: forma, tamaño habitual con patrón granular fino, de medidas LD: 12.5 cm y LI: 6.3 cm, limites bien definidos, parénquima heterogeneo, ecogenicidad aumentada, imágenes de vasos visibles y vías biliares intrahepaticas sin alteraciones.
Vesícula Biliar: tamaño y forma habitual plenificada de medidas long: 4.7 cm trans: 1.9 cm, de paredes engrosadas, conducto biliar de calibre adecuado, con presencia de barro biliar en su interior.
Páncreas: de forma y configuración habitual sin liquido peripancreatico, ecogenicidad aumentada, con medidas de cabeza cuerpo y cola 2.1cm x 1.6cm x 1.6cm
Riñón Derecho: adecuadamente visible con movilidad respiratoria normal, de medidas long: 10 cm, transv: 5.8 cm, de tamaño dentro del rango normal, parénquima heterogéneo, ecogenicidad conservada, con presencia de litiasis de 0.6cm, sin presencia de Pielocalectasia, conservando la relación médula corteza.
Riñón Izquierdo: adecuadamente visible con movilidad respiratoria normal, de medidas long: 10.1 cm, transv: 6.3 cm, de tamaño dentro del rango normal, parénquima heterogéneo, ecogenicidad conservada, con presencia de microlitiasis, sin presencia de Pielocalectasia, conservando la relación médula corteza.
Bazo: parénquima homogéneo, de medidas long: 10.6 cm. transv: 4 cm, de tamaño normal, sin evidencia de lesiones focales o expansivas ni liquido periesplenico.
Intestino: peristaltismo conservado, con presencia de gases y heces, sin evidencia de líquido libre en cavidad, no se observan ganglios linfáticos aumentados de tamaño ni otras masas ocupantes de espacio patológicas, aorta y cava inferior sin alteraciones.

Conclusión:	1) Hígado Graso Grado I
		2) Vesicular Biliar con paredes engrosadas y presencia de barro biliar en su interior
		3) Litiasis Renal derecha de 0.6 cm.
		4) Microlitiasis Renal izquierda.
```
