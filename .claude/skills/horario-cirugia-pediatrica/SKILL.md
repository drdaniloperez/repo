---
name: horario-cirugia-pediatrica
description: Genera el horario mensual (imagen PNG + PDF con logo PDVSA) de guardias, quirófanos y consultas del servicio de Cirugía Pediátrica del Hospital Jesús Farías (PDVSA), continuando la rotación de guardias. Úsala cuando Danilo pida "el horario/la programación/las guardias de <mes>", "el horario de PDVSA", "haz el horario del próximo mes" o cambie un especialista, día de consulta o la rotación.
---

# Horario de Cirugía Pediátrica — Hospital Jesús Farías (PDVSA)

## Reglas del servicio (4 especialistas: Pérez = Danilo, Santana, Marín, Arreaza)
- **Guardias de 24 h cada 4 días**, orden fijo y continuo entre meses:
  Arreaza → Pérez → Santana → Marín → … (ancla: 1-nov-2026 = Arreaza).
- **Consulta fija, 1 por semana:** lunes Pérez · miércoles Marín · jueves Santana · viernes Arreaza.
- **Martes:** quirófano electivo, sin consulta (la guardia sí corre).
- **Sábado y domingo:** solo guardia.

Todo esto está en `scripts/config.json`; si algo cambia (nuevo especialista, otro día de consulta,
intercambio permanente de guardia), **edita config.json** (si cambia el orden, mueve también el
`ancla` a una fecha con la guardia correcta) y súbelo a la rama principal del cerebro.

## Cómo generar
```bash
python3 .claude/skills/horario-cirugia-pediatrica/scripts/generar_horario.py AÑO MES [N_MESES] --out <scratchpad>/horarios
```
- Escribe HTML y lo convierte a PNG (2×, para WhatsApp) y PDF (imprimir) con `scripts/render.js`
  (Playwright de Node, ya instalado en la nube).
- Revisa el PNG (Read) antes de enviarlo y mándalo con SendUserFile (PNG + PDF).
- **No guardes los horarios generados en el repo** (es público): van al scratchpad.

## Al entregar, comenta
- Reparto del mes (tabla del pie): guardias totales y de fin de semana por especialista; los
  desbalances de 1 se compensan con la rotación.
- Cada especialista cae **una vez cada 4 semanas** en consulta saliendo de guardia (inevitable con
  consulta fija + guardia cada 4 días); dile a Danilo cuál le toca a él (consulta lunes tras guardia domingo).
- Cambios puntuales de un mes (permisos, vacaciones, intercambios): pregúntalos y, si los hay,
  edita el HTML generado de ese mes en vez de config.json.
