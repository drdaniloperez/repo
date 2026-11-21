#!/usr/bin/env python3
"""Agranda las imágenes de la tabla final (2 columnas) de un informe ya generado y deja espacio sobre ella.
  python3 agrandar_imagenes.py "<informe>.docx" 9.0     # ancho de cada imagen en cm (la tabla invade un poco los márgenes)
Aprobado por Danilo 2026-11-21 (eco de mama con 2 imágenes de 4 cuadrantes: 9 cm, separadas 16 pt de la firma)."""
import sys, docx
from docx.shared import Pt, Cm, Emu
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
p=sys.argv[1]; W=float(sys.argv[2]); d=docx.Document(p)
t=d.tables[-1]; tbl=t._tbl
cell=W+0.3; total=2*cell; text=16.51; ind=-(total-text)/2
tp=tbl.tblPr
for tag,val in (('w:tblW',total),('w:tblInd',ind)):
    e=tp.find(qn(tag))
    if e is None: e=OxmlElement(tag); tp.append(e)
    e.set(qn('w:w'),str(int(val*567))); e.set(qn('w:type'),'dxa')
for g in tbl.tblGrid.findall(qn('w:gridCol')): g.set(qn('w:w'),str(int(cell*567)))
for c in t.rows[0].cells: c.width=Cm(cell)
for il in tbl.iter(qn('wp:inline')):
    e=il.find(qn('wp:extent')); cx,cy=int(e.get('cx')),int(e.get('cy')); k=Cm(W)/cx
    ncx,ncy=int(cx*k),int(cy*k); e.set('cx',str(ncx)); e.set('cy',str(ncy))
    for x in il.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}ext'): x.set('cx',str(ncx)); x.set('cy',str(ncy))
# space before table: last paragraph before it
prev=tbl.getprevious()
while prev is not None and prev.tag!=qn('w:p'): prev=prev.getprevious()
docx.text.paragraph.Paragraph(prev,None).paragraph_format.space_after=Pt(16)
d.save(p)
