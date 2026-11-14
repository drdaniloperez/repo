#!/usr/bin/env python3
"""Registro sencillo de los informes ecográficos de Danilo (Excel): paciente, tipo de estudio, fecha y centro,
más una hoja de resumen con conteos por centro y por tipo de estudio.

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
    celda(ws, fila, 2, r["paciente"])
    celda(ws, fila, 3, r["estudio"])
    celda(ws, fila, 4, dt.datetime.strptime(r["fecha"], "%d/%m/%Y").date(), h="center").number_format = "dd/mm/yyyy"
    celda(ws, fila, 5, r["centro"], h="center")


def crear(datos, salida):
    wb = Workbook()
    ws = wb.active
    ws.title = "Informes"
    for c, (t, w) in enumerate(COLS, 1):
        x = celda(ws, 1, c, t, h="center", font={"bold": True, "color": "FFFFFF"})
        x.fill = AZUL
        ws.column_dimensions[chr(64 + c)].width = w
    for i, r in enumerate(datos, 1):
        escribir_fila(ws, i + 1, i, r)
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:E{MAXR}"
    for lista, col in ((CENTROS, "E"), (ESTUDIOS, "C")):
        dv = DataValidation(type="list", formula1='"' + ",".join(lista) + '"', allow_blank=True)
        ws.add_data_validation(dv)
        dv.add(f"{col}2:{col}{MAXR}")

    rs = wb.create_sheet("Resumen")
    rs.column_dimensions["A"].width = 32
    rs.column_dimensions["B"].width = 12
    fila = 1

    def bloque(titulo, etiquetas, col):
        nonlocal fila
        for c, t in enumerate((titulo, "Informes"), 1):
            x = celda(rs, fila, c, t, h="center", font={"bold": True, "color": "FFFFFF"})
            x.fill = AZUL
        fila += 1
        for e in etiquetas:
            celda(rs, fila, 1, e)
            celda(rs, fila, 2, f'=COUNTIF(Informes!${col}$2:${col}${MAXR},"{e}")', h="center")
            fila += 1
        fila += 1

    celda(rs, fila, 1, "Total de informes", font={"bold": True})
    celda(rs, fila, 2, f"=COUNTA(Informes!$B$2:$B${MAXR})", h="center", font={"bold": True})
    fila += 2
    bloque("Centro", CENTROS, "E")
    bloque("Tipo de estudio", ESTUDIOS, "C")
    nota = rs.cell(fila, 1, "Se actualiza solo al agregar filas en la hoja Informes. Usa los filtros del encabezado para buscar.")
    nota.font = Font(name=F, italic=True, size=9, color="595959")
    wb.save(salida)


def agregar(registro, datos):
    wb = load_workbook(registro)
    ws = wb["Informes"]
    ultima = max((r for r in range(2, MAXR + 1) if ws.cell(r, 2).value), default=1)
    n = ws.cell(ultima, 1).value or 0
    for i, r in enumerate(datos, 1):
        escribir_fila(ws, ultima + i, int(n) + i, r)
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
