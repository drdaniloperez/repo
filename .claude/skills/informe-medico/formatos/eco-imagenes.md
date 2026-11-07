# Imágenes en los informes de eco

Aprendido de 38 informes reales.

## Fotos de origen
Fotos verticales del teléfono (3000×4000) a la pantalla del ecógrafo. La pantalla suele ocupar
**todo el ancho de la foto y salirse por los lados**; arriba se ve pared/marco y abajo el marco o
teclado. En Word Danilo recorta solo arriba y abajo. Ahora se recorta con
`scripts/recortar_pantalla.py`: corrige la perspectiva y deja únicamente la pantalla.
Equipos vistos: Mindray portátil (C. E. M. Colina, pantalla oscura, recuadro de medidas abajo a la
derecha "1 Distancia 5.06 cm"), Mindray de carro (Hospital Jesús Farías – PDVSA, "Dist 5.97 cm"), MediSono P12Exp
(Policlínica San José: marco blanco, interfaz azul, encabezado "POLICLINICA SAN JOSE" junto al logo MediSono,
medidas arriba a la derecha "1 D: 25.21 mm"; transductores L742 lineal, 2P1 sectorial, C344 convex).
- Rendimiento en 57 fotos reales: ~80 % de recortes correctos automáticamente. El resto queda con
  una franja de marco/pared y se corrige con `--esquinas` mirando la vista previa con cuadrícula.
  Verificar SIEMPRE cada recorte.
- Fotos del equipo completo (pantalla pequeña en la foto): el recorte automático falla; usar
  `--esquinas`. Para los informes conviene fotografiar la pantalla de cerca, llenando la foto.
- Atención a las unidades: el equipo de San José mide en **mm** → convertir a cm para el informe.

## Cantidad y orden
| Estudio | Nº de imágenes | Orden |
|---|---|---|
| Abdominal | 5–7 | Hígado → Vesícula → Páncreas → Riñón derecho → Riñón izquierdo → Bazo (→ otras) |
| Abdominopélvico | 6–10 | Igual + Vejiga → Útero/ovarios o Próstata |
| Abdominal con énfasis renal / renal (pediátrico) | 3–5 | Riñón derecho → Riñón izquierdo → Vejiga (→ hígado/vesícula/bazo) |
| Prostático | 2 | Transversal → Longitudinal (con volumen) |
| Piel y partes blandas | 1–2 | La lesión con medidas (→ Doppler/otro corte) |

## Maquetación
- Van **después del bloque de firma**, en cuadrícula de **2 columnas**, sin pies de foto.
- Ancho ≈ 8.3 cm en sus originales, pero en la cuadrícula generada usar **7.9 cm**: 2 × 8.3 cm + márgenes de
  celda no caben en carta con márgenes de 2.54 cm y Word **recorta el borde derecho** (se pierden las medidas).
  Revisar siempre la vista previa: la columna de medidas de la derecha debe leerse completa.
- Abdominal: el texto llena la página 1 y las imágenes pasan a la página 2 (3 filas × 2).
- Prostático: 2 imágenes lado a lado en la misma página que el texto.
- Con `informe_desde_modelo.py`: `"columnas": 2, "ancho_imagen_cm": 8.3` (prostático: 8.0 para que quepan en la página 1).
