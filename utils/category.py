# coding=utf-8
from kivy.animation import Animation
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
import random

from utils.texts import Text
import sizes
from gui import ImageWrap


class Category(object):
    #has: name, el1, el2, target
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


# draggable element scatter (touchable by children)
class ElementScatter(Scatter):
    def __init__(self, **kwargs):
        super(ElementScatter, self).__init__()
        # has: name, first
        # defaults: positive, correction

        self.do_rotation = self.do_scale = False # disable other moves than translation (drag & drop)
        self.touch_enabled = True #enable the reaction to touch
        self.positive = True # if False, should define positive_ref
        self.correction = False # if true, should define correction_no and correction_yes
        for k, v in kwargs.items():
            setattr(self, k, v)



        # _orig to replace object at their correct original placement
        self.x_orig = sizes.width_border_left
        self.y_orig = sizes.height_left_first if self.first else sizes.height_left_second
        self.pos = (self.x_orig, self.y_orig)
        self.size_hint = (None, None)
        self.size = (sizes.width_left_elements, sizes.width_left_elements)

        self.image.source = self.source
        self.image.size = (sizes.width_left_images, sizes.width_left_images)
        self.image.pos = (sizes.border_small, sizes.border_small)


def init_category_struct(frame):
    duration_start = 2

    def anim_setup_p1():
        animal = ImageWrap(
            pos=(0, sizes.height / 2),
            size = (88, 73),
            source = 'images/animations/eaux/grenouille_saute.zip',
            anim_delay=0.1)
        frame.add_widget(animal)
        return animal


    def anim_start_p1():
        return Animation(pos=sizes.event_c1, duration=duration_start)

    def anim_end_p1(animal):
        #todo: love of the grenouille
        anim = Animation(duration=1)
        return anim

    def anim_end_n1(animal):
        #todo: plouf of the grenouille
        animal.image.source = 'images/scenery/transparency.png'
        anim = Animation(duration=2)
        return anim

    p1 = ElementScatter(name=Text(fr="Etang", de="de", en="en"),
                        first=random.choice([True, False]),
                        source='images/non_animes/etang.png',
                        event_pos=sizes.event_c1,
                        anim_setup=anim_setup_p1,
                        anim_start=anim_start_p1,
                        anim_end=anim_end_p1)
    n1 = ElementScatter(name=Text(fr="Piscine", de="de", en="en"),
                        first=not p1.first,
                        positive=False,
                        positive_ref=p1,
                        source='images/animations/eaux/piscine_scintille.zip',
                        event_pos=sizes.event_c1,
                        anim_setup=anim_setup_p1,
                        anim_start=anim_start_p1,
                        anim_end=anim_end_n1,
                        anim_end_alt=anim_end_p1,
                        correction=True,
                        correction_no='images/corrections/piscine_echelle_no.png',
                        correction_yes='images/corrections/piscine_echelle_yes.png',
                        correction_img=ImageWrap(source='images/corrections/piscine_echelle_v1.png',
                                                 size=(22, 20),
                                                 pos=(sizes.width_left_margin + 265, 503))
                        )
    t1 = ImageWrap(pos=sizes.pos_c1,
                   size=sizes.size_c1,
                   source='images/animations/zones/eaux.zip')
    c1 = Category(name=Text("Plans d'eau", "de", "en"),
                  element1=p1, element2=n1, target=t1)

    def anim_setup_p2():
        animal = ImageWrap(
            pos=(sizes.width, sizes.height / 2),
            size = (75, 152),
            source = 'images/animations/haies/mesange_vole.zip',
            anim_delay=0.1)
        frame.add_widget(animal)
        return animal

    def anim_start_p2():
        return Animation(pos=sizes.event_c2, duration=duration_start)

    def anim_end_p2(animal):
        anim = Animation(x=250, y=200, duration=1)
        anim += Animation(x=-100, y=175, duration=2)
        return anim

    def anim_end_n2(animal):
        animal.flip()
        return Animation(x=100 + sizes.width, y=sizes.height / 2, duration=2)

    p2 = ElementScatter(name=Text(fr="Haies de diverses espèces", de="de", en="en"),
                        first=random.choice([True, False]),
                        source='images/non_animes/haie_diverses_especes.png',
                        event_pos=sizes.event_c2,
                        anim_setup=anim_setup_p2,
                        anim_start=anim_start_p2,
                        anim_end=anim_end_p2)
    n2 = ElementScatter(name=Text(fr="Haies de thuyas", de="de", en="en"),
                        first=not p2.first,
                        positive=False,
                        positive_ref=p2,
                        source='images/non_animes/haie_de_thuya.png',
                        event_pos=sizes.event_c2,
                        anim_setup=anim_setup_p2,
                        anim_start=anim_start_p2,
                        anim_end=anim_end_n2,
                        anim_end_alt=anim_end_p2,
                        correction=False)
    t2 = ImageWrap(pos=sizes.pos_c2,
                   size=sizes.size_c2,
                   source='images/animations/zones/haies.zip')
    c2 = Category(name=Text("Haies", "de", "en"),
                  element1=p2, element2=n2, target=t2)

    def anim_setup_p3():
        animal = ImageWrap(
            pos=(sizes.width, 0),
            size=(52,44),
            source='images/animations/abris/herisson_marche.zip',
            anim_delay=0.1)
        frame.add_widget(animal)
        return animal

    def anim_setup_n3a():
        animal = anim_setup_p3()
        animal.image.source = 'images/animations/mur/ecureuil_court.zip'
        animal.image.size = (200, 200)
        return animal

    def anim_start_p3():
        return Animation(pos=sizes.event_c3, duration=duration_start)

    def anim_start_n3a():
        return Animation(pos=sizes.event_c3alt2, duration=duration_start)

    def anim_end_p3(animal):
        anim = Animation(x=sizes.width_left_margin + 50, y=sizes.height, duration=1)
        return anim

    def anim_end_n3a_alt(animal):
        def after(t, r):
            animal.image.source = 'images/animations/mur/ecureuil_court.zip'
            anim = Animation(x=sizes.width_left_margin + 50, y=sizes.height, duration=1)
            anim.start(animal.image)
        animal.image.source = 'images/animations/mur/ecureuil_grimpe.zip'
        anim = Animation(y=animal.image.y + 80, duration=1.5)
        anim.bind(on_complete=after)
        return anim

    def anim_end_n3a(animal):
        animal.image.source = 'images/animations/mur/ecureuil_tombe.zip'
        anim = Animation(duration=2)
        return anim

    def anim_end_n3b(animal):
        animal.image.source = 'images/animations/abris/herisson_mal.zip'
        anim = Animation(duration=2)
        return anim

    p3 = ElementScatter(name=Text(fr="Barrière espacée", de="de", en="en"),
                        first=random.choice([True, False]),
                        source='images/non_animes/barrieres_espacee.png',
                        event_pos=sizes.event_c3,
                        anim_setup=anim_setup_p3,
                        anim_start=anim_start_p3,
                        anim_end=anim_end_p3)
    n3a = ElementScatter(name=Text(fr="Barriere en béton", de="de", en="en"),
                         first=random.choice([True, False]),
                         positive=False,
                         positive_ref=p3,
                         source='images/non_animes/barriere_beton.png',
                         event_pos=sizes.event_c3,
                         anim_setup=anim_setup_n3a,
                         anim_start=anim_start_n3a,
                         anim_end=anim_end_n3a,
                         anim_end_alt=anim_end_n3a_alt,
                         correction=True,
                         correction_no='images/corrections/barriere_lierre_no.png',
                         correction_yes='images/corrections/barriere_lierre_yes.png',
                         correction_img=ImageWrap(source='images/corrections/barriere_lierre.png',
                                                  size=(126,117),
                                                  pos=(sizes.event_c3alt)))
    n3b = ElementScatter(name=Text(fr="Barriere en ras de sol", de="de", en="en"),
                         first=not n3a.first,
                         positive=False,
                         positive_ref=p3,
                         source='images/non_animes/barrieres_ras_de_sol.png',
                         event_pos=sizes.event_c3,
                         anim_setup=anim_setup_p3,
                         anim_start=anim_start_p3,
                         anim_end=anim_end_n3b,
                         anim_end_alt=anim_end_p3,
                         correction=True,
                         correction_no='images/corrections/barriere_trou_no.png',
                         correction_yes='images/corrections/barriere_trou_yes.png',
                         correction_img=ImageWrap(source='images/corrections/barriere_trou.png',
                                                  size=(19, 28),
                                                  pos=(sizes.event_c3)))
    t3 = ImageWrap(pos=sizes.pos_c3,
                   size=sizes.size_c3,
                   source='images/animations/zones/mur.zip')
    c3 = Category(name=Text("Murs", "de", "en"),
                  element1=n3a, element2=n3b, target=t3)


    p4 = ElementScatter(name=Text(fr="Terrasse Pavé Drainant", de="de", en="en"),
                        first=random.choice([True, False]),
                        source='images/non_animes/terrasse_pave_drainant.png',
                        event_pos=sizes.event_c1,
                        anim_setup=anim_setup_p1,
                        anim_start=anim_start_p1,
                        anim_end=anim_end_p1)
    n4 = ElementScatter(name=Text(fr="Terrasse Grès Noir", de="de", en="en"),
                        first=not p4.first,
                        positive=False,
                        positive_ref=p4,
                        source='images/non_animes/terrasse_gres_noir.png',
                        event_pos=sizes.event_c4,
                        anim_setup=anim_setup_p1,
                        anim_start=anim_start_p1,
                        anim_end=anim_end_n1,
                        anim_end_alt=anim_end_p1,
                        correction=False)
    t4 = ImageWrap(pos=sizes.pos_c4,
                   size=sizes.size_c4,
                   source='images/animations/zones/terrasse.zip')
    c4 = Category(name=Text("Animaux", "de", "en"),
                  element1=p4, element2=n4, target=t4)

    p5 = ElementScatter(name=Text(fr="Tas de bois", de="de", en="en"),
                        first=random.choice([True, False]),
                        source='images/non_animes/tas_de_bois.png',
                        event_pos=sizes.event_c1,
                        anim_setup=anim_setup_p1,
                        anim_start=anim_start_p1,
                        anim_end=anim_end_p1)
    n5 = ElementScatter(name=Text(fr="Prairie fleurie", de="de", en="en"),
                        first=not p5.first,
                        source='images/non_animes/prairie_fleurie.png',
                        event_pos=sizes.event_c5,
                        anim_setup=anim_setup_p1,
                        anim_start=anim_start_p1,
                        anim_end=anim_end_n1)
    t5 = ImageWrap(pos=sizes.pos_c5,
                   size=sizes.size_c5,
                   source='images/animations/zones/abris.zip')
    c5 = Category(name=Text("Abris", "de", "en"),
                  element1=p5, element2=n5, target=t5)

    p6 = ElementScatter(name=Text(fr="Chèvres", de="de", en="en"),
                        first=random.choice([True, False]),
                        source='images/animations/animaux/chevre.zip',
                        event_pos=sizes.event_c6,
                        anim_setup=anim_setup_p1,
                        anim_start=anim_start_p1,
                        anim_end=anim_end_p1)
    n6 = ElementScatter(name=Text(fr="Chat", de="de", en="en"),
                        first=not p6.first,
                        positive=False,
                        positive_ref=p6,
                        source='images/animations/animaux/chat_marche.zip',
                        event_pos=sizes.event_c2,
                        anim_setup=anim_setup_p1,
                        anim_start=anim_start_p1,
                        anim_end=anim_end_n1,
                        anim_end_alt=anim_end_p1,
                        correction=True,
                        correction_no='images/corrections/arbre_cone_no.png',
                        correction_yes='images/corrections/arbre_cone_yes.png',
                        correction_img=ImageWrap(source='images/corrections/arbre_cone.png',
                                                 size=(48, 29),
                                                 pos=(sizes.width_left_margin + 454 - 10, 225)))
    t6 = ImageWrap(pos=sizes.pos_c6,
                   size=sizes.size_c6,
                   source='images/animations/zones/animaux.zip')
    c6 = Category(name=Text("Animaux", "de", "en"),
                  element1=p6, element2=n6, target=t6)


    p7 = ElementScatter(name=Text(fr="Herbes aromatiques", de="de", en="en"),
                        first=random.choice([True, False]),
                        source='images/non_animes/bac_herbes_aromatiques.png',
                        event_pos=sizes.event_c7,
                        anim_setup=anim_setup_p1,
                        anim_start=anim_start_p1,
                        anim_end=anim_end_p1)
    n7 = ElementScatter(name=Text(fr="Géraniums", de="de", en="en"),
                        first=not p7.first,
                        positive=False,
                        positive_ref=p7,
                        source='images/non_animes/bac_geraniums.png',
                        event_pos=sizes.event_c2,
                        anim_setup=anim_setup_p1,
                        anim_start=anim_start_p1,
                        anim_end=anim_end_n1,
                        anim_end_alt=anim_end_p1,
                        correction=False)
    t7 = ImageWrap(pos=sizes.pos_c7,
                   size=sizes.size_c7,
                   source='images/animations/zones/fleurs.zip')
    c7 = Category(name=Text("Plantes au balcon", "de", "en"),
                  element1=p7, element2=n7, target=t7)




    categories = {c3} #, c2, c3, c4, c5, c6, c7}
    categories = random.sample(categories, categories.__len__())
    return categories