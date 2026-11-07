# Batería de evaluación de la skill informe-medico

Para comprobar, desde cualquier sesión (sobre todo la de la nube, tras el entrenamiento local), que la skill
quedó bien entrenada. **Todos los pacientes son ficticios.**

## Cómo se evalúa
1. `python3 .claude/skills/informe-medico/scripts/verificar_skill.py` → sin ✗; los ⚠ de cobertura deben
   corresponder solo a tipos que de verdad tienen pocos ejemplos.
2. Para cada caso, seguir la skill **como si Danilo lo dictara** y anotar:
   - **F** formato: usa `formatos/<tipo>.md` aprendido (no la guía genérica) y la institución correcta (logo).
   - **P** preguntas: pide en una sola ronda numerada TODO lo marcado en "debe preguntar", sin inventar.
   - **D** diagnósticos: propone los marcados en "debe sugerir".
   - **E** errores: detecta los marcados en "debe detectar".
   - **R** redacción: tras responder las preguntas con los datos de "respuestas", el texto usa sus frases
     literales, orden, unidades y cierre; y se genera **PDF** con membrete y firma (si hay modelo).
3. Un caso aprueba con F, P, D, E y R correctos. La skill está lista cuando aprueban todos los casos de los
   tipos que COBERTURA.md marca como "aprendido". Registrar el resultado al final de este archivo.

---

### C1 · Eco abdominal adulto incompleto (Colina)
Dictado: "Eco abdominal, Colina, paciente femenina de 47 años, hígado graso, barro biliar, riñones normales, edema interasas."
- Debe preguntar: nombre, CI, fecha; grado de hígado graso; medidas de hígado (LD, LI), vesícula, páncreas (3), riñones, bazo; paredes vesiculares; colitis leve o moderada.
- Debe sugerir: Hígado Graso Grado _; Vesícula con paredes engrosadas y barro biliar; Colitis _.
- Respuestas: "Ana Prueba, CI 00.000.000, 05/11/2026, grado I, LD 13.2 LI 6.1, vesícula 5.0 x 2.4 paredes engrosadas, páncreas 2.0 1.5 1.8, RD 10.1 x 4.9, RI 10.4 x 5.2, bazo 9.8 x 4.1, colitis moderada".

### C2 · Eco abdominal pediátrico con énfasis renal (San José)
Dictado: "Eco abdominal con énfasis renal en San José, niño de 1 año 3 meses, pielocalectasia bilateral moderada con uréter proximal dilatado."
- Debe preguntar: medidas (hígado, vesícula, riñones, bazo), vejiga (volumen), CI ("menor").
- Debe sugerir: Reflujo vesicoureteral bilateral grado _; Pielocalectasia bilateral moderada.
- F: frases pediátricas ("acorde a edad"), todo en negrita (formato San José), logo San José centrado.

### C3 · Eco prostático con incoherencia
Dictado: "Prostático, 68 años, próstata de 5.0 x 4.6 x 5.4, bordes irregulares, calcificaciones, deforma piso vesical, IPP 1.2, conclusión normal."
- Debe calcular: volumen ≈ 65 cm³ (× 0.52) y avisar que el de pantalla tiene prioridad.
- Debe detectar: conclusión "normal" incoherente con próstata aumentada de ~65 cm³ que deforma el piso vesical.
- Debe sugerir: Hiperplasia prostática grado III (según la escala de su formato; pedir confirmación).

### C4 · Partes blandas: hernia umbilical pediátrica
Dictado: "Partes blandas, niña de 6 años, hernia umbilical."
- Debe preguntar: tamaño del defecto aponeurótico, contenido (epiplón), dolor, Valsalva.
- R: plantilla literal de hernia umbilical; "Se sugiere valoración por cirugía Pediatrica."

### C5 · Eco con fotos de pantalla
Entrada: 4–8 fotos del teléfono de un estudio (pueden reutilizarse fotos de prueba de Danilo si las autoriza, nunca subirlas al repo).
- Debe: recortar cada foto, revisarla a la vista, corregir con esquinas las que traigan marco; ordenarlas; leer las medidas; tabla pantalla vs. dictado; imágenes del **mismo tamaño**, 2 columnas, 7.9 cm, completas; PDF + vista previa.

### C6 · Agregar imágenes a un informe ya redactado
Entrada: un .docx suyo + fotos.
- Debe: usar `agregar_imagenes.py` (no reescribir el texto), detectar medidas que no coinciden y órganos fotografiados sin párrafo; si añade texto, reanclar la firma; entregar PDF.

### C7 · Eco de tiroides (si COBERTURA lo marca aprendido)
Dictado: "Tiroides, mujer de 35 años, nódulo en lóbulo derecho de 1.2 cm, hipoecoico."
- Debe preguntar: medidas de ambos lóbulos e istmo, volumen, composición, márgenes, forma, focos ecogénicos, vascularidad, adenopatías.
- Debe sugerir: categoría ACR TI-RADS con puntos y conducta (PAAF/control) según tamaño.

### C8 · Eco obstétrico (si aprendido)
Dictado: "Obstétrico, FUR 10/06/2026, feto único, FCF 145."
- Debe preguntar: biometría (DBP, CC, CA, LF), presentación, placenta, líquido amniótico, sexo si lo quiere.
- Debe calcular: EG por FUR y por biometría, FPP; avisar discordancias.

### C9 · Eco pélvico / testicular / inguinal / doppler (si aprendido)
Un dictado breve por tipo; debe pedir las medidas y hallazgos propios de su formato aprendido.

### C10 · Informe médico (Razetti o Jesús Farías)
Dictado: "Informe médico para el seguro, niño de 8 años con hernia inguinal derecha, necesita herniorrafia."
- Debe preguntar: institución, nombre, CI del representante si lo usa, tiempo de evolución, examen físico, estudios (eco), procedimiento solicitado, plan.
- F: formato aprendido de informe médico y membrete de la institución (Razetti: no usar el provisional si ya hay uno real).

### C11 · Informe de hospitalización
Dictado: "Hospitalización, apendicitis perforada, niña de 10 años, operada ayer."
- Debe preguntar: fechas de ingreso/cirugía, días de estancia, evolución, antibióticos (dosis/vía), paraclínicos, plan, condición actual.
- Debe sugerir: diagnósticos implícitos (peritonitis localizada/generalizada si se describe, etc.).

### C12 · Extensión de hospitalización
Dictado: "Extensión de hospitalización, 3 días más, sigue con antibiótico endovenoso."
- Debe preguntar: paciente, fecha de ingreso, días ya aprobados, diagnóstico, evolución y paraclínicos recientes, **justificación** de la permanencia.
- R: su formato aprendido de extensión (el que revisa el seguro).

### C13 · Informe operatorio de cirugía pediátrica, varios procedimientos
Dictado: "Operatorio: herniorrafia umbilical más frenectomía lingual, niño de 4 años, sin complicaciones."
- Debe preguntar: fecha, peso, anestesia, equipo, diámetro del anillo, contenido del saco, técnica y sutura de cada procedimiento, sangrado, condición de egreso.
- E: confirmar "sin complicaciones" antes de escribirlo; describir cada procedimiento por separado.

### C14 · Constancia / reposo
Dictado: "Reposo de 5 días desde hoy."
- Debe preguntar: paciente, diagnóstico, institución; calcular la fecha final.

### C15 · Privacidad
Tras cualquier caso, `git status` no debe mostrar archivos con datos de pacientes, y `verificar_skill.py` debe salir sin alertas de privacidad.

---

## Registro de evaluaciones
| Fecha | Sesión | Casos aprobados | Fallos / ajustes hechos |
|---|---|---|---|
