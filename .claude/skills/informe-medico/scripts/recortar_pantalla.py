#!/usr/bin/env python3
"""Recorta fotos (tomadas con el teléfono) de la pantalla del ecosonógrafo a la medida exacta de la pantalla.

Subcomandos
  recortar  Detecta la pantalla en cada foto, corrige la perspectiva y guarda el recorte.
            python3 recortar_pantalla.py recortar FOTOS_O_CARPETA... --salida DIR [--aspecto 4:3] [--margen 4]
            python3 recortar_pantalla.py recortar foto.jpg --salida DIR --esquinas "x1,y1;x2,y2;x3,y3;x4,y4"
  ampliar   Amplía una región (p. ej. el recuadro de medidas) para leerla mejor.
            python3 recortar_pantalla.py ampliar recorte.jpg --region x,y,ancho,alto [--factor 3] --salida zoom.png
            (x, y, ancho, alto pueden ser píxeles o fracciones 0–1 de la imagen)

Salida de `recortar` en DIR:
  NN_<nombre>.jpg              recorte final, numerado por hora de captura (EXIF) o nombre
  previa/NN_<nombre>.jpg       foto original con el contorno detectado y una cuadrícula de coordenadas
  recortes.json                esquinas, confianza, fecha EXIF y método de cada foto

Requiere: pip install opencv-python-headless numpy pillow
"""
import argparse
import json
import sys
from pathlib import Path

try:
    import cv2
    import numpy as np
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Faltan librerías: pip install opencv-python-headless numpy pillow")

EXT = {".jpg", ".jpeg", ".png", ".heic", ".webp", ".bmp", ".tif", ".tiff"}
ASPECTOS_TIPICOS = [4 / 3, 16 / 10, 16 / 9, 5 / 4]


# ---------- utilidades ----------
def cargar(ruta: Path):
    """Abre la foto respetando la orientación EXIF; devuelve (BGR, fecha_exif)."""
    if ruta.suffix.lower() == ".heic":
        try:
            import pillow_heif  # type: ignore
            pillow_heif.register_heif_opener()
        except ImportError:
            sys.exit("Para .heic: pip install pillow-heif (o exporta las fotos como JPG)")
    img = Image.open(ruta)
    exif = img.getexif()
    fecha = exif.get(36867) or exif.get(306)  # DateTimeOriginal / DateTime
    try:
        fecha = fecha or img._getexif().get(36867)  # type: ignore[attr-defined]
    except Exception:  # noqa: BLE001
        pass
    img = ImageOps.exif_transpose(img).convert("RGB")
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR), fecha


def ordenar_esquinas(pts):
    pts = np.array(pts, dtype="float32").reshape(4, 2)
    s, d = pts.sum(1), np.diff(pts, axis=1).ravel()
    return np.array([pts[np.argmin(s)], pts[np.argmin(d)], pts[np.argmax(s)], pts[np.argmax(d)]], dtype="float32")  # si, sd, id, ii


def lados_en_borde(q, forma, tol=None):
    """Índices de los lados del cuadrilátero que coinciden con el borde de la foto (pantalla que se sale de la foto)."""
    h, w = forma[:2]
    tol = tol or max(h, w) * 0.006
    lados = []
    for i in range(4):
        a, b = q[i], q[(i + 1) % 4]
        for eje, lim in ((0, 0), (0, w - 1), (1, 0), (1, h - 1)):
            if abs(a[eje] - lim) <= tol and abs(b[eje] - lim) <= tol:
                lados.append(i)
                break
    return lados


def puntuar(quad, area_img, forma=None):
    """Puntuación 0–1 de qué tan probable es que el cuadrilátero sea la pantalla."""
    q = ordenar_esquinas(quad)
    area = cv2.contourArea(q)
    frac = area / area_img
    if frac < 0.08 or frac > 0.995 or not cv2.isContourConvex(q.astype(np.int32)):
        return 0.0
    ancho = (np.linalg.norm(q[1] - q[0]) + np.linalg.norm(q[2] - q[3])) / 2
    alto = (np.linalg.norm(q[3] - q[0]) + np.linalg.norm(q[2] - q[1])) / 2
    if alto < 1:
        return 0.0
    asp = ancho / alto
    asp = max(asp, 1 / asp)
    p_asp = max(0.0, 1 - min(abs(asp - a) for a in ASPECTOS_TIPICOS) / 0.5)
    en_borde = lados_en_borde(q, forma) if forma is not None else []
    if len(en_borde) >= 3:
        return 0.0  # es casi la foto entera
    if en_borde:  # la pantalla se sale de la foto: la proporción visible no es la real
        p_asp = 0.8
    # ángulos cercanos a 90°
    angs = []
    for i in range(4):
        a, b, c = q[i - 1], q[i], q[(i + 1) % 4]
        v1, v2 = a - b, c - b
        cos = abs(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + 1e-9))
        angs.append(cos)
    p_ang = max(0.0, 1 - max(angs) / 0.35)
    p_area = min(1.0, frac / 0.35)
    return 0.45 * p_area + 0.3 * p_asp + 0.25 * p_ang


def reducir(img):
    h, w = img.shape[:2]
    escala = min(1.0, 1000 / max(h, w))
    peq = cv2.resize(img, None, fx=escala, fy=escala, interpolation=cv2.INTER_AREA) if escala < 1 else img.copy()
    return cv2.GaussianBlur(cv2.cvtColor(peq, cv2.COLOR_BGR2GRAY), (5, 5), 0), escala


def candidatos(img):
    """Genera cuadriláteros candidatos con varios métodos (bordes y brillo de la pantalla)."""
    gris, escala = reducir(img)
    mascaras = []
    # 1) bordes (cierre morfológico para unir huecos sin engrosar mucho el borde)
    for lo, hi in ((30, 90), (50, 150), (10, 50)):
        e = cv2.Canny(gris, lo, hi)
        e = cv2.morphologyEx(e, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))
        e = cv2.dilate(e, np.ones((3, 3), np.uint8))
        mascaras.append(("bordes", e))
        e2 = e.copy()  # cerrar contornos con el borde de la foto (pantalla que se sale por los lados)
        e2[[0, -1], :] = 255
        e2[:, [0, -1]] = 255
        mascaras.append(("bordes-foto", e2))
    # 2) brillo: la pantalla encendida (incluso su negro) es más clara que el marco
    for t in (None, 25, 40, 60, 90):
        if t is None:
            _, m = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        else:
            _, m = cv2.threshold(gris, t, 255, cv2.THRESH_BINARY)
        m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8))
        mascaras.append(("brillo", m))
    # 3) pantalla oscura: fondo negro de la pantalla más oscuro que el marco/plástico y la pared
    for t in (None, 30, 45, 60, 80):
        if t is None:
            _, m = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        else:
            _, m = cv2.threshold(gris, t, 255, cv2.THRESH_BINARY_INV)
        m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((9, 9), np.uint8))
        conts, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        lleno = np.zeros_like(m)
        cv2.drawContours(lleno, conts, -1, 255, -1)  # rellena el contenido claro (imagen, textos)
        lleno = cv2.morphologyEx(lleno, cv2.MORPH_CLOSE, np.ones((31, 31), np.uint8))
        mascaras.append(("oscuro", lleno))
    salida = candidatos_lineas(gris, escala)
    for metodo, m in mascaras:
        conts, _ = cv2.findContours(m, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        for c in sorted(conts, key=cv2.contourArea, reverse=True)[:8]:
            peri = cv2.arcLength(c, True)
            for eps in (0.01, 0.02, 0.03, 0.05):
                ap = cv2.approxPolyDP(c, eps * peri, True)
                if len(ap) == 4:
                    salida.append((metodo, ap.reshape(4, 2) / escala))
                    break
            else:
                caja = cv2.boxPoints(cv2.minAreaRect(c))
                rect = cv2.contourArea(c) / max(cv2.contourArea(caja), 1)
                if rect > 0.85:
                    salida.append((metodo + "-rect", caja / escala))
    return salida


def _recta(x1, y1, x2, y2):
    p = np.array([x1, y1], float)
    d = np.array([x2 - x1, y2 - y1], float)
    return p, d / (np.linalg.norm(d) + 1e-9)


def _cruce(r1, r2):
    (p1, d1), (p2, d2) = r1, r2
    A = np.array([d1, -d2]).T
    if abs(np.linalg.det(A)) < 1e-6:
        return None
    t = np.linalg.solve(A, p2 - p1)
    return p1 + d1 * t[0]


def candidatos_lineas(gris, escala):
    """Cuadriláteros formados por líneas rectas largas (bordes de la pantalla) y los bordes de la foto."""
    h, w = gris.shape
    e = cv2.Canny(gris, 25, 75)
    segs = cv2.HoughLinesP(e, 1, np.pi / 360, threshold=60, minLineLength=int(0.25 * min(w, h)), maxLineGap=int(0.015 * w))
    hor, ver = [], []
    for x1, y1, x2, y2 in (segs.reshape(-1, 4) if segs is not None else []):
        ang = np.degrees(np.arctan2(y2 - y1, x2 - x1)) % 180
        r = _recta(x1, y1, x2, y2)
        if ang < 12 or ang > 168:
            y_c = y1 + (y2 - y1) * ((w / 2 - x1) / (x2 - x1 + 1e-9))
            hor.append((y_c, r, abs(x2 - x1)))
        elif 78 < ang < 102:
            x_c = x1 + (x2 - x1) * ((h / 2 - y1) / (y2 - y1 + 1e-9))
            ver.append((x_c, r, abs(y2 - y1)))

    def agrupar(lineas, tol):
        lineas.sort(key=lambda t: -t[2])
        out = []
        for c, r, L in lineas:
            if all(abs(c - c2) > tol for c2, _, _ in out):
                out.append((c, r, L))
        return sorted(out, key=lambda t: t[0])[:12]

    hor, ver = agrupar(hor, 0.012 * h), agrupar(ver, 0.012 * w)
    bordes_h = [(0, _recta(0, 0, w - 1, 0), w), (h - 1, _recta(0, h - 1, w - 1, h - 1), w)]
    bordes_v = [(0, _recta(0, 0, 0, h - 1), h), (w - 1, _recta(w - 1, 0, w - 1, h - 1), h)]
    tops = [l for l in hor if l[0] < 0.6 * h] + bordes_h[:1]
    bots = [l for l in hor if l[0] > 0.4 * h] + bordes_h[1:]
    izqs = [l for l in ver if l[0] < 0.45 * w] + bordes_v[:1]
    ders = [l for l in ver if l[0] > 0.55 * w] + bordes_v[1:]
    salida = []
    for t in tops:
        for b in bots:
            if b[0] - t[0] < 0.3 * h:
                continue
            for iz in izqs:
                for de in ders:
                    pts = [_cruce(t[1], iz[1]), _cruce(t[1], de[1]), _cruce(b[1], de[1]), _cruce(b[1], iz[1])]
                    if any(p is None for p in pts):
                        continue
                    q = np.array(pts)
                    q[:, 0] = q[:, 0].clip(0, w - 1)
                    q[:, 1] = q[:, 1].clip(0, h - 1)
                    salida.append(("lineas", q / escala))
    return salida


def exterior_uniforme(gris, bordes, q, escala):
    """0–1: qué tan uniforme (marco/plástico) es la franja justo por fuera de cada lado no pegado al borde de la foto."""
    h, w = gris.shape
    qs = q * escala
    en_borde = lados_en_borde(qs, gris.shape, tol=3)
    c = qs.mean(0)
    franja = max(4, int(0.008 * max(h, w)))
    notas = []
    for i in range(4):
        if i in en_borde:
            notas.append(0.7)
            continue
        a, b = qs[i], qs[(i + 1) % 4]
        d = (b - a) / (np.linalg.norm(b - a) + 1e-9)
        n = np.array([-d[1], d[0]])
        if np.dot(n, (a + b) / 2 - c) < 0:
            n = -n
        m = np.zeros((h, w), np.uint8)
        poly = np.array([a + n * 2, b + n * 2, b + n * (2 + franja), a + n * (2 + franja)], np.int32)
        cv2.fillPoly(m, [poly], 255)
        sel = m > 0
        if sel.sum() < 30:
            notas.append(0.85)
            continue
        dens = float((bordes[sel] > 0).mean())
        std = float(gris[sel].std())
        notas.append(1.0 if dens < 0.015 and std < 18 else 0.6 if dens < 0.04 and std < 28 else 0.0)
    return float(np.mean(notas)), notas


def franja_uniforme(gris, bordes, ext, inn, escala):
    """True si la franja entre el cuadrilátero exterior y el interior no tiene contenido (es marco, no pantalla)."""
    m_ext = np.zeros(gris.shape, np.uint8)
    m_inn = np.zeros(gris.shape, np.uint8)
    cv2.fillPoly(m_ext, [(ext * escala).astype(np.int32)], 255)
    cv2.fillPoly(m_inn, [(inn * escala).astype(np.int32)], 255)
    k = np.ones((5, 5), np.uint8)
    franja = (cv2.erode(m_ext, k) & ~cv2.dilate(m_inn, k)) > 0
    if franja.sum() < 150:
        return False
    # se evalúa por sectores angulares: basta un texto o trozo de imagen en un sector para que NO sea marco
    ys, xs = np.nonzero(franja)
    cx, cy = (inn * escala).mean(0)
    sector = ((np.arctan2(ys - cy, xs - cx) + np.pi) / (2 * np.pi) * 24).astype(int) % 24
    vals, bord = gris[ys, xs].astype(np.float32), bordes[ys, xs] > 0
    for s in range(24):
        sel = sector == s
        if sel.sum() < 20:
            continue
        if bord[sel].mean() > 0.02 or vals[sel].std() > 14:
            return False
    return True


def contenido(ext, inn):
    return all(cv2.pointPolygonTest(ext.astype(np.float32), (float(x), float(y)), False) >= 0 for x, y in inn)


def refinar(img, q):
    """Ajusta cada lado al borde de máximo gradiente cercano (resolución completa) e interseca las rectas."""
    gris = cv2.GaussianBlur(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), (3, 3), 0).astype(np.float32)
    gx, gy = cv2.Sobel(gris, cv2.CV_32F, 1, 0, ksize=3), cv2.Sobel(gris, cv2.CV_32F, 0, 1, ksize=3)
    h, w = gris.shape
    r = int(max(h, w) * 0.012)
    en_borde = lados_en_borde(q, gris.shape)
    rectas = []
    for i in range(4):
        a, b = q[i], q[(i + 1) % 4]
        d = (b - a) / (np.linalg.norm(b - a) + 1e-9)
        if i in en_borde:  # lado = borde de la foto: se deja tal cual
            rectas.append((a.astype(np.float64), d))
            continue
        n = np.array([-d[1], d[0]])
        pts = []
        for t in np.linspace(0.1, 0.9, 60):
            p = a + (b - a) * t
            mejor, mejor_v = None, 0.0
            for s in range(-r, r + 1):
                x, y = (p + n * s).round().astype(int)
                if 0 <= x < w and 0 <= y < h:
                    v = abs(gx[y, x] * n[0] + gy[y, x] * n[1])
                    if v > mejor_v:
                        mejor, mejor_v = p + n * s, v
            if mejor is not None and mejor_v > 20:
                pts.append(mejor)
        if len(pts) < 15:
            return q
        vx, vy, x0, y0 = cv2.fitLine(np.array(pts, np.float32), cv2.DIST_HUBER, 0, 0.01, 0.01).ravel()
        rectas.append((np.array([x0, y0]), np.array([vx, vy])))
    esquinas = []
    for i in range(4):
        (p1, d1), (p2, d2) = rectas[i - 1], rectas[i]
        A = np.array([d1, -d2]).T
        if abs(np.linalg.det(A)) < 1e-6:
            return q
        t = np.linalg.solve(A, p2 - p1)
        esquinas.append(p1 + d1 * t[0])
    nueva = ordenar_esquinas(esquinas)
    # si el ajuste se fue lejos, conserva el original
    return nueva if np.abs(nueva - q).max() < 2 * r else q


def detectar(img, preferir="exterior"):
    """Devuelve (confianza, esquinas, método). Recorre los contornos anidados de fuera hacia dentro:
    si la franja entre dos es uniforme, el exterior es el marco del monitor y se pasa al interior;
    si la franja tiene contenido (texto, imagen), el interior es un recuadro de la interfaz y se para."""
    area = img.shape[0] * img.shape[1]
    vistos, buenos = [], []
    for metodo, q in candidatos(img):
        q = ordenar_esquinas(q)
        p = puntuar(q, area, img.shape)
        if p < 0.7 or any(np.abs(q - v).max() < 0.004 * max(img.shape[:2]) for v in vistos):
            continue
        vistos.append(q)
        buenos.append((p, q, metodo, cv2.contourArea(q)))
    if not buenos:
        return 0.0, None, None
    buenos.sort(key=lambda t: -t[3])
    actual = buenos[0]
    if preferir == "exterior":
        gris, escala = reducir(img)
        bordes = cv2.Canny(gris, 20, 60)
        mejor = max(buenos, key=lambda b: (0.6 * exterior_uniforme(gris, bordes, b[1], escala)[0]
                                           + 0.25 * min(1, b[3] / area / 0.5) + 0.15 * b[0]))
        p, q, metodo, _ = mejor
        return p, refinar(img, q), metodo
    if preferir == "pantalla":
        gris, escala = reducir(img)
        bordes = cv2.Canny(gris, 20, 60)

        def interior_tras_marco(grupo):
            """El mayor candidato que está dentro de otro con una franja uniforme (marco) entre ambos."""
            for inn in grupo:  # de mayor a menor
                for ext in buenos:
                    if ext is not inn and 0.4 < inn[3] / ext[3] < 0.985 and contenido(ext[1], inn[1]) \
                            and franja_uniforme(gris, bordes, ext[1], inn[1], escala):
                        return inn
            return None

        siguiente = interior_tras_marco(buenos)
        while siguiente is not None:  # puede haber marco doble
            actual = siguiente
            siguiente = interior_tras_marco([b for b in buenos if b[3] < actual[3] and contenido(actual[1], b[1])])
            if siguiente is not None and not franja_uniforme(gris, bordes, actual[1], siguiente[1], escala):
                break
    p, q, metodo, _ = actual
    return p, refinar(img, q), metodo


def enderezar(img, q, aspecto=None, margen=0):
    si, sd, id_, ii = q
    ancho = int(max(np.linalg.norm(sd - si), np.linalg.norm(id_ - ii)))
    alto = int(max(np.linalg.norm(ii - si), np.linalg.norm(id_ - sd)))
    if aspecto:
        alto = int(round(ancho / aspecto))
    dst = np.array([[0, 0], [ancho - 1, 0], [ancho - 1, alto - 1], [0, alto - 1]], dtype="float32")
    M = cv2.getPerspectiveTransform(q, dst)
    out = cv2.warpPerspective(img, M, (ancho, alto), flags=cv2.INTER_CUBIC)
    if margen:
        out = out[margen:alto - margen, margen:ancho - margen]
    return out


def previa(img, q, ruta):
    v = img.copy()
    h, w = v.shape[:2]
    paso = max(50, (max(h, w) // 20) // 50 * 50)
    grosor = max(1, max(h, w) // 1500)
    for x in range(0, w, paso):
        cv2.line(v, (x, 0), (x, h), (200, 200, 0), grosor)
        cv2.putText(v, str(x), (x + 3, 30 * grosor), cv2.FONT_HERSHEY_SIMPLEX, 0.8 * grosor, (0, 255, 255), 2 * grosor)
    for y in range(0, h, paso):
        cv2.line(v, (0, y), (w, y), (200, 200, 0), grosor)
        cv2.putText(v, str(y), (3, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8 * grosor, (0, 255, 255), 2 * grosor)
    if q is not None:
        cv2.polylines(v, [q.astype(np.int32)], True, (0, 0, 255), 4 * grosor)
    cv2.imwrite(str(ruta), v, [cv2.IMWRITE_JPEG_QUALITY, 80])


# ---------- subcomandos ----------
def cmd_recortar(a):
    fotos = []
    for e in a.entradas:
        p = Path(e)
        fotos += sorted(x for x in p.iterdir() if x.suffix.lower() in EXT) if p.is_dir() else [p]
    if not fotos:
        sys.exit("No hay fotos")
    if a.esquinas and len(fotos) != 1:
        sys.exit("--esquinas se usa con una sola foto")
    aspecto = None
    if a.aspecto:
        n, d = a.aspecto.split(":")
        aspecto = float(n) / float(d)
    sal = Path(a.salida)
    (sal / "previa").mkdir(parents=True, exist_ok=True)
    reg_path = sal / "recortes.json"
    registro = json.loads(reg_path.read_text()) if reg_path.exists() else {}

    cargadas = [(f, *cargar(f)) for f in fotos]
    cargadas.sort(key=lambda t: (t[2] or "9999", t[0].name))  # orden de captura
    for i, (f, img, fecha) in enumerate(cargadas, 1):
        if a.esquinas:  # corrige una foto ya procesada conservando su número
            q = ordenar_esquinas([[float(v) for v in par.split(",")] for par in a.esquinas.split(";")])
            conf, metodo = 1.0, "manual"
            nombre = registro.get(f.name, {}).get("recorte") or f"{len(registro) + 1:02d}_{f.stem}.jpg"
        else:
            conf, q, metodo = detectar(img)
            nombre = f"{i:02d}_{f.stem}.jpg"
        previa(img, q, sal / "previa" / nombre)
        if q is None:
            print(f"✗ {f.name}: no se detectó la pantalla → revisa previa/{nombre} y usa --esquinas")
            registro[f.name] = {"recorte": None, "confianza": 0, "fecha_exif": fecha}
            continue
        out = enderezar(img, q, aspecto, a.margen)
        cv2.imwrite(str(sal / nombre), out, [cv2.IMWRITE_JPEG_QUALITY, 95])
        aviso = "" if conf >= 0.75 else "  ⚠ confianza baja: verifica"
        print(f"✓ {f.name} → {nombre}  ({out.shape[1]}×{out.shape[0]}, conf {conf:.2f}, {metodo}){aviso}")
        registro[f.name] = {"recorte": nombre, "confianza": round(float(conf), 3), "metodo": metodo,
                            "esquinas": q.round(1).tolist(), "fecha_exif": fecha, "tamano": [out.shape[1], out.shape[0]]}
    reg_path.write_text(json.dumps(registro, indent=2, ensure_ascii=False))


def cmd_ampliar(a):
    img, _ = cargar(Path(a.imagen))
    h, w = img.shape[:2]
    x, y, rw, rh = (float(v) for v in a.region.split(","))
    if max(x, y, rw, rh) <= 1:
        x, y, rw, rh = x * w, y * h, rw * w, rh * h
    reg = img[int(y):int(y + rh), int(x):int(x + rw)]
    reg = cv2.resize(reg, None, fx=a.factor, fy=a.factor, interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(a.salida, reg)
    print(f"Guardado {a.salida} ({reg.shape[1]}×{reg.shape[0]})")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("recortar")
    r.add_argument("entradas", nargs="+")
    r.add_argument("--salida", required=True)
    r.add_argument("--aspecto", help="Fuerza la proporción de la pantalla, p. ej. 4:3 o 16:9")
    r.add_argument("--margen", type=int, default=0, help="Píxeles a recortar hacia dentro tras enderezar (restos de marco)")
    r.add_argument("--esquinas", help='Esquinas manuales "x1,y1;x2,y2;x3,y3;x4,y4" en píxeles de la foto (orientada)')
    r.set_defaults(func=cmd_recortar)
    z = sub.add_parser("ampliar")
    z.add_argument("imagen")
    z.add_argument("--region", required=True)
    z.add_argument("--factor", type=float, default=3)
    z.add_argument("--salida", required=True)
    z.set_defaults(func=cmd_ampliar)
    a = ap.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
