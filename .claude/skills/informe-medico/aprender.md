# Modo aprendizaje: estudiar el repertorio completo de informes de Danilo

Objetivo: que la skill sepa redactar **todos** los tipos de documento que Danilo hace, idénticos a los
suyos, y que una sesión en la nube pueda comprobarlo después con `scripts/verificar_skill.py` y
`evaluacion/casos.md`.

Fuente: disco externo **Rodolfo SSD** (subcarpeta que indique Danilo; se mencionó "Alarms", nombre que
pudo llegar mal por dictado). macOS `/Volumes/Rodolfo SSD/...`, Windows `<letra>:\...`.
Si no aparece: `ls /Volumes`, `ls "/Volumes/Rodolfo SSD"` y pregunta.

## Requisitos (sesión local)
- Claude Code en la computadora con el disco conectado, **abierto dentro del clon del cerebro**, en la rama
  principal `claude/zealous-cray-ira4xc` (`git pull` antes de empezar).
- `pip install -r .claude/skills/informe-medico/scripts/requirements.txt` (y LibreOffice para .doc y PDF).
- Leer antes `memoria/informes-eco.md`, `formatos/centros.md` y los formatos ya aprendidos: **se amplían,
  no se rehacen** (vienen de 39 informes reales revisados con Danilo).

## Reglas de privacidad (el repo es PÚBLICO)
- Nunca subir: informes reales, textos extraídos, nombres, cédulas, teléfonos, direcciones, fechas de
  nacimiento, n.º de historia, nombres de otros médicos/colegas, la firma ni el sello de Danilo,
  ni un `.docx` modelo que los contenga.
- Sí se suben: formatos anonimizados (`[NOMBRE]`, `[CI]`, `[EDAD]`, `[FECHA]`, `[MÉDICO]`), logos de
  instituciones (ya están en `formatos/logos/`), estadísticas agregadas.
- Los textos extraídos quedan fuera del repo (`~/informes-extraidos/`).
- Antes de cada commit: `python3 .claude/skills/informe-medico/scripts/verificar_skill.py` debe salir sin
  alertas de privacidad.

## Pasos
1. **Extraer e inventariar** (no leer los archivos uno por uno):
   `python3 .claude/skills/informe-medico/scripts/extraer_textos.py "<carpeta>" --con-imagenes`
   → `~/informes-extraidos/textos/`, `imagenes/`, `inventario.csv` (tipo sugerido por el título, n.º de imágenes).
   Revisa el conteo por tipo; abre los `sin-clasificar`/`ERROR` y reasígnalos. Si aparece un tipo nuevo,
   añade su patrón a `TITULOS_ECO`/`TIPOS` en el extractor.
2. **Identificar institución** de cada documento por su logo (huellas en `formatos/logos/logos.json`):
   Colina, Policlínica San José, Hospital Jesús Farías (PDVSA), Hospital Universitario Dr. Luis Razetti.
   Si aparece otra institución o un logo nuevo, guárdalo en `formatos/logos/` y en `logos.json`
   (con su tamaño y posición) y actualiza `centros.md`. El membrete del **Razetti está provisional**:
   ajústalo con sus informes reales.
3. **Muestrear por tipo**: 10–20 ejemplos variados por tipo (fechas, normales/patológicos, adultos/niños,
   instituciones). Con muchos tipos, un subagente por tipo en paralelo; cada uno devuelve el formato
   destilado y anonimizado.
4. **Destilar cada tipo** en `formatos/<tipo>.md` siguiendo `formatos/_plantilla.md`. Secciones obligatorias
   (las comprueba el verificador):
   `## Estructura`, `## Frases`, `## Conclusión`, `## Preguntar si falta`, `## Ejemplo anonimizado`.
   Incluye: frases literales normales y patológicas, medidas que siempre reporta y su orden, unidades y
   decimales, cómo cierra, recomendaciones típicas y **la lista de datos que la skill debe pedir** cuando
   Danilo no los dicte (medidas, técnica, anestesia, días, hallazgos relacionados, diagnósticos que suele
   añadir según los hallazgos).
   Tipos esperados (según lo que haya): ecos de cada región (abdominal, renal, prostático, partes blandas,
   tiroides/cuello, mamas, pélvico, obstétrico, testicular, inguinal, doppler…), informe médico, informe de
   hospitalización, **extensión de hospitalización**, **informe operatorio / procedimiento quirúrgico**
   (cirugía pediátrica), epicrisis, referencias, constancias, reposos, récipes, lista de pendientes.
5. **Imágenes**: amplía `formatos/eco-imagenes.md` (cantidad y orden por tipo de eco) respetando lo ya
   aprobado en `memoria/informes-eco.md` (todas del mismo tamaño, 2 columnas, 7.9 cm, solo pantalla).
6. **Cobertura**: actualiza `formatos/COBERTURA.md` con una fila por tipo: nº de documentos en el disco,
   nº estudiados, archivo de formato, instituciones donde aparece y estado (aprendido / pocos ejemplos).
   Los tipos con < 3 ejemplos se marcan "pocos ejemplos".
7. **Probar**: genera con datos FICTICIOS al menos un documento de cada tipo con
   `informe_desde_modelo.py` (modelo real del disco, salida fuera del repo) y compáralo con un original:
   estructura, frases, membrete, firma, PDF. Corrige el formato hasta que quede igual.
8. **Validar con Danilo**: muéstrale el resumen de cada formato y los documentos de prueba.
9. **Verificar y persistir**: `verificar_skill.py` sin alertas → commit
   `skill: informe-medico — formatos aprendidos (<tipos>)` y push a `claude/zealous-cray-ira4xc`.
   Al final, deja en `formatos/COBERTURA.md` la fecha del entrenamiento y la ruta de origen (sin datos).
