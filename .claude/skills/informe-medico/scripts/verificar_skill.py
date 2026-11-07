#!/usr/bin/env python3
"""Verifica que la skill informe-medico esté bien entrenada y que el repo (PÚBLICO) no tenga datos de pacientes.

Uso:
  python3 verificar_skill.py                                  # en cualquier sesión (nube o local)
  python3 verificar_skill.py --inventario ~/informes-extraidos/inventario.csv \
                             --textos ~/informes-extraidos/textos   # en la sesión local, tras extraer

Comprueba:
  1. Cobertura: tipos de formatos/COBERTURA.md (y del inventario, si se da) con su archivo de formato.
  2. Calidad: cada formatos/<tipo>.md tiene Estructura, Frases, Conclusión, Preguntar si falta y Ejemplo.
  3. Logos: los archivos de formatos/logos/logos.json existen.
  4. Privacidad: cédulas, teléfonos, correos y (con --textos) los nombres reales de pacientes del disco
     en memoria/ y en la skill. Sale con código 1 si hay alertas de privacidad.
"""
import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
REPO = SKILL.parent.parent.parent
FORMATOS = SKILL / "formatos"
SECCIONES = {
    "Estructura": r"^#+\s*Estructura",
    "Frases": r"^#+\s*(Frases|Plantillas)",
    "Conclusión": r"^#+\s*.*(Conclusi|Cierre)",
    "Preguntar si falta": r"^#+\s*(Preguntar|Qué preguntar|Datos obligatorios)",
    "Ejemplo anonimizado": r"^#+\s*Ejemplo",
}
NO_SON_TIPOS = {"README", "_plantilla", "COBERTURA", "centros", "eco-imagenes"}
PATRONES_PRIVADOS = {
    "cédula": r"(?<![\w.])(?:[VvEe]-?)?\d{1,2}\.\d{3}\.\d{3}(?![\w.])|(?<![\w.#-])\d{7,8}(?![\w.])",
    "teléfono": r"(?<!\d)0(?:2\d{2}|4(?:12|14|16|24|26))[- ]?\d{3}[- ]?\d{4}(?!\d)",
    "correo": r"[\w.+-]+@[\w-]+\.[\w.]+",
}
PERMITIDOS = {"danilo", "pérez", "perez", "danilo pérez", "danilo perez", "paciente de prueba"}


def archivos_a_revisar():
    for base in (REPO / "memoria", SKILL):
        for p in base.rglob("*"):
            if p.is_file() and p.suffix in {".md", ".py", ".json", ".txt", ".csv"} and "__pycache__" not in p.parts:
                yield p
    yield REPO / "CLAUDE.md"
    yield REPO / "README.md"


def nombres_de_pacientes(textos_dir):
    nombres = set()
    for t in Path(textos_dir).rglob("*.txt"):
        for linea in t.read_text(errors="ignore").splitlines()[:15]:
            m = re.match(r"\s*(?:Px|Paciente|Nombre)\s*:\s*(.+)", linea, re.I)
            if m:
                n = re.split(r"\s{2,}|\t|\bC\.?I\b|\bCi\b|\bEdad\b", m.group(1))[0].strip(" .,:")
                if len(n) >= 5 and n.lower() not in PERMITIDOS:
                    nombres.add(n.lower())
    return nombres


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--inventario", help="inventario.csv de extraer_textos.py (sesión local)")
    ap.add_argument("--textos", help="carpeta de textos extraídos, para buscar nombres reales de pacientes")
    a = ap.parse_args()
    alertas, avisos = [], []

    # 1. Cobertura
    formatos = {p.stem: p for p in FORMATOS.glob("*.md") if p.stem not in NO_SON_TIPOS}
    print(f"== Formatos aprendidos ({len(formatos)}): {', '.join(sorted(formatos))}")
    cob = FORMATOS / "COBERTURA.md"
    if cob.exists():
        filas = [l for l in cob.read_text().splitlines() if l.startswith("|") and not set(l) <= set("|- ")][1:]
        for f in filas:
            celdas = [c.strip() for c in f.strip("|").split("|")]
            arch = re.search(r"`([^`]+\.md)`", f)
            if arch and not ((FORMATOS / arch.group(1)).exists() or (SKILL / arch.group(1)).exists()):
                alertas.append(f"COBERTURA cita {arch.group(1)} y no existe")
            if "pocos" in f.lower() or "pendiente" in f.lower():
                avisos.append(f"Cobertura incompleta: {celdas[0]} → {celdas[-1]}")
    else:
        avisos.append("Falta formatos/COBERTURA.md")
    if a.inventario:
        conteo = Counter(r["tipo_sugerido"] for r in csv.DictReader(open(a.inventario, encoding="utf-8")))
        print("== Inventario del disco:")
        for tipo, n in conteo.most_common():
            tiene = tipo in formatos or any(tipo.startswith(f) or f.startswith(tipo) for f in formatos)
            marca = "✓" if tiene else ("·" if tipo in {"ERROR", "sin-clasificar"} else "✗")
            print(f"   {marca} {tipo:32s} {n:5d}")
            if marca == "✗" and n >= 3:
                alertas.append(f"Tipo sin formato: {tipo} ({n} documentos)")

    # 2. Calidad de cada formato
    print("== Secciones por formato:")
    for nombre, p in sorted(formatos.items()):
        txt = p.read_text()
        faltan = [s for s, rx in SECCIONES.items() if not re.search(rx, txt, re.M | re.I)]
        print(f"   {'✓' if not faltan else '⚠'} {nombre}" + (f"  (falta: {', '.join(faltan)})" if faltan else ""))
        if faltan:
            avisos.append(f"{nombre}: falta {', '.join(faltan)}")

    # 3. Logos
    lj = FORMATOS / "logos" / "logos.json"
    if lj.exists():
        for clave, d in json.loads(lj.read_text()).items():
            if not (FORMATOS / "logos" / d["archivo"]).exists():
                alertas.append(f"Logo de {clave} no existe: {d['archivo']}")

    # 4. Privacidad
    nombres = nombres_de_pacientes(a.textos) if a.textos else set()
    if a.textos:
        print(f"== Buscando {len(nombres)} nombres reales de pacientes en el repo…")
    for p in archivos_a_revisar():
        if not p.exists():
            continue
        txt = p.read_text(errors="ignore")
        rel = p.relative_to(REPO)
        if p.suffix == ".json":
            txt = re.sub(r'"[0-9a-f]{32}"', '""', txt)  # huellas md5 de logos
        for tipo, rx in PATRONES_PRIVADOS.items():
            for m in re.finditer(rx, txt):
                ctx = txt[max(0, m.start() - 25):m.end() + 5].replace("\n", " ")
                if re.search(r"12\.345\.678|00\.000\.000|\[CI\]|ejemplo|ficticio", ctx, re.I):
                    continue
                alertas.append(f"PRIVACIDAD ({tipo}) en {rel}: …{ctx}…")
        bajo = txt.lower()
        for n in nombres:
            if n in bajo:
                alertas.append(f"PRIVACIDAD (nombre de paciente) en {rel}: {n}")

    print()
    for x in avisos:
        print("⚠ " + x)
    for x in alertas:
        print("✗ " + x)
    if not avisos and not alertas:
        print("✓ Todo en orden")
    sys.exit(1 if any(x.startswith("PRIVACIDAD") or "sin formato" in x or "no existe" in x for x in alertas) else 0)


if __name__ == "__main__":
    main()
