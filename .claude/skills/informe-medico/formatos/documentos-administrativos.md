# Formato: Documentos administrativos y de servicio (varios tipos)

Aprendido de 11 documentos del disco (05/2025–09/2026), instituciones: Centro de Especialidades Médicas Colina (balance-ecos 2, ordenes-medicas 1, solicitud-presupuesto 2 con formulario de Colina), Hospital Jesús Farías / PDVSA Oriente (listado-insumos 2, morbilidad 1), dirigidos a otras clínicas (solicitud-cortesia 2, carta-recomendacion 1).
Estado: **pocos ejemplos** en todos (1–2 por tipo). Cada tipo tiene además un archivo corto `formatos/<tipo>.md` que remite aquí.

| Tipo | Docs | Fechas | Institución | Imágenes |
|---|---|---|---|---|
| balance-ecos | 2 | 09/2025, 11/2025 | Colina (logo COLINA) | logo + firma/sello |
| solicitud-cortesia | 2 | 09/2026 | dirigido a clínicas de Puerto La Cruz | firma (1 de 2) |
| listado-insumos | 2 | sin fecha | PDVSA Oriente | ninguna |
| solicitud-presupuesto | 2 | 05/2025 | formulario de Colina escaneado | 1 imagen de página completa |
| carta-recomendacion | 1 | 10/2025 | firmada por otro cirujano pediatra | sello/firma |
| morbilidad | 1 | junio (2025) | PDVSA Oriente | ninguna |
| ordenes-medicas | 1 | 05/2025 | Colina (logo COLINA) | logo + firma/sello |

## Estructura

### balance-ecos
Relación de ecografías hechas en una jornada para un convenio/empresa, para cobrar. Todo **centrado y en negrita**, logo COLINA.
```
Ecos Realizados [dd/mm/aa]
<CONVENIO> / CLINICA COLINA

[NOMBRE] [CI] Eco <tipo>[ /Eco <tipo>].
[NOMBRE] [CI] Eco abdominal y Eco prostatico.
…

Total: <N> estudios.

Dr. Danilo Pérez T.
CIRUJANO PEDIATRA-ECOGRAFISTA
MPPS:[MPPS] CMA: [CMA]
RIF: [RIF]
```
- El total cuenta **estudios, no pacientes** (un paciente con 2 ecos suma 2). En el disco: 12 pacientes → 14 estudios; 7 pacientes → 14 estudios.
- Convenios vistos: empresas/aseguradoras (nombre corto en mayúsculas o "Fasme-cumana").

### solicitud-cortesia
Carta de Danilo pidiendo "cortesía" (privilegios para operar/atender) en una clínica privada. Fuente 14 pt.
```
Solicitud de cortesía                                  (centrado)

                                    Puerto La Cruz [d/m/aa]   (derecha)

Dirección medica, <Clínica>.
Dr(a) [MÉDICO].

Yo Dr. Danilo Pérez, Cirujano Pediatra CI. [CI]. Presento la intención de solicitar la cortesía en <Clínica>. Consignando los requisitos solicitados para su revisión, agradeciendo de antemano colaboración con lo solicitado.   (justificado)

                    Danilo Pérez Torres.               (centrado, con firma encima)
                    Cirujano Pediatra.
                    CI.[CI]
```

### listado-insumos
Lista de medicamentos e insumos que el representante debe traer para la cirugía pediátrica (PDVSA). Fuente 14 pt.
```
Listado de medicamentos e insumos para cirugía pediátrica      (centrado)
PDVSA ORIENTE                                                   (centrado)

AMPICILINA SULBACTAN (AMP/ SUSP)
…
```
Sin numeración, sin firma, sin fecha, nombre del medicamento en MAYÚSCULAS + presentación entre paréntesis.

### solicitud-presupuesto
Formulario **impreso de Colina "SOLICITUD DE PRESUPUESTO"** que Danilo llena a mano; en el .docx es **una imagen escaneada de
página completa (16.4 × 22.1 cm)** con **cuadros de texto superpuestos** (Calibri, centrados) que tapan los datos del
paciente anterior: nombre, fecha (dd-mm-aaaa), edad ("Menor"), teléfono y diagnóstico ("Apendicitis Aguda"). Es decir,
reutiliza el formulario de otro paciente y solo cambia esos campos — el resto (honorarios, laboratorio…) queda del anterior: ⚠ revisarlo.
Campos del formulario (de arriba abajo), con el logo COLINA arriba a la izquierda:
```
SOLICITUD DE PRESUPUESTO                                   Fecha: __/__/____
Nombre del paciente: ____________________                  Edad: ______
C.I.: ____________          Telf: ____________
Diagnóstico de ingreso: ______________________________________
Para tratamiento Médico [ ]   Quirúrgico [ ]
Días de Hospitalización: ______        Días de Terapia: ______
Horas de Quirófano: ______
Honorarios Médicos:                     Servicios Clínicos:
Cirujano: ____________                  Laboratorio: ____________
Primer Ayudante: ____________           Rx: ____________
Segundo Ayudante: ____________          Anatomía patológica: ______
Anestesiólogo: ____________
Especialista Interconsultantes: ______________________________
Material Especial: ___________________________ (varias líneas)
Observación: ______________________________________
Especialista: ____________              Firma y Sello: ____________
```

### carta-recomendacion
Carta que **otro cirujano pediatra firma recomendando a Danilo** (plantilla genérica reutilizada). Título en negrita 16 pt.
```
Carta de recomendación                                         (centrado, negrita)

[d de Mes de aaaa].
Para: <Institución>. (Dirección médica)                        (negrita)
Anzoátegui, Venezuela.

	Me permito informarle que conozco amplia y detalladamente al Dr. Danilo Jesús Pérez Torres  C.I: [CI]. cirujano Pediatra del estado Anzoátegui y puedo asegurar que es una persona íntegra, estable, totalmente responsable y competente para cualquier tipo de actividad que se le encomiende.

	Por lo anterior no tengo inconveniente ninguno en recomendarla ampliamente, agradeciendo de antemano la atención y facilidades que le puedan brindar. Se extiende la presente para los efectos legales que al interesado convenga.
Muy atentamente.

__________________________________
Dr. [MÉDICO]
C.I: [CI]
Cirujano Pediatra.

[TELÉFONO]      [correo]      Barcelona                         (pie con iconos pequeños)
```

### morbilidad
Relación mensual de pacientes atendidos en consulta (estadística del servicio, PDVSA). Texto plano, sin formato especial.
```
Servicio de Cirugía Pediatrica.
Morbilidad de pacientes atendidos en consulta
Hospital industrial Jesús Farías Pdvsa Oriente.
Mes de <mes>.
Cirujanos:
Dra [MÉDICO A]. Dra [MÉDICO C]. Dr [MÉDICO B]. Dr Perez.

[NOMBRE] [EDAD] <POM/POT de …  |  diagnóstico>
…                           (línea en blanco entre bloques = día de consulta)
```

### ordenes-medicas
Órdenes de hospitalización en Colina (con logo COLINA y bloque de firma), todo en negrita, ítems justificados.
```
Órdenes medicas.                         (centrado)

Px: [NOMBRE]
Ci: menor Peso [N]kg
Edad: [EDAD]
Fecha: [FECHA]
Hora [h:mm]pm

1) Hospitalizar a cargo de Cirugía Pediátrica.
2) Dieta …
3) <Fármaco> (<dosis/kg>) <dosis> vev c/<N> horas.
…
N) C s/v.
N+1) A/E.

Dr. Danilo Pérez T.
CIRUJANO PEDIATRA-ECOGRAFISTA
MPPS:[MPPS] CMA: [CMA]
RIF: [RIF]
```
⚠ Para órdenes del **Hospital Universitario Dr. Luis Razetti** existe la skill de usuario **`ordenes-medicas-razetti`**
(formato, jerarquía de vías y convenciones propias): usarla en vez de esto. Este formato es solo para Colina/privado.

## Frases

### balance-ecos
- `Eco partes Blandas.` · `Eco abdominal /Eco pelvico` · `Eco MAMARIO` · `Eco tiroideo` · `Eco tiroideo/ Eco mamario` · `Eco Abdominal y Eco prostatico.` · `Abdominal y prostatico.`
- `Total: <N> estudios.`

### solicitud-cortesia
- Fórmula fija: "Presento la intención de solicitar la cortesía en <Clínica>. Consignando los requisitos solicitados para su revisión, agradeciendo de antemano colaboración con lo solicitado."
- Destinatario: `Dirección medica, <Clínica>.` + `Dr/Dra <nombre>.`

### listado-insumos (lista completa, en este orden)
AMPICILINA SULBACTAN (AMP/ SUSP) · CEFADROXILO (AMP/ SUSP) · HIDROCORTISONA (AMP/ CREMA) · KETOPROFENO (AMP) · IBUPROFENO (SUSP) ·
DIPIRONA (AMP) · METOCLOPRAMIDA (AMP) · ONDASETRON (AMP) · OMEPRAZOL (AMP) · ACETAMINOFEN (SUSP) · DEXAMETASONA (AMP) ·
BARGONIL (CREMA) · GASAS ESTERILES · GUANTES 7 1/2 · ADHESIVO DE TELA · BETADINE · Solución 0.9% · Solución 0.45%
(la versión "1" añade las dos soluciones al final).

### solicitud-presupuesto
- Diagnóstico de ingreso en los 2 del disco: `Apendicitis Aguda`; Edad: `Menor`; fecha con guiones `dd-mm-aaaa`.

### carta-recomendacion
- "persona íntegra, estable, totalmente responsable y competente para cualquier tipo de actividad que se le encomiende."
- "Se extiende la presente para los efectos legales que al interesado convenga." · "Muy atentamente."

### morbilidad
- Abreviaturas: `POM` (postoperatorio mediato), `POT` (postoperatorio tardío), `HU` (hernia umbilical), `HII` / `HID` (hernia inguinal
  izquierda/derecha), `HIB` (bilateral), `Supra` (supraumbilical), `SL` (sublingual: "frenulectomia SL", "corte de frenillo sl"),
  `ABP` (adherencias balanoprepuciales: "liberación de ABP", "liberación de adherencias bp").
- Ejemplos: `POM de HU+ Fimosectomia` · `POM de HU + HIB + Fimosectomia` · `POM de HU + Supra + HIB+ Orquidopexia` ·
  `POT de Hernia inguinal izq+ Hidrocele izq` · `Hernia umbilical + Fimosis severa` · `Hernia umbilical Dolorosa+ Abp` ·
  `POT de HU+ Exceresis de Cicatriz  Queloide`.

### ordenes-medicas
- `Hospitalizar a cargo de Cirugía Pediátrica.` · `Dieta completa.`
- Fármaco con la dosis por kg entre paréntesis: `Omeprazol (40) 40 mg vev c/24 horas.` · `Ampicilina (200) 1.5gr vev c/6horas.` ·
  `Ceftriaxona (50) 1 gr vev c/24 horas.` · `Amikacina (15) 380 MG c/24 h.` · `ketoprofeno (5) 55 mg vev c 8 horas sos dolor.` ·
  `Dipirona (0.03) 1.2 CC vev c/6 horas sos fiebre.` · `Ondasetron (0.15) 6 mg vev sos náuseas o vómito.`
- `Deambulación cada 3 horas.` · `Curas 3 veces al dia en herida quirúrgica con <antiséptico>.` · `C s/v.` (control de signos vitales) · `A/E.` (avisar eventualidades).
- vev = vía endovenosa; sos = si es necesario.

Errores/tipeos a vigilar: "Hospitalizae", "Deambulancion", "Ondasetron" (ondansetrón), "SULBACTAN", "policlínica puerto a cruz",
"Hospital industrial Jesús ferias" (Farías), "Hernis", "Chalazioen", "recomendarla" (femenino en la carta), correo sin "@".

## Conclusión (cierre de cada tipo)
- balance-ecos: `Total: <N> estudios.` + bloque de firma de Danilo (centrado, negrita) con firma/sello del modelo.
- solicitud-cortesia: firma encima de `Danilo Pérez Torres.` / `Cirujano Pediatra.` / `CI.[CI]` (centrado).
- listado-insumos: termina con el último insumo; sin firma.
- solicitud-presupuesto: `Especialista:` y `Firma y Sello:` del propio formulario.
- carta-recomendacion: `Muy atentamente.` + línea de firma + nombre, CI y especialidad del firmante + pie de contacto.
- morbilidad: termina con el último paciente; sin total ni firma.
- ordenes-medicas: último ítem `A/E.` + bloque de firma de Danilo.

## Preguntar si falta
- balance-ecos: fecha de la jornada, convenio/empresa, centro, lista de pacientes con CI y estudios de cada uno (para el total).
- solicitud-cortesia: clínica, ciudad, nombre del director médico, fecha.
- listado-insumos: si cambia algún medicamento/insumo o la talla de guantes; para qué cirugía/paciente (si lo quiere personalizado).
- solicitud-presupuesto: nombre, CI, edad, teléfono, diagnóstico, tratamiento médico o quirúrgico, días de hospitalización/terapia,
  horas de quirófano, ayudantes, anestesiólogo, laboratorio/Rx, interconsultas, material especial; y si hay que limpiar los datos del formulario reutilizado.
- carta-recomendacion: destinatario, fecha, quién la firma (datos que ese médico autorice).
- morbilidad: mes, cirujanos, pacientes vistos con edad y diagnóstico o POM/POT de qué cirugía.
- ordenes-medicas: peso, edad, fecha y hora, institución (si es Razetti → skill `ordenes-medicas-razetti`), diagnóstico/cirugía,
  dieta, antibióticos y analgésicos con dosis/kg, curas, alergias.

## Ejemplo anonimizado

### balance-ecos
```
Ecos Realizados [FECHA]
[CONVENIO] / CLINICA COLINA

[NOMBRE] [CI] Eco abdominal y Eco prostatico.
[NOMBRE] [CI] Eco tiroideo/ Eco mamario
[NOMBRE] [CI] Eco partes blandas.

Total: 5 estudios.

Dr. Danilo Pérez T.
CIRUJANO PEDIATRA-ECOGRAFISTA
MPPS:[MPPS] CMA: [CMA]
RIF: [RIF]
```

### solicitud-cortesia
```
Solicitud de cortesía

Puerto La Cruz [FECHA]

Dirección medica, Clínica [NOMBRE].
Dr. [MÉDICO].

Yo Dr. Danilo Pérez, Cirujano Pediatra CI. [CI]. Presento la intención de solicitar la cortesía en Clínica [NOMBRE]. Consignando los requisitos solicitados para su revisión, agradeciendo de antemano colaboración con lo solicitado.

Danilo Pérez Torres.
Cirujano Pediatra.
CI.[CI]
```

### listado-insumos
```
Listado de medicamentos e insumos para cirugía pediátrica
PDVSA ORIENTE

AMPICILINA SULBACTAN (AMP/ SUSP)
KETOPROFENO (AMP)
ACETAMINOFEN (SUSP)
GASAS ESTERILES
GUANTES 7 1/2
Solución 0.9%
```

### solicitud-presupuesto
```
Nombre del paciente: [NOMBRE]     Fecha: [FECHA]     Edad: Menor
C.I.: [CI]     Telf: [TELÉFONO]
Diagnóstico de ingreso: Apendicitis Aguda
Quirúrgico [X]   Días de Hospitalización: 2 días   Horas de Quirófano: 1 hora
Cirujano: Danilo Pérez   Laboratorio: Hematología completa, PT, PTT   Rx: de tórax AP
Especialista: Danilo Pérez T.
```

### carta-recomendacion
```
Carta de recomendación

[FECHA].
Para: [INSTITUCIÓN]. (Dirección médica)
Anzoátegui, Venezuela.

	Me permito informarle que conozco amplia y detalladamente al Dr. Danilo Jesús Pérez Torres  C.I: [CI]. cirujano Pediatra del estado Anzoátegui y puedo asegurar que es una persona íntegra, estable, totalmente responsable y competente para cualquier tipo de actividad que se le encomiende.
	Por lo anterior no tengo inconveniente ninguno en recomendarlo ampliamente, agradeciendo de antemano la atención y facilidades que le puedan brindar. Se extiende la presente para los efectos legales que al interesado convenga.
Muy atentamente.

__________________________________
Dr. [MÉDICO]
C.I: [CI]
Cirujano Pediatra.
```

### morbilidad
```
Servicio de Cirugía Pediatrica.
Morbilidad de pacientes atendidos en consulta
Hospital industrial Jesús Farías Pdvsa Oriente.
Mes de [MES].
Cirujanos:
Dra [MÉDICO A]. Dra [MÉDICO C]. Dr [MÉDICO B]. Dr Perez.

[NOMBRE] 8 años POM de HU + HIB + Fimosectomia
[NOMBRE] 5 años Hernia umbilical + ABP

[NOMBRE] 9 años POT de HU
```

### ordenes-medicas
```
Órdenes medicas.

Px: [NOMBRE]
Ci: menor Peso 20kg
Edad: 6 años
Fecha: [FECHA]
Hora 4:00pm

1) Hospitalizar a cargo de Cirugía Pediátrica.
2) Dieta completa.
3) Omeprazol (1) 20 mg vev c/24 horas.
4) Ceftriaxona (50) 1 gr vev c/24 horas.
5) Ketoprofeno (1) 20 mg vev c/8 horas sos dolor.
6) Curas 3 veces al dia en herida quirúrgica.
7) C s/v.
8) A/E.

Dr. Danilo Pérez T.
CIRUJANO PEDIATRA-ECOGRAFISTA
MPPS:[MPPS] CMA: [CMA]
RIF: [RIF]
```
