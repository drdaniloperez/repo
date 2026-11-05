# Formato: Informe ecográfico ABDOMINAL (y variantes)

Aprendido de 30 informes reales (2025–2026) de Clínica Colinas, Policlínica San José y Centro Clínico
Hospital Jesús Farías (PDVSA). Variantes de título:
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
