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
--centro      colinas | san-jose | pdvsa | razetti → membrete con el LOGO de esa institución (formatos/logos/) y la tabla
              Px | Ci | Edad | Fecha (--px --ci --edad --fecha) como en los informes de Danilo; --titulo es el título.
--firma       imagen de firma/sello (solo local; nunca se guarda en el repo), se coloca antes del bloque de firma
              (la línea que empieza por "Dr.").
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


LOGOS = Path(__file__).resolve().parent.parent / "formatos" / "logos"


def borde_tabla(tabla, visible=True):
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    tblPr = tabla._tbl.tblPr
    b = OxmlElement("w:tblBorders")
    for lado in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement(f"w:{lado}")
        e.set(qn("w:val"), "single" if visible else "nil")
        if visible:
            e.set(qn("w:sz"), "8")
            e.set(qn("w:color"), "000000")
        b.append(e)
    look = tblPr.find(qn("w:tblLook"))  # el orden de los hijos de tblPr importa
    if look is not None:
        look.addprevious(b)
    else:
        tblPr.append(b)


def anchos_columnas(tabla, anchos_cm):
    from docx.oxml.ns import qn
    for gc, w in zip(tabla._tbl.tblGrid.findall(qn("w:gridCol")), anchos_cm):
        gc.set(qn("w:w"), str(int(w * 567)))
    for fila in tabla.rows:
        for c, w in zip(fila.cells, anchos_cm):
            c.width = Cm(w)


def separador(doc, pt=2):
    """Párrafo mínimo entre tablas (dos tablas pegadas se fusionan en Word/LibreOffice)."""
    from docx.shared import Pt
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.space_before = Pt(0)
    p.add_run().font.size = Pt(pt)
    return p


def membrete(doc, centro, titulo, px, ci, edad, fecha):
    info = json.loads((LOGOS / "logos.json").read_text(encoding="utf-8"))[centro]
    logo = LOGOS / info["archivo"]
    tam = dict(width=Cm(info["ancho_cm"]), height=Cm(info["alto_cm"])) if info.get("alto_cm") else dict(width=Cm(info["ancho_cm"]))
    for sec in doc.sections:  # carta, márgenes de sus informes
        sec.page_width, sec.page_height = Cm(21.59), Cm(27.94)
        sec.left_margin = sec.right_margin = Cm(2.54)
        sec.top_margin, sec.bottom_margin = Cm(1.5), Cm(1.5)
    doc.styles["Normal"].font.name = "Calibri"  # fuente de sus informes
    if info.get("orientacion") == "horizontal":  # p. ej. programación quirúrgica del Razetti (carta apaisada)
        from docx.enum.section import WD_ORIENT
        for sec in doc.sections:
            sec.orientation = WD_ORIENT.LANDSCAPE
            sec.page_width, sec.page_height = Cm(27.94), Cm(21.59)
            sec.left_margin = sec.right_margin = Cm(2.5)
            sec.top_margin = sec.bottom_margin = Cm(3.0)
    if info.get("lineas_membrete"):  # membrete real del Razetti: escudo a la izquierda, texto azul alineado a la derecha
        from docx.shared import RGBColor
        util = (doc.sections[0].page_width - doc.sections[0].left_margin - doc.sections[0].right_margin) / 360000
        t = doc.add_table(rows=1, cols=2)
        borde_tabla(t, False)
        t.cell(0, 0).paragraphs[0].add_run().add_picture(str(logo), **tam)
        anchos_columnas(t, (info["ancho_cm"] + 0.3, util - info["ancho_cm"] - 0.3))
        celda = t.cell(0, 1)
        for i, linea in enumerate(info["lineas_membrete"]):
            p = celda.paragraphs[0] if i == 0 else celda.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(linea.replace("<MES AÑO>", fecha or ""))
            r.font.size = Pt(info.get("tam_membrete_pt", 16))
            r.font.color.rgb = RGBColor.from_string(info.get("color_membrete", "4472C4"))
        if titulo:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            agregar_runs(p, f"**{titulo}**")
    elif info.get("titulo_al_lado"):
        t = doc.add_table(rows=1, cols=2)
        borde_tabla(t, False)
        t.cell(0, 0).paragraphs[0].add_run().add_picture(str(logo), **tam)
        anchos_columnas(t, (info["ancho_cm"] + 0.7, 16.5 - info["ancho_cm"] - 0.7))
        p = t.cell(0, 1).paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        agregar_runs(p, f"**{titulo}**")
        from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
        t.cell(0, 1).vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    else:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if info["posicion"] == "centrado" else WD_ALIGN_PARAGRAPH.LEFT
        p.add_run().add_picture(str(logo), **tam)
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        agregar_runs(p, f"**{titulo}**")
    if not info.get("lineas_membrete"):
        separador(doc)
    if not any((px, ci, edad)):  # documentos sin tabla de identificación (programación, listas)
        doc.add_paragraph()
        return info
    t = doc.add_table(rows=1, cols=4)
    borde_tabla(t, True)
    t.autofit = False
    anchos_columnas(t, (6.2, 3.2, 3.1, 4.0))
    for c, (et, v) in zip(t.rows[0].cells, (("Px:", px), ("Ci:", ci), ("Edad:", edad), ("Fecha:", fecha))):
        agregar_runs(c.paragraphs[0], f"**{et} {v}**")
    doc.add_paragraph()
    return info


def escribir_texto(doc, lineas, firma=None):
    for linea in lineas:
        s = linea.rstrip()
        if not s.strip():
            continue
        if firma and re.match(r"\s*Dr\.?\s", s):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.add_run().add_picture(str(firma), width=Cm(5.3))
            firma = None
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
    ap.add_argument("--centro", choices=["colinas", "san-jose", "pdvsa", "razetti"])
    ap.add_argument("--titulo", default="INFORME ECOGRÁFICO")
    ap.add_argument("--px", default="")
    ap.add_argument("--ci", default="")
    ap.add_argument("--edad", default="")
    ap.add_argument("--fecha", default="")
    ap.add_argument("--firma")
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
    if a.centro:
        info = membrete(doc, a.centro, a.titulo, a.px, a.ci, a.edad, a.fecha)
        print(f"Membrete: {info['nombre']}")
    escribir_texto(doc, antes, a.firma)
    if imagenes:
        if a.imagenes_en == "pagina-nueva":
            doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        escribir_imagenes(doc, imagenes, a.columnas, ancho, a.pies)
    escribir_texto(doc, despues, a.firma)
    doc.save(a.salida)
    print(f"Guardado {a.salida} ({len(imagenes)} imágenes)")


if __name__ == "__main__":
    main()
