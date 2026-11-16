#!/usr/bin/env python3
"""Acabado aprobado (2026-11-16) para resumen/informe de egreso de Colina generado con informe_desde_modelo.py --texto.

  python3 egreso_estilo.py "<egreso>.docx"            # firma en línea, negrita selectiva, espacios, firma chica en hoja 1

1) Firma/sello del bloque final: de anclada a en línea, centrada, en un párrafo antes de "_____" (no tapa el nombre).
2) Quita párrafos vacíos; negrita SOLO en datos del paciente, signos vitales, diagnóstico del IDX, títulos de sección
   (subrayados) y rótulos del examen (Piel:, Abdomen:…); el resto normal. Interlineado 1.15, espacios entre secciones,
   18 pt antes de la firma, margen inferior 2 cm.
3) Firma y sello completos, pequeños (4.2 cm), en la esquina inferior derecha de la hoja 1 (ampliados ×4 con Lanczos).
No contiene datos de pacientes; la firma la toma del propio .docx.
"""
import copy, io, re, sys
import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn
from docx.shared import Cm, Pt
from docx.text.paragraph import Paragraph
from PIL import Image, ImageFilter

A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
HEAD = ('Nombre /', 'Médico tratante', 'Fecha de ingreso', 'Motivo de consulta')
SECC = ('Examen físico de egreso:', 'IDX.:', 'Se indica el siguiente plan médico:', 'Solicitando el siguiente')
LAB = re.compile(r'^(Piel:|Boca:|Cardiopulmonar:|Abdomen:|Genitales:|Extremidades:|Neurológico:)')


def firma_en_linea(d):
    par = [x for x in d.paragraphs if x.text.startswith('_____')][0]
    blob = None
    for a in list(par._p.iter(qn('wp:anchor'))):
        b = next(a.iter(A + 'blip')).get(qn('r:embed')); blob = d.part.related_parts[b].blob
        inl = OxmlElement('wp:inline')
        for k in ('distT', 'distB', 'distL', 'distR'): inl.set(k, '0')
        for tag in ('wp:extent', 'wp:effectExtent', 'wp:docPr', 'wp:cNvGraphicFramePr', 'a:graphic'):
            e = a.find(qn(tag))
            if e is not None: inl.append(copy.deepcopy(e))
        drawing = a.getparent(); drawing.replace(a, inl); run = drawing.getparent()
        newp = copy.deepcopy(par._p)
        for r in list(newp):
            if r.tag != qn('w:pPr'): newp.remove(r)
        par._p.addprevious(newp); newp.append(run)
        pp = Paragraph(newp, par._parent); pp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        pp.paragraph_format.space_before = Pt(18); pp.paragraph_format.space_after = Pt(0)
        par.paragraph_format.space_before = Pt(0); par.paragraph_format.space_after = Pt(0)
    if blob is None:  # ya estaba en línea
        prev = par._p.getprevious(); b = next(prev.iter(A + 'blip')).get(qn('r:embed'))
        blob = d.part.related_parts[b].blob
    return blob


def estilo(d):
    for x in d.paragraphs[2:]:
        if not x.text.strip() and not list(x._p.iter(qn('w:drawing'))): x._p.getparent().remove(x._p)
    start = False; prev = None
    for x in d.paragraphs:
        t = x.text
        if t.startswith(('INFORME MEDICO', 'RESUMEN DE EGRESO')): start = True; x.paragraph_format.space_after = Pt(10); continue
        if not start: continue
        if t.startswith('_____'): break
        if list(x._p.iter(qn('w:drawing'))) or not t.strip(): continue
        r0 = x.runs[0]; size, name = r0.font.size, r0.font.name
        for r in list(x.runs): r._r.getparent().remove(r._r)
        def add(txt, b, u=False):
            r = x.add_run(txt); r.bold = b; r.underline = u; r.font.size = size; r.font.name = name
        pf = x.paragraph_format; pf.space_before = Pt(0); pf.line_spacing = 1.15; pf.space_after = Pt(2)
        if t.startswith(HEAD):
            if t.startswith('Motivo'):
                a, b_ = t.split(':', 1); add(a + ':', True, True); add(b_, False); pf.space_after = Pt(8)
            else: add(t, True)
        elif t.startswith(SECC): add(t, True, True); pf.space_before = Pt(8)
        elif t.startswith('Fc:'): add(t, True); pf.space_after = Pt(4)
        elif prev and prev.startswith('IDX'): add(t, True)
        elif LAB.match(t): m = LAB.match(t).group(1); add(m, True); add(t[len(m):], False)
        elif t.startswith(('Se trata', 'Quién', 'Se evalúa')): add(t, False); pf.space_after = Pt(6)
        elif t.startswith(('El cual', 'La cual')): add(t, False); pf.space_before = Pt(6); pf.space_after = Pt(6)
        else: add(t, False)
        prev = t
    d.sections[0].bottom_margin = Cm(2.0)


def firma_hoja1(d, blob, ancho_cm=4.2):
    im = Image.open(io.BytesIO(blob)).convert('RGBA')
    big = im.resize((im.width * 4, im.height * 4), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=2, percent=80, threshold=2))
    buf = io.BytesIO(); big.save(buf, 'PNG'); buf.seek(0)
    par = [x for x in d.paragraphs if x.text.startswith(('INFORME MEDICO', 'RESUMEN DE EGRESO'))][0]
    run = par.add_run(); run.add_picture(buf, width=Cm(ancho_cm))
    inl = run._r.find('.//' + qn('wp:inline')); ext = inl.find(qn('wp:extent'))
    cx, cy = int(ext.get('cx')), int(ext.get('cy')); s = d.sections[0]
    x = s.page_width - Cm(1.3) - cx; y = s.page_height - Cm(0.6) - cy
    anc = parse_xml(f'<wp:anchor xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
                    f'distT="0" distB="0" distL="0" distR="0" simplePos="0" relativeHeight="251659264" behindDoc="0" '
                    f'locked="0" layoutInCell="1" allowOverlap="1"><wp:simplePos x="0" y="0"/>'
                    f'<wp:positionH relativeFrom="page"><wp:posOffset>{int(x)}</wp:posOffset></wp:positionH>'
                    f'<wp:positionV relativeFrom="page"><wp:posOffset>{int(y)}</wp:posOffset></wp:positionV>'
                    f'<wp:extent cx="{cx}" cy="{cy}"/><wp:effectExtent l="0" t="0" r="0" b="0"/><wp:wrapNone/></wp:anchor>')
    for tag in ('wp:docPr', 'wp:cNvGraphicFramePr', 'a:graphic'):
        e = inl.find(qn(tag))
        if e is not None: anc.append(e)
    inl.getparent().replace(inl, anc)


if __name__ == '__main__':
    p = sys.argv[1]; d = docx.Document(p)
    blob = firma_en_linea(d); estilo(d); firma_hoja1(d, blob); d.save(p); print('OK', p)
