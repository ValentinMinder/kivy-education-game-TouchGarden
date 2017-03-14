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

txt_main_title_short = "TouchGarden"

txt_main_title = Text(
    fr="Mon jardin peut être un corridor biologique!",
    de="Mein Garten kann ein Wildtierkorridor sein!",
    en="My garden could be a wildlife corridor!")

txt_main_title_fr = Text(
    fr="Mon jardin peut être un corridor biologique!",
    de="Mon jardin peut être un corridor biologique!")

txt_main_title_de = Text(
    fr="Mein Garten kann ein Wildtierkorridor sein!",
    de="Mein Garten kann ein Wildtierkorridor sein!")

txt_main_title_en = Text(
    fr="My garden could be a wildlife corridor!",
    de="My garden could be a wildlife corridor!")

txt_watermark_heig = Text(
    fr="Projet de service civil réalisé en partenariat entre Pro Natura et l'HEIG-VD (IICT). Retrouvez ce jeu dans l'exposition du Centre Pro Natura de Champ-Pittet du 18 mars au 1er novembre 2017.",
    de="Ein Projekt des Zivildienstes, in Zusammenarbeit mit Pro Natura und der Fachhochschule HEIG-VD. Das Spiel ist im Ausstellung im Champ-Pittet vom 18. März bis am 1. November 2017 vorzufinden.",
    en="Swiss civilian project in a partnership bewteen Pro Natura and HEIG-VD School of Engineering. Find this game in the exhibition of Champ-Pittet, Yverdon, from March 18th to November 1st 2017.")

# CATEGORIES and objects names

# CATEGORIES TITLES
txt_cat_water = Text(
    fr="Plans d'eau",
    de="Gewässer",
    en="Bodies of water")

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
    fr="Haie d'espèces indigènes",
    de="Einheimische Hecke",
    en="Hedge of various native species")

txt_cat_hedge_bad = Text(
    fr="Haie de thuyas ou de laurelles",
    de="Thuja- oder Kirschlorbeerhecke",
    en="Hedge of thuja and laurel")

txt_cat_fence = Text(
    fr="Murs et barrières",
    de="Mauern und Absperrungen",
    en="Fences and walls")

txt_cat_fence_space = Text(
    fr="Barrière de jardin",
    de="Gartenzaun",
    en="Garden fence")

txt_cat_fence_wall = Text(
    fr="Mur en béton",
    de="Betonmauer",
    en="Concrete wall")

txt_cat_floor = Text(
    fr="Terrasses",
    de="Terrassen",
    en="Patios")

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
    de="Unterschlüpfe und Verstecke",
    en="Shelters and hideouts")

txt_cat_shelter_wood = Text(
    fr="Tas de feuilles et bois morts",
    de="Laubhaufen und Totholz",
    en="Pile of old wood and dead leafs")

txt_cat_shelter_flower = Text(
    fr="Coin de prairie fleurie",
    de="Ein Stück Blumenwiese",
    en="Portion of meadow covered in flowers")

txt_cat_animal = Text(
    fr="Animaux de compagnie",
    de="Haustiere",
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
    de="Balkonpflanzen",
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

txt_impressum = Text(
    fr="Impressum",
    de="Impressum")

txt_impressum_full = \
    "[b]Jeu pédagogique et interactif d'éducation à l'environnement[/b]\n" \
    "Interaktives pädagogisches Spiel zur Umweltausbildung\n" \
    "[i]Interactive serious game about environmental education[/i]\n\n" \
    "[b]Mandataire[/b]: Centre Pro Natura de Champ-Pittet, Yverdon-les-Bains, Suisse\n" \
    "[b]Illustrations[/b]: Ariane Nicollier / Fabrica Collective, Lucas Oettli\n" \
    "[b]Conception graphique[/b]: Marc-Olivier Schatz\n" \
    "[b]Contenus et textes[/b]: Briséïs Castella, Layne Meinich\n" \
    "[b]Traductions [i]deutsch[/i][/b]: Alena Wehrli, Florence Kupferschmid, Mira Maeder\n" \
    "[b]Relectures[/b]: Marie Bovay, Andrea Strässle, Lucas Oettli, Alan Regley\n" \
    "[b]Développement informatique et programmation[/b]: Valentin Minder\n" \
    "[b]Partenaire[/b]: Institute for Information and Communication Technologies ([b]IICT[/b])\n" \
    "Haute Ecole d'Ingénierie et de Gestion Vaud ([b]HEIG-VD[/b])\n" \
    "Haute Ecole Spécialisée de Suisse Occidentale ([b]HES-SO[/b])\n" \
    "[i]University of Applied Sciences and Arts Western Switzerland[/i]\n\n" \
    "[b]Copyright (C)[/b] Pro Natura 2016-2018\n"

txt_scenery_notxt = Text(
    fr="",
    de="",
    en="")

# general layout
txt_scenery_category = Text(
    fr="Catégorie",
    de="Kategorie",
    en="Category")

txt_scenery_score = Text(
    fr="Score",
    de="Punktzahl",
    en="Score")

# RECOVER OPTIONS (window)

txt_recover_header = Text(
    fr="Ce n'était pas le meilleur choix...",
    de="Das war nicht die beste Wahl...",
    en="This wasn't the best choice...")

txt_recover_infos = Text(
    color=color.white,
    fr="Plus d'infos",
    de="Mehr Infos",
    en="Tell me more")

txt_recover_keep = Text(
    fr="Garder",
    de="Behalten",
    en="Keep")

txt_recover_remove = Text(
    fr="Enlever",
    de="Entfernen",
    en="Remove")

txt_recover_replace = Text(
    fr="Remplacer",
    de="Ersetzen",
    en="Replace")

txt_recover_correct = Text(
    fr="Corriger",
    de="Anpassen",
    en="Adapt")

# WELCOME AND INSTRUCTIONS
txt_tutorial_welcome_p0 = Text(
    fr="Bienvenue dans mon jardin !",
    de="Herzlich Willkommen in meinem Garten!",
    en="Welcome in my garden!")
txt_dot = Text(fr="  •  ", de="  •  ")
txt_tutorial_welcome_p1 = Text(
    fr="\n\n[b]BUT DU JEU[/b]\n" \
       "Aménager des corridors biologiques dans son jardin.\n\n\n" \
       "[b]DEROULEMENT DU JEU[/b]\n" \
       "[anchor=dot000x]Dans la colonne de gauche, une série d’objets pour aménager le jardin apparaissent.\n" \
       "[anchor=dot000y]Choisir un objet, le glisser et le déposer dans le jardin.\n" \
       "[anchor=dot000z]Chaque bon choix rapporte des points. Chaque mauvais choix enlève des points. Plus le score sera élevé, plus le jardin sera accueillant pour la faune qui le traverse.\n\n\n" \
       "[b]CHOIX STRATEGIQUE[/b]\n" \
       "On apprend en faisant des erreurs ! Il est possible de corriger les mauvaix choix et d’améliorer son score.\n",
    de="\n\n[b]ZIEL DES SPIELS[/b]\n" \
       "Gestalten eines biologischen Korridors im eigenen Garten\n\n" \
       "[b]ABLAUF DES SPIELS[/b]\n" \
       "[anchor=dot000x]In der linken Kolonne erscheint eine Auswahl von Objekten, mit denen der Garten eingerichtet werden kann.\n" \
       "[anchor=dot000y]Ein Objekt aussuchen, in den Garten ziehen und positionieren.\n" \
       "[anchor=dot000z]Jede gute Wahl bringt Punkte ein. Bei jeder schlechten Wahl werdent Punkte abgezogen. Je höher die Punktzahl, desto einladender ist der Garten für die Wildtiere, die ihn durchqueren.\n\n" \
       "[b]STRATEGIE[/b]\n" \
       "Aus Fehlern lernt man ! Eine schlechte Wahl kann korrigiert und die Punktzahl verbessert werden.",
    en="The goal of the game is to help me set up my backyard layout.")

txt_tutorial_play = Text(
    color=color.white,
    fr="Démarrer",
    de="Starten",
    en="Start")

# INTERACTIONS

txt_interact_problems = Text(
    color=color.white,
    fr="Problèmes",
    de="Probleme",
    en="Problems")

txt_interact_solutions = Text(
    color=color.white,
    fr="Solutions",
    de="Lösungen",
    en="Solutions")

txt_interact_confirm = Text(
    fr="Confirmation: veux-tu vraiment arrêter le jeu ?",
    de="Bestätigung: Willst du das Spiel wirklich beenden?",
    en="Confirmation: stop playing this game ?")

txt_interact_confirm_lang = "Tu pourras changer la langue en redémarrant le jeu. Du kannst die Sprache wechseln, indem du das Spiel neustartest. You can change the language by stopping the game."

txt_interact_continue = Text(
    fr="Non, continuer à jouer ce jeu",
    de="Nein, ich will weiterspielen",
    en="No, continue playing this game")

txt_interact_stop = Text(
    fr="Oui, arrêter et redémarrer le jeu",
    de="Ja, Spiel abbrechen und neustarten",
    en="Yes, Abort game and start over")

txt_interact_infos = Text(
    fr="Tu peux accéder à plus d'informations ou passer à la suite du jeu.",
    de="Du kannst noch mehr Informationen abrufen oder weiterspielen",
    en="TOEN")

txt_interact_forward = Text(
    color=color.white,
    fr="Continuer",
    de="Weiter- spielen",
    en="TOEN")

txt_interact_timeout = Text(
    color=color.magenta,
    fr="Aucune action réalisée, redémarrage du jeu dans 10 secondes.",
    de="Keine Handlungen vorgenommen, das Spiel wird in 10 Sekunden neugestartet",
    en="TOEN")

txt_end_level1 = Text(
    color=color.green,
    fr="[b]Bravo et félicitations ![/b]\n\n[b]Vous avez obtenu plus de 3 points, votre jardin est un véritable corridor biologique![/b] Les animaux s’y sentent bien pour vivre, se déplacer, se reproduire, se nourrir, etc…",
    de="[b]Herzlichen Glückwunsch ![/b]\n\n[b]Sie haben mehr als 3 Punkte erreicht, Ihr Garten ist ein echter biologischer Korridor![/b] Die Tiere fühlen sich wohl bei Ihnen und können sich frei bewegen,  fortpflanzen, ernähren etc…",
    en="TOEN")

txt_end_level2 = Text(
    color=color.orange,
    fr="[b]Bravo mais vous pouvez encore apporter quelques améliorations![/b]\n\n[b]Vous avez obtenu entre 0 et 3 points, votre jardin est peut-être un corridor biologique pour quelques animaux[/b], mais pour d’autres, il y aura des pièges!",
    de="[b]Nicht schlecht, aber Sie können noch einige Verbesserungen anbringen! [/b]\n\n[b] Sie haben zwischen 0 und 3 Punkten erreicht, Ihr Garten kann einigen Tieren als biologischer  Korridor dienen[/b]. Für  andere jedoch birgt er Fallen!",
    en="TOEN")

txt_end_level3 = Text(
    color=color.magenta,
    fr="[b]C'est pas terrible… [/b]\n\n[b]Vous n’avez obtenu que des points négatifs, votre jardin n'est pas du tout un corridor biologique![/b]\n La plupart des animaux auront beaucoup de difficultés pour vivre, se déplacer, se reproduire et se nourrir chez vous.",
    de="[b]Nicht gerade umwerfend… [/b]\n\n[b] Sie haben nur Negativpunkte erhalten, Ihr Garten ist überhaupt kein biologischer Korridor![/b]\n Die meisten Tierarten werde grosse Schwierigkeiten haben, sich bei Ihnen frei  zu bewegen,  fortzupflanzen und zu ernähren.",
    en="TOEN")

txt_end_play = Text(
    fr="Redémarrer et jouer à nouveau",
    de="Spiel neustarten und nochmals spielen",
    en="Abort game and start over again")

txt_end_score = Text(
    color=color.magenta,
    fr="Score final: \n",
    de="Endpunktzahl: \n",
    en="Final score: \n")

txt_end_category = Text(
    fr="[b]Fin du jeu![/b]",
    de="[b]Ende das Spiel![/b]",
    en="[b]The end![/b]")

txt_end_point = Text(
    color=color.magenta,
    fr=" point",
    de=" Punkt",
    en=" point")

txt_end_points = Text(
    color=color.magenta,
    fr=" points",
    de=" Punkte",
    en=" points")


# SPEECH
# instructions
txt_game_move_play = Text(
    fr="Choisis un objet et glisse-le sur la zone clignotante",
    de="Wähle ein Objekt aus und ziehe es in den blinkenden Bereich",
    en="Choose an object and drag it to the blinking area")

# game move when target is not reached
txt_game_move_unreached = Text(
    fr="Pas le bon endroit, essaie encore...",
    de="Nicht der richtige Ort, versuche es nochmals...",
    en="Not the right spot, try again...")

# game move target reached, correct positive element
txt_game_move_positive = Text(
    color=color.green,
    fr="Bravo, bien joué!",
    de="Gut gemacht!",
    en="Well done!")

# game move target reached, uncorrect negative element
txt_game_move_negative = Text(
    color=color.magenta,
    fr="Ce n'est pas le meilleur choix...",
    de="Das ist nicht die beste Wahl...",
    en="It is not the best choice...")

# game move target reached, uncorrect negative element
txt_game_move_pass = Text(
    color=color.orange,
    fr="Catégorie passée, aucun point attribué",
    de="übersprungene Kategorie, keine Punkte erreicht",
    en="Skipped category, no point recieved")

# quiz

txt_quiz_intro_fr = "Merci d'évaluer l'exposition pour participer au concours"
txt_quiz_intro_de = "Bitte geben Sie uns eine Bewertung um am Wettbewerb teilzunehmen"
txt_quiz_intro_conf_fr = "Réponse enregsitrée, merci!"
txt_quiz_intro_conf_de = "Antwort gespeichert, danke!"

txt_quiz_conf = Text(
    fr="Merci pour votre évaluation. Vous pouvez maintenant participer au concours en répondant correctement à quelques questions.",
    de="Vielen Dank für Ihre Bewertung. Sie können jetzt am Wettbewerb teilnehmen, indem Sie einige Fragen richtig beantworten.")

txt_quiz_end_positive = Text(
    fr="Bravo, vous avez répondu correctement à toutes les questions, vous allez participer au tirage au sort.",
    de="Bravo, Sie haben alle Fragen richtig beantwortet! Sie werden an der Auslosung teilnehmen.")

txt_quiz_end_negative = Text(
    fr="Vous avez fait quelques erreurs, malheureusement… à bientôt!",
    de="Sie haben leider einige Fehler gemacht… Auf Wiedersehen und bis bald!")

txt_quiz_tombola_start = Text(
    fr="Attention, tirage au sort en cours!",
    de="Achtung, die Auslosung findet statt!")

txt_quiz_tombola_win = Text(
    fr="Bravo, vous avez gagné! Veuillez vous présenter à la réception avec le code suivant:",
    de="Bravo, Sie haben gewonnen! Bitte melden Sie sich mit folgendem Code an der Rezeption:")

txt_quiz_tombola_win = Text(
    fr="Désolé, c'est perdu... à la prochaine!'",
    de="Leider kein Glück gehabt… bis zum nächsten Mal!")

txt_info_problems_fr = "" + color.magenta + "[b]Problèmes:[/b] \n" + color.end
txt_info_problems_de = "" + color.magenta + "[b]Problemen:[/b] \n" + color.end
txt_info_problem_fr = "" + color.magenta + "[b]Problème:[/b] " + color.end
txt_info_problem_de = "" + color.magenta + "[b]Problem:[/b] " + color.end
txt_info_warning_fr = "" + color.magenta + "[b]Attention:[/b] " + color.end
txt_info_warning_de = "" + color.magenta + "[b]Achtung:[/b] " + color.end
txt_info_solutions_fr = "" + color.green + "[b]Solutions:[/b] \n" + color.end
txt_info_solutions_de = "" + color.green + "[b]Lösungen:[/b] \n" + color.end

txt_info_pond = Text(
    fr="[anchor=dot100]Un étang constitue un [b]relais important dans un corridor biologique.[/b]\n" \
       "[anchor=dot101]Beaucoup d’amphibiens et d’insectes aquatiques, comme les larves de libellules, y passent une partie de leur vie. \n\n" \
       + txt_info_warning_fr + "\n" +
       "[anchor=dot102][b]Ne pas y installer d’animaux[/b], ils viendront très vite tous seuls. \n" \
       "[anchor=dot103][b]Ne pas introduire de poissons ou de tortues[/b], ils mangeraient les têtards et les larves de libellules.\n" \
       "[anchor=dot104][b]Ne pas construire un étang si le jardin est entouré de routes.[/b]\n" \
       "[anchor=dot105]Plus d’infos dans la [b]brochure Pro Natura « Des amphibiens près de chez vous[anchor=end] »[/b]",
    de="[anchor=dot100]Weiher sind [b]wichtige Elemente von Vernetzungsachsen.[/b]\n" \
       "[anchor=dot101]Zahlreiche Amphibien und viele aquatische Insekten wie Libellenlarven verbringen darin einen Teil ihres Lebens.\n\n" \
       + txt_info_warning_de + "\n" +
       "[anchor=dot102][b]Setzen Sie keine Tiere in den Weiher um[/b] – sie werden rasch von selbst zuwandern.\n" \
       "[anchor=dot103][b]Setzen Sie keine Fische oder Schildkröten in den Weiher[/b], denn sie fressen die Kaulquappen und Libellenlarven.\n" \
       "[anchor=dot104][b]Bauen Sie keinen Weiher, wenn Ihr Garten von Strassen umgeben ist.[/b]\n" \
       "[anchor=dot105]Weitere Infos im Pro Natura Faltblatt [b]„Amphibien rund ums Haus[anchor=end]“[/b]",
    en="Pond")

txt_info_pool = Text(
    fr=txt_info_problems_fr +
       "[anchor=dot100][b]Les grenouilles, les hérissons ou les insectes tombent et meurent noyés[/b] dans les piscines car ils n’arrivent pas à en escalader les parois verticales, trop hautes et glissantes. \n" \
       "[anchor=dot101][b]Le chlore est très nocif pour les amphibiens[/b] car ils respirent par la peau.\n\n" \
       + txt_info_solutions_fr +
       "[anchor=dot102][b]Installer une petite rampe[/b] qui permettra aux animaux de ressortir de l’eau sans difficulté.\n" \
       "[anchor=dot103][b]Veiller à éteindre l’éclairage de la piscine durant la nuit[/b] pour éviter un plongeon mortel à bon nombre d’insectes.\n" \
       "[anchor=dot104][b]Eviter de désinfecter la piscine avec du chlore.[/b] Les traitements par électrolyse ou à base de magnésium sont des alternatives moins nocives.\n" \
       "[anchor=dot105]Plus d’infos dans la [b]Charte des jardins[/b] et dans la [b]brochure Pro Natura « Des amphibiens près de chez vous[anchor=end] »[/b]",
    de=txt_info_problems_de +
       "[anchor=dot100][b]Wenn Frösche, Igel oder Insekten in ein Schwimmbecken fallen, ertrinken sie[/b], weil sie an den senkrechten und glatten Wänden nicht mehr hochklettern können.\n" \
       "[anchor=dot101][b]Chloriertes Wasser ist für Amphibien sehr schädlich[/b], weil die Tiere auch über die Haut atmen.\n\n" \
       + txt_info_solutions_de +
       "[anchor=dot102][b]Bringen Sie eine kleine Rampe an[/b], über welche die Tiere problemlos aus dem Wasser steigen können.\n" \
       "[anchor=dot103][b]Schalten Sie die Poolbeleuchtung über Nacht aus[/b], damit die Insekten nicht haufenweise ertrinken.\n" \
       "[anchor=dot104][b]Desinfizieren Sie Ihr Schwimmbad möglichst nicht mit Chlor.[/b] Als weniger schädliche Alternativen bieten sich die Elektrolyse und die Wasseraufbereitung mit Magnesium an.\n" \
       "[anchor=dot105]Weitere Infos in der [b]Garten-Charta[/b] und im Pro Natura Faltblatt [b]„Amphibien rund ums Haus[anchor=end]“[/b]",
    en="Swimming pool")

txt_info_hedge_good = Text(
    fr="[anchor=dot100][b]Exemple d’espèces d’arbustes indigènes[/b] : fusain d’Europe, chèvrefeuille, noisetier, cornouiller sanguin\n" \
       "[anchor=dot101][b]Les haies indigènes sont des éléments essentiels des corridors biologiques.[/b]\n" \
       "[anchor=dot102][b]Beaucoup d’animaux se déplacent le long de ces haies.[/b]\n" \
       "[anchor=dot103][b]Ces haies offrent des abris et de la nourriture à beaucoup d’animaux.[/b]\n" \
       "[anchor=dot104][b]Ces haies demandent peu d’entretien.[/b]\n" \
       "[anchor=dot105][b]Ces haies amènent de la couleur[/b] dans le jardin et permettent de confectionner de [b]délicieux sirops ou confitures.[/b]\n" \
       "[anchor=dot106]Plus d’infos dans la [b]Charte des jardins[/b] ou dans la [b]brochure de Pro Natura Genève «Planter des haies indigènes[anchor=end]»[/b]",
    de="[anchor=dot100][b]Beispiele für einheimische Straucharten[/b]: Pfaffenhütchen, Heckenkirsche, Hasel, Hartriegel\n" \
       "[anchor=dot101][b]Einheimische Hecken sind wichtige Elemente von Vernetzungsachsen.[/b]\n" \
       "[anchor=dot102][b]Viele Tiere bewegen sich entlang von Hecken.[/b]\n" \
       "[anchor=dot103][b]Einheimische Hecken bieten einer grossen Zahl von Tieren Unterschlupf und Nahrung.[/b]\n" \
       "[anchor=dot104][b]Sie benötigen nicht viel Pflege.[/b]\n" \
       "[anchor=dot105][b]Sie bringen Farbe[/b] in den Garten und liefern köstliche Zutaten zur Herstellung von [b]Sirups und Konfitüren.[/b]\n" \
       "[anchor=dot106]Weitere Infos in der [b]Garten-Charta[b] oder im Pro Natura Faltblatt [b]„Invasive Neophyten im Garten[anchor=end]“[/b]",
    en="Hedge of various native species")

txt_info_hedge_bad = Text(
    fr=txt_info_problems_fr +
       "[anchor=dot100][b]Le thuya et la laurelle sont des arbustes asiatiques[/b] auxquels très peu d’animaux indigènes sont adaptés. \n" \
       "[anchor=dot101][b]Ces « murs » verts n’apportent ni nourriture, ni abri à la faune[/b], même s’ils isolent bien de la rue et des voisins.\n" \
       "[anchor=dot102][b]Une haie de thuyas est infranchissable pour les animaux.[/b]\n" \
       "[anchor=dot103][b]La laurelle est toxique pour l’homme et pour beaucoup de papillons.[/b] \n" \
       "[anchor=dot104][b]La laurelle est une plante envahissante[/b] qui a la fâcheuse tendance à s’échapper des jardins pour s’établir en forêt. \n\n" \
       + txt_info_solutions_fr +
       "[anchor=dot105][b]Remplacer votre haie de thuyas ou de laurelles par une haie indigène[/b] constituée d’espèces d’arbustes locaux. Elle offrira de la nourriture et des abris aux animaux ainsi que des [b]petits fruits ou fleurs pour fabriquer de délicieux sirops ou confitures.[/b] \n" \
       "[anchor=dot106][b]Faire quelques trous dans votre haie[/b], au niveau du sol, pour permettre à des animaux tels que les hérissons de se déplacer d’un jardin à l’autre. \n" \
       "[anchor=dot107]Plus d’infos dans la [b]Charte des jardins[/b] ou dans la [b]brochure de Pro Natura Genève «Planter des haies indigènes[anchor=end]»[/b]",
    de=txt_info_problems_de +
       "[anchor=dot100][b]Thuja und Kirschlorbeer sind asiatische Sträucher[/b], die nur für sehr wenige einheimische Tiere nützlich sind.\n" \
       "[anchor=dot101]Als grüne «Wände» schirmen sie zwar gut vor Strassen oder Nachbarn ab, [b]der Tieren bieten sie aber weder Nahrung noch Unterschlupf.[/b]\n" \
       "[anchor=dot102][b]Thujahecken stellen für Tiere unüberwindbare Hindernisse dar.[/b]\n" \
       "[anchor=dot103][b]Der Kirschlorbeer ist für Menschen und auch für viele Schmetterlinge giftig.[/b]\n" \
       "[anchor=dot104][b]Der Kirschlorbeer ist eine invasive Pflanze[/b], die häufig zum Gartenflüchtling wird und sich in den Wäldern ansiedelt.\n\n" \
       + txt_info_solutions_de +
       "[anchor=dot105][b]Ersetzen Sie Ihre Thuja- oder Kirschlorbeerhecke durch eine einheimische Hecke[/b] aus Wildsträuchern aus der Region. Eine solche Hecke bietet den Tieren Nahrung und Unterschlupf und liefert [b]Beeren oder Blüten, aus denen sich feine Sirups und Konfitüren herstellen lassen.[/b]\n" \
       "[anchor=dot106][b]Öffnen Sie am Fuss Ihrer Hecke ein paar Durchgänge[/b], damit Igel und andere Tiere mühelos von einem in den anderen Garten gelangen können.\n" \
       "[anchor=dot107]Weitere Infos in der [b]Garten-Charta[/b] oder im Pro Natura Faltblatt [b]„Invasive Neophyten im Garten[anchor=end]“[/b]",
    en="Hedge of thuja and laurel")

txt_info_fence_nospace = Text(
    fr=txt_info_problem_fr + "Une barrière ou un grillage touchant le sol [b]ne laisse pas passer les animaux terrestres[/b] tels que les hérissons ou les renards.\n\n" \
       + txt_info_solutions_fr +
       "[anchor=dot100]Faire un trou dans le bas du grillage d’au moins 15 centimètres de hauteur et de largeur.\n" \
       "[anchor=dot101]Surélever la barrière d’au moins 15 centimètres. Plus d’infos dans la [b]Charte des jardins[/b].\n" \
       "[anchor=dot102][i]Images:[/i] A favoriser - exemple de clotûres permettant le libre passage de la petite faune. Ces méthodes d'espace ou de trous au pied peuvent également être appliquées aux murs et palissades.  [i]Crédits: Ecotec/Etat de [anchor=end]Genève[/i]",
    de=txt_info_problem_de + "Zäune oder Gitter, die bis auf den Boden reichen, [b]sind Barrieren für Landtiere wie Igel oder Füchse.[/b]\n\n" \
       + txt_info_solutions_de +
       "[anchor=dot100][b]Heben Sie den Zaun an[/b], mindestens um 15 Zentimeter.\n" \
       "[anchor=dot101][b]Schneiden Sie am Boden ein Loch in das Gitter[/b], mindestens 15 Zentimeter hoch und breit. Weitere Infos in der [b]Garten-Charta[/b].\n" \
       "[anchor=dot102][i]Bildern:[/i] Vorzuziehen - Beispiele von Zäunen, welche kleinen Tieren einen freien Durchgang ermöglichen. Diese Methode -Abstand oder Löcher am unteren Ende- kann auch bei Mauern und Palisaden angewandt werden.  [i]Ecotec/Kanton [anchor=end]Genf[/i]",
    en="Garden fence close to the ground ")

# two fences have the same texts (chang it if not logical)
txt_info_fence_space = txt_info_fence_nospace

txt_info_fence_wall = Text(
    fr=txt_info_problem_fr + "Un mur en béton est [b]infranchissable pour beaucoup d’animaux.[/b]\n" \
       + txt_info_solutions_fr +
       "[anchor=dot100][b]Faire pousser des plantes grimpantes sur votre mur.[/b] Le lierre, par exemple, servira de cachette et de garde-manger à de nombreux animaux et permettra également aux écureuils d’escalader le mur pour se déplacer dans le jardin voisin.\n" \
       "[anchor=dot101][b]Créer de petites ouvertures[/b] d’au moins 15 centimètres de largeur et de hauteur, près du sol. Les hérissons et les grenouilles, par exemple, pourront facilement passer de l’autre côté du mur.\n" \
       "[anchor=dot102]Plus d’infos dans la [b]Charte des jardins.[/b]  [i]Crédits photo: Reverdy Carrasco/[anchor=end]flickr[/i]",
    de=txt_info_problem_de + "Betonmauern sind [b]für viele Tiere unüberwindbare Hindernisse.[/b]\n" \
       + txt_info_solutions_de +
       "[anchor=dot100][b]Lassen Sie Kletterpflanzen an Ihrer Mauer hochwachsen.[/b] Efeu zum Beispiel wird von vielen Tieren als Versteck und Vorratskammer genutzt und dient Eichhörnchen als Klettergerüst, wenn ihnen die Mauer den Weg in den Nachbargarten versperrt.\n" \
       "[anchor=dot101][b]Öffnen Sie am Fuss der Mauer kleine Durchgänge[/b] von mindestens 15 Zentimeter Höhe und Breite, damit kleinere Tiere wie Igel oder Frösche auf die andere Seite der Mauer gelangen können.\n" \
       "[anchor=dot102]Weitere Infos in der [b]Garten-Charta[/b].  [i]Bild: Reverdy Carrasco/[anchor=end]flickr[/i]",
    en="Concrete wall")

txt_info_floor_grass = Text(
    fr="[anchor=dot100][b]Le gravier, les galets ou les pavés herbeux sont beaucoup moins chauffés par le soleil et restent frais[/b], même sous un soleil plombant.\n" \
       "[anchor=dot101][b]Les petits animaux terrestres ne se brûlent pas[/b] en passant sur ce genre de surface.\n" \
       "[anchor=dot102]Le gravier, les galets ou les pavés herbeux [b]demandent peu d’entretien.[/b]\n" \
       "[anchor=dot103][b]L’eau s’infiltre naturellement dans le sol[/b], évitant la formation de boue sur votre terrain.  [i]Crédits photo: Patrick Standish/[anchor=end]flickr[/i]",
    de="[anchor=dot100][b]Kies, Schotter oder Rasengittersteine heizen sich in der Sonne viel weniger stark auf.[/b] Eine Terrasse mit Rasengittersteinen bleibt frisch, auch wenn die Sonne brennt.\n" \
       "[anchor=dot101][b]Kleine Landtiere verbrennen sich nicht[/b], wenn sie die Fläche überqueren.\n" \
       "[anchor=dot102][b]Kies, Schotter oder Rasengittersteine benötigen nur wenig Unterhalt.[/b]\n" \
       "[anchor=dot103][b]Das Wasser versickert auf natürliche Weise im Untergrund[/b], ohne dass der Boden verschlammt.  [i]Bild: Patrick Standish/[anchor=end]flickr[/i]",
    en="Patio with grassy floor")

txt_info_floor_stone = Text(
    fr=txt_info_problems_fr +
       "[anchor=dot100][b]De grandes dalles de béton ou des pierres foncées chauffent très vite au soleil.[/b]\n" \
       "[anchor=dot101][b]Une terrasse chauffée par le soleil est infranchissable pour de nombreux petits animaux terrestres.[/b]\n" \
       "[anchor=dot102][b]L’eau de pluie ne peut pas s’infiltrer dans le sol[/b], le terrain à proximité de la terrasse risque donc de devenir très boueux.\n\n"
       + txt_info_solutions_fr +
       "[anchor=dot103][b]Le gravier, les galets ou les pavés herbeux sont beaucoup moins chauffés par le soleil et restent frais[/b], même sous un soleil plombant.  [i]Crédits photo: Patrick Standish/[anchor=end]flickr[/i]",
    de=txt_info_problems_de +
       "[anchor=dot100][b]Grosse Betonplatten oder dunkle Steine werden in der Sonne schnell heiss.[/b]\n" \
       "[anchor=dot101][b]Eine von der Sonne aufgeheizte Terrasse ist für viele kleine Landtiere nicht begehbar.[/b]\n" \
       "[anchor=dot102][b]Das Regenwasser kann nicht im Untergrund versickern[/b], sodass der Boden rund um die Terrasse verschlammt.\n\n"
       + txt_info_solutions_de +
       "[anchor=dot103][b]Kies, Schotter oder Rasengittersteine heizen sich in der Sonne viel weniger stark auf.[/b] Eine Terrasse mit Rasengittersteinen bleibt frisch, auch wenn die Sonne brennt.\n[i]Bild: Patrick Standish/[anchor=end]flickr[/i]",
    en="Patio with black sandstone floor")

txt_info_shelter_wood = Text(
    fr=txt_info_problem_fr + "Beaucoup de personnes se débarrassent des branches et des feuilles mortes[/b] pour avoir un jardin « propre ». Or, beaucoup d’animaux ont besoin des feuilles et du bois morts pour se nourrir, se cacher ou pondre.\n\n" \
       + txt_info_solutions_fr +
       "[anchor=dot100][b]Rassembler les feuilles et le bois morts en petits tas[/b] qui offriront un refuge bienvenu pour les hérissons ou les insectes, par exemple. \n" \
       "[anchor=dot101][b]Ne jamais brûler un tas de feuilles ou de branches[/b], vous risqueriez de brûler vifs tous les animaux qui y sont cachés.\n" \
       "[anchor=dot102]Plus d’infos dans la [b]Charte des jardins.[/b]  [i]Crédits photo: Pro Natura Champ-[anchor=end]Pittet[/i]",
    de=txt_info_problem_de + "Viele Leute räumen heruntergefallene Zweige und Blätter weg[/b], um einen «sauberen» Garten zu haben. Zahlreiche Tiere sind aber angewiesen auf Laub und Totholz als Nahrungsquelle, Versteck oder Eiablageplatz.\n\n" \
       + txt_info_solutions_de +
       "[anchor=dot100][b]Schichten Sie Laub und Totholz zu kleinen Haufen auf.[/b] So entstehen wertvolle Schlupfwinkel für Igel, Insekten und andere Tiere.\n" \
       "[anchor=dot101][b]Zünden Sie Laub- oder Asthaufen niemals an.[/b] Die vielen Tiere, die darin hausen, würden bei lebendigem Leib verbrennen.\n" \
       "[anchor=dot102]Weitere Infos in der [b]Garten-Charta.[/b]  [i]Bild: Pro Natura Champ-[anchor=end]Pittet[/i]",
    en="Pile of old wood and dead leafs")

txt_info_shelter_flower = Text(
    fr="[anchor=dot100][b]Les prairies fleuries sont des éléments importants des corridors biologiques.[/b]\n" \
       "[anchor=dot101][b]Les prairies fleuries sont utiles à beaucoup d’animaux.[/b] Les papillons, par exemple, y trouvent du nectar pour se nourrir et des plantes où pondre leurs œufs. C’est aussi un refuge pour beaucoup de petits mammifères, oiseaux, amphibiens et insectes. \n" \
       "[anchor=dot102][b]Une prairie fleurie demande beaucoup moins d’entretien que le gazon[/b], il suffit de la faucher une ou deux fois par année. Plus d’infos dans les brochures de Pro Natura « [i]Des papillons dans son jardin[/i] » et « [i]Prairies fleuries, aménagement et entretien[/i] » (en vente)\n" \
       "[anchor=dot103]" + txt_info_warning_fr + " Pour une belle prairie fleurie, [b]ne pas utiliser d’engrais ou de désherbant.[/b]\n" \
                                       "[anchor=dot104][b]Ne pas utiliser de pesticides[/b], ce sont des poisons pour la plupart des animaux qui se réfugient dans les prairies fleuries.  [i]Crédits photo: CSD Ingénieurs [anchor=end]SA[/i]",
    de="[anchor=dot100][b]Blumenwiesen sind wichtige Elemente von Vernetzungsachsen.[/b]\n" \
       "[anchor=dot101][b]Blumenwiesen sind für viele Tiere nützlich.[/b] So liefern sie zum Beispiel Schmetterlingen Nahrung in Form von Nektar sowie geeignete Pflanzen für die Eiablage. Sie dienen aber auch zahlreichen kleinen Säugetieren, Vögeln, Amphibien und Insekten als Unterschlupf.\n" \
       "[anchor=dot102][b]Eine Blumenwiese braucht viel weniger Pflege als ein Rasen.[/b] Es genügt, sie ein- oder zweimal pro Jahr zu mähen. Weitere Infos im Pro Natura Faltblatt [i]„Schmetterlinge im Garten“[/i] und Broschüre [i]„Blumenwiesen anlegen und pflegen“[/i] (zu kaufen an der Rezeption)\n" \
       "[anchor=dot103]" + txt_info_warning_de + " Wer eine schöne Blumenwiese wünscht, darf [b]weder Dünger noch Unkrautvertilger einsetzen.[/b] " \
                                       "[b]Verwenden Sie keine Pestizide. Sie sind für die meisten Tiere der Blumenwiesen giftig.[/b]  [i]Bild: CSD Ingénieurs [anchor=end]SA[/i]",
    en="Portion of meadow covered in flowers")

txt_info_animal_goat = Text(
    fr="[anchor=dot100][b]Les chèvres naines sont de véritables tondeuses écologiques[/b] qui vous « mâcheront » le travail dans votre jardin.\n" \
       "[anchor=dot101][b]Les moutons sont utilisés pour les plus grands espaces.[/b] La Ville de Lausanne et la Commune d’Yverdon-les-Bains les utilisent depuis plusieurs années pour la tonte de certains parcs publics.  \n" \
       "[anchor=dot102][b]Les petits animaux qui vivent dans la pelouse ne sont plus pris par surprise dans les lames acérées de la tondeuse à gazon.[/b]\n" \
       "[anchor=dot103]Il est possible de [b]louer des chèvres et des moutons[/b] juste pour quelques jours.\n" \
       "[anchor=dot104]Plus d’infos : contacter [b]La Mergerie du Bonheur[/b] www.la-mergerie.ch [i](Images)[/i]\n" \
       "[anchor=dot105]" + txt_info_warning_fr + "[b]Les chèvres doivent toujours être au moins deux[anchor=end].[/b]",
    de="[anchor=dot100][b]Zwergziegen sind regelrechte Ökomäher[/b], die Ihnen im Garten die Arbeit abnehmen können.\n" \
       "[anchor=dot101][b]Schafe eignen sich für den Unterhalt grösserer Flächen.[/b] Die Gemeinde Yverdon-les-Bains und die Stadt Lausanne setzen seit mehreren Jahren Schafe für das «Mähen» einzelner Grünanlagen ein.\n" \
       "[anchor=dot102][b]Die Kleintiere, die in der Wiese leben, werden nicht mehr von den scharfen Klingen des Rasenmähers getötet.[/b]\n" \
       "[anchor=dot103]Es ist auch möglich, [b]Ziegen und Schafe nur für ein paar Tage zu mieten.[/b]\n" \
       "[anchor=dot104]Weitere Auskünfte erteilt die [b]Mergerie du Bonheur[/b] www.la-mergerie.ch [i](Bildern)[/i]\n" \
       "[anchor=dot105]" + txt_info_warning_de + "[b]Ziegen müssen immer mindestens zu zweit sein[anchor=end].[/b]",
    en="Pygmy dwarf goats")

txt_info_animal_cat = Text(
    fr=txt_info_problems_fr +
       "[anchor=dot100][b]Les chats sont des prédateurs redoutables.[/b] Certaines études les citent même comme [b]la première cause de mortalité pour la petite faune sauvage[/b] (oiseaux, petits mammifères, amphibiens et insectes).\n" \
       "[anchor=dot101][b]Les colliers à clochettes ne sont pas efficaces[/b] pour empêcher les chats de s’attaquer à la petite faune sauvage car ils développent des stratégies pour chasser encore plus furtivement et discrètement[anchor=end].",
    de=txt_info_problems_de +
       "[anchor=dot100][b]Katzen sind geschickte Jäger.[/b] Manchen Studien zufolge sind sie sogar [b]die häufigste Todesursache für kleine Wildtiere[/b] (Vögel, kleine Säugetiere, Amphibien und Insekten).\n" \
       "[anchor=dot101][b]Ein Halsband mit Glöckchen hindert die Katze nicht[/b] daran, kleine Wildtiere zu erbeuten. Sie entwickelt dann einfach Strategien, um noch lautloser und vorsichtiger zu jagen[anchor=end].",
    en="cat")

txt_info_animal_cat_sol = Text(
    fr=txt_info_solutions_fr +
       "[anchor=dot100][b]Mettre un collier très coloré au chat[/b] pour le rendre plus visible et permettre à beaucoup d’animaux de s’enfuir.  [i]Crédits photos: Birdsbesafe® LLC[/i]\n" \
       "[anchor=dot101][b]Dans les arbres, installer des collerettes[/b] qui empêcheront le chat de grimper. \n" \
       "[anchor=dot102][b]Garder le chat à l’intérieur durant la nuit[/b] car c’est le moment où beaucoup de petits animaux sortent et se déplacent[anchor=end].",
    de=txt_info_solutions_de +
       "[anchor=dot100][b]Ziehen Sie der Katze ein buntes Halsband an.[/b] Das macht sie sichtbarer und hilft den Beutetieren, rechtzeitig zu flüchten.  [i]Bildern: Birdsbesafe® LLC[/i]\n"\
       "[anchor=dot101][b]Bringen Sie am Stamm Ihrer Bäume einen Kragen an[/b], der Katzen am Hochklettern hindert.\n"\
       "[anchor=dot102][b]Behalten Sie die Katze nachts im Haus[/b], denn dann verlassen viele Kleintiere ihre Verstecke und wandern umher[anchor=end].",
    en="cat")

txt_info_balcony_herbs = Text(
    fr="[anchor=dot100][b]Votre balcon peut être un relais important dans un corridor biologique.[/b]\n" \
       "[anchor=dot101][b]Quelques plantes aromatiques transformeront votre balcon en véritable bar à papillons[/b] qui raffolent du nectar des fleurs d’origan, de mélisse, de thym ou de romarin. \n" \
       "[anchor=dot102][b]Ces plantes parfument agréablement votre balcon et vous permettent de réaliser de délicieuses tisanes et d’aromatiser vos plats[anchor=end].[/b]",
    de="[anchor=dot100][b]Ihr Balkon kann ein wichtiger Trittstein in einer Vernetzungsachse werden.[/b]\n" \
       "[anchor=dot101][b]Mit ein paar Gewürzpflanzen machen Sie aus Ihrem Balkon eine Bar für Schmetterlinge.[/b] Diese saugen bei den Blüten von Origano, Melisse, Thymian oder Rosmarin gerne Nektar.\n" \
       "[anchor=dot102][b]Die Kräuter verströmen angenehme Düfte und liefern Ihnen die nötigen Zutaten für köstliche Tees und würzige Speisen[anchor=end].[/b]",
    en="en")

txt_info_balcony_geranium = Text(
    fr=txt_info_problems_fr +
       "[anchor=dot100][b]Les géraniums que l’on trouve dans le commerce sont généralement des espèces africaines[/b] qui ont très peu d’intérêt pour les insectes de Suisse. \n\n" \
       + txt_info_solutions_fr +
       "[anchor=dot101][b]Cultiver des plantes aromatiques[/b] telles que la mélisse ou le romarin sur votre balcon. Elles sont [b]utiles aux insectes indigènes et permettent de faire de délicieuses tisanes ou d’aromatiser vos plats[anchor=end].[/b]",
    de=txt_info_problems_de +
       "[anchor=dot100][b]Bei den Geranien, die im Handel angeboten werden, handelt es sich in der Regel um afrikanische Arten[/b], die für die Insekten der Schweiz kaum von Nutzen sind.\n\n" \
       + txt_info_solutions_de +
       "[anchor=dot101][b]Ziehen Sie auf Ihrem Balkon Gewürzkräuter[/b] wie Melisse oder Rosmarin. [b]Sie sind für die einheimischen Insekten nützlich, liefern feine Tees und aromatisieren Ihre Speisen[anchor=end].[/b]",
    en="Geraniums")
