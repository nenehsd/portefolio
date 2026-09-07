# -*- coding: utf-8 -*-
"""Moteur de rendu double: une description de slide -> PPTX (editable) + PDF.
Repere: points, 960 x 540 (16:9), origine en haut a gauche.
"""
import os

W, H = 960.0, 540.0
BASE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(BASE, "fonts")
IMG = os.path.join(BASE, "img")
ROOT = os.path.dirname(BASE)

# --- Charte graphique Sadiya Digital Agri -----------------------------------
VERT_FONCE = "1F5E3A"
TURQUOISE = "1AAB70"
OLIVE = "42612D"
GRISE = "9FB8A2"
TRES_FONCE = "0A1A01"
BLANC = "FFFFFF"
CREME = "F4F7F5"
SAFRAN = "FFB800"
ROSE = "E8134B"          # accent Simplon (logos partenaires)
GRISE_CLAIR = "DCE8DE"

ALFA = "Alfa Slab One"
POP = "Poppins"

FONT_FILES = {
    (POP, False, False): "Poppins-Regular.ttf",
    (POP, True, False): "Poppins-Bold.ttf",
    ("Poppins Medium", False, False): "Poppins-Medium.ttf",
    ("Poppins SemiBold", False, False): "Poppins-SemiBold.ttf",
    (ALFA, False, False): "AlfaSlabOne-Regular.ttf",
    (ALFA, True, False): "AlfaSlabOne-Regular.ttf",
}


def hx(c):
    return tuple(int(c[i:i + 2], 16) / 255.0 for i in (0, 2, 4))


class Slide(object):
    def __init__(self, name=""):
        self.name = name
        self.ops = []

    # ---- primitives ----
    def rect(self, x, y, w, h, fill=None, line=None, lw=1.0, radius=0.0, alpha=1.0):
        self.ops.append(("rect", dict(x=x, y=y, w=w, h=h, fill=fill, line=line,
                                      lw=lw, radius=radius, alpha=alpha)))

    def ellipse(self, x, y, w, h, fill=None, line=None, lw=1.0, alpha=1.0):
        self.ops.append(("ellipse", dict(x=x, y=y, w=w, h=h, fill=fill, line=line,
                                         lw=lw, alpha=alpha)))

    def poly(self, pts, fill=None, line=None, lw=1.0, alpha=1.0):
        self.ops.append(("poly", dict(pts=pts, fill=fill, line=line, lw=lw, alpha=alpha)))

    def line(self, x1, y1, x2, y2, color=VERT_FONCE, lw=1.0, dash=None, alpha=1.0):
        self.ops.append(("line", dict(x1=x1, y1=y1, x2=x2, y2=y2, color=color,
                                      lw=lw, dash=dash, alpha=alpha)))

    def image(self, path, x, y, w, h):
        self.ops.append(("image", dict(path=path, x=x, y=y, w=w, h=h)))

    def text(self, s, x, y, w, size=14, font=POP, bold=False, italic=False,
             color=TRES_FONCE, align="l", h=None, valign="t", leading=1.30,
             spacing=0.0, caps=False):
        """y = haut du bloc. align: l/c/r"""
        self.ops.append(("text", dict(s=s, x=x, y=y, w=w, size=size, font=font,
                                      bold=bold, italic=italic, color=color, align=align,
                                      h=h, valign=valign, leading=leading,
                                      spacing=spacing, caps=caps)))

    def bullets(self, items, x, y, w, size=13, color=TRES_FONCE, gap=9,
                marker="dot", mcolor=TURQUOISE, font=POP, bold=False, leading=1.32):
        self.ops.append(("bullets", dict(items=items, x=x, y=y, w=w, size=size,
                                         color=color, gap=gap, marker=marker,
                                         mcolor=mcolor, font=font, bold=bold,
                                         leading=leading)))
