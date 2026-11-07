# Cobertura del entrenamiento

Lo actualiza el modo aprendizaje (`../aprender.md`); lo lee `../scripts/verificar_skill.py`.
Sin datos de pacientes: solo conteos.

Último entrenamiento: **2026-11-07**, sesión local (Windows), disco **Rodolfo SSD**, carpeta `D:\Alarms\Alarms`
(copia local idéntica). 1.986 archivos: 1.879 ecos, 69 documentos clínicos/administrativos, 22 personales de Danilo
(excluidos: no son plantillas), 2 sin clasificar (un .docx solo con imágenes y un informe escaneado) y 1 hoja de cálculo
no extraída (programación de quirófano .xlsx). Entrenamiento anterior: 2026-11-04/07, nube, 39 informes subidos por Danilo.
"Estudiados" = leídos a fondo; además, en cada tipo se contaron las frases en **todos** sus documentos.

| Tipo | Documentos en el disco | Estudiados | Formato | Instituciones | Estado |
|---|---|---|---|---|---|
| Eco abdominal (+ FAST, pared abdominal, doppler hepático) | 629 | ≈40 | `eco-abdominal.md` | Colina 360, San José 261 | aprendido |
| Eco renal / abdominal con énfasis renal / renal y vesical / doppler renal | 320 | ≈25 | `eco-renal.md` | Colina 177, San José 138, Jesús Farías 3 | aprendido |
| Eco prostático (+ prostático y vesical) | 281 | ≈26 | `eco-prostatico.md` | Colina 272, San José 7 | aprendido |
| Eco piel y partes blandas (± doppler) | 158 | ≈30 | `eco-partes-blandas.md` | San José 82, Colina 73 | aprendido |
| Eco abdominopélvico | 129 | ≈10 | `eco-abdominopelvico.md` | Colina 95, San José 30 | aprendido |
| Eco tiroideo (± doppler) | 125 | ≈20 | `eco-tiroides.md` | Colina 102, San José 23 | aprendido |
| Eco testicular (± doppler) | 95 | 20 | `eco-testicular.md` | Colina 52, San José 43 | aprendido |
| Eco mamario | 70 | ≈15 | `eco-mamario.md` | Colina 35, San José 33 | aprendido |
| Eco vesical (pre/posmiccional) | 51 | ≈25 | `eco-vesical.md` | Colina 43, San José 3 | aprendido |
| Eco pélvico (transabdominal) | 21 | 21 | `eco-pelvico.md` | Colina 11, San José 9 | aprendido |
| Imágenes de los ecos (cantidad y orden por tipo) | 1.879 | conteo de todos | `eco-imagenes.md` | todas | aprendido |
| Resumen de ingreso (Cirugía Pediátrica) | 18 | 18 | `resumen-ingreso.md` | Colina 15, San José 2 | aprendido |
| Informe de egreso / hospitalización | 18 | 18 | `hospitalizacion.md` | Colina 16, San José 1 | aprendido |
| Lista de pacientes por operar | 18 | 6 + conteo | `lista-pendientes-quirurgicos.md` | Jesús Farías (PDVSA) | aprendido |
| Cronograma de guardias y consultas | 7 | 7 | `cronograma-guardia.md` (se genera con la skill `horario-cirugia-pediatrica`) | Jesús Farías (PDVSA) | aprendido |
| Informe médico de Cirugía Pediátrica | 4 | 4 | `informe-medico.md` | Colina 3, San José 1 | aprendido |
| Evaluación de Cirugía Pediátrica (emergencia/interconsulta) | 3 | 3 | `evaluacion-cirugia-pediatrica.md` | Colina 2, Jesús Farías 1 | aprendido |
| Extensión de hospitalización | 2 (el mismo documento) | 2 | `extension-hospitalizacion.md` | Colina | pocos ejemplos |
| Programación quirúrgica semanal | 2 | 2 | `programacion-quirurgica.md` | Razetti 1, sin logo 1 | pocos ejemplos |
| Membrete Hospital Luis Razetti | 1 | 1 | `centros.md` + `logos/hulr-luis-razetti-2022.png` | Razetti | aprendido (membrete real) |
| Balance de ecos realizados | 2 | 2 | `balance-ecos.md` | Colina | pocos ejemplos |
| Solicitud de cortesía | 2 | 2 | `solicitud-cortesia.md` | — | pocos ejemplos |
| Listado de medicamentos e insumos | 2 | 2 | `listado-insumos.md` | Jesús Farías (PDVSA) | pocos ejemplos |
| Solicitud de presupuesto (formulario escaneado) | 2 | 2 | `solicitud-presupuesto.md` | Colina | pocos ejemplos |
| Carta de recomendación | 1 | 1 | `carta-recomendacion.md` | — | pocos ejemplos |
| Morbilidad mensual de consulta | 1 | 1 | `morbilidad.md` | Jesús Farías (PDVSA) | pocos ejemplos |
| Órdenes médicas | 1 | 1 | `ordenes-medicas.md` (Razetti: skill `ordenes-medicas-razetti`) | Colina | pocos ejemplos |
| Informe operatorio / procedimiento quirúrgico | 0 | 0 | — (guía genérica `tipos/procedimiento-quirurgico.md`) | — | pendiente (no hay ejemplos en el disco) |
| Otros ecos (obstétrico, transvaginal) | 0 | 0 | — (guía genérica `tipos/ecosonograma.md`) | — | pendiente (no hay ejemplos en el disco) |

Documentos de prueba (datos ficticios) generados con `scripts/informe_desde_modelo.py` para todos los tipos con
formato, convertidos a PDF y comparados con su original (membrete, estructura, firma); quedaron fuera del repo.
