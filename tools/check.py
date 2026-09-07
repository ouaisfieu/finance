#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vigie — contrôle qualité du site engendré.

Vérifie : doctype et langue, unicité des identifiants, hiérarchie des titres,
existence de tous les liens internes et de toutes les ancres, métadonnées SEO,
validité de chaque bloc JSON-LD, absence de script exécutable et de ressource
externe non déclarée, cohérence du sitemap, du RSS et de robots.txt, longueur
des titres SEO, doublons de sources, protocole des URL.

Usage :  python3 tools/check.py
Sortie :  code 0 si aucune erreur.
"""

import json
import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import urldefrag, unquote

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "tools"))

from contenu import SITE, SOURCES, PARTIES, IMPUTABILITE   # noqa: E402
from dossiers import DOSSIERS                              # noqa: E402

ERREURS = []
AVERTISSEMENTS = []

# Seul appel extérieur toléré, déclaré sur la page méthode et en pied de page.
HOTES_AUTORISES = {"www.youtube-nocookie.com"}


def erreur(fichier, message):
    ERREURS.append("%s : %s" % (fichier, message))


def avertir(fichier, message):
    AVERTISSEMENTS.append("%s : %s" % (fichier, message))


class Analyseur(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.liens = []
        self.titres = []
        self.scripts = []
        self.externes = []
        self.metas = {}
        self.title = None
        self._dans_title = False
        self._script_type = None
        self.jsonld = []
        self._buffer = []
        self.images_sans_alt = 0
        self.iframes = []
        self.lang = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang")
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "a" and "href" in a:
            self.liens.append(a["href"])
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.titres.append(int(tag[1]))
        if tag == "script":
            self._script_type = a.get("type", "text/javascript")
            self.scripts.append(a)
            self._buffer = []
        if tag == "title":
            self._dans_title = True
            self._buffer = []
        if tag == "meta":
            cle = a.get("name") or a.get("property")
            if cle:
                self.metas[cle] = a.get("content", "")
        if tag == "img" and not a.get("alt"):
            self.images_sans_alt += 1
        if tag == "iframe":
            self.iframes.append(a.get("src", ""))
        rel = (a.get("rel") or "").lower()
        for attribut in ("src", "href"):
            valeur = a.get(attribut, "")
            if valeur.startswith("http://") or valeur.startswith("https://"):
                if tag == "link" and rel in ("canonical", "alternate"):
                    continue
                self.externes.append((tag, valeur))
        for cle in a:
            if cle.startswith("on"):
                self.scripts.append({"gestionnaire": cle})

    def handle_endtag(self, tag):
        if tag == "title":
            self.title = "".join(self._buffer).strip()
            self._dans_title = False
            self._buffer = []
        if tag == "script":
            if self._script_type == "application/ld+json":
                self.jsonld.append("".join(self._buffer))
            self._script_type = None
            self._buffer = []

    def handle_data(self, data):
        if self._dans_title or self._script_type:
            self._buffer.append(data)


def fichiers_html():
    for base, _, noms in os.walk(RACINE):
        if ".git" in base or "/tools" in base:
            continue
        for nom in noms:
            if nom.endswith(".html"):
                yield os.path.join(base, nom)


def controler():
    ancres = {}
    pages = {}

    for chemin in sorted(fichiers_html()):
        rel = os.path.relpath(chemin, RACINE)
        contenu = open(chemin, encoding="utf-8").read()

        if not contenu.lstrip().lower().startswith("<!doctype html>"):
            erreur(rel, "doctype manquant")

        p = Analyseur()
        p.feed(contenu)
        pages[rel] = p
        ancres[rel] = set(p.ids)

        # langue
        if p.lang != "fr":
            erreur(rel, "attribut lang absent ou incorrect")

        # titres
        if p.titres.count(1) != 1:
            erreur(rel, "%d balises h1 (une seule attendue)" % p.titres.count(1))
        precedent = 0
        for niveau in p.titres:
            if precedent and niveau > precedent + 1:
                erreur(rel, "saut de niveau de titre : h%d après h%d" % (niveau, precedent))
            precedent = niveau

        # identifiants uniques
        vus = set()
        for ident in p.ids:
            if ident in vus:
                erreur(rel, "identifiant en double : %s" % ident)
            vus.add(ident)

        # métadonnées
        if not p.title:
            erreur(rel, "titre absent")
        elif len(p.title) > 75:
            avertir(rel, "titre de %d caractères (75 conseillés au plus)" % len(p.title))
        for meta in ("description", "og:title", "og:description", "og:image", "twitter:card"):
            if meta not in p.metas or not p.metas[meta]:
                erreur(rel, "métadonnée manquante : %s" % meta)
        if "description" in p.metas and len(p.metas["description"]) > 320:
            avertir(rel, "meta description de %d caractères" % len(p.metas["description"]))
        if 'rel="canonical"' not in contenu:
            erreur(rel, "lien canonique absent")

        # scripts exécutables
        for s in p.scripts:
            if "gestionnaire" in s:
                erreur(rel, "gestionnaire d’événement en ligne : %s" % s["gestionnaire"])
            elif s.get("type") != "application/ld+json":
                erreur(rel, "script exécutable détecté")

        # JSON-LD
        for bloc in p.jsonld:
            try:
                donnees = json.loads(bloc)
            except json.JSONDecodeError as exc:
                erreur(rel, "JSON-LD invalide : %s" % exc)
                continue
            if "@graph" not in donnees:
                erreur(rel, "JSON-LD sans @graph")
            else:
                for objet in donnees["@graph"]:
                    if "@type" not in objet:
                        erreur(rel, "objet JSON-LD sans @type")

        # ressources externes
        for tag, url in p.externes:
            hote = url.split("/")[2] if "//" in url else ""
            if tag in ("script", "link", "img", "iframe") and hote not in HOTES_AUTORISES:
                erreur(rel, "ressource externe non autorisée : %s (%s)" % (url, tag))
            if url.startswith("http://"):
                avertir(rel, "lien en http non sécurisé : %s" % url)

        # iframes
        for src in p.iframes:
            if not src.startswith("https://www.youtube-nocookie.com/"):
                erreur(rel, "iframe non autorisée : %s" % src)

        if p.images_sans_alt:
            erreur(rel, "%d image(s) sans attribut alt" % p.images_sans_alt)

        # balisage résiduel du micro-langage
        for motif, nom in ((r"\{\{[a-z0-9\-]", "terme de lexique non résolu"),
                           (r"(?m)^:::", "encadré non fermé"),
                           (r"(?m)^@@", "bandeau de chiffres non résolu"),
                           (r"\*\*[^*<]{1,60}\*\*", "gras markdown non résolu")):
            if re.search(motif, contenu):
                erreur(rel, nom)

    # liens internes et ancres
    for rel, p in pages.items():
        dossier = os.path.dirname(rel)
        for lien in p.liens:
            if lien.startswith(("http://", "https://", "mailto:", "tel:")):
                continue
            cible, ancre = urldefrag(lien)
            cible = unquote(cible)
            if not cible:
                if ancre and ancre not in ancres[rel]:
                    erreur(rel, "ancre interne inexistante : #%s" % ancre)
                continue
            if cible.startswith("/"):
                chemin_cible = cible.lstrip("/")
                if chemin_cible.startswith("finance/"):
                    chemin_cible = chemin_cible[len("finance/"):]
            else:
                chemin_cible = os.path.normpath(os.path.join(dossier, cible))
            plein = os.path.join(RACINE, chemin_cible)
            if not os.path.exists(plein):
                erreur(rel, "lien interne cassé : %s" % lien)
                continue
            if ancre and chemin_cible in ancres and ancre not in ancres[chemin_cible]:
                erreur(rel, "ancre inexistante dans %s : #%s" % (chemin_cible, ancre))

    # cohérence des annexes
    sitemap = open(os.path.join(RACINE, "sitemap.xml"), encoding="utf-8").read()
    for slug in DOSSIERS:
        if "/dossiers/%s.html" % slug not in sitemap:
            erreur("sitemap.xml", "dossier absent : %s" % slug)
    rss = open(os.path.join(RACINE, "rss.xml"), encoding="utf-8").read()
    for slug in DOSSIERS:
        if "/dossiers/%s.html" % slug not in rss:
            erreur("rss.xml", "dossier absent : %s" % slug)
    robots = open(os.path.join(RACINE, "robots.txt"), encoding="utf-8").read()
    if "Sitemap:" not in robots:
        erreur("robots.txt", "référence au sitemap absente")
    llms = open(os.path.join(RACINE, "llms.txt"), encoding="utf-8").read()
    for slug in DOSSIERS:
        if slug not in llms:
            erreur("llms.txt", "dossier absent : %s" % slug)

    # sources
    urls = {}
    for i, s in enumerate(SOURCES, 1):
        if not s["url"].startswith("https://"):
            avertir("sources", "source %d : URL non sécurisée (%s)" % (i, s["url"]))
        urls.setdefault(s["url"], []).append(i)
        for champ in ("auteur", "titre", "editeur", "date", "nature"):
            if not s.get(champ):
                erreur("sources", "source %d : champ %s vide" % (i, champ))
    for url, indices in urls.items():
        if len(indices) > 1:
            avertir("sources", "URL répétée aux entrées %s : %s" % (indices, url))

    # cohérence du plan
    annonces = [s for partie in PARTIES for s in partie["dossiers"]]
    if len(annonces) != len(set(annonces)):
        erreur("plan", "un dossier figure dans plusieurs parties")
    if set(annonces) != set(DOSSIERS):
        erreur("plan", "écart entre les dossiers annoncés et les dossiers écrits")
    for slug, d in DOSSIERS.items():
        if d["imputabilite"] not in IMPUTABILITE:
            erreur(slug, "mention d’imputabilité inconnue : %s" % d["imputabilite"])
        if len(d["seo_titre"]) > 72:
            avertir(slug, "seo_titre de %d caractères" % len(d["seo_titre"]))
        if len(d["resume"]) < 40:
            avertir(slug, "résumé trop court")
        if not d.get("faq"):
            avertir(slug, "aucune question fréquente")

    # longueur moyenne des phrases (lisibilité)
    total_mots = total_phrases = 0
    for d in DOSSIERS.values():
        texte = re.sub(r"[|@:*`\[\]{}#-]", " ", d["corps"])
        phrases = [p for p in re.split(r"[.!?]+\s", texte) if len(p.split()) > 2]
        total_phrases += len(phrases)
        total_mots += sum(len(p.split()) for p in phrases)
    moyenne = total_mots / max(total_phrases, 1)
    if moyenne > 26:
        avertir("lisibilité", "phrase moyenne de %.1f mots" % moyenne)

    print("Vigie — contrôle : %d pages HTML, %d dossiers, %d sources."
          % (len(pages), len(DOSSIERS), len(SOURCES)))
    print("Longueur moyenne des phrases : %.1f mots." % moyenne)
    for a in AVERTISSEMENTS:
        print("  avertissement — %s" % a)
    for e in ERREURS:
        print("  ERREUR — %s" % e)
    print("Résultat : %d erreur(s), %d avertissement(s)." % (len(ERREURS), len(AVERTISSEMENTS)))
    return 1 if ERREURS else 0


if __name__ == "__main__":
    sys.exit(controler())
