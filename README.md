# Vigie

> *finance sans conscience n’est que ruine de l’humanité*

Site statique Jamstack — trente-quatre dossiers sur la finance contemporaine, ses instruments de
puissance et l’absence d’un endroit où lui demander des comptes.

Adresse cible : **https://ouaisfieu.github.io/finance/**

---

## Thèse

La critique courante soutient que la finance a échappé au contrôle politique. Les faits de
2022-2026 disent l’inverse : gel de 210 milliards d’euros de réserves d’une banque centrale,
exclusion de banques entières des réseaux de messagerie interbancaire, licence obligatoire dès
0,1 % de terre rare chinoise, droits de douane imposés par décret puis annulés par une cour
suprême. La finance n’est pas hors de contrôle : **elle est devenue le contrôle**, et la chaîne de
commandement ne comprend aucun citoyen.

Le déficit n’est donc pas un déficit d’autorité, mais un **déficit d’imputabilité** : l’absence
d’un lieu où quelqu’un doive répondre de ce qu’il fait.

## Le dispositif éditorial : l’échelle d’imputabilité

Chaque dossier porte une mention en quatre degrés :

| Mention | Ce qu’elle constate | Dossiers |
| --- | --- | --- |
| **Imputable** | Un acteur nommé décide et répond devant un juge, un parlement ou un électorat. | 15 |
| **Diluée** | La décision est réelle mais répartie sur tant d’acteurs qu’aucun n’en répond. | 8 |
| **Déléguée** | La décision est confiée à un tiers privé ou technique sans que la responsabilité suive. | 7 |
| **Sans répondant** | Les personnes affectées n’ont aucun canal pour contester. | 4 |

L’échelle ne note pas la moralité : elle constate l’existence ou l’absence d’une instance. Toute
mention est réfutable — produire l’instance manquante fait monter le dossier d’un degré. Les règles
d’attribution figurent sur `methode.html`.

## Contenu

- **34 dossiers** en 7 parties, environ 33 000 mots
- **110 sources** classées par nature et reliées aux dossiers qui les citent
- **33 termes** de lexique, ancrés depuis les dossiers
- **32 repères** de chronologie, de Sumer à 2028
- **24 indicateurs** datés et sourcés, en `Dataset` JSON-LD
- Accueil, sommaire, chronologie, chiffres, lexique, sources, méthode, 404
- `sitemap.xml`, `robots.txt`, `rss.xml`, `llms.txt`, `og.png`, `og.svg`, `favicon.svg`
- Aucun JavaScript, aucun cookie, aucun traqueur, aucune mesure d’audience
- Thème sombre par défaut (vert tendre et lilas), variante claire si le système la demande,
  feuille d’impression

Seule ressource externe : le lecteur vidéo de la page d’accueil, chargé depuis
`youtube-nocookie.com`. Il peut être bloqué sans conséquence pour le reste du site.

## Documents sources

Le dossier [`/download`](download/) réunit le corpus de départ de l’enquête. Voir
[`download/README.md`](download/README.md) pour la liste des pièces.

Ressources annexes de l’éditeur : <https://dl.ouaisfi.eu/usba/>

## Construire le site

Aucune dépendance à installer. Python 3 suffit.

```sh
python3 tools/build.py     # engendre toutes les pages à la racine
python3 tools/check.py     # contrôle qualité, code de sortie 1 en cas d'erreur
```

Le contrôle vérifie : doctype et langue, un seul `h1` par page, hiérarchie des titres sans saut,
unicité des identifiants, existence de **tous** les liens internes et de **toutes** les ancres,
métadonnées SEO et lien canonique, parsage de chaque bloc JSON-LD, absence de script exécutable et
de ressource externe non déclarée, cohérence de `sitemap.xml`, `rss.xml`, `robots.txt` et
`llms.txt`, protocole et doublons des sources, longueur moyenne des phrases.

Résultat attendu : **42 pages, 0 erreur, 0 avertissement**.

## Modifier le contenu

| Fichier | Contenu |
| --- | --- |
| `tools/contenu.py` | métadonnées du site, sources, lexique, chronologie, indicateurs, page méthode |
| `tools/dossiers_a.py` | parties I (La conscience) et II (La machine) |
| `tools/dossiers_b.py` | parties III (Le gouvernement des grands nombres) et IV (L’arme) |
| `tools/dossiers_c.py` | partie V (La ruine, mesurée) |
| `tools/dossiers_d.py` | parties VI (Les promesses) et VII (Le répondant) |
| `assets/style.css` | feuille de style unique |

Micro-langage de balisage utilisé dans les dossiers :

```
## Titre de section              → h2 avec ancre
### Sous-titre                   → h3 avec ancre
**gras**  *italique*  `code`
[libellé](url)                   → lien
[12]  ou  [12, 45]               → renvoi vers la source numérotée
{{slug}}  ou  {{slug|libellé}}   → renvoi vers le lexique
@@ valeur | libellé ;; …         → bandeau de chiffres  (préfixe « lilas » pour la teinte)
| a | b |                        → tableau, légende optionnelle sur la ligne « ^ … »
:::objection Titre … :::         → encadré (objection, doute, calcul, note)
```

Après toute modification : `python3 tools/build.py && python3 tools/check.py`.

Le rendu est reproductible — aucune date n’est engendrée dynamiquement. Un workflow GitHub Actions
reconstruit le site à chaque poussée et échoue si la sortie ne correspond pas aux sources.

## Régénérer `og.png`

`og.png` est le rendu de `og.svg` en 1200 × 630. Avec un outil de rastérisation :

```sh
rsvg-convert -w 1200 -h 630 og.svg -o og.png
```

À régénérer lorsque le nombre de dossiers ou de sources change.

## Auteur et responsabilité

Textes signés **Vigie**, nom de plume. Rédaction assistée par Claude (Anthropic). Le choix des
angles, la vérification des sources, les arbitrages éditoriaux et la publication relèvent de
l’éditeur du dépôt, qui en répond. Les corrections établies sont appliquées et consignées sur la
page méthode.

Signalements d’erreur : par les *issues* de ce dépôt.
