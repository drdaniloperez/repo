#!/usr/bin/env python3
"""Genera un informe nuevo usando como modelo un informe anterior de Danilo del MISMO centro y tipo.

Conserva del modelo: logo/membrete, título, tabla de identificación, márgenes, fuentes, formato de los párrafos,
firma/sello (imágenes pequeñas) y bloque de firma. Reemplaza: datos del paciente, hallazgos, conclusión e imágenes.

Uso:
  python3 informe_desde_modelo.py --modelo "<informe anterior>.docx" --datos datos.json --salida "<nuevo>.docx" [--centro colinas|san-jose|pdvsa|razetti]

La institución del modelo se reconoce por su LOGO (formatos/logos/logos.json). Si se indica --centro (o "centro" en
datos.json) y el modelo es de otra institución, se detiene: el logo y el membrete deben ser los de la institución
donde se hizo el estudio.

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
  "ancho_imagen_cm": 7.6, "columnas": 2, "uniformar": true     (máx. 7.6 cm; las imágenes se igualan de tamaño)
}
Documentos de texto (resumen de ingreso, egreso, extensión, evaluación, informe médico, listas, cartas):
  python3 informe_desde_modelo.py --modelo "<documento anterior>.docx" --texto nuevo.txt --salida "<nuevo>.docx" [--centro …]
  nuevo.txt = el documento completo, una línea por párrafo (la primera es el título; tabulaciones con TAB). Se conservan
  el membrete/logos, márgenes, fuentes, la firma/sello y el bloque de firma del modelo; cada párrafo nuevo copia el
  formato del párrafo del modelo con la misma etiqueta ("Examen físico:", "IDX.:", "Tlfno", "1." …) o, si no la hay,
  el del párrafo narrativo más largo. Si el .txt trae su propio bloque de firma, se ignora (manda el del modelo).
  Líneas con "|" forman una tabla con el formato de la primera tabla del modelo (1.ª línea = encabezado;
  "//" separa párrafos dentro de una celda), p. ej. la programación quirúrgica del Razetti.
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
UMBRAL_ECO_CM = 4.5  # imágenes del eco: > 4.5 cm de ancho y > 4 cm de alto (logo: bajo; firma/sello: < 2 cm de alto).
# Antes era 7.0 y quedaban imágenes viejas del modelo de 6.1 cm (San José, 2026-11-08).


LOGOS_JSON = Path(__file__).resolve().parent.parent / "formatos" / "logos" / "logos.json"


def centro_del_modelo(doc):
    """Reconoce la institución por el md5 de las imágenes del documento (logo)."""
    import hashlib
    try:
        info = json.loads(LOGOS_JSON.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None, {}
    hashes = {hashlib.md5(rel.target_part.blob).hexdigest()
              for rel in doc.part.rels.values() if "image" in rel.reltype}
    for clave, d in info.items():
        if hashes & set(d.get("md5_en_docx", [])):
            return clave, info
    return None, info


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


def a_en_linea(anc):
    """Convierte un wp:anchor (imagen flotante) en wp:inline conservando tamaño, id y gráfico."""
    inl = anc.makeelement(qn("wp:inline"), {k: "0" for k in ("distT", "distB", "distL", "distR")})
    for tag in ("wp:extent", "wp:effectExtent", "wp:docPr", "wp:cNvGraphicFramePr", "a:graphic"):
        e = anc.find(qn(tag))
        if e is not None:
            inl.append(e)
    return inl


def espaciado(p_el, antes=None, despues=None, sencillo=False):
    ppr = p_el.find(qn("w:pPr"))
    if ppr is None:
        ppr = p_el.makeelement(qn("w:pPr"), {})
        p_el.insert(0, ppr)
    sp = ppr.find(qn("w:spacing"))
    if sp is None:
        sp = ppr.makeelement(qn("w:spacing"), {})
        ppr.append(sp)
    if antes is not None:
        sp.set(qn("w:before"), str(antes))
    if despues is not None:
        sp.set(qn("w:after"), str(despues))
    if sencillo:
        sp.set(qn("w:line"), "240")
        sp.set(qn("w:lineRule"), "auto")


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
    ap.add_argument("--datos")
    ap.add_argument("--texto", help="documento de texto completo (modo documentos clínicos/listas)")
    ap.add_argument("--salida", required=True)
    ap.add_argument("--centro", choices=["colinas", "san-jose", "pdvsa", "razetti"])
    a = ap.parse_args()
    if not a.datos and not a.texto:
        sys.exit("Indica --datos (informe de eco) o --texto (documento de texto)")
    datos = json.loads(Path(a.datos).read_text(encoding="utf-8")) if a.datos else {}
    base_dir = Path(a.datos or a.texto).parent
    doc = abrir_reparado(a.modelo)
    centro, info = centro_del_modelo(doc)
    pedido = a.centro or datos.get("centro")
    nombre = lambda c: info.get(c, {}).get("nombre", c)
    print(f"Institución del modelo (por su logo): {nombre(centro) if centro else 'no reconocida'}")
    if pedido and centro and pedido != centro:
        sys.exit(f"El modelo es de {nombre(centro)} pero el estudio es de {nombre(pedido)}: usa un modelo con el logo de "
                 f"{nombre(pedido)} (o armar_informe_docx.py --centro {pedido}).")
    if pedido and not centro:
        print(f"⚠ No reconocí el logo del modelo; verifica que sea el de {nombre(pedido)}.")
    body = doc.element.body
    if a.texto:
        documento_de_texto(doc, Path(a.texto).read_text(encoding="utf-8").splitlines())
        quitar_vacios_finales(body)
        doc.core_properties.author = "Dr. Danilo Pérez T."
        doc.save(a.salida)
        print(f"Guardado {a.salida}")
        return
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
        if anc is not None:  # firma/sello EN LÍNEA (centrada, justo encima del nombre): sin huecos ni solapes (2026-11-08)
            d.replace(anc, a_en_linea(anc))
        alto_firma = max(alto_firma, alto_cm(d))
        porta.append(r)
    if alto_firma:
        Paragraph(porta, None).alignment = WD_ALIGN_PARAGRAPH.CENTER
        espaciado(porta, antes=120, despues=0)
    nuevos.append(porta)
    for el in nuevos:
        firma._p.addprevious(el)

    # 3b) bloque de firma compacto (pedido por Danilo 2026-11-08): interlineado sencillo y sin espacio entre líneas
    for el in list(body)[idx_seguro(body, firma._p):][:6]:
        if el.tag == qn("w:p") and (el is firma._p or RX_FIRMA.match(texto_runs(el))):
            espaciado(el, antes=0, despues=0, sencillo=True)

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
        # celdas de ≈ 8.26 cm (4680 dxa) con márgenes de 0.19 cm: más de 7.6 cm corta el recuadro de medidas
        ancho = min(float(datos.get("ancho_imagen_cm", 7.6)), 7.6)
        if datos.get("uniformar", True):  # todas del mismo tamaño, rellenando con el fondo oscuro (sin estirar ni recortar)
            sys.path.insert(0, str(Path(__file__).resolve().parent))  # también con python -I (modo aislado)
            from agregar_imagenes import uniformar
            faltan = [r for r in imagenes if not r.exists()]
            if faltan:
                sys.exit(f"No existe la imagen: {faltan[0]}")
            imagenes = [Path(r) for r in uniformar([str(r) for r in imagenes])]
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

    quitar_vacios_finales(body)
    doc.core_properties.author = "Dr. Danilo Pérez T."
    doc.save(a.salida)
    print(f"Guardado {a.salida}")


RX_FIRMA = re.compile(r"\s*(MPPS|RIF|CIRUJANO|ECOGRAF|C\.?M\.?A)", re.I)  # líneas que abren el bloque de firma


def clave_parrafo(texto):
    """Etiqueta que identifica el tipo de párrafo: 'examen físico:', 'idx.:', '#' (línea numerada), 'tlfno'…"""
    t = texto.strip().lower()
    if re.match(r"\d+\s*[.)-]", t):
        return "#"
    m = re.match(r"([^:]{1,40}):", t)
    if m:
        return m.group(1).strip()
    return t.split(" ")[0] if t else ""


def documento_de_texto(doc, lineas):
    body = doc.element.body
    hijos = [el for el in body if el.tag in (qn("w:p"), qn("w:tbl"))]
    textos = [texto_runs(el).strip() for el in hijos]
    i_tit = next((i for i, t in enumerate(textos) if t and hijos[i].tag == qn("w:p")), None)
    if i_tit is None:
        sys.exit("El modelo no tiene texto")
    # bloque de firma: "____" o "Dr. …" seguido de MPPS/RIF/cirujano…
    i_fin = len(hijos)
    for i in range(i_tit + 1, len(hijos)):
        if re.match(r"\s*(_{3,}|Dr\.?\s|Danilo\s+P[eé]rez)", textos[i]) and any(RX_FIRMA.match(t) for t in textos[i + 1:i + 5]):
            i_fin = i
            break
    # quitar del .txt líneas de control y su propio bloque de firma
    lineas = [l.rstrip(chr(13)) for l in lineas if not l.startswith(("MODELO:", "CENTRO:"))]
    while lineas and not lineas[0].strip():
        lineas.pop(0)
    for k, l in enumerate(lineas):
        if re.match(r"\s*(_{3,}|Dr\.?\s+Danilo|Danilo\s+P[eé]rez)", l) and any(RX_FIRMA.match(x) for x in lineas[k + 1:k + 5]):
            lineas = lineas[:k]
            break
    while lineas and not lineas[-1].strip():
        lineas.pop()
    if not lineas:
        sys.exit("El texto está vacío")
    # título
    tit = hijos[i_tit]
    runs = runs_texto(tit)
    if runs:
        for r in runs[1:]:
            tit.remove(r)
        tit.replace(runs[0], run_con_texto(runs[0], lineas[0].strip()))
    # modelos de formato por etiqueta
    cuerpo = hijos[i_tit + 1:i_fin]
    modelos, vacio, narrativo = {}, None, None
    for el in cuerpo:
        if el.tag != qn("w:p"):
            continue
        t = texto_runs(el)
        if not t.strip():
            vacio = vacio if vacio is not None else copy.deepcopy(el)
            continue
        modelos.setdefault(clave_parrafo(t), copy.deepcopy(el))
        if narrativo is None or len(t) > len(texto_runs(narrativo)):
            narrativo = copy.deepcopy(el)
    if narrativo is None:
        narrativo = copy.deepcopy(tit)
    for m in [vacio, narrativo, *modelos.values()]:  # un salto de sección escondido en el modelo no debe repetirse
        if m is not None:
            for sp in m.findall(qn("w:pPr") + "/" + qn("w:sectPr")):
                sp.getparent().remove(sp)
    # firma/sello (dibujos anclados en el cuerpo) se conservan
    pequenos = [r for el in cuerpo for r in el.iter(qn("w:r")) if r.find(qn("w:drawing")) is not None]
    for el in cuerpo:
        body.remove(el)
    tabla_modelo = next((copy.deepcopy(el) for el in cuerpo if el.tag == qn("w:tbl")), None)
    ancla = hijos[i_fin] if i_fin < len(hijos) else body.find(qn("w:sectPr"))
    bloque = []  # filas de tabla pendientes ("celda | celda | …")

    def volcar_tabla():
        if bloque and tabla_modelo is not None:
            ancla.addprevious(tabla_desde_modelo(tabla_modelo, bloque))
        elif bloque:  # sin tabla en el modelo: una línea por fila, celdas separadas por tabulación
            for fila in bloque:
                ancla.addprevious(nuevo_parrafo(narrativo, [("	".join(fila), False)]))
        bloque.clear()

    for linea in lineas[1:]:
        if "|" in linea:
            celdas = linea.rstrip().split("|")  # " | A | B" = primera celda vacía (columna N.º)
            if linea.startswith("|"):
                celdas = celdas[1:]
            if linea.rstrip().endswith("|"):
                celdas = celdas[:-1]
            bloque.append([c.strip() for c in celdas])
            continue
        volcar_tabla()
        if not linea.strip():
            p = copy.deepcopy(vacio) if vacio is not None else nuevo_parrafo(narrativo, [("", False)])
            for r in p.findall(qn("w:r")):
                p.remove(r)
        else:
            m = modelos.get(clave_parrafo(linea), narrativo)
            if not texto_runs(m)[:1].isspace():  # sangría/tab que el modelo no lleva (desplaza el texto a una tabulación)
                linea = linea.lstrip()
            rs = [r for r in runs_texto(m) if texto_runs(r).strip()]
            p = m.makeelement(qn("w:p"), {})
            if m.find(qn("w:pPr")) is not None:
                p.append(copy.deepcopy(m.find(qn("w:pPr"))))
            et = re.match(r"(\s*[^:]{1,40}:)(.*)", linea) if ":" in linea[:41] else None
            if et and rs:
                p.append(run_con_texto(rs[0], et.group(1)))
                if et.group(2):
                    p.append(run_con_texto(rs[-1] if len(rs) > 1 else rs[0], et.group(2)))
            else:
                base = rs[0] if rs else p.makeelement(qn("w:r"), {})
                p.append(run_con_texto(base, linea))
        ancla.addprevious(p)
    volcar_tabla()
    # los párrafos vacíos que el modelo deja antes del bloque de firma (espacio para la firma/sello)
    finales = 0
    for el in reversed(cuerpo):
        if el.tag == qn("w:p") and not texto_runs(el).strip() and el.find(".//" + qn("w:drawing")) is None:
            finales += 1
        else:
            break
    for _ in range(finales):
        p = copy.deepcopy(vacio) if vacio is not None else nuevo_parrafo(narrativo, [("", False)])
        for r in p.findall(qn("w:r")):
            p.remove(r)
        ancla.addprevious(p)
    if pequenos:
        destino = hijos[i_fin] if i_fin < len(hijos) else None
        # estilo clínico (Colina/San José): la firma se superpone a "____" y/o "Dr. …" y termina encima de
        # "Ecografista Integral/Cirujano Pediatra." — estilo eco: va en su propio espacio encima de "Dr. …"
        lineas_sobre = 0
        if destino is not None:
            if re.match(r"\s*_{3,}", texto_runs(destino)):
                lineas_sobre = 2
            elif any(re.match(r"\s*Ecografista\s+Integral", t) for t in textos[i_fin + 1:i_fin + 3]):
                lineas_sobre = 1
        sobre_linea = lineas_sobre > 0
        if not sobre_linea:  # estilo eco: firma/sello en su propio párrafo, encima de "Dr. …", con su alto reservado
            porta = nuevo_parrafo(narrativo, [("", False)])
            ancla.addprevious(porta)
            destino = porta
        alto_max = 0.0
        for r in pequenos:
            d = r.find(qn("w:drawing"))
            alto_max = max(alto_max, alto_cm(d))
            anc = d.find(qn("wp:anchor"))
            if anc is not None:
                pv = anc.find(qn("wp:positionV"))
                if pv is not None:
                    pv.set("relativeFrom", "paragraph")
                    for h in list(pv):
                        pv.remove(h)
                    off = pv.makeelement(qn("wp:posOffset"), {})
                    # sobre "____ / Dr. …": termina justo encima de "Ecografista…/MPPS/RIF" (como en sus originales)
                    off.text = str(int(((0.6 * lineas_sobre - 0.05 - alto_cm(d)) if sobre_linea else 0.2) * EMU_CM))
                    pv.append(off)
            destino.append(r)
        if not sobre_linea and alto_max:
            ppr = destino.find(qn("w:pPr"))
            if ppr is None:
                ppr = destino.makeelement(qn("w:pPr"), {})
                destino.insert(0, ppr)
            sp = ppr.find(qn("w:spacing"))
            if sp is None:
                sp = ppr.makeelement(qn("w:spacing"), {})
                ppr.append(sp)
            sp.set(qn("w:before"), "120")
            sp.set(qn("w:after"), str(int((alto_max + 0.3) * 567)))


def tabla_desde_modelo(tabla, filas):
    """Copia la tabla del modelo: la 1.ª fila nueva usa el formato de su encabezado y las demás el de su 2.ª fila."""
    t = copy.deepcopy(tabla)
    trs = t.findall(qn("w:tr"))
    enc, dato = trs[0], (trs[1] if len(trs) > 1 else trs[0])
    for tr in trs:
        t.remove(tr)
    for k, fila in enumerate(filas):
        tr = copy.deepcopy(enc if k == 0 else dato)
        tcs = tr.findall(qn("w:tc"))
        for j, tc in enumerate(tcs):
            ps = tc.findall(qn("w:p"))
            for extra in ps[1:]:
                tc.remove(extra)
            p0 = ps[0]
            rs = [r for r in runs_texto(p0)]
            base = next((r for r in rs if texto_runs(r).strip()), rs[0] if rs else None)
            for r in rs:
                p0.remove(r)
            valor = fila[j] if j < len(fila) else ""
            partes = valor.split("//")  # "//" = salto de párrafo dentro de la celda
            for n, parte in enumerate(partes):
                pp = p0 if n == 0 else copy.deepcopy(p0)
                if n:
                    for r in pp.findall(qn("w:r")):
                        pp.remove(r)
                    tc.append(pp)
                pp.append(run_con_texto(base if base is not None else pp.makeelement(qn("w:r"), {}), parte.strip()))
        t.append(tr)
    return t


def quitar_vacios_finales(body):
    """Borra los párrafos vacíos del final (crean una página en blanco); deja uno mínimo tras una tabla final."""
    from docx.shared import Pt
    hijos = [el for el in body if el.tag != qn("w:sectPr")]
    while len(hijos) > 1 and hijos[-1].tag == qn("w:p") and not texto_runs(hijos[-1]).strip() \
            and hijos[-1].find(".//" + qn("w:drawing")) is None and hijos[-1].find(".//" + qn("w:br")) is None:
        if hijos[-2].tag == qn("w:tbl"):  # Word exige un párrafo después de una tabla final: se deja diminuto
            p = Paragraph(hijos[-1], None)
            p.paragraph_format.space_before = p.paragraph_format.space_after = Pt(0)
            for r in p.runs:
                r.font.size = Pt(1)
            ppr = hijos[-1].find(qn("w:pPr"))
            rpr = ppr.find(qn("w:rPr")) if ppr is not None else None
            if ppr is not None and rpr is None:
                rpr = ppr.makeelement(qn("w:rPr"), {})
                ppr.append(rpr)
            if rpr is not None:
                for v in rpr.findall(qn("w:sz")):
                    rpr.remove(v)
                sz = rpr.makeelement(qn("w:sz"), {qn("w:val"): "2"})
                rpr.append(sz)
            break
        body.remove(hijos.pop())


def idx_seguro(body, el):
    return list(body).index(el)


if __name__ == "__main__":
    main()
