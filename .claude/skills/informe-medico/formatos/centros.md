# Centros y membretes

Danilo trabaja en cuatro instituciones; cada una tiene su membrete. **El documento final se arma con
`scripts/informe_desde_modelo.py` usando como modelo un informe anterior suyo del mismo centro y tipo**:
así quedan idénticos el logo, la tabla, las fuentes, la firma/sello y el bloque de firma.

| Centro | Cómo se reconoce | Diseño |
|---|---|---|
| **Centro de Especialidades Médicas Colina** (archivos "COLINA…/colinas…") | Logo COLINA arriba a la izquierda; título a su derecha | Tabla de 1 fila × 4 (Px, Ci, Edad, Fecha) con borde. Texto con etiqueta en negrita. Firma+sello como imagen sobre el nombre. Equipo Mindray (portátil). |
| **Policlínica San José** | Logo SAN JOSÉ centrado arriba; título centrado debajo | Misma tabla. Todo el texto en negrita. |
| **Hospital Jesús Farías (PDVSA)** — donde trabaja; pocos ecos allí | Logo PDVSA arriba a la izquierda; título centrado | Misma tabla. Todo el texto en negrita. Equipo Mindray de carro. |
| **Hospital Universitario Dr. Luis Razetti** (Barcelona, Anzoátegui) — servicio de Cirugía Pediátrica | Escudo H.U.L.R. (logo ya guardado) | ⚠ Diseño PROVISIONAL (logo 2.6 cm a la izquierda, título al lado): aún no hay informes de ejemplo; pedirlos y ajustar. |

Bloque de firma (texto, centrado y en negrita, debajo de la imagen de firma y sello): nombre,
"CIRUJANO PEDIATRA-ECOGRAFISTA", registros MPPS/CMA y RIF. Se copia del modelo; no se reescribe.

## Logos (cada institución con el suyo — nunca mezclar)
Guardados en `formatos/logos/` (son públicos; la firma y el sello NO se guardan aquí):
| Archivo | Institución | Tamaño y posición en sus informes |
|---|---|---|
| `colinas.png` | COLINA — Centro de Especialidades Médicas | 4.8 × 2.3 cm, arriba a la izquierda, título a la derecha |
| `pdvsa-jesus-farias.png` | Hospital Jesús Farías (PDVSA) — logo oficial que envió Danilo, alta resolución | 6.0 × 1.7 cm, arriba a la izquierda, título centrado debajo |
| `san-jose.png` | Policlínica San José | 8.9 × 1.4 cm, centrado, título centrado debajo |
| `hulr-luis-razetti.png` | Hospital Universitario Dr. Luis Razetti | 2.6 × 2.6 cm, arriba a la izquierda, título a la derecha (provisional) |

`logos.json` guarda además la huella (md5) del logo tal como está dentro de sus .docx:
- `informe_desde_modelo.py` reconoce la institución del modelo por su logo y **se detiene si no es la
  institución del estudio** (`--centro` o `"centro"` en datos.json).
- `armar_informe_docx.py --centro <x>` arma el membrete con el logo correcto cuando no hay modelo.

**Cómo saber la institución del estudio:** lo dice Danilo; si no, se deduce del encabezado de la
pantalla del ecógrafo en las fotos ("CENTRO DE ESPECIALIDADES M…" = Colina, "CENTRO CLINICO PDVSA
ORIENTE" = Hospital Jesús Farías (PDVSA), "POLICLINICA SAN JOSE" = San José) y **se confirma con él antes de generar**.
Hay dos versiones de su imagen de firma y sello; en partes blandas usa la segunda (la da el modelo).

## Dónde están los modelos
El repositorio del cerebro es **público**: aquí NO se guardan los modelos `.docx` (llevan la firma, el
sello y datos de pacientes). Opciones, en orden de preferencia:
1. Carpeta de modelos en su equipo (p. ej. el disco Rodolfo SSD o `~/informes-modelos/`) en sesiones locales.
2. Que Danilo adjunte un informe anterior del centro en la sesión.
3. Si Danilo hace privado el repositorio, guardar un modelo limpio por centro y tipo en
   `formatos/modelos/` (sin datos de pacientes: se generan con el propio script y datos ficticios).
