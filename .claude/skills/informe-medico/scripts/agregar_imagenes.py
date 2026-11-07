#!/usr/bin/env python3
"""Añade las imágenes del eco a un informe YA redactado (.docx), sin tocar su texto, logo ni firma.

Uso:
  python3 agregar_imagenes.py --informe informe.docx --salida informe_con_imagenes.docx \
      [--columnas 2] [--ancho-cm 7.9] [--reemplazar] img1.jpg img2.jpg ...

- Las imágenes van en el orden dado, en una cuadrícula sin bordes, justo después del bloque de firma
  (línea "Dr. …" y las siguientes: especialidad, MPPS/CMA, RIF), como en los informes de Danilo.
- Por defecto todas las imágenes quedan del MISMO tamaño: se llevan a la proporción mediana rellenando con el color
  de fondo de la pantalla (sin estirar ni recortar: no se deforma la anatomía ni se pierden medidas). --sin-uniformar lo evita.
- --reemplazar quita antes las imágenes del eco que ya tuviera el informe (anchas y altas); logo y firma se conservan.
Requiere: pip install python-docx
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from informe_desde_modelo import abrir_reparado, es_eco, texto_runs  # noqa: E402

from docx.enum.table import WD_TABLE_ALIGNMENT  # noqa: E402
from docx.enum.text import WD_ALIGN_PARAGRAPH  # noqa: E402
from docx.oxml.ns import qn  # noqa: E402
from docx.shared import Cm  # noqa: E402


def uniformar(rutas):
    """Lleva todas las imágenes a la proporción (ancho/alto) mediana, rellenando con el color del borde."""
    import statistics
    import tempfile
    import numpy as np
    from PIL import Image
    ims = [Image.open(r).convert("RGB") for r in rutas]
    objetivo = statistics.median(im.width / im.height for im in ims)
    destino = Path(tempfile.mkdtemp(prefix="uniformes_"))
    salida = []
    for i, im in enumerate(ims):
        w, h = im.size
        if w / h > objetivo:          # más ancha: se añade alto (abajo, donde la pantalla es fondo oscuro)
            nw, nh = w, round(w / objetivo)
            franja = im.crop((0, h - max(4, h // 12), w, h))
            x, y = 0, 0
        else:                          # más alta: se añade ancho repartido a ambos lados
            nw, nh = round(h * objetivo), h
            franja = im.crop((0, 0, max(2, w // 50), h))
            x, y = (nw - w) // 2, 0
        arr = np.asarray(franja.convert("RGB")).reshape(-1, 3)
        orden = np.argsort(arr.sum(1))
        color = tuple(int(v) for v in arr[orden[len(orden) // 5]])  # tono oscuro del fondo de la pantalla (percentil 20)
        lienzo = Image.new("RGB", (nw, nh), color)
        lienzo.paste(im, (x, y))
        ruta = destino / f"{i:02d}.jpg"
        lienzo.save(ruta, quality=95)
        salida.append(str(ruta))
    return salida


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--informe", required=True)
    ap.add_argument("--salida", required=True)
    ap.add_argument("--columnas", type=int, default=2)
    ap.add_argument("--ancho-cm", type=float, default=7.9)  # 2 × 8.3 cm no cabe en carta con márgenes de 2.54 cm: Word recorta la imagen
    ap.add_argument("--reemplazar", action="store_true")
    ap.add_argument("--sin-uniformar", action="store_true", help="No igualar el tamaño de las imágenes")
    ap.add_argument("imagenes", nargs="+")
    a = ap.parse_args()
    for i in a.imagenes:
        if not Path(i).exists():
            sys.exit(f"No existe la imagen: {i}")

    if not a.sin_uniformar and len(a.imagenes) > 1:
        a.imagenes = uniformar(a.imagenes)
    doc = abrir_reparado(a.informe)
    body = doc.element.body
    if a.reemplazar:
        for d in list(body.iter(qn("w:drawing"))):
            if es_eco(d):
                r = d.getparent()
                r.getparent().remove(r)

    hijos = [el for el in body if el.tag == qn("w:p")]
    firma = next((p for p in hijos if re.match(r"\s*Dr\.?\s", texto_runs(p))), None)
    if firma is None:
        sys.exit('No encontré la línea de firma ("Dr. …")')
    ultimo = firma
    sig = firma.getnext()
    for _ in range(6):  # especialidad, MPPS/CMA, RIF…
        if sig is None or sig.tag != qn("w:p"):
            break
        if re.search(r"RIF|MPPS|CMA|CIRUJANO|ECOGRAF", texto_runs(sig), re.I):
            ultimo = sig
        sig = sig.getnext()

    cols = a.columnas
    t = doc.add_table(rows=(len(a.imagenes) + cols - 1) // cols, cols=cols)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, ruta in enumerate(a.imagenes):
        par = t.cell(i // cols, i % cols).paragraphs[0]
        par.alignment = WD_ALIGN_PARAGRAPH.CENTER
        par.add_run().add_picture(str(ruta), width=Cm(a.ancho_cm))
    ultimo.addnext(t._tbl)
    doc.save(a.salida)
    print(f"Guardado {a.salida} ({len(a.imagenes)} imágenes)")


if __name__ == "__main__":
    main()
