# Aprendizajes y hechos a recordar

<!-- La skill `recordar` añade entradas aquí con fecha. Formato: - AAAA-MM-DD: hecho -->

- El repositorio del cerebro (drdaniloperez/repo) es **público**: nunca subir datos de pacientes,
  informes reales, la firma ni el sello de Danilo. Solo plantillas/formatos anonimizados.
- 2026-11-05: Danilo hace ecografías en el Centro de Especialidades Médicas Colina, la Policlínica San José
  y el Hospital Jesús Farías de PDVSA (allí pocos ecos). Del Hospital Luis Razetti ya está el logo, pero aún no hay informes de ejemplo
  (membretes en `.claude/skills/informe-medico/formatos/centros.md`).
- 2026-11-07: entrenamiento con el disco Rodolfo SSD (`D:\Alarms\Alarms`, 1.986 archivos; inventario en
  `formatos/COBERTURA.md`). Membrete REAL del Razetti tomado de su programación quirúrgica 2023 (escudo 1953-2022,
  texto azul a la derecha, carta horizontal). Los documentos clínicos (ingreso, egreso, extensión, evaluación, informe)
  los hace sobre todo en Colina, con su logo personal "DP" (no se sube al repo). No hay informes operatorios ni ecos
  obstétricos en el disco. Los .docx del disco traen las imágenes con CRC dañado: abrirlos con `abrir_reparado()`.
- 2026-11-05: Servicio de Cirugía Pediátrica del Hospital Jesús Farías (PDVSA): 4 especialistas (Pérez = Danilo,
  Santana, Marín, Arreaza). Guardias cada 4 días (Arreaza → Pérez → Santana → Marín; 1-nov-2026 = Arreaza),
  consulta fija semanal (lun Pérez, mié Marín, jue Santana, vie Arreaza), martes quirófano electivo sin
  consulta, fines de semana solo guardia. El horario mensual se hace con la skill `horario-cirugia-pediatrica`.
- 2026-11-08: **Modelos .docx de informes de eco (con firma, sello y registros):** no se guardan en este repo porque es
  público, y las sesiones en la nube empiezan de cero. Al pedir un eco, si en la sesión no hay modelo del centro
  (Colina o San José), pedirle a Danilo un eco anterior suyo en Word de ese centro **al inicio**, antes de armar el informe.
  Ya los envió una vez (Colina y San José, eco abdominal 2026) y funcionaron con `informe_desde_modelo.py`.
  Si algún día hace **privado** el repositorio, guardar un modelo por centro en
  `.claude/skills/informe-medico/formatos/modelos/` para no pedirlos más (pendiente de que él decida).
