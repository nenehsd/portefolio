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


def footer(s, dark=False, page=None, logos=False, mention=False):
    """Pied de page : pagination seule. La mention et les logos partenaires
    ne figurent que sur la couverture et la slide de remerciement."""
    col = BLANC if dark else VERT_FONCE
    if mention:
        s.text(u"Programme de Pré-incubation 2026 de la\nfabrique 360 de Simplon Sénégal",
               620, 500, 200, size=6.8, font=POP, color=GRISE, leading=1.35, align="r")
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

# ============================================================== 02 CONTEXTE & PROBLEMATIQUE
s = new(u"Contexte & Problématique")
titlebar(s, u"Point de départ", u"Contexte & Problématique",
         u"Un secteur qui produit beaucoup, mais qui se vend mal en ligne.", page=2)

# --- Le contexte, en 3 reperes chiffres
s.text(u"LE CONTEXTE — UN MARCHÉ PORTEUR", 52, 168, 500, size=10, font=POP,
       bold=True, color=TURQUOISE, spacing=1.6)
ctx = [(u"11,5 M", u"utilisateurs internet", u"60,6 % de pénétration, fin 2025", TURQUOISE),
       (u"5,42 M", u"identités sur les réseaux", u"28,5 % de la population, fin 2025", VERT_FONCE),
       (u"63 %", u"des PMI industrielles", u"évoluent dans l'agroalimentaire", OLIVE)]
for i, (big, lbl, sub, c) in enumerate(ctx):
    x = 52 + i * 288
    card(s, x, 190, 268, 104)
    s.rect(x, 190, 268, 4, fill=c, radius=2)
    s.text(big, x + 22, 204, 226, size=26, font=ALFA, color=c)
    s.text(lbl, x + 22, 242, 230, size=11.5, font=POP, bold=True, color=VERT_FONCE)
    s.text(sub, x + 22, 262, 230, size=9.2, font=POP, color=OLIVE, leading=1.35)
s.rect(52, 304, 856, 32, fill=TURQUOISE, alpha=0.13, radius=8)
s.text(u"Les Sénégalais passent en moyenne 2 h 24 par jour sur les réseaux sociaux.",
       52, 314, 856, size=11.5, font=POP, bold=True, color=VERT_FONCE, align="c")

s.text(u"LA PROBLÉMATIQUE", 52, 344, 400, size=10, font=POP, bold=True,
       color=SAFRAN, spacing=1.6)
pbs = [(u"01", u"Présence faible", u"Des pages inactives, peu de contenu."),
       (u"02", u"Pas de stratégie", u"On publie sans objectif ni calendrier."),
       (u"03", u"Aucune conversion", u"De la visibilité, mais pas de clients.")]
for i, (n, t, d) in enumerate(pbs):
    x = 52 + i * 288
    card(s, x, 366, 268, 82)
    s.rect(x, 366, 4, 82, fill=SAFRAN, radius=2)
    numbadge(s, x + 22, 381, n, d=24, fill=SAFRAN, tcol=TRES_FONCE, size=10)
    s.text(t, x + 56, 385, 200, size=13.5, font=POP, bold=True, color=VERT_FONCE)
    s.text(d, x + 22, 417, 230, size=10.2, font=POP, color=TRES_FONCE, leading=1.4)

s.rect(52, 460, 856, 32, fill=VERT_FONCE, radius=8)
s.text(u"Des produits de qualité restent invisibles pendant que les marques "
       u"importées occupent le terrain.",
       52, 470, 856, size=11.5, font=POP, bold=True, color=BLANC, align="c")

# ============================================================== 03 ACCROCHE (interrogation)
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

# ============================================================== 04 LA SOLUTION
s = new(u"La Solution")
s.rect(0, 0, W, H, fill=CREME)
s.rect(0, 0, 6, H, fill=VERT_FONCE)
s.poly([(700, 0), (960, 0), (960, 88), (798, 88)], fill=TURQUOISE)
dots(s, 872, 372, 6, 7, step=12, r=2.1, color=VERT_FONCE, alpha=0.5, fade=True)

s.rect(52, 44, 3.5, 13, fill=TURQUOISE)
s.text(u"NOTRE RÉPONSE", 63, 44, 400, size=9, font=POP, bold=True,
       color=TURQUOISE, spacing=1.9)
s.text(u"La Solution", 52, 62, 500, size=40, font=ALFA, color=VERT_FONCE)

# --- Le logo, mis en avant dans un bloc dedie
s.rect(52, 132, 380, 150, fill=BLANC, line=GRISE_CLAIR, radius=12)
s.rect(52, 132, 380, 5, fill=TURQUOISE, radius=2)
s.image(LOGO, 96, 162, 292, 118)

# --- La promesse
s.rect(456, 132, 452, 150, fill=VERT_FONCE, radius=12)
s.text(u"Une agence de community\nmanagement spécialisée dans\nl'agro-industrie sénégalaise.",
       484, 162, 400, size=17.5, font=POP, bold=True, color=BLANC, leading=1.4)
s.rect(484, 244, 60, 3.5, fill=TURQUOISE)

# --- Les 3 services
srv = [(u"Stratégie\nSocial Media", u"Objectifs, réseaux et ligne éditoriale", TURQUOISE),
       (u"Création\nde Contenu", u"Visuels, carrousels et vidéos courtes", VERT_FONCE),
       (u"Gestion de\nCommunauté", u"Animation, modération et relation client", OLIVE)]
for i, (t, d, c) in enumerate(srv):
    x = 52 + i * 288
    card(s, x, 306, 268, 122)
    s.rect(x, 306, 268, 4, fill=c, radius=2)
    checkmark(s, x + 22, 326, 22, fill=c)
    s.text(t.replace("\n", " "), x + 54, 328, 200, size=14.5, font=POP, bold=True,
           color=VERT_FONCE, leading=1.25)
    s.text(d, x + 22, 384, 230, size=10.5, font=POP, color=TRES_FONCE, leading=1.4)

s.rect(52, 448, 856, 42, fill=TURQUOISE, radius=9)
s.text(u"La double expertise agriculture + digital, unique sur ce marché.",
       52, 461, 856, size=13, font=POP, bold=True, color=BLANC, align="c")
footer(s, page=4)

# ============================================================== 05 MARCHE CIBLE
s = new("Notre marché cible")
s.rect(0, 0, W, H, fill=BLANC)
s.rect(0, 0, W, 92, fill=CREME)
s.rect(0, 92, W, 448, fill="E4EEE6")
s.text(u"NOTRE MARCHÉ CIBLE", 52, 28, 600, size=26, font=ALFA, color=TRES_FONCE)
s.text(u"Un marché 100 % B2B au cœur de l'agroalimentaire sénégalais",
       178, 64, 640, size=13, font=POP, color=OLIVE)
s.image(LOGO, 848, 26, 74, 30)
# noyau central
s.rect(310, 132, 340, 152, fill=VERT_FONCE, radius=13)
s.text(u"SADIYA DIGITAL AGRI", 310, 148, 340, size=10.5, font=POP, bold=True,
       color=BLANC, align="c", spacing=1.3)
s.text(u"Digitaliser la visibilité\net la commercialisation", 320, 174, 320,
       size=18.5, font=ALFA, color=BLANC, align="c", leading=1.25)
s.text(u"des acteurs agroalimentaires sénégalais", 320, 246, 320, size=9,
       font=POP, color=GRISE, align="c")

segs = [
    (u"PRODUCTEURS", u"cible_producteur.jpg", 52, 160, 232),
    (u"ACHETEURS PRO", u"cible_acheteur.jpg", 676, 160, 232),
    (u"TRANSFORMATEURS", u"cible_transformateur.jpg", 62, 336, 226),
    (u"GIE & COOPÉRATIVES", u"cible_gie.jpg", 366, 360, 228),
    (u"DISTRIBUTEURS", u"cible_distributeur.jpg", 672, 336, 232),
]
for t, photo, x, y, w in segs:
    card(s, x, y, w, 84, fill=BLANC, line=TURQUOISE, radius=10, lw=0.9)
    s.image(IM(photo), x + 12, y + 12, 60, 60)
    s.text(t, x + 84, y + 34, w - 96, size=12.5, font=POP, bold=True,
           color=VERT_FONCE, leading=1.2)
for (x, y) in [(284, 202), (676, 202), (288, 366), (480, 374), (672, 366)]:
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
    s.ellipse(x + 22, y + 26, 44, 44, fill=c, alpha=0.14)
    s.text(l, x + 22, y + 39, 44, size=17 if len(l) < 3 else 12, font=ALFA,
           color=c, align="c")
    s.text(t, x + 78, y + 30, 180, size=17, font=POP, bold=True, color=VERT_FONCE)
    s.text(d, x + 78, y + 56, 186, size=11, font=POP, color=OLIVE, leading=1.4)

# ============================================================== 07 TARGET
s = new("T — Target")
titlebar(s, u"T · Target", u"À qui nous adressons-nous ?",
         u"Un marché B2B concentré, identifiable et joignable directement en ligne.",
         page=7)
# --- Persona principal, seul sujet de la page
s.rect(52, 170, 856, 250, fill=VERT_FONCE, radius=12)
s.image(IM("persona_aminata.jpg"), 94, 204, 132, 132)

s.text(u"PERSONA PRINCIPAL", 262, 202, 400, size=10, font=POP, bold=True,
       color=TURQUOISE, spacing=1.8)
s.text(u"Aminata, 36 ans", 262, 224, 560, size=32, font=ALFA, color=BLANC)
s.rect(262, 274, 64, 3.5, fill=TURQUOISE)
s.text(u"Directrice générale d'une PME de transformation de fruits "
       u"et légumes à Dakar.",
       262, 292, 600, size=14, font=POP, color=BLANC, leading=1.45)

per = [(u"Besoin", u"Faire connaître ses gammes de jus locaux", TURQUOISE),
       (u"Frein", u"Manque de temps et d'expertise interne", TURQUOISE),
       (u"Réseaux", u"LinkedIn · Facebook · TikTok", TURQUOISE)]
for i, (k, v, c) in enumerate(per):
    bx = 96 + i * 276
    s.rect(bx, 344, 256, 56, fill=BLANC, alpha=0.10, radius=8)
    s.rect(bx, 344, 3.5, 56, fill=c, radius=1.75)
    s.text(k.upper(), bx + 18, 356, 220, size=8.6, font=POP, bold=True,
           color=TURQUOISE, spacing=1.4)
    s.text(v, bx + 18, 372, 226, size=11, font=POP, color=BLANC, leading=1.3)

s.text(u"« De bons produits locaux, mais ni le temps ni les compétences "
       u"pour les rendre visibles. »",
       52, 446, 856, size=14, font=ALFA, color=VERT_FONCE, align="c")

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
    card(s, x, 166, 268, 212)
    s.rect(x, 166, 268, 5, fill=c, radius=2)
    s.text(t, x + 22, 194, 220, size=11.5, font=POP, bold=True, color=c, spacing=1.5)
    s.text(big, x + 22, 218, 220, size=50, font=ALFA, color=VERT_FONCE)
    s.text(unit, x + 22, 284, 220, size=12, font=POP, bold=True, color=OLIVE)
    s.line(x + 22, 316, x + 246, 316, color=GRISE_CLAIR, lw=1)
    s.rect(x + 22, 334, 96, 26, fill=c, radius=13)
    s.text(ech, x + 22, 341, 96, size=10, font=POP, bold=True,
           color=BLANC, align="c")
s.rect(52, 412, 856, 52, fill=VERT_FONCE, radius=9)
s.text(u"Visibilité  ›  Engagement  ›  Prospects  ›  Clients",
       52, 428, 856, size=17, font=POP, bold=True, color=TURQUOISE, align="c",
       spacing=0.8)

# ============================================================== 09 MESSAGE
s = new("M — Message")
titlebar(s, u"M · Message", u"Qu'est-ce que je veux dire ?",
         u"Un positionnement clair, une proposition de valeur unique, un ton reconnaissable.",
         page=9)
s.rect(52, 166, 546, 108, fill=VERT_FONCE, radius=10)
s.text(u"PROPOSITION DE VALEUR", 76, 182, 300, size=10, font=POP, bold=True,
       color=TURQUOISE, spacing=1.6)
s.text(u"« Rendre les produits locaux sénégalais aussi visibles\n"
       u"en ligne qu'ils le sont dans les rayons. »",
       76, 204, 500, size=16, font=ALFA, color=BLANC, leading=1.32)
card(s, 614, 166, 294, 108)
s.rect(614, 166, 4, 108, fill=SAFRAN, radius=2)
s.text(u"POSITIONNEMENT", 636, 182, 250, size=10, font=POP, bold=True,
       color=OLIVE, spacing=1.6)
s.text(u"L'agence qui combine expertise agricole et maîtrise digitale "
       u"au service de l'agroalimentaire.",
       636, 204, 252, size=11, font=POP, color=TRES_FONCE, leading=1.55)
s.text(u"NOS MESSAGES CLÉS", 52, 296, 400, size=10, font=POP, bold=True,
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
    s.text(m, 90, y + 12, 496, size=11, font=POP, color=TRES_FONCE)
card(s, 614, 296, 294, 182)
s.text(u"TON DE VOIX", 636, 314, 250, size=10, font=POP, bold=True,
       color=OLIVE, spacing=1.6)
for i, w_ in enumerate([u"Professionnel", u"Chaleureux",
                        u"Pédagogique", u"Dynamique"]):
    y = 342 + i * 34
    checkmark(s, 636, y, 20, fill=TURQUOISE)
    s.text(w_, 666, y + 3, 230, size=13, font=POP, bold=True, color=TRES_FONCE)

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
    card(s, x, 170, 268, 152)
    s.rect(x, 170, 268, 5, fill=c, radius=2)
    s.text(n, x + 22, 196, 220, size=23, font=ALFA, color=VERT_FONCE)
    s.text(r, x + 22, 234, 220, size=11, font=POP, bold=True, color=c, spacing=1.1)
    s.line(x + 22, 260, x + 246, 260, color=GRISE_CLAIR, lw=1)
    s.rect(x + 22, 278, 92, 26, fill=c, radius=13)
    s.text(step, x + 22, 285, 92, size=11, font=POP, bold=True, color=BLANC, align="c")
    if i < 2:
        s.text(u"›", x + 272, 222, 16, size=22, font=POP, bold=True, color=GRISE, align="c")
s.rect(52, 348, 856, 54, fill=VERT_FONCE, radius=9)
s.text(u"PARCOURS", 76, 367, 90, size=9, font=POP, bold=True, color=TURQUOISE, spacing=1.4)
s.text(u"TikTok attire  ›  Facebook fédère  ›  LinkedIn crédibilise  ›  convertir",
       172, 365, 720, size=13.5, font=POP, bold=True, color=BLANC)
piliers = [u"🌱 Éducation", u"🚜 Valorisation", u"📱 Expertise", u"💼 Offres", u"🤝 Communauté"]
s.text(u"5 PILIERS ÉDITORIAUX", 52, 420, 300, size=10, font=POP, bold=True,
       color=OLIVE, spacing=1.5)
for i, p in enumerate(piliers):
    x = 52 + i * 172
    s.rect(x, 442, 160, 32, fill=BLANC, line=GRISE_CLAIR, radius=16)
    s.text(p.split(" ", 1)[1], x, 451, 160, size=11, font=POP, bold=True,
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
    s.text(lbl, x, 174, w_, size=9, font=POP, bold=True, color=TURQUOISE, spacing=1.2)
for i, (d, r, ct, ob, c) in enumerate(rows):
    y = 200 + i * 46
    s.rect(52, y, 546, 40, fill=BLANC if i % 2 == 0 else CREME,
           line=GRISE_CLAIR, radius=5)
    s.rect(52, y, 4, 40, fill=c, radius=2)
    s.text(d, 68, y + 13, 90, size=11.5, font=POP, bold=True, color=VERT_FONCE)
    s.text(r, 158, y + 13, 150, size=10.5, font=POP, color=TRES_FONCE)
    s.text(ct, 308, y + 13, 180, size=10.5, font=POP, color=TRES_FONCE)
    s.rect(488, y + 10, 84, 20, fill=c, radius=10)
    s.text(ob, 488, y + 14, 84, size=9, font=POP, bold=True, color=BLANC, align="c")
s.text(u"ANIMATION DE LA COMMUNAUTÉ", 52, 358, 400, size=10, font=POP, bold=True,
       color=OLIVE, spacing=1.5)
anim = [(u"2-3", u"stories / sem."), (u"1", u"sondage / sem."),
        (u"2", u"Q&R / mois"), (u"1", u"live / mois"), (u"1-2", u"défis TikTok")]
for i, (n, l) in enumerate(anim):
    x = 52 + i * 111
    s.rect(x, 378, 100, 52, fill=BLANC, line=GRISE_CLAIR, radius=7)
    s.text(n, x, 386, 100, size=19, font=ALFA, color=TURQUOISE, align="c")
    s.text(l, x + 4, 414, 92, size=8.6, font=POP, color=OLIVE, align="c")
card(s, 614, 168, 294, 262)
s.rect(614, 168, 294, 4, fill=TURQUOISE, radius=2)
s.text(u"MOYENS MOBILISÉS", 636, 188, 250, size=10, font=POP, bold=True,
       color=VERT_FONCE, spacing=1.5)
tools = [u"Canva Free", u"CapCut", u"Meta Business Suite", u"TikTok Studio",
         u"LinkedIn", u"Google Drive", u"Google Sheets"]
for i, t in enumerate(tools):
    y = 214 + i * 30
    s.rect(636, y + 5, 6, 6, fill=TURQUOISE, radius=3)
    s.text(t, 654, y, 240, size=12, font=POP, bold=True, color=TRES_FONCE)

# ============================================================== 12 EXECUTION
s = new("E — Execution")
titlebar(s, u"E · Execution", u"Comment je produis et j'anime ?",
         u"Une production organisée, une modération cadrée, une relation client rapide.",
         page=12)
blocks = [
    (u"01", u"Production", TURQUOISE,
     [u"Thèmes définis en début de mois",
      u"Contenus créés en avance",
      u"Programmation Meta Suite & TikTok"]),
    (u"02", u"Modération", VERT_FONCE,
     [u"Ton professionnel et respectueux",
      u"Critiques constructives conservées",
      u"Réclamations traitées en privé"]),
    (u"03", u"Relation client", OLIVE,
     [u"Surveillance quotidienne",
      u"Réponse sous 24 h ouvrées",
      u"Demandes commerciales en privé"]),
]
for i, (n, t, c, its) in enumerate(blocks):
    x = 52 + i * 288
    card(s, x, 166, 268, 190)
    s.rect(x, 166, 268, 4, fill=c, radius=2)
    numbadge(s, x + 22, 188, n, d=24, fill=c, size=10)
    s.text(t, x + 56, 192, 210, size=14, font=POP, bold=True, color=VERT_FONCE)
    s.bullets(its, x + 22, 238, 232, size=11, color=TRES_FONCE, gap=11,
              marker="dot", mcolor=c, leading=1.4)
s.rect(52, 374, 856, 104, fill=VERT_FONCE, radius=10)
s.text(u"PLAN BAD BUZZ", 76, 392, 200, size=10, font=POP, bold=True,
       color=TURQUOISE, spacing=1.6)
steps = [u"Identifier", u"Vérifier", u"Répondre", u"Traiter", u"Suivre", u"Tirer les leçons"]
for i, st in enumerate(steps):
    x = 76 + i * 136
    s.ellipse(x, 412, 22, 22, fill=TURQUOISE, alpha=0.22)
    s.text(str(i + 1), x, 418, 22, size=9, font=POP, bold=True, color=TURQUOISE, align="c")
    s.text(st, x + 30, 417, 106, size=10.5, font=POP, bold=True, color=BLANC)
    if i < 5:
        s.line(x + 108, 423, x + 128, 423, color=TURQUOISE, lw=0.8, alpha=0.5)
s.text(u"Règle d'or : ne jamais répondre sous le coup de l'émotion.",
       76, 450, 700, size=11, font=POP, italic=True, color=GRISE)

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
    s.text(t, 76, y + 11, 160, size=14.5, font=POP, bold=True, color=VERT_FONCE)
    s.text(k, 76, y + 35, 310, size=10, font=POP, color=TRES_FONCE)
    s.text(o, 392, y + 13, 200, size=9.4, font=POP, color=OLIVE, leading=1.4)
    s.rect(392, y + 38, 96, 18, fill=c, radius=9)
    s.text(f, 392, y + 41, 96, size=8.4, font=POP, bold=True, color=BLANC, align="c")
card(s, 614, 168, 294, 234)
s.rect(614, 168, 294, 4, fill=SAFRAN, radius=2)
s.text(u"BOUCLE D'AMÉLIORATION", 636, 188, 250, size=10, font=POP, bold=True,
       color=VERT_FONCE, spacing=1.4)
cycle = [u"Publier", u"Mesurer", u"Analyser", u"Ajuster", u"Améliorer"]
for i, cst in enumerate(cycle):
    y = 214 + i * 36
    s.ellipse(636, y, 24, 24, fill=TURQUOISE if i % 2 == 0 else VERT_FONCE)
    s.text(str(i + 1), 636, y + 7, 24, size=9, font=POP, bold=True, color=BLANC, align="c")
    s.text(cst, 672, y + 5, 200, size=12.5, font=POP, bold=True, color=TRES_FONCE)
    if i < 4:
        s.line(648, y + 26, 648, y + 34, color=GRISE, lw=1.2)
s.rect(52, 420, 546, 58, fill=VERT_FONCE, radius=9)
s.text(u"Chaque semaine : identifier les contenus performants.\n"
       u"Chaque mois : comparer aux objectifs et ajuster.",
       76, 436, 500, size=11.5, font=POP, color=BLANC, leading=1.45)

# ============================================================== 14 OFFRES
s = new(u"Nos offres")
titlebar(s, u"Business model", u"Nos Offres d'Abonnement",
         u"Trois formules mensuelles, plus des prestations à la demande.",
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
    y = 172 if not hl else 162
    h = 208 if not hl else 228
    card(s, x, y, 268, h, fill=VERT_FONCE if hl else BLANC,
         line=TURQUOISE if hl else GRISE_CLAIR, lw=1.6 if hl else 1.0)
    if hl:
        s.rect(x + 88, y - 11, 92, 22, fill=TURQUOISE, radius=11)
        s.text(u"RECOMMANDÉ", x + 88, y - 6, 92, size=7.4, font=POP, bold=True,
               color=BLANC, align="c", spacing=0.8)
    s.text(n, x + 22, y + 22, 220, size=12, font=POP, bold=True,
           color=TURQUOISE if hl else c, spacing=1.8)
    s.text(p, x + 22, y + 44, 220, size=33, font=ALFA, color=BLANC if hl else VERT_FONCE)
    s.text(u"FCFA / mois", x + 22, y + 90, 220, size=10, font=POP,
           color=GRISE if hl else OLIVE)
    s.line(x + 22, y + 104, x + 246, y + 104, color=TURQUOISE if hl else GRISE_CLAIR, lw=1)
    s.bullets(feats, x + 22, y + 122, 230, size=11,
              color=BLANC if hl else TRES_FONCE, gap=12, marker="check",
              mcolor=TURQUOISE if hl else VERT_FONCE)
s.rect(52, 404, 856, 44, fill=CREME, line=TURQUOISE, radius=9)
s.rect(52, 404, 5, 44, fill=SAFRAN, radius=2)
s.text(u"REVENUS COMPLÉMENTAIRES", 76, 411, 300, size=9, font=POP, bold=True,
       color=TURQUOISE, spacing=1.5)
s.text(u"Contenus à la demande, publicité et stratégie ponctuelle — dès 25 000 FCFA.",
       76, 427, 780, size=11, font=POP, color=TRES_FONCE)
s.text(u"Paiement mensuel d'avance  ·  engagement 3 mois minimum",
       52, 462, 856, size=10, font=POP, italic=True, color=OLIVE, align="c")

# ============================================================== 15 PROJECTIONS
s = new(u"Rentabilité & projections")
titlebar(s, u"Business model", u"Rentabilité & Projections",
         u"Un point mort atteignable dès le troisième client régulier.",
         page=15)
kpis = [(u"85 000", u"FCFA", u"Charges mensuelles estimées", OLIVE),
        (u"3", u"clients", u"Seuil de rentabilité (offre Pro)", TURQUOISE),
        (u"450 000", u"FCFA", u"Revenu mensuel visé à 6 mois", VERT_FONCE),
        (u"5,4 M", u"FCFA", u"Chiffre d'affaires annualisé cible", TURQUOISE)]
for i, (big, unit, lbl, c) in enumerate(kpis):
    x = 52 + i * 216
    card(s, x, 166, 196, 104)
    s.rect(x, 166, 196, 4, fill=c, radius=2)
    s.text(big, x + 18, 188, 164, size=27, font=ALFA, color=VERT_FONCE)
    s.text(unit, x + 18, 226, 160, size=9.5, font=POP, bold=True, color=c)
    s.text(lbl, x + 18, 244, 168, size=9.2, font=POP, color=OLIVE, leading=1.35)
# scenario de montee en charge
s.text(u"SCÉNARIO DE MONTÉE EN CHARGE", 52, 292, 400, size=10, font=POP, bold=True,
       color=OLIVE, spacing=1.5)
scen = [(u"Mois 1–3", u"2 clients", u"150 000", 0.28, GRISE),
        (u"Mois 4–6", u"3 clients", u"450 000", 0.62, TURQUOISE),
        (u"Mois 7–12", u"5 clients", u"750 000", 1.0, VERT_FONCE)]
for i, (per, cl, rev, frac, c) in enumerate(scen):
    y = 316 + i * 46
    s.text(per, 52, y + 11, 84, size=11, font=POP, bold=True, color=TRES_FONCE)
    s.text(cl, 142, y + 11, 70, size=10.5, font=POP, color=OLIVE)
    s.rect(208, y + 8, 292, 22, fill=GRISE_CLAIR, radius=11)
    s.rect(208, y + 8, 292 * frac, 22, fill=c, radius=11)
    s.text(rev + u" FCFA/mois", 508, y + 11, 176, size=10.5, font=POP, bold=True,
           color=VERT_FONCE)
card(s, 700, 292, 208, 172)
s.rect(700, 292, 208, 4, fill=SAFRAN, radius=2)
s.text(u"CHARGES PRINCIPALES", 718, 308, 180, size=9, font=POP, bold=True,
       color=VERT_FONCE, spacing=1.3)
charges = [(u"Connexion internet", u"25 000"), (u"Déplacements terrain", u"20 000"),
           (u"Outils & abonnements", u"20 000"), (u"Divers & imprévus", u"20 000")]
for i, (k, v) in enumerate(charges):
    y = 330 + i * 26
    s.text(k, 718, y, 132, size=9.4, font=POP, color=TRES_FONCE)
    s.text(v, 826, y, 64, size=9.4, font=POP, bold=True, color=OLIVE, align="r")
s.line(718, 434, 890, 434, color=GRISE_CLAIR, lw=1)
s.text(u"Total", 718, 442, 100, size=10, font=POP, bold=True, color=VERT_FONCE)
s.text(u"85 000 FCFA", 786, 442, 104, size=10, font=POP, bold=True,
       color=TURQUOISE, align="r")
s.text(u"Hypothèses prudentes : outils gratuits, structure sans salarié.",
       52, 482, 640, size=9.4, font=POP, italic=True, color=OLIVE)

# ============================================================== 16 BENCHMARKING
s = new(u"Benchmarking")
titlebar(s, u"Benchmarking", u"Ce Que J'ai de Plus Qu'Eux",
         u"Comparaison sur les cinq critères qui comptent pour une PME agroalimentaire.",
         page=16)

cols = [(u"Sadiya Digital Agri", u"75 000 – 250 000 FCFA/mois", TURQUOISE, True),
        (u"Agences établies", u"130 000 – 600 000 FCFA/mois", GRISE, False),
        (u"CM freelance", u"50 000 – 150 000 FCFA/mois", GRISE, False)]
crit = [(u"Expertise agricole", 2, 0, 0),
        (u"Spécialisation agro", 2, 0, 0),
        (u"Tarifs adaptés aux PME", 2, 0, 1),
        (u"Stratégie structurée", 2, 2, 0),
        (u"Reporting et mesure", 2, 2, 0)]

LX, LW = 52, 300
CW, CG = 172, 16
CX = LX + LW + 12

# --- En-tetes de colonnes
for i, (nom, prix, c, hl) in enumerate(cols):
    x = CX + i * (CW + CG)
    s.rect(x, 160, CW, 56, fill=VERT_FONCE if hl else BLANC,
           line=None if hl else GRISE_CLAIR, radius=8)
    s.text(nom, x + 8, 172, CW - 16, size=11.5, font=POP,
           bold=True, color=BLANC if hl else OLIVE, align="c", leading=1.2)
    s.text(prix, x + 8, 192, CW - 16, size=7.6, font=POP,
           color=TURQUOISE if hl else OLIVE, align="c")

# --- Lignes de criteres
for j, (lbl, a, b, cc) in enumerate(crit):
    y = 226 + j * 44
    s.rect(LX, y, LW, 38, fill=BLANC, line=GRISE_CLAIR, radius=7)
    s.text(lbl, LX + 18, y + 12, LW - 30, size=11.5, font=POP, bold=True,
           color=TRES_FONCE)
    for i, val in enumerate((a, b, cc)):
        x = CX + i * (CW + CG)
        hl = (i == 0)
        s.rect(x, y, CW, 38, fill="E9F5EE" if hl else BLANC,
               line=TURQUOISE if hl else GRISE_CLAIR, radius=7,
               lw=1.4 if hl else 1.0)
        cx = x + CW / 2.0 - 11
        if val == 2:
            checkmark(s, cx, y + 8, 22, fill=TURQUOISE if hl else VERT_FONCE)
        elif val == 1:
            s.ellipse(cx, y + 8, 22, 22, fill=GRISE)
            s.rect(cx + 5.5, y + 18, 11, 2.6, fill=BLANC, radius=1.3)
        else:
            s.ellipse(cx, y + 8, 22, 22, fill="D8DEDA")
            s.line(cx + 6.6, y + 14.6, cx + 15.4, y + 23.4, color=BLANC, lw=2)
            s.line(cx + 15.4, y + 14.6, cx + 6.6, y + 23.4, color=BLANC, lw=2)

s.rect(52, 452, 856, 40, fill=VERT_FONCE, radius=9)
s.text(u"Seule offre du marché à combiner expertise agronomique et maîtrise digitale.",
       52, 464, 856, size=12.5, font=POP, bold=True, color=BLANC, align="c")

# ============================================================== 17 REALISATIONS — identite
s = new(u"Réalisations — identité de marque")
titlebar(s, u"Traction", u"Ce que j'ai déjà réalisé",
         u"Une marque complète, construite de A à Z : logo, charte, bannière et carte de visite.",
         page=17)
# logo
card(s, 52, 168, 268, 152)
s.rect(52, 168, 268, 4, fill=TURQUOISE, radius=2)
s.text(u"LOGO", 74, 184, 200, size=9.5, font=POP, bold=True, color=TURQUOISE, spacing=1.5)
s.image(LOGO, 88, 208, 196, 79)
s.text(u"Version horizontale couleur", 74, 296, 224, size=9.4, font=POP, color=OLIVE)
# palette
card(s, 336, 168, 268, 152)
s.rect(336, 168, 268, 4, fill=VERT_FONCE, radius=2)
s.text(u"PALETTE", 358, 184, 200, size=9.5, font=POP, bold=True, color=VERT_FONCE, spacing=1.5)
pal = [(VERT_FONCE, u"#1F5E3A"), (TURQUOISE, u"#1AAB70"), (OLIVE, u"#42612D"),
       (GRISE, u"#9FB8A2"), (TRES_FONCE, u"#0A1A01"), (BLANC, u"#FFFFFF")]
for i, (c, code) in enumerate(pal):
    x = 358 + (i % 3) * 78
    y = 204 + (i // 3) * 48
    s.rect(x, y, 62, 32, fill=c, line=GRISE_CLAIR if c == BLANC else None, radius=6)
    s.text(code, x, y + 34, 62, size=6.2, font=POP, color=OLIVE, align="c")
s.text(u"6 couleurs officielles", 358, 302, 224, size=9.4, font=POP, color=OLIVE)
# typographie
card(s, 620, 168, 288, 152)
s.rect(620, 168, 288, 4, fill=OLIVE, radius=2)
s.text(u"TYPOGRAPHIE", 642, 184, 200, size=9.5, font=POP, bold=True, color=OLIVE, spacing=1.5)
s.text(u"Sadiya", 642, 204, 240, size=22, font=ALFA, color=VERT_FONCE)
s.text(u"Alfa Slab One — titres", 642, 238, 240, size=9, font=POP, color=OLIVE)
s.text(u"Digital Agri", 642, 252, 240, size=17, font=POP, bold=True, color=TURQUOISE)
s.text(u"Poppins — sous-titres et textes", 642, 282, 240, size=9, font=POP, color=OLIVE)
s.text(u"Hiérarchie à 3 niveaux", 642, 302, 240, size=9.4, font=POP, color=OLIVE)
# banniere
card(s, 52, 336, 552, 130)
s.rect(52, 336, 552, 4, fill=TURQUOISE, radius=2)
s.text(u"BANNIÈRE RÉSEAUX SOCIAUX", 74, 352, 300, size=9.5, font=POP, bold=True,
       color=TURQUOISE, spacing=1.5)
s.image(IM("banniere.png"), 74, 372, 508, 82)
# carte de visite
card(s, 620, 336, 288, 130)
s.rect(620, 336, 288, 4, fill=VERT_FONCE, radius=2)
s.text(u"CARTE DE VISITE", 642, 352, 250, size=9.5, font=POP, bold=True,
       color=VERT_FONCE, spacing=1.5)
s.image(IM("carte_visite.png"), 642, 374, 244, 68)

# ============================================================== 18 REALISATIONS — presence digitale
s = new(u"Réalisations — présence digitale & outils")
titlebar(s, u"Traction", u"Présence Digitale & Outils Maîtrisés",
         u"Des canaux actifs, un site portfolio en ligne et une gestion de projet outillée.",
         page=18)
ICO = lambda n: os.path.join(IMG, "tools", n)
SOC = os.path.join(ROOT, "assets", "img", "icons")

# --- Canaux en ligne
s.text(u"CANAUX EN LIGNE", 52, 164, 400, size=10, font=POP, bold=True,
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
    s.text(t, x + 18, 250, 168, size=11.5, font=POP, bold=True, color=VERT_FONCE)
    s.rect(x + 18, 274, 68, 19, fill=TURQUOISE, radius=9.5)
    s.text(st, x + 18, 278, 68, size=8.4, font=POP, bold=True, color=BLANC, align="c")

# --- Autres reseaux
s.text(u"AUSSI PRÉSENTE SUR", 52, 320, 300, size=9.5, font=POP, bold=True,
       color=OLIVE, spacing=1.4)
for i, (f, lbl) in enumerate([("instagram.png", u"Instagram"), ("tiktok.png", u"TikTok"),
                              ("whatsapp.png", u"WhatsApp Business"), ("email.png", u"Email pro")]):
    x = 52 + i * 108
    s.rect(x, 340, 96, 30, fill=BLANC, line=GRISE_CLAIR, radius=15)
    s.image(os.path.join(SOC, f), x + 9, 347, 16, 16)
    s.text(lbl, x + 30, 349, 64, size=8, font=POP, bold=True, color=VERT_FONCE)

# --- Outils maitrises
s.text(u"OUTILS MAÎTRISÉS", 52, 388, 300, size=10, font=POP, bold=True,
       color=TURQUOISE, spacing=1.5)
tools = [(ICO("canva.png"), u"Canva", u"Visuels & carrousels"),
         (ICO("capcut.png"), u"CapCut", u"Montage vidéo"),
         (ICO("trello.png"), u"Trello", u"Suivi de projet"),
         (ICO("charte.png"), u"Charte", u"Identité visuelle")]
for i, (ic, t, d) in enumerate(tools):
    x = 52 + i * 138
    card(s, x, 410, 126, 62)
    s.image(ic, x + 12, 424, 30, 30)
    s.text(t, x + 50, 426, 74, size=11, font=POP, bold=True, color=VERT_FONCE)
    s.text(d, x + 50, 442, 76, size=7.6, font=POP, color=OLIVE, leading=1.3)

# --- Gestion de projet Trello (encart)
s.rect(620, 320, 288, 152, fill=VERT_FONCE, radius=10)
s.image(ICO("trello.png"), 642, 338, 30, 30)
s.text(u"SUIVI DE PROJET", 682, 340, 200, size=9, font=POP, bold=True,
       color=TURQUOISE, spacing=1.4)
s.text(u"Trello", 682, 352, 200, size=16, font=ALFA, color=BLANC)
s.bullets([u"Un tableau par client", u"Calendrier éditorial partagé",
           u"Validation des contenus", u"Suivi des KPI"],
          642, 386, 250, size=10.4, color=BLANC, gap=9, marker="dot",
          mcolor=TURQUOISE, leading=1.4)

# ============================================================== 19 AMBITIONS
s = new(u"Ambitions")
titlebar(s, u"Vision", u"Ambitions",
         u"Où je veux emmener Sadiya Digital Agri dans les 12 prochains mois.",
         page=19)
amb = [
    (u"1", u"Acquérir mes premiers clients agro-industriels", u"0–6 mois", TURQUOISE),
    (u"2", u"Développer un portefeuille de clients réguliers", u"6–9 mois", VERT_FONCE),
    (u"3", u"Renforcer mon expertise en publicité en ligne", u"6–9 mois", OLIVE),
    (u"4", u"Structurer une offre de production vidéo terrain", u"9–12 mois", TURQUOISE),
    (u"5", u"Faire de Sadiya Digital Agri une agence reconnue", u"12 mois +", VERT_FONCE),
]
for i, (n, t, ech, c) in enumerate(amb):
    y = 172 + i * 58
    card(s, 52, y, 856, 48)
    s.rect(52, y, 4, 48, fill=c, radius=2)
    numbadge(s, 76, y + 11, n, d=26, fill=c, size=11)
    s.text(t, 120, y + 14, 600, size=15, font=POP, bold=True, color=VERT_FONCE)
    s.rect(790, y + 13, 96, 22, fill=c, radius=11)
    s.text(ech, 790, y + 19, 96, size=9, font=POP, bold=True, color=BLANC,
           align="c")

# --- Cap final
s.rect(52, 472, 856, 38, fill=VERT_FONCE, radius=9)
s.text(u"LE CAP", 76, 484, 70, size=8.5, font=POP, bold=True, color=TURQUOISE,
       spacing=1.4)
s.text(u"Faire des produits sénégalais une référence digitale.",
       146, 482, 740, size=12.5, font=POP, bold=True, color=BLANC)

# ============================================================== 20 EQUIPE
s = new(u"Notre équipe")
titlebar(s, u"L'équipe", u"Notre Équipe",
         u"Trois compétences complémentaires : expertise métier, création et développement commercial.",
         page=20)
team = [
    (IM("team_ceo.jpg"), u"Nene H. S. Diallo", u"Fondatrice & CEO",
     [u"Stratégie digitale", u"Expertise agro"], TURQUOISE),
    (IM("team_createur.jpg"), u"Créatrice de contenu", u"Poste à pourvoir",
     [u"Canva & CapCut", u"Vidéo terrain"], VERT_FONCE),
    (IM("team_commercial.jpg"), u"Responsable commercial", u"Poste à pourvoir",
     [u"Prospection B2B", u"Négociation"], OLIVE),
]
for i, (photo, nom, role, tags, c) in enumerate(team):
    x = 52 + i * 288
    card(s, x, 168, 268, 276)
    s.rect(x, 168, 268, 4, fill=c, radius=2)
    s.image(photo, x + 71, 190, 126, 168)
    s.text(nom, x + 16, 370, 236, size=14, font=POP, bold=True, color=VERT_FONCE,
           align="c", leading=1.2)
    s.text(role, x + 16, 392, 236, size=10.5, font=POP, bold=True, color=c,
           align="c")
    for k, tg in enumerate(tags):
        tw = 112
        s.rect(x + 18 + k * 120, 414, tw, 21, fill=c, alpha=0.14, radius=10.5)
        s.text(tg, x + 18 + k * 120, 419, tw, size=8.2, font=POP, bold=True,
               color=c, align="c")
s.rect(52, 462, 856, 38, fill=VERT_FONCE, radius=9)
s.text(u"AUJOURD'HUI", 76, 474, 116, size=9, font=POP, bold=True,
       color=TURQUOISE, spacing=1.4)
s.text(u"Je porte seule l'activité. Recrutements en freelance dès le 3e client.",
       186, 473, 700, size=11.5, font=POP, color=BLANC)

# ============================================================== 21 CTA
s = new(u"Appel à l'action")
titlebar(s, u"Ce dont j'ai besoin", u"Appel à l'Action",
         u"Un financement de 1 850 000 FCFA pour passer à l'échelle.",
         page=21)

# --- Montant
s.rect(52, 168, 258, 116, fill=VERT_FONCE, radius=10)
s.text(u"FINANCEMENT DEMANDÉ", 74, 186, 220, size=9, font=POP, bold=True,
       color=TURQUOISE, spacing=1.4)
s.text(u"1 850 000", 74, 206, 220, size=32, font=ALFA, color=BLANC)
s.text(u"FCFA — sur 12 mois", 74, 252, 220, size=10.5, font=POP, bold=True,
       color=TURQUOISE)

# --- 4 postes de depense
posts = [(u"Équipements de production",
          u"Ordinateur, smartphone, éclairage, micro", u"1 020 000", TURQUOISE),
         (u"Abonnements & outils",
          u"Meta Ads, Canva Pro, CapCut Pro, hébergement", u"305 000", VERT_FONCE),
         (u"Formations",
          u"Analytics, marketing B2B, acquisition client", u"275 000", OLIVE),
         (u"Site vitrine",
          u"Offres, portfolio et formulaire de devis", u"250 000", TURQUOISE)]
for i, (t, d, m, c) in enumerate(posts):
    x = 336 + (i % 2) * 288
    y = 168 + (i // 2) * 62
    card(s, x, y, 268, 52)
    s.rect(x, y, 4, 52, fill=c, radius=2)
    s.text(t, x + 20, y + 9, 176, size=11, font=POP, bold=True, color=VERT_FONCE)
    s.text(d, x + 20, y + 28, 184, size=8, font=POP, color=OLIVE)
    s.text(m, x + 186, y + 17, 64, size=10.5, font=POP, bold=True, color=c, align="r")

# --- Besoins non financiers
s.text(u"AU-DELÀ DU FINANCEMENT", 52, 306, 400, size=9.5, font=POP, bold=True,
       color=OLIVE, spacing=1.5)
needs = [(u"Accompagnement", u"Mentorat business : offre,\npricing et gestion", TURQUOISE),
         (u"Partenariat", u"Accès aux réseaux\nagro-industriels", VERT_FONCE),
         (u"Visibilité", u"Références et premiers\nclients pilotes", OLIVE)]
for i, (t, d, c) in enumerate(needs):
    x = 52 + i * 288
    card(s, x, 328, 268, 76)
    s.rect(x, 328, 4, 76, fill=c, radius=2)
    s.text(t, x + 20, 342, 224, size=13.5, font=POP, bold=True, color=VERT_FONCE)
    s.text(d, x + 20, 366, 230, size=10, font=POP, color=OLIVE, leading=1.45)

s.text(u"« Avec votre soutien, mon activité peut créer plus d'impact "
       u"et d'opportunités. »",
       52, 428, 856, size=13, font=ALFA, color=VERT_FONCE, align="c")

# ============================================================== 22 MERCI
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
footer(s, page=22, logos=True, mention=True)


# ------------------------------------------------------------------- BUILD
if __name__ == "__main__":
    out_pdf = os.path.join(ROOT, "Pitch_Deck_Sadiya_Digital_Agri.pdf")
    out_ppt = os.path.join(ROOT, "Pitch_Deck_Sadiya_Digital_Agri.pptx")
    render_pdf.render(SLIDES, out_pdf)
    render_pptx.render(SLIDES, out_ppt)
    print("OK %d slides" % len(SLIDES))
    for p in (out_pdf, out_ppt):
        print("  %s  %.1f Ko" % (os.path.basename(p), os.path.getsize(p) / 1024.0))
