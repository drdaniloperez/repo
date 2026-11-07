# Formato: Cronograma mensual de guardias y consultas (Cirugía Pediátrica PDVSA)

Aprendido de 7 documentos del disco (07/2025–05/2026: jul-2025, nov-2025, dic-2025, feb-2026 ×2, mar-2026, may-2026), instituciones: Hospital Jesús Farías (PDVSA Oriente) — .docx sin logo reconocido (uno trae logo pequeño).

**Para generarlo usar la skill `horario-cirugia-pediatrica`** (PNG + PDF con logo PDVSA, rotación en `scripts/config.json`).
Los colegas van como [MÉDICO A/B/C] (regla de privacidad de `aprender.md`); sus nombres reales están en `config.json` de esa skill.
Este archivo documenta cómo los hacía Danilo a mano en Word, para comprobar que la skill coincide.

### ¿Coincide con la skill horario-cirugia-pediatrica?
- **Rotación de guardia: SÍ, en los 7.** Una guardia de 24 h cada día, rotando entre los 4 en el orden
  [MÉDICO A] → Pérez → [MÉDICO B] → [MÉDICO C]. Comprobado contra el ancla de config.json (1-nov-2026 = [MÉDICO A]):
  1-jul-2025 [MÉDICO A], 1-nov-2025 [MÉDICO C], 1-dic-2025 Pérez, 1-feb-2026 [MÉDICO C], 1-mar-2026 [MÉDICO C], 1-may-2026 [MÉDICO A] → todos cuadran.
- **Consultas: SÍ desde nov-2025**: lunes Pérez · martes QUIROFANO (sin consulta) · miércoles [MÉDICO C] · jueves [MÉDICO B] ·
  viernes [MÉDICO A] · sábado y domingo solo guardia.
- ⚠ **Julio 2025 era distinto**: lunes Pérez · martes [MÉDICO C] · miércoles [MÉDICO A] · jueves [MÉDICO B] · viernes sin consulta,
  sin día de quirófano. Si Danilo pide un mes antiguo, no aplicar la regla actual.
- Excepción vista: diciembre 2025 sin consultas del 22 al 31 (vacaciones), solo guardias. La skill debe preguntar por feriados/vacaciones.

## Estructura
Plantilla de calendario descargada (iCalendario.net; julio de calendario-ok.com) pegada en Word:
- Página horizontal: carta (27.9 × 21.6 cm) o A4 horizontal (nov-2025, jul-2025).
- Título en una línea arriba, con orden variable: `PDVSA CIRUGÍA PEDIÁTRICA Febrero 2026` / `CIRUGÍA PEDIATRÍCA PDVSA Marzo2026` /
  `Cirugía Pediátrica Mayo2026 PDVSA` / `Guardia Cirugía Pediátrica Diciembre 2025 PDVSA` / `NOVIEMBRE CIRUGÍA PEDIÁTRICA 2025 Pdvsa.`
- Una tabla de 7 columnas (Lunes … Domingo) y 6–7 filas (semanas). Cada celda: número del día y debajo
  `G: <apellido>` y `C: <apellido>` o `QUIROFANO` (martes).
- Las celdas de días de otro mes (antes del 1 o después del último) se usan para el **cuadro de especialistas**:
  `Especialistas` y cada uno `Dra [MÉDICO A]` + `[TELÉFONO]`, `Dra [MÉDICO C]` + `[TELÉFONO]`, `Dr [MÉDICO B]` + `[TELÉFONO]`, `Dr Pérez` + `[TELÉFONO]`.
- Leyenda opcional: `G=Guardia` `C= Consulta` (o `G: Guardia` / `C: Consulta`).
- Colores de la plantilla (cabecera gris 7f7f7f / roja e43947 / turquesa 7cc8cb según el mes), texto 14–16 pt.
- Queda el pie de la plantilla "iCalendario.net" (borrarlo).

## Frases
- Celda de lunes: `G: Pérez` / `C: Pérez` (o con título: `G:Dr Perez` / `C:Dr Perez`).
- Celda de martes: `QUIROFANO` + `G: <apellido>`.
- Fin de semana: solo `G: <apellido>`.
- Con o sin título ("Dra [MÉDICO A]", "Dra [MÉDICO C]", "Dr [MÉDICO B]", "Dr Pérez"); en marzo y mayo 2026 solo apellidos.

Errores/tipeos a vigilar: "Dra Pérez", "Dr [MÉDICO C]", "Dr [MÉDICO A]", "Dra [MÉDICO B]" (género cambiado), "Dra[MÉDICO A]" pegado,
"Qirofano", "C:De [MÉDICO B]", "PEDIATRÍCA" con tilde mal puesta, "Marzo2026" sin espacio, celdas con `C` vacía.

## Cierre (Conclusión)
Sin conclusión ni firma: termina con la última semana del mes y el cuadro de especialistas. Al entregar, la skill comenta
el reparto (guardias totales y de fin de semana por especialista).

## Preguntar si falta
- Mes y año.
- Cambios puntuales: permisos, vacaciones, intercambios de guardia, feriados (p. ej. sin consultas en Navidad).
- Si cambió algún día de consulta o el día de quirófano, o entró/salió un especialista (→ editar config.json de la skill).
- Si quiere teléfonos en el cuadro de especialistas (no guardarlos en el repo).

## Ejemplo anonimizado
```
CIRUGÍA PEDIÁTRICA PDVSA Noviembre 2026
Lunes        | Martes        | Miércoles    | Jueves       | Viernes      | Sábado       | Domingo
26 Especialistas | 27 Dra [MÉDICO A] [TELÉFONO] | 28 Dra [MÉDICO C] [TELÉFONO] | 29 Dr [MÉDICO B] [TELÉFONO] | 30 Dr Pérez [TELÉFONO] | 31 G=Guardia C=Consulta | 1 G: [MÉDICO A]
2 C: Pérez G: Pérez | 3 QUIROFANO G: [MÉDICO B] | 4 C: [MÉDICO C] G: [MÉDICO C] | 5 C: [MÉDICO B] G: [MÉDICO A] | 6 C: [MÉDICO A] G: Pérez | 7 G: [MÉDICO B] | 8 G: [MÉDICO C]
9 C: Pérez G: [MÉDICO A] | 10 QUIROFANO G: Pérez | …
```
