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
    s.ellipse(636, y + 2, 9, 9, fill=c)
    s.text(u"✓" if ok else u"✕", 636, y + 3.4, 9, size=6, font=POP, bold=True,
           color=BLANC, align="c")
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

# ============================================================== 14 MODELE ECO
s = new("Modèle économique")
titlebar(s, u"Business model", u"Modèle Économique",
         u"Trois offres d'abonnement mensuel, plus des prestations à la demande.",
         page=14)
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
    y = 166 if not hl else 156
    h = 216 if not hl else 236
    card(s, x, y, 268, h, fill=VERT_FONCE if hl else BLANC,
         line=TURQUOISE if hl else GRISE_CLAIR, lw=1.6 if hl else 1.0)
    if hl:
        s.rect(x + 88, y - 11, 92, 22, fill=TURQUOISE, radius=11)
        s.text(u"RECOMMANDÉ", x + 88, y - 6, 92, size=7.4, font=POP, bold=True,
               color=BLANC, align="c", spacing=0.8)
    s.text(n, x + 22, y + 24, 220, size=11, font=POP, bold=True,
           color=TURQUOISE if hl else c, spacing=1.8)
    s.text(p, x + 22, y + 44, 220, size=30, font=ALFA, color=BLANC if hl else VERT_FONCE)
    s.text(u"FCFA / mois", x + 22, y + 86, 220, size=8.6, font=POP,
           color=GRISE if hl else OLIVE)
    s.line(x + 22, y + 108, x + 246, y + 108, color=TURQUOISE if hl else GRISE_CLAIR, lw=1)
    s.bullets(feats, x + 22, y + 122, 226, size=9.2,
              color=BLANC if hl else TRES_FONCE, gap=10, marker="check",
              mcolor=TURQUOISE if hl else VERT_FONCE)
s.rect(52, 412, 856, 62, fill=CREME, line=TURQUOISE, radius=9)
s.rect(52, 412, 5, 62, fill=SAFRAN, radius=2)
s.text(u"REVENUS COMPLÉMENTAIRES", 76, 428, 300, size=8.5, font=POP, bold=True,
       color=TURQUOISE, spacing=1.5)
s.text(u"Création de contenus à la demande, campagnes publicitaires et prestations "
       u"ponctuelles de stratégie digitale — à partir de 25 000 FCFA.",
       76, 446, 780, size=10, font=POP, color=TRES_FONCE)

# ============================================================== 15 CONCURRENCE
s = new("Marché & différenciation")
titlebar(s, u"Benchmark", u"Concurrence & Différenciation",
         u"Un marché occupé par des généralistes — aucune agence spécialisée agro.",
         page=15)
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

# ============================================================== 16 REALISATIONS
s = new("Réalisations & ambitions")
titlebar(s, u"Traction", u"Réalisations & Ambitions",
         u"Ce que j'ai déjà accompli — et où je veux aller.", page=16)
done = [(u"Formalisation de l'entreprise", u"NINEA + Registre de commerce"),
        (u"Identité visuelle Sadiya Digital Agri", u"Charte graphique + réseaux sociaux créés"),
        (u"Formation Community Management", u"7 semaines — Design & CM, Simplon Sénégal"),
        (u"Formation en agriculture", u"Licence en Agronomie — UCAD")]
goals = [u"Acquérir mes premiers clients agro-industriels",
         u"Développer un portefeuille de clients réguliers",
         u"Renforcer mon expertise en stratégie digitale",
         u"Faire de Sadiya Digital Agri une agence reconnue"]
s.rect(52, 164, 420, 30, fill=VERT_FONCE, radius=6)
s.text(u"CE QUE J'AI DÉJÀ ACCOMPLI", 72, 173, 380, size=9.5, font=POP,
       bold=True, color=TURQUOISE, spacing=1.2)
for i, (t, d) in enumerate(done):
    y = 204 + i * 58
    card(s, 52, y, 420, 50, fill=BLANC)
    s.ellipse(70, y + 16, 18, 18, fill=TURQUOISE)
    s.text(u"✓", 70, y + 20, 18, size=9, font=POP, bold=True, color=BLANC, align="c")
    s.text(t, 100, y + 11, 356, size=10.2, font=POP, bold=True, color=VERT_FONCE)
    s.text(d, 100, y + 28, 356, size=8.4, font=POP, color=OLIVE)
s.rect(488, 164, 420, 30, fill=TURQUOISE, radius=6)
s.text(u"MES OBJECTIFS (6–12 MOIS)", 508, 173, 380, size=9.5, font=POP,
       bold=True, color=BLANC, spacing=1.2)
for i, g in enumerate(goals):
    y = 204 + i * 58
    card(s, 488, y, 420, 50, fill=BLANC)
    s.rect(488, y, 4, 50, fill=SAFRAN, radius=2)
    numbadge(s, 508, y + 15, str(i + 1), d=20, fill=VERT_FONCE, size=8.5)
    s.text(g, 540, y + 18, 356, size=10.2, font=POP, bold=True, color=TRES_FONCE)

# ============================================================== 17 CTA
s = new("Appel à l'action")
s.rect(0, 0, W, H, fill=VERT_FONCE)
s.rect(0, 0, 6, H, fill=TURQUOISE)
dots(s, 856, 60, 8, 8, step=11, r=2.0, color=TURQUOISE, alpha=0.5, fade=True)
s.poly([(0, 470), (200, 470), (140, 540), (0, 540)], fill=TURQUOISE, alpha=0.25)
s.rect(52, 44, 3.5, 13, fill=TURQUOISE)
s.text(u"CE DONT J'AI BESOIN", 63, 44, 400, size=8.5, font=POP, bold=True,
       color=TURQUOISE, spacing=1.9)
s.text(u"Appel à l'Action", 52, 62, 600, size=34, font=ALFA, color=BLANC)
s.text(u"De quoi ai-je besoin pour faire grandir Sadiya Digital Agri ?",
       52, 116, 620, size=12, font=POP, color=GRISE)
s.image(LOGOW, 830, 40, 92, 28)
needs = [(u"Financement", u"Amorcer la production\net les campagnes"),
         (u"Accompagnement", u"Mentorat business\net structuration"),
         (u"Partenariat", u"Accès aux réseaux\nagro-industriels"),
         (u"Équipements", u"Matériel de captation\nphoto et vidéo"),
         (u"Visibilité", u"Références et\nrecommandations"),
         (u"Formation", u"Publicité en ligne\net stratégie avancée")]
for i, (t, d) in enumerate(needs):
    x = 52 + (i % 3) * 288
    y = 168 + (i // 3) * 118
    s.rect(x, y, 268, 100, fill=BLANC, alpha=0.08, radius=9)
    s.rect(x, y, 4, 100, fill=TURQUOISE, radius=2)
    s.text(t, x + 24, y + 22, 220, size=14, font=POP, bold=True, color=BLANC)
    s.text(d, x + 24, y + 48, 226, size=9, font=POP, color=GRISE, leading=1.45)
s.text(u"« Avec votre soutien, mon activité peut créer plus d'impact "
       u"et d'opportunités. »",
       52, 434, 856, size=13, font=ALFA, color=TURQUOISE, align="c")
footer(s, dark=True, page=17)

# ============================================================== 18 MERCI
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
footer(s, page=18)


# ------------------------------------------------------------------- BUILD
if __name__ == "__main__":
    out_pdf = os.path.join(ROOT, "Pitch_Deck_Sadiya_Digital_Agri.pdf")
    out_ppt = os.path.join(ROOT, "Pitch_Deck_Sadiya_Digital_Agri.pptx")
    render_pdf.render(SLIDES, out_pdf)
    render_pptx.render(SLIDES, out_ppt)
    print("OK %d slides" % len(SLIDES))
    for p in (out_pdf, out_ppt):
        print("  %s  %.1f Ko" % (os.path.basename(p), os.path.getsize(p) / 1024.0))
