# -*- coding: utf-8 -*-
import os
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont as RTTFont
from reportlab.lib.colors import Color

from deck_core import (W, H, FONTS, FONT_FILES, hx, POP, ALFA)
import textutil as TU

_registered = False
_PDFNAME = {}


def _register():
    global _registered
    if _registered:
        return
    for (fam, bold, ital), fn in FONT_FILES.items():
        name = "%s%s" % (fam.replace(" ", ""), "-B" if bold else "")
        if name not in _PDFNAME.values():
            try:
                pdfmetrics.registerFont(RTTFont(name, os.path.join(FONTS, fn)))
            except Exception:
                pass
        _PDFNAME[(fam, bold)] = name
    _registered = True


def pdfname(font, bold):
    _register()
    return _PDFNAME.get((font, bold)) or _PDFNAME.get((font, False)) or _PDFNAME[(POP, bold)]


def C(hexs, alpha=1.0):
    r, g, b = hx(hexs)
    return Color(r, g, b, alpha=alpha)


def Y(y):
    return H - y


def draw_text_block(c, o):
    s = o["s"].upper() if o["caps"] else o["s"]
    font, bold, size = o["font"], o["bold"], o["size"]
    lines = TU.wrap(s, font, bold, size, o["w"], o["spacing"])
    lead = size * o["leading"]
    total = lead * len(lines)
    y0 = o["y"]
    if o["h"] and o["valign"] == "m":
        y0 = o["y"] + (o["h"] - total) / 2.0
    elif o["h"] and o["valign"] == "b":
        y0 = o["y"] + o["h"] - total
    c.setFillColor(C(o["color"]))
    fn = pdfname(font, bold)
    c.setFont(fn, size)
    for i, ln in enumerate(lines):
        lw_ = TU.text_w(ln, font, bold, size, o["spacing"])
        if o["align"] == "c":
            x = o["x"] + (o["w"] - lw_) / 2.0
        elif o["align"] == "r":
            x = o["x"] + o["w"] - lw_
        else:
            x = o["x"]
        by = Y(y0 + lead * i + size * 0.82)
        if o["spacing"]:
            cx = x
            for ch in ln:
                c.drawString(cx, by, ch)
                cx += TU.char_w(ch, font, bold, size, o["spacing"])
        else:
            c.drawString(x, by, ln)
    return total


def render(slides, path):
    _register()
    c = canvas.Canvas(path, pagesize=(W, H))
    for sl in slides:
        for kind, o in sl.ops:
            if kind == "rect":
                if o["fill"]:
                    c.setFillColor(C(o["fill"], o["alpha"]))
                if o["line"]:
                    c.setStrokeColor(C(o["line"], o["alpha"]))
                    c.setLineWidth(o["lw"])
                mode = (1 if o["fill"] else 0, 1 if o["line"] else 0)
                if o["radius"]:
                    c.roundRect(o["x"], Y(o["y"] + o["h"]), o["w"], o["h"], o["radius"],
                                stroke=mode[1], fill=mode[0])
                else:
                    c.rect(o["x"], Y(o["y"] + o["h"]), o["w"], o["h"],
                           stroke=mode[1], fill=mode[0])
            elif kind == "ellipse":
                if o["fill"]:
                    c.setFillColor(C(o["fill"], o["alpha"]))
                if o["line"]:
                    c.setStrokeColor(C(o["line"], o["alpha"]))
                    c.setLineWidth(o["lw"])
                c.ellipse(o["x"], Y(o["y"] + o["h"]), o["x"] + o["w"], Y(o["y"]),
                          stroke=1 if o["line"] else 0, fill=1 if o["fill"] else 0)
            elif kind == "poly":
                p = c.beginPath()
                pts = o["pts"]
                p.moveTo(pts[0][0], Y(pts[0][1]))
                for x, y in pts[1:]:
                    p.lineTo(x, Y(y))
                p.close()
                if o["fill"]:
                    c.setFillColor(C(o["fill"], o["alpha"]))
                if o["line"]:
                    c.setStrokeColor(C(o["line"], o["alpha"]))
                    c.setLineWidth(o["lw"])
                c.drawPath(p, stroke=1 if o["line"] else 0, fill=1 if o["fill"] else 0)
            elif kind == "line":
                c.setStrokeColor(C(o["color"], o["alpha"]))
                c.setLineWidth(o["lw"])
                if o["dash"]:
                    c.setDash(o["dash"], 0)
                c.line(o["x1"], Y(o["y1"]), o["x2"], Y(o["y2"]))
                c.setDash([], 0)
            elif kind == "image":
                c.drawImage(o["path"], o["x"], Y(o["y"] + o["h"]), o["w"], o["h"],
                            mask="auto", preserveAspectRatio=False)
            elif kind == "text":
                draw_text_block(c, o)
            elif kind == "bullets":
                y = o["y"]
                for it in o["items"]:
                    if o["marker"] == "dot":
                        c.setFillColor(C(o["mcolor"]))
                        c.circle(o["x"] + 3.2, Y(y + o["size"] * 0.45), 3.0, stroke=0, fill=1)
                        tx, tw = o["x"] + 13, o["w"] - 13
                    elif o["marker"] == "check":
                        c.setFillColor(C(o["mcolor"]))
                        c.circle(o["x"] + 5, Y(y + o["size"] * 0.45), 5.2, stroke=0, fill=1)
                        c.setStrokeColor(C("FFFFFF"))
                        c.setLineWidth(1.5)
                        yy = Y(y + o["size"] * 0.45)
                        c.line(o["x"] + 2.6, yy + 0.2, o["x"] + 4.4, yy - 2.0)
                        c.line(o["x"] + 4.4, yy - 2.0, o["x"] + 7.6, yy + 2.6)
                        tx, tw = o["x"] + 16, o["w"] - 16
                    else:
                        tx, tw = o["x"], o["w"]
                    used = draw_text_block(c, dict(
                        s=it, x=tx, y=y, w=tw, size=o["size"], font=o["font"],
                        bold=o["bold"], italic=False, color=o["color"], align="l",
                        h=None, valign="t", leading=o["leading"], spacing=0.0, caps=False))
                    y += used + o["gap"]
        c.showPage()
    c.save()
