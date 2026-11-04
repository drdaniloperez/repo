# Modo aprendizaje: estudiar los informes de ejemplo de Danilo

Fuente: disco externo **Rodolfo SSD**, subcarpeta **Alarms** (más de 1000 archivos: informes médicos,
ecos, hospitalización, extensión de hospitalización, procedimientos quirúrgicos, etc.).
Rutas típicas: macOS `/Volumes/Rodolfo SSD/Alarms`, Windows `<letra>:\Alarms`.
Si no aparece, búscala (`ls /Volumes`, `ls "/Volumes/Rodolfo SSD"`) y confirma el nombre con Danilo
(el nombre "Alarms" pudo llegar mal por dictado).

## Requisito: acceso al disco
- **Sesión local** (Claude Code en la computadora con el disco conectado): acceso directo.
- **Sesión en la nube**: solo si Danilo comparte esa carpeta por Remote Control
  (`list_computer_folders` → `request_computer_folder`). Si no está disponible, dile que ejecute este
  modo desde Claude Code en su computadora, o que suba una muestra de archivos a la sesión.

## Pasos
1. **Extraer e inventariar** (no leer 1000 archivos a mano):
   `python3 .claude/skills/informe-medico/scripts/extraer_textos.py "<carpeta>"`
   → `~/informes-extraidos/textos/` + `inventario.csv` con un tipo sugerido por archivo.
   Revisa el conteo por tipo y los `sin-clasificar`/`ERROR` (abre algunos y reasigna).
2. **Muestrear por tipo**: de cada tipo lee 10–20 ejemplos variados (fechas distintas, normales y
   patológicos). Usa subagentes en paralelo, uno por tipo, si hay muchos tipos.
3. **Destilar el formato** de cada tipo en `formatos/<tipo>.md` (usa `formatos/_plantilla.md`):
   - Estructura exacta: encabezado, título, bloque de identificación, secciones en orden, cierre y firma.
   - Frases fijas literales que se repiten (descripciones normales de cada órgano, frases de cierre).
   - Variantes patológicas frecuentes con su redacción típica.
   - Convenciones: mayúsculas, viñetas/numeración, unidades, decimales (coma o punto), abreviaturas.
   - Medidas que siempre reporta y en qué orden; valores de referencia que él cita.
   - Cómo redacta la conclusión/impresión diagnóstica y las recomendaciones.
   - 1–2 ejemplos completos **anonimizados**.
4. **Anonimizar SIEMPRE** antes de escribir en el repo: nombres, cédulas, fechas de nacimiento,
   teléfonos, direcciones, n.º de historia, nombres de otros médicos o pacientes → `[NOMBRE]`,
   `[CI]`, `[EDAD]`, `[FECHA]`, etc. Revisa con `grep` que no quede ningún dato real. Los textos
   extraídos (`~/informes-extraidos`) no se suben nunca.
5. **Validar con Danilo**: muéstrale el resumen de cada formato y un informe de prueba generado con
   datos ficticios; ajusta lo que diga.
6. **Persistir**: commit `skill: informe-medico — formatos aprendidos (<tipos>)` y push a la rama
   principal del cerebro (ver `CLAUDE.md`).
