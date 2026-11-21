#!/usr/bin/env python3
"""Mejora la calidad de los recortes de fotos de la pantalla del ecógrafo (pedido por Danilo, 2026-11-21).

Las fotos del teléfono a la pantalla traen moiré (bandas de colores tipo arcoíris), ruido y poco contraste.
  python3 mejorar_imagenes.py rec/*.jpg --salida rec_hq
1) Quita el moiré de color: en zonas poco saturadas (la imagen ecográfica, que es gris) elimina el color;
   conserva los colores fuertes (rótulos amarillos/verdes, medidas, barras azules del equipo).
2) Reduce ruido sin borrar bordes (fastNlMeans), 3) mejora contraste local (CLAHE suave), 4) enfoque (unsharp).
Guarda PNG (sin pérdida) para que el PDF no vuelva a comprimir sobre JPEG.
"""
import argparse, pathlib
import cv2, numpy as np

def mejorar(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float32)
    s, v = hsv[..., 1], hsv[..., 2]
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # máscara de color "real" (texto/medidas): saturación alta y brillo alto
    h = hsv[..., 0]
    # texto amarillo/verde/rojo: se conserva aunque sea fino
    texto = ((((h >= 15) & (h <= 95)) | (h <= 8) | (h >= 170)) & (s > 90) & (v > 110)).astype(np.uint8) * 255
    # azul: solo bloques grandes (barras y botones del equipo), no los puntitos del moiré
    azul = (((h > 95) & (h < 135)) & (s > 100) & (v > 70)).astype(np.uint8) * 255
    azul = cv2.morphologyEx(azul, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(azul)
    grande = np.zeros_like(azul)
    for i in range(1, n):  # barras/botones: bloques anchos y sólidos
        x, y, w, hh, area = st[i]
        m = lab == i
        if area > 0.0015 * azul.size and area > 0.45 * w * hh and s[m].mean() > 150 and v[m].mean() > 110:
            grande[lab == i] = 255
    azul = grande
    real = cv2.dilate(cv2.bitwise_or(texto, azul), np.ones((5, 5), np.uint8))
    real = cv2.GaussianBlur(real, (5, 5), 0).astype(np.float32)[..., None] / 255
    g3 = cv2.cvtColor(gris, cv2.COLOR_GRAY2BGR).astype(np.float32)
    out = (img.astype(np.float32) * real + g3 * (1 - real)).astype(np.uint8)
    out = cv2.fastNlMeansDenoisingColored(out, None, 5, 5, 7, 21)
    lab = cv2.cvtColor(out, cv2.COLOR_BGR2LAB)
    lab[..., 0] = cv2.createCLAHE(clipLimit=1.6, tileGridSize=(8, 8)).apply(lab[..., 0])
    out = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
    blur = cv2.GaussianBlur(out, (0, 0), 2.0)
    return cv2.addWeighted(out, 1.5, blur, -0.5, 0)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('imagenes', nargs='+'); ap.add_argument('--salida', required=True)
    a = ap.parse_args(); o = pathlib.Path(a.salida); o.mkdir(parents=True, exist_ok=True)
    for f in a.imagenes:
        p = pathlib.Path(f); r = mejorar(cv2.imread(str(p)))
        cv2.imwrite(str(o / (p.stem + '.png')), r); print('OK', o / (p.stem + '.png'))
