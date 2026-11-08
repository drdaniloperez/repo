# Centros y membretes

Danilo trabaja en cuatro instituciones; cada una tiene su membrete.
Del disco (1.986 archivos, 2026-11-07): Colina 1.261 documentos, San José 635, Jesús Farías (PDVSA) 3 ecos + listas
y guardias sin logo, Razetti 1 (programación quirúrgica). **El documento final se arma con
`scripts/informe_desde_modelo.py` usando como modelo un informe anterior suyo del mismo centro y tipo**:
así quedan idénticos el logo, la tabla, las fuentes, la firma/sello y el bloque de firma.

| Centro | Cómo se reconoce | Diseño |
|---|---|---|
| **Centro de Especialidades Médicas Colina** (archivos "COLINA…/colinas…") | Logo COLINA arriba a la izquierda; título a su derecha | Tabla de 1 fila × 4 (Px, Ci, Edad, Fecha) con borde. Texto con etiqueta en negrita. Firma+sello como imagen sobre el nombre. Equipo Mindray (portátil). |
| **Policlínica San José** | Logo SAN JOSÉ centrado arriba; título centrado debajo. ⚠ En su modelo 2026 (eco abdominal, 2026-11-08): logo de alta resolución con RIF **flotante arriba a la izquierda (6.0 × 1.4 cm)** y el título a su derecha; firma+sello (4.2 × 1.9 cm) sobre el bloque "Dr. … / CIRUJANO PEDIATRA-ECOGRAFISTA / MPPS… CMA… / RIF…" centrado y compacto | Misma tabla. Todo el texto en negrita. ⚠ (disco, 2026-11-07) la negrita depende de la **plantilla**, no del centro: la plantilla corta ("…3.5MHz donde se evidencia:") y los ecos renales, testiculares, mamarios y prostáticos de San José llevan solo la etiqueta en negrita; la plantilla larga, ≈70 % todo el párrafo. Manda el modelo `.docx`. |
| **Hospital Jesús Farías (PDVSA)** — donde trabaja; pocos ecos allí | Logo PDVSA arriba a la izquierda; título centrado | Misma tabla. Todo el texto en negrita. Equipo Mindray de carro. |
| **Hospital Universitario Dr. Luis Razetti** (Barcelona, Anzoátegui) — servicio de Cirugía Pediátrica | Escudo H.U.L.R. "1953 - 2022" arriba a la izquierda; a la derecha, en azul, "HOSPITAL UNIVERSITARIO DR. LUIS RAZETTI BARCELONA, ANZOÁTEGUI / SERVICIO DE CIRUGÍA PEDIÁTRICA / <MES AÑO>" | **Membrete REAL** (ajustado 2026-11-07 con su programación quirúrgica de junio 2023, único documento del Razetti en el disco): carta **horizontal**, escudo 3.9 × 4.3 cm detrás del texto, tres líneas alineadas a la derecha, color 4472C4, 16 pt, sin negrita; debajo, tabla por día. No hay ecos ni informes clínicos del Razetti en el disco. |

Bloque de firma (texto, centrado y en negrita, debajo de la imagen de firma y sello): nombre,
"CIRUJANO PEDIATRA-ECOGRAFISTA", registros MPPS/CMA y RIF. Se copia del modelo; no se reescribe.

## Logos (cada institución con el suyo — nunca mezclar)
Guardados en `formatos/logos/` (son públicos; la firma y el sello NO se guardan aquí):
| Archivo | Institución | Tamaño y posición en sus informes |
|---|---|---|
| `colinas.png` | COLINA — Centro de Especialidades Médicas | 4.8 × 2.3 cm, arriba a la izquierda, título a la derecha |
| `pdvsa-jesus-farias.png` | Hospital Jesús Farías (PDVSA) — logo oficial que envió Danilo, alta resolución | 6.0 × 1.7 cm, arriba a la izquierda, título centrado debajo |
| `san-jose.png` | Policlínica San José | 8.9 × 1.4 cm, centrado, título centrado debajo |
| `hulr-luis-razetti-2022.png` | Hospital Universitario Dr. Luis Razetti — escudo "1953 - 2022", recortado tal como aparece en su programación quirúrgica real | 3.9 × 4.3 cm, arriba a la izquierda (detrás del texto); membrete en azul alineado a la derecha |
| `hulr-luis-razetti.png` | Hospital Universitario Dr. Luis Razetti — escudo anterior "1963 - 2007" que envió Danilo | Ya no se usa por defecto (queda como `archivo_anterior`) |

`logos.json` guarda además la huella (md5) del logo tal como está dentro de sus .docx:
- `informe_desde_modelo.py` reconoce la institución del modelo por su logo y **se detiene si no es la
  institución del estudio** (`--centro` o `"centro"` en datos.json).
- `armar_informe_docx.py --centro <x>` arma el membrete con el logo correcto cuando no hay modelo.

**Cómo saber la institución del estudio:** lo dice Danilo; si no, se deduce del encabezado de la
pantalla del ecógrafo en las fotos ("CENTRO DE ESPECIALIDADES M…" = Colina, "CENTRO CLINICO PDVSA
ORIENTE" = Hospital Jesús Farías (PDVSA), "POLICLINICA SAN JOSE" = San José, verificado en foto del equipo MediSono P12Exp) y **se confirma con él antes de generar**.
Hay dos versiones de su imagen de firma y sello; en partes blandas usa la segunda (la da el modelo).

## Dónde están los modelos
El repositorio del cerebro es **público**: aquí NO se guardan los modelos `.docx` (llevan la firma, el
sello y datos de pacientes). Opciones, en orden de preferencia:
1. Carpeta de modelos en su equipo (p. ej. el disco Rodolfo SSD o `~/informes-modelos/`) en sesiones locales.
2. Que Danilo adjunte un informe anterior del centro en la sesión.
3. Si Danilo hace privado el repositorio, guardar un modelo limpio por centro y tipo en
   `formatos/modelos/` (sin datos de pacientes: se generan con el propio script y datos ficticios).

## Firma y sello al editar un informe ya hecho
En sus .docx la imagen de firma/sello suele estar anclada a una posición fija de la **página**
(`wp:positionV relativeFrom="page"`). Si se añaden líneas al texto, la conclusión baja y la firma la tapa.
Al añadir texto: cambiar el ancla a `relativeFrom="paragraph"` (párrafo vacío previo a "Dr. …", offset ≈ 0.15 cm)
y revisar la vista previa.

## Documentos clínicos de Cirugía Pediátrica (ampliado 2026-11-07, disco)
Resumen de ingreso, informe de egreso, extensión, evaluación e informe médico de cirugía pediátrica se hicieron
sobre todo en **Colina** (y algunos en San José): llevan el logo de la institución, a veces además el **logo personal
"DP · Dr. Danilo Pérez T. · Cirujano Pediatra"** (círculo negro) y la imagen de firma/sello. El logo personal y la firma
NO se guardan en el repo (contienen su nombre y la firma); se toman del modelo `.docx` en la sesión local.
Bloque de firma de estos documentos (texto): "Dr. Danilo Pérez T." / "Ecografista Integral/Cirujano Pediatra." /
"MPPS: [MPPS] CMA: [CMA]" / "RIF.: [RIF]".

## Huellas añadidas (2026-11-07)
- Colina: segunda versión del logo (verde, "COLINA Centro de Especialidades Médicas") usada en los documentos clínicos.
- San José: versión de alta resolución del logo con "RIF" de la policlínica, usada en ecos recientes.
- Razetti: la captura recortada del escudo 1953-2022 que lleva su programación quirúrgica.
- `armar_informe_docx.py --centro razetti` arma ya el membrete real (carta horizontal, texto azul a la derecha); si no se
  dan Px/Ci/Edad no pone la tabla de identificación (listas y programaciones).

## Medidas reales del logo en el disco (2026-11-07, todos los .docx con logo reconocido)
| Institución | Documentos | Tamaño y colocación más frecuentes |
|---|---|---|
| Colina | 1.261 | 4.8 × 2.2–2.3 cm flotante (ecos, ≈ 745); 4.8 × 2.8 y 4.3 × 2.8 cm flotante (versión verde de los documentos clínicos y ecos recientes, ≈ 330) |
| San José | 635 | 8.9 × 1.4 cm en línea, centrado (282); 7.8 × 1.4 cm flotante (151); 5.7 × 1.9 cm flotante (98, logo de alta resolución con RIF); 8.9 × 1.4 cm flotante (63) |
| Jesús Farías (PDVSA) | 3 ecos | 6.0 × 1.7 cm flotante, arriba a la izquierda (los 3) — confirma lo documentado |
| Razetti | 1 | 3.9 × 4.3 cm flotante detrás del texto (programación quirúrgica) |
Con `informe_desde_modelo.py` el tamaño lo da el modelo; con `armar_informe_docx.py` se usa el de `logos.json`
(la variante más frecuente). Las listas y guardias de PDVSA no llevan logo.

## Modelos 2026 que Danilo envió (2026-11-08) — diseño, sin datos
- **Colina, eco abdominal 2026:** logo COLINA verde flotante arriba a la izquierda (5.3 × 2.6 cm), título debajo; misma tabla
  Px | Ci | Edad | Fecha; plantilla B; firma+sello flotante (5.2 × 2.4 cm) sobre el bloque "Dr. … / CIRUJANO PEDIATRA-ECOGRAFISTA /
  MPPS… CMA… / RIF…"; 8 imágenes de 7.9 cm en 2 columnas tras la firma. `informe_desde_modelo.py` lo reconoce (huella Colina)
  y arma bien el informe (probado con datos ficticios).
- **San José, eco abdominal 2026:** ver la fila de San José arriba.
- Los .docx modelo NO se guardan en este repo (público: firma, sello, registros y datos de pacientes). Pedírselos a Danilo
  en cada sesión nueva, o guardarlos en un lugar privado si él lo decide.
