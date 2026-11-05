#!/usr/bin/env python3
"""Genera un informe nuevo usando como modelo un informe anterior de Danilo del MISMO centro y tipo.

Conserva del modelo: logo/membrete, título, tabla de identificación, márgenes, fuentes, formato de los párrafos,
firma/sello (imágenes pequeñas) y bloque de firma. Reemplaza: datos del paciente, hallazgos, conclusión e imágenes.

Uso:
  python3 informe_desde_modelo.py --modelo "<informe anterior>.docx" --datos datos.json --salida "<nuevo>.docx"

datos.json:
{
  "titulo": "INFORME ECOGRÁFICO ABDOMINAL",
  "px": "Nombre Apellido", "ci": "12.345.678", "edad": "52 años", "fecha": "15/10/2026",
  "introduccion": "Se realiza estudio ecográfico en tiempo real con transductor convex de 3.5MHz en múltiples proyecciones, donde se evidencian los siguientes hallazgos:",
  "hallazgos": [["Hígado:", " forma, tamaño habitual ..."], ["Vesícula Biliar:", " ..."]],
  "extra_hallazgos": [["Vol prostático:", " 46.4 cm³"]],          (opcional, párrafos con la misma forma)
  "conclusion": ["Hígado Graso Grado I.", "Litiasis renal bilateral, RD: 0.4 cm, RI: 0.3 cm."],
  "conclusion_sin_numero": false,                                   (true → "Conclusión: Hiperplasia prostática grado II.")
  "despues_conclusion": ["Resto de estructuras dentro de limites normales."],   (opcional, texto normal)
  "imagenes": ["recortes/01_x.jpg", "recortes/02_y.jpg"],          (en orden)
  "ancho_imagen_cm": 8.3, "columnas": 2
}
Requiere: pip install python-docx
"""
import argparse
import copy
import io
import json
import re
import sys
import zipfile
from pathlib import Path

try:
    from docx import Document
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml.ns import qn
    from docx.shared import Cm
    from docx.text.paragraph import Paragraph
except ImportError:
    sys.exit("Falta python-docx: pip install python-docx")

EMU_CM = 360000
UMBRAL_ECO_CM = 7.0  # imágenes más anchas que esto son imágenes del eco; las menores son logo/firma/sello


def abrir_reparado(ruta):
    """Abre el .docx reescribiéndolo en memoria (tolera CRC dañado en imágenes)."""
    z = zipfile.ZipFile(ruta)
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as o:
        for n in z.namelist():
            try:
                d = z.read(n)
            except zipfile.BadZipFile:
                with z.open(n) as f:
                    f._expected_crc = None
                    d = f.read()
            o.writestr(n, d)
    buf.seek(0)
    return Document(buf)


def ancho_cm(drawing):
    ext = drawing.find(".//" + qn("wp:extent"))
    return int(ext.get("cx")) / EMU_CM if ext is not None else 0


def alto_cm(drawing):
    ext = drawing.find(".//" + qn("wp:extent"))
    return int(ext.get("cy")) / EMU_CM if ext is not None else 0


def es_eco(drawing):
    """Imagen del eco: ancha y alta. Los logos son anchos pero bajos; firma/sello son pequeños."""
    return ancho_cm(drawing) > UMBRAL_ECO_CM and alto_cm(drawing) > 4.0


def texto_runs(p_el):
    return "".join(t.text or "" for t in p_el.iter(qn("w:t")))


def runs_texto(p_el):
    return [r for r in p_el.findall(qn("w:r")) if r.find(qn("w:drawing")) is None and r.find(qn("w:pict")) is None]


def poner_texto_celda(celda, etiqueta, valor):
    p = celda.paragraphs[0]
    runs = runs_texto(p._p)
    if not runs:
        p.add_run(f"{etiqueta} {valor}")
        return
    for r in runs[1:]:
        p._p.remove(r)
    t = runs[0].find(qn("w:t"))
    if t is None:
        t = runs[0].makeelement(qn("w:t"), {})
        runs[0].append(t)
    t.text = f"{etiqueta} {valor}"
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    for extra in celda.paragraphs[1:]:
        extra._p.getparent().remove(extra._p)


def run_con_texto(modelo_run, texto, negrita=None):
    r = copy.deepcopy(modelo_run)
    for hijo in list(r):
        if hijo.tag != qn("w:rPr"):
            r.remove(hijo)
    if negrita is not None:
        rpr = r.find(qn("w:rPr"))
        if rpr is None:
            rpr = r.makeelement(qn("w:rPr"), {})
            r.insert(0, rpr)
        for b in rpr.findall(qn("w:b")) + rpr.findall(qn("w:bCs")):
            rpr.remove(b)
        if negrita:
            rpr.insert(0, rpr.makeelement(qn("w:b"), {}))
    partes = texto.split("\t")
    for i, parte in enumerate(partes):
        if i:
            r.append(r.makeelement(qn("w:tab"), {}))
        if parte:
            t = r.makeelement(qn("w:t"), {})
            t.text = parte
            t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
            r.append(t)
    return r


def nuevo_parrafo(modelo_p, segmentos):
    """segmentos: [(texto, negrita)] — copia pPr y el formato del primer run del párrafo modelo."""
    p = modelo_p.makeelement(qn("w:p"), {})
    ppr = modelo_p.find(qn("w:pPr"))
    if ppr is not None:
        p.append(copy.deepcopy(ppr))
    base = runs_texto(modelo_p)
    base = base[0] if base else p.makeelement(qn("w:r"), {})
    for texto, negrita in segmentos:
        p.append(run_con_texto(base, texto, negrita))
    return p


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--modelo", required=True)
    ap.add_argument("--datos", required=True)
    ap.add_argument("--salida", required=True)
    a = ap.parse_args()
    datos = json.loads(Path(a.datos).read_text(encoding="utf-8"))
    base_dir = Path(a.datos).parent
    doc = abrir_reparado(a.modelo)
    body = doc.element.body
    parrafos = [Paragraph(p, doc) for p in body.iter(qn("w:p"))]

    # 1) tabla de identificación
    tabla = next((t for t in doc.tables if re.search(r"Px\s*:", t.rows[0].cells[0].text, re.I)), None)
    if tabla is None:
        sys.exit("No encontré la tabla de identificación (Px / Ci / Edad / Fecha) en el modelo")
    etiquetas = []
    for c in tabla.rows[0].cells:
        m = re.match(r"\s*([^:]+:)", c.text)
        etiquetas.append(m.group(1).strip() if m else "")
    valores = {"px": datos.get("px", ""), "ci": datos.get("ci", ""), "edad": datos.get("edad", ""), "fecha": datos.get("fecha", "")}
    vistos = set()
    for c, et in zip(tabla.rows[0].cells, etiquetas):
        if id(c._tc) in vistos:
            continue
        vistos.add(id(c._tc))
        clave = {"px": "px", "ci": "ci", "edad": "edad", "fecha": "fecha"}.get(et.lower().rstrip(":").strip())
        if clave:
            poner_texto_celda(c, et, valores[clave])

    # 2) título
    titulo = next((p for p in parrafos if "INFORME" in p.text.upper() and p._p.getparent() is body), None)
    if titulo is not None and datos.get("titulo"):
        runs = runs_texto(titulo._p)
        for r in runs[1:]:
            titulo._p.remove(r)
        if runs:
            nuevo = run_con_texto(runs[0], datos["titulo"])
            titulo._p.replace(runs[0], nuevo)

    # 3) cuerpo: desde la introducción/primer hallazgo hasta la línea "Dr. ..." de la firma
    hijos = list(body)
    def idx(el):
        return hijos.index(el)
    firma = next((p for p in parrafos if p._p.getparent() is body and re.match(r"\s*Dr\.?\s", p.text)), None)
    if firma is None:
        sys.exit("No encontré la línea de firma (\"Dr. ...\") en el modelo")
    inicio_el = None
    for p in parrafos:
        if p._p.getparent() is not body or idx(p._p) >= idx(firma._p):
            continue
        if titulo is not None and idx(p._p) <= idx(titulo._p):
            continue
        if idx(p._p) <= idx(tabla._tbl):
            continue
        if p.text.strip() and not re.match(r"\s*(Px|Ci|Edad|Fecha)\s*:", p.text):
            inicio_el = p._p
            break
    if inicio_el is None:
        sys.exit("No encontré el cuerpo del informe en el modelo")
    cuerpo = [el for el in hijos[idx(inicio_el):idx(firma._p)] if el.tag == qn("w:p")]

    # párrafos modelo para el formato
    def con_etiqueta(el):
        rs = runs_texto(el)
        return rs and texto_runs(el).strip() and ":" in texto_runs(el)[:40]
    m_intro = next((el for el in cuerpo if texto_runs(el).strip().lower().startswith("se realiza")), cuerpo[0])
    m_hall = next((el for el in cuerpo if con_etiqueta(el) and not texto_runs(el).strip().lower().startswith(("se realiza", "conclus"))), m_intro)
    m_conc = next((el for el in cuerpo if texto_runs(el).strip().lower().startswith("conclus")), m_hall)
    todo_negrita = all((r.find(qn("w:rPr")) is not None and r.find(qn("w:rPr")).find(qn("w:b")) is not None)
                       for r in runs_texto(m_hall) if texto_runs(r).strip())
    m_hall, m_intro, m_conc = (copy.deepcopy(x) for x in (m_hall, m_intro, m_conc))

    # guardar dibujos pequeños (firma/sello) que estén anclados en el cuerpo
    pequenos = []
    for el in cuerpo:
        for r in el.findall(qn("w:r")):
            d = r.find(qn("w:drawing"))
            if d is not None and not es_eco(d):
                pequenos.append(r)
    for el in cuerpo:
        body.remove(el)

    nuevos = []
    if datos.get("introduccion"):
        nuevos.append(nuevo_parrafo(m_intro, [(datos["introduccion"], None)]))
    for et, tx in datos.get("hallazgos", []) + datos.get("extra_hallazgos", []):
        nuevos.append(nuevo_parrafo(m_hall, [(et, True), (tx, True if todo_negrita else False)]))
    conc = datos.get("conclusion", [])
    if conc:
        vacio = nuevo_parrafo(m_hall, [("", False)])
        nuevos.append(vacio)
        if datos.get("conclusion_sin_numero"):
            nuevos.append(nuevo_parrafo(m_conc, [("Conclusión: " + conc[0], True)]))
        else:
            for i, c in enumerate(conc, 1):
                pref = "Conclusión:\t" if i == 1 else "\t\t"
                nuevos.append(nuevo_parrafo(m_conc, [(f"{pref}{i}) {c}", True)]))
    for linea in datos.get("despues_conclusion", []):
        nuevos.append(nuevo_parrafo(m_conc, [("\t" + linea, False)]))
    # párrafo que sostiene la firma/sello
    porta = nuevo_parrafo(m_conc, [("", False)])
    alto_firma = 0.0
    for r in pequenos:
        d = r.find(qn("w:drawing"))
        anc = d.find(qn("wp:anchor"))
        if anc is not None:  # la firma/sello queda pegada justo encima del nombre, no en una posición fija de la página
            pv = anc.find(qn("wp:positionV"))
            if pv is not None:
                pv.set("relativeFrom", "paragraph")
                off = pv.find(qn("wp:posOffset"))
                if off is None:
                    for h in list(pv):
                        pv.remove(h)
                    off = pv.makeelement(qn("wp:posOffset"), {})
                    pv.append(off)
                off.text = str(int(0.2 * EMU_CM))
        alto_firma = max(alto_firma, alto_cm(d))
        porta.append(r)
    if alto_firma:  # reservar el alto de la firma
        ppr = porta.find(qn("w:pPr"))
        if ppr is None:
            ppr = porta.makeelement(qn("w:pPr"), {})
            porta.insert(0, ppr)
        sp = ppr.find(qn("w:spacing"))
        if sp is None:
            sp = ppr.makeelement(qn("w:spacing"), {})
            ppr.append(sp)
        sp.set(qn("w:before"), "120")
        sp.set(qn("w:after"), str(int((alto_firma + 0.3) * 567)))
    nuevos.append(porta)
    for el in nuevos:
        firma._p.addprevious(el)

    # 4) quitar imágenes del eco del modelo (en cualquier parte) y párrafos que queden vacíos
    for d in list(body.iter(qn("w:drawing"))):
        if es_eco(d):
            r = d.getparent()
            p = r.getparent()
            p.remove(r)
            if p.tag == qn("w:p") and not texto_runs(p).strip() and p.find(".//" + qn("w:drawing")) is None and p.getparent() is body:
                body.remove(p)
    for t in list(body.iter(qn("w:tbl"))):  # tablas que solo contenían imágenes del eco
        if t is not tabla._tbl and not texto_runs(t).strip() and t.find(".//" + qn("w:drawing")) is None:
            t.getparent().remove(t)

    # 5) imágenes nuevas en cuadrícula, después del bloque de firma
    imagenes = [base_dir / i if not Path(i).is_absolute() and not Path(i).exists() else Path(i) for i in datos.get("imagenes", [])]
    if imagenes:
        cols = int(datos.get("columnas", 2))
        ancho = float(datos.get("ancho_imagen_cm", 8.3))
        bloque = [el for el in list(body)[idx_seguro(body, firma._p):] if el.tag == qn("w:p")]
        ultimo = firma._p
        for el in bloque[:6]:
            if re.search(r"RIF|MPPS|CMA|CIRUJANO|ECOGRAF", texto_runs(el), re.I):
                ultimo = el
        filas = (len(imagenes) + cols - 1) // cols
        t = doc.add_table(rows=filas, cols=cols)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        for i, ruta in enumerate(imagenes):
            if not ruta.exists():
                sys.exit(f"No existe la imagen: {ruta}")
            par = t.cell(i // cols, i % cols).paragraphs[0]
            par.alignment = WD_ALIGN_PARAGRAPH.CENTER
            par.add_run().add_picture(str(ruta), width=Cm(ancho))
        ultimo.addnext(t._tbl)

    doc.core_properties.author = "Dr. Danilo Pérez T."
    doc.save(a.salida)
    print(f"Guardado {a.salida}")


def idx_seguro(body, el):
    return list(body).index(el)


if __name__ == "__main__":
    main()
