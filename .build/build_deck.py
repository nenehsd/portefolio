# -*- coding: utf-8 -*-
"""Pitch Deck — Sadiya Digital Agri
Structure: modele "Fabrique Ndeye Khady Dione" / contenu: strategie TOMSTER
Charte graphique Sadiya Digital Agri.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from deck_core import *
import textutil as TU
import render_pdf, render_pptx

IM = lambda n: os.path.join(IMG, n)
LOGO = os.path.join(ROOT, "assets", "img", "logo-sadiya.png")
LOGOW = os.path.join(ROOT, "assets", "img", "logo-sadiya-white.png")
MARK = os.path.join(ROOT, "assets", "img", "mark-512.png")
FOOTLOGOS = IM("logos_footer.png")

SLIDES = []


def new(name):
    s = Slide(name)
    SLIDES.append(s)
    return s


# ---------------------------------------------------------------- decorations
def dots(s, x, y, cols, rows, step=9, r=1.7, color=VERT_FONCE, alpha=1.0, fade=False):
    for i in range(cols):
        for j in range(rows):
            a = alpha
            if fade:
                a = alpha * (0.25 + 0.75 * (1 - i / float(max(cols - 1, 1))))
            s.ellipse(x + i * step, y + j * step, r * 2, r * 2, fill=color, alpha=a)


def sidelabel(s, color=GRISE):
    """Bandeau vertical 'PITCH DECK PRESENTATION' comme dans le modele."""
    s.text("PITCH DECK PRESENTATION", 0, 0, 0, size=0)  # placeholder no-op
    # rendu horizontal discret en bas a gauche (lisible, sans rotation)
    s.text(u"PITCH DECK  ·  PRESENTATION", 40, 505, 260, size=6.5, font=POP,
           bold=True, color=color, spacing=1.6)


def footer(s, dark=False, page=None, logos=True):
    col = BLANC if dark else VERT_FONCE
    sub = GRISE if dark else GRISE
    s.text(u"Programme de Pré-incubation 2026 de la\nfabrique 360 de Simplon Sénégal",
           620, 500, 200, size=6.8, font=POP, color=sub, leading=1.35, align="r")
    if logos:
        s.image(FOOTLOGOS, 838, 496, 88, 17)
    if page is not None:
        s.text(str(page).zfill(2), 40, 498, 30, size=9, font=POP, bold=True, color=col)


def titlebar(s, kicker, title, sub=None, page=None, accent=TURQUOISE):
    """En-tete standard des slides de contenu."""
    s.rect(0, 0, W, H, fill=CREME)
    s.rect(0, 0, 6, H, fill=VERT_FONCE)
    if kicker:
        s.rect(52, 40, 3.5, 13, fill=accent)
        s.text(kicker, 63, 40, 500, size=8.5, font=POP, bold=True, color=accent,
               spacing=1.9, caps=True)
    s.text(title, 52, 58, 640, size=27, font=ALFA, color=VERT_FONCE, leading=1.12)
    if sub:
        s.text(sub, 52, 95, 620, size=11, font=POP, color=OLIVE, leading=1.35)
    s.image(LOGO, 848, 34, 74, 30)
    footer(s, page=page)


def checkmark(s, cx, cy, d=18, fill=TURQUOISE, col=BLANC):
    """Pastille ronde avec une coche dessinee (pas de glyphe)."""
    s.ellipse(cx, cy, d, d, fill=fill)
    r = d / 18.0
    s.line(cx + 4.6 * r, cy + 9.2 * r, cx + 7.6 * r, cy + 12.4 * r, color=col, lw=1.7 * r)
    s.line(cx + 7.6 * r, cy + 12.4 * r, cx + 13.4 * r, cy + 5.8 * r, color=col, lw=1.7 * r)


def card(s, x, y, w, h, fill=BLANC, line=GRISE_CLAIR, radius=9, lw=1.0):
    s.rect(x, y, w, h, fill=fill, line=line, lw=lw, radius=radius)


def chevron(s, x, y, w, h, fill, tip=26):
    s.poly([(x, y), (x + w - tip, y), (x + w, y + h / 2.0), (x + w - tip, y + h), (x, y + h)],
           fill=fill)


def numbadge(s, x, y, n, d=21, fill=VERT_FONCE, tcol=BLANC, size=9):
    s.ellipse(x, y, d, d, fill=fill)
    s.text(n, x, y + d / 2.0 - size * 0.62, d, size=size, font=POP, bold=True,
           color=tcol, align="c")


# =============================================================== 01 COUVERTURE
s = new("Couverture")
s.rect(0, 0, W, H, fill=BLANC)
s.rect(0, 0, W, H * 0.34, fill=CREME)
# carte verte centrale
s.rect(140, 128, 680, 366, fill=VERT_FONCE, radius=18)
# decor
dots(s, 16, 250, 7, 12, step=10, r=1.9, color=TURQUOISE, fade=True)
dots(s, 880, 128, 7, 10, step=10, r=1.9, color=VERT_FONCE, fade=True)
s.poly([(820, 400), (960, 400), (960, 494), (860, 494)], fill=TURQUOISE, alpha=0.9)
# logos partenaires
s.image(IM("logo_fabrique.png"), 52, 26, 118, 79)
s.image(IM("logo_simplon.png"), 800, 30, 128, 65)
# photo hero
s.image(IM("hero_team.png"), 292, 22, 376, 187)
# bloc texte
s.text(u"SADIYA DIGITAL AGRI", 190, 232, 580, size=29, font=ALFA, color=BLANC,
       align="c", spacing=0.8)
s.line(232, 278, 296, 278, color=TURQUOISE, lw=1.6)
s.line(714, 278, 778, 278, color=TURQUOISE, lw=1.6)
s.text(u"DESIGN & COMMUNITY MANAGEMENT", 190, 271, 580, size=12.5, font=POP,
       bold=True, color=TURQUOISE, align="c", spacing=1.4)
s.text(u"Votre partenaire en production agricole\net communication digitale",
       230, 298, 500, size=10.5, font=POP, color=GRISE, align="c", leading=1.4)
s.line(300, 344, 660, 344, color=TURQUOISE, lw=0.7, alpha=0.55)
s.text(u"SIMPLON SÉNÉGAL", 190, 356, 580, size=14, font=POP, bold=True,
       color=BLANC, align="c", spacing=3.2)
s.text(u"PROGRAMME DE PRÉ-INCUBATION 2026", 190, 382, 580, size=8.8, font=POP,
       bold=True, color=TURQUOISE, align="c", spacing=2.4)
s.text(u"Juillet – Septembre 2026", 190, 402, 580, size=9, font=POP, italic=True,
       color=GRISE, align="c")
s.rect(230, 426, 500, 32, fill=TURQUOISE, radius=16)
s.text(u"Présentatrice : Nene Halimatou Sahdiya Diallo",
       230, 436, 500, size=11.5, font=POP, bold=True, color=BLANC, align="c")
s.text(u"Fondatrice & CEO — Sadiya Digital Agri", 230, 466, 500, size=8.5,
       font=POP, color=GRISE, align="c")

# ============================================================== 02 ACCROCHE
s = new("Accroche")
s.rect(0, 0, W, H, fill=BLANC)
s.rect(0, 0, 452, H, fill=CREME)
s.image(IM("produits_locaux.png"), 470, 62, 476, 442)
s.poly([(410, 0), (700, 0), (640, 78), (470, 78)], fill=TURQUOISE)
dots(s, 18, 96, 6, 11, step=10, r=2.0, color=VERT_FONCE, fade=True)
s.text(u"DU LOCAL", 62, 128, 380, size=44, font=ALFA, color=VERT_FONCE)
s.text(u"AU DIGITAL,", 62, 190, 380, size=44, font=ALFA, color=TURQUOISE)
s.rect(62, 262, 46, 3.5, fill=SAFRAN)
s.text(u"Si nos produits ne sont pas visibles,\ncomment donner envie de les\nconsommer ?",
       62, 284, 344, size=14.5, font=POP, bold=True, color=TRES_FONCE, leading=1.45)
s.text(u"Au Sénégal, des centaines de PME agroalimentaires produisent\n"
       u"d'excellents produits locaux… mais restent invisibles en ligne.",
       62, 392, 348, size=8.6, font=POP, color=OLIVE, leading=1.5)
s.rect(0, 524, W, 16, fill=TURQUOISE)
s.image(FOOTLOGOS, 62, 466, 96, 19)

# ============================================================== 03 LE PROBLEME
s = new("Le Problème")
titlebar(s, u"Constat terrain", u"Le Problème",
         u"Trois freins qui empêchent les acteurs agroalimentaires de vendre en ligne.",
         page=3, accent=SAFRAN)
probs = [
    (u"01", u"Faible présence\nsur les réseaux",
     u"Pages inactives, contenus rares et irréguliers : la marque n'existe pas là où se trouvent ses clients."),
    (u"02", u"Manque de stratégie\nde communication",
     u"On publie sans objectif, sans ligne éditoriale ni calendrier — donc sans résultat mesurable."),
    (u"03", u"Visibilité qui ne\nconvertit pas",
     u"Des vues, parfois des likes, mais aucun prospect qualifié ni contrat signé au bout."),
]
x0, cw, gap = 52, 278, 16
for i, (n, t, d) in enumerate(probs):
    x = x0 + i * (cw + gap)
    card(s, x, 168, cw, 208, fill=BLANC)
    s.rect(x, 168, cw, 4, fill=[SAFRAN, TURQUOISE, VERT_FONCE][i], radius=2)
    numbadge(s, x + 22, 194, n, fill=[SAFRAN, TURQUOISE, VERT_FONCE][i],
             tcol=TRES_FONCE if i == 0 else BLANC)
    s.text(t, x + 22, 232, cw - 44, size=14.5, font=POP, bold=True,
           color=VERT_FONCE, leading=1.28)
    s.line(x + 22, 292, x + 52, 292, color=GRISE, lw=1.4)
    s.text(d, x + 22, 306, cw - 44, size=9.2, font=POP, color=OLIVE, leading=1.55)
s.rect(52, 400, 856, 56, fill=VERT_FONCE, radius=9)
s.text(u"Conséquence", 76, 414, 130, size=9, font=POP, bold=True, color=TURQUOISE,
       spacing=1.4, caps=True)
s.text(u"Des produits de qualité restent inconnus, pendant que les marques importées "
       u"occupent tout l'espace digital.",
       76, 430, 800, size=11.5, font=POP, bold=True, color=BLANC)

# ============================================================== 04 LA SOLUTION
s = new("La Solution")
s.rect(0, 0, W, H, fill=CREME)
s.rect(0, 0, 6, H, fill=VERT_FONCE)
s.image(IM("boutique_phone.png"), 540, 150, 410, 346)
s.poly([(700, 0), (960, 0), (960, 96), (790, 96)], fill=TURQUOISE)
s.text(u"La Solution", 52, 44, 500, size=40, font=ALFA, color=VERT_FONCE)
s.rect(52, 108, 54, 4, fill=SAFRAN)
s.text(u"Une agence de community management spécialisée\ndans le secteur agro-industriel.",
       52, 130, 470, size=15.5, font=POP, bold=True, color=TRES_FONCE, leading=1.4)
chevron(s, 52, 208, 450, 148, VERT_FONCE, tip=30)
s.bullets([u"Stratégie Social Media", u"Création de Contenu", u"Gestion de Communauté"],
          82, 232, 340, size=13, color=BLANC, gap=17, marker="check", mcolor=TURQUOISE,
          font=POP, bold=True)
s.text(u"La double expertise qui fait la différence", 52, 380, 460, size=9, font=POP,
       bold=True, color=TURQUOISE, spacing=1.3, caps=True)
for i, (t, d) in enumerate([(u"Agriculture", u"Licence en agronomie, terrain connu"),
                            (u"Digital", u"Community management certifié Simplon")]):
    x = 52 + i * 232
    card(s, x, 400, 216, 62, fill=BLANC)
    s.text(t, x + 16, 412, 190, size=11.5, font=POP, bold=True, color=VERT_FONCE)
    s.text(d, x + 16, 431, 190, size=8.3, font=POP, color=OLIVE, leading=1.4)
footer(s, page=4)

# ============================================================== 05 MARCHE CIBLE
s = new("Notre marché cible")
s.rect(0, 0, W, H, fill=BLANC)
s.rect(0, 0, W, 92, fill=CREME)
s.rect(0, 92, W, 448, fill="E4EEE6")
s.text(u"NOTRE MARCHÉ CIBLE", 52, 30, 600, size=24, font=ALFA, color=TRES_FONCE)
s.text(u"Un marché 100 % B2B au cœur de l'agroalimentaire sénégalais",
       178, 66, 640, size=12, font=POP, color=OLIVE)
s.image(LOGO, 848, 26, 74, 30)
# noyau central
s.rect(310, 132, 340, 152, fill=VERT_FONCE, radius=13)
s.text(u"SADIYA DIGITAL AGRI", 310, 150, 340, size=10, font=POP, bold=True,
       color=BLANC, align="c", spacing=1.3)
s.text(u"Digitaliser la visibilité\net la commercialisation", 320, 176, 320,
       size=17, font=ALFA, color=BLANC, align="c", leading=1.25)
s.text(u"des acteurs agroalimentaires sénégalais", 320, 244, 320, size=8.2,
       font=POP, color=GRISE, align="c")
segs = [
    (u"01", u"PRODUCTEURS", u"Exploitations agricoles\n& entreprises de production", 52, 156, 232),
    (u"05", u"ACHETEURS PRO", u"Hôtels, restaurants,\ncommerces & enseignes", 676, 156, 232),
    (u"02", u"TRANSFORMATEURS", u"PME et entreprises\nde transformation", 62, 332, 226),
    (u"03", u"GIE & COOPÉRATIVES", u"Structures collectives\nà professionnaliser", 366, 356, 228),
    (u"04", u"DISTRIBUTEURS", u"Grossistes, distributeurs\n& acteurs de la chaîne", 672, 332, 232),
]
for n, t, d, x, y, w in segs:
    card(s, x, y, w, 96, fill=BLANC, line=TURQUOISE, radius=10, lw=0.9)
    numbadge(s, x + 16, y + 14, n, d=20, size=8.5)
    s.text(t, x + 43, y + 18, w - 55, size=11.5, font=POP, bold=True, color=VERT_FONCE)
    s.text(d, x + 16, y + 50, w - 32, size=9, font=POP, color=TRES_FONCE, leading=1.45)
for (x, y) in [(284, 200), (676, 200), (288, 356), (480, 356), (672, 356)]:
    s.line(480, 258, x, y, color=TURQUOISE, lw=0.6, dash=[2, 3], alpha=0.75)
s.rect(0, 522, W, 18, fill=VERT_FONCE)

# ============================================================== 06 TOMSTER
s = new("Méthode TOMSTER")
titlebar(s, u"Notre méthode", u"La stratégie TOMSTER",
         u"Six étapes pour transformer une présence digitale en opportunités commerciales.",
         page=6)
items = [
    ("T", u"Target", u"À qui je m'adresse ?", TURQUOISE),
    ("O", u"Objectives", u"Ce que je veux accomplir", VERT_FONCE),
    ("M", u"Message", u"Ce que je dis, et comment", OLIVE),
    ("S", u"Strategy", u"Mon approche globale", TURQUOISE),
    ("T", u"Tactics", u"Mes actions concrètes", VERT_FONCE),
    ("E+R", u"Execution & Results", u"Je produis, je mesure, j'ajuste", OLIVE),
]
for i, (l, t, d, c) in enumerate(items):
    x = 52 + (i % 3) * 288
    y = 172 + (i // 3) * 150
    card(s, x, y, 268, 128)
    s.rect(x, y, 4, 128, fill=c, radius=2)
    s.ellipse(x + 22, y + 20, 40, 40, fill=c, alpha=0.14)
    s.text(l, x + 22, y + 32, 40, size=15 if len(l) < 3 else 11, font=ALFA,
           color=c, align="c")
    s.text(t, x + 74, y + 24, 180, size=14.5, font=POP, bold=True, color=VERT_FONCE)
    s.text(d, x + 74, y + 46, 180, size=9, font=POP, color=OLIVE, leading=1.4)
    s.line(x + 22, y + 84, x + 246, y + 84, color=GRISE_CLAIR, lw=1)
    s.text([u"Cible & persona", u"Objectifs SMART", u"Positionnement & valeur",
            u"Réseaux & parcours", u"Calendrier éditorial", u"KPI & ajustement"][i],
           x + 22, y + 96, 220, size=8.5, font=POP, bold=True, color=c)

# ============================================================== 07 TARGET
s = new("T — Target")
titlebar(s, u"T · Target", u"À qui nous adressons-nous ?",
         u"Un marché B2B concentré, identifiable et joignable directement en ligne.",
         page=7)
card(s, 52, 168, 420, 132)
s.rect(52, 168, 420, 4, fill=TURQUOISE, radius=2)
s.text(u"CIBLE PRINCIPALE", 74, 186, 300, size=9, font=POP, bold=True,
       color=TURQUOISE, spacing=1.4)
s.text(u"Dirigeants et responsables communication des PME agroalimentaires "
       u"sénégalaises : marques locales, coopératives, unités artisanales et "
       u"agro-industrielles.",
       74, 208, 376, size=10, font=POP, color=TRES_FONCE, leading=1.55)
card(s, 488, 168, 420, 132)
s.rect(488, 168, 420, 4, fill=OLIVE, radius=2)
s.text(u"CIBLE SECONDAIRE", 510, 186, 300, size=9, font=POP, bold=True,
       color=OLIVE, spacing=1.4)
s.text(u"Grandes entreprises et industries agroalimentaires sénégalaises, "
       u"disposant de budgets structurés et d'enjeux de marque nationale.",
       510, 208, 376, size=10, font=POP, color=TRES_FONCE, leading=1.55)
# persona
s.rect(52, 318, 856, 148, fill=VERT_FONCE, radius=11)
s.ellipse(80, 344, 76, 76, fill=TURQUOISE, alpha=0.22)
s.text(u"A", 80, 366, 76, size=30, font=ALFA, color=TURQUOISE, align="c")
s.text(u"PERSONA PRINCIPAL", 178, 338, 300, size=8.5, font=POP, bold=True,
       color=TURQUOISE, spacing=1.6)
s.text(u"Aminata, 36 ans", 178, 354, 300, size=17, font=ALFA, color=BLANC)
s.text(u"Directrice générale d'une PME de transformation de fruits et légumes à Dakar.",
       178, 386, 420, size=9.2, font=POP, color=GRISE, leading=1.45)
per = [(u"Besoin", u"Faire connaître ses gammes\nde jus locaux"),
       (u"Frein", u"Manque de temps et\nd'expertise interne"),
       (u"Réseaux", u"LinkedIn · Facebook\n· TikTok")]
for i, (k, v) in enumerate(per):
    bx = 178 + i * 240
    by = 418
    s.rect(bx, by, 226, 36, fill=BLANC, alpha=0.10, radius=6)
    s.text(k.upper(), bx + 12, by + 7, 200, size=7.2, font=POP, bold=True,
           color=TURQUOISE, spacing=1.2)
    s.text(v.replace("\n", " "), bx + 12, by + 18, 206, size=8.2, font=POP, color=BLANC)
s.text(u"« Elle possède de bons produits locaux mais manque de temps et de compétences "
       u"pour les rendre visibles en ligne. »",
       52, 478, 856, size=9.5, font=POP, italic=True, color=OLIVE, align="c")

# ============================================================== 08 OBJECTIVES
s = new("O — Objectives")
titlebar(s, u"O · Objectives", u"Qu'est-ce que je veux accomplir ?",
         u"Trois objectifs SMART, mesurables et échelonnés sur les 6 premiers mois.",
         page=8)
objs = [
    (u"1", u"NOTORIÉTÉ", u"500", u"abonnés qualifiés",
     u"Faire connaître Sadiya Digital Agri auprès des PME agroalimentaires "
     u"via des contenus spécialisés et pédagogiques.", u"3 mois", TURQUOISE),
    (u"2", u"PROSPECTION", u"30", u"demandes qualifiées",
     u"Générer des prospects grâce aux contenus éducatifs, études de cas "
     u"et appels à l'action ciblés.", u"6 mois", VERT_FONCE),
    (u"3", u"CONVERSION", u"5", u"contrats signés",
     u"Transformer les prospects en clients avec des offres adaptées "
     u"aux budgets des PME et un suivi personnalisé.", u"6 mois", OLIVE),
]
for i, (n, t, big, unit, d, ech, c) in enumerate(objs):
    x = 52 + i * 288
    card(s, x, 166, 268, 246)
    s.rect(x, 166, 268, 5, fill=c, radius=2)
    s.text(t, x + 22, 188, 220, size=10.5, font=POP, bold=True, color=c, spacing=1.5)
    s.text(big, x + 22, 210, 220, size=44, font=ALFA, color=VERT_FONCE)
    s.text(unit, x + 22, 268, 220, size=9.5, font=POP, bold=True, color=OLIVE)
    s.line(x + 22, 292, x + 246, 292, color=GRISE_CLAIR, lw=1)
    s.text(d, x + 22, 304, 224, size=9, font=POP, color=TRES_FONCE, leading=1.5)
    s.rect(x + 22, 372, 84, 22, fill=c, radius=11)
    s.text(ech, x + 22, 378, 84, size=8.5, font=POP, bold=True,
           color=BLANC, align="c")
s.rect(52, 434, 856, 44, fill=VERT_FONCE, radius=9)
s.text(u"Visibilité  ›  Engagement  ›  Prospects  ›  Clients",
       52, 448, 856, size=14, font=POP, bold=True, color=TURQUOISE, align="c",
       spacing=0.8)

# ============================================================== 09 MESSAGE
s = new("M — Message")
titlebar(s, u"M · Message", u"Qu'est-ce que je veux dire ?",
         u"Un positionnement clair, une proposition de valeur unique, un ton reconnaissable.",
         page=9)
s.rect(52, 166, 546, 108, fill=VERT_FONCE, radius=10)
s.text(u"PROPOSITION DE VALEUR", 76, 182, 300, size=8.5, font=POP, bold=True,
       color=TURQUOISE, spacing=1.6)
s.text(u"« Rendre les produits locaux sénégalais aussi visibles\n"
       u"en ligne qu'ils le sont dans les rayons. »",
       76, 202, 500, size=14.5, font=ALFA, color=BLANC, leading=1.32)
card(s, 614, 166, 294, 108)
s.rect(614, 166, 4, 108, fill=SAFRAN, radius=2)
s.text(u"POSITIONNEMENT", 636, 182, 250, size=8.5, font=POP, bold=True,
       color=OLIVE, spacing=1.6)
s.text(u"L'agence qui combine expertise agricole et maîtrise digitale "
       u"au service de l'agroalimentaire sénégalais.",
       636, 202, 252, size=9.5, font=POP, color=TRES_FONCE, leading=1.55)
s.text(u"NOS MESSAGES CLÉS", 52, 296, 400, size=9, font=POP, bold=True,
       color=TURQUOISE, spacing=1.6)
msgs = [u"Sadiya Digital Agri comprend à la fois l'agriculture et le digital.",
        u"Les produits cultivés et transformés au Sénégal méritent d'être visibles en ligne.",
        u"Nous transformons votre présence sociale en visibilité, communauté et opportunités."]
for i, m in enumerate(msgs):
    y = 318 + i * 46
    card(s, 52, y, 546, 38, fill=BLANC)
    s.ellipse(66, y + 12, 14, 14, fill=TURQUOISE, alpha=0.18)
    s.text(str(i + 1), 66, y + 15, 14, size=8, font=POP, bold=True,
           color=VERT_FONCE, align="c")
    s.text(m, 90, y + 13, 496, size=9.6, font=POP, color=TRES_FONCE)
card(s, 614, 296, 294, 182)
s.text(u"TON DE VOIX", 636, 312, 250, size=8.5, font=POP, bold=True,
       color=OLIVE, spacing=1.6)
for i, (w_, ok) in enumerate([(u"Professionnel", 1), (u"Chaleureux", 1),
                              (u"Pédagogique", 1), (u"Dynamique", 1),
                              (u"Jargon inutile", 0), (u"Promesses irréalistes", 0),
                              (u"Ton agressif", 0)]):
    y = 334 + i * 20
    c = TURQUOISE if ok else "C4453F"
    if ok:
        checkmark(s, 636, y + 1, 11, fill=c)
    else:
        s.ellipse(636, y + 1, 11, 11, fill=c)
        s.line(638.4, y + 3.4, 644.6, y + 9.6, color=BLANC, lw=1.4)
        s.line(644.6, y + 3.4, 638.4, y + 9.6, color=BLANC, lw=1.4)
    s.text(w_, 652, y, 240, size=9, font=POP, color=TRES_FONCE if ok else OLIVE)

# ============================================================== 10 STRATEGY
s = new("S — Strategy")
titlebar(s, u"S · Strategy", u"Quelle approche globale ?",
         u"Trois réseaux, trois rôles complémentaires dans un parcours unique.",
         page=10)
nets = [
    (u"TikTok", u"Réseau de visibilité", u"Vidéo courte et dynamique pour élargir "
     u"la portée et rendre l'agri-digital accessible.", u"Attirer", TURQUOISE),
    (u"Facebook", u"Réseau principal", u"Informer, éduquer, présenter l'offre "
     u"et fédérer une communauté d'acteurs locaux.", u"Engager", VERT_FONCE),
    (u"LinkedIn", u"Réseau B2B", u"Crédibilité, expertise et prospection directe "
     u"auprès des dirigeants et responsables marketing.", u"Convertir", OLIVE),
]
for i, (n, r, d, step, c) in enumerate(nets):
    x = 52 + i * 288
    card(s, x, 170, 268, 176)
    s.rect(x, 170, 268, 5, fill=c, radius=2)
    s.text(n, x + 22, 192, 220, size=19, font=ALFA, color=VERT_FONCE)
    s.text(r, x + 22, 222, 220, size=9, font=POP, bold=True, color=c, spacing=1.1)
    s.line(x + 22, 244, x + 246, 244, color=GRISE_CLAIR, lw=1)
    s.text(d, x + 22, 256, 224, size=9.2, font=POP, color=TRES_FONCE, leading=1.5)
    s.rect(x + 22, 308, 76, 22, fill=c, radius=11)
    s.text(step, x + 22, 314, 76, size=8.8, font=POP, bold=True, color=BLANC, align="c")
    if i < 2:
        s.text(u"›", x + 272, 240, 16, size=20, font=POP, bold=True, color=GRISE, align="c")
s.rect(52, 368, 856, 50, fill=VERT_FONCE, radius=9)
s.text(u"PARCOURS", 76, 384, 90, size=8, font=POP, bold=True, color=TURQUOISE, spacing=1.4)
s.text(u"TikTok attire  ›  Facebook fédère  ›  LinkedIn crédibilise  ›  "
       u"message privé pour convertir",
       160, 383, 730, size=11.5, font=POP, bold=True, color=BLANC)
piliers = [u"🌱 Éducation", u"🚜 Valorisation", u"📱 Expertise", u"💼 Offres", u"🤝 Communauté"]
s.text(u"5 PILIERS ÉDITORIAUX", 52, 434, 300, size=8.5, font=POP, bold=True,
       color=OLIVE, spacing=1.5)
for i, p in enumerate(piliers):
    x = 52 + i * 172
    s.rect(x, 452, 160, 26, fill=BLANC, line=GRISE_CLAIR, radius=13)
    s.text(p.split(" ", 1)[1], x, 459, 160, size=9, font=POP, bold=True,
           color=VERT_FONCE, align="c")

# ============================================================== 11 TACTICS
s = new("T — Tactics")
titlebar(s, u"T · Tactics", u"Quelles actions concrètes ?",
         u"Un calendrier éditorial réaliste : 3 jours de publication par semaine.",
         page=11)
rows = [
    (u"MARDI", u"LinkedIn + Facebook", u"Post + visuel expert", u"Crédibilité", VERT_FONCE),
    (u"VENDREDI", u"Facebook + TikTok", u"Carrousel + vidéo courte", u"Engagement", TURQUOISE),
    (u"DIMANCHE", u"LinkedIn + TikTok", u"Storytelling / étude de cas", u"Prospection", OLIVE),
]
s.rect(52, 168, 546, 26, fill=VERT_FONCE, radius=5)
for lbl, x, w_ in [(u"JOUR", 68, 90), (u"RÉSEAUX", 158, 150),
                   (u"CONTENU", 308, 180), (u"OBJECTIF", 488, 100)]:
    s.text(lbl, x, 175, w_, size=7.8, font=POP, bold=True, color=TURQUOISE, spacing=1.2)
for i, (d, r, ct, ob, c) in enumerate(rows):
    y = 200 + i * 46
    s.rect(52, y, 546, 40, fill=BLANC if i % 2 == 0 else CREME,
           line=GRISE_CLAIR, radius=5)
    s.rect(52, y, 4, 40, fill=c, radius=2)
    s.text(d, 68, y + 14, 90, size=10, font=POP, bold=True, color=VERT_FONCE)
    s.text(r, 158, y + 14, 150, size=9.2, font=POP, color=TRES_FONCE)
    s.text(ct, 308, y + 14, 180, size=9.2, font=POP, color=TRES_FONCE)
    s.rect(488, y + 10, 84, 20, fill=c, radius=10)
    s.text(ob, 488, y + 15, 84, size=8, font=POP, bold=True, color=BLANC, align="c")
s.text(u"ANIMATION DE LA COMMUNAUTÉ", 52, 358, 400, size=8.5, font=POP, bold=True,
       color=OLIVE, spacing=1.5)
anim = [(u"2-3", u"stories / sem."), (u"1", u"sondage / sem."),
        (u"2", u"Q&R / mois"), (u"1", u"live / mois"), (u"1-2", u"défis TikTok")]
for i, (n, l) in enumerate(anim):
    x = 52 + i * 111
    s.rect(x, 378, 100, 52, fill=BLANC, line=GRISE_CLAIR, radius=7)
    s.text(n, x, 386, 100, size=17, font=ALFA, color=TURQUOISE, align="c")
    s.text(l, x + 6, 412, 88, size=7.6, font=POP, color=OLIVE, align="c")
card(s, 614, 168, 294, 262)
s.rect(614, 168, 294, 4, fill=TURQUOISE, radius=2)
s.text(u"MOYENS MOBILISÉS", 636, 186, 250, size=8.5, font=POP, bold=True,
       color=VERT_FONCE, spacing=1.5)
tools = [(u"Canva Free", u"visuels & carrousels"), (u"CapCut", u"montage vidéo"),
         (u"Meta Business Suite", u"programmation FB"), (u"TikTok Studio", u"gestion TikTok"),
         (u"LinkedIn", u"publication & stats"), (u"Google Drive", u"stockage"),
         (u"Google Sheets", u"calendrier & suivi")]
for i, (t, d) in enumerate(tools):
    y = 208 + i * 30
    s.rect(636, y + 4, 5, 5, fill=TURQUOISE, radius=2.5)
    s.text(t, 650, y, 240, size=9.4, font=POP, bold=True, color=TRES_FONCE)
    s.text(d, 650, y + 12, 240, size=7.8, font=POP, color=OLIVE)

# ============================================================== 12 EXECUTION
s = new("E — Execution")
titlebar(s, u"E · Execution", u"Comment je produis et j'anime ?",
         u"Une production organisée, une modération cadrée, une relation client rapide.",
         page=12)
blocks = [
    (u"01", u"Production & publication", TURQUOISE,
     [u"Début du mois : thèmes et objectifs définis.",
      u"Chaque semaine : création, validation, préparation.",
      u"Contenus créés en avance, jamais improvisés.",
      u"Programmation via Meta Suite et TikTok Studio."]),
    (u"02", u"Modération", VERT_FONCE,
     [u"Ton professionnel, chaleureux et respectueux.",
      u"Répondre avec courtoisie, jamais de conflit.",
      u"Critiques constructives conservées.",
      u"Réclamations déplacées en message privé."]),
    (u"03", u"Relation client", OLIVE,
     [u"Surveillance quotidienne des messages.",
      u"Délai cible : moins de 24 h ouvrées.",
      u"Demande commerciale : orientée en privé.",
      u"Sujets sensibles transmis au client."]),
]
for i, (n, t, c, its) in enumerate(blocks):
    x = 52 + i * 288
    card(s, x, 166, 268, 190)
    s.rect(x, 166, 268, 4, fill=c, radius=2)
    numbadge(s, x + 22, 186, n, d=20, fill=c, size=8.5)
    s.text(t, x + 50, 190, 210, size=11.5, font=POP, bold=True, color=VERT_FONCE)
    s.bullets(its, x + 22, 224, 228, size=8.6, color=TRES_FONCE, gap=7,
              marker="dot", mcolor=c, leading=1.42)
s.rect(52, 374, 856, 104, fill=VERT_FONCE, radius=10)
s.text(u"PLAN BAD BUZZ", 76, 392, 200, size=8.5, font=POP, bold=True,
       color=TURQUOISE, spacing=1.6)
steps = [u"Identifier", u"Vérifier", u"Répondre", u"Traiter", u"Suivre", u"Tirer les leçons"]
for i, st in enumerate(steps):
    x = 76 + i * 136
    s.ellipse(x, 412, 22, 22, fill=TURQUOISE, alpha=0.22)
    s.text(str(i + 1), x, 418, 22, size=9, font=POP, bold=True, color=TURQUOISE, align="c")
    s.text(st, x + 28, 418, 104, size=9, font=POP, bold=True, color=BLANC)
    if i < 5:
        s.line(x + 108, 423, x + 128, 423, color=TURQUOISE, lw=0.8, alpha=0.5)
s.text(u"Règle d'or : ne jamais répondre sous le coup de l'émotion.",
       76, 450, 700, size=9.5, font=POP, italic=True, color=GRISE)

# ============================================================== 13 RESULTS
s = new("R — Results")
titlebar(s, u"R · Results", u"Est-ce que ça marche ?",
         u"Des KPI clairs par objectif, un bilan hebdomadaire et mensuel.",
         page=13)
kpis = [
    (u"Notoriété", u"Abonnés · portée · impressions · vues",
     u"Statistiques Facebook, LinkedIn, TikTok", u"Mensuel", TURQUOISE),
    (u"Prospects", u"Messages · demandes · clics · leads qualifiés",
     u"Statistiques + tableau de suivi", u"Hebdo + mensuel", VERT_FONCE),
    (u"Conversion", u"Prospects convertis · contrats · taux",
     u"Tableau de suivi commercial", u"Mensuel", OLIVE),
]
for i, (t, k, o, f, c) in enumerate(kpis):
    y = 168 + i * 78
    card(s, 52, y, 546, 66)
    s.rect(52, y, 5, 66, fill=c, radius=2)
    s.text(t, 76, y + 12, 150, size=13, font=POP, bold=True, color=VERT_FONCE)
    s.text(k, 76, y + 34, 300, size=8.8, font=POP, color=TRES_FONCE)
    s.text(o, 392, y + 14, 200, size=8.4, font=POP, color=OLIVE, leading=1.4)
    s.rect(392, y + 38, 96, 18, fill=c, radius=9)
    s.text(f, 392, y + 42, 96, size=7.4, font=POP, bold=True, color=BLANC, align="c")
card(s, 614, 168, 294, 234)
s.rect(614, 168, 294, 4, fill=SAFRAN, radius=2)
s.text(u"BOUCLE D'AMÉLIORATION", 636, 186, 250, size=8.5, font=POP, bold=True,
       color=VERT_FONCE, spacing=1.4)
cycle = [u"Publier", u"Mesurer", u"Analyser", u"Ajuster", u"Améliorer"]
for i, cst in enumerate(cycle):
    y = 214 + i * 36
    s.ellipse(636, y, 24, 24, fill=TURQUOISE if i % 2 == 0 else VERT_FONCE)
    s.text(str(i + 1), 636, y + 7, 24, size=9, font=POP, bold=True, color=BLANC, align="c")
    s.text(cst, 670, y + 6, 200, size=11, font=POP, bold=True, color=TRES_FONCE)
    if i < 4:
        s.line(648, y + 26, 648, y + 34, color=GRISE, lw=1.2)
s.rect(52, 420, 546, 58, fill=VERT_FONCE, radius=9)
s.text(u"Chaque semaine : identifier les contenus performants.   |   "
       u"Chaque mois : comparer aux objectifs et ajuster.",
       76, 442, 500, size=9.6, font=POP, color=BLANC, leading=1.45)

# ============================================================== 14 MODELE ECO — vue d'ensemble
s = new(u"Modèle économique — vue d'ensemble")
titlebar(s, u"Business model", u"Modèle Économique",
         u"Comment Sadiya Digital Agri crée, délivre et capture de la valeur.",
         page=14)
blocks = [
    (u"Proposition\nde valeur", TURQUOISE,
     [u"Communication digitale spécialisée agro", u"Double expertise agriculture + digital",
      u"Produits locaux rendus visibles et attractifs"]),
    (u"Clients", VERT_FONCE,
     [u"PME agroalimentaires sénégalaises", u"Coopératives & GIE de producteurs",
      u"Grandes industries (cible secondaire)"]),
    (u"Canaux", OLIVE,
     [u"LinkedIn : prospection B2B directe", u"Facebook : communauté et offre",
      u"TikTok : portée et notoriété"]),
    (u"Sources de\nrevenus", TURQUOISE,
     [u"Abonnements mensuels récurrents", u"Prestations ponctuelles à la demande",
      u"Campagnes publicitaires gérées"]),
    (u"Ressources\nclés", VERT_FONCE,
     [u"Compétences agro + community management", u"Canva, CapCut, Meta Suite, TikTok Studio",
      u"Identité de marque et site portfolio"]),
    (u"Structure\nde coûts", OLIVE,
     [u"Outils en version gratuite au démarrage", u"Connexion, déplacements terrain",
      u"Budget publicitaire refacturé au client"]),
]
for i, (t, col, its) in enumerate(blocks):
    x = 52 + (i % 3) * 288
    y = 168 + (i // 3) * 156
    card(s, x, y, 268, 140)
    s.rect(x, y, 268, 4, fill=col, radius=2)
    s.text(t.replace("\n", " "), x + 20, y + 18, 230, size=12.5, font=POP, bold=True,
           color=VERT_FONCE)
    s.line(x + 20, y + 42, x + 248, y + 42, color=GRISE_CLAIR, lw=1)
    s.bullets(its, x + 20, y + 54, 232, size=8.4, color=TRES_FONCE, gap=6,
              marker="dot", mcolor=col, leading=1.4)

# ============================================================== 15 OFFRES
s = new(u"Nos offres")
titlebar(s, u"Business model", u"Nos Offres d'Abonnement",
         u"Trois formules mensuelles, plus des prestations à la demande.",
         page=15)
offers = [
    (u"ESSENTIEL", u"75 000", [u"8 publications / mois", u"Visuels personnalisés",
                               u"Gestion de communauté"], False, GRISE),
    (u"PRO", u"150 000", [u"12 publications + 4 vidéos", u"Animation de communauté",
                          u"Stratégie éditoriale"], True, TURQUOISE),
    (u"PREMIUM", u"250 000", [u"16 publications + 8 vidéos", u"Stratégie + publicité",
                              u"Reporting mensuel"], False, VERT_FONCE),
]
for i, (n, p, feats, hl, c) in enumerate(offers):
    x = 52 + i * 288
    y = 172 if not hl else 162
    h = 208 if not hl else 228
    card(s, x, y, 268, h, fill=VERT_FONCE if hl else BLANC,
         line=TURQUOISE if hl else GRISE_CLAIR, lw=1.6 if hl else 1.0)
    if hl:
        s.rect(x + 88, y - 11, 92, 22, fill=TURQUOISE, radius=11)
        s.text(u"RECOMMANDÉ", x + 88, y - 6, 92, size=7.4, font=POP, bold=True,
               color=BLANC, align="c", spacing=0.8)
    s.text(n, x + 22, y + 22, 220, size=11, font=POP, bold=True,
           color=TURQUOISE if hl else c, spacing=1.8)
    s.text(p, x + 22, y + 42, 220, size=30, font=ALFA, color=BLANC if hl else VERT_FONCE)
    s.text(u"FCFA / mois", x + 22, y + 84, 220, size=8.6, font=POP,
           color=GRISE if hl else OLIVE)
    s.line(x + 22, y + 104, x + 246, y + 104, color=TURQUOISE if hl else GRISE_CLAIR, lw=1)
    s.bullets(feats, x + 22, y + 118, 226, size=9.2,
              color=BLANC if hl else TRES_FONCE, gap=10, marker="check",
              mcolor=TURQUOISE if hl else VERT_FONCE)
s.rect(52, 404, 856, 44, fill=CREME, line=TURQUOISE, radius=9)
s.rect(52, 404, 5, 44, fill=SAFRAN, radius=2)
s.text(u"REVENUS COMPLÉMENTAIRES", 76, 412, 300, size=8, font=POP, bold=True,
       color=TURQUOISE, spacing=1.5)
s.text(u"Contenus à la demande, campagnes publicitaires et stratégie ponctuelle "
       u"— à partir de 25 000 FCFA.",
       76, 426, 780, size=9.5, font=POP, color=TRES_FONCE)
s.text(u"Paiement mensuel d'avance  ·  engagement 3 mois minimum  ·  devis sur mesure "
       u"au-delà de 16 publications",
       52, 460, 856, size=8.6, font=POP, italic=True, color=OLIVE, align="c")

# ============================================================== 16 PROJECTIONS
s = new(u"Rentabilité & projections")
titlebar(s, u"Business model", u"Rentabilité & Projections",
         u"Un point mort atteignable dès le troisième client régulier.",
         page=16)
kpis = [(u"85 000", u"FCFA", u"Charges mensuelles estimées", OLIVE),
        (u"3", u"clients", u"Seuil de rentabilité (offre Pro)", TURQUOISE),
        (u"450 000", u"FCFA", u"Revenu mensuel visé à 6 mois", VERT_FONCE),
        (u"5,4 M", u"FCFA", u"Chiffre d'affaires annualisé cible", TURQUOISE)]
for i, (big, unit, lbl, c) in enumerate(kpis):
    x = 52 + i * 216
    card(s, x, 166, 196, 104)
    s.rect(x, 166, 196, 4, fill=c, radius=2)
    s.text(big, x + 18, 186, 160, size=25, font=ALFA, color=VERT_FONCE)
    s.text(unit, x + 18, 220, 160, size=8.5, font=POP, bold=True, color=c)
    s.text(lbl, x + 18, 238, 164, size=8, font=POP, color=OLIVE, leading=1.35)
# scenario de montee en charge
s.text(u"SCÉNARIO DE MONTÉE EN CHARGE", 52, 292, 400, size=8.5, font=POP, bold=True,
       color=OLIVE, spacing=1.5)
scen = [(u"Mois 1–3", u"2 clients", u"150 000", 0.28, GRISE),
        (u"Mois 4–6", u"3 clients", u"450 000", 0.62, TURQUOISE),
        (u"Mois 7–12", u"5 clients", u"750 000", 1.0, VERT_FONCE)]
for i, (per, cl, rev, frac, c) in enumerate(scen):
    y = 316 + i * 46
    s.text(per, 52, y + 12, 80, size=9.5, font=POP, bold=True, color=TRES_FONCE)
    s.text(cl, 138, y + 12, 70, size=9, font=POP, color=OLIVE)
    s.rect(208, y + 8, 292, 22, fill=GRISE_CLAIR, radius=11)
    s.rect(208, y + 8, 292 * frac, 22, fill=c, radius=11)
    s.text(rev + u" FCFA/mois", 508, y + 12, 172, size=9, font=POP, bold=True,
           color=VERT_FONCE)
card(s, 700, 292, 208, 172)
s.rect(700, 292, 208, 4, fill=SAFRAN, radius=2)
s.text(u"CHARGES PRINCIPALES", 718, 308, 180, size=8, font=POP, bold=True,
       color=VERT_FONCE, spacing=1.3)
charges = [(u"Connexion internet", u"25 000"), (u"Déplacements terrain", u"20 000"),
           (u"Outils & abonnements", u"20 000"), (u"Divers & imprévus", u"20 000")]
for i, (k, v) in enumerate(charges):
    y = 330 + i * 26
    s.text(k, 718, y, 130, size=8.2, font=POP, color=TRES_FONCE)
    s.text(v, 828, y, 62, size=8.2, font=POP, bold=True, color=OLIVE, align="r")
s.line(718, 434, 890, 434, color=GRISE_CLAIR, lw=1)
s.text(u"Total", 718, 442, 100, size=8.6, font=POP, bold=True, color=VERT_FONCE)
s.text(u"85 000 FCFA", 788, 442, 102, size=8.6, font=POP, bold=True,
       color=TURQUOISE, align="r")
s.text(u"Hypothèses prudentes : outils en version gratuite, structure sans salarié, "
       u"budget publicitaire refacturé au client.",
       52, 482, 640, size=8.2, font=POP, italic=True, color=OLIVE)

# ============================================================== 17 CONCURRENCE
s = new("Marché & différenciation")
titlebar(s, u"Benchmark", u"Concurrence & Différenciation",
         u"Un marché occupé par des généralistes — aucune agence spécialisée agro.",
         page=17)
comp = [
    (u"Agence Kolonell", u"250–600 k FCFA/mois", u"Expert, axé résultats et stratégie"),
    (u"Agence WEDRAOGO", u"dès 130 k FCFA/mois", u"Professionnel, créatif et attractif"),
    (u"CM freelance", u"50–150 k FCFA/mois", u"Généraliste et informel"),
]
s.text(u"LE MARCHÉ AUJOURD'HUI", 52, 166, 300, size=8.5, font=POP, bold=True,
       color=OLIVE, spacing=1.5)
for i, (n, p, po) in enumerate(comp):
    y = 188 + i * 54
    card(s, 52, y, 420, 46, fill=BLANC)
    s.text(n, 72, y + 9, 180, size=10.5, font=POP, bold=True, color=TRES_FONCE)
    s.text(po, 72, y + 26, 240, size=8.2, font=POP, color=OLIVE)
    s.text(p, 320, y + 16, 136, size=9.4, font=POP, bold=True, color=VERT_FONCE, align="r")
s.rect(52, 356, 420, 118, fill=VERT_FONCE, radius=10)
s.text(u"NOTRE DIFFÉRENCIATION", 76, 374, 300, size=8.5, font=POP, bold=True,
       color=TURQUOISE, spacing=1.5)
s.text(u"La seule offre qui combine double expertise agriculture + digital "
       u"et spécialisation exclusive sur les acteurs agroalimentaires sénégalais.",
       76, 394, 372, size=10.5, font=POP, color=BLANC, leading=1.5)
s.text(u"Tarifs d'entrée compétitifs · structure agile · connaissance du terrain",
       76, 448, 372, size=8.4, font=POP, italic=True, color=GRISE)
# SWOT
swot = [(u"FORCES", TURQUOISE, [u"Double expertise agri + digital",
                                u"Agilité d'une structure légère",
                                u"Tarifs compétitifs"]),
        (u"FAIBLESSES", "C4453F", [u"Notoriété à construire",
                                   u"Portfolio grands comptes limité",
                                   u"Ressources de production réduites"]),
        (u"OPPORTUNITÉS", VERT_FONCE, [u"Dynamique « Consommer local »",
                                       u"Digitalisation de l'agro",
                                       u"Niche encore inexploitée"]),
        (u"MENACES", OLIVE, [u"Agences établies",
                             u"Budgets PME limités",
                             u"Contraintes de connectivité"])]
for i, (t, c, its) in enumerate(swot):
    x = 490 + (i % 2) * 212
    y = 166 + (i // 2) * 156
    card(s, x, y, 196, 142)
    s.rect(x, y, 196, 4, fill=c, radius=2)
    s.text(t, x + 16, y + 16, 170, size=9, font=POP, bold=True, color=c, spacing=1.3)
    s.bullets(its, x + 16, y + 42, 172, size=8.2, color=TRES_FONCE, gap=6,
              marker="dot", mcolor=c, leading=1.4)

# ============================================================== 18 REALISATIONS — identite
s = new(u"Réalisations — identité de marque")
titlebar(s, u"Traction", u"Ce que j'ai déjà réalisé",
         u"Une marque complète, construite de A à Z : logo, charte, bannière et carte de visite.",
         page=18)
# logo
card(s, 52, 168, 268, 152)
s.rect(52, 168, 268, 4, fill=TURQUOISE, radius=2)
s.text(u"LOGO", 74, 184, 200, size=8, font=POP, bold=True, color=TURQUOISE, spacing=1.5)
s.image(LOGO, 88, 208, 196, 79)
s.text(u"Version horizontale couleur", 74, 296, 224, size=8, font=POP, color=OLIVE)
# palette
card(s, 336, 168, 268, 152)
s.rect(336, 168, 268, 4, fill=VERT_FONCE, radius=2)
s.text(u"PALETTE", 358, 184, 200, size=8, font=POP, bold=True, color=VERT_FONCE, spacing=1.5)
pal = [(VERT_FONCE, u"#1F5E3A"), (TURQUOISE, u"#1AAB70"), (OLIVE, u"#42612D"),
       (GRISE, u"#9FB8A2"), (TRES_FONCE, u"#0A1A01"), (BLANC, u"#FFFFFF")]
for i, (c, code) in enumerate(pal):
    x = 358 + (i % 3) * 78
    y = 204 + (i // 3) * 48
    s.rect(x, y, 62, 32, fill=c, line=GRISE_CLAIR if c == BLANC else None, radius=6)
    s.text(code, x, y + 34, 62, size=6.2, font=POP, color=OLIVE, align="c")
s.text(u"6 couleurs officielles", 358, 302, 224, size=8, font=POP, color=OLIVE)
# typographie
card(s, 620, 168, 288, 152)
s.rect(620, 168, 288, 4, fill=OLIVE, radius=2)
s.text(u"TYPOGRAPHIE", 642, 184, 200, size=8, font=POP, bold=True, color=OLIVE, spacing=1.5)
s.text(u"Sadiya", 642, 204, 240, size=22, font=ALFA, color=VERT_FONCE)
s.text(u"Alfa Slab One — titres", 642, 236, 240, size=7.6, font=POP, color=OLIVE)
s.text(u"Digital Agri", 642, 252, 240, size=17, font=POP, bold=True, color=TURQUOISE)
s.text(u"Poppins — sous-titres et textes", 642, 280, 240, size=7.6, font=POP, color=OLIVE)
s.text(u"Hiérarchie à 3 niveaux", 642, 300, 240, size=8, font=POP, color=OLIVE)
# banniere
card(s, 52, 336, 552, 130)
s.rect(52, 336, 552, 4, fill=TURQUOISE, radius=2)
s.text(u"BANNIÈRE RÉSEAUX SOCIAUX", 74, 352, 300, size=8, font=POP, bold=True,
       color=TURQUOISE, spacing=1.5)
s.image(IM("banniere.png"), 74, 372, 508, 82)
# carte de visite
card(s, 620, 336, 288, 130)
s.rect(620, 336, 288, 4, fill=VERT_FONCE, radius=2)
s.text(u"CARTE DE VISITE", 642, 352, 250, size=8, font=POP, bold=True,
       color=VERT_FONCE, spacing=1.5)
s.image(IM("carte_visite.png"), 642, 374, 244, 68)

# ============================================================== 19 REALISATIONS — presence digitale
s = new(u"Réalisations — présence digitale & outils")
titlebar(s, u"Traction", u"Présence Digitale & Outils Maîtrisés",
         u"Des canaux actifs, un site portfolio en ligne et une gestion de projet outillée.",
         page=19)
ICO = lambda n: os.path.join(IMG, "tools", n)
SOC = os.path.join(ROOT, "assets", "img", "icons")

# --- Canaux en ligne
s.text(u"CANAUX EN LIGNE", 52, 164, 400, size=8.5, font=POP, bold=True,
       color=TURQUOISE, spacing=1.5)
channels = [
    (ICO("site.png"), u"Site portfolio", u"nene-hsd.vercel.app", u"En ligne"),
    (os.path.join(SOC, "linkedin.png"), u"Page pro LinkedIn", u"/company/sadiyadigitalagri", u"Active"),
    (os.path.join(SOC, "facebook.png"), u"Page Facebook", u"/sadiyadigitalagri", u"Active"),
    (ICO("pub.png"), u"Meta Business Suite", u"Page pub & programmation", u"Configurée"),
]
for i, (ic, t, d, st) in enumerate(channels):
    x = 52 + i * 216
    card(s, x, 186, 196, 118)
    s.rect(x, 186, 196, 4, fill=TURQUOISE, radius=2)
    s.image(ic, x + 18, 204, 34, 34)
    s.text(t, x + 18, 248, 164, size=10, font=POP, bold=True, color=VERT_FONCE)
    s.text(d, x + 18, 264, 168, size=7.4, font=POP, color=OLIVE, leading=1.35)
    s.rect(x + 18, 282, 58, 15, fill=TURQUOISE, radius=7.5)
    s.text(st, x + 18, 285, 58, size=6.6, font=POP, bold=True, color=BLANC, align="c")

# --- Autres reseaux
s.text(u"AUSSI PRÉSENTE SUR", 52, 320, 300, size=8, font=POP, bold=True,
       color=OLIVE, spacing=1.4)
for i, (f, lbl) in enumerate([("instagram.png", u"Instagram"), ("tiktok.png", u"TikTok"),
                              ("whatsapp.png", u"WhatsApp Business"), ("email.png", u"Email pro")]):
    x = 52 + i * 108
    s.rect(x, 340, 96, 30, fill=BLANC, line=GRISE_CLAIR, radius=15)
    s.image(os.path.join(SOC, f), x + 9, 347, 16, 16)
    s.text(lbl, x + 30, 350, 62, size=7, font=POP, bold=True, color=VERT_FONCE)

# --- Outils maitrises
s.text(u"OUTILS MAÎTRISÉS", 52, 388, 300, size=8.5, font=POP, bold=True,
       color=TURQUOISE, spacing=1.5)
tools = [(ICO("canva.png"), u"Canva", u"Visuels & carrousels"),
         (ICO("capcut.png"), u"CapCut", u"Montage vidéo"),
         (ICO("trello.png"), u"Trello", u"Suivi de projet"),
         (ICO("charte.png"), u"Charte", u"Identité visuelle")]
for i, (ic, t, d) in enumerate(tools):
    x = 52 + i * 138
    card(s, x, 410, 126, 62)
    s.image(ic, x + 12, 424, 30, 30)
    s.text(t, x + 50, 424, 70, size=9.4, font=POP, bold=True, color=VERT_FONCE)
    s.text(d, x + 50, 439, 74, size=6.8, font=POP, color=OLIVE, leading=1.3)

# --- Gestion de projet Trello (encart)
s.rect(620, 320, 288, 152, fill=VERT_FONCE, radius=10)
s.image(ICO("trello.png"), 642, 338, 30, 30)
s.text(u"SUIVI DE PROJET", 682, 340, 200, size=8, font=POP, bold=True,
       color=TURQUOISE, spacing=1.4)
s.text(u"Trello", 682, 352, 200, size=14, font=ALFA, color=BLANC)
s.bullets([u"Un tableau par client", u"Calendrier éditorial partagé",
           u"Validation des contenus en ligne", u"Suivi des KPI et des livrables"],
          642, 384, 250, size=8.2, color=BLANC, gap=6, marker="dot",
          mcolor=TURQUOISE, leading=1.4)

# ============================================================== 20 AMBITIONS
s = new(u"Ambitions")
titlebar(s, u"Vision", u"Ambitions",
         u"Où je veux emmener Sadiya Digital Agri dans les 12 prochains mois.",
         page=20)
amb = [
    (u"1", u"Acquérir mes premiers\nclients agro-industriels",
     u"Signer 5 contrats avec des PME agroalimentaires sénégalaises.",
     u"0–6 mois", TURQUOISE),
    (u"2", u"Développer un portefeuille\nde clients réguliers",
     u"Passer d'une logique de mission ponctuelle à l'abonnement récurrent.",
     u"6–9 mois", VERT_FONCE),
    (u"3", u"Renforcer mon expertise\nen publicité en ligne",
     u"Maîtriser Meta Ads et l'analytics pour prouver le ROI de chaque campagne.",
     u"6–9 mois", OLIVE),
    (u"4", u"Structurer une offre de\nproduction vidéo terrain",
     u"Filmer du champ à l'assiette : le format qui valorise le mieux le local.",
     u"9–12 mois", TURQUOISE),
    (u"5", u"Faire de Sadiya Digital Agri\nune agence reconnue",
     u"Devenir la référence de la communication digitale agroalimentaire au Sénégal.",
     u"12 mois +", VERT_FONCE),
]
# --- Les 3 premieres en cartes hautes
for i, (n, t, d, ech, c) in enumerate(amb[:3]):
    x = 52 + i * 288
    card(s, x, 166, 268, 172)
    s.rect(x, 166, 268, 4, fill=c, radius=2)
    s.ellipse(x + 22, y_ := 186, 34, 34, fill=c, alpha=0.15)
    s.text(n, x + 22, 195, 34, size=15, font=ALFA, color=c, align="c")
    s.text(t.replace("\n", " "), x + 22, 232, 226, size=12.5, font=POP, bold=True,
           color=VERT_FONCE, leading=1.3)
    s.line(x + 22, 282, x + 246, 282, color=GRISE_CLAIR, lw=1)
    s.text(d, x + 22, 292, 228, size=8.4, font=POP, color=OLIVE, leading=1.45)
    s.rect(x + 190, 176, 66, 18, fill=c, radius=9)
    s.text(ech, x + 190, 180, 66, size=7, font=POP, bold=True, color=BLANC, align="c")
# --- Les 2 dernieres, format large
for i, (n, t, d, ech, c) in enumerate(amb[3:]):
    x = 52 + i * 440
    card(s, x, 352, 420, 76)
    s.rect(x, 352, 4, 76, fill=c, radius=2)
    numbadge(s, x + 20, 366, n, d=26, fill=c, size=11)
    s.rect(x + 344, 364, 62, 17, fill=c, radius=8.5)
    s.text(ech, x + 344, 368, 62, size=7, font=POP, bold=True, color=BLANC, align="c")
    s.text(t.replace("\n", " "), x + 58, 366, 278, size=11, font=POP, bold=True,
           color=VERT_FONCE, leading=1.25)
    s.text(d, x + 58, 400, 344, size=8.2, font=POP, color=OLIVE, leading=1.4)
# --- Cap final
s.rect(52, 444, 856, 40, fill=VERT_FONCE, radius=9)
s.text(u"LE CAP", 76, 456, 70, size=8, font=POP, bold=True, color=TURQUOISE, spacing=1.4)
s.text(u"Faire des produits agroalimentaires sénégalais une référence digitale — "
       u"visibles, désirables et vendus en ligne.",
       142, 455, 740, size=10.5, font=POP, bold=True, color=BLANC)

# ============================================================== 21 CTA
s = new(u"Appel à l'action")
titlebar(s, u"Ce dont j'ai besoin", u"Appel à l'Action",
         u"De quoi ai-je besoin pour faire grandir Sadiya Digital Agri ?",
         page=21)

# --- Le montant demande
s.rect(52, 164, 268, 132, fill=VERT_FONCE, radius=10)
s.text(u"FINANCEMENT DEMANDÉ", 74, 184, 230, size=8, font=POP, bold=True,
       color=TURQUOISE, spacing=1.5)
s.text(u"1 850 000", 74, 206, 230, size=32, font=ALFA, color=BLANC)
s.text(u"FCFA", 74, 248, 230, size=11, font=POP, bold=True, color=TURQUOISE)
s.line(74, 270, 298, 270, color=TURQUOISE, lw=0.8, alpha=0.55)
s.text(u"Soit environ 2 820 € — décaissement sur 12 mois",
       74, 276, 232, size=7.6, font=POP, color=GRISE)

# --- Repartition du financement
posts = [(u"Équipements de production", u"1 020 000", 1.00, TURQUOISE),
         (u"Abonnements & outils (12 mois)", u"305 000", 0.30, VERT_FONCE),
         (u"Formations professionnelles", u"275 000", 0.27, OLIVE),
         (u"Site vitrine professionnel", u"250 000", 0.25, TURQUOISE)]
s.text(u"RÉPARTITION DU FINANCEMENT", 344, 170, 400, size=8, font=POP, bold=True,
       color=TURQUOISE, spacing=1.5)
for i, (lbl, montant, frac, c) in enumerate(posts):
    y = 192 + i * 27
    s.text(lbl, 344, y, 250, size=9, font=POP, color=TRES_FONCE)
    s.rect(596, y + 2, 200, 9, fill=GRISE_CLAIR, radius=4.5)
    s.rect(596, y + 2, 200 * frac, 9, fill=c, radius=4.5)
    s.text(montant, 808, y, 100, size=9, font=POP, bold=True, color=VERT_FONCE,
           align="r")
s.line(344, 304, 908, 304, color=GRISE_CLAIR, lw=1)
s.text(u"TOTAL", 344, 310, 200, size=9.5, font=POP, bold=True, color=VERT_FONCE)
s.text(u"1 850 000 FCFA", 708, 310, 200, size=9.5, font=POP, bold=True,
       color=TURQUOISE, align="r")

# --- Besoins non financiers
s.text(u"AU-DELÀ DU FINANCEMENT", 52, 344, 400, size=8, font=POP, bold=True,
       color=OLIVE, spacing=1.5)
needs = [(u"Accompagnement", u"Mentorat business : structuration\nde l'offre, pricing et gestion", TURQUOISE),
         (u"Partenariat", u"Accès aux réseaux et fédérations\nagro-industriels du Sénégal", VERT_FONCE),
         (u"Visibilité", u"Références, recommandations\net premiers clients pilotes", OLIVE)]
for i, (t, d, c) in enumerate(needs):
    x = 52 + i * 288
    card(s, x, 366, 268, 84)
    s.rect(x, 366, 4, 84, fill=c, radius=2)
    s.text(t, x + 22, 380, 220, size=13, font=POP, bold=True, color=VERT_FONCE)
    s.text(d, x + 22, 404, 228, size=8.4, font=POP, color=OLIVE, leading=1.45)

s.text(u"« Avec votre soutien, mon activité peut créer plus d'impact "
       u"et d'opportunités. »",
       52, 466, 856, size=13, font=ALFA, color=VERT_FONCE, align="c")

# ============================================================== 22 BUDGET DETAILLE
s = new(u"Détail du financement")
titlebar(s, u"Appel à l'action", u"À Quoi Servira le Financement",
         u"Chaque poste est directement lié à la production de contenu et à l'acquisition client.",
         page=22)
ICO = lambda n: os.path.join(IMG, "tools", n)
SOC = os.path.join(ROOT, "assets", "img", "icons")

# ---- Colonne 1 : equipements
card(s, 52, 164, 420, 178)
s.rect(52, 164, 420, 4, fill=TURQUOISE, radius=2)
s.text(u"ÉQUIPEMENTS DE PRODUCTION", 74, 180, 300, size=8, font=POP, bold=True,
       color=TURQUOISE, spacing=1.4)
s.text(u"1 020 000 FCFA", 320, 179, 130, size=9.5, font=POP, bold=True,
       color=VERT_FONCE, align="r")
equip = [(u"Ordinateur portable", u"Montage vidéo, design et reporting", u"450 000"),
         (u"Smartphone photo/vidéo", u"Captation terrain chez les producteurs", u"350 000"),
         (u"Trépied + stabilisateur", u"Vidéos stables en extérieur", u"60 000"),
         (u"Disque dur externe 1 To", u"Archivage des contenus clients", u"60 000"),
         (u"Kit éclairage LED", u"Photo produit et interviews", u"55 000"),
         (u"Micro-cravate sans fil", u"Témoignages et interviews terrain", u"45 000")]
for i, (t, d, m) in enumerate(equip):
    y = 202 + i * 23
    s.rect(74, y + 6, 5, 5, fill=TURQUOISE, radius=2.5)
    s.text(t, 88, y, 210, size=8.6, font=POP, bold=True, color=TRES_FONCE)
    s.text(d, 88, y + 11, 240, size=6.8, font=POP, color=OLIVE)
    s.text(m, 372, y + 3, 78, size=8.4, font=POP, bold=True, color=VERT_FONCE, align="r")

# ---- Colonne 2 : abonnements
card(s, 488, 164, 420, 178)
s.rect(488, 164, 420, 4, fill=VERT_FONCE, radius=2)
s.text(u"ABONNEMENTS & OUTILS — 12 MOIS", 510, 180, 320, size=8, font=POP, bold=True,
       color=VERT_FONCE, spacing=1.4)
s.text(u"305 000 FCFA", 756, 179, 130, size=9.5, font=POP, bold=True,
       color=VERT_FONCE, align="r")
abos = [(ICO("pub.png"), u"Meta Business — budget publicitaire",
         u"Campagnes de test et acquisition B2B", u"150 000"),
        (ICO("site.png"), u"Hébergement + nom de domaine",
         u"Mise en ligne du site vitrine", u"60 000"),
        (ICO("canva.png"), u"Canva Pro",
         u"Marque, gabarits et exports HD", u"55 000"),
        (ICO("capcut.png"), u"CapCut Pro",
         u"Montage sans filigrane, sous-titres auto", u"40 000")]
for i, (ic, t, d, m) in enumerate(abos):
    y = 204 + i * 34
    s.image(ic, 510, y, 22, 22)
    s.text(t, 542, y, 220, size=8.8, font=POP, bold=True, color=TRES_FONCE)
    s.text(d, 542, y + 12, 240, size=6.8, font=POP, color=OLIVE)
    s.text(m, 808, y + 4, 78, size=8.4, font=POP, bold=True, color=VERT_FONCE, align="r")

# ---- Colonne 3 : formations
card(s, 52, 358, 420, 120)
s.rect(52, 358, 420, 4, fill=OLIVE, radius=2)
s.text(u"FORMATIONS PROFESSIONNELLES", 74, 374, 300, size=8, font=POP, bold=True,
       color=OLIVE, spacing=1.4)
s.text(u"275 000 FCFA", 320, 373, 130, size=9.5, font=POP, bold=True,
       color=VERT_FONCE, align="r")
forms = [(u"Analytics & data", u"Mesurer la performance, prouver le ROI client", u"100 000"),
         (u"Marketing B2B", u"Vendre à des dirigeants d'entreprise", u"100 000"),
         (u"Acquisition client", u"Prospection structurée et closing", u"75 000")]
for i, (t, d, m) in enumerate(forms):
    y = 396 + i * 26
    s.rect(74, y + 6, 5, 5, fill=OLIVE, radius=2.5)
    s.text(t, 88, y, 210, size=8.8, font=POP, bold=True, color=TRES_FONCE)
    s.text(d, 88, y + 12, 250, size=6.8, font=POP, color=OLIVE)
    s.text(m, 372, y + 4, 78, size=8.4, font=POP, bold=True, color=VERT_FONCE, align="r")

# ---- Colonne 4 : site vitrine
s.rect(488, 358, 420, 120, fill=VERT_FONCE, radius=9)
s.image(ICO("site.png"), 510, 376, 26, 26)
s.text(u"SITE VITRINE PROFESSIONNEL", 546, 378, 260, size=8, font=POP, bold=True,
       color=TURQUOISE, spacing=1.4)
s.text(u"250 000 FCFA", 756, 377, 130, size=9.5, font=POP, bold=True,
       color=BLANC, align="r")
s.text(u"Une vitrine qui présente les offres, les réalisations et les études de cas, "
       u"avec formulaire de devis — pour convertir la visibilité en demandes entrantes.",
       510, 408, 376, size=8.4, font=POP, color=GRISE, leading=1.5)
for i, tag in enumerate([u"Offres & tarifs", u"Portfolio clients", u"Formulaire de devis"]):
    x = 510 + i * 126
    s.rect(x, 448, 116, 18, fill=TURQUOISE, radius=9)
    s.text(tag, x, 452, 116, size=7, font=POP, bold=True, color=BLANC, align="c")

s.rect(52, 488, 400, 24, fill=VERT_FONCE, radius=12)
s.text(u"TOTAL DEMANDÉ : 1 850 000 FCFA", 52, 495, 400, size=9.5, font=POP,
       bold=True, color=BLANC, align="c", spacing=0.6)

# ============================================================== 23 MERCI
s = new("Merci")
s.rect(0, 0, W, H, fill=CREME)
s.rect(0, 0, W, 330, fill=VERT_FONCE)
s.poly([(700, 330), (960, 330), (960, 420), (800, 420)], fill=TURQUOISE)
dots(s, 30, 60, 6, 9, step=11, r=2.0, color=TURQUOISE, alpha=0.45, fade=True)
s.image(LOGOW, 404, 60, 152, 47)
s.text(u"Merci", 52, 132, 856, size=62, font=ALFA, color=BLANC, align="c")
s.text(u"pour votre attention !", 52, 226, 856, size=17, font=POP, color=TURQUOISE,
       align="c", spacing=1.4)
card(s, 200, 292, 560, 128, fill=BLANC)
s.text(u"Nene Halimatou Sahdiya Diallo", 200, 314, 560, size=18, font=ALFA,
       color=VERT_FONCE, align="c")
s.text(u"Fondatrice & CEO — Sadiya Digital Agri", 200, 346, 560, size=10, font=POP,
       color=OLIVE, align="c")
s.line(400, 372, 560, 372, color=GRISE_CLAIR, lw=1)
s.text(u"Dakar, Sénégal   ·   Communication digitale & agro-industrie",
       200, 386, 560, size=9.2, font=POP, color=TRES_FONCE, align="c")
s.text(u"Sadiya Digital Agri accompagne les entreprises agroalimentaires sénégalaises "
       u"pour mieux communiquer, valoriser leurs produits et développer leur visibilité "
       u"grâce au digital.",
       190, 440, 580, size=9, font=POP, color=OLIVE, align="c", leading=1.55)
footer(s, page=23)


# ------------------------------------------------------------------- BUILD
if __name__ == "__main__":
    out_pdf = os.path.join(ROOT, "Pitch_Deck_Sadiya_Digital_Agri.pdf")
    out_ppt = os.path.join(ROOT, "Pitch_Deck_Sadiya_Digital_Agri.pptx")
    render_pdf.render(SLIDES, out_pdf)
    render_pptx.render(SLIDES, out_ppt)
    print("OK %d slides" % len(SLIDES))
    for p in (out_pdf, out_ppt):
        print("  %s  %.1f Ko" % (os.path.basename(p), os.path.getsize(p) / 1024.0))
