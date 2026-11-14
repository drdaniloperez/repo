#!/usr/bin/env python3
"""Base de datos de informes realizados (Excel): una hoja por clínica (Clínicas Colina / Policlínica San José) con
N°, paciente, tipo de estudio y fecha, más una hoja Resumen con conteos por clínica y por tipo de estudio.

El registro tiene NOMBRES DE PACIENTES: vive solo en el equipo de Danilo / en la sesión, NUNCA en este repo público.

  python3 registro_informes.py crear   --datos filas.json --salida "Registro de informes.xlsx"
  python3 registro_informes.py agregar --registro "Registro de informes.xlsx" --datos filas_nuevas.json

filas.json = lista de objetos {"paciente": ..., "estudio": ..., "fecha": "dd/mm/aaaa", "centro": ...}
"""
import argparse
import datetime as dt
import json
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

COLS = [("N°", 6), ("Paciente", 28), ("Tipo de estudio ecográfico", 30), ("Fecha realizado", 15), ("Centro", 18)]
CENTROS = ["Clínicas Colina", "Policlínica San José"]
ESTUDIOS = ["Abdominal", "Abdominal con énfasis renal", "Abdominopélvico", "Renal", "Vesical", "Prostático",
            "Tiroideo", "Mamario", "Partes blandas", "Pélvico", "Testicular", "Otro"]
MAXR = 2000
F = "Arial"
AZUL = PatternFill("solid", start_color="1F4E78")
LINEA = Side(style="thin", color="BFBFBF")
BORDE = Border(left=LINEA, right=LINEA, top=LINEA, bottom=LINEA)


def celda(ws, f, c, v, **kw):
    x = ws.cell(f, c, v)
    x.font = Font(name=F, size=10, **kw.pop("font", {}))
    x.border = BORDE
    x.alignment = Alignment(horizontal=kw.pop("h", "left"), vertical="center")
    return x


def escribir_fila(ws, fila, n, r):
    celda(ws, fila, 1, n, h="center")
    celda(ws, fila, 2, r.get("paciente", ""))
    celda(ws, fila, 3, r["estudio"])
    celda(ws, fila, 4, dt.datetime.strptime(r["fecha"], "%d/%m/%Y").date(), h="center").number_format = "dd/mm/yyyy"
    celda(ws, fila, 5, r["centro"], h="center")


HOJAS = {"Clínicas Colina": "Clínicas Colina", "Policlínica San José": "San José"}


def hoja_clinica(wb, nombre, filas, primera=False):
    ws = wb.active if primera else wb.create_sheet()
    ws.title = nombre
    for c, (t, w) in enumerate(COLS, 1):
        x = celda(ws, 1, c, t, h="center", font={"bold": True, "color": "FFFFFF"})
        x.fill = AZUL
        ws.column_dimensions[chr(64 + c)].width = w
    for i, r in enumerate(filas, 1):
        escribir_fila(ws, i + 1, i, r)
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:E{MAXR}"
    dv = DataValidation(type="list", formula1='"' + ",".join(ESTUDIOS) + '"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f"C2:C{MAXR}")


def crear(datos, salida):
    wb = Workbook()
    for k, (centro, hoja) in enumerate(HOJAS.items()):
        hoja_clinica(wb, hoja, [r for r in datos if r["centro"] == centro], primera=(k == 0))
    rs = wb.create_sheet("Resumen")
    rs.column_dimensions["A"].width = 32
    for c in "BCD":
        rs.column_dimensions[c].width = 16
    hojas = list(HOJAS.values())
    for c, t in enumerate(["Tipo de estudio"] + hojas + ["Total"], 1):
        celda(rs, 1, c, t, h="center", font={"bold": True, "color": "FFFFFF"}).fill = AZUL
    for f, e in enumerate(ESTUDIOS, 2):
        celda(rs, f, 1, e)
        for c, h in enumerate(hojas, 2):
            celda(rs, f, c, f"=COUNTIF('{h}'!$C$2:$C${MAXR},\"{e}\")", h="center")
        celda(rs, f, len(hojas) + 2, f"=SUM(B{f}:C{f})", h="center")
    f = len(ESTUDIOS) + 2
    celda(rs, f, 1, "Total de informes", font={"bold": True})
    for c in range(2, len(hojas) + 3):
        col = chr(64 + c)
        celda(rs, f, c, f"=SUM({col}2:{col}{f - 1})", h="center", font={"bold": True})
    nota = rs.cell(f + 2, 1, "Se actualiza solo al agregar filas en las hojas de cada clínica.")
    nota.font = Font(name=F, italic=True, size=9, color="595959")
    wb.save(salida)


def agregar(registro, datos):
    wb = load_workbook(registro)
    for r in datos:
        ws = wb[HOJAS[r["centro"]]]
        ultima = max((x for x in range(2, MAXR + 1) if ws.cell(x, 4).value), default=1)
        escribir_fila(ws, ultima + 1, int(ws.cell(ultima, 1).value or 0) + 1, r)
    wb.save(registro)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("crear"); c.add_argument("--datos", required=True); c.add_argument("--salida", required=True)
    a = sub.add_parser("agregar"); a.add_argument("--registro", required=True); a.add_argument("--datos", required=True)
    args = ap.parse_args()
    datos = json.loads(Path(args.datos).read_text(encoding="utf-8"))
    crear(datos, args.salida) if args.cmd == "crear" else agregar(args.registro, datos)
    print("OK")


if __name__ == "__main__":
    main()
