# -*- coding: utf-8 -*-
"""Mesure et decoupe de texte partagees par les deux moteurs de rendu."""
import os
from fontTools.ttLib import TTFont
from deck_core import FONTS, FONT_FILES, POP

_cache = {}


def _metrics(font, bold):
    key = (font, bold)
    if key in _cache:
        return _cache[key]
    fn = FONT_FILES.get((font, bold, False)) or FONT_FILES.get((font, False, False)) \
        or FONT_FILES[(POP, bold, False)]
    tt = TTFont(os.path.join(FONTS, fn))
    upm = tt["head"].unitsPerEm
    hmtx = tt["hmtx"].metrics
    cmap = tt.getBestCmap()
    widths = {}
    for cp, gname in cmap.items():
        if gname in hmtx:
            widths[cp] = hmtx[gname][0] / float(upm)
    default = widths.get(ord(" "), 0.26)
    _cache[key] = (widths, default)
    return _cache[key]


def char_w(ch, font, bold, size, spacing=0.0):
    widths, default = _metrics(font, bold)
    return widths.get(ord(ch), default) * size + spacing


def text_w(s, font, bold, size, spacing=0.0):
    widths, default = _metrics(font, bold)
    return sum(widths.get(ord(c), default) for c in s) * size + spacing * max(len(s) - 1, 0)


def wrap(s, font, bold, size, maxw, spacing=0.0):
    """Retourne une liste de lignes. Respecte les \n explicites."""
    out = []
    for para in s.split("\n"):
        if not para.strip():
            out.append("")
            continue
        words, cur = para.split(" "), ""
        for wd in words:
            t = wd if not cur else cur + " " + wd
            if text_w(t, font, bold, size, spacing) <= maxw or not cur:
                cur = t
            else:
                out.append(cur)
                cur = wd
        out.append(cur)
    return out
