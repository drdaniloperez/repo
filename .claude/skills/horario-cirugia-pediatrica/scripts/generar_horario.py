"""Horario mensual de Cirugía Pediátrica — Hospital Jesús Farías (PDVSA) → HTML + PNG + PDF.

Uso:
  python3 generar_horario.py AÑO MES [MESES] [--out DIR]
  p. ej.  python3 generar_horario.py 2026 12          (diciembre 2026)
          python3 generar_horario.py 2027 1 6 --out /tmp/x   (enero a junio 2027)

Las reglas viven en config.json (junto a este script): rotación de guardia, ancla,
día de consulta fijo de cada especialista y colores. La guardia es continua entre meses
porque se calcula desde la fecha ancla (cada 4 días el mismo especialista).
"""
import argparse, base64, calendar, datetime as dt, json, subprocess
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CFG = json.loads((AQUI / "config.json").read_text(encoding="utf-8"))
LOGO = (AQUI / CFG["logo"]).resolve()

ROTACION = CFG["rotacion_guardia"]
ANCLA = dt.date.fromisoformat(CFG["ancla"]["fecha"])
IDX_ANCLA = ROTACION.index(CFG["ancla"]["guardia"])
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
CONSULTA = {DIAS.index(d): n for n, d in CFG["consulta_fija"].items()}  # weekday -> nombre
QX = DIAS.index(CFG["dia_quirofano"])
COLOR = CFG["colores"]
MESES = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto",
         "Septiembre", "Octubre", "Noviembre", "Diciembre"]


def guardia(d):
    return ROTACION[(IDX_ANCLA + (d - ANCLA).days) % len(ROTACION)]


def chip(tipo, nombre):
    bg, fg = COLOR[nombre]
    return (f'<div class="chip" style="background:{bg};color:{fg}">'
            f'<span class="tag">{tipo}</span><b>{nombre}</b></div>')


def html_mes(año, mes):
    semanas = calendar.Calendar(0).monthdatescalendar(año, mes)
    celdas, stats = [], {n: {"g": 0, "fs": 0, "c": 0} for n in ROTACION}
    for semana in semanas:
        for d in semana:
            if d.month != mes:
                celdas.append('<div class="cell out"></div>')
                continue
            wd, g = d.weekday(), guardia(d)
            stats[g]["g"] += 1
            cls, cuerpo = "cell", chip("Guardia", g)
            if wd >= 5:
                cls += " fs"
                stats[g]["fs"] += 1
            elif wd == QX:
                cls += " qx"
                cuerpo += '<div class="qxbar">QUIRÓFANO ELECTIVO</div>'
            elif wd in CONSULTA:
                c = CONSULTA[wd]
                stats[c]["c"] += 1
                cuerpo += chip("Consulta", c)
            celdas.append(f'<div class="{cls}"><div class="num">{d.day}</div>{cuerpo}</div>')

    martes = ", ".join(str(d.day) for s in semanas for d in s if d.month == mes and d.weekday() == QX)
    resumen = "".join(
        f'<tr><td><span class="dot" style="background:{COLOR[n][1]}"></span>Dr(a). {n}</td>'
        f'<td>{CFG["consulta_fija"][n]}</td><td>{s["g"]}</td><td>{s["fs"]}</td><td>{s["c"]}</td></tr>'
        for n, s in stats.items())
    cabecera = "".join(f'<div class="hd{" we" if i >= 5 else ""}">{d}</div>' for i, d in enumerate(DIAS))
    logo64 = base64.b64encode(LOGO.read_bytes()).decode()

    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<title>Cirugía Pediátrica {MESES[mes]} {año}</title><style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Inter,sans-serif;background:#fff;color:#1d2433;width:1600px;padding:40px 48px}}
header{{display:flex;align-items:center;gap:32px;padding-bottom:22px;border-bottom:4px solid #D7322B}}
header img{{height:72px}}
.tit{{flex:1}}
.tit h1{{font-size:30px;font-weight:800;letter-spacing:-.3px}}
.tit h2{{font-size:18px;font-weight:500;color:#5a6478;margin-top:4px}}
.mes{{text-align:right}}
.mes .m{{font-size:40px;font-weight:800;color:#D7322B;line-height:1;text-transform:uppercase}}
.mes .y{{font-size:20px;font-weight:600;color:#5a6478}}
.reglas{{display:flex;gap:12px;margin:20px 0 18px;flex-wrap:wrap}}
.reglas div{{background:#f3f5f9;border-radius:999px;padding:8px 16px;font-size:15px;font-weight:500;color:#39445a}}
.grid{{display:grid;grid-template-columns:repeat(7,1fr);gap:6px}}
.hd{{background:#1d2a44;color:#fff;font-weight:700;font-size:16px;text-align:center;padding:11px 0;border-radius:8px}}
.hd.we{{background:#5a6478}}
.cell{{min-height:132px;border:1px solid #e2e6ee;border-radius:10px;padding:9px 10px;display:flex;flex-direction:column;gap:6px;background:#fff}}
.cell.out{{background:#f7f8fa;border-style:dashed}}
.cell.fs{{background:#f5f6f9}}
.cell.qx{{background:#fff7f6;border-color:#f3c9c6}}
.num{{font-size:20px;font-weight:800;color:#1d2433}}
.chip{{border-radius:7px;padding:6px 9px;font-size:16px;display:flex;justify-content:space-between;align-items:center}}
.chip .tag{{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.6px;opacity:.8}}
.qxbar{{background:#D7322B;color:#fff;font-weight:700;font-size:13px;letter-spacing:.5px;text-align:center;border-radius:7px;padding:7px 4px}}
.pie{{display:flex;gap:28px;margin-top:24px;align-items:flex-start}}
table{{border-collapse:collapse;font-size:16px;flex:1.4}}
th{{text-align:left;font-size:12px;text-transform:uppercase;letter-spacing:.6px;color:#5a6478;padding:8px 12px;border-bottom:2px solid #1d2a44}}
td{{padding:9px 12px;border-bottom:1px solid #e2e6ee;font-weight:500}}
td:nth-child(n+3),th:nth-child(n+3){{text-align:center}}
.dot{{display:inline-block;width:12px;height:12px;border-radius:50%;margin-right:10px;vertical-align:-1px}}
.nota{{flex:1;background:#f3f5f9;border-radius:12px;padding:16px 20px;font-size:14.5px;line-height:1.6;color:#39445a}}
.nota b{{color:#1d2433}}
footer{{margin-top:18px;font-size:12.5px;color:#8a93a6;text-align:right}}
</style></head><body>
<header><img src="data:image/png;base64,{logo64}" alt="PDVSA">
<div class="tit"><h1>Hospital Jesús Farías · Cirugía Pediátrica</h1>
<h2>Programación de guardias, quirófanos y consultas</h2></div>
<div class="mes"><div class="m">{MESES[mes]}</div><div class="y">{año}</div></div></header>
<div class="reglas"><div>Guardias rotativas cada {len(ROTACION)} días</div><div>1 consulta fija por semana</div>
<div>{CFG["dia_quirofano"]}: quirófano electivo · sin consulta</div><div>Sábado y domingo: solo guardia</div></div>
<div class="grid">{cabecera}{''.join(celdas)}</div>
<div class="pie"><table><tr><th>Especialista</th><th>Consulta fija</th><th>Guardias</th><th>Fin de semana</th><th>Consultas</th></tr>{resumen}</table>
<div class="nota"><b>Orden de guardia:</b> {' → '.join(ROTACION)} → (se repite).<br>
<b>Quirófano electivo:</b> todos los {CFG["dia_quirofano"].lower()} ({martes}).<br>
<b>Cambios de guardia:</b> notificar al servicio con antelación.</div></div>
<footer>Servicio de Cirugía Pediátrica · Hospital Jesús Farías (PDVSA)</footer>
</body></html>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("año", type=int)
    ap.add_argument("mes", type=int)
    ap.add_argument("meses", type=int, nargs="?", default=1, help="cuántos meses seguidos")
    ap.add_argument("--out", default=".", help="carpeta de salida (no usar el repo: es público)")
    ap.add_argument("--solo-html", action="store_true")
    a = ap.parse_args()
    out = Path(a.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    año, mes = a.año, a.mes
    for _ in range(a.meses):
        f = out / f"horario-cirugia-pediatrica-{año}-{mes:02d}-{MESES[mes].lower()}.html"
        f.write_text(html_mes(año, mes), encoding="utf-8")
        if not a.solo_html:
            subprocess.run(["node", str(AQUI / "render.js"), str(f)], check=True)
        print(f.with_suffix(".png") if not a.solo_html else f)
        mes += 1
        if mes == 13:
            año, mes = año + 1, 1


if __name__ == "__main__":
    main()
