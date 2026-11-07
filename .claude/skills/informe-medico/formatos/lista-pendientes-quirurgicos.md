# Formato: Lista de pacientes pendientes por operar (Cirugía Pediátrica)

Aprendido de 19 documentos: 1 inicial + 18 versiones del disco (02/2025–07/2025), instituciones: Hospital Jesús Farías (PDVSA Oriente, Barcelona) — los .docx no llevan logo. (ampliado 2026-11-07, disco)

Aprendido de 1 documento (Hospital Jesús Farías, PDVSA Oriente). Lista de trabajo, no informe.

## Estructura
```
Pacientes pendientes por operar Cirugía Pediátrica
 <Centro> <Ciudad> <dd/mm/aaaa>
<Dra. X/ Dra. Y/ Dr. Pérez./ Dr. Z.>

<N>. <Nombre Apellido>		<edad: N años / N meses>		<Diagnóstico 1 + Diagnóstico 2 + …>
Tlfno: <teléfono(s)>
[nota: p. ej. anestesiólogo asignado]
```
(ampliado 2026-11-07, disco)
- Es **un solo documento vivo** que se va copiando y actualizando (16 pacientes en 02/2025 → ≈ 75 en 07/2025). Las versiones
  se nombran por fecha y estado: "ACT"/"ACTUALIZADA" (se añadieron pacientes), "DEPURADA" (se quitaron operados/duplicados).
- Formato real (python-docx): carta vertical, Calibri 11, sin tablas ni negritas. Las 3 líneas del encabezado van
  **centradas y resaltadas en amarillo**. Columnas separadas con tabulaciones (o muchos espacios en las entradas añadidas después).
- Línea 3 (equipo): `Dra. [MÉDICO]/ Dra. [MÉDICO]/ Dr. Pérez./ Dr [MÉDICO].` — los 4 especialistas del servicio (desde 03/2025; en 02/2025 eran 3).
- Numeración: los primeros 13–19 pacientes usan la **numeración automática de Word** (no se ve en el texto extraído) y los
  añadidos después llevan el número tecleado (`33.`, `40. `), por eso hay saltos y repetidos al depurar.
- ⚠ La fecha del encabezado muchas veces NO se actualiza (archivos de 04/2025 y 05/2025 conservan "27/03/2025"): al generar, poner la fecha de hoy.

### Listas por grupo (consulta de pediatría y anestesia)
Sub-listas de ≈ 20 pacientes tomadas de la lista general para citarlos a evaluación preoperatoria (pediatría + anestesia) un día concreto:
```
Grupo 2 jueves 29 Px pendientes por operar Cirugía Pediátrica
 PDVSA Oriente Barcelona
                                                     ← sin fecha completa ni línea de cirujanos
1.[Nombre Apellido]          [edad]          [Diagnósticos]
Tlfno: [TELÉFONO]
…
20.[Nombre Apellido]   …
```
- Encabezado: `Grupo <N> <día de la semana> <día> Px pendientes por operar Cirugía Pediátrica` (amarillo, centrado), numeración 1–20 reiniciada.
- Archivo: "Grupo 2 jueves 29 PX por operar consulta pediatria y anestesia C-P PDVSA". Existieron al menos grupo 2 (jueves) y grupo 3 (viernes).
- El orden sigue el de la lista general (los más antiguos primero).

## Frases
- Numeración consecutiva; diagnósticos unidos con "+" y abreviaturas propias: ABP (adenoamigdalectomía/
  ⚠ confirmar significado), HIB (hernia inguinal bilateral), c/c (complicado con).
- Diagnósticos frecuentes: hernia umbilical, supraumbilical, inguinal (izq/der/bilateral), fimosis/anillo
  fimótico, anquiloglosia, testículo en ascensor, criptorquidia, hidrocele, cicatriz queloide.
- Al añadir pacientes: revisar duplicados y numeración (en el ejemplo hay números repetidos: 36, 37).

### Frases y abreviaturas del disco (ampliado 2026-11-07, disco) — frecuencia de cada diagnóstico en las 18 versiones
- ⚠ en el disco también aparece que **ABP = adherencias balanoprepuciales** (no adenoamigdalectomía): solo figura en varones,
  junto a fimosis/anillo fimótico, y en la morbilidad del mismo servicio se escribe "liberación de ABP" / "liberación de
  adherencias bp"; en la programación del Razetti aparece "Adherencia balanoprepucial". Confirmar con Danilo.
- Abreviaturas: `HU` (hernia umbilical, 57), `HIB` (hernia inguinal bilateral), `c/c` (complicado con), `Izq` / `Der`,
  `Supra` o `Supra Umbilical` (hernia supraumbilical), `test en ascensor` (testículo), `LOE` (lesión ocupante de espacio), `Tlfno`.
- Diagnósticos (conteo de apariciones acumuladas): Hernia Umbilical (≈ 720) · ABP (174) · Anillo fimotico (80) · Anquiloglosia (77 + 17 "Aquiloglosia") ·
  Supra umbilical / Supraumbilical / Hernia Supraumbilical (≈ 185) · Hernia inguinal bilateral (≈ 100) · Fimosis severa (41) ·
  Prepucio redundante (26) · Cicatriz patológica Queloide (17) · Hernia Inguinal Izq (17) · Criptorquidea recidivante (16) ·
  Fimosis c/c Balanitis (15) · Testículo(s) en ascensor [bilateral] (≈ 55) · Apéndices preauriculares bilateral + fistula preauricular der (15) ·
  Hidrocele der/derecho (26) · Hernia umbilical dolorosa (12) · Hernia umbilical recidivante dolorosa (8) · Litiasis vesicular + obesidad (10) ·
  Sinequia de labios menores (6) · Seno preauricular bilateral (6) · Estenosis meato uretral (4) · Verrugas (4).
- Comorbilidad o dato relevante al final del diagnóstico, a veces en MAYÚSCULAS: `AGENESIA RENAL`, `autismo`, `obesidad`.
- Nota de anestesia: `Dra [MÉDICO] ANESTESIOLOGO` en línea propia o tras `Tlfno:`.
- Teléfonos: `Tlfno [TELÉFONO]`, `Tlfno: [TELÉFONO]- [TELÉFONO]` o `/` para dos números; si no se tiene, queda `Tlfno` vacío.
- Edad: `5 Años`, `7 años.`, `11 meses`, `5 meses`.

## Conclusión
No lleva conclusión: termina con el último paciente. Si se entrega impresa, puede llevar fecha de actualización.
(ampliado 2026-11-07, disco) Tampoco lleva firma. Cierre = último paciente (a veces con su línea `Tlfno` vacía).
**Depuración** (lo que hace en las versiones "DEPURADA"): quitar los ya operados (en la morbilidad aparecen como POM/POT),
quitar duplicados (mismo nombre en dos posiciones), completar teléfonos, renumerar. Una lista depurada pasa de ~42 a ~40
entradas; las actualizadas añaden al final.

## Preguntar si falta
Edad, diagnóstico(s) completos con lateralidad, teléfono del representante, especialista o anestesiólogo asignado.
(ampliado 2026-11-07, disco)
- Si es la lista general o un **grupo** (número de grupo, día de la semana y fecha de la consulta).
- Qué pacientes ya se operaron (para depurar) y si hay duplicados.
- Fecha de actualización del encabezado; equipo de cirujanos de la línea 3.
- Comorbilidades que quiera destacar (agenesia renal, obesidad, autismo…).

## Ejemplo anonimizado
```
Pacientes pendientes por operar Cirugía Pediátrica
 PDVSA Oriente Barcelona [FECHA]
[MÉDICO]/ [MÉDICO]/ Dr. Pérez./ [MÉDICO]

1. [NOMBRE]		5 años		Hernia Umbilical + Fimosis Severa
Tlfno: [TELÉFONO]
2. [NOMBRE]		11 meses		Hernia Umbilical + Anquiloglosia + ABP
Tlfno: [TELÉFONO]
```
Ejemplo de grupo (ampliado 2026-11-07, disco):
```
Grupo 3 viernes [DÍA] Px pendientes por operar Cirugía Pediátrica
 PDVSA Oriente Barcelona

1. [NOMBRE]            4 años.            Hernia umbilical+ supra umbilical+ anillo fimotico
Tlfno: [TELÉFONO]
2. [NOMBRE]            6 años.            Hernia umbilical + HIB + ABP
Tlfno: [TELÉFONO]
3. [NOMBRE]            8 meses            Hernia Umbilical + Testiculo en ascensor Bilateral
Tlfno
```
