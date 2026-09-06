# -*- coding: utf-8 -*-
"""Genere des vignettes 'poste a pourvoir' : silhouette humaine + point d'interrogation."""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(BASE, "img")
FONTS = os.path.join(BASE, "fonts")

W, H = 660, 880           # meme ratio 3:4 que les photos
SS = 3                    # supersampling anti-aliasing


def silhouette(path, bg, body, accent):
    w, h = W * SS, H * SS
    im = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(im)

    cx = w // 2
    # --- tete
    r = int(w * 0.148)
    cy = int(h * 0.365)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=body)

    # --- buste (epaules arrondies)
    bw = int(w * 0.46)          # demi-largeur des epaules
    top = cy + int(r * 1.34)    # haut des epaules
    bot = int(h * 0.86)
    rad = int(w * 0.30)
    d.rounded_rectangle([cx - bw, top, cx + bw, bot + rad], rad, fill=body)
    d.rectangle([cx - bw, bot, cx + bw, h], fill=bg)

    # --- pastille point d'interrogation
    pr = int(w * 0.132)
    px, py = cx + int(w * 0.235), cy - int(r * 0.92)
    d.ellipse([px - pr - SS * 4, py - pr - SS * 4,
               px + pr + SS * 4, py + pr + SS * 4], fill=bg)
    d.ellipse([px - pr, py - pr, px + pr, py + pr], fill=accent)

    try:
        f = ImageFont.truetype(os.path.join(FONTS, "Poppins-Bold.ttf"), int(pr * 1.44))
    except Exception:
        f = ImageFont.load_default()
    tb = d.textbbox((0, 0), "?", font=f)
    d.text((px - (tb[2] - tb[0]) / 2 - tb[0],
            py - (tb[3] - tb[1]) / 2 - tb[1]), "?", font=f, fill=bg)

    im.resize((W, H), Image.LANCZOS).save(path, quality=95)
    print("  ", os.path.basename(path))


print("Vignettes 'poste a pourvoir' :")
# creatrice de contenu — fond vert tres clair, silhouette vert fonce
silhouette(os.path.join(IMG, "team_createur.jpg"),
           bg="#E4EEE6", body="#1F5E3A", accent="#1AAB70")
# responsable commercial — fond gris-vert, silhouette olive
silhouette(os.path.join(IMG, "team_commercial.jpg"),
           bg="#EDF2EE", body="#42612D", accent="#1AAB70")
