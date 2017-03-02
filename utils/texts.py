#!/usr/bin/python
# coding=utf-8

# language & internationalization management
# Warning: english is not supported everywhere
# change current to change future texts callings
class lang:
    fr = 0
    de = 1
    en = 2
    default = fr
    current = default


# text color handling
class color:
    black = "[color=#323a47]"  # rgb(50, 58, 71)
    green = "[color=#00aa50]"  # rgb(0, 170, 80)
    green_light = "[color=#599875]"  # rgb(89, 152, 117)
    orange = "[color=#ff8000]"  # rgb(255,128,0)
    magenta = "[color=#e4235f]"  # rgb(228, 35, 95)
    grey = "[color=#969696]"  # rgb(150, 150, 150)
    grey_light = "[color=#d0c7d1]"  # rgb(208, 199,209)
    white = "[color=#ffffff]"  # rgb(255, 255, 255)
    end = "[/color]"
    default = black

    # for backgrounds
    back_grey = (0.58, 0.58, 0.58, 1)
    back_grey_dark = (0.2, 0.2, 0.2, 1)
    back_magenta = (0.89, 0.13, 0.37, 1)
    back_green = (0, 0.66, 0.195, 1)
    back_selected = (1, 0.5, 0, 1)


class Text:
    def __init__(self, fr, de, en="en", color=color.default):
        self.french = fr
        self.german = de
        self.english = en
        self.color = color

    def get(self):
        switch = {
            lang.fr: self.french,
            lang.de: self.german,
            lang.en: self.english
        }
        return self.color + switch.get(lang.current)  # + color.end


# CATEGORIES and objects names

txt_cat_water = Text(
    fr="Plan d'eau",
    de="de",
    en="Body of water")

txt_cat_pond = Text(
    fr="Étang",
    de="Weiher",
    en="Pond")

txt_cat_pool = Text(
    fr="Piscine",
    de="Schwimmbecken",
    en="Swimming pool")

txt_cat_hedge = Text(
    fr="Haies",
    de="Hecken",
    en="Hedges")

txt_cat_hedge_good = Text(
    fr="Haie diverses espèces indigènes",
    de="Einheimische Hecke",
    en="Hedge of various native species")

txt_cat_hedge_bad = Text(
    fr="Haie de thuyas ou de laurelles",
    de="Thuja- oder Kirschlorbeerhecke",
    en="Hedge of thuja and laurel")

txt_cat_fence = Text(
    fr="Murs et barrières",
    de="de",
    en="Fences and walls")

txt_cat_fence_space = Text(
    fr="Barrière de jardin avec espace",
    de="Gartenzaun",  # TODE: check
    en="Garden fence with space underneath")

txt_cat_fence_nospace = Text(
    fr="Barrière de jardin à ras du sol",
    de="Gartenzaun",  # TODE: check
    en="Garden fence close to the ground ")

txt_cat_fence_wall = Text(
    fr="Mur en béton",
    de="Betonmauer",
    en="Concrete wall")

txt_cat_floor = Text(
    fr="Revêtements de terrasses",
    de="de",
    en="Patio's floor")

txt_cat_floor_grass = Text(
    fr="Terrasse en pavés herbeux",
    de="Terrasse mit Rasengittersteinen",
    en="Patio with grassy floor")

txt_cat_floor_stone = Text(
    fr="Terrasse en béton",
    de="Betonierte Terrasse",
    en="Black sandstone patio")

txt_cat_shelter = Text(
    fr="Abris et cachettes",
    de="de",
    en="Shelters and hideouts")

txt_cat_shelter_wood = Text(
    fr="Tas de feuilles et bois mort",
    de="Laubhaufen und Totholz",
    en="Pile of old wood and dead leafs")

txt_cat_shelter_flower = Text(
    fr="Coin de prairie fleurie",
    de="Ein Stück Blumenwiese",
    en="Portion of meadow covered in flowers")

txt_cat_animal = Text(
    fr="Animaux de compagnie",
    de="de",
    en="Animals / pets")

txt_cat_animal_goat = Text(
    fr="Chèvres naines",
    de="Westafrikanische Zwergziege und Schafe",
    en="Pygmy dwarf goats")

txt_cat_animal_cat = Text(
    fr="Chat",
    de="Katze",
    en="Cat")

txt_cat_balcony_plants = Text(
    fr="Plantes au balcon",
    de="de",
    en="Plants at the balcony")

txt_cat_balcony_herbs = Text(
    fr="Plantes aromatiques",
    de="Gewürzkräuter",
    en="Aromatic herbs")

txt_cat_balcony_geranium = Text(
    fr="Géraniums",
    de="Geranien",
    en="Geraniums")

# SCENERY ELEMENTS (game setting)

txt_scenery_notxt = Text(
    fr="",
    de="",
    en="")

txt_scenery_category = Text(
    fr="Catégorie",
    de="Kategorie",
    en="Category")

txt_scenery_score = Text(
    fr="Score",
    de="TODE",
    en="Score")

# RECOVER OPTIONS (window)

txt_recover_header = Text(
    fr="Ce n'était pas le meilleur choix...",
    de="TODE",
    en="This wasn't the best choice...")

txt_recover_infos = Text(
    color=color.white,
    fr="Plus d'infos",
    de="TODE",
    en="Tell me more")

txt_recover_keep = Text(
    fr="Garder l'objet",
    de="TODE",
    en="Keep object")

txt_recover_remove = Text(
    fr="Enlever l'objet",
    de="TODE",
    en="Remove object")

txt_recover_replace = Text(
    fr="Remplacer l'objet",
    de="TODE",
    en="Replace object")

txt_recover_correct = Text(
    fr="Corriger l'objet",
    de="TODE",
    en="Adapt object")

# WELCOME AND INSTRUCTIONS
txt_tutorial_welcome_p0 = Text(
    fr="Bienvenue dans mon jardin !",
    de="TODE",
    en="Welcome in  my garden!")

txt_tutorial_welcome_p1 = Text(
    fr=" •   [b]Le but de ce jeu est de m'aider à aménager mon arrière-cour[/b], dans une sorte de 'simcity' simplifié version jardin. \n" \
       " •   Dans l'aménagement idéal, [b]mon jardin peut être un corridor biologique[/b], c'est à dire un endroit où les divers animaux se sentent bien pour vivre, se déplacer, se reproduire, se nourrir, entre autres.\n" \
       " •   Pour chaque catégorie d'objet, il y a [b]le choix entre deux objets[/b] dans le menu de gauche. Par glisser-déposer, place l'objet dans le jardin sur la zone clignotante prévue pour l'accueillir.\n" \
       " •   Une fois l'objet correctement placé, une animation avec un animal va apparaitre, et un point sera gagné ou perdu.\n" \
       " •   Dans le cas d'un mauvais choix, il est encore possible de changer d'avis ou tenter d'améliorer le choix.\n" \
       " •   Dans tous les cas, on peut [b]accéder à plus d'informations et des explications[/b], afin de comprendre pourquoi tel objet est utile ou néfaste aux mouvements des animaux.",
    de="TODE",
    en="The goal of the game is to help me set up my backyard layout, like in a simple garden-version of 'simcity'.")

txt_tutorial_play = Text(
    color=color.white,
    fr="Démarrer",
    de="Starten",
    en="Start")

# INTERACTIONS

txt_start_fr = "[b] DEMARRER LE JEU EN FRANCAIS [/b]"
txt_start_de = "[b] STARTEN DAS SPIEL AUF DEUTSCH [/b]"
txt_start_en = "[b] START THE GAME IN ENGLISH [/b]"

txt_interact_problems = Text(
    color=color.white,
    fr="Problèmes",
    de="TODE",
    en="Problems")

txt_interact_solutions = Text(
    color=color.white,
    fr="Solutions",
    de="TODE",
    en="Solutions")

txt_interact_confirm = Text(
    fr="Confirmation: veux-tu vraiment arrêter le jeu ?",
    de="DE",
    en="Confirmation: stop playing this game ?")

txt_interact_confirm_lang = "Tu pourras changer la langue en redémarrant le jeu. Du kannst die Sprache wechseln. You can change the language by stopping the game."

txt_interact_continue = Text(
    fr="Non, continuer à jouer ce jeu",
    de="DE",
    en="No, continue playing this game")

txt_interact_stop = Text(
    fr="Oui, arrêter et redémarrer le jeu",
    de="DE",
    en="Yes, Abort game and start over")

txt_interact_infos = Text(
    fr="Tu peux accéder à plus d'informations ou passer à la suite du jeu.",
    de="TODE",
    en="TOEN")

txt_interact_forward = Text(
    color=color.white,
    fr="Continuer",
    de="TODE",
    en="TOEN")

txt_interact_timeout = Text(
    color=color.magenta,
    fr="Aucune action réalisée, redémarrage du jeu dans 10 secondes.",
    de="TODE",
    en="TOEN")

txt_end_level1 = Text(
    color=color.green,
    fr="Tu as obtenu plus de 3 points, ton jardin est un véritable couloir biologique! Ton arrière-cour est un endroit où les divers animaux se sentent bien pour vivre, se déplacer, se reproduire, se nourrir, entre autres.",
    de="TODE",
    en="TOEN")

txt_end_level2 = Text(
    color=color.orange,
    fr="Tu as obtenu entre 0 et 3 points, ton jardin est partiellement un couloir biologique, mais cela pourrait être mieux! Certains animaux sentent bien pour vivre, se déplacer, se reproduire, se nourrir, mais d'autres auront plus de difficultés.",
    de="TODE",
    en="TOEN")

txt_end_level3 = Text(
    color=color.magenta,
    fr="Tu n'as obtenu que des points négatifs, ton jardin n'est pas du tout un couloir biologique! La plupart des animaux auront beaucoup de difficultés pour vivre, se déplacer, se reproduire, se nourrir, entre autres.",
    de="TODE",
    en="TOEN")

txt_end_play = Text(
    fr="Redémarrer et jouer à nouveau",
    de="TODE",
    en="TOEN")

# SPEECH
# instructions
txt_game_move_play = Text(
    fr="Choisis un objet et glisse-le sur la zone clignotante",
    de="TODE",
    en="Choose an object and drag it to the blinking area")

# game move when target is not reached
txt_game_move_unreached = Text(
    fr="Pas le bon endroit, essaie encore...",
    de="TODE",
    en="Not the right spot, try again...")

# game move target reached, correct positive element
txt_game_move_positive = Text(
    color=color.green,
    fr="Bravo, bien joué!",
    de="TODE",
    en="Well done!")

# game move target reached, uncorrect negative element
txt_game_move_negative = Text(
    color=color.magenta,
    fr="Ce n'est pas le meilleur choix...",
    de="TODE",
    en="It is not the best choice...")

# game move target reached, uncorrect negative element
txt_game_move_pass = Text(
    color=color.orange,
    fr="Catégorie passée, aucun point attribué",
    de="TODE",
    en="Skipped category, no point recieved")

# quiz

txt_quiz_intro_fr = "Merci d'évaluer l'exposition pour participer au concours"
txt_quiz_intro_de = "TODE Bitte geben Sie uns eine Note"
txt_quiz_intro_conf_fr = "Réponse enregsitrée, merci!"
txt_quiz_intro_conf_de = "TODE Antwort gespeichert, Danke!"

txt_quiz_conf = Text(
    fr="Merci pour ton évaluation. Tu peux maintenant participer au concours en répondant correctement à quelques questions.",
    de="TODE")

txt_info_problems_fr = "" + color.magenta + "[b]Problèmes:[/b] \n" + color.end
txt_info_problems_de = "" + color.magenta + "[b]Problemen:[/b] \n" + color.end
txt_info_problem_fr = "" + color.magenta + "[b]Problème:[/b] " + color.end
txt_info_problem_de = "" + color.magenta + "[b]Problem:[/b] " + color.end
txt_info_warning_fr = "" + color.magenta + "[b]Attention:[/b] " + color.end
txt_info_warning_de = "" + color.magenta + "[b]Achtung:[/b] " + color.end
txt_info_solutions_fr = "" + color.green + "[b]Solutions:[/b] \n" + color.end
txt_info_solutions_de = "" + color.green + "[b]TODE:[/b] \n" + color.end

txt_info_pond = Text(
    fr=" •   Un étang constitue un [b]relais important dans un corridor biologique.[/b]\n" \
       " •   Beaucoup d’amphibiens et d’insectes aquatiques, comme les larves de libellules, y passent une partie de leur vie. \n\n" \
       + txt_info_warning_fr + "\n" +
       " •   [b]Ne pas y installer d’animaux[/b], ils viendront très vite tous seuls. \n" \
       " •   [b]Ne pas introduire de poissons ou de tortues[/b], ils mangeraient les têtards et les larves de libellules.\n" \
       " •   [b]Ne pas construire un étang si le jardin est entouré de routes.[/b]\n" \
       " •   Plus d’infos dans la [b]brochure Pro Natura « Des amphibiens près de chez vous »[/b]",
    de=" •   Weiher sind [b]wichtige Elemente von Vernetzungsachsen.[/b]\n" \
       " •   Zahlreiche Amphibien und viele aquatische Insekten wie Libellenlarven verbringen darin einen Teil ihres Lebens.\n\n" \
       + txt_info_warning_de + "\n" +
       " •   [b]Setzen Sie keine Tiere in den Weiher um[/b] – sie werden rasch von selbst zuwandern.\n" \
       " •   [b]Setzen Sie keine Fische oder Schildkröten in den Weiher[/b], denn sie fressen die Kaulquappen und Libellenlarven.\n" \
       " •   [b]Bauen Sie keinen Weiher, wenn Ihr Garten von Strassen umgeben ist.[/b]\n" \
       " •   Weitere Infos im Pro Natura Faltblatt [b]«Amphibien rund ums Haus».[/b]",
    en="Pond")

txt_info_pool = Text(
    fr=txt_info_problems_fr +
       " •   [b]Les grenouilles, les hérissons ou les insectes tombent et meurent noyés[/b] dans les piscines car ils n’arrivent pas à en escalader les parois verticales, trop hautes et glissantes. \n" \
       " •   [b]Le chlore est très nocif pour les amphibiens[/b] car ils respirent par la peau.\n\n" \
       + txt_info_solutions_fr +
       " •   [b]Installer une petite rampe[/b] qui permettra aux animaux de ressortir de l’eau sans difficulté.\n" \
       " •   [b]Veiller à éteindre l’éclairage de la piscine durant la nuit[/b] pour éviter un plongeon mortel à bon nombre d’insectes.\n" \
       " •   [b]Eviter de désinfecter la piscine avec du chlore.[/b] Les traitements par électrolyse ou à base de magnésium sont des alternatives moins nocives.\n" \
       " •   Plus d’infos dans la [b]Charte des jardins[/b] et dans la [b]brochure Pro Natura « Des amphibiens près de chez vous ».[/b]",
    de=txt_info_problems_de +
       " •   [b]Wenn Frösche, Igel oder Insekten in ein Schwimmbecken fallen, ertrinken sie[/b], weil sie an den senkrechten und glatten Wänden nicht mehr hochklettern können.\n" \
       " •   [b]Chloriertes Wasser ist für Amphibien sehr schädlich[/b], weil die Tiere auch über die Haut atmen.\n\n" \
       + txt_info_solutions_de +
       " •   [b]Bringen Sie eine kleine Rampe an[/b], über welche die Tiere problemlos aus dem Wasser steigen können.\n" \
       " •   [b]Schalten Sie die Poolbeleuchtung über Nacht aus[/b], damit die Insekten nicht haufenweise ertrinken.\n" \
       " •   [b]Desinfizieren Sie Ihr Schwimmbad möglichst nicht mit Chlor.[/b] Als weniger schädliche Alternativen bieten sich die Elektrolyse und die Wasseraufbereitung mit Magnesium an.\n" \
       " •   Weitere Infos in der [b]Garten-Charta[/b] und im Pro Natura Faltblatt [b]«Amphibien rund ums Haus».[/b]",
    en="Swimming pool")

txt_info_hedge_good = Text(
    fr=" •   [b]Exemple d’espèces d’arbustes indigènes[/b] : fusain d’Europe, chèvrefeuille, noisetier, cornouiller sanguin\n" \
       " •   [b]Les haies indigènes sont des éléments essentiels des corridors biologiques.[/b]\n" \
       " •   [b]Beaucoup d’animaux se déplacent le long de ces haies.[/b]\n" \
       " •   [b]Ces haies offrent des abris et de la nourriture à beaucoup d’animaux.[/b]\n" \
       " •   [b]Ces haies demandent peu d’entretien.[/b]\n" \
       " •   [b]Ces haies amènent de la couleur[/b] dans le jardin et permettent de confectionner de [b]délicieux sirops ou confitures.[/b]\n" \
       " •   Plus d’infos dans la [b]Charte des jardins[/b] ou dans la [b]brochure de Pro Natura Genève «Planter des haies indigènes».[/b]",
    de=" •   [b]Beispiele für einheimische Straucharten: Pfaffenhütchen, Heckenkirsche, Hasel, Hartriegel\n" \
       " •   [b]Einheimische Hecken sind wichtige Elemente von Vernetzungsachsen.[/b]\n" \
       " •   [b]Viele Tiere bewegen sich entlang von Hecken.[/b]\n" \
       " •   [b]Einheimische Hecken bieten einer grossen Zahl von Tieren Unterschlupf und Nahrung.[/b]\n" \
       " •   [b]Sie benötigen nicht viel Pflege.[/b]\n" \
       " •   [b]Sie bringen Farbe[/b] in den Garten und liefern köstliche Zutaten zur Herstellung von [b]Sirups und Konfitüren.[/b]\n" \
       " •   Weitere Infos in der [b]Garten-Charta[b] oder im Pro Natura Faltblatt [b]“Invasive Neophyten im Garten».[/b]",
    en="Hedge of various native species")

txt_info_hedge_bad = Text(
    fr=txt_info_problems_fr +
       " •   [b]Le thuya et la laurelle sont des arbustes asiatiques[/b] auxquels très peu d’animaux indigènes sont adaptés. \n" \
       " •   [b]Ces « murs » verts n’apportent ni nourriture, ni abri à la faune[/b], même s’ils isolent bien de la rue et des voisins.\n" \
       " •   [b]Une haie de thuyas est infranchissable pour les animaux.[/b]\n" \
       " •   [b]La laurelle est toxique pour l’homme et pour beaucoup de papillons.[/b] \n" \
       " •   [b]La laurelle est une plante envahissante[/b] qui a la fâcheuse tendance à s’échapper des jardins pour s’établir en forêt. \n\n" \
       + txt_info_solutions_fr +
       " •   [b]Remplacer votre haie de thuyas ou de laurelles par une haie indigène[/b] constituée d’espèces d’arbustes locaux. Elle offrira de la nourriture et des abris aux animaux ainsi que des [b]petits fruits ou fleurs pour fabriquer de délicieux sirops ou confitures.[/b] \n" \
       " •   [b]Faire quelques trous dans votre haie[/b], au niveau du sol, pour permettre à des animaux tels que les hérissons de se déplacer d’un jardin à l’autre. \n" \
       " •   Plus d’infos dans la [b]Charte des jardins[/b] ou dans la [b]brochure de Pro Natura Genève «Planter des haies indigènes».[/b]",
    de=txt_info_problems_de +
       " •   [b]Thuja und Kirschlorbeer sind asiatische Sträucher[/b], die nur für sehr wenige einheimische Tiere nützlich sind.\n" \
       " •   Als grüne «Wände» schirmen sie zwar gut vor Strassen oder Nachbarn ab, [b]der Tieren bieten sie aber weder Nahrung noch Unterschlupf.[/b]\n" \
       " •   [b]Thujahecken stellen für Tiere unüberwindbare Hindernisse dar.[/b]\n" \
       " •   [b]Der Kirschlorbeer ist für Menschen und auch für viele Schmetterlinge giftig.[/b]\n" \
       " •   [b]Der Kirschlorbeer ist eine invasive Pflanze[/b], die häufig zum Gartenflüchtling wird und sich in den Wäldern ansiedelt.\n\n" \
       + txt_info_solutions_de +
       " •   [b]Ersetzen Sie Ihre Thuja- oder Kirschlorbeerhecke durch eine einheimische Hecke[/b] aus Wildsträuchern aus der Region. Eine solche Hecke bietet den Tieren Nahrung und Unterschlupf und liefert [b]Beeren oder Blüten, aus denen sich feine Sirups und Konfitüren herstellen lassen.[/b]\n" \
       " •   [b]Öffnen Sie am Fuss Ihrer Hecke ein paar Durchgänge[/b], damit Igel und andere Tiere mühelos von einem in den anderen Garten gelangen können.\n" \
       " •   Weitere Infos in der [b]Garten-Charta[/b] oder im Pro Natura Faltblatt [b]“Invasive Neophyten im Garten».[/b]",
    en="Hedge of thuja and laurel")

txt_info_fence_nospace = Text(
    fr=txt_info_problem_fr + "Une barrière ou un grillage touchant le sol [b]ne laisse pas passer les animaux terrestres[/b] tels que les hérissons ou les renards.\n\n" \
       + txt_info_solutions_fr +
       " •   Surélever la barrière d’au moins 15 centimètres.\n" \
       " •   Faire un trou dans le bas du grillage d’au moins 15 centimètres de hauteur et de largeur.\n" \
       " •   Plus d’infos dans la Charte des jardins",
    de=txt_info_problem_de + "Zäune oder Gitter, die bis auf den Boden reichen, [b]sind Barrieren für Landtiere wie Igel oder Füchse.[/b]\n\n" \
       + txt_info_solutions_de +
       " •   [b]Heben Sie den Zaun an[/b], mindestens um 15 Zentimeter.\n" \
       " •   [b]Schneiden Sie am Boden ein Loch in das Gitter[b/], mindestens 15 Zentimeter hoch und breit.\n" \
       " •   Weitere Infos in der Garten-Charta.",
    en="Garden fence close to the ground ")

# two fences have the same texts (chang it if not logical)
txt_info_fence_space = txt_info_fence_nospace

txt_info_fence_wall = Text(
    fr=txt_info_problem_fr + "Un mur en béton est [b]infranchissable pour beaucoup d’animaux.[/b]\n" \
       + txt_info_solutions_fr +
       " •   [b]Faire pousser des plantes grimpantes sur votre mur.[/b] Le lierre, par exemple, servira de cachette et de garde-manger à de nombreux animaux et permettra également aux écureuils d’escalader le mur pour se déplacer dans le jardin voisin.\n" \
       " •   [b]Créer de petites ouvertures[/b] d’au moins 15 centimètres de largeur et de hauteur, près du sol. Les hérissons et les grenouilles, par exemple, pourront facilement passer de l’autre côté du mur.\n" \
       " •   Plus d’infos dans la [b]Charte des jardins.[/b]",
    de=txt_info_problem_de + "Betonmauern sind [b]für viele Tiere unüberwindbare Hindernisse.[/b]\n" \
       + txt_info_solutions_de +
       " •   [b]Lassen Sie Kletterpflanzen an Ihrer Mauer hochwachsen.[/b] Efeu zum Beispiel wird von vielen Tieren als Versteck und Vorratskammer genutzt und dient Eichhörnchen als Klettergerüst, wenn ihnen die Mauer den Weg in den Nachbargarten versperrt.\n" \
       " •   [b]Öffnen Sie am Fuss der Mauer kleine Durchgänge[/b] von mindestens 15 Zentimeter Höhe und Breite, damit kleinere Tiere wie Igel oder Frösche auf die andere Seite der Mauer gelangen können.\n" \
       " •   Weitere Infos in der [b]Garten-Charta.[/b]",
    en="Concrete wall")

txt_info_floor_grass = Text(
    fr=" •   [b]Le gravier, les galets ou les pavés herbeux sont beaucoup moins chauffés par le soleil et restent frais[/b], même sous un soleil plombant.\n" \
       " •   [b]Les petits animaux terrestres ne se brûlent pas[/b] en passant sur ce genre de surface.\n" \
       " •   Le gravier, les galets ou les pavés herbeux [b]demandent peu d’entretien.[/b]\n" \
       " •   [b]L’eau s’infiltre naturellement dans le sol[/b], évitant la formation de boue sur votre terrain. ",
    de=" •   [b]Kies, Schotter oder Rasengittersteine heizen sich in der Sonne viel weniger stark auf.[/b] Eine Terrasse mit Rasengittersteinen bleibt frisch, auch wenn die Sonne brennt.\n" \
       " •   [b]Kleine Landtiere verbrennen sich nicht[/b], wenn sie die Fläche überqueren.\n" \
       " •   [b]Kies, Schotter oder Rasengittersteine benötigen nur wenig Unterhalt.[/b]\n" \
       " •   [b]Das Wasser versickert auf natürliche Weise im Untergrund[/b], ohne dass der Boden verschlammt.",
    en="Patio with grassy floor")

txt_info_floor_stone = Text(
    fr=txt_info_problems_fr +
       " •   [b]De grandes dalles de béton ou des pierres foncées chauffent très vite au soleil.[/b]\n" \
       " •   [b]Une terrasse chauffée par le soleil est infranchissable pour de nombreux petits animaux terrestres.[/b]\n" \
       " •   [b]L’eau de pluie ne peut pas s’infiltrer dans le sol[/b], le terrain à proximité de la terrasse risque donc de devenir très boueux.\n\n"
       + txt_info_solutions_fr +
       " •   [b]Le gravier, les galets ou les pavés herbeux sont beaucoup moins chauffés par le soleil et restent frais[/b], même sous un soleil plombant.",
    de=txt_info_problems_de +
       " •   [b]Grosse Betonplatten oder dunkle Steine werden in der Sonne schnell heiss.[/b]\n" \
       " •   [b]Eine von der Sonne aufgeheizte Terrasse ist für viele kleine Landtiere nicht begehbar.[/b]\n" \
       " •   [b]Das Regenwasser kann nicht im Untergrund versickern[/b], sodass der Boden rund um die Terrasse verschlammt\n\n."
       + txt_info_solutions_de +
       " •   [b]Kies, Schotter oder Rasengittersteine heizen sich in der Sonne viel weniger stark auf.[/b] Eine Terrasse mit Rasengittersteinen bleibt frisch, auch wenn die Sonne brennt.",
    en="Patio with black sandstone floor")

txt_info_shelter_wood = Text(
    fr=txt_info_problem_fr + "Beaucoup de personnes se débarrassent des branches et des feuilles mortes[/b] pour avoir un jardin « propre ». Or, beaucoup d’animaux ont besoin des feuilles et du bois morts pour se nourrir, se cacher ou pondre.\n\n" \
       + txt_info_solutions_fr +
       " •   [b]Rassembler les feuilles et le bois mort en petits tas[/b] qui offriront un refuge bienvenu pour les hérissons ou les insectes, par exemple. \n" \
       " •   [b]Ne jamais brûler un tas de feuilles ou de branches[/b], vous risqueriez de brûler vifs tous les animaux qui y sont cachés.\n" \
       " •   Plus d’infos dans la [b]Charte des jardins.[/b]",
    de=txt_info_problem_de + "Viele Leute räumen heruntergefallene Zweige und Blätter weg[/b], um einen «sauberen» Garten zu haben. Zahlreiche Tiere sind aber angewiesen auf Laub und Totholz als Nahrungsquelle, Versteck oder Eiablageplatz.\n\n" \
       + txt_info_solutions_de +
       " •   [b]Schichten Sie Laub und Totholz zu kleinen Haufen auf.[/b] So entstehen wertvolle Schlupfwinkel für Igel, Insekten und andere Tiere.\n" \
       " •   [b]Zünden Sie Laub- oder Asthaufen niemals an.[/b] Die vielen Tiere, die darin hausen, würden bei lebendigem Leib verbrennen.\n" \
       " •   Weitere Infos in der [b]Garten-Charta.[/b]",
    en="Pile of old wood and dead leafs")

txt_info_shelter_flower = Text(
    fr=" •   [b]Les prairies fleuries sont des éléments importants des corridors biologiques.[/b]\n" \
       " •   [b]Les prairies fleuries sont utiles à beaucoup d’animaux.[/b] Les papillons, par exemple, y trouvent du nectar pour se nourrir et des plantes où pondre leurs œufs. C’est aussi un refuge pour beaucoup de petits mammifères, oiseaux, amphibiens et insectes. \n" \
       " •   [b]Une prairie fleurie demande beaucoup moins d’entretien que le gazon[/b], il suffit de la faucher une ou deux fois par année. Plus d’infos dans les [b]brochures de Pro Natura « Des papillons dans son jardin » et « Prairies fleuries, aménagement et entretien ».[/b]\n" \
       " •   " + txt_info_warning_fr + " Pour une belle prairie fleurie, [b]ne pas utiliser d’engrais ou de désherbant.[/b]\n" \
                                       " •   [b]Ne pas utiliser de pesticides[/b], ce sont des poisons pour la plupart des animaux qui se réfugient dans les prairies fleuries.",
    de=" •   [b]Blumenwiesen sind wichtige Elemente von Vernetzungsachsen.[/b]\n" \
       " •   [b]Blumenwiesen sind für viele Tiere nützlich.[/b] So liefern sie zum Beispiel Schmetterlingen Nahrung in Form von Nektar sowie geeignete Pflanzen für die Eiablage. Sie dienen aber auch zahlreichen kleinen Säugetieren, Vögeln, Amphibien und Insekten als Unterschlupf.\n" \
       " •   [b]Eine Blumenwiese braucht viel weniger Pflege als ein Rasen.[/b] Es genügt, sie ein- oder zweimal pro Jahr zu mähen. Weitere Infos im Pro Natura Faltblatt [b]«Schmetterlinge im Garten»[/b] und in der Pro Natura Broschüre [b]„Blumenwiesen anlegen und pflegen“[/b].\n" \
       " •   " + txt_info_warning_de + " Wer eine schöne Blumenwiese wünscht, darf [b]weder Dünger noch Unkrautvertilger einsetzen.[/b]\n" \
                                       " •   [b]Verwenden Sie keine Pestizide. Sie sind für die meisten Tiere der Blumenwiesen giftig.[/b]",
    en="Portion of meadow covered in flowers")

txt_info_animal_goat = Text(
    fr=" •   [b]Les chèvres naines sont de véritables tondeuses écologiques[/b] qui vous « mâcheront » le travail dans votre jardin.\n" \
       " •   [b]Les moutons sont utilisés pour les plus grands espaces.[/b] La Commune d’Yverdon-les-Bains et la Ville de Lausanne les utilisent depuis plusieurs années pour la tonte de certains parcs publiques.  \n" \
       " •   [b]Les petits animaux qui vivent dans la pelouse ne sont plus pris par surprise dans les lames acérées de la tondeuse à gazon.[/b]\n" \
       " •   Il est possible de [b]louer des chèvres et des moutons[/b] juste pour quelques jours.\n" \
       " •   Plus d’infos : contacter [b]La Mergerie du Bonheur[/b] www.la-mergerie.ch.\n" \
       " •   " + txt_info_warning_fr + "[b]Les chèvres doivent toujours être au moins deux.[/b]",
    de=" •   [b]Zwergziegen sind regelrechte Ökomäher[/b], die Ihnen im Garten die Arbeit abnehmen können.\n" \
       " •   [b]Schafe eignen sich für den Unterhalt grösserer Flächen.[/b] Die Gemeinde Yverdon-les-Bains und die Stadt Lausanne setzen seit mehreren Jahren Schafe für das «Mähen» einzelner Grünanlagen ein.\n" \
       " •   [b]Die Kleintiere, die in der Wiese leben, werden nicht mehr von den scharfen Klingen des Rasenmähers getötet.[/b]\n" \
       " •   Es ist auch möglich, [b]Ziegen und Schafe nur für ein paar Tage zu mieten.[/b]\n" \
       " •   Weitere Auskünfte erteilt die [b]Mergerie du Bonheur[/b] www.la-mergerie.ch\n" \
       " •   " + txt_info_warning_de + "[b]Ziegen müssen immer mindestens zu zweit sein.[/b]",
    en="Pygmy dwarf goats")

txt_info_animal_cat = Text(
    fr=txt_info_problems_fr +
       " •   [b]Les chats sont des prédateurs redoutables.[/b] Certaines études les citent même comme [b]la première cause de mortalité pour la petite faune sauvage[/b] (oiseaux, petits mammifères, amphibiens et insectes).\n" \
       " •   [b]Les colliers à clochettes ne sont pas efficaces[/b] pour empêcher les chats de s’attaquer à la petite faune sauvage car ils développent des stratégies pour chasser encore plus furtivement et discrètement.\n\n"
       + txt_info_solutions_fr +
       " •   [b]Mettre un collier très coloré au chat[/b] pour le rendre plus visible et permettre à beaucoup d’animaux de s’enfuir. \n" \
       " •   [b]Dans les arbres, installer des collerettes[/b] qui empêcheront le chat de grimper. \n" \
       " •   [b]Garder le chat à l’intérieur durant la nuit[/b] car c’est le moment où beaucoup de petits animaux sortent et se déplacent.",
    de=txt_info_problems_de +
       " •   [b]Katzen sind geschickte Jäger.[/b] Manchen Studien zufolge sind sie sogar [b]die häufigste Todesursache für kleine Wildtiere[/b] (Vögel, kleine Säugetiere, Amphibien und Insekten).\n" \
       " •   [b]Ein Halsband mit Glöckchen hindert die Katze nicht[/b] daran, kleine Wildtiere zu erbeuten. Sie entwickelt dann einfach Strategien, um noch lautloser und vorsichtiger zu jagen.\n\n"
       + txt_info_solutions_de +
       " •   [b]Ihr Balkon kann ein wichtiger Trittstein in einer Vernetzungsachse werden.[b]\n" \
       " •   [b]Mit ein paar Gewürzpflanzen machen Sie aus Ihrem Balkon eine Bar für Schmetterlinge.[/b] Diese saugen bei den Blüten von Origano, Melisse, Thymian oder Rosmarin gerne Nektar.\n" \
       " •   [b]Die Kräuter verströmen angenehme Düfte und liefern Ihnen die nötigen Zutaten für köstliche Tees und würzige Speisen.[/b]",
    en="cat")

txt_info_balcony_herbs = Text(
    fr=" •   [b]Votre balcon peut être un relais important dans un corridor biologique.[/b]\n" \
       " •   [b]Quelques plantes aromatiques transformeront votre balcon en véritable bar à papillons[/b] qui raffolent du nectar des fleurs d’origan, de mélisse, de thym ou de romarin. \n" \
       " •   [b]Ces plantes parfument agréablement votre balcon et vous permettent de réaliser de délicieuses tisanes et d’aromatiser vos plats.[/b]",
    de=" •   [b]Ihr Balkon kann ein wichtiger Trittstein in einer Vernetzungsachse werden.[b]\n" \
       " •   [b]Mit ein paar Gewürzpflanzen machen Sie aus Ihrem Balkon eine Bar für Schmetterlinge.[/b] Diese saugen bei den Blüten von Origano, Melisse, Thymian oder Rosmarin gerne Nektar.\n" \
       " •   [b]Die Kräuter verströmen angenehme Düfte und liefern Ihnen die nötigen Zutaten für köstliche Tees und würzige Speisen.[/b]",
    en="en")

txt_info_balcony_geranium = Text(
    fr=txt_info_problems_fr +
       " •   [b]Les géraniums que l’on trouve dans le commerce sont généralement des espèces africaines[/b] qui ont très peu d’intérêt pour les insectes de Suisse. \n\n" \
       + txt_info_solutions_fr +
       " •   [b]Cultiver des plantes aromatiques[/b] telles que la mélisse ou le romarin sur votre balcon. Elles sont [b]utiles aux insectes indigènes et permettent de faire de délicieuses tisanes ou d’aromatiser vos plats.[/b]",
    de=txt_info_problems_de +
       " •   [b]Bei den Geranien, die im Handel angeboten werden, handelt es sich in der Regel um afrikanische Arten[/b], die für die Insekten der Schweiz kaum von Nutzen sind.\n\n" \
       + txt_info_solutions_de +
       " •   [b]Ziehen Sie auf Ihrem Balkon Gewürzkräuter[/b] wie Melisse oder Rosmarin. [b]Sie sind für die einheimischen Insekten nützlich, liefern feine Tees und aromatisieren Ihre Speisen.[/b]",
    en="Geraniums")
