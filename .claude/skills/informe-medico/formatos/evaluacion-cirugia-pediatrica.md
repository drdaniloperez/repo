Aprendido de 3 documentos del disco (03/2025 – 05/2026), instituciones: Centro de Especialidades Médicas Colina (2: emergencia y terapia intensiva), Hospital Jesús Farías PDVSA "HIJF" (1; el logo de ese documento no lo reconoce `logos.json`, el título dice "PDVSA HIJF"). Los 3 son pacientes politraumatizados por accidente de tránsito.

# Formato: Evaluación de Cirugía Pediátrica (interconsulta / evaluación de emergencia)

Nota de interconsulta que deja Danilo cuando lo llaman (emergencia, pediatría o terapia intensiva) a valorar a un niño.
A diferencia de los resúmenes, la identificación va en líneas cortas Px / Ci / Edad / Fecha / hora, y solo las etiquetas
van en negrita. Membrete: logo de la institución (+ logo "DP" en Colina) y firma/sello al final (2–3 imágenes; **no se
copian, las da el modelo**). El bloque de firma aquí es la versión "CIRUJANO PEDIATRA-ECOGRAFISTA".

## Estructura
```
Evaluación de Cirugía Pediátrica [PDVSA HIJF]     ← centrado, negrita (sin subrayado); "PDVSA HIJF" solo en el Hospital Jesús Farías
Px: [NOMBRE]
Ci: <Menor | [CI]>
Edad: [EDAD]
Fecha: [dd/mm/aaaa]
[hora: 9:50am / 10:00pm]
 
Motivo de consulta: accidente de tránsito. (<MOTO-CARRO | CARRO- tipo volcamiento | Colisión autobús- camion>)
Se trata de <adolecente masculino | es femenino> de [EDAD] de edad quien inicia enfermedad actual el [FECHA] a las [hora] aprox. cuando posterior a <mecanismo> … motivo por el cual es trasladado a <centro>, donde se evalua paciente a petición de <servicio de emergencia | servicio de Pediatria | intensivista pediatra, en área de terapia intensiva>, con Diagnóstico: 1.<Paciente politraumatizado | Traumatismos multiples>
1.1 Traumatismo craneoencefálico <Leve|moderado|severo>
1.2 Traumatismo toraco abdominal cerrado A/D
1.3 Traumatismo osteomuscular[ ( fractura de fémur izquierdo)].
Examen Físico:
Paciente en regulares condiciones generales eupneico afebril tolerando O2 ambiente.
Signos vitales: Temperatura: [N]   FC: [N]   FR: [N]   TA: [N/N]mmhg   Sat: [N]%
Piel: …
Cardio-respirstorio: …            (paciente en UCIP: Hemodinámico / Ventilatorio / Infeccioso / Metabolico Renal)
Abdomen: …
Genitales: …
Extremidades: …
Neurológico: …
En vista de condiciones actuales de px, se indica [PLAN:] dieta absoluta, Se solicita Lab: … control cada [N] horas. 
Rx de torax ap y lateral.
Rx de abdomen simple ap y lateral. 
Rx de pelvis centrada en pubis.
<Ecografía fast. | Ecografía abdominal.>
<TAC …>
[Cupo en terapia intensiva pediátrica.]
Posición semisentada, oxigenoterapia, analgesia.
Actualmente sin criterio quirúrgico de emergencia por cirugía pediátrica, avisar al consignar solicitado.

<bloque de firma del modelo, centrado, negrita, sin línea: Dr. Danilo Pérez T. / CIRUJANO PEDIATRA-ECOGRAFISTA / MPPS:[MPPS] CMA: [CMA] / RIF: [RIF]>
```

## Frases
**Enfermedad actual (politrauma)** — literales
- Volcamiento: "… cuando posterior a (volcamiento-carro) sale expedida e impacta con pavimento y arbustos presentando múltiples escoriaciones a nivel facial, tórax anterior y posterior así también en miembros superiores e inferiores ademas de traumatismo cráneo-encefalico Moderado con Glasgow de [N] pts. Perdida de la conciencia, y deformidad en Miembro inferior izquierdo, motivo por el cual es trasladado a centro de especialidades colinas, donde se evalua paciente a petición de servicio de emergencia, con Diagnóstico: …"
- Moto: "… cuando posterior a colisión moto-carro (en condición de parrilero) sale expedido e impacta con vehículo presentando múltiples escoriaciones … ademas de traumatismo cráneo-encefalico severo con Glasgow de [N] pts. Evento emético de contenido hemático y perdida de la conciencia motivo por el cual es trasladado a centro de su localidad y posteriormente a …"
- Colisión: "… cuando posterior a colision (autobus-camion) presenta múltiples escoriaciones a nivel facial  craneal, … traumatismo cráneo-encefalico leve con Glasgow de 15/15pts. Perdida de la conciencia (segun familiar), …"

**Examen físico**
- General: "Paciente en regulares condiciones generales eupneico afebril tolerando O2 ambiente." / UCIP: "Paciente en condiciones de cuidado intubado conectado a ventilación mecánica con parámetros habituales de protección para edad y peso. Bajo sedación"
- Piel: "morena normotermica normohidratada llanado capilar menor 3 seg. Con multpiles escoriación y quemadura por fricción a nivel facial, torácica, miembros superiores e inferiores dispersas." (+ "Cabeza con herida rafiada y vendaje comprensivo." / zonas con medida "(10 x10 cm)")
- Cardio-respirstorio: "tórax simétrico N/E, Rs Rs Ps sin agregados, RsCsRsRs S/s S/g." / "… sin agregados, disminuidos discretamente en ápices pulmonares bilaterales."
- UCIP por sistemas: "Hemodinámico: sin apoyo inotrópico RsCsRsRs sin soplos ni galope" · "Ventilatorio: intubado conectado a ventilación mecánica con parámetros habituales de protección para edad y peso. …" · "Infeccioso: afebril, recibiendo ATB a base de <fármacos> a dosis acorde a edad y peso a través de via venosa central en <sitio> funcional permeables" · "Metabolico Renal: en dieta absoluta con hp y electrolitos a dosis habitual, micciones + evacuaciones –"
- Abdomen normal: "plano, blando, deprimibles, no impresiona doloroso a la palpación profunda, sin signos de irritación peritoneal, no se palpan masas ni megalias, sin escoriaciones ni estigmas, RsHs +."
- Abdomen con trauma: "plano, blando, deprimibles,  impresiona doloroso a la palpación profunda, sin signos de irritación peritoneal, no se palpan masas ni megalias, con escoriaciones en regiones bilaterales del mismo RsHs +."
- Genitales: "normocofigurados de fenotipo fememino." / "se evidencia sonda veisal conectada a bolsa recolectora con orinas claras."
- Extremidades: "asimetricas con deformación de miembro inferior izquierdo (fémur izquierdo), eutróficas sin edema con escoriciones dispersas en miembros superiores e inferiores" / "simetrica, miembro inferior izquierdo (rodilla izquierda) con escoriacion, eutróficas sin edema."
- Neurológico: "somnoliento con respuesta a estímulos dolorosos con pupilas con respuesta a la luz y reflejos presentes." / "activa, vigil, …" / "bajo sedación con pupilas con respuesta a la luz y reflejos presentes."

**Plan** (literal)
- "En vista de condiciones actuales de px, se indica PLAN: dieta absoluta, Se solicita Lab: hematología completa ( cada 4 horas), glicemia, urea, creatinina, tgo, tgp, ggt, amilasa, lipasa, electrolitos séricos, examen de orina, pt y ptt, control cada 6 horas." (variante "control cada 4 horas y luego cada 6.")
- "Rx de torax ap y lateral." "Rx de abdomen simple ap y lateral." "Rx de pelvis centrada en pubis."
- "Ecografía fast." / "Ecografía abdominal."
- "TAC TORACOABDOMINO-PELVICA con contraste." / "TAC TORACOABDOMINO-PELVICA (en vista de mecanismo de acción del trauma)." / "TAC TORACOABDOMINAL con doble contraste."
- "Cupo en terapia intensiva pediátrica."
- "Posición semisentada, oxigenoterapia, analgesia." / "… oxigenoterapia (a criterio de servicio tratante), analgesia."

## Conclusión
Cierra SIEMPRE (3/3) con la frase: **"Actualmente sin criterio quirúrgico de emergencia por cirugía pediátrica, avisar al consignar solicitado."**
Si hubiera criterio quirúrgico, preguntar a Danilo la redacción (no hay ejemplo; en el resumen de ingreso usa
"Resolución quirúrgica oportuna."). El diagnóstico va dentro de la enfermedad actual, numerado "1." + "1.1, 1.2, 1.3".

## Convenciones
- Etiquetas en negrita (Px:, Ci:, Edad:, Fecha:, Examen Físico:, Signos vitales:, Piel:, …); el texto NO va en negrita
  (a diferencia de los resúmenes de ingreso/egreso). Justificado.
- Ci de menores: "Menor". Fecha dd/mm/aaaa y hora en línea aparte ("2:30pm").
- Abreviaturas: A/D, N/E, Rs Rs Ps, RsCsRsRs S/s S/g (ruidos cardiacos rítmicos regulares sin soplo sin galope), RsHs,
  px, Lab, ATB, hp (hidratación parenteral), UCIP, HIJF.
- Tipeos sistemáticos: "Cardio-respirstorio", "llanado capilar", "multpiles escoriación", "normocofigurados",
  "fememino", "escoriciones", "evalua", "adolecente", "es femenino" (falta el grupo etario: usar escolar/adolescente).
- Diferencias por institución: HIJF (PDVSA) añade "PDVSA HIJF" al título, la paciente la pide "servicio de Pediatria";
  Colina: "servicio de emergencia" o "intensivista pediatra".

## Preguntar si falta
- Px, Ci (o Menor), edad, fecha y hora de la evaluación, institución, servicio que solicita la evaluación.
- Mecanismo del trauma (vehículo, volcamiento/colisión, posición: conductor/parrillero/peatón), hora del evento,
  pérdida de conciencia, vómitos, Glasgow, traslados previos.
- Lesiones: escoriaciones/heridas (sitio, tamaño), deformidades/fracturas, sonda vesical, vía central, intubación.
- Signos vitales completos (Temp, FC, FR, TA, Sat).
- Abdomen: dolor, irritación peritoneal, escoriaciones/estigmas.
- Estudios pedidos (Lab y frecuencia de control, Rx, eco FAST, TAC y contraste), cupo UCIP, valoraciones.
- ¿Tiene o no criterio quirúrgico? (frase de cierre).

## Ejemplo anonimizado
```
Evaluación de Cirugía Pediátrica
Px: [NOMBRE]
Ci: Menor
Edad: 8 años
Fecha: [FECHA]
11:00pm
 
Motivo de consulta: accidente de tránsito. (CARRO- tipo colision)
Se trata de escolar masculino de 8 años de edad quien inicia enfermedad actual el [FECHA] a las 9:00 pm aprox. cuando posterior a (colision-carro) presenta múltiples escoriaciones a nivel facial y miembros superiores, ademas de traumatismo cráneo-encefalico leve con Glasgow de 15/15 pts, sin perdida de la conciencia, motivo por el cual es trasladado a centro de especialidades colinas, donde se evalua paciente a petición de servicio de emergencia, con Diagnóstico: 1.Paciente politraumatizado.
1.1 Traumatismo craneoencefálico leve
1.2 Traumatismo toraco abdominal cerrado A/D
1.3 Traumatismo osteomuscular.
Examen Físico:
Paciente en regulares condiciones generales eupneico afebril tolerando O2 ambiente.
Signos vitales: Temperatura: 36.5   FC: 105   FR: 22   TA: 110/70mmhg   Sat: 99%
Piel: morena normotermica normohidratada llanado capilar menor 3 seg. Con multpiles escoriación a nivel facial y miembros superiores dispersas.
Cardio-respirstorio: tórax simétrico N/E, Rs Rs Ps sin agregados, RsCsRsRs S/s S/g.
Abdomen: plano, blando, deprimibles, no impresiona doloroso a la palpación profunda, sin signos de irritación peritoneal, no se palpan masas ni megalias, sin escoriaciones ni estigmas, RsHs +.
Genitales: normocofigurados de fenotipo masculino.
Extremidades: simétricas, eutróficas sin edema con escoriciones dispersas en miembros superiores.
Neurológico: activo, vigil, orientado, con pupilas con respuesta a la luz y reflejos presentes.
En vista de condiciones actuales de px, se indica PLAN: dieta absoluta, Se solicita Lab: hematología completa ( cada 4 horas), glicemia, urea, creatinina, tgo, tgp, ggt, amilasa, lipasa, electrolitos séricos, examen de orina, pt y ptt, control cada 6 horas. 
Rx de torax ap y lateral.
Rx de abdomen simple ap y lateral. 
Rx de pelvis centrada en pubis.
Ecografía fast.
Posición semisentada, oxigenoterapia, analgesia.
Actualmente sin criterio quirúrgico de emergencia por cirugía pediátrica, avisar al consignar solicitado.

Dr. Danilo Pérez T.
CIRUJANO PEDIATRA-ECOGRAFISTA
MPPS:[MPPS] CMA: [CMA]
RIF: [RIF]
```
