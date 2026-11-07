# Formato: Órdenes médicas de hospitalización (Colina/privado)

Aprendido de 1 documento del disco (05/2025), instituciones: Centro de Especialidades Médicas Colina. Estado: **pocos ejemplos**.
Detalle completo (estructura literal, frases, tipeos): `documentos-administrativos.md`, sección `### ordenes-medicas`.

## Estructura
"Órdenes medicas." centrado / Px, Ci + Peso, Edad, Fecha, Hora / ítems numerados "1)" justificados / bloque de firma. Todo en negrita, logo COLINA. Para el Hospital Luis Razetti usar la skill de usuario `ordenes-medicas-razetti`.

## Frases
"Hospitalizar a cargo de Cirugía Pediátrica.", "Ceftriaxona (50) 1 gr vev c/24 horas." (dosis/kg entre paréntesis), "C s/v.", "A/E."

## Conclusión
Último ítem "A/E." + bloque de firma de Danilo.

## Preguntar si falta
peso, edad, fecha y hora, institución, dieta, fármacos con dosis/kg, curas, alergias.

## Ejemplo anonimizado
```
Órdenes medicas.

Px: [NOMBRE]
Ci: menor Peso 20kg
Edad: 6 años
Fecha: [FECHA]
Hora 4:00pm

1) Hospitalizar a cargo de Cirugía Pediátrica.
2) Dieta completa.
3) Ceftriaxona (50) 1 gr vev c/24 horas.
4) C s/v.
5) A/E.
```
