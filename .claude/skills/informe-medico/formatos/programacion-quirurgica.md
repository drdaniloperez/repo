# Formato: Programación quirúrgica semanal (Cirugía Pediátrica)

Aprendido de 2 documentos del disco (06/2023–08/2023), instituciones: Hospital Universitario Dr. Luis Razetti (1, con escudo HULR), sin logo (1).
Estado: **pocos ejemplos** (< 3). Formato descrito con python-docx.

Dos variantes:
- **A. Programación de planes (Razetti)**: una tabla por día (lunes a viernes) con los pacientes a operar ("plan electivo").
- **B. Relación semanal de procedimientos** ("Semana <mes> del <dd-dd>"): una sola tabla N / Nombre / Edad / Teléfono / Procedimiento / Fecha.

Relación: la variante A coincide con lo que la skill `ordenes-medicas-razetti` llama "plan de cirugía/plan electivo";
las órdenes de cada paciente programado se hacen con esa skill.

## Estructura

### A. Programación de planes — Hospital Universitario Dr. Luis Razetti
- Página **carta horizontal** (27.9 × 21.6 cm), márgenes sup/inf 3.0 cm, izq/der 2.5 cm. Fuente Calibri (tema).
- Membrete en el cuerpo (no en el encabezado de Word): **escudo HULR** flotante a la izquierda (≈ 3.9 × 4.3 cm, anclado al
  margen izquierdo, sin ajuste de texto) y, **alineado a la derecha, en azul 4472C4, 16 pt, sin negrita**, tres líneas:
```
                                   HOSPITAL UNIVERSITARIO DR. LUIS RAZETTI BARCELONA, ANZOÁTEGUI
                                                              SERVICIO DE CIRUGÍA PEDIÁTRICA
                                                                                <MES AÑO>
```
- Luego, por cada día: título del día alineado a la derecha, azul 4F81BD 16 pt (el último día salió 548DD4 18 pt):
  `Lunes 19 de Junio de 2023` → `Lunes [DÍA] de [Mes] de [AÑO]`; tras él, la tabla de ese día.
- Tabla del día: 9 columnas, bordes sencillos de 0.5 pt (sz 4) en todo (exterior e interior), sin sombreado, texto 10 pt,
  centrado horizontal y verticalmente. Anchos (cm) aproximados:

| # | NOMBRE Y APELLIDO | CEDULA | EDAD | DIAGNÓSTICO | TIEMPO QUIRÚRGICO | ESPECIALISTA | PREANESTESIA | TELÉFONO |
|---|---|---|---|---|---|---|---|---|
| 0.4 | 3.4–3.6 | 1.5–2.0 | 1.2–1.3 | 5.8–7.3 | 2.5–3.4 | 2.2–2.5 | 2.4–2.6 | 2.2–2.5 |

- Fila de encabezado en mayúsculas, color negro; **solo "NOMBRE Y APELLIDO" va en negrita** (el resto normal). La 1.ª celda vacía.
- Filas: 2–3 pacientes por día, numerados 1, 2, 3 en la 1.ª columna.

### B. Relación semanal de procedimientos (sin logo)
- Carta vertical, tabla "Table Grid" de 6 columnas (anchos ≈ 0.9 / 4.3 / 1.8 / 3.5 / 2.9 / 2.6 cm), sin título ni negritas.
- Encabezado: `N | Nombre | Edad | Teléfono | Procedimiento | Fecha`.
- **Una fila por procedimiento** (N cuenta procedimientos, no pacientes): el paciente con varios procedimientos ocupa varias filas;
  en las siguientes se dejan vacíos Nombre, Edad y Teléfono. Fecha `dd/mm/aaaa` en todas las filas.

## Frases
Variante A (contenido de las celdas):
- CEDULA: `CI No posee` + salto + `HC: [HC]` (niños sin cédula; se anota la historia clínica).
- EDAD: `6` + salto + `años`, `10 meses`, `4 Años`.
- DIAGNÓSTICO numerado dentro de la celda, un ítem por línea: `1. Hernia Umbilical` / `2. Fimosis severa` /
  `2.Hernia inguinal Bilateral C/c Hidrocele derecho` / `2.Adherencia balanoprepusial` / `3. Anillo fimotico` /
  `1. Quiste tirogloso` / `1. MAR: Fistula perianal` / `MAR: Ano anterior` (MAR = malformación anorrectal) /
  `2. Hernia inguinoescrotal derecha`.
- TIEMPO QUIRÚRGICO: `20 MIN`, `30MIN`, `1 HORA`, `1HORA`, `2 HORA` (en mayúsculas, sin plural sistemático).
- ESPECIALISTA: `Dra. [MÉDICO]` / `Dr. [MÉDICO]` — un especialista por día (el mismo para todos los pacientes del día).
- PREANESTESIA: fecha de la evaluación preanestésica `16/6/23` (vacía si aún no se hizo).
- TELÉFONO: `[TELÉFONO]`.
Variante B (procedimientos): `Exceresis de Quiste branquial`, `Hernioplastia umbilical`, `Hernioplastia inguinal derecha`,
`Hernioplastia inguinal izquierda`, `Adherenciolisis balano-prepucial`, `Fimoplastia`, `Fimosectomía`,
`Apendicectomía Abierta`, `Restitución del tránsito gastrointestinal`.

Errores/tipeos a vigilar: "balanoprepusial" (→ balanoprepucial), "Miercoles" sin tilde, "30 HORA" (debe ser 30 MIN),
"Viernes 23 de Junio 2023" (falta "de"), plural "1 HORAS".

## Cierre (Conclusión)
No lleva conclusión ni firma: termina con la tabla del viernes (A) o con la última fila (B).

## Preguntar si falta
- Semana (fechas lunes–viernes) y mes/año del membrete.
- Por paciente: nombre, CI o "No posee" + n.º de historia, edad, diagnósticos (con lateralidad), tiempo quirúrgico estimado,
  especialista del día, fecha de preanestesia, teléfono.
- Qué días hay quirófano y cuántos cupos por día.
- Para la variante B: procedimientos realizados por paciente y su fecha.

## Ejemplo anonimizado
Variante A (para `informe_desde_modelo.py --texto`: líneas con "|" = tabla; "//" separa párrafos dentro de la celda):
```
HOSPITAL UNIVERSITARIO DR. LUIS RAZETTI BARCELONA, ANZOÁTEGUI
SERVICIO DE CIRUGÍA PEDIÁTRICA
NOVIEMBRE 2026
Lunes 9 de Noviembre de 2026
 | NOMBRE Y APELLIDO | CEDULA | EDAD | DIAGNÓSTICO | TIEMPO QUIRÚRGICO | ESPECIALISTA | PREANESTESIA | TELÉFONO
1 | [NOMBRE] | CI No posee // HC: [HC] | 6 // años | 1. Hernia Umbilical // 2. Fimosis severa | 1 HORA | Dr. Pérez | [FECHA] | [TELÉFONO]
2 | [NOMBRE] | CI No posee // HC: [HC] | 3 años | 1. Hernia umbilical // 2. Adherencia balanoprepucial | 30 MIN | Dr. Pérez | [FECHA] | [TELÉFONO]
Martes 10 de Noviembre de 2026
 | NOMBRE Y APELLIDO | CEDULA | EDAD | DIAGNÓSTICO | TIEMPO QUIRÚRGICO | ESPECIALISTA | PREANESTESIA | TELÉFONO
1 | [NOMBRE] | CI No posee // HC: [HC] | 10 // meses | 1. MAR: Fistula perianal | 2 HORA | [MÉDICO] | [FECHA] | [TELÉFONO]
```
Variante B:
```
N | Nombre | Edad | Teléfono | Procedimiento | Fecha
1 | [NOMBRE] | 2 años | [TELÉFONO] | Exceresis de Quiste branquial | [FECHA]
2 | [NOMBRE] | 5 años | [TELÉFONO] | Hernioplastia umbilical | [FECHA]
3 |  |  |  | Fimosectomía | [FECHA]
4 | [NOMBRE] | 7 años | [TELÉFONO] | Apendicectomía Abierta | [FECHA]
```
