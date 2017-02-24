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
        return self.color + "[b]" + switch.get(lang.current) + "[/b]"  # + color.end


# CATEGORIES and objects names

txt_cat_water = Text(
    fr="Plan d'eau",
    de="de",
    en="Body of water")

txt_cat_pond = Text(
    fr="Étang",
    de="de",
    en="Pond")

txt_cat_pool = Text(
    fr="Piscine",
    de="de",
    en="Swimming pool")

txt_cat_hedge = Text(
    fr="Haies",
    de="de",
    en="Hedges")

txt_cat_hedge_good = Text(
    fr="Haie de diverses espèces natives",
    de="de",
    en="Hedge of various native species")

txt_cat_hedge_bad = Text(
    fr="Haie de thuyas et laurelle",
    de="de",
    en="Hedge of thuja and laurel")

txt_cat_fence = Text(
    fr="Murs et barrières",
    de="de",
    en="Fences and walls")

txt_cat_fence_space = Text(
    fr="Barrière de jardin avec espace",
    de="de",
    en="Garden fence with space underneath")

txt_cat_fence_nospace = Text(
    fr="Barrière de jardin à ras du sol",
    de="de",
    en="Garden fence close to the ground ")

txt_cat_fence_wall = Text(
    fr="Mur en béton",
    de="de",
    en="Concrete wall")

txt_cat_floor = Text(
    fr="Revêtements de terrasses",
    de="de",
    en="Patio's floor")

txt_cat_floor_grass = Text(
    fr="Terrasse avec sol de pavés herbeux",
    de="de",
    en="Patio with grassy floor")

txt_cat_floor_stone = Text(
    fr="Terrasse avec sol en pierres de grès noir",
    de="de",
    en="Patio with black sandstone floor")

txt_cat_shelter = Text(
    fr="Abris et cachettes",
    de="de",
    en="Shelters and hideouts")

txt_cat_shelter_wood = Text(
    fr="Tas de vieux bois et feuilles mortes",
    de="de",
    en="Pile of old wood and dead leafs")

txt_cat_shelter_flower = Text(
    fr="Coin de prairie fleurie",
    de="de",
    en="Portion of meadow covered in flowers")

txt_cat_animal = Text(
    fr="Animaux de compagnie",
    de="de",
    en="Animals / pets")

txt_cat_animal_goat = Text(
    fr="Chèvres naines",
    de="Westafrikanische Zwergziege",
    en="Pygmy dwarf goats")

txt_cat_animal_cat = Text(
    fr="Chat",
    de="de",
    en="Cat")

txt_cat_balcony_plants = Text(
    fr="Plantes au balcon",
    de="de",
    en="Plants at the balcony")

txt_cat_balcony_herbs = Text(
    fr="Herbes aromatiques: mélisse, romarin",
    de="de",
    en="en")

txt_cat_balcony_geranium = Text(
    fr="Géraniums",
    de="de",
    en="Geraniums")

# SCENERY ELEMENTS (game setting)

txt_scenery_notxt = Text(
    fr="pas de texte",
    de="de",
    en="no text available")

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
    fr="Le but de ce jeu est de m'aider à aménager mon arrière-cour, dans une sorte de 'simcity' simplifié version jardin.",
    de="TODE",
    en="The goal of the game is to help me set up my backyard layout, like in a simple garden-version of 'simcity'.")

txt_tutorial_welcome_p2 = Text(
    fr="Dans l'aménagement idéal, mon jardin peut être un corridor biologique, c'est à dire un endroit où les divers animaux se sentent bien pour vivre, se déplacer, se reproduire, se nourrir, entre autres.",
    de="TODE",
    en="TOEN")

txt_tutorial_welcome_p3 = Text(
    fr="Pour chaque catégorie d'objet, tu auras le choix entre deux objets dans le menu de gauche. Choisis un objet et glisse-le dans le jardin sur la zone clignotante prévue pour l'accueillir.",
    de="TODE",
    en="TOEN")

txt_tutorial_welcome_p4 = Text(
    fr="Une fois l'objet correctement placé, une animation avec un animal va apparaitre, et tu vas gagner ou perdre un point.",
    de="TODE",
    en="TOEN")

txt_tutorial_welcome_p5 = Text(
    fr="Dans le cas d'un mauvais choix, tu pourras encore changer d'avis ou tenter d'améliorer ton choix.",
    de="TODE",
    en="TOEN")

txt_tutorial_welcome_p6 = Text(
    fr="Dans tous les cas, tu pourras accéder à plus d'informations et des explications, afin de comprendre pourquoi tel objet est utile ou néfaste aux mouvements des animaux.",
    de="TODE",
    en="TOEN")

txt_tutorial_play = Text(
    fr="Démarrer",
    de="Starten",
    en="Start")

# INTERACTIONS

txt_start_fr = "[b] DEMARRER LE JEU EN FRANCAIS [/b]"
txt_start_de = "[b] STARTEN DAS SPIEL AUF DEUTSCH [/b]"
txt_start_en = "[b] START THE GAME IN ENGLISH [/b]"

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
    fr="Continuer le jeu immédiatement",
    de="TODE",
    en="TOEN")

txt_interact_timeout = Text(
    color=color.magenta,
    fr="Aucune action réalisée, redémarrage du jeu dans 10 secondes.",
    de="TODE",
    en="TOEN")

txt_end_level1 = Text(
    color = color.green,
    fr="Tu as obtenu plus de 3 points, ton jardin est un véritable couloir biologique! Ton arrière-cour est un endroit où les divers animaux se sentent bien pour vivre, se déplacer, se reproduire, se nourrir, entre autres.",
    de="TODE",
    en="TOEN")

txt_end_level2 = Text(
    color = color.orange,
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
    fr= "Merci pour ton évaluation. Tu peux maintenant participer au concours en répondant correctement à quelques questions.",
    de = "TODE")
