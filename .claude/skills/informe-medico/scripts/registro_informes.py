#!/usr/bin/env python3
"""Registro (base de datos) de los informes ecográficos de Danilo en Excel, con hoja de estadísticas.

El registro tiene DATOS DE PACIENTES: vive solo en el equipo de Danilo / en la sesión, NUNCA en este repo público.

  python3 registro_informes.py crear   --datos filas.json --salida "Registro de informes.xlsx"
  python3 registro_informes.py agregar --registro "Registro de informes.xlsx" --datos filas_nuevas.json

filas.json = lista de objetos con las claves:
  fecha (dd/mm/aaaa), centro, paciente, cedula, edad (número de años), estudio, diagnostico, recomendacion,
  tirads_birads, imagenes (número), observaciones
"""
import argparse
import datetime as dt
import json
import sys
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

COLS = [("N°", 6), ("Fecha del estudio", 13), ("Centro", 20), ("Paciente", 24), ("Cédula", 13), ("Edad (años)", 9),
        ("Grupo etario", 14), ("Tipo de estudio", 24), ("Diagnósticos / conclusión", 70), ("Tirads / Birads", 11),
        ("Recomendación / referencia", 34), ("N° imágenes", 10), ("Observaciones", 30)]
MAXR = 2000
F = "Arial"
AZUL = PatternFill("solid", start_color="1F4E78")
CLARO = PatternFill("solid", start_color="DDEBF7")
LINEA = Side(style="thin", color="BFBFBF")
BORDE = Border(left=LINEA, right=LINEA, top=LINEA, bottom=LINEA)
CENTROS = ["Centro de Especialidades Médicas Colina", "Policlínica San José", "Hospital Jesús Farías (PDVSA)",
           "Hospital Universitario Dr. Luis Razetti"]
ESTUDIOS = ["Abdominal", "Abdominal con énfasis renal", "Abdominopélvico", "Renal", "Vesical", "Prostático",
            "Tiroideo", "Mamario", "Partes blandas", "Pélvico", "Testicular", "Otro"]
CLAVES = [("Litiasis o microlitiasis renal", "*litiasis renal*"), ("   de ellas, microlitiasis", "*microlitiasis*"),
          ("Hígado graso", "*hígado graso*"), ("Hepatomegalia", "*hepato*"), ("Colitis", "*colitis*"),
          ("Enteritis", "*enteritis*"), ("Barro biliar", "*barro biliar*"), ("Litiasis vesicular", "*litiasis vesicular*"),
          ("Quistes (cualquier órgano)", "*quist*"), ("Hernia", "*hernia*"), ("Tiroiditis", "*tiroiditis*"),
          ("Hiperplasia prostática", "*hiperplasia*"), ("Mioma", "*mioma*"), ("Edema perirrenal / ITU alta", "*peri*ren*")]


def fila_valores(n, r):
    fecha = dt.datetime.strptime(r["fecha"], "%d/%m/%Y").date()
    return [n, fecha, r["centro"], r["paciente"], r.get("cedula", ""), r.get("edad"), None, r["estudio"],
            r.get("diagnostico", ""), r.get("tirads_birads", ""), r.get("recomendacion", ""), r.get("imagenes", 0),
            r.get("observaciones", "")]


def escribir_fila(ws, fila, vals):
    for c, v in enumerate(vals, 1):
        cell = ws.cell(fila, c, v)
        cell.font = Font(name=F, size=10)
        cell.border = BORDE
        cell.alignment = Alignment(vertical="top", wrap_text=c in (4, 8, 9, 11, 13),
                                   horizontal="center" if c in (1, 2, 5, 6, 7, 10, 12) else "left")
    ws.cell(fila, 2).number_format = "dd/mm/yyyy"
    ws.cell(fila, 7).value = f'=IF(F{fila}="","",IF(F{fila}<18,"Pediátrico",IF(F{fila}>=65,"Adulto mayor","Adulto")))'


def hoja_informes(wb, filas):
    ws = wb.active
    ws.title = "Informes"
    for c, (t, w) in enumerate(COLS, 1):
        cell = ws.cell(1, c, t)
        cell.font = Font(name=F, bold=True, color="FFFFFF", size=10)
        cell.fill = AZUL
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = BORDE
        ws.column_dimensions[get_column_letter(c)].width = w
    ws.row_dimensions[1].height = 30
    for i, r in enumerate(filas, 1):
        escribir_fila(ws, i + 1, fila_valores(i, r))
    ws.freeze_panes = "E2"
    ws.auto_filter.ref = f"A1:M{MAXR}"
    dv1 = DataValidation(type="list", formula1='"' + ",".join(CENTROS) + '"', allow_blank=True)
    dv2 = DataValidation(type="list", formula1='"' + ",".join(ESTUDIOS) + '"', allow_blank=True)
    ws.add_data_validation(dv1); ws.add_data_validation(dv2)
    dv1.add(f"C2:C{MAXR}"); dv2.add(f"H2:H{MAXR}")
    return ws


def hoja_estadisticas(wb):
    ws = wb.create_sheet("Estadísticas")
    ws.column_dimensions["A"].width = 42
    ws.column_dimensions["B"].width = 14
    ws.column_dimensions["C"].width = 14
    R = lambda col: f"Informes!${col}$2:${col}${MAXR}"
    fila = 1

    def titulo(t):
        nonlocal fila
        c = ws.cell(fila, 1, t); c.font = Font(name=F, bold=True, size=12, color="1F4E78"); fila += 1

    def encabezado(*ts):
        nonlocal fila
        for i, t in enumerate(ts, 1):
            c = ws.cell(fila, i, t); c.font = Font(name=F, bold=True, color="FFFFFF", size=10); c.fill = AZUL
            c.alignment = Alignment(horizontal="center"); c.border = BORDE
        fila += 1

    def linea(etq, formula, pct_de=None):
        nonlocal fila
        a = ws.cell(fila, 1, etq); b = ws.cell(fila, 2, formula)
        for c in (a, b):
            c.font = Font(name=F, size=10); c.border = BORDE
        b.alignment = Alignment(horizontal="center")
        if pct_de:
            p = ws.cell(fila, 3, f"=IF({pct_de}=0,0,B{fila}/{pct_de})")
            p.number_format = "0.0%"; p.font = Font(name=F, size=10); p.border = BORDE
            p.alignment = Alignment(horizontal="center")
        fila += 1

    titulo("Resumen general")
    encabezado("Indicador", "Valor", "")
    tot = f"B{fila}"
    linea("Total de informes", f'=COUNTA({R("D")})')
    linea("Pacientes distintos (por nombre)",
          f'=SUMPRODUCT(({R("D")}<>"")/COUNTIF({R("D")},{R("D")}&""))')
    linea("Primer estudio registrado", f'=MIN({R("B")})'); ws.cell(fila - 1, 2).number_format = "dd/mm/yyyy"
    linea("Último estudio registrado", f'=MAX({R("B")})'); ws.cell(fila - 1, 2).number_format = "dd/mm/yyyy"
    linea("Total de imágenes anexadas", f'=SUM({R("L")})')
    linea("Edad promedio (años)", f'=IFERROR(AVERAGE({R("F")}),0)'); ws.cell(fila - 1, 2).number_format = "0.0"
    linea("Informes con referencia / recomendación", f'=COUNTIF({R("K")},"?*")', tot)
    fila += 1
    titulo("Informes por centro")
    encabezado("Centro", "Informes", "%")
    for c in CENTROS:
        linea(c, f'=COUNTIF({R("C")},"{c}")', tot)
    fila += 1
    titulo("Informes por tipo de estudio")
    encabezado("Tipo de estudio", "Informes", "%")
    for e in ESTUDIOS:
        linea(e, f'=COUNTIF({R("H")},"{e}")', tot)
    fila += 1
    titulo("Informes por grupo etario")
    encabezado("Grupo", "Informes", "%")
    for g in ("Pediátrico", "Adulto", "Adulto mayor"):
        linea(g + (" (< 18 años)" if g == "Pediátrico" else " (≥ 65 años)" if g == "Adulto mayor" else " (18–64 años)"),
              f'=COUNTIF({R("G")},"{g}")', tot)
    fila += 1
    titulo("Hallazgos más frecuentes (búsqueda por palabra en el diagnóstico)")
    encabezado("Hallazgo", "Informes", "%")
    for etq, patron in CLAVES:
        linea(etq, f'=COUNTIF({R("I")},"{patron}")', tot)
    fila += 1
    c = ws.cell(fila, 1, "Las cifras se recalculan solas al añadir filas en la hoja Informes (hasta la fila "
                         f"{MAXR}). Los hallazgos se cuentan por palabra clave en la columna de diagnósticos.")
    c.font = Font(name=F, italic=True, size=9, color="595959")
    return ws


def hoja_instrucciones(wb):
    ws = wb.create_sheet("Instrucciones")
    ws.column_dimensions["A"].width = 110
    textos = [
        ("Registro de informes ecográficos — Dr. Danilo Pérez T.", True),
        ("Hoja Informes: una fila por informe. Para agregar uno, escribe en la primera fila vacía; el N°, la fecha y la edad"
         " son datos; el Grupo etario se calcula solo.", False),
        ("Centro y Tipo de estudio tienen lista desplegable. Usa los filtros del encabezado para buscar por paciente, "
         "cédula, centro, tipo de estudio o fecha, y Ctrl+F para buscar un diagnóstico.", False),
        ("Hoja Estadísticas: totales y porcentajes por centro, tipo de estudio, grupo etario y hallazgos frecuentes; "
         "se actualizan automáticamente.", False),
        ("Claude puede agregar los informes nuevos: súbele este archivo al empezar la sesión y te lo devuelve actualizado.", False),
        ("Contiene datos de pacientes: guárdalo en tu equipo o en tu nube privada; no lo compartas públicamente.", False),
    ]
    for i, (t, b) in enumerate(textos, 1):
        c = ws.cell(i, 1, t)
        c.font = Font(name=F, bold=b, size=12 if b else 10)
        c.alignment = Alignment(wrap_text=True, vertical="top")


def crear(datos, salida):
    wb = Workbook()
    hoja_informes(wb, datos)
    hoja_estadisticas(wb)
    hoja_instrucciones(wb)
    wb.save(salida)


def agregar(registro, datos):
    wb = load_workbook(registro)
    ws = wb["Informes"]
    ultima = max((r for r in range(2, MAXR + 1) if ws.cell(r, 4).value), default=1)
    n = ws.cell(ultima, 1).value or 0
    for i, r in enumerate(datos, 1):
        escribir_fila(ws, ultima + i, fila_valores(int(n) + i, r))
    wb.save(registro)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("crear"); c.add_argument("--datos", required=True); c.add_argument("--salida", required=True)
    a = sub.add_parser("agregar"); a.add_argument("--registro", required=True); a.add_argument("--datos", required=True)
    args = ap.parse_args()
    datos = json.loads(Path(args.datos).read_text(encoding="utf-8"))
    if args.cmd == "crear":
        crear(datos, args.salida)
    else:
        agregar(args.registro, datos)
    print("OK")


if __name__ == "__main__":
    main()
