#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vigie — générateur de site statique.

Aucune dépendance : bibliothèque standard de Python 3 uniquement.
Usage :  python3 tools/build.py   (depuis la racine du dépôt)
"""

import html
import json
import os
import re
import shutil
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "tools"))

from contenu import (          # noqa: E402
    SITE, PARTIES, IMPUTABILITE, CHRONOLOGIE, INDICATEURS,
    LEXIQUE, SOURCES, PAGES_STATIQUES, FAQ_ACCUEIL,
)
from dossiers import DOSSIERS  # noqa: E402


# --------------------------------------------------------------------------
# petites fabriques
# --------------------------------------------------------------------------

def e(txt):
    return html.escape(txt, quote=False)


def attr(txt):
    return html.escape(txt, quote=True)


def slugifier(texte):
    texte = texte.lower()
    remplacements = {
        "à": "a", "â": "a", "ä": "a", "é": "e", "è": "e", "ê": "e", "ë": "e",
        "î": "i", "ï": "i", "ô": "o", "ö": "o", "ù": "u", "û": "u", "ü": "u",
        "ç": "c", "œ": "oe", "æ": "ae", "’": "-", "'": "-",
    }
    for a, b in remplacements.items():
        texte = texte.replace(a, b)
    texte = re.sub(r"[^a-z0-9]+", "-", texte)
    return texte.strip("-")[:60] or "section"


# --------------------------------------------------------------------------
# rendu du micro-langage de balisage
# --------------------------------------------------------------------------

RE_TERME = re.compile(r"\{\{([a-z0-9\-]+)(?:\|([^}]+))?\}\}")
RE_LIEN = re.compile(r"\[([^\]\[]+)\]\(([^)\s]+)\)")
RE_GRAS = re.compile(r"\*\*([^*]+)\*\*")
RE_ITAL = re.compile(r"(?<![\*\w])\*([^*\n]+)\*(?!\*)")
RE_REF = re.compile(r"\[(\d+(?:,\s*\d+)*)\]")
RE_CODE = re.compile(r"`([^`]+)`")

# Cible des renvois de sources : chaîne vide lorsque la page porte sa propre
# liste de sources, chemin vers sources.html sinon.
HREF_SOURCES = [""]


def cible_sources(chemin):
    HREF_SOURCES[0] = chemin


def rendre_inline(texte, prefixe_lexique="", refs_vues=None, contexte=""):
    """Transforme le balisage en ligne en HTML."""
    out = e(texte)

    def _terme(m):
        slug, libelle = m.group(1), m.group(2)
        if slug not in LEXIQUE:
            raise SystemExit(
                "Terme de lexique inconnu : %s (dans %s)" % (slug, contexte))
        libelle = libelle or LEXIQUE[slug]["terme"]
        LEXIQUE[slug].setdefault("_renvois", set())
        if contexte:
            LEXIQUE[slug]["_renvois"].add(contexte)
        return '<a class="terme" href="%slexique.html#%s">%s</a>' % (
            prefixe_lexique, slug, e(libelle))

    out = RE_TERME.sub(_terme, out)

    def _ref(m):
        numeros = [n.strip() for n in m.group(1).split(",")]
        morceaux = []
        for n in numeros:
            idx = int(n)
            if idx < 1 or idx > len(SOURCES):
                raise SystemExit("Renvoi de source hors bornes : %s (%s)" % (n, contexte))
            if refs_vues is not None:
                refs_vues.append(idx)
            morceaux.append(
                '<a class="renvoi" href="%s#s%d">%d</a>' % (HREF_SOURCES[0], idx, idx))
        return "".join(morceaux)

    out = RE_REF.sub(_ref, out)
    out = RE_LIEN.sub(
        lambda m: '<a href="%s"%s>%s</a>' % (
            attr(m.group(2)),
            ' rel="noopener"' if m.group(2).startswith("http") else "",
            m.group(1)),
        out)
    out = RE_GRAS.sub(lambda m: "<strong>%s</strong>" % m.group(1), out)
    out = RE_ITAL.sub(lambda m: "<em>%s</em>" % m.group(1), out)
    out = RE_CODE.sub(lambda m: "<code>%s</code>" % m.group(1), out)
    return out


def rendre_bloc(corps, prefixe_lexique="", refs_vues=None, contexte="", titres=None):
    """Transforme un bloc de texte multi-lignes en HTML."""
    html_parts = []
    lignes = corps.strip("\n").split("\n")
    i = 0
    while i < len(lignes):
        ligne = lignes[i]
        nue = ligne.strip()

        if not nue:
            i += 1
            continue

        # titres
        if nue.startswith("### "):
            titre = nue[4:].strip()
            ident = slugifier(titre)
            html_parts.append(
                '<h3 id="%s">%s <a class="ancre" href="#%s" aria-label="Lien vers cette section">#</a></h3>'
                % (ident, rendre_inline(titre, prefixe_lexique, refs_vues, contexte), ident))
            i += 1
            continue
        if nue.startswith("## "):
            titre = nue[3:].strip()
            ident = slugifier(titre)
            if titres is not None:
                titres.append((ident, titre))
            html_parts.append(
                '<h2 id="%s">%s <a class="ancre" href="#%s" aria-label="Lien vers cette section">#</a></h2>'
                % (ident, rendre_inline(titre, prefixe_lexique, refs_vues, contexte), ident))
            i += 1
            continue

        # encadré  :::type Titre ... :::
        if nue.startswith(":::"):
            entete = nue[3:].strip()
            genre, _, titre = entete.partition(" ")
            contenu = []
            i += 1
            while i < len(lignes) and lignes[i].strip() != ":::":
                contenu.append(lignes[i])
                i += 1
            i += 1
            classe = {"objection": "encadre encadre--objection",
                      "doute": "encadre encadre--doute",
                      "calcul": "encadre encadre--calcul",
                      "note": "encadre"}.get(genre, "encadre")
            interne = rendre_bloc("\n".join(contenu), prefixe_lexique, refs_vues, contexte)
            html_parts.append(
                '<aside class="%s"><h3>%s</h3>%s</aside>'
                % (classe, e(titre.strip() or "Note"), interne))
            continue

        # bandeau de chiffres  @@ valeur | libellé ;; valeur | libellé
        if nue.startswith("@@"):
            reste = nue[2:].strip()
            teinte = ""
            if reste.startswith("lilas "):
                teinte = " chiffres--lilas"
                reste = reste[6:]
            cellules = []
            for morceau in reste.split(";;"):
                valeur, _, libelle = morceau.partition("|")
                valeur = valeur.strip()
                classe_cellule = "chiffre"
                if valeur.startswith("lilas "):
                    classe_cellule = "chiffre chiffre--lilas"
                    valeur = valeur[6:].strip()
                cellules.append(
                    '<div class="%s"><span class="valeur">%s</span>'
                    '<span class="libelle">%s</span></div>'
                    % (classe_cellule,
                       rendre_inline(valeur, prefixe_lexique, refs_vues, contexte),
                       rendre_inline(libelle.strip(), prefixe_lexique, refs_vues, contexte)))
            html_parts.append('<div class="chiffres%s">%s</div>' % (teinte, "".join(cellules)))
            i += 1
            continue

        # tableau
        if nue.startswith("|"):
            bloc = []
            legende = ""
            while i < len(lignes) and lignes[i].strip().startswith("|"):
                bloc.append(lignes[i].strip())
                i += 1
            if i < len(lignes) and lignes[i].strip().startswith("^ "):
                legende = lignes[i].strip()[2:]
                i += 1
            html_parts.append(rendre_tableau(bloc, legende, prefixe_lexique, refs_vues, contexte))
            continue

        # listes
        if nue.startswith("- ") or re.match(r"^\d+\. ", nue):
            ordonnee = bool(re.match(r"^\d+\. ", nue))
            items = []
            while i < len(lignes):
                cour = lignes[i].strip()
                if ordonnee and re.match(r"^\d+\. ", cour):
                    items.append(re.sub(r"^\d+\. ", "", cour))
                elif (not ordonnee) and cour.startswith("- "):
                    items.append(cour[2:])
                elif cour and items and (lignes[i].startswith("  ")):
                    items[-1] += " " + cour
                else:
                    break
                i += 1
            balise = "ol" if ordonnee else "ul"
            html_parts.append("<%s>%s</%s>" % (
                balise,
                "".join("<li>%s</li>" % rendre_inline(it, prefixe_lexique, refs_vues, contexte)
                        for it in items),
                balise))
            continue

        # paragraphe
        paragraphe = [nue]
        i += 1
        while i < len(lignes) and lignes[i].strip() and not re.match(
                r"^(#{2,3} |:::|@@|\||- |\d+\. |\^ )", lignes[i].strip()):
            paragraphe.append(lignes[i].strip())
            i += 1
        html_parts.append("<p>%s</p>" % rendre_inline(
            " ".join(paragraphe), prefixe_lexique, refs_vues, contexte))

    return "".join(html_parts)


def rendre_tableau(lignes, legende, prefixe_lexique, refs_vues, contexte):
    rangs = []
    for ligne in lignes:
        if re.match(r"^\|[\s:|-]+\|$", ligne):
            continue
        cellules = [c.strip() for c in ligne.strip("|").split("|")]
        rangs.append(cellules)
    if not rangs:
        return ""
    entete, corps = rangs[0], rangs[1:]

    def cellule(txt, balise):
        classe = ' class="nombre"' if re.match(r"^[\-–+]?[\d\s].*", txt) and balise == "td" else ""
        return "<%s%s>%s</%s>" % (
            balise, classe, rendre_inline(txt, prefixe_lexique, refs_vues, contexte), balise)

    out = ['<div class="tableau-defilant"><table>']
    if legende:
        out.append("<caption>%s</caption>" % rendre_inline(
            legende, prefixe_lexique, refs_vues, contexte))
    out.append("<thead><tr>%s</tr></thead>" % "".join(cellule(c, "th") for c in entete))
    out.append("<tbody>")
    for rang in corps:
        out.append("<tr>%s</tr>" % "".join(
            cellule(c, "th" if k == 0 and False else "td") for k, c in enumerate(rang)))
    out.append("</tbody></table></div>")
    return "".join(out)


# --------------------------------------------------------------------------
# gabarits
# --------------------------------------------------------------------------

def badge_imputabilite(cle, prefixe=""):
    niveau = IMPUTABILITE[cle]
    jauge = "▮" * niveau["rang"] + "▯" * (4 - niveau["rang"])
    return ('<a class="imput imput--%d" href="%smethode.html#l-echelle-d-imputabilite" '
            'title="%s">%s <span class="jauge" aria-hidden="true">%s</span></a>'
            % (niveau["rang"], prefixe, attr(niveau["definition"]), e(niveau["nom"]), jauge))


def jsonld(objets):
    graphe = {"@context": "https://schema.org", "@graph": objets}
    return ('<script type="application/ld+json">%s</script>'
            % json.dumps(graphe, ensure_ascii=False, separators=(",", ":")))


def page(chemin, titre_seo, description, mots_cles, corps, *, prefixe="",
         graphe=None, classe_nav=None, og_type="WebPage"):
    """Assemble une page complète."""
    canonique = SITE["url"] + "/" + (chemin if chemin != "index.html" else "")
    nav = []
    for lien, libelle in SITE["navigation"]:
        courant = ' aria-current="page"' if lien == classe_nav else ""
        nav.append('<li><a href="%s%s"%s>%s</a></li>' % (prefixe, lien, courant, e(libelle)))

    doc = []
    doc.append("<!doctype html>")
    doc.append('<html lang="fr">')
    doc.append("<head>")
    doc.append('<meta charset="utf-8">')
    doc.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
    doc.append("<title>%s</title>" % e(titre_seo))
    doc.append('<meta name="description" content="%s">' % attr(description))
    doc.append('<meta name="keywords" content="%s">' % attr(", ".join(mots_cles)))
    doc.append('<meta name="author" content="%s">' % attr(SITE["auteur"]))
    doc.append('<link rel="canonical" href="%s">' % attr(canonique))
    doc.append('<meta name="theme-color" content="#0d1013">')
    doc.append('<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">')
    doc.append('<meta property="og:type" content="%s">' % ("article" if og_type == "Article" else "website"))
    doc.append('<meta property="og:site_name" content="%s">' % attr(SITE["nom"]))
    doc.append('<meta property="og:locale" content="fr_BE">')
    doc.append('<meta property="og:title" content="%s">' % attr(titre_seo))
    doc.append('<meta property="og:description" content="%s">' % attr(description))
    doc.append('<meta property="og:url" content="%s">' % attr(canonique))
    doc.append('<meta property="og:image" content="%s/og.png">' % SITE["url"])
    doc.append('<meta property="og:image:width" content="1200">')
    doc.append('<meta property="og:image:height" content="630">')
    doc.append('<meta property="og:image:alt" content="%s">' % attr(SITE["og_alt"]))
    doc.append('<meta name="twitter:card" content="summary_large_image">')
    doc.append('<meta name="twitter:title" content="%s">' % attr(titre_seo))
    doc.append('<meta name="twitter:description" content="%s">' % attr(description))
    doc.append('<meta name="twitter:image" content="%s/og.png">' % SITE["url"])
    doc.append('<link rel="icon" href="%sfavicon.svg" type="image/svg+xml">' % prefixe)
    doc.append('<link rel="alternate" type="application/rss+xml" title="%s" href="%srss.xml">'
               % (attr(SITE["nom"]), prefixe))
    doc.append('<link rel="stylesheet" href="%sassets/style.css">' % prefixe)
    if graphe:
        doc.append(jsonld(graphe))
    doc.append("</head>")
    doc.append("<body>")
    doc.append('<a class="saut" href="#contenu">Aller au contenu</a>')
    doc.append('<header class="bandeau"><div class="enveloppe bandeau-interieur">')
    doc.append('<a class="marque" href="%sindex.html">%s</a>' % (prefixe, e(SITE["nom"])))
    doc.append('<span class="marque-devise">%s</span>' % e(SITE["devise"]))
    doc.append('<nav class="navigation" aria-label="Navigation principale"><ul>%s</ul></nav>' % "".join(nav))
    doc.append("</div></header>")
    doc.append('<main id="contenu"><div class="enveloppe">')
    doc.append(corps)
    doc.append("</div></main>")
    doc.append(pied(prefixe))
    doc.append("</body></html>")

    ecrire(chemin, "\n".join(doc))


def pied(prefixe):
    return """<footer class="pied"><div class="enveloppe">
<div class="pied-colonnes">
<div>
<h2>Le site</h2>
<ul>
<li><a href="{p}sommaire.html">Sommaire des 34 dossiers</a></li>
<li><a href="{p}chronologie.html">Chronologie</a></li>
<li><a href="{p}chiffres.html">Chiffres</a></li>
<li><a href="{p}lexique.html">Lexique</a></li>
<li><a href="{p}sources.html">Sources</a></li>
<li><a href="{p}methode.html">Méthode et limites</a></li>
</ul>
</div>
<div>
<h2>Documents</h2>
<ul>
<li><a href="{depot}/tree/main/download">Documents sources : dossier <code>/download</code> du dépôt</a></li>
<li><a href="{depot}">Code du site sur GitHub</a></li>
<li><a href="{usba}" rel="noopener">Atelier de l’éditeur — dl.ouaisfi.eu/usba</a></li>
<li><a href="{p}rss.xml">Flux RSS</a></li>
<li><a href="{p}llms.txt">llms.txt</a></li>
</ul>
</div>
<div>
<h2>Mentions</h2>
<p>Textes signés <strong>Vigie</strong>, nom de plume. Rédaction assistée par Claude (Anthropic) ; l’éditeur assume le choix des angles, la vérification et la publication.</p>
<p>Site statique : aucun cookie, aucun traqueur, aucune mesure d’audience. Le seul appel extérieur est le lecteur vidéo de la page d’accueil, chargé depuis <code>youtube-nocookie.com</code>.</p>
<p>Dernière mise à jour du corpus : {maj}.</p>
</div>
</div>
</div></footer>""".format(p=prefixe, depot=SITE["depot"], usba=SITE["usba"], maj=SITE["maj"])


def ecrire(chemin, contenu):
    cible = os.path.join(RACINE, chemin)
    os.makedirs(os.path.dirname(cible) or ".", exist_ok=True)
    with open(cible, "w", encoding="utf-8") as fh:
        fh.write(contenu)


# --------------------------------------------------------------------------
# pages
# --------------------------------------------------------------------------

def index_dossiers():
    """Ordonne les dossiers et calcule les voisinages."""
    ordre = []
    for partie in PARTIES:
        for slug in partie["dossiers"]:
            if slug not in DOSSIERS:
                raise SystemExit("Dossier annoncé mais absent : %s" % slug)
            ordre.append(slug)
    inconnus = set(DOSSIERS) - set(ordre)
    if inconnus:
        raise SystemExit("Dossiers non rattachés à une partie : %s" % ", ".join(sorted(inconnus)))
    return ordre


def construire_dossier(slug, numero, ordre, partie):
    cible_sources("")
    d = DOSSIERS[slug]
    refs = []
    titres = []
    corps_html = rendre_bloc(d["corps"], prefixe_lexique="../", refs_vues=refs,
                             contexte=slug, titres=titres)

    sommaire = ""
    if len(titres) >= 3:
        sommaire = ('<nav class="encadre" aria-label="Sommaire du dossier">'
                    '<h2>Dans ce dossier</h2><ul>%s</ul></nav>'
                    % "".join('<li><a href="#%s">%s</a></li>' % (i, e(t)) for i, t in titres))

    faq_html = ""
    if d.get("faq"):
        faq_html = ('<section class="faq"><h2 id="questions-frequentes">Questions fréquentes '
                    '<a class="ancre" href="#questions-frequentes" aria-label="Lien vers cette section">#</a></h2><dl>%s</dl></section>'
                    % "".join("<dt>%s</dt><dd>%s</dd>" % (
                        e(q), rendre_inline(r, "../", refs, slug)) for q, r in d["faq"]))

    refs_uniques = sorted(set(refs))
    liste_sources = ""
    if refs_uniques:
        items = []
        for n in refs_uniques:
            s = SOURCES[n - 1]
            items.append('<li id="s%d" value="%d">%s, <a href="%s" rel="noopener">%s</a>'
                         ' <span class="editeur">— %s</span></li>'
                         % (n, n, e(s["auteur"]), attr(s["url"]), e(s["titre"]), e(s["editeur"])))
        liste_sources = ('<section class="note-sources"><h2>Sources citées</h2><ol>%s</ol>'
                         '<p class="mention">Numérotation commune à tout le site : voir la '
                         '<a href="../sources.html">bibliographie complète</a>.</p></section>'
                         % "".join(items))

    # pagination
    pos = ordre.index(slug)
    pagination = []
    if pos > 0:
        prec = DOSSIERS[ordre[pos - 1]]
        pagination.append('<a class="precedent" href="%s.html"><span class="sens">Dossier précédent</span>'
                          '<span class="cible">%s</span></a>' % (ordre[pos - 1], e(prec["titre"])))
    else:
        pagination.append('<a class="precedent" href="../sommaire.html"><span class="sens">Retour</span>'
                          '<span class="cible">Sommaire</span></a>')
    if pos < len(ordre) - 1:
        suiv = DOSSIERS[ordre[pos + 1]]
        pagination.append('<a class="suivant" href="%s.html"><span class="sens">Dossier suivant</span>'
                          '<span class="cible">%s</span></a>' % (ordre[pos + 1], e(suiv["titre"])))
    else:
        pagination.append('<a class="suivant" href="../sources.html"><span class="sens">Suite</span>'
                          '<span class="cible">Les sources</span></a>')

    voisins = [s for s in partie["dossiers"] if s != slug]
    bloc_voisins = ""
    if voisins:
        bloc_voisins = ('<section class="voisins"><h2>Dans la même partie — %s</h2><ul>%s</ul></section>'
                        % (e(partie["titre"]),
                           "".join('<li><a href="%s.html">%s</a></li>' % (v, e(DOSSIERS[v]["titre"]))
                                   for v in voisins)))

    imp = IMPUTABILITE[d["imputabilite"]]

    corps = """<nav class="fil" aria-label="Fil d’Ariane"><ol>
<li><a href="../index.html">Vigie</a></li>
<li><a href="../sommaire.html">Dossiers</a></li>
<li><a href="../sommaire.html#{pslug}">{partie}</a></li>
<li>{titre}</li>
</ol></nav>
<article class="article">
<p class="sur-titre">Dossier {num} sur {total} — {partie}</p>
<h1>{titre}</h1>
<p class="chapeau">{chapeau}</p>
<div class="imput-ligne">{badge}<span class="imput-motif">{motif}</span></div>
{sommaire}
{corps}
{faq}
{sources}
{voisins}
<nav class="pagination" aria-label="Navigation entre dossiers">{pagination}</nav>
</article>""".format(
        pslug=partie["slug"], partie=e(partie["titre"]), titre=e(d["titre"]),
        num=numero, total=len(ordre),
        chapeau=rendre_inline(d["chapeau"], "../", refs, slug),
        badge=badge_imputabilite(d["imputabilite"], "../"),
        motif=rendre_inline(d["motif"], "../", refs, slug),
        sommaire=sommaire, corps=corps_html, faq=faq_html,
        sources=liste_sources, voisins=bloc_voisins,
        pagination="".join(pagination))

    citations = [{"@type": "CreativeWork", "name": SOURCES[n - 1]["titre"],
                  "url": SOURCES[n - 1]["url"]} for n in refs_uniques]
    graphe = [
        {"@type": "Article", "@id": SITE["url"] + "/dossiers/" + slug + ".html#article",
         "headline": d["titre"], "description": d["resume"],
         "inLanguage": "fr", "isPartOf": {"@id": SITE["url"] + "/#site"},
         "author": {"@id": SITE["url"] + "/#auteur"},
         "publisher": {"@id": SITE["url"] + "/#auteur"},
         "datePublished": SITE["publication"], "dateModified": SITE["maj_iso"],
         "articleSection": partie["titre"],
         "keywords": ", ".join(d["mots_cles"]),
         "citation": citations,
         "mainEntityOfPage": SITE["url"] + "/dossiers/" + slug + ".html"},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Vigie", "item": SITE["url"] + "/"},
            {"@type": "ListItem", "position": 2, "name": "Dossiers", "item": SITE["url"] + "/sommaire.html"},
            {"@type": "ListItem", "position": 3, "name": d["titre"],
             "item": SITE["url"] + "/dossiers/" + slug + ".html"}]},
    ]
    if d.get("faq"):
        graphe.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"\[\d+(?:,\s*\d+)*\]", "", r)}}
            for q, r in d["faq"]]})

    page("dossiers/%s.html" % slug, d["seo_titre"], d["resume"], d["mots_cles"],
         corps, prefixe="../", graphe=graphe, classe_nav="sommaire.html", og_type="Article")

    return refs_uniques


def construire_accueil(ordre):
    cible_sources("sources.html")
    parties_html = []
    for partie in PARTIES:
        liens = "".join(
            '<li><a href="dossiers/%s.html">%s</a></li>' % (s, e(DOSSIERS[s]["titre"]))
            for s in partie["dossiers"])
        parties_html.append(
            '<div><h3>%s. %s</h3><ul class="mention">%s</ul></div>'
            % (partie["numero"], e(partie["titre"]), liens))

    cartes = "".join(
        '<a class="carte" href="%s"><h2>%s</h2><p>%s</p></a>' % (u, e(t), e(x))
        for u, t, x in [
            ("sommaire.html", "Les 34 dossiers",
             "Sept parties, de la sentence de Rabelais aux avoirs gelés d’Euroclear."),
            ("chiffres.html", "Les chiffres",
             "Vingt-quatre indicateurs sourcés, chacun daté et relié à son dossier."),
            ("chronologie.html", "La chronologie",
             "De −3000 à 2027 : trente-deux repères de la dette, de la monnaie et de l’arme économique."),
            ("methode.html", "La méthode",
             "L’échelle d’imputabilité, les corrections apportées au corpus, les lacunes assumées."),
        ])

    faq_html = "".join("<dt>%s</dt><dd>%s</dd>" % (e(q), rendre_inline(r, "", None, "accueil"))
                       for q, r in FAQ_ACCUEIL)

    corps = """<div class="accroche">
<p class="sur-titre">Enquête — {maj}</p>
<h1>Vigie</h1>
<p class="devise-principale">{devise}</p>
<p class="chapeau">Rabelais écrivait, en 1532, « science sans conscience n’est que ruine de l’âme ». Ce site instruit la version financière de la phrase — et conteste la lecture qu’on en fait d’ordinaire.</p>

<p class="these"><strong>Thèse.</strong> La critique courante dit que la finance a échappé au contrôle politique. Les faits de 2022-2026 disent l’inverse : gel de 210 milliards d’euros de réserves d’une banque centrale, exclusion de banques entières du réseau de messagerie interbancaire, licence obligatoire dès 0,1&nbsp;% de terre rare chinoise, droits de douane décidés seuls puis annulés par une cour. La finance n’est pas hors de contrôle. <strong>Elle est devenue le contrôle</strong> — et la chaîne de commandement ne comprend aucun citoyen.</p>

<p>D’où le déplacement que propose ce site. La « conscience » de Rabelais n’est pas un supplément d’âme ajouté à la technique : c’est la <strong>capacité de répondre</strong> de ce que l’on fait. Un système est sans conscience non pas quand il est immoral, mais quand plus personne n’y est en position de répondre. Chacun des trente-quatre dossiers porte donc une mention — <em>imputable</em>, <em>diluée</em>, <em>déléguée</em>, <em>sans répondant</em> — qui dit qui décide, qui paie, et qui répond.</p>
</div>

{cartes}

<section class="mesure">
<h2 id="la-video">Le point de départ</h2>
<p>{video_texte}</p>
<div class="video-cadre">
<iframe src="https://www.youtube-nocookie.com/embed/{video_id}?rel=0" title="{video_titre}" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" referrerpolicy="no-referrer" allowfullscreen></iframe>
</div>
<p class="video-legende">Si le lecteur ne s’affiche pas, la vidéo reste accessible à l’adresse <a href="https://www.youtube.com/watch?v={video_id}" rel="noopener">youtube.com/watch?v={video_id}</a>. C’est le seul contenu du site chargé depuis un serveur tiers.</p>
</section>

<section class="mesure">
<h2 id="ou-sont-les-documents">Où sont les documents</h2>
<p>Le corpus de départ — quatre rapports d’analyse, une note critique et deux dossiers documentaires — est déposé dans le dossier <code>/download</code> du dépôt&nbsp;: <a href="{depot}/tree/main/download" rel="noopener">{depot_court}/download</a>. La page <a href="sources.html">Sources</a> recense en plus les {nb_sources} références extérieures utilisées pour vérifier, corriger et prolonger ce corpus. L’atelier de l’éditeur — guides, fichiers et annexes — se trouve sur <a href="{usba}" rel="noopener">dl.ouaisfi.eu/usba</a>.</p>
</section>

<section class="mesure">
<h2 id="questions-frequentes">Questions fréquentes</h2>
<dl class="faq">{faq}</dl>
</section>

<section>
<h2 id="plan">Le plan complet</h2>
<div class="cartes">{parties}</div>
<p class="mention"><a href="sommaire.html">Voir le sommaire détaillé, avec les résumés et les mentions d’imputabilité →</a></p>
</section>""".format(
        maj=SITE["maj"], devise=e(SITE["devise"]), cartes='<div class="cartes">%s</div>' % cartes,
        video_id=SITE["video_id"], video_titre=attr(SITE["video_titre"]),
        video_texte=rendre_inline(SITE["video_texte"], "", None, "accueil"),
        depot=SITE["depot"], depot_court=SITE["depot"].replace("https://", ""),
        usba=SITE["usba"], nb_sources=len(SOURCES),
        faq=faq_html,
        parties="".join(parties_html))

    graphe = [
        {"@type": "WebSite", "@id": SITE["url"] + "/#site", "url": SITE["url"] + "/",
         "name": SITE["nom"], "alternateName": SITE["devise"],
         "description": SITE["description"], "inLanguage": "fr",
         "publisher": {"@id": SITE["url"] + "/#auteur"}},
        {"@type": "Person", "@id": SITE["url"] + "/#auteur", "name": SITE["auteur"],
         "description": "Nom de plume. Textes rédigés avec l’assistance de Claude (Anthropic) ; "
                        "vérification et publication assurées par l’éditeur.",
         "url": SITE["url"] + "/methode.html"},
        {"@type": "WebPage", "@id": SITE["url"] + "/#accueil", "url": SITE["url"] + "/",
         "name": SITE["seo_titre"], "isPartOf": {"@id": SITE["url"] + "/#site"},
         "datePublished": SITE["publication"], "dateModified": SITE["maj_iso"],
         "about": [{"@type": "Thing", "name": "Finance durable"},
                   {"@type": "Thing", "name": "Guerre économique"},
                   {"@type": "Thing", "name": "Économie politique"}]},
        {"@type": "VideoObject", "name": SITE["video_titre"],
         "description": SITE["video_description"],
         "embedUrl": "https://www.youtube-nocookie.com/embed/" + SITE["video_id"],
         "url": "https://www.youtube.com/watch?v=" + SITE["video_id"],
         "thumbnailUrl": "https://i.ytimg.com/vi/%s/hqdefault.jpg" % SITE["video_id"]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"\[\d+(?:,\s*\d+)*\]", "", r)}}
            for q, r in FAQ_ACCUEIL]},
        {"@type": "ItemList", "name": "Les 34 dossiers de Vigie",
         "numberOfItems": len(ordre),
         "itemListElement": [
             {"@type": "ListItem", "position": i + 1, "name": DOSSIERS[s]["titre"],
              "url": SITE["url"] + "/dossiers/" + s + ".html"}
             for i, s in enumerate(ordre)]},
    ]
    page("index.html", SITE["seo_titre"], SITE["description"], SITE["mots_cles"],
         corps, graphe=graphe, classe_nav="index.html")


def construire_sommaire(ordre):
    cible_sources("sources.html")
    blocs = []
    numero = 0
    for partie in PARTIES:
        items = []
        for slug in partie["dossiers"]:
            numero += 1
            d = DOSSIERS[slug]
            items.append(
                '<li><a class="dossier-lien" href="dossiers/%s.html">'
                '<span class="dossier-numero">%02d</span>'
                '<span class="dossier-titre">%s</span>'
                '<span class="dossier-resume">%s</span></a>'
                '<div class="dossier-meta">%s</div></li>'
                % (slug, numero, e(d["titre"]), e(d["resume"]),
                   badge_imputabilite(d["imputabilite"])))
        blocs.append(
            '<section class="partie" id="%s"><h2>%s. %s</h2>'
            '<p class="partie-note">%s</p><ol class="liste-dossiers">%s</ol></section>'
            % (partie["slug"], partie["numero"], e(partie["titre"]),
               rendre_inline(partie["note"], "", None, "sommaire"), "".join(items)))

    repartition = {}
    for slug in ordre:
        repartition[DOSSIERS[slug]["imputabilite"]] = repartition.get(
            DOSSIERS[slug]["imputabilite"], 0) + 1
    lignes = "".join(
        "<tr><td>%s</td><td>%s</td><td>%d</td></tr>"
        % (IMPUTABILITE[k]["nom"], IMPUTABILITE[k]["definition"], repartition.get(k, 0))
        for k in sorted(IMPUTABILITE, key=lambda x: IMPUTABILITE[x]["rang"]))

    corps = """<article class="article large">
<p class="sur-titre">Sommaire</p>
<h1>Trente-quatre dossiers</h1>
<p class="chapeau">Sept parties. On part de la phrase de Rabelais et de la distinction d’Aristote, on démonte la machine, on identifie qui décide, on suit l’arme économique, on mesure la ruine, on inventorie les promesses réglementaires, on cherche enfin ce qui rend quelqu’un comptable de ses actes.</p>
<div class="tableau-defilant"><table>
<caption>Répartition des trente-quatre dossiers sur l’échelle d’imputabilité</caption>
<thead><tr><th>Mention</th><th>Ce qu’elle constate</th><th class="nombre">Dossiers</th></tr></thead>
<tbody>%s</tbody></table></div>
<p class="mention">L’échelle et ses règles d’attribution sont exposées sur la <a href="methode.html#l-echelle-d-imputabilite">page méthode</a>. Elle ne note pas la moralité d’un acteur : elle mesure l’existence, ou l’absence, d’un endroit où l’on peut lui demander des comptes.</p>
%s
</article>""" % (lignes, "".join(blocs))

    graphe = [
        {"@type": "CollectionPage", "@id": SITE["url"] + "/sommaire.html",
         "name": "Sommaire — les 34 dossiers de Vigie",
         "isPartOf": {"@id": SITE["url"] + "/#site"},
         "inLanguage": "fr", "dateModified": SITE["maj_iso"]},
        {"@type": "ItemList", "numberOfItems": len(ordre), "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": DOSSIERS[s]["titre"],
             "description": DOSSIERS[s]["resume"],
             "url": SITE["url"] + "/dossiers/" + s + ".html"} for i, s in enumerate(ordre)]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Vigie", "item": SITE["url"] + "/"},
            {"@type": "ListItem", "position": 2, "name": "Sommaire",
             "item": SITE["url"] + "/sommaire.html"}]},
    ]
    page("sommaire.html", "Sommaire — les 34 dossiers | Vigie",
         "Les trente-quatre dossiers de Vigie, en sept parties, chacun accompagné de sa mention "
         "d’imputabilité : qui décide, qui paie, qui répond.",
         ["sommaire", "finance", "économie politique", "sanctions", "finance durable"],
         corps, graphe=graphe, classe_nav="sommaire.html")


def construire_chronologie():
    cible_sources("sources.html")
    items = []
    for jalon in CHRONOLOGIE:
        classe = ' class="jalon-lilas"' if jalon.get("teinte") == "lilas" else ""
        renvoi = ""
        if jalon.get("dossier"):
            renvoi = ' <a href="dossiers/%s.html">→ %s</a>' % (
                jalon["dossier"], e(DOSSIERS[jalon["dossier"]]["titre"]))
        items.append(
            '<li%s><span class="date">%s</span><span class="fait"><strong>%s</strong>'
            '<span class="precision">%s%s</span></span></li>'
            % (classe, e(jalon["date"]), rendre_inline(jalon["fait"], "", None, "chronologie"),
               rendre_inline(jalon["precision"], "", None, "chronologie"), renvoi))

    corps = """<article class="article large">
<p class="sur-titre">Repères</p>
<h1>Chronologie</h1>
<p class="chapeau">Trente-deux repères, du premier registre de dettes sumérien au calendrier réglementaire de 2027-2028. Les jalons en lilas marquent les moments où la finance a été explicitement employée comme arme.</p>
<ol class="chrono">%s</ol>
<p class="mention">Chaque date est rattachée à la source qui l’établit, sur la page <a href="sources.html">Sources</a>.</p>
</article>""" % "".join(items)

    graphe = [{"@type": "WebPage", "@id": SITE["url"] + "/chronologie.html",
               "name": "Chronologie | Vigie", "isPartOf": {"@id": SITE["url"] + "/#site"},
               "inLanguage": "fr", "dateModified": SITE["maj_iso"]}]
    graphe += [{"@type": "Event", "name": j["fait"], "startDate": j["iso"],
                "description": j["precision"],
                "location": {"@type": "Place", "name": j.get("lieu", "Monde")}}
               for j in CHRONOLOGIE if j.get("iso")]
    page("chronologie.html", "Chronologie de la finance et de l’arme économique | Vigie",
         "De Sumer à 2028 : trente-deux repères de la monnaie, de la dette, de la spéculation et "
         "des sanctions économiques, chacun sourcé.",
         ["chronologie", "histoire économique", "sanctions", "monnaie", "dette"],
         corps, graphe=graphe, classe_nav="chronologie.html")


def construire_chiffres():
    cible_sources("")
    lignes = []
    for ind in INDICATEURS:
        renvoi = ('<a href="dossiers/%s.html">%s</a>'
                  % (ind["dossier"], e(DOSSIERS[ind["dossier"]]["titre"]))) if ind.get("dossier") else "—"
        lignes.append(
            "<tr><td>%s</td><td class=\"nombre\">%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
            % (rendre_inline(ind["libelle"], "", None, "chiffres"), e(ind["valeur"]),
               e(ind["date"]), rendre_inline("[%d]" % ind["source"], "", [], "chiffres"), renvoi))

    corps = """<article class="article large">
<p class="sur-titre">Données</p>
<h1>Les chiffres</h1>
<p class="chapeau">Vingt-quatre indicateurs, chacun avec sa date de mesure, sa source et le dossier qui l’interprète. Un chiffre sans date est un argument, pas une donnée : c’est pourquoi la colonne « mesuré » n’est jamais vide.</p>
<div class="tableau-defilant"><table>
<caption>Indicateurs retenus par Vigie — état au %s</caption>
<thead><tr><th>Indicateur</th><th class="nombre">Valeur</th><th>Mesuré</th><th>Source</th><th>Dossier</th></tr></thead>
<tbody>%s</tbody></table></div>
<h2 id="ce-que-ces-chiffres-ne-disent-pas">Ce que ces chiffres ne disent pas</h2>
<p>Un montant notionnel de produits dérivés n’est pas une somme d’argent à risque : c’est la base de calcul d’un flux. Une part de patrimoine détenue par un centile dépend fortement du traitement des actifs non cotés et de l’immobilier. Un « financement fossile » agrège prêts syndiqués et émissions obligataires, dont une part n’est pas portée au bilan de la banque qui les arrange. Ces réserves sont détaillées dans la <a href="methode.html">page méthode</a>&nbsp;; elles ne détruisent aucun des ordres de grandeur, elles interdisent de les additionner naïvement.</p>
<div class="note-sources"><h2>Sources citées</h2><ol>%s</ol></div>
</article>""" % (
        SITE["maj"], "".join(lignes),
        "".join('<li id="s%d" value="%d">%s, <a href="%s" rel="noopener">%s</a> '
                '<span class="editeur">— %s</span></li>'
                % (n, n, e(SOURCES[n - 1]["auteur"]), attr(SOURCES[n - 1]["url"]),
                   e(SOURCES[n - 1]["titre"]), e(SOURCES[n - 1]["editeur"]))
                for n in sorted({i["source"] for i in INDICATEURS})))

    graphe = [
        {"@type": "WebPage", "@id": SITE["url"] + "/chiffres.html", "name": "Les chiffres | Vigie",
         "isPartOf": {"@id": SITE["url"] + "/#site"}, "inLanguage": "fr",
         "dateModified": SITE["maj_iso"]},
        {"@type": "Dataset", "name": "Indicateurs Vigie — finance, inégalités, sanctions, climat",
         "description": "Vingt-quatre indicateurs sourcés et datés sur la finance mondiale, la "
                        "concentration patrimoniale, les sanctions économiques et le financement "
                        "des énergies fossiles.",
         "creator": {"@id": SITE["url"] + "/#auteur"}, "inLanguage": "fr",
         "license": "https://creativecommons.org/licenses/by-sa/4.0/",
         "dateModified": SITE["maj_iso"],
         "variableMeasured": [
             {"@type": "PropertyValue", "name": i["libelle"], "value": i["valeur"],
              "measurementTechnique": i["date"]} for i in INDICATEURS]},
    ]
    page("chiffres.html", "Les chiffres de la finance mondiale, datés et sourcés | Vigie",
         "Vingt-quatre indicateurs sur la dette, la concentration du patrimoine, le financement "
         "fossile, les sanctions et la gestion d’actifs — chacun daté, sourcé et rattaché à un dossier.",
         ["chiffres", "dette mondiale", "inégalités", "financement fossile", "sanctions"],
         corps, graphe=graphe, classe_nav="chiffres.html")


def construire_lexique(ordre):
    cible_sources("sources.html")
    entrees = []
    for slug in sorted(LEXIQUE, key=lambda s: LEXIQUE[s]["terme"].lower()):
        item = LEXIQUE[slug]
        renvois = sorted(r for r in item.get("_renvois", set()) if r in DOSSIERS)
        liens = ""
        if renvois:
            liens = ('<p class="renvois">Employé dans : %s</p>'
                     % ", ".join('<a href="dossiers/%s.html">%s</a>' % (r, e(DOSSIERS[r]["titre"]))
                                 for r in renvois))
        entrees.append('<dt id="%s">%s</dt><dd>%s%s</dd>'
                       % (slug, e(item["terme"]),
                          rendre_inline(item["definition"], "", None, ""), liens))

    corps = """<article class="article large">
<p class="sur-titre">Vocabulaire</p>
<h1>Lexique</h1>
<p class="chapeau">Trente-trois termes. Le vocabulaire financier n’est pas neutre : « produit structuré », « optimisation », « instrument de politique étrangère » sont des mots qui, en nommant, apaisent. Chaque définition dit aussi ce que le terme escamote.</p>
<dl class="lexique">%s</dl>
</article>""" % "".join(entrees)

    graphe = [
        {"@type": "WebPage", "@id": SITE["url"] + "/lexique.html", "name": "Lexique | Vigie",
         "isPartOf": {"@id": SITE["url"] + "/#site"}, "inLanguage": "fr",
         "dateModified": SITE["maj_iso"]},
        {"@type": "DefinedTermSet", "@id": SITE["url"] + "/lexique.html#set",
         "name": "Lexique de Vigie", "inLanguage": "fr",
         "hasDefinedTerm": [
             {"@type": "DefinedTerm", "@id": SITE["url"] + "/lexique.html#" + s,
              "name": LEXIQUE[s]["terme"],
              "description": re.sub(r"\*\*", "",
                                    re.sub(r"\{\{[a-z0-9\-]+(?:\|([^}]+))?\}\}", r"\1",
                                           re.sub(r"\[\d+(?:,\s*\d+)*\]", "",
                                                  LEXIQUE[s]["definition"]))),
              "inDefinedTermSet": SITE["url"] + "/lexique.html#set"}
             for s in sorted(LEXIQUE)]},
    ]
    page("lexique.html", "Lexique critique de la finance | Vigie",
         "Trente-deux termes de la finance, de l’économie politique et de la guerre économique, "
         "définis avec ce que chacun escamote.",
         ["lexique", "définitions", "finance", "chrématistique", "imputabilité"],
         corps, graphe=graphe, classe_nav="lexique.html")


def construire_sources(usage):
    cible_sources("")
    par_nature = {}
    for i, s in enumerate(SOURCES, 1):
        par_nature.setdefault(s["nature"], []).append((i, s))

    filtres = " ".join('<a href="#%s">%s (%d)</a>' % (slugifier(n), e(n), len(v))
                       for n, v in sorted(par_nature.items()))
    blocs = []
    for nature, items in sorted(par_nature.items()):
        li = []
        for n, s in items:
            cites = sorted(usage.get(n, []))
            cite_par = ""
            if cites:
                cite_par = ('<span class="cite-par">Cité dans : %s</span>'
                            % ", ".join('<a href="dossiers/%s.html">%s</a>'
                                        % (c, e(DOSSIERS[c]["titre"])) for c in cites))
            li.append('<li id="s%d"><span class="num">%d</span>%s, '
                      '<a href="%s" rel="noopener">%s</a> '
                      '<span class="editeur">— %s, %s</span>%s</li>'
                      % (n, n, e(s["auteur"]), attr(s["url"]), e(s["titre"]),
                         e(s["editeur"]), e(s["date"]), cite_par))
        blocs.append('<section><h2 id="%s">%s</h2><ol class="sources">%s</ol></section>'
                     % (slugifier(nature), e(nature), "".join(li)))

    corps = """<article class="article large">
<p class="sur-titre">Bibliographie</p>
<h1>Sources</h1>
<p class="chapeau">%d références, classées par nature. Une source institutionnelle n’est pas plus vraie qu’une source militante : elle est intéressée autrement. Le classement sert à voir d’où parle chaque chiffre.</p>
<nav class="filtre-nature" aria-label="Filtrer par nature de source">%s</nav>
%s
<h2 id="corpus-de-depart">Le corpus de départ</h2>
<p>Sept documents constituent le point de départ de ce site : quatre rapports d’analyse, une note critique sur le récit du troc, et deux dossiers documentaires sur le système économique mondial et sur la guerre économique. Ils sont déposés dans le dossier <code>/download</code> du dépôt : <a href="%s/tree/main/download" rel="noopener">%s/download</a>. Ce que ce site en retient, ce qu’il corrige et ce qu’il écarte est exposé sur la <a href="methode.html">page méthode</a>.</p>
</article>""" % (len(SOURCES), filtres, "".join(blocs),
                 SITE["depot"], SITE["depot"].replace("https://", ""))

    graphe = [{"@type": "WebPage", "@id": SITE["url"] + "/sources.html", "name": "Sources | Vigie",
               "isPartOf": {"@id": SITE["url"] + "/#site"}, "inLanguage": "fr",
               "dateModified": SITE["maj_iso"],
               "citation": [{"@type": "CreativeWork", "name": s["titre"], "url": s["url"]}
                            for s in SOURCES]}]
    page("sources.html", "Sources — %d références classées par nature | Vigie" % len(SOURCES),
         "Les %d sources de Vigie, classées par nature (institutions, presse, recherche, ONG, "
         "professionnels) et reliées aux dossiers qui les citent." % len(SOURCES),
         ["sources", "bibliographie", "vérification", "méthode"],
         corps, graphe=graphe, classe_nav="sources.html")


def construire_pages_statiques(ordre):
    for chemin, meta in PAGES_STATIQUES.items():
        cible_sources("")
        refs = []
        corps_html = rendre_bloc(meta["corps"], "", refs, chemin.replace(".html", ""))
        liste = ""
        if refs:
            liste = ('<div class="note-sources"><h2>Sources citées</h2><ol>%s</ol></div>'
                     % "".join('<li id="s%d" value="%d">%s, <a href="%s" rel="noopener">%s</a> '
                               '<span class="editeur">— %s</span></li>'
                               % (n, n, e(SOURCES[n - 1]["auteur"]), attr(SOURCES[n - 1]["url"]),
                                  e(SOURCES[n - 1]["titre"]), e(SOURCES[n - 1]["editeur"]))
                               for n in sorted(set(refs))))
        corps = """<article class="article large">
<p class="sur-titre">%s</p>
<h1>%s</h1>
<p class="chapeau">%s</p>
%s
%s
</article>""" % (e(meta["sur_titre"]), e(meta["titre"]),
                 rendre_inline(meta["chapeau"], "", refs, chemin), corps_html, liste)
        graphe = [{"@type": "WebPage", "@id": SITE["url"] + "/" + chemin,
                   "name": meta["seo_titre"], "isPartOf": {"@id": SITE["url"] + "/#site"},
                   "inLanguage": "fr", "dateModified": SITE["maj_iso"]}]
        page(chemin, meta["seo_titre"], meta["description"], meta["mots_cles"],
             corps, graphe=graphe, classe_nav=chemin if chemin == "methode.html" else None)


def construire_404():
    corps = """<article class="article">
<p class="sur-titre">Erreur 404</p>
<h1>Cette page n’existe pas</h1>
<p class="chapeau">L’adresse demandée ne correspond à aucune page de ce site. Ce n’est pas votre faute : un lien a pu changer.</p>
<ul>
<li><a href="/finance/sommaire.html">Le sommaire des trente-quatre dossiers</a></li>
<li><a href="/finance/chiffres.html">Les chiffres</a></li>
<li><a href="/finance/sources.html">Les sources</a></li>
<li><a href="/finance/index.html">La page d’accueil</a></li>
</ul>
</article>"""
    page("404.html", "Page introuvable | Vigie", "La page demandée n’existe pas sur Vigie.",
         ["404"], corps)


# --------------------------------------------------------------------------
# fichiers annexes
# --------------------------------------------------------------------------

def construire_annexes(ordre):
    pages = ["index.html", "sommaire.html", "chronologie.html", "chiffres.html",
             "lexique.html", "sources.html"] + list(PAGES_STATIQUES)
    urls = [(SITE["url"] + "/", "1.0")]
    urls += [(SITE["url"] + "/" + p, "0.8") for p in pages if p != "index.html"]
    urls += [(SITE["url"] + "/dossiers/" + s + ".html", "0.7") for s in ordre]

    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, prio in urls:
        sitemap.append("<url><loc>%s</loc><lastmod>%s</lastmod>"
                       "<changefreq>monthly</changefreq><priority>%s</priority></url>"
                       % (u, SITE["maj_iso"], prio))
    sitemap.append("</urlset>")
    ecrire("sitemap.xml", "\n".join(sitemap))

    ecrire("robots.txt", """User-agent: *
Allow: /

Sitemap: %s/sitemap.xml
""" % SITE["url"])

    # RSS : les dossiers, dans l'ordre de lecture
    items = []
    for i, slug in enumerate(ordre, 1):
        d = DOSSIERS[slug]
        items.append("""<item>
<title>%s</title>
<link>%s/dossiers/%s.html</link>
<guid isPermaLink="true">%s/dossiers/%s.html</guid>
<description>%s</description>
<pubDate>%s</pubDate>
<category>%s</category>
</item>""" % (e(("%02d. " % i) + d["titre"]), SITE["url"], slug, SITE["url"], slug,
              e(d["resume"]), SITE["publication_rfc"], e(d["mots_cles"][0])))
    ecrire("rss.xml", """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
<title>%s — %s</title>
<link>%s/</link>
<atom:link href="%s/rss.xml" rel="self" type="application/rss+xml" />
<description>%s</description>
<language>fr-be</language>
<lastBuildDate>%s</lastBuildDate>
%s
</channel>
</rss>""" % (e(SITE["nom"]), e(SITE["devise"]), SITE["url"], SITE["url"],
             e(SITE["description"]), SITE["publication_rfc"], "\n".join(items)))

    # llms.txt
    lignes = ["# Vigie", "",
              "> %s" % SITE["devise"], "",
              SITE["description"], "",
              "## Thèse",
              "",
              "La critique habituelle affirme que la finance a échappé au contrôle politique. "
              "Ce site soutient l'inverse : depuis 2022, les mêmes instruments (réserves de change, "
              "messagerie interbancaire, licences d'exportation, droits de douane) sont employés "
              "délibérément comme armes par des États. La finance n'est pas hors de contrôle, "
              "elle est devenue le contrôle. Le déficit n'est pas un déficit d'autorité mais "
              "un déficit d'imputabilité : personne, dans la chaîne, n'est en position de répondre.",
              "",
              "## Dispositif éditorial",
              "",
              "Chaque dossier porte une mention sur une échelle en quatre degrés — imputable, "
              "diluée, déléguée, sans répondant — qui indique qui décide, qui paie et qui répond. "
              "Cette échelle ne note pas la moralité : elle constate l'existence ou l'absence "
              "d'un lieu où demander des comptes.",
              "", "## Dossiers", ""]
    numero = 0
    for partie in PARTIES:
        lignes.append("### %s. %s" % (partie["numero"], partie["titre"]))
        lignes.append("")
        for slug in partie["dossiers"]:
            numero += 1
            d = DOSSIERS[slug]
            lignes.append("- [%02d. %s](%s/dossiers/%s.html) — %s (imputabilité : %s)"
                          % (numero, d["titre"], SITE["url"], slug, d["resume"],
                             IMPUTABILITE[d["imputabilite"]]["nom"].lower()))
        lignes.append("")
    lignes += ["## Pages transversales", "",
               "- [Sommaire](%s/sommaire.html)" % SITE["url"],
               "- [Chronologie](%s/chronologie.html)" % SITE["url"],
               "- [Chiffres](%s/chiffres.html)" % SITE["url"],
               "- [Lexique](%s/lexique.html)" % SITE["url"],
               "- [Sources](%s/sources.html)" % SITE["url"],
               "- [Méthode et limites](%s/methode.html)" % SITE["url"],
               "", "## Documents sources", "",
               "Le corpus de départ est déposé dans le dossier /download du dépôt : %s/tree/main/download"
               % SITE["depot"],
               "", "## Auteur", "",
               "Textes signés Vigie (nom de plume), rédigés avec l'assistance de Claude (Anthropic). "
               "Vérification, choix éditoriaux et publication : l'éditeur du dépôt. Dernière mise à "
               "jour : %s." % SITE["maj"], ""]
    ecrire("llms.txt", "\n".join(lignes))

    ecrire(".nojekyll", "")


def construire_images():
    favicon = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="Vigie">
<rect width="64" height="64" fill="#0d1013"/>
<circle cx="32" cy="34" r="21" fill="none" stroke="#27323a" stroke-width="2"/>
<circle cx="32" cy="34" r="12" fill="none" stroke="#27323a" stroke-width="2"/>
<path d="M32 34 L32 13 A21 21 0 0 1 50.2 23.5 Z" fill="#9fe6a0" opacity="0.85"/>
<circle cx="32" cy="34" r="4" fill="#c3aef5"/>
<path d="M32 34 L52 22" stroke="#c3aef5" stroke-width="2.4" stroke-linecap="round"/>
</svg>"""
    ecrire("favicon.svg", favicon)

    og = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
<defs>
<linearGradient id="l" x1="0" y1="0" x2="1" y2="0">
<stop offset="0" stop-color="#9fe6a0"/><stop offset="1" stop-color="#c3aef5"/>
</linearGradient>
</defs>
<rect width="1200" height="630" fill="#0d1013"/>
<rect x="0" y="0" width="1200" height="6" fill="url(#l)"/>
<g opacity="0.16" stroke="#9fe6a0" fill="none" stroke-width="1.5">
<circle cx="980" cy="330" r="70"/><circle cx="980" cy="330" r="130"/><circle cx="980" cy="330" r="190"/>
<line x1="790" y1="330" x2="1170" y2="330"/><line x1="980" y1="140" x2="980" y2="520"/>
</g>
<path d="M980 330 L980 200 A130 130 0 0 1 1092 265 Z" fill="#9fe6a0" opacity="0.30"/>
<circle cx="980" cy="330" r="9" fill="#c3aef5"/>
<text x="80" y="180" font-family="Georgia, serif" font-size="104" font-weight="700" fill="#e4e9e8">Vigie</text>
<text x="80" y="252" font-family="Helvetica, Arial, sans-serif" font-size="30" fill="#9fe6a0" letter-spacing="1">finance sans conscience</text>
<text x="80" y="296" font-family="Helvetica, Arial, sans-serif" font-size="30" fill="#9fe6a0" letter-spacing="1">n&#8217;est que ruine de l&#8217;humanit&#233;</text>
<text x="80" y="392" font-family="Helvetica, Arial, sans-serif" font-size="23" fill="#a8b3b2">34 dossiers &#183; qui d&#233;cide, qui paie, qui r&#233;pond</text>
<text x="80" y="432" font-family="Helvetica, Arial, sans-serif" font-size="23" fill="#a8b3b2">Une enqu&#234;te sur l&#8217;imputabilit&#233; en finance</text>
<rect x="80" y="500" width="360" height="2" fill="#c3aef5" opacity="0.6"/>
<text x="80" y="546" font-family="Helvetica, Arial, sans-serif" font-size="21" fill="#7c8a89">ouaisfieu.github.io/finance</text>
</svg>"""
    ecrire("og.svg", og)


# --------------------------------------------------------------------------

def principal():
    ordre = index_dossiers()
    usage = {}
    numero = 0
    for partie in PARTIES:
        for slug in partie["dossiers"]:
            numero += 1
            refs = construire_dossier(slug, numero, ordre, partie)
            for n in refs:
                usage.setdefault(n, []).append(slug)

    construire_accueil(ordre)
    construire_sommaire(ordre)
    construire_chronologie()
    construire_chiffres()
    construire_pages_statiques(ordre)
    construire_lexique(ordre)   # après les dossiers : les renvois sont collectés
    construire_sources(usage)
    construire_404()
    construire_annexes(ordre)
    construire_images()

    total = len(ordre) + 7 + len(PAGES_STATIQUES)
    print("Vigie — %d dossiers, %d pages HTML, %d sources, %d termes de lexique."
          % (len(ordre), total, len(SOURCES), len(LEXIQUE)))
    orphelines = [n for n in range(1, len(SOURCES) + 1) if n not in usage]
    if orphelines:
        print("Sources jamais citées dans un dossier : %s" % orphelines)


if __name__ == "__main__":
    principal()
