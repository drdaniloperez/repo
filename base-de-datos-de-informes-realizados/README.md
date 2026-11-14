# Base de datos de informes realizados

Informes ecográficos hechos con Claude, **clasificados por clínica** (Danilo indica en cada informe cuál es):

| Archivo | Clínica |
|---|---|
| `clinicas-colina.csv` | Clínicas Colina (Centro de Especialidades Médicas Colina) |
| `policlinica-san-jose.csv` | Policlínica San José |

Columnas: `n` (correlativo por clínica), `fecha` (dd/mm/aaaa, fecha del estudio), `estudio` (tipo de eco:
Abdominal, Abdominal con énfasis renal, Abdominopélvico, Renal, Vesical, Prostático, Tiroideo, Mamario,
Partes blandas, Pélvico, Testicular…).

- **Sin nombres ni cédulas**: este repositorio es público. El Excel con nombres
  ("Base de datos de informes realizados.xlsx") lo guarda Danilo en su equipo; si hace privado el repo, se añade la
  columna `paciente` aquí.
- **Tras cada informe final**: añadir la fila en el CSV de su clínica, commit y push a la rama principal.
- **Reportes**: leer los CSV y resumir (totales por clínica, tipo de estudio, mes) o generar el Excel con
  `.claude/skills/informe-medico/scripts/registro_informes.py crear`.
