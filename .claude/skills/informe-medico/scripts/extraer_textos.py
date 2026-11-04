#!/usr/bin/env python3
"""Extrae el texto de los informes de ejemplo y arma un inventario clasificado por tipo.

Uso (en el equipo donde está conectado el disco):
    python3 extraer_textos.py "/Volumes/Rodolfo SSD/Alarms"            # macOS
    python3 extraer_textos.py "E:\\Alarms" --salida "C:\\informes-txt"   # Windows

Escribe en --salida (por defecto ~/informes-extraidos, FUERA del repo, porque contiene datos de pacientes):
    textos/<ruta-relativa>.txt   texto plano de cada archivo
    imagenes/<ruta-relativa>/    imágenes incrustadas en cada .docx (solo con --con-imagenes)
    inventario.csv               archivo, extensión, tamaño, tipo sugerido, primera línea, caracteres, n.º de imágenes

Formatos: .docx .docm .dotx (sin dependencias), .pdf (pypdf o pdftotext), .doc .rtf .odt .pages
(textutil en macOS, o antiword / LibreOffice si están instalados), .txt.
"""
import argparse
import csv
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

TIPOS = [  # (tipo, patrones) — se evalúan en orden; gana el primero que coincide
    ("extension-hospitalizacion", r"extensi[oó]n\s+de\s+(la\s+)?hospitalizaci[oó]n|pr[oó]rroga|d[ií]as\s+adicionales"),
    ("hospitalizacion", r"hospitalizaci[oó]n|epicrisis|fecha\s+de\s+ingreso|egreso"),
    ("procedimiento-quirurgico", r"operatori|intervenci[oó]n\s+quir|t[eé]cnica\s+quir|cirujano|anestesia|procedimiento\s+quir"),
    ("eco-obstetrico", r"(eco|ultra).{0,40}obst[eé]tric|biometr[ií]a\s+fetal|frecuencia\s+card[ií]aca\s+fetal|l[ií]quido\s+amni[oó]tico"),
    ("eco-tiroides", r"(eco|ultra).{0,40}(tiroid|cuello)|ti-?rads"),
    ("eco-mamario", r"(eco|ultra).{0,40}mama|bi-?rads"),
    ("eco-pelvico", r"(eco|ultra).{0,40}(p[eé]lvic|transvaginal|ginecol)|endometrio"),
    ("eco-renal", r"(eco|ultra).{0,40}(renal|vías\s+urinarias|urol[oó]gic|prost)"),
    ("eco-testicular", r"(eco|ultra).{0,40}(testic|escrot)"),
    ("eco-doppler", r"doppler"),
    ("eco-partes-blandas", r"(eco|ultra).{0,40}(partes\s+blandas|musculoesquel|pared\s+abdominal|inguinal)"),
    ("eco-abdominal", r"(eco|ultra).{0,40}abdom|h[ií]gado.{0,200}ves[ií]cula"),
    ("eco-otro", r"ecosonograma|ecograf[ií]a|ultrasonido"),
    ("informe-medico", r"informe\s+m[eé]dico|a\s+quien\s+pueda\s+interesar|impresi[oó]n\s+diagn[oó]stica"),
    ("constancia-reposo", r"constancia|reposo\s+m[eé]dico"),
    ("recipe", r"r[eé]cipe|indicaciones"),
]
EXT_OK = {".docx", ".docm", ".dotx", ".pdf", ".doc", ".rtf", ".odt", ".pages", ".txt"}


def texto_docx(ruta: Path) -> str:
    ns = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    partes = []
    with zipfile.ZipFile(ruta) as z:
        nombres = ["word/document.xml"] + sorted(n for n in z.namelist() if re.match(r"word/(header|footer)\d*\.xml", n))
        for nombre in nombres:
            if nombre not in z.namelist():
                continue
            raiz = ET.fromstring(z.read(nombre))
            for p in raiz.iter(f"{ns}p"):
                linea = "".join(((t.text or "") if t.tag == f"{ns}t" else "\t") for t in p.iter() if t.tag in (f"{ns}t", f"{ns}tab"))
                partes.append(linea)
    return "\n".join(partes)


def texto_pdf(ruta: Path) -> str:
    try:
        from pypdf import PdfReader  # type: ignore
        return "\n".join((pag.extract_text() or "") for pag in PdfReader(str(ruta)).pages)
    except ImportError:
        pass
    if shutil.which("pdftotext"):
        return subprocess.run(["pdftotext", "-layout", str(ruta), "-"], capture_output=True, text=True, timeout=120).stdout
    raise RuntimeError("instala pypdf (pip install pypdf) o poppler (pdftotext)")


def texto_otro(ruta: Path) -> str:
    if shutil.which("textutil"):  # macOS
        return subprocess.run(["textutil", "-convert", "txt", "-stdout", str(ruta)], capture_output=True, text=True, timeout=120).stdout
    if ruta.suffix.lower() == ".doc" and shutil.which("antiword"):
        return subprocess.run(["antiword", str(ruta)], capture_output=True, text=True, timeout=120).stdout
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if soffice:
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run([soffice, "--headless", "--convert-to", "txt:Text", "--outdir", tmp, str(ruta)], capture_output=True, timeout=180)
            salida = Path(tmp) / (ruta.stem + ".txt")
            return salida.read_text(errors="replace") if salida.exists() else ""
    raise RuntimeError("sin conversor para este formato (usa macOS textutil, antiword o LibreOffice)")


def extraer(ruta: Path) -> str:
    ext = ruta.suffix.lower()
    if ext in {".docx", ".docm", ".dotx"}:
        return texto_docx(ruta)
    if ext == ".pdf":
        return texto_pdf(ruta)
    if ext == ".txt":
        return ruta.read_text(errors="replace")
    return texto_otro(ruta)


def imagenes_docx(ruta: Path, destino: Path | None) -> int:
    """Cuenta (y opcionalmente guarda) las imágenes incrustadas de un .docx."""
    if ruta.suffix.lower() not in {".docx", ".docm", ".dotx"}:
        return 0
    with zipfile.ZipFile(ruta) as z:
        medios = [n for n in z.namelist() if n.startswith("word/media/")]
        if destino and medios:
            destino.mkdir(parents=True, exist_ok=True)
            for n in medios:
                (destino / Path(n).name).write_bytes(z.read(n))
    return len(medios)


def clasificar(texto: str, nombre: str) -> str:
    muestra = (nombre + "\n" + texto[:3000]).lower()
    for tipo, patron in TIPOS:
        if re.search(patron, muestra):
            return tipo
    return "sin-clasificar"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("origen", type=Path, help="Carpeta con los informes de ejemplo")
    ap.add_argument("--salida", type=Path, default=Path.home() / "informes-extraidos")
    ap.add_argument("--con-imagenes", action="store_true", help="Guarda también las imágenes incrustadas de los .docx")
    args = ap.parse_args()

    if not args.origen.is_dir():
        sys.exit(f"No existe la carpeta: {args.origen}")
    textos = args.salida / "textos"
    textos.mkdir(parents=True, exist_ok=True)

    filas, errores = [], 0
    archivos = sorted(p for p in args.origen.rglob("*") if p.is_file() and p.suffix.lower() in EXT_OK and not p.name.startswith(("~$", "._")))
    for i, ruta in enumerate(archivos, 1):
        rel = ruta.relative_to(args.origen)
        try:
            texto = extraer(ruta).strip()
            destino = textos / rel.with_suffix(rel.suffix + ".txt")
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.write_text(texto, encoding="utf-8")
            n_img = imagenes_docx(ruta, args.salida / "imagenes" / rel if args.con_imagenes else None)
            primera = next((l.strip() for l in texto.splitlines() if l.strip()), "")
            filas.append([str(rel), ruta.suffix.lower(), ruta.stat().st_size, clasificar(texto, ruta.name), primera[:120], len(texto), n_img])
        except Exception as e:  # noqa: BLE001 — seguimos con el resto
            errores += 1
            filas.append([str(rel), ruta.suffix.lower(), ruta.stat().st_size, "ERROR", str(e)[:120], 0, 0])
        if i % 100 == 0:
            print(f"  {i}/{len(archivos)}…")

    with open(args.salida / "inventario.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["archivo", "extension", "bytes", "tipo_sugerido", "primera_linea", "caracteres", "imagenes"])
        w.writerows(filas)

    conteo = {}
    for fila in filas:
        conteo[fila[3]] = conteo.get(fila[3], 0) + 1
    print(f"\n{len(archivos)} archivos procesados ({errores} con error). Salida: {args.salida}")
    for tipo, n in sorted(conteo.items(), key=lambda x: -x[1]):
        print(f"  {tipo:28s} {n}")


if __name__ == "__main__":
    main()
