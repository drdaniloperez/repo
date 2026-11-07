# Formato: Informe ecográfico PROSTATICO

Aprendido de 292 documentos: 11 informes reales iniciales + 281 del disco (02/2025–10/2026), instituciones: Centro de Especialidades Médicas Colina (272), Policlínica San José (7), sin logo reconocido (2). (ampliado 2026-11-07, disco)

Aprendido de 11 informes reales (Centro de Especialidades Médicas Colina). Membrete compacto (márgenes superiores pequeños);
la firma va inmediatamente después de la conclusión y **las 2 imágenes van en la misma página**,
debajo del bloque de firma.
- (ampliado 2026-11-07, disco) Imágenes: el .docx típico trae 4 imágenes = logo + firma/sello + **2 imágenes del eco**
  (251/281); 3 imágenes en 23 (una sola del eco), 5 en 6 (3 del eco, p. ej. cuando se añade vejiga). Las del eco
  miden ≈ 8.3–9.8 × 8.9–10.5 cm, una al lado de la otra.
- (ampliado 2026-11-07, disco) Pacientes adultos (mediana 54 años, mayoría 45–85).

## Estructura
```
INFORME ECOGRÁFICO PROSTATICO
| Px: … | Ci: … | Edad: … | Fecha: … |

Se realiza estudio ecográfico en tiempo real con transductor convex de 3.5MHz en múltiples proyecciones, donde se evidencian los siguientes hallazgos:

Próstata: …
Vol prostático: [N] cm³
[Nota: …]
Conclusión: Hiperplasia prostática grado [I/II/III].        ← sin numeración cuando es una sola
```
(ampliado 2026-11-07, disco)
- Título: `INFORME ECOGRÁFICO PROSTATICO` (266/281, sin tilde en PROSTATICO); `INFORME ECOGRÁFICO PROSTÁTICO` (13);
  `INFORME ECOGRÁFICO PROSTATICO Y VESICAL` (2) cuando se valora la vejiga con volumen pre y posmiccional.
- La introducción es idéntica en los 281 (transductor convex de 3.5MHz).
- Variante PROSTATICO Y VESICAL (Vejiga va ANTES de Próstata):
```
INFORME ECOGRÁFICO PROSTATICO Y VESICAL
| Px: [NOMBRE] | Ci: [CI] | Edad: [EDAD] | Fecha: [FECHA] |

Se realiza estudio ecográfico … donde se evidencian los siguientes hallazgos:
Vejiga: plenificada, de paredes [delgadas/engrosadas], de contenido anecoico …, Vol aprox [N] cc. Pre miccional.
Vol aprox [N] cc postmiccional
Próstata: …
Vol prostático: [N]cm³
Conclusión: 1) Hiperplasia prostática grado [1/2].
            2) Vejiga de paredes engrosadas con abundantes detritos.      ← si aplica
```
- Otras formas de dar el residuo (6 documentos en total): `Volumen vesical pre-miccional. [N]cc aprox.` /
  `Volumen vesical Post-miccional. [N] cc aprox.`; `Vol premiccional: [N] cc.` / `Vol post miccional [N] cc.`;
  `Vol Vejiga postmiccional: [N] cc`.
- Negritas (python-docx, Colina y San José): título en negrita; en **Próstata:** solo la etiqueta va en negrita;
  en Colina "Vol prostático:" lleva la etiqueta en negrita; la línea **Conclusión** va entera en negrita.
  ⚠ en el disco también aparece que en San José los párrafos de próstata NO van todo en negrita (solo la etiqueta),
  a diferencia de lo que dice `centros.md` para San José: lo da el modelo.

## Frases literales
- Aumentada: **Próstata:** de tamaño y forma aumentado, de medidas long: [L] cm trans: [T] cm oblicua: [O] cm de bordes [regulares/irregulares], parénquima heterogéneo, [sin calcificaciones / con microcalcificaciones / con calcificaciones escasas] en su interior. Ecogenicidad [conservada / ligeramente aumentado], que [deforma / no deforma] piso de vejiga. IPP: [N] cm
- Normal: **Próstata:** de tamaño conservado, forma acorde a edad, de medidas long:[L] cm trans:[T]cm oblicua: [O]cm de bordes bien definidos, parénquima heterogéneo, sin presencia de calcificaciones en su interior. Ecogenicidad conservada, que no deforma suelo de vejiga.
- **Vol prostático:** [N] cm³ — tomarlo de la pantalla del ecógrafo (las medidas mostradas van
  redondeadas; recalcular con × 0,52 da un valor algo menor). Si no está, calcular L × T × O × 0,52 y avisar.
- `Nota: Px con antecedente quirúrgico previo de …` cuando aplica.
- Conclusión normal: `1) Estudio ecografico dentro de límites normales.`

### Frases del disco (ampliado 2026-11-07, disco) — con su frecuencia en 281
- Normal más frecuente (42): `Próstata: de tamaño y forma acorde a edad, de medidas long [L] cm trans: [T] cm oblicua: [O] cm de bordes bien definidos, parénquima heterogéneo, sin calcificaciones en su interior. Ecogenicidad conservada, que no deforma piso de vejiga.`
  (ojo: aquí "long" va sin dos puntos).
- Normal segunda forma (≈ 60 entre variantes de espacios): `Próstata: de tamaño conservado, forma acorde a edad, de medidas long: [L]cm trans: [T]cm oblicua: [O] cm de bordes bien definidos, parénquima heterogéneo, sin calcificaciones en su interior. Ecogenicidad conservada, que no deforma suelo de vejiga.`
- Tamaño: "de tamaño conservado," (84) · "de tamaño y forma acorde a edad," (64) · "de tamaño aumentado y forma acorde a edad," (24) ·
  "de tamaño y forma aumentado," (38) · "de tamaño aumentado," (14) · "de tamaño aumentado levemente [y forma acorde a edad]," (14) ·
  "de tamaño [ligeramente] aumenado," (9, tipeo) · "de tamaño y forma ligeramente aumentado," (3) · "de tamaño aumentado y forma irregular," (3).
- Bordes: "bien definidos" (207) · "parcialmente definidos" (19) · "regulares" (17) · "irregulares" (15) · "mal definidos" (9) · "poco definidos" (6).
- Calcificaciones: "sin calcificaciones en su interior" (184) · "sin presencia de calcificaciones en su interior" (37) ·
  "con escasas calcificaciones en su interior" (15) · "con calcificaciones en su interior" (12) · "con calcificaciones escasas en su interior" (6) ·
  "con presencia de calcificaciones escasas en su interior" (6) · "con microcalcificaciones en su interior" (3) · "con calcificaciones dispersas en su interior" (3) ·
  "con calcificación en su interior de [N] cm aproximadamente en tercio medio" (calcificación única medida).
- Ecogenicidad: "conservada" (258) · "aumentada" (8) · "ligeramente aumentado" (2) · "disminuida" (1) · "aumentada y zonas de cirugía anterior" (1).
- Piso vesical ("piso" y "suelo" se usan igual): "que no deforma piso de vejiga" (74) · "que no deforma suelo de vejiga" (74) ·
  "que deforma piso de vejiga" (41) · "que deforma parcialmente piso de vejiga" (40) · "que deforma suelo de vejiga" (12) ·
  "que deforma parcialmente suelo de vejiga" (10) · "que deforma levemente piso de vejiga" (2) ·
  "que no deforma suelo de vejiga con detritos escaso en su interior" (3).
- IPP solo en 20/281, casi siempre cuando "deforma piso": `IPP: [N] cm` · `IPP: [N] mm` · `IPP: > 1 cm` · `Ipp: [N]cm`;
  en San José una vez: `índice de protrucion prostatica >10 mm.` y en la conclusión `Ipp: >10 mm elevado.`
- Volumen: `Vol prostático: [N] cm³` (262, a veces sin espacio: `37.1cm³`); variantes raras `VOL: [N] cc.` / `VOL: [N] ml.` (10) y
  `Volumetría [N]cc` (2, dentro del párrafo de próstata).
- Vejiga (cuando se describe):
  - `Vejiga: plenificada de contenido anecoico, de paredes delgadas, sin imágenes patológicas en su interior.` + `Vol. Aprox: [N] cc.`
  - `Vejiga: plenificada, de paredes engrosadas, de contenido anecoico en su mayoría, con imágenes hiperecogenicas en fondo vesical sugestivas de detritos abundantes, Vol aprox [N] cc. Pre miccional.`
  - `Vejiga: de contenido anecoico, de volumen aprox [N] cc, fondo vesical sin deformidades con escasos detritos en su interior,`
  - Litiasis: `Vejiga: se evidencian litos, móviles, hiperecogénicos, con sombra acústica posterior en fondo vesical, de medidas [A] x [B] cm y de [A] x [B] cm, paredes engrosadas.`
- Notas (8): `Nota: px postoperado de prostectomia.` · `Nota: px refiere prostatectomia hace [N] años.` ·
  `Nota: paciente operado hace [N] años de prostectomia radical.` · `Nota: se evidencia en fondo de vejiga formación sacular cercana a la próstata que impresiona pólipo vesical.` ·
  `Nota: px Con POT de prostatectomia por CA de prostata. Se sugiere UROTAC al compensar Px.`
- Sin próstata: `Próstata: no posee por antecedente quirúrgico previo.` → `Conclusión: 1. No posee próstata por antecedente quirúrgico previo.`

## Conclusión
- Una sola conclusión, sin numeración: `Conclusión: Hiperplasia prostática grado [I/II/III].`
- Normal: `Conclusión: 1) Estudio ecografico dentro de límites normales.`
- La conclusión debe ser coherente con la descripción (aumentada ↔ hiperplasia; deforma piso ↔ IPP).

### Conclusión en el disco (ampliado 2026-11-07, disco)
- Sin numeración 182/281, numerada `1)` (o `1.`) 99/281. Grado en romanos (91) o arábigos (54): `grado II` / `Grado 2`.
- Normal, dos fórmulas casi igual de frecuentes: `Estudio ecografico sin hallazgos patologicos.` (84 con variantes de
  tilde/mayúscula) y `1) Estudio ecografico dentro de límites normales.` (92). Variante: `1) Estudio Ecográfico dentro de límites normales acorde a edad.`
- Hiperplasia: `Hiperplasia prostática grado [N].` (95) y `Hiperplasia prostático grado [N].` (62, concordancia errónea
  pero sistemática: al generar usar "prostática").
- **Existe grado IV** (12 informes, 57–117 cm³): `Hiperplasia prostático grado IV.` / `1) Hiperplasia prostática grado IV` / `Hiperplasia prostática Grado 4.`
- Con prostatitis: `1. Hiperplasia prostática grado I, sugestivo de prostatitis.` (4); con calcificación: `2. Calcificación prostática de 0.5 cm aproximadamente.`
- Hallazgos vesicales en 2.º ítem: `2) Fondo vesical con abundante detritos y paredes engrosadas.` · `2) Vejiga urinaria con litos en su interior y paredes engrosadas.` ·
  `1) pólipo vesical de medidas [A]x[B] cm en fondo vesical. 2) próstata dentro de limites normales.`
- Recomendación (17/281), en línea aparte tras la conclusión: `Se sugiere valoración por urología.`; urgente: `Nota de sugiere valoración por urología urgente.` (tipeo "de" por "se").
  Suele aparecer en grado II alto, III y IV, o con hallazgos vesicales.

## Grado según volumen (inferido de sus informes — ⚠ confirmar con Danilo)
| Volumen | Conclusión usada |
|---|---|
| ≈ 21 cm³ | Estudio ecográfico dentro de límites normales |
| ≈ 27 cm³ | Hiperplasia prostática grado I |
| 46–52 cm³ | Hiperplasia prostática grado II |
| ≈ 80 cm³ | Hiperplasia prostática grado III |
Escala propuesta: < 25 normal · 25–40 grado I · 40–60 grado II · > 60 grado III.
(Un informe con 38.4 cm³ y próstata "aumentada" concluyó "normal": señalar ese tipo de discrepancia.)

### Verificación con 265 informes con volumen (ampliado 2026-11-07, disco)
| Volumen (cm³) | Normal | Grado I | Grado II | Grado III | Grado IV |
|---|---|---|---|---|---|
| < 20 | 25 | – | – | – | – |
| 20–24.9 | 84 | 5 | – | – | – |
| 25–29.9 | 4 | 17 | – | – | – |
| 30–34.9 | – | 24 | – | – | – |
| 35–39.9 | 1 | 16 | 10 | – | – |
| 40–44.9 | – | 2 | 14 | 1 | – |
| 45–49.9 | – | – | 22 | 2 | – |
| 50–54.9 | – | – | 7 | 2 | – |
| 55–59.9 | – | – | 3 | 4 | 1 |
| 60–69.9 | – | – | – | 5 | 2 |
| ≥ 70 | – | – | – | 2 | 9 |

Medianas: normal 20.9 · grado I 30.8 · grado II 46.3 · grado III 57.6 · grado IV 94.
Escala que mejor reproduce su práctica (⚠ confirmar): **< 25 normal · 25–37 grado I · 38–55 grado II · 55–70 grado III · > 70 grado IV**.
- La frontera I/II es difusa (35–40 cm³ aparece como I o II); III/IV también (55–70).
- ⚠ en el disco también aparece grado IV, que la escala inicial (hasta III) no contemplaba: no borrar la escala de arriba,
  pero al generar, con > 70 cm³ preguntar si es grado III o IV.
- Discrepancias a señalar: 5 informes de 21–24 cm³ concluyen "grado I" (plantilla vieja); 1 de 38.4 cm³ "normal";
  3 de 40–49 cm³ "grado III".

## Preguntar si falta
Las 3 medidas, volumen, IPP (protrusión intravesical), bordes, calcificaciones, si deforma el piso
vesical, residuo posmiccional si lo menciona, antecedente de prostatectomía/RTU.
(ampliado 2026-11-07, disco)
- Si el volumen cae en zona dudosa (35–40 o 55–70 cm³): qué grado quiere.
- Si se valoró la vejiga: volumen premiccional y posmiccional → título "PROSTATICO Y VESICAL"; paredes (delgadas/engrosadas), detritos, litos (medidas), pólipo.
- Si hay calcificación única: su tamaño y localización (tercio medio…).
- Si sugiere prostatitis, si añade "Se sugiere valoración por urología" (urgente o no).
- Fórmula de normal: "sin hallazgos patológicos" o "dentro de límites normales" (usar la del modelo si no dice).

## Errores y tipeos frecuentes a vigilar (ampliado 2026-11-07, disco)
- "Hiperplasia prostático" (62) → "prostática"; "aumenado" (9) → "aumentado"; "Ecogenicidad ligeramente aumentado" → "aumentada";
  "prostectomia/protastectomia" → "prostatectomía"; "litros" por "litos"; "dent4o"; "2))"; "Nota de sugiere".
- Medidas de una plantilla anterior: el nombre del archivo no siempre coincide con el paciente del informe (se reutiliza el
  documento): verificar Px, Ci, Edad, Fecha y que conclusión ↔ volumen sean coherentes.
- Campos de plantilla sin rellenar: "Vejiga:" vacía, "Si (  ) No (  )", "Vol vesical:  cc" → quitarlos.
- Grado en romanos vs. arábigos en el mismo documento: unificar (preferir romanos).
- ⚠ Los .docx del disco (carpeta Alarms) tienen las imágenes con CRC dañado: python-docx no los abre como modelo; usar un
  informe reciente que Danilo envíe o reparar el zip.

## Ejemplo anonimizado
```
INFORME ECOGRÁFICO PROSTATICO
| Px: [NOMBRE] | Ci: [CI] | Edad: [EDAD] | Fecha: [FECHA] |

Se realiza estudio ecográfico en tiempo real con transductor convex de 3.5MHz en múltiples proyecciones, donde se evidencian los siguientes hallazgos:

Próstata: de tamaño y forma aumentado, de medidas long: 4.5 cm trans: 4.3 cm oblicua: 4.8 cm de bordes irregulares, parénquima heterogéneo, con microcalcificaciones en su interior. Ecogenicidad conservada, que deforma piso de vejiga. IPP: 0.7 cm
Vol prostático: 46.4 cm³
Conclusión: Hiperplasia prostática grado II.
```
Ejemplo PROSTATICO Y VESICAL (ampliado 2026-11-07, disco):
```
INFORME ECOGRÁFICO PROSTATICO Y VESICAL
| Px: [NOMBRE] | Ci: [CI] | Edad: [EDAD] | Fecha: [FECHA] |

Se realiza estudio ecográfico en tiempo real con transductor convex de 3.5MHz en múltiples proyecciones, donde se evidencian los siguientes hallazgos:
Vejiga: plenificada, de paredes engrosadas, de contenido anecoico en su mayoría, con imágenes hiperecogenicas en fondo vesical sugestivas de detritos abundantes, Vol aprox 210 cc. Pre miccional.
Vol aprox 85 cc postmiccional
Próstata: de tamaño y forma aumentado, de medidas long 3.6 cm trans: 4.0 cm oblicua: 4.3 cm de bordes mal definidos, parénquima heterogéneo, con calcificaciones escasas en su interior. Ecogenicidad conservada, que deforma parcialmente piso de vejiga.
Vol prostático: 32.4 cm³
Conclusión: 1) Hiperplasia prostática grado I.
            2) Vejiga de paredes engrosadas con abundantes detritos.
Se sugiere valoración por urología.
```
