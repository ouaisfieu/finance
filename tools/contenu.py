# -*- coding: utf-8 -*-
"""Vigie — métadonnées, sources, lexique, chronologie, indicateurs, pages transversales."""

SITE = {
    "nom": "Vigie",
    "devise": "finance sans conscience n’est que ruine de l’humanité",
    "url": "https://ouaisfieu.github.io/finance",
    "depot": "https://github.com/ouaisfieu/finance",
    "usba": "https://dl.ouaisfi.eu/usba/",
    "auteur": "Vigie",
    "seo_titre": "Vigie — finance sans conscience n’est que ruine de l’humanité",
    "description": (
        "Trente-quatre dossiers sur la finance contemporaine : non pas une machine hors de "
        "contrôle, mais un instrument de contrôle sans personne pour en répondre. Chiffres datés, "
        "sources croisées, échelle d’imputabilité."),
    "mots_cles": [
        "finance sans conscience", "imputabilité", "financiarisation", "guerre économique",
        "sanctions", "avoirs russes gelés", "Euroclear", "finance durable", "SFDR", "CSRD",
        "Rabelais", "chrématistique", "Polanyi", "banques éthiques", "Belgique"],
    "og_alt": "Vigie — une enquête sur l’imputabilité en finance, 34 dossiers.",
    "publication": "2026-09-07",
    "publication_rfc": "Mon, 07 Sep 2026 09:00:00 +0200",
    "maj": "7 septembre 2026",
    "maj_iso": "2026-09-07",
    "navigation": [
        ("index.html", "Accueil"),
        ("sommaire.html", "Dossiers"),
        ("chronologie.html", "Chronologie"),
        ("chiffres.html", "Chiffres"),
        ("lexique.html", "Lexique"),
        ("sources.html", "Sources"),
        ("methode.html", "Méthode"),
    ],
    "video_id": "rGJVVBKwqSQ",
    "video_titre": "Vidéo mise en avant par l’éditeur — le point de départ de l’enquête",
    "video_description": (
        "Vidéo choisie par l’éditeur comme point de départ de l’enquête Vigie sur la finance "
        "et la conscience."),
    "video_texte": (
        "Cette vidéo est le point de départ retenu par l’éditeur. Elle n’est pas une source "
        "au sens où l’entend ce site : rien de ce qui suit n’en dépend, et aucun chiffre n’en "
        "est tiré. Elle donne le ton d’une question — que vaut une technique qui ne répond de "
        "rien — que les trente-quatre dossiers essaient ensuite d’instruire pièce par pièce."),
}

# ---------------------------------------------------------------------------
# échelle d'imputabilité — le dispositif éditorial propre à ce site
# ---------------------------------------------------------------------------

IMPUTABILITE = {
    "imputable": {
        "rang": 1, "nom": "Imputable",
        "definition": "Un acteur nommé décide, et il répond devant un juge, un parlement ou un électorat.",
    },
    "diluee": {
        "rang": 2, "nom": "Diluée",
        "definition": "La décision est réelle mais répartie sur tant d’acteurs que plus personne n’en répond.",
    },
    "deleguee": {
        "rang": 3, "nom": "Déléguée",
        "definition": "La décision a été confiée à un tiers privé ou technique sans que la responsabilité suive.",
    },
    "sans-repondant": {
        "rang": 4, "nom": "Sans répondant",
        "definition": "La décision produit ses effets sur des personnes qui n’ont aucun canal pour la contester.",
    },
}

# ---------------------------------------------------------------------------
# plan
# ---------------------------------------------------------------------------

PARTIES = [
    {
        "numero": "I", "slug": "partie-la-conscience", "titre": "La conscience",
        "note": "Ce que dit vraiment la phrase de Rabelais, ce que dit Aristote, et pourquoi le "
                "récit d’une monnaie née du commerce pacifique est faux.",
        "dossiers": ["rabelais-et-la-finance", "oikonomia-et-chrematistique",
                     "le-mythe-du-troc", "le-desencastrement"],
    },
    {
        "numero": "II", "slug": "partie-la-machine", "titre": "La machine",
        "note": "Comment la valeur est définie, à qui elle revient, et à quelle vitesse elle circule.",
        "dossiers": ["la-frontiere-de-la-production", "la-doctrine-friedman",
                     "les-rachats-d-actions", "la-vitesse", "les-produits-derives"],
    },
    {
        "numero": "III", "slug": "partie-le-gouvernement", "titre": "Le gouvernement des grands nombres",
        "note": "Qui décide réellement de l’allocation du capital : trois gestionnaires, "
                "quelques indices, trois agences, une norme comptable, deux banques centrales.",
        "dossiers": ["les-trois-gestionnaires", "l-indice-comme-legislateur",
                     "les-agences-de-notation", "la-gouvernance-par-les-nombres",
                     "la-banque-centrale-et-le-marche"],
    },
    {
        "numero": "IV", "slug": "partie-l-arme", "titre": "L’arme",
        "note": "La finance comme instrument de puissance : généalogie, effets sur les civils, "
                "et le dossier belge des avoirs immobilisés.",
        "dossiers": ["l-interdependance-retournee", "l-arme-economique-1914",
                     "les-sanctions-et-les-civils", "les-avoirs-geles", "les-tarifs-et-la-loi"],
    },
    {
        "numero": "V", "slug": "partie-la-ruine", "titre": "La ruine, mesurée",
        "note": "Ce que l’on peut chiffrer : concentration, financement fossile, actifs échoués, "
                "matière extraite, dette.",
        "dossiers": ["la-concentration", "le-financement-du-chaos", "la-bulle-carbone",
                     "le-decouplage-introuvable", "la-dette"],
    },
    {
        "numero": "VI", "slug": "partie-les-promesses", "titre": "Les promesses",
        "note": "Ce que la régulation européenne a produit — puis défait — entre 2021 et 2026.",
        "dossiers": ["la-double-materialite", "l-omnibus", "sfdr-et-l-etiquette",
                     "la-fin-des-alliances"],
    },
    {
        "numero": "VII", "slug": "partie-le-repondant", "titre": "Le répondant",
        "note": "Ce qui rétablit un endroit où demander des comptes — et ce que cela coûte.",
        "dossiers": ["la-banque-que-l-on-choisit", "la-finance-solidaire",
                     "la-monnaie-que-l-on-fait", "les-communs", "taxer-le-mouvement", "verdict"],
    },
]

# ---------------------------------------------------------------------------
# sources — numérotation unique, utilisée par les renvois [n] dans tout le site
# ---------------------------------------------------------------------------

def _s(auteur, titre, editeur, date, url, nature):
    return {"auteur": auteur, "titre": titre, "editeur": editeur,
            "date": date, "url": url, "nature": nature}


SOURCES = [
    # --- 1 à 12 : philosophie, anthropologie, histoire ---
    _s("François Rabelais", "Pantagruel, chapitre VIII (lettre de Gargantua)", "1532",
       "1532", "https://fr.wikisource.org/wiki/Pantagruel/%C3%89dition_Marty-Laveaux/Chapitre_8",
       "Textes classiques"),
    _s("Aristote", "Politique, livre I, et Éthique à Nicomaque, livre V",
       "IVe siècle av. J.-C.", "IVe s. av. J.-C.",
       "https://fr.wikisource.org/wiki/Politique_(Aristote)", "Textes classiques"),
    _s("Caroline Humphrey", "Barter and Economic Disintegration", "Man (RAI), vol. 20 n° 1",
       "1985", "https://www.jstor.org/stable/2802221", "Recherche"),
    _s("David Graeber", "Debt: The First 5,000 Years", "Melville House",
       "2011", "https://en.wikipedia.org/wiki/Debt:_The_First_5,000_Years", "Ouvrages"),
    _s("Michael Hudson", "…and forgive them their debts", "ISLET",
       "2018", "https://michael-hudson.com/books/and-forgive-them-their-debts/", "Ouvrages"),
    _s("Georg Friedrich Knapp", "The State Theory of Money", "Macmillan (éd. angl.)",
       "1905 / 1924", "https://archive.org/details/in.ernet.dli.2015.271375", "Textes classiques"),
    _s("Karl Polanyi", "La Grande Transformation", "Gallimard (éd. fr.)",
       "1944", "https://fr.wikipedia.org/wiki/La_Grande_Transformation", "Ouvrages"),
    _s("Karl Marx", "Le Capital, livre I, chapitre I, § 4 — le fétichisme de la marchandise",
       "1867", "1867", "https://fr.wikipedia.org/wiki/F%C3%A9tichisme_de_la_marchandise",
       "Textes classiques"),
    _s("Ivan Illich", "La Convivialité", "Seuil",
       "1973", "https://www.editionspoints.com/ouvrage/la-convivialite-ivan-illich/9782757891223",
       "Ouvrages"),
    _s("Alain Supiot", "La Gouvernance par les nombres — cours au Collège de France", "Fayard",
       "2015", "https://www.college-de-france.fr/fr/agenda/cours/du-gouvernement-par-les-lois-la-gouvernance-par-les-nombres",
       "Ouvrages"),
    _s("Bernard Stiegler", "La Société automatique — l’avenir du travail", "Fayard",
       "2015", "https://www.actu-philosophia.com/bernard-stiegler-ce-qui-fait-que-la-vie-vaut-la-308/",
       "Ouvrages"),
    _s("Nicholas Mulder", "The Economic Weapon: The Rise of Sanctions as a Tool of Modern War",
       "Yale University Press", "2022", "https://yalebooks.yale.edu/book/9780300259360/the-economic-weapon/",
       "Ouvrages"),

    # --- 13 à 22 : théorie économique contemporaine ---
    _s("Mariana Mazzucato", "The Value of Everything: Making and Taking in the Global Economy",
       "Allen Lane", "2018", "https://marianamazzucato.com/books/the-value-of-everything/",
       "Ouvrages"),
    _s("Milton Friedman", "The Social Responsibility of Business Is to Increase Its Profits",
       "The New York Times Magazine", "13 septembre 1970",
       "https://en.wikipedia.org/wiki/Friedman_doctrine", "Textes classiques"),
    _s("Oliver Hart et Luigi Zingales", "Companies Should Maximize Shareholder Welfare Not Market Value",
       "Journal of Law, Finance, and Accounting", "2017",
       "https://www.chicagobooth.edu/review/its-time-rethink-milton-friedmans-shareholder-value-argument",
       "Recherche"),
    _s("World Inequality Lab", "World Inequality Report 2026", "WID.world",
       "décembre 2025", "https://wir2026.wid.world/insight/executive-summary/", "Recherche"),
    _s("Kate Raworth", "Doughnut Economics: Seven Ways to Think Like a 21st-Century Economist",
       "Random House", "2017", "https://doughnuteconomics.org/about-doughnut-economics", "Ouvrages"),
    _s("Herman Daly, à la suite de Nicholas Georgescu-Roegen",
       "Steady-State Economics et la loi d’entropie appliquée au processus économique",
       "Island Press", "1977 / 1971",
       "https://www.veblen-institute.org/IMG/pdf/croissance_non_economique_victor-1.pdf", "Ouvrages"),
    _s("Tim Jackson", "Prospérité sans croissance", "De Boeck",
       "2009 / 2017", "https://journals.openedition.org/nrt/19964", "Ouvrages"),
    _s("Jason Hickel", "Less is More: How Degrowth Will Save the World", "William Heinemann",
       "2020", "https://www.jasonhickel.org/less-is-more", "Ouvrages"),
    _s("Henry Farrell et Abraham Newman", "Weaponized Interdependence: How Global Economic Networks "
       "Shape State Coercion", "International Security, vol. 44 n° 1", "2019",
       "https://direct.mit.edu/isec/article/44/1/42/12237/Weaponized-Interdependence-How-Global-Economic",
       "Recherche"),
    _s("Antonio Sánchez Serrano", "High-Frequency Trading and Systemic Risk: A Structured Review of "
       "Findings and Policies", "Review of Economics, vol. 71 n° 3", "2020",
       "https://www.degruyterbrill.com/document/doi/10.1515/roe-2020-0028/html", "Recherche"),

    # --- 23 à 36 : institutions financières et données macroéconomiques ---
    _s("Institute of International Finance", "Global Debt Monitor — dette mondiale au 1er trimestre 2026",
       "IIF", "21 mai 2026",
       "https://www.iif.com/Publications/ID/6581/IIF-Global-Debt-Monitor-Key-Takeaways-and-Views-from-our-Experts",
       "Institutions et données"),
    _s("Fonds monétaire international", "Perspectives de l’économie mondiale, avril 2026", "FMI",
       "avril 2026", "https://www.imf.org/fr/publications/weo/issues/2026/04/14/world-economic-outlook-april-2026",
       "Institutions et données"),
    _s("Marijn Bolhuis, Jiaqian Chen, Benjamin Kett (FMI)", "Les coûts de la fragmentation géoéconomique",
       "Finances & Développement", "juin 2023",
       "https://www.imf.org/fr/publications/fandd/issues/2023/06/the-costs-of-geoeconomic-fragmentation-bolhuis-chen-kett",
       "Institutions et données"),
    _s("Banque des règlements internationaux", "OTC derivatives statistics at end-June 2025", "BRI",
       "8 décembre 2025", "https://www.bis.org/publ/otc_hy2512.htm", "Institutions et données"),
    _s("ISDA", "Key Trends in the Size and Composition of OTC Derivatives Markets, H2 2025", "ISDA",
       "9 juillet 2026", "https://www.isda.org/2026/07/09/key-trends-in-the-size-and-composition-of-otc-derivatives-markets-in-the-second-half-of-2025/",
       "Professionnels du secteur"),
    _s("Iñaki Aldasoro, Sebastian Doerr, Daniel Rees (BRI)",
       "Financing the AI boom: cash flows, debt and the shifting risk landscape, BIS Bulletin n° 120",
       "Banque des règlements internationaux", "7 janvier 2026",
       "https://www.bis.org/publ/bisbull120.htm", "Institutions et données"),
    _s("Conseil de stabilité financière", "Report on Vulnerabilities in Private Credit", "FSB",
       "6 mai 2026", "https://www.fsb.org/2026/05/report-on-vulnerabilities-in-private-credit/",
       "Institutions et données"),
    _s("Banque centrale européenne", "La BCE fait avancer ses travaux sur le climat et la nature",
       "BCE", "16 janvier 2026",
       "https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.pr260116~4b4a05a179.fr.html",
       "Institutions et données"),
    _s("Institut Veblen", "Stabilité par la durabilité — trois recommandations pour la révision du "
       "cadre de garanties de l’Eurosystème", "Institut Veblen", "2024",
       "https://www.veblen-institute.org/Stabilite-par-la-durabilite-Trois-recommandations-pour-la-revision-de-la.html",
       "ONG et société civile"),
    _s("Toute l’Europe", "Six questions sur l’euro numérique", "Toute l’Europe", "2026",
       "https://www.touteleurope.eu/economie-et-social/argent-six-questions-sur-l-euro-numerique/",
       "Presse"),
    _s("Association française des trésoriers d’entreprise",
       "Le Parlement européen valide le lancement de l’euro numérique", "AFTE", "juin 2026",
       "https://www.afte.com/publication/actualites/le-parlement-europeen-valide-le-lancement-de-leuro-numerique",
       "Professionnels du secteur"),
    _s("France Épargne", "Dernière réunion de Jerome Powell à la Fed : quatre dissidences, "
       "taux inchangés", "France Épargne", "avril 2026",
       "https://www.france-epargne.fr/news/powell-derniere-reunion-fed-4-dissidents-gouverneur-2028",
       "Presse"),
    _s("BestBrokers, d’après les données COFER du FMI",
       "Part du dollar dans les réserves de change mondiales, 1er trimestre 2026", "BestBrokers",
       "2026", "https://www.bestbrokers.com/forex-trading/us-dollar-share-of-global-currency-reserves/",
       "Institutions et données"),
    _s("Conseil d’analyse économique", "La crise des subprimes (rapport n° 78)",
       "La Documentation française", "2008", "https://cae-eco.fr/static/pdf/078.pdf", "Recherche"),

    # --- 37 à 50 : climat, matière, énergie ---
    _s("Rainforest Action Network, Reclaim Finance, BankTrack, Oil Change International, Sierra Club, "
       "Indigenous Environmental Network", "Banking on Climate Chaos 2026", "BOCC", "9 juin 2026",
       "https://www.bankingonclimatechaos.org/", "ONG et société civile"),
    _s("Reclaim Finance", "Global banks financed fossil fuels with $8.7 trillion since the Paris "
       "Agreement", "Reclaim Finance", "9 juin 2026",
       "https://reclaimfinance.org/site/en/2026/06/09/global-banks-financed-fossil-fuels-with-8-7-trillion-since-the-paris-agreement/",
       "ONG et société civile"),
    _s("Fédération bancaire française", "Réaction de la FBF au rapport Banking on Climate Chaos",
       "FBF", "2025", "https://www.fbf.fr/fr/reaction-de-la-fbf-au-rapport-banking-on-climate-chaos-publie-par-un-consortium-dong/",
       "Professionnels du secteur"),
    _s("InfluenceMap", "Carbon Majors: 2025 Data Update", "InfluenceMap", "5 mars 2025",
       "https://influencemap.org/pressrelease/Carbon-Majors-2025-Update-31826", "ONG et société civile"),
    _s("Carbon Tracker Initiative", "Unburnable Carbon et Stranded Assets", "Carbon Tracker",
       "2013-2014", "https://carbontracker.org/reports/unburnable-carbon-wasted-capital-and-stranded-assets/",
       "ONG et société civile"),
    _s("Agence internationale de l’énergie", "Net Zero by 2050 — a Roadmap for the Global Energy "
       "Sector", "AIE", "2021 (mise à jour 2023)", "https://www.iea.org/reports/net-zero-by-2050",
       "Institutions et données"),
    _s("Programme des Nations unies pour l’environnement", "Global Resources Outlook 2024", "PNUE",
       "2024", "https://www.unep.org/resources/Global-Resource-Outlook-2024", "Institutions et données"),
    _s("Circle Economy", "Circularity Gap Report 2026", "Circle Economy", "2026",
       "https://circularintelligence.io/resources/insights/circularity-gap-2026", "ONG et société civile"),
    _s("Stockholm Resilience Centre / Potsdam Institute", "Planetary Health Check 2025",
       "Stockholm Resilience Centre", "2025",
       "https://www.stockholmresilience.org/research/planetary-boundaries.html", "Recherche"),
    _s("Global Footprint Network", "Earth Overshoot Day 2026 tombe le 30 juillet",
       "Global Footprint Network", "juin 2026",
       "https://overshoot.footprintnetwork.org/newsroom/press-release-june-2026-english/",
       "ONG et société civile"),
    _s("European Environmental Bureau", "Decoupling Debunked", "EEB", "juillet 2019",
       "https://eeb.org/wp-content/uploads/2019/07/Decoupling-Debunked.pdf", "ONG et société civile"),
    _s("Fonds monétaire international", "The Generalized Jevons Paradox and the Future of Energy "
       "(WP/2026/157)", "FMI", "2026",
       "https://www.imf.org/-/media/files/publications/wp/2026/english/wpiea2026157-source-pdf.pdf",
       "Recherche"),
    _s("UBS", "Global Wealth Report 2026", "UBS", "30 juin 2026",
       "https://www.ubs.com/global/en/media/display-page-ndp/en-20260630-gwr-2026.html",
       "Professionnels du secteur"),
    _s("The Guardian", "Just 0.001% hold three times the wealth of poorest half of humanity",
       "The Guardian", "10 décembre 2025",
       "https://www.theguardian.com/inequality/2025/dec/10/just-0001-hold-three-times-the-wealth-of-poorest-half-of-humanity-report-finds",
       "Presse"),

    # --- 51 à 62 : régulation européenne ---
    _s("Union européenne", "Directive « Omnibus I » modifiant la CSRD et la CS3D — publication au "
       "Journal officiel", "Journal officiel de l’Union européenne", "26 février 2026",
       "https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=OJ:L_202600473", "Institutions et données"),
    _s("WeCount", "Omnibus CSRD et CS3D : les derniers éléments à retenir", "WeCount", "2026",
       "https://www.wecount.io/ressources-articles/csrd-omnibus", "Professionnels du secteur"),
    _s("Commission européenne", "Sustainability-related disclosure in the financial services sector "
       "(SFDR)", "Commission européenne", "2026",
       "https://finance.ec.europa.eu/sustainable-finance/disclosures/sustainability-related-disclosure-financial-services-sector_en",
       "Institutions et données"),
    _s("Paul Hastings", "SFDR II: Negotiations Continue as European Parliament Vote Slips to September",
       "Paul Hastings", "août 2026",
       "https://www.paulhastings.com/insights/client-alerts/sfdr-ii-negotiations-continue-as-european-parliament-vote-slips-to-september",
       "Professionnels du secteur"),
    _s("Morrison Foerster", "EU Sustainable Finance: Council Agrees Negotiating Mandate for SFDR 2.0",
       "Morrison Foerster", "29 juin 2026",
       "https://www.mofo.com/resources/insights/260629-eu-sustainable-finance-council-agrees-negotiating-mandate",
       "Professionnels du secteur"),
    _s("IEEFA", "SFDR 2.0: Making labels work for the consumer", "IEEFA", "2026",
       "https://ieefa.org/resources/sfdr-20-making-labels-work-consumer", "ONG et société civile"),
    _s("Autorité des marchés financiers", "Proposition de critères minimaux environnementaux pour les "
       "produits financiers", "AMF", "2025",
       "https://www.amf-france.org/fr/actualites-publications/positions-ue-de-lamf/proposition-de-criteres-minimaux-environnementaux-pour-les-produits-financiers-des-categories-art9",
       "Institutions et données"),
    _s("Reclaim Finance", "Directive sur le devoir de vigilance : une occasion manquée pour la finance",
       "Reclaim Finance", "26 avril 2024",
       "https://reclaimfinance.org/site/2024/04/26/directive-sur-le-devoir-de-vigilance-une-occasion-manquee-pour-la-finance/",
       "ONG et société civile"),
    _s("Reclaim Finance", "SFDR : la Commission européenne acte la contradiction entre expansion "
       "fossile et transition", "Reclaim Finance", "20 novembre 2025",
       "https://reclaimfinance.org/site/2025/11/20/sfdr-la-commission-europeenne-acte-la-contradiction-entre-expansion-fossile-et-transition/",
       "ONG et société civile"),
    _s("ESG Today", "Net-Zero Banking Alliance Ceases Operations", "ESG Today", "octobre 2025",
       "https://www.esgtoday.com/net-zero-banking-alliance-ceases-operations/", "Presse"),
    _s("Global Trade Review", "Net Zero Banking Alliance closure shows hurdle of setting single "
       "standards", "GTR", "2025",
       "https://www.gtreview.com/news/sustainability/net-zero-banking-alliance-closure-shows-hurdle-of-setting-single-standards-industry-body-says/",
       "Presse"),
    _s("Chaire Double Matérialité", "La double matérialité dans le monde", "Chaire Double Matérialité",
       "février 2025", "https://chaire-double-materialite.org/La_Double_Materialite_dans_le_monde_RAPPORT_FEV2025.pdf",
       "Recherche"),

    # --- 63 à 74 : guerre économique ---
    _s("The World Data", "US Sanctions Statistics 2026", "The World Data", "2026",
       "https://theworlddata.com/us-sanctions-statistics/", "Institutions et données"),
    _s("LCB-FT.fr", "Le 20e paquet de sanctions de l’Union européenne contre la Russie", "LCB-FT.fr",
       "23 avril 2026", "https://www.lcb-ft.fr/news/ue-20eme-paquet-sanctions-russie", "Presse"),
    _s("Le Grand Continent", "La Cour suprême déclare illégaux les droits de douane IEEPA",
       "Le Grand Continent", "20 février 2026",
       "https://legrandcontinent.eu/fr/2026/02/20/la-plus-importante-defaite-juridique-de-trump-la-cour-supreme-declare-illegales-les-droits-de-douane-ieepa/",
       "Presse"),
    _s("KPMG Avocats", "Droits de douane américains : décision historique de la Cour suprême", "KPMG",
       "février 2026", "https://kpmg.com/fr/fr/articles/juridique/droits-de-douane-usa-decision-cour-supreme.html",
       "Professionnels du secteur"),
    _s("Le Grand Continent", "Restrictions à l’exportation des terres rares et droits de douane : "
       "comprendre l’escalade entre la Chine et les États-Unis", "Le Grand Continent",
       "12 octobre 2025",
       "https://legrandcontinent.eu/fr/2025/10/12/restrictions-a-lexportation-des-terres-rares-et-droits-de-douane-comprendre-lescalade-entre-la-chine-et-les-etats-unis/",
       "Presse"),
    _s("Peterson Institute for International Economics", "Four years into the trade war, are the US "
       "and China decoupling?", "PIIE", "2022",
       "https://www.piie.com/blogs/realtime-economics/2022/four-years-trade-war-are-us-and-china-decoupling",
       "Recherche"),
    _s("Pablo Fajgelbaum et alii", "The Economic Impacts of the US-China Trade War (NBER w29315)",
       "National Bureau of Economic Research", "2021",
       "https://www.nber.org/system/files/working_papers/w29315/w29315.pdf", "Recherche"),
    _s("Carnegie Endowment for International Peace", "How Trump’s Tariffs Really Affected the U.S. "
       "Job Market", "Carnegie", "janvier 2021",
       "https://carnegieendowment.org/china-financial-markets/2021/01/how-trumps-tariffs-really-affected-the-us-job-market",
       "Recherche"),
    _s("Kevin Kim et alii", "The Violence of Non-Violence: A Systematic Mixed-Studies Review on the "
       "Health Effects of Sanctions", "PMC / International Journal of Health Services", "2023",
       "https://pmc.ncbi.nlm.nih.gov/articles/PMC9975820/", "Recherche"),
    _s("Humanity: An International Journal of Human Rights",
       "Studying the Impacts of Economic Sanctions in Iran: Everyday Life, Power, and Foreign Policy",
       "Humanity Journal", "2024",
       "https://humanityjournal.org/wp-content/uploads/2024/01/Iran-Dossier-Intro.pdf", "Recherche"),
    _s("Africa Is a Country", "Sanctions as civilizational warfare", "Africa Is a Country",
       "mai 2025", "https://africasacountry.com/2025/05/sanctions-as-civilizational-warfare",
       "Presse"),
    _s("Conseil de l’Union européenne", "Impact of sanctions on the Russian economy", "Consilium",
       "2026", "https://www.consilium.europa.eu/en/infographics/impact-sanctions-russian-economy/",
       "Institutions et données"),

    # --- 75 à 86 : Belgique ---
    _s("La Libre Belgique", "Pourquoi la question de l’utilisation des avoirs russes immobilisés "
       "revient à l’agenda européen", "La Libre", "1er septembre 2026",
       "https://www.lalibre.be/international/europe/2026/09/01/pourquoi-la-question-de-lutilisation-des-avoirs-russes-immobilises-pour-lukraine-revient-maintenant-a-lagenda-europeen-IVOK2XQDPND63CJ6W2EQHJECVU/",
       "Presse"),
    _s("La Libre Belgique", "Bart De Wever obtient une victoire au sommet européen, avec l’abandon "
       "du plan de financement par les actifs russes", "La Libre", "19 décembre 2025",
       "https://www.lalibre.be/international/europe/2025/12/19/bart-de-wever-obtient-une-victoire-au-sommet-europeen-avec-labandon-du-plan-pour-renflouer-lukraine-avec-les-actifs-russes-immobilises-dans-lue-F2TDL6IYQVD47HZKALHCKZWAMY/",
       "Presse"),
    _s("La Libre Belgique", "Euroclear va distribuer à l’Europe 1,4 milliard d’euros venant des "
       "avoirs russes en dépôt", "La Libre", "8 mai 2026",
       "https://www.lalibre.be/economie/entreprises-startup/2026/05/08/euroclear-va-distribuer-a-leurope-14-milliard-deuros-venant-des-avoirs-russes-en-depot-22F7LSB62BHKNPZ53ABAWCFPCM/",
       "Presse"),
    _s("La Libre Belgique / Belga", "Un tribunal en Russie condamne Euroclear à verser 250 milliards "
       "de dollars", "La Libre", "15 mai 2026",
       "https://www.lalibre.be/dernieres-depeches/2026/05/15/avoirs-russes-geles-un-tribunal-en-russie-condamne-euroclear-a-verser-250-milliards-de-dollars-KWEEU3VASVE7PKOR3N53NT7HLM/",
       "Presse"),
    _s("RTBF", "Avoirs russes immobilisés chez Euroclear : « la solution sur la table n’est pas "
       "réaliste », selon la directrice générale d’Euroclear", "RTBF", "2026",
       "https://www.rtbf.be/article/utiliser-les-avoirs-russes-immobilises-chez-euroclear-la-solution-sur-la-table-n-est-pas-realiste-11642949",
       "Presse"),
    _s("Bureau fédéral du Plan", "Perspectives économiques 2026-2031", "Bureau fédéral du Plan",
       "juin 2026", "https://www.plan.be/publications/", "Institutions et données"),
    _s("21News", "Vers une dette publique de 122 % du PIB", "21News", "13 juin 2026",
       "https://www.21news.be/vers-une-dette-publique-de-122-du-pib-la-belgique-fonce-droit-dans-le-mur/",
       "Presse"),
    _s("La Libre Belgique", "La dette belge coûtera près de 21 milliards par an d’ici 2030",
       "La Libre", "30 janvier 2026",
       "https://www.lalibre.be/economie/conjoncture/2026/01/30/la-dette-belge-coutera-pres-de-21-milliards-par-an-dici-2030-4KVCAMFYKJHATH5R6YVXEU2Y24/",
       "Presse"),
    _s("Financité et FairFin", "Scan des banques 2026 : le fossé entre les banques durables et les "
       "grandes banques continue de se creuser", "Financité", "31 mars 2026",
       "https://www.financite.be/actualit%C3%A9/scan-des-banques-le-fosse-entre-les-banques-durables-et-les-grandes-banques-continue-de",
       "ONG et société civile"),
    _s("Trends-Tendances", "Scan des banques : les grandes institutions belges à la traîne",
       "Trends-Tendances", "31 mars 2026",
       "https://trends.levif.be/a-la-une/banque/scan-des-banques-les-grandes-institutions-belges-a-la-traine/",
       "Presse"),
    _s("Financité", "Label Finance solidaire — critères et baromètre", "Financité", "2025-2026",
       "https://labelfinancesolidaire.be/a-propos-du-label/", "ONG et société civile"),
    _s("Fédération européenne des banques éthiques et alternatives", "Présentation et membres",
       "FEBEA", "2026", "https://febea.org/", "ONG et société civile"),

    # --- 87 à 98 : alternatives, coopératives, monnaies ---
    _s("La Nef", "Rapport d’activité et indépendance réglementaire", "La Nef", "2024-2026",
       "https://www.lanef.com/", "Professionnels du secteur"),
    _s("Triodos Bank", "Politique d’investissement et exclusions", "Triodos", "2026",
       "https://www.triodos.be/fr/banque-durable", "Professionnels du secteur"),
    _s("vdk bank", "Scan des banques FairFin et Financité : vdk renforce sa position", "vdk", "2026",
       "https://www.vdk.be/fr/scan-des-banques-fairfin-et-financite-vdk-banque-renforce-sa-position-de-banque-durable",
       "Professionnels du secteur"),
    _s("Zinne asbl", "La monnaie locale citoyenne bruxelloise — réseau et comptoirs", "Zinne", "2026",
       "https://www.zinne.brussels/", "ONG et société civile"),
    _s("FAIR — Finance à impact social", "Baromètre de la finance solidaire 2026", "FAIR",
       "24 juin 2026",
       "https://www.finance-fair.org/fr/actualites/barometre-de-la-finance-solidaire-2026-les-francais-donnent-de-plus-en-plus-de-sens-leur",
       "ONG et société civile"),
    _s("Community Land Trust Bruxelles", "Le modèle du CLT : dissociation du sol et du bâti",
       "CLTB", "2012-2026", "https://www.cltweb.org/fr/bibliotheque-de-ressources/etudes-de-cas-clt/community-land-trust-bruxelles/",
       "ONG et société civile"),
    _s("SMart", "Rapport spécial sur la réalisation du but social", "SmartCoop", "2020",
       "https://smartbe.be/wp-content/uploads/2020/06/BE_SmartCoop_AGE-20_Rapport_special_realisation_but_social.pdf",
       "Professionnels du secteur"),
    _s("CRISP", "NewB : ambitions et revers d’une banque coopérative", "Courrier hebdomadaire du "
       "CRISP", "2020", "https://shs.cairn.info/article/CRIS_2676_0005", "Recherche"),
    _s("Alliance coopérative internationale", "Facts and figures — le poids mondial des coopératives",
       "ICA", "2023-2026", "https://ica.coop/en/cooperatives/facts-and-figures",
       "Institutions et données"),
    _s("Repair Together", "Réseau des Repair Cafés en Belgique", "Repair Together", "2026",
       "https://repairtogether.be/", "ONG et société civile"),
    _s("Business AM", "La Wallonie et Bruxelles disposent désormais de 16 monnaies locales",
       "Business AM", "2021",
       "https://fr.businessam.be/la-wallonie-et-bruxelles-disposent-desormais-de-16-monnaies-locales-et-elles-ont-le-vent-en-poupe-aussi-sur-smartphone/",
       "Presse"),
    _s("Crédal", "Microcrédit et financement de l’économie sociale", "Crédal", "2026",
       "https://www.credal.be/", "Professionnels du secteur"),

    # --- 99 à 108 : gestion d'actifs, notation, monnaie privée, fiscalité ---
    _s("Investing in the Web", "Largest Asset Managers by AUM in 2026 (données au 30 juin 2026)",
       "Investing in the Web", "2026", "https://investingintheweb.com/blog/largest-asset-managers/",
       "Professionnels du secteur"),
    _s("Jan Fichtner, Eelke Heemskerk, Javier Garcia-Bernardo", "Hidden power of the Big Three? "
       "Passive index funds, re-concentration of corporate ownership, and new financial risk",
       "Business and Politics (Cambridge University Press)", "2017",
       "https://www.cambridge.org/core/journals/business-and-politics/article/hidden-power-of-the-big-three-passive-index-funds-reconcentration-of-corporate-ownership-and-new-financial-risk/30AD689509AAD62F5B677E916C28C4B6",
       "Recherche"),
    _s("Moody’s Ratings", "Communiqués de notation souveraine — Belgique et France", "Moody’s",
       "2025-2026", "https://www.moodys.com/", "Professionnels du secteur"),
    _s("MSCI", "Index Methodology — Global Investable Market Indexes", "MSCI", "2026",
       "https://www.msci.com/indexes/index-resources/methodology", "Professionnels du secteur"),
    _s("Brookings Institution", "Stablecoins after GENIUS: private money, public debt, and the "
       "global dollar", "Brookings", "juin 2026",
       "https://www.brookings.edu/articles/stablecoins-after-genius/", "Recherche"),
    _s("Standard & Poor’s Dow Jones Indices", "S&P 500 Buybacks — communiqués trimestriels",
       "S&P Global", "2025-2026",
       "https://www.spglobal.com/spdji/en/corporate-news/article/sp-500-buybacks-set-quarterly-and-12-month-records-again/",
       "Professionnels du secteur"),
    _s("Gaël Giraud", "L’Illusion financière", "Éditions de l’Atelier", "2012 (rééd. 2014)",
       "https://www.melchior.fr/note-de-lecture/l-illusion-financiere", "Ouvrages"),
    _s("Gabriel Zucman", "Un impôt plancher sur la fortune des ultra-riches", "Débat public et "
       "travaux de l’EU Tax Observatory", "2024-2026",
       "https://fr.wikipedia.org/wiki/Taxe_Zucman", "Recherche"),
    _s("ONE Campaign", "Les taxes solidaires : un héritage français humaniste", "ONE", "2024",
       "https://www.one.org/fr/actualites/taxes-solidaires-un-heritage-humaniste/",
       "ONG et société civile"),
    _s("Commission des questions économiques du Conseil de l’Europe / Alena Douhan (ONU)",
       "Rapports de la rapporteuse spéciale sur l’impact négatif des mesures coercitives "
       "unilatérales", "Nations unies", "2020-2025",
       "https://www.ohchr.org/en/special-procedures/sr-unilateral-coercive-measures",
       "Institutions et données"),
    _s("CNBC", "Kevin Warsh wins Senate confirmation as the next Federal Reserve chair",
       "CNBC", "13 mai 2026",
       "https://www.cnbc.com/2026/05/13/kevin-warsh-wins-senate-confirmation-as-the-next-federal-reserve-chair.html",
       "Presse"),
    _s("CountryEconomy, d’après Eurostat", "Produit intérieur brut nominal de la Belgique",
       "CountryEconomy", "2026", "https://countryeconomy.com/gdp/belgium",
       "Institutions et données"),
]

# ---------------------------------------------------------------------------
# lexique
# ---------------------------------------------------------------------------

def _t(terme, definition):
    return {"terme": terme, "definition": definition}


LEXIQUE = {
    "chrematistique": _t("Chrématistique",
        "Chez Aristote, l’art d’acquérir des richesses pour elles-mêmes, par opposition à "
        "l’{{oikonomia}}. Son trait distinctif n’est pas l’avidité mais l’**absence de terme** : "
        "un estomac se remplit, un compte non. Le mot est souvent employé comme une insulte ; "
        "il désigne d’abord une structure, celle d’une activité sans point d’arrêt interne. [2]"),
    "oikonomia": _t("Oikonomia",
        "L’administration de la maison, puis de la communauté, ordonnée à un besoin fini. Le mot "
        "escamote un point gênant : l’oikos grec reposait sur l’esclavage et l’exclusion des "
        "femmes. Sa limite était réelle, sa justice ne l’était pas. [2]"),
    "desencastrement": _t("Désencastrement",
        "Chez Polanyi, le mouvement par lequel l’activité marchande cesse d’être une fonction "
        "auxiliaire de la société pour lui imposer ses règles. Le terme est contesté : Polanyi "
        "lui-même admet qu’une économie totalement désencastrée est impossible, puisqu’elle "
        "détruirait sa propre base. Il désigne donc une tendance, pas un état atteint. [7]"),
    "marchandise-fictive": _t("Marchandise fictive",
        "Chez Polanyi, ce qui est traité comme une marchandise sans avoir été produit pour la "
        "vente : le travail (qui est de la vie humaine), la terre (qui est la nature), la monnaie "
        "(qui est une convention politique). [7]"),
    "financiarisation": _t("Financiarisation",
        "Processus par lequel les acteurs, les critères et les horizons de temps financiers "
        "deviennent déterminants pour les décisions des entreprises et des États. Le mot est "
        "commode et flou : il agrège des phénomènes distincts — croissance des marchés, "
        "endettement des ménages, gouvernance actionnariale — qui n’ont ni les mêmes causes ni "
        "les mêmes remèdes."),
    "imputabilite": _t("Imputabilité",
        "La possibilité d’attribuer une décision à quelqu’un, et de le faire répondre devant une "
        "instance. À distinguer de la responsabilité morale, qui n’exige pas d’instance, et de la "
        "responsabilité juridique, qui exige en plus une faute qualifiée. C’est la grandeur que "
        "mesure l’échelle propre à ce site."),
    "valeur-actionnariale": _t("Maximisation de la valeur actionnariale",
        "Doctrine selon laquelle les dirigeants d’une entreprise n’ont d’autre mandat légitime "
        "que d’accroître la valeur détenue par les actionnaires. Formulée par Friedman en 1970, "
        "elle n’est presque jamais une obligation légale : c’est une norme de gouvernance devenue "
        "si dominante qu’on la prend pour du droit. [14, 15]"),
    "rachat-d-actions": _t("Rachat d’actions",
        "Opération par laquelle une société achète ses propres titres pour les annuler, "
        "augmentant mécaniquement le bénéfice par action restante. Techniquement neutre ; "
        "économiquement, un arbitrage : ce montant n’ira ni à l’investissement, ni aux salaires, "
        "ni au désendettement. [104]"),
    "frontiere-de-production": _t("Frontière de la production",
        "Ligne comptable qui sépare, dans le calcul du produit intérieur brut, ce qui est réputé "
        "créer de la valeur de ce qui n’en crée pas. Elle a été déplacée : depuis les années "
        "1970, toute activité obtenant un prix sur un marché est comptée comme productive, ce qui "
        "fait disparaître statistiquement la notion de {{rente}}. [13]"),
    "rente": _t("Rente",
        "Revenu tiré d’une position — propriété, monopole, accès privilégié — plutôt que d’une "
        "contribution productive. Les économistes classiques la distinguaient soigneusement du "
        "profit ; la comptabilité nationale contemporaine ne les distingue plus. [13]"),
    "titrisation": _t("Titrisation",
        "Transformation de créances peu liquides en titres négociables. L’opération répartit le "
        "risque, mais elle **découple** aussi celui qui accorde le crédit de celui qui en supporte "
        "le défaut : c’est un cas d’école d’imputabilité diluée. [36]"),
    "produit-derive": _t("Produit dérivé",
        "Contrat dont la valeur dépend de celle d’un actif sous-jacent. Le « montant notionnel » "
        "qui sert à le mesurer n’est pas une somme d’argent à risque : c’est une base de calcul. "
        "Confondre les deux produit des chiffres spectaculaires et faux. [26, 27]"),
    "thf": _t("Trading à haute fréquence",
        "Négociation automatisée à l’échelle de la microseconde. Sa liquidité est réelle mais "
        "**conditionnelle** : elle se retire précisément lorsque le marché en aurait besoin, "
        "comme en mai 2010. [22]"),
    "flash-crash": _t("Flash crash",
        "Effondrement et rebond des cours en quelques minutes, sans nouvelle économique "
        "correspondante. Celui du 6 mai 2010 a effacé environ mille milliards de dollars de "
        "capitalisation avant de les rendre. [22]"),
    "gestion-passive": _t("Gestion passive",
        "Gestion qui réplique un indice au lieu de sélectionner des titres. Elle a fait chuter "
        "les frais supportés par les épargnants — un gain réel — tout en concentrant les droits "
        "de vote de milliers d’entreprises entre quelques mains. [99, 100]"),
    "propriete-commune": _t("Propriété commune",
        "Situation où les mêmes investisseurs détiennent simultanément les principaux concurrents "
        "d’un secteur. La littérature discute son effet sur la concurrence ; elle s’accorde sur "
        "le fait qu’elle déplace le lieu réel de l’arbitrage. [100]"),
    "collateral": _t("Collatéral",
        "Actif remis en garantie pour obtenir un financement. La liste des collatéraux qu’une "
        "banque centrale accepte est une politique industrielle qui ne dit pas son nom. [30, 31]"),
    "neutralite-de-marche": _t("Neutralité de marché",
        "Principe selon lequel une banque centrale ne doit pas fausser l’allocation du capital, "
        "et doit donc calquer ses achats sur la composition des marchés. Comme les marchés "
        "obligataires sont pondérés vers les secteurs les plus intensifs en carbone, la "
        "neutralité produit un biais qu’elle prétend éviter. [30, 31]"),
    "interdependance-instrumentalisee": _t("Interdépendance instrumentalisée",
        "Concept de Farrell et Newman : les réseaux économiques mondiaux ont des nœuds, et l’État "
        "qui contrôle un nœud peut s’en servir pour surveiller ou pour exclure. Plus un pays est "
        "intégré, plus il est vulnérable. [21]"),
    "sanction-ciblee": _t("Sanction ciblée",
        "Mesure censée frapper des responsables plutôt qu’une population. En pratique, le "
        "sur-respect des banques — qui refusent toute transaction douteuse par crainte des "
        "amendes — étend l’effet bien au-delà de la cible désignée. [71, 108]"),
    "sur-conformite": _t("Sur-conformité",
        "Comportement d’un opérateur privé qui applique une règle au-delà de ce qu’elle exige, "
        "par prudence. Elle transforme une sanction ciblée en embargo de fait, sans que personne "
        "ne l’ait décidé ni n’en réponde. [71]"),
    "avoirs-immobilises": _t("Avoirs immobilisés",
        "Actifs bloqués sans transfert de propriété. À distinguer de la confiscation, qui "
        "transfère la propriété et engage une responsabilité juridique différente. Toute la "
        "querelle européenne de 2025-2026 tient dans cette distinction. [75, 76]"),
    "actif-echoue": _t("Actif échoué",
        "Actif dont la valeur s’effondre avant la fin de sa vie économique prévue, parce que le "
        "droit, la technique ou la demande ont changé. Le terme dépolitise : un actif « échoue » "
        "surtout parce qu’une décision publique a été prise, ou parce qu’elle a tardé. [41]"),
    "bulle-carbone": _t("Bulle carbone",
        "Écart entre la valorisation boursière des producteurs d’énergies fossiles, fondée sur "
        "leurs réserves prouvées, et la part de ces réserves qui pourra être brûlée sans "
        "dépasser les objectifs climatiques. [41, 42]"),
    "double-materialite": _t("Double matérialité",
        "Obligation d’analyser à la fois ce que l’environnement fait à l’entreprise (matérialité "
        "financière) et ce que l’entreprise fait à l’environnement (matérialité d’impact). C’est "
        "le seul dispositif européen qui institue une imputabilité sortante. [62]"),
    "greenwashing": _t("Écoblanchiment",
        "Présentation d’un produit ou d’une entreprise comme durable au-delà de ce que les faits "
        "établissent. Le mot désigne un mensonge ; le problème réglementaire est plus étroit : "
        "l’absence de définition opposable de ce qu’est un investissement durable. [56, 59]"),
    "monnaie-locale": _t("Monnaie locale complémentaire",
        "Unité de compte adossée à l’euro, valable dans un périmètre et un réseau donnés. Elle ne "
        "concurrence pas la monnaie officielle : elle ajoute une friction volontaire qui empêche "
        "la richesse de quitter un territoire. [90, 97]"),
    "mnbc": _t("Monnaie numérique de banque centrale",
        "Forme numérique de la monnaie de banque centrale accessible au public. Dans le débat "
        "européen, elle est présentée comme une réponse aux systèmes de paiement étrangers et aux "
        "monnaies privées ; elle pose en retour la question du seuil de détention et de la trace "
        "des paiements. [32, 33]"),
    "stablecoin": _t("Jeton stable",
        "Jeton numérique adossé à une monnaie, généralement le dollar, et gagé sur des titres du "
        "Trésor américain. C’est de la monnaie privée : sa stabilité dépend d’un émetteur, pas "
        "d’une banque centrale. [103]"),
    "credit-prive": _t("Crédit privé",
        "Prêt accordé par un fonds plutôt que par une banque, hors marché coté et hors "
        "supervision bancaire. Marché estimé entre 1 500 et 2 000 milliards de dollars, "
        "jamais éprouvé par une récession sévère. [29]"),
    "clt": _t("Community Land Trust",
        "Structure qui détient le sol de manière inaliénable et n’en vend que le bâti, avec une "
        "charte plafonnant la plus-value à la revente. Le sol sort du marché ; le logement y "
        "reste, mais à prix encadré. [92]"),
    "ttf": _t("Taxe sur les transactions financières",
        "Prélèvement de faible taux sur chaque transaction, proposé par James Tobin en 1972 pour "
        "« jeter du sable dans les rouages ». Son rendement dépend entièrement de l’assiette "
        "retenue — et c’est sur l’assiette, non sur le principe, que les négociations échouent "
        "depuis 2011. [107]"),
    "convivialite": _t("Convivialité",
        "Chez Illich, la propriété d’un outil que son usager contrôle, qui n’engendre ni maîtres "
        "ni esclaves et dont le rendement décroît au-delà d’un seuil. Le critère n’est pas la "
        "taille : c’est la possibilité, pour l’usager, de s’en passer. [9]"),
}

# ---------------------------------------------------------------------------
# chronologie
# ---------------------------------------------------------------------------

CHRONOLOGIE = [
    {"date": "IIIe millénaire av. J.-C.", "iso": "", "lieu": "Mésopotamie",
     "fait": "Les premières unités de compte sont des dettes",
     "precision": "Les temples et palais de Sumer tiennent des comptes en orge et en argent bien "
                  "avant toute pièce frappée. Les proclamations royales d’effacement des dettes "
                  "(*amargi*) montrent que la dette est d’emblée un enjeu politique. [5]",
     "dossier": "le-mythe-du-troc"},
    {"date": "vers 600 av. J.-C.", "iso": "", "lieu": "Lydie",
     "fait": "Première monnaie métallique standardisée",
     "precision": "En électrum, sous les Mermnades. Elle rend possible le paiement d’armées de "
                  "mercenaires : la monnaie frappée et la guerre naissent ensemble. [4]",
     "dossier": "le-mythe-du-troc"},
    {"date": "IVe siècle av. J.-C.", "iso": "", "lieu": "Athènes",
     "fait": "Aristote sépare oikonomia et chrématistique",
     "precision": "La *Politique* distingue l’administration ordonnée à un besoin fini de "
                  "l’acquisition sans terme. [2]",
     "dossier": "oikonomia-et-chrematistique"},
    {"date": "1532", "iso": "", "lieu": "Lyon",
     "fait": "Rabelais publie Pantagruel",
     "precision": "« Science sans conscience n’est que ruine de l’âme », dans la lettre de "
                  "Gargantua à son fils. [1]",
     "dossier": "rabelais-et-la-finance"},
    {"date": "20 mars 1602", "iso": "1602-03-20", "lieu": "Provinces-Unies", "teinte": "lilas",
     "fait": "La VOC reçoit le droit de faire la guerre",
     "precision": "Première société par actions à capital permanent ; sa charte l’autorise à "
                  "lever des armées, conclure des traités et battre monnaie. Le commerce armé "
                  "n’est pas une dérive tardive du capitalisme, c’en est la forme initiale.",
     "dossier": "le-desencastrement"},
    {"date": "1776 et 1817", "iso": "", "lieu": "Royaume-Uni",
     "fait": "Smith puis Ricardo fondent le récit du commerce pacificateur",
     "precision": "La « propension à échanger » et l’avantage comparatif deviennent le socle "
                  "d’une histoire linéaire que l’anthropologie contredira. [3, 4]",
     "dossier": "le-mythe-du-troc"},
    {"date": "1806-1814", "iso": "", "lieu": "Europe", "teinte": "lilas",
     "fait": "Blocus continental",
     "precision": "Napoléon tente d’étrangler le commerce britannique ; le continent souffre "
                  "davantage que l’île. Première guerre économique à l’échelle d’un continent. [12]",
     "dossier": "l-arme-economique-1914"},
    {"date": "1914-1919", "iso": "", "lieu": "Europe", "teinte": "lilas",
     "fait": "Le blocus allié devient « l’arme économique »",
     "precision": "Mulder date de là l’institutionnalisation des sanctions ; l’article 16 du "
                  "Pacte de la Société des Nations en fait un instrument de paix. [12]",
     "dossier": "l-arme-economique-1914"},
    {"date": "juin 1930", "iso": "1930-06-17", "lieu": "États-Unis", "teinte": "lilas",
     "fait": "Tarif Smoot-Hawley",
     "precision": "Le tarif moyen sur les importations taxables passe d’environ 40 % en 1929 à "
                  "59 % en 1932 ; les représailles contractent le commerce mondial.",
     "dossier": "les-tarifs-et-la-loi"},
    {"date": "1944", "iso": "1944-01-01", "lieu": "New York",
     "fait": "Polanyi publie La Grande Transformation",
     "precision": "Le marché autorégulateur y est décrit comme une construction politique, pas "
                  "comme un état de nature. [7]",
     "dossier": "le-desencastrement"},
    {"date": "1949-1994", "iso": "", "lieu": "Bloc occidental", "teinte": "lilas",
     "fait": "Le CoCom organise l’embargo technologique",
     "precision": "Contrôle coordonné des exportations de technologies duales vers le bloc "
                  "soviétique : matrice directe des contrôles sur les semi-conducteurs.",
     "dossier": "l-interdependance-retournee"},
    {"date": "1962", "iso": "1962-02-07", "lieu": "États-Unis / Cuba", "teinte": "lilas",
     "fait": "Embargo américain sur Cuba",
     "precision": "Toujours en vigueur soixante-quatre ans plus tard ; condamné chaque année par "
                  "l’Assemblée générale des Nations unies. [72]",
     "dossier": "les-sanctions-et-les-civils"},
    {"date": "15 août 1971", "iso": "1971-08-15", "lieu": "États-Unis",
     "fait": "Fin de la convertibilité or du dollar",
     "precision": "Le système de Bretton Woods s’achève ; la mobilité des capitaux s’installe.",
     "dossier": "la-dette"},
    {"date": "13 septembre 1970", "iso": "1970-09-13", "lieu": "New York",
     "fait": "Friedman publie sa doctrine",
     "precision": "« La responsabilité sociale de l’entreprise est d’accroître ses profits » : le "
                  "texte fondateur de la primauté actionnariale. [14]",
     "dossier": "la-doctrine-friedman"},
    {"date": "1972-1973", "iso": "1972-01-01", "lieu": "Princeton / Rome",
     "fait": "Tobin propose sa taxe ; le Club de Rome publie Halte à la croissance",
     "precision": "Deux réponses contemporaines à la même accélération : freiner les capitaux, "
                  "borner la matière. [107, 18]",
     "dossier": "taxer-le-mouvement"},
    {"date": "1990-2003", "iso": "1990-08-06", "lieu": "Irak", "teinte": "lilas",
     "fait": "Sanctions globales des Nations unies contre l’Irak",
     "precision": "Le cas qui a discrédité les sanctions générales et fait naître la doctrine des "
                  "sanctions dites ciblées. [71]",
     "dossier": "les-sanctions-et-les-civils"},
    {"date": "2007-2009", "iso": "2008-09-15", "lieu": "Monde",
     "fait": "Crise des subprimes",
     "precision": "Chômage américain de 4,6 % à 9,6 % ; commerce mondial en volume −12,2 % en "
                  "2009 ; dette publique américaine de 86,4 % à 125,8 % du PIB. [36]",
     "dossier": "la-vitesse"},
    {"date": "6 mai 2010", "iso": "2010-05-06", "lieu": "Chicago / New York",
     "fait": "Flash crash",
     "precision": "Le Dow Jones perd plus de mille points en quelques minutes puis rebondit ; les "
                  "teneurs de marché algorithmiques se retirent simultanément. [22]",
     "dossier": "la-vitesse"},
    {"date": "1er août 2012", "iso": "2012-08-01", "lieu": "New York",
     "fait": "Knight Capital",
     "precision": "Un code obsolète réactivé par erreur génère des millions d’ordres : 460 "
                  "millions de dollars perdus en quarante-cinq minutes. [22]",
     "dossier": "la-vitesse"},
    {"date": "2013-2014", "iso": "2013-04-01", "lieu": "Londres",
     "fait": "Carbon Tracker formule la bulle carbone",
     "precision": "*Unburnable Carbon* : la valorisation des producteurs suppose de brûler des "
                  "réserves que le budget carbone interdit. [41]",
     "dossier": "la-bulle-carbone"},
    {"date": "février-mars 2022", "iso": "2022-02-28", "lieu": "Union européenne", "teinte": "lilas",
     "fait": "Gel des réserves de la banque centrale russe",
     "precision": "Environ 210 milliards d’euros immobilisés dans l’Union, dont 185 milliards "
                  "déposés chez Euroclear, à Bruxelles. Franchissement d’un seuil : ce sont les "
                  "réserves d’un État, pas les avoirs de personnes désignées. [75]",
     "dossier": "les-avoirs-geles"},
    {"date": "7 octobre 2022", "iso": "2022-10-07", "lieu": "Washington", "teinte": "lilas",
     "fait": "Contrôles américains sur les semi-conducteurs avancés",
     "precision": "L’objectif déclaré n’est plus de dissuader mais de retarder durablement la "
                  "capacité technologique d’un rival. [67]",
     "dossier": "l-interdependance-retournee"},
    {"date": "5 janvier 2024 – 1er janvier 2025", "iso": "2024-01-05", "lieu": "Union européenne",
     "fait": "Entrée en application de la CSRD",
     "precision": "La double matérialité devient une obligation de reporting auditée. [62]",
     "dossier": "la-double-materialite"},
    {"date": "décembre 2024 – août 2025", "iso": "2025-01-07", "lieu": "États-Unis / Europe",
     "fait": "Départ en cascade des grandes banques de la Net-Zero Banking Alliance",
     "precision": "Goldman Sachs, puis JPMorgan, Bank of America, Citigroup, les banques "
                  "canadiennes, HSBC en juillet, UBS et Barclays en août. [60]",
     "dossier": "la-fin-des-alliances"},
    {"date": "3 octobre 2025", "iso": "2025-10-03", "lieu": "Genève",
     "fait": "La Net-Zero Banking Alliance cesse ses activités",
     "precision": "Ses membres votent la transformation de l’alliance en simple cadre "
                  "méthodologique. Elle comptait plus de 140 banques et 74 000 milliards de "
                  "dollars d’actifs en 2024. [60, 61]",
     "dossier": "la-fin-des-alliances"},
    {"date": "9 octobre 2025", "iso": "2025-10-09", "lieu": "Pékin", "teinte": "lilas",
     "fait": "La Chine étend ses contrôles sur les terres rares",
     "precision": "Licence obligatoire dès 0,1 % de contenu chinois, y compris pour des produits "
                  "fabriqués hors de Chine : premier dispositif chinois à portée "
                  "extraterritoriale comparable à la règle américaine. [67]",
     "dossier": "les-tarifs-et-la-loi"},
    {"date": "10 décembre 2025", "iso": "2025-12-10", "lieu": "Paris",
     "fait": "World Inequality Report 2026",
     "precision": "Les 0,001 % les plus riches détiennent trois fois le patrimoine de la moitié la "
                  "plus pauvre de l’humanité. [16, 50]",
     "dossier": "la-concentration"},
    {"date": "18-19 décembre 2025", "iso": "2025-12-19", "lieu": "Bruxelles", "teinte": "lilas",
     "fait": "La Belgique fait échouer le prêt de réparation",
     "precision": "Le Conseil européen renonce à mobiliser les avoirs immobilisés et retient un "
                  "prêt de 90 milliards d’euros financé autrement. [76]",
     "dossier": "les-avoirs-geles"},
    {"date": "20 février 2026", "iso": "2026-02-20", "lieu": "Washington", "teinte": "lilas",
     "fait": "La Cour suprême invalide les droits de douane IEEPA",
     "precision": "Environ 150 milliards de dollars avaient déjà été perçus ; le taux moyen "
                  "effectif retombe à 9,1 %, le plus élevé depuis 1946. [65, 66]",
     "dossier": "les-tarifs-et-la-loi"},
    {"date": "26 février 2026", "iso": "2026-02-26", "lieu": "Bruxelles",
     "fait": "Publication de la directive Omnibus I",
     "precision": "Environ 80 % des entreprises sortent du champ de la CSRD ; les plans de "
                  "transition climatique obligatoires et le régime européen de responsabilité "
                  "civile sont supprimés. [51, 52]",
     "dossier": "l-omnibus"},
    {"date": "31 mars 2026", "iso": "2026-03-31", "lieu": "Bruxelles",
     "fait": "Scan des banques 2026",
     "precision": "KBC, BNP Paribas et Belfius réinvestissent dans des producteurs d’armes "
                  "nucléaires ; Argenta autorise des systèmes d’armes automatisés. [83, 84]",
     "dossier": "la-banque-que-l-on-choisit"},
    {"date": "23 avril 2026", "iso": "2026-04-23", "lieu": "Bruxelles", "teinte": "lilas",
     "fait": "Vingtième paquet de sanctions européennes contre la Russie",
     "precision": "Vingt banques russes supplémentaires, 46 navires de la flotte de l’ombre "
                  "(632 au total), interdiction sectorielle des plateformes crypto russes. [64]",
     "dossier": "les-sanctions-et-les-civils"},
    {"date": "15 mai 2026", "iso": "2026-05-15", "lieu": "Moscou / Bruxelles", "teinte": "lilas",
     "fait": "Un tribunal russe condamne Euroclear à 250 milliards de dollars",
     "precision": "Décision sans effet exécutoire en Belgique, mais qui matérialise le risque de "
                  "représailles invoqué par le gouvernement belge. [78]",
     "dossier": "les-avoirs-geles"},
    {"date": "23 juin 2026", "iso": "2026-06-23", "lieu": "Strasbourg",
     "fait": "Le Parlement européen valide le cadre de l’euro numérique",
     "precision": "Adopté en commission par 43 voix contre 14 ; plafond de détention encore "
                  "discuté, phases pilotes prévues en 2027. [32, 33]",
     "dossier": "la-monnaie-que-l-on-fait"},
    {"date": "30 juillet 2026", "iso": "2026-07-30", "lieu": "Monde",
     "fait": "Jour du dépassement",
     "precision": "L’humanité consomme 73 % plus vite que la biosphère ne régénère ; la dette "
                  "écologique cumulée équivaut à 20,6 années de production biologique. [46]",
     "dossier": "le-decouplage-introuvable"},
    {"date": "septembre-octobre 2026", "iso": "2026-09-14", "lieu": "Strasbourg / Bruxelles",
     "fait": "Vote parlementaire et trilogues sur SFDR 2.0",
     "precision": "Près de 600 amendements déposés ; l’écart porte sur les exclusions fossiles et "
                  "les seuils d’alignement à la taxonomie. [54]",
     "dossier": "sfdr-et-l-etiquette"},
    {"date": "19 mars 2027 et 26 juillet 2028", "iso": "2027-03-19", "lieu": "États membres",
     "fait": "Échéances de transposition de l’Omnibus",
     "precision": "CSRD révisée en 2027, devoir de vigilance en 2028 : les prochaines fenêtres "
                  "politiques où la double matérialité peut être défaite ou rétablie. [52]",
     "dossier": "l-omnibus"},
]

# ---------------------------------------------------------------------------
# indicateurs
# ---------------------------------------------------------------------------

INDICATEURS = [
    {"libelle": "Dette mondiale, tous secteurs", "valeur": "> 350 000 Md$",
     "date": "T1 2026", "source": 23, "dossier": "la-dette"},
    {"libelle": "Hausse de la dette mondiale sur le trimestre", "valeur": "+ 4 400 Md$",
     "date": "T1 2026", "source": 23, "dossier": "la-dette"},
    {"libelle": "Dette publique belge", "valeur": "≈ 108 % du PIB",
     "date": "2026", "source": 82, "dossier": "la-dette"},
    {"libelle": "Trajectoire de la dette publique belge", "valeur": "122 % du PIB",
     "date": "projection 2031", "source": 82, "dossier": "la-dette"},
    {"libelle": "Charges d’intérêt de la dette belge", "valeur": "≈ 21 Md€/an",
     "date": "projection 2030", "source": 83, "dossier": "la-dette"},
    {"libelle": "Financement bancaire des énergies fossiles", "valeur": "906 Md$",
     "date": "année 2025", "source": 37, "dossier": "le-financement-du-chaos"},
    {"libelle": "Financement fossile cumulé depuis l’accord de Paris", "valeur": "8 700 Md$",
     "date": "2016-2025", "source": 38, "dossier": "le-financement-du-chaos"},
    {"libelle": "Financement de l’expansion fossile", "valeur": "508 Md$ (+ 27 %)",
     "date": "année 2025", "source": 38, "dossier": "le-financement-du-chaos"},
    {"libelle": "Premier financeur mondial (JPMorgan Chase)", "valeur": "58 Md$",
     "date": "année 2025", "source": 38, "dossier": "le-financement-du-chaos"},
    {"libelle": "Part des douze premières banques dans le total", "valeur": "≈ 40 %",
     "date": "année 2025", "source": 38, "dossier": "le-financement-du-chaos"},
    {"libelle": "Actifs sous gestion des trois premiers gestionnaires", "valeur": "≈ 33 600 Md$",
     "date": "30 juin 2026", "source": 99, "dossier": "les-trois-gestionnaires"},
    {"libelle": "Actifs sous gestion de BlackRock", "valeur": "15 300 Md$",
     "date": "30 juin 2026", "source": 99, "dossier": "les-trois-gestionnaires"},
    {"libelle": "Part du patrimoine mondial détenue par les 10 % les plus riches", "valeur": "75 %",
     "date": "2025", "source": 16, "dossier": "la-concentration"},
    {"libelle": "Part détenue par la moitié la plus pauvre de l’humanité", "valeur": "2 %",
     "date": "2025", "source": 16, "dossier": "la-concentration"},
    {"libelle": "Patrimoine des 0,001 % rapporté à celui des 50 % les plus pauvres", "valeur": "× 3",
     "date": "2025", "source": 50, "dossier": "la-concentration"},
    {"libelle": "Croissance du patrimoine mondial", "valeur": "+ 10,8 %",
     "date": "année 2025", "source": 49, "dossier": "la-concentration"},
    {"libelle": "Extraction mondiale de matières", "valeur": "≈ 106 Gt/an",
     "date": "2024", "source": 43, "dossier": "le-decouplage-introuvable"},
    {"libelle": "Part de matières secondaires dans l’économie mondiale", "valeur": "6,9 %",
     "date": "2025", "source": 44, "dossier": "le-decouplage-introuvable"},
    {"libelle": "Dépassement des capacités de régénération", "valeur": "73 %",
     "date": "2026", "source": 46, "dossier": "le-decouplage-introuvable"},
    {"libelle": "Émissions industrielles liées à 36 entreprises", "valeur": "> 50 %",
     "date": "année 2023", "source": 40, "dossier": "la-bulle-carbone"},
    {"libelle": "Avoirs de la banque centrale russe immobilisés dans l’Union", "valeur": "≈ 210 Md€",
     "date": "septembre 2026", "source": 75, "dossier": "les-avoirs-geles"},
    {"libelle": "Part de ces avoirs déposée chez Euroclear, à Bruxelles", "valeur": "185 Md€",
     "date": "septembre 2026", "source": 75, "dossier": "les-avoirs-geles"},
    {"libelle": "Taux de douane moyen effectif aux États-Unis après l’arrêt de la Cour suprême",
     "valeur": "9,1 %", "date": "février 2026", "source": 65, "dossier": "les-tarifs-et-la-loi"},
    {"libelle": "Encours du crédit privé mondial", "valeur": "1 500 à 2 000 Md$",
     "date": "mai 2026", "source": 29, "dossier": "les-produits-derives"},
]

# ---------------------------------------------------------------------------
# questions fréquentes de l'accueil
# ---------------------------------------------------------------------------

FAQ_ACCUEIL = [
    ("Que veut dire « finance sans conscience » ?",
     "Ce site ne prend pas « conscience » au sens de scrupule moral, mais au sens de capacité de "
     "répondre. Une finance sans conscience est une finance dont les décisions ne peuvent être "
     "rapportées à personne : ni à un dirigeant qu’un tribunal pourrait entendre, ni à une "
     "assemblée qu’un électeur pourrait sanctionner. C’est une définition vérifiable, donc "
     "réfutable."),
    ("La finance a-t-elle vraiment échappé au contrôle politique ?",
     "Non, et c’est la thèse du site. Entre 2022 et 2026, des États ont immobilisé 210 milliards "
     "d’euros de réserves d’une banque centrale, exclu des banques entières des circuits de "
     "paiement, soumis à licence tout produit contenant 0,1 % de terre rare chinoise, et imposé "
     "puis vu annuler des droits de douane décidés seuls. La finance obéit très bien. La question "
     "est de savoir à qui — et devant qui cet acteur répond."),
    ("Qu’est-ce que l’échelle d’imputabilité ?",
     "Une mention portée par chacun des trente-quatre dossiers, en quatre degrés : imputable, "
     "diluée, déléguée, sans répondant. Elle ne note pas la moralité d’un acteur ni la gravité "
     "d’un fait : elle constate s’il existe, ou non, un endroit où lui demander des comptes. Sa "
     "règle d’attribution est publiée sur la page méthode, et chaque mention est réfutable en "
     "produisant l’instance manquante."),
    ("D’où viennent les chiffres ?",
     "De 110 sources classées par nature — institutions, recherche, presse, ONG, acteurs du "
     "secteur — et systématiquement datées. Lorsqu’une donnée du corpus de départ s’est révélée "
     "périmée ou fragile, la correction est signalée sur la page méthode plutôt que discrètement "
     "appliquée."),
    ("Le site prend-il parti ?",
     "Oui, et il le dit. Il soutient que l’imputabilité est le critère décisif, et que le recul "
     "réglementaire européen de 2026 l’a affaiblie. Il présente en contrepartie l’objection la "
     "plus sérieuse dans chaque dossier, et il indique ce qui le ferait changer d’avis."),
]

# ---------------------------------------------------------------------------
# pages statiques
# ---------------------------------------------------------------------------

PAGES_STATIQUES = {
    "methode.html": {
        "sur_titre": "Transparence",
        "titre": "Méthode et limites",
        "seo_titre": "Méthode, corrections et limites | Vigie",
        "description": "Comment ce site est fabriqué : l’échelle d’imputabilité et sa règle "
                       "d’attribution, les corrections apportées au corpus de départ, les "
                       "réserves sur les chiffres, les lacunes assumées.",
        "mots_cles": ["méthode", "imputabilité", "corrections", "limites", "vérification"],
        "chapeau": "Un site qui reproche à d’autres de n’avoir de comptes à rendre à personne se "
                   "doit d’indiquer où on peut lui en demander. Cette page dit comment les "
                   "mentions sont attribuées, ce qui a été corrigé dans le corpus de départ, et "
                   "ce que ce site ne traite pas.",
        "corps": """
## L’échelle d’imputabilité

C’est le dispositif éditorial propre à ce site. Chaque dossier porte une mention en quatre
degrés. Elle ne mesure pas la gravité d’un fait, ni la moralité d’un acteur, ni la qualité du
dossier : elle constate l’existence, ou l’absence, d’un lieu où l’on peut demander des comptes.

| Mention | Ce qu’elle constate | Test d’attribution |
| --- | --- | --- |
| Imputable | Un acteur nommé décide et répond devant un juge, un parlement ou un électorat. | Peut-on citer l’instance et un cas où elle a effectivement statué ? |
| Diluée | La décision est réelle mais répartie sur tant d’acteurs qu’aucun n’en répond. | Chacun peut-il dire, sans mentir, qu’il n’a fait qu’appliquer une règle ou suivre un indice ? |
| Déléguée | La décision a été confiée à un tiers privé ou technique sans que la responsabilité suive. | Existe-t-il un acte formel de délégation, et la responsabilité y est-elle restée en amont ? |
| Sans répondant | La décision produit ses effets sur des personnes qui n’ont aucun canal pour la contester. | Les personnes affectées disposent-elles d’un recours, d’un vote ou d’une représentation ? |

Trois règles encadrent l’attribution.

1. **Une seule mention par dossier**, celle du maillon décisif — celui sans lequel la chaîne
   d’imputabilité tiendrait. Un dossier peut contenir plusieurs degrés ; le badge retient le plus
   bas des maillons indispensables.
2. **La mention porte sur la structure, pas sur les personnes.** « Diluée » ne veut pas dire que
   personne n’est fautif : cela veut dire que la structure rend l’attribution impossible.
3. **Toute mention est réfutable.** Produire l’instance manquante — un tribunal compétent, une
   commission parlementaire saisie, un recours ouvert aux personnes affectées — suffit à faire
   monter le dossier d’un degré. La correction sera publiée ici.

:::note Pourquoi pas une note morale
Une note morale se discute sans fin et n’engage rien. Un constat d’imputabilité se vérifie : soit
l’instance existe, soit elle n’existe pas. C’est aussi ce qui rend l’échelle utile politiquement,
puisqu’elle indique exactement ce qu’il faudrait créer.
:::

## Ce que ce site fait du corpus de départ

Sept documents ont servi de point de départ : quatre rapports d’analyse sur la finance éthique,
l’aliénation économique et le système économique mondial, une note critique sur le récit du troc,
et deux dossiers documentaires sur l’économie et sur la guerre économique. Ils sont déposés dans
le dossier `/download` du dépôt.

Ce site ne les résume pas. Il les instruit : il vérifie leurs chiffres, en corrige plusieurs,
écarte ce qui n’est pas établi, et ajoute ce qui manquait. Les cinq corrections principales sont
publiées ci-dessous.

### Corrections apportées

1. **Financement fossile.** Le corpus s’arrêtait à 869 milliards de dollars en 2024 et 906
   milliards en 2025 sans le détail. L’édition 2026 du rapport *Banking on Climate Chaos*, publiée
   le 9 juin 2026, confirme les 906 milliards pour 2025 mais ajoute deux faits que le corpus
   n’avait pas : le cumul depuis l’accord de Paris atteint 8 700 milliards de dollars, et le
   financement de l’**expansion** — pas seulement du maintien — progresse de 27 % pour atteindre
   508 milliards, record absolu. [37, 38]
2. **Jour du dépassement.** Le corpus donnait le 24 juillet 2025 et « aux alentours du 30 juillet »
   pour 2026. La date confirmée est le **30 juillet 2026**, six jours plus tard qu’en 2025 — ce
   qui ne signale pas une amélioration, la méthode ayant été révisée, mais le niveau de
   dépassement le plus élevé jamais mesuré. [46]
3. **Alliances climatiques.** Le corpus décrivait les engagements volontaires des banques comme
   un acquis fragile. Ils ont cessé d’exister : la Net-Zero Banking Alliance a mis fin à ses
   activités le **3 octobre 2025**. Le corpus ne pouvait pas le savoir ; le site en tire une
   conclusion qu’il n’avait pas tirée. [60, 61]
4. **Régulation européenne.** Le corpus présentait la CSRD et la double matérialité comme
   installées, et SFDR 2.0 comme un durcissement. Depuis, la directive Omnibus I publiée le
   **26 février 2026** a retiré environ 80 % des entreprises du champ de la CSRD, supprimé
   l’obligation de plan de transition climatique et abandonné le régime européen de
   responsabilité civile ; SFDR 2.0 n’est toujours pas adoptée et fait l’objet de près de 600
   amendements. [51, 52, 54]
5. **Trading algorithmique.** Le corpus donnait « 60 à 70 % » des transactions boursières
   exécutées algorithmiquement, en s’appuyant sur une source de vulgarisation ; un autre document
   du même corpus donnait 50 %. Ces chiffres circulent sans définition commune de ce qu’on
   compte. Le site ne retient donc aucun pourcentage global et s’appuie sur des faits
   vérifiables : le mécanisme du retrait simultané de liquidité, documenté par la revue de
   littérature de Sánchez Serrano. [22]

### Ce qui a été écarté

- L’affirmation selon laquelle la VOC aurait « valu 7 900 milliards de dollars actuels » : chiffre
  invérifiable, déjà écarté par le corpus lui-même, et repris ici de la même manière.
- Le chiffre de « 100 entreprises responsables de 71 % des émissions » : la formulation courante
  confond émissions industrielles liées à des producteurs et émissions imputables à des
  consommateurs. Le site retient la formulation d’InfluenceMap : plus de la moitié des émissions
  de 2023 sont liées à 36 entreprises, dont 16 des 20 premières sont publiques. [40]
- Les estimations de surmortalité attribuées aux sanctions sont conservées mais présentées comme
  des ordres de grandeur discutés, jamais comme des décomptes. [71]

## Réserves sur les chiffres

- Un **montant notionnel** de produits dérivés n’est pas une somme exposée : c’est une base de
  calcul. Ce site n’en cite aucun comme mesure de risque. [26, 27]
- Les **parts de patrimoine** dépendent fortement du traitement des actifs non cotés, des retraites
  et de l’immobilier ; les ordres de grandeur sont robustes, les décimales ne le sont pas. [16, 49]
- Le **financement fossile** agrège prêts syndiqués et arrangements obligataires : une part n’est
  pas portée au bilan de la banque qui les organise. La fédération bancaire française conteste sur
  ce point ; son argument est repris dans le dossier concerné plutôt que relégué. [39]
- Les **conversions de devises** ne sont pas harmonisées : chaque chiffre est donné dans l’unité
  de sa source, avec sa date.

## Ce que ce site ne traite pas

- L’assurance et la réassurance, pourtant décisives pour le risque climatique.
- Les retraites et la gestion des fonds de pension, traitées seulement de biais.
- Le crédit aux ménages, le surendettement et l’exclusion bancaire — un angle mort assumé, alors
  qu’il constitue l’essentiel du travail de terrain des associations citées.
- La finance islamique, la microfinance dans les pays du Sud, et les systèmes de paiement mobile
  africains, qui déplaceraient largement la question de la monnaie privée.
- Les Pays-Bas, le Luxembourg et l’Irlande comme places de domiciliation, alors que le triangle
  Bruxelles-Luxembourg-Dublin structure une grande partie de ce qui est décrit ici.

## La vidéo

La vidéo de la page d’accueil est le point de départ retenu par l’éditeur. Ce site ne reprend ni
son titre exact, ni sa date, ni son auteur : ces métadonnées n’ont pas pu être vérifiées depuis
l’environnement de rédaction, et aucun élément du site n’en dépend. Aucun chiffre, aucune
affirmation des trente-quatre dossiers n’en est tiré.

## Fabrication technique

Site statique en HTML et CSS, engendré par un script Python sans aucune dépendance. Pas de
JavaScript, pas de cookie, pas de traqueur, pas de mesure d’audience. Le seul appel à un serveur
tiers est le lecteur vidéo de la page d’accueil, chargé depuis `youtube-nocookie.com` ; il peut
être bloqué sans conséquence sur le reste du site. Thème sombre par défaut, variante claire si le
système la demande, feuille d’impression fournie.

Un script de contrôle vérifie à chaque construction : la validité de la structure des titres,
l’unicité des identifiants, l’existence de tous les liens internes et de toutes les ancres, la
présence des métadonnées, le parsage de chaque bloc JSON-LD, l’absence de script exécutable et
l’absence de ressource externe hors du lecteur vidéo.

## Auteur et responsabilité

Les textes sont signés **Vigie**, nom de plume. Ils ont été rédigés avec l’assistance de Claude
(Anthropic). Le choix des angles, la vérification des sources, les arbitrages éditoriaux et la
publication relèvent de l’éditeur du dépôt, qui en répond. Le dire est cohérent avec le sujet :
un site consacré à l’imputabilité ne peut pas dissimuler la sienne.

Signalements d’erreur : par les *issues* du dépôt. Toute correction établie est appliquée et
consignée sur cette page.
""",
    },
}
