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
    green = "[color=#599875]"  # rgb(89, 152, 117)
    magenta = "[color=#e4235f]"  # rgb(228, 35, 95)
    grey = "[color=#969696]"  # rgb(150, 150, 150)
    white = "[color=#ffffff]"  # rgb(255, 255, 255)
    end = "[/color]"
    default = black


# default text switch, always define ALL languages
def txt_notxt():
    switch = {
        lang.fr: "TODO: texte français manquant, désolé...",
        lang.de: "TODO: keine deutsche Übersetzung, Entschuldigung...",
        lang.en: "TODO: no english translation, sorry..."
    }
    return color.default + switch.get(lang.current) + color.end


# welcome text (start of game)
def txt_tutorial_welcome():
    switch = {
        lang.fr: "Bienvenue dans mon jardin.",
        lang.de: "TODO: keine deutsche Übersetzung, Entschuldigung...",
        lang.en: "TODO: no english translation, sorry..."
    }
    return color.default + switch.get(lang.current) + color.end


# game move when target is not reached
def txt_game_move_unreached():
    switch = {
        lang.fr: "Pas le bon endroit, essaie encore...",
        lang.de: "TODO: keine deutsche Übersetzung, Entschuldigung",
        lang.en: "TODO: no english translation, sorry"
    }
    return color.default + switch.get(lang.current) + color.end


# game move target reached, correct positive element
def txt_game_move_positive():
    switch = {
        lang.fr: "Bravo, bien joué!",
        lang.de: "TODO: keine deutsche Übersetzung, Entschuldigung...",
        lang.en: "TODO: no english translation, sorry..."
    }
    return color.green + switch.get(lang.current) + color.end


# game move target reached, uncorrect negative element
def txt_game_move_negative():
    switch = {
        lang.fr: "Pas le bon choix, essaie encore",
        lang.de: "TODO: keine deutsche Übersetzung, Entschuldigung...",
        lang.en: "TODO: no english translation, sorry..."
    }
    return color.magenta + switch.get(lang.current) + color.end
