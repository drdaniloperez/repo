#!/usr/bin/env python3
"""Arma el informe en Word (.docx): texto + imágenes del eco en cuadrícula, en el orden dado.

Uso:
  python3 armar_informe_docx.py --texto informe.md --manifiesto imagenes.json --salida "Eco abdominal - Paciente.docx" \
      [--plantilla membrete.docx] [--columnas 2] [--ancho-cm 8] [--imagenes-en final|pagina-nueva] [--pies]

--texto       Marcado sencillo: "# " título centrado, "## " subtítulo, "- " viñeta, **negrita**, línea en blanco = párrafo nuevo.
              Una línea que sea exactamente  [[IMAGENES]]  indica dónde van las imágenes (si no, van al final).
--manifiesto  JSON: [{"ruta": "01_x.jpg", "pie": "Hígado - corte longitudinal"}, ...]  (o usa --imagenes a.jpg b.jpg …)
--plantilla   .docx con el membrete/encabezado/pie de página de Danilo (SIN datos de pacientes); se conserva su
              encabezado, pie, márgenes y estilos, y se reemplaza el cuerpo.
Requiere: pip install python-docx
"""
import argparse
import json
import re
import sys
from pathlib import Path

try:
    from docx import Document
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
    from docx.shared import Cm, Pt
except ImportError:
    sys.exit("Falta python-docx: pip install python-docx")


def agregar_runs(par, texto, tam=None):
    for i, trozo in enumerate(re.split(r"\*\*", texto)):
        if trozo:
            r = par.add_run(trozo)
            r.bold = i % 2 == 1
            if tam:
                r.font.size = Pt(tam)


def escribir_texto(doc, lineas):
    for linea in lineas:
        s = linea.rstrip()
        if not s.strip():
            continue
        if s.startswith("# "):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            agregar_runs(p, f"**{s[2:].strip()}**", 13)
        elif s.startswith("## "):
            p = doc.add_paragraph()
            agregar_runs(p, f"**{s[3:].strip()}**")
        elif s.lstrip().startswith(("- ", "• ")):
            try:
                p = doc.add_paragraph(style="List Bullet")
            except KeyError:
                p = doc.add_paragraph("• ")
            agregar_runs(p, s.lstrip()[2:])
        else:
            agregar_runs(doc.add_paragraph(), s)


def escribir_imagenes(doc, imagenes, columnas, ancho_cm, pies):
    filas = (len(imagenes) + columnas - 1) // columnas
    tabla = doc.add_table(rows=filas, cols=columnas)
    tabla.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, im in enumerate(imagenes):
        celda = tabla.cell(i // columnas, i % columnas)
        p = celda.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(str(im["ruta"]), width=Cm(ancho_cm))
        if pies and im.get("pie"):
            pp = celda.add_paragraph()
            pp.alignment = WD_ALIGN_PARAGRAPH.CENTER
            agregar_runs(pp, im["pie"], 8)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--texto", required=True)
    ap.add_argument("--manifiesto")
    ap.add_argument("--imagenes", nargs="*", default=[])
    ap.add_argument("--plantilla")
    ap.add_argument("--columnas", type=int, default=2)
    ap.add_argument("--ancho-cm", type=float)
    ap.add_argument("--imagenes-en", choices=["final", "pagina-nueva"], default="final")
    ap.add_argument("--pies", action="store_true", help="Muestra el pie (órgano/corte) bajo cada imagen")
    ap.add_argument("--salida", required=True)
    a = ap.parse_args()

    imagenes = json.loads(Path(a.manifiesto).read_text()) if a.manifiesto else [{"ruta": r} for r in a.imagenes]
    base = Path(a.manifiesto).parent if a.manifiesto else Path(".")
    for im in imagenes:
        ruta = Path(im["ruta"])
        im["ruta"] = ruta if ruta.is_absolute() or ruta.exists() else base / ruta
        if not Path(im["ruta"]).exists():
            sys.exit(f"No existe la imagen: {im['ruta']}")

    if a.plantilla:
        doc = Document(a.plantilla)
        cuerpo = doc.element.body
        for el in list(cuerpo):
            if not el.tag.endswith("sectPr"):
                cuerpo.remove(el)
    else:
        doc = Document()
        for s in doc.sections:
            s.left_margin = s.right_margin = Cm(2)
            s.top_margin = s.bottom_margin = Cm(1.5)
        doc.styles["Normal"].font.name = "Arial"
        doc.styles["Normal"].font.size = Pt(11)

    sec = doc.sections[0]
    util_cm = (sec.page_width - sec.left_margin - sec.right_margin) / 360000
    ancho = a.ancho_cm or (util_cm / a.columnas - 0.4)

    lineas = Path(a.texto).read_text(encoding="utf-8").splitlines()
    if "[[IMAGENES]]" in [l.strip() for l in lineas]:
        k = [l.strip() for l in lineas].index("[[IMAGENES]]")
        antes, despues = lineas[:k], lineas[k + 1:]
    else:
        antes, despues = lineas, []
    escribir_texto(doc, antes)
    if imagenes:
        if a.imagenes_en == "pagina-nueva":
            doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        escribir_imagenes(doc, imagenes, a.columnas, ancho, a.pies)
    escribir_texto(doc, despues)
    doc.save(a.salida)
    print(f"Guardado {a.salida} ({len(imagenes)} imágenes)")


if __name__ == "__main__":
    main()
