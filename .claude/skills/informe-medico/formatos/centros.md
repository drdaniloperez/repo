# Centros y membretes

Danilo informa en tres centros; cada uno tiene su membrete. **El documento final se arma con
`scripts/informe_desde_modelo.py` usando como modelo un informe anterior suyo del mismo centro y tipo**:
así quedan idénticos el logo, la tabla, las fuentes, la firma/sello y el bloque de firma.

| Centro | Cómo se reconoce | Diseño |
|---|---|---|
| **Clínica Colinas** (archivos "COLINA…/colinas…") | Logo COLINA arriba a la izquierda; título a su derecha | Tabla de 1 fila × 4 (Px, Ci, Edad, Fecha) con borde. Texto con etiqueta en negrita. Firma+sello como imagen sobre el nombre. Equipo Mindray (portátil). |
| **Policlínica San José** | Logo SAN JOSÉ centrado arriba; título centrado debajo | Misma tabla. Todo el texto en negrita. |
| **Centro Clínico PDVSA Oriente** | Logo PDVSA arriba a la izquierda; título centrado | Misma tabla. Todo el texto en negrita. Equipo Mindray de carro. |

Bloque de firma (texto, centrado y en negrita, debajo de la imagen de firma y sello): nombre,
"CIRUJANO PEDIATRA-ECOGRAFISTA", registros MPPS/CMA y RIF. Se copia del modelo; no se reescribe.

## Dónde están los modelos
El repositorio del cerebro es **público**: aquí NO se guardan los modelos `.docx` (llevan la firma, el
sello y datos de pacientes). Opciones, en orden de preferencia:
1. Carpeta de modelos en su equipo (p. ej. el disco Rodolfo SSD o `~/informes-modelos/`) en sesiones locales.
2. Que Danilo adjunte un informe anterior del centro en la sesión.
3. Si Danilo hace privado el repositorio, guardar un modelo limpio por centro y tipo en
   `formatos/modelos/` (sin datos de pacientes: se generan con el propio script y datos ficticios).
