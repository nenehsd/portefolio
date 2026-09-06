# -*- coding: utf-8 -*-
"""Genere le script de pitch oral (4-5 min) au format Word."""
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
LOGO = os.path.join(ROOT, "assets", "img", "logo-sadiya.png")

VERT = RGBColor(0x1F, 0x5E, 0x3A)
TURQ = RGBColor(0x1A, 0xAB, 0x70)
OLIVE = RGBColor(0x42, 0x61, 0x2D)
NOIR = RGBColor(0x0A, 0x1A, 0x01)
GRIS = RGBColor(0x6B, 0x7A, 0x6C)

doc = Document()

# --- Mise en page
sec = doc.sections[0]
sec.page_width, sec.page_height = Cm(21), Cm(29.7)
for a in ("top_margin", "bottom_margin"):
    setattr(sec, a, Cm(1.8))
sec.left_margin = sec.right_margin = Cm(2.2)

st = doc.styles["Normal"]
st.font.name = "Poppins"
st.font.size = Pt(10.5)
st.font.color.rgb = NOIR
st._element.rPr.rFonts.set(qn("w:eastAsia"), "Poppins")
st.paragraph_format.space_after = Pt(6)
st.paragraph_format.line_spacing = 1.25


def shade(cell, hexcolor):
    el = OxmlElement("w:shd")
    el.set(qn("w:val"), "clear")
    el.set(qn("w:fill"), hexcolor)
    cell._tc.get_or_add_tcPr().append(el)


def para(text="", size=10.5, bold=False, italic=False, color=NOIR, align=None,
         space_before=0, space_after=6, leading=1.25, font="Poppins"):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = leading
    if align:
        p.alignment = {"c": WD_ALIGN_PARAGRAPH.CENTER, "r": WD_ALIGN_PARAGRAPH.RIGHT,
                       "j": WD_ALIGN_PARAGRAPH.JUSTIFY}[align]
    if text:
        r = p.add_run(text)
        r.font.name = font
        r.font.size = Pt(size)
        r.bold = bold
        r.italic = italic
        r.font.color.rgb = color
    return p


def rule(color="1AAB70", size=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(10)
    pbdr = OxmlElement("w:pBdr")
    b = OxmlElement("w:bottom")
    b.set(qn("w:val"), "single"); b.set(qn("w:sz"), str(size))
    b.set(qn("w:space"), "1"); b.set(qn("w:color"), color)
    pbdr.append(b)
    p._p.get_or_add_pPr().append(pbdr)


def section(num, titre, slides, duree):
    """Bandeau de section : numero, titre, slides visees, minutage."""
    t = doc.add_table(rows=1, cols=2)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    t.columns[0].width = Cm(12.4)
    t.columns[1].width = Cm(4.2)
    c0, c1 = t.rows[0].cells
    c0.width, c1.width = Cm(12.4), Cm(4.2)
    for c in (c0, c1):
        shade(c, "1F5E3A")
        c.paragraphs[0].paragraph_format.space_before = Pt(3)
        c.paragraphs[0].paragraph_format.space_after = Pt(3)
    r = c0.paragraphs[0].add_run(u"%s · %s" % (num, titre))
    r.font.name = "Poppins"; r.font.size = Pt(11.5); r.bold = True
    r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    p1 = c1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r1 = p1.add_run(u"%s  |  %s" % (slides, duree))
    r1.font.name = "Poppins"; r1.font.size = Pt(8.5); r1.bold = True
    r1.font.color.rgb = RGBColor(0x1A, 0xAB, 0x70)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def dire(text):
    """Le texte a prononcer."""
    p = para(text, size=11, leading=1.4, space_after=8, align="j")
    return p


def note(text):
    """Indication de jeu / respiration."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(12)
    p.paragraph_format.left_indent = Cm(0.4)
    pbdr = OxmlElement("w:pBdr")
    b = OxmlElement("w:left")
    b.set(qn("w:val"), "single"); b.set(qn("w:sz"), "12")
    b.set(qn("w:space"), "6"); b.set(qn("w:color"), "9FB8A2")
    pbdr.append(b)
    p._p.get_or_add_pPr().append(pbdr)
    r = p.add_run(text)
    r.font.name = "Poppins"; r.font.size = Pt(8.5); r.italic = True
    r.font.color.rgb = OLIVE


# ============================================================ EN-TETE
try:
    doc.add_picture(LOGO, width=Cm(4.6))
    doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.paragraphs[-1].paragraph_format.space_after = Pt(4)
except Exception:
    pass

para(u"SCRIPT DE PITCH ORAL", size=9, bold=True, color=TURQ, align="c",
     space_after=2)
para(u"Sadiya Digital Agri", size=26, bold=True, color=VERT, align="c",
     space_after=2, font="Alfa Slab One")
para(u"Programme de Pré-incubation 2026 — Fabrique 360, Simplon Sénégal",
     size=10, color=OLIVE, align="c", space_after=10)
rule()

# --- Bandeau infos
t = doc.add_table(rows=1, cols=3)
t.alignment = WD_TABLE_ALIGNMENT.CENTER
infos = [(u"DURÉE", u"4 min 30"), (u"MOTS", u"± 700"),
         (u"DÉBIT", u"~155 mots / min")]
for i, (k, v) in enumerate(infos):
    c = t.rows[0].cells[i]
    c.width = Cm(5.5)
    shade(c, "F4F7F5")
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(1)
    r = p.add_run(k); r.font.name = "Poppins"; r.font.size = Pt(7.5)
    r.bold = True; r.font.color.rgb = TURQ
    p2 = c.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.space_after = Pt(4)
    r2 = p2.add_run(v); r2.font.name = "Poppins"; r2.font.size = Pt(11)
    r2.bold = True; r2.font.color.rgb = VERT
doc.add_paragraph().paragraph_format.space_after = Pt(4)

note(u"Mode d'emploi — le texte en grand est à dire ; les encadrés en vert olive "
     u"sont des indications de rythme et de gestuelle, à ne pas lire. "
     u"Les minutages sont cumulés depuis le début.")

# ============================================================ 1 ACCROCHE
section(u"1", u"Accroche", u"Slides 1 à 3", u"0:00 → 0:35")
dire(u"Bonjour à toutes et à tous. Je m'appelle Nene Halimatou Sahdiya Diallo, "
     u"et je suis la fondatrice de Sadiya Digital Agri.")
dire(u"Je voudrais commencer par une question toute simple. Au Sénégal, nous "
     u"produisons d'excellents produits locaux : du jus de baobab, du fonio, "
     u"de la pâte d'arachide, de la sauce bissap. Mais si ces produits ne sont "
     u"pas visibles en ligne… comment donner envie de les consommer ?")
note(u"Marquer une vraie pause de deux secondes après la question. "
     u"Regarder le jury, ne pas enchaîner tout de suite.")

# ============================================================ 2 PROBLEME
section(u"2", u"Contexte & problématique", u"Slide 2", u"0:35 → 1:10")
dire(u"Regardons le contexte. Fin 2025, le Sénégal compte onze millions cinq "
     u"cent mille internautes, soit plus de soixante pour cent de la population, "
     u"et cinq millions quatre cent mille identités actives sur les réseaux "
     u"sociaux. Nos concitoyens y passent en moyenne deux heures vingt-quatre "
     u"par jour. Et soixante-trois pour cent des PMI industrielles du pays "
     u"évoluent dans l'agroalimentaire.")
dire(u"Le marché est donc là. Pourtant les entreprises agroalimentaires font "
     u"face à trois freins : une présence très faible sur les réseaux, "
     u"un manque de stratégie — on publie sans objectif ni calendrier — et une "
     u"visibilité qui ne convertit pas : des vues, parfois des likes, mais "
     u"aucun client au bout.")
dire(u"Résultat : des produits de qualité restent inconnus, pendant que les "
     u"marques importées occupent tout l'espace digital.")
note(u"Appuyer sur « aucun client au bout » — c'est le point qui parle "
     u"le plus à un jury d'entrepreneurs.")

# ============================================================ 3 SOLUTION
section(u"3", u"La solution & le marché", u"Slides 4 et 5", u"1:10 → 1:55")
dire(u"Ma réponse, c'est Sadiya Digital Agri : une agence de community management "
     u"spécialisée dans le secteur agro-industriel. Nous proposons trois choses : "
     u"la stratégie social media, la création de contenu, et la gestion de "
     u"communauté.")
dire(u"Ce qui me différencie, c'est une double expertise. J'ai une licence en "
     u"agronomie à l'UCAD, donc je connais le terrain, les producteurs, les "
     u"contraintes du secteur. Et j'ai été formée sept semaines en design et "
     u"community management à Simplon Sénégal. Cette combinaison, agriculture "
     u"et digital, personne ne la propose aujourd'hui sur ce marché.")
dire(u"Mon marché est cent pour cent B2B : producteurs, transformateurs, "
     u"coopératives, distributeurs et acheteurs professionnels.")
note(u"C'est le cœur de votre crédibilité. Ralentir sur « agriculture et digital » "
     u"et laisser la phrase respirer.")

# ============================================================ 4 STRATEGIE
section(u"4", u"La stratégie TOMSTER", u"Slides 6 à 13", u"1:55 → 2:50")
dire(u"Pour y arriver, j'applique la méthode TOMSTER. Je vais vous en donner "
     u"l'essentiel.")
dire(u"Ma cible, c'est Aminata : trente-six ans, directrice générale d'une PME "
     u"de transformation de fruits et légumes à Dakar. Elle a de très bons "
     u"produits, mais ni le temps ni les compétences pour les rendre visibles. "
     u"C'est elle que j'ai en tête à chaque contenu que je produis.")
dire(u"Mes objectifs sont chiffrés : cinq cents abonnés qualifiés en trois mois, "
     u"trente demandes de renseignements et cinq contrats signés en six mois.")
dire(u"Ma stratégie repose sur trois réseaux complémentaires : TikTok attire, "
     u"Facebook fédère, LinkedIn crédibilise et permet de prospecter. Je publie "
     u"trois jours par semaine, et chaque mois je mesure la portée, les demandes "
     u"et les contrats signés — puis j'ajuste.")
note(u"Section dense : ne pas accélérer. Si le temps manque, supprimer la phrase "
     u"sur les cinq piliers, pas les chiffres.")

# ============================================================ 5 MODELE ECO
section(u"5", u"Modèle économique & benchmark", u"Slides 14 à 17", u"2:50 → 3:30")
dire(u"Mon modèle repose sur l'abonnement mensuel : Essentiel à soixante-quinze "
     u"mille francs, Pro à cent cinquante mille, Premium à deux cent cinquante "
     u"mille, plus des prestations ponctuelles dès vingt-cinq mille.")
dire(u"Mes charges mensuelles sont estimées à quatre-vingt-cinq mille francs. "
     u"Autrement dit, dès le troisième client en formule Pro, l'activité est "
     u"rentable. Mon objectif à six mois : quatre cent cinquante mille francs "
     u"de revenus mensuels.")
dire(u"Face à la concurrence, ma différence tient en une phrase : je suis la "
     u"seule à combiner expertise agronomique et maîtrise digitale. Les agences "
     u"établies facturent de cent trente mille à six cent mille francs par mois : "
     u"elles ont la méthode, mais aucune ne parle vraiment agro. Les freelances, "
     u"entre cinquante et cent cinquante mille, ont les tarifs mais pas la "
     u"stratégie. Je me positionne entre les deux, avec la spécialisation en plus.")
note(u"Annoncer le seuil de rentabilité avec assurance, puis enchaîner sur le "
     u"benchmark : c'est ce qu'un jury retient d'un business model.")

# ============================================================ 6 TRACTION
section(u"6", u"Réalisations & équipe", u"Slides 18 à 21", u"3:30 → 4:05")
dire(u"Et je ne pars pas de zéro. L'entreprise est formalisée : NINEA et registre "
     u"de commerce. L'identité de marque est construite : logo, charte, bannière, "
     u"carte de visite. Ma présence digitale est en place : site portfolio, "
     u"LinkedIn, Facebook et Meta Business Suite. Je travaille avec Canva, CapCut "
     u"et Trello.")
dire(u"Mon ambition, maintenant, c'est de signer mes cinq premiers clients, de "
     u"construire un portefeuille récurrent, et de faire de Sadiya Digital Agri "
     u"la référence de la communication digitale agroalimentaire au Sénégal.")
dire(u"Aujourd'hui je porte l'activité seule. Dès le troisième client régulier, "
     u"je m'entourerai de deux profils en freelance : une créatrice de contenu "
     u"pour la production visuelle et vidéo, et un responsable commercial pour "
     u"la prospection.")
note(u"Énumérer les réalisations d'un ton posé et factuel. C'est la preuve "
     u"que vous exécutez déjà.")

# ============================================================ 7 CTA
section(u"7", u"L'appel à l'action", u"Slide 22", u"4:05 → 4:30")
dire(u"Pour franchir cette étape, je sollicite un million huit cent cinquante "
     u"mille francs CFA : mes équipements de production, mes abonnements et outils "
     u"sur douze mois, trois formations — analytics, marketing B2B et acquisition "
     u"client — et un site vitrine professionnel.")
dire(u"Au-delà du financement, j'ai besoin d'un accompagnement en mentorat "
     u"business, de partenariats avec les réseaux agro-industriels, et de "
     u"visibilité pour décrocher mes premiers clients pilotes.")
dire(u"Avec votre soutien, mon activité peut créer plus d'impact et "
     u"d'opportunités. Je vous remercie pour votre attention.")
note(u"Dernière phrase : ralentir nettement, regarder le jury, sourire. "
     u"Ne pas enchaîner sur autre chose — laisser le silence.")

# ============================================================ ANNEXE
doc.add_page_break()
para(u"AIDE-MÉMOIRE", size=9, bold=True, color=TURQ, space_after=2)
para(u"À relire juste avant de passer", size=20, bold=True, color=VERT,
     space_after=8, font="Alfa Slab One")
rule()

para(u"Les 6 chiffres à ne pas oublier", size=12, bold=True, color=VERT,
     space_before=6, space_after=6)
chiffres = [(u"1 850 000 FCFA", u"le financement demandé"),
            (u"85 000 FCFA", u"mes charges mensuelles"),
            (u"3 clients", u"mon seuil de rentabilité"),
            (u"11,5 M / 2 h 24", u"internautes sénégalais, usage quotidien"),
            (u"75 / 150 / 250 k", u"mes trois formules mensuelles"),
            (u"500 / 30 / 5", u"abonnés, demandes, contrats")]
t = doc.add_table(rows=len(chiffres), cols=2)
t.alignment = WD_TABLE_ALIGNMENT.CENTER
for i, (a, b) in enumerate(chiffres):
    ca, cb = t.rows[i].cells
    ca.width, cb.width = Cm(5.0), Cm(11.6)
    shade(ca, "F4F7F5")
    for cell, txt, bold, col, sz in ((ca, a, True, VERT, 11), (cb, b, False, NOIR, 10)):
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(txt); r.font.name = "Poppins"; r.font.size = Pt(sz)
        r.bold = bold; r.font.color.rgb = col
doc.add_paragraph().paragraph_format.space_after = Pt(2)

para(u"Questions probables du jury", size=12, bold=True, color=VERT,
     space_before=8, space_after=6)
qa = [
    (u"Pourquoi vous et pas une agence établie ?",
     u"Parce qu'aucune agence sénégalaise ne combine agronomie et community "
     u"management. Je comprends le vocabulaire d'un transformateur, ses saisons, "
     u"ses contraintes de production. Une agence généraliste doit tout apprendre."),
    (u"Comment allez-vous trouver vos premiers clients ?",
     u"Par la prospection directe sur LinkedIn, en proposant un diagnostic gratuit "
     u"de leur présence digitale. C'est concret, sans engagement, et cela démontre "
     u"ma valeur avant même de facturer."),
    (u"Vos tarifs ne sont-ils pas trop bas ?",
     u"Ce sont des tarifs d'entrée assumés, adaptés aux budgets réels des PME "
     u"sénégalaises. Ils me permettent de constituer un portefeuille et des études "
     u"de cas ; je les réévaluerai une fois mes résultats prouvés."),
    (u"Que faites-vous si un client n'obtient pas de résultats ?",
     u"Je mesure chaque mois et j'ajuste. Mon reporting compare les KPI aux "
     u"objectifs fixés ensemble. Si un contenu ne fonctionne pas, je change de "
     u"format — c'est précisément la boucle publier, mesurer, analyser, ajuster."),
    (u"Êtes-vous seule ? Comment absorberez-vous la croissance ?",
     u"Oui, je démarre seule, ce qui me rend agile et compétitive. Au-delà de cinq "
     u"clients réguliers, je prévois de m'appuyer sur des freelances pour le "
     u"montage vidéo et le graphisme."),
]
for q, a in qa:
    para(u"« " + q + u" »", size=10, bold=True, color=OLIVE,
         space_before=4, space_after=2)
    para(a, size=10, align="j", space_after=8)

para(u"Trois réflexes pendant le pitch", size=12, bold=True, color=VERT,
     space_before=8, space_after=6)
for tip in [u"Respirer après chaque chiffre — c'est ce qui leur laisse le temps "
            u"de l'enregistrer.",
            u"Regarder alternativement les différents membres du jury, pas "
            u"seulement ses notes ou l'écran.",
            u"Si un mot est oublié, reformuler avec ses propres mots plutôt que "
            u"de s'arrêter : personne ne connaît le texte."]:
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(tip); r.font.name = "Poppins"; r.font.size = Pt(10)
    r.font.color.rgb = NOIR

out = os.path.join(ROOT, "Pitch_Oral_Sadiya_Digital_Agri.docx")
doc.save(out)
print(u"OK -> %s (%.1f Ko)" % (os.path.basename(out), os.path.getsize(out) / 1024.0))

# comptage de mots du texte a dire
import re
words = 0
for p in doc.paragraphs:
    if p.style.name == "Normal" and p.runs and p.runs[0].font.size == Pt(11):
        words += len(re.findall(r"\w+", p.text))
print(u"Mots à prononcer : ~%d  ->  %.1f min à 155 mots/min" % (words, words / 155.0))
