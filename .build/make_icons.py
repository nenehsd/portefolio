# -*- coding: utf-8 -*-
"""Genere des icones d'outils (badges arrondis aux couleurs des marques)."""
import os
from PIL import Image, ImageDraw

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img", "tools")
os.makedirs(OUT, exist_ok=True)
S = 256
R = 56


def base(bg):
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, S - 1, S - 1], R, fill=bg)
    return im, d


def save(im, name):
    im.resize((512, 512), Image.LANCZOS).save(os.path.join(OUT, name))


# ---- Trello : fond bleu + 2 colonnes blanches
im, d = base("#0C66E4")
d.rounded_rectangle([46, 46, 116, 186], 12, fill="white")
d.rounded_rectangle([140, 46, 210, 130], 12, fill="white")
save(im, "trello.png")

# ---- Canva : cercle degrade-ish + C blanc
im, d = base("#00C4CC")
d.ellipse([28, 28, S - 28, S - 28], fill="#7D2AE8")
d.ellipse([54, 54, S - 54, S - 54], fill="#00C4CC")
d.arc([76, 72, 186, 184], start=40, end=320, fill="white", width=22)
save(im, "canva.png")

# ---- CapCut : fond noir + obturateur blanc/cyan
im, d = base("#111111")
d.ellipse([50, 50, 206, 206], outline="white", width=20)
d.ellipse([98, 98, 158, 158], fill="#00E5D0")
save(im, "capcut.png")

# ---- Site portfolio : fenetre navigateur
im, d = base("#1F5E3A")
d.rounded_rectangle([40, 56, 216, 200], 14, fill="white")
d.rectangle([40, 56, 216, 92], fill="#9FB8A2")
d.rounded_rectangle([40, 56, 216, 80], 14, fill="#9FB8A2")
for i, x in enumerate((60, 82, 104)):
    d.ellipse([x, 66, x + 14, 80], fill="white")
d.rounded_rectangle([60, 108, 196, 126], 6, fill="#1AAB70")
d.rounded_rectangle([60, 140, 160, 154], 5, fill="#DCE8DE")
d.rounded_rectangle([60, 166, 130, 180], 5, fill="#DCE8DE")
save(im, "site.png")

# ---- Meta Business / publicite : megaphone stylise
im, d = base("#1AAB70")
d.polygon([(62, 108), (150, 62), (150, 194), (62, 148)], fill="white")
d.rounded_rectangle([44, 106, 74, 150], 8, fill="white")
d.rounded_rectangle([92, 150, 122, 208], 10, fill="white")
d.arc([150, 86, 214, 170], start=300, end=60, fill="white", width=16)
save(im, "pub.png")

# ---- Charte graphique : palette
im, d = base("#42612D")
cols = ["#1F5E3A", "#1AAB70", "#9FB8A2", "#FFFFFF"]
for i, c in enumerate(cols):
    x = 44 + (i % 2) * 88
    y = 44 + (i // 2) * 88
    d.rounded_rectangle([x, y, x + 68, y + 68], 12, fill=c)
save(im, "charte.png")

print("icones generees dans", OUT)
for f in sorted(os.listdir(OUT)):
    print("  ", f)
