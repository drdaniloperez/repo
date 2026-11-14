# Registro de informes ecográficos (versión pública, SIN datos de pacientes)

`informes-ecograficos.csv`: una fila por informe hecho con Claude — `n, fecha (dd/mm/aaaa), centro, estudio`.
Centros: "Clínicas Colina" o "Policlínica San José". Sirve para estadísticas y reportes (por fecha, centro y tipo).

- **No hay nombres ni cédulas** porque este repositorio es público. El Excel completo con nombres
  ("Registro de informes ecograficos.xlsx") lo guarda Danilo en su equipo.
- Si Danilo hace **privado** el repositorio, se puede añadir la columna `paciente` aquí y dejar de depender del Excel local.
- Al terminar cada informe, Claude agrega su fila aquí (commit + push a la rama principal) y, si Danilo sube su Excel,
  también lo actualiza con `.claude/skills/informe-medico/scripts/registro_informes.py agregar`.
- Para un reporte: leer este CSV y resumir (totales por centro, tipo de estudio, mes) o generar el Excel con
  `registro_informes.py crear` (columna Paciente vacía).
