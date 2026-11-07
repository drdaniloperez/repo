# Formato: Informe ecográfico PIEL Y PARTES BLANDAS

Aprendido de 8 informes reales (Centro de Especialidades Médicas Colina). 1–2 imágenes.

## Estructura
```
INFORME ECOGRÁFICO PIEL Y PARTES BLANDAS
| Px: … | Ci: … | Edad: … | Fecha: … |

Se realiza estudio ecográfico en tiempo real con transductor LINEAL de 7.5MHz en múltiples proyecciones, donde se evidencian los siguientes hallazgos:

Region <zona y lado>: <piel> , <tejido celular subcutáneo>, se evidencia <lesión> …, de medidas [a x b (x c)] cm, <dolor a la exploración>.

Conclusión: 	1) <diagnóstico> en región <zona y lado> [de medidas …]
Se sugiere valoración [oportuna] por <especialidad>.
```

## Plantillas literales frecuentes
- **Hernia umbilical:** Region umbilical: piel sin alteraciones con ligero aumento de volumen al realizar maniobra de valsalva tejido celular subcutáneo sin alteracionnes, se evidencia defecto aponeurotico umbilical de [X] cm con contenido en su interior sugestivo de epliplon, con dolor a la exploración.
  → `1) Defecto aponeutico umbilical de [X] cm con contenido en su interior (epliplon)` · `Se sugiere valoración por cirugía [Pediatrica].` (pediátrica si es menor)
- **Quiste (sinovial / Baker / seroma):** Region <zona>: piel sin alteraciones con ligero aumento de volumen, tejido celular subcutáneo sin alteracionnes, se evidencia quiste de bordes bien definidos de contenido anecoico heterogéneo, sugestivo de <quiste sinovial / quiste de baker / Seroma Postraumático>, de medidas [a x b] cm, con dolor leve a la exploración.
  → `1) <Quiste …> en región <zona>.` · `Se sugiere valoracion oportuna por <traumatología / cirugia>.`
- **Lesión de piel inflamatoria:** "piel con cambios de coloración eritema y mácula de aprox [a x b] cm con bordes mal definidos y aumento en el grosor epidérmico, con evidente congestión vascular local, densidad heterogenea, con áreas hipoecoicas y edema que se extiende a tejido celular subcutáneo, sin acumulación de liquido perilesional, sin relación con planos profundos."
  → `1) Hallazgos ecografícos sugestivos a <dx> <zona>.` · `Se sugiere valoración por dermatología.`

## Conclusión
- `Conclusión: \t1) <diagnóstico> en región <zona y lado> [de medidas …]`
- Siempre seguida de `Se sugiere valoración [oportuna] por <especialidad>.` (cirugía pediátrica si es menor).

## Preguntar si falta
Zona exacta y **lateralidad**, medidas (2–3 ejes), contenido (anecoico/heterogéneo), bordes,
vascularidad, relación con planos profundos, dolor, comportamiento con Valsalva (hernias),
tamaño del defecto aponeurótico y contenido, especialidad a la que se sugiere referir.

## Ejemplo anonimizado
```
INFORME ECOGRÁFICO PIEL Y PARTES BLANDAS
| Px: [NOMBRE] | Ci: [CI o menor] | Edad: [EDAD] | Fecha: [FECHA] |

Se realiza estudio ecográfico en tiempo real con transductor LINEAL de 7.5MHz en múltiples proyecciones, donde se evidencian los siguientes hallazgos:

Region umbilical: piel sin alteraciones con ligero aumento de volumen al realizar maniobra de valsalva tejido celular subcutáneo sin alteracionnes, se evidencia defecto aponeurotico umbilical de 0.6 cm con contenido en su interior sugestivo de epliplon, con dolor a la exploración.

Conclusión: 	1) Defecto aponeutico umbilical de 0.6 cm con contenido en su interior (epliplon)
Se sugiere valoración por cirugía Pediatrica.
```
